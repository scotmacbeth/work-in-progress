# Standalone paper drafted: "Effects and coeffects entwine on containers"

**2026-07-31 WRITE session.** First full draft of the Neil-steered standalone
effects-and-coeffects paper is done and compiling clean.

- **File:** `/home/agent/projects/papers/effects-coeffects-containers.tex` (+ `.pdf`)
- **Class:** amsart, `\author{MacBeth}`, **16 pages**, `pdflatex ×2`, **0 undefined refs,
  0 LaTeX warnings**. Main theorem (the dichotomy) lands on **page 2**.
- Shared by projects volume (no PR — seed is off GitHub). Robin can read the PDF directly.

## What it says (the spine Neil asked for on 07-30)
One monad `M` on Set, two container feeds — effect monad `T_M` (M on shapes, Ahman–Bauer)
and coeffect comonad `G_M` (M on positions, the transfer). The paper LEADS with the
unrestricted face:

1. **Bialgebra face — ALL M.** Canonical mixed distributive law `λ: T_M G_M ⇒ G_M T_M`
   (the oplax product-comparison `str`, on positions) satisfies the four entwining axioms
   for every M, branching or not. Plotkin–Turi λ-bialgebra: `G_M` on `T_M`-algebras,
   `T_M` on `G_M`-coalgebras. Nondeterminism (`Pf`), lists included. (Theorem 4.2)
2. **Arrow face — non-branching only.** Reverse compositor `κ: G_M T_M ⇒ T_M G_M` gives a
   biKleisli category / Hughes arrow / Freyd category over `(Cont,×)` **iff M non-branching**;
   sole obstruction = associativity E2′; branching also kills the effect strength by
   leaf-symmetry (a second, independent face). (Theorems 6.3, 6.7)
3. **Classification.** Cartesian non-branching M = **writer-with-absorbing-exceptions**
   `E + A×(−)` (A monoid, E left A-set); E2′ holds throughout. (Theorem 7.1)
4. **Machine-checked** Maybe arrow category (`BiKleisliMaybe.lean`, sorry-free). (§8)

The one-sentence takeaway I put in the conclusion: *the unification of effects and coeffects
is unconditional as a bialgebra and conditional as an arrow, and branching obstructs the
orientation of the interaction, not the interaction itself.*

## ⚠ Two citation TODOs (blocked on browse — I could not fix in a write session)
While provenance-checking against `reading/sources.json` I found **two neighbours are only at
`agent-summary` depth**, below the paper citation floor, so I did NOT formally cite them —
they appear as an uncited "neighbours read only in outline" paragraph in §9:
- **Goncharov et al. 2602.18295** (HO bialgebraic denotational semantics, ICFP 2026) — needs
  a deep-read, then a proper distinguishing citation.
- **Dumas–Duval–Reynaud 1310.0605** — "*Patterns for computational effects arising from a
  monad or a comonad*" (2013). Note: my WRITE.md draft-note and an early bibitem I wrote had
  the WRONG paper attached (a 2011 JSC "Cartesian effect categories are Freyd-categories");
  the correct 1310.0605 is the *Patterns* paper. Needs a deep-read + correct citation.

Both are flagged in `scratch/write-2026-07-31.md`. Neither is load-bearing for a theorem —
they are related-work neighbours — so the paper is honest and complete without them, but the
related-work section is one deep-read away from being fully cited.

## Honest gaps (all in the paper as Remarks, none hidden)
- mult-T general symbolic index-chase is mechanical (machine-verified incl. `Pf`) — Rmk 4.4.
- Scope = ∏-cointerpretation lifting; Dirichlet-⊗ arrow open — Rmk 7.4.
- Finite branching+non-commutative untested (`List` witness is infinite) — Rmk 7.4.
- Lean covers the Maybe arrow associativity only; general E2′ across the class not yet Lean.

## Open venue question
Target is arXiv → ACT or a semantics venue (MFPS/CMCS). Neil had the venue question from the
07-31 daily; if he lands on a specific venue I can recalibrate the background assumptions
(currently: container-defining, GSOS/bialgebra-literate).

— MacBeth
