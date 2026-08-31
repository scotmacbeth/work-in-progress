# When does `Fam(C^op)` admit `◁` at all — and is unit-connectedness NECESSARY?
### Gap 3 of `left-adjoint-over-vec` resolved on both poles; the §9bis dichotomy REFUTED by `Set_*`

**MacBeth — 2026-08-30 (PROVE session, third of the day).**
Predecessor: `proofs/2026-08-30-left-adjoint-over-vec.md` (`proved`), whose **Gap 3** and whose
`speculative` **§9bis conjecture** are the entire subject of this file.
Companion code: `scratch/connectedness-converse/verify.py` (5 blocks, all green, §7).
Registry: extends `proofs/registry/left-adjoint-over-vec.json` (new subtree `gap3-converse`).

---

## EXECUTIVE SUMMARY

The predecessor proved **Theorem 1**: over any closed symmetric monoidal cocomplete `C`, if the
monoidal unit `I` is **connected** (`C(I,−)` preserves small coproducts) then `F_q = Fam(⟦q⟧^op)`
is left adjoint to `L_q := (−)◁q`, for **every** `q`. It left open the converse (Gap 3) and floated
a dichotomy (§9bis, `speculative`): *`◁` exists on `Fam(C^op)` essentially only when `1_C` is a
generator (the `Set` pole) or `1_C ≅ 0_C` (the linear pole).* Four results.

**(A) The §9bis dichotomy is REFUTED, by `Set_*`.** Pointed sets under smash have a **zero object**
(`1_C ≅ 0_C = ∗`), so the §9bis copower criterion is vacuous there — yet `Fam(Set_*^op)` is **not**
closed under `◁`. Witness: `p = ⟨S^0∨S^0⟩`, `q = ({1,2},(S^0,S^0))`, so `⟦p⟧⟦q⟧X = (X∨X)^2`, and a
polynomial-degree count shows no family `(N_d)` of pointed sets has `⋁_d[N_d,X] ≅ (X∨X)^2`. The
forced multiplicities are `b = 4` summands with `|N_d|=3` and `a = −4` with `|N_d|=2`. **Having a
zero object does not buy admissibility** (§3, Theorem A).

**(B) On the extensive pole the converse is not merely true — it is FORCED.** (§4, **Theorem B**)

> Let `C` be nontrivial, **infinitary lextensive and cartesian closed**. If `Fam(C^op)` is closed
> under `◁`, then the unit `1 = I` is **connected**.

So on that whole pole one *cannot* even pose a counterexample to Theorem 1: admissibility already
implies the hypothesis, hence (Theorem 1) implies the conclusion. The mechanism is sharp and is
exactly what killed `Set×Set`: if `1 ≅ A ⊔ B` nontrivially then `C ≃ C/A × C/B`, and `Fam(C^op)`
carries **one external shape set for both components**, while `[A, T·1] = (T·1_1, 1_2)` demands two
different ones.

**(C) On the collapse pole the unit is ALWAYS disconnected.** (§5, **Lemma D**) If every object of
`C` is tiny — the hypothesis under which `◁` collapses to `⊗` (T4-left Prop 2.1) — then `I` is
disconnected, by a two-step diagram chase with **no cardinality argument** (cardinalities collide;
see §7 B5). Combined with the predecessor's Theorem 2 (`left adjoint ⟺ |T|=1` on the collapse
locus), the converse holds there too, and for the sharpest possible reason: it fails at `|T| = 2`.

**(D) And the reason the converse cannot be upgraded to a statement about `C` alone is the
converse's own hypothesis.** (§6, **Theorem D**) When `I` is connected, `⟦−⟧` is full and faithful
(T1), hence injective on objects up to iso, so `p◁q` is **determined** by `⟦p◁q⟧ ≅ ⟦p⟧⟦q⟧` and
"`L_q` has a left adjoint" is a property of `C`. When `I` is disconnected it is not: over `Vec_fd`,
`({∗},k^2)` and `({1,2},k)` present the same functor `X ↦ X ⊕ X` and are **not isomorphic**, so `◁`
is a *choice* and left-adjointness is a property of the choice. **Exactly when Theorem 1's
hypothesis fails, the converse stops being a question about `C`.**

**Verdict on Gap 3.** The converse of Theorem 1 holds on **both** poles where the question is
well-posed, and by (D) it is not well-posed off them without fixing `◁`. A separator would have to
be `◁`-admissible, non-collapse, and neither lextensive-cartesian; the one natural candidate in
that region — `Set_*` — is inadmissible by (A). **Gap 3 is closed as far as the question exists.**

