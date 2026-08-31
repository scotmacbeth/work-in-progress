# The non-abelian Mackey/Shapiro Ext tower: D₈

**Date:** 2026-08-21
**Author:** MacBeth
**Status:** Formula confirmed (classical Mackey/Shapiro) + independently verified by
minimal free resolution over the genuine non-abelian `k[D₈]`. Registry node: **computed**.
Novelty is the *meeting-point dictionary reading in the non-collapse regime*, **not** the
formula — and a **correction** to the proposed test case.

---

## 1. Statement

For a finite group `G`, subgroups `A, B ≤ G`, and `k = F₂`:
```
    Ext^n_{kG}(k[G/A], k[G/B]) ≅ ⊕_{g ∈ A\G/B} H^n(A ∩ gBg⁻¹ ; k)      (⋆)
```
where `k[G/A] = Ind_A^G k` is the permutation module on the left cosets `G/A`, and the sum
runs over a set of representatives `g` of the double cosets `A\G/B`.

This is **classical** (Shapiro + Mackey, below). The object of this session is to (i) assemble
the proof cleanly, (ii) verify `(⋆)` in the **genuine non-abelian regime** `G = D₈` by an
*independent* minimal free resolution over `k[D₈]`, and (iii) read the tower as a
meeting-point / emergent-holonomy invariant, correcting the naive expectation.

---

## 2. Proof of (⋆) — classical assembly

Write `Res`, `Ind` for restriction/induction between `kG` and `kH` (`H ≤ G`). Over a finite
group `Ind_H^G = Coind_H^G`, and `k[G/H] = Ind_H^G k`.

**Step 1 (Shapiro / adjunction).** `Ind_A^G = kG ⊗_{kA} (−)` is left adjoint to `Res_A`, and
it is exact (kG is free as a right kA-module), so it is derived-trivial:
```
    Ext^n_{kG}(Ind_A^G k, M) ≅ Ext^n_{kA}(k, Res_A M) = H^n(A; Res_A M).
```
Apply with `M = k[G/B] = Ind_B^G k`:
```
    Ext^n_{kG}(k[G/A], k[G/B]) ≅ H^n(A; Res_A Ind_B^G k).                    (1)
```

**Step 2 (Mackey).** The Mackey double-coset formula for the trivial module:
```
    Res_A Ind_B^G k ≅ ⊕_{g ∈ A\G/B} Ind_{A ∩ gBg⁻¹}^A k
                    = ⊕_{g ∈ A\G/B} k[A / (A ∩ gBg⁻¹)].                       (2)
```
(The twist `^g k` is trivial because `k` is the trivial module.)

**Step 3 (Shapiro again, downstairs).** Cohomology commutes with the finite direct sum, and
for each summand Shapiro over the subgroup `A ∩ gBg⁻¹ ≤ A` gives
```
    H^n(A; Ind_{A∩gBg⁻¹}^A k) ≅ H^n(A ∩ gBg⁻¹ ; k).                          (3)
```
Combining (1)–(3) yields `(⋆)`. ∎

Nothing here needs `G` abelian; the only inputs are Shapiro's lemma and Mackey's formula,
both valid for arbitrary finite `G` and any coefficient ring. The **content of a non-abelian
example** is that the conjugate intersections `A ∩ gBg⁻¹` genuinely differ across double
cosets, so `(⋆)` becomes a sum of *distinct* cohomology rings rather than `h` copies of one.

---

## 3. The test case D₈ — and a correction

`D₈ = ⟨r, s | r⁴ = s² = e, srs = r⁻¹⟩`, `|D₈| = 8`, `p = 2`. Center `Z = ⟨r²⟩ ≅ Z/2`.

### 3.1 The proposed case (two Klein fours) COLLAPSES

The PROVE brief suggested `A = ⟨r², s⟩`, `B = ⟨r², rs⟩` (the two Klein-four subgroups meeting
in `Z`). **Both are normal** (index 2). For normal `A`, `AgB = g·AB` and
`|AB| = |A||B|/|A∩B| = 16/2 = 8 = |G|`, so `AB = G`: there is a **single double coset**.
Hence
```
    A\G/B = {G},   A ∩ B = Z ≅ Z/2,   Ext^n = H^n(Z/2) = [1,1,1,1,…].
```
This is the *collapse* regime (one coset, one intersection), **not** the intended per-coset
non-collapse. Two normal subgroups can never give a multi-coset example. *This is a genuine
correction to the brief: the two-Klein-four choice does not exhibit non-collapse.*

