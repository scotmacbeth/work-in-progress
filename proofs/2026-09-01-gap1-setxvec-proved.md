# `Set × Vec_fd` is `◁`-admissible — the natural iso, the locus, the coherence obstruction

### Promotion of the Gap-1 inhabitant from `computed` to `proved`; and why no fg-module base is irreducible Gap-1

**MacBeth — 2026-09-01 (PROVE session).**
Predecessor: `proofs/2026-09-01-gap1-inhabited-setxvec.md` (`computed`) and
`proofs/2026-08-30-admissibility-and-the-connectedness-converse.md` (Thms A/B/D, Lemma S).
Companion code: `scratch/2026-09-01-gap1-verify.py` (Task 1 explicit maps; Task 2 dual numbers).
Registry: `proofs/registry/left-adjoint-over-vec.json`, node `open-middle-region`.

---

## EXECUTIVE SUMMARY

**Target (1) — PROVED.** On the precisely-stated **finite-vec-support locus** `𝒫`, the base
`C = Set × Vec_fd` is `◁`-admissible: for all `p,q ∈ 𝒫` I construct `r = p◁q ∈ 𝒫` and an
**explicit natural isomorphism** `Θ : ⟦p◁q⟧ ⟹ ⟦p⟧∘⟦q⟧` of endofunctors of `C` — both components,
natural in `(X_s,X_v)`, built as maps, not matched by cardinality (§3). With the settled facts that
`C` is non-collapse, non-cartesian, and has a disconnected unit (§2), this makes
`Set × Vec_fd` a **`proved` Gap-1 inhabitant**, so **Theorem B is not sharp**: admissibility does
*not* imply connectedness in general — its lextensive-cartesian hypotheses are essential.

**Locus (§1).** `⟦p⟧` is an endofunctor of `Set × Vec_fd` iff `p` has **finite vec-support**
(`{s : V_s ≠ 0}` finite); `𝒫` = objects with finite vec-support (shape `S`, set-positions `A_s`
arbitrary). `𝒫` is closed under `◁`. Outside `𝒫` the Vec direct sum leaves `Vec_fd`; over full
`Vec` non-fd positions are not copower-tiny and the absorption fails (predecessor Gap 1, open).

**Coherence (§4).** `◁` has **no canonical** monoidal structure on `𝒫` — the construction picks a
slot `d_0 ∈ ∐_s T^{A_s}` (needs choice, not natural). A **non-canonical** monoidal structure exists
(concentrate via the Set-associator). The obstruction to canonicity is *exactly* the
non-faithfulness of `⟦−⟧` on the Vec factor (Theorem D). The canonical monoid lives in the image
`⟦𝒫⟧ ⊆ [C,C]`.

**Target (2) — the dual-numbers probe REFUTED, and the family killed wholesale (§5).**
`k[ε]/ε²`-modules do **not** inhabit Gap 1. General lemma: **every finitely generated module over
any ring is copower-tiny**, so for `R` commutative Noetherian the base `fg-R-Mod` is a **collapse
base** (all objects tiny, `◁ = ⊗_R`), structurally identical to `Vec_fd = fg-k-Mod`. This kills the
entire "modules over a mixed ring" candidate family for *irreducible* Gap-1 at once (dual numbers,
`k[x]`, `ℤ`, recollements/pullbacks of module categories). The brief's intuition conflated
*dualizable* (projective) with *copower-tiny*; the programme's axis is copower-tiny **= finitely
generated**, and over an Artinian ring every fg module is tiny.

**Structural payoff (§6).** Admissibility is a **per-object** property:
`Fam(C^op)` is admissible **⟺ every object of `C` is absorptive**
(`X ↦ [P,⟦q⟧X]` an extension for every `q`). Two sources of absorptivity — copower-tiny
(flexible) and distributive/extensive (rigid). Gap 1 sits at their **seam**: additive-fg bases are
all-tiny (collapse), extensive non-collapse bases have connected unit forced (Thm B), so a
non-collapse disconnected base must combine both mechanisms. The product `Set × Vec_fd` realises
this. **Irreducible** realisations are conjecturally confined to (i) non-additive disconnected bases
(only `Set_*` known — inadmissible, Thm A) or (ii) additive **non-fg** bases (predecessor Gap 1,
open). Conjecture: every "nice" Gap-1 inhabitant decomposes as *rigid-extensive × flexible-additive*.

---

