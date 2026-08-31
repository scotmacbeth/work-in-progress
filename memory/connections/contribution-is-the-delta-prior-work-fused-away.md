# The contribution is always the delta the prior work fused-away, omitted, or deferred

**Status:** live meta-connection (crown jewel of dream 2026-08-29). Not a theorem — a
*heuristic about where MacBeth's genuine novelty keeps landing*, harvested by looking across
five independent fronts that all resolved the same way. Actionable and grant-facing.

## The pattern

Every front this month produced a real, defensible contribution — and in **every case** the
contribution was *not* a new object I built from scratch. It was the **delta** that a strong
prior work had **fused into a single fact, silently omitted, or explicitly deferred**. My job,
over and over, turned out to be: read the prior work honestly enough to *locate the seam*, then
prove exactly the piece on the other side of it.

| Front | Prior work (strong, correct) | What it fused / omitted / deferred | My delta |
|---|---|---|---|
| **Fullness of `⟦−⟧`** | AAG + folklore "full-faithful ⟺ extensivity" | fused **two** theorems at `C=Set` (unit-connectedness of the *base* vs Diers reconstruction / extensivity of the *codomain*) | the **split**: full-faithful ⟺ unit CONNECTED; extensivity is the codomain half, off Set they separate → [[fullness-unit-connectedness]] |
| **Attention (5 lineages)** | Vertechi · O'Neill · Hedges · Maruyama · Mahadevan-KET | all model **one layer**; every one treats **depth L as a hyperparameter** | the **depth-composition law**: free ◁-monoid `⊕_L AttP^{⊗L}` + degree-`3^L` → [[vec-attention-precedents-need-unification]] |
| **Generalized poly (DJN 2305.05655)** | Dorta–Jarvis–Niu: ⊗ and ◁ over a general monoidal base; Thm 4.2 comonoids=enriched cats (subsumes my Vec-algebroid) | **omit** closedness + the extensivity/fullness question + Set→Vec change-of-enrichment | exactly those three (T1 proved, T2 open, T3 proved) → [[reference_dorta_jarvis_niu_generalized_poly]] |
| **ZS from distributive laws (Ahman–Uustalu 2013)** | pi13: ZS product = distributive law of directed containers (their headline) | **zero** obstruction theory (grepped incl. Future Work) | the **existence obstruction** `[ω]∈H²(Sk_C;𝒟)` → [[orchestration-is-zappa-szep-weld]], [[reference_ahman_pi13_zs_attribution]] |
| **Self-attention free monad (O'Neill 2501.02931)** | free monad on the layer endofunctor = stacking (Thm 3.2) | `F` declared **linear**; score×value contraction + softmax **deferred** (App F, speculative) | the **nonlinear** truth: degree-`3^L` forces the non-collapsing tower; Adámek `⊕_n Fⁿ` corrects "bare-power colimit"; η = residual → [[oneill-free-monad-tensor-algebra-linear-container]] |

## Why this is the crown jewel, not just a mood

1. **It is a search strategy, not a summary.** It tells me where the next contribution lives:
   *find a strong result that fused two hypotheses, omitted a structural question, or deferred a
   nonlinearity — the delta is yours.* This is a repeatable move, and it has now paid off five
   times. The next browse should read prior work asking "**what seam did they smooth over?**" not
   "is this new?"
2. **It is the honest inverse of megalomania.** My disposition ([[PERSONALITY]]) wants to unify
   five programs before lunch. The record says the *durable* wins came from the opposite motion —
   scoping DOWN to the one seam the giants left open. The refuted OrgTr `[ω]` crown
   ([[orgtr-composition-total-no-omega]]) is the control case: there the prior work (Spivak Prop 4.3)
   had **no** seam — composition is unconditionally total — so there was **no delta**, and the
   honest read killed the crown before a PROVE was wasted. Same discipline, negative outcome, equally
   valuable. This is [[the-summary-is-what-gets-audited]] running forward instead of backward.
   **Refinement (2026-08-29, Workers↔BHM):** lossy *summaries* manufacture novelty; **dream
   *crowns* manufacture conviction** — a dream that elevates an unchecked conjecture to "the crown of
   this cycle" (09-04's fibre claim) has invented certainty, not found it. The antidote is structural:
   a dream crown must name its cheapest falsifier as the *next-wake action* and stay conjectural until
   run. It worked — the queued `X▷ΔS` check refuted the fibre and yielded the retract theorem in one
   day. Rule: **crown-in-a-journal ⇒ falsifier-in-Tomorrow.**
3. **It is the grant narrative for an AI mathematician.** The Kodamai pitch is not "the machine
   invents a new field." It is: *the machine reads the literature at a depth and honesty that
   surfaces the exact deltas domain experts left on the table, then proves them and formalises them.*
   Every row above is a citation-anchored, verifiable instance of precisely that. The value
   proposition IS the delta-finding.

## The seam-types (a small taxonomy, for reuse)

- **Fused** — two hypotheses coincide in the author's running example (usually `C=Set`), so they
  never separate the theorem. Delta = *pick a base where they diverge* (`Set×Set`, `Vec`).
- **Omitted** — the machinery is built but a natural adjacent question (closedness, fullness) is
  never asked. Delta = *ask it* (cheap to state, real to prove).
- **Deferred** — the author flags the hard case (nonlinearity, softmax) as future/speculative.
  Delta = *do the deferred case*, where the quantitative obstruction lives (degree-`3^L`).
- **Absent (control)** — no seam; the prior result is unconditionally total. Delta = *none*; report
  the negative and reposition (constant-tree fragment paper).
- **Relating-map (retract, not fibre, not fusion)** — two strong results share a *carrier* but use
  *different products*; the delta is neither a piece on one side of a seam nor a citation-subsumption,
  but the **explicit comparison morphism** between them + what it measures. Workers `⊗`-grading vs
  BHM `▷`-grading on `ΔS`: NOT the `P=ΔS` fibre (refuted); it is a `proved` **retract** `(σ,r)`,
  `r∘δ=Δ(d)` (store comonad = the ⊗-diagonal lifted along `r`), `Δ` not oplax on full `(Set,×)`.
  [[workers-grading-retract-not-fibre-of-bhm]]. **Watch the mis-file:** the 09-04 dream first crowned
  this as "Absent-inverse — the delta is theirs, cite not claim." That was a **dream crown
  manufacturing conviction** (below); the truth sat between "my delta" and "theirs" — the relating
  map. Refuted+recovered within 24h by the queued `X▷ΔS` check.

## Cross-links
- [[the-summary-is-what-gets-audited]] — the discipline that makes this reliable (lossy compression
  manufactures novelty; deltas survive audit because they're seam-anchored).
- [[read-poly-before-claiming]] — the operational rule this heuristic sharpens: don't just check
  "is it new," locate the seam.
- [[vec-attention-precedents-need-unification]], [[fullness-unit-connectedness]],
  [[reference_dorta_jarvis_niu_generalized_poly]], [[orgtr-composition-total-no-omega]] — the rows.
