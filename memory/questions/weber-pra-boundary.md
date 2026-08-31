# Q: What does Weber's p.r.a./familial machinery actually buy me?

**Opened:** 2026-09-06 (dream), on the strength of the 2026-08-29-browse2 recovery of the
primary source.

## ★ STATUS 2026-09-09 (dream) — this file is now MOSTLY CLOSED. Front summary first.

- **Q1 — answered as far as the literature can answer it: NO cleaner source exists.** Three
  independent audits, all negative: **Fujii–Lack `2507.05529`** (their Def 4.4 is Weber's Def 5.2
  *verbatim* — same `Spl(R1)` split-fibration factorization; zero container/Poly content, browse
  2026-09-07); **Arkor–McDermott `2404.01281`** (`grep` over the full text: **zero** hits for
  "familial"/"parametric right adjoint"; their axis is a *dense root*, Def 2.5 — orthogonal; browse
  2026-09-07); **Shapiro `2111.14796`** ("Familial Monads as Higher Category Theories", v2
  2026-06-01 — an *independent* representation-theoretic apparatus, Def 1.3/1.11, Thm 2.1
  `Rep ≃ Fam`, never engaging Weber's Def 5.2/Prop 2.6; browse 2026-09-08). Exact-phrase search on
  MO/Math.SE for "familial representability" returns essentially nothing outside Weber himself.
  ⇒ **Write the δ≟Φ / T2 material directly from Weber TAC 18 Def 2.3 / Def 5.2. There is no
  simpler secondary statement to wait for.** The sub-question that remains — does Prop 2.6's
  genericity characterisation *sharpen* T2's conjuncts A/B? — is a `/prove` or `/expository` task
  against the primary text, not a browse task.
- **Q2 — RESOLVED, NEGATIVE, 2026-08-30.** The falsifier named in advance ran and the re-filing is
  **REFUTED**: over `Set`, `(−)◁q` has an honest left adjoint for *every* `q` (= Meyers /
  Niu–Spivak `2312.00990` **Prop 6.57**), so p.r.a. discriminates nothing; and the diagnosis is
  **wrong adjoint side** — every probe instance of mine tests a *right* adjoint. Registry
  `pra-vs-probe-method` (`proved`). Strengthened by the successor: `L_q` is p.r.a. over `Vec` too
  (`Fam/(T,0) ≅ Fam^T`), so it discriminates nothing on *either* base while the probes separate on
  both. See `connections/one-representability-functional-two-probes.md` §"Falsifier: RUN".
- **Q3 — still open**, and now the only genuinely live question in this file.
- **Q4 — RESOLVED, NEGATIVE, 2026-08-30** (different axes; see bottom).
- **Browse verdict:** the Weber-p.r.a. **citation trail is exhausted** — three consecutive negative
  audits, 104 S2 / 72 OpenAlex reverse citers fully swept, all 2025 citers tracked and ruled out.
  **Dropped from the standing browse keyword rotation 2026-09-08.** One soft lead parked for a
  future `Fam(V)`-focused session: **`2305.04042`** "On effective descent V-functors and familial
  descent morphisms" (2023) — effective descent for `V ↦ Fam(V)`, adjacent to Neil's #1 `Fam(C^op)`
  priority, though its "familial" means *descent morphisms*, not Weber-Def-5.2 representability.
  Also confirmed: the "2026 Contemp. Math. decomposition-spaces chapter" is the same content as
  `1612.09225` (2016), **not** fresh — caveat upgraded to confirmed duplicate.

**Source now on file (this was the gate):** Weber, *"Familial 2-functors and parametric right
adjoints"*, **TAC 18(22):665–732 (2007)**, DOI `10.70930/tac/9l84qqh9`, no arXiv ID —
`sources.json` key `weber-2007-familial-2-functors-pra`, `deep-read`, recovered independently
by two agents via the WebFetch-caches-binary + `pdftotext -layout` trick from the author's
mirror. **DO NOT conflate** with Weber `1106.1983` ("Polynomials in categories with
pullbacks", TAC 30 (2015) 533–598) — both load-bearing, distinct, and easy to merge under a
bare "Weber" grep (flagged independently by two agents).

Definitions I now hold: **Def 2.3** p.r.a. = `T` restricted along `A/1` has a left adjoint
`L_T` (a monad is p.r.a. when its functor part is and unit/mult are cartesian); **Ex 2.4**
polynomial functors are always p.r.a., `T=h_!f^*g_*`, `L_T=g_!f^*`; **Ex 2.5** the
free-category-on-a-graph endofunctor on `Graph` is p.r.a. but **NOT polynomial** (`L_T`
replaces an edge labelled `n` by a path of length `n`, which does not preserve monos);
**Def 5.2** familial 2-functor = p.r.a. + classifying map factors through split fibrations
`Spl(T1)`; **§5.9/5.13** `Fam:CAT→CAT` is familial but **NOT opfamilial**.

---

## Q1 — Does p.r.a. sharpen T2's "Φ familially representable", or merely restate it?
T2's closedness criterion (`proved`, registry `t2-day-closedness-famcop`) is
`Φ(Z)=∏_t∐_r C(M_r, Z⊗Q_t)` familially representable. That phrase has been cited only via
nLab / a 2021 n-Café secondary discussion. Check whether **Def 2.3 / Prop 2.6**'s genericity
characterisation gives a *sharper* statement (e.g. names the generic factorisation my
conjuncts A/B split along). **This also discharges the citation gate on the δ≟Φ upgrade** —
see `questions/weber-delta-vs-t2-phi.md`. `/expository` or `/prove`.

## Q2 — Is the "one functional, many probes" method literally p.r.a.-failure across a slice?
See [[../connections/one-representability-functional-two-probes]]. A p.r.a. condition is by
construction a slice-indexed family of representability conditions; my probes look like
objects of that slice. **Cheapest falsifier, named in advance:** over `Set`, decide whether
`L_q=(−)◁q` is p.r.a. as an endofunctor of `Fam(Set^op)=Cont`. If it is p.r.a. for **every**
`q` while my probes fail for every `|T|≥2`, the re-filing is wrong. One `Set` session.
*Conjectural until this runs — do not let it become load-bearing.*

## Q3 — Does DCont≅Cat extend to p.r.a. functors, or is Weber Ex 2.5 genuinely outside?
`Cat` reaches me two ways: as **◁-comonoids inside Poly** (Ahman–Uustalu / Spivak; the
equivalence chain, entirely *inside* container territory), and as **algebras for a monad on
`Graph` that is p.r.a. but not polynomial** (Ex 2.5). The witness for
p.r.a. ⊋ polynomial is exactly "shapes with variable arity" (paths). So: is the co-side
(comonoids) able to capture what the algebra side cannot, or is Ex 2.5 a genuine outside
case for the whole framing? A clean citable boundary example for
[[../connections/dcont-cat-is-the-convergence-hub]] either way.

## Q4 — [RESOLVED — see bottom of file] Is `Fam` familial-but-not-opfamilial the SAME seam as my one-sided joint BC?
I proved (`joint-bc-cont-cod`, `proved`) that `Cont(cod)` is a **co-hyperdoctrine** with
**one-sided** Beck–Chevalley/Frobenius: right-adjoint (∀/E) quantifiers carry both;
left-adjoint (∃/A) quantifiers **fail both**, obstructed uniformly by **co-topos
non-distributivity** of `(Set/P)^op` (`sum-of-products ≠ product-of-sums`). Weber's `Fam` is
familial but not *op*familial — an asymmetry of the same construction in the same
left/right direction. Also candidate-adjacent: T1 fullness needing unit-connectedness in one
direction only. **Cheapest check:** read §5.9/5.13 and see whether the counterexample to
opfamiliality is itself a `∐∏` vs `∏∐` distributivity failure. If yes, one obstruction, two
vocabularies; if no, a second independent asymmetry axis — which, per the fibredness result,
is historically the more likely and the more interesting answer.

---

**Also flagged, lower priority:** Fujii–Lack `2507.05529` (2025-07-07, abstract-level only)
— the enrichment 2-functor for virtual double categories is a parametric right 2-adjoint
with familial character; may state familial representability more cleanly than nLab.
Arkor–McDermott `2404.01281` (TAC 2025) — nerve theorem for relative monads, the
theorem-family Weber 2007 sits in; secondary citation if the machinery goes load-bearing.

Related: [[../connections/one-representability-functional-two-probes]],
[[../connections/weakenings-of-sigma-pi-delta-vec-fails-all]], [[weber-delta-vs-t2-phi]].

---

## Q4 — RESOLVED 2026-08-30: **DIFFERENT AXES**. Verdict NO.

The cheapest check named above was run and returns negative. Weber's non-opfamiliality
argument is the unnumbered prose between Cor 5.14 and Prop 5.15 (§5.9 is a subsection
heading spanning 5.10–5.16). Source verified: author's mirror `webercat.au/fam2fun.pdf`,
re-downloaded and md5-matched; extract at `/tmp/browse/weber-fam2fun.txt`.

**Deciding quote** (immediately after Cor 5.14): applying `Fam` to the discrete opfibration
`τ : Set_• → Set` does not give a discrete opfibration; the unique chosen cartesian map
`f : (S,S)→(S)` "admits no lifting … **if such a lifting existed we would have `x = z = y`,
but `x` and `y` are different**."

**Why this is NOT my seam.** Every diagnostic separates them:

| | Weber non-opfamiliality | my one-sided BC/Frobenius |
|---|---|---|
| index sets | ONE | TWO (interchange) |
| comparison map | the **diagonal** `S → S×S` | the distributivity map |
| failure mode | `x ≠ y` (equaliser over a non-singleton fibre) | `∐∏ ≠ ∏∐` cardinality gap |
| empty fibre | ALSO fails, via *uniqueness* not existence | no analogue |
| coproducts | **absent from the argument entirely** | essential |

Def 5.2 fn 15 confirms it independently: opfamiliality is purely a **2-cell orientation**
axis ("reverse all the 2-cells … replacing split fibrations by split opfibrations").

**Residue, INFERRED and explicitly NOT load-bearing.** Weber's very next sentence: *"dually
the endo-2-functor of `CAT` whose object map is `X ↦ Fam(X^op)^op` is opfamilial but not
familial."* That is literally the **fibrewise-op move** ([[../connections/contravariance-is-the-fibrewise-op]]),
the same operation that flips my Frobenius from `Σ_!` to `E=(Σ_!)^op` — same operation,
*different property* toggled. It also plausibly places `Fam(C^op)` / `Cont(cod)` on Weber's
**opfamilial** side with primary-source backing. The identification with his endo-2-functor
of `CAT` is **unverified**; do not build on it. Worth one cheap session someday.

Full note: `scratch/2026-08-30-weber-opfamilial-vs-onesided-bc.md`.

### ★ Meta-observation (and a distinction I must not blur)
This is the **fourth** consecutive time a "surely these two conditions are the same" question
has come back NEGATIVE (after T2's conjuncts, δ≟Φ, and BHM-fibredness≟T4-closure). But Q4 is
**NOT** a fourth instance of the "one functional, many probes" method — that method is about
*one formula, different factors*, and here the two obstructions do not share a formula at all.
Q4 is an instance of the weaker **meta**-pattern ("conditions that coincide over the standard
base separate off it"), not of the method. Keep the two claims apart: inflating the meta-pattern
into method instances is exactly the lossy-compression failure mode of
[[../connections/the-summary-is-what-gets-audited]].
