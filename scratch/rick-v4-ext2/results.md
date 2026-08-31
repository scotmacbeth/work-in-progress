# Ext over F₂[V₄]: transverse permutation modules, twist, and mapping cone

**Computed by exact F₂ linear algebra (own code, no GAP/Sage available). Every dimension
below is the output of an actual computation cross-checked two independent ways.**

Scripts (all in this directory):
- `f2lib.py` — exact F₂ linear algebra (rref, rank, kernel, solve).
- `modules.py` — F₂[V₄]-modules, minimal free resolutions, `ext_tower`.
- `main.py` — Parts 1 & 2 (untwisted + twisted towers, Res_A N, the line L).
- `hyper.py` — full resolutions with augmentation/boundary matrices, comparison chain maps.
- `part3.py` — Part 3 (natural maps, composite check, mapping-cone hyper-Ext).
- `validate_resolve.py` — cross-validation of the resolution machinery.

## Setup

- G = V₄ = ℤ/2 × ℤ/2 = {e, a, b, ab}, k = F₂, kG = F₂[V₄].
  kG ≅ F₂[x,y]/(x²,y²) with x = a+1, y = b+1: local, self-injective (Frobenius),
  radical J = (x,y), J³ = 0. Projective = injective = free.
- A = ⟨a⟩, B = ⟨b⟩: transverse (A ≠ B, A ∩ B = {e}, AB = G).
- M = k[G/A] = k↑ᴬ_G: 2-dim, **a acts trivially, b swaps the two cosets**. M ≅ kG/(x).
- N = k[G/B] = k↑ᴮ_G: 2-dim, **b acts trivially, a swaps**. N ≅ kG/(y).

Minimal free resolution of M = kG/(x): since ann(x) = (x), it is **1-periodic**
`… → R →ˣ R →ˣ R → M`. Betti numbers of M = [1,1,1,1,…] (confirmed computationally).

## Part 1 — Untwisted tower Extⁿ_{kG}(M, N)

| n | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **(1a) direct, min. free resolution** | 1 | 0 | 0 | 0 | 0 |
| **(1b) Eckmann–Shapiro Hⁿ(A; Res_A N)** | 1 | 0 | 0 | 0 | 0 |

Both methods **agree**.

**Identification of Res_A N.** Restricting N = k[G/B] to A = ⟨a⟩: the generator a *swaps*
the two cosets of B, so Res_A N is the module on which a acts by a single 2-cycle
= the **regular module kA = F₂[ℤ/2]** (free, verified: action matrix = `[[0,1],[1,0]]`).
This is Mackey: A\G/B is a single double coset with A ∩ B = {e}, so
Res_A Ind_B^G k = Ind_{e}^A k = kA. Being **free = injective** over the self-injective ring kA,
it has H^{≥1}(A; Res_A N) = 0 and H⁰ = (kA)^A = 1-dim (socle/norm element). Hence the tower [1,0,0,…].

Contrast (sanity, computed): Extⁿ(M,M) = Extⁿ(N,N) = **[2,2,2,2,2]** (periodic, nonzero
in all degrees) because Res_A M and Res_B N are *trivial ⊕ trivial*, giving Hⁿ(ℤ/2;k²)=2 ∀n.
This proves the machinery **does** detect nonvanishing higher Ext — so the zeros for
Ext(M,N) are real, not an artifact. The whole point is the asymmetry:
**transversality ⟹ restriction is FREE ⟹ higher Ext vanishes.**

## Part 2 — The twist L = det(k[G/A]) ⊗ det(k[G/B])⁻¹

**What L is.** det of a 2-point permutation representation = sign of the permutation.
Computed determinants of the generators:

- det(M): [e,a,b,ab] = [1,1,1,1]   (b acts by a transposition; det = −1 = **1 in char 2**)
- det(N): [e,a,b,ab] = [1,1,1,1]
- **L character = [1,1,1,1] → L is the TRIVIAL module.**

The sign representation collapses in characteristic 2 (−1 = 1). Even more strongly:
over F₂ the unit group F₂* is trivial, so Hom(V₄, F₂*) = 0 — **there is no nontrivial
1-dimensional kG-module at all.** Any "line" over F₂[G] is forced to be trivial. So
L = k necessarily and N ⊗ L = N.

**Twisted tower Extⁿ_{kG}(M, N ⊗ L):**

| n | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| direct | 1 | 0 | 0 | 0 | 0 |
| Hⁿ(A; Res_A(N⊗L)) | 1 | 0 | 0 | 0 | 0 |

