# Lean: `[ω] = ε` machine-checked (re-entrancy obstruction, finite 𝔽₂ core)

**Date:** 2026-07-21 (lean session)
**File:** `lean/Containers/Containers/Reentrancy.lean` (sorry-free, wired into root `Containers.lean`)
**Registry:** `orchestration-zs.json` → new `lean-verified` child `lean-omega-equals-epsilon`
under `class-equals-bit`.
**Source proof:** `proofs/2026-07-20-orchestration-reentrancy-obstruction-analytic.tex`
(§"Normalized cochain complex", §"The obstruction class equals the token-mutation bit").

## What is now machine-checked

The **finite class computation** of the grant-Impact orchestration theorem. The
analytic proof reduces the categorical obstruction to a tiny complex over 𝔽₂;
this Lean transcribes that complex and verifies the class computation on it:

- `C2 := Bool × Bool` — the 2-cochains `C² ≅ 𝔽₂²` (𝔽₂ = `Bool`, `xor` = `±`).
- `d1 t := (t, t)` — the coboundary image `B² = im δ¹ = ⟨(1,1)⟩` (diagonal), after
  reparametrising `δ¹`'s 1-dim'l source by `t = h[p] − h[q]`.
- `omega ε := (false, ε)` — the transversal defect cocycle `ω_T = (0, ε)`.
- `phi (a,b) := xor a b` — the gauge-invariant class map `(a,b) ↦ b − a`.

Theorems:
- **`phi_omega : phi (omega ε) = ε`** — the sharp *class form* of `[ω] = ε`.
- **`omega_inB2_iff_zero : InB2 (omega ε) ↔ ε = false`** — *membership form*
  `[ω] = 0 ⟺ ε = 0` (⟺ the Zappa–Szép product `K_ε = C ⋈ D` exists).
- `phi_ker_eq_inB2 : phi x = false ↔ InB2 x` — `ker φ = B²`, so `φ` descends to an
  injective `H² = C²/B² → 𝔽₂`.
- `phi_surjective` — with the above, this gives the iso `H² ≅ 𝔽₂`.

`#print axioms`: `phi_omega`, `phi_surjective`, `omega_class_zero_iff` depend on
**no axioms**; `omega_inB2_iff_zero`, `phi_ker_eq_inB2` depend only on `propext`.
No `sorry`, no `Classical.choice`.

## What is NOT checked (honest grading)

The **reduction** of the categorical obstruction `[ω] ∈ H²(Sk_C; 𝒟)` to this
finite complex (orbit category `Sk_C`, presheaf `𝒟`, `C³ = 0`, defect =
`(0, ε)`) stays the paper's `proved` step — it is *transcribed* here, not
re-derived. So `class-equals-bit` remains `proved`; only its finite-arithmetic
tail is `lean-verified`.

## Design note

The project is **pure core Lean, no Mathlib** (matches `Basic.lean`,
`ZappaSzep.lean`). LEAN.md suggested Mathlib's `ZMod 2`/`Submodule.Quotient`, but
adding Mathlib to a no-Mathlib build is a heavy, risky change for a computation
that is entirely finite. `Bool` with `xor` **is** the additive group of 𝔽₂
(`false = 0`, `true = 1`); everything is a 4-element case check. I judged the
in-style pure-core route the honest, low-risk deliverable. If Robin/Neil want a
Mathlib `ZMod 2` version for the paper's citation, that's a follow-up (would need
Mathlib added to the lake config).

For the paper `papers/containers-for-orchestration.tex`: it can now cite a
Lean-verified `[ω] = ε` (upgrade the grant claim from "proved on paper" to
"machine-checked finite core").
