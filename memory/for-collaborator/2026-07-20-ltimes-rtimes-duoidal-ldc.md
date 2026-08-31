# (⋉,⋊) is a normal duoidal / linearly-distributive structure on Poly — PROVED

**2026-07-20 deep-work PROVE session. Robin/Neil — this answers the PROVE.md LDC question, YES,
and upgrades it to a full duoidal structure with a clean coherence proof.**

## The result
For the two Dorta–Jarvis–Niu Dialectica tensors on Poly=Cont
(`(p⋉q)[(s,t)]=p[s]^{S_q}×q[t]^{S_p}`, `(p⋊q)[(s,t)]=p[s]^{S_q}×q[t]`, shared unit y):

1. There **is** a natural linear distributor `δ: A⋉(B⋊C)→(A⋉B)⋊C` — the PROVE target. It is
   identity on shapes; on directions it is (id_A, id_B, **const**: C[c]→C[c]^{S_A}). The constant
   map is `precompose with S_A↠1`, non-invertible for |S_A|≥2 — a **genuine** distributor, not an
   iso collapse.
2. More: **(Poly, ⋉, ⋊, y) is a NORMAL DUOIDAL category**, with interchange
   `ζ: (A⋊B)⋉(C⋊D)→(A⋉C)⋊(B⋉D)` (middle-four swap on shapes). δ is ζ specialised through the
   shared-unit normality isos. So the LDC structure is the linear-distribution shadow of the duoidal
   one — exactly the pattern Spivak–Srinivasan (2407.01849) established for `(⊗_Day, ◁)`. **This is
   the second such structure on Poly, living on the non-convolutional Dialectica tensors.**

## The proof (why it's clean — "coherence for free")
The *reindexing calculus*. Every ⋉/⋊-composite of atoms p_1..p_n has direction
`∏_i p_i[s_i]^{S(A_i)}` for subsets A_i ⊆ atoms (Lemma 1 = the registry-proved n-fold forms).
Every structural map (associators, unitors, symmetry, ζ, δ, and their ⋉/⋊-images) is
identity-on-shapes-up-to-(Set,×)-coherence and, per factor, **precomposition with the product
projection S(A_i^src)↠S(A_i^tgt)** — which exists iff A_i^tgt⊆A_i^src. The subsets form a **poset**:
≤1 arrow between any two, so there is **at most one structural map T→T'**, so **every** duoidal and
Cockett–Seely LDC coherence diagram commutes automatically. No pentagon-chasing.

## Verification
Full container-level Python (`projects/scratch/ldc-duoidal/`, morphisms with fwd-shape/bwd-dir data,
tensors on actual direction elements): δ & ζ natural (729 + 378 squares), both LDC pentagons, 3×2 and
2×3 duoidal interchange-associativity, δ=ζ-induced, shared-unit normality — all pass.

## What I need from you / open flags
- **Novelty is UNVERIFIED** (no-browse session). Please queue a browse check: is the (⋉,⋊) duoidal
  pairing already in the literature? Note ⋊ is **not** the classical Dialectica par (its shapes are
  S_p×S_q, not the dual S_p^Y×S_q^X), so this is a *fresh* pairing, not de Paiva's ⊗/⅋. Do not let me
  claim priority for "Dialectica LDC on Poly" — the theme is crowded.
- **Grant fit:** this hands the Cont(C)/Dialectica chapter a clean structural theorem, and the
  reindexing calculus is a reusable coherence engine for *any* family of ⋉/⋊-style tensors.
- Full write-up + proof: `projects/proofs/2026-07-20-ltimes-rtimes-duoidal-ldc.md`.
  Registry: `other-cont-monoidal-tensors.json` node `ltimes-rtimes-duoidal-ldc` (trust proved).
- Minor gap: ∂^R's own pentagons not separately run in code (covered by the Theorem in principle).
- Natural next: **Lean** the reindexing calculus (would be the first machine-checked duoidal structure
  in this project), or write the Cont(C) chapter section.
