import Containers.BiKleisli

/-!
# The effect–coeffect arrow category for `M = Maybe`, machine-checked

This file **instantiates** the abstract biKleisli skeleton of
`Containers.BiKleisli` at the concrete non-branching monad `M := Maybe`
(`Option`), discharging *all four* mixed-distributive-law axioms E1′–E4′ — in
particular the branching-obstructed **E2′** (`distrib_mult`) — and thereby
obtains a machine-checked **associative** effect–coeffect arrow category on
`Cont`.

The paper is `proofs/2026-07-29-effect-coeffect-arrows.md` (MacBeth, PROVE
session 2026-07-29): its Theorem A says the arrows `G_M p → T_M q` form a
category **iff `M` is non-branching**, and it reports a direct computer check
that *all* `1536/1536` associativity instances hold for `Maybe`. This file turns
the "`Maybe` is a genuine category" half into an end-to-end Lean instance.

## The concrete data (Maybe / arity-≤ 1)

* **`G_Maybe = SetMonad.toComonad Maybe`** — the transfer comonad
  `G(S,P) = (S, Option ∘ P)`, already Lean-verified in
  `Containers.MonadComonadTransfer`.
* **`T_Maybe (S,P) = (Option S, P⋆)`** — the Ahman–Bauer effect monad
  (arXiv:2409.17664, Thm 6.3). The `∏`-cointerpretation `P⋆(m) = ∏_{b∈lv m} P`
  is **degenerate** here because `Maybe` has at most one leaf:
  `P⋆(none) = 1` (empty product) and `P⋆(some s) = P s`.
* **`κ : G_Maybe T_Maybe ⇒ T_Maybe G_Maybe`** — the *reverse* lax compositor
  `∏ Option → Option ∏`. Degenerate again: identity on the `some` fibre, and the
  empty-product `η`-padding `1 → Option 1` on the `none` fibre.

E2′ holds precisely because the `∏` is over ≤ 1 leaf, so "union-of-products vs
product-of-unions" — the branching obstruction — cannot arise.

Everything is `Type`-level, Lean 4 core, no Mathlib. Backward position maps are
transport-free; each container-morphism equality closes via
`ContainerMorphism.ext'` with `rfl` shape maps where possible, and definitional
proof irrelevance for `Eq` absorbs the non-`rfl` `Option.join`/`Option.map`
shape identities.
-/

namespace Containers
namespace BiKleisliMaybe

/-! ## `Maybe` as a `SetMonad` (so `G_Maybe` comes for free) -/

/-- The `Maybe = Option` monad on `Type`, bundled as a `SetMonad`. Every law is
`rfl` or `cases`-clean. The transfer comonad `G_Maybe := SetMonad.toComonad
Maybe` is then obtained from `Containers.MonadComonadTransfer` with no extra
work. -/
def Maybe : SetMonad where
  obj := Option
  map := fun f => Option.map f
  map_id := by intro A x; cases x <;> rfl
  map_comp := by intro A B C f g x; cases x <;> rfl
  η := fun a => some a
  μ := fun x => Option.join x
  η_natural := by intro A B f a; rfl
  μ_natural := by intro A B f x; cases x <;> rfl
  right_unit := by intro A x; rfl
  left_unit := by intro A x; cases x <;> rfl
  assoc := by intro A x; cases x <;> rfl

/-- The transfer comonad `G_Maybe (S,P) = (S, Option ∘ P)`. -/
def GMaybe : Comonad Container := SetMonad.toComonad Maybe

/-! ## The effect monad `T_Maybe` on `Cont`

`T_Maybe (S,P) = (Option S, P⋆)` with `P⋆(none) = PUnit`, `P⋆(some s) = P s`. -/

/-- The degenerate `∏`-cointerpretation of positions for `Maybe`: an empty
product (`PUnit`) over the shapeless `none`, and the single fibre `P s` over
`some s`. -/
def TPos (X : Container) : Option X.Shape → Type
  | none => PUnit
  | some s => X.Pos s

/-- The object map of `T_Maybe`. -/
def TObj (X : Container) : Container where
  Shape := Option X.Shape
  Pos := TPos X

