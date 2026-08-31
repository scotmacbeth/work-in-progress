# Fibredness of `◁` in its left variable versus `◁`-left-closure

### — BHM's parenthetical, proved; and separated from the T4-left obstruction

**MacBeth — 2026-08-30 (PROVE session).** Answers sub-Q2 of
`memory/questions/workers-grading-vs-bhm-polynomial-grading.md`: *is Braithwaite–Hedges–Mihejevs'
claim "the composition product `▷` is not fibred in its left variable" the same obstruction as my
proved T4-left failure of `◁`-left-closure?*

Companion code `scratch/fibredness-vs-closure/verify.py` (all green).
Registry `proofs/registry/fibredness-vs-left-closure.json`.

---

## 0. Headline

**NO. They are two different conditions that happen to coincide over `Set`.**

Sharpened: for a fixed container `q=(T,Q)` consider the endofunctor `L_q := (−)◁q` on
`Fam(C^op)` and the **shape fibration** `π : Fam(C^op) → Set`, `π(S,P)=S`. Three conditions:

| | | |
|---|---|---|
| **(V)** | `L_q` is **vertical** | `π L_q ≅ π`, cartesian maps preserved |
| **(F)** | `L_q` is **fibred** | `π L_q ≅ F_0 π` for some `F_0:Set→Set`, cartesian maps preserved |
| **(C)** | `L_q` is **left-closed** | `L_q` has a right adjoint (the `◁`-left-closure) |

> **Theorem A (over `Set`).** `(V) ⟺ (F) ⟺ (C) ⟺ |T|=1` (`q` a monomial `y^Q`).
>
> **Theorem B (over `Vec_fd`).** `(V) ⟺ |T|=1`; `(C) ⟺ #{t : Q_t ≠ 0}` is finite;
> `(F)` holds **always**. Hence
> ```
>              (V)  ⊊  (C)  ⊊  (F)          strictly, witnesses |T|=2 and |T|=ℕ.
> ```

So the answer to sub-Q2 is **no** under *either* reading of "fibred" (vertical or fibred-over-a-base-
functor), and the separation is two-sided: over `Vec_fd` there are `q` that are closed but not
vertical (`|T|=2`) and `q` that are fibred but not closed (`|T|=ℕ`). The `Set` coincidence of
Theorem A is an artefact of `Set` having exactly one collapse mechanism.

**Diagnosis (§5).** Both conditions are instances of *one* test — "is
`G_r(Z) := Fam(⟨Z⟩◁q, r)` familially representable?" — evaluated at **different probing objects**
`r`. At the **shape probe** `r=(R, 0)` (all positions initial) the test sees only the shape object
`π(⟨Z⟩◁q)` and becomes exactly fibredness. At the **position probe** `r=⟨I⟩` it sees only whether
the forced position object exists in the base (summability). Over `Set` the shape probe is the
binding one and it *forces* `|T|=1`, after which summability is automatic. Over `Vec_fd` the shape
probe is vacuous (tininess has already collapsed the shape object to `S×T`) and the position probe
becomes binding. **Fibredness = collapse. Closure = collapse *and* summability.**

**The real content of BHM's clause (§2) — prior art, accounted for in §8.** `◁` **is** fibred in its
*right* variable, for every `q`, with base functor literally the polynomial functor `⟦q⟧` itself:
`π(q◁p) = Σ_{t∈T} (π p)^{Q_t} = ⟦q⟧(π p)`. **This is not mine: it is Pradic–Price, Lemma 15**
(`2601.15420`, p. 14, proof p. 31), with the same base functor. And in **both** variables `◁`
preserves cartesian morphisms unconditionally — **also not mine over `Set`**: that is Niu–Spivak
`2312.00990`, Proposition 6.88 (p. 213), which Pradic–Price invoke by name at p. 31. So the failure
BHM point at is purely a failure of **base-functoriality**, never of cartesianness — which is what
makes it a failure with no repair by a comparison map. *That isolation of the two halves is what is
left as mine here; PP's Remark 16 (p. 14) is bare. Full accounting in §8.*

---

## 1. Setup

### 1.1 The category and the fibration

Let `(C,⊗,I,[-,-])` be a closed symmetric monoidal cocomplete category. `Fam(C^op)` has objects
`p=(S,P)` — a set `S` and a family `(P_s)_{s∈S}` of objects of `C` — and

> `Fam(C^op)\big((S,P),(S',P')\big) \;=\; ∏_{s∈S} ∐_{s'∈S'} C(P'_{s'},\,P_s).`

Concretely a morphism is a **forward** map `f:S→S'` on shapes together with **backward** maps
`f^♯_s : P'_{f s} → P_s` in `C`. For `C=Set` this is `Cont(Set) = Poly`. Write `⟨Z⟩ := ({∗},Z)`
(over `Set`: the representable `y^Z`) and `y := ⟨I⟩` for the unit.

**Definition 1.1 (shape fibration).** `π : Fam(C^op) → Set`, `π(S,P)=S`, `π(f,f^♯)=f`.

**Lemma 1.2.** `π` is a (split, cloven) fibration — it is the family fibration of `C^op`. The
cartesian lift of `f:S→S'` at `(S',P')` is `(f, \mathrm{id}) : (S, P'∘f) → (S',P')`, and a morphism
`(f,f^♯)` is `π`-cartesian **iff every component `f^♯_s` is an isomorphism**.

*Proof.* `Fam(D) → Set` is the family fibration for any `D`; here `D=C^op`, and an isomorphism in
`C^op` is an isomorphism in `C`. Given `(g,g^♯):(S'',P'')→(S',P')` and `h:S''→S` with `f h=g`, the
unique factorisation through `(f,\mathrm{id})` is `(h, g^♯)`, which typechecks because
`P'∘f∘h = P'∘g`. Conversely if some `f^♯_s` is not iso the factorisation of the cartesian lift
through `(f,f^♯)` fails at `s`. ∎

**Definition 1.3 (fibred, vertical — stated as mine).** Let `π:E→B` be a fibration. A **fibred
endofunctor** on `π` is a pair `(F,F_0)`, `F:E→E`, `F_0:B→B`, together with a natural isomorphism
`π F ≅ F_0 π`, such that `F` carries `π`-cartesian morphisms to `π`-cartesian morphisms. It is
**vertical** if moreover `F_0 = \mathrm{Id}` (so `π F ≅ π`).

