import Containers.Dirichlet

/-!
# Bare `⊗`-comonoids in `Cont` are families of monoids (forward direction)

`Containers.Dirichlet` equips `Cont` with the **Dirichlet tensor** `(Cont, ⊗, y)`
(`⊗ = Day(Set, ×, 1)`, Niu–Spivak *Polynomial Functors* arXiv:2312.00990 Prop. 3.79). This
file cashes out the **comonoid** structure for that tensor. A `⊗`-comonoid is a container `c`
with a counit `ε : c ⟶ y` and comultiplication `δ : c ⟶ c ⊗ c` obeying the two counit laws
and coassociativity, *stated internally to `Cont`* (no reference to `Ext`, functors, or
`[Set, Set]`).

The theorem (MacBeth, PROVE note `2026-07-17-bare-dirichlet-comonoid.md`, answering the
`Poly/⊗`-comonoid slice of **Niu–Spivak Ch. 9, Question 5**, open in the book):

> A bare `⊗`-comonoid on `c` is exactly a **family of monoids** — a monoid structure
> `(c[s], mul_s, one_s)` on every direction set `c[s]`.

This file formalises the **forward** direction:

  `Container.DirichletComonoid c  ⟶  Container.FamilyOfMonoids c`.

The mechanism, in container coordinates:

* the counit `ε` picks, on each shape `s`, a distinguished element `one s := ε♯_s(∗) ∈ c[s]`
  (the monoid **unit**); this is transport-free (`y[∗] = Unit`);
* the counit laws force `δ` to be **diagonal on shapes** (`δ.onShapes s = (s, s)`), proved as
  `DirichletComonoid.hdiag`; with shapes diagonal, `δ♯_s : c[s] × c[s] → c[s]` is a binary
  operation `mul s` (the monoid **multiplication**);
* the two counit laws give the left/right **unit laws** for `one s`;
* coassociativity gives **associativity** of `mul s`.

There is no cross-shape condition (a `Cont` morphism is an *independent* family of backward
maps) and no cocommutativity is forced. So each `(c[s], mul s, one s)` is an *arbitrary*
monoid. Cf. the `◁`-comonoid story (`Containers.Comonoid`: directed containers ≅ categories);
the two layers sit over the same carrier but see different algebra.

The **converse** (assemble a comonoid from a family of monoids) and the category-level
statement `Comon(Cont, ⊗, y) ≅ Fam(Monᵒᵖ)` are natural follow-ups, not done here.

STATUS (2026-07-18). The forward map `toFamilyOfMonoids` is **complete and sorry-free**: the
shape-diagonal forcing (`hdiag`, `fst_diag`, `snd_diag`), the multiplication normal form
(`mul_apply`), both **unit laws** (`one_mul_law`, `mul_one_law`), and **associativity**
(`mul_assoc_law`) are all machine-checked. Associativity is the special case of the general
lemma `Container.dirichlet_mul_assoc` (any diagonal-on-shapes `δ : C ⟶ C ⊗ C` with
coassociativity induces an associative fibre multiplication), obtained by making `δ` a free
variable and `subst`ing the diagonal shape law so that all three comultiplication indices
become literally `(s, s)`. Registry `bare-dirichlet-comonoid` child `lean-forward` is now
`lean-verified`.

Everything is `Type`-level, Lean 4 core, no Mathlib. Every declaration closes with only
`Quot.sound`/definitional proof irrelevance for `Eq`; no `sorry`, no classical axioms.
-/

namespace Containers

open Container

/-! ## Transport toolkit

The counit laws only force `δ` diagonal on shapes *propositionally*, so the position maps of
the comonoid live over fibres that agree with the diagonal fibres only up to transport. Two
small `cases`-proved lemmas isolate every such transport.

`Container.dirPosTransport` computes the transport of a `⊗`-position pair along a shape
equality *componentwise* (the analogue of `Container.seq_pos_transport` for `⊗`). `onPosOfEq`
turns a morphism equation into a position equation, exposing the induced shape transport. Both
close by `cases` on the equality, and thereafter proof irrelevance for `Eq` collapses the
residual transports (any two proofs of the same `α = β` are definitionally equal). -/