## 0. Setting

`C = Set × Vec_fd` over a field `k`. Objects `X = (X_s, X_v)`, `X_s` a set, `X_v` a
finite-dimensional `k`-vector space. Componentwise closed symmetric monoidal structure:

- tensor `X ⊗ Y = (X_s × Y_s, X_v ⊗_k Y_v)`, unit `I = (1, k)`;
- internal hom `[X,Y] = (Y_s^{X_s}, \mathrm{Hom}_k(X_v, Y_v))`;
- coproduct `X ⊔ Y = (X_s ⊔ Y_s, X_v ⊕ Y_v)` — note the Vec factor is the **biproduct**.

`Fam(C^op)`: objects `p = (S, (P_s)_{s∈S})`, `P_s = (A_s, V_s)` with `A_s` a set and `V_s` fd.
Extension
> `⟦p⟧(X) = ∐_{s∈S}[P_s, X] = \big(\ ∐_{s∈S} X_s^{A_s}\ ,\ ⊕_{s∈S}\mathrm{Hom}_k(V_s, X_v)\ \big).`  (E)

I write `[V,W]` for `\mathrm{Hom}_k(V,W)` on the Vec factor and `X^A` for `\mathrm{Set}(A,X)`.

---

## 1. The locus, and why it is the right one

**Lemma 1.1 (locus).** `⟦p⟧` restricts to an endofunctor of `C = Set × Vec_fd` **iff** `p` has
**finite vec-support**: `\mathrm{supp}_v(p) := \{s∈S : V_s ≠ 0\}` is finite.

*Proof.* By (E) the Vec component of `⟦p⟧(X)` is `⊕_{s∈S}[V_s, X_v]`, which is finite-dimensional
for all fd `X_v` iff only finitely many summands are nonzero, i.e. iff `\mathrm{supp}_v(p)` is
finite (each `[V_s,X_v]` is fd, and `[V_s,X_v] = 0 ⟺ V_s = 0` when `X_v ≠ 0`). The Set component
`∐_s X_s^{A_s}` is a set for any `S`, `A_s`. ∎

Let `𝒫 ⊆ Fam(C^op)` be the full subcategory of finite-vec-support objects. The shape set `S` and
the set-positions `A_s` remain **arbitrary** (possibly infinite); only the vector positions are
constrained, to finitely many nonzero ones.

**Remark (the summability boundary, stated).** Two independent finiteness conditions, both tracing
to the single fact *fd = copower-tiny in `Vec`*:
(i) *finite vec-support* keeps `⟦p⟧` inside `Vec_fd` (Lemma 1.1);
(ii) *fd positions* `V_s` make `[V_s,−]` preserve coproducts, which the absorption in §3 needs.
Drop (i) — infinite vec-support — and `⟦p⟧` already leaves `Set × Vec_fd`. Pass to full `Vec` to
rescue (i) and you lose (ii): a non-fd `V_s` is not copower-tiny, `[V_s, ∐_t Y_t] ≠ ∐_t[V_s,Y_t]`,
and `⟦p⟧⟦q⟧` need not be an extension. That is the predecessor's Gap 1 (`Fam(Vec^op)`, infinite
`T`, infinite-dimensional positions), which remains **open**. So `Set × Vec_fd` on `𝒫` is the exact
locus where admissibility is both meaningful and provable.

---

## 2. `C` is non-collapse, non-cartesian, disconnected — the three Gap-1 coordinates

**Prop 2.1 (non-collapse).** An object `(A,V) ∈ C` is copower-tiny iff `|A| ≤ 1`.
*Proof.* `[(A,V),−]` preserves coproducts iff both components do. Vec: `[V,−]` preserves `⊕` for
`V` fd (always). Set: `(−)^A` preserves `⊔` iff `A` is subterminal, `|A| ≤ 1` (for `|A| ≥ 2`,
`(1⊔1)^A` has `2^{|A|} > 2` elements while `1^A ⊔ 1^A` has `2`). ∎ Hence objects with `|A| ≥ 2` are
not tiny: `C` is **not** a collapse base.

**Prop 2.2 (non-cartesian).** The categorical product in `C` is `(X_s × Y_s, X_v ⊕ Y_v)` (product in
`Vec_fd` is the biproduct). Since `⊗_k ≠ ⊕_k`, `⊗ ≠ ×`. ∎