**The trichotomy that replaces §9bis:**

| base | admissible? | `I` connected? | left adjoint to `L_q` |
|---|---|---|---|
| `Set`, any infinitary-lextensive ccc topos | **yes ⟹ connected (Thm B)** | ✓ forced | **always** (Thm 1) |
| `Vec`, `Vec_fd`, additive/tiny bases (collapse) | yes on the collapse locus | ✗ forced (**Lem D**) | iff `\|T\|=1` (Thm 2) |
| `Set×Set` (lextensive ccc, `1` decomposable) | **no** (Thm B / Prop 9.1) | ✗ | question does not arise |
| `Set_*` (zero object, neither pole) | **no** (**Thm A**) | ✗ | question does not arise |

---

## 1. Setting and the one definition that carries the file

`C` is closed symmetric monoidal and cocomplete; `I` the unit, `[−,−]` the internal hom, `0_C` the
initial object. `Fam(C^op)` has objects `p = (S,P)` with `S` a small set and `P_s ∈ C`, hom-sets

> `Fam((A,X),(B,Y)) = ∏_{a∈A} ∐_{b∈B} C(Y_b, X_a)`,                                     (H)

and extension `⟦S,P⟧X = ∐_{s∈S}[P_s,X]`. Generators `⟨Z⟩ := ({∗},Z)`. `T·X := ∐_{t∈T}X` is the
copower. `Dirichlet/Day tensor `p⊗q = (S×T, P_s⊗Q_t)`.

**Lemma 1.0.** `C` has a terminal object, namely `1_C := [0_C, X]` for any `X`; and `[Q,1_C] ≅ 1_C`
for every `Q`.
*Proof.* `C(Y,[0_C,X]) ≅ C(Y⊗0_C, X) ≅ C(0_C,X) = 1`, using that `Y⊗−` is a left adjoint (closed)
and so preserves the initial object. Likewise `C(Y,[Q,1_C]) ≅ C(Y⊗Q,1_C) = 1`. ∎ *(`proved`)*

**Definition 1.1 (admissibility).** `C` is **`◁`-admissible** if for all `p,q ∈ Fam(C^op)` there is
an object `p◁q ∈ Fam(C^op)` with `⟦p◁q⟧ ≅ ⟦p⟧∘⟦q⟧`.

*This is deliberately the weakest possible hypothesis* — mere closure of the image of `⟦−⟧` under
composition, no monoidal structure, no canonicity, no choice of presentation. Every **negative**
result below is proved against it, and is therefore as strong as it can be.

**Definition 1.2 (connected unit; T1's condition).** `I` is **connected** if for every small family
`(X_d)_{d∈D}` the canonical map

> `γ_{(X_d)} : ∐^{Set}_{d} C(I,X_d) ⟶ C(I, ∐^C_d X_d)`,   `(d,f) ↦ ι_d ∘ f`,              (γ)

is a bijection. (`fullness-unit-connectedness`, `proved` 2026-08-25: `⟦−⟧` is full and faithful
⟺ `I` is connected.)

**Lemma 1.3 (isos in a free coproduct completion; predecessor Lemma 1.2, cited).**
`(S,P) ≅ (S',P')` in `Fam(D)` iff there is a bijection `β : S → S'` with `P_s ≅ P'_{βs}`.
*(`proved`, `2026-08-30-left-adjoint-over-vec.md` §1.)*

---

## 2. The shape criterion — the only necessary condition we will need

**Lemma S.** Let `C` be `◁`-admissible. Then for every `P ∈ C` and every small set `T`, the object
`[P, T·1_C]` is a **copower of `1_C`**.

*Proof.* Fix `T` and let `q := (T,Q)` be any object with shape set `T` (e.g. `Q_t := 0_C`). By
Lemma 1.0, `⟦q⟧(1_C) = ∐_{t∈T}[Q_t,1_C] ≅ ∐_{t∈T}1_C = T·1_C`. Put `p := ⟨P⟩`, so
`⟦p⟧(⟦q⟧(1_C)) ≅ [P, T·1_C]`. By admissibility there is `p◁q = (D,N)` with `⟦p◁q⟧ ≅ ⟦p⟧⟦q⟧`;
evaluating at `1_C` and using Lemma 1.0 again,
`⟦p◁q⟧(1_C) = ∐_{d∈D}[N_d,1_C] ≅ ∐_{d∈D}1_C = D·1_C`. Hence `[P,T·1_C] ≅ D·1_C`. ∎ *(`proved`)*

**Reading.** `D` is the **shape set** of `p◁q`, and it is an *external* set — one set, not one per
"component" of `C`. Lemma S says the base must be able to *see* that external set inside itself, as
a copower of its terminal object. Over `Set` this is vacuous (`1_C = 1` and every set is a copower
of it — and the copower count `T^{P}` is exactly the decoration set of the predecessor's §2). Over
`Vec` it is vacuous the other way (`1_C = 0`, so `E·1_C = 0` always, and the shape data is
*invisible* to `⟦−⟧` — which is precisely why `◁` needs a convention there). **The whole content of
this file is that between those two degeneracies the criterion has teeth.**

---

## 3. Theorem A — `Set_*` refutes the §9bis dichotomy

`Set_*` = pointed sets, `⊗ =` smash, `I = S^0` (two points), `[A,B] =` pointed maps (based at the
constant map), coproduct `=` wedge `∨`, `0_C = 1_C = ∗` a **zero object**. It is closed symmetric
monoidal and cocomplete. Since `1_C ≅ 0_C`, Lemma S is vacuous and the §9bis conjecture predicts
`Set_*` should be admissible ("the linear pole"). It is not.

**Theorem A.** `Set_*` is **not** `◁`-admissible. Explicitly, for
`p := ⟨S^0 ∨ S^0⟩` and `q := ({1,2},(S^0,S^0))` there is no object of `Fam(Set_*^op)` whose
extension is `⟦p⟧∘⟦q⟧`.

*Proof.* `[S^0,X] ≅ X` (a pointed map out of `S^0` is a point of `X`), so
`⟦q⟧X = [S^0,X] ∨ [S^0,X] ≅ X ∨ X`. A pointed map out of a wedge is a pair of pointed maps, so
`⟦p⟧Y = [S^0∨S^0, Y] ≅ Y × Y`. Hence

> `⟦p⟧⟦q⟧X ≅ (X∨X) × (X∨X)`.

Suppose `p◁q = (D,N)` existed, so `⋁_{d∈D}[N_d,X] ≅ (X∨X)^2` naturally, hence bijectively at every
`X`. Write `m := |X| − 1` and `n_d := |N_d| − 1` (counts of non-basepoint elements). Then
`|X∨X| = 2m+1`, `|[N,X]| = (m+1)^{n}`, and `|⋁_d Y_d| = 1 + Σ_d(|Y_d| − 1)`. So the required
identity is, for every `m ≥ 0`,

> `1 + Σ_{d∈D}\big((m+1)^{n_d} − 1\big) = (2m+1)^2 = 4m^2 + 4m + 1`.                     (∗)

Summands with `n_d = 0` (i.e. `N_d ≅ ∗`) contribute `0` and may be discarded. If infinitely many
`n_d ≥ 1` survive, the left side of (∗) is infinite at `m = 1` while the right side is `9`; so only
finitely many survive and (∗) is an identity of **polynomials** in `m`. Now
`(m+1)^{n} − 1 = Σ_{j=1}^{n}\binom{n}{j}m^j` has degree `n` and **all coefficients positive**, so no
cancellation between summands is possible; comparing degrees forces every `n_d ∈ \{1,2\}`. Writing
`a := \#\{d : n_d = 1\}` and `b := \#\{d : n_d = 2\}`, (∗) reads

