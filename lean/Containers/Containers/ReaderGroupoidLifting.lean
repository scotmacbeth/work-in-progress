import Containers.Directed
import Containers.StateComonad
import Containers.ReaderStateOutsidePiMendler

/-!
# The ℤ/2 groupoid: a Reader monad lifting that is neither ∏ nor Σ

This file machine-checks the **load-bearing witness** of MacBeth's crown result
`proofs/2026-08-09-reader-liftings-are-categories.md` (registry node
`reader-liftings-are-categories`, proved): the classification "fibred
proof-relevant polynomial monad liftings of Reader `y^E` = `E`-indexed families
of small categories" has a genuine **third** point beyond the two canonical ones
(∏ and Σ). Concretely, at the minimal index `E = 1` (one leaf) there is a
lifting whose per-leaf aggregator is the **one-object groupoid ℤ/2** — its
products live *within* a single leaf, so it is neither the ∏ lifting `T_M` nor
any Σ lifting `M ◁ −`.

## The object

By the crown's Step E ("each leaf = a polynomial comonad = a small category"),
a monad lifting of Reader is, per leaf, a **polynomial comonad on `Set`**, i.e.
(Ahman–Chapman–Uustalu, *When is a container a comonad?*, arXiv:1408.5809) a
small category — realised here as a `Containers.DirectedContainer`. The ℤ/2
groupoid is the smallest *non-discrete* such category:

* **objects:** one (`Shape = Unit`);
* **morphisms:** the group `ℤ/2 = {e, g}` (`Pos _ = Z2`), so the aggregator is
  `L(B) = B^{ℤ/2} = B²` (`Ext readerGroupoidLifting X ≅ X²`);
* **identity / counit:** the neutral element `e` (`root _ = e`);
* **composition / comultiplication:** the group multiplication `Z2.mul`
  (`shift _ p q = p * q`), whose defining feature is the **swap** `g * g = e`.

The three comonad laws are inherited from `Containers.Directed` and *are* the
three group axioms of ℤ/2:

* left counit  ⟸ D1 & D2  =  **left identity** `e * q = q`;
* right counit ⟸ D3       =  **right identity** `q * e = q`;
* coassociativity ⟸ D4 & D5 =  **associativity** `(p*q)*r = p*(q*r)`.

("One operation, two faces": the lift is a *monad* on `Cont`, but its per-leaf
aggregator is a *comonad* on `Set` — the fibrewise op turns the lift's
multiplication into the category's composition; `position-op-monads-to-comonads`.
We formalise the comonad = small-category side, which is the honest classifying
datum of the crown; the monad-on-`Cont` face is its fibrewise dual.)

## The two separations

* **Not Σ (`M ◁ −`).** A Σ lifting gives, per leaf, a **discrete** category —
  its only endomorphism is the identity, so composition is trivial. The ℤ/2
  groupoid has a *non-identity* morphism `g ≠ e` with a *nontrivial* composite
  `g * g = e ≠ g`. We contrast it against the discrete one-object category
  (`= deltaDC Unit`), whose hom-set is a subsingleton.
* **Not ∏ (`T_M`).** For Reader the ∏-cointerpretation `T_M` carries **no**
  monad multiplication at all (`reader_kappa_not_total`, the DROP certificate of
  `Containers.ReaderStateOutsidePiMendler`), whereas the groupoid lifting `L`
  *does* — its comultiplication `δ`, driven by the swap `g * g = e`. So `L` is a
  monad lifting that the ∏ construction cannot supply.

Everything is `Type`-level Lean 4 core, no Mathlib, no `sorry`. The group laws
are pure `rfl` after case analysis (`Z2` is hand-rolled to keep them
definitional and axiom-free — no `decide`, no `propext`).

Reference: MacBeth PROVE `proofs/2026-08-09-reader-liftings-are-categories.md`,
§3 (Steps A–E) and §4 (the table row `B_0² with swap δ = one-object groupoid
ℤ/2`); the ∏ exclusion is `proofs/2026-08-06-state-reader-ladder-census.md`
(node `state-reader-outside-pi-mendler`); DCont ≅ Cat is Ahman–Chapman–Uustalu
arXiv:1408.5809.
-/

namespace Containers

namespace ReaderGroupoid

/-! ## 1. The group `ℤ/2` as morphisms of the one-object groupoid

