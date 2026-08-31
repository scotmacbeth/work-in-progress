# Classifying the left-closed convolutional tensors on Cont: they are `⊗` and the `▷_S` family

MacBeth — 2026-07-23. Deep-work session. Continues `2026-07-22-vacuity-resolved-collapse-tensor.md`
and answers the refined target of `state/PROVE.md`. Registry: `closed-day-structures`,
new node `closed-convolutional-classification-2` (this file).

## Summary

The 2026-07-15 biconditional says a Day-convolutional tensor `⊙_⋆` on `Cont ≅ Fam(Set^op)` is
**left-closed** iff `R_B := (−)⋆B : Set → Set` is **polynomial** (preserves connected limits) for
every set `B`. Yesterday's collapse tensor showed this is a genuine (non-vacuous) restriction. This
note **classifies** the symmetric monoidal `(Set,⋆,I)` satisfying it:

> **Main Theorem.** Let `(Set,⋆,I)` be a *symmetric* monoidal structure with `R_B` polynomial for
> every set `B`. Then the **arities** of the family `{R_B}` are either all `≤ 1` or unbounded, and
> in the bounded case exactly one of:
> - `I = 1` and `⋆ ≅ ×` (cartesian product), giving the **Dirichlet tensor `⊗`** on `Cont`; or
> - `I = ∅` and `⋆ ≅ ∨_S` for a unique set `S`, where `A ∨_S B := A + A×S×B + B`, giving the
>   **`▷_S` family** on `Cont` (`∨_∅ = +`, i.e. `▷_∅` = the product `×` on `Cont`).
>
> Conversely `×` and every `∨_S` are symmetric monoidal with `R_B` polynomial (indeed *affine*)
> for all `B`. The unbounded-arity case is conjectured vacuous (§6, the one open gap).

So, modulo excluding hypothetical unbounded-arity structures, **the left-closed (= biclosed)
convolutional tensors on `Cont` are precisely `⊗` and the `▷_S` family.** This makes the census of
Theorem A (`2026-07-14`) *effective* on the closed locus and vindicates Neil's intuition that the
three known closures (`⊗`, `×`, `▷_S`) are not accidents but the complete list.

---

## 1. Setup and conventions

`⋆ : Set × Set → Set` symmetric monoidal, unit `I`, associator `α`, unitors, braiding. Standing

**Hypothesis (H):** `R_B := (−)⋆B` is a **polynomial functor** for every set `B`, i.e.
`R_B ≅ Σ_{i} y^{A_i}` (a coproduct of representables); equivalently `R_B` preserves connected
limits (Carboni–Johnstone, "Connected limits, familial representability and Artin glueing", 1995).

Under (H), write the polynomial normal form of `R_B` as
```
        X ⋆ B  ≅  Σ_{u ∈ 1⋆B}  X^{A_{B,u}}          (naturally in X),          (1)
```
where the **index set** is `1⋆B = R_B(1)` and, for each `u ∈ 1⋆B`, the **arity** `A_{B,u}` is a
set. (Both are recovered functorially: `R_B(1)=1⋆B` is the index set, and the fibre of the map
`R_B(2) → R_B(1)` induced by `2 → 1` over `u` is `2^{A_{B,u}} = Set(A_{B,u},2)`.)

Define the **degree** `d(B) := sup_{u ∈ 1⋆B} |A_{B,u}| ∈ Card ∪ {∞}` and the **global degree**
`κ := sup_B d(B)`.

A polynomial functor is **affine** (degree `≤1`) iff all its arities have `|A_{B,u}| ≤ 1`, iff it
has the form `X ↦ C + D×X` for sets `C` (the arity-`∅` indices) and `D` (the arity-`1` indices).

**Two running examples.** `∨_S B := A + A×S×B + B` (unit `∅`) has `X ⋆ B = B + (1+S×B)×X`: affine,
`C_B = B`, `D_B = 1 + S×B`. `×` (unit `1`) has `X⋆B = B×X`: affine, `C_B=∅`, `D_B=B`.

---

## 2. Lemma 1 — the unit is small: `|I| ≤ 1`

**Lemma 1.** Under (H), `I ∈ {∅, 1}`.

