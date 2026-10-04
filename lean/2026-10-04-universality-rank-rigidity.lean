/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# Finite / rig-internal oracle for the universality-of-vertical-lift rank rigidity

This file machine-checks the **decidable arithmetic core** of MacBeth's PROVE result
*"A rig-internal proof of the solid-correspondence converse"*
(`proofs/2026-10-04-solid-correspondence-converse.md`; registry node
`tangent-uniqueness-spoly.json#solid-correspondence-converse`). That proof closes the one gap
between trust `computed` and `proved` for the uniqueness theorem *"`∂` is the unique nontrivial
representable first-order tangent structure on finite-support polynomial functors"* — the SPoly
port of Lanfranchi–Lemay's PID rigidity for representable tangent structures on affine schemes
(arXiv:2505.09080, Thm 4.17 / Cor 4.18).

## What the informal proof does, and what is decidable here

Let `T = (−)◁D` be a representable first-order tangent structure on `SPoly`, with
`D = y ⊕ M`, `M = S·y` a **linear** container of rank `n = |S|` (linearity forced by the
additive-bundle axiom, companion §2). The **universality of the vertical lift** axiom
(Cockett–Cruttwell 2014, Def. 2.3) asserts the comparison square is a pullback, i.e. the
functor-isomorphism `T₂ ≅ V`. Since `◁` preserves pullbacks on both sides (proof note §1,
Lemma A, via Gambino–Kock Prop. 1.9), one has `T₂ = (−)◁D₂` and `V = (−)◁P'`; evaluating at
`y ∈ SPoly` (`y◁E = E`) collapses the axiom to a single isomorphism in `SPoly`:

> `D₂ ≅ P'`.

The proof note's one genuinely new idea is that all three relevant objects are **direct
coproducts** of surviving summands in the extensive category `SPoly`, so their ranks are computed
by **addition**, never by the subtraction / short-exact-sequence step Lanfranchi–Lemay use over a
commutative ring. Writing `n = rank M` (and `n² = rank (M◁M)`):

| object | coproduct of summands | rank |
|---|---|---|
| `D◁D` | `y ⊕ ε_in ⊕ ε_out ⊕ (M◁M)` | `1 + n + n + n²  = (1+n)²` |
| `D₂ = D ×_y D` | `y ⊕ M ⊕ M` (fibre product: **no** mixed term) | `1 + n + n` |
| `P'` (vertical fibre) | `y ⊕ ε_out ⊕ (M◁M)` (`ĝ` kills `ε_in`) | `1 + n + n²` |

By Lemma 1 of the companion note (shape-count is a complete iso-invariant on the linear layer),
`D₂ ≅ P'` reads `1 + 2n = 1 + n + n²`. Over the **cancellative** rig `ℕ` (no zero divisors) this
forces, with **no subtraction and no additive inverses**, `n² = n`, hence `n ∈ {0,1}`:
`n = 0` ↔ `T = Id`, `n = 1` ↔ `T = ∂` (AAGM dual numbers).

This file certifies, sorry-free and Mathlib-free (the 2026-10-03 oracle pattern of
`lean/2026-10-03-spoly-solid-idempotent.lean` and `…-tangent-container-bridge-finite.lean`):

1. **The coproduct counts** (`rankDcompD`, `rankD2`, `rankPprime`) and the three **extensivity
   identities** showing ranks relate purely **additively** — `D◁D = (1+n)²`,
   `D◁D = P' + ε_in` (`+ n`), `D◁D = D₂ + (M◁M)` (`+ n²`). This is the honesty certificate for the
   "ranks add, never subtract" claim (proof note §2, §4): the derivation forms no difference.
2. **The universality rigidity** (`universality_forces_idempotent`): `rank D₂ = rank P'`
   ⟺ `n ∈ {0,1}`, proved rig-internally by `Nat.add_left_cancel` reducing to the idempotent
   collapse `n² = n ↔ n ∈ {0,1}` (`solid_rank_eq`). No `omega` on the cancellation step, so the
   proof literally exhibits additive cancellation over `ℕ`, matching proof note §3.
3. **Finite enumeration and the dual-number / excluded witnesses**: the ranks `n ∈ 0..12` with
   `rank D₂ = rank P'` are exactly `[0,1]`; `n = 1` (dual numbers) gives `3 = 3` (universality
   holds); `n = 2` (square-zero rank 2) gives `5 ≠ 7` (correctly excluded, matching L–L's
   "only `r ∈ {0,1}`").

