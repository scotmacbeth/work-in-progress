import Containers.BiKleisli

/-!
# The effect–coeffect arrow category for the whole non-branching class `M = E + A×(−)`

This file **instantiates** the abstract biKleisli skeleton of `Containers.BiKleisli`
at the *general* cartesian non-branching monad

`M X = E + A × X`     (`A` a monoid, `E` a left `A`-set),

discharging *all four* mixed-distributive-law axioms E1′–E4′ — in particular the
branching-obstructed **E2′** (`distrib_mult`) — and thereby obtaining a
machine-checked **associative** effect–coeffect arrow category on `Cont` for the
entire classified family at once.

This is the *fusion* of the two boundary generators already Lean-verified
separately:

* `Containers.BiKleisliMaybe` — the exception corner `E + (−)` (`A = 1`);
* `Containers.BiKleisliWriter` — the writer corner `A × (−)` (`E = ∅`).

Here both generators run simultaneously: a `Sum` case-split on the shape sends the
`inl e` (nullary / exception) summand through the Maybe apparatus and the
`inr (a, s)` (unary / writer) summand through the Writer apparatus. The monad `μ`
lets the writer log **act** on an outer exception (`inr (a, inl e') ↦ inl (a ⊙ e')`),
which is exactly the left `A`-set structure of the classification.

## The classification (paper: `proofs/2026-07-30-affine-classification.md`, MacBeth)

Theorem T1 there says: for a cartesian Set-monad `M`, the effect–coeffect arrow
category `Arr_M` exists **iff** `M` is non-branching **iff** `M ≅ E + A×(−)` is a
*writer-with-absorbing-exceptions* monad — `(A,·,e)` a monoid, `(E, ⊙)` a left
`A`-set, unit `η_X(x) = (e, x)`, and multiplication
```
   μ_X : E + A×(E + A×X) → E + A×X,
   inl e'             ↦ inl e'                (outer exception absorbs)
   inr (a, inl e')    ↦ inl (a ⊙ e')          (log acts on the exception)
   inr (a, inr (a',x))↦ inr (a·a', x)         (writer multiplication).
```
Theorem T2 says `κ` satisfies E1′–E4′ across the whole non-branching class, the
`∏`-cointerpretation being a product over `≤ 1` leaf so the "union-of-products vs
product-of-unions" obstruction never forms. This file is the machine-checked
witness of both, for arbitrary `A`, `E`, and (crucially) an arbitrary left action.

`T_M` is the Ahman–Bauer effect monad (arXiv:2409.17664, Thm 6.3), `G_M`/`κ` are
MacBeth's 07-25/27/29 transfer comonad and reverse compositor.

## Where the genuine transport lives

As in `BiKleisliWriter`, the only non-`rfl` shape maps are the three `T_M` monad
laws, which rearrange monoid multiplication and the `A`-action (`one_mul`,
`mul_one`, `mul_assoc`, `one_act`, `mul_act`). Because every position fibre is
either `PUnit` (over `inl`) or `X.Pos s` (over `inr (a, s)`) — independent of the
mutated `A`-coordinate — the position transport is discharged by the `heq_pos`
helper. All four `κ`-axioms are `cases`-then-`rfl`, the nullary summand carrying
the Maybe-style `η^M`-padding.

Everything is `Type`-level, Lean 4 core, no Mathlib. No `sorry`, no classical
axioms; declarations close with `[propext, Quot.sound]`-style definitional
reasoning plus `eq_of_heq`.
-/

namespace Containers
namespace BiKleisliAffine

/-! ## The algebraic datum: a monoid `A` acting on a set `E` (Mathlib-free) -/