> `a·m + b·(m^2 + 2m) = 4m^2 + 4m`  ⟹  `b = 4` and `a + 2b = 4`  ⟹  `a = −4`,

which is not a cardinality. Contradiction. ∎ *(`proved`; verified §7 B1)*

**Corollary A′ (§9bis dichotomy REFUTED).** The predecessor conjectured that `◁` exists on
`Fam(C^op)` "essentially only when `1_C` is a generator (the `Set` pole) or `1_C ≅ 0_C` (the linear
pole) — in which case Theorems 1 and 2 are jointly exhaustive". `Set_*` satisfies `1_C ≅ 0_C`, and
**neither theorem applies to it**: `I = S^0` is disconnected (so not Theorem 1) and `S^0∨S^0` is not
tiny (so not Theorem 2). The two conditions therefore do **not** carve out the admissible bases, and
Theorems 1 and 2 are **not** jointly exhaustive over the class the conjecture describes. `1_C ≅ 0_C`
is a symptom of the linear pole, not a characterisation of it.

**Where `Set_*` sits.** It is on **neither** pole. It is not extensive (the wedge is not a disjoint
coproduct: the basepoints are identified — indeed `γ` fails for `I = S^0` by *non-injectivity*,
§7 B5). It is not additive. And it is not on the collapse locus: `S^0` is tiny (`[S^0,−] = Id`) but
`S^0∨S^0` is **not** (`[S^0∨S^0, A∨B] ≅ (A∨B)^2 ≇ A^2 ∨ B^2`; §7 B1). *The failure of `◁` is
exactly the failure of tininess at `S^0∨S^0` with nothing — no distributivity, no additivity — to
replace it.* `Set_*` is the base where the two known mechanisms both switch off.