Identical to the untwisted tower. Res_A(N ⊗ L) is still the free module (= `[[0,1],[1,0]]`).

### VERDICT on Rick's Ext²-shifted-class bet: **NO — the class does NOT appear.**

MacBeth's prediction is **confirmed**. Two independent reasons, both verified:

1. **Char-2 collapse.** L is trivial (sign rep dies since −1=1; and F₂* is trivial so no
   nontrivial character exists to twist by). The twist is a no-op: N ⊗ L = N.
2. **The structural reason MacBeth gave, which holds even for a hypothetical nontrivial line.**
   Res_A N is *free* over kA. Tensoring a free module by any 1-dimensional line stays free
   (Res_A(N⊗L) = Res_A N ⊗ Res_A L = free ⊗ line = free). By Eckmann–Shapiro,
   Ext^{≥1}_{kG}(M, N⊗L) = H^{≥1}(A; free) = 0 regardless of the twist. No shifted class in Ext².

Rick's intuition (a twist should shift a class into Ext²) fails because there is simply
**no Ext² to begin with**: transversality makes the relevant restriction free, and freeness
is stable under line-twisting. The obstruction he is betting on lives in H²(B;A)-type
emergent-holonomy computations for *aligned/overlapping* subgroups, not for transverse ones.

## Part 3 — Mapping cone of k[G/A] → kG → k[G/B]

Here A ∩ B = {e} so k[G/(A∩B)] = kG (regular, 4-dim). Natural permutation-module maps:

- **transfer** f: M = k[G/A] → kG,  gA ↦ Σ_{h∈gA} h  (cosets {e,a}↦e+a, {b,ab}↦b+ab).
- **projection** g: kG → N = k[G/B],  h ↦ hB.

Both verified kG-linear.

**Ambiguity / honesty note.** With these fully-natural maps the composite is
`g∘f = [[1,1],[1,1]]`, **rank 1 ≠ 0**. So the 3-term sequence
k[G/A] → kG → k[G/B] is **NOT a chain complex** (d² ≠ 0), and its "hypercohomology"
as a 3-term complex is not defined. (Geometrically: natural projections go
k[G/(A∩B)] → k[G/A] and → k[G/B], i.e. *outward* from the middle; the sequence as written
mixes a transfer-up with a projection-down, and the composite is precisely the unique nonzero
element of Hom(M,N) = Ext⁰ — reflecting that Hom(M,N) ≠ 0.) There is a 2-parameter family of
choices for each map; I use the canonical transfer/projection and report that honestly.

**What IS well-defined: the mapping cones of the single maps.** RHom(−, N) hyper-Ext
(computed via explicit comparison chain maps between minimal free resolutions;
machinery validated: Cone(id_M) gives [0,0,0,0,0], and Cone(0:M→N) gives
Ext(N,N) ⊕ Ext(M,N)[−1] = [2,3,2,2,2], both correct):

| k | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **HExtᵏ(Cone(f: k[G/A]→kG), N)** | 1 | 0 | 0 | 0 | 0 |
| **HExtᵏ(Cone(g: kG→k[G/B]), N)** | 0 | 2 | 2 | 2 | 2 |

- Cone(f) = [k[G/A] → kG]: hyper-Ext = [1,0,0,…]. Entirely accounted for by
  Ext(kG,N)=[2,0,…] and Ext(M,N)=[1,0,…] with f* surjective in degree 0.
  **No new shifted class.**
- Cone(g) = [kG → k[G/B]]: hyper-Ext = [0,2,2,2,2]. The persistent 2's are **exactly
  Ext^*(N,N) = [2,2,2,2,2]** (the self-extension periodicity of N: Res_B N = trivial²
  ⟹ Hⁿ(B; k²)=2 ∀n). They are **not** a transverse-obstruction class between M and N;
  they are the ordinary self-extensions of k[G/B], surfacing because the cone contains N.

**Part 3 conclusion.** No genuine 3-term complex exists for the canonical maps
(composite ≠ 0), and neither well-defined mapping cone produces any new "shifted class"
linking the two transverse permutation modules. Every hyper-Ext dimension is explained by
the constituent Ext towers already computed in Parts 1–2. Consistent with the Part-2 verdict.

## One-line summary

Transversality (A ∩ B = {e}) forces Res_A N to be the **free** kA-module, killing all higher
Ext_{kG}(M,N); the orientation line L is **trivial** in char 2 (sign rep collapses, and F₂ has
no nontrivial characters at all), so the twist changes nothing; and no mapping-cone construction
resurrects a class. **Rick's Ext²-shifted-class bet fails — there is no Ext² to shift into.**