> **Attribution note (updated 2026-08-30 — the paper is now on disk and read; see §8).** BHM cite
> [PP26] = Pradic–Price `2601.15420` (*Problems with Fixpoints of Polynomials of Polynomials*,
> v2 [cs.LO] 11 May 2026, LICS 2026) for the notion of fibred endofunctor used for fixpoints. That
> paper is now at `papers/pradic-price_2601.15420_fixpoints-poly-of-poly.pdf` (+ `.txt`); verbatim
> extraction in `scratch/2026-08-30-pradic-price-fibred-def.md`. Both previously-open sub-questions
> are answered.
> **(a) Their fibration is Definition 1.1.** §2.2, pp. 8–9: *"`shape` extends to a functor
> `Cont(C) → C` by considering the map `(φ,ψ) ↦ φ` on morphisms. In fact, `shape` is a Grothendieck
> fibration, and it is straightforward to check that it is **exactly the fibrewise opposite of the
> codomain fibration** `cod : C^→ → C` … So given a morphism `P → Q` in `Cont(C)` given by `(φ,ψ)`,
> we will call it **cartesian** or horizontal if `ψ` is an isomorphism and **vertical** if `φ = id`."*
> Over `C = Set` that **is** `π(S,P)=S`, and their cartesian/vertical are Lemma 1.2. (My own
> `Cont(C) = ∫_{Set}(\mathrm{cod})^{op}`, `contravariance-is-fibrewise-op`, von Glehn TAC 33.)
> **(b) Their fibredness is the `(F,F_0)` form, and strict.** Definition 13 clause 1, §3.1, p. 14:
> *"`(F, F_0)` is a fibred functor `shape^k → shape` for some **uniquely determined**
> `F_0 : C^k → C` (see [60, Definition 2.2])"* — Streicher's cartesian/fibred functor, i.e.
> `shape ∘ F = F_0 ∘ shape^k` **on the nose** plus preservation of cartesians, where Definition 1.3
> below asks only for a natural isomorphism. So **PP-fibred ⟹ (F)**: Definition 1.3 is the weaker
> notion, and every *negative* result below therefore holds *a fortiori* for theirs. Their *fibred
> polynomial* adds two polynomiality clauses (Def 13.2, 13.3) that I do not impose; those are
> orthogonal extra structure, not a different fibredness. Neither of us takes the vertical form as
> *the* definition — `(V)` is my own extra rung.
> (Citation glitch, minor, and mine to note rather than theirs: `[60]` is Streicher, *Fibered
> categories à la Jean Bénabou*, `arXiv:1801.02927`, and in its v20 (13 Sep 2023) **Definition 2.2
> is the definition of a fibration**; the fibred/cartesian **functor** is Definition 2.3. PP's
> "[60, Definition 2.2]" is off by one against that version, or matches a different numbering. The
> intent is unambiguous and nothing below depends on it.)
> Definition 1.3 is therefore still stated as **mine** (it is the up-to-iso variant), everything
> below is proved relative to it, and I prove **both** forms so that no conclusion depends on which
> is meant. **Prior art, scope, and what all this costs and buys the results below: §8.**
> *(This corrects `state/PROVE.md`, which described the fibration reading as an "agent-summary":
> the entry is a deep-read, but of a different question. Recorded in `sources.json`.)* I prove both the `F_0`-general and the `F_0=\mathrm{Id}`
> versions precisely so the conclusion does not depend on which they meant. BHM's own statement is
> a **single unproved parenthetical clause** in a 2-page extended abstract
> (`papers/BHM-polylang-ACT2026.pdf`, §3 Fixpoints, no definition, no proof); it is cited here as
> **corroboration of the phenomenon, never as a lemma**.

### 1.2 The two products, and `◁` over a general base

Over `Set`, with `p=(S,P)`, `q=(T,Q)`:

> **(SUB)** `p ◁ q \;=\; \big(\;Σ_{s∈S} T^{P_s}\;,\;\; (s,τ) ↦ Σ_{d∈P_s} Q_{τ(d)}\;\big)`,
> **(DIR)** `p ⊗ q \;=\; \big(\;S×T\;,\;\;(s,t) ↦ P_s × Q_t\;\big)`,

`⟦p◁q⟧ = ⟦p⟧∘⟦q⟧` where `⟦S,P⟧X = Σ_s X^{P_s}` (over a general `C`: `⟦S,P⟧X = ∐_s [P_s,X]`).
Over a general `C`, `⊗` is Day convolution and is given by the same formula (DIR) with `×` replaced
by `⊗`. Both are functorial in each variable and **preserve coproducts in each variable**
(coproducts in `Fam(C^op)` are disjoint unions of shape sets).

**On `Vec_fd`.** An object `Z∈C` is **tiny** if `[Z,−]` preserves small coproducts; in a closed
symmetric monoidal category every dualizable object is tiny (`[Z,−] ≅ Z^{*}⊗(−)` is a left
adjoint), and in `Vec` tiny = dualizable = finite-dimensional.

**Proposition 1.4 (collapse).** If every `P_s` is tiny then `⟦p⟧∘⟦q⟧ ≅ ⟦p⊗q⟧`:
```
   ∐_s [P_s, ∐_t [Q_t,X]]  ≅  ∐_s ∐_t [P_s,[Q_t,X]]   (P_s tiny)
                           ≅  ∐_{(s,t)} [P_s⊗Q_t, X]   (tensor–hom)  =  ⟦p⊗q⟧X.
```
Accordingly **on `Fam(Vec_fd^op)` I take (DIR) as the definition of `◁`**: `p◁q := p⊗q =
(S×T, P_s⊗Q_t)`. This is my proved Prop 4.1 of `2026-08-18-linear-containers-vec.md`.

> *Honesty note.* `⟦−⟧` is **not** full over `Vec` (my T1: fullness ⟺ the monoidal unit is
> connected, which fails for `Vec` because `∐ ⊊ ⊕`), so "the object whose extension is the
> composite" is not determined up to isomorphism by Proposition 1.4 alone. I therefore *define*
> `◁ := ⊗` on the tiny locus rather than deducing it. Theorem B may equivalently be read as a
> theorem about `(−)⊗q` on `Fam(Vec_fd^op)`, which is what its proof actually uses.

---

## 2. Cartesianness is free; `◁` is fibred on the right

**Lemma 2.1 (cartesian preservation is unconditional — the `Set` half is prior art: Niu–Spivak
Prop. 6.88).** For every `q`, both `(−)◁q` and `q◁(−)`
carry `π`-cartesian morphisms to `π`-cartesian morphisms — over `Set` and over any base on which
the relevant product is defined.

> **Prior art (added 2026-08-30).** Over `Set` (`Fam(Set^op) = Poly`) this is **Niu–Spivak
> `2312.00990`, Proposition 6.88, p. 213** — *"if `φ : p → p'` and `ψ : q → q'` are cartesian, so is
> `φ ◁ ψ`"* — which Pradic–Price invoke by name in the proof of their Lemma 15 (p. 31: *"That the
> functor is fibred follows since if `ϕ:P→P'`, `ψ:Q→Q'` are cartesian, then so is `ψ⋆ϕ` [50,
> Proposition 6.88]"*, `[50]` = Niu–Spivak). The `Set` half of Lemma 2.1 is therefore **not mine**;
> what is proved fresh here is the `Fam(C^op)` half with `◁ = ⊗` (last paragraph of the proof), and
> the *use* made of it in §8.2. See §8.

*Proof.* Over `Set`, let `φ=(f,φ^♯):(S,P)→(S',P')` be cartesian, so each `φ^♯_s : P'_{fs} → P_s`
is a bijection (Lemma 1.2).

*Left variable.* `φ◁q` acts on shapes by `(s,τ) ↦ (f s,\ τ∘φ^♯_s)` — this is the shape part of
the whiskering `⟦φ⟧⟦q⟧`, since `⟦φ⟧(s,g)=(fs,\ g∘φ^♯_s)` — and on positions by reindexing along
`φ^♯_s`:
`Σ_{d'∈P'_{fs}} Q_{τ φ^♯_s(d')} → Σ_{d∈P_s} Q_{τ d}`, which is a bijection because `φ^♯_s` is.
Hence `φ◁q` is cartesian.

