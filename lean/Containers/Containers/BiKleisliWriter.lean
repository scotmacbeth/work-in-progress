import Containers.BiKleisli

/-!
# The effect–coeffect arrow category for `M = Writer` over a monoid, machine-checked

This file **instantiates** the abstract biKleisli skeleton of
`Containers.BiKleisli` at the concrete non-branching monad `M := Writer A` (the
writer monad `A × (−)` over an arbitrary monoid `A`), discharging *all four*
mixed-distributive-law axioms E1′–E4′ — in particular the branching-obstructed
**E2′** (`distrib_mult`) — and thereby obtains a machine-checked **associative**
effect–coeffect arrow category on `Cont`.

Together with `Containers.BiKleisliMaybe` (the exception corner `E + (−)`), this
file (the writer corner `A × (−)`) supplies the *second* generator of the affine
class `E + A × (−)` of `proofs/2026-07-30-affine-classification.md` (MacBeth,
PROVE session 2026-07-30). The paper's Theorem A says the arrows `G_M p → T_M q`
form a category **iff `M` is non-branching**; `Writer A` is non-branching (it has
exactly one leaf shape), so E2′ holds unconditionally here — the `∏`-cointerpretation
is over exactly one leaf, so the "union-of-products vs product-of-unions"
branching obstruction cannot arise.

## The concrete data (Writer / arity `= 1`)

* **`GWriter W = SetMonad.toComonad (Writer W)`** — the transfer comonad
  `G(S,P) = (S, A × P)`, from `Containers.MonadComonadTransfer`.
* **`TWriter W (S,P) = (A × S, P ∘ π₂)`** — the Ahman–Bauer effect monad
  (arXiv:2409.17664, Thm 6.3). Each writer shape `(a,s)` has exactly one leaf, so
  the `∏`-cointerpretation `P⋆(a,s) = ∏_{one leaf} P = P s` is single-fibred.
