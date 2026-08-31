# Is the Karamlou–Shah no-go an H² obstruction? — RESULT: refuted, with scope

**Date:** 2026-06-12  **Status:** Complete (negative result + salvaged positive).
**Full write-up:** `2026-06-12-ks-nogo-level-analysis.tex` (6pp, compiles clean).

## Problem statement
Conjecture (PROVE.md): the Karamlou–Shah no-go theorems — list/stream/tree directed
containers do not distribute over the distribution monad Δ or nondeterminism monad P
— are *precisely* (G)-failures of the pairwise Zappa–Szép criterion, witnessed by a
nontrivial cohomology class [ω] ∈ H²(Sk_C; 𝒟). Success required, as step 2,
"express the probability/nondeterminism monad as a wide subcategory 𝒟."

## Solution (the Level Theorem)
**The conjecture is false, for a precisely locatable reason.**

1. The (L)/(G)/H² criterion is *defined only* when the right factor 𝒟 is a small
   category = directed container = polynomial comonad (Ahman–Chapman–Uustalu,
   Ahman–Uustalu). So step 2 requires the monad to be a polynomial functor.

2. **P and Δ are not polynomial functors** (elementary, machine-checked):
   - Powerset: if P ≅ ∐_S (−)^{P_s}, then P(1)=2 ⇒ |S|=2; P(0)=1 ⇒ one shape has
     empty positions; so P(2) = 1 + 2^k. But P(2)=4 ⇒ 2^k=3, impossible.
   - Distribution: Δ(1)=1 ⇒ (if polynomial) Δ representable ⇒ preserves products.
     But the marginal map Δ(2×2)→Δ(2)×Δ(2) is non-injective (independent vs.
     perfectly-correlated coin pairs share uniform marginals). So Δ not
     representable, not polynomial.

3. **Therefore step 2 is unsatisfiable.** Δ, P cannot be a wide subcategory 𝒟; (L)
   and (G) are not even defined for them. The K–S obstruction lies *strictly below*
   (L): it is a non-representability obstruction, not a cohomological closure class.
   Orientation-independent: both factors of an SFS are small categories, so the
   monad would have to be polynomial whichever side it takes.

4. **Bicategorical mismatch (independent second reason).** A Zappa–Szép law is a
   distributive law of two *categories* (monads in Span(Set)) ↔ strict
   factorization (Rosebrugh–Wood). The K–S law is a *mixed* comonad–monad law
   GT⟹TG in [Set,Set] — an entwining/lifting (Beck; Brzeziński–Majid; Power–
   Watanabe), classified by bialgebras, NOT a factorization. So even a perfectly
   good comonad–monad law is the wrong *kind* of distributive law for H².

5. **Salvaged positive content.** Among genuine directed-container-over-directed-
   container no-go theorems, the obstruction *is* [ω] ∈ H²(Sk_C; 𝒟). The rigid
   twist (𝒟 = ℤ/2 at a, a directed container) realizes the generator of ℤ/2:
   (L) holds, (G) fails, no Zappa–Szép complement exists. This is the honest
   in-Poly analogue of a K–S statement, *with* a computable cohomological obstruction.

## Verification
- `ks_level_check.py`: P non-polynomial (2^k=3 has no integer soln); Δ marginal map
  non-injective (two explicit 2×2 joints, equal marginals). Both CONFIRMED.
- `cohomology_holonomy.py` (pre-existing): rigid twist (L) holds, no closing
  transversal, dim_F2 H² = 1, [ω] ≠ 0. CONFIRMED.

## Gaps (honestly stated)
- I did **not** reprove the K–S no-go itself (no access to their proof; worked from
  the published statement only). I classified the *type* of their obstruction, not
  the mechanism of their proof.
- The non-polynomiality of P, Δ and the bicategorical distinction each independently
  suffice to refute the conjectured identification; both are airtight.
- Hypothesis (H) (abelian vertex groups, trivial left action) bounds the positive
  half, as in the parent G-obstruction note; the nonabelian boundary is the open
  continuation there, unaffected here.

## Grant takeaway
"Compositional correctness has a computable obstruction" stands — *scoped to the
polynomial / Cat# world*: for directed-container distributive laws the obstruction
is [ω] ∈ H²(Sk_C; 𝒟). The probability/nondeterminism no-go theorems are a different,
deeper (non-representability) phenomenon. Locating that boundary is the result.