/-- Transport of a `⊗`-position pair `⟨x, y⟩` along a shape equality `h : a = b` distributes
over the two coordinates. The `⊗`-fibre over `(a₁, a₂)` is `C.Pos a₁ × C.Pos a₂`, so a shape
equality moves each coordinate along its own projection. -/
theorem Container.dirPosTransport {C E : Container} {a b : C.Shape × E.Shape} (h : a = b)
    (x : C.Pos a.1) (y : E.Pos a.2) :
    (h ▸ (⟨x, y⟩ : (C ⊗ E).Pos a) : (C ⊗ E).Pos b)
      = ⟨congrArg Prod.fst h ▸ x, congrArg Prod.snd h ▸ y⟩ := by
  cases h; rfl

/-- Second projection of a transported `⊗`-position pair. -/
theorem Container.dirPosTransport_snd {C E : Container} {a b : C.Shape × E.Shape} (h : a = b)
    (x : C.Pos a.1) (y : E.Pos a.2) :
    (h ▸ (⟨x, y⟩ : (C ⊗ E).Pos a) : (C ⊗ E).Pos b).2 = congrArg Prod.snd h ▸ y := by
  cases h; rfl

/-- First projection of a transported `⊗`-position pair. -/
theorem Container.dirPosTransport_fst {C E : Container} {a b : C.Shape × E.Shape} (h : a = b)
    (x : C.Pos a.1) (y : E.Pos a.2) :
    (h ▸ (⟨x, y⟩ : (C ⊗ E).Pos a) : (C ⊗ E).Pos b).1 = congrArg Prod.fst h ▸ x := by
  cases h; rfl

/-- Reading a morphism equation `e : φ = ψ` off at the position level: at each shape `s`, `φ`
and `ψ` act by the same map once the `B`-position is transported along the (forced) shape
equality `φ.onShapes s = ψ.onShapes s`. Proved by `cases e`. -/
theorem onPosOfEq {A B : Container} {φ ψ : ContainerMorphism A B} (e : φ = ψ) (s : A.Shape)
    (p : B.Pos (φ.onShapes s)) :
    φ.onPos s p = ψ.onPos s (congrArg (fun m => m.onShapes s) e ▸ p) := by
  cases e; rfl

/-- Value of a dependent function at a propositionally-equal index is a transport of its value
at the original index. Lets us pull `counit`/`comult` position maps between the fibre index
`(δ.onShapes s).1/2` and the diagonal index `s`. Proved by `cases h` — the indices are genuine
variables here, so no `s`-occurs-check obstruction. -/
theorem depFunTransport {α : Type} {β : α → Type} (f : (a : α) → β a) {a b : α} (h : a = b) :
    f b = h ▸ f a := by cases h; rfl

/-- A **comonoid in the monoidal category `(Cont, ⊗, y)`** (the Dirichlet tensor). Mirrors
`Container.Comonoid` for `◁`, with `⊗`/`y` and their unitors/associator in place of `◁`/`I`. -/
structure Container.DirichletComonoid (C : Container) where
  /-- The counit `ε : C ⟶ y`. -/
  counit : ContainerMorphism C Container.y
  /-- The comultiplication `δ : C ⟶ C ⊗ C`. -/
  comult : ContainerMorphism C (C ⊗ C)
  /-- Left counit law `δ ; (ε ⊗ C) = λ⁻¹`. -/
  left_counit :
    comult.comp (Container.dir₂ counit (ContainerMorphism.id C))
      = (Container.dirLeftUnitor C).inv
  /-- Right counit law `δ ; (C ⊗ ε) = ρ⁻¹`. -/
  right_counit :
    comult.comp (Container.dir₂ (ContainerMorphism.id C) counit)
      = (Container.dirRightUnitor C).inv
  /-- Coassociativity `δ ; (δ ⊗ C) ; α = δ ; (C ⊗ δ)`. -/
  coassoc :
    (comult.comp (Container.dir₂ comult (ContainerMorphism.id C))).comp
        (Container.dirAssociator C C C).hom
      = comult.comp (Container.dir₂ (ContainerMorphism.id C) comult)