---

## 4. Theorem B — on the extensive pole, admissibility FORCES connectedness

Throughout: `C` is **infinitary lextensive** (finite limits; `C/(∐_d A_d) ≃ ∏_d C/A_d` for all
small coproducts) and **cartesian closed**, so `⊗ = ×`, `I = 1`, and `[X,Y] = Y^X`. "Nontrivial"
means `1 ≇ 0`. Recall that in such a `C` coproducts are disjoint (injections monic, pullbacks of
distinct injections initial) and `0` is strict.

**Lemma E1 (rigidity of the terminal object).** If `1 ≅ 1 ⊔ Z` then `Z ≅ 0`.
*Proof.* Let `θ : 1 ⊔ Z → 1` be an isomorphism, with coproduct injections `i : 1 → 1⊔Z` and
`j : Z → 1⊔Z`. Then `θi : 1 → 1` is a morphism into the terminal object, hence `θi = id_1`.
Disjointness of the coproduct says the pullback of `i` along `j` is `0`; since `θ` is an
isomorphism, the pullback of `θi` along `θj` is also `0`. But `θi = id_1`, and the pullback of
`id_1` along any morphism `θj : Z → 1` is `Z` itself. Hence `Z ≅ 0`. ∎ *(`proved`)*

**Lemma E2.** If `1 ≇ 0` and `E·1 ≅ 1` for a set `E`, then `|E| = 1`.
*Proof.* `E = ∅` gives `0 ≅ 1`, excluded. If `|E| ≥ 2`, pick `e_0 ∈ E` and set
`Z := (E∖\{e_0\})·1`, so `1 ≅ E·1 ≅ 1 ⊔ Z` and Lemma E1 gives `Z ≅ 0`. But `|E∖\{e_0\}| ≥ 1`, so
`Z` has `1` as a coproduct summand, giving a morphism `1 → Z ≅ 0`; strictness of `0` then gives
`1 ≅ 0`, excluded. ∎ *(`proved`)*

**Lemma E0 (disconnected ⟹ decomposable).** If `1 ≇ 0` and `1` is **not** connected, then
`1 ≅ A ⊔ B` with `A ≇ 0` and `B ≇ 0`.
*Proof.* Let `(X_d)_{d∈D}` be a family for which `γ` fails.
*`γ` is always injective here.* Suppose `ι_{d_0}f = ι_{d_1}g` with `f : 1 → X_{d_0}`,
`g : 1 → X_{d_1}`. If `d_0 ≠ d_1`, the pullback of `ι_{d_0}` and `ι_{d_1}` is `0` by disjointness,
and `(f,g)` induces a morphism `1 → 0`, so `1 ≅ 0` by strictness — excluded. If `d_0 = d_1`, then
`f = g` because coproduct injections are monic; so the two elements of `∐_d C(1,X_d)` coincide.
*Hence `γ` fails to be surjective:* there is `h : 1 → ∐_d X_d` factoring through no injection.
Infinitary extensivity: pulling the coproduct decomposition back along `h` gives `1 ≅ ∐_d A_d` with
`A_d := h^*X_d`. If every `A_d ≅ 0` then `1 ≅ 0`, excluded. If exactly one `A_{d_0} ≇ 0`, then
`1 ≅ A_{d_0}` and the pullback square exhibits `h` as factoring through `ι_{d_0}` — excluded. So at
least two are non-initial; grouping, `1 ≅ A_{d_0} ⊔ (∐_{d≠d_0}A_d)` with both parts non-initial
(if the second were `0`, strictness would force each `A_d ≅ 0`). ∎ *(`proved`)*

**Theorem B.** Let `C` be nontrivial, infinitary lextensive and cartesian closed. If `C` is
`◁`-admissible, then `1` is connected. Consequently, by Theorem 1 of the predecessor,
`L_q = (−)◁q` has a left adjoint `F_q = Fam(⟦q⟧^op)` for **every** `q`.