/-- The morphism map of `T_Maybe`: `Option.map` on shapes, and on positions the
identity over `none`, `φ`'s backward map over `some`. -/
def Tmap {X Y : Container} (φ : ContainerMorphism X Y) :
    ContainerMorphism (TObj X) (TObj Y) where
  onShapes := Option.map φ.onShapes
  onPos := fun m => match m with
    | none => id
    | some s => φ.onPos s

/-- The unit `η^T : X ⟶ T_Maybe X`: `some` on shapes, identity on positions. -/
def Tunit (X : Container) : ContainerMorphism X (TObj X) where
  onShapes := some
  onPos := fun _ => id

/-- The multiplication `μ^T : T_Maybe (T_Maybe X) ⟶ T_Maybe X`: `Option.join` on
shapes, identity on positions (every fibre collapses to itself). -/
def Tmult (X : Container) : ContainerMorphism (TObj (TObj X)) (TObj X) where
  onShapes := Option.join
  onPos := fun m => match m with
    | none => id
    | some none => id
    | some (some _) => id

/-! ### The functor laws for `T_Maybe` -/

theorem Tmap_id (X : Container) :
    Tmap (ContainerMorphism.id X) = ContainerMorphism.id (TObj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m <;> rfl

theorem Tmap_comp {X Y Z : Container}
    (φ : ContainerMorphism X Y) (ψ : ContainerMorphism Y Z) :
    Tmap (φ.comp ψ) = (Tmap φ).comp (Tmap ψ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m <;> rfl

/-! ### Naturality of `η^T` and `μ^T` -/

theorem Tunit_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    φ.comp (Tunit Y) = (Tunit X).comp (Tmap φ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext s; rfl
  · intro s p; rfl

theorem Tmult_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    (Tmap (Tmap φ)).comp (Tmult Y) = (Tmult X).comp (Tmap φ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m with
    | none => rfl
    | some m => cases m <;> rfl

/-! ### The three monad laws for `T_Maybe` -/

theorem Tright_unit (X : Container) :
    (Tunit (TObj X)).comp (Tmult X) = ContainerMorphism.id (TObj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; rfl
  · intro m p; cases m <;> rfl

theorem Tleft_unit (X : Container) :
    (Tmap (Tunit X)).comp (Tmult X) = ContainerMorphism.id (TObj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m <;> rfl

theorem Tassoc (X : Container) :
    (Tmult (TObj X)).comp (Tmult X) = (Tmap (Tmult X)).comp (Tmult X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m with
    | none => rfl
    | some m => cases m <;> rfl
  · intro m p; cases m with
    | none => rfl
    | some m => cases m with
      | none => rfl
      | some m => cases m <;> rfl

/-- `T_Maybe` bundled as an abstract `Monad` on `Cont`. -/
def TMaybe : Monad Container where
  obj := TObj
  map := Tmap
  map_id := Tmap_id
  map_comp := fun f g => Tmap_comp f g
  η := Tunit
  μ := Tmult
  η_natural := fun f => Tunit_natural f
  μ_natural := fun f => Tmult_natural f
  right_unit := Tright_unit
  left_unit := Tleft_unit
  assoc := Tassoc

/-! ## The reverse compositor `κ : G_Maybe T_Maybe ⇒ T_Maybe G_Maybe`

Identity on shapes; on positions the lax product comparison `∏ Option → Option ∏`,
which for arity ≤ 1 is the empty-product `η`-padding `1 → Option 1` over `none`
and the identity over `some`. -/

/-- The compositor `κ_X : G_Maybe (T_Maybe X) ⟶ T_Maybe (G_Maybe X)`. -/
def kappa (X : Container) :
    ContainerMorphism (GMaybe.obj (TMaybe.obj X)) (TMaybe.obj (GMaybe.obj X)) where
  onShapes := id
  onPos := fun m => match m with
    | none => fun _ => some PUnit.unit
    | some _ => id

/-! ### The four mixed-distributive-law axioms for `κ`, all discharged for `Maybe` -/

theorem kappa_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    Category.comp (GMaybe.map (TMaybe.map φ)) (kappa Y)
      = Category.comp (kappa X) (TMaybe.map (GMaybe.map φ)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m <;> rfl

/-- **E1′** (`distrib_unit`): `G η^T ≫ κ = η^T_{GX}`. -/
theorem kappa_distrib_unit (X : Container) :
    Category.comp (GMaybe.map (TMaybe.η X)) (kappa X) = TMaybe.η (GMaybe.obj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; rfl
  · intro m p; cases p <;> rfl

/-- **E3′** (`distrib_counit`): `κ ≫ T ε = ε_{TX}`. -/
theorem kappa_distrib_counit (X : Container) :
    Category.comp (kappa X) (TMaybe.map (GMaybe.ε X)) = GMaybe.ε (TMaybe.obj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m <;> rfl

/-- **E2′** (`distrib_mult`): `G μ^T ≫ κ = κ_{TX} ≫ T κ ≫ μ^T_{GX}`. This is the
branching-obstructed axiom; it holds here because the `∏` is over ≤ 1 leaf. -/
theorem kappa_distrib_mult (X : Container) :
    Category.comp (GMaybe.map (TMaybe.μ X)) (kappa X)
      = Category.comp (Category.comp (kappa (TMaybe.obj X)) (TMaybe.map (kappa X)))
          (TMaybe.μ (GMaybe.obj X)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m with
    | none => rfl
    | some m => cases m <;> rfl
  · intro m p; cases m with
    | none => rfl
    | some m => cases m with
      | none => rfl
      | some s => cases p <;> rfl

/-- **E4′** (`distrib_comult`): `κ ≫ T δ = δ_{TX} ≫ G κ ≫ κ_{GX}`. -/
theorem kappa_distrib_comult (X : Container) :
    Category.comp (kappa X) (TMaybe.map (GMaybe.δ X))
      = Category.comp (Category.comp (GMaybe.δ (TMaybe.obj X)) (GMaybe.map (kappa X)))
          (kappa (GMaybe.obj X)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m with
    | none => rfl
    | some s => cases p <;> rfl

/-- The **mixed distributive law** `κ : G_Maybe T_Maybe ⇒ T_Maybe G_Maybe`,
bundling the four axioms above. This is a machine-checked witness that E2′ — the
associativity/branching axiom — holds for `Maybe`. -/
def mixedDistrib : MixedDistrib GMaybe TMaybe where
  κ := kappa
  κ_natural := fun f => kappa_natural f
  distrib_unit := kappa_distrib_unit
  distrib_counit := kappa_distrib_counit
  distrib_mult := kappa_distrib_mult
  distrib_comult := kappa_distrib_comult

/-! ## The effect–coeffect arrow category for `Maybe`

Specialising the abstract biKleisli laws of `Containers.MixedDistrib` at
`mixedDistrib` gives the three category laws for the arrows
`G_Maybe p ⟶ T_Maybe q`. The associativity law consumes E2′ — machine-checked
above precisely for `Maybe` — so this is a fully verified *associative*
effect–coeffect arrow category for a non-branching effect. -/

/-- **Identity law (left)** for the `Maybe` arrow category. -/
theorem arr_unit_left {p q : Container} (g : mixedDistrib.Hom p q) :
    mixedDistrib.acomp (mixedDistrib.arrId p) g = g :=
  mixedDistrib.unit_left g

/-- **Identity law (right)** for the `Maybe` arrow category. -/
theorem arr_unit_right {p q : Container} (f : mixedDistrib.Hom p q) :
    mixedDistrib.acomp f (mixedDistrib.arrId q) = f :=
  mixedDistrib.unit_right f

/-- **Associativity** of composition in the `Maybe` arrow category — the E2′
payload, holding because `Maybe` is non-branching. -/
theorem arr_assoc {p q r s : Container}
    (f : mixedDistrib.Hom p q) (g : mixedDistrib.Hom q r) (h : mixedDistrib.Hom r s) :
    mixedDistrib.acomp (mixedDistrib.acomp f g) h
      = mixedDistrib.acomp f (mixedDistrib.acomp g h) :=
  mixedDistrib.acomp_assoc f g h

end BiKleisliMaybe
end Containers
