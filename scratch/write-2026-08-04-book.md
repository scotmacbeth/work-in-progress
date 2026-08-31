# Write session 2026-08-04 — fold two-feeds into book Ch "Monads and comonads"

## Situation
WRITE.md: paper PAUSED (Neil 08-02). Fold two-feeds material into book
`projects/books/category-of-containers.tex`, Ch "Monads and comonads" (ch:moncomon).
Use `/book` skill. Lead with Neil's UID-88 **profunctor Arr_M on Cont** framing.

## What is ALREADY in the book (audit result — all present, coherent)
- Transfer G_M(S,P)=(S,M∘P): §sec:moncomon-transfer (2282). Full: fibrational teachbox,
  coclosure/Lan remark, Ahman–Bauer novelty demarcation, Maybe example. ✅
- Entwining λ: T_M G_M ⇒ G_M T_M: §sec:moncomon-entwine (2452), thm:entwine. str=oplax
  product-comparison; branching obstruction for reverse (Pf, ex:entwine-branching);
  dichotomy table; rem:entwine-scope (honest open general-Mendler). ✅
- Arrow κ + classification: §sec:threemodes (3012), thm:arrows. Arr_M(p,q)=Cont(G_M p,T_M q),
  category iff non-branching iff M≅E+A×(−). Two-faces paragraph (3139). ✅

## The GAP Neil's UID-88 flags ("lead with profunctor Arr_M on Cont")
- The word/concept **profunctor** appears NOWHERE. Arr_M is presented only as a hom-assignment.
- In the two-feeds subsection (Monads-and-Comonads ch, where G_M/T_M live), the reverse κ is
  presented ONLY negatively ("fails mult-T"). Arr_M never introduced there — reader meets it
  50 lines later in a different chapter.
- The explicit biKleisli composite (δ–Gf–κ–Tg–μ^T) is in lambda-kappa-note but NOT in the book.

## Decision
PRIMARY edit: add a closing movement to §sec:moncomon-entwine (after line 2594, before
rem:entwine-scope) that:
  1. reframes the "failed" reverse κ as the compositor of an **arrow calculus**;
  2. Definition `def:arrowprof`: Arr_M(p,q)=Cont(G_M p, T_M q) is a **profunctor**
     Cont^op×Cont→Set for EVERY M (both feeds are functors — free, no proof needed);
  3. names κ, gives the explicit biKleisli composite + identity η^T∘ε;
  4. astonishment (teachbox): **the profunctor is free; the CATEGORY is what branching costs**;
  5. forward-ref thm:arrows for classification + one line E+A×(−) answering Neil UID-85
     restrictiveness worry (writer+exceptions = logging-with-failure, not tiny).
COHERENCE edits: §sec:threemodes effect-coeffect para + thm:arrows reference def:arrowprof and
use the word "profunctor"; don't re-introduce κ/Arr_M as new.

Honesty: profunctor claim is immediate from functoriality of G_M, T_M (both established) — an
Observation, NOT a new theorem. Tag exposition. No new proofs (WRITE.md rule).

## Macro added
\newcommand{\Arr}{\mathsf{Arr}} in preamble.

## Composite (from lambda-kappa-note def:arr, verified)
id_{p⤳p} = η^T_p ∘ ε_p.
g∘f = μ^T_r ∘ T_M g ∘ κ_q ∘ G_M f ∘ δ_p : G_M p → T_M r.
Freyd pure functor arr(φ)=η^T_q ∘ φ ∘ ε_p for φ:p→q.

## DONE
All edits landed. `category-of-containers.tex` compiles clean (2-pass), 66pp, 0 undefined
refs, no new overfulls, no new citations. Placement:
- def:arrowprof + arrow movement + teachbox inserted in sec:moncomon-entwine (after the
  "one direction only" branching-obstruction close, before rem:entwine-scope). Narrative:
  "reverse κ fails as a global law → but that failure IS the arrow compositor → profunctor
  free, category costs branching → E+A×X boundary".
- sec:threemodes effect-coeffect para + thm:arrows + two-faces bullet now reference
  def:arrowprof and use profunctor language.
Disclosure + for-robin note + memory (neil-steer-2026-08-04-pause-paper) updated.
No git push (projects/ not a repo); no email (write-session rule). Share pending email phase.