/-- An **`S`-indexed family of monoids** on a container `C`: a monoid structure on every
direction set `C.Pos s`. This is the intended classification target for bare `⊗`-comonoids. -/
structure Container.FamilyOfMonoids (C : Container) where
  /-- Fibrewise multiplication `mul s : C[s] × C[s] → C[s]`. -/
  mul : (s : C.Shape) → C.Pos s → C.Pos s → C.Pos s
  /-- Fibrewise unit `one s ∈ C[s]`. -/
  one : (s : C.Shape) → C.Pos s
  /-- Associativity of each `mul s`. -/
  mul_assoc : ∀ (s : C.Shape) (x y z : C.Pos s),
    mul s (mul s x y) z = mul s x (mul s y z)
  /-- Left unit law for each `mul s`. -/
  one_mul : ∀ (s : C.Shape) (x : C.Pos s), mul s (one s) x = x
  /-- Right unit law for each `mul s`. -/
  mul_one : ∀ (s : C.Shape) (x : C.Pos s), mul s x (one s) = x

/-! ## Associativity from coassociativity, at the level of a bare morphism

The one substantive law that resisted the fibrewise transport calculus above is
**associativity**, because the comultiplication is read at *three* shape indices
(`s`, and the two shifted indices `(δ.onShapes s).1`, `(δ.onShapes s).2`) that
agree with `s` only propositionally. Rather than fight three nested transports,
we prove the whole thing at the level of a bare morphism `δ : C ⟶ C ⊗ C` that is
diagonal on shapes: making `δ` a *free variable* lets us `cases` on it and
`subst` the (now function-level) diagonal equation `δ.onShapes = fun a => (a, a)`.
Once substituted, every shape index is *literally* `(s, s)` — not merely up to
transport — so `onPosOfEq` on coassociativity reads off exactly the associativity
equation, with all transports collapsing by definitional proof irrelevance for
`Eq`. This is the general fact; the comonoid instance is the special case
`δ = D.comult`, `hd = D.hdiag`, `hco = D.coassoc`. -/

/-- The fibrewise multiplication induced by *any* morphism `δ : C ⟶ C ⊗ C` that is
diagonal on shapes (`hd : ∀ a, δ.onShapes a = (a, a)`). This is definitionally
`Container.DirichletComonoid.mul` when `δ = D.comult` and `hd = D.hdiag`. -/
def Container.dirMulOf {C : Container} (δ : ContainerMorphism C (C ⊗ C))
    (hd : ∀ a, δ.onShapes a = (a, a)) (s : C.Shape) (x y : C.Pos s) : C.Pos s :=
  δ.onPos s ((hd s).symm ▸ (⟨x, y⟩ : (C ⊗ C).Pos (s, s)))

/-- **Coassociativity of a diagonal-on-shapes `δ` makes its induced fibre
multiplication associative.** The proof: `cases` on `δ` exposes its shape and
position maps as free variables; `funext hd` turns the pointwise diagonal law
into the function equation `δ.onShapes = fun a => (a, a)`, which `subst` then
eliminates. With shapes literally diagonal, `onPosOfEq` applied to
coassociativity at the position `⟨x, ⟨y, z⟩⟩` *is* the associativity equation —
the associator `α.hom` re-brackets `⟨x, ⟨y, z⟩⟩ ↦ ⟨⟨x, y⟩, z⟩` definitionally,
and every shape transport is `rfl` by proof irrelevance for `Eq`. -/
theorem Container.dirichlet_mul_assoc {C : Container} (δ : ContainerMorphism C (C ⊗ C))
    (hd : ∀ a, δ.onShapes a = (a, a))
    (hco : (δ.comp (Container.dir₂ δ (ContainerMorphism.id C))).comp
              (Container.dirAssociator C C C).hom
            = δ.comp (Container.dir₂ (ContainerMorphism.id C) δ))
    (s : C.Shape) (x y z : C.Pos s) :
    Container.dirMulOf δ hd s (Container.dirMulOf δ hd s x y) z
      = Container.dirMulOf δ hd s x (Container.dirMulOf δ hd s y z) := by
  obtain ⟨fS, fP⟩ := δ
  have hfS : fS = fun a => (a, a) := funext hd
  subst hfS
  exact onPosOfEq hco s ⟨x, ⟨y, z⟩⟩