/-- A **monoid `A` together with a left `A`-set `E`** — the algebraic datum of the
non-branching class `M X = E + A×X` (paper `2026-07-30-affine-classification.md`,
Thm T1(4)). Bundled with the three monoid laws and the two action laws, enough to
build the writer-with-absorbing-exceptions monad with no Mathlib dependency. -/
structure Aff where
  /-- The monoid carrier (the unary / writer shapes). -/
  A : Type
  /-- The exception carrier (the nullary shapes), a left `A`-set. -/
  E : Type
  /-- The monoid unit. -/
  one : A
  /-- The monoid multiplication. -/
  mul : A → A → A
  /-- The left action `⊙ : A × E → E`. -/
  act : A → E → E
  /-- Left unit law of `A`. -/
  one_mul : ∀ a, mul one a = a
  /-- Right unit law of `A`. -/
  mul_one : ∀ a, mul a one = a
  /-- Associativity of `A`. -/
  mul_assoc : ∀ a b c, mul (mul a b) c = mul a (mul b c)
  /-- The action is unital. -/
  one_act : ∀ e, act one e = e
  /-- The action is associative with `mul`. -/
  mul_act : ∀ a b e, act (mul a b) e = act a (act b e)

/-! ## `M = E + A×(−)` as a `SetMonad` (so `G_M` comes for free) -/