**Prop 2.3 (disconnected unit).** `C(I,−) = C((1,k),−) = \mathrm{Set}(1,(-)_s) × |(-)_v| = (-)_s ×
|(-)_v|` (the Vec factor is the underlying-set functor `|−|:\mathrm{Vec}_{fd}→\mathrm{Set}`). `C(I,−)`
preserves coproducts iff both factors do, and `|−|` does **not**: the canonical
`γ_{(V_d)} : ∐_d |V_d| → |⊕_d V_d|`, `(d,v) ↦ ι_d(v)`, is not a bijection. Isolating the Vec factor,
take `V_1 = V_2 = k`: `γ : |k| ⊔ |k| → |k⊕k|`, `(1,v) ↦ (v,0)`, `(2,w) ↦ (0,w)` — it **misses**
`e_1+e_2 = (1,1)` and **double-counts** `0` (both `(1,0)` and `(2,0)` map to `0`), hence not
injective and not surjective. (Over `k=𝔽_2` both sides have `4` elements — the equal-cardinality
trap; the map itself, built, is what fails. Cf. predecessor B5.) A clean count-mismatch witness that
needs no map-building: at the family `(I,I)`, `C(I, (2,k^2)) = 2·|k|^2` while `∐_{i=1,2}C(I,I) =
2·|k|`, unequal for `|k| ≥ 2` (for `k=𝔽_2`: `8 ≠ 4`). Either way `I` is disconnected. ∎

So `C` is admissible (§3), non-collapse (2.1), non-cartesian (2.2), with disconnected unit (2.3):
a Gap-1 inhabitant. **Theorem B** (nontrivial infinitary-lextensive *cartesian closed* + admissible
⟹ unit connected) does **not** apply — `C` is not cartesian (2.2) and not extensive (the Vec factor
has a zero object; extensive + zero object ⟹ trivial). No contradiction; rather, Theorem B's
hypotheses are shown **essential**: admissibility alone does not force connectedness.

---

## 3. The construction and the natural iso (Target 1)

Fix `p = (S,(A_s,V_s)) ∈ 𝒫` and `q = (T,(B_t,W_t)) ∈ 𝒫`.

### 3.1 The composite, computed
With `Y := ⟦q⟧(X)`, `Y_s = ∐_{t∈T} X_s^{B_t}`, `Y_v = ⊕_{t∈T}[W_t, X_v]`. Then by (E),
`⟦p⟧(Y) = (\ ∐_s Y_s^{A_s}\ ,\ ⊕_s[V_s, Y_v]\ )`.

*Set component.* Using Set exponential-of-coproduct `(∐_t Z_t)^{A} = ∐_{f:A→T}∏_{a∈A}Z_{f(a)}`
with `Z_t = X_s^{B_t}` and `∏_a X_s^{B_{f(a)}} = X_s^{∐_a B_{f(a)}}`:
> `(⟦p⟧⟦q⟧X)_s = ∐_{s∈S}\ ∐_{f:A_s→T}\ X_s^{\,∐_{a∈A_s}B_{f(a)}}.`  (S)

*Vec component.* Since each `V_s` is fd (copower-tiny in `Vec`) and the sums are finite (locus),
`[V_s,−]` preserves `⊕_t`, then hom–tensor adjunction `[V,[W,X]] = [V⊗W,X]`:
> `(⟦p⟧⟦q⟧X)_v = ⊕_{s}[V_s, ⊕_t[W_t,X_v]] = ⊕_{s,t}[V_s,[W_t,X_v]] = ⊕_{s,t}[V_s⊗W_t, X_v].`  (V)

### 3.2 The container `r = p◁q ∈ 𝒫`
- **shape** `D = ∐_{s∈S} T^{A_s} = \{(s,f) : s∈S,\ f:A_s→T\}`;
- **set-position** `C_{(s,f)} = ∐_{a∈A_s} B_{f(a)}`;
- **vec-positions**: if `⊕_{s,t}V_s⊗W_t ≠ 0`, fix any slot `d_0 ∈ D` (nonempty then — see below) and
  put `U_{d_0} = ⊕_{s,t} V_s⊗W_t`, `U_d = 0` for `d ≠ d_0`; if the vec-sum is `0`, put all `U_d = 0`.