namespace Container.DirichletComonoid

variable {C : Container} (D : C.DirichletComonoid)

/-- The right counit law forces the **first** shape projection of `δ` to be the identity:
`(δ.onShapes s).1 = s`. Read off the shape components of `right_counit` (a defeq unfolding of
`dir₂` and the right unitor). -/
theorem fst_diag (s : C.Shape) : (D.comult.onShapes s).1 = s :=
  congrArg (fun m => (m.onShapes s).1) D.right_counit

/-- The left counit law forces the **second** shape projection of `δ` to be the identity:
`(δ.onShapes s).2 = s`. -/
theorem snd_diag (s : C.Shape) : (D.comult.onShapes s).2 = s :=
  congrArg (fun m => (m.onShapes s).2) D.left_counit

/-- Both counit laws together force `δ` to be **diagonal on shapes**: `δ.onShapes s = (s, s)`.
This is "shapes carry the unique cartesian comonoid structure": `×` on `Set` is cartesian, so
its Day image on shapes admits only the diagonal. -/
theorem hdiag (s : C.Shape) : D.comult.onShapes s = (s, s) := by
  calc D.comult.onShapes s
      = ((D.comult.onShapes s).1, (D.comult.onShapes s).2) := rfl
    _ = (s, s) := by rw [D.fst_diag s, D.snd_diag s]

/-- The monoid **unit** on the fibre `C[s]`: the distinguished element `ε♯_s(∗)` picked out by
the counit. Transport-free, since `y[∗] = Unit`. -/
def one (s : C.Shape) : C.Pos s := D.counit.onPos s ()

/-- The monoid **multiplication** on the fibre `C[s]`: the backward map of `δ` at `s`, which
is a binary operation `C[s] × C[s] → C[s]` once shapes are known diagonal (`hdiag`). The pair
`⟨x, y⟩ : (C ⊗ C).Pos (s, s)` is transported back along `hdiag` into the actual fibre
`(C ⊗ C).Pos (δ.onShapes s)` that `δ.onPos s` consumes. -/
def mul (s : C.Shape) (x y : C.Pos s) : C.Pos s :=
  D.comult.onPos s ((D.hdiag s).symm ▸ (⟨x, y⟩ : (C ⊗ C).Pos (s, s)))

/-- `mul` written with the two coordinatewise shape transports made explicit — the diagonal
transport in the definition distributes over the pair (`dirPosTransport`), and the resulting
per-coordinate transports agree with `fst_diag`/`snd_diag` by proof irrelevance. -/
theorem mul_apply (s : C.Shape) (x y : C.Pos s) :
    D.mul s x y
      = D.comult.onPos s ⟨(D.fst_diag s).symm ▸ x, (D.snd_diag s).symm ▸ y⟩ :=
  congrArg (D.comult.onPos s) (Container.dirPosTransport (D.hdiag s).symm x y)

/-- Round-trip transport `h.symm ▸ (h ▸ z) = z`. -/
theorem castSymmCast {α : Type} {P : α → Type} {a b : α} (h : a = b) (z : P a) :
    (h.symm ▸ (h ▸ z : P b) : P a) = z := by cases h; rfl

/-- Round-trip transport `h ▸ (h.symm ▸ z) = z`. -/
theorem castCastSymm {α : Type} {P : α → Type} {a b : α} (h : a = b) (z : P b) :
    (h ▸ (h.symm ▸ z : P a) : P b) = z := by cases h; rfl