We hand-roll the two-element group so that its axioms are definitional (`rfl`
after case analysis), keeping the whole development axiom-free (no `decide`,
hence no `propext`). `e` is the identity morphism, `g` the swap. -/

/-- The two-element group `ℤ/2`, as the single hom-set of the one-object
groupoid: `e` (identity) and `g` (the swap). -/
inductive Z2 : Type
  | e
  | g
  deriving DecidableEq

/-- Group multiplication = **composition** of the one-object groupoid. Defined by
its table so that `e * b = b` (and the swap `g * g = e`) hold by `rfl`. -/
def Z2.mul : Z2 → Z2 → Z2
  | e, b => b
  | g, e => g
  | g, g => e

/-- **Left identity** `e * q = q` — holds by `rfl` (first row of the table). This
is the group axiom behind the comonad's *left counit* law (via D2). -/
theorem Z2.mul_e_left (q : Z2) : Z2.mul Z2.e q = q := rfl

/-- **Right identity** `q * e = q` — the group axiom behind the *right counit*
law (via D3). -/
theorem Z2.mul_e_right (q : Z2) : Z2.mul q Z2.e = q := by cases q <;> rfl

/-- **Associativity** `(p * q) * r = p * (q * r)` — the group axiom behind
*coassociativity* (via D5). -/
theorem Z2.mul_assoc (p q r : Z2) :
    Z2.mul (Z2.mul p q) r = Z2.mul p (Z2.mul q r) := by
  cases p <;> cases q <;> cases r <;> rfl

/-- **The swap** `g * g = e`: the composite of the non-identity morphism with
itself is the identity. This single equation is what makes the category a
*non-discrete groupoid* — and hence neither Σ nor ∏. -/
theorem Z2.g_mul_g : Z2.mul Z2.g Z2.g = Z2.e := rfl

/-- `e ≠ g`: the hom-set has (at least) two elements — the groupoid is not
discrete. -/
theorem Z2.e_ne_g : Z2.e ≠ Z2.g := fun h => Z2.noConfusion h

/-- **`ℤ/2` is a group**: every morphism is invertible. For `Z2` each element is
its own inverse (`g * g = e`, `e * e = e`), so the one-object category is a
*groupoid*, not merely a monoid. -/
theorem Z2.isGroupoid (a : Z2) : ∃ b : Z2, Z2.mul a b = Z2.e ∧ Z2.mul b a = Z2.e := by
  cases a
  · exact ⟨Z2.e, rfl, rfl⟩
  · exact ⟨Z2.g, rfl, rfl⟩

/-! ## 2. The lifting as a directed container (= the one-object groupoid) -/

/-- The **ℤ/2 groupoid lifting** of Reader at `E = 1`, as a directed container
(= a small category, by Ahman–Chapman–Uustalu). One object (`Shape = Unit`),
hom-set `ℤ/2` (`Pos _ = Z2`), identity `e`, composition the group
multiplication. All five directed-container laws hold — D1/D4 by `Unit`-eta,
D2/D3/D5 are exactly the ℤ/2 group axioms `Z2.mul_e_left`/`_right`/`_assoc`. -/
def readerGroupoidLifting : DirectedContainer where
  toContainer := { Shape := Unit, Pos := fun _ => Z2 }
  root := fun _ => Z2.e
  sub := fun _ _ => ()
  shift := fun _ p q => Z2.mul p q
  d1 := fun _ => rfl
  d4 := fun _ _ _ => rfl
  d2 := fun _ q => (Z2.mul_e_left q)
  d3 := fun _ p => (Z2.mul_e_right p)
  d5 := fun _ p q r => (Z2.mul_assoc p q r)

/-- The aggregator is `L(B) = B^{ℤ/2}`: `Ext readerGroupoidLifting X` is a single
shape carrying a `ℤ/2`-indexed labelling — i.e. `X²`. -/
theorem readerGroupoid_ext (X : Type) :
    Ext readerGroupoidLifting.toContainer X = ((_ : Unit) × (Z2 → X)) := rfl

/-! ## 3. The three comonad laws = the three ℤ/2 group axioms

The laws come for free from `Containers.Directed`; here we name them and expose
their pointwise content, so that the identification "(co)monad law = group axiom"
is on the record. -/

