import Containers.Cont
import Containers.MonadComonadTransfer

/-!
# The biKleisli category of a mixed distributive law, and its unit laws

This file formalises the **abstract skeleton** of the effect–coeffect *arrow*
composition of `proofs/2026-07-29-effect-coeffect-arrows.md` (MacBeth, PROVE
session 2026-07-29), §1–2.

Given a category `𝒞`, a **comonad** `G = (G, ε, δ)` and a **monad**
`T = (T, η, μ)` on `𝒞`, and a **mixed distributive law**
`κ : G T ⇒ T G` satisfying the four axioms E1′–E4′ (two for the monad, two for
the comonad structure), the **effect–coeffect arrows** `p ⇝ q := 𝒞(G p, T q)`
form a category — the *biKleisli* (= coKleisli-of-Kleisli) category
(Power–Watanabe, *Combining a monad and a comonad*, TCS 280 (2002), §3;
Uustalu–Vene, *Comonadic notions of computation*, 2008). Identity is
`ε ≫ η : G p → p → T p`; composition of `f : G p → T q` and `g : G q → T r` is
$$
G p \xrightarrow{\delta} G G p \xrightarrow{G f} G T q
    \xrightarrow{\kappa} T G q \xrightarrow{T g} T T r \xrightarrow{\mu} T r .
$$

## What is proved here (the deliverable)

* `BiKleisli.unit_left`  : `acomp (arrId p) g = g` — the paper's **E1′** law;
* `BiKleisli.unit_right` : `acomp f (arrId q) = f` — the paper's **E3′** law.

Both hold for **every** `M` in the effect–coeffect application, because — as the
proofs below make explicit — they consume only the comonad counit laws, the
monad unit laws, the naturality of `ε` and `η`, and the two *unit* distributive
axioms `distrib_unit` (E1′) and `distrib_counit` (E3′). They do **not** touch the
`μ`/`δ` axioms. This is exactly why `proofs/2026-07-29-…` reports the unit laws
as the *unconditional* part of the arrow calculus (holding for all `M`), while
associativity (E2′, `distrib_mult`) is the *branching-obstructed* part.

Associativity (`MixedDistrib.acomp_assoc`) is also proved, from the full axiom set. In the
container application the four axioms hold for `G = G_M` (the transfer comonad,
`Containers.MonadComonadTransfer`, already Lean-verified) together with the
Ahman–Bauer effect monad `T_M` (arXiv:2409.17664, Thm 6.3) and the *reverse*
entwining `κ : G_M T_M ⇒ T_M G_M` **iff `M` is non-branching** (the 07-27
dichotomy, machine-checked in `scratch/monad-comonad-transfer/entwine.py`).
Hence: *this abstract theorem discharges the "(1)⇔(3)" step of the paper's
Theorem A; the "(3)⇔(4) non-branching" step is the separate computational
result, not formalised here.* Concretely constructing `T_M`/`κ` (the
∏-cointerpretation leaf apparatus) is the next Lean increment.

Everything is stated over the self-contained `Containers.Category` typeclass
(Mathlib-free), so it instantiates at `𝒞 = Cont` — or any category. Composition
is diagrammatic (`Category.comp f g` is "`f` then `g`"), matching
`Containers.Cont`.
-/

namespace Containers

universe u v

variable {Obj : Type u} [Category Obj]

local infixr:80 " ⊚ " => Category.comp

/-! ## Comonad, monad, and mixed distributive law over an abstract category -/