/-- The unit element read at the *fibre* index `(δ.onShapes s).1` is the transport of `one s`.
Moves `ε♯` between the diagonal index `s` and the shape `δ` actually produces. -/
theorem one_at_fst (s : C.Shape) :
    D.counit.onPos (D.comult.onShapes s).1 () = (D.fst_diag s).symm ▸ D.one s := by
  show D.counit.onPos (D.comult.onShapes s).1 ()
      = (D.fst_diag s).symm ▸ D.counit.onPos s ()
  rw [depFunTransport (fun a => D.counit.onPos a ()) (D.fst_diag s), castSymmCast]

/-- The unit element read at the fibre index `(δ.onShapes s).2` is the transport of `one s`. -/
theorem one_at_snd (s : C.Shape) :
    D.counit.onPos (D.comult.onShapes s).2 () = (D.snd_diag s).symm ▸ D.one s := by
  show D.counit.onPos (D.comult.onShapes s).2 ()
      = (D.snd_diag s).symm ▸ D.counit.onPos s ()
  rw [depFunTransport (fun a => D.counit.onPos a ()) (D.snd_diag s), castSymmCast]

/-- Position content of the **left** counit law: multiplying by the unit in the first slot,
then transporting back, is the identity (up to the forced shape transport). -/
theorem left_counit_apply (s : C.Shape) (q : C.Pos (D.comult.onShapes s).2) :
    D.comult.onPos s ⟨D.counit.onPos (D.comult.onShapes s).1 (), q⟩ = D.snd_diag s ▸ q := by
  have h := onPosOfEq D.left_counit s (⟨(), q⟩ : (Container.y ⊗ C).Pos _)
  refine h.trans ?_
  exact Container.dirPosTransport_snd (congrArg (fun m => m.onShapes s) D.left_counit) () q

/-- Position content of the **right** counit law: multiplying by the unit in the second slot. -/
theorem right_counit_apply (s : C.Shape) (p : C.Pos (D.comult.onShapes s).1) :
    D.comult.onPos s ⟨p, D.counit.onPos (D.comult.onShapes s).2 ()⟩ = D.fst_diag s ▸ p := by
  have h := onPosOfEq D.right_counit s (⟨p, ()⟩ : (C ⊗ Container.y).Pos _)
  refine h.trans ?_
  exact Container.dirPosTransport_fst (congrArg (fun m => m.onShapes s) D.right_counit) p ()

theorem one_mul_law (s : C.Shape) (x : C.Pos s) : D.mul s (D.one s) x = x := by
  rw [D.mul_apply s (D.one s) x, ← D.one_at_fst s, D.left_counit_apply s, castCastSymm]

theorem mul_one_law (s : C.Shape) (x : C.Pos s) : D.mul s x (D.one s) = x := by
  rw [D.mul_apply s x (D.one s), ← D.one_at_snd s, D.right_counit_apply s, castCastSymm]

/-- **Associativity of each fibre multiplication**, from coassociativity of `δ`.
The special case of `Container.dirichlet_mul_assoc` at `δ = D.comult`,
`hd = D.hdiag`, `hco = D.coassoc`: `D.mul` is *definitionally*
`Container.dirMulOf D.comult D.hdiag`, so the general lemma applies on the nose.
Paper proof: `2026-07-17-bare-dirichlet-comonoid.md` §4. -/
theorem mul_assoc_law (s : C.Shape) (x y z : C.Pos s) :
    D.mul s (D.mul s x y) z = D.mul s x (D.mul s y z) :=
  Container.dirichlet_mul_assoc D.comult D.hdiag D.coassoc s x y z

/-- **Forward direction of the classification.** Every bare `⊗`-comonoid on `C` determines a
family of monoids on its direction sets. -/
def toFamilyOfMonoids : C.FamilyOfMonoids where
  mul := D.mul
  one := D.one
  mul_assoc := D.mul_assoc_law
  one_mul := D.one_mul_law
  mul_one := D.mul_one_law

end Container.DirichletComonoid

end Containers
