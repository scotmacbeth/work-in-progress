import Containers.Cont

/-!
# The comonad → monad transfer on containers

For a comonad `W = (W, ε, δ)` on `Set` (here: `Type`), the assignment
`H (S, P) = (S, W ∘ P)` — apply `W` to every fibre of the direction bundle,
leaving shapes untouched — is a **monad** on the category `Cont` of containers.
Its unit and multiplication are the comonad's counit and comultiplication *read
backward through the position-contravariance*, and its three monad laws are
**exactly** `W`'s three comonad laws:

* left-unit   `μ_H ∘ η_H = id`     ⟺ `W`'s left-counit  `ε ∘ δ = id`;
* right-unit  `μ_H ∘ H η_H = id`   ⟺ `W`'s right-counit `W ε ∘ δ = id`;
* associativity `μ_H ∘ μ_H = μ_H ∘ H μ_H` ⟺ `W`'s coassociativity `δ ∘ δ = W δ ∘ δ`.

This is the **exact dual** of `Containers.MonadComonadTransfer` (Neil Ghani's
Chapter 4, "Monads and Comonads", item 2), which sent a monad `M` on `Set` to a
comonad `G (S, P) = (S, M ∘ P)` on `Cont`. Together the two files close the
transfer story in Lean in **both directions**. The paper companion is
`proofs/2026-07-25-monad-comonad-transfer.md` (MacBeth, PROVE session
2026-07-25); the coordinate identifications of the substitution product `◁`
appear in Niu–Spivak, *Polynomial Functors*, arXiv:2312.00990, **§6**.

## Why it is clean

A container morphism is a forward map on shapes together with a *backward*
(contravariant) map on positions, and `H`, `η_H`, `μ_H` are all the identity on
shapes. So every equation reduces — via `ContainerMorphism.ext'` with `rfl` on
shapes — to a family of maps in `Type`, one per fibre, and each such fibre
equation is *literally* the correspondingly-named comonad law applied pointwise.
No transports appear (the shape maps agree definitionally), mirroring
`Containers.MonadComonadTransfer`.

Everything is `Type`-level, Lean 4 core, no Mathlib. Every declaration closes
with only definitional proof irrelevance for `Eq`; no `sorry`, no classical
axioms.
-/

namespace Containers

/-- A **comonad on `Type`** (= `Set`), bundled as an endofunctor with counit and
comultiplication and their laws — enough to state and prove the transfer, with no
Mathlib dependency. This is the exact dual of
`Containers.SetMonad`.

`obj`/`map` is the underlying functor; `ε`/`δ` are the counit and
comultiplication; `ε_natural`/`δ_natural` are their naturality squares;
`left_counit`/`right_counit`/`coassoc` are the three comonad laws in the
pointwise form `ε ∘ δ = id`, `W ε ∘ δ = id`, `δ ∘ δ = W δ ∘ δ`. -/
structure SetComonad where
  /-- Object map of the endofunctor `W`. -/
  obj : Type → Type
  /-- Morphism map of `W`. -/
  map : {A B : Type} → (A → B) → obj A → obj B
  /-- Functor law: `W` preserves identities. -/
  map_id : ∀ {A : Type} (x : obj A), map (@id A) x = x
  /-- Functor law: `W` preserves composition. -/
  map_comp : ∀ {A B C : Type} (f : A → B) (g : B → C) (x : obj A),
    map (g ∘ f) x = map g (map f x)
  /-- The counit `ε : W A → A`. -/
  ε : {A : Type} → obj A → A
  /-- The comultiplication `δ : W A → W (W A)`. -/
  δ : {A : Type} → obj A → obj (obj A)
  /-- Naturality of the counit `ε`. -/
  ε_natural : ∀ {A B : Type} (f : A → B) (x : obj A), ε (map f x) = f (ε x)
  /-- Naturality of the comultiplication `δ`. -/
  δ_natural : ∀ {A B : Type} (f : A → B) (x : obj A),
    δ (map f x) = map (map f) (δ x)
  /-- Left-counit comonad law, `ε ∘ δ = id`. -/
  left_counit : ∀ {A : Type} (x : obj A), ε (δ x) = x
  /-- Right-counit comonad law, `W ε ∘ δ = id`. -/
  right_counit : ∀ {A : Type} (x : obj A), map ε (δ x) = x
  /-- Coassociativity comonad law, `δ ∘ δ = W δ ∘ δ`. -/
  coassoc : ∀ {A : Type} (x : obj A), δ (δ x) = map δ (δ x)