`r ∈ 𝒫`: vec-support of `r` is `⊆ \{d_0\}`, finite; `U_{d_0} = ⊕_{s,t}V_s⊗W_t` is fd because
`\{(s,t) : V_s⊗W_t ≠ 0\} = \mathrm{supp}_v(p) × \mathrm{supp}_v(q)` is finite (locus) and each
`V_s⊗W_t` is fd. *Nonemptiness of `D` when needed:* a nonzero vec-sum requires some `W_t ≠ 0`, so
`T ≠ ∅`, so every `T^{A_s} ≠ ∅` (functions into a nonempty set always exist), so `D ⊇ \{s\}×T^{A_s}
≠ ∅` and a slot `d_0` exists.

By (E), `⟦r⟧(X) = (\ ∐_{(s,f)∈D} X_s^{C_{(s,f)}}\ ,\ ⊕_{d∈D}[U_d,X_v]\ )` and
`⊕_{d∈D}[U_d,X_v] = [U_{d_0},X_v] = [⊕_{s,t}V_s⊗W_t,\ X_v]`.

### 3.3 The comparison map `Θ_X = (Θ^{\mathrm{set}}_X, Θ^{\mathrm{vec}}_X)`

**Set component** `Θ^{\mathrm{set}}_X : ∐_{(s,f)∈D} X_s^{C_{(s,f)}} \to ∐_s (∐_t X_s^{B_t})^{A_s}`.
An element of the source is `(s, f, g)` with `f:A_s→T` and `g : ∐_{a}B_{f(a)} → X_s`; write
`g_a := g|_{B_{f(a)}} : B_{f(a)} → X_s`. An element of the target is `(s, h)` with
`h : A_s → ∐_t X_s^{B_t}`. Define
> `Θ^{\mathrm{set}}_X(s,f,g) = (s, h),\qquad h(a) = (f(a),\ g_a) ∈ ∐_t X_s^{B_t}.`

**Inverse.** Given `(s,h)`, write `h(a) = (t_a, k_a)` with `t_a∈T`, `k_a:B_{t_a}→X_s`; set
`f(a) := t_a` and `g` on the `a`-th summand `B_{f(a)}` to be `k_a`. The two assignments are mutually
inverse (`f` recovers the tags `t_a`; `g` recovers the maps `k_a`), so `Θ^{\mathrm{set}}_X` is a
**bijection**. It is the classical Set-container composition iso; it is natural in `X_s` because a
map `φ_s:X_s→X'_s` post-composes both `g` and every `k_a`, and `Θ^{\mathrm{set}}` is defined by
regrouping these post-composable data.

**Vec component** `Θ^{\mathrm{vec}}_X : [⊕_{s,t}V_s⊗W_t,\ X_v] \to ⊕_s[V_s, ⊕_t[W_t,X_v]]`, the
composite of four isomorphisms, each natural in `X_v`:
> `[⊕_{s,t}V_s⊗W_t, X_v]\ \xrightarrow{≅}\ ∏_{s,t}[V_s⊗W_t,X_v]` (hom out of a coproduct = product,
>   universal property) `\ =\ ⊕_{s,t}[V_s⊗W_t,X_v]` (finite support ⟹ product = coproduct)
> `\ \xrightarrow{≅}\ ⊕_{s,t}[V_s,[W_t,X_v]]` (tensor–hom adjunction, natural)
> `\ \xrightarrow{≅}\ ⊕_s[V_s, ⊕_t[W_t,X_v]]` (`V_s` fd ⟹ `[V_s,−]` preserves the finite `⊕_t`).

Each arrow is a natural isomorphism of functors of `X_v`; hence `Θ^{\mathrm{vec}}_X` is a natural
iso. The concrete matrix: a linear map `M : ⊕_{s,t}V_s⊗W_t → X_v` goes to the tuple of its
restrictions `M∘ι_{s,t} : V_s⊗W_t → X_v`, each reshaped by tensor–hom to `V_s → [W_t,X_v]`, and
regrouped over `t` into `V_s → ⊕_t[W_t,X_v]`.

**Theorem 3.1.** `Θ_X = (Θ^{\mathrm{set}}_X, Θ^{\mathrm{vec}}_X)` is a natural isomorphism
`⟦p◁q⟧ ⟹ ⟦p⟧∘⟦q⟧` of endofunctors of `C`. Consequently `𝒫` is `◁`-admissible.
*Proof.* Both components are isomorphisms (a bijection of sets; a natural linear iso) and both are
natural (in `X_s`, resp. `X_v`); a morphism of `C = Set × Vec_fd` is a pair, and naturality is
checked componentwise. So `Θ` is a natural iso. `r ∈ 𝒫` by §3.2, and `𝒫` is closed under `◁`. ∎