*Proof.* `R_1 = R_B|_{B=1}` is polynomial, say `R_1(X) = X⋆1 = Σ_{k∈K} X^{M_k}` with `K = 1⋆1`.
The right unitor gives `R_I = (−)⋆I ≅ Id`, so `1⋆I = R_I(1) = 1`; by symmetry `I⋆1 ≅ 1⋆I = 1`.
Hence `R_1(I) = I⋆1 = 1`, i.e.
```
        Σ_{k∈K} I^{M_k}  =  1.
```
Suppose `|I| ≥ 2`. Each summand `I^{M_k} = |I|^{|M_k|} ≥ 1`, so a sum equal to `1` forces `|K|=1`
and the unique term `I^{M_{k₀}} = 1`, i.e. `M_{k₀} = ∅` (as `|I|≥2`). Thus `R_1(X) = X^∅ = 1` is
constant: `X⋆1 = 1` for all `X`. In particular `∅⋆1 = 1`, and by symmetry `1⋆∅ = 1`, so
`R_∅(1) = 1⋆∅ = 1`: `R_∅` has a single index, `X⋆∅ = X^{A}` where `A := A_{∅,*}`. Evaluating at
`X = I`: `I⋆∅ = I^{A}`. But the left unitor gives `I⋆∅ ≅ ∅`. Hence `I^{A} = ∅`, forcing `|I| = 0`
— contradicting `|I| ≥ 2`. ∎

*(Uses only the unit isomorphisms, symmetry, and polynomiality of `R_1, R_∅`; no arity bound. The
finite computation `scratch/cardinality-classification.py` corroborates: symmetric associative
unital polynomial operations on `ℕ` exist only for unit `0` and unit `1`; units `≥ 2` admit none.)*

---

## 3. Proposition 2 — degrees multiply: `d(C⋆B) = d(C)·d(B)`

**Proposition 2.** Under (H), for all `B,C` with `d(B),d(C) ≥ 1`: `d(C⋆B) = d(C)·d(B)` (cardinal
product).

*Proof.* Associativity gives, naturally in `X`,
```
        R_B(R_C(X)) = (X⋆C)⋆B ≅ X⋆(C⋆B) = R_{C⋆B}(X),      so   R_B ∘ R_C ≅ R_{C⋆B}.      (2)
```
Compose the normal forms `R_C = Σ_{c∈1⋆C} y^{A_{C,c}}`, `R_B = Σ_{b∈1⋆B} y^{A_{B,b}}`. Distributing
a product over a coproduct in the exponent,
```
   R_B(R_C(X)) = Σ_{b∈1⋆B} ( Σ_{c∈1⋆C} X^{A_{C,c}} )^{A_{B,b}}
              = Σ_{b∈1⋆B} Σ_{φ: A_{B,b}→1⋆C} X^{ Σ_{i∈A_{B,b}} A_{C,φ(i)} },                (3)
```
so the composite's arities are `Σ_{i∈A_{B,b}} A_{C,φ(i)}`, of size `≤ |A_{B,b}|·d(C) ≤ d(B)·d(C)`.
Choosing `b` with `|A_{B,b}| = d(B)` (achieved when `d(B)` is attained; for the argument below only
this direction is needed) and `φ` constant at a `c` with `|A_{C,c}| = d(C)` gives an arity of size
exactly `d(B)·d(C)`. By (2) these are the arities of `R_{C⋆B}`, so `d(C⋆B) = d(B)·d(C)`. ∎

Thus `d` is a monoid homomorphism `(Set,⋆,I) → (Card,·,1)` on the sub-semigroup where `d ≥ 1`
(note `d(∅ or 1) ` includes the unit: `d(I)=1` since `R_I ≅ Id`).

---

## 4. Key Lemma — no high arities (bounded case)

**Key Lemma.** Under (H), either every arity satisfies `|A_{B,u}| ≤ 1`, or `κ = sup_B d(B)` is
infinite.

*Proof.* Suppose some arity has size `≥ 2`, so `κ ≥ 2`, and suppose `κ < ∞`. Pick `B` and `u` with
`|A_{B,u}| = κ` (the global sup, attained since it is a finite maximum). By Proposition 2,
`d(B⋆B) = d(B)² = κ² > κ` for finite `κ ≥ 2`. But `d(B⋆B) ≤ κ` since `κ` is the global supremum —
contradiction. Hence `κ ≤ 1` unless `κ` is infinite. ∎

So under (H) **plus** the mild hypothesis `κ < ∞` (uniformly bounded arities), all `R_B` are affine.
The infinite case is deferred to §6; every family in the conclusion (`×`, all `∨_S`) has `κ = 1`, so
the bounded hypothesis excludes only *hypothetical* pathologies, never a genuine closed tensor.

*(Corroboration: the cardinality classification of §7 shows that for finite probes no single-variable
degree-`≥2` term is compatible with associativity + unit — the exact finite shadow of this lemma.)*

---

## 5. Reconstruction — affine `⟹` `×` or `∨_S`

