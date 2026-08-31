import Containers.DirichletComonoid

/-!
# Converse: a family of monoids assembles a bare `⊗`-comonoid

`Containers.DirichletComonoid` proves the **forward** half of the classification of bare
`⊗`-comonoids in `(Cont, ⊗, y)` (the Dirichlet tensor, `⊗ = Day(Set, ×, 1)`, Niu–Spivak
*Polynomial Functors* arXiv:2312.00990 Prop. 3.79): every `Container.DirichletComonoid C` gives a
`Container.FamilyOfMonoids C` (an arbitrary monoid `(mul s, one s)` on every direction set
`C[s]`). This file supplies the **converse**, completing the `⊗`-comonoid column to a full
isomorphism — the sibling of `Containers.DirichletMonoidConverse` for the monoid column.

Source: MacBeth PROVE note `2026-07-17-bare-dirichlet-comonoid.md` §4 ("Converse"), answering the
`Poly/⊗`-comonoid slice of **Niu–Spivak Ch. 9, Question 5** (open in the book).

The construction is the mirror of the forward extraction (§§3–4 read backwards):

* the counit `ε : C ⟶ y` sends every shape to `∗` (forced) and picks, on directions at `s`, the
  monoid unit `one s` (the backward map `y[∗] = 1 → C[s]`);
* the comultiplication `δ : C ⟶ C ⊗ C` is the **diagonal** on shapes (`s ↦ (s, s)`) and, on
  directions, the fibre multiplication `mul s : C[s] × C[s] → C[s]` (recall `(C ⊗ C).Pos (s, s)`
  is `C.Pos s × C.Pos s` definitionally).

Because we *choose* the comultiplication diagonal on shapes, the converse laws are
**transport-free**: unlike the forward direction — where `δ.onShapes` is only *propositionally*
diagonal (`DirichletComonoid.hdiag`) and every fibre read carries a shape transport — here each
law reduces on the nose. The two counit laws are `one_mul`/`mul_one`; coassociativity is
`mul_assoc` (the Dirichlet associator re-brackets `C[s] × (C[s] × C[s])` definitionally, exactly
as in the `⊗`-monoid converse). Each law is discharged by `ContainerMorphism.ext'` with shape
equality `rfl` (both legs are literally the diagonal / a `Unit`-collapse).

Both round trips then hold:

* `FamilyOfMonoids → DirichletComonoid → FamilyOfMonoids = id` by `rfl` (`mul`/`one` round-trip
  definitionally — the forward `mul` transports along `hdiag : (s,s) = (s,s)`, which is `rfl` up to
  proof irrelevance for `Eq` — and the law fields are `Prop`-valued, hence proof-irrelevant);
* `DirichletComonoid → FamilyOfMonoids → DirichletComonoid = id` via a structure-extensionality
  lemma `DirichletComonoid.ext` (the law fields are `Prop`): the counit round-trips by `Unit` η,
  and the comult by `ext'` with shape equality `funext (fun s => (D.hdiag s).symm)` — the forward
  `mul` unfolds to exactly `D.comult.onPos` post-composed with the transport `ext'` inserts, and the
  two transports agree by proof irrelevance for `Eq` and `Prod`/`Unit` η.

So

  `Container.DirichletComonoid C  ≅  Container.FamilyOfMonoids C`

as an honest isomorphism, both directions machine-checked.

STATUS (2026-07-20). Sorry-free. The converse laws use `funext` (hence `Quot.sound`) via `ext'`;
the two round trips need only `rfl`/proof irrelevance. See `#print axioms` at the end.

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

open Container

namespace Container.FamilyOfMonoids

variable {C : Container} (F : C.FamilyOfMonoids)

/-- The **counit** `ε : C ⟶ y` of the assembled `⊗`-comonoid: every shape goes to the unique shape
`∗`, and the backward map `y[∗] = 1 → C[s]` picks the monoid unit `one s`. -/
def counitMor : ContainerMorphism C Container.y where
  onShapes := fun _ => ()
  onPos := fun s _ => F.one s

/-- The **comultiplication** `δ : C ⟶ C ⊗ C`: the diagonal `s ↦ (s, s)` on shapes, and the fibre
multiplication `mul s` on directions. The codomain `(C ⊗ C).Pos (s, s)` is `C.Pos s × C.Pos s`
definitionally, so no transport is needed. -/
def comultMor : ContainerMorphism C (C ⊗ C) where
  onShapes := fun s => (s, s)
  onPos := fun s p => F.mul s p.1 p.2

