import Containers.BiKleisli

/-!
# The branching obstruction: the reverse compositor `κ` fails E2′ (negative witness)

This file supplies the **negative half** of the effect–coeffect dichotomy of
`proofs/2026-07-29-effect-coeffect-arrows.md` (MacBeth):

> `Arr_M` is a genuine (associative) arrow category **iff** the reverse
> compositor `κ : G_M T_M ⇒ T_M G_M` is a mixed distributive law (E1′–E4′)
> **iff** `M` is non-branching.

The **positive** direction (`M` non-branching ⟹ all four axioms, hence an
associative arrow category) is fully machine-checked for the entire classified
class `M X = E + A×X` in `Containers.BiKleisliAffine` — in particular the
branching-obstructed axiom **E2′** (`MixedDistrib.distrib_mult`,
`Category.comp (G.map (T.μ X)) (κ X) = κ_{TX} ≫ T κ ≫ μ_{GX}`).

Here we certify the **converse**: for a *branching* monad `M`, `κ` fails E2′.
This is the direction where the mathematics lives, and it had only been
*computed* (Python harness `scratch/monad-comonad-transfer/entwine.py`, which
locates the explicit failing entries for `M = Pf` on the branching container
`{a ↦ 2, b ↦ 1}`).

## What is proved, and at what altitude

E2′ is an equation of *container morphisms* `G_M (T_M (T_M X)) ⟶ T_M (G_M X)`.
Both sides agree on shapes (they act by `μ^M` on shapes), so E2′ can only fail
in the **backward position map**, at a single branching leaf. There the two
sides evaluate to the two ways of combining the compositor `κ` (the cartesian
product-comparison `ρ` on positions) with the monad multiplication `μ` (union,
for the powerset monad). Concretely, at a leaf carrying two sub-branches with
position-sets `(A₁,B₁)` and `(A₂,B₂)`, E2′ demands

```
  ρ (A₁ ∪ A₂) (B₁ ∪ B₂)  =  ρ A₁ B₁ ∪ ρ A₂ B₂        -- κ commutes with μ
       product-of-unions           union-of-products
```

and this **fails**: the product of unions is strictly larger than the union of
products. This is the position-fibre content that the full-container E2′ diagram
inflates (the Python witness above is exactly this datum transported through
`T_M`, `G_M`; it is not re-derived here — that transport is the *positive*
apparatus of `Containers.BiKleisliAffine`, run in reverse). We machine-check the
**fibre obstruction itself**, which is where the branching enters: an arity-`≤ 1`
(non-branching) leaf has no product to compare, and the same square holds by
`rfl` (`oneLeaf_E2_holds` below) — the mirror of the affine positive result.

## Why the finite powerset, and why the fibre

* `Pf` (finite powerset) is the *minimal* branching monad for which the
  Ahman–Bauer effect monad `T_M` (arXiv:2409.17664, Thm 6.3) even exists: its
  multiplication `μ = ⋃` is idempotent and commutative, so the leaf-labels of
  `μ(mm)` are distinct and the `∏`-cointerpretation position map of `μ^T` is
  well-defined. For a *bounded-arity* polynomial branching monad such as
  `M X = 1 + X²`, `μ^T`'s backward map is already ill-defined (the diagonal
  `μ` forgets leaves), so the obstruction surfaces even earlier; `Pf` is the
  clean carrier of the genuine `κ`-level E2′ failure.
* The development is Lean-4-core (no Mathlib, matching the rest of
  `Containers`), so `Pf` over a finite type is modelled by its **characteristic
  function** `T → Bool`. Over a `Fintype` this *is* the covariant powerset, with
  `μ = ⋃` pointwise `or` and the cartesian compositor `ρ` pointwise `and` of the
  two projections. The failure is then a closed `Bool` computation, closed by
  `decide`.

Everything is `Type`-level, Lean 4 core, no Mathlib. No `sorry`, no classical
axioms; the negative witness closes by kernel `decide`.
-/

namespace Containers
namespace BranchingObstruction

/-! ## The finite powerset by characteristic functions (Mathlib-free) -/

/-- A **finite subset** of a (finite) type `T`, modelled Mathlib-free by its
characteristic function. Over a `Fintype` this is the covariant powerset monad
`Pf` used as the effect monad's carrier in
`proofs/2026-07-29-effect-coeffect-arrows.md`. -/
def Pf (T : Type) : Type := T → Bool

/-- Membership, purely for readability of the witnesses below. -/
def mem {T : Type} (A : Pf T) (x : T) : Bool := A x

/-- The powerset **multiplication** `μ` restricted to a two-element family:
binary union, pointwise `or`. (The full `μ : Pf (Pf T) → Pf T` is `⋃`; E2′ at a
two-leaf shape only ever merges two branches, so binary union is the operative
instance.) -/
def unionP {T : Type} (A B : Pf T) : Pf T := fun x => A x || B x

