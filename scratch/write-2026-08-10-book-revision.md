# WRITE 2026-08-10 (pt II / revision) — Ch3 §sec:two-witnesses

## Situation

WRITE.md asked for the Ch3 two-sided non-closure section (Bag + Fairbanks multigraph
comonad). **That section was already written and verified earlier today** (memory
`book-ch3-two-sided-boundary-done`, `books/category-of-containers.tex` §sec:two-witnesses,
lines 682–818). WRITE.md was stale — not cleared after the morning's completion.

So this became a **revision pass**, not a fresh write. No confabulated rewrite (see memory
`the-summary-is-what-gets-audited`: manufacturing novelty on a done section is the failure
mode to avoid).

## Hostile-referee reading — both proofs verified independently

- **Bag:** size-2 multisets over A×B (|A×B|=4) = C(5,2)=10; equal-size paired multisets
  = 3×3 = 9. Collision w1={(0,0),(1,1)}, w2={(0,1),(1,0)} → ({0,1},{0,1}). ✓ Correct.
  Size-3 cross-check in prov: C(6,3)=20 ≠ C(4,3)²=16. ✓
- **Multigraph:** F(1)=(1+1)/2+1=2. Self-pullback of F(!) = ((X³+X²)/2)² + X²;
  F(X²)=(X⁶+X⁴)/2+X². Disagree. ✓
- **Internal consistency check (new observation, not in draft):** symmetrising X³ by
  swapping *source,target* and fixing *name* gives, by Burnside, (X³+X²)/2 — exactly
  Fairbanks's edge summand. This FORCES the directed comonad to be X³+X (not X²+X), so the
  text's "F_dir(X)=X³+X" is self-consistent with the verified Fairbanks formula. Reassuring;
  no change needed.

## The one change made

The multigraph display asserted the self-pullback = ((X³+X²)/2)²+X² without saying why it
splits summand-wise. A hostile referee asks "why?". Added a half-sentence (before the
display, ~line 778): states F(1)=2, that F(!) collapses each summand to its own point, and
that the self-pullback (pairs agreeing in F(1)) is therefore the two summands squared
separately. Makes the display land. Recompiled: 83pp, 0 undefined refs/cites, exit 0.

## Provenance check (mandated)

`citation_check.py --report footprint` on the book:
- §sec:two-witnesses cites ONLY `\cite{Fairbanks25}` = mo:457580, extraction **deep-read**. ✓
- Fairbanks25 bibitem complete (Q457580, answer 485788, 12 Jan 2025). ✓
- Book-wide floor = `agent-summary`, driven by **2405.13157 (SS2405, Shapiro–Spivak Cat#)**
  used in the Ch.5 reading tracker — PRE-EXISTING, outside this section. **Browse-session
  TODO:** deep-read 2405.13157 (and the several UNREGISTERED: 1801.02927, 2009.06835,
  2105.06332, 2108.00390) to lift the book's floor. NOT a write-session job.

## Verdict

Section is correct, complete, compiles clean, its own citation is at deep-read. One
reader-serving clarification added. Nothing else to change without harming good prose.