* **`kappa : G_W T_W ⇒ T_W G_W`** — the *reverse* lax compositor. Because there is
  **no nullary leaf** (unlike `Maybe`'s `none`), both sides have shape `A × S` and
  fibre `A × P s`, definitionally, so `kappa` is the **identity** morphism — even
  cleaner than the `Maybe` compositor's empty-product `η`-padding.

The only place a genuine (non-`rfl`) transport surfaces is the three monad laws of
`T_W` whose *shape* map rearranges monoid multiplication (`Tright_unit`/`Tleft_unit`/
`Tassoc`, needing `one_mul`/`mul_one`/`mul_assoc`); since the position fibre `P s`
does not depend on the mutated `A`-coordinate, the transport is absorbed by the
`heq_pos` helper (`HEq (h ▸ p) p`) and `eq_of_heq`.

Everything is `Type`-level, Lean 4 core, no Mathlib. No `sorry`, no classical
axioms; every declaration closes with only `[propext, Quot.sound]`-style
definitional reasoning plus `eq_of_heq`.
-/

namespace Containers
namespace BiKleisliWriter

/-! ## A bare monoid, Mathlib-free -/

/-- A **monoid** on a `Type`, bundled with the three laws — enough to build the
writer monad `A × (−)` with no Mathlib dependency. -/
structure Mon where
  /-- The carrier. -/
  A : Type
  /-- The unit. -/
  one : A
  /-- The multiplication. -/
  mul : A → A → A
  /-- Left unit law. -/
  one_mul : ∀ a, mul one a = a
  /-- Right unit law. -/
  mul_one : ∀ a, mul a one = a
  /-- Associativity. -/
  mul_assoc : ∀ a b c, mul (mul a b) c = mul a (mul b c)

/-- `ℤ/2` as a `Mon`: `Bool` with `xor` (unit `false`). The concrete witness the
LEAN target asks for; all three laws close by `decide`/`cases`. -/
def Z2 : Mon where
  A := Bool
  one := false
  mul := xor
  one_mul := fun a => by cases a <;> rfl
  mul_one := fun a => by cases a <;> rfl
  mul_assoc := fun a b c => by cases a <;> cases b <;> cases c <;> rfl

/-! ## `Writer W` as a `SetMonad` (so `G_W` comes for free) -/

/-- The **writer monad** `Writer W X = A × X` over a monoid `W`, bundled as a
`SetMonad`. Unit is `(1, −)`; multiplication multiplies the two `A`-tags. The
functor/naturality laws are `rfl` (product η); the three monad laws are exactly
`W`'s `one_mul`/`mul_one`/`mul_assoc`. The transfer comonad
`G_W := SetMonad.toComonad (Writer W)` then comes from
`Containers.MonadComonadTransfer` with no extra work. -/
def Writer (W : Mon) : SetMonad where
  obj := fun X => W.A × X
  map := fun f p => (p.1, f p.2)
  map_id := fun _ => rfl
  map_comp := fun _ _ _ => rfl
  η := fun x => (W.one, x)
  μ := fun p => (W.mul p.1 p.2.1, p.2.2)
  η_natural := fun _ _ => rfl
  μ_natural := fun _ _ => rfl
  right_unit := fun x => by
    show (W.mul W.one x.1, x.2) = x
    rw [W.one_mul]
  left_unit := fun x => by
    show (W.mul x.1 W.one, x.2) = x
    rw [W.mul_one]
  assoc := fun x => by
    show (W.mul (W.mul x.1 x.2.1) x.2.2.1, x.2.2.2)
       = (W.mul x.1 (W.mul x.2.1 x.2.2.1), x.2.2.2)
    rw [W.mul_assoc]

/-- The transfer comonad `G_W (S,P) = (S, A × P)`. -/
def GWriter (W : Mon) : Comonad Container := SetMonad.toComonad (Writer W)

section
variable (W : Mon)

/-! ## The effect monad `T_W` on `Cont`

`T_W (S,P) = (A × S, P ∘ π₂)`: prepend an `A`-tag to the shape, positions
unchanged (the single leaf carries the whole fibre). -/

/-- The object map of `T_W`: `Shape = A × S`, `Pos (a,s) = P s`. -/
def TObj (X : Container) : Container where
  Shape := W.A × X.Shape
  Pos := fun as => X.Pos as.2

/-- The morphism map of `T_W`: `A × (−)` on shapes, `φ`'s backward map on the
single fibre. -/
def Tmap {X Y : Container} (φ : ContainerMorphism X Y) :
    ContainerMorphism (TObj W X) (TObj W Y) where
  onShapes := fun as => (as.1, φ.onShapes as.2)
  onPos := fun as => φ.onPos as.2

/-- The unit `η^T : X ⟶ T_W X`: tag with `1` on shapes, identity on the fibre. -/
def Tunit (X : Container) : ContainerMorphism X (TObj W X) where
  onShapes := fun s => (W.one, s)
  onPos := fun _ => id

/-- The multiplication `μ^T : T_W (T_W X) ⟶ T_W X`: multiply the two `A`-tags on
shapes, identity on the fibre. -/
def Tmult (X : Container) : ContainerMorphism (TObj W (TObj W X)) (TObj W X) where
  onShapes := fun abs => (W.mul abs.1 abs.2.1, abs.2.2)
  onPos := fun _ => id

/-! ### A transport helper for the monoid-shaped laws

The three monad laws below have a *shape* map that rearranges monoid
multiplication, so the `ContainerMorphism.ext'` shape hypothesis is not `rfl`;
but the position fibre `P s` is independent of the mutated `A`-coordinate, so the
resulting transport is trivial. `heq_pos` packages this. -/

/-- Transport along an equality is `HEq` to the original term. -/
theorem heq_pos {α : Type} {motive : α → Type} {a b : α} (h : a = b)
    (p : motive a) : HEq (h ▸ p) p := by
  subst h; rfl

/-! ### The functor laws for `T_W` -/

theorem Tmap_id (X : Container) :
    Tmap W (ContainerMorphism.id X) = ContainerMorphism.id (TObj W X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext as; rfl
  · intro as p; rfl

theorem Tmap_comp {X Y Z : Container}
    (φ : ContainerMorphism X Y) (ψ : ContainerMorphism Y Z) :
    Tmap W (φ.comp ψ) = (Tmap W φ).comp (Tmap W ψ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext as; rfl
  · intro as p; rfl

/-! ### Naturality of `η^T` and `μ^T` -/

theorem Tunit_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    φ.comp (Tunit W Y) = (Tunit W X).comp (Tmap W φ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext s; rfl
  · intro s p; rfl

theorem Tmult_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    (Tmap W (Tmap W φ)).comp (Tmult W Y) = (Tmult W X).comp (Tmap W φ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext abs; rfl
  · intro abs p; rfl

/-! ### The three monad laws for `T_W`

These are the only declarations with a non-`rfl` shape map (monoid
`one_mul`/`mul_one`/`mul_assoc`); the position transport is discharged by
`heq_pos`. -/

theorem Tright_unit (X : Container) :
    (Tunit W (TObj W X)).comp (Tmult W X) = ContainerMorphism.id (TObj W X) := by
  have hs : ((Tunit W (TObj W X)).comp (Tmult W X)).onShapes
      = (ContainerMorphism.id (TObj W X)).onShapes := by
    funext as
    show (W.mul W.one as.1, as.2) = as
    rw [W.one_mul]; rfl
  refine ContainerMorphism.ext' hs ?_
  intro s p
  exact (eq_of_heq (heq_pos (congrFun hs s) p)).symm

theorem Tleft_unit (X : Container) :
    (Tmap W (Tunit W X)).comp (Tmult W X) = ContainerMorphism.id (TObj W X) := by
  have hs : ((Tmap W (Tunit W X)).comp (Tmult W X)).onShapes
      = (ContainerMorphism.id (TObj W X)).onShapes := by
    funext as
    show (W.mul as.1 W.one, as.2) = as
    rw [W.mul_one]; rfl
  refine ContainerMorphism.ext' hs ?_
  intro s p
  exact (eq_of_heq (heq_pos (congrFun hs s) p)).symm

theorem Tassoc (X : Container) :
    (Tmult W (TObj W X)).comp (Tmult W X) = (Tmap W (Tmult W X)).comp (Tmult W X) := by
  have hs : ((Tmult W (TObj W X)).comp (Tmult W X)).onShapes
      = ((Tmap W (Tmult W X)).comp (Tmult W X)).onShapes := by
    funext abs
    show (W.mul (W.mul abs.1 abs.2.1) abs.2.2.1, abs.2.2.2)
       = (W.mul abs.1 (W.mul abs.2.1 abs.2.2.1), abs.2.2.2)
    rw [W.mul_assoc]
  refine ContainerMorphism.ext' hs ?_
  intro s p
  exact (eq_of_heq (heq_pos (congrFun hs s) p)).symm

/-- `T_W` bundled as an abstract `Monad` on `Cont`. -/
def TWriter : Monad Container where
  obj := TObj W
  map := Tmap W
  map_id := Tmap_id W
  map_comp := fun f g => Tmap_comp W f g
  η := Tunit W
  μ := Tmult W
  η_natural := fun f => Tunit_natural W f
  μ_natural := fun f => Tmult_natural W f
  right_unit := Tright_unit W
  left_unit := Tleft_unit W
  assoc := Tassoc W

/-! ## The reverse compositor `κ : G_W T_W ⇒ T_W G_W`

Both `G_W (T_W X)` and `T_W (G_W X)` have shape `A × S` and fibre `A × P s`
definitionally (no nullary leaf), so `κ` is the identity morphism. -/

/-- The compositor `κ_X : G_W (T_W X) ⟶ T_W (G_W X)` — the identity. -/
def kappa (X : Container) :
    ContainerMorphism ((GWriter W).obj ((TWriter W).obj X))
      ((TWriter W).obj ((GWriter W).obj X)) where
  onShapes := id
  onPos := fun _ => id

/-! ### The four mixed-distributive-law axioms for `κ`, all discharged for `Writer` -/

theorem kappa_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    Category.comp ((GWriter W).map ((TWriter W).map φ)) (kappa W Y)
      = Category.comp (kappa W X) ((TWriter W).map ((GWriter W).map φ)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; rfl
  · intro m p; rfl

/-- **E1′** (`distrib_unit`): `G η^T ≫ κ = η^T_{GX}`. -/
theorem kappa_distrib_unit (X : Container) :
    Category.comp ((GWriter W).map ((TWriter W).η X)) (kappa W X)
      = (TWriter W).η ((GWriter W).obj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext s; rfl
  · intro s p; rfl

/-- **E3′** (`distrib_counit`): `κ ≫ T ε = ε_{TX}`. -/
theorem kappa_distrib_counit (X : Container) :
    Category.comp (kappa W X) ((TWriter W).map ((GWriter W).ε X))
      = (GWriter W).ε ((TWriter W).obj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; rfl
  · intro m p; rfl

/-- **E2′** (`distrib_mult`): `G μ^T ≫ κ = κ_{TX} ≫ T κ ≫ μ^T_{GX}`. The
branching-obstructed axiom; it holds here because the `∏` is over a single
leaf. -/
theorem kappa_distrib_mult (X : Container) :
    Category.comp ((GWriter W).map ((TWriter W).μ X)) (kappa W X)
      = Category.comp
          (Category.comp (kappa W ((TWriter W).obj X)) ((TWriter W).map (kappa W X)))
          ((TWriter W).μ ((GWriter W).obj X)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; rfl
  · intro m p; rfl

/-- **E4′** (`distrib_comult`): `κ ≫ T δ = δ_{TX} ≫ G κ ≫ κ_{GX}`. -/
theorem kappa_distrib_comult (X : Container) :
    Category.comp (kappa W X) ((TWriter W).map ((GWriter W).δ X))
      = Category.comp
          (Category.comp ((GWriter W).δ ((TWriter W).obj X)) ((GWriter W).map (kappa W X)))
          (kappa W ((GWriter W).obj X)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; rfl
  · intro m p; rfl

/-- The **mixed distributive law** `κ : G_W T_W ⇒ T_W G_W`, bundling the four
axioms above. Machine-checked witness that E2′ — the associativity/branching
axiom — holds for `Writer W`. -/
def mixedDistrib : MixedDistrib (GWriter W) (TWriter W) where
  κ := kappa W
  κ_natural := fun f => kappa_natural W f
  distrib_unit := kappa_distrib_unit W
  distrib_counit := kappa_distrib_counit W
  distrib_mult := kappa_distrib_mult W
  distrib_comult := kappa_distrib_comult W

/-! ## The effect–coeffect arrow category for `Writer W`

Specialising the abstract biKleisli laws of `Containers.MixedDistrib` at
`mixedDistrib` gives the three category laws for the arrows
`G_W p ⟶ T_W q`. Associativity consumes E2′ — machine-checked above for
`Writer W` — so this is a fully verified *associative* effect–coeffect arrow
category for the writer generator of the affine class. -/

/-- **Identity law (left)** for the `Writer` arrow category. -/
theorem arr_unit_left {p q : Container} (g : (mixedDistrib W).Hom p q) :
    (mixedDistrib W).acomp ((mixedDistrib W).arrId p) g = g :=
  (mixedDistrib W).unit_left g

/-- **Identity law (right)** for the `Writer` arrow category. -/
theorem arr_unit_right {p q : Container} (f : (mixedDistrib W).Hom p q) :
    (mixedDistrib W).acomp f ((mixedDistrib W).arrId q) = f :=
  (mixedDistrib W).unit_right f

/-- **Associativity** of composition in the `Writer` arrow category — the E2′
payload, holding because `Writer W` is non-branching. -/
theorem arr_assoc {p q r s : Container}
    (f : (mixedDistrib W).Hom p q) (g : (mixedDistrib W).Hom q r)
    (h : (mixedDistrib W).Hom r s) :
    (mixedDistrib W).acomp ((mixedDistrib W).acomp f g) h
      = (mixedDistrib W).acomp f ((mixedDistrib W).acomp g h) :=
  (mixedDistrib W).acomp_assoc f g h

end

/-! ## The concrete `ℤ/2` witness

Instantiating the general construction at `Z2` (`Bool`/`xor`) gives the explicit
machine-checked associative arrow category the LEAN target asks for. -/

/-- The associativity law for the `ℤ/2` writer arrow category — the concrete
`E2′` witness for the writer generator of the affine class. -/
theorem arr_assoc_Z2 {p q r s : Container}
    (f : (mixedDistrib Z2).Hom p q) (g : (mixedDistrib Z2).Hom q r)
    (h : (mixedDistrib Z2).Hom r s) :
    (mixedDistrib Z2).acomp ((mixedDistrib Z2).acomp f g) h
      = (mixedDistrib Z2).acomp f ((mixedDistrib Z2).acomp g h) :=
  arr_assoc Z2 f g h

end BiKleisliWriter
end Containers