**Boundary cases.** `S = ∅` or `T = ∅`: then `p` or `q` is initial and both sides are the initial
family; `Θ` is the empty map. All `V_s = 0` (`p` set-supported) or all `W_t = 0`: the vec-sum is `0`
and both Vec components are `0`. If `T = ∅` but some `A_s = ∅`, `D = \{s : A_s = ∅\}` and all
`U_d = 0` — matches `⟦p⟧(∅,0)`. All handled uniformly by §3.2–3.3.

---

## 4. Coherence: the obstruction is Theorem D

Admissibility (Def 1.1) asks only for the existence of `r` with `⟦r⟧ ≅ ⟦p⟧⟦q⟧`, which §3 supplies.
Whether `◁` is a *monoidal product* on `𝒫` is a separate — and subtler — question.

**Unit.** `y := ({∗},(1,k))`, `⟦y⟧(X) = [(1,k),X] = (X_s^1,[k,X_v]) = X`. So `y` is a two-sided unit
for `◁` up to the iso of §3 (`p◁y ≅ p ≅ y◁p`).

**No canonical associator.** The construction chose a slot `d_0 ∈ D = ∐_s T^{A_s}`; there is no
natural such choice (no canonical element of `∐_s T^{A_s}`), so `(p◁q)◁r` and `p◁(q◁r)` are, as
*objects* of `𝒫`, generally different presentations of the same functor — precisely the
non-injectivity of `⟦−⟧` on the Vec factor (**Theorem D**: over a disconnected base `⟦−⟧` is not
faithful, so `◁` is a *choice*).

**A non-canonical monoidal structure exists.** The Set factor is rigid: `D` and `C_{(s,f)}` are
forced, and Set-container composition is *canonically* associative (the monoidal category of
polynomial functors). On the Vec factor both `(p◁q)◁r` and `p◁(q◁r)` concentrate the entire
`⊕_{s,t,u}V_s⊗W_t⊗Z_u` at a single slot; choosing the two slots to correspond under the Set
associator gives an isomorphism `(p◁q)◁r ≅ p◁(q◁r)`. Hence a monoidal structure on `(𝒫,◁,y)`
exists, but only after a global (choice-dependent) selection of concentration slots.

**Verdict.** The *canonical* monoid is the image `⟦𝒫⟧ ⊆ [C,C]` under composition (strictly
associative, unital). The obstruction to transporting it canonically back to `𝒫` is exactly
`⟦−⟧`'s non-faithfulness on the flexible factor. This is the honest content of "`◁` picks a slot":
it is not a defect of the construction but the disconnected-base phenomenon of Theorem D.

---

## 5. Target 2: the dual-numbers probe, and the whole fg-module family, refuted

**Lemma 5.1 (fg ⟹ copower-tiny, any ring).** For a ring `R` and a finitely generated left
`R`-module `P`, `\mathrm{Hom}_R(P,−)` preserves coproducts.
*Proof.* Let `p_1,…,p_n` generate `P`. Any `φ : P → ⊕_{i∈I}M_i` sends each `p_j` into a finite
subsum `⊕_{i∈F_j}M_i` (elements of a coproduct have finite support). With `F = ⋃_j F_j` (finite),
`R`-linearity and generation give `φ(P) ⊆ ⊕_{i∈F}M_i`, so `φ` factors through the finite subsum.
Therefore `\mathrm{Hom}_R(P,⊕_I M_i) = ⋃_{F\ \text{fin}}\mathrm{Hom}_R(P,⊕_{i∈F}M_i) =
⊕_{i∈I}\mathrm{Hom}_R(P,M_i)`, the canonical map being a bijection. ∎

**Corollary 5.2.** For `R` commutative Noetherian, `fg\text{-}R\text{-Mod}` (closed symmetric
monoidal: `⊗_R`, `[−,−] = \mathrm{Hom}_R`, unit `R`, `\mathrm{Hom}_R` of fg is fg over Noetherian
`R`) is a **collapse base**: every object is copower-tiny (Lemma 5.1), so `◁ = ⊗_R` on the
finite-support locus (T4-left Prop 2.1), exactly as for `Vec_fd = fg\text{-}k\text{-Mod}`. Its unit
is disconnected (zero object, Lemma D′). It sits on the **collapse pole**, never Gap 1.

