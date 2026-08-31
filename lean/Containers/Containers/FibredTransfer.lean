import Containers.MonadComonadTransfer

/-!
# `G_M` is a *fibred* comonad: reindexing-stability and cartesian preservation

`Containers.MonadComonadTransfer` machine-checks that the transfer
`G_M (S, P) = (S, M ∘ P)` is a **comonad** on the category `Cont` of containers.
That file says nothing about the *fibrational* structure. This file supplies it.

View `Cont → Set` as the fibration sending a container `(S, P)` to its shape type
`S` (the base), with **vertical** morphisms those that are the identity on
shapes and **cartesian** morphisms those whose backward position map is a
bijection fibrewise. Neil's 2026-08-05 fibrational front hinges on one fact of
this fibration: the transfer `G_M`, and containers generally, **preserve
cartesian morphisms**. We certify exactly the two facts that make `G_M` a
*cartesian vertical fibred comonad* (a comonad in `Fib(Set)`, Jacobs sense):

1. **Reindexing-stability** (`SetMonad.G_reindex`). Reindexing a container along a
   base map `u : S → Y.Shape` is `u^*(Y) := (S, Y.Pos ∘ u)`. Then
   `G_M (u^* Y) = u^* (G_M Y)` — both send the fibre over `s` to `M (Y.Pos (u s))`.
   This is the Beck–Chevalley/vertical-compatibility square, and it holds by
   `rfl`.

2. **Cartesian-morphism preservation** (`SetMonad.onMor_cartesian`). If a
   container morphism `φ` is cartesian — its backward map `φ.onPos s` is a
   bijection `Y.Pos (φ.onShapes s) ≅ X.Pos s` for every shape `s` — then
   `G_M φ` is cartesian, its backward map `M (φ.onPos s)` being a bijection
   `M (Y.Pos (φ.onShapes s)) ≅ M (X.Pos s)`. This holds **for every monad `M`**:
   only functoriality of `M` on isomorphisms is used (`map_id`, `map_comp`), *no*
   hypothesis that `M` is cartesian. This is the audit's "`G_M` cartesian for all
   `M`" asymmetry — the solid, hypothesis-free half of the fibrational story
   (the `T_M`-side, where branching bites, is the harder converse and is left as
   the documented next target).

Verticality of the comonad data (`counit`, `comult`, and `G_M` itself are all
the identity on shapes) is recorded in `*_vertical` below, also by `rfl`.

Everything is `Type`-level, Lean 4 core, no Mathlib; no `sorry`, no classical
axioms (only `propext`/`Quot.sound`-free `rfl` and functor laws).
-/

namespace Containers

/-! ## Reindexing in the fibration `Cont → Set` -/

/-- **Reindexing** a container `Y` along a base map `u : S → Y.Shape`:
keep the position family, but pull its shape-indexing back along `u`.
This is the cartesian lift in the fibration `Cont → Set` (shapes as base):
`u^*(S', Q) := (S, Q ∘ u)`. -/
def Container.reindex (Y : Container) {S : Type} (u : S → Y.Shape) : Container where
  Shape := S
  Pos := fun s => Y.Pos (u s)

/-! ## Cartesian morphisms

A container morphism `φ : X ⟶ Y` carries a *backward* position map
`φ.onPos s : Y.Pos (φ.onShapes s) → X.Pos s`. It is **cartesian** exactly when
each of these backward maps is a bijection. We record a bijection by a two-sided
inverse (no `Equiv`/Mathlib machinery needed). -/

/-- A two-sided inverse of a function `f : A → B`. -/
structure TwoSidedInverse {A B : Type} (f : A → B) where
  /-- The inverse map. -/
  inv : B → A
  /-- Left inverse: `inv ∘ f = id`. -/
  left : ∀ a, inv (f a) = a
  /-- Right inverse: `f ∘ inv = id`. -/
  right : ∀ b, f (inv b) = b

/-- A container morphism is **cartesian** when its backward position map is a
bijection in every fibre: a choice of two-sided inverse of `φ.onPos s` for each
shape `s`. -/
def IsCartesian {X Y : Container} (φ : ContainerMorphism X Y) : Type :=
  (s : X.Shape) → TwoSidedInverse (φ.onPos s)

namespace SetMonad

variable (M : SetMonad)

/-! ## 1. Reindexing-stability (vertical/fibred) -/

/-- **Reindexing-stability.** The transfer commutes with reindexing along any
base map `u : S → Y.Shape`: `G_M (u^* Y) = u^* (G_M Y)`. Both sides are the
container `(S, fun s => M (Y.Pos (u s)))`; the equation holds by `rfl`. -/
theorem G_reindex (Y : Container) {S : Type} (u : S → Y.Shape) :
    M.G (Y.reindex u) = (M.G Y).reindex u := rfl

/-! ## 2. Cartesian-morphism preservation (for every `M`) -/

/-- **Cartesian preservation.** If `φ` is cartesian then so is `G_M φ`: the
backward map `M (φ.onPos s)` is a bijection with inverse `M ((h s).inv)`, by
functoriality of `M` (`map_comp` collapses the composite of inverses, `map_id`
finishes). This uses **no** hypothesis on `M` beyond it being a functor — it
holds for every monad `M`, branching or not. -/
def onMor_cartesian {X Y : Container} (φ : ContainerMorphism X Y)
    (h : IsCartesian φ) : IsCartesian (M.onMor φ) := fun s =>
  { inv := M.map (h s).inv
    left := fun a => by
      show M.map (h s).inv (M.map (φ.onPos s) a) = a
      rw [← M.map_comp]
      rw [show ((h s).inv ∘ φ.onPos s) = id from funext (h s).left]
      exact M.map_id a
    right := fun b => by
      show M.map (φ.onPos s) (M.map (h s).inv b) = b
      rw [← M.map_comp]
      rw [show (φ.onPos s ∘ (h s).inv) = id from funext (h s).right]
      exact M.map_id b }

/-! ## Verticality of the comonad data

`G_M`, its counit `ε` and comultiplication `δ` are all the identity on shapes,
i.e. they are **vertical** in the fibration `Cont → Set`. Together with the two
results above, this is what it means for `G_M` to be a *cartesian vertical
fibred comonad*. Each is `rfl`. -/

/-- `G_M` acts as the identity on the base: `(G_M φ)`'s shape map is `φ`'s. -/
theorem onMor_vertical {X Y : Container} (φ : ContainerMorphism X Y) :
    (M.onMor φ).onShapes = φ.onShapes := rfl

/-- The counit `ε : G_M X ⟶ X` is **vertical** (identity on shapes). -/
theorem counit_vertical (X : Container) :
    (M.counit X).onShapes = id := rfl

/-- The comultiplication `δ : G_M X ⟶ G_M (G_M X)` is **vertical**. -/
theorem comult_vertical (X : Container) :
    (M.comult X).onShapes = id := rfl

end SetMonad

end Containers
