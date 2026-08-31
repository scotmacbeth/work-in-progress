# Linear containers over Vec: the biproduct collapse and the extensivity crux

**MacBeth — 2026-08-18 (PROVE session)**

Fix a field `k`. Write `Vec = Vec_k` for the category of `k`-vector spaces (all of
them, unless finiteness is stated), `[Vec,Vec]` for the category of `k`-linear
(additive) endofunctors and natural transformations, and `Vec(P,W)` for the hom
vector space. All functors below are `Vec`-functors: their action on homs
`Vec(V,W) → Vec(FV,FW)` is `k`-linear.

---

## 0. Definitions

**Definition 0.1 (linear container).** A *linear container* is an object of
`LinCont := Fam(Vec^op)`: a pair `(S,(P_s)_{s∈S})` with `S` a set (the *shapes*)
and each `P_s ∈ Vec` (the *position space* of shape `s`). A morphism
`(S,(P_s)) → (T,(Q_t))` is a pair `(f, (φ_s))` with `f : S → T` a function and,
for each `s∈S`, a linear map `φ_s : Q_{f(s)} → P_s` (contravariant on positions,
exactly as for Set containers). Write `n_s := dim P_s`.

**Definition 0.2 (extension).** The *extension* of `(S,P)` is the functor
`⟦S,P⟧ : Vec → Vec`,

    ⟦S,P⟧ W := ⊕_{s∈S} Vec(P_s, W).

Choosing a basis of `P_s` gives `Vec(P_s,W) ≅ W^{n_s}` (natural in `W`), so
`⟦S,P⟧ W ≅ ⊕_{s∈S} W^{⊕ n_s}`, a "direct sum of powers". On morphisms
`(f,(φ_s))` the natural transformation is `(g_s)_s ↦ (g_{f(s)}∘φ_s)_s` in the
evident way; `⟦−⟧ : Fam(Vec^op) → [Vec,Vec]` is a functor.

Write `h_P := Vec(P,-)` for the *corepresentable* at `P`. Then
`⟦S,P⟧ = ⊕_{s∈S} h_{P_s}`, and `h_k = Vec(k,-) ≅ Id`.

The whole paper studies the single functor `⟦−⟧` and asks how much of the Set
container theory (`Cont ≅ Fam(Set^op) ↪ [Set,Set]`) survives the base change
`Set ↝ Vec`. The one-line answer: **the coproduct/product distinction that makes
Set containers rigid becomes a biproduct, and everything that the Set theory reads
off "for free" collapses.**

---

## 1. Three lemmas

**Lemma 1.1 (co-Yoneda, linear form).** For any `Vec`-functor `G : Vec → Vec` and
any `P ∈ Vec` there is an isomorphism of vector spaces
`Nat(h_P, G) ≅ G(P)`, natural in `G` and `P`. In particular
`Nat(Id, G) ≅ G(k)` and `Nat(h_P, h_Q) ≅ Vec(Q,P)`.

*Proof.* Given `α : h_P ⇒ G`, set `ξ := α_P(id_P) ∈ G(P)`. For any `φ : P → W`,
naturality of `α` along the postcomposition map `φ_* : Vec(P,P) → Vec(P,W)` gives
`α_W(φ) = α_W(φ_* id_P) = G(φ)(α_P id_P) = G(φ)(ξ)`. So `α` is determined by
`ξ`. Conversely, for any `ξ ∈ G(P)` define `α_W(φ) := G(φ)(ξ)`; this is linear in
`φ` because `G` is a `Vec`-functor (so `φ ↦ G(φ)` is linear) followed by
evaluation at `ξ`, and it is natural in `W` by functoriality of `G`. The two
constructions are mutually inverse and `k`-linear in `ξ`, so
`Nat(h_P,G) ≅ G(P)`. For `G = h_Q`, `G(P) = Vec(Q,P)`. ∎

**Lemma 1.2 (`h` is additive and fully faithful; a unique indecomposable).**
The assignment `h : Vec^op → [Vec,Vec]`, `P ↦ h_P`, is fully faithful and sends
finite biproducts to biproducts: `h_{P⊕Q} ≅ h_P ⊕ h_Q`. Consequently the only
indecomposable corepresentable is `h_k ≅ Id`, and `End(Id) = k`.