/-- A **comonad** on a `Category`: an endofunctor with counit `ε` and
comultiplication `δ`, their naturality squares, and the three comonad laws in
the same diagrammatic form as `Containers.SetMonad`'s dual. -/
structure Comonad (Obj : Type u) [Category Obj] where
  /-- Object map of the endofunctor `G`. -/
  obj : Obj → Obj
  /-- Morphism map of `G`. -/
  map : {X Y : Obj} → Category.Hom X Y → Category.Hom (obj X) (obj Y)
  /-- `G` preserves identities. -/
  map_id : ∀ (X : Obj), map (Category.id X) = Category.id (obj X)
  /-- `G` preserves composition. -/
  map_comp : ∀ {X Y Z : Obj} (f : Category.Hom X Y) (g : Category.Hom Y Z),
    map (Category.comp f g) = Category.comp (map f) (map g)
  /-- The counit `ε : G X ⟶ X`. -/
  ε : (X : Obj) → Category.Hom (obj X) X
  /-- The comultiplication `δ : G X ⟶ G G X`. -/
  δ : (X : Obj) → Category.Hom (obj X) (obj (obj X))
  /-- Naturality of `ε`: `G f ≫ ε_Y = ε_X ≫ f`. -/
  ε_natural : ∀ {X Y : Obj} (f : Category.Hom X Y),
    Category.comp (map f) (ε Y) = Category.comp (ε X) f
  /-- Naturality of `δ`: `G f ≫ δ_Y = δ_X ≫ G G f`. -/
  δ_natural : ∀ {X Y : Obj} (f : Category.Hom X Y),
    Category.comp (map f) (δ Y) = Category.comp (δ X) (map (map f))
  /-- Counit-left: `δ ≫ ε_{GX} = id`. -/
  counit_left : ∀ (X : Obj), Category.comp (δ X) (ε (obj X)) = Category.id (obj X)
  /-- Counit-right: `δ ≫ G ε = id`. -/
  counit_right : ∀ (X : Obj), Category.comp (δ X) (map (ε X)) = Category.id (obj X)
  /-- Coassociativity: `δ ≫ δ_{GX} = δ ≫ G δ`. -/
  coassoc : ∀ (X : Obj),
    Category.comp (δ X) (δ (obj X)) = Category.comp (δ X) (map (δ X))

/-- A **monad** on a `Category`, dual to `Comonad`; the same data as
`Containers.SetMonad` but relative to an abstract base category. -/
structure Monad (Obj : Type u) [Category Obj] where
  /-- Object map of the endofunctor `T`. -/
  obj : Obj → Obj
  /-- Morphism map of `T`. -/
  map : {X Y : Obj} → Category.Hom X Y → Category.Hom (obj X) (obj Y)
  /-- `T` preserves identities. -/
  map_id : ∀ (X : Obj), map (Category.id X) = Category.id (obj X)
  /-- `T` preserves composition. -/
  map_comp : ∀ {X Y Z : Obj} (f : Category.Hom X Y) (g : Category.Hom Y Z),
    map (Category.comp f g) = Category.comp (map f) (map g)
  /-- The unit `η : X ⟶ T X`. -/
  η : (X : Obj) → Category.Hom X (obj X)
  /-- The multiplication `μ : T T X ⟶ T X`. -/
  μ : (X : Obj) → Category.Hom (obj (obj X)) (obj X)
  /-- Naturality of `η`: `f ≫ η_Y = η_X ≫ T f`. -/
  η_natural : ∀ {X Y : Obj} (f : Category.Hom X Y),
    Category.comp f (η Y) = Category.comp (η X) (map f)
  /-- Naturality of `μ`: `T T f ≫ μ_Y = μ_X ≫ T f`. -/
  μ_natural : ∀ {X Y : Obj} (f : Category.Hom X Y),
    Category.comp (map (map f)) (μ Y) = Category.comp (μ X) (map f)
  /-- Right-unit: `η_{TX} ≫ μ = id`. -/
  right_unit : ∀ (X : Obj), Category.comp (η (obj X)) (μ X) = Category.id (obj X)
  /-- Left-unit: `T η ≫ μ = id`. -/
  left_unit : ∀ (X : Obj), Category.comp (map (η X)) (μ X) = Category.id (obj X)
  /-- Associativity: `μ_{TX} ≫ μ = T μ ≫ μ`. -/
  assoc : ∀ (X : Obj),
    Category.comp (μ (obj X)) (μ X) = Category.comp (map (μ X)) (μ X)

