import Containers.Free

/-!
# The universal property of the free monad on a container

For a container `X = (S ◁ P)`, `Free.lean` builds the **free monad** `m_X = X.free` — the
container of `P`-trees with leaves as positions — and verifies its three `◁`-monoid laws
(`Container.freeMonoid`). This file adds the **universal property** of that monoid: the
insertion of generators `α_X : X ⟶ m_X` is universal from `X` to the forgetful functor
`U : Mon(Cont) → Cont`. Concretely, for every monoid `M` and morphism `g : X ⟶ U(M)` there
is a *unique* monoid morphism `ĝ : m_X ⟶ M` with `α_X ; ĝ = g`.

The informal companion is `projects/proofs/2026-07-24-free-monad-universal-property.md`; the
construction and theorem are **prior art** — Gambino–Kock, *Polynomial functors and
polynomial monads*, arXiv:0906.4931, Theorem 4.5 (2009) — while the container-coordinate
proof (the piece the grafting-laws note left open) is the local contribution.

## Scope of this file

The **forward / shape** backbone of the universal property, transport-free and axiom-clean:

* `Container.freeInsert` — the insertion `α_X`;
* `Container.freeExtShape` — the induced shape map `ĝ₁ : S* → M.Shape`, by tree recursion;
* `Container.freeExtShape_triangle` — `ĝ₁` computes `g` on generators (uses `M`'s
  **right-unit** law), i.e. the shape half of the adjunction triangle `α ; ĝ = g`;
* `Container.freeExtend_triangle` — the adjunction triangle `α ; ĝ = g` in full (both
  components); the position half uses `M`'s right-unit backward (`mult_right_unit_pos`);
* `Container.freeExtend_unit` — `ĝ` preserves the monoid unit (the unit homomorphism law);
* `Container.mult_assoc_shape` — `M`'s associativity in forward/shape coordinates;
* `Container.freeExtShape_mult` — **MULT forward**: the shape half of the multiplication
  homomorphism law `μ ; ĝ = (ĝ ◁ ĝ) ; μ_M`, by tree induction reducing to `M`'s left-unit
  (base) and associativity (step);
* `Container.freeExtShape_unique` — `ĝ₁` is the **unique** shape map satisfying the base
  and node recursions; this is the uniqueness of the extension at the object level;
* `Container.mult_left_unit_pos` and `Container.mult_assoc_pos` — the **backward (position)
  halves** of `M`'s left-unit and associativity laws, extracted from `Mon.left_unit` /
  `Mon.assoc` via `onPos_congr` (the duals of `mult_left_unit` / `mult_assoc_shape`). These
  are the two `M`-law inputs the backward multiplication law (companion §4.3) consumes.

**Not yet formalised (the remaining Lean work):**

1. The **backward (position) half** of the multiplication homomorphism law — the
   `split`-vs-`M.mult`-position identity `freeExtPos_mult`. Its two `M`-law inputs
   (`mult_left_unit_pos`, `mult_assoc_pos`) are now in place and the **base case** (`lf`,
   reducing to `mult_left_unit_pos` + `cast_symm_cast`) is verified; the **node step**
   remains — it threads `mult_assoc_pos` through `split`'s `nd`-clause after a childwise
   forward-IH (`freeExtShape_mult`) family-transport, mirroring `Free.split_assoc` plus the
   associativity-backward reconciliation. Companion §4.3; assembly sketch in
   `projects/memory/for-collaborator/free-monad-mult-backward-lean.md`.
2. **Backward-uniqueness** — the position half of `freeExtShape_unique`, forced by the
   bijectivity of `split` (companion §6). This needs the `cat`/`split` inverse pair and
   `split`-bijectivity, which are not yet in `Free.lean`.

Everything below is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

open Container

variable {X : Container}

/-! ## The insertion of generators `α_X : X ⟶ m_X` -/

/-- **Insertion of generators** `α_X : X ⟶ m_X` (companion §2). A shape `s : X.Shape` is
sent to the single node `nd s (fun _ => lf)` whose children are all leaves; its unique
leaf `⟨p, ()⟩` names back the position `p : X.Pos s`. This is the unit of the adjunction. -/
def Container.freeInsert (X : Container) : ContainerMorphism X X.free where
  onShapes := fun s => PTree.nd s (fun _ => PTree.lf)
  onPos := fun _ pu => pu.1

