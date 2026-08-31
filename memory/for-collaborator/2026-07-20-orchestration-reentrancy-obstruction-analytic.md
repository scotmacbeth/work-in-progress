# Re-entrancy obstruction theorem — PROVED (analytic), 2026-07-20

**For:** Neil, Robin. **Status:** orchestration-zs node promoted COMPUTED → **PROVED**.
**Artifact:** `projects/proofs/2026-07-20-orchestration-reentrancy-obstruction-analytic.tex`
(compiles, 6 pp). **Cross-check:** `projects/scratch/orchestration_zs_parametrized.py`.
**Registry:** `proofs/registry/orchestration-zs.json` (status `proved`, validates under macbeth.json).

## What is now proved

The surviving-novelty layer of the orchestration programme (the Zappa–Szép obstruction,
*not* the interface=container mechanism, which is Aberlé/Spivak prior art) is proved cleanly.

Parametrize the minimal supervisor–worker handoff category by a **single token-mutation bit**
`ε ∈ ℤ/2`: the re-entrant worker outcome sends the dispatch to `s₂∘p = q·τ^ε` (`s∘p = q` fixed by
normalization). So `ε=0` = worker *fixes* the supervisor's turn token, `ε=1` = worker *mutates* it.
Fix the token-internal moves `D = {id_S, τ, id_W, id_R}` as the right factor.

> **Theorem.** `[ω(K_ε)] = ε·(generator)` in `H²(Sk_C; D) ≅ ℤ/2`.
>
> **Corollary (re-entrancy dichotomy).** `K_ε = C ⋈ D` (a distributive law / Zappa–Szép product /
> serialization into one joint agent) exists **iff `ε=0`, i.e. iff the worker fixes the token**;
> and for `ε=1` the obstruction is the nonzero generator of `H² ≅ ℤ/2` — the unprotected-re-entrancy
> failure mode.

**The degree-two obstruction class equals the token-mutation bit, on the nose.** That is the crisp
statement I did not have before: one bit of behaviour (does a callee mutate caller state during a
pending call?) *is* the cohomology class that decides composability.

## Why this is more than the 19 July "computed" note

The old note relied on (a) a **machine-verified isomorphism** `K_bug ≅` ten-morphism rigid twist to
transport the H² class, and (b) **brute-force `#SFS` counts**. Both are gone. The new proof:

1. verifies **(L)** (freeness) and **hypothesis (H)** for the whole family `K_ε` **by hand**;
2. applies the *general* `(G)⟺[ω]=0` classification (T3) — the rigid twist was only *its example*,
   so there is no circularity — and computes `Sk_C`, the presheaf (all restrictions zero), the
   complex (`C³=0 ⇒ H² = (ℤ/2)²/diagonal ≅ ℤ/2`), and the defect `ω_T = (0,ε)` **analytically**;
3. chains (T2 pairwise-ZS) + (T3 g-obstruction) into the iff.

The iso to the rigid twist survives only as a *remark/corollary*. The gain is **uniformity**: the
single instance became the parametrized identity `[ω] = ε`.

## Honesty ledger

- Scaffolding (T2, T3, the H² machinery = Baues–Wirsching / Rosebrugh–Wood) is **cited, not reproved**.
- **No new cohomology.** The models are **minimal faithful abstractions** of the two-worker
  re-dispatch pattern — I do *not* claim any named framework (LangGraph etc.) *is* `K_ε` (registry
  dead-end). Empirical GA-style instantiation is the future step.
- The two composing regimes (independent → `C×D`; coherent → `S₃`) stay **computed context**, not part
  of the proved core.

## Grant relevance (Impact anchor)

Unprotected re-entrancy in agent orchestration **is a nonzero degree-two class on the handoff
category** — one degree above the H⁰/H¹ sheaf-Laplacian invariants the MAS literature puts on the
*communication* graph (consensus / identifiability). This is the composability differentiator, and it
is now a theorem, not a computation.

**Suggested next:** Lean the `[ω(K_ε)]=ε` computation (the H² machinery is finite `𝔽₂` linear algebra
— tractable), and/or an empirical instantiation showing a real re-entrant orchestration exhibits the
`ε=1` signature.
