/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# The two-model distinction: Weil base change vs. honest `◁`-substitution

This file machine-checks the **decidable arithmetic heart** of Rick's referee correction
(2026-10-05, ACCEPTED; memory `rick-uniqueness-ambient-category-correction`) to MacBeth's
container-derivative uniqueness note. The correction is one of *scope*, not refutation: the
uniqueness theorem *"`∂` is the unique nontrivial representable first-order tangent structure"*
is true in the **Weil base-change model** `T = (−) ⊗ W`, `W = ℕ[ε]/ε²`, but **false** in the
**full-`◁` polynomial model** `T = (−) ◁ D` — the write-ups conflated the two. `◁` and `⊗W`
agree only on the linear/module layer; on full `Poly` the `◁`-substitution has no truncation
(`y² ◁ (2y) = 4y² ≠ 3y²`, and `yⁿ ◁ D = Dⁿ` is multiplicative).

The two models give genuinely different representable-universality rank equations:

* **Weil model** (dual numbers, `ε² = 0`): the vertical-lift universality isomorphism `D₂ ≅ P'`
  reads `1 + 2n = 1 + n + n²`, i.e. `n² = n`, with solution set `{0, 1} = {id, ∂}`. (This is the
  content already `lean-verified` in `lean/2026-10-04-universality-rank-rigidity.lean` and
  `lean/2026-10-03-spoly-solid-idempotent.lean`; the `solid_rank_eq` core is reproduced here so the
  oracle is self-contained.) The port of Lanfranchi–Lemay's PID rigidity for representable tangent
  structures on affine schemes (arXiv:2505.09080, Thm 4.17 / Cor 4.18).

* **Honest-`◁` model** (no truncation): the tangent-bundle rank is `D₂(n) = (1 + n)²` and the
  vertical rank is `P'(n) = 1 + n`, so representable universality forces `(1 + n)² = 1 + n`, i.e.
  `n·(n + 1) = 0`. Over `ℕ` the factor `1 + n ≥ 1` is never zero, so this collapses to **`n = 0`
  only**: the survivor set is `{0} = {id}`. The `∂` tangent structure (`n = 1`) does **not** exist
  as a representable tangent structure in full `◁`-`Poly`.

**The headline (`two_model_distinction`): the two survivor sets differ.** `{0, 1}` (Weil) vs. `{0}`
(honest-`◁`). Concretely, `n = 1` — the dual-number derivative `∂` — satisfies the Weil equation
`n² = n` but violates the honest-`◁` equation `(1 + n)² = 1 + n`. Hence the ambient category is
**not** interchangeable, and the corrected Theorem 1 (the Weil statement) is the one with content.

## Scope / honesty

This is the finite / rig-internal ORACLE for the *rank arithmetic* of the two models and their
divergence. It does **not** formalise the structural inputs — the vertical-lift universality axiom
(Cockett–Cruttwell 2014), that `◁` preserves pullbacks, or the rank counts themselves (that
`D₂ = (1+n)²` under full `◁` vs. `1 + 2n` under `⊗W`); those are cited framework facts / proof-note
derivations, not `decide`-able. What is certified: given the two rank equations, their solution sets
over `ℕ` are `{0,1}` and `{0}` respectively, and they differ precisely at `∂` (`n = 1`).
Cross-checked against `scratch/` enumeration (`n = 0..12`: identical). Registered as
`tangent-uniqueness-spoly.json#lean-two-model-distinction`.
-/

namespace TwoModelDistinction

/-! ### 0. Shared idempotent collapse over `ℕ`

`m² = m ↔ m ∈ {0,1}` on `ℕ`, with no PID hypothesis and no subtraction — `ℕ` is a cancellative rig
with no zero divisors. Reproduced from `lean/2026-10-03-spoly-solid-idempotent.lean#solid_rank_eq`
so both model equations below reduce to a single arithmetic fact. -/