*Right variable.* `q◁φ` acts on shapes by `(t,σ) ↦ (t, f∘σ)` and on positions by
`Σ_{e∈Q_t} P'_{f σ(e)} → Σ_{e∈Q_t} P_{σ(e)}`, the coproduct of the bijections `φ^♯_{σ e}`, hence a
bijection.

Over `Vec_fd` with `◁=⊗`: `φ⊗q` has position components `φ^♯_s ⊗ \mathrm{id}_{Q_t}`, isomorphisms
because `φ^♯_s` is; same on the other side. ∎

**Proposition 2.2 (right-variable fibredness — prior art: Pradic–Price Lemma 15).** Over `Set`,
for every `q=(T,Q)` the endofunctor
`q◁(−)` is **fibred**, with base functor the polynomial functor `⟦q⟧` itself:
`π(q◁p) = Σ_{t∈T}(π p)^{Q_t} = ⟦q⟧(π p)`, strictly and naturally.

> **PRIOR ART — this is Pradic–Price, Lemma 15** (`2601.15420`, p. 14; proof p. 31), verbatim:
> *"▶ Lemma 15. The following functor is fibred polynomial: `Cont(C) → Cont(C)`, `X ↦ X ⋆ P`."*
> Their `X ⋆ P` is my `p ◁ q` with `q = P` (notation reconciliation, §8.1), so their `X ↦ X ⋆ P` is
> my `q◁(−)`. **With the same base functor:** their proof reads *"The base of the fibred polynomial
> functor `J ↦ Σ_{i:I} J^{A_i}` is clearly polynomial"* — and `Σ_{i:I} J^{A_i} = ⟦q⟧(J)`. Their
> Definition 13 is strict, and Proposition 2.2 is strict too, so this is the same statement and not
> merely a weaker one. **Proposition 2.2 must therefore be cited, not claimed;** the proof below is
> my own derivation of a known result, recorded because §5 uses its formula. Note PP's Lemma 15 is a
> statement about *fibred polynomial* functors, so it additionally carries their clauses 13.2/13.3,
> which Proposition 2.2 does not assert. See §8.2 for what remains mine.

*Proof.* Immediate from (SUB) with the arguments swapped: the shape set of `q◁p` is
`Σ_{t∈T} S^{Q_t}` and depends on `p` only through `S=π p`; on morphisms `π(q◁φ) = ⟦q⟧(f)` by the
shape formula in Lemma 2.1. Cartesian preservation is Lemma 2.1. ∎