namespace SetComonad

variable (W : SetComonad)

/-! ## The functor `H` -/

/-- The transfer functor on objects: `H (S, P) = (S, W ∘ P)` — leave the shapes
alone, apply `W` to every fibre. -/
def H (X : Container) : Container where
  Shape := X.Shape
  Pos := fun s => W.obj (X.Pos s)

/-- The transfer functor on morphisms: `H (u, f) = (u, {W(f_s)})`. The backward
position map is `W`'s functorial action on the backward map of `φ`. -/
def onMor {X Y : Container} (φ : ContainerMorphism X Y) :
    ContainerMorphism (W.H X) (W.H Y) where
  onShapes := φ.onShapes
  onPos := fun s => W.map (φ.onPos s)

/-- `H` preserves identities. Reduces fibrewise to `W`'s functor law `W id = id`. -/
theorem onMor_id (X : Container) :
    W.onMor (ContainerMorphism.id X) = ContainerMorphism.id (W.H X) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact W.map_id p

/-- `H` preserves composition. Reduces fibrewise to `W`'s functor law
`W (g ∘ f) = W g ∘ W f` (backward maps compose in the opposite order, so the
inner map is `ψ`'s). -/
theorem onMor_comp {X Y Z : Container}
    (φ : ContainerMorphism X Y) (ψ : ContainerMorphism Y Z) :
    W.onMor (φ.comp ψ) = (W.onMor φ).comp (W.onMor ψ) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact W.map_comp (ψ.onPos (φ.onShapes s)) (φ.onPos s) p

/-! ## The monad data: unit and multiplication -/

/-- The **unit** `η : X ⟶ H X`: identity on shapes; on positions it is the
comonad counit `ε_{P s} : W (P s) → P s` (contravariant, so it points out of the
`H`-fibre `W (P s)`). -/
def unit (X : Container) : ContainerMorphism X (W.H X) where
  onShapes := id
  onPos := fun _ => W.ε

/-- The **multiplication** `μ : H (H X) ⟶ H X`: identity on shapes; on positions
it is the comonad comultiplication `δ_{P s} : W (P s) → W (W (P s))`. -/
def mult (X : Container) : ContainerMorphism (W.H (W.H X)) (W.H X) where
  onShapes := id
  onPos := fun _ => W.δ

/-! ## Naturality of the unit and multiplication -/

/-- `η` is a natural transformation `Id ⟹ H`. Fibrewise this is the naturality
square of `ε` at the backward map `φ.onPos s`. -/
theorem unit_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    φ.comp (W.unit Y) = (W.unit X).comp (W.onMor φ) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact (W.ε_natural (φ.onPos s) p).symm

/-- `μ` is a natural transformation `H ∘ H ⟹ H`. Fibrewise this is the
naturality square of `δ` at `φ.onPos s`. -/
theorem mult_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    (W.onMor (W.onMor φ)).comp (W.mult Y) = (W.mult X).comp (W.onMor φ) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact (W.δ_natural (φ.onPos s) p).symm

/-! ## The three monad laws

Each is an equation of container morphisms that `ext'` reduces (with `rfl` on
shapes — no transport) to the correspondingly-named comonad law applied in the
fibre `W (P s)`. -/

/-- **Left-unit law** `μ ∘ η_{HX} = id_{HX}` (diagrammatic order:
`η_{HX} ≫ μ`). Fibrewise `ε (δ p) = p`, i.e. `W`'s **left-counit** law. -/
theorem unit_left (X : Container) :
    (W.unit (W.H X)).comp (W.mult X) = ContainerMorphism.id (W.H X) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact W.left_counit p

/-- **Right-unit law** `μ ∘ H η = id_{HX}` (diagrammatic order: `H η ≫ μ`).
Fibrewise `W ε (δ p) = p`, i.e. `W`'s **right-counit** law. -/
theorem unit_right (X : Container) :
    (W.onMor (W.unit X)).comp (W.mult X) = ContainerMorphism.id (W.H X) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact W.right_counit p

/-- **Associativity** `μ_{HX} ∘ μ = H μ ∘ μ` (diagrammatic order:
`μ_{HX} ≫ μ = H μ ≫ μ`). Fibrewise `δ (δ p) = W δ (δ p)`, i.e. `W`'s
**coassociativity** law. -/
theorem mult_assoc (X : Container) :
    (W.mult (W.H X)).comp (W.mult X)
      = (W.onMor (W.mult X)).comp (W.mult X) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s p
  exact W.coassoc p

end SetComonad

end Containers
