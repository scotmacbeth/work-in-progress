import Containers.TimesMonoid

/-!
# Converse: a monoid on shapes plus oplax coproduct fibres assembles a bare `×`-monoid

`Containers.TimesMonoid` proves the **forward** half of the classification of bare
`×`-monoids in `(Cont, ×, 1)` (the product/cartesian tensor, `× = Day(Set, ⊔, ∅)`): every
`Container.TimesMonoid C` gives a `Container.ShapeMonoidOplaxFibresCoproduct C` (a monoid
`(·, e)` on the shape set `S = C(1)` with **empty identity fibre** `C[e] = ∅`, together with an
oplax monoidal functor `s ↦ C[s]` on the fibres into `(Set, ⊔, ∅)`). This file supplies the
**converse**, completing the `×`-monoid column to a full isomorphism — the mirror of
`Containers.DirichletMonoidConverse` (the `⊗` side, MacBeth 2026-07-20).

This formalises **Theorem B** of MacBeth's PROVE note `2026-07-19-dirichlet-monoid-classification.md`
§6; Theorems A (`⊗`) and B (`×`) are one theorem parameterised by the fibre monoidal structure the
Day tensor uses (`⊗` uses `(Set, ×, 1)`, `×` uses `(Set, ⊔, ∅)`).

The construction is the exact mirror of the forward extraction:

* the unit `η : 1 ⟶ C` sends the unique shape `∗` to the monoid unit `e`, with backward map the
  **empty-fibre witness** `posEmpty : C[e] → ∅ = 1[∗]` (this is where `×` differs from `⊗`: the
  identity fibre is empty, not a singleton);
* the multiplication `μ : C × C ⟶ C` is **forward** on shapes by the monoid product `s · t`
  and **backward** on positions by the oplax structure map / routing
  `ψ_{s,t} : C[s·t] → C[s] ⊕ C[t]` (the codomain `(C × C)[s,t] = C[s] ⊕ C[t]` definitionally).

The three internal `Cont`-laws are read back off the algebraic data via
`ContainerMorphism.ext'`. On shapes each law is a monoid axiom (`one_smul`, `smul_one`,
`smul_assoc`); on positions it is the corresponding oplax coherence
(`psi_one_smul`, `psi_smul_one`, `psi_assoc`). The unit-law positions are exposed by `show` and
closed by rewriting with the oplax unit coherence — the `Sum.elim` collapses the routed injection
(and the empty-fibre summand never fires). The associativity positions are exactly `psi_assoc`;
the associator re-brackets `(C[s] ⊕ C[t]) ⊕ C[u]` definitionally, and the induced shape transport
`congrFun hs r` agrees with `smul_assoc s t u` by definitional proof irrelevance for `Eq`.

Both round trips hold **by `rfl`**: the data fields of `TimesMonoid`/
`ShapeMonoidOplaxFibresCoproduct` round-trip definitionally (shape/position maps agree up to
`Prod`/`Unit` η), and the law fields are `Prop`-valued, hence proof-irrelevant. So

  `Container.TimesMonoid C  ≅  Container.ShapeMonoidOplaxFibresCoproduct C`

as an honest isomorphism, both directions machine-checked.

STATUS (2026-07-20). Sorry-free. The three converse laws use `funext` (hence `Quot.sound`) to
package the pointwise shape law into a function equality for `ext'`; the two round-trip identities
are pure `rfl`. See `#print axioms` at the end.

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

open Container

namespace Container.ShapeMonoidOplaxFibresCoproduct

variable {C : Container} (F : C.ShapeMonoidOplaxFibresCoproduct)

/-- The **unit morphism** `η : 1 ⟶ C` of the assembled `×`-monoid: it sends the unique shape
`∗` to the monoid unit `e`, and its backward map is the empty-fibre witness
`posEmpty : C[e] → ∅ = 1[∗]`. -/
def unitMor : ContainerMorphism Container.one C where
  onShapes := fun _ => F.e
  onPos := fun _ => F.posEmpty

/-- The **multiplication morphism** `μ : C × C ⟶ C`: forward on shapes by the monoid product
`s · t`, backward on positions by the oplax structure map `ψ_{s,t} : C[s·t] → C[s] ⊕ C[t]`. The
codomain `(C × C).Pos (s, t)` is `C.Pos s ⊕ C.Pos t` definitionally. -/
def mulMor : ContainerMorphism (C.prod C) C where
  onShapes := fun st => F.smul st.1 st.2
  onPos := fun st => F.psi st.1 st.2