*Proof.* Full faithfulness is Lemma 1.1 with `G = h_Q`: `Nat(h_P,h_Q) ≅ Vec(Q,P)
= Vec^op(P,Q)`. Additivity: `h_{P⊕Q}(W) = Vec(P⊕Q,W) ≅ Vec(P,W) × Vec(Q,W) =
(h_P ⊕ h_Q)(W)`, using that a finite product in `Vec` is a biproduct and that
biproducts in `[Vec,Vec]` are computed pointwise; naturality is clear. Since every
`P` with `dim P ≥ 2` splits as `k ⊕ (·)` and `h` is additive, `h_P` decomposes
unless `dim P = 1`; and `h_0 = 0`. So the unique indecomposable corepresentable is
`h_k`. Finally `End(Id) = Nat(Id,Id) ≅ Id(k) = k` by Lemma 1.1. ∎

**Lemma 1.3 (finite positions distribute over `⊕`).** If `dim P < ∞` then for any
family `(V_t)_{t∈T}`, `Vec(P, ⊕_t V_t) ≅ ⊕_t Vec(P, V_t)`, naturally.
Equivalently, `h_P` preserves coproducts iff `P` is finite-dimensional.

*Proof.* Let `e_1,…,e_n` be a basis of `P`. A linear map `φ : P → ⊕_t V_t` is
determined by the finite tuple `(φ(e_1),…,φ(e_n))`, and each `φ(e_i)` has finite
support in `T`; hence `im φ` lies in a finite subsum `⊕_{t∈F} V_t`. Therefore `φ`
lies in `⊕_t Vec(P,V_t)` (the finitely-supported families), giving the inclusion
`⊇`; the reverse inclusion is immediate. For `P` infinite-dimensional the identity
`P → P = ⊕_{i∈I} k` has infinite support, so it lies in `∏_i k` but not
`⊕_i k`, and the isomorphism fails. ∎

---

## 2. Part 1 — the biproduct collapse

### 2(a). Terminal recovery fails; the replacement

The terminal object of `Vec` is the zero object `0` (terminal = initial). Hence

    ⟦S,P⟧(0) = ⊕_{s∈S} Vec(P_s, 0) = ⊕_s 0 = 0.

**The Set slogan `F(1) = S` has no analog: the shapes are invisible at the
terminal object.** The natural replacement — evaluation at the monoidal unit `k` —
gives `⟦S,P⟧(k) = ⊕_s Vec(P_s,k) = ⊕_s P_s^*`, a single vector space of dimension
`Σ_s n_s`. This records only the *total* position dimension, and even then only as
a bare vector space: no partition into shapes.

The honest replacement for "shapes = points of `F(1)`" is *homological*, not
evaluative:

> **Shapes over `Vec` = indecomposable direct summands of the functor `F`** — and
> Theorem 2.1 shows how badly that differs from the naive shape set.

### 2(b). Finite collapse

**Theorem 2.1 (finite collapse).** Let `S` be finite and every `n_s = dim P_s`
finite, and set `N := Σ_{s∈S} n_s = dim(⊕_{s∈S} P_s)`. Then there is a natural
isomorphism `⟦S,P⟧ ≅ Id^N`. Consequently:

1. `⟦S,P⟧ ≅ ⟦S',P'⟧` as functors **iff** `N = N'`. A finite linear container is
   classified up to isomorphism of its extension by the single number `N`.
2. `Id` is indecomposable with `End(Id) = k` (Lemma 1.2), and `End(Id^N) = M_N(k)`
   is semiperfect, so by the Krull–Schmidt–Azumaya theorem the decomposition
   `⟦S,P⟧ ≅ Id^{⊕N}` into indecomposables is unique up to isomorphism and
   permutation. The recovered invariant is exactly the multiplicity `N`; the
   shape set `S` and the partition `N = Σ_s n_s` are not recoverable.

*Proof.* By Lemma 1.3 with each `V` a single copy — more directly, choosing a
basis of each `P_s`, `Vec(P_s,W) ≅ W^{n_s}` naturally in `W`. Since `S` is finite,
`⟦S,P⟧ W = ⊕_{s∈S} Vec(P_s,W) ≅ ⊕_{s∈S} W^{n_s} = W^{⊕ Σ_s n_s} = Id^N(W)`,
naturally in `W`. This proves the isomorphism; (1) is immediate since `Id^N ≅
Id^{N'}` iff `N=N'` (evaluate at `k`). For (2), `Id` is indecomposable because
`End(Id) = k` has no idempotents `≠ 0,1`; `[Vec,Vec]` is additive and
idempotent-complete (idempotents split pointwise), and `End(Id^N) = M_N(k)` is
Artinian hence semiperfect, so Krull–Schmidt–Azumaya applies. ∎

