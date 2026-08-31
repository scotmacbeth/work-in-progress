import Containers.Comonoid

/-!
# The free monad on a container as a `◁`-monoid

For a container `C = (S ◁ P)` this file constructs the **free monad** on `C` as a
**monoid in the monoidal category `(Cont, ◁, I)`** — the mirror of
`Containers.Comonoid`, where a directed container is exhibited as a `◁`-*co*monoid.

The carrier is the container of well-founded `P`-trees:

* **shapes** `PTree C` — closed `P`-trees `t ::= lf | nd s κ` (`s : S`, `κ : P s → PTree`);
* **positions** `leaves t` — the *leaves* of `t` (`leaves lf = Unit`,
  `leaves (nd s κ) = Σ p : P s, leaves (κ p)`), NOT all vertices. Directions =
  leaves is the free/cofree distinction (the cofree comonad carrier has directions =
  all vertices, Niu–Spivak Prop. 8.18).

The unit is `η = lf` and the multiplication is **grafting** `μ = graft` (substitute a
labelling of the leaves of `t` by trees), whose backward position map `split` cuts a
leaf-path at its unique `t`-leaf boundary.

## Provenance

The *construction* (positions = trees, directions = leaves, multiplication = grafting)
is **Gambino–Kock, "Polynomial functors and polynomial monads", arXiv:0906.4931,
Theorem 4.5 (2009)**, who state the monad laws are "lengthy but routine" and omit them.
This file discharges **all three** monoid laws as machine-checked equations of container
morphisms: the two **unit** laws, and **associativity** — its forward (shape) half is
`graft_assoc` (Lemma C) and its backward (position) half is `split_assoc` (Lemma D). The
whole `Container.freeMonoid` is axiom-clean (`Quot.sound` only). The single-variable case
is Gambino–Hyland (TYPES 2003); the W-type / container technology is Abbott–Altenkirch–Ghani
(ICALP 2004).
The informal companion (all three laws in coordinates) is
`projects/proofs/2026-07-16-free-monad-grafting-laws.md`.

This is the monoid mirror of `Comonoid.lean` / `ComonoidConverse.lean` (M3/M3b).

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

open Container

/-! ## The carrier: `P`-trees and their leaves -/

/-- A **closed `P`-tree** for a container `C = (S ◁ P)`: the initial algebra of
`Y ↦ 1 + Σ s : S, (P s → Y)`. `lf` is a bare leaf; `nd s κ` is an internal node of
shape `s` with one child `κ p` per position `p : P s`. This is the carrier of the
free-monad functor's shapes, `S* = Tr(1)` (Gambino–Kock 4.5). -/
inductive PTree (C : Container) where
  | lf : PTree C
  | nd : (s : C.Shape) → (C.Pos s → PTree C) → PTree C

/-- The **leaves** of a `P`-tree — the positions of the free container. A leaf of `lf`
is the tree itself (`Unit`); a leaf of `nd s κ` chooses a position `p : P s` and then a
leaf of the child `κ p`. This is `P* t = leaves t`; directions are leaves, not vertices. -/
def leaves {C : Container} : PTree C → Type
  | .lf => Unit
  | .nd s κ => (p : C.Pos s) × leaves (κ p)

/-- The **free container** `m = (S* ◁ P*)`: shapes are closed `P`-trees, positions are
their leaves. Its extension is the free-monad functor `F*` on `⟦C⟧`. -/
def Container.free (C : Container) : Container where
  Shape := PTree C
  Pos := leaves

/-! ## Grafting and its section -/

/-- **Grafting** `graft t u = t[u]`: substitute the tree `u ℓ` for each leaf `ℓ` of `t`.
Structural recursion on `t`. On `lf` it returns the single substituted tree; on `nd s κ`
it grafts into each child, restricting the leaf-labelling `u` along the chosen position. -/
def graft {C : Container} : (t : PTree C) → (leaves t → PTree C) → PTree C
  | .lf, u => u ()
  | .nd s κ, u => .nd s (fun p => graft (κ p) (fun r => u ⟨p, r⟩))

/-- **The section** `split t u` of the graft–leaf bijection (Lemma A): the backward
position map of `μ`. It sends a leaf of `graft t u` to the pair `(ℓ, w)` of the `t`-leaf
`ℓ` it passes through and the leaf `w` of `u ℓ` beyond it — cutting at the unique
`t`-leaf boundary. Structural recursion on `t`. -/
def split {C : Container} : (t : PTree C) → (u : leaves t → PTree C) →
    leaves (graft t u) → (ℓ : leaves t) × leaves (u ℓ)
  | .lf, _, w => ⟨(), w⟩
  | .nd _ κ, u, z =>
      let rec' := split (κ z.1) (fun r => u ⟨z.1, r⟩) z.2
      ⟨⟨z.1, rec'.1⟩, rec'.2⟩

/-! ## The monoid structure maps

`η : I ⇒ m` picks the bare leaf; `μ : m ◁ m ⇒ m` is grafting with `split` running
backwards on positions. -/

