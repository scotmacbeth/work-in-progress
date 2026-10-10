# Strathclyde-ready revisions — three notes, for Rick (CC Neil) — 2026-10-10

**Status:** QUEUED for WAKE delivery (WRITE has no email tool). Email to Rick
(grandparick20@gmail.com), CC Robin. Content commit **6089268**, pushed as **6330238** to
`github.com/scotmacbeth/work-in-progress` (`papers/`). All three recompile clean (13 / 17 / 9 pp).

Rick — these land your three re-review reports (UID 211 nerve, UID 212 uniqueness) plus the
crown Stage-2 clause-1 upgrade, all gating Neil's Oct 13–16 mini-course. Nothing here promotes a
registry grade from the WRITE phase; the two weld nodes stay demoted pending your check of the
rewritten splitting derivation.

## A. Nerve-level-two note — `composition-is-a-nerve-level-two-datum.{tex,pdf}` (your UID 211)

- **N2 (the serious one) done.** The `[ω]∈H²` gloss is rewritten throughout: the 2-cocycle
  **condition** `d²ω=0` *is* associativity; the **class** `[ω]` measures **splitting** of an
  already-associative weld (Eilenberg–Mac Lane). Re-entrancy `[ω]=ε≠0` is now stated as a
  **non-split but associative** weld, not a non-associative one. The honest `N₂<N₃`
  non-associativity separator is the unital magma `{1,x,y}` (Thm *assembly*); the weld became a
  **parallel splitting-obstruction remark** (new Remark, "the weld is a splitting obstruction, not
  an associativity test"). `K=C⋈D ⟺ (L)∧(G)` and `(G)⟺[ω]=0` untouched — only the gloss changed.
- **N1 done.** `U(p)` is no longer equated with `tr₁N`; it is a strictly coarser shadow (out-degree
  family only). Witness in prelim: interval `[1]` and `B(ℤ/2)⊔pt` both give `U=y²+y`, different
  reflexive graphs. The Z/2-vs-{1,e} H¹/N₂ separation is untouched.
- **N3 done.** Introduced **cochain level** (the `N_k` the datum is a function on) vs **nerve
  level** (= cocycle-condition/binding level = degree+1, the grade the note uses), used
  consistently; flagged explicitly that the weld is cochain level 2 but nerve level 3.
- Page-1 recipient added.

## B. Uniqueness note — `container-derivative-uniqueness.{tex,pdf}` (your UID 212, wording only)

- **w1** "only nontrivial" scoped to *representable Weil base change* in Sec 8/9 (title/intro were
  already scoped).
- **w2** footnote 1 reworded: the "exhaustive search" was vacuous (no bijection `K→K×K` at finite
  rank ≥2, so the diagonal fails surjectivity by cardinality with nothing to search); steps (4)–(5)
  do the real work at infinite rank.
- **w3** solidity disambiguated into **abstract** solidity (∃ module iso `M≅M⊗M`, i.e. `|S|²=|S|`)
  vs **vertical-lift** solidity (`ℓ_M` of a tangent structure iso). `ℕ·y` is abstractly solid only;
  reflected in abstract, lead-in, Prop *infinite*, Remark *part-not-structure*, conclusion.
- **w4** page-1 recipient. Smaller: c-twist flagged **idle** in step (4) (forced by step 3); Thm 18
  (converse) now cites Thm 13 (rank-free) step (1) for the shared universality input.
- No statements touched — your *proved* / *peer-reviewed* grades stand.

## C. Crown Stage 2 — `crown-stage2-unfolding-vs-descent.{tex,pdf}` (clause 1 conditional → PROVED)

- The `(∗)` hedge (arboreal cartesian lift of a *branching* subtree embedding = preimage) is
  **discharged**: new **Lemma** (branching cartesian lift is preimage) specialising Jakl–Reggio, then
  an **unconditional Proposition**. Old Remark 4.4 rewritten as "what was formerly conditional".
  Clauses 2, 3 unchanged. Abstract, intro, main-theorem clause (1), scope all updated to *proved*.
- **Citation correction you should know about.** WRITE.md and my proof file §2A both cited
  "Jakl–Reggio **Thm 23 / Thm 26**". My own deep-read record (`reading/sources.json`, 2603.21841,
  extraction `deep-read`) pins both facts — `ℙ` a Street fibration **and** cartesian = pathwise
  embedding — to a single **Theorem 7.3**. I cited **Theorem 7.3** in the note (the number my
  verification actually supports) and did **not** propagate the 23/26 numbering. **TODO (next
  prove/lean session):** correct `proofs/2026-10-09-crown-stage2-multishape-branch-extension.md` §2A
  and the registry node to read Thm 7.3. Flagging so you can sanity-check the locator against your
  copy of the paper.

---
*Delivery log (WAKE fills): —*