**Example.** `({∗}, k^2)` and `({∗_1,∗_2}, (k,k))` are non-isomorphic in
`Fam(Vec^op)` (different shape sets) yet both have extension `Id^2`, `W ↦ W^2`.
Over `Set` the analogous containers `({∗}, 2)` and `({∗_1,∗_2},(1,1))` have
*distinct* extensions `X^2` and `2·X`, separated at `X = 1`. The collapse is
precisely the failure of that separation.

### 2(c). Where content survives

The collapse of Theorem 2.1 used **both** finiteness of `S` (to turn `⊕` into a
finite biproduct) **and** finite-dimensionality of the positions (Lemma 1.3). Drop
either and content returns:

- **Infinite `S`.** With all `P_s = k`, `⟦S,P⟧ = ⊕_{s∈S} Id = Id^{⊕|S|}`. This is
  *not* representable and `⊕_{s} Id ≠ ∏_s Id` (a coproduct of `|S|` copies of `Id`
  differs from the product for infinite `S`): the functor is genuinely new. Still,
  Krull–Schmidt–Azumaya recovers only the cardinal `|S|` (the number of `Id`
  summands), not any further shape structure.
- **Infinite-dimensional positions.** By Lemma 1.3, `h_P` for `dim P = ∞` does not
  preserve coproducts: `h_P(W) = Vec(P,W) ≅ ∏_{i∈I} W` is an *infinite product*
  functor, not a coproduct of copies of `Id`. Such `h_P` are not built from `Id`
  under `⊕`, and by Lemma 1.2 (`h` fully faithful) distinct infinite-dimensional
  `P` give non-isomorphic `h_P`. Here `P` **is** recovered from a single
  representable.
- **The morphism layer.** Even where objects collapse, the *category*
  `Fam(Vec^op)` and the natural-transformation spaces between extensions do not —
  this is Part 2, and it is where the extensivity crux lives.

---

## 3. Part 2 — the representation theorem and the extensivity crux

The Set representation theorem states that `⟦−⟧ : Fam(Set^op) → [Set,Set]` is
fully faithful, with essential image the polynomial functors, and the data `(S,P)`
recovered from `F` as `S = π₀(el F)` with positions the generic elements
(Diers/familial representability). We show precisely which half survives over
`Vec` and locate the failure in **one symbol**.

**Theorem 3.1 (hom formula).** For linear containers `(S,P)`, `(T,Q)`,

    Nat(⟦S,P⟧, ⟦T,Q⟧) ≅ ∏_{s∈S} ⊕_{t∈T} Vec(Q_t, P_s).

*Proof.* `⟦S,P⟧ = ⊕_s h_{P_s}` is a coproduct, so
`Nat(⊕_s h_{P_s}, G) ≅ ∏_s Nat(h_{P_s}, G) ≅ ∏_s G(P_s)` by Lemma 1.1. With
`G = ⟦T,Q⟧`, `G(P_s) = ⊕_t Vec(Q_t, P_s)`. ∎

**Theorem 3.2 (container-hom).** The morphisms of `Fam(Vec^op)` are

    Fam(Vec^op)((S,P),(T,Q)) ≅ ∏_{s∈S} ( ∐_{t∈T} Vec(Q_t, P_s) ),

where `∐` is the coproduct in `Set` (disjoint union): a morphism assigns to each
`s` a choice of `t = f(s)` together with a linear map in `Vec(Q_{f(s)}, P_s)`.

*Proof.* Immediate from Definition 0.1: a morphism is `f : S → T` plus, for each
`s`, an element `φ_s ∈ Vec(Q_{f(s)}, P_s)`; packaging `(f(s), φ_s)` as an element
of the disjoint union `∐_t Vec(Q_t,P_s)` and ranging over `s` gives the product. ∎

**Theorem 3.3 (the extension is faithful-on-nonzero but not full; the crux).**
The functor `⟦−⟧` induces, on each hom, the canonical map

    ∏_s ∐_t Vec(Q_t, P_s)  ⟶  ∏_s ⊕_t Vec(Q_t, P_s),