/-- The **unit** `η : I ⇒ m`: the single shape `()` maps to the leaf tree `lf`, and the
unique leaf of `lf` maps back to the unique `I`-position. -/
def Container.freeUnit (C : Container) : ContainerMorphism Container.I C.free where
  onShapes := fun _ => .lf
  onPos := fun _ _ => ()

/-- The **multiplication** `μ : m ◁ m ⇒ m`. A shape of `m ◁ m` is `(t, u)` with
`t : PTree` and `u : leaves t → PTree`; forward it grafts, `μ₁ (t, u) = graft t u`, and
backward it is `split t u`. -/
def Container.freeMult (C : Container) : ContainerMorphism (C.free ◁ C.free) C.free where
  onShapes := fun tu => graft tu.1 tu.2
  onPos := fun tu => split tu.1 tu.2

/-! ## The right-unit tree identity (Lemma B) and its section -/

/-- **Lemma B** (right-unit tree identity, companion note §4.2): grafting the all-leaf
labelling is the identity, `graft t (fun _ => lf) = t`. Structural induction on `t`. This
is the forward (shape) component of the monoid right-unit law. -/
theorem graft_unit_right {C : Container} :
    ∀ t : PTree C, graft t (fun _ => PTree.lf) = t
  | .lf => rfl
  | .nd s κ => by
      show PTree.nd s (fun p => graft (κ p) (fun _ => PTree.lf)) = PTree.nd s κ
      exact congrArg (PTree.nd s) (funext fun p => graft_unit_right (κ p))

/-- Transport of a `nd`-leaf along a change of the child family, computed
componentwise: transporting `z : leaves (nd s f)` along `congrArg (nd s) e` leaves the
chosen position `z.1` fixed and transports the inner leaf `z.2` along `congrFun e z.1`.
The `leaves`-analogue of `Container.seq_pos_transport`. -/
theorem leaves_nd_transport {C : Container} {s : C.Shape} {f g : C.Pos s → PTree C}
    (e : f = g) (z : leaves (PTree.nd s f)) :
    (congrArg (PTree.nd s) e ▸ z : leaves (PTree.nd s g))
      = ⟨z.1, (congrFun e z.1) ▸ z.2⟩ := by
  cases e
  rfl

/-- The backward (position) component of the right-unit law: under the all-leaf
labelling `split` recovers the leaf itself, transported along Lemma B. Structural
induction on `t`; the transport at `nd` is `leaves_nd_transport`, and the residual
casts collapse by proof irrelevance. -/
theorem split_unit_right {C : Container} :
    ∀ (t : PTree C) (p : leaves (graft t (fun _ => PTree.lf))),
      (split t (fun _ => PTree.lf) p).1 = graft_unit_right t ▸ p
  | .lf, _ => rfl
  | .nd s κ, z => by
      have ih := split_unit_right (κ z.1) z.2
      -- `graft_unit_right (nd s κ)` is *defeq* to `congrArg (nd s) (funext …)`, so the
      -- transport lemma applies to the goal's RHS as stated.
      have hb : (graft_unit_right (PTree.nd s κ) ▸ z : leaves (PTree.nd s κ))
          = ⟨z.1, (congrFun (funext fun p => graft_unit_right (κ p)) z.1) ▸ z.2⟩ :=
        leaves_nd_transport (funext fun p => graft_unit_right (κ p)) z
      rw [hb]
      -- LHS reduces to `⟨z.1, (split (κ z.1) (fun _ => lf) z.2).1⟩`; apply the IH. The two
      -- inner transports are along proof-irrelevant-equal proofs, hence defeq.
      exact congrArg (Sigma.mk z.1) ih

/-! ## Associativity of grafting (Lemma C) and split coherence (Lemma D) -/

/-- **Lemma C** (associativity of grafting, companion §4.3, forward/shape half).
Grafting `t` with `u` and then the result with a leaf-labelling `k` (of the *split*
coordinates) equals grafting `t` with the leafwise composite. Here `k` is indexed by the
composite-position type `Σ ℓ : leaves t, leaves (u ℓ)`; the outer graft feeds it
`k ∘ split t u`, and on the right `k ⟨ℓ, w⟩` selects the corresponding block. Structural
induction on `t`; the `nd` step is `congrArg (nd s)` of the childwise IH, with the split
computations collapsing definitionally. -/
theorem graft_assoc {C : Container} :
    ∀ (t : PTree C) (u : leaves t → PTree C)
      (k : (ℓ : leaves t) × leaves (u ℓ) → PTree C),
      graft (graft t u) (fun q => k (split t u q))
        = graft t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩))
  | .lf, _, _ => rfl
  | .nd s κ, u, k => by
      exact congrArg (PTree.nd s) (funext (fun p =>
        graft_assoc (κ p) (fun r => u ⟨p, r⟩)
          (fun q => k ⟨⟨p, q.1⟩, q.2⟩)))

