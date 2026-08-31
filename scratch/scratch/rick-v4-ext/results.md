# Ext¹ over k = F₂ for V₄ = Klein four in S₄

**Date:** 2026-08-19. Script: `ext_v4.py` (self-contained, hand-rolled GF(2) linear algebra).

## Setup

V₄ = {e, a, b, c}, a=(12)(34), b=(13)(24), c=(14)(23)=ab; codes e=(0,0), a=(1,0), b=(0,1), c=(1,1), product = XOR.

Modules over k = F₂ (S = [[0,1],[1,0]], the swap):

| | ρ(a) | ρ(b) | ρ(c) |
|---|---|---|---|
| **M** = k[V₄/A], A=⟨a⟩ | I | S | S |
| **N** = k[V₄/B], B=⟨b⟩ | S | I | S |

Both 2-dimensional; M is the inflation of the regular rep of V₄/A≅Z/2, N along V₄/B. A ≠ B, so different quotient maps. Verified both are genuine representations (ρ(g)ρ(h)=ρ(gh) for all pairs).

## THE ANSWER

**dim_k Ext¹_{kV₄}(M, N) = 0.**

Context values:
- **dim Hom_{kV₄}(M, N) = 1**
- **dim Ext¹_{kV₄}(M, M) = 2** (self-ext sanity check)

## Methods and key intermediate numbers

### Method 1 — honest minimal projective resolution of M, then Hom(−, N)
kV₄ is local self-injective (V₄ a 2-group). Minimal resolution computed algorithmically (projective cover via top = X/rad·X, then Ω = kernel, recurse):

```
P₀ = kV₄¹ → M,   Ω¹M = ker, dim 2
P₁ = kV₄¹ → Ω¹M, Ω²M dim 2
P₂ = kV₄¹ → Ω²M
```
So M has the expected periodic resolution … → kV₄ → kV₄ → kV₄ → M → 0 (all Betti numbers 1, matching that M is Ω of the trivial module up to the Z/2-inflation — an "endotrivial-like" 1-generated module).

Apply Hom_{kV₄}(−, N) = N¹ at each spot (dim 2 each). Cohomology at position 1:
- dim ker(d₂*) = 1, dim im(d₁*) = 1 ⟹ **Ext¹ = 1 − 1 = 0.**

### Method 2 — H¹(V₄, Hom_k(M,N)) with conjugation action (cross-check)
W = Hom_k(M,N), 4-dimensional, g·φ = ρ_N(g) φ ρ_M(g)⁻¹. Computed via full standard cochain complex C⁰→C¹→C²:
- dim Z¹ = 3, dim B¹ = 3 ⟹ **H¹ = 0.**

Structural reason (verified by the action matrices): a and b act on the 4 matrix units {E₁₁,E₁₂,E₂₁,E₂₂} as commuting fixed-point-free involutions generating a **free transitive** V₄-action. Hence **W ≅ kV₄, the regular (= free = injective) module**, so H¹(V₄, kV₄) = Ext¹(k, injective) = 0.

### Method 3 — Shapiro / Frobenius reciprocity (analytic confirmation)
M = Ind_A^{V₄} k, so Ext¹_{kV₄}(M, N) ≅ Ext¹_{kA}(k, Res_A N) = H¹(A, Res_A N).
- Res_A N: a acts on N as S (the swap), so Res_A N ≅ kA, the **free** kA-module ⟹ H¹(A, kA) = 0 ✓ (gives 0).
- Res_A M: a acts trivially, so Res_A M ≅ k⊕k ⟹ Ext¹(M,M) = H¹(A, k⊕k) = 2·H¹(Z/2,F₂) = 2·1 = **2** ✓.

All three routes agree: **Ext¹(M,N)=0, Ext¹(M,M)=2, Hom(M,N)=1.**

## The Hom(M,N)=1 computation (explicit)
φ 2×2 with ρ_N(g)φ = φρ_M(g) ∀g:
- g=a: Sφ=φ ⟹ rows of φ equal.
- g=b: φ=φS ⟹ columns of φ equal.
Together φ = p·J (J all-ones). One free parameter ⟹ dim 1. (The single intertwiner is the "sum" map k[V₄/A]→k→k[V₄/B].)

## Verdict vs Rick's predictions {1, 2, 8}

The computed dimension is **0** — it matches **none** of {1, 2, 8}. So the honest answer is **"other: 0."**

Interpretation for Rick: the two order-2 subgroups A, B being **distinct** is exactly what kills the Ext. The Ext is governed (Shapiro) by H¹(A, Res_A N), and because A's generator acts *freely* on N (it swaps N's two B-cosets), Res_A N is projective over kA and the cohomology vanishes. Contrast the self-case Ext¹(M,M)=2, where A acts *trivially* on M and H¹ survives. So the pairing is NOT "just reading off dim H¹(U;k)" (that would give a nonzero constant regardless): the answer genuinely depends on how one subgroup acts on the other's coset module. Ext¹(M,N)=0 says M and N have **no nonsplit extension** in either direction over kV₄ — the mismatch of the two Z/2 directions makes Hom_k(M,N) free, hence cohomologically trivial. If Rick's "formula survives" (prediction 1) was meant to predict a *nonzero* pairing here, this computation refutes it for the A≠B case; if his formula actually predicts 0 when the two directions are transverse, then it survives with value 0 and 1/2/8 were the wrong guesses.
