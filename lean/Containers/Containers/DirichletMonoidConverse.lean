import Containers.DirichletMonoid

/-!
# Converse: a monoid on shapes plus oplax fibres assembles a bare `⊗`-monoid

`Containers.DirichletMonoid` proves the **forward** half of the classification of bare
`⊗`-monoids in `(Cont, ⊗, y)`: every `Container.DirichletMonoid C` gives a
`Container.ShapeMonoidOplaxFibres C` (a monoid `(·, e)` on the shape set `S = C(1)` together
with an oplax monoidal functor `s ↦ C[s]` on the fibres). This file supplies the **converse**,
completing the `⊗`-monoid column to a full isomorphism.

The construction is the exact mirror of the forward extraction:

* the unit `η : y ⟶ C` sends the unique shape `∗` to the monoid unit `e`, with the forced
  (unique) backward map into `y[∗] = 1`;
* the multiplication `μ : C ⊗ C ⟶ C` is **forward** on shapes by the monoid product `s · t`
  and **backward** on positions by the oplax structure map `φ_{s,t} : C[s·t] → C[s] × C[t]`.

The three internal `Cont`-laws are read back off the algebraic data via
`ContainerMorphism.ext'`. On shapes each law is a monoid axiom (`one_smul`, `smul_one`,
`smul_assoc`); on positions it is the corresponding oplax coherence
(`phi_one_smul`, `phi_smul_one`, `phi_assoc`), with the induced shape transport collapsing by
definitional proof irrelevance for `Eq` (the associator re-brackets definitionally, exactly as
in the forward direction). No bespoke transport lemmas are needed beyond the library's `ext'`.

Both round trips hold **by `rfl`**: the data fields of `DirichletMonoid`/
`ShapeMonoidOplaxFibres` round-trip definitionally (shape/position maps agree up to `Prod`/`Unit`
η), and the law fields are `Prop`-valued, hence proof-irrelevant. So

  `Container.DirichletMonoid C  ≅  Container.ShapeMonoidOplaxFibres C`

as an honest isomorphism, both directions machine-checked.

STATUS (2026-07-19). Sorry-free. The forward map depended on *no* axioms; the converse laws use
`funext` (hence `Quot.sound`) to package the pointwise shape law into a function equality for
`ext'`. The two round-trip identities are pure `rfl` (no axioms). See `#print axioms` at the end.

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

open Container

namespace Container.ShapeMonoidOplaxFibres

variable {C : Container} (F : C.ShapeMonoidOplaxFibres)

/-- The **unit morphism** `η : y ⟶ C` of the assembled `⊗`-monoid: it sends the unique shape
`∗` to the monoid unit `e`, and its backward map is the forced unique map into `y[∗] = 1`. -/
def unitMor : ContainerMorphism Container.y C where
  onShapes := fun _ => F.e
  onPos := fun _ _ => ()

/-- The **multiplication morphism** `μ : C ⊗ C ⟶ C`: forward on shapes by the monoid product
`s · t`, backward on positions by the oplax structure map `φ_{s,t} : C[s·t] → C[s] × C[t]`. The
codomain `(C ⊗ C).Pos (s, t)` is `C.Pos s × C.Pos t` definitionally. -/
def mulMor : ContainerMorphism (C ⊗ C) C where
  onShapes := fun st => F.smul st.1 st.2
  onPos := fun st => F.phi st.1 st.2

/-- **Left unit law** `(η ⊗ C) ; μ = λ`. On shapes it is `one_smul`; the second position
coordinate is the oplax left-unit coherence `phi_one_smul`, and the first lands in `y[∗] = 1`. -/
theorem left_unit_law :
    (Container.dir₂ F.unitMor (ContainerMorphism.id C)).comp F.mulMor
      = (Container.dirLeftUnitor C).hom := by
  refine ContainerMorphism.ext' (funext fun s => F.one_smul s.2) ?_
  intro s p
  show ((), (F.phi F.e s.2 p).2) = ((), _)
  rw [F.phi_one_smul s.2 p]
  rfl

/-- **Right unit law** `(C ⊗ η) ; μ = ρ`. On shapes it is `smul_one`; the first position
coordinate is the oplax right-unit coherence `phi_smul_one`. -/
theorem right_unit_law :
    (Container.dir₂ (ContainerMorphism.id C) F.unitMor).comp F.mulMor
      = (Container.dirRightUnitor C).hom := by
  refine ContainerMorphism.ext' (funext fun s => F.smul_one s.1) ?_
  intro s p
  show ((F.phi s.1 F.e p).1, ()) = (_, ())
  rw [F.phi_smul_one s.1 p]
  rfl

/-- **Associativity** `(μ ⊗ C) ; μ = α ; (C ⊗ μ) ; μ`. On shapes it is `smul_assoc`; on
positions it is exactly the oplax associativity hexagon `phi_assoc`. The associator re-brackets
`((C[s] × C[t]) × C[u])` definitionally, and the shape transport `congrFun hs r` agrees with
`smul_assoc s t u` by proof irrelevance, so `phi_assoc` matches on the nose. -/
theorem assoc_law :
    (Container.dir₂ F.mulMor (ContainerMorphism.id C)).comp F.mulMor
      = ((Container.dirAssociator C C C).hom.comp
          (Container.dir₂ (ContainerMorphism.id C) F.mulMor)).comp F.mulMor := by
  refine ContainerMorphism.ext' (funext fun r => F.smul_assoc r.1.1 r.1.2 r.2) ?_
  intro r p
  exact F.phi_assoc r.1.1 r.1.2 r.2 p

/-- **Converse direction of the classification.** A monoid on shapes together with an oplax
monoidal functor on fibres assembles a bare `⊗`-monoid on `C`. -/
def toDirichletMonoid : C.DirichletMonoid where
  unit := F.unitMor
  mul := F.mulMor
  left_unit := F.left_unit_law
  right_unit := F.right_unit_law
  assoc := F.assoc_law

end Container.ShapeMonoidOplaxFibres

/-! ## The two maps are mutually inverse

Both round trips hold by `rfl`. The data fields round-trip definitionally (shape and position
maps agree up to `Prod`/`Unit` η), and the law fields are `Prop`-valued, hence irrelevant. This
upgrades the two forward/converse maps to a genuine isomorphism
`Container.DirichletMonoid C ≅ Container.ShapeMonoidOplaxFibres C`. -/

/-- Round trip `ShapeMonoidOplaxFibres → DirichletMonoid → ShapeMonoidOplaxFibres = id`. -/
theorem Container.ShapeMonoidOplaxFibres.toDirichletMonoid_toShapeMonoidOplaxFibres
    {C : Container} (F : C.ShapeMonoidOplaxFibres) :
    F.toDirichletMonoid.toShapeMonoidOplaxFibres = F := rfl

/-- Round trip `DirichletMonoid → ShapeMonoidOplaxFibres → DirichletMonoid = id`. -/
theorem Container.DirichletMonoid.toShapeMonoidOplaxFibres_toDirichletMonoid
    {C : Container} (M : C.DirichletMonoid) :
    M.toShapeMonoidOplaxFibres.toDirichletMonoid = M := rfl

end Containers
