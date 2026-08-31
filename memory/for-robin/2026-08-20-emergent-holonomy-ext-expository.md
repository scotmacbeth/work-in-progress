# For Robin — expository note: emergent holonomy lives in degree zero

**2026-08-20, WRITE session.** Draft complete, compiles clean (8pp).

**File:** `projects/expository/emergent-holonomy-is-ext.tex` (+ `.pdf`, 8 pages).

## What it is

The write-up of this cycle's PROVE result (`proofs/2026-08-20-emergent-holonomy-is-ext-tower.md`).
Per the PROVE guardrail — the Mackey/Eckmann–Shapiro/Nakaoka formula (★) is *classical* — this is
an **expository** note, not a novelty paper. It routes to option (a) of the WRITE trigger: a short
standalone note that spells out the group-cohomology backbone for the container audience, then
foregrounds the actual contribution.

## The one sentence

The emergent-holonomy count of an unprotected Zappa–Szép orchestration is
`h(s) = dim_k Hom_{kU}(k[U/A], k[U/B])` — a **degree-0** invariant — and the entire higher
`Ext`-tower vanishes identically, so the invariant is representation-theoretic yet has no higher
cohomological shadow to hunt for.

## What's in it (8 pages)

1. **Intro** — orchestration → the crossing count `h(s)` → the question "is it cohomological?" →
   the two headline theorems (dictionary + degree-0 concentration) → the corrected reading (W2
   witness kills "higher tower detects alignment") → grant framing → an explicit *On novelty*
   paragraph flagging (★) as classical.
2. **Preliminaries** — Ind/Res, permutation modules, group cohomology (with the Maschke remark:
   only p-divisible subgroups contribute a tower), double cosets, the exact-factorisation setup,
   and the transversality lemma (cleaned-up 3-line proof: conjugate into `P∩P'={e}`).
3. **§3** — the three classical ingredients (Eckmann–Shapiro, Mackey, coinduction-Shapiro) each
   stated with a one-line proof, assembled into Theorem (★). Explicitly flagged classical /
   proved-as-assembled.
4. **§4 — the delta.** Cor (h = dim Ext⁰), Thm (degree-0 concentration: transversality ⟹ every
   `A∩uBu⁻¹={e}` ⟹ tower `[h,0,0,…]`), Remark (the corrected reading, incl. why Rick's Ext²-bet
   was structurally void), Cor (twist-stability).
5. **§5** — the independent 17-case F_p verification, with the table. W1 (`Ext⁰=h=2`) and **W2**
   (`h=2>1` misaligned yet tower `≡0`) called out as the decisive rows.
6. **Conclusion** — "detection is degree 0, nothing deeper to audit"; a clear *do-not-conflate*
   paragraph separating emergent holonomy from the general non-factorisation tower
   (p-divisible overlap); two open directions.

## Honesty ledger

- (★) is **not** claimed new anywhere — headline is the dictionary + concentration.
- Corrects the earlier working hypothesis "a higher class detects alignment" (W2 is the witness).
- Consistent with `two-omega-sites` (no H²-class for h) and `rick-v4-ext-vanishes-transverse`.
- Citations: Benson (Reps & Cohomology I), Brown (Cohomology of Groups) — textbooks — plus my own
  internal proof notes. **No arXiv browse-agent-summary provenance** is relied on, so the
  citation-footprint concern doesn't bite. (Note: `memory/code/citation_check.py` isn't present in
  this container — flagging in case the tooling moved.)

## Notes for you / next steps

- No git remote on the `projects` volume, so I couldn't push to GitHub — you can read the .tex/.pdf
  directly from the host. If you want it on GitHub, tell me the repo and I'll prep it next session.
- Possible follow-on (a LEAN trigger, not this session): the concentration theorem reduces to
  `Res_A N` free over `kA`, which the existing `Disjointness.lean` already underpins — a short Lean
  corollary `Ext^{≥1}=0` in the transverse case may be within reach.
- Two open questions parked in the conclusion: (i) does Ext-triviality *characterise* exact
  factorisations among subgroup pairs with a given Ext⁰? (ii) does the general overlap-tower have
  its own orchestration meaning (a graded "how badly two unrelated agents share state")?

— MacBeth

---

## ADDENDUM — 2026-08-20 (later WRITE session): §6 "The full dichotomy" added

Extended the note with a closing section, **§6 `Ext = h · H*(A∩B)` over an abelian group**.
Now **10 pages**, still compiles clean (pdflatex, no undefined refs, no overfull in the new
content). Writes up the 08-22 non-transverse computation
(`scratch/rick-v4-ext-nontransverse/results.md`, both methods agree, registry
`nontransverse-shakehands`).

**What §6 says** (all presented as corollaries of the classical Mackey Thm, scrupulously
attributed — nothing claimed new):
- **Cor (abelian factorisation).** For finite abelian G: `Ext^n_{kG}(k[G/A],k[G/B]) ≅
  H^n(A∩B;k)^⊕h` with `h = [G:AB] = |G||A∩B|/(|A||B|)`. Separation of variables: `h` = a
  *degree-independent multiplicity* (the same meeting count that measures holonomy); `H*(A∩B)` =
  the *per-degree shape*.
- **Cor (transverse corner).** `A∩B={e} ⟹ [h,0,0,…]` — the degree-0 concentration is the
  degenerate shape. So over abelian G, holonomy-vanishing and the surviving towers are two values
  of *one* formula. Remark flags the honesty point: the non-abelian concentration theorem (Thm 12)
  is **not** subsumed (it needs all-conjugates transversality), but the abelian examples coincide.
- **V₄ worked example** (Table 1, deg 0–6): `⟨a⟩,⟨a⟩→[2,2,2,…]`; `⟨a⟩,V₄→[1,1,1,…]`;
  transverse `⟨a⟩,⟨b⟩→[1,0,0,…]`; `V₄,V₄→[1,2,3,…]=H*(V₄)`.
- **Two structural readings** (Rick's Q1/Q2): Q1 — the surviving class is *intrinsically a sum*
  over double cosets, each carrying a full `H*(⟨a⟩)` copy, swapped by the residual symmetry
  `b·(−)`; not isolable. Q2 — support geometry: `supp Ext*(M,N) = V_r(M)∩V_r(N)`;
  `V_r(k[V₄/⟨a⟩]) = {(1:0)}` (proved parametrically — `x` acts as literal zero, so it holds over
  any field, closing the F₂-only-3-points gap). Transverse = **disjoint** points → empty
  intersection → vanishing; non-transverse = **same** point → survives. Support-variety identity
  invoked from Carlson / Avrunin–Scott / Benson II, **cited not reproved**.

**New refs added:** Benson *Reps & Cohomology II* (support varieties), Carlson (J. Algebra 85,
1983), Avrunin–Scott (Invent. Math. 66, 1982). All classical; `citation_check.py --report
footprint` reports "no arXiv citations" ⟹ no browse-summary provenance relied on. (The checker
lives at `projects/code/citation_check.py`, not `memory/code/` — correcting my earlier note.)

Abstract, intro outline, and conclusion ("do-not-conflate" + "Directions") lightly updated to
weave §6 in. The conclusion's two open questions now point at the explicit shape factor and ask
what it becomes when U is non-abelian (where `ᵘB` genuinely varies).

— MacBeth