Assume now all `R_B` affine: `X⋆B ≅ C_B + D_B × X` naturally in `X`, with `C_B, D_B ⊆ 1⋆B` the
arity-`∅` and arity-`1` index sets (functorial in `B`). Split on `I` (Lemma 1).

### 5.1 Case `I = 1` — `⋆ ≅ ×`
Right unit `X⋆1 = X` gives `C_1 = ∅`, `D_1 = 1`. By symmetry `1⋆∅ = ∅⋆1 = R_1(∅) = ∅`, and
`R_∅(1) = 1⋆∅ = ∅` forces `R_∅ ≡ ∅` (an affine functor with `C_∅ + D_∅ = 1⋆∅ = ∅` and
`C_∅ = R_∅(∅) = ∅⋆∅`; from `1⋆∅=∅` and affineness `R_∅(X)=C_∅+D_∅X` with `C_∅=D_∅=∅`), so `X⋆∅ = ∅`
for all `X`. Hence `C_B = R_B(∅) = ∅⋆B = ∅`, and `C_B + D_B = R_B(1) = 1⋆B = B` gives `D_B = B`.
Therefore `X⋆B = B × X`, i.e. `⋆ ≅ ×`. ∎

### 5.2 Case `I = ∅` — `⋆ ≅ ∨_S`
Left unit `∅⋆B = B` gives `C_B = R_B(∅) = ∅⋆B = B` (naturally). So `X⋆B = B + D_B × X`. By symmetry,
```
        B + D_B × X  ≅  B⋆X... = X + D_X × B          (naturally in X and B).          (4)
```
Read (4) as functors of `B` (fix `X`): the right side `B ↦ X + D_X×B` is affine in `B` (since `D_X`
is constant in `B`). Hence the left side `B ↦ B + D_B×X` is affine in `B`, so `D_B×X` is affine in
`B` for every `X`; taking `X=1`, **`D_B` is an affine functor of `B`**:
```
        D_B  ≅  D_∅ + S × B,        S := the arity-1 part of D.
```
Setting `X = ∅` in (4): `B ≅ D_∅ × B` naturally, so `D_∅ ≅ 1`. Therefore `D_B = 1 + S×B` and
```
        X ⋆ B  =  B + (1 + S×B) × X  =  X + B + S × X × B  =  X ∨_S B.
```
`S` is uniquely determined (the linear coefficient of the affine functor `B ↦ D_B`). Associativity
independently forces the compatibility `D_{B⋆C} ≅ D_B × D_C` with `D_∅ = 1` (a strong-monoidal
functor `D:(Set,⋆,∅)→(Set,×,1)`), which `1+S×B` satisfies; this pins the associator, so `⋆ ≅ ∨_S`
as symmetric monoidal structures. ∎

*(All of §5 verified on finite sets for `×` and `∨_S`, `S ≤ 3`: `scratch/verify_reconstruction.py`
— unit, associativity/`R_B∘R_C=R_{C⋆B}`, the affine form, the symmetry identity (4), and
`D_{B⋆C}=D_B·D_C` all PASS.)*

### 5.3 Conclusion (bounded case)
Lemma 1 + Key Lemma (bounded) + §5.1/§5.2 give the Main Theorem's dichotomy. Under `⟦−⟧` and
Theorem A (`2026-07-14`), `× ↦ ⊗`, `∨_S ↦ ▷_S` (`∨_∅ = + ↦ ×_{Cont}`). ∎

---

## 6. The one gap: excluding unbounded / infinite arities

The Key Lemma leaves open the case `κ = sup_B d(B)` infinite — either some `A_{B,u}` is an infinite
set, or the arities are finite but unbounded. Proposition 2's growth argument cannot close it,
because `κ² = κ` for infinite cardinals; the finite-cardinality classification (§7) cannot see it,
because such a `⋆` need not be finite-valued on finite sets (already `∨_S` with `S` infinite has
`1⋆n` infinite — though its *arities* stay `≤1`; the pathology would need infinite *exponents*).

**Conjecture (gap).** Under (H) there are no infinite arities: `κ ≤ 1` always, so the Main Theorem
is unconditional.

**Status (updated 2026-07-24, `2026-07-24-arity-gap-further-work.md`).** The gap is a *genuine
open problem*, not a technicality — with meaningful probability the conjecture is **false**. Three
new facts sharpen it:

- **(Lemma A) affine = connected-colimit preservation.** "All arities `≤1`" is exactly "`R_B`
  preserves connected **colimits**". So the missing step is: every `R_B` preserves connected
  colimits, given (H) = preserves connected limits.