componentwise the inclusion of the disjoint union `∐_t` into the biproduct `⊕_t`
sending a choice `(t, φ)` to the element supported at `t`. Therefore:

1. **Not full.** As soon as some shape `s∈S` admits two shapes `t≠t'∈T` with
   `Vec(Q_t,P_s) ≠ 0 ≠ Vec(Q_{t'},P_s)`, there are natural transformations
   `⟦S,P⟧ ⇒ ⟦T,Q⟧` not in the image of `⟦−⟧` — namely any whose `s`-component is a
   genuine linear combination `φ_t + φ_{t'}` supported on two shapes. The cokernel
   of the inclusion measures exactly the cross-shape linear combinations that the
   biproduct permits and a shape-function `f` forbids.
2. **Extensivity is the whole story.** Over `Set` the same computation gives
   `Nat(⟦S,P⟧,⟦T,Q⟧) ≅ ∏_s ⊕_t Set(Q_t,P_s)` where now `⊕_t = Σ_t` is the
   coproduct in `Set` — i.e. the disjoint union `∐_t`. Hence `Set`-container-hom
   `= Nat` and `⟦−⟧` is fully faithful (the classical representation theorem). The
   only thing that changes under `Set ↝ Vec` is that the coproduct in the hom
   formula splits into two inequivalent notions: `∐_t` (container morphisms, one
   shape per `s`) `⊊` `⊕_t` (natural transformations, linear combinations across
   shapes). **`Set` is extensive — its coproduct is the disjoint union — and that
   is exactly what makes `⟦−⟧` full; `Vec` is not extensive — its coproduct is a
   biproduct — and the fullness gap `∐ ⊊ ⊕` is the precise, quantified
   manifestation of that failure.**

*Proof.* The description of the induced map on homs is the naturality of the
`⟦−⟧`-action against Theorems 3.1–3.2: a container morphism `(f,(φ_s))` produces
the natural transformation whose `s`-component is the composite through the single
summand `t = f(s)`, i.e. the element of `⊕_t Vec(Q_t,P_s)` supported at `f(s)`.
The map `∐_t X_t → ⊕_t X_t` (choice ↦ supported element) is injective away from
zero and misses every element with support of size `≥ 2`; taking `X_t =
Vec(Q_t,P_s) ≠ 0` for two values of `t` exhibits a missed element, proving (1).
For (2): in `Set`, `Nat(⟦S,P⟧,⟦T,Q⟧) ≅ ∏_s ⟦T,Q⟧(P_s) = ∏_s Σ_t Set(Q_t,P_s)`,
and `Σ_t = ∐_t`, so this equals `Fam(Set^op)((S,P),(T,Q))`; the induced map is the
identity and `⟦−⟧` is fully faithful. The lone difference over `Vec` is
`⊕_t ≠ ∐_t`. ∎

**Corollary 3.4 (finite recovery, sharp).** Restrict to finite containers with
finite-dimensional positions. Then `⟦−⟧` recovers from `⟦S,P⟧`:

- the total position space `⊕_{s∈S} P_s ∈ Vec` up to isomorphism (equivalently the
  number `N`), by Theorem 2.1 and Lemma 1.2 — `⊕_s h_{P_s} ≅ h_{⊕_s P_s}` and `h`
  is fully faithful, so the extension determines `⊕_s P_s` exactly;
- **nothing** about the partition of `N` into shapes.

Thus over `Vec` the honest representation theorem is:
`F` is a *finite* linear container `⟺` `F ≅ Id^N` `⟺` `F` is `Vec`-cocontinuous
with `F(k)` finite-dimensional (`F ≅ F(k)⊗-` by Eilenberg–Watts, and finite
dimension forces `Id^N`); and the data `(S,P)` is recovered *only up to the
biproduct ambiguity* — a single object `⊕_s P_s` with no canonical shape
decomposition. This is the negative-with-a-remedy the extensivity crux predicts.

**Remark 3.5 (contrast with strict polynomial functors).** The objects `⊕_s
h_{P_s}` are the additive (degree-1) corner of the strict polynomial functors of
Friedlander–Suslin (`P_1 ≃ Vec`, corepresentables `Vec(P,-) ≅ (-)^{dim P}`). That
theory never indexes a *shape set* over its additive part — precisely because, as
Theorem 3.3 shows, the shape set is not an invariant of the functor. The
container/`Fam(Vec^op)` framing is what *introduces* the shape index, and the
biproduct collapse is the price of doing so over a non-extensive base.

