import Containers.EndpointLocality
import Containers.ReaderGroupoidLifting

/-!
# The ℤ/2-holonomy witness: a machine-checked refutation of "liftings are holonomy-free"

This file certifies the **dual** of `Containers.EndpointLocality` (the *collapse
engine*: a functor out of the codiscrete category is a trivial iso-system, so a
classification factoring through it collapses to one object, `π₀ = 1`). Here we
exhibit a classifier whose transport does **not** factor through a codiscrete
category, and show the classification genuinely **refuses to collapse** — the
holonomy survives.

## Background (MacBeth PROVE `2026-08-11-update-monad-liftings-holonomy-full.md`)

The general-`M` liftings of the update monad `Upd_{(S,P,↓)}` are **holonomy-full**:
they are equivalent to `Fun(𝔸(↓), Cat)`, where `𝔸(↓)` is the *action category*
of `↓ : P ↷ S`. The decisive counterexample: `P = ℤ/2` acting **trivially** on a
single free orbit gives `𝔸 = Bℤ/2` — the **one-object** category whose hom-monoid
is the group `ℤ/2`. A functor `Bℤ/2 ⥤ Cat` is exactly a `ℤ/2`-action on a
category, and there are `≥ 2` non-isomorphic such liftings: the **trivial** action
and the **swap** action are not naturally isomorphic. This is precisely why `π₀`
is *not* the invariant (Reader has `π₀ = 2 → 1` transport, but trivial-`ℤ/2` has
`π₀ = 2 → 4` liftings).

## What is certified here

1. `BZ2` — the one-object category `Bℤ/2` (`Obj = Unit`, `Hom = ℤ/2`,
   composition = group multiplication). Its category laws **are** the group axioms
   of `ℤ/2` (`Z2.mul_e_left`/`_right`/`_assoc`, reused from
   `Containers.ReaderGroupoidLifting`). This is `𝔸(↓)` for a single free orbit.
2. `DiscreteBool` — the two-object discrete category on `Bool` (the target `D`);
   `idF` and `swapF : D ⥤ D` — the identity self-functor and the **swap** induced
   by `Bool.not`. `swapF` is a genuine involutive automorphism (`swapF_involutive`:
   `not (not b) = b`), so both
   * `actTriv` — the **trivial** `ℤ/2`-action (`F_triv : Bℤ/2 ⥤ Cat`), and
   * `actSwap` — the **swap** action (`F_swap`), sending the generator to `swapF`,
   are honest functors: their only nontrivial functor law, `g·g ↦ swap∘swap = id`,
   is exactly the involution (`actSwap_mul_obj`).
3. **The refutation payoff** (`no_natTrans_triv_to_swap`): there is **no natural
   transformation** `F_triv ⟹ F_swap` — a fortiori no natural isomorphism
   (`no_natIso_triv_swap`). A component would be a self-functor `α` of `D` with
   `α ≫ F_swap(g) = F_triv(g) ≫ α`, i.e. `swap ∘ α = α`, forcing on objects
   `not (α b) = α b` — impossible in `Bool`. So the two liftings over the **same**
   action category `Bℤ/2` are genuinely distinct: the classification does not
   collapse.
4. **Contrast with the collapse engine** (`BZ2_hom_not_subsingleton`): `Bℤ/2` is
   **not** codiscrete — its endo-hom-monoid `ℤ/2` has two distinct elements, not a
   `PUnit`. That is exactly why `EndpointLocality.collapse` (which needs *unique*
   parallel arrows) does not apply and the holonomy survives.

Everything is `Type`-level Lean 4 core, no Mathlib, no `sorry`. `DiscreteBool`'s
hom-sets are `PLift`s of `Prop`s, so definitional proof irrelevance keeps every
category/functor law clean; the non-iso step is an elementary `cases` on `Bool`.

Reference: MacBeth PROVE `proofs/2026-08-11-update-monad-liftings-holonomy-full.md`
(§4, the `Bℤ/2` counterexample); DCont ≅ Cat is Ahman–Chapman–Uustalu,
arXiv:1408.5809; the action-category picture is Ahman–Uustalu, *Directed
containers as categories* (2016). Dual to `Containers.EndpointLocality`.
-/

namespace Containers

open ReaderGroupoid

namespace SmallCat

/-- The **identity functor** on a small category. All three laws are `rfl`. -/
def Functor.id (C : SmallCat) : Functor C C where
  obj a := a
  map f := f
  map_id _ := rfl
  map_comp _ _ := rfl