### 3.2 The genuine non-collapse: A = B = ⟨s⟩ (a NON-normal reflection)

Take `A = B = ⟨s⟩ = {e, s}`, an order-2 reflection subgroup — **not normal**. Then
`A\G/A` has **three** double cosets, with representatives `g = e, r, r²`:

| `g`  | `AgB`                    | `A ∩ gAg⁻¹`        | type     | `H^*` (deg 0..6)     |
|------|--------------------------|--------------------|----------|----------------------|
| `e`  | `{e, s}`                 | `⟨s⟩`              | `Z/2`    | `[1,1,1,1,1,1,1]`    |
| `r`  | `{r, rs, r³s, r³}`       | `{e}`              | trivial  | `[1,0,0,0,0,0,0]`    |
| `r²` | `{r², r²s}`              | `⟨s⟩`              | `Z/2`    | `[1,1,1,1,1,1,1]`    |

(For `g=r`: `r⟨s⟩r⁻¹ = ⟨rsr⁻¹⟩ = ⟨r²s⟩`, and `⟨s⟩ ∩ ⟨r²s⟩ = {e}` — a *transverse* meeting.)

Assembling `(⋆)`:
```
    Ext^n_{kD₈}(k[G/⟨s⟩], k[G/⟨s⟩]) = [1,1,1,…] + [1,0,0,…] + [1,1,1,…]
                                     = [3, 2, 2, 2, 2, 2, 2].
```

**This is the crown phenomenon.** `deg 0 = 3 = h = |A\G/B|` (the meeting count), but the
stabilised higher tower is `2 < 3`. In the abelian non-transverse regime the multiplicity is
*uniform across all degrees* (`Ext^n = h·dim H^n(A∩B)`, so deg-0 equals the higher value when
`A∩B ≅ Z/2`). Here the meeting count **strictly exceeds** the higher-degree dimension, because
one of the three meetings (`g=r`) is *transverse*: it contributes a summand only in degree 0
and vanishes for `n ≥ 1`.

**Dictionary reading.**
- **Degree 0 = total meeting count.** `dim Ext⁰ = |A\G/B| = h`. Hom is Mackey-blind to
  conjugation; every double coset contributes exactly one `H⁰`.
- **Higher tower is supported only on NON-transverse meetings.** `dim Ext^n = Σ_g dim
  H^n(A∩gBg⁻¹)` picks out, for `n ≥ 1`, precisely the double cosets whose conjugate
  intersection is nontrivial. When every nontrivial intersection is `≅ Z/2` (rank 1),
  ```
      #{ transverse double cosets } = dim Ext⁰ − dim Ext¹.
  ```
  For `A=B=⟨s⟩`: `3 − 2 = 1` transverse coset (`g=r`). The gap between the meeting count and
  the first-cohomology dimension *counts the transverse (perfectly-aligned-away) meetings*.

### 3.3 The full spread (all verified, §4)

| Case (`A`, `B`) | `h` | intersections | `Ext^0..6` | regime |
|---|---|---|---|---|
| `G, G` (sanity) | 1 | `D₈` | `[1,2,3,4,5,6,7]` | `H*(D₈)`, `dim=n+1` |
| `⟨r²,s⟩, ⟨r²,rs⟩` (Klein) | 1 | `Z` | `[1,1,1,…]` | **collapse** (both normal) |
| `⟨s⟩, ⟨s⟩` | 3 | `Z/2, {e}, Z/2` | `[3,2,2,…]` | **non-collapse, deg0 > tower** |
| `⟨s⟩, ⟨rs⟩` | 2 | `{e}, {e}` | `[2,0,0,…]` | both transverse |
| `⟨r²,s⟩, ⟨s⟩` | 2 | `⟨s⟩, ⟨r²s⟩` | `[2,2,2,…]` | distinct subgroups, same `H*` |
| `⟨r⟩, ⟨s⟩` (`C4`,refl) | 1 | `{e}` | `[1,0,0,…]` | transverse, single coset |

The `(⟨r²,s⟩, ⟨s⟩)` row is instructive: the two conjugate intersections `⟨s⟩` and `⟨r²s⟩` are
**distinct subgroups** yet both `≅ Z/2`, so the sum *looks* collapsed (`[2,2,2,…]`) even though
the double cosets and their intersections genuinely differ. Cohomological collapse is coarser
than subgroup-equality: the tower sees only the isomorphism type of each `A∩gBg⁻¹`.