**SCOPE / HONESTY.** This is the finite / cancellative ORACLE for the *rank arithmetic* of the
vertical-lift universality collapse plus the coproduct-count identities. It does **not** formalise
the structural inputs — the universality-of-the-vertical-lift axiom (CC 2014), `◁`-preserves-
pullbacks (Lemma A / Gambino–Kock), or that `M` is linear (additive-bundle axiom) — all of which
are cited framework facts in the proof note, not `decide`-able. Finiteness is load-bearing: the
countable case `κ = ℵ₀` satisfies `1 + 2κ = 1 + κ + κ²`, so universality does *not* exclude
`M = ℕ·y` (witnessed separately by the Cantor-window injectivity of
`lean/2026-10-03-spoly-solid-idempotent.lean`). Cross-checked against
`scratch/verify_universality_counts.py` (ground-truth tables for `n = 0..5`: identical).
Registered as `tangent-uniqueness-spoly.json#lean-universality-rank-rigidity`.
-/

namespace UniversalityRankRigidity

/-! ### 1. The coproduct ranks of the three vertical-lift objects

On the linear layer of `SPoly` a container is pinned by its shape-count (rank); `M = S·y` has rank
`n`, and `M◁M = (S×S)·y` has rank `n²` (bundle tensor `◁` multiplies rank on the linear layer,
Lemma 0 / Lemma 1 of the note). In the extensive category `SPoly` each of the three objects below
is a *direct coproduct* of surviving summands, so its rank is the **sum** of summand ranks. -/

/-- `rank (D◁D)` where `D = y ⊕ M`, `rank M = n`. Four coproduct summands
`y ⊕ ε_in ⊕ ε_out ⊕ (M◁M)`, ranks `1 + n + n + n²`. -/
def rankDcompD (n : Nat) : Nat := 1 + n + n + n * n

/-- `rank (D₂)`, `D₂ = D ×_y D`. A fibre product creates **no** mixed infinitesimal term, so the
three summands are `y ⊕ M ⊕ M`, ranks `1 + n + n`. -/
def rankD2 (n : Nat) : Nat := 1 + n + n

/-- `rank (P')`, the vertical-bundle fibre. `ĝ = p̂◁D` kills the inner `ε_in` summand and the mixed
term is retained via `ε_out`; the surviving coproduct is `y ⊕ ε_out ⊕ (M◁M)`, ranks `1 + n + n²`.
Crucially this is a direct sub-coproduct (extensivity), so its rank is computed by **addition**,
not as `rank(D◁D) − rank(im ẑ)` (the subtraction step that fails over the rig `ℕ`). -/
def rankPprime (n : Nat) : Nat := 1 + n + n * n

/-! ### 2. Extensivity identities — ranks relate purely by addition (no subtraction)

These certify the proof note's central structural claim (§2, §4): the three objects' ranks are
tied together by **sums**, so the whole derivation is rig-internal. -/

/-- `rank (D◁D) = (1 + n)²`: `D◁D = (y ⊕ M)◁(y ⊕ M)` has total rank `(1+n)²`. -/
theorem rankDcompD_eq_sq (n : Nat) : rankDcompD n = (1 + n) * (1 + n) := by
  simp only [rankDcompD, Nat.mul_add, Nat.add_mul, Nat.one_mul, Nat.mul_one]
  exact Nat.add_assoc (1 + n) n (n * n)

/-- `rank (D◁D) = rank (P') + n`: `P'` is `D◁D` with the `ε_in` summand (rank `n`) removed, stated
as an **addition** `D◁D = P' ⊕ ε_in`. No difference of ranks is formed. -/
theorem rankDcompD_eq_rankPprime_add (n : Nat) : rankDcompD n = rankPprime n + n := by
  simp only [rankDcompD, rankPprime]
  exact Nat.add_right_comm (1 + n) n (n * n)

/-- `rank (D◁D) = rank (D₂) + n²`: `D◁D` is `D₂` with the mixed term `M◁M` (rank `n²`) adjoined,
stated as an **addition** `D◁D = D₂ ⊕ (M◁M)`. -/
theorem rankDcompD_eq_rankD2_add (n : Nat) : rankDcompD n = rankD2 n + n * n := by
  simp only [rankDcompD, rankD2]

/-! ### 3. The idempotent collapse (rig-internal, over `ℕ`)

`n² = n ↔ n ∈ {0,1}` on `ℕ`, with no PID hypothesis and no subtraction — `ℕ` is a cancellative rig
with no zero divisors. Reproduced from `lean/2026-10-03-spoly-solid-idempotent.lean#solid_rank_eq`
so this oracle is self-contained. -/

/-- **The solid idempotent collapse (general, over `ℕ`).** `n² = n ↔ n ∈ {0,1}`. The SPoly analogue
of Lanfranchi–Lemay's `n² = n ⟹ n ∈ {0,1}` rigidity (arXiv:2505.09080, inside Thm 4.17), here over
the rig `ℕ`. Proof by additive/multiplicative cancellation — no subtraction. -/
theorem solid_rank_eq (n : Nat) : n * n = n ↔ n = 0 ∨ n = 1 := by
  constructor
  · intro h
    match n, h with
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

/-! ### 4. Universality of the vertical lift forces `n ∈ {0,1}`