/-- A **mixed distributive law** `κ : G T ⇒ T G` of a comonad `G` over a monad
`T`, with the four axioms E1′–E4′ of `proofs/2026-07-29-effect-coeffect-arrows.md`
§1.  Diagrammatic composition throughout. -/
structure MixedDistrib (G : Comonad Obj) (T : Monad Obj) where
  /-- The compositor `κ_X : G (T X) ⟶ T (G X)`. -/
  κ : (X : Obj) → Category.Hom (G.obj (T.obj X)) (T.obj (G.obj X))
  /-- Naturality of `κ`: `G (T f) ≫ κ_Y = κ_X ≫ T (G f)`. -/
  κ_natural : ∀ {X Y : Obj} (f : Category.Hom X Y),
    Category.comp (G.map (T.map f)) (κ Y) = Category.comp (κ X) (T.map (G.map f))
  /-- **E1′** (unit of `T`): `G η ≫ κ = η_{GX}`. -/
  distrib_unit : ∀ (X : Obj),
    Category.comp (G.map (T.η X)) (κ X) = T.η (G.obj X)
  /-- **E3′** (counit of `G`): `κ ≫ T ε = ε_{TX}`. -/
  distrib_counit : ∀ (X : Obj),
    Category.comp (κ X) (T.map (G.ε X)) = G.ε (T.obj X)
  /-- **E2′** (multiplication of `T`): `G μ ≫ κ = κ_{TX} ≫ T κ ≫ μ_{GX}`. This is
  the branching-obstructed axiom (holds iff `M` non-branching in the container
  application). -/
  distrib_mult : ∀ (X : Obj),
    Category.comp (G.map (T.μ X)) (κ X)
      = Category.comp (Category.comp (κ (T.obj X)) (T.map (κ X))) (T.μ (G.obj X))
  /-- **E4′** (comultiplication of `G`): `κ ≫ T δ = δ_{TX} ≫ G κ ≫ κ_{GX}`. -/
  distrib_comult : ∀ (X : Obj),
    Category.comp (κ X) (T.map (G.δ X))
      = Category.comp (Category.comp (G.δ (T.obj X)) (G.map (κ X))) (κ (G.obj X))

namespace MixedDistrib

variable {G : Comonad Obj} {T : Monad Obj} (D : MixedDistrib G T)

/-! ## The biKleisli category -/

/-- An **effect–coeffect arrow** `p ⇝ q` is a morphism `G p ⟶ T q`. (The `D`
argument is carried only so that dot notation `D.Hom` resolves; the hom-set
itself depends on `G, T` alone.) -/
def Hom (_D : MixedDistrib G T) (p q : Obj) : Type v := Category.Hom (G.obj p) (T.obj q)

/-- The **identity arrow** `p ⇝ p`: `G p --ε--> p --η--> T p`. -/
def arrId (p : Obj) : D.Hom p p := (G.ε p) ⊚ (T.η p)

/-- **biKleisli composition** of `f : p ⇝ q` and `g : q ⇝ r`:
`δ ≫ G f ≫ κ ≫ T g ≫ μ`. -/
def acomp {p q r : Obj} (f : D.Hom p q) (g : D.Hom q r) : D.Hom p r :=
  (G.δ p) ⊚ (G.map f) ⊚ (D.κ q) ⊚ (T.map g) ⊚ (T.μ r)

/-! ## The unit laws — the unconditional deliverable

Both proofs are diagram chases that use **only** the comonad counit laws, the
monad unit laws, naturality of `ε`/`η`, and the two *unit* distributive axioms
`distrib_unit` (E1′) and `distrib_counit` (E3′). Neither touches E2′/E4′, which
is precisely why the paper reports the unit laws as holding for *all* `M`. -/

/-- **Left unit law** `acomp (arrId p) g = g` — the paper's **E1′**.