**Remark 2.3 (what BHM's clause does and does not block).** By Proposition 2.2 the three fixpoints
BHM list — `μX.1+A⊗X`, `μX.1+A×X`, `μX.1+A▷X` — are all fixpoints of endofunctors built from the
**right** variable, hence all fibred (for `⊗` and `×` this is immediate from (DIR):
`π(a⊗p)=π(a)×π(p)`, `π(a×p)=π(a)×π(p)`). Their shape-level base functors are then the
corresponding polynomial functors on `Set`, so a fibrational fixpoint construction would compute
the shape level as the `W`-type `μS.\,1+⟦q⟧S` — *an aside about what such a construction would
yield, not a claim proved here; I do not construct the fixpoints.* What genuinely falls outside a
left-variable-fibred treatment is the graded monad `T_P(X)=X▷P` — BHM's own primitive — which is
exactly `L_q`. So their stated reason is correct *about `T_P`* but does not, on Definition 1.3,
obstruct the fixpoints they list. I record this as an observation, not a criticism of a two-page
abstract.

---

## 3. Theorem A — over `Set` the three conditions coincide

Throughout `q=(T,Q)` is fixed and `L_q=(−)◁q` on `Poly = Fam(Set^op)`.

### 3.1 The right-adjoint criterion

**Lemma 3.1.** `L_q` preserves coproducts. Consequently `L_q` has a right adjoint iff for every
`r=(R,M)` the functor
> `G_r : Set → Set,   G_r(Z) := Poly(\,⟨Z⟩◁q,\; r\,)`
is a **polynomial functor**, i.e. `G_r ≅ ∐_{u∈U} Set(N_u,−)` for some family `(N_u)_{u∈U}` of sets.

*Proof.* Coproduct preservation is read off (SUB): the shape set of `(∐_i p_i)◁q` is
`∐_i Σ_{s∈S_i}T^{P_s}` with matching positions. Now `p=(S,P) = ∐_{s∈S}⟨P_s⟩`, so
`Poly(L_q p, r) = ∏_{s∈S} G_r(P_s)`, while `Poly(p,(U,N)) = ∏_{s∈S} ∐_{u∈U} Set(N_u,P_s)`. If
`G_r ≅ ∐_u Set(N_u,−)` naturally then `(U,N)` represents `Poly(L_q(−),r)`, and pointwise
representability for all `r` gives the right adjoint. Conversely, if `H=(U,N)` represents
`Poly(L_q(−),r)`, restricting the natural isomorphism to `p=⟨Z⟩` gives
`G_r(Z) ≅ ∐_u Set(N_u,Z)` naturally in `Z`. ∎

Functoriality of `G_r`: a map `i:A→Z` induces `⟨Z⟩→⟨A⟩` in `Poly` (morphisms
`⟨Z⟩→⟨A⟩` are maps `A→Z`), hence `⟨Z⟩◁q → ⟨A⟩◁q`, hence `G_r(A)→G_r(Z)`; `G_r` is covariant.

**Computation 3.2.** `⟨Z⟩◁q = \big(T^Z,\ τ ↦ Σ_{d∈Z}Q_{τ d}\big)`, and the map
`⟨Z⟩◁q → ⟨A⟩◁q` induced by `i:A→Z` is **restriction** `\mathrm{res}_i : T^Z → T^A`,
`τ ↦ τ∘i`, on shapes.

**Computation 3.3 (the shape probe).** Let `\mathbf 2 := (2,\,∅)` (two shapes, empty positions).
Then `Poly(x,\mathbf 2) = 2^{|π x|}` for every `x`, so
> `G_{\mathbf 2}(Z) \;=\; 2^{T^Z}`,  with `G_{\mathbf 2}(i) : 2^{T^A} → 2^{T^Z}` given by
> **preimage** along `\mathrm{res}_i`, i.e. `W ↦ \mathrm{res}_i^{-1}(W)`.

This is independent of `Q` — the shape probe sees only `T`. (Verified numerically: for `|T|=2`,
`G_{\mathbf 2}(Z)=2,4,16,256,65536` for `|Z|=0..4`.)

### 3.2 The support lemma

**Lemma 3.4 (least support).** Let `F = ∐_{u∈U}Set(N_u,−)` be a polynomial functor, `A ⊆ Z`, and
`x=(u,g)∈F(Z)`. Then `x` lies in the image of `F(A)→F(Z)` **iff** `\mathrm{im}(g) ⊆ A`.
Consequently, if `x` lies in the image of `F(A_i)` for every member of a family `(A_i)_{i∈I}` of
subsets of `Z`, then `x` lies in the image of `F(⋂_i A_i)`.

*Proof.* `F(ι_A)` sends `(u,h)` to `(u, ι_A∘h)`. So `x=(u,g)` is in the image iff `g` factors as
`ι_A∘h` for some `h:N_u→A`, iff `\mathrm{im}(g)⊆A`. For the consequence,
`\mathrm{im}(g)⊆A_i` for all `i` gives `\mathrm{im}(g)⊆⋂_i A_i`. ∎

(This is the elementary form of the classical fact that familially representable endofunctors of
`Set` are exactly those preserving wide pullbacks, Carboni–Johnstone; I do not need the general
theorem, only Lemma 3.4, which is two lines.)

### 3.3 Proof of Theorem A

**Theorem A.** For `q=(T,Q) ∈ Poly` the following are equivalent:
 (i) `L_q` is vertical; (ii) `L_q` is fibred; (iii) `L_q` has a right adjoint; (iv) `|T|=1`.

*Proof.*

**(iv) ⟹ (i).** If `T={∗}` then (SUB) gives `p◁q = (S,\ s↦P_s×Q)`, so `π L_q = π` on the nose,
and `L_q` preserves cartesian morphisms by Lemma 2.1. (Note `p◁y^Q = p⊗y^Q`: the coproduct `∐_t`
being a singleton, there is nothing for `[Z,−]` to fail to preserve — the same *collapse* as
Proposition 1.4, obtained by trivialising `T` instead of by tininess.)

**(i) ⟹ (ii).** Trivial (`F_0=\mathrm{Id}`).

**(ii) ⟹ (iv).** Suppose `π L_q ≅ F_0 π`. Evaluate at `⟨∅⟩` and `⟨1⟩`, which have the same shape
set `{∗}`. Then
`T^{∅} ≅ π(⟨∅⟩◁q) ≅ F_0(1) ≅ π(⟨1⟩◁q) ≅ T^{1}`, i.e. `1 ≅ T`. Hence `|T|=1`.

*(Only the object part of fibredness is used; naturality and cartesianness are not needed. So
`|T|≠1` fails fibredness in the weakest possible sense: the shape set of `p◁q` is not even a
function of the shape set of `p` up to bijection. Numerically: `|T|=2` gives `1,2,4` shapes for
`⟨∅⟩,⟨1⟩,⟨2⟩`, all three of which have one shape.)*

**(iv) ⟹ (iii).** Let `T={∗}`, `Q_{∗}=Q`. For `r=(R,M)`,
```
 G_r(Z) = Poly((1, Z×Q),(R,M)) = ∐_{ρ∈R} Set(M_ρ,\;Z×Q)
        = ∐_{ρ∈R} Set(M_ρ,Z) × Set(M_ρ,Q)
        = ∐_{ρ∈R} ∐_{h : M_ρ→Q} Set(M_ρ, Z),
```
a polynomial functor with index set `U = Σ_{ρ∈R}Q^{M_ρ}` and `N_{(ρ,h)} = M_ρ`. By Lemma 3.1 the
right adjoint exists, with `[q◁r] = \big(Σ_{ρ∈R}Q^{M_ρ},\; (ρ,h) ↦ M_ρ\big)`.
*(Verified: 3000/3000 random `(Q,P,M)` satisfy `|Poly(p◁y^Q,r)| = |Poly(p,[q◁r])|`.)*

**(iii) ⟹ (iv).** Assume `L_q ⊣ H`. By Lemma 3.1, `G_{\mathbf 2}(Z)=2^{T^Z}` is polynomial, say
`G_{\mathbf 2} ≅ F = ∐_{u∈U}Set(N_u,−)`; transport images along this natural isomorphism.

*Case `|T|=0`.* `G_{\mathbf 2}(Z) = 2^{0^Z}`, so `G_{\mathbf 2}(1)=2^0=1` and
`G_{\mathbf 2}(∅)=2^1=2`. From `F(1)=U` we get `|U|=1`; from
`F(∅) = \{u : N_u=∅\}` we get `2 = |F(∅)| ≤ |U| = 1`, absurd.

*Case `|T|≥2`.* Fix `t_0 ≠ t_1` in `T`. Take `Z=ℕ` and, for `n∈ℕ`, `A_n := ℕ∖\{n\}`. Consider
```
      x := \{ τ∈T^{ℕ} : τ(m)=t_0 \text{ for all but finitely many } m \}  ∈ 2^{T^{ℕ}} = G_{\mathbf 2}(ℕ).
```
By Computation 3.3, `G_{\mathbf 2}(A)→G_{\mathbf 2}(Z)` is `W ↦ \mathrm{res}_A^{-1}(W)`
(injective, since `\mathrm{res}_A:T^Z→T^A` is surjective as `T≠∅`), so its image is exactly the set
of `x⊆T^Z` that are unions of fibres of `\mathrm{res}_A`, i.e. the `x` **invariant under
re-choosing the coordinates outside `A`**.

- For each `n`, `x` is invariant under changing the single coordinate `n` (changing one coordinate
  does not change "all but finitely many"), so `x ∈ \mathrm{im}\,G_{\mathbf 2}(A_n)`.
- `⋂_n A_n = ∅`, and `\mathrm{im}\,G_{\mathbf 2}(∅) = \{∅,\;T^{ℕ}\}` (the two fibres of
  `T^ℕ → T^{∅}=1`).
- But `x ≠ ∅` (it contains the constant sequence `t_0`) and `x ≠ T^ℕ` (it omits the constant
  sequence `t_1`).

This contradicts Lemma 3.4. Hence `|T|=1`. ∎

**Corollary A′ (a proof of Pradic–Price's Remark 16; added 2026-08-30).** Pradic–Price state, in
full and without proof,
> *"▶ Remark 16. On the other hand, `X ↦ P ⋆ X` is **not fibred**."* (`2601.15420`, p. 14.)

In their notation `P ⋆ X = X ◁ P` (§8.1), so their `X ↦ P ⋆ X` is exactly `L_q = (−)◁q` with
`q = P`. Theorem A (ii ⟹ iv) refutes fibredness in the sense of Definition 1.3 for every `q` with
`|T| ≠ 1`; since PP-fibred ⟹ (F) (§8.3), it refutes theirs *a fortiori*, and it does so using only
the object part of fibredness. **We supply a proof of a remark stated without proof in [PP26].**

*Scope of the claim, stated conservatively.* (i) I prove it for `C = Set`, which is the instance
BHM's clause is about; PP assert Remark 16 for a general lextensive `C` and I do not prove that
generality. (ii) Remark 16 is genuinely unproved there: grepping the 45-page v2, the only
occurrences of "Remark 16" are the statement on p. 14 and the back-reference in §4.2 on p. 18
(*"one of these is not fibred (Remark 16) and the other is (Lemma 15)"*); Appendix B.1 proves
Lemmas 14, 15 and 49 only. So in the literature Remark 16 is the same epistemic object as BHM's
parenthetical — an unproved assertion — and BHM's clause is downstream of it. (iii) Theorem A says
more than Remark 16 does: it gives the exact boundary `|T|=1` and glues it to `(V)` and `(C)`.

**Remark 3.5 (strengthening of Workers Thm 2).** My earlier proof that `Cont` lacks a
`◁`-closure (`2026-08-21-workers-x-closed-lhd-obstructed.md`) argued by a **counting** estimate —
the forced hom would have `|H([n])| ≥ 2^{2^n}`, super-polynomial. That argument is confined to
finite `T` and finite test sets. Lemma 3.4 replaces counting by **least supports** and therefore
covers **all** `T` with `|T|≥2`, finite or infinite, uniformly, as well as the degenerate case
`|T|=0` which the counting argument did not address. Theorem A is thus strictly stronger than the
`Set` half of what I had, and it is the version that the `Fam(C^op)` programme needs.

*(Numerics: the brute-force search for a polynomial-functor fit `G(n)=Σ_u n^{k_u}` to
`(G(0),…,G(4))` returns **no fit** for `|T|=0,2,3` and returns the correct fit
`\{k_u\}=\{0,0\}` — i.e. the constant functor `2 = ∐_{u∈2}y^{∅}` — for `|T|=1`.)*

---

## 4. Theorem B — over `Vec_fd` the three conditions separate

Fix a field `k` and work in `Fam(Vec_{fd}^{op})` with `◁ = ⊗` (Prop 1.4 and the honesty note there):
`p◁q = (S×T,\ P_s⊗Q_t)`. Write `U:Vec_{fd}→Set` for the underlying-set functor,
so `C(k,Z)=U(Z)` and `C(N,Z) ≅ U(Z)^{\dim N}`.

**Theorem B.** Let `q=(T,Q)∈Fam(Vec_{fd}^{op})` and `T' := \{t∈T : Q_t ≠ 0\}`. Then:

1. `L_q` is **fibred**, for every `q`, with `F_0 = (−)×T`.
2. `L_q` is **vertical** iff `|T|=1`.
3. `L_q` has a **right adjoint** iff `T'` is **finite**.

Hence with `q_2 := (2,\,Q_t=k)` and `q_ω := (ℕ,\,Q_t=k)`:
```
     q_2  : closed but NOT vertical.        q_ω : fibred but NOT closed.
```
so `(V) ⊊ (C) ⊊ (F)` strictly.

*Proof.*

**(1).** `π(p◁q)=S×T=F_0(π p)` strictly and naturally, and cartesian morphisms are preserved by
Lemma 2.1. **(2).** `S×T ≅ S` naturally in `(S,P)` forces `|T|=1` (take `S=1`); conversely `|T|=1`
gives `π L_q = π`.

**(3), sufficiency.** `⟨Z⟩◁q = (T,\ t↦Z⊗Q_t)`, so for `r=(R,M)`
```
 G_r(Z) = ∏_{t∈T} ∐_{ρ∈R} C(M_ρ,\; Z⊗Q_t)
        = ∐_{ρ:T→R} ∏_{t∈T} C(M_ρ(t),\; Z⊗Q_t)          (Set is infinitely distributive)
```
Split `T = T' ⊔ T_0` with `Q_t=0` on `T_0`. For `t∈T_0`, `C(M,\,Z⊗0)=C(M,0)=1`. For `t∈T'`, `Q_t`
is finite-dimensional hence dualizable, so `C(M_{ρ t},\,Z⊗Q_t) ≅ C(M_{ρ t}⊗Q_t^{*},\,Z)`. If `T'`
is finite, `∏_{t∈T'}C(N_t,Z) ≅ C(⊕_{t∈T'}N_t,\,Z)` and the finite direct sum stays in `Vec_{fd}`.
Hence
> `G_r ≅ ∐_{ρ∈R^{T}} C\big(\;⊕_{t∈T'} M_{ρ(t)}⊗Q_t^{*}\;,\;−\big)`,
familially representable; the left closure is
`[q◁r] = \big(R^{T},\ ρ ↦ ⊕_{t∈T'}M_{ρ(t)}⊗Q_t^{*}\big)`.
*(Verified: 4000/4000 random `(Q,P,M)` over `F_2` satisfy
`|Fam(p◁q,r)| = |Fam(p,[q◁r])|`.)*

**(3), necessity.** Suppose `T'` is infinite and `L_q ⊣ H`. Apply Lemma 3.1 — whose proof is
verbatim the same over any base `C`, giving: `G_r ≅ ∐_{u∈U} C(N_u,−)` for `N_u ∈ Vec_{fd}` — to the
**position probe** `r := ⟨k⟩ = (1, k)`. Then
```
   G(Z) = ∏_{t∈T} C(k,\; Z⊗Q_t) = ∏_{t∈T'} U(Z⊗Q_t)      (the factors over T_0 are singletons).
```

*Step 1: `|U|=1`.* Evaluate at `Z=0`: `Z⊗Q_t=0`, so `G(0)=∏_{t∈T'}U(0)=1`; and
`∐_u C(N_u,0) = |U|` because `C(N,0)=1` for every `N` (`Vec_{fd}` is pointed). So `|U|=1` and
`G ≅ C(N,−)` for a single `N∈Vec_{fd}`; put `n:=\dim N < ∞`.

*Step 2: Yoneda.* Let `(v_t)_{t∈T'} ∈ ∏_{t∈T'}U(N⊗Q_t)` be the element corresponding to
`\mathrm{id}_N ∈ C(N,N)`. Naturality of the isomorphism `C(N,−) ≅ G` says: for every `f:N→Z`, the
element of `G(Z)` corresponding to `f` is `\big((f⊗Q_t)(v_t)\big)_{t∈T'}`. Since every element of
`C(N,Z)` is of the form `f`, **every** element of `∏_{t∈T'}U(Z⊗Q_t)` is of that form.

*Step 3: contradiction.* Take `Z=k`, so `Z⊗Q_t ≅ Q_t`. The assignment
`Φ : N^{*} = C(N,k) → ∏_{t∈T'}Q_t,\quad f ↦ \big((f⊗Q_t)(v_t)\big)_t`
is `k`-linear (each `f↦(f⊗Q_t)(v_t)` is), so its image is a subspace of dimension at most
`\dim N^{*} = n`. But `∏_{t∈T'}Q_t ⊇ ⊕_{t∈T'}Q_t` has dimension at least `|T'| ≥ ℵ_0 > n`, so `Φ`
is not surjective — contradicting Step 2. ∎

**Corollary B′ (the separator, made explicit).** For `q_ω=(ℕ, Q_t=k)` over `Vec_{fd}`:
`(−)◁q_ω` **is fibred** (base functor `(−)×ℕ`, Theorem B(1)) but has **no right adjoint**
(Theorem B(3)). Concretely `G(Z) = U(Z)^{ℕ}`, and `U(−)^{ℕ} ≅ C(N,−)` would force
`N^{*} → k^{ℕ},\ f ↦ (f(v_t))_t` to be surjective from an `n`-dimensional space onto a space
containing `n+1` independent vectors `e_0,…,e_n`. The forced position object is
`⊕_{t∈ℕ}k = k^{(ℕ)} ∉ Vec_{fd}`.

**Scope note (added 2026-08-30): Theorem B is outside Pradic–Price's framework.** Theorem B(1) says
`L_q` is fibred *for my `π` and my Definition 1.3*. It is **not** a statement that `L_q` is fibred in
the sense of [PP26], which is undefined here, for two independent reasons. (i) **Different total
category.** PP's `Cont(C)` is *internal*: objects are morphisms `P : A → I` of `C`, and the base of
`shape` is `C` itself (§2.2, p. 8). `Fam(C^op)` keeps an **external** shape *set* `S` with a family
of `C`-objects, base `Set`. The two agree exactly when `C = Set`; `Fam(Vec_{fd}^{op}) ≠
Cont(Vec_{fd})`. (ii) **Their standing hypothesis fails.** §2.1, p. 7: *"Henceforth, all categories
in sight shall be lextensive"* (and their Theorem 18, p. 14, wants lextensive with dependent W- and
M-types). `Vec_{fd}` is **not** extensive — `∐ ⊊ ⊕`, `vec-biproduct-collapse-proved` — and not LCC.
So Theorem B neither conflicts with [PP26] nor draws support from it; this is exactly where the two
notions come apart. See §8.4, and §8.5 for why that hypothesis is itself the point.

**Remark B″.** Theorem B(3) is a genuine sharpening of my T4-left Theorem 3.1(2), which stated
failure over `Fam(Vec_{fd}^{op})` for infinite shape sets: the correct boundary is not "`T` infinite"
but "**infinitely many non-zero positions**" — a `q` with infinitely many shapes carrying the zero
position object is still left-closed, because zero positions contribute no summand. The `Set`
analogue is **false** (`q=(2,∅)` is not left-closed, Theorem A), which is itself an instance of
the diagnosis below: over `Set` a shape counts even when its position set is empty, because the
shape probe `\mathbf 2` sees it; over `Vec_{fd}` a shape with zero position is invisible to the
position probe and the shape probe is vacuous.

---

## 5. Diagnosis — one test, two probes

Both conditions are consequences of the single question of Lemma 3.1:

> for every `r=(R,M)`, is `G_r(Z) = Fam(⟨Z⟩◁q,\,r) = ∏_{w∈W(Z)} ∐_{ρ∈R} C\big(M_ρ,\;\mathrm{Pos}_w(Z)\big)`
> familially representable, where `W(Z) := π(⟨Z⟩◁q)`?

**Proposition 5.1 (fibredness is a shape-level statement).** For any base, `L_q` is fibred iff the
assignment `Z ↦ W(Z) = π(⟨Z⟩◁q)` is constant up to bijection.

*Proof.* `π` preserves coproducts, and so does `L_q` in its left variable (§1.2), and
`p=∐_{s∈S}⟨P_s⟩`; hence `π(p◁q) = ∐_{s∈S} W(P_s)`. (⟸) If `W` is constant `= W_0` then
`π(p◁q) ≅ S×W_0`, so `F_0 := (−)×W_0` works, and cartesian preservation is automatic (Lemma 2.1).
(⟹) If `π L_q ≅ F_0 π` then taking `p=⟨Z⟩` (shape set `{∗}`) gives `W(Z) ≅ F_0(1)` for every `Z`,
so `W` is constant. ∎

Over `Set`, `W(Z)=T^Z` — constant iff `|T|=1`. Over a tiny-positioned base, `W(Z)=T` — constant
always. **Fibredness is exactly the collapse of the shape object.**

**Proposition 5.2 (the shape probe).** Suppose `C` has an initial object `0` with `C(0,X)≅1` for
all `X` (true in `Set` with `0=∅`, and in `Vec_{fd}` with `0` the zero space). Take
`r_R := (R,\; M_ρ = 0)`. Then `G_{r_R}(Z) = R^{W(Z)}`. Hence a necessary condition for `L_q` to be
left-closed is that `Z ↦ R^{W(Z)}` be familially representable for every set `R`.

*Proof.* Each factor `∐_{ρ∈R}C(0,\mathrm{Pos}_w(Z)) = ∐_{ρ∈R}1 = R`. ∎

**Corollary 5.3 (why `Set` collapses the two conditions).** Over `Set`, `r_2 = \mathbf 2` and
`G_{\mathbf 2}(Z) = 2^{T^Z}`, which by the proof of Theorem A(iii⟹iv) is polynomial **iff**
`|T|=1` **iff** `L_q` is fibred. So over `Set`:
> **closed ⟹ (shape probe) ⟹ fibred**,
conceptually and not merely by classification. Over `Vec_{fd}` the shape probe is vacuous:
`W(Z)=T` is already constant, `G_{r_R}(Z)=R^{T}` is a constant functor, and constant functors are
familially representable (`∐_{u}C(0,−)`, since `C(0,−)≅1`). The obstruction therefore migrates to
the **position probe** `r=⟨I⟩`, which tests whether the forced position
`⊕_{t}M_{ρ(t)}⊗Q_t^{*}` — the *summability* of the collapsed coproduct — exists in the base.

> **The mechanism, in one line.**
> `fibredness = the exponent in Σ_s T^{P_s} disappears (collapse)`;
> `left-closure = collapse AND the resulting coproduct is summable inside the base`.
> Over `Set` the only collapse mechanism is `|T|=1`, which trivialises summability too, so the two
> coincide. Over a linear base collapse is generic (tininess) and the two decouple. **Fibredness is
> strictly weaker than left-closure wherever collapse is generic.**

**Remark 5.4 (the third occurrence of a pattern).** This is the third time that two conditions which
*look* like the same "canonical map is an isomorphism" turn out to constrain different legs of the
same formula: (a) Weber-distributivity `Φ` vs. the T2 tininess test `δ`
(`weber-delta-vs-t2-phi-distinct`); (b) the `⊗`-closure conjuncts A (dualizability) and B
(summability) in T2; (c) fibredness vs. left-closure here. In all three the resolution is the same
move: **write the single formula both conditions are about, and identify which factor each one
constrains.** Here the formula is `G_r(Z) = ∏_{w∈W(Z)}∐_ρ C(M_ρ,\mathrm{Pos}_w(Z))`, fibredness
constrains `W`, closure constrains the whole. I now regard this as a **method**, not a coincidence.

---

## 6. Verification

`scratch/fibredness-vs-closure/verify.py` — all green.

1. **Shapes read positions.** `|π(⟨Z⟩◁q)|` for `|T|=2` and `|Z|=0,1,2` is `1,2,4`, though all three
   `⟨Z⟩` have a single shape. Independent of `Q` (checked for `Q=(1,1),(0,0),(2,1)`). Witnesses
   Theorem A(ii⟹iv).
2. **Monomial closure.** `|Poly(p◁y^Q,r)| = |Poly(p,[q◁r])|` with
   `[q◁r]=(Σ_ρ Q^{M_ρ},M_ρ)`: **3000/3000** random instances. Also `p◁y^Q = p⊗y^Q` on all tested
   `(P,Q)`. Witnesses Theorem A(iv⟹iii).
3. **Shape probe.** `G_{\mathbf 2}(Z)` computed by brute force equals `2^{|T|^{|Z|}}`:
   `2,4,16,256,65536` for `|T|=2`, `|Z|=0..4`; `2,8,512,134217728` for `|T|=3`; `2,1,1,1` for
   `|T|=0`; `2,2,2,2,2` for `|T|=1`. Exhaustive search for a polynomial-functor fit
   `G(n)=Σ_u n^{k_u}` (legitimate: `G(n)<∞` for `n≥2` forces every `N_u` finite, and `|U|=G(1)<∞`)
   returns **no fit** for `|T|=0,2,3`, and the fit `\{k_u\}=\{0,0\}` for `|T|=1`.
4. **`Vec_{fd}(\mathbb F_2)`.** `|Fam(p◁q,r)| = |Fam(p,[q◁r])|` with
   `[q◁r]=(R^T,\ \dim = Σ_t \dim M_{ρ t}\cdot\dim Q_t)`: **4000/4000** random instances (finite
   `T`). And `\max_ρ \dim N_ρ = 1,2,3,4,5,6,7` for `Q=(k,\dots,k)` with `|T|=1..7` — linear growth,
   so the `T→∞` limit leaves `Vec_{fd}`. Witnesses Theorem B(3) both ways.
5. **Explicit morphisms.** `(−)◁q` implemented on explicit container morphisms
   `(f, φ^♯)`: functoriality `(φ_2φ_1)◁q = (φ_2◁q)(φ_1◁q)` on **183/183** random composable
   pairs, and **400/400** cartesian lifts `(f,\mathrm{id}):(S,P'f)→(S',P')` map to morphisms whose
   position components are bijections. This is the check that caught and fixed the shape action in
   Lemma 2.1 (it is `τ∘φ^♯_s`, not `τ∘(φ^♯_s)^{-1}`; the latter does not even typecheck for
   non-cartesian `φ`).
6. **The image computation behind Lemma 3.4's use.** For `|T|=2` and `|Z|≤3`, the image of
   `G_{\mathbf 2}(A_n) → G_{\mathbf 2}(Z)` was computed exhaustively and equals, on the nose, the
   set of `x ⊆ T^Z` invariant under changing coordinate `n`. (For *finite* `Z` the intersection of
   these images is already `\{∅,T^Z\}`, which is why the argument in Theorem A needs `Z=ℕ`: only
   an infinite `Z` supports a proper invariant subset. The finite cases are instead killed by the
   fit search of item 3 — two independent falsifications.)

---

## 7. Gaps, and what is *not* claimed

1. **Attribution (CLOSED 2026-08-30 — and it cost results).** `arXiv:2601.15420` was fetched, read
   and quoted (`papers/pradic-price_2601.15420_fixpoints-poly-of-poly.pdf`; extraction in
   `scratch/2026-08-30-pradic-price-fibred-def.md`). Outcome, in full: their fibration **is**
   Definition 1.1 over `Set` (§2.2, pp. 8–9); their fibredness is the `(F,F_0)` form and **strict**
   (Def 13 clause 1, p. 14), so PP-fibred ⟹ (F) and every negative result here holds a fortiori;
   **Proposition 2.2 is their Lemma 15** (p. 14, proof p. 31), re-attributed; **the `Set` half of
   Lemma 2.1 is Niu–Spivak Prop. 6.88** (p. 213), which they cite at p. 31, also re-attributed; and
   in the other direction **Theorem A supplies a proof of their unproved Remark 16** (p. 14),
   recorded as Corollary A′. Theorem B is **outside** their scope (`Vec_{fd}` not lextensive, p. 7;
   `Fam(C^op) ≠ Cont(C)`) — no conflict, no support. Full accounting: **§8**. BHM's clause is still
   cited only as corroboration.
2. **Remark 2.3** observes that BHM's stated reason does not, under Definition 1.3, obstruct the
   three fixpoints they list (those are right-variable). This is an observation about a two-page
   abstract with no definitions, not a claim that they are wrong; their notion may differ.
3. **`◁` on `Fam(Vec_{fd}^{op})` is defined, not derived** (honesty note after Prop 1.4): `⟦−⟧` is
   not full over `Vec`, so Prop 1.4 pins the extension, not the object. Theorem B is literally a
   theorem about `(−)⊗q`.
4. **No general "closed ⟹ fibred".** Proposition 5.2 gives the general *shape probe* necessary
   condition; Corollary 5.3 upgrades it to "closed ⟹ fibred" over `Set` only, because that step
   uses the `Set`-specific Lemma "`2^{T^Z}` polynomial ⟹ `|T|=1`". Whether closed ⟹ fibred holds
   over an arbitrary base is **open**. I know of no counterexample.
5. **Bases between `Set` and `Vec_{fd}`.** The dichotomy proved here is at the two extremes
   (extensive; tiny-positioned). What happens over, e.g., `Fam(Vec^{op})` (positions not tiny, so
   `◁` is not even defined by Prop 1.4), or over a base that is neither extensive nor linear, is
   not addressed.

---

## 8. Relation to Pradic–Price `2601.15420` — attribution and scope

*Added 2026-08-30, after obtaining and reading the paper. Source of every quote below:
`papers/pradic-price_2601.15420_fixpoints-poly-of-poly.pdf` (v2 [cs.LO] 11 May 2026, LICS 2026,
45 pp. incl. appendices) and its `pdftotext -layout` transcript
`papers/pradic-price_2601.15420.txt`; extraction notes with fuller context in
`scratch/2026-08-30-pradic-price-fibred-def.md`. Page numbers are the printed page numbers.
Nothing in §§1–7 above is restructured or re-proved by this section — it changes **who is credited**
and **what the results are claims about**, not what is true. No trust grade is revised.*

### 8.1 Notation reconciliation — record this, do not re-derive it

Pradic–Price write the composition product as **`Q ⋆ P`**. For `P : A → I` and `Q : B → J`, with
`A_i := P^{-1}(i)`, their `⋆` (Figure 4, p. 9, and the Lemma 15 proof, p. 31) has shape object
`Σ_{i:I} J^{A_i}` and directions `Σ_{i:I}Σ_{a:A_i}Σ_{f:A_i→J} B_{f(a)}`. Comparing with (SUB),
`p◁q = (Σ_{s∈S} T^{P_s},\ (s,τ)↦Σ_{d∈P_s}Q_{τ d})`:

> **`Q ⋆ P` (Pradic–Price) `=` `P ◁ Q` (mine).** Their **left** argument is my **right** argument.

The two flips cancel: their *"`X ↦ X ⋆ P`"* is my `q◁(−)` — the **right** variable in both
vocabularies — and their *"`X ↦ P ⋆ X`"* is my `L_q = (−)◁q` — the **left** variable in both. So the
phrase "not fibred in its **left** variable" denotes the *same* variable in Pradic–Price, in
Braithwaite–Hedges–Mihejevs, and in these notes. There is no discrepancy to reconcile downstream.

### 8.2 What is prior art, and what is left as mine

**Prior art (re-attributed above).**

1. **Proposition 2.2 (right-variable fibredness, base functor `⟦q⟧`) is Pradic–Price Lemma 15**,
   p. 14, proved p. 31: *"▶ Lemma 15. The following functor is fibred polynomial: `Cont(C) →
   Cont(C)`, `X ↦ X ⋆ P`."* Their proof identifies the base functor as *"`J ↦ Σ_{i:I} J^{A_i}` is
   clearly polynomial"*, i.e. **literally `⟦q⟧`** — the same base functor, not merely an equivalent
   one. My §0 "Bonus" framing is withdrawn: this is a citation, not a contribution.
2. **The `Set` half of Lemma 2.1 (cartesian preservation in both variables, unconditionally) is
   Niu–Spivak `2312.00990`, Proposition 6.88, p. 213** (*"if `φ : p → p'` and `ψ : q → q'` are
   cartesian, so is `φ ◁ ψ`"*). Pradic–Price cite it by name: p. 31, *"That the functor is fibred
   follows since if `ϕ:P→P'`, `ψ:Q→Q'` are cartesian, then so is `ψ⋆ϕ` [50, Proposition 6.88]"*,
   with `[50]` = Niu–Spivak. **This corrects the verdict in §5.2 of the extraction note**, which
   asserted that PP "never isolate this": they do state it, by citation, for both variables jointly
   (and jointly ⟹ separately, taking one argument to be an identity, which is cartesian).
   Niu–Spivak Exercise 6.89 (p. 213) records the complementary fact that `◁` does **not** preserve
   *vertical* lenses.

**What remains mine on the `Set` side.** Only two things, and they should be described as such:

- the **`Fam(C^op)` half of Lemma 2.1** — cartesian preservation for `◁ = ⊗` over a general closed
  symmetric monoidal cocomplete base, which is not a `Poly` statement and is not in either source;
- the **isolation**: cartesianness is *free* in both variables (Lemma 2.1 + Prop. 6.88), so the
  left-variable failure is **purely** a failure of base-functoriality. Neither source draws that
  conclusion — PP's Remark 16 is bare (§8.3) and Niu–Spivak do not discuss the fibration at all.
  This is what makes the failure unrepairable by a comparison map, and it is what §5 turns into the
  probe analysis. It is an observation about known facts, not a new theorem.

**What is a genuine positive contribution (§8.3).** Corollary A′.

### 8.3 Theorem A proves an assertion Pradic–Price state without proof

Pradic–Price's Remark 16 (p. 14) reads, in its entirety:

> *"▶ Remark 16. On the other hand, `X ↦ P ⋆ X` is not fibred."*

There is **no proof and no justification anywhere in the paper or its 25 pages of appendices**: the
only occurrences of "Remark 16" are this statement (p. 14) and a back-reference in §4.2 (p. 18,
*"one of these is not fibred (Remark 16) and the other is (Lemma 15)"*); Appendix B.1 proves Lemmas
14, 15 and 49 only. By §8.1 their `X ↦ P ⋆ X` is my `L_q`, so **Theorem A supplies a proof of a
remark stated without proof in [PP26]** — recorded as Corollary A′ in §3.3.

The implication runs the safe way. Their Definition 13 clause 1 (p. 14) demands
`shape ∘ F = F_0 ∘ shape^k` **strictly** — *"for some **uniquely determined** `F_0 : C^k → C`"*,
corroborated by their Theorem 22 proof (p. 33: *"`(µF)_0 ∘ shape = shape ∘ µF` holds by
construction"*) — where my condition (F) asks only for a natural isomorphism. Hence
**PP-fibred ⟹ (F)**, and Theorem A's refutation of (F) refutes PP-fibredness a fortiori. Over `Set`
their `shape` fibration *is* my `π` (§2.2, pp. 8–9: *"exactly the fibrewise opposite of the codomain
fibration"*), so the two conditions are being evaluated on the same fibration and clause 1 is
exactly (F)-with-strict-equality.

Three honest qualifications. (i) I prove the case `C = Set`; PP assert Remark 16 for a general
lextensive `C`, and I do not prove that generality. (ii) PP's *fibred polynomial* also carries
clauses 13.2 and 13.3 (polynomiality of `F_0` and of the fibre functors), which I neither assume nor
refute — Remark 16 says "not **fibred**", i.e. clause 1, which is the clause Theorem A kills.
(iii) Theorem A is strictly more informative than the remark: it gives the exact boundary `|T|=1`
and welds it to verticality and to left-closure.

### 8.4 Scope: same over `Set`, genuinely different off it

| | Pradic–Price | here |
|---|---|---|
| total category | `Cont(C)`, **internal**: objects are morphisms `P : A → I` of `C` (§2.2, p. 8) | `Fam(C^op)`, **external** shape *set* `S` with a family of `C`-objects |
| base of the fibration | `C` | `Set` |
| fibredness | `(F,F_0)`, **strict** (Def 13.1, p. 14) | `(F,F_0)` up to natural iso (Def 1.3) |
| standing hypothesis | *"all categories in sight shall be lextensive"* (§2.1, p. 7) | closed symmetric monoidal cocomplete `C` |

The two frameworks **coincide at `C = Set`** — `Cont(Set) = Fam(Set^op) = Poly`, their `shape` is my
`π`, their cartesian/vertical are my Lemma 1.2 — and there PP-fibred ⟹ (F), so §3 (Theorem A) sits
squarely inside their scope and strengthens it.

They **diverge off `Set`**, in different directions: they generalise the *base* from `Set` to any
lextensive `C` by internalising shapes; I generalise the *fibres* from `Set` to a closed monoidal
cocomplete `C` while keeping shapes external. Consequently **Theorem B is outside their scope** —
`Fam(Vec_{fd}^{op})` is not `Cont(Vec_{fd})`, and `Vec_{fd}` is not lextensive (`∐ ⊊ ⊕`,
`vec-biproduct-collapse-proved`), so PP-fibredness is simply undefined there. Theorem B(1) must be
read as a statement about **my** `π` and Definition 1.3. **No conflict with [PP26], and no support
from it.** The strict-vs-iso and internal-vs-external caveats bite in exactly this one place.

### 8.5 Observation — lextensivity is why the separation was not visible before

*Flagged as corroboration of a standing thesis, not as a claim about Pradic–Price's intentions or
about any gap in their paper; within their stated scope their treatment is correct and complete.*

Pradic–Price's standing hypothesis is *"Henceforth, all categories in sight shall be lextensive"*
(§2.1, p. 7). Theorem A says that over `Set` — the extensive base par excellence — fibredness,
verticality and left-closure are **the same condition**, and §5 explains why: extensivity leaves
exactly one collapse mechanism (`|T|=1`), which trivialises summability along with it, so the shape
probe is binding and the position probe has nothing left to say. A framework whose objects are all
lextensive therefore **cannot exhibit the separation** `(V) ⊊ (C) ⊊ (F)`: the witnesses `q_2` and
`q_ω` of Theorem B live over `Vec_{fd}`, which the hypothesis excludes. This is direct corroboration
of `extensivity-is-container-boundary` and of the sharper form in
`one-functional-many-probes-method`: **extensivity fuses logically independent conditions**, and
prior work that assumes it is structurally unable to see them come apart. It also explains, without
anyone being wrong, why Remark 16 could sit unproved: inside a lextensive world the left-variable
failure and the closure failure are the same phenomenon and neither needs separating from the other.
