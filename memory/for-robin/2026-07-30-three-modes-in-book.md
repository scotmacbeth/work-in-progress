# For Robin — Three-modes-of-composition synthesis is now in the book (2026-07-30 write)

**File:** `projects/books/category-of-containers.tex` (readable from the host; no GitHub — seed is off-repo).
Backup of the pre-edit version at `/tmp/coc-backup-threemodes.tex`.
**Build:** compiles clean with `pdflatex` (×2), **64 pages**, **0 undefined references**, no citation warnings.

## What landed
A new capstone **§ "Three modes of composition"** (`\label{sec:threemodes}`) at the **end of Chapter 8**
("Composing systems: Zappa–Szép and distributive laws"). Placement rationale: Ch8's title already covers
mode 1 (ZS) and mode 3 (distributive laws); all three modes are developed by the end of Ch8, so the table
has **no forward references**. It also gives a previously thin chapter real weight and completes the
"two axes → three axes" framing that the Workers section had flagged `[in development]`.

The section delivers:
1. **The three-modes table** — directed/ZS (`[ω]∈H²`, may fail), state/Workers (no obstruction, grade
   multiplies `S×T`), effect–coeffect (branching obstruction, exists iff `M` non-branching). Explicit
   "do NOT collapse into one master obstruction" paragraph.
2. **Theorem `\ref{thm:arrows}`** developing mode 3 (new to the book): effect–coeffect arrows
   `G_M p → T_M q` form a Hughes-arrow/Freyd category iff `M` non-branching; positive class =
   writer-with-absorbing-exceptions `E + A×X` (A monoid, E a left A-set); E2′ holds across the whole class.
   Tagged `[MacBeth]` with an honest footnote on Lean status (unit fragment checked in BiKleisli.lean,
   E2′ machine-verified for examples only, not committed to this tree).
3. **The branching double-duty paragraph** (the deepest point): one entwined structure, two faces —
   bialgebra `λ:TG⇒GT` exists for ALL M (Plotkin–Turi YES), arrow `κ:GT⇒TG` exists iff non-branching.
   Obstruction = which *direction* you commute effect past coeffect.
4. **KRU neighbour Remark `\ref{rem:kru}`** — their interaction laws are *pairings* (Chu/Day monoid
   objects), not our compositor; distributive laws are inputs to their machinery, never outputs;
   their degeneracy Thms 1–3 = extensive-category sibling of our arity criterion.
5. **"For the grant: Path 5"** framing paragraph.

## Also changed (2 small edits in Ch7)
- The Workers "two axes" grant paragraph now points forward to §threemodes (third axis).
- The `[in development]` teachbox is de-flagged: the arrow category is now developed (Thm arrows);
  only the *Workers-embed-into-arrows* sub-question stays open.
- New bib entry `\bibitem{KRU20}` (Katsumata–Rivas–Uustalu, FoSSaCS 2020 / arXiv:1912.13477).

## Provenance note
KRU 1912.13477 was stale in `reading/sources.json` at `agent-summary`, but I have a full-text deep-read
note (`reading/2026-07-29-katsumata-rivas-uustalu-1912-13477.md`). I upgraded the sources.json entry to
`deep-read` to match the existing artifact (bookkeeping catch-up, not new browsing). Both citations in the
new section (KRU20, AhmanBauer24) are now at deep-read. The book's *overall* footprint floor stays
`agent-summary` due to **pre-existing** citations (2405.13157, 2503.21974, 2508.00727, 2111.10968) — each
already hedged in the book's tracker appendix; not touched this session.

## Not done (deliberately deferred)
- arXiv:2607.23228 (LS-category / directed-homotopy invariant) — WRITE.md said cite only if a close read
  confirms the parallel to `[ω]=0 ⟺ global coherence`. Not deep-read → omitted, not even as a footnote.
- Lean for the Set-monad-level classification (`monad ⟺ monoid with left-zero ideal`) — a LEAN target.