---

## 4. Part 3 — composition `◁` (computed; a further collapse)

**Proposition 4.1 (composition of linear containers, finite-dim positions).**
For linear containers with finite-dimensional positions,

    ⟦S,P⟧ ◁ ⟦T,Q⟧ := ⟦S,P⟧ ∘ ⟦T,Q⟧ ≅ ⟦ S×T, (P_s ⊗ Q_t)_{(s,t)} ⟧.

Thus on `Fam(Vec^op)` (finite-dim positions) composition is
`(S,P) ◁ (T,Q) = (S×T, (P_s⊗Q_t))`, with unit `I = ({∗}, k)` (extension `Id`).

*Proof.* `⟦S,P⟧(⟦T,Q⟧ W) = ⊕_s Vec(P_s, ⊕_t Vec(Q_t,W))`. Since `P_s` is
finite-dimensional, Lemma 1.3 gives `Vec(P_s, ⊕_t Vec(Q_t,W)) ≅ ⊕_t Vec(P_s,
Vec(Q_t,W))`, and the tensor–hom adjunction (with `P_s` finite-dimensional)
gives `Vec(P_s, Vec(Q_t,W)) ≅ Vec(P_s⊗Q_t, W)`. Summing, `≅ ⊕_{(s,t)}
Vec(P_s⊗Q_t, W)`. The unit: `({∗},k)◁(T,Q) = ({∗}×T, k⊗Q_t) = (T,Q)`. ∎

**A genuine structural difference.** This is *not* the Set container composition,
whose shapes are the dependent sum `∐_{s∈S} T^{P_s}`. The reason is exactly Lemma
1.3: a linear map `P_s → ⊕_t V_t` is a *sum of components*, not a *choice of
branch*, so the dependency `T^{P_s}` disappears. Linearity flattens the dependent
sum into a plain product of shapes with tensored positions.

