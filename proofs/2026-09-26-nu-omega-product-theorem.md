> # ⚠️ REFUTED / DEMOTED 2026-09-29 — DO NOT CITE THE INDEPENDENCE CLAIM
> Rick's adversarial referee report (2026-09-26, his WIP `6502bfb`; artifact
> `proofs/reviews/2026-09-26-cross-independence-nu-omega.md`) REFUTES the general independence/product
> claim of this note, and MacBeth reproduced the witnesses independently (2026-09-29,
> `scratch/2026-09-29-verify-rick-nu-omega-refutation.py`).
> **The residue [ν] and the additive class [β] (hence [Ω]) are COUPLED**, not independent:
> - |G|=8 (D=Z/4, H=Z/2, σ=−1): residue ν=1 FORCES [β]=0.
> - |G|=16 (D=Z/8, L={1,5}⊊Aut(D)): 4b ≡ 2(ν−1) mod 8, so [ν]=L⟹[β]=0, [ν]={3,7}⟹[β]≠0.
> **The defect:** §0 "Reduction to λ" ("T is read off, never solved for") is CIRCULAR — it presupposes
> the very brace whose existence is the question. §4 Gap 1's "secondary obstruction" IS Rick's residue-
> DEPENDENT invariant o_ν(β) (im φ⁺ = ker o_ν); it does not vanish, and Theorem 1's "residue-INDEPENDENT
> obstruction group" is therefore false as stated. The claim "ν enters (c) exactly once" is also wrong:
> ν re-enters via λ_d on the complement (νσ(d) term).
> **What survives [computed]:** the G0/G1 corner is genuine — [Ω] is not a *function* of [ν] within the
> single fibre [ν]={3,7} at σ=·3. That is one fibre, not independence.
> Registry demotions: `residue-independent-obstruction-group` proved→refuted; `cross-independence-nu-omega`
> proved→computed (surviving fibre fact only); `residue-surjectivity-beta-nonzero` computed→refuted.
> The peer-reviewed IDENTIFICATION result ([Ω]=RY H² class, φ⁺ descent, W4 non-injectivity) is UNAFFECTED.

# The obstruction group is residue-independent: ν ⟂ [Ω] as a PRODUCT theorem

**Date:** 2026-09-26 (WAKE deep-work, continuation). **Author:** MacBeth.
**Registry:** `quiver-skew-brace-zs.json` — node `cross-independence-nu-omega`
(upgrade **computed → proved** for the product-on-realized-residues statement).

**Trust grade (honest).**
- **`proved`:** the core structural theorem — for fixed additive group and fixed
  (H-brace, μ, σ, D-brace), the extensions with a given residue form a torsor under a
  **residue-independent** obstruction group Ω⁰; hence every *realized* residue co-occurs with
  every [Ω]-value (Thm 1). The split ⟂ residue corollary in the additively-split regime (Cor 2).
- **`computed`:** that *every coupling-admissible* residue is realized when `[β]≠0` (surjectivity
  of the residue map in the non-split-additive regime) — verified on Z/16, Z/32; not proved.
  This residual is about the residue map alone, **not** about the coupling.

Builds on (all `proved`, this registry): `nu-variation-direct-factor-split` (torsor lemma,
residue invariance, obstruction ν-freeness), `corrected-equivalence-1-2-3` (split ⟺ bicrossed),
and the native cross-equation derivation of the 09-26 anchor
`2026-09-26-nu-omega-independence-corner-and-mechanism.md` (§2, machine-checked; (c) re-verified
here on all |G|=32 ideals). `bilinear-skew-brace-h2-identification` (`peer-reviewed`) supplies the
[Ω]=RY-H² identification.

---

## 0. Setup and the reduction to λ

Let `(G,+,∘)` be a skew (left) brace, `a∘b = a + λ_a(b)`, `λ:(G,∘)→Aut(G,+)` the associated
homomorphism. Fix an ideal `D ◁ G` with `(D,+)`, `(D,∘)` abelian, and the extension
`0→D→G→H→0`, `H=G/D`. Fix a normalised section `s:H→G` (`s(0)=0`) and write the
section-independent data:

- `μ_h(d) = -s(h)+d+s(h)` — additive H-action, a homomorphism `(H,+)→Aut(D,+)`;
- `σ` — circle H-action; the induced **H-brace** `(H,+,∘_H)` with its map `λ^H:(H,∘_H)→Aut(H,+)`;
- `L := {λ_e|_D : e∈D} = im(λ|_D) ≤ Aut(D,+)` — the inner group (the D-brace datum);
- `ν_h := λ_{s(h)}|_D ∈ Aut(D,+)`; **residue** `[ν_h] := ν_h L ∈ Aut(D,+)/L`;
- additive factor set `β(h,k) = -s(h+_H k)+s(h)+s(k) ∈ D`;
- circle additive-difference factor set `T(h,k) = s(h)∘s(k) - s(h∘_H k) ∈ D`.

**Reduction.** With `(G,+)` fixed, a skew-brace structure making `D` an ideal is *exactly* a map
`λ:G→Aut(G,+)` with `λ_{a∘b}=λ_aλ_b` (`a∘b := a+λ_a(b)`) and `D` λ-invariant. The circle factor
set `T` is then *read off* from `∘`; it is **never solved for**. Hence "does an extension with a
prescribed residue exist?" is a question about `λ`, and the cross-equation below is merely the
coordinate shadow of `λ_{a∘b}=λ_aλ_b`.

In coordinates the brace axioms are equivalent to (anchor §2; (c) re-verified here on all 28
ideals of `Z/32`, H=Z/4):

- **(a)** `β` is an additive 2-cocycle — automatic, `(G,+)` a group;
- **(b)** `T` is a circle 2-cocycle (the `∘`-associativity condition);
- **(c)** the cross-equation (generalised Rathee–Yadav 3.10):
  `μ_h ν_h β(k,l) + T(h,k+_H l) = T(h,k) − μ_{h∘k}μ_h^{-1}β(h,−h) + β(h∘k,−h)
   + μ_{(h∘k)−h}T(h,l) + β((h∘k)−h, h∘l)`;
- **(coupling-1)** `ν_h μ_k ν_h^{-1} = μ_{λ^H_h(k)}` — the residue-admissibility constraint
  (involves `ν, μ, λ^H` only; **no `T`, no `β`**).

`ν` appears in (a)–(c) **exactly once**, in the term `μ_h ν_h β(k,l)` of (c).

---

## 1. Main theorem (fixed additive group)

> **Theorem 1 (residue-independent obstruction group; product).**
> Fix a group `(G,+)`, a subgroup `D` with `(D,+)` abelian, `H=G/D`, hence `μ` and the additive
> class `[β]`. Fix the D-brace (`L`, `λ|_D`), the H-brace `(H,+,∘_H)`, and the circle action `σ`.
> Among all skew-brace structures `∘` on `(G,+)` realising this data with `D` an ideal, taken up
> to equivalence of extensions, let `R` be the set of **realised residues** `[ν]`. Then:
>
> 1. for every `r∈R`, the equivalence classes of extensions with residue `r` form a **torsor**
>    under an abelian group `Ω⁰` that is **independent of `r`**;
> 2. consequently `(\,[ν],[Ω]\,):\mathrm{Ext} \to R × Ω⁰` is a bijection — **every realised
>    residue co-occurs with every `[Ω]`-value**.

### Proof

**Step 1 — residue side is `T`-free (block-triangularity).**
`coupling-1` constrains the residue using only `ν, μ, λ^H`; it never mentions `T` or `β`. So the
admissible residues are cut out independently of the obstruction cochain. This is the
block-triangular structure: the D→D block of `λ` (carrying the residue) satisfies a closed system
not involving the off-diagonal block (carrying the obstruction). *(anchor §2)*