/-- **The solid idempotent collapse (over `ℕ`).** `m² = m ↔ m ∈ {0,1}`. Proof by
additive/multiplicative cancellation — no subtraction, no additive inverses. -/
theorem solid_rank_eq (m : Nat) : m * m = m ↔ m = 0 ∨ m = 1 := by
  constructor
  · intro h
    match m, h with
    | 0, _ => exact Or.inl rfl
    | 1, _ => exact Or.inr rfl
    | (k + 2), h =>
        exfalso
        have e : (k + 2) * (k + 2) = (k + 2) * (k + 1) + (k + 2) := by rw [Nat.mul_succ]
        rw [e] at h
        have h' : (k + 2) * (k + 1) + (k + 2) = 0 + (k + 2) := by rw [Nat.zero_add]; exact h
        have h0 : (k + 2) * (k + 1) = 0 := Nat.add_right_cancel h'
        have pos : 0 < (k + 2) * (k + 1) := Nat.mul_pos (Nat.succ_pos (k + 1)) (Nat.succ_pos k)
        rw [h0] at pos
        exact Nat.lt_irrefl 0 pos
  · rintro (h | h) <;> subst h <;> rfl

/-! ### 1. The Weil base-change model (`T = (−) ⊗ W`, `W = ℕ[ε]/ε²`)

The dual-number / square-zero truncation. Vertical-lift universality `D₂ ≅ P'` reads
`1 + 2n = 1 + n + n²` (proof note §6 counts; `lean/2026-10-04-universality-rank-rigidity.lean`). -/

/-- `rank D₂` in the Weil model: `D₂ = D ×_y D` has summands `y ⊕ M ⊕ M`, rank `1 + n + n`. -/
def weilD2 (n : Nat) : Nat := 1 + n + n

/-- `rank P'` in the Weil model: the vertical fibre `y ⊕ ε_out ⊕ (M◁M)`, rank `1 + n + n²`. -/
def weilPprime (n : Nat) : Nat := 1 + n + n * n

/-- **Weil universality rigidity.** `rank D₂ = rank P' ⟺ n ∈ {0,1}`. The survivors are
`n = 0` (`T = id`) and `n = 1` (`T = ∂`, the dual-number derivative). -/
theorem weil_universality (n : Nat) : weilD2 n = weilPprime n ↔ n = 0 ∨ n = 1 := by
  rw [← solid_rank_eq n]
  unfold weilD2 weilPprime
  constructor
  · intro h
    -- `(1 + n) + n = (1 + n) + n*n`; cancel the common summand `1 + n` (NO subtraction).
    exact (Nat.add_left_cancel h).symm
  · intro h
    rw [h]

/-! ### 2. The honest-`◁` model (`T = (−) ◁ D`, no truncation)

Full `◁`-substitution is multiplicative (`yⁿ ◁ D = Dⁿ`), so the tangent bundle has rank
`D₂(n) = (1 + n)²` and the vertical fibre has rank `P'(n) = 1 + n`. Representable universality
`D₂ ≅ P'` reads `(1 + n)² = 1 + n`. -/

/-- `rank D₂` in the honest-`◁` model: full multiplicative `◁`-substitution gives `(1 + n)²`. -/
def honestD2 (n : Nat) : Nat := (1 + n) * (1 + n)

/-- `rank P'` in the honest-`◁` model: the vertical fibre has rank `1 + n`. -/
def honestPprime (n : Nat) : Nat := 1 + n

/-- **Honest-`◁` universality rigidity.** `(1 + n)² = 1 + n ⟺ n = 0`. The only survivor is
`n = 0` (`T = id`): over `ℕ` the factor `1 + n ≥ 1` is never zero, so `∂` (`n = 1`) is **excluded**.
Proof: the equation is `solid_rank_eq` applied to `m = 1 + n`, whose `{0,1}` solution set meets
`1 + n ≥ 1` only at `1 + n = 1`, i.e. `n = 0`. -/
theorem honest_universality (n : Nat) : honestD2 n = honestPprime n ↔ n = 0 := by
  unfold honestD2 honestPprime
  rw [solid_rank_eq (1 + n)]
  constructor
  · rintro (h | h)
    · -- `1 + n = 0` is impossible over `ℕ` (`1 + n = n.succ ≠ 0`).
      rw [Nat.one_add] at h
      exact absurd h (Nat.succ_ne_zero n)
    · -- `1 + n = 1` forces `n = 0`.
      rw [Nat.one_add] at h
      exact Nat.succ.inj h
  · rintro rfl
    exact Or.inr rfl