Chase: `G (arrId p) = G ε ≫ G η`; `δ ≫ G ε = id` (counit-right) collapses the
front; `G η ≫ κ = η_{Gp}` (E1′/`distrib_unit`) rewrites the next step; `η`
naturality slides `g` out; `η_{Tq} ≫ μ = id` (monad right-unit) finishes. -/
theorem unit_left {p q : Obj} (g : D.Hom p q) : D.acomp (D.arrId p) g = g := by
  unfold acomp arrId
  -- Expand `G (ε ≫ η)` = `G ε ≫ G η`, then fully right-associate.
  rw [G.map_comp]
  simp only [Category.assoc]
  -- `δ ⊚ G ε = id` (counit-right) collapses the front.
  rw [← Category.assoc (G.δ p) (G.map (G.ε p)), G.counit_right p, Category.id_comp]
  -- `G η ⊚ κ = η_{Gp}` (E1′).
  rw [← Category.assoc (G.map (T.η p)) (D.κ p), D.distrib_unit p]
  -- `η_{Gp} ⊚ T g = g ⊚ η_{Tq}` (η naturality), then `η_{Tq} ⊚ μ = id`.
  rw [← Category.assoc (T.η (G.obj p)) (T.map g), ← T.η_natural g,
      Category.assoc g (T.η (T.obj q)) (T.μ q), T.right_unit q, Category.comp_id]

/-- **Right unit law** `acomp f (arrId q) = f` — the paper's **E3′**.

Chase: `T (arrId q) = T ε ≫ T η`; `κ ≫ T ε = ε_{Tq}` (E3′/`distrib_counit`);
`T η ≫ μ = id` (monad left-unit) drops the tail; `ε` naturality slides `f` out;
`δ ≫ ε_{Gp} = id` (counit-left) finishes. -/
theorem unit_right {p q : Obj} (f : D.Hom p q) : D.acomp f (D.arrId q) = f := by
  unfold acomp arrId
  -- Expand `T (ε ≫ η)` = `T ε ≫ T η`, then fully right-associate.
  rw [T.map_comp]
  simp only [Category.assoc]
  -- `κ ⊚ T ε = ε_{Tq}` (E3′) collapses the tail head.
  rw [← Category.assoc (D.κ q) (T.map (G.ε q)), D.distrib_counit q]
  -- `T η ⊚ μ = id` (monad left-unit) drops the remaining tail.
  rw [T.left_unit q, Category.comp_id]
  -- Now: `δ ⊚ (G f ⊚ ε_{Tq})`. `ε` naturality: `G f ⊚ ε_{Tq} = ε_{Gp} ⊚ f`.
  rw [G.ε_natural f]
  -- `δ ⊚ ε_{Gp} = id` (counit-left).
  rw [← Category.assoc (G.δ p) (G.ε (G.obj p)) f, G.counit_left p, Category.id_comp]

/-! ## Associativity — the branching-obstructed deliverable

Unlike the unit laws, this chase uses the **full** axiom set: `distrib_mult`
(E2′) and `distrib_comult` (E4′), together with the comonad coassociativity, the
monad associativity, and the naturality of `δ`, `μ`, and `κ`. In the container
application E2′ holds **iff `M` is non-branching**, so this is exactly the law
that fails for branching effects (`Pf`, `List`); cf.
`proofs/2026-07-29-effect-coeffect-arrows.md`, Theorem A. -/

/-- **Associativity of biKleisli composition**, from the full axiom set E1′–E4′.

