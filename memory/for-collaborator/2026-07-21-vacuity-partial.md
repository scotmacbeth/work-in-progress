# Closure-condition vacuity — partial resolution, one open core (2026-07-21)

**For Neil / Robin.** This is the follow-up to Neil's "we were lucky with ⊗ and ×" scepticism.

## The question
The 2026-07-15 biconditional: `(Cont, ⊙_⋆)` left closed ⟺ `(−)⋆B` polynomial ∀B. Is the
right side ever FALSE — i.e. is there a Day-convolutional tensor on `Cont` that is genuinely
NOT left closed? Equivalently (clean form): **does every monoidal structure on `Set` preserve
connected limits in each variable?**

## Where I got to (honest)
**Not fully resolved, but reduced to one sentence and heavily constrained.** I did not find a
counterexample; I killed the three most natural ones, each by a *different* axiom — which is
itself the interesting content.

- **`max`** (`|A⋆B|=max`): not even a bifunctor. Interchange forces one map to be
  simultaneously rank ≤1 (through the pinch `1⋆1`, size 1) and rank 2. Dies at
  bifunctoriality, before coherence.
- **support tensor** `A⋆B = A ⊔ B ⊔ {• iff both nonempty}`: a bifunctor, cardinality-
  associative, **pentagon and triangle both pass** — but **no natural associator exists**
  (exhaustively checked). It breaks at the map `∅→1` filling an empty slot: the single
  separator point can't record *which* leaves it separates. This is the sharp one.
- **`Sym²`-type** (degree-2 extra): breaks associativity by growth (degree 4 vs 2).

The moral, which I think is genuinely book-worthy: **polynomiality = provenance-tracking =
coherence.** A polynomial functor records which first-argument elements each output uses (its
fibre exponent). `∨_S` is coherent precisely because its normal form keeps a term for every
subset of leaves — that bookkeeping *is* the exponent that makes it polynomial. A non-
polynomial "extra" throws the bookkeeping away, and associativity's naturality demands it back.

## Two rigorous tools produced
1. **Retraction lemma** (any monoidal ⋆ on Set): with `i₀,i₁:1⇉2`, `t:2→1`, any `(u,v)`
   equalizing into `2⋆B` has `u=v`. This proves the *injective half* of connected-limit
   preservation in general and reduces the rest to a clean "independence of the first slot"
   condition. The open core is the surjective half.
2. **Unit-terminal (semicartesian) case**: `A×B` is a natural retract of `A⋆B`; the structure
   is almost certainly `= ×` (Dirichlet), computationally confirmed on small sets — but there
   is a real gap (the "extra" is a retract, not obviously a subfunctor; closes via Fox's
   theorem if `μ` is monoidal-natural, which I did not verify).

## The open core (if anyone wants to finish it)
Prove: for a monoidal `⋆` on `Set` (unit initial), `u ∈ 1⋆B` satisfies
`(i₀⋆B)(u) = (i₁⋆B)(u)` **iff** `u` lies in the image of `∅⋆B → 1⋆B` — and the wide-pullback
analogue. That is exactly "⋆ preserves connected limits in the left variable," and it is the
whole of the Vacuity Conjecture. §1.3 of the proof note gives half of it for free.

Full write-up: `proofs/2026-07-21-closure-condition-vacuity.md`. Registry:
`proofs/registry/closed-day-structures.json` node `condition-vacuity` (+ 5 children).

**Recommendation for the book (Ch 3 closed structures):** state the biconditional, then the
"provenance = polynomiality = coherence" story with the support tensor as the cautionary
example (bifunctor + pentagon + triangle, yet not monoidal). That is a better pedagogical
beat than a bare vacuity claim, and it is fully rigorous even without closing the conjecture.
