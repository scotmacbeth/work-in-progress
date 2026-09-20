# Note for Neil (cc Robin) — grant-narrative synthesis is up

**2026-09-20.** In response to your 2026-09-19 request for "a complete write-up of our work",
I have drafted a single synthesis / overview that maps the whole program onto the grant's three
pillars — theory, applications, formalisation — plus impact.

**Where it is.**
- Source + PDF: `papers/compositional-correctness-synthesis.{tex,pdf}` in `scotmacbeth/work-in-progress`.
- URL: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/compositional-correctness-synthesis.pdf
- Content commit: `scotmacbeth/work-in-progress@16f02d3` (stamped on page 1). 10 pages.

**What it is — and is not.** It is an *accurate map*, not a new theorem. No new mathematics; it
cites the existing artifacts at their honest registry grades (peer-reviewed = Rick-refereed only;
then Lean-verified, proved, computed, open). The organising slogan is

> compositional correctness = (L) ∧ [ω] = 0 ∈ H².

**The three gaps are stated plainly, not buried:**
1. **Tax computation** is named in the grant but has *no artifact yet* — the one grant-named
   application with nothing built.
2. **ℰ = 0 (Conjecture 6.2 / Gap-S)** is *open*. The 2026-09-20 module reduction reframed it (the
   Baer–Specker obstruction is void) but did not close it. The *reduction* is proved and is itself
   publishable as a precise open problem.
3. **Nothing is externally published.** The strongest grade in the program is Rick-refereed.

**Grade corrections I made while writing** (against the registry, which wins): orchestration = ZS
is `proved`, not peer-reviewed — the peer-reviewed writeup filed under that node is actually the
re-entrancy note (Rick, 2026-09-03), so re-entrancy carries the peer-reviewed grade. The
equivalence chain is `in-progress` (its fronts proved; the PolyComon ≃ Cat node is Shapiro–Spivak's,
taken as given), not "one node peer-reviewed" as I had loosely noted at wake.

**Roadmap I propose at the end**, in priority order: (1) close or cleanly write up the ℰ = 0 wall;
(2) formalise the assembled equivalence chain (the hub — would anchor the theory pillar); (3) build
the tax application or drop it. And the two most venue-ready artifacts for a first external
submission are the re-entrancy obstruction and the tool-calling-protocols note.

This is an internal grant document, so it stays in `work-in-progress` — I have deliberately *not*
pushed it to `publishable-result`. It did not go through Rick, since it is a synthesis of
already-graded work rather than a new claim. Happy to restructure toward a specific venue if you'd
rather have (b) a named-venue paper than (a) this overview.

— MacBeth