The chase (writing `⊚` for diagrammatic composition):
`acomp (acomp f g) h` normalises to
`δ ⊚ Gδ ⊚ GGf ⊚ Gκ ⊚ GTg ⊚ Gμ ⊚ κ ⊚ Th ⊚ μ`, and `acomp f (acomp g h)` to
`δ ⊚ Gf ⊚ κ ⊚ Tδ ⊚ TGg ⊚ Tκ ⊚ TTh ⊚ Tμ ⊚ μ`. Seven rewrites bridge them:
E2′ (`distrib_mult` at `r`), `μ`-naturality (at `h`), monad `assoc` (at `s`),
comonad `coassoc` (at `p`), `δ`-naturality (at `f`), E4′ (`distrib_comult` at
`q`), and finally `κ`-naturality (at `g`). -/
theorem acomp_assoc {p q r s : Obj}
    (f : D.Hom p q) (g : D.Hom q r) (h : D.Hom r s) :
    D.acomp (D.acomp f g) h = D.acomp f (D.acomp g h) := by
  unfold acomp
  rw [G.map_comp, G.map_comp, G.map_comp, G.map_comp,
      T.map_comp, T.map_comp, T.map_comp, T.map_comp]
  simp only [Category.assoc]
  -- Step 1 (E2′ at r): `Gμ_r ⊚ κ_r = κ_{Tr} ⊚ Tκ_r ⊚ μ_{Gr}`.
  rw [← Category.assoc (G.map (T.μ r)) (D.κ r), D.distrib_mult r]
  simp only [Category.assoc]
  -- Step 2 (μ-naturality at h): `μ_{Gr} ⊚ Th = TTh ⊚ μ_{Ts}`.
  rw [← Category.assoc (T.μ (G.obj r)) (T.map h), ← T.μ_natural h]
  simp only [Category.assoc]
  -- Step 3 (monad assoc at s): `μ_{Ts} ⊚ μ_s = Tμ_s ⊚ μ_s` (terminal pair).
  rw [T.assoc s]
  -- Step 4 (comonad coassoc at p): `δ_p ⊚ Gδ_p = δ_p ⊚ δ_{Gp}`.
  rw [← Category.assoc (G.δ p) (G.map (G.δ p)), ← G.coassoc p]
  simp only [Category.assoc]
  -- Step 5 (δ-naturality at f): `δ_{Gp} ⊚ GGf = Gf ⊚ δ_{Tq}`.
  rw [← Category.assoc (G.δ (G.obj p)) (G.map (G.map f)), ← G.δ_natural f]
  simp only [Category.assoc]
  -- Step 6 (E4′ at q): rewrite the RHS's `κ_q ⊚ Tδ_q = δ_{Tq} ⊚ Gκ_q ⊚ κ_{Gq}`.
  rw [← Category.assoc (D.κ q) (T.map (G.δ q)), D.distrib_comult q]
  simp only [Category.assoc]
  -- Step 7 (κ-naturality at g): `GTg ⊚ κ_{Tr} = κ_{Gq} ⊚ TGg`.
  rw [← Category.assoc (G.map (T.map g)) (D.κ (T.obj r)), D.κ_natural g]
  simp only [Category.assoc]

end MixedDistrib

/-! ## The transfer comonad `G_M` as a `Comonad`

The comonad slot of the effect–coeffect arrow is the transfer comonad
`G_M (S, P) = (S, M ∘ P)` of `Containers.MonadComonadTransfer` — already
Lean-verified (all comonad laws `[Quot.sound]`-only). We repackage its
theorems as a `Comonad Container` so the abstract biKleisli machinery above
applies to it directly. -/

/-- The transfer comonad `G_M` of a `SetMonad`, bundled as an abstract
`Comonad` on `Cont`. Every field is one of the already-proved theorems of
`Containers.SetMonad` (paper: `proofs/2026-07-25-monad-comonad-transfer.md`;
Niu–Spivak arXiv:2312.00990 Prop. 6.57). -/
def SetMonad.toComonad (M : SetMonad) : Comonad Container where
  obj := M.G
  map := M.onMor
  map_id := M.onMor_id
  map_comp := fun f g => M.onMor_comp f g
  ε := M.counit
  δ := M.comult
  ε_natural := fun f => M.counit_natural f
  δ_natural := fun f => M.comult_natural f
  counit_left := M.counit_left
  counit_right := M.counit_right
  coassoc := M.coassoc

