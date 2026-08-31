import Containers.DirichletClosed

/-!
# The Dirichlet internal hom in Π-form: `[q, r] ≅ Πᵢ (r ◁ q[i]·y)`

`Containers.DirichletClosed` proves `(Cont, ⊗, y)` is closed using the
**morphism-form** internal hom

  `[q, r] = Container.ihom q r`,   `Shape = ContainerMorphism q r`,
  `Pos f = (t : q.Shape) × r.Pos (f.onShapes t)`

(Niu–Spivak, *Polynomial Functors*, Eq. 4.79, arXiv:2312.00990). This file
formalises the **uniform Π-form** of the same internal hom,

  `[q, r]  ≅  Πᵢ₌ₛq ( r ◁ (q[i] · y) )`,

as an isomorphism of containers (`ContainerIso`). Here:

* `q[i] · y` is the monomial container `Container.monomialY (q.Pos i)` — shape set
  `q.Pos i`, one position per shape;
* `◁` is the sequential/composition operator (`Container.seq`, `Containers.Sequential`);
* `Πᵢ` is the arbitrary-index container product `Container.piCont` defined here
  (the binary product `Container.prod` is the `Bool`-indexed case).

## Why this matters

The Π-form is the closure formula MacBeth quotes to Neil; before this file only
the morphism form was machine-checked. Closing the gap makes the uniform-formula
claim as solid as the morphism-form one. See the 2026-07-15 proof
`proofs/2026-07-20-…`/`proofs/2026-07-15-uniform-closure-day-tensors.md`.

## The mathematical content

On shapes the iso is the **type-theoretic axiom of choice** (`ΠΣ ≅ ΣΠ`):

  `ContainerMorphism q r  ≅  Πᵢ ( Σ t : r.Shape, (r.Pos t → q.Pos i) )`,

carrying a morphism `(u, φ)` to `i ↦ ⟨u i, φ i⟩`. On positions it is the
regrouping `Σᵢ (r.Pos (σ i).1 × Unit)  ≅  Σ t, r.Pos (…)`, the trailing `Unit`
coming from the single position of `y`.

## Note on the proofs

Every round trip is `rfl`. The shape bijection is definitional because Lean 4 has
**definitional eta** for structures (`ContainerMorphism`), for `Sigma`, and for
functions; the position regrouping is definitional additionally by **`Unit`-eta**
(`x.2.2 : Unit` collapses to `()`). No transports, no `ext'`, no `funext` — the
same pleasant situation as the morphism-form closure (`DirichletClosed`) and the
`◁` associator (`Sequential`). This confirms the LEAN.md worry about
"propositionally-invertible choice / `heq_sigma_mk` transport" does **not**
materialise here.

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

/-! ## The monomial container and the indexed product -/

/-- The **monomial** container `A · y`: shape set `A`, exactly one position per
shape. Its extension is `X ↦ A × X`. This is `q[i] · y` when `A = q.Pos i`. -/
def Container.monomialY (A : Type) : Container where
  Shape := A
  Pos := fun _ => Unit

/-- The **indexed product** `Πᵢ Cᵢ` of a family of containers over an arbitrary
index type `I`. A shape is a choice function `(i : I) → (C i).Shape`; a position
over a choice `s` is a dependent pair `(i : I) × (C i).Pos (s i)`.

This is the product of the induced polynomial functors. The binary product
`Container.prod` (`Containers.Cont`) is the `I = Bool` case: `Shape = Π_Bool`,
`Pos = Σ_Bool`. -/
def Container.piCont (I : Type) (C : I → Container) : Container where
  Shape := (i : I) → (C i).Shape
  Pos := fun s => (i : I) × (C i).Pos (s i)

/-- Notation for the right-hand side of the Π-form: the indexed product
`Πᵢ ( r ◁ (q[i] · y) )`. -/
def Container.ihomPi (q r : Container) : Container :=
  Container.piCont q.Shape (fun i => r ◁ Container.monomialY (q.Pos i))

/-! ## The isomorphism

We spell out the four data of the `ContainerIso` and observe that both round
trips are `rfl`.

The shape maps:

* forward `hom.onShapes`: a morphism `f : q ⟶ r` becomes the choice function
  `i ↦ ⟨f.onShapes i, f.onPos i⟩` (its shape map at `i` together with its
  backward position map at `i`);
* backward `inv.onShapes`: a choice function `s` becomes the morphism with shape
  map `i ↦ (s i).1` and backward position map `i ↦ (s i).2`.

The position maps (running backward, per the contravariance of `Cont`):

* `hom.onPos`: an `ihomPi`-position `⟨i, ⟨p, ()⟩⟩` drops the `Unit` to give the
  `ihom`-position `⟨i, p⟩`;
* `inv.onPos`: an `ihom`-position `⟨t, p⟩` pads with `()` to give `⟨t, ⟨p, ()⟩⟩`.
-/

/-- **The Π-form of the Dirichlet internal hom.**

`[q, r]  ≅  Πᵢ₌ₛq ( r ◁ (q[i] · y) )` as containers. Both round trips are `rfl`.

Together with `dirichlet_closure` (`Containers.DirichletClosed`) this shows the
uniform closure formula `[q, r] = Πᵢ r ◁ (q[i]·y)` denotes the *same* internal
hom as the morphism form `ContainerMorphism q r`, so the closed structure on
`(Cont, ⊗, y)` may be read off the uniform formula. -/
def Container.ihomPiIso (q r : Container) :
    ContainerIso (Container.ihom q r) (Container.ihomPi q r) where
  hom :=
    { onShapes := fun f i => ⟨f.onShapes i, f.onPos i⟩
      onPos := fun _ x => ⟨x.1, x.2.1⟩ }
  inv :=
    { onShapes := fun s =>
        { onShapes := fun i => (s i).1
          onPos := fun i => (s i).2 }
      onPos := fun _ x => ⟨x.1, x.2, ()⟩ }
  hom_inv := rfl
  inv_hom := rfl

/-! ## Shape and position sanity checks

These record, definitionally, what the two sides *are* — useful for downstream
citation and to pin the convention. -/

/-- The shapes of the Π-form are choice functions selecting, for each `q`-shape
`i`, an `r`-shape together with a relabelling of its positions by `q.Pos i`. -/
theorem Container.ihomPi_shape_eq (q r : Container) :
    (Container.ihomPi q r).Shape
      = ((i : q.Shape) → (t : r.Shape) × (r.Pos t → q.Pos i)) := rfl

/-- The positions of the Π-form over a choice `s` are `Σᵢ (r.Pos (s i).1 × Unit)`. -/
theorem Container.ihomPi_pos_eq (q r : Container)
    (s : (Container.ihomPi q r).Shape) :
    (Container.ihomPi q r).Pos s
      = ((i : q.Shape) × (_ : r.Pos (s i).1) × Unit) := rfl

/-- The forward map sends a morphism to its choice function `i ↦ ⟨u i, φ i⟩`. -/
theorem Container.ihomPiIso_hom_onShapes (q r : Container)
    (f : ContainerMorphism q r) (i : q.Shape) :
    (Container.ihomPiIso q r).hom.onShapes f i = ⟨f.onShapes i, f.onPos i⟩ := rfl

end Containers