/-- **Left counit law** `δ ; (ε ⊗ C) = λ⁻¹`. On shapes both legs are `s ↦ (∗, s)` (`rfl`); on
directions the first coordinate lands in `y[∗] = 1` and the second is `mul s (one s) (·) = (·)`,
which is the monoid left-unit law `one_mul`. -/
theorem left_counit_law :
    F.comultMor.comp (Container.dir₂ F.counitMor (ContainerMorphism.id C))
      = (Container.dirLeftUnitor C).inv := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact F.one_mul s p.2

/-- **Right counit law** `δ ; (C ⊗ ε) = ρ⁻¹`. Mirror of `left_counit_law`, using `mul_one`. -/
theorem right_counit_law :
    F.comultMor.comp (Container.dir₂ (ContainerMorphism.id C) F.counitMor)
      = (Container.dirRightUnitor C).inv := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact F.mul_one s p.1

/-- **Coassociativity** `δ ; (δ ⊗ C) ; α = δ ; (C ⊗ δ)`. On shapes both legs are `s ↦ (s, (s, s))`
(`rfl`, the associator re-bracketing the diagonal definitionally); on directions it is exactly the
monoid associativity `mul_assoc`. -/
theorem coassoc_law :
    (F.comultMor.comp (Container.dir₂ F.comultMor (ContainerMorphism.id C))).comp
        (Container.dirAssociator C C C).hom
      = F.comultMor.comp (Container.dir₂ (ContainerMorphism.id C) F.comultMor) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact F.mul_assoc s p.1 p.2.1 p.2.2

/-- **Converse direction of the classification.** A family of monoids on the direction sets of `C`
assembles a bare `⊗`-comonoid on `C`. -/
def toDirichletComonoid : C.DirichletComonoid where
  counit := F.counitMor
  comult := F.comultMor
  left_counit := F.left_counit_law
  right_counit := F.right_counit_law
  coassoc := F.coassoc_law

end Container.FamilyOfMonoids

/-! ## The two maps are mutually inverse

`DirichletComonoid.ext` reduces equality of two comonoids to equality of their counit and
comultiplication (the three law fields are `Prop`-valued, hence proof-irrelevant). With it, both
round trips close: `Family → Comonoid → Family` by `rfl`, and `Comonoid → Family → Comonoid` by
matching the counit (`Unit` η) and the comult (`ext'` along `hdiag`). -/

/-- Extensionality for `⊗`-comonoids: equal counit and comultiplication force equal comonoids, the
coherence laws being `Prop`. -/
theorem Container.DirichletComonoid.ext {C : Container} {D D' : C.DirichletComonoid}
    (hc : D.counit = D'.counit) (hm : D.comult = D'.comult) : D = D' := by
  obtain ⟨c, m, _, _, _⟩ := D
  obtain ⟨c', m', _, _, _⟩ := D'
  cases hc
  cases hm
  rfl

/-- Round trip `FamilyOfMonoids → DirichletComonoid → FamilyOfMonoids = id`. Holds by `rfl`: the
recovered `mul` is `δ.onPos` after transport along `hdiag : (s, s) = (s, s)`, which is `rfl` up to
proof irrelevance for `Eq`, so it reduces to the original `mul`; `one` round-trips on the nose; the
monoid-law fields are proof-irrelevant. -/
theorem Container.FamilyOfMonoids.toDirichletComonoid_toFamilyOfMonoids
    {C : Container} (F : C.FamilyOfMonoids) :
    F.toDirichletComonoid.toFamilyOfMonoids = F := rfl

/-- Round trip `DirichletComonoid → FamilyOfMonoids → DirichletComonoid = id`. The counit matches by
`Unit` η (both backward maps are `one s = ε♯_s(∗)`, and every `y`-position is `∗`); the comult
matches by `ext'` with shape equality `funext (fun s => (D.hdiag s).symm)` — the recovered `mul`
unfolds to `D.comult.onPos` after the same shape transport `ext'` supplies (the two transport proofs
agree by proof irrelevance for `Eq`, and `⟨p.1, p.2⟩ = p` by `Prod` η). -/
theorem Container.DirichletComonoid.toFamilyOfMonoids_toDirichletComonoid
    {C : Container} (D : C.DirichletComonoid) :
    D.toFamilyOfMonoids.toDirichletComonoid = D := by
  refine Container.DirichletComonoid.ext ?_ ?_
  · exact ContainerMorphism.ext' rfl (fun s p => rfl)
  · exact ContainerMorphism.ext' (funext fun s => (D.hdiag s).symm) (fun s p => rfl)

end Containers
