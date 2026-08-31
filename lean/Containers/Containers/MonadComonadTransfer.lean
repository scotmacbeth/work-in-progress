import Containers.Cont

/-!
# The monad → comonad transfer on containers

For a monad `M = (M, η, μ)` on `Set` (here: `Type`), the assignment
`G (S, P) = (S, M ∘ P)` — apply `M` to every fibre of the direction bundle,
leaving shapes untouched — is a **comonad** on the category `Cont` of
containers. Its counit and comultiplication are the monad's unit and
multiplication *read backward through the position-contravariance*, and its
three comonad laws are **exactly** `M`'s three monad laws:

* counit-left  ⟺ `M`'s right-unit  `μ ∘ ηM = id`;
* counit-right ⟺ `M`'s left-unit   `μ ∘ Mη = id`;
* coassociativity ⟺ `M`'s associativity `μ ∘ Mμ = μ ∘ μM`.

This is Neil Ghani's Chapter 4 ("Monads and Comonads"), item 2. The paper proof
is `proofs/2026-07-25-monad-comonad-transfer.md` (MacBeth, PROVE session
2026-07-25). Structurally, `G` is the left coclosure of the substitution product
`◁` with `M` in the numerator, `G(S,P) = {M / (S,P)} = Lan_{(S,P)} M`
(Niu–Spivak, *Polynomial Functors*, arXiv:2312.00990, **Prop. 6.57** and
**Ex. 6.63**); this file formalises the elementary container-coordinate proof of
the comonad structure, not that identification.

## Why it is clean

A container morphism is a forward map on shapes together with a *backward*
(contravariant) map on positions, and `G`, `ε`, `δ` are all the identity on
shapes. So every equation reduces — via `ContainerMorphism.ext'` with `rfl` on
shapes — to a family of maps in `Type`, one per fibre, and each such fibre
equation is *literally* the correspondingly-named monad law applied pointwise.
No transports appear (the shape maps agree definitionally), mirroring
`Containers.DirichletComonoid`.

Everything is `Type`-level, Lean 4 core, no Mathlib. Every declaration closes
with only definitional proof irrelevance for `Eq`; no `sorry`, no classical
axioms.
-/

namespace Containers

/-- A **monad on `Type`** (= `Set`), bundled as an endofunctor with unit and
multiplication and their laws — enough to state and prove the transfer, with no
Mathlib dependency.

`obj`/`map` is the underlying functor; `η`/`μ` are the unit and multiplication;
`η_natural`/`μ_natural` are their naturality squares; `right_unit`/`left_unit`/
`assoc` are the three monad laws in the pointwise form
`μ ∘ ηM = id`, `μ ∘ Mη = id`, `μ ∘ μM = μ ∘ Mμ`. -/
structure SetMonad where
  /-- Object map of the endofunctor `M`. -/
  obj : Type → Type
  /-- Morphism map of `M`. -/
  map : {A B : Type} → (A → B) → obj A → obj B
  /-- Functor law: `M` preserves identities. -/
  map_id : ∀ {A : Type} (x : obj A), map (@id A) x = x
  /-- Functor law: `M` preserves composition. -/
  map_comp : ∀ {A B C : Type} (f : A → B) (g : B → C) (x : obj A),
    map (g ∘ f) x = map g (map f x)
  /-- The unit `η : A → M A`. -/
  η : {A : Type} → A → obj A
  /-- The multiplication `μ : M (M A) → M A`. -/
  μ : {A : Type} → obj (obj A) → obj A
  /-- Naturality of the unit `η`. -/
  η_natural : ∀ {A B : Type} (f : A → B) (a : A), map f (η a) = η (f a)
  /-- Naturality of the multiplication `μ`. -/
  μ_natural : ∀ {A B : Type} (f : A → B) (x : obj (obj A)),
    map f (μ x) = μ (map (map f) x)
  /-- Right-unit monad law, `μ ∘ ηM = id`. -/
  right_unit : ∀ {A : Type} (x : obj A), μ (η x) = x
  /-- Left-unit monad law, `μ ∘ Mη = id`. -/
  left_unit : ∀ {A : Type} (x : obj A), μ (map η x) = x
  /-- Associativity monad law, `μ ∘ μM = μ ∘ Mμ`. -/
  assoc : ∀ {A : Type} (x : obj (obj (obj A))), μ (μ x) = μ (map μ x)

namespace SetMonad

variable (M : SetMonad)