/-- **Composition** of small-category functors, in diagrammatic order (`F.comp G`
travels along `F` first, then `G`). -/
def Functor.comp {C D E : SmallCat} (F : Functor C D) (G : Functor D E) :
    Functor C E where
  obj a := G.obj (F.obj a)
  map f := G.map (F.map f)
  map_id a := by rw [F.map_id, G.map_id]
  map_comp f h := by rw [F.map_comp, G.map_comp]

end SmallCat

namespace HolonomyWitness

/-! ## 1. `Bℤ/2` — the action category `𝔸(↓)` for a single free ℤ/2 orbit

One object, hom-monoid the group `ℤ/2`; the category laws are literally the group
axioms (reused from `ReaderGroupoidLifting`). This is the base of the functor
`Bℤ/2 ⥤ Cat` whose two points refuse to collapse. -/

/-- The one-object category `Bℤ/2`: `Obj = Unit`, `Hom = ℤ/2`, composition the
group multiplication `Z2.mul`. Unit laws = `Z2.mul_e_left`/`_right`; associativity
= `Z2.mul_assoc`. -/
def BZ2 : SmallCat where
  Obj := Unit
  Hom _ _ := Z2
  id _ := Z2.e
  comp p q := Z2.mul p q
  id_comp f := Z2.mul_e_left f
  comp_id f := Z2.mul_e_right f
  assoc p q r := Z2.mul_assoc p q r

/-! ## 2. The target `D = DiscreteBool` and the two self-functors

`DiscreteBool` has objects `Bool` and a **unique** morphism `a ⟶ b` exactly when
`a = b` (`Hom a b := PLift (a = b)`), so it is the two-object discrete category.
Because hom-sets are `PLift`s of `Prop`s, definitional proof irrelevance makes all
category and functor laws `rfl`. -/

/-- The two-object **discrete** category on `Bool`. -/
def DiscreteBool : SmallCat where
  Obj := Bool
  Hom a b := PLift (a = b)
  id _ := ⟨rfl⟩
  comp f g := ⟨f.down.trans g.down⟩
  id_comp _ := rfl
  comp_id _ := rfl
  assoc _ _ _ := rfl

/-- The **identity** self-functor `D ⥤ D` (image of the generator under the
trivial `ℤ/2`-action). -/
def idF : SmallCat.Functor DiscreteBool DiscreteBool := SmallCat.Functor.id DiscreteBool

/-- The **swap** self-functor `D ⥤ D`: `Bool.not` on objects, transported on the
(proof-irrelevant) morphisms. This is the nontrivial `ℤ/2`-automorphism of `D`. -/
def swapF : SmallCat.Functor DiscreteBool DiscreteBool where
  obj := Bool.not
  map h := ⟨congrArg Bool.not h.down⟩
  map_id _ := rfl
  map_comp _ _ := rfl

/-- **`swapF` is an involution:** `not (not b) = b`. This single equation is the
only nontrivial functor law of `F_swap` (it certifies `g·g ↦ swap∘swap = id`), and
is what makes `swapF` a genuine automorphism of the target category. -/
theorem swapF_involutive (b : Bool) : swapF.obj (swapF.obj b) = b := by
  cases b <;> rfl

/-! ## 3. The two liftings `F_triv, F_swap : Bℤ/2 ⥤ Cat`

A functor `Bℤ/2 ⥤ Cat` is a `ℤ/2`-action on a category: the generator `g` is sent
to a self-functor, subject to `g·g = e ↦ (that functor)² = id`. We give the two
actions on `D = DiscreteBool` and certify their functor laws pointwise on objects
(the morphism level is proof-irrelevant). -/

/-- `F_triv`: the **trivial** `ℤ/2`-action — every group element acts as `id`. -/
def actTriv : Z2 → SmallCat.Functor DiscreteBool DiscreteBool := fun _ => idF

/-- `F_swap`: the **swap** action — the identity `e` acts as `id`, the generator
`g` acts as `swapF`. -/
def actSwap : Z2 → SmallCat.Functor DiscreteBool DiscreteBool
  | Z2.e => idF
  | Z2.g => swapF

/-- Functor law for `F_triv` on the unit: `F_triv(e) = id`. -/
theorem actTriv_e : actTriv Z2.e = idF := rfl

/-- Functor law for `F_triv` on composites, pointwise on objects:
`F_triv(z·w) = F_triv(z) ∘ F_triv(w)` (trivially, everything is `id`). -/
theorem actTriv_mul_obj (z w : Z2) (b : Bool) :
    (actTriv (Z2.mul z w)).obj b = ((actTriv z).comp (actTriv w)).obj b := rfl

/-- Functor law for `F_swap` on the unit: `F_swap(e) = id`. -/
theorem actSwap_e : actSwap Z2.e = idF := rfl

