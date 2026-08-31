# For Neil (via daily email) — three graded-monad pictures converge on my Workers result

Consolidated this cycle from the ACT-2026 papers (both deep-read). Worth raising
with Neil because **his own paper is one of the three.**

Three independent graded-monad constructions now sit on my proved Workers line
(`workers-graded-category-proved`: `ΔS`-graded `(Set,×)`-category, `ΔS⊗ΔT=Δ(S×T)`):

1. **Ghani–Nordvall Forsberg–Fish, "Snoc Trees" (ACT 2026), Thm 3.5** — `F_*` is
   the free `ℕ`-graded monad on `F`. Neil's own paper.
2. **Braithwaite–Hedges–Mihejevs, "Polylang" / "Substructural Type Theories"
   (ACT 2026)** — composition product as graded monad `T_P(X)=X▷P` over an
   *arbitrary* polynomial `P`. My `ΔS`-grading is conjecturally the
   `P=ΔS`-representable fibre — their generality subsumes mine (I cite, not claim).
3. **Workers (mine, proved)** — `ΔS`, `(Set,×)`-graded.

Two things I'd want Neil's read on:
- Are these three *fibres of one construction*? A unification with the PI's paper
  inside it.
- BHM say `▷`(=`◁`) is "not fibred in its left variable" — this is independent
  confirmation of my proved **T4-left** obstruction (`◁`-left-closure repairs only
  at tininess). Same seam, two vocabularies. Is the non-fibredness *literally* my
  tininess collapse?

Cheap first step queued: write `X▷ΔS` explicitly and check the `P=ΔS`
specialization (one page). Details:
`connections/workers-grading-is-fibre-of-bhm-polynomial-grading.md`.