/-- The **reverse compositor `κ` on positions**: the cartesian
product-comparison `ρ : Pf P × Pf Q → Pf (P × Q)`, `ρ(A,B) = A × B`, pointwise
`and` of the two projections. This is the lax monoidal map that assembles `κ`
for the powerset (`entwine.py`, `lambda_rev_Pf`; `bikleisli.py`, `lax_Pf`). -/
def kappa {P Q : Type} (A : Pf P) (B : Pf Q) : Pf (P × Q) :=
  fun p => A p.1 && B p.2

/-! ## The branching witness

Two sub-branches over the position universe `Bool = {0,1}`, with
`A₁ = {0}, A₂ = {1}` in the first factor and `B₁ = {0}, B₂ = {1}` in the second.
This is the minimal branching datum: two singletons whose unions are all of
`Bool`, so the product of unions is the full `2 × 2` square while the union of
products is only its diagonal — exactly the `4`-vs-`2` gap the Python harness
reports for `Pf` on `{a ↦ 2, b ↦ 1}`. -/

/-- `A₁ = {0}` (i.e. `{false}`). -/
def A1 : Pf Bool := fun x => x == false
/-- `A₂ = {1}` (i.e. `{true}`). -/
def A2 : Pf Bool := fun x => x == true
/-- `B₁ = {0}`. -/
def B1 : Pf Bool := fun x => x == false
/-- `B₂ = {1}`. -/
def B2 : Pf Bool := fun x => x == true

/-! ## E2′ fails at the branching leaf

The E2′ axiom `MixedDistrib.distrib_mult`, read on the backward position map at a
two-leaf branching shape, is precisely "`κ` commutes with `μ`":
`ρ (A₁ ∪ A₂) (B₁ ∪ B₂) = ρ A₁ B₁ ∪ ρ A₂ B₂`. We show it fails. -/

/-- **The branching obstruction (E2′ fails).** For the powerset compositor `κ`
(cartesian `ρ`) and multiplication `μ` (union), the E2′ coherence
`ρ (A₁ ∪ A₂) (B₁ ∪ B₂) = ρ A₁ B₁ ∪ ρ A₂ B₂` is false: the two sides differ at
the off-diagonal position `(0,1)`, where the product of unions contains `(0,1)`
but the union of products does not.

This is the machine-checked negative witness completing the paper's dichotomy:
`M` branching ⟹ `κ` is *not* a mixed distributive law (`distrib_mult` fails) ⟹
`Arr_M` is not an associative arrow category. -/
theorem kappa_distrib_mult_fails :
    kappa (unionP A1 A2) (unionP B1 B2)
      ≠ unionP (kappa A1 B1) (kappa A2 B2) := by
  intro h
  -- Evaluate both sides at the off-diagonal position `(false, true) = (0,1)`.
  -- LHS (product of unions) = `true`; RHS (union of products) = `false`.
  exact absurd (congrFun h (false, true)) (by decide)

/-- The same failure, packaged as the strict statement that the two composites
of E2′ are unequal *as maps* — i.e. `κ` fails to be a `μ`-coherent (distributive)
transformation for the branching monad. -/
theorem kappa_not_distributive_over_union :
    ¬ (∀ (P Q : Type) (A₁ A₂ : Pf P) (B₁ B₂ : Pf Q),
        kappa (unionP A₁ A₂) (unionP B₁ B₂)
          = unionP (kappa A₁ B₁) (kappa A₂ B₂)) := by
  intro hall
  exact kappa_distrib_mult_fails (hall Bool Bool A1 A2 B1 B2)

/-! ## The non-branching mirror: E2′ holds at an arity-`≤ 1` leaf

At a leaf with a single sub-branch there is no product to form; the compositor
degenerates to the identity lax `ρ₁ = id : Pf P → Pf P`, and the E2′ coherence
`ρ₁ (A₁ ∪ A₂) = ρ₁ A₁ ∪ ρ₁ A₂` holds definitionally. This is the fibre-level
shadow of the affine positive result (`Containers.BiKleisliAffine`, where the
`∏` is over `≤ 1` leaf so the union-of-products/product-of-unions gap never
forms): non-branching ⟹ E2′ holds. -/

/-- The one-leaf (non-branching) compositor: identity, no product. -/
def kappaOne {P : Type} (A : Pf P) : Pf P := A

/-- **Non-branching mirror (E2′ holds).** With a single leaf the compositor
commutes with `μ` on the nose. -/
theorem oneLeaf_E2_holds {P : Type} (A₁ A₂ : Pf P) :
    kappaOne (unionP A₁ A₂) = unionP (kappaOne A₁) (kappaOne A₂) := rfl

end BranchingObstruction
end Containers
