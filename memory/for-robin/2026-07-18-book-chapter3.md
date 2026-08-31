# Book Chapter 3 — "Which functors are containers?" — drafted & integrated
*2026-07-18 write session. For Neil (uid-64 request) + Robin. To be emailed in a wake/browse session — write sessions can't send.*

## What landed
Neil asked (uid 64, 17 Jul) to **include the wide-pullback theorem in the book, motivated by the
final-coalgebra limits `1 ← F1 ← FF1 ← ⋯`**, and to get the first three chapters complete.

Done. `projects/books/category-of-containers.tex` now has a new **Chapter 3, "Which functors are
containers?"** — compiles clean (`pdflatex`, 29 pp, no undefined refs). The book is now 7 chapters:

1. Containers and their extension functor
2. The category **Cont**
3. **Which functors are containers?**  ← NEW
4. Algebraic structure on **Cont**
5. Comonoids: directed containers and small categories
6. Composing systems: Zappa–Szép
7. Functors over **Cont** (Phase 2 — outline)

So the foundational trio Neil wanted complete = **Chapters 1–3**, with the characterisation theorem as
the capstone.

## What the chapter says
- **Leads with Neil's hook.** The opening motivates the whole characterisation through the cofree
  comonad's terminal sequence `1 ← F1 ← FF1 ← ⋯`: its limit is *cofiltered*, the final coalgebra lives
  there, and the construction only works if `F` preserves it — so *which* functors do? This also does
  pedagogical double-duty: it's the concrete cofiltered limit that shows why the theorem needs
  cofiltered limits and not merely wide pullbacks.
- **The theorem.** `F : Set→Set` is a container ⟺ preserves connected limits (= wide pullbacks +
  cofiltered limits) ⟺ is a coproduct of representables. [Cited: Gambino–Kock §1.18 & Prop 1.22;
  equivalence orig. Diers 1977, Carboni–Johnstone 1995.]
- **Position recovery + the honest correction.** `S = F(1)`; `P(s)` = the *generic element* (initial
  object of the `s`-slice of `el F`). And the correction you flagged is stated as a teaching box:
  the fibre of `F(2)→F(1)` computes `2^{P(s)}` (the **powerset** of the positions), **not** `P(s)` —
  recovering the positions genuinely needs the universal property, not an evaluation.
- **Empty-diagram teaching box.** The empty diagram is *disconnected* (a connected category must be
  nonempty), its limit is `1`, and `⟦S,P⟧(1) = S ≇ 1` unless `|S|=1` — so "connected" is exactly the
  right word, sitting between "wide pullbacks only" (too weak) and "all limits" (too strong). Turned
  into the memorable sanity check: if `F(1)≠1`, the terminal object is not preserved.
- **Limits/colimits.** `Cont ≅ Fam(Set^op)` is complete and cocomplete; `⟦–⟧` preserves connected
  limits and (co)products but is **not** cocontinuous — the first thing it fails to preserve is the
  coequaliser (the same quotient wall that kills the powerset).

## Two honesty flags for you
1. **Provenance downgrade.** The standalone paper tagged products/coproducts
   "[MacBeth, Lean-verified: Cont.lean]". In the book I downgraded this to **[MacBeth]** + a footnote,
   because `Cont.lean` is **not committed** to this repo's `lean/` tree (only `Basic`/`Directed`/
   `ZappaSzep` are). The formalisation exists; the source just isn't in this tree yet. Under-claiming,
   per the book's convention.
2. **One unpinned citation (TODO).** "`⟦–⟧` does not preserve coequalisers" is stated as folklore with
   no theorem number. I expect Abbott's thesis is the pin; it's flagged `[Open]` in the chapter and
   left as a browse/prove-session task. No number attributed until verified.

## Placement note for Neil
You said "Chapter 2"; I placed it as **Chapter 3**, immediately after the morphism chapter. Reason:
the chapter opens with `Cont ≅ Fam(Set^op)`, which uses the backward-position variance defined in the
morphism chapter — so the dependency wants it third. If you'd rather it sit literally as Chapter 2
(before morphisms), the connected-limits *test* itself is self-contained and can be promoted; only the
`Fam(Set^op)` section needs the variance. Happy to restructure on a word from you.

## Provenance floor
The new material's citations clear at `deep-read` (Gambino–Kock 0906.4931). The sub-`deep-read` sources
the footprint checker flags (Shapiro–Spivak nerves `agent-summary`, BW-modern `abstract`, Clarke/Spivak
unregistered) all live in the *pre-existing* comonoids/Zappa–Szép chapters, already honestly marked
"skimmed" in the tracker — untouched this session.

---

## Revision-pass addendum (later same day, separate write session)
Re-entered fresh, found the chapter already integrated (above). Ran it as a hostile-referee pass:
recompiled clean (29 pp, no undefined refs / citation warnings), re-checked all five of your asks are
present, and hand-refereed the mathematics — it's airtight and internally consistent (in particular
the `Cont≅Fam(Set^op)` product formula lines up exactly with the Prop-3.x product-of-containers).

**One improvement made.** In §3.4 the "positions of a *product* are a *sum*" surprise was justified only
by the variance argument. I added the upstream reason it is *forced*: a product in `Fam(𝒞)` is fibrewise,
and a product in `Set^op` is a coproduct in `Set` — so the moment you accept `Cont≅Fam(Set^op)`, the
sum is inevitable, not a computation. Ties §3.1 back to §3.4. Recompiles clean. No other edits — the
chapter didn't need them. TODOs (Abbott coequaliser pin; later-chapter cite upgrades; committing
`Cont.lean`) stand unchanged.
