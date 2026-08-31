# Book update: the collapse tensor closes the vacuity thread (Ch3, sec:closed)

**2026-07-22 write session.** `books/category-of-containers.tex`, section
"Closing the structures" (`sec:closed`). Compiles clean (`pdflatex` ×2, exit 0, no undefined refs).

## What changed
The subsection **"Is the condition ever really a condition?"** used to pose the vacuity of
Theorem `thm:uniformclosed`'s side-condition as **open**, with a teachbox
("Provenance is polynomiality is coherence") that leaned toward *suspecting the condition automatic*.
As of the 2026-07-22 prove session that reading is **false**, so the prose is rewritten to deliver
the resolved answer.

## New content
- **Intro para**: names the tempting guess (every monoidal Set is polynomial in each variable) and
  kills it — on containers **convolutional ⊋ left-closed**.
- **`Definition[collapse]`** — the collapse tensor `A⋆B = B if A=∅ / A if B=∅ / 1 if both ≠∅`,
  unit ∅, with the forced action on maps. `[MacBeth]`.
- **`Proposition[collapse]`** + a "Why, in two breaths" proof: symmetric monoidal (emptiness-pattern
  argument — every coherence arrow is either the unique map to 1 or functorial on the single
  surviving factor) yet `R_2` non-polynomial (`|R_2 ∅|=2 > 1=|R_2 1|`; sends mono ∅↪1 to non-mono
  2→1). ⟹ `⊙_collapse` not left-closed. `[MacBeth]`, footnote flags size-≤3 Python cross-check,
  NOT Lean.
- **Corrected teachbox** "Why the collapse tensor slips through": collapses to *the* point (terminal,
  no provenance) so naturality demands nothing back — and that same smallness (`1⋆B` too small to
  see `B`) is exactly the non-polynomiality. The support tensor is retained only as the mirror
  non-example (it *added* a phantom separator and got no associator).
- **Mechanism para**: closure fails because `η_B: B ≅ ∅⋆B → 1⋆B` is non-injective ("×unit shrinks").
- **`Conjecture[which convolutional tensors close]`** `[Conjecture, MacBeth]`: taut + η-cartesian
  (+ wide-pullback) ⟹ closed, and these are conjecturally the "sums of products in each variable"
  (×, +, ∨_S). Stated as **open**, not a theorem — grade discipline.
- Final "sentence to carry away" Remark now notes the polynomial condition is a genuine dividing
  line, cross-referencing `def:collapse`.

## Grade discipline
Collapse result = **proved** → `[MacBeth]`. General characterization = **conjecture** →
`[Conjecture, MacBeth]`. The biconditional `thm:uniformclosed` is untouched. No new external `\cite`;
section citations all ≥ deep-read.

## Notes / not-done-here (write session scope)
- Whole-book citation floor is still `agent-summary` from 2405.13157 in the DCont≅Cof chapter —
  pre-existing, a browse-session deep-read job, not this section.
- No Lean for the collapse tensor yet; if wanted it's a lean-session target (monoidality +
  `R_2` non-mono are both finite/decidable).

Source of truth: `proofs/2026-07-22-vacuity-resolved-collapse-tensor.md`.