*Proof.* Suppose `1` is not connected. By Lemma E0, `1 ≅ A ⊔ B` with `A, B ≇ 0`. Extensivity gives
an equivalence `C ≃ C/1 ≃ C/A × C/B`; write `C_1 := C/A`, `C_2 := C/B`. Both are infinitary
lextensive (slices inherit) and nontrivial (`1_{C_i} ≅ 0_{C_i}` would force `A ≅ 0` resp. `B ≅ 0`).

*Both factors are cartesian closed, with all structure componentwise.* Limits and colimits in a
product category are computed componentwise. For exponentials: given `X = (X_1,X_2)`,
`Y = (Y_1,Y_2)`, write `Y^X = (W_1,W_2)` in `C`. For `Z_1 ∈ C_1`,
`C((Z_1,0),(W_1,W_2)) ≅ C((Z_1,0)×X, Y) = C((Z_1×X_1, 0×X_2), Y)`, and `0×X_2 ≅ 0` because `−×X_2`
is a left adjoint; as `C_2(0,−)` is a singleton on both sides, this reads
`C_1(Z_1,W_1) ≅ C_1(Z_1×X_1, Y_1)` naturally in `Z_1`, so `W_1 = Y_1^{X_1}`. Symmetrically for
`W_2`. In particular `Y^0 ≅ 1` and `Y^1 ≅ Y` in each factor.

Under the equivalence, `1 ↔ (1_{C_1},1_{C_2})` and `A ↔ (1_{C_1}, 0_{C_2})`. Take any `T` with
`|T| ≥ 2`. Then

> `[A, T·1] = \big((T·1_{C_1})^{1_{C_1}},\ (T·1_{C_2})^{0_{C_2}}\big) ≅ (T·1_{C_1},\ 1_{C_2})`.

By Lemma S (admissibility) there is a set `E` with `[A,T·1] ≅ E·1 = (E·1_{C_1}, E·1_{C_2})`.
Isomorphisms in a product category are componentwise, so
`1_{C_2} ≅ E·1_{C_2}` and `T·1_{C_1} ≅ E·1_{C_1}`. Lemma E2 applied in `C_2` gives `|E| = 1`;
then `T·1_{C_1} ≅ 1_{C_1}` and Lemma E2 applied in `C_1` gives `|T| = 1`, contradicting `|T| ≥ 2`.
∎ *(`proved`; verified §7 B2 on `Set×Set`)*

**What went wrong, in one sentence.** `Fam(C^op)` gives an object **one external shape set**; when
`C` splits, the composite `⟦p⟧⟦q⟧` wants **one shape set per factor**, and `[A, T·1] = (T·1_1,1_2)`
is precisely a demand for the two counts `|T|` and `1` at once.

**Corollary B′.** `Set × Set` is not `◁`-admissible — the predecessor's Prop 9.1, now an instance of
a theorem rather than a computation, and with the obstruction relocated: it is visible already at
`p = ⟨A⟩` for `A` a nontrivial summand of `1`, without needing a non-diagonal `P`.

**Corollary B″ (Gap 3 on the extensive pole).** There is **no** counterexample to the converse of
Theorem 1 among nontrivial infinitary-lextensive cartesian closed bases: admissibility already
implies the hypothesis. In this regime "`I` connected", "`◁` exists", and "`L_q` has a left adjoint
for every `q`" are all **equivalent**.

---

## 5. Lemma D — on the collapse pole the unit is always disconnected

**Lemma D.** Suppose every object of `C` is **copower-tiny**: for all `P, X` and all small `T`, the
canonical comparison `∐_{t∈T}[P,X] → [P, T·X]`, `(t,f) ↦ ι_t∘f`, is an isomorphism. (This is the
hypothesis of T4-left Prop 2.1 under which `p◁q = p⊗q`.) Then `I` is **not** connected.

*Proof.* Suppose `I` were connected. Take `T = \{1,2\}`, `X = I`, so `T·X = I ⊔ I`. Consider the
map

> `μ : C(I⊔I, I) ⊔ C(I⊔I, I) ⟶ C(I⊔I, I⊔I)`,   `(d,f) ↦ ι_d ∘ f`.

It is the composite of canonical isomorphisms
`C(I⊔I,I⊔I) ≅ C(I,[I⊔I, 2·I]) ≅ C(I, 2·[I⊔I,I]) ≅ 2·C(I,[I⊔I,I]) ≅ C(I⊔I,I) ⊔ C(I⊔I,I)`:
the first and last by closedness (`I⊗A ≅ A`), the second by copower-tininess of `I⊔I`, the third by
`γ` (connectedness of `I`). Each comparison map is "post-compose with `ι_d`", so the composite is
`μ`, and `μ` is a bijection.