---

## 4. Independent verification (minimal free resolution over k[D₈])

The prediction of §3 is checked against a *from-scratch* computation that never invokes
Mackey: build the group algebra `k[D₈]` from the multiplication table, compute a **minimal
free resolution** `… → P₁ → P₀ → k[G/A] → 0` over `k[D₈]` by iterated syzygies
(minimal generators via Nakayama = lifting a basis of `M/JM`, `J` = augmentation ideal),
apply `Hom_{kD₈}(−, k[G/B])`, and take cohomology of the resulting cochain complex.

Engine: `scratch/rick-d8-ext/gen_d8.py` (general finite-group F₂ engine, generalising the
`(Z/2)^r` engine of `rick-v8-ext/`), driver `run_d8.py`, resolution validator
`validate_resolution.py`.

**Results.** For every case in the §3.3 table the direct Ext tower **equals** the
Mackey/Shapiro prediction (`6/6` cases, degrees `0..6`). Internal checks passed:
- **Group axioms.** `D₈` multiplication table verified associative, unital, with inverses.
- **Genuine resolutions.** For each `A`, the computed boundaries satisfy `dₙ∘dₙ₊₁ = 0` and
  `ker dₙ = im dₙ₊₁` in positive degrees (exactness), i.e. they really resolve `k[G/A]`.
- **`H*(D₈;F₂)` sanity.** `A=B=G` resolves the trivial module; betti numbers
  `[1,2,3,4,5,6,7,8]` reproduce `dim H^n(D₈;F₂) = n+1`, matching the hand count from
  `H*(D₈;F₂) = F₂[x,y,w]/(xy)`, `|x|=|y|=1, |w|=2` (Benson/Carlson): degree-`n` monomials
  `w^k x^i` (`i≥0`) and `w^k y^j` (`j≥1`) number `(⌊n/2⌋+1)+(⌊(n−1)/2⌋+1) = n+1`.

This is an **independent** confirmation: the resolution side knows nothing about double cosets;
the agreement is the theorem `(⋆)` doing its work in a non-abelian group.

---

## 5. What is proved, and what is (only) computed

- **`(⋆)` itself** is *proved* — it is the classical Shapiro+Mackey assembly of §2, valid for
  all finite `G`. This session writes the assembly out; it does not claim the formula as new.
- **The D₈ instances** of §3–4 are *computed* (exact F₂ linear algebra, two independent methods
  agreeing). This is a corroboration of `(⋆)` in the non-abelian regime, plus:
- **The correction** (two normal Klein fours ⟹ single coset ⟹ collapse) is *proved*
  (elementary: `AB=G` for distinct index-2 subgroups).
- **The dictionary reading** — `dim Ext⁰ = h` = meeting count; higher tower supported on
  non-transverse meetings; `deg0 − Ext¹ = #transverse cosets` when nontrivial intersections
  are rank-1 — is *proved* as a direct corollary of `(⋆)` (degree-0 count and the additivity of
  `H^n` over cosets), and is the honest novel content: the emergent-holonomy meeting-point
  invariant now reads **per coset**, with the strict `deg0 > tower` gap as the non-abelian
  signature absent from the abelian uniform-multiplicity regime.

## 6. Gaps / limits

- No gaps in the D₈ verification (finite, exact, cross-checked). The engine currently assumes
  the intersection subgroups are elementary abelian for the *prediction* side (true throughout
  D₈: intersections are `{e}`, `Z/2`, `Z/2`, or the whole `V₄`/`D₈` handled explicitly). For a
  larger group with cyclic-`C₄` or nonabelian intersections one would feed the correct
  `H^*(A∩gBg⁻¹)` Poincaré series; the resolution side needs no such assumption.
- The general non-abelian statement `(⋆)` is a *corollary of classical facts*; per the brief we
  do **not** overclaim it as an original theorem. The registry lands D₈ as a **computed**
  attempt under `emergent-holonomy-is-ext-tower`, and the write-up route is **expository**
  (the meeting-point reading) rather than a new-theorem paper.

---

## Appendix: reproduce

```
cd /home/agent/projects/scratch/rick-d8-ext
python3 run_d8.py               # 6/6 cases: direct Ext == Mackey prediction
python3 validate_resolution.py  # resolutions exact (d∘d=0, ker=im), H*(D8) betti = n+1
```
