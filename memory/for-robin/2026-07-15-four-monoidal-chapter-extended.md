# The monoidal chapter, extended: closures + the duoidal interaction

**2026-07-15, write session.** The chapter Neil asked for is now the full deliverable he specified
in the 14 July email: the four structures *plus* the closed structures *plus* a section on how they
interact. It supersedes yesterday's `four-monoidal-structures.tex`.

## The file
`projects/papers/four-monoidal-chapter.tex` — **24pp, compiles clean** with `pdflatex`
(PDF: `four-monoidal-chapter.pdf`). Self-contained; drops into `books/category-of-containers.tex`
by deleting the preamble down to `\begin{document}` and turning the top `\section`s into the
chapter's sections (header comment explains). I did **not** touch the seed — per your instruction I
worked against a copy (`category-of-containers.SEED-COPY.tex`) and left the book untouched.

**I have not emailed this** — write-session rules bar me from sending mail. When you (or I, next wake
session) want it in Neil's inbox, the `.tex` + PDF are ready to attach. You can also just read them
off the projects volume.

## What is new vs. yesterday's 18pp draft
Yesterday's Theorems A / B⁺ / C are unchanged (they were already correct and honestly attributed).
Three additions:

1. **§ Closing the structures.** The Dirichlet internal hom (shapes = container morphisms) — *cited*
   to Niu–Spivak Ex. 4.78 / Spivak eq. (44), the formula is not mine. **What is mine is the Lean
   certification**: `DirichletClosed.lean` makes `(Cont,⊗,y)` a closed monoidal category, both
   round-trips `rfl`, zero axioms — believed the first machine-checked Dirichlet closure. Plus: the
   `◁` right-coclosure (cited, Meyers — with the left/right naming clash between the two Spivak
   sources flagged), and Cont CCC-but-not-LCC (Altenkirch–Levy–Staton). A `[computed]`-graded remark
   gives one uniform closure formula `[p,q]_⋆ = ∏_I q ◁ (p[I]⋆y)` unifying Spivak's eqs. (38)–(40),
   with the tempting converse left explicitly `[speculative]`.

2. **§ How the four interact.** The normal duoidal `(Cont,⊗,◁)` (cited Spivak–Srinivasan), with the
   comparitor as its spine, then the headline: **double comonoids in `(Cont,◁,⊗)` are exactly the
   sets of commutative monoids** (Thm, registry `comparitor-comonoid-nogo` = proved). Fibrewise
   Eckmann–Hilton. It corrects the natural "degenerate polynomials" guess *in both directions*
   (`y^{S_3}` wrongly in; `2y²` wrongly out). Remark scopes the delta honestly against Spivak's
   eq. (33): the converse direction + the commutativity it forces are mine; Indep, the iso-locus and
   the ⊗-comonoid classification are Spivak's.

3. **The erratum (§1.3) now has three items**, not two: I added the retraction of "the pentagon is
   trivial" — bad word, the fact is that `◁` coherence is `rfl` (a syntactic normal-form coincidence),
   Mac Lane is *pre-paid* not free. You/Neil pushed back on that wording and were right.

## Honesty ledger (so the referee in Neil doesn't have to dig)
- All four cited arXiv sources are at `deep-read` or `verified-quote` in `sources.json` — no floor
  below `deep-read`. `citation_check.py` **does** exist (it's in `projects/code/`, not `memory/` —
  the /write skill's path is still wrong; noted again).
- Grades in the text match the registry: A/B⁺/C/double-comonoid = `proved`; uniform closure formula =
  `computed`; closed-convolutional converse = `speculative`; the Lean closure = `lean-verified`.
- The "Jules Hedges ~10 relationships" section is deliberately **not** a manufactured list — I state
  the relations I can grade (interchange, comparitor, closures, double comonoids) and flag a full
  atlas as future work. I had no browse source for the enumeration and would not invent one.

## Still standing from yesterday
GitHub is policy-blocked by design (confidential Kodamai material) — I'm not trying to push. Delivery
is projects-volume + email. If Neil wants per-chapter PRs that's a you-and-him infrastructure
question; the chapter is drop-in ready either way.
