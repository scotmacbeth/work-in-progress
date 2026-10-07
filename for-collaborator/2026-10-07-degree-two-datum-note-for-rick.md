# For Rick (cc Robin) — synthesis note: "Composition is a degree-two datum"

**Status:** drafted this write session (2026-10-07), pushed to work-in-progress. **Not yet emailed**
(write-session rule: no email). This is the natural PDF to route to Rick for review — it is the
synthesis that would gate the degree-2 story toward `publishable` (PROTOCOL §4.2). Email to follow
in a later session.

- **PDF / source:** `papers/composition-is-a-degree-two-datum.{pdf,tex}` on wip `main`.
- **Content commit (page 1):** `ae9d67a` (stamp commit `d998b34`).
- **Length:** 9pp, `article`/11pt, house style.

## What it is

A positioning / synthesis note for the AI-Mathematician **Theory** pillar and a framing appendix
for the Strathclyde mini-course (Oct 13–16). It organizes **three independently-proved**
compositional invariants of a directed container by the **cohomological degree** of the datum each
reads, and argues the degree records what the invariant can and cannot detect.

- **Degree 0** — tangent-regularity ⟺ out-degree homogeneous; factors through `U:Cat→Poly`;
  **blind to composition** (`ℤ/2` vs `{1,e}` invisible). [cite `parallelizability-does-not-port`,
  commit e154282]
- **Degree 1** — supply-chain inventory consistency `[θ_R]=0∈H¹(𝒮;R)`, **independent** of the weld
  `[ω]∈H²(Sk;𝒟)` (two witnesses, both directions). [cite `supply-chain-inventory-degree-one`,
  commit 6f1fbd2]
- **Degree 2** — the weld `[ω]∈H²` is composition's own class; and the **δ-left-translation**
  invariant *sees* composition: δ-trivializable ⟺ groupoid, separating `ℤ/2` from `{1,e}` — exactly
  the pair degree 0 could not. [cite proof `2026-10-06-delta-left-translation-trivialization`]
- **Capstone** — the three-level **monodromy tower** generic ⊊ groupoid (local system) ⊊ thin
  groupoid (constant presheaf), separated by the vertex group `Aut(a)` as a discrete holonomy class.
  [cite proof `2026-10-07-constant-presheaf-thin-groupoid`]

## The honesty posture I'd most want you to stress-test

1. **The degree grading is a PROGRAM, not a theorem.** Stated as such in ¶"This is a program, not a
   theorem" (intro) and in §7 with explicit open requirements (i)–(iii). The general claim ("every
   compositional invariant is classified by its degree") is labelled a conjecture. Please check I
   never let it drift into a result.
2. **Degrees do not collapse.** I use `Bℤ` (`H¹=A`, `H²=0`) to block any suspension-style
   `H¹≅H²` bridge (Remark 5.4 + intro). The "ladder" is a grading of *data*, not a filtration of one
   theory. Flag if any sentence reads as a single filtration.
3. **No overclaim on the δ-tower.** Rungs 2–3 are composition-*sensitive* invariants of δ, and
   `Aut(a)` is a holonomy class — I explicitly decline to call them literal `H²` classes (§6 last ¶).
   The literal cohomological anchors stay `[θ_R]∈H¹` and `[ω]∈H²`. Is that line clean enough?
4. **Fair to Lanfranchi and to supply-chain modelling** — both *sharpen*, not debunk (§3, §5, §7
   acknowledgement). Lanfranchi's theorem is about Cartesian tangent categories; the port fails
   because the container tangent structure is `(−)⊗W`, monoidal not Cartesian.

Every instance statement was diffed sentence-by-sentence against the proof files (not memory/dream
journal), per the standing write-up failure mode.

## Not included (deliberate)

Zwart–Marsden (2003.12531) — deep-read, concluded **parallel not a sharpening** (their no-gos live
over Set/free-algebra, orthogonal to the H²/Cat obstruction). Left out entirely, as planned.

## Citation footprint

`python3 code/citation_check.py --report footprint` → floor **deep-read** (Gambino–Kock 0906.4931,
Ahman–Uustalu 1604.01187, Lanfranchi 2609.03449 all deep-read). AAGM and internal notes are not
arXiv-keyed; AAGM matches the already-shipped siblings. Clean.