/-- The honest-`◁` equation in the exact `^2` form of the referee-correction statement:
`(1 + n)² = 1 + n ↔ n = 0`. -/
theorem honest_universality_pow (n : Nat) : (1 + n) ^ 2 = 1 + n ↔ n = 0 := by
  have hsq : (1 + n) ^ 2 = (1 + n) * (1 + n) := by
    rw [Nat.pow_succ, Nat.pow_succ, Nat.pow_zero, Nat.one_mul]
  rw [hsq]
  exact honest_universality n

/-! ### 3. The two-model distinction — the survivor sets differ

The headline consequence of the referee correction: the two ambient categories are **not**
interchangeable. -/

/-- **Weil survivors** over `n ∈ 0..12`: exactly `{0, 1} = {id, ∂}`. -/
theorem weil_survivors :
    (List.range 13).filter (fun n => weilD2 n == weilPprime n) = [0, 1] := by decide

/-- **Honest-`◁` survivors** over `n ∈ 0..12`: exactly `{0} = {id}`. -/
theorem honest_survivors :
    (List.range 13).filter (fun n => honestD2 n == honestPprime n) = [0] := by decide

/-- **The distinguishing witness is `∂` (`n = 1`).** The dual-number derivative satisfies the Weil
universality equation (`weilD2 1 = weilPprime 1`) but **violates** the honest-`◁` one
(`honestD2 1 ≠ honestPprime 1`). This single `n = 1` is the whole content of the scope correction:
`∂` exists as a representable tangent structure in the Weil model and **not** in full `◁`-`Poly`. -/
theorem partial_exists_in_weil_not_honest :
    (weilD2 1 = weilPprime 1) ∧ ¬ (honestD2 1 = honestPprime 1) := by decide

/-- **The two-model distinction, packaged.** The two ambient-category models give provably
different representable-tangent survivor sets:

1. **Weil model** (`⊗W`, dual numbers): `rank D₂ = rank P' ⟺ n ∈ {0,1}` — survivors `{id, ∂}`;
2. **Honest-`◁` model** (`◁`, no truncation): `(1 + n)² = 1 + n ⟺ n = 0` — survivors `{id}`;
3. **They differ**, and differ precisely at `∂` (`n = 1`): the finite survivor lists are `[0,1]`
   vs. `[0]`, and `n = 1` is a Weil survivor that is **not** an honest-`◁` survivor.

Hence the ambient category is load-bearing: the corrected Theorem 1 is the Weil statement, and the
mis-stated full-`◁` version is genuinely false (not merely awkwardly worded). -/
theorem two_model_distinction :
    (∀ n : Nat, weilD2 n = weilPprime n ↔ n = 0 ∨ n = 1)
    ∧ (∀ n : Nat, honestD2 n = honestPprime n ↔ n = 0)
    ∧ (∀ n : Nat, (1 + n) ^ 2 = 1 + n ↔ n = 0)
    ∧ (List.range 13).filter (fun n => weilD2 n == weilPprime n) = [0, 1]
    ∧ (List.range 13).filter (fun n => honestD2 n == honestPprime n) = [0]
    ∧ ((weilD2 1 = weilPprime 1) ∧ ¬ (honestD2 1 = honestPprime 1)) :=
  ⟨weil_universality, honest_universality, honest_universality_pow,
    weil_survivors, honest_survivors, partial_exists_in_weil_not_honest⟩

-- Axiom audit: expected `propext` only (core `Nat`/`List` rewriting + `decide`) — free of
-- `sorryAx`, `Quot.sound`, and `Classical.choice`.
#print axioms two_model_distinction

end TwoModelDistinction