- **(Prop B) closure buys only limits.** The 2026-07-15 biconditional, read through
  `Cont ≅ Fam(Set^op)` (free coproduct completion), gives *exactly* connected-**limit**
  preservation of `R_B` and nothing about colimits. Connected-limit and connected-colimit
  preservation are independent for polynomial functors, so there is no categorical shortcut: the
  bounded case was closed purely by the cardinal count `κ² > κ`, vacuous for infinite `κ`.
- **(Prop C) counting is provably blind.** The associativity arity-recursion
  `A_{C⋆B,(b,φ)} = Σ_{i∈A_{B,b}} A_{C,φ(i)}` is a *fixed point* at an infinite seed:
  `R_2 = y + y^λ` (`λ` infinite) propagates coherently to `R_{2⋆2} = y + 2^λ·y^λ`, with the
  associator `(X⋆2)⋆2 ≅ X⋆(2⋆2)` a genuine natural (in `X`) iso of polynomial functors. No
  contradiction at the level of cardinalities, arities, or one-variable naturality.

So the earlier "killed by associator naturality" heuristic is misleading (in the classification
direction the associator is *given* and natural). The residual obstruction, if any, lives in the
*element-level* pentagon/hexagon jointly in all variables — a coherence computation, not a
counting one. **The precise next target** (a Further Work statement, not a moonshot for this week):
decide whether the seed `R_2 = y + y^λ` admits an associator natural in all variables satisfying
the pentagon. I did not manufacture a proof I do not have. See §8 and the 2026-07-24 note.

---

## 7. Computational evidence

**Cardinality classification** (`scratch/cardinality-classification.py`, SymPy solve at total degree
`D = 2,3,4` + brute force over coeffs `{0..3}`, associativity checked on `{0..6}³`; two methods
agree):

- Symmetric associative unital polynomial ops `f:ℕ×ℕ→ℕ` with nonneg-integer coeffs are **exactly**:
  `f = x + y + s·xy` (unit `0`, `s ∈ ℤ_{≥0}` free) and `f = x·y` (unit `1`). Units `2,3` admit none.
- **No single-variable degree-`≥2` term ever survives** (`c₂₀ = c₀₂ = 0` in every solution),
  through degree `4`. This is the finite shadow of the Key Lemma; no surprises appear at higher
  degree.

**Reconstruction checks** (`scratch/verify_reconstruction.py`): for `×` and `∨_S` (`S ≤ 3`), the unit
laws, associativity (`R_B∘R_C = R_{C⋆B}`), the affine normal form `X⋆B = C_B + D_B×X`, the symmetry
identity (4), and `D_{B⋆C} = D_B·D_C`, `D_∅ = 1` all PASS. Consistent with the collapse tensor
(2026-07-22) being **excluded**: `R_2^{collapse}(∅)=2 > 1 = R_2^{collapse}(1)` is not affine (indeed
not polynomial), so it violates the Key Lemma's conclusion — exactly as it must.

---

## 8. Grade discipline

- `proved`: Lemma 1 (`|I|≤1`); Prop 2 (degree multiplicativity); Key Lemma **in the bounded case**
  (`κ<∞`); §5 reconstruction (`affine ⟹ × or ∨_S`, with unique `S`); hence the **Main Theorem under
  the bounded-arity hypothesis**.
- `computed`: the finite cardinality classification and all reconstruction spot-checks.
- `conjecture`: the §6 gap (no infinite/unbounded arities). Until closed, the classification is
  proved for **uniformly-bounded-arity** monoidal `⋆` — which includes every `×` and `∨_S`, so the
  *conclusion families are complete*; only the *exhaustiveness* against hypothetical unbounded
  pathologies is conditional.

## 9. Provenance / novelty

- The families `×`, `∨_S` and their images `⊗`, `▷_S` are prior/own art (Spivak; `2026-07-14`).
- The 2026-07-15 biconditional (closed ⟺ `R_B` polynomial) and Theorem A are own art.
- **New here:** the *classification* of the closed locus — that `×` and the `∨_S` family are (modulo
  the §6 gap) the *only* closed convolutional tensors — together with Lemma 1, Prop 2, the Key Lemma,
  and the affine-reconstruction. Complements yesterday's non-vacuity: the collapse tensor is the
  minimal excluded structure; this note describes what remains.

## 10. Non-symmetric remark

Left-closedness needs only `R_B = (−)⋆B` polynomial (not `A⋆(−)`). Lemma 1, the reconstruction, and
the two-sided identity (4) all use symmetry, so the theorem as proved classifies the **symmetric
(= biclosed)** convolutional tensors. Whether a *non-symmetric* monoidal `⋆` can be left-closed
without being right-closed (hence outside `{×}∪{∨_S}`) is a separate open question.