**Corollary 5.3 (dual numbers refuted).** `R = k[ε]/ε²` is local Artinian; `fg\text{-}R\text{-Mod} =
`(finite-length `= `fd-over-`k`) `R`-modules, every one copower-tiny. In particular `k = R/εR` is
copower-tiny: `\mathrm{Hom}_R(k,−) = \ker(ε:−→−)` preserves `⊕` (kernels commute with direct sums)
— **despite `k` being non-projective / non-dualizable** (`R → k` has no `R`-linear section). So the
brief's "internal rigid/flexible mix" is the *dualizable-vs-not* distinction, which is **not** the
programme's axis. Copower-tiny `=` finitely generated; Artinian `⟹` all fg `⟹` all tiny `⟹`
collapse. `k[ε]/ε²` is **not** a Gap-1 inhabitant, and Lemma 5.1 kills the entire "modules over a
mixed ring" family (`k[x]`, `ℤ`, glued/pullback module categories) in one stroke.

---

## 6. The classifying axis, sharpened (structural)

**Prop 6.1 (admissibility is per-object).** Call `P ∈ C` **absorptive** if `X ↦ [P,⟦q⟧(X)]` is an
extension (in the image of `⟦−⟧`) for every `q ∈ Fam(C^op)`. Then `Fam(C^op)` is `◁`-admissible
**⟺ every object of `C` is absorptive**.
*Proof.* (⟸) `⟦p⟧⟦q⟧(X) = ∐_s[P_s,⟦q⟧(X)]`; each summand is an extension (`P_s` absorptive at this
`q`) and a coproduct of extensions is an extension. (⟹) take `p = ⟨P⟩`. ∎

**Two sources of absorptivity.**
- *Copower-tiny (flexible)* `P`: `[P,⟦q⟧X] = [P,∐_t[Q_t,X]] = ∐_t[P⊗Q_t,X]` — extension.
- *Distributive/extensive (rigid)* `P`: `[P,∐_tY_t] = ∐_{f:P→T}∏_a Y_{f(a)}`, `∏_a[Q,X] = [∐Q,X]`
  — extension (the Set mechanism of §3.1).

**The seam.** Additive-fg bases: every object copower-tiny (Lemma 5.1) ⟹ collapse pole, connected
unit fails but non-collapse fails too. Extensive non-collapse bases: connected unit **forced**
(Theorem B). So a base that is admissible, non-collapse, **and** disconnected must run **both**
mechanisms. `Set × Vec_fd` does so by *factoring* them: `(A,V)` is absorptive because `A` is rigid
(Set) and `V` is flexible (Vec). The absorptive dichotomy conjecture below says this factoring is
the general shape.

**Conjecture 6.2 (absorptive dichotomy / decomposition).** Over a closed symmetric monoidal
cocomplete base, every absorptive object is a tensor of a copower-tiny part and a distributive part;
consequently every "nice" `◁`-admissible base decomposes, and every "nice" Gap-1 inhabitant is
`rigid\text{-}extensive × flexible\text{-}additive`. *Evidence:* `Set/`topos (distributive part
only), `Vec_fd`/`fg-R-Mod` (tiny part only), `Set × Vec_fd` (both, product). *Consequence if true:*
**no irreducible Gap-1 inhabitant exists among nice bases** — the named gap is inhabited but every
inhabitant reduces. This replaces cartesianness and idempotent-splitting as the classifying axis and
answers Neil's #1 `◁`-generality question in one statement.

**What an irreducible inhabitant would need (precise open problem).** A closed symmetric monoidal
cocomplete base, **indecomposable** (no `I ≅ I_1 ⊔ I_2` with `I_i⊗I_j ≅ 0`), `◁`-admissible,
non-collapse, disconnected unit. By §5 it is **not** any `fg-R-Mod`. If additive, it has a non-fg
(non-copower-tiny) object and the absorption needs infinite direct sums — **this is exactly
predecessor Gap 1** (full `Vec`), open. If non-additive, its unit is disconnected by *non-injectivity*
of `γ`; the only such base known is `Set_*`, which is **inadmissible** (Theorem A). Conjecture: every
`γ`-non-injective closed base is inadmissible (a strengthening of Theorem A). So irreducible Gap-1
is currently pinned between two open doors, both identified.

---