/-- The backward (position) half of associativity — **Lemma D** (split coherence, companion
§4.3). Both composite backward maps of the associativity square regroup a leaf of the
doubly-grafted tree into `⟨⟨ℓ, w⟩, x⟩`; that they agree is the associativity of leaf-path
concatenation, here reduced to definitional computation of `split` plus the transport
`leaves_nd_transport` at each `nd`. The statement is the exact `ContainerMorphism.ext_eq`
position obligation of the associativity law, transported along `graft_assoc`. -/
theorem split_assoc {C : Container} :
    ∀ (t : PTree C) (u : leaves t → PTree C)
      (k : (ℓ : leaves t) × leaves (u ℓ) → PTree C)
      (z : leaves (graft (graft t u) (fun q => k (split t u q)))),
      (⟨split t u (split (graft t u) (fun q => k (split t u q)) z).1,
        (split (graft t u) (fun q => k (split t u q)) z).2⟩ :
          (p : (ℓ : leaves t) × leaves (u ℓ)) × leaves (k p))
        = (fun z' : leaves (graft t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩))) =>
            (⟨⟨(split t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)) z').1,
                (split (u (split t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)) z').1)
                  (fun w => k ⟨(split t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)) z').1, w⟩)
                  (split t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)) z').2).1⟩,
              (split (u (split t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)) z').1)
                (fun w => k ⟨(split t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)) z').1, w⟩)
                (split t (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)) z').2).2⟩ :
              (p : (ℓ : leaves t) × leaves (u ℓ)) × leaves (k p)))
            (graft_assoc t u k ▸ z)
  | .lf, u, k, z => rfl
  | .nd s κ, u, k, z => by
      have hb := leaves_nd_transport
        (funext (fun p => graft_assoc (κ p) (fun r => u ⟨p, r⟩)
          (fun q => k ⟨⟨p, q.1⟩, q.2⟩))) z
      generalize hgen : (graft_assoc (PTree.nd s κ) u k ▸ z :
          leaves (graft (PTree.nd s κ) (fun ℓ => graft (u ℓ) (fun w => k ⟨ℓ, w⟩)))) = w
      rw [show w = _ from hgen.symm.trans hb]
      exact congrArg
        (fun t3 : (p : (ℓ : leaves (κ z.1)) × leaves (u ⟨z.1, ℓ⟩)) × leaves (k ⟨⟨z.1, p.1⟩, p.2⟩) =>
          (⟨⟨⟨z.1, t3.1.1⟩, t3.1.2⟩, t3.2⟩ :
            (p : (ℓ : leaves (PTree.nd s κ)) × leaves (u ℓ)) × leaves (k p)))
        (split_assoc (κ z.1) (fun r => u ⟨z.1, r⟩) (fun q => k ⟨⟨z.1, q.1⟩, q.2⟩) z.2)

/-! ## The free monad is a `◁`-monoid -/

/-- A **monoid in the monoidal category `(Cont, ◁, I)`** — the mirror of
`Container.Comonoid`. Its extension is a monad on `⟦C⟧`. -/
structure Container.Monoid (C : Container) where
  /-- The unit `η : I ⟶ C`. -/
  unit : ContainerMorphism Container.I C
  /-- The multiplication `μ : C ◁ C ⟶ C`. -/
  mult : ContainerMorphism (C ◁ C) C
  /-- Left unit law `(η ◁ C) ; μ = λ`. -/
  left_unit :
    (Container.seq₂ unit (ContainerMorphism.id C)).comp mult
      = (Container.leftUnitor C).hom
  /-- Right unit law `(C ◁ η) ; μ = ρ`. -/
  right_unit :
    (Container.seq₂ (ContainerMorphism.id C) unit).comp mult
      = (Container.rightUnitor C).hom
  /-- Associativity `(μ ◁ C) ; μ = α ; (C ◁ μ) ; μ`. -/
  assoc :
    (Container.seq₂ mult (ContainerMorphism.id C)).comp mult
      = ((Container.associator C C C).hom.comp
          (Container.seq₂ (ContainerMorphism.id C) mult)).comp mult

/-- **The free monad on `C` as a `◁`-monoid** (Gambino–Kock 4.5 in coordinates).
All three monoid laws are machine-checked: unit is `freeUnit`, multiplication is `freeMult`,
the unit laws use `graft_unit_right`/`split_unit_right`, and associativity uses `graft_assoc`
(Lemma C, shapes) and `split_assoc` (Lemma D, positions). Axiom-clean (`Quot.sound` only). -/
def Container.freeMonoid (C : Container) : Container.Monoid C.free where
  unit := C.freeUnit
  mult := C.freeMult
  left_unit := ContainerMorphism.ext' rfl (fun _ _ => rfl)
  right_unit := by
    refine ContainerMorphism.ext_eq (fun s => graft_unit_right s.1) ?_
    intro s p
    exact congrArg (fun z : leaves s.1 => (⟨z, ()⟩ : (q : leaves s.1) × Unit))
      (split_unit_right s.1 p)
  -- FM-assoc: forward (shape) half is `graft_assoc` (Lemma C); backward (position) half is
  -- `split_assoc` (Lemma D), the transported `ext_eq` position obligation.
  assoc := by
    refine ContainerMorphism.ext_eq (fun tf => graft_assoc tf.1.1 tf.1.2 tf.2) ?_
    intro tf p
    exact split_assoc tf.1.1 tf.1.2 tf.2 p

end Containers
