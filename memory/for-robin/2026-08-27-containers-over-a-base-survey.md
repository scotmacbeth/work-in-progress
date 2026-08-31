# Draft complete — "Approaches to Containers over a Base"

**2026-08-27 WRITE session.** File: `projects/papers/containers-over-a-base.tex` (+ `.pdf`, 12pp).
Compiles clean with `pdflatex` (two passes), 0 undefined refs, 0 errors. Citation floor: **deep-read**
(checker green on all four arXiv sources).

## What it is
Neil's UID-125 contemplation deliverable, made concrete: the definitive map of what "a container in a
category" can mean once the base isn't `Set`, discriminated by two properties of the base and run with
`Fam(Vec^op)` as the worked example. This is an **expository survey** carrying three of my proved
theorems as its technical spine.

## The thesis (one sentence)
Extensivity and local cartesian closure of the base are the two axes along which the four notions of
container diverge; the linear base `Vec` has neither, so only the external-family approach reaches
`Fam(Vec^op)` — and T1/T2/T4 are the quantitative shadow of that.

## Structure
- **§1 Intro** — the ambiguity (four constructions), the two-axis thesis, the discriminator table
  (main result, lands **page 2**), the three theorems stated, what's new vs prior art.
- **§2 Preliminaries** — closed SMC base, `Fam(C^op)`, the two tensors `⊗`/`◁`, extensivity/LCC/
  connectedness/tininess (only what's used); Remark 2.5 = "Vec is the double-negative example."
- **§3 External approach** — proves **T1** (full-faithful ⟺ unit connected; Set×Set counterexample;
  Diers folklore resolution), **T2** (`⊗`-closed ⟺ familial rep; linear dichotomy), **T4** (`◁`-left-
  closed ⟺ collapse `◁=⊗`; the extensivity-inversion crown, Table 2).
- **§4 Indexed Σ-Π-Δ** — cannot form `Π` over `Vec` (negative result).
- **§5 Fibrational** — the referee: family fibration vs codomain fibration; reconciles enriched-Yoneda
  with my set-level T1 (Neil's flagged dependency).
- **§6 Walker LSCC** — the fourth weakening; verdict `Vec` not locally subcartesian closed (framed as
  a reading result, not a proof of mine).
- **§7 Synthesis** — the two-axis discriminator theorem.
- **§8 Conclusion** — names the single sharpest open PROVE target (below).

## The open target it surfaces (seeds next PROVE.md)
**Does the four-level branching hierarchy `λ-inv ⊊ non-branch ⊊ cartesian ⊊ Π-Mendler` for liftings of
`M◁(−)` lift index-wise to De Pascalis–Uustalu–Veltrì's indexed containers `IC_I`, refining their
cartesian/general dichotomy into a four-step tower over each index?** A positive answer bridges the
external approach (1) and the indexed approach (2) at the level of composition structure — the first
structural bridge between them over a base richer than `Set`. (Secondary target: Walker Q2 — are his
Street-span subcartesian polynomials the same object as my family-`∐` `⊗/◁`, or disjoint?)

## Honesty notes
- Approaches (2),(3),(4) reaching `Vec` are **negative** results; stated as such.
- T1 corrects the "extensive ⟺ full" folklore: the invariant is unit-**connectedness**; faithful is
  NOT automatic over Vec.
- T2 fails over BOTH Vecs by dual mechanisms (cocompleteness over `Vec_fd`, dualizability over full
  `Vec`); closed only on `Fam_fin(Vec_fd^op)`.
- T4's `◁`-closure exists ONLY via the collapse `◁=⊗`; extensivity is opposed to it — inverts T1/T2.
- Walker verdict = my direct reading of `2607.10242` (I read the on-disk `walker_lscc.txt` verbatim
  this session; upgraded the sources.json entry agent-summary→deep-read with a locator), framed as a
  reading/understanding result.

## Two caveats for you / Neil
1. **WRITE.md NB unresolved.** WRITE.md said "check Neil's reply first — does he want the survey
   WRITTEN or a proof target first?" This is a no-email WRITE session, so I could not check. I wrote
   the survey per the WRITE.md main directive. **If Neil's reply redirected toward a proof-first path,
   the next wake should re-scope** — the draft is a clean artifact either way and the open-target in §8
   is exactly the proof-first handle.
2. **No GitHub push** — settled policy (no write access). Share via the projects volume (you can read
   `projects/papers/containers-over-a-base.pdf` on the host) or I can email the PDF/summary next wake.

Minor: two ~13–20pt overfull hboxes (long inline math in the T2/T4 dichotomy items) — cosmetic, left
for a revision pass.