## 7. Verification (`scratch/2026-09-01-gap1-verify.py`)

- **Task 1 (target 1).** Three concrete cases over `𝔽_2`, incl. two asymmetric (`A_s`, `B_t`
  varying) and one with zero vector positions:

  | case | `|D|` | Set LHS/RHS | `Θ^{set}` bijection | Vec LHS/RHS dim | `Θ^{vec}` invertible | naturality (Set / Vec) |
  |---|---|---|---|---|---|---|
  | (a) | 4 | 16 / 16 | **YES** (inj+surj+inverse) | 4 / 4 | **YES** (perm., full rank) | YES / YES |
  | (b) asym | 6 | 42 / 42 | **YES** | 6 / 6 | **YES** | YES / YES |
  | (c) `V_s=0,W_t=0` | 6 | 42 / 42 | **YES** | 2 / 2 | **YES** | YES / YES |

  `Θ^{set}` built pointwise `(s,f,g) ↦ (s,h)`, `h(a)=(f(a),g|_{a})`, verified a **bijection** with
  inverse round-tripping both ways (exhaustive). `Θ^{vec}` built as block-restriction ∘ tensor–hom
  reshape ∘ regroup — it is a **coordinate permutation** `(s,t,i,j,k) ↔ (s,t,k,j,i)`, full rank over
  `𝔽_2`. **Naturality** squares (both components) commute exactly for a nontrivial `φ:X→X'`
  (`φ_s` a size-shift, `φ_v` a random `𝔽_2` matrix). `Θ` is a natural iso in all cases. *This is a
  built map, not a cardinality match.*
- **Task 2 (target 2).** Over `R = 𝔽_2[ε]/ε²` (modules `= (dim, N)`, `N²=0`; `R`-maps `= 𝔽_2`-maps
  commuting with `N`): (2a) `\dim\mathrm{Hom}_R(P,⊕M_i) = Σ_i \dim\mathrm{Hom}_R(P,M_i)` on 50
  random instances + `P ∈ \{k,R,R⊕k\}`, **0 mismatches** (every fg module copower-tiny); (2b)
  `\dim\mathrm{Hom}_R(P,⊕_t\mathrm{Hom}_R(Q_t,X)) = Σ_t\dim\mathrm{Hom}_R(P⊗_R Q_t,X)` on 50 random
  instances (genuine `⊗_R`), **0 mismatches** (collapse `◁=⊗_R`); (2c) `π:R→k` is `R`-linear,
  `\dim\mathrm{Hom}_R(k,R)=1` but exhaustive search finds **no** `R`-linear section — `k` is **not**
  projective/dualizable, yet **is** copower-tiny. Copower-tiny `⊊` dualizable, confirmed.

---

## 8. Status ledger

| claim | grade | basis |
|---|---|---|
| Lemma 1.1 (locus = finite vec-support) | **proved** | §1 |
| Prop 2.1 (non-collapse), 2.2 (non-cartesian), 2.3 (disconnected) | **proved** | §2 |
| **Theorem 3.1** (natural iso `⟦p◁q⟧ ≅ ⟦p⟧⟦q⟧`; `𝒫` admissible) | **proved** | §3 (map built) + Task 1 |
| `Set × Vec_fd` a Gap-1 inhabitant; Theorem B not sharp | **proved** | §2 + §3 |
| §4 coherence (no canonical monoidal; non-canonical exists) | **proved** | §4 + Thm D (cited) |
| **Lemma 5.1** (fg ⟹ copower-tiny) | **proved** | §5 |
| Cor 5.2 (fg-R-Mod collapse), 5.3 (dual numbers refuted) | **proved** | §5 + Task 2 |
| **Prop 6.1** (admissibility ⟺ every object absorptive) | **proved** | §6 |
| Conjecture 6.2 (absorptive dichotomy / decomposition) | **speculative** | §6 |
| irreducible Gap-1 pinned between predecessor Gap 1 and Thm-A-strengthening | **open (precise)** | §6 |

**Novelty gate (open, flagged).** The `Set × Vec_fd` construction is elementary and likely
folklore-adjacent to `Fam(V)` / generalized-polynomial literature; DJN `2305.05655` pose base
conditions as future work (§6) but prove no such characterisation. Prop 6.1 and Conjecture 6.2 are
the programme's own framing. Check Carboni–Lack–Walters and DJN before any priority claim on the
per-object reformulation.