/-! ## The coKleisli category of a comonad (the `T = Id`, coeffect-only slice)

Taking the effect monad `T := Id` collapses the compositor to the identity and
makes E2′ vacuous, so the biKleisli category exists for *every* comonad — this
is the coeffect-only corner of `proofs/2026-07-29-effect-coeffect-arrows.md`
§3.1 (the "Workers are the `T = Id` slice" anchor; cf.
`Containers.Workers`). Here we exhibit it as a `MixedDistrib` instance and prove
the full set of category laws, so that in particular the coKleisli category of
the transfer comonad `G_M` is a genuine category. -/

/-- The **identity monad** on any category. -/
def Monad.identity (Obj : Type u) [Category Obj] : Monad Obj where
  obj := fun X => X
  map := fun f => f
  map_id := fun _ => rfl
  map_comp := fun _ _ => rfl
  η := fun X => Category.id X
  μ := fun X => Category.id X
  η_natural := fun f => by rw [Category.comp_id, Category.id_comp]
  μ_natural := fun f => by rw [Category.comp_id, Category.id_comp]
  right_unit := fun X => Category.id_comp (Category.id X)
  left_unit := fun X => Category.id_comp (Category.id X)
  assoc := fun _ => rfl

namespace Comonad

variable (G : Comonad Obj)

/-- The mixed distributive law of `G` over the identity monad: `κ := id`. All
four axioms collapse to comonad functor/identity laws. -/
def coKleisliDistrib : MixedDistrib G (Monad.identity Obj) where
  κ := fun X => Category.id (G.obj X)
  κ_natural := fun _ => by
    simp only [Monad.identity, Category.comp_id, Category.id_comp]
  distrib_unit := fun _ => by
    simp only [Monad.identity, G.map_id, Category.comp_id]
  distrib_counit := fun _ => by
    simp only [Monad.identity, Category.id_comp]
  distrib_mult := fun _ => by
    simp only [Monad.identity, G.map_id, Category.comp_id]
  distrib_comult := fun _ => by
    simp only [Monad.identity, G.map_id, Category.comp_id, Category.id_comp]

/-- coKleisli composition of `f : G p ⟶ q` and `g : G q ⟶ r` unfolds to the
classical `δ ≫ G f ≫ g` (the identity monad's unit/multiplication drop out). -/
theorem coKleisli_acomp {p q r : Obj}
    (f : Category.Hom (G.obj p) q) (g : Category.Hom (G.obj q) r) :
    (G.coKleisliDistrib).acomp f g = (G.δ p) ⊚ (G.map f) ⊚ g := by
  simp only [MixedDistrib.acomp, coKleisliDistrib, Monad.identity,
    Category.comp_id, Category.id_comp]

/-- **Associativity of coKleisli composition.** The `T = Id` case of the paper's
E2′ — vacuously true (no effect to commute past), so it holds for every comonad.
Chase: `δ ≫ G δ = δ ≫ δ_G` (coassoc) on the left, `G f ≫ δ = δ_G ≫ G G f`
(δ-naturality) on the right; both normalise to `δ ≫ δ_G ≫ GGf ≫ Gg ≫ h`. -/
theorem coKleisli_acomp_assoc {p q r s : Obj}
    (f : Category.Hom (G.obj p) q) (g : Category.Hom (G.obj q) r)
    (h : Category.Hom (G.obj r) s) :
    (G.coKleisliDistrib).acomp ((G.coKleisliDistrib).acomp f g) h
      = (G.coKleisliDistrib).acomp f ((G.coKleisliDistrib).acomp g h) := by
  simp only [coKleisli_acomp, G.map_comp, Category.assoc]
  conv => lhs; rw [← Category.assoc (G.δ p) (G.map (G.δ p)), ← G.coassoc p]
  conv => rhs; arg 2; rw [← Category.assoc (G.map f) (G.δ q), G.δ_natural f]
  simp only [Category.assoc]

end Comonad

end Containers
