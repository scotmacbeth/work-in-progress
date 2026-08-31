# PROVE — Is the branching dichotomy a GRADED Freyd statement? (Atkey index-degree)

**Date:** 2026-07-31. Scratch notebook.

## The conjecture (PROVE.md)
Boolean dichotomy is banked: `Arr_M` (arrows `Gp→Tq`) is a Freyd category ⟺ M non-branching.
Conjecture: for branching M with max arity n, the Atkey index of `Arr_M` is *graded* by M's
branching profile, so "arity ≤1" is the bottom of a tower "arity ≤ n" — a GRADED Freyd statement.

## Strategic analysis (before computing)

### Tension #1 — for branching M, `Arr_M` is not a category AT ALL.
Theorem A: `>>>` is non-associative for branching M. So there is no Freyd category, indexed or
not. A "tower of Freyd categories arity ≤ n" cannot be literal. Any grading must RESTORE
associativity by tracking a grade, with the Boolean failure = the shadow of forgetting the grade.

### Tension #2 — the ARITY GAP: there is no finite level n≥2 among cartesian monads.
Claim (to prove): a cartesian (∏-cointerpretation) Set-monad has max arity ∈ {≤1, ∞}. No finite
intermediate. Reason: cartesian μ preserves leaves; a shape s of arity 2 plugged into itself gives
arity 2+2=4, then 8, … unbounded. So "arity ≤ n" as a property OF M has no rungs strictly between
1 and ∞ (in the class where T_M even exists). ⟹ grading M by its own max-arity is EMPTY of levels.
This is an honest sharp finding — a limitation on the naive reading of the conjecture.

### The correct reframe — grade the ARROWS by leaf-count, monoid (ℕ,×).
The grade lives on morphisms, not on M. An arrow f:Gp→Tq is **uniform-k** if f₀(s)∈MS_q has
exactly k leaves for every source shape s. Uniform-k arrows are closed under composition and the
grade MULTIPLIES: a k-leaf shape, each leaf spawning a j-leaf shape, gives k·j leaves. Identity
`η^T∘ε` produces η^M-shapes = 1 leaf = grade 1. So the grade monoid is **(ℕ, ×)** (identity 1,
0 = nullary/exception absorbing).
- Non-branching M ⟹ every arrow has grade ∈ {0,1} (Boolean submonoid {0,1}⊂(ℕ,×)) ⟹ collapse to
  a plain Freyd category.
- Branching M ⟹ grades ≥2 appear ⟹ genuinely graded.

### KEY EMPIRICAL TEST (crux)
The known Pf non-associativity witness is **NON-uniform**: fwd a↦{a} (1 leaf), b↦{a,b} (2 leaves).
HYPOTHESIS: restricting `>>>` to uniform-leaf-count arrows RESTORES associativity for branching M.
If TRUE: `Arr_M` is a (ℕ,×)-graded Freyd category for all M; ungraded collapse (mixing grades /
applying μ^T across leaf-counts) is a category ⟺ grades trivial ⟺ non-branching. This is the
graded refinement, and the grade monoid (ℕ,×) with M's realised leaf-counts IS the "index degree."

## Plan
1. TEST: uniform-leaf arrows associative for Pf? (extend bikleisli.py) — CRUX.
2. If yes: identify the grade category J_M; prove graded associativity; state the graded Freyd thm.
3. Prove the arity-gap proposition (Tension #2) rigorously.
4. Connect to Atkey's indexed Freyd categories honestly (his index = the coeffect/comonad param).
5. If the uniform test FAILS: the grade is finer than a single ℕ (a leaf-tree); go to the
   uncollapsed composition `Tg∘κ∘Gf∘δ : Gp→TTr` (no μ^T) and grade by T-layer.

## Computational Evidence

1. **Known Pf non-assoc witness is NON-uniform** (grade None): a↦{a} (1 leaf), b↦{a,b} (2 leaves).
   Suggested the fix — but see #2.
2. **Leaf grade FAILS for Pf.** Uniform-leaf arrows (cap 8/grade, A1-all): 12/13824 associativity
   violations REMAIN. And grade-multiplicativity fails (128 viol): grade(f)=2, grade(g)=1 →
   grade(g∘f)=1. Mechanism: Pf's μ^T = UNION is idempotent; f=λ.{a,b}, g=λ.{a} → both branches
   emit 'a', union MERGES them → 2·1 collapses to 1. The collapse μ^T destroys any leaf grade.
3. **Multiset is OUTSIDE the ∏-coint class.** mu_T (entwine.py:234) ASSERTS leaves of μ(mm) have
   distinct labels. Multiset μ([[a,b],[a]])=[a,a,b] repeats 'a' → assertion fails → T_multiset
   undefined. So multiset/List are NOT valid effect monads. ⟹ within the valid class, branching
   forces label-sharing at small A ⟹ forces merging ⟹ E2′ failure. Branching and merging are NOT
   separable here; Theorem A ("category ⟺ non-branching") stands, no correction needed.
4. **Arity gap confirmed.** Free magma arities: node=2, node(s,L)=3, node(s,s)=4, …(s2,s2)=8.
   Cartesian μ SUMS leaves; a max-arity-n≥2 shape self-plugs to arity n²>n. No finite rung >1.

## RESOLUTION (negative, with two precise obstructions + a correction)

The branching dichotomy does NOT refine to a graded Freyd tower along arity. Three findings:

**(R1) The conjecture conflates two DISTINCT, NESTED boundaries.**
- "Genuine (non-indexed) Freyd category" = plain Kleisli = NO coeffect comonad = W=Id. Here
  W = G_M, and G_M=Id ⟺ M∘P≅P ∀P ⟺ **M=Id**.
- "Non-branching" = arity≤1 = M=E+A×X, which INCLUDES Maybe, Writer (M≠Id, so W=G_M≠Id).
- So {M=Id} ⊊ {non-branching} ⊊ {all M}. Index-collapse (M=Id) is STRICTLY STRONGER than
  non-branching. The conjecture's "non-branching = index collapse" is FALSE. By Theorem B,
  non-branching M≠Id give genuine Hughes arrows (= INDEXED Freyd cats, W≠Id), NOT plain ones.
  Atkey's index measures the COEFFECT (M≠Id), orthogonal to & coarser than branching.

**(R2) Arity gap: the arity axis has no intermediate rungs.** A cartesian Set-monad has max
  leaf-arity ∈ {≤1, ∞}. Proof: cartesian μ preserves leaves; a max-arity-n≥2 shape s, plugged
  into each of its own n leaves, is an M-shape of arity n·n=n²>n — contradiction. So "arity ≤ n"
  as a graded family between n=1 (bottom) and n=∞ (top) is EMPTY of rungs. (∏-coint branching
  monads like Pf also have unbounded arity.)

**(R3) The associativity obstruction E2′ is Boolean, not gradeable by leaf-count.** Within the
  ∏-coint class branching forces merging (mu_T distinctness); the merging μ^T that gives units
  and interchange also collapses the leaf grade (#2). Uniform-leaf arrows are STILL non-assoc.
  Both obstructions (E2′; and the strength/first obstruction of Thm B, Lemma 3 — a merge-INDEP
  Yoneda "C^n→C = n projections" argument) are equivalent to arity≤1, ON/OFF, no degree.

**Open residue:** a genuine grading may live on the COEFFECT side (graded comonad G_M), à la
Vollmer–Paviotti–Orchard's Gmd machine (CT2026, not accessible this session). Flagged.