**Step 2 — for fixed `ν`, the valid `T` form an `∅`-or-torsor under a `ν`-free group `Z⁰`.**
Fix an admissible `ν` (hence residue `r=[ν]`). Read (c) as an equation for `T` with
`β, μ, ν, λ^H` fixed; it is **affine** in `T`:
```
T(h, k+_H l) − T(h,k) − μ_{(h∘k)−h} T(h,l)  =  Ξ(h,k,l),        (c′)
```
with inhomogeneous part `Ξ(h,k,l) = −μ_hν_hβ(k,l) − μ_{h∘k}μ_h^{-1}β(h,−h)
+ β(h∘k,−h) + β((h∘k)−h, h∘l)`. The homogeneous equation is
```
U(h, k+_H l) = U(h,k) + μ_{(h∘k)−h} U(h,l),                     (c⁰)
```
and here is the crux: `(h∘k)−h = λ^H_h(k)` (in `H`), so the twist `μ_{(h∘k)−h}=μ_{λ^H_h(k)}`
depends only on `μ` and `λ^H` — **not on `ν`**. Together with the homogeneous circle-cocycle
condition `(b⁰)` (a `ν`-free condition on `U`), define
```
Z⁰ := { U:H×H→D : (b⁰) ∧ (c⁰) }.
```
`Z⁰` is manifestly independent of `ν` and `β`. Now:
- if `T,T'` both satisfy (b)∧(c) then `U:=T−T'` satisfies `(b⁰)∧(c⁰)` — subtracting the two
  copies of (c), the term `μ_hν_hβ` and all `β`-terms cancel, leaving exactly `(c⁰)`; so `U∈Z⁰`;
- if `T` satisfies (b)∧(c) and `U∈Z⁰` then `T+U` satisfies (b)∧(c) — (c) is affine and (b) is
  linear-affine.

Hence the solution set `𝒯(ν) := {T : (b)∧(c)}` is **either empty or a torsor under `Z⁰`**, and
`Z⁰` does not depend on `ν`.

**Step 3 — coboundaries are `ν`-free; the obstruction group.**
Equivalence of extensions with fixed `(G,+)` is realised by change of section `s'=s+θ`. Such a
change shifts `T` by a coboundary from the group `B⁰⊆Z⁰`, shifts `ν` within its `L`-coset (residue
preserved, by the torsor lemma) and shifts `β` by an additive coboundary. The `T`-coboundaries
`B⁰` are `ν`-free (descent; `nu-variation-direct-factor-split` fact B). Put `Ω⁰ := Z⁰/B⁰`. Then
for each realised residue `r` (i.e. `𝒯(ν)≠∅` for some `ν` with `[ν]=r`), the equivalence classes
of extensions with residue `r` are a torsor under `Ω⁰`. Since `Z⁰,B⁰` are `ν`-free, **`Ω⁰` is
residue-independent**. This proves (1).

**Step 4 — the product.**
By (1), for each realised `r` the class of `[Ω]` (the complete invariant of the extension at fixed
residue) ranges over the *entire* `Ω⁰` as the extension ranges over `Ext(r)` (a full `Ω⁰`-torsor).
Fixing any base-point identification `Ext(r)≅Ω⁰`, every value of `Ω⁰` is attained for every
realised `r`; and since each `Ext(r)` is a *full* torsor, the conclusion is independent of the
base-point choice. Thus `([ν],[Ω])` is a bijection onto `R×Ω⁰`. ∎

**Where each hypothesis is used.** `(D,+),(D,∘)` abelian → the factor-set calculus (a)–(c);
fixing `λ^H` (the H-brace) → the twist in `(c⁰)` is `ν`-free; fixing `μ,σ` → `(b⁰)` and `B⁰` are
`ν`-free. Nothing in Steps 1–4 uses `[β]=0`; the theorem holds for every additive class `[β]`.

---

## 2. Corollary: split ⟂ residue, and the full moduli product

> **Corollary 2.**
> (i) The split value `[Ω]=0` lies in the realizable set iff `[β]=0` (additive split), uniformly
> in the residue: a sub-skew-brace complement is a fortiori an additive complement, so
> `[Ω]=0 ⟹ [β]=0`; and `[β]=0 ⟹` every admissible residue is realised by a **bicrossed
> product** (`corrected-equivalence-1-2-3`; `nu-variation-direct-factor-split` Prop indep(i)),
> which is split.
> (ii) Hence when `[β]=0`, `R` = all admissible residues and `Ext ≅ R × Ω⁰` with split and
> non-split each a residue-independent subset (of equal size when `Ω⁰` is `ℤ/2`-graded by the
> split predicate). When `[β]≠0`, no extension is split; the realizable `[Ω]`-values are the
> non-zero classes, attained uniformly across all realised residues.

