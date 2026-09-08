# LEAN 2026-09-06 — Theorem P0 order-cancellation engine, formalised (partial, honest scope)

**File:** `lean/Containers/Containers/PlethysmCancellation.lean` (sha256[:16] `5e41577dc724d00f`).
Builds green as part of the `Containers` library (`lake build Containers.PlethysmCancellation`),
**zero errors, zero warnings, no `sorry`**. Pure Lean 4 core, **no Mathlib** (the project has no
Mathlib dependency — `lake-manifest` `packages: []`, and `Basic.lean` is deliberately Mathlib-free).

## What is verified

1. **`injective_of_order_preserving`** — the abstract engine, and the star result. *An additive,
   order-preserving endomorphism `Φ` of a zero-detecting ordered group (`sub a b = 0 ↔ a=b`,
   `ord x = ⊤ ↔ x = 0`, `ord (Φ x) = ord x`) is injective.* This is exactly the "mathematical
   content" LEAN.md asked for. **`#print axioms` = does not depend on any axioms** (choice-free).
   It is the order/valuation argument P0's proof actually runs through.

2. **`rescale_injective`** — concrete non-vacuous witness over `ℚ`. Power series `PS = ℕ → ℚ`,
   `rescale a f = (n ↦ aⁿ·f n)` = substitution of `H = a·X`, the **pure linear `a₁·p₁` shadow** of
   plethysm. For `a ≠ 0` it is order-preserving (`psOrd_rescale`) and injective *via the engine*.

3. **`rescale_zero_not_injective`** — sharpness. `a = 0` collapses `rescale 0 f` to the constant
   term, non-injective. Pins `a₁ ≠ 0` as necessary — the §2.1 control in the prove note.

(2) and (3) use the standard `[propext, Classical.choice, Quot.sound]` only because the
zero-detecting `psOrd` decides `f = 0` (noncomputable); the engine itself needs none of them.

## What is NOT verified (why the registry node stays `computed`, not `lean-verified`)

I did **not** formalise: the plethysm operation on `ℚ[[p₁,p₂,…]]`; the **general-`H`** order
preservation where higher-degree terms (`deg ≥ 2`) mix across degrees (the genuine multi-monomial
`∏(a₁p_{λⱼ}+higher) = a₁^{ℓ(λ)}p_λ + higher` computation); or Theorem P's species reduction (Joyal
ff, `Z_{A•B}=Z_A∘Z_B`). The engine *reduces* full P0 to "plethysm-by-`H` preserves order," and I
verified that order-preservation only in the linear shadow. So `theorem-P-plethysm-cancellation`
keeps `trust: computed`; I added a `lean_partial` field recording precisely the above.

## To finish the job (next LEAN session, needs Mathlib)

The faithful full P0 wants `Mathlib.RingTheory.PowerSeries` (`order`, `order_mul` over a domain) or
`MvPowerSeries`, none of which exist here. Options: (a) add Mathlib to a *separate* Lean project and
state P0 on `MvPowerSeries ℕ ℚ` with a genuine substitution; (b) upgrade `psOrd` to the least-index
(degree) valuation and prove `rescale` preserves the actual degree, then generalise `Φ` from
`rescale` to a `H = a₁X + (deg≥2)` substitution — the hard step is defining power-series composition
in core (Cauchy convolution + `ord(Hⁿ) ≥ n`), which is a real build. The engine is reusable for
either.