The axiom collapses (proof note §1) to `D₂ ≅ P'`, i.e. `rank D₂ = rank P'`, i.e.
`1 + n + n = 1 + n + n²`. Rig-internal cancellation of the common summand `1 + n` (via
`Nat.add_left_cancel` — **no subtraction**) reduces this to `n² = n`, then the idempotent collapse
gives `n ∈ {0,1}`. -/

/-- **Universality rigidity (the converse's arithmetic heart).** The vertical-lift universality
isomorphism `D₂ ≅ P'`, read on ranks, holds iff `n ∈ {0,1}`:
`rank D₂ = rank P'  ⟺  n = 0 ∨ n = 1`. The forward direction is pure additive cancellation over
the rig `ℕ`, matching proof note §3 — it forms no difference of ranks. -/
theorem universality_forces_idempotent (n : Nat) :
    rankD2 n = rankPprime n ↔ n = 0 ∨ n = 1 := by
  unfold rankD2 rankPprime
  constructor
  · intro h
    -- `(1 + n) + n = (1 + n) + n*n`; cancel the common `1 + n` summand (NO subtraction).
    exact (solid_rank_eq n).mp (Nat.add_left_cancel h).symm
  · rintro (rfl | rfl) <;> rfl

/-- **Finite enumeration.** Among ranks `n ∈ 0..12`, universality `rank D₂ = rank P'` holds for
exactly `n ∈ {0,1}`. -/
theorem finite_universality_survivors :
    (List.range 13).filter (fun n => rankD2 n == rankPprime n) = [0, 1] := by decide

/-- **Dual-number witness** (`n = 1`): universality holds, `rank D₂ = rank P' = 3`. This is the
`∂` tangent structure (`D = y + εv`), and `3` is the Weil-algebra rank of `k[ε₁,ε₂]/(ε₁²,ε₂²,ε₁ε₂)`
(proof note §5). -/
theorem dualNumber_universality : rankD2 1 = 3 ∧ rankPprime 1 = 3 := by decide

/-- **Excluded witness** (`n = 2`, square-zero rank 2): universality **fails**, `5 ≠ 7`. Correctly
excluded — this is the first Whitney-sum obstruction, matching L–L's "only `r ∈ {0,1}`"
(proof note §5). -/
theorem rank2_excluded : rankD2 2 ≠ rankPprime 2 := by decide

/-! ### 5. Packaged oracle -/

/-- **The universality-rank rigidity oracle, packaged.** Certifies the decidable / rig-internal core
of `proofs/2026-10-04-solid-correspondence-converse.md`:

1. **Extensivity (ranks add)** — `rank(D◁D) = (1+n)²`, `= rank(P') + n`, `= rank(D₂) + n²`: the
   three vertical-lift objects' ranks relate purely additively, so the derivation forms no
   difference (proof note §2, §4);
2. **Universality rigidity** — `rank D₂ = rank P' ⟺ n ∈ {0,1}`, by rig-internal additive
   cancellation reducing to the idempotent collapse `n² = n ↔ n ∈ {0,1}` (proof note §3);
3. **Enumeration & witnesses** — finite survivors `[0,1]`; dual-number `n=1` holds (`3=3`);
   square-zero `n=2` excluded (`5≠7`).

NOT certified (out of scope, cited framework facts in the note): the vertical-lift universality
axiom (Cockett–Cruttwell 2014), `◁`-preserves-pullbacks (Lemma A / Gambino–Kock Prop. 1.9), and
`M` linear (additive-bundle axiom). Finiteness is load-bearing (the countable case escapes `{0,1}`;
witnessed in `lean/2026-10-03-spoly-solid-idempotent.lean`). -/
theorem universality_rank_rigidity_oracle :
    (∀ n : Nat, rankDcompD n = (1 + n) * (1 + n))
    ∧ (∀ n : Nat, rankDcompD n = rankPprime n + n)
    ∧ (∀ n : Nat, rankDcompD n = rankD2 n + n * n)
    ∧ (∀ n : Nat, rankD2 n = rankPprime n ↔ n = 0 ∨ n = 1)
    ∧ (List.range 13).filter (fun n => rankD2 n == rankPprime n) = [0, 1]
    ∧ (rankD2 1 = 3 ∧ rankPprime 1 = 3)
    ∧ rankD2 2 ≠ rankPprime 2 :=
  ⟨rankDcompD_eq_sq, rankDcompD_eq_rankPprime_add, rankDcompD_eq_rankD2_add,
    universality_forces_idempotent, finite_universality_survivors, dualNumber_universality,
    rank2_excluded⟩

-- Axiom audit: expected `propext` only (core `Nat` rewriting) — free of `sorryAx`, `Quot.sound`,
-- and `Classical.choice`.
#print axioms universality_rank_rigidity_oracle

end UniversalityRankRigidity