/-! ## The induced shape map `ĝ₁ : S* → M.Shape` -/

/-- The **induced shape map** `ĝ₁` (companion §3, forward). Given a monoid `M` and a
morphism `g : X ⟶ M`, recurse on the tree: a leaf goes to the unit `ε = M.unit ⟨⟩`, and a
node `nd s κ` goes to `μ_M(g s, fun q ↦ ĝ₁(κ (g♯_s q)))`, where `q : M.Pos (g s)` and
`g♯_s q : X.Pos s` selects the subtree. The recursive calls are on structural subtrees. -/
def Container.freeExtShape {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) : PTree X → M.Shape
  | .lf => Mon.unit.onShapes ()
  | .nd s κ =>
      Mon.mult.onShapes ⟨g.onShapes s, fun q => freeExtShape Mon g (κ (g.onPos s q))⟩

/-- Node computation rule for `freeExtShape`, stated for use in the uniqueness proof. -/
theorem Container.freeExtShape_nd {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) (s : X.Shape) (κ : X.Pos s → PTree X) :
    Container.freeExtShape Mon g (PTree.nd s κ)
      = Mon.mult.onShapes ⟨g.onShapes s, fun q => freeExtShape Mon g (κ (g.onPos s q))⟩ :=
  rfl

/-! ## `M`'s monoid laws in forward / shape coordinates

We extract the shape components of `M`'s unit and associativity laws from the packaged
`ContainerMorphism` equations by applying `congrArg onShapes` and evaluating at a chosen
shape.  These are hypotheses (`M` is a monoid), never obligations. -/

/-- **(M-RUNIT) forward.** `μ_M(a, fun _ ↦ ε) = a`. Extracted from `M.right_unit`. -/
theorem Container.mult_right_unit {M : Container} (Mon : Container.Monoid M) (a : M.Shape) :
    Mon.mult.onShapes ⟨a, fun _ => Mon.unit.onShapes ()⟩ = a :=
  congrFun (congrArg ContainerMorphism.onShapes Mon.right_unit)
    (⟨a, fun _ => ()⟩ : (M ◁ Container.I).Shape)

/-- **(M-LUNIT) forward.** `μ_M(ε, fun _ ↦ c) = c`. Extracted from `M.left_unit`. -/
theorem Container.mult_left_unit {M : Container} (Mon : Container.Monoid M) (c : M.Shape) :
    Mon.mult.onShapes ⟨Mon.unit.onShapes (), fun _ => c⟩ = c :=
  congrFun (congrArg ContainerMorphism.onShapes Mon.left_unit)
    (⟨(), fun _ => c⟩ : (Container.I ◁ M).Shape)

/-! ## The induced position map `ĝ♯` and the packaged morphism `ĝ` -/

/-- The **induced position map** `ĝ♯_t : M.Pos(ĝ₁ t) → leaves t` (companion §3, backward,
equation (†)). At a leaf it is the unique map into `Unit`; at a node `nd s κ` a target
position `r` is split by `μ_M`'s backward map into `⟨q, ρ⟩` (`q : M.Pos(g s)` names the
container position `g♯_s q : X.Pos s`, `ρ` recurses into the corresponding subtree). -/
def Container.freeExtPos {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) :
    (t : PTree X) → M.Pos (Container.freeExtShape Mon g t) → leaves t
  | .lf => fun _ => ()
  | .nd s κ => fun r =>
      let qρ := Mon.mult.onPos
        ⟨g.onShapes s, fun q => Container.freeExtShape Mon g (κ (g.onPos s q))⟩ r
      ⟨g.onPos s qρ.1, Container.freeExtPos Mon g (κ (g.onPos s qρ.1)) qρ.2⟩

/-- The **induced monoid morphism** `ĝ : m_X ⟶ M` on the free monad, packaging the shape
map `freeExtShape` and the position map `freeExtPos`. Companion §3. -/
def Container.freeExtend {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) : ContainerMorphism X.free M where
  onShapes := Container.freeExtShape Mon g
  onPos := Container.freeExtPos Mon g