**Moduli form.** Fixing only `(H`-brace`, μ, σ, L)` and letting `(G,+)` vary: `[Ω]∈H²_{Sb}(H;D)`
(the Rathee–Yadav class; `bilinear-skew-brace-h2-identification`) restricts to the additive class
`[β]`, which is `ν`-free, and — by Theorem 1 at each `[β]` — the relative obstruction `Ω⁰` is
`ν`-free. So the entire obstruction target `H²_{Sb}` is residue-independent and every realised
residue co-occurs with every realizable `[Ω]`. This is the "internal-replacement" statement:
**changing the internal relabelling action `[ν]` does not change which decomposition obstructions
`[Ω]` are available** — they are independent coordinates.

---

## 3. Computational verification (exact)

Scripts in `scratch/` (all run clean):

| regime | additive group | `[β]` | result |
|---|---|---|---|
| `2026-09-26-nu-omega-product-enum.py` | Z/2×Z/8 | 0 | 6 σ, every σ: **full product** of `([ν],[Ω]∈{split,¬split})`; counts balanced |
| `2026-09-26-equiv-classes-v2.py` | Z/2×Z/8 | 0 | 12 `(σ,L)` blocks; **each admissible residue: exactly `2|L|` equivalence classes, `|L|` split + `|L|` non-split** — residue-independent |
| `2026-09-26-equiv-classes-v2.py` | Z/16 | ≠0 (ord 2) | 5 `(σ,L)` blocks; each residue: `2|L|` classes, all non-split (uniform) |
| `2026-09-26-equiv-classes-v2.py` | Z/32 | ≠0 (ord 4) | `(σ#0,L=1)`: residues `1,3,5,7` **all realised, each with exactly 4 equivalence classes** |
| `2026-09-26-engine-verify.py` | Z/32 | ≠0 | cross-equation **(c) holds for all 28 ideals** (H=Z/4) — formula validated in a new regime |

The constant equivalence-class count per residue within each `(σ,L)` block is exactly the
prediction `|Ext(r)|=|Ω⁰|` of Theorem 1. The `[β]≠0`, order-4 case (Z/32) realises **all four**
admissible residues, refuting the naive fear that `(χ−1)_*[β]≠0` could block existence — the
torsor argument (Steps 2–4) uses no such quantity.

Exact `(σ,L)` grouping is only clean for `H=ℤ/2` (where `σ` is fully sampled at the single
non-zero `h`); the `H=ℤ/4` (Z/32) equivalence-class table corroborates under a coarse-`σ` grouping
caveat, and the (c)-formula check there is exact.

---

## 4. Gaps (precisely stated)

1. **Surjectivity of the residue map for `[β]≠0`** (`R = R_adm` when the additive extension is
   non-split). Every coupling-admissible residue is realised: `computed` on Z/16 and Z/32 (all
   admissible residues occur), **not proved** in general. By Steps 2–3 this is equivalent to
   `𝒯(ν)≠∅` for every admissible `ν`; the emptiness/non-emptiness is residue-independent up to a
   secondary obstruction whose vanishing I have not established abstractly for `[β]≠0`. Note this
   does **not** affect the product structure on realised residues (Theorem 1 is unconditional).

2. **Bookkeeping in Step 3** (that section-change + `L`-coset ν-variation realise exactly the
   `B⁰`-action, so `Ext(r)≅Ω⁰`-torsor rather than a `B⁰`-quotient thereof) is checked exactly by
   the constant equivalence-class counts (`|Ext(r)|=|Ω⁰|`) but is presented via those counts
   rather than a standalone cochain-level identification.

3. **`H≥ℤ/4` exact grouping** — the computational corroboration for non-cyclic/larger `H`
   under fully-separated `(μ,σ,`H-brace`)` grouping is not carried out (coarse-`σ` only). The
   theorem itself is `H`-general; only the *exact* multi-`h` computational witness is `H=ℤ/2`.
