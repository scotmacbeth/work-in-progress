# Effects–coeffects paper — editorial polish pass (2026-07-31 write session)

**File:** `~/projects/papers/effects-coeffects-containers.tex` — amsart, **19pp**, compiles
clean (pdflatex ×2, 0 undefined refs/cites), citation footprint floor **deep-read**.

This was the polish pass Neil's WRITE.md asked for — no new structure, no new proofs. Five
tasks, all done. One of them turned out to matter more than "polish."

## The one that matters: I corrected a claim the draft got wrong

The old Atkey remark (`rem:atkey`, §5) said **"non-branching = Atkey's index trivialises, so
Arr_M becomes a plain non-indexed Freyd category."** That is **false**, and I know it's false
because *I* refuted it in the 07-31 PROVE session
(`proofs/2026-07-31-atkey-index-degree.md`, Prop 2.1 + Cor 2.3):

- Atkey's index measures the **coeffect** `W = G_M`, and `G_M = Id ⟺ M = Id`.
- So index-collapse is the single condition **`M = Id`**, which is **strictly inside**
  non-branching: `Maybe`, `Writer` are non-branching with `G_M ≠ Id`, yet Thm B still makes
  their `Arr_M` a genuine Freyd category — via the **strength** of `T_M`, *not* via any index
  collapse.
- The branching axis and Atkey's index axis are **orthogonal**. The old remark conflated them.

I rewrote the remark to say exactly this (keeping the correct parts: `Arr_M` = Atkey's
biKleisli arrow verbatim; branching κ degrades *below* an indexed Freyd category). This is
aligning the paper to my own proof notes, not new maths — but it removes a genuinely wrong
interpretive claim, so I did not defer it as a TODO. Honesty beats leaving it.

I also added a **"A graded refinement?" further-work bullet** to the conclusion: the two
*natural* gradings (arity on M; leaf-count on arrows) are both ruled out — cartesian max-arity
∈ {≤1, ∞} with no finite rung (`n ↦ n²` self-plug), and μ^T's merging kills the leaf grade —
so the dichotomy is honestly **Boolean**. The open direction is a coeffect-side graded comonad.
I did **not** cite Vollmer–Paviotti–Orchard (still not on arXiv, not deep-read) — phrased it
generically.

## The other four (routine)

1. **Abstract** — tightened 270 → **185 words**, every claim preserved.
2. **Intro** — added the two missing theorem cross-refs (associativity → Thm arrowsA,
   strength → Lemma strong) in the "Third" contribution. Did not add a bulleted Contributions
   list; the main theorem + three worth-stating points already do that job.
3. **Consistency** — standardized **Turi–Plotkin** (was mixed with Plotkin–Turi); dropped 2
   orphan macros (`\Poly`, `\Cat`); everything else already consistent.
4. **Typesetting** — killed the one egregious 65pt overfull (the §5 dichotomy table) with a
   `\small` centered box. Remaining overfulls all ≤30pt, in theorem heads / display math.

## Still open (unchanged, honestly flagged in the paper)
- mult-`T` index-chase + general E2′ across the class are coordinates-proven, not fully Lean'd
  (`rem:e2gap`, §7) — **a lean-session problem**, not touched here.
- Venue still **HELD** for Neil (container-background level unchanged, per your instruction).
- The two "outline neighbour" cites (Goncharov 2602.18295, DDR 1310.0605) remain uncited at
  `agent-summary` — a browse-session deep-read would upgrade them.

Read the paper straight off the projects volume. Decisions log:
`~/projects/scratch/write-2026-07-31-polish.md`.

— MacBeth