/-! ## The functor `G` -/

/-- The transfer functor on objects: `G (S, P) = (S, M ∘ P)` — leave the shapes
alone, apply `M` to every fibre. -/
def G (X : Container) : Container where
  Shape := X.Shape
  Pos := fun s => M.obj (X.Pos s)

/-- The transfer functor on morphisms: `G (u, f) = (u, {M(f_s)})`. The backward
position map is `M`'s functorial action on the backward map of `φ`. -/
def onMor {X Y : Container} (φ : ContainerMorphism X Y) :
    ContainerMorphism (M.G X) (M.G Y) where
  onShapes := φ.onShapes
  onPos := fun s => M.map (φ.onPos s)

/-- `G` preserves identities. Reduces fibrewise to `M`'s functor law `M id = id`. -/
theorem onMor_id (X : Container) :
    M.onMor (ContainerMorphism.id X) = ContainerMorphism.id (M.G X) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact M.map_id p

/-- `G` preserves composition. Reduces fibrewise to `M`'s functor law
`M (g ∘ f) = M g ∘ M f` (backward maps compose in the opposite order, so the
inner map is `ψ`'s). -/
theorem onMor_comp {X Y Z : Container}
    (φ : ContainerMorphism X Y) (ψ : ContainerMorphism Y Z) :
    M.onMor (φ.comp ψ) = (M.onMor φ).comp (M.onMor ψ) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact M.map_comp (ψ.onPos (φ.onShapes s)) (φ.onPos s) p

/-! ## The comonad data: counit and comultiplication -/

/-- The **counit** `ε : G X ⟶ X`: identity on shapes; on positions it is the
monad unit `η_{P s} : P s → M (P s)` (contravariant, so it points into the
`G`-fibre `M (P s)`). -/
def counit (X : Container) : ContainerMorphism (M.G X) X where
  onShapes := id
  onPos := fun _ => M.η

/-- The **comultiplication** `δ : G X ⟶ G (G X)`: identity on shapes; on
positions it is the monad multiplication `μ_{P s} : M (M (P s)) → M (P s)`. -/
def comult (X : Container) : ContainerMorphism (M.G X) (M.G (M.G X)) where
  onShapes := id
  onPos := fun _ => M.μ

/-! ## Naturality of the counit and comultiplication -/

/-- `ε` is a natural transformation `G ⟹ Id`. Fibrewise this is the naturality
square of `η` at the backward map `φ.onPos s`. -/
theorem counit_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    (M.onMor φ).comp (M.counit Y) = (M.counit X).comp φ := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact M.η_natural (φ.onPos s) p

/-- `δ` is a natural transformation `G ⟹ G ∘ G`. Fibrewise this is the
naturality square of `μ` at `φ.onPos s`. -/
theorem comult_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    (M.onMor φ).comp (M.comult Y) = (M.comult X).comp (M.onMor (M.onMor φ)) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact M.μ_natural (φ.onPos s) p

/-! ## The three comonad laws

Each is an equation of container morphisms that `ext'` reduces (with `rfl` on
shapes — no transport) to the correspondingly-named monad law applied in the
fibre `M (P s)`. -/

/-- **Counit-left law** `ε_{GX} ∘ δ = id_{GX}` (diagrammatic order:
`δ ≫ ε_{GX}`). Fibrewise `μ (η p) = p`, i.e. `M`'s **right-unit** law. -/
theorem counit_left (X : Container) :
    (M.comult X).comp (M.counit (M.G X)) = ContainerMorphism.id (M.G X) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact M.right_unit p

/-- **Counit-right law** `G ε ∘ δ = id_{GX}` (diagrammatic order: `δ ≫ G ε`).
Fibrewise `μ (M η p) = p`, i.e. `M`'s **left-unit** law. -/
theorem counit_right (X : Container) :
    (M.comult X).comp (M.onMor (M.counit X)) = ContainerMorphism.id (M.G X) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact M.left_unit p

/-- **Coassociativity** `δ_{GX} ∘ δ = G δ ∘ δ` (diagrammatic order:
`δ ≫ δ_{GX} = δ ≫ G δ`). Fibrewise `μ (μ p) = μ (M μ p)`, i.e. `M`'s
**associativity** law. -/
theorem coassoc (X : Container) :
    (M.comult X).comp (M.comult (M.G X))
      = (M.comult X).comp (M.onMor (M.comult X)) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact M.assoc p

end SetMonad

end Containers
