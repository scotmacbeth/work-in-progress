# ⋉/⋊ non-closed — proved, with a one-sidedness correction (2026-07-18)

**Proof:** `proofs/2026-07-18-dialectica-tensors-non-closed.md`. **Check:** `scratch/nonclosed_check.py`.

## The results

Let `(p⋉q)[(s,t)] = p[s]^{S_q} × q[t]^{S_p}` (symmetric) and `(p⋊q)[(s,t)] = p[s]^{S_q} × q[t]`
(directed) be DJN's two tensors on Cont (unit `y`) — **their §6 formulas; the
name "Dialectica" is my own identification, not DJN's, who ask what they mean.**

- **Theorem 1.** `⋉` is neither left- nor right-closed. Witness `p = q = y²`: both `p⋉(−)` and
  `(−)⋉q` fail to preserve `y+y` (direction profile ⟨4,4⟩ vs ⟨2,2⟩), so — a left adjoint preserves
  colimits (Mac Lane V.5) — neither has a right adjoint.
- **Theorem 2.** `⋊` is **not right-closed** (`p⋊(−)` fails identically). **But `(−)⋊q` DOES
  preserve binary coproducts** for every `q`. The obstruction is **one-sided**.

## Why this was worth a session (the correction)

The companion note (`2026-07-17-ltimes-rtimes-dialectica.md` §A.3(ii)) said "the same computation
kills ⋊." **That is false in the left variable.** For `(−)⋊q`, the exponent `S_q` is *fixed* and
`(p₁+p₂)[s]` at a summand shape is just `pᵢ[s]`, so `((p₁+p₂)⋊q) ≅ (p₁⋊q)+(p₂⋊q)` by plain
distributivity `(S_{p₁}⊔S_{p₂})×S_q ≅ (S_{p₁}×S_q)⊔(S_{p₂}×S_q)` — an honest container iso, verified
with actual direction *sets* not just cardinalities. The exponent only eats the coproduct when the
*varied* shape set sits in it. So:

| functor | growing exponent? | preserves `+`? | right adjoint? |
|---|---|---|---|
| `p⋉(−)` | `p[s]^{S_q}` yes | no | no |
| `(−)⋉q` | `q[t]^{S_p}` yes | no | no |
| `p⋊(−)` | `p[s]^{S_q}` yes | no | no |
| `(−)⋊q` | none (S_q fixed) | **YES** | not refuted |

The punchline (§4): **the closure obstruction inherits ⋊'s directedness.** ⋊ fails closure exactly
on the side the exponent reaches. Slogan: *`(−)⊙q` loses coproducts iff the varied shape set appears
in an exponent of the direction formula* — reads off closure for all four Cont tensors at a glance.

## What I need / what's open

**Open Question 5 (my next PROVE target): is ⋊ left-closed?** The coproduct obstruction is gone, but
that only means `(−)⋊q` *might* be a left adjoint. To settle it: either (i) show `(−)⋊q` preserves
all small colimits (coequalizers in `Cont ≃ Fam(Set^op)` are **not** shapewise — genuinely untested)
plus an accessibility/solution-set condition, or (ii) construct the internal hom `[p,−]_⋊` directly.
My conjecture: **YES**, ⋊ is left-closed — which would make it a *directed-closed* monoidal category,
a clean and (I think) unusual example. If you have intuition on colimits in Fam(Set^op) beyond
coproducts, that's the crux.

**Lean:** Theorems 1–2 are Lean-ready (finite witness; only non-elementary input is
`Adjunction.rightAdjoint`/`preservesColimits` from Mathlib). Not attempted this session.

**Chapter erratum owed:** `four-monoidal-chapter.tex` §10 and note §A.3(iii) both say "neither ⋉ nor
⋊ is left-closed" — should read "⋉ not left-closed; ⋊ not *right*-closed (left-closure open)."
