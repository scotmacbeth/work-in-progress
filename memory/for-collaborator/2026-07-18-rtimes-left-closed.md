# ⋊ is left-closed — the directed Dialectica tensor is a one-sided-closed monoidal category

**Date:** 2026-07-18 (prove-2) · **Author:** MacBeth
**Full proof:** `proofs/2026-07-18-rtimes-left-closed.md` · **Registry:**
`other-cont-monoidal-tensors` child `rtimes-left-closed` (proved, validates).

## The one-line result
The directed Dialectica tensor `(p ⋊ q)[(s,t)] = p[s]^{S_q} × q[t]` on `Cont` is **left-closed**:
`(−) ⋊ q ⊣ [q,−]_⋊` for every `q`, with

> **`[q,r]_⋊ = ( Cont(q,r), (a,c) ↦ S_q × ∐_{t∈S_q} r[a t] )`.**

The **shape set of the internal hom is the external hom `Cont(q,r)`**. Directions over a morphism
`φ=(a,c): q→r` are `S_q` copies of the total space of `r` pulled back along the forward map `a`.

## Why it matters
This morning's PROVE showed `⋊` is **not right-closed** (`p ⋊ (−)` loses coproducts) but that
`(−) ⋊ q` **preserves** coproducts, leaving left-closure open (Open Question 5). This note closes it:
`⋊` is **directed-closed** — left-closed but not right-closed. The *handedness of the closure equals
the handedness of the tensor*: in `p ⋊ q` the left factor carries the exponent `(−)^{S_q}`, and it is
exactly the left variable `(−) ⋊ q` that stays a left adjoint. To my knowledge this pairing
("directed tensor, closed on precisely the exponent-base side") is not stated for Poly/Cont in
Dorta–Jarvis–Niu or elsewhere I can check offline.

Refined structural dial (supersedes the earlier "in-an-exponent" slogan):

> `(−) ⊙ q` is a **left adjoint** (closure-eligible on that side) **iff the *varied* shape set does
> not appear in an exponent** of the direction formula.

Reading this dial across the Cont tensors: `×`, `⊗` closed both sides; `◁` one side (coclosed); `⋉`
neither (varied set in an exponent on both sides); `⋊` exactly the base side.

## How it's proved
Explicit right adjoint, not an abstract AFT existence claim. Bijection
`Θ: Cont(p⋊q,r) ≅ Cont(p,[q,r])` by unpacking a morphism out of `p⋊q` and re-partitioning via the
standard currying/exponential-coproduct adjunctions; naturality in `p` checked termwise (§3 of the
proof, full index tracking); then the pointwise-adjoint criterion (Mac Lane IV.1). As a left adjoint,
`(−)⋊q` preserves **all** small colimits — so the morning's coproduct-preservation is now a one-liner.

## Verified computationally
- `|Cont(p⋊q,r)| = |Cont(p,[q,r])|` on 2000 random container triples — all match.
- The explicit `Θ` is injective (hence bijective) on a 4096-morphism example built on real direction
  *sets*, confirming the index bookkeeping, not just cardinalities.
- `[y,r]_⋊ ≅ r` (unit sanity, 500 trials) — consistent with `(−)⋊y = Id`.
(`scratch/rtimes_leftclosed_check.py`, `scratch/rtimes_theta_check.py`.)

## Honesty
This does **not** contradict de Paiva's closed `Dial(Set)`: we work in the `C=1` predicate-free slice
(all of `Cont`), where the entailment side-condition on Dialectica morphisms is absent. External
novelty of "⋊ left-closed / directed-closed on Cont" is owed a live arXiv check next browse
(de Paiva / Trotta / Spivak / Hedges, "directed Dialectica", "one-sided closed polynomial tensor");
the **mathematics is proved** regardless. Grade: proved.

## Next
- **Chapter:** `four-monoidal-chapter.tex` §10 — replace any "⋊ is not closed" with **⋊ is
  directed-closed**, stating `[q,r]_⋊` and Cor 4.2. (Pairs with the morning's non-closed theorems.)
- **Lean:** `(−)⋊q ⊣ [q,−]_⋊` via `Adjunction.mkOfHomEquiv` on the existing `Container` type — would
  be the **first machine-checked one-sided-closed structure** in the container development. Natural
  `/lean` target.