/-- Functor law for `F_swap` on composites, pointwise on objects:
`F_swap(z·w) = F_swap(z) ∘ F_swap(w)`. The only non-formal case is `(g, g)`, where
it is exactly the involution `swap ∘ swap = id`; all four cases close by `cases`
on the object. -/
theorem actSwap_mul_obj (z w : Z2) (b : Bool) :
    (actSwap (Z2.mul z w)).obj b = ((actSwap z).comp (actSwap w)).obj b := by
  cases z <;> cases w <;> cases b <;> rfl

/-! ## 4. Natural transformations and the refutation

A natural transformation between two `ℤ/2`-actions on `D` is a self-functor
`component : D ⥤ D` making every naturality square commute. The refutation: no
such transformation exists from `F_triv` to `F_swap`. -/

/-- A **natural transformation** `F ⟹ G` between two `ℤ/2`-actions on
`DiscreteBool` (i.e. two functors `Bℤ/2 ⥤ Cat` landing on `D`): a component
self-functor together with the naturality square for every group element `z`
(diagrammatic: `component ≫ G(z) = F(z) ≫ component`). -/
structure NatTrans (act act' : Z2 → SmallCat.Functor DiscreteBool DiscreteBool) where
  component : SmallCat.Functor DiscreteBool DiscreteBool
  naturality : ∀ z : Z2, component.comp (act' z) = (act z).comp component

/-- A **natural isomorphism** `F ≅ G` in particular carries an underlying natural
transformation `F ⟹ G`. (We need only this projection to refute existence, so the
inverse/coherence data is omitted.) -/
structure NatIso (act act' : Z2 → SmallCat.Functor DiscreteBool DiscreteBool) where
  hom : NatTrans act act'

/-- **The refutation.** There is **no** natural transformation `F_triv ⟹ F_swap`.

A component `α` would satisfy naturality at the generator `g`:
`α ≫ F_swap(g) = F_triv(g) ≫ α`, i.e. `swap ∘ α = α` (as `F_triv(g) = id`).
Evaluating on the object `false` gives `not (α.obj false) = α.obj false`, which no
`Bool` satisfies. Hence the two liftings over the common action category `Bℤ/2`
are genuinely distinct — the classification does **not** collapse. -/
theorem no_natTrans_triv_to_swap : NatTrans actTriv actSwap → False :=
  fun t => by
    have hobj : Bool.not (t.component.obj false) = t.component.obj false :=
      congrArg (fun F : SmallCat.Functor DiscreteBool DiscreteBool => F.obj false)
        (t.naturality Z2.g)
    revert hobj
    cases t.component.obj false <;> intro hobj <;> exact Bool.noConfusion hobj

/-- **Not naturally isomorphic.** A natural isomorphism would supply a natural
transformation `F_triv ⟹ F_swap`, which `no_natTrans_triv_to_swap` forbids. -/
theorem no_natIso_triv_swap : NatIso actTriv actSwap → False :=
  fun i => no_natTrans_triv_to_swap i.hom

/-! ## 5. Contrast with the collapse engine

`Containers.EndpointLocality.collapse` collapses any classification factoring
through the **codiscrete** category `Codiscrete S` (unique parallel arrows,
`Hom = PUnit`). `Bℤ/2` violates that hypothesis: its endo-hom-monoid is the group
`ℤ/2`, which has two distinct elements. This is *why* the holonomy survives. -/

/-- `Bℤ/2` is **not** codiscrete: its (unique-object) hom-set has two distinct
morphisms `e ≠ g`, so the `EndpointLocality` collapse — which requires unique
parallel arrows — does not apply. -/
theorem BZ2_hom_not_subsingleton : ∃ a b : BZ2.Hom () (), a ≠ b :=
  ⟨Z2.e, Z2.g, Z2.e_ne_g⟩

/-! ## 6. The packaged witness -/

/-- **`holonomy_survives`.** The clean deliverable: over the single action category
`Bℤ/2`, the swap lifting is a genuine functor `Bℤ/2 ⥤ Cat` (its only nontrivial
law `swap∘swap = id` holds, `swapF_involutive`), yet it admits **no** natural
transformation from the trivial lifting (`no_natTrans_triv_to_swap`), hence they
are non-isomorphic; and this is possible precisely because `Bℤ/2` is *not*
codiscrete (`BZ2_hom_not_subsingleton`) — the dual of the `EndpointLocality`
collapse. -/
theorem holonomy_survives :
    (∀ b : Bool, swapF.obj (swapF.obj b) = b)
      ∧ (NatTrans actTriv actSwap → False)
      ∧ (∃ a b : BZ2.Hom () (), a ≠ b) :=
  ⟨swapF_involutive, no_natTrans_triv_to_swap, Z2.e, Z2.g, Z2.e_ne_g⟩

end HolonomyWitness

end Containers