variable {X : Type}

/-- **Counit** `ε ⟨(), v⟩ = v e`: evaluate the labelling at the **identity**
morphism `e`. (In the monad-on-`Cont` face this is the lift's unit.) -/
theorem readerGroupoid_counit (v : Z2 → X) :
    readerGroupoidLifting.counit (X := X) ⟨(), v⟩ = v Z2.e := rfl

/-- **Comultiplication** `δ ⟨(), v⟩ = ⟨(), fun p => ⟨(), fun q => v (p * q)⟩⟩`:
re-index the labelling along **composition** `p * q`. This is the ℤ/2 group
multiplication — the operation that Σ (discrete) lacks and ∏ cannot supply. -/
theorem readerGroupoid_comult (v : Z2 → X) :
    readerGroupoidLifting.comult (X := X) ⟨(), v⟩
      = ⟨(), fun p => ⟨(), fun q => v (Z2.mul p q)⟩⟩ := rfl

/-- **Left counit law** `ε ∘ δ = id` — inherited from D1/D2, i.e. from the group
*left identity* `e * q = q`. -/
theorem readerGroupoid_left_counit :
    readerGroupoidLifting.counit ∘ readerGroupoidLifting.comult
      = (id : Ext readerGroupoidLifting.toContainer X → _) :=
  readerGroupoidLifting.left_counit

/-- **Right counit law** `(map ε) ∘ δ = id` — inherited from D3, i.e. from the
group *right identity* `q * e = q`. -/
theorem readerGroupoid_right_counit :
    Ext.map readerGroupoidLifting.counit ∘ readerGroupoidLifting.comult
      = (id : Ext readerGroupoidLifting.toContainer X → _) :=
  readerGroupoidLifting.right_counit

/-- **Coassociativity** `(map δ) ∘ δ = δ ∘ δ` — inherited from D4/D5, i.e. from
group *associativity* `(p*q)*r = p*(q*r)`. -/
theorem readerGroupoid_coassoc :
    Ext.map readerGroupoidLifting.comult ∘ readerGroupoidLifting.comult
      = (readerGroupoidLifting.comult ∘ readerGroupoidLifting.comult :
          Ext readerGroupoidLifting.toContainer X → _) :=
  readerGroupoidLifting.coassoc

/-! ## 4. It is **not Σ**: the composition is nontrivial (non-discrete category)

A Σ lifting `M ◁ −` gives, per leaf, a **discrete** category: the hom-set out of
an object is a singleton (only the identity), so composition is forced trivial.
The ℤ/2 groupoid has *two* distinct morphisms and a *nontrivial* composite
`g * g = e ≠ g`. We make the contrast concrete against the discrete one-object
category `deltaDC Unit` (the codiscrete category on `Unit`, whose hom bundle
`Σ_{s'} 1` is a singleton). -/

/-- The **discrete one-object category** = the Σ point at `E = 1`: `deltaDC Unit`
(one object, one morphism). Its hom-set `Pos ()` is `Unit`, a subsingleton — no
room for a nontrivial composite. -/
def discreteOneObject : DirectedContainer := deltaDC Unit

/-- The discrete category's hom-set is a **subsingleton**: any two morphisms out
of the object are equal (there is only the identity). -/
theorem discrete_hom_subsingleton (a b : discreteOneObject.Pos ()) : a = b :=
  rfl

/-- The ℤ/2 groupoid's hom-set has **two distinct** morphisms — it is not
discrete. -/
theorem groupoid_hom_not_subsingleton :
    ∃ a b : readerGroupoidLifting.Pos (), a ≠ b :=
  ⟨Z2.e, Z2.g, Z2.e_ne_g⟩

/-- **The Σ-separation, concretely.** The groupoid has a non-identity morphism
`g` (distinct from the identity `root () = e`) whose self-composite is the
identity — `g * g = e` — a *nontrivial* composition. No discrete category (no Σ
lifting `M ◁ −`) admits such a morphism: its hom-set is a subsingleton
(`discrete_hom_subsingleton`). Hence the ℤ/2 groupoid lifting is **not** a Σ
lifting. -/
theorem readerGroupoid_not_sigma :
    (∃ h : readerGroupoidLifting.Pos (),
        h ≠ readerGroupoidLifting.root () ∧
          readerGroupoidLifting.shift () h h = readerGroupoidLifting.root ())
      ∧ (∀ a b : discreteOneObject.Pos (), a = b) :=
  ⟨⟨Z2.g, fun h => Z2.e_ne_g h.symm, Z2.g_mul_g⟩,
   fun _ _ => rfl⟩

/-! ## 5. It is **not ∏**: `T_Reader` has no multiplication, `L` does

For Reader the ∏-cointerpretation `T_M` (Ahman–Bauer, arXiv:2409.17664, Thm 6.3)
carries **no** monad multiplication: its laxator's covering `κ_μ` is not
forward-total (Reader's `μ` is the diagonal, which *drops* off-diagonal inner
leaves). This is `reader_kappa_not_total` from
`Containers.ReaderStateOutsidePiMendler`. The ℤ/2 groupoid lifting, by contrast,
*has* a genuine — and nontrivial — comultiplication `δ` (the group
multiplication, with `g * g = e`). So `L` is a monad lifting of Reader that the ∏
construction cannot supply: `L ≠ T_M`. -/

open ReaderStateOutsidePiMendler in
/-- **The ∏-separation, concretely.** (i) The ∏-lifting `T_Reader` has no monad
multiplication (`reader_kappa_not_total`: its `κ_μ` is not forward-total at the
witness `Gw`). (ii) The groupoid lifting `L` has a nontrivial comultiplication:
its composition realises the swap `g * g = e` on a non-identity morphism `g`.
Two liftings, one carrying multiplicative structure the other provably lacks —
so `L ≠ T_M`. -/
theorem readerGroupoid_not_pi :
    (¬ ReaderKappaTotal Gw)
      ∧ (Z2.g ≠ Z2.e ∧ readerGroupoidLifting.shift () Z2.g Z2.g = Z2.e) :=
  ⟨reader_kappa_not_total, fun h => Z2.e_ne_g h.symm, Z2.g_mul_g⟩

/-! ## 6. The packaged witness

The clean deliverable of the LEAN session: the ℤ/2 groupoid lifting satisfies the
three (co)monad laws (= ℤ/2 group axioms) and is **neither ∏ nor Σ**. -/

open ReaderStateOutsidePiMendler in
/-- **`reader_groupoid_is_neither_pi_nor_sigma`.** The one-object ℤ/2 groupoid is
a monad lifting of Reader (its per-leaf polynomial comonad satisfies the three
laws — bundled as the group axioms `Z2.mul_e_left`/`_right`/`_assoc`) that is:

* **not ∏** — `T_Reader` has no multiplication (`reader_kappa_not_total`) whereas
  `L` does (the group multiplication, `g * g = e`);
* **not Σ** — its per-leaf category is *non-discrete*: a non-identity morphism
  `g` with nontrivial composite `g * g = e`, impossible in the discrete
  categories that Σ (`M ◁ −`) yields.

This certifies the single most surprising claim of the crown: the ∏/Σ/mix
partition of Reader's liftings is **false** — categorical products *inside one
leaf* give a genuine third lifting. -/
theorem reader_groupoid_is_neither_pi_nor_sigma :
    -- three (co)monad laws = ℤ/2 group axioms
    ((∀ q : Z2, Z2.mul Z2.e q = q)
      ∧ (∀ q : Z2, Z2.mul q Z2.e = q)
      ∧ (∀ p q r : Z2, Z2.mul (Z2.mul p q) r = Z2.mul p (Z2.mul q r)))
    -- not ∏: T_Reader has no multiplication, L's is nontrivial
      ∧ (¬ ReaderKappaTotal Gw
          ∧ readerGroupoidLifting.shift () Z2.g Z2.g = Z2.e)
    -- not Σ: non-discrete (a nontrivial hom), unlike any discrete Σ lifting
      ∧ ((∃ a b : readerGroupoidLifting.Pos (), a ≠ b)
          ∧ (∀ a b : discreteOneObject.Pos (), a = b)) :=
  ⟨⟨Z2.mul_e_left, Z2.mul_e_right, Z2.mul_assoc⟩,
   ⟨reader_kappa_not_total, Z2.g_mul_g⟩,
   ⟨⟨Z2.e, Z2.g, Z2.e_ne_g⟩, fun _ _ => rfl⟩⟩

end ReaderGroupoid

end Containers