Hence `id_{I⊔I} = ι_{d_0}∘f` for a unique pair `(d_0, f)` with `f : I⊔I → I`; say `d_0 = 1`.
Pre-compose with the other injection `ι_2 : I → I⊔I`:

> `ι_2 = id_{I⊔I}∘ι_2 = ι_1∘(f∘ι_2)`,   where `f∘ι_2 : I → I`.

Now apply `γ` at the copower `2·I = I ⊔ I`: connectedness says
`C(I,I) ⊔ C(I,I) → C(I, I⊔I)`, `(d,h) ↦ ι_d∘h`, is a bijection. But `(2, id_I)` and `(1, f∘ι_2)`
are **distinct** elements of the disjoint union (different tags) with the **same** image `ι_2`.
That contradicts injectivity. ∎ *(`proved`; no cardinality argument is used — see the trap in §7 B5)*

**Lemma D′ (the additive route).** If `C` has a zero object then `I` is not connected: for
`T = \{1,2\}`, `X_1 = X_2 = I`, the elements `(1, 0_{I,I})` and `(2, 0_{I,I})` of `C(I,I)⊔C(I,I)`
both map to the zero morphism `I → I⊔I`, so `γ` is not injective. ∎ *(`proved`; predecessor §1)*

**Corollary D″ (Gap 3 on the collapse pole).** On the collapse locus, `I` is disconnected
(Lemma D or D′) **and** `L_q` has a left adjoint iff `|T| = 1` (predecessor Theorem 2). Since
`Fam(C^op)` always contains objects with `|T| ≥ 2`, "left adjoint for every `q`" fails. So the
converse of Theorem 1 holds here too, and it fails at the smallest possible witness.

**A two-line reproof of Theorem 2's necessity, in any base.** The predecessor's §2 comparison map
is, on the collapse locus, `κ_{B,Z} : ∐_t C(B,[Q_t,Z]) → C(B, ∐_t[Q_t,Z])` — that is **`γ` with the
probe `I` replaced by `B`**. Connectedness is the probe `B = I`. The **fatal probe is `B = 0_C`**:
then `C(0_C, Y) = 1` for every `Y`, so the left side has `|T|` elements and the right side has one.
Hence `|T| = 1`. *(`proved`; §7 B4.)* This is the house method — *one functional, many probes*
(`one-representability-functional-two-probes`) — with the probe now ranging over `C` itself, and it
identifies `I` and `0_C` as the two probes that matter.

---

## 6. Theorem D — why the converse cannot be a statement about `C` alone

**Theorem D.** (i) If `I` is connected then `⟦−⟧ : Fam(C^op) → [C,C]` is full and faithful (T1),
hence injective on objects up to isomorphism; so an admissible `C` has `p◁q` determined up to
canonical isomorphism by `⟦p◁q⟧ ≅ ⟦p⟧⟦q⟧`, and "`L_q` has a left adjoint" is a property of `C`.
(ii) If `I` is disconnected this can fail, and does over `Vec_fd`: the objects `({∗},k^2)` and
`(\{1,2\},k)` both present `X ↦ X ⊕ X`, yet they are **not** isomorphic (Lemma 1.3: shape sets of
size `1` and `2`). Hence `p◁q` is not pinned down, `◁` is a **choice**, and left-adjointness is a
property of the choice.

*Proof.* (i) A full and faithful functor reflects isomorphisms and is injective on objects up to
iso: if `⟦x⟧ ≅ ⟦y⟧`, fullness produces `u : x → y` and `v : y → x` with `⟦u⟧,⟦v⟧` the iso and its
inverse, and faithfulness makes `vu = id`, `uv = id`. (ii) `⟦({∗},k^2)⟧X = [k^2,X] ≅ X ⊕ X` and
`⟦(\{1,2\},k)⟧X = [k,X] ⊕ [k,X] ≅ X ⊕ X`. ∎ *(`proved`)*

**The punchline.** Theorem 1 says: *`I` connected ⟹ left adjoint for every `q`.* Theorem D says:
*`I` connected ⟹ the question is about `C` at all.* The hypothesis of Theorem 1 is simultaneously
what makes its converse true (Theorems B, D″) and what makes its converse **meaningful**. Off it,
the honest statement is not "the converse fails" but "there is nothing left to be the converse
**of** until you name a `◁`" — and for the two `◁`'s in actual use (`Set`'s container substitution;
`⊗` on the collapse locus) the answer is respectively yes and no, matching connectedness exactly.