/-! ## `ĝ` preserves the monoid unit -/

/-- **`ĝ` is unit-preserving**: `freeUnit ; ĝ = M.unit`. Both sides send the shape `⟨⟩` to
`ε` (definitionally, since `ĝ₁(lf) = ε`) and their position maps land in `Unit`, so they
agree by `Unit`-eta. This is the unit half of "`ĝ` is a monoid morphism". -/
theorem Container.freeExtend_unit {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) :
    (Container.freeUnit X).comp (Container.freeExtend Mon g) = Mon.unit :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-- **Projection of a morphism equality onto positions.** From `φ = ψ`, the position maps
agree after transporting along the induced shape equality. This is the inverse of
`ContainerMorphism.ext'`; `cases h` collapses the transport to `rfl`. -/
theorem ContainerMorphism.onPos_congr {C D : Container}
    {φ ψ : ContainerMorphism C D} (h : φ = ψ) (s : C.Shape) (p : D.Pos (φ.onShapes s)) :
    φ.onPos s p
      = ψ.onPos s (congrFun (congrArg ContainerMorphism.onShapes h) s ▸ p) := by
  cases h; rfl

/-- **(M-RUNIT) backward.** The first projection of `μ_M`'s backward map at a right-unit
shape `(a, fun _ ↦ ε)` recovers the input position (transported along `mult_right_unit`).
Extracted from `M.right_unit` via `onPos_congr`; the residual second component lands in
`Unit`. Companion §4.1 (M-RUNIT), backward clause. -/
theorem Container.mult_right_unit_pos {M : Container} (Mon : Container.Monoid M)
    (a : M.Shape) (p : M.Pos (Mon.mult.onShapes ⟨a, fun _ => Mon.unit.onShapes ()⟩)) :
    (Mon.mult.onPos ⟨a, fun _ => Mon.unit.onShapes ()⟩ p).1
      = Container.mult_right_unit Mon a ▸ p :=
  congrArg Sigma.fst
    (ContainerMorphism.onPos_congr Mon.right_unit (⟨a, fun _ => ()⟩ : (M ◁ Container.I).Shape) p)

/-- **(M-LUNIT) backward.** The second projection of `μ_M`'s backward map at a left-unit
shape `(ε, fun _ ↦ c)` recovers the input position (transported along `mult_left_unit`).
Extracted from `M.left_unit` via `onPos_congr`; the residual first component lands in
`Unit`. Companion §4.1 (M-LUNIT), backward clause. -/
theorem Container.mult_left_unit_pos {M : Container} (Mon : Container.Monoid M)
    (c : M.Shape)
    (p : M.Pos (Mon.mult.onShapes ⟨Mon.unit.onShapes (), fun _ => c⟩)) :
    (Mon.mult.onPos ⟨Mon.unit.onShapes (), fun _ => c⟩ p).2
      = (Container.mult_left_unit Mon c ▸ p : M.Pos c) :=
  congrArg (fun z : (_q : Unit) × M.Pos c => z.2)
    (ContainerMorphism.onPos_congr Mon.left_unit
      (⟨(), fun _ => c⟩ : (Container.I ◁ M).Shape) p)

/-! ## The triangle `α_X ; ĝ = g` -/

/-- **Shape half of the adjunction triangle** `α_X ; ĝ = g` (companion §5, forward). On a
generator `s`, `ĝ₁(α₁ s) = ĝ₁(nd s (fun _ ↦ lf)) = μ_M(g s, fun _ ↦ ε) = g s` by `M`'s
**right-unit** law — fittingly, since `α` puts the generator at the root with leaf
children (the right-unit configuration). -/
theorem Container.freeExtShape_triangle {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) (s : X.Shape) :
    Container.freeExtShape Mon g ((Container.freeInsert X).onShapes s) = g.onShapes s :=
  Container.mult_right_unit Mon (g.onShapes s)

