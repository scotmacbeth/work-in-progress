# For Robin — Convergence-hub Applications section drafted (2026-08-11 WRITE)

**File:** `/home/agent/projects/papers/convergence-hub.tex` (+ `.pdf`, 7 pp, compiles clean under
`pdflatex`, no undefined refs/cites).

## What it is
The Applications section WRITE.md asked for: makes the crown **"DCont≅Cat is the convergence hub"**
explicit and citable. Thesis — *a composable agent, at the object level, IS a small category =
directed container* — supported by four already-proved/verified fronts, plus the honest CAI-II
contrast. Self-contained; does **not** depend on the still-open State-completeness lemma. Reusable
verbatim as a grant Applications passage.

## The four fronts (§3)
1. **Classified INTO it** — Reader/State proof-relevant monad liftings ARE small categories one
   level down (my prove/lean). [proved/lean]; State completeness flagged open in a scope remark.
2. **Cited AS infrastructure** — Smithe CAI II (arXiv:2208.12173, Topos/VERSES): verbatim quote of
   Prop 2.7 "Famously, ◁-comonoids correspond to categories … [8]". [external, deep-read verified].
3. **Generalized UPWARD** — topos direction (pullback-preserving comonads on Set ⟺ Grothendieck
   toposes w/ enough points). Anchored on *Comonads as Spaces* (2607.15091, deep-read). Garner
   "Ionads" named in prose as a **signpost only** — I removed its formal \bibitem so the bibliography
   is strictly deep-read sources (Garner not yet in sources.json; flag, don't lean).
4. **Bounded FROM OUTSIDE** — Ch3 two witnesses: Bag (|Bag(2×2)|=10≠9) + Fairbanks multigraph
   comonad. [proved/computed].

## The contrast I was careful with (§4, Prop "convergent peers")
- Convergence is on the **object** (DCont≅Cat), divergence on the **composition law**.
- CAI II composes via **Bayesian lenses / monoidal bicategory of cilia** (Def 3.8, 3.15, 3.21);
  I compose via **ZS weld C⋈D**, obstruction `[ω]∈H²` (re-entrancy = ε, Reentrancy.lean).
- Stated explicitly that CAI II is **not** distributive-law-free — it *has* Def 3.13, but of
  internal-hom-over-tensor, **not** a monad distributive law in the Beck/ZS sense. And I do **not**
  claim Smithe uses the weld. (Both caveats from your WRITE.md are honoured in-text.)

## Provenance
`citation_check.py --report footprint` → floor = **deep-read** (all four arXiv cites: 1604.01187,
2208.12173, 2312.00990, 2607.15091). Self-cites are Kodamai notes.

## Notes for you / next steps
- Can't push: `projects/` isn't a git repo here. If you want this in `scotmacbeth/ghani-containers`,
  it's a drop-in (amsart, self-contained bib). Or I can splice it into the book's Applications
  chapter (no such chapter in `books/book.tex` yet — it's currently a section-less standalone).
- TODO for a future browse/prove session, not this one: deep-read Garner "Ionads" to promote front 3
  from signpost to load-bearing; finish the State-completeness holonomy lemma to upgrade §3.1's
  scope remark.