**Consequence for the predecessor's caveat (D).** The predecessor flagged `◁ := ⊗` on the collapse
locus as "a definition, not a deduction" and worried that its Theorem 2 necessity proof (a) was
convention-dependent. Theorem D explains *why* that caveat is unavoidable and cannot be discharged:
over `Vec` no convention-free choice exists. It also shows the predecessor's §5.2(b) (binary
products, finite `T`) is the load-bearing necessity argument — it survives any re-choice of `◁` that
keeps shape sets multiplicative — while §5.2(a) (terminal object) is the convention-sensitive one.

---

## 7. Verification

`scratch/connectedness-converse/verify.py`, five blocks, all green.

1. **B1 — `Set_*`.** Explicit construction of pointed sets, wedges and pointed-map sets:
   `|[3_∗, X∨X]| = (2m+1)^2` confirmed for `m = 0,…,4` (values `1,9,25,49,81`). Exhaustive search
   over all multiplicity vectors `(a_1,…,a_4)` with `a_j ≤ 12`, required to satisfy (∗)
   simultaneously for `m = 0,…,8`: **empty solution set**. The forced values `b = 4`, `a = −4`
   confirmed. Also: `3_∗` is not tiny (`|[3_∗,A∨B]| = 9 ≠ 7 = |[3_∗,A]∨[3_∗,B]|` at `|A|=|B|=2`);
   `S^0` is tiny. **`computed`.**
2. **B2 — `Set×Set`.** `[A, T·1] = (T,1)` for `A = (1,0)`; diagonal (= a copower of `1`) iff
   `|T| = 1`, checked for `|T| ∈ \{1,2,3,5\}`. **`computed`.**
3. **B3 — positive control over `Set`.** `|[P, T×X]| = |∐_{T^P}[P,X]|` for all `P ≤ 3`, `T ≤ 3`,
   `|X| ≤ 3` (30 instances). The decoration set is `T^P`; the identity is distributivity.
   **`computed`.**
4. **B4 — the fatal probe.** At `B = 0_C`: `|∐_t C(0,Y_t)| = |T|` versus `|C(0,∐_t Y_t)| = 1`.
   **`computed`.**
5. **B5 — connectedness of `I`.** `Set` ✓; `Set_∗` ✗ (basepoint identification); `Set×Set` ✗;
   `Vec/𝔽₂` ✗ — **and this one had to be built as a map**: at `dim(V) = dim(W) = 1` the two sides
   both have 4 elements, so a cardinality check would have passed. `γ` is neither injective (zero
   vector counted twice) nor surjective (`e_1+e_2` missed). **`computed`.**
   *This is the second time in two sessions that a cardinality-only check would have hidden the
   phenomenon at the smallest case. Build the map.*

---

## 8. Status ledger

| claim | grade | basis |
|---|---|---|
| Lemma 1.0 (`[0_C,X]` terminal; `[Q,1_C] ≅ 1_C`) | **proved** | §1, closedness |
| **Lemma S** (admissible ⟹ `[P,T·1_C]` a copower of `1_C`) | **proved** | §2 |
| **Theorem A** (`Set_*` is not `◁`-admissible) | **proved** | §3, polynomial degree |
| Corollary A′ (§9bis dichotomy REFUTED) | **proved** | §3 |
| Lemma E1 (extensive: `1 ≅ 1⊔Z ⟹ Z ≅ 0`), E2, E0 | **proved** | §4 |
| **Theorem B** (lextensive ccc + admissible ⟹ `1` connected) | **proved** | §4 |
| Cor B′ (`Set×Set` inadmissible), B″ (Gap 3, extensive pole) | **proved** | §4 + Thm 1 (cited) |
| **Lemma D** (all objects copower-tiny ⟹ `I` disconnected) | **proved** | §5, diagram chase |
| Lemma D′ (zero object ⟹ `I` disconnected) | **proved** | §5 |
| Cor D″ (Gap 3, collapse pole) | **proved** | §5 + Thm 2 (cited) |
| `κ_{B,Z} = γ^B`; the fatal probe is `B = 0_C` | **proved** | §5 |
| **Theorem D** (well-posedness; `Vec_fd` witness) | **proved** | §6 + T1 (cited) |
| the five verification blocks | **computed** | `scratch/connectedness-converse/verify.py` |
| Theorem 1, Theorem 2, T1, T4-left Prop 2.1 | **proved (cited, not re-proved)** | predecessor + my own files |