/-- **The adjunction triangle** `α_X ; ĝ = g`, in full (both shape and position
components); companion §5. The shape half is `freeExtShape_triangle` (`M`'s right-unit,
forward); the position half is `mult_right_unit_pos` (`M`'s right-unit, backward),
transported into `g`'s backward map. This is the universal arrow condition: `ĝ` extends
`g` along the insertion of generators. -/
theorem Container.freeExtend_triangle {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) :
    (Container.freeInsert X).comp (Container.freeExtend Mon g) = g := by
  refine ContainerMorphism.ext_eq (fun s => Container.freeExtShape_triangle Mon g s) ?_
  intro s p
  exact congrArg (g.onPos s) (Container.mult_right_unit_pos Mon (g.onShapes s) p)

/-! ## `M`'s associativity in forward / shape coordinates -/

/-- **(M-ASSOC) forward** (companion §4.1, M-ASSOC forward clause). The shape half of
`M`'s associativity law, extracted from `Mon.assoc` by `congrArg onShapes` at the shape
`⟨⟨a, b⟩, C⟩` of `(M ◁ M) ◁ M`. Both sides reduce definitionally to the coordinate
associativity of `μ_M`; this is a hypothesis (`M` is a monoid), never an obligation. -/
theorem Container.mult_assoc_shape {M : Container} (Mon : Container.Monoid M)
    (a : M.Shape) (b : M.Pos a → M.Shape)
    (C : ((q : M.Pos a) × M.Pos (b q)) → M.Shape) :
    Mon.mult.onShapes ⟨Mon.mult.onShapes ⟨a, b⟩, fun q' => C (Mon.mult.onPos ⟨a, b⟩ q')⟩
      = Mon.mult.onShapes ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun q' => C ⟨q, q'⟩⟩⟩ :=
  congrFun (congrArg ContainerMorphism.onShapes Mon.assoc)
    (⟨⟨a, b⟩, C⟩ : ((M ◁ M) ◁ M).Shape)

/-- **(M-ASSOC) backward** (companion §4.1, M-ASSOC backward clause). The position half of
`M`'s associativity, extracted from `Mon.assoc` via `onPos_congr` at `⟨⟨a, b⟩, C⟩`. Splitting
a target position `r` of the left-associated shape by `μ_M` twice (outer then along the
`(a, b)` factor) equals — after transporting `r` along `mult_assoc_shape` to the
right-associated shape and splitting the other way — the same regrouped triple
`⟨⟨q, q'⟩, x⟩` of `Σ_{q}Σ_{q'} M.Pos (C ⟨q, q'⟩)`. Mirror of `mult_assoc_shape`; the transport
term is *literally* `mult_assoc_shape` (both are the same `congrFun (congrArg onShapes …)`),
so it threads through without a coercion. A hypothesis (`M` is a monoid), never an obligation. -/
theorem Container.mult_assoc_pos {M : Container} (Mon : Container.Monoid M)
    (a : M.Shape) (b : M.Pos a → M.Shape)
    (C : ((q : M.Pos a) × M.Pos (b q)) → M.Shape)
    (r : M.Pos (Mon.mult.onShapes
      ⟨Mon.mult.onShapes ⟨a, b⟩, fun q' => C (Mon.mult.onPos ⟨a, b⟩ q')⟩)) :
    (⟨Mon.mult.onPos ⟨a, b⟩
        (Mon.mult.onPos ⟨Mon.mult.onShapes ⟨a, b⟩,
          fun q' => C (Mon.mult.onPos ⟨a, b⟩ q')⟩ r).1,
      (Mon.mult.onPos ⟨Mon.mult.onShapes ⟨a, b⟩,
          fun q' => C (Mon.mult.onPos ⟨a, b⟩ q')⟩ r).2⟩
        : (w : (q : M.Pos a) × M.Pos (b q)) × M.Pos (C w))
      = (⟨⟨(Mon.mult.onPos ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun v => C ⟨q, v⟩⟩⟩
              (Container.mult_assoc_shape Mon a b C ▸ r)).1,
            (Mon.mult.onPos
              ⟨b (Mon.mult.onPos ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun v => C ⟨q, v⟩⟩⟩
                    (Container.mult_assoc_shape Mon a b C ▸ r)).1,
                fun v => C ⟨(Mon.mult.onPos
                  ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun v => C ⟨q, v⟩⟩⟩
                    (Container.mult_assoc_shape Mon a b C ▸ r)).1, v⟩⟩
              (Mon.mult.onPos ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun v => C ⟨q, v⟩⟩⟩
                (Container.mult_assoc_shape Mon a b C ▸ r)).2).1⟩,
          (Mon.mult.onPos
            ⟨b (Mon.mult.onPos ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun v => C ⟨q, v⟩⟩⟩
                  (Container.mult_assoc_shape Mon a b C ▸ r)).1,
              fun v => C ⟨(Mon.mult.onPos
                ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun v => C ⟨q, v⟩⟩⟩
                  (Container.mult_assoc_shape Mon a b C ▸ r)).1, v⟩⟩
            (Mon.mult.onPos ⟨a, fun q => Mon.mult.onShapes ⟨b q, fun v => C ⟨q, v⟩⟩⟩
              (Container.mult_assoc_shape Mon a b C ▸ r)).2).2⟩
        : (w : (q : M.Pos a) × M.Pos (b q)) × M.Pos (C w)) :=
  ContainerMorphism.onPos_congr Mon.assoc (⟨⟨a, b⟩, C⟩ : ((M ◁ M) ◁ M).Shape) r

