# Book Chapter 6 "Monads and Comonads" — drafted

**Date:** 2026-07-23 (write session)
**File:** `projects/books/category-of-containers.tex` (read it directly on the projects volume — the
book is off GitHub, so no PR). Compiles clean with `pdflatex` (48 pp, 0 new overfull boxes).
**Pre-edit backup:** `/tmp/coc-backup.tex` (in case you want a diff).

## What this is
Neil's 07-23 steer was: next book chapter = **"Monads and Comonads"**, a 3-milestone spec promoting
the old Phase-2 §7.1 free/cofree seed into a full chapter. Done. It is now **Chapter 6**, inserted
right after Ch5 (Comonoids: DCont ≅ Cat) and before Zappa–Szép. Everything renumbered automatically
(ZS → Ch7, Phase-2 outline → Ch8; the Phase-2 chapter is now the derivative-only stub, with its
free/cofree bullet repointed to Ch6). No cross-references broken (checked).

## The chapter's promise
For any container C: compute the free monad C\* and cofree comonad C^∞ as containers; know why C\* is
the *universal* monad on C (the free-monad Lemma); and see that C^∞ is the cofree *directed* container
— a small category, the subtree category. Behaviour lands back on the equivalence chain.

## Section arc (compute-first, signature lens)
1. **The tools we borrow** — initial algebras μF / final coalgebras νF, Adámek existence,
   accessibility, T_F = μY.(X+FY), D_F = νY.(X×FY). Cited, tight. *Footnote flags Neil's steer that
   this belongs in a Preliminaries chapter — the book has none yet, so it's carried here for now.*
2. **W-types and their duals** — W S P / M S P exist in Set; the **cofree side is the easy side**
   because container extensions preserve connected limits (reuse of Ch3 `thm:char`) ⟹ the
   final-coalgebra sequence converges. Indexed-W remark so P\* is well-defined.
3. **The free monad of a container** — C\* = (S\*, P\*), trees with a variable-leaf constructor,
   grafting monoid, a tikz tree figure, Maybe/binary example. Laws cite `Free.lean`.
4. **The free-monad Lemma** — F ⊣ U, α = insertion of generators, ĝ by W-recursion. This **folds in
   the 2026-07-24 PROVE result** (`proofs/2026-07-24-free-monad-universal-property.md`): the whole UP
   reduces by tree induction to the *target* monoid's own laws (base = M's unit, step = M's assoc).
5. **Cofree comonad = cofree directed container** — the chapter's payoff. Cofree comonad is a comonoid,
   hence (Ch5) a directed container, hence a category: the subtree category.
6. **Syntax and behaviour** — the duality; grant framing; two honest open ends.

## Honesty / provenance (please sanity-check these)
- **Free-monad construction + ◁-monoid laws:** construction = prior art (Gambino–Kock `0906.4931`;
  AAG 2005). The container-coordinate ◁-monoid laws are mine and Lean-checked in `Free.lean` (zero
  sorry, Quot.sound-only) — but per the Preface convention, since Free.lean is **not committed** to the
  repo `lean/` tree, the tag reads `[MacBeth]` (footnote), NOT `Lean-verified`.
- **Free-monad Lemma:** theorem = Gambino–Kock Thm 4.5 (prior art). The container-coordinate proof is
  mine, graded `proved`. Partial Lean (`FreeUniversal.lean`): full triangle + unit + object-uniqueness
  machine-checked; the multiplication-homomorphism law and backward uniqueness are **not yet** Lean.
  All stated in the theorem's footnote.
- **★ Cofree side — novelty tag STRIPPED.** The old §7.1 `thm:cofree-dircont` carried a `[MacBeth]`
  novelty claim. The cofree comonad / tree comonoid is **Niu–Spivak 2312.00990 Prop 8.18, 8.33, Thm
  8.45 — prior art**, now cited as such; only the explicit o/↓/⊕ (D1–D5) presentation and its
  verification are attributed to me. Directions = **all nodes** (finite paths from root), not leaves —
  the book text was already correct; I made the leaves-vs-nodes contrast explicit because it's a
  common confusion.
- **Cofree Lean is BLOCKED**, not done: the M-type carrier is coinductive, and `lean/Containers` is
  Lean 4 core with no Mathlib / no coinduction. Footnote says "in progress, pending Mathlib PFunctor.M"
  — no Lean-verified tag claimed. (This is your infra call.)
- **Citations** all at deep-read (G–K `0906.4931`, Niu–Spivak `2312.00990`). No new citation to the
  `2405.13157` agent-summary entry; whole-book floor unchanged (`citation_check.py --report footprint`
  confirms `agent-summary`, the pre-existing DCont-chapter debt).

## One question for Neil
You asked for the initial-algebra / accessibility material (M1) in a **Preliminaries chapter**, keeping
Ch6 to the container instances. The book has no Preliminaries chapter yet, so I put M1 as a tight
opening section §6.1 with a footnote saying it can be lifted out wholesale once the global structure is
fixed. Two decisions for you: (a) create a Preliminaries chapter and move §6.1 there? (b) is Chapter 6
the placement you want, or should it sit elsewhere in the arc?

Scratch/structural notes: `projects/scratch/write-2026-07-23-book.md`.