/-- The **writer-with-absorbing-exceptions monad** `M X = E + A×X`, bundled as a
`SetMonad`. Unit is the writer unit `(1, −)`; multiplication absorbs an outer
exception, lets the log act on an inner exception, and multiplies two logs. The
functor/naturality laws are `cases`-`rfl`; the three monad laws are exactly the
monoid + action laws of `W`. The transfer comonad `G_M := SetMonad.toComonad (MAff
W)` then comes from `Containers.MonadComonadTransfer` with no extra work. -/
def MAff (W : Aff) : SetMonad where
  obj := fun X => W.E ⊕ W.A × X
  map := fun f x => match x with
    | Sum.inl e => Sum.inl e
    | Sum.inr p => Sum.inr (p.1, f p.2)
  map_id := by intro A x; cases x <;> rfl
  map_comp := by intro A B C f g x; cases x <;> rfl
  η := fun x => Sum.inr (W.one, x)
  μ := fun x => match x with
    | Sum.inl e => Sum.inl e
    | Sum.inr (a, Sum.inl e') => Sum.inl (W.act a e')
    | Sum.inr (a, Sum.inr (a', y)) => Sum.inr (W.mul a a', y)
  η_natural := by intro A B f a; rfl
  μ_natural := by
    intro A B f x
    cases x with
    | inl e => rfl
    | inr p => cases p with
      | mk a y => cases y <;> rfl
  right_unit := by
    intro A x
    cases x with
    | inl e => show Sum.inl (W.act W.one e) = Sum.inl e; rw [W.one_act]
    | inr p => cases p with
      | mk a y => show Sum.inr (W.mul W.one a, y) = Sum.inr (a, y); rw [W.one_mul]
  left_unit := by
    intro A x
    cases x with
    | inl e => rfl
    | inr p => cases p with
      | mk a y => show Sum.inr (W.mul a W.one, y) = Sum.inr (a, y); rw [W.mul_one]
  assoc := by
    intro A x
    cases x with
    | inl e => rfl
    | inr p => cases p with
      | mk a y => cases y with
        | inl e' => rfl
        | inr q => cases q with
          | mk a' z => cases z with
            | inl e'' =>
              show Sum.inl (W.act (W.mul a a') e'') = Sum.inl (W.act a (W.act a' e''))
              rw [W.mul_act]
            | inr r => cases r with
              | mk a'' w =>
                show Sum.inr (W.mul (W.mul a a') a'', w) = Sum.inr (W.mul a (W.mul a' a''), w)
                rw [W.mul_assoc]

/-- The transfer comonad `G_M (S,P) = (S, E + A × P)`. -/
def GAff (W : Aff) : Comonad Container := SetMonad.toComonad (MAff W)

section
variable (W : Aff)

/-! ## The effect monad `T_M` on `Cont`

`T_M (S,P) = (E + A×S, P⋆)` with `P⋆(inl e) = PUnit` (nullary) and
`P⋆(inr (a,s)) = P s` (single leaf). -/

/-- The `∏`-cointerpretation of positions for `M = E + A×(−)`: an empty product
(`PUnit`) over the shapeless `inl e`, and the single fibre `P s` over `inr (a,s)`. -/
def TPos (X : Container) : (W.E ⊕ W.A × X.Shape) → Type
  | Sum.inl _ => PUnit
  | Sum.inr as => X.Pos as.2

/-- The object map of `T_M`. -/
def TObj (X : Container) : Container where
  Shape := W.E ⊕ W.A × X.Shape
  Pos := TPos W X

/-- The morphism map of `T_M`: `M`'s shape action on shapes, identity over the
`inl` fibre, `φ`'s backward map over the single `inr` fibre. -/
def Tmap {X Y : Container} (φ : ContainerMorphism X Y) :
    ContainerMorphism (TObj W X) (TObj W Y) where
  onShapes := fun s => match s with
    | Sum.inl e => Sum.inl e
    | Sum.inr as => Sum.inr (as.1, φ.onShapes as.2)
  onPos := fun s => match s with
    | Sum.inl _ => id
    | Sum.inr as => φ.onPos as.2

/-- The unit `η^T : X ⟶ T_M X`: writer-tag with `1`, identity on the fibre. -/
def Tunit (X : Container) : ContainerMorphism X (TObj W X) where
  onShapes := fun s => Sum.inr (W.one, s)
  onPos := fun _ => id

/-- The multiplication `μ^T : T_M (T_M X) ⟶ T_M X`: `μ^M` on shapes (absorb / act /
multiply), identity on every fibre (each collapses to the same set). -/
def Tmult (X : Container) : ContainerMorphism (TObj W (TObj W X)) (TObj W X) where
  onShapes := fun m => match m with
    | Sum.inl e => Sum.inl e
    | Sum.inr (a, Sum.inl e') => Sum.inl (W.act a e')
    | Sum.inr (a, Sum.inr (a', s)) => Sum.inr (W.mul a a', s)
  onPos := fun m => match m with
    | Sum.inl _ => id
    | Sum.inr (_, Sum.inl _) => id
    | Sum.inr (_, Sum.inr _) => id

/-! ### A transport helper for the monoid/action-shaped laws (as in `BiKleisliWriter`) -/

/-- Transport along an equality is `HEq` to the original term. -/
theorem heq_pos {α : Type} {motive : α → Type} {a b : α} (h : a = b)
    (p : motive a) : HEq (h ▸ p) p := by
  subst h; rfl

/-! ### The functor laws for `T_M` -/

theorem Tmap_id (X : Container) :
    Tmap W (ContainerMorphism.id X) = ContainerMorphism.id (TObj W X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext s; cases s <;> rfl
  · intro s p; cases s <;> rfl

theorem Tmap_comp {X Y Z : Container}
    (φ : ContainerMorphism X Y) (ψ : ContainerMorphism Y Z) :
    Tmap W (φ.comp ψ) = (Tmap W φ).comp (Tmap W ψ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext s; cases s <;> rfl
  · intro s p; cases s <;> rfl

/-! ### Naturality of `η^T` and `μ^T` -/

theorem Tunit_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    φ.comp (Tunit W Y) = (Tunit W X).comp (Tmap W φ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext s; rfl
  · intro s p; rfl

theorem Tmult_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    (Tmap W (Tmap W φ)).comp (Tmult W Y) = (Tmult W X).comp (Tmap W φ) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m
    cases m with
    | inl e => rfl
    | inr p => cases p with
      | mk a s => cases s <;> rfl
  · intro m p
    cases m with
    | inl e => rfl
    | inr q => cases q with
      | mk a s => cases s <;> rfl

/-! ### The three monad laws for `T_M`

The only declarations with a non-`rfl` shape map (`one_mul`/`mul_one`/`mul_assoc`
and `one_act`/`mul_act`); the position transport is discharged by `heq_pos`. -/

theorem Tright_unit (X : Container) :
    (Tunit W (TObj W X)).comp (Tmult W X) = ContainerMorphism.id (TObj W X) := by
  have hs : ((Tunit W (TObj W X)).comp (Tmult W X)).onShapes
      = (ContainerMorphism.id (TObj W X)).onShapes := by
    funext s
    cases s with
    | inl e => show Sum.inl (W.act W.one e) = Sum.inl e; rw [W.one_act]
    | inr p => cases p with
      | mk a x => show Sum.inr (W.mul W.one a, x) = Sum.inr (a, x); rw [W.one_mul]
  refine ContainerMorphism.ext' hs ?_
  intro s p
  cases s with
  | inl e => exact (eq_of_heq (heq_pos (congrFun hs (Sum.inl e)) p)).symm
  | inr q => cases q with
    | mk a x => exact (eq_of_heq (heq_pos (congrFun hs (Sum.inr (a, x))) p)).symm

theorem Tleft_unit (X : Container) :
    (Tmap W (Tunit W X)).comp (Tmult W X) = ContainerMorphism.id (TObj W X) := by
  have hs : ((Tmap W (Tunit W X)).comp (Tmult W X)).onShapes
      = (ContainerMorphism.id (TObj W X)).onShapes := by
    funext s
    cases s with
    | inl e => rfl
    | inr p => cases p with
      | mk a x => show Sum.inr (W.mul a W.one, x) = Sum.inr (a, x); rw [W.mul_one]
  refine ContainerMorphism.ext' hs ?_
  intro s p
  cases s with
  | inl e => exact (eq_of_heq (heq_pos (congrFun hs (Sum.inl e)) p)).symm
  | inr q => cases q with
    | mk a x => exact (eq_of_heq (heq_pos (congrFun hs (Sum.inr (a, x))) p)).symm

theorem Tassoc (X : Container) :
    (Tmult W (TObj W X)).comp (Tmult W X) = (Tmap W (Tmult W X)).comp (Tmult W X) := by
  have hs : ((Tmult W (TObj W X)).comp (Tmult W X)).onShapes
      = ((Tmap W (Tmult W X)).comp (Tmult W X)).onShapes := by
    funext m
    cases m with
    | inl e => rfl
    | inr p => cases p with
      | mk a y => cases y with
        | inl e' => rfl
        | inr q => cases q with
          | mk a' z => cases z with
            | inl e'' =>
              show Sum.inl (W.act (W.mul a a') e'') = Sum.inl (W.act a (W.act a' e''))
              rw [W.mul_act]
            | inr r => cases r with
              | mk a'' w =>
                show Sum.inr (W.mul (W.mul a a') a'', w) = Sum.inr (W.mul a (W.mul a' a''), w)
                rw [W.mul_assoc]
  refine ContainerMorphism.ext' hs ?_
  intro m p
  cases m with
  | inl e => exact (eq_of_heq (heq_pos (congrFun hs (Sum.inl e)) p)).symm
  | inr pp => cases pp with
    | mk a y => cases y with
      | inl e' => exact (eq_of_heq (heq_pos (congrFun hs (Sum.inr (a, Sum.inl e'))) p)).symm
      | inr q => cases q with
        | mk a' z => cases z with
          | inl e'' =>
            exact (eq_of_heq (heq_pos (congrFun hs (Sum.inr (a, Sum.inr (a', Sum.inl e'')))) p)).symm
          | inr r => cases r with
            | mk a'' w =>
              exact (eq_of_heq
                (heq_pos (congrFun hs (Sum.inr (a, Sum.inr (a', Sum.inr (a'', w))))) p)).symm

/-- `T_M` bundled as an abstract `Monad` on `Cont`. -/
def TAff : Monad Container where
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

/-! ## The reverse compositor `κ : G_M T_M ⇒ T_M G_M`

Identity on shapes. On positions: the empty-product `η^M`-padding
`1 → M 1 = E + A×1` over the nullary `inl` summand (Maybe-style), and the identity
over the unary `inr` summand (Writer-style, both fibres are `M (X.Pos s)`). -/

/-- The compositor `κ_X : G_M (T_M X) ⟶ T_M (G_M X)`. -/
def kappa (X : Container) :
    ContainerMorphism ((GAff W).obj ((TAff W).obj X)) ((TAff W).obj ((GAff W).obj X)) where
  onShapes := id
  onPos := fun s => match s with
    | Sum.inl _ => fun _ => Sum.inr (W.one, PUnit.unit)
    | Sum.inr _ => id

/-! ### The four mixed-distributive-law axioms for `κ`, all discharged for `E + A×(−)` -/

theorem kappa_natural {X Y : Container} (φ : ContainerMorphism X Y) :
    Category.comp ((GAff W).map ((TAff W).map φ)) (kappa W Y)
      = Category.comp (kappa W X) ((TAff W).map ((GAff W).map φ)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m <;> rfl

/-- **E1′** (`distrib_unit`): `G η^T ≫ κ = η^T_{GX}`. -/
theorem kappa_distrib_unit (X : Container) :
    Category.comp ((GAff W).map ((TAff W).η X)) (kappa W X) = (TAff W).η ((GAff W).obj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; rfl
  -- `κ = id` on the unary summand, leaving `M.map id`, which reduces once `p` is split.
  · intro m p; cases p <;> rfl

/-- **E3′** (`distrib_counit`): `κ ≫ T ε = ε_{TX}`. -/
theorem kappa_distrib_counit (X : Container) :
    Category.comp (kappa W X) ((TAff W).map ((GAff W).ε X)) = (GAff W).ε ((TAff W).obj X) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p; cases m <;> rfl

/-- **E2′** (`distrib_mult`): `G μ^T ≫ κ = κ_{TX} ≫ T κ ≫ μ^T_{GX}`. The
branching-obstructed axiom; it holds because the `∏` is over `≤ 1` leaf. -/
theorem kappa_distrib_mult (X : Container) :
    Category.comp ((GAff W).map ((TAff W).μ X)) (kappa W X)
      = Category.comp (Category.comp (kappa W ((TAff W).obj X)) ((TAff W).map (kappa W X)))
          ((TAff W).μ ((GAff W).obj X)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m
    cases m with
    | inl e => rfl
    | inr p => cases p with
      | mk a s => cases s <;> rfl
  · intro m p
    cases m with
    | inl e => rfl
    | inr q => cases q with
      | mk a s => cases s with
        | inl e' => rfl
        | inr r => cases r with
          -- deepest unary/unary shape: `κ = id` throughout, `M.map id` reduces on `p`.
          | mk a' t => cases p <;> rfl

/-- **E4′** (`distrib_comult`): `κ ≫ T δ = δ_{TX} ≫ G κ ≫ κ_{GX}`. -/
theorem kappa_distrib_comult (X : Container) :
    Category.comp (kappa W X) ((TAff W).map ((GAff W).δ X))
      = Category.comp (Category.comp ((GAff W).δ ((TAff W).obj X)) ((GAff W).map (kappa W X)))
          (kappa W ((GAff W).obj X)) := by
  refine ContainerMorphism.ext' ?_ ?_
  · funext m; cases m <;> rfl
  · intro m p
    cases m with
    | inl e =>
      -- Nullary summand: both sides collapse to the `η^M`-padding, but the RHS
      -- multiplies `one · one` via `μ^M`, so this is `one_mul`, not `rfl`.
      show (Sum.inr (W.one, PUnit.unit) : W.E ⊕ W.A × PUnit)
         = Sum.inr (W.mul W.one W.one, PUnit.unit)
      rw [W.one_mul]
    | inr q => cases q with
      | mk a s =>
        -- Unary summand: `κ = id`, and `M.map id` reduces once the position is
        -- split, so each case is `rfl`.
        cases p with
        | inl e0 => rfl
        | inr pp => cases pp with
          | mk a' y => cases y with
            | inl e' => rfl
            | inr r => cases r with
              | mk a'' w => rfl

/-- The **mixed distributive law** `κ : G_M T_M ⇒ T_M G_M`, bundling the four
axioms above. Machine-checked witness that E2′ holds for the *entire*
non-branching class `E + A×(−)`. -/
def mixedDistrib : MixedDistrib (GAff W) (TAff W) where
  κ := kappa W
  κ_natural := fun f => kappa_natural W f
  distrib_unit := kappa_distrib_unit W
  distrib_counit := kappa_distrib_counit W
  distrib_mult := kappa_distrib_mult W
  distrib_comult := kappa_distrib_comult W

/-! ## The effect–coeffect arrow category for `E + A×(−)`

Specialising the abstract biKleisli laws of `Containers.MixedDistrib` at
`mixedDistrib` gives the three category laws for the arrows `G_M p ⟶ T_M q`.
Associativity consumes E2′ — machine-checked above for the *whole class* — so this
is a fully verified *associative* effect–coeffect arrow category for every
writer-with-absorbing-exceptions monad. -/

/-- **Identity law (left)** for the `E + A×(−)` arrow category. -/
theorem arr_unit_left {p q : Container} (g : (mixedDistrib W).Hom p q) :
    (mixedDistrib W).acomp ((mixedDistrib W).arrId p) g = g :=
  (mixedDistrib W).unit_left g

/-- **Identity law (right)** for the `E + A×(−)` arrow category. -/
theorem arr_unit_right {p q : Container} (f : (mixedDistrib W).Hom p q) :
    (mixedDistrib W).acomp f ((mixedDistrib W).arrId q) = f :=
  (mixedDistrib W).unit_right f

/-- **Associativity** of composition in the `E + A×(−)` arrow category — the E2′
payload, holding because the whole class is non-branching. -/
theorem arr_assoc {p q r s : Container}
    (f : (mixedDistrib W).Hom p q) (g : (mixedDistrib W).Hom q r)
    (h : (mixedDistrib W).Hom r s) :
    (mixedDistrib W).acomp ((mixedDistrib W).acomp f g) h
      = (mixedDistrib W).acomp f ((mixedDistrib W).acomp g h) :=
  (mixedDistrib W).acomp_assoc f g h

end

/-! ## A concrete `|E| ≥ 2, |A| ≥ 2` witness

Instantiating at `A = ℤ/2` (`Bool`/`xor`), `E = Bool`, trivial action — the
`|E| = 2, |A| = 2` case flagged in `PROVE.md` — gives the explicit machine-checked
associative arrow category for a genuine two-exception, two-log writer. -/

/-- `M X = 2 + (ℤ/2)×X`: `A = Bool` with `xor`, `E = Bool`, trivial action. All
laws close by `cases`/`decide`. -/
def Z2E2 : Aff where
  A := Bool
  E := Bool
  one := false
  mul := xor
  act := fun _ e => e
  one_mul := fun a => by cases a <;> rfl
  mul_one := fun a => by cases a <;> rfl
  mul_assoc := fun a b c => by cases a <;> cases b <;> cases c <;> rfl
  one_act := fun _ => rfl
  mul_act := fun _ _ _ => rfl

/-- The associativity law for the `2 + (ℤ/2)×(−)` arrow category — the concrete
`E2′` witness for the fused non-branching class. -/
theorem arr_assoc_Z2E2 {p q r s : Container}
    (f : (mixedDistrib Z2E2).Hom p q) (g : (mixedDistrib Z2E2).Hom q r)
    (h : (mixedDistrib Z2E2).Hom r s) :
    (mixedDistrib Z2E2).acomp ((mixedDistrib Z2E2).acomp f g) h
      = (mixedDistrib Z2E2).acomp f ((mixedDistrib Z2E2).acomp g h) :=
  arr_assoc Z2E2 f g h

end BiKleisliAffine
end Containers