**Proposition 4.2 (◁-comonoids collapse to families of algebras).** A `◁`-comonoid
`((S,P), δ, ε)` in `(Fam(Vec^op)_{fin}, ◁, I)` is equivalent to: the shape set `S`
(with its unique `(Set,×)`-comonoid structure, the diagonal) together with, for
each `s∈S`, a `k`-algebra structure on `P_s`. In particular a one-shape
`◁`-comonoid `({∗},P)` is exactly a `k`-algebra `P` (Mitchell's one-object case).

*Proof (sketch — banked as `computed`).* The comultiplication `δ : (S,P) →
(S,P)◁(S,P) = (S×S, (P_a⊗P_b))` has shape component a function `S → S×S`; the
counit `ε : (S,P) → I=({∗},k)` has shape component `S → {∗}`. Coassociativity and
counitality of the shape components make `S` a comonoid in `(Set,×)`, which forces
the diagonal `s ↦ (s,s)` (every set is uniquely such a comonoid). With `a=b=id`,
the position component of `δ` is a family `φ_s : P_s⊗P_s → P_s`, and of `ε` a
family `η_s : k → P_s`; coassociativity/counitality of `δ` become associativity
and the unit laws for `(φ_s, η_s)`, i.e. a `k`-algebra on each `P_s`. Distinct
shapes never interact (the diagonal cannot reach off-diagonal shape pairs). ∎

**The crown target, honestly assessed.** The Set spine is `poly-comonoid ≅ small
category`; one hoped `◁`-comonoid over `Vec` `≅` `k`-linear category (algebroid,
Mitchell). Proposition 4.2 shows the finite-dimensional analog is **weaker**: a
`◁`-comonoid yields only a *family of `k`-algebras* — a "diagonal" algebroid with
no morphisms between distinct objects — because the linear composition `◁` of
Prop 4.1 has lost the dependent-sum structure that, over `Set`, lets a comonoid
encode composable arrows between different objects. **The biproduct/linearity
collapse strikes a third time**, now degrading algebroids to algebra-families. A
full algebroid requires a genuinely different (lax/bimodule) composition; pinning
that down is Further Work.

---

## 5. Verification

Computational checks in `scratch/vec-containers/verify.py` (all pass):

- **Finite collapse** (Thm 2.1): `dim ⟦{a,b},(k²,k)⟧(k^d) = 3d = dim (k^d)^3`
  for `d = 0..4`.
- **Hom formula & non-fullness** (Thm 3.1–3.3): `Nat(Id²,Id²)` has dimension `4 =
  Σ_s Σ_t dim Vec(k,k)`; the natural transformation `[[1,1],[0,0]]` (whose first
  component mixes two shapes) is *not* realizable as a container morphism
  `({1,2},(k,k)) → ({1,2},(k,k))` — confirmed by exhausting monomial matrices.
- **Lemma 1.3**: `dim Vec(k², ⊕_{|T|} k) = 2|T| = dim ⊕_{|T|} Vec(k²,k)` for
  `|T| = 1..4`.
- **Composition** (Prop 4.1): `dim` of `(S,P)◁(T,Q)` total position `= N·M`.

Boundary cases: `S = ∅` gives `⟦∅,−⟧ = 0` (the zero functor), consistent with
`N=0`, `Id^0 = 0`. `P_s = 0` contributes a zero summand, consistent.

---

## 6. Status of the three parts

- **PART 1 — biproduct collapse: PROVED.** Theorem 2.1 (finite collapse, with
  Krull–Schmidt uniqueness), §2(a) (terminal recovery fails; replacement stated),
  §2(c) (survival regimes). This is the primary deliverable.
- **PART 2 — representation / extensivity crux: PROVED (as a negative-with-remedy).**
  Theorems 3.1–3.3 and Corollary 3.4 give the hom formula, the precise failure of
  fullness, its identification with the failure of extensivity (`∐ ⊊ ⊕`), and the
  sharp finite recovery statement. The general infinite/infinite-dimensional
  characterization (which `F : Vec→Vec` are arbitrary small coproducts of
  corepresentables) is stated but not fully characterized — **Further Work**.
- **PART 3 — comonoid probe: COMPUTED.** Proposition 4.1 (`◁ = (S×T, P⊗Q)`),
  Proposition 4.2 (`◁`-comonoid = family of `k`-algebras; one shape = a
  `k`-algebra), and the honest finding that the algebroid guess fails in the
  finite-dimensional case. Banked as `computed`, not `proved` (Prop 4.2 is a
  sketch pending a full comonoid-law verification).

## 7. Gaps (precisely stated)

1. **General representation theorem (Part 2(ii)).** For arbitrary (infinite `S`,
   infinite-dim `P_s`) linear containers, characterize the essential image of
   `⟦−⟧` in `[Vec,Vec]` intrinsically (candidate: accessible functors preserving
   connected limits that are small coproducts of corepresentables) and describe
   the recovery of `(S,P)` up to biproduct ambiguity via a Krull–Schmidt /
   generic-factorization statement in `[Vec,Vec]`. Diers' extensivity hypothesis
   is exactly what obstructs a clean equivalence; the coordinate-free invariant is
   open beyond the finite case.
2. **Full comonoid-law check (Prop 4.2).** Verify coassociativity/counitality in
   full (currently a sketch), and settle whether a modified composition on
   `Fam(Vec^op)` (bimodule/lax) recovers genuine algebroids — the true `Vec`
   analog of `DCont ≅ Cat`.
3. **Tensor–hom step in Prop 4.1** uses `P_s` finite-dimensional; the
   infinite-dimensional composition is not addressed.

## Novelty caveat (recorded per PROVE.md)

Strict polynomial functors (Friedlander–Suslin, Invent. Math. 127 (1997);
Krause arXiv:1203.0311) own the *objects* — additive endofunctors of `Vec` are
their degree-1 corner. Vector species / TCAs (Sam–Snowden arXiv:1209.5122) own the
Day/analytic `⊗`-story. Diers' familial representability (nLab *multirepresentable
functor*; Carboni–Johnstone 1995) owns "coproduct of representables" and carries
the extensivity hypothesis. Mitchell (*Rings with several objects*, Adv. Math. 8,
1972) owns "algebroid". **The claimed delta is the assembly**: the
`Fam(Vec^op)`-container framing, the shape-index it introduces, and — the load
bearing contribution — the identification of the shape-collapse (objects) and the
fullness gap (morphisms) as one phenomenon, namely the failure of extensivity
`∐ ⊊ ⊕` under the base change `Set ↝ Vec`.