**REFUTED this session:** the §9bis dichotomy conjecture (`Set_*`, Theorem A).
**CLOSED this session:** Gap 3, on both poles (Corollaries B″ and D″) and as a question
(Theorem D).
**RELOCATED this session:** the `Set×Set` obstruction — from an ad-hoc computation (Prop 9.1) to an
instance of Theorem B, visible at `p = ⟨A⟩` for `A` any nontrivial summand of `1`.

---

## 9. Gaps, precisely stated

1. **The middle region is uncharted, not proved empty.** Theorem B covers infinitary-lextensive
   **cartesian closed** bases; Corollary D″ covers the collapse locus. A separator for the converse
   of Theorem 1 would have to be `◁`-admissible, non-collapse, and closed symmetric monoidal with
   `⊗ ≠ ×` or without infinitary extensivity. **I have no example and no proof that none exists.**
   *Lead:* if `I ≅ I_1 ⊔ I_2` in a closed monoidal `C`, then `X ≅ (X⊗I_1) ⊔ (X⊗I_2)` for every `X`,
   which looks like an idempotent splitting of `C` — if one can show `I_i⊗I_j ≅ 0` for `i ≠ j`, the
   Theorem B argument would run verbatim without cartesianness. Not attempted.
   *Also unaddressed:* bases where `I` is disconnected by **non-injectivity** of `γ` without a zero
   object. `Set_*` is the only one I know, and it is inadmissible.
2. **Is Lemma S sufficient?** Lemma S is necessary for admissibility. Over `Set` and over `Vec` it
   is vacuous and admissibility holds (for the appropriate `q`); over `Set×Set` it fails and
   admissibility fails. **Whether "Lemma S + extensivity ⟹ admissible" is unproved.** The natural
   sufficiency proof needs `[P, ∐_t Y_t] ≅ ∐_{c : P → T·1}∏_t[P^c_t, Y_t]` **internally**, and I
   only verified the external hom-set version.
3. **Gap 1 of the predecessor is untouched:** `◁` on `Fam(Vec^op)` for infinite `T` and
   infinite-dimensional positions. My probe `F(X) = ∏_ℕ(⊕_ℕ X)` versus `∐_d[N_d,X]` was not
   decided by dimension count (both sit at `2^{ℵ_0}` for every finite-dimensional `X`).
4. **Novelty gate.** Theorem 1's general-base form remains ungated (predecessor Gap 2). Theorems A,
   B, D of this file are **also ungated** — the natural places to check are Carboni–Lack–Walters on
   extensive categories (for E1/E2, which may well be folklore — I would not be surprised, and I
   claim no priority for them), and DJN `2305.05655` for whether their indexed formulation dodges
   Theorem B entirely (it plausibly does: with one index set *per component* the obstruction
   evaporates, which would make Theorem B a theorem about **my external-shape** `Fam(C^op)`, not
   about generalized polynomials as such). **Flag this prominently before any claim of novelty.**
5. **`⟦−⟧` injective on objects up to iso.** Theorem D(i) gets this from T1 for connected `I`;
   Theorem D(ii) refutes it over `Vec_fd`. Whether *disconnected ⟹ non-injective* in general is
   unproved, so Theorem D(ii) is a witness, not a theorem about all disconnected bases.

---

## 10. Grant framing

The predecessor classified both adjoints of `L_q = (−)◁q`; this file classifies **where the
question exists**. For the theory section that is a better sentence than either:

> *Substitution of processes is available on a resource base `C` only at two extremes — a
> **set-like** base, where the external shape data is visible inside `C` as a copower of the
> terminal object, and a **linear** base, where it is invisible and the substitution collapses to
> the tensor. On set-like bases, `Fam(C^op)` embeds in `[C,C]`, substitution is canonical, and the
> slot-reindexing left adjoint always exists. On linear bases, none of the three holds, and each
> failure is the same arithmetic fact: `C(I,−)` does not preserve coproducts. In between — pointed
> resources, `Set_*` — substitution does not exist at all.*

For applications (`orchestration-is-zappa-szep-weld`, `applications-are-directed-containers`): a
composition calculus for processes needs its resource base to be set-like *or* linear; a "pointed"
resource model, where every process type has a distinguished trivial inhabitant but resources do
not add, admits **no** substitution operation at all. That is a design constraint on process
algebras with a distinguished `skip`/`fail` element, and it is a genuinely predictive statement —
it says which semantic bases can carry a compositional plug-in calculus before you build one.
