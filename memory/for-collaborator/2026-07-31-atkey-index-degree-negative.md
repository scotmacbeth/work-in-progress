# Atkey index-degree conjecture: RESOLVED NEGATIVE (the dichotomy is genuinely Boolean)

**MacBeth, PROVE 2026-07-31 (pm).** For Neil/Robin. Proof:
`proofs/2026-07-31-atkey-index-degree.md`. Registry node `atkey-index-degree` (proved) under
`effect-coeffect-arrows.json`.

## The question
PROVE.md conjectured the non-branching dichotomy (`Arr_M` a Freyd category ⟺ M non-branching) is
secretly a **graded** Freyd statement: Atkey's index of `Arr_M` graded by M's arity, so "arity ≤ 1"
is the bottom of a tower "arity ≤ n". Hoped-for outcome: a degree refining the Boolean ON/OFF.

## The answer: NO — and three reasons why, plus one corrected identification

1. **The conjecture conflated two distinct, nested boundaries (the key correction).** Collapse of
   Atkey's index to a *plain* (non-indexed) Freyd category means the coeffect comonad `W = G_M`
   becomes trivial — and `G_M = Id ⟺ M = Id`. That is **strictly stronger** than non-branching
   (`M = E + A×X`, which contains `Maybe`, `Writer`, all with `W ≠ Id`). So
   `{M=Id} ⊊ {non-branching} ⊊ {all}`. Atkey's index measures the **coeffect** (`M ≠ Id`) — an axis
   *orthogonal to and coarser than* branching. "Non-branching = index collapse" is false; they are
   different boundaries. **This sharpens the paper's Atkey remark and is citable on its own.**

2. **Arity gap — the arity axis has no rungs.** A cartesian monad has max arity ∈ {≤1, ∞}: a
   max-arity-`n≥2` shape plugged into its own `n` leaves is an M-shape of arity `n²>n`. So "arity
   ≤ n" for finite `n≥2` is empty of monads; the invariant is two-valued. Boolean because the
   underlying invariant is two-valued.

3. **The leaf grade is destroyed by merging.** The natural `(ℕ,×)` leaf-count grade fails: `Pf`
   uniform-leaf arrows are still non-associative (computed), because idempotent-union `μ^T` merges
   (grade non-multiplicative). And within the ∏-cointerpretation class *branching forces merging*
   (multiset/List are excluded — `μ` would repeat leaf labels), so **Theorem A stands uncorrected**:
   branching and merging are inseparable in the valid class.

## What this means for the grant / paper
- The effects⊗coeffects paper's Atkey remark should state the **nesting** (index-collapse `M=Id`
  ⊊ non-branching), not equate them. The dichotomy is Boolean *by design of the invariant*.
- The "graded" story the field is building (Earnshaw–Nester–Román PCM-graded ≅ Freyd; Vollmer–
  Paviotti–Orchard `Gmd`) grades along **other** axes; the arity axis is not gradeable — one more
  confirmation the arity dimension is genuinely ours and genuinely two-valued.

## Honest limits (see proof §8)
- I refuted the two *natural* gradings + corrected the boundary. I did **not** prove "no grading
  whatsoever" (would quantify over all PCMs). The conjecture *as stated* is refuted.
- **Open:** a grading on the **coeffect** side (graded comonad `G_M`, Vollmer–Paviotti–Orchard
  `Gmd`, CT2026) — inaccessible this no-browse session. Worth a browse pass when it hits arXiv.
- Atkey ENTCS 229's exact indexed-Freyd definition was **not** deep-read (the PROVE.md gate;
  deferred under no-browse). §2 is built so it does *not* depend on Atkey's precise axioms — only
  on "plain Freyd = no coeffect" + my Theorem B. A line-by-line match to Atkey's Def. is still owed
  before any *positive* index claim.

## Links
[[branching-obstruction-is-atkeys-index]] · [[affine-classification-writer-exceptions]] ·
[[effect-coeffect-arrows-first-strength]] · [[three-modes-of-composition]]
