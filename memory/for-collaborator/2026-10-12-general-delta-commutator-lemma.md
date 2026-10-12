# General δ-commutator lemma + T² coupling criterion — PROVED (route B)

**For:** Rick (referee), Neil (grant: Theory lane). **Date:** 2026-10-12.
**Proof:** `proofs/2026-10-12-general-delta-commutator-lemma.md`.
**Registry:** `supply-chain-inventory-gerbe-h2.json`, new node `coupled-T2-general-delta-lemma` **[proved]**,
child of `coupled-T2-d2-witness`; promotes the asserted `lifting-delta-commutator-lemma` (now a
superseded computed stub). Trustcheck: validates.

## What's new (vs. the 10-11 witness)

The 10-11 witness note asserted the δ-commutator lemma in one paragraph ("the relator evaluates the
obstruction cocycle on the fundamental 2-cell"). This session **does the bookkeeping**, generally and
in the discrete Schreier register, with two non-classical deliverables:

1. **Explicit bar↔Koszul comparison chain map for ℤ²:** φ₂(e_st) = [s|t] − [t|s]. I verified the
   chain-map identity by hand (∂₂ᴮ([s|t]−[t|s]) = (s−1)[t]−(t−1)[s] = φ₁∂₂ᴷe_st, using st=ts). This
   turns the slogan into the identity ⟨[f], e_st⟩ = f(s,t) − f(t,s), and with the obvious section
   gives **δ(ρ) = [w], w = [A,B] ∈ Inn G**, under H²(T²;M) = M/((σ−1)M+(τ−1)M).

2. **The coupling criterion:** G couples on T² ⟺ some commuting outer pair has NO commuting lifts.
   Split (∗) ⟹ decouple, so coupling ⟹ Aut G→Out G non-split. **Non-split is NECESSARY, not
   sufficient** — M₁₆ and C₄⋊C₄ are non-split yet carry no coupled band (rank-1 never couples).

## Honesty ledger (where to aim the referee)

- **Classical, CITED not re-derived:** the backbone — extensions-with-abelian-kernel ↔ H², split ↔ 0;
  homomorphic lift ↔ splitting; [E_ρ] = ρ*[∗] (Brown GTM 87, IV.3–4; Eilenberg–MacLane 1947). If you
  think any of these needs stating more carefully for the nerve/simplicial site, that's the place.
- **The twisted case is the real test.** The D₄×C₂ witness has trivial action (σ=τ=id), so it cannot
  exercise the coboundary term in the lift-independence formula (4.1) w′−w = τ(σ−1)v − σ(τ−1)u. I
  verified (4.1) **element-wise in Aut G** across the whole class-2 battery over all commuting outer
  pairs and all u,v — **including 168 nontrivial-action pairs / 13 608 checks for Heis(𝔽₃)** — plus the
  equivalence "commuting lift ⟺ w ∈ (σ−1)M+(τ−1)M". All pass (`scratch/verify_twisted_liftindep.py`).
- **Sharp criterion is "no commuting lifts", not "[A,B]≠0 in Inn G".** The latter is the trivial-action
  shorthand; in general one needs w ∉ (σ−1)M+(τ−1)M (nonzero in the coinvariants).
- **Scope:** class ≤2 essential (Inn G abelian ⟹ ordinary H²); base T² only (ℤ² two-generator
  one-relator Koszul). Battery enumeration is `computed`, not a full order-≤16 census.

## Grant hook

This is the Theory-lane capstone of the inventory-gerbe program: a place where the two Giraud strata
couple (band forces the degree-2 lifting class), now with the general mechanism proved, not just
witnessed. The clean statement — "composition on T² couples iff Aut→Out is non-split *and* detects a
commuting pair" — is a crisp compositional-correctness criterion for the supply-chain/orchestration
narrative: strict global rectification of an outer transport over a 2-torus base is obstructed exactly
by a commutator of automorphism lifts.

## Natural next node (not done)

Genus-g surface Σ_g: the single ℤ² relator becomes the genus-g relator ∏[aᵢ,bᵢ]; δ should be the sum
of commutators of lifts. Only §3 (the Koszul resolution) is ℤ²-special; the rest ports. Candidate for
a LEAN leaf (the comparison map is finite, decidable).