/-! ## The multiplication homomorphism law (forward / shape half) -/

/-- **MULT forward** (companion §4.2): the shape half of the multiplication homomorphism
law `μ ; ĝ = (ĝ ◁ ĝ) ; μ_M`. Grafting `t` with `u` then extending equals `μ_M` of the
extension of `t` with the extension of the (`ĝ♯_t`-reindexed) leaf labelling. Structural
induction on `t`: the base is `M`'s **left-unit** law (`mult_left_unit`), the node step is
`M`'s **associativity** (`mult_assoc_shape`) applied after the childwise inductive
hypothesis. This is the exact mirror of how the free monoid's own laws reduced to grafting
associativity — here the *morphism* law reduces to `M`'s laws. -/
theorem Container.freeExtShape_mult {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) :
    ∀ (t : PTree X) (u : leaves t → PTree X),
      Container.freeExtShape Mon g (graft t u)
        = Mon.mult.onShapes ⟨Container.freeExtShape Mon g t,
            fun q' => Container.freeExtShape Mon g (u (Container.freeExtPos Mon g t q'))⟩
  | .lf, u => (Container.mult_left_unit Mon (Container.freeExtShape Mon g (u ()))).symm
  | .nd s κ, u =>
      (congrArg (fun bb => Mon.mult.onShapes ⟨g.onShapes s, bb⟩)
        (funext fun q =>
          Container.freeExtShape_mult Mon g (κ (g.onPos s q))
            (fun r => u ⟨g.onPos s q, r⟩))).trans
        (Container.mult_assoc_shape Mon (g.onShapes s)
          (fun q => Container.freeExtShape Mon g (κ (g.onPos s q)))
          (fun qq => Container.freeExtShape Mon g
            (u ⟨g.onPos s qq.1,
              Container.freeExtPos Mon g (κ (g.onPos s qq.1)) qq.2⟩))).symm

/-! ## Uniqueness of the extension on shapes -/

/-- **Uniqueness on shapes** (companion §6, forward). Any shape map `f : S* → M.Shape`
that sends a leaf to `ε` and satisfies the same node recursion as `ĝ₁` *is* `ĝ₁`. A clean
structural induction on the tree — no transports, no monoid laws, just the two recursion
equations. This is the object-level uniqueness of the free-monad extension. -/
theorem Container.freeExtShape_unique {M : Container} (Mon : Container.Monoid M)
    (g : ContainerMorphism X M) (f : PTree X → M.Shape)
    (hlf : f PTree.lf = Mon.unit.onShapes ())
    (hnd : ∀ (s : X.Shape) (κ : X.Pos s → PTree X),
      f (PTree.nd s κ)
        = Mon.mult.onShapes ⟨g.onShapes s, fun q => f (κ (g.onPos s q))⟩) :
    ∀ t : PTree X, f t = Container.freeExtShape Mon g t
  | .lf => hlf
  | .nd s κ => by
      rw [hnd s κ, Container.freeExtShape_nd]
      exact congrArg (fun b => Mon.mult.onShapes ⟨g.onShapes s, b⟩)
        (funext fun q => Container.freeExtShape_unique Mon g f hlf hnd (κ (g.onPos s q)))

end Containers
