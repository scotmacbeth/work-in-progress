# Book Ch (transfer): the State pole of the liftings classification — WRITTEN

**MacBeth — WRITE session, 2026-08-11.** For Robin / Neil.

## What landed

`books/category-of-containers.tex`, subsection `sec:liftings-are-categories` (the "which
liftings, all of them" climax of the monads-and-comonads chapter). The **State pole** is now
written up and the classification is presented as **one theorem with two solved poles**,
unified by `π₀(position-threading action)`.

**Replaced** the outdated teachbox "The open frontier: State and general container monads"
(which flagged State completeness as `[open]`) with:

1. **`\subsection{The State pole: the store multiplication is invisible}`** (`sec:state-liftings`)
   - **Thm `state-classification`**: State liftings ≅ Cat, `C ↦ 𝕊×C`; aggregator
     grade-independent. Prov: MacBeth proved (object level; morphism level by mirror +
     exhaustive |S|=2 check); soundness Lean-verified (`StateProductLifting.lean`).
   - Proof-sketch "Why it holds — the store multiplication is a mirage": grade-independence
     (`sh_t`/`pr_t` inverse via outermost-object of associativity) → ASSOC-DEEP asymmetry →
     endpoint-locality → functor out of the codiscrete category → trivial holonomy → `𝕊×C`.
   - Remark "Why the graded category was a mirage": copresheaf is functorial but not
     endpoint-local ⟹ fails associativity; transitivity ⟹ fibres forced isomorphic.
2. **Teachbox "One theorem, two poles"**: table Reader (discrete, π₀=|E|) vs State (codiscrete,
   π₀=1). The astonishment: the store multiplication contributes *nothing* to the classification.
3. **Teachbox "An outside view"**: CBP (ter Horst–Mahadevan–Zambrano, `\cite{CBP}`, Thm 6.14) as
   structural resonance — trivial holonomy ⟹ global glue — explicitly NOT a container result.
4. **Teachbox "The frontier: general container monads are holonomy-full"** (replaces the naive
   "compute π₀" cliffhanger): today's PROVE result — Upd liftings ≅ Fun(𝔸(↓),Cat), holonomy-FULL;
   π₀ does NOT classify (Z2_triv: π₀=2 but 4 liftings). Reader/State = the two holonomy-trivial
   degeneracies (discrete action / reset-collapse). Genuine open beyond Upd & higher degree.

The surviving forward-glances (higher-order trees, store→Workers) still bridge into
`sec:moncomon-workers` and were left in place.

## Bib additions
- `\bibitem{CBP}` ter Horst–Mahadevan–Zambrano, arXiv:2601.04456 (2026) — deep-read, citable.
- `\bibitem{AhmanUustalu13}` Update monads, TYPES 2013.

## Flags for Robin/Neil
- **`AhmanUustalu13` is NOT yet in `reading/sources.json`.** I cite it only for the *definition*
  of the update monad (standard, and the target of today's proof), not for any claim. Please
  deep-read + upgrade in a browse session, or confirm the venue (TYPES 2013 post-proc, LIPIcs 26).
- **Novelty check deferred**: the Upd-liftings ≅ Fun(𝔸(↓),Cat) claim needs checking against
  Uustalu "Container combinatorics" (TTCS 2017) before any priority language leaves the book.
  The frontier teachbox already says "to my knowledge, new" + defers this.
- **State thm honesty**: object-level fully proved; morphism-level is the mirror argument +
  exhaustive |S|=2 machine check, not written in closed backward-β detail. Tagged as such.

Compiles clean: `pdflatex` → 85 pp, no undefined refs/cites. Structural scratch:
`scratch/write-2026-08-11-book.md`.

## Question for Neil (from WRITE.md, non-blocking)
I gave State its own `\subsection` climax rather than folding it into Reader's. Trivial resplit
if you'd rather one combined "two poles" subsection — say the word.
