# The (G)-obstruction cohomology is ALL citations — abelian AND nonabelian

**For:** Neil (and whoever finalises the pairwise ZS paper, PR #9 — now merged).
**Date:** 2026-06-12 (dream consolidation of the 06-12 browse).
**TL;DR:** Frame the H² remark as a *citation*, not a contribution. There is no new
cohomology theorem here — bank it in one line and move on (your "rabbit hole" call was right).

## What changed

On 06-11 I proved (G) ⟺ [ω] ∈ H²(Sk_C;𝒟) and *conjectured* it was Baues–Wirsching.
Two browse findings now make the whole tower established theory:

| Layer | Statement | Citation |
|-------|-----------|----------|
| Existence | DL ⟺ strict factorization system | **Rosebrugh–Wood**, JPAA 175 (2002) |
| Abelian classification | H²_BW classifies linear extensions of small categories; a ZS product with abelian fibre IS a linear extension, so (G)⟺[ω]=0 | **Baues–Wirsching**, JPAA 38 (1985) 187–211 |
| Nonabelian classification | nonabelian Schreier theorem `Tracks(π,G) ≅ H²(π,G)` for ALL small categories | **Pirashvili**, "Schreier Theory of Track Categories," arXiv:1512.03250, Thm 7 |

The nonabelian case (nontrivial left action) was sitting in my notes as the *next PROVE
target*. It is already a citation. **Do not prove it; cite Pirashvili.**

## What our genuine delta is (state it plainly)

Not new cohomology. It is: (1) the **identification** ZS-closure ⟺ linear extension /
track; (2) the **directed-container computation** — the rigid-twist family realizes the
explicit Z/2 generator, and the pairwise 4-object (non-groupoid D) case realizes the same
class; (3) the **Lean / container packaging**. Connective + concrete. That is enough; it
just isn't a new theorem in cohomology.

## Concrete action

- In the pairwise ZS paper's cohomology remark: cite Baues–Wirsching 1985 (abelian) and
  Pirashvili arXiv:1512.03250 (nonabelian); present (G)⟺[ω]=0 as a corollary of the BW
  linear-extension classification, with the rigid twist as our worked example. One
  paragraph, not a section.
- Still worth doing in Tallinn: talk to **Bumpus–Capucci** (ACT 2026) — their
  presheaf-cohomology local-to-global obstruction is the same shape as (G); offer the
  rigid-twist family as test cases.

## Where the real open frontier is (if we want a cohomology-adjacent PROVE target)

Not the classification — that's closed. The genuinely-open theorem in this neighbourhood
is **enriched DCont ≅ Cof** (Clarke–Di Meglio arXiv:2209.01144 state it as future work;
the programme has been stalled since 2022). V=Set recovers my Lean M4. That is a real
theorem with a natural Lean on-ramp — unlike the cohomology, which is now citations all
the way down.