/-- **Left unit law** `(η × C) ; μ = λ`. On shapes it is `one_smul`; on positions the routing
`ψ_{e,s}` lands entirely in the `C[s]` summand (`psi_one_smul`), so the `Sum.elim` of the
`prod₂`-onPos collapses to `Sum.inr`, matching the left unitor `p ↦ inr p`. -/
theorem left_unit_law :
    (Container.prod₂ F.unitMor (ContainerMorphism.id C)).comp F.mulMor
      = (Container.prodLeftUnitor C).hom := by
  refine ContainerMorphism.ext' (funext fun s => F.one_smul s.2) ?_
  intro s p
  show Sum.elim (Sum.inl ∘ F.posEmpty) Sum.inr (F.psi F.e s.2 p)
      = Sum.inr (F.one_smul s.2 ▸ p)
  rw [F.psi_one_smul s.2 p]
  rfl

/-- **Right unit law** `(C × η) ; μ = ρ`. On shapes it is `smul_one`; on positions `ψ_{s,e}`
lands entirely in the `C[s]` summand (`psi_smul_one`), matching the right unitor `p ↦ inl p`. -/
theorem right_unit_law :
    (Container.prod₂ (ContainerMorphism.id C) F.unitMor).comp F.mulMor
      = (Container.prodRightUnitor C).hom := by
  refine ContainerMorphism.ext' (funext fun s => F.smul_one s.1) ?_
  intro s p
  show Sum.elim Sum.inl (Sum.inr ∘ F.posEmpty) (F.psi s.1 F.e p)
      = Sum.inl (F.smul_one s.1 ▸ p)
  rw [F.psi_smul_one s.1 p]
  rfl

/-- **Associativity** `(μ × C) ; μ = α ; (C × μ) ; μ`. On shapes it is `smul_assoc`; on
positions it is exactly the oplax associativity hexagon `psi_assoc`. The associator re-brackets
`((C[s] ⊕ C[t]) ⊕ C[u])` definitionally, and the shape transport `congrFun hs r` agrees with
`smul_assoc s t u` by proof irrelevance, so `psi_assoc` matches on the nose. -/
theorem assoc_law :
    (Container.prod₂ F.mulMor (ContainerMorphism.id C)).comp F.mulMor
      = ((Container.prodAssociator C C C).hom.comp
          (Container.prod₂ (ContainerMorphism.id C) F.mulMor)).comp F.mulMor := by
  refine ContainerMorphism.ext' (funext fun r => F.smul_assoc r.1.1 r.1.2 r.2) ?_
  intro r p
  exact F.psi_assoc r.1.1 r.1.2 r.2 p

/-- **Converse direction of the classification.** A monoid on shapes with empty identity fibre,
together with an oplax monoidal functor on fibres into `(Set, ⊔, ∅)`, assembles a bare
`×`-monoid on `C`. -/
def toTimesMonoid : C.TimesMonoid where
  unit := F.unitMor
  mul := F.mulMor
  left_unit := F.left_unit_law
  right_unit := F.right_unit_law
  assoc := F.assoc_law

end Container.ShapeMonoidOplaxFibresCoproduct

/-! ## The two maps are mutually inverse

Both round trips hold by `rfl`. The data fields round-trip definitionally (shape and position
maps agree up to `Prod`/`Unit` η), and the law fields are `Prop`-valued, hence irrelevant. This
upgrades the forward/converse pair to a genuine isomorphism
`Container.TimesMonoid C ≅ Container.ShapeMonoidOplaxFibresCoproduct C`. -/

/-- Round trip
`ShapeMonoidOplaxFibresCoproduct → TimesMonoid → ShapeMonoidOplaxFibresCoproduct = id`. -/
theorem Container.ShapeMonoidOplaxFibresCoproduct.toTimesMonoid_toShapeMonoidOplaxFibresCoproduct
    {C : Container} (F : C.ShapeMonoidOplaxFibresCoproduct) :
    F.toTimesMonoid.toShapeMonoidOplaxFibresCoproduct = F := rfl

/-- Round trip
`TimesMonoid → ShapeMonoidOplaxFibresCoproduct → TimesMonoid = id`. -/
theorem Container.TimesMonoid.toShapeMonoidOplaxFibresCoproduct_toTimesMonoid
    {C : Container} (M : C.TimesMonoid) :
    M.toShapeMonoidOplaxFibresCoproduct.toTimesMonoid = M := rfl

end Containers
