# Write session 2026-07-31 — editorial polish of effects-coeffects-containers.tex

## Mandate (WRITE.md)
Editorial polish ONLY. Structurally complete 19pp, clean compile. NO new structure, NO new claims.
Venue HELD (awaiting Neil). Polish venue-independently.

## Five polish tasks
1. Abstract — tighten to crisp ≤200 words.
2. Intro — flow; explicit contributions list, each cross-refs its section/theorem.
3. Consistency sweep — notation (T_M,G_M,κ,λ,Arr_M,E+A×(−)), thm numbering, all refs/cites resolve, no orphan macros.
4. Conclusion — three-modes context + open Atkey index-degree Q as honest "further work", no overclaim.
5. Recompile ×2, zero undefined, report page count.

## Baseline observations (first full read)
- Paper reads very well already. Dense MacBeth prose but disciplined.
- Abstract currently ~250 words (over target). Candidate for trimming.
- Main result (Thm 1.1) stated by ~p.3 — GOOD, within reach.
- Notation looks internally consistent on first pass.
- Conclusion has three-modes para in Related Work (§8) AND open Qs in §9. The Atkey
  index-DEGREE question: memory says the index-degree conjecture went NEGATIVE (07-31),
  dichotomy is Boolean not graded. Must NOT claim graded story. Check Rmk 5.11 (rem:atkey)
  and conclusion for any overclaim re: index-degree.

## Decisions / changes made (all 5 tasks done)

1. **Abstract** — rewritten, ~270→185 words. Every claim preserved (two feeds, λ all-M,
   κ iff non-branching, E+A×X class, Hughes/Freyd, two-axiom failure). Tighter openers,
   "another story" pivot. Under 200 ✓.

2. **Intro contributions** — added cross-refs in the "Third" worth-stating point:
   associativity → (Theorem 4.x arrowsA), strength → (Lemma 5.x strong). The other
   contributions already cross-ref via the main-theorem parts (1)–(3) map. Did NOT add a
   separate bulleted "Contributions" list — the main theorem + three worth-stating points
   already serve as an explicit, cross-referenced contributions statement; a bullet list
   would bloat an already 2pp intro.

3. **Consistency sweep**
   - Removed 2 orphan macros: \Poly, \Cat (defined, never used).
   - Standardized Turi--Plotkin (author order, matches \cite + "Turi and Plotkin" prose);
     was mixed Plotkin--Turi (4×) / Turi--Plotkin (1×). Now 5× Turi--Plotkin.
   - biKleisli / coKleisli / non-branching (37×) / coeffect (37×) already consistent.
   - All \ref/\cite resolve (0 undefined in .log). No multiply-defined.

4. **rem:atkey CORRECTION (the substantive one)** — the draft claimed "non-branching =
   Atkey index trivialises → non-indexed Freyd category." This is FALSE per my own 07-31
   PROVE session (proofs/2026-07-31-atkey-index-degree.md, Prop 2.1 + Cor 2.3):
   index-collapse (G_M=Id) ⟺ M=Id, STRICTLY inside non-branching (Maybe/Writer are
   non-branching with G_M≠Id yet still Freyd via the STRENGTH, not index-collapse).
   Rewrote to the honest statement: the branching axis and Atkey's index (=coeffect) axis
   are orthogonal; index-collapse is M=Id ⊊ non-branching. Kept the correct verbatim-
   construction opener and the branching-degrades-below-arrow closer. This is aligning the
   paper to established (my own) proof notes, NOT new mathematics. Honesty > leaving a
   known-false interpretive remark.

   **Conclusion further-work bullet** — added "A graded refinement?": states honestly that
   the two NATURAL gradings are ruled out (arity gap: cartesian max-arity ∈ {≤1,∞}, n↦n²
   self-plug, no finite rung; leaf-count grade killed by μ^T merging), leaving the
   coeffect-side graded-comonad question open. Did NOT cite Vollmer–Paviotti–Orchard
   (not-yet-arXiv, not deep-read) — phrased generically as "a graded comonad on G_M".
   Attributed the arity-gap facts to "a companion analysis" (my notes), not restated as a
   numbered theorem — respects "no new structure".

5. **Compile** — pdflatex ×2, exit 0, **19 pages**, 0 undefined refs/cites. Citation
   footprint floor = deep-read (unchanged; no new cites). Fixed the egregious 65pt overfull
   in the §5 dichotomy table (was pre-existing) by \small + centered box + arraycolsep 4pt,
   dropping the redundant "(no overlap)" cell (its meaning is in the adjacent prose).
   Remaining overfulls all ≤30pt, in theorem-head lines / unbreakable display math —
   acceptable for a share-ready draft.

## NOT changed (out of scope, honest flags left in place)
- rem:e2gap and rem:scope mechanical-gap flags untouched (Lean session problem).
- No new proofs, no new theorems, no structural changes.
- Venue still HELD (Neil). Container-background level unchanged.
