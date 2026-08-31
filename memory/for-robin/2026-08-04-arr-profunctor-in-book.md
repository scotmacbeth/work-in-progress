# The arrow profunctor Arr_M, now leading the two-feeds story in the book

**Date:** 2026-08-04 (write session)
**File:** `projects/books/category-of-containers.tex` (66pp, compiles clean, 0 undefined refs)
**Section touched:** Ch "Monads and comonads", §"The two feeds entwine" (`sec:moncomon-entwine`);
light coherence edits in §"Three modes of composition" (`sec:threemodes`).

## Why
WRITE.md (from Neil's 08-02 steer): the standalone effects–coeffects **paper is paused** — the
material is container theory and belongs in the book. And Neil's UID-88 note asks to **lead with
the profunctor `Arr_M` on Cont** framing. When I audited the chapter, the mathematics was already
all there (transfer, entwining λ, the arrow classification `thm:arrows`, the two-faces summary) —
but the *word* profunctor appeared nowhere, and the reverse compositor κ was presented only as a
**failure** ("the reverse orientation fails mult-T for branching") in the very chapter where the
two feeds `G_M`, `T_M` are built. The reader met `Arr_M` only 50 lines later, in a different chapter.

## What changed (exposition/placement only — no new math, no new proofs, no new citations)
A closing movement added to §"The two feeds entwine", reframing κ's "failure" as the thing it is
*for*:

- **`Definition def:arrowprof` — the arrow profunctor.** `Arr_M(p,q) := Cont(G_M p, T_M q)`. Because
  both feeds are *functors* on Cont, this is a profunctor `Cont^op × Cont → Set` for **every** monad
  M — contravariant in p via G_M, covariant in q via T_M. Identity `η^T ∘ ε`; explicit biKleisli
  composite `μ^T · T_M g · κ · G_M f · δ`.
- **The astonishment (teachbox):** *the profunctor is free; the category is what branching costs.*
  The underlying data of "an effect–coeffect arrow p⤳q" always exists — it is just a container map
  out of `G_M p` into `T_M q`. What is **not** free is that these arrows *compose* associatively —
  that `Arr_M` be the hom-profunctor of an actual category (a Freyd category over `(Cont,×)`). That
  needs the compositor κ to be coherent, and κ is coherent **iff M is non-branching** (`thm:arrows`).
  Branching does not destroy the arrows; it destroys their *composition*.
- **Neil's restrictiveness worry (UID-85), answered inside the text:** the non-branching (Π-liftable)
  monads are exactly the **writer-with-exceptions** monads `MX ≅ E + A×X` — the effect monads of
  logging-that-may-fail. Not a curiosity; a boundary, not a defect.

Coherence: `sec:threemodes` and `thm:arrows` now *reference* `def:arrowprof` (using "profunctor" /
"hom-profunctor of a category") instead of re-introducing κ and the arrows as if new.

## Status / open (unchanged from prior sessions — flagged, not touched)
- Entwining λ proved for the Π-cointerpretation class; general Mendler case open (`rem:entwine-scope`).
- `thm:arrows` associativity axiom E2′ proved in coordinates + machine-checked for the Set-monad
  examples; not yet Lean-certified in general (tag `[MacBeth]`).
- Book citation floor still agent-summary (pre-existing 2405.13157); this session added no sources.

Working copy is `projects/books/category-of-containers.tex`; you can read it from the host. Happy to
send the PDF once email is back in the loop (this was a no-email write session).
