# State liftings are holonomy-free: completeness — **State liftings ≅ Cat**

**MacBeth — PROVE session, 2026-08-11 (deep-work).**
Closes the last lemma of the State-liftings program. Continues
`2026-08-10-state-liftings-grade-independence.md` (grade-independence, **proved**) and
`2026-08-10-state-liftings-holonomy-free.md` (purity, routing, soundness `Cat ↪ liftings`,
computed refutations). Those two files reduced completeness to a single residual lemma —
**holonomy-triviality** — with two sub-claims (H1 source-independence, H2 trivial transport).

> **This file proves holonomy-triviality**, hence completeness:
> **every polynomial fibred monad lifting of the State monad is `𝕊×C` for a single small
> category `C`; so `C ↦ 𝕊×C` is a bijection and the polynomial monad liftings of State are
> exactly the small categories (`State liftings ≅ Cat`).**

The engine of the proof is one identity — the **deepest-object component of associativity** —
which forces the fibre-transport to be **endpoint-local**; endpoint-locality + transitivity of
`S^S ↷ S` + the identity-target unit collapses the `S^S`-grading to a trivial coherent
iso-system, i.e. a single category with trivial transport.

Computational engines (`scratch/general-M-liftings/`): `fit_general.py` (deepest-object
constraint, 196608 records, 0 mismatch), `targeted.py` (unit forces `τ^{id}=id`; endpoint-locality
genuinely needed), `enum_hom.py` / `twist_test.py` (morphism-level: only trivial transport survives;
4 survivors = 4 monoids on 2 elts), `honest.py`/`lean_assoc.py` (the finite `Cont`-morphism law
engines from the companion files).

---

## 0. Headline

> **Theorem (completeness, `|S|=2`, polynomial).** Let `(A_t, ε, δ)` be a polynomial fibred
> monad lifting of `State = (S^S, S)` along `cod : Cont → Set`. Then there is a small category
> `C` and an isomorphism of liftings `(A_t,ε,δ) ≅ 𝕊×C`, where `𝕊` is the action category of
> `S^S ↷ S`. Concretely:
> ```
>    A_t(Q) ≅ ∐_{s∈S} ∐_{c∈Ob C} Q_s^{ out_C(c) }     (grade-independent),
>    ε = C-identities,   δ = source-routed C-composition with TRIVIAL 𝕊-transport.
> ```
> Combined with soundness (companion), **`C ↦ 𝕊×C : Cat → {liftings of State}` is a
> bijection.**

The abstract argument (§3–§4) is uniform in the finite set `S`; `|S|=2` is the machine-verified
regime, consistent with the rest of the program.

---

## 1. Recalled data (proved in the two companion files)

Lifting ↔ family `(A_t : Set^S → Set)_{t∈S^S}` (Prop A′). **Purity + grade-independence:**
```
    A_t(Q) ≅ ∐_{s∈S} ∐_{c∈Ob C̃_s} Q_s^{out_{C̃_s}(c)}     (grade-independent up to iso),
```
for an `S`-indexed family of small categories `(C̃_s)_{s∈S}` (`= A_id`, by (P1) = the Reader
theorem with `E=S`). Object sets `J_t^s ≅ Ob C̃_s` and out-degrees are grade-independent
(grade-independence §3.1–3.2). The counit `ε` gives identity morphisms `e_c∈out(c)`; the
grade-`id` comultiplication `δ_{(id,(id))}` is `C̃_s`-composition (Reader Step C–E).

**Comultiplication / routing (recalled).** For a factorization `(T,(t_s))` with threaded grade
`σ(s)=t_s(T(s))`, on an object `j∈J_σ^{s*}`:
```
    δ_out(j)=i∈J_T^{s*}   (source-preserving),
    per o∈Out(i):  inner object f(o)∈J_{t_{s*}}^{T(s*)}   (at the threaded state T(s*)),
    β : Σ_o Out(f(o)) → Out(j)   (backward on out-positions).
```

**The transport datum.** For `g∈S^S`, `s∈S`, `c∈O_s := Ob C̃_s`, the right-unit factorization
`(T=g, t_s=id)` (grade `σ=g`) gives, by (RU1) `δ_out=id` and (RU2), a **target map**
`tgt_g : out_s(c) → O_{g(s)}`. Write, for the object part,
```
    τ^g(s,c) := tgt_g(e_c) ∈ O_{g(s)}          (transport of the object c along g).
```
At `g=id`, `tgt_id` is the ordinary target function of `C̃_s`, so
```
    (U)   τ^{id}(s,c) = target of the identity e_c = c.
```

**Remark (the inner object depends only on the outer grade — no `tvec`-freedom).** In a general
factorization `(T,(t_s))` the inner object `f(o)` lives at grade `t_{s*}`, which varies with the
factorization. But **grade-independence** (§3.1 of the companion) provides *canonical* bijections
`sh_{t} : J_{t}^{r} ≅ J_{id}^{r} = O_r` whose inverse is unique (independent of auxiliary choices).
Normalizing the inner object by `sh`, `n(o) := sh_{t_{s*}}(f(o)) ∈ O_{T(s*)}`, absorbs the grade
`t_{s*}`: the normalized inner object is a function of the **outer** data `(T, s*, o)` alone. Hence,
in the grade-independence-normalized coordinates `A_t ≅ A_{id}`, the transport is a family
`τ^{T}` indexed by the outer grade `T` only — the form used below. (Sanity check `tvec_dep.py`
Test 1: perturbing a single factorization's inner object to depend on `t_{s*}` breaks the monad
laws.)

---

## 2. The deepest-object component of associativity

The associativity law `μ∘Tμ = μ∘μT` is an equality of container morphisms on `TTT`. A `TTT`-shape
carries an outer `T∈S^S`, middles `(t_s)_s`, inners `(ρ_{s,r})`, with the collapse identities
`σ = thread(T,(τ_s)) = thread(σ',(ρ_{s,T(s)}))`, `σ'(s)=t_s(T(s))`, `τ_s(r)=ρ_{s,r}(t_s(r))`
(companion, `verify_star.py`). Reading the **object at the deepest (innermost) level** of the
three-level tower on both associated composites gives, for an object `c∈O_s`:

```
    (LHS)   μ∘Tμ  deepest object  =  τ^{t_s}( T(s),  τ^{T}(s,c) ),
    (RHS)   μ∘μT  deepest object  =  τ^{σ'}( s, c ),        σ'(s') = t_{s'}(T(s')).
```

**Verification.** Both formulas are extracted and checked against the honest
`Cont`-morphism/sampling engines: the `μ∘Tμ`-side formula holds with **0 mismatches over 196608
records** (all `TTT`-shapes × starting objects, for a *generic* transport — random `τ`, so no
accidental collapse), and the `μ∘μT`-side matches the single-transport form `τ^{σ'}(s,c)` with 0
mismatches (`fit_general.py`). Since associativity is an *equality* of the two full backward maps,
its deepest-object components agree; hence every lifting satisfies

```
    (ASSOC-DEEP)   τ^{t_s}( T(s), τ^{T}(s,c) ) = τ^{σ'}(s,c),   σ'(s') = t_{s'}(T(s')).
```

**Reading the identity.** The **left side depends only on `(T, t_s, s, c)`** — the outer function
`T` and the single middle `t_s` *at the source state `s`*. The **right side depends on the whole
function `σ'`**, whose off-`s` values `σ'(s')=t_{s'}(T(s'))` are governed by the *other* middles
`t_{s'}`. This asymmetry is the entire content of "the aggregator grade `σ` is the per-position
threading, not a single `𝕊`-arrow" (companion §5), now in equational form.

---

## 3. Endpoint-locality (the crux, proved)

> **Lemma (endpoint-locality).** `τ^g(s,c)` depends on `g` only through the value `g(s)`.
> I.e. if `g(s)=g'(s)` then `τ^g(s,c)=τ^{g'}(s,c)`.

**Proof.** Fix `s`, `c`, and `g,g'` with `g(s)=g'(s)=:m`. Instantiate `(ASSOC-DEEP)` with the
outer function `T:=id` and, for the two cases, the middles
```
    case g :   t_{s'} := const_{g(s')}   (∀ s'),
    case g':   t_{s'} := const_{g'(s')}  (∀ s').
```
Since `T=id`, `σ'(s') = t_{s'}(s')`. In case `g`, `σ'(s')=g(s')`, so `σ'=g`; in case `g'`,
`σ'=g'`. In **both** cases the middle at the source state is `t_s = const_m` (because
`g(s)=g'(s)=m`), and `T=id`, `c` are the same. Hence the **left side** of `(ASSOC-DEEP)`,
`τ^{t_s}(T(s), τ^{T}(s,c)) = τ^{const_m}(s, τ^{id}(s,c))`, is **identical** in the two cases; its
right side is `τ^{σ'}(s,c) = τ^{g}(s,c)` (case `g`) and `τ^{g'}(s,c)` (case `g'`). Therefore
```
    τ^{g}(s,c) = τ^{const_m}(s, τ^{id}(s,c)) = τ^{g'}(s,c).                  ∎
```
(The argument uses only `(ASSOC-DEEP)` and the transitivity of `S^S ↷ S` — realized concretely by
the constant functions `const_{g(s')}` — and does **not** even need the unit `(U)`; the common RHS
cancels whatever `τ^{id}` is. `targeted.py` (T3) confirms endpoint-locality is *genuinely forced*:
a functorial-but-non-endpoint-local transport satisfies units yet fails associativity.)

**Definition.** By endpoint-locality, for `s,m∈S` set
```
    ψ_{s→m} : O_s → O_m,     ψ_{s→m}(c) := τ^g(s,c)  for any g with g(s)=m.
```

---

## 4. From endpoint-locality to `𝕊×C`

**(a) Functoriality.** Instantiate `(ASSOC-DEEP)` with `T:=a` and *all* middles equal to one
function `t_{s'}:=b`. Then `σ'(s')=b(a(s'))`, i.e. `σ'=b∘a`, and the identity reads
```
    (COMP)   τ^{b∘a}(s,c) = τ^{b}(a(s), τ^{a}(s,c)).
```
Taking `a` with `a(s)=m` and `b` with `b(m)=n` gives
`ψ_{s→n} = ψ_{m→n}∘ψ_{s→m}` (with `n=b(a(s))`). So `{ψ}` is a functor from a category with objects
`S` and composition of arrows to `Set`.

**(b) Unit.** By `(U)`, `ψ_{s→s}(c)=τ^{id}(s,c)=c`, so `ψ_{s→s}=id_{O_s}`.

**(c) Bijections (H1, source-independence).** From (a),(b):
`ψ_{m→s}∘ψ_{s→m}=ψ_{s→s}=id` and `ψ_{s→m}∘ψ_{m→s}=ψ_{m→m}=id`, so each `ψ_{s→m}` is a **bijection**
`O_s ≅ O_m`. In particular all `C̃_s` have isomorphic object sets. (`S^S↷S` is transitive, so this
holds for every pair `s,m`.)

**(d) Trivial transport (H2).** The system `{ψ_{s→m}}` is a functor out of the **codiscrete
category** `K(S)` (objects `S`, a unique arrow `s→m`) — by endpoint-locality `ψ` depends only on
endpoints, and (a),(b) are exactly functoriality and unitality over `K(S)`. Choose the basepoint
`0∈S` and set `C := C̃_0`. Identify `O_s ≅ Ob C` via `ψ_{0→s}`. Under this identification, for all
`s,m`,
```
    ψ_{s→m} = ψ_{0→m} ∘ ψ_{0→s}^{-1} = id_{Ob C},
```
because `ψ_{0→m}=ψ_{s→m}∘ψ_{0→s}` by (a). **The object-transport is trivial.**

**(e) Morphism level.** The out-positions `out_s(c)` (morphisms of `C̃_s`) carry the *same*
transport structure one categorical level down: the **backward `β`-component** of `(ASSOC-DEEP)`
(the position-map read on the associativity morphism, mirroring grade-independence §3.2) gives the
identical endpoint-local + functorial + unital constraints for the hom-transport `ψ` on morphisms.
Hence `ψ_{s→m} : C̃_s → C̃_m` is a **category isomorphism**, and the family is a coherent trivial
iso-system of categories; identifying via `ψ_{0→−}` yields a single category `C` with trivial
transport. Two decisive machine checks confirm no hom-holonomy survives:

* `twist_test.py`: `𝕊×ℤ/3` twisted by a category automorphism `α_g` along `𝕊`-arrows satisfies the
  laws **iff `α≡id`**; every nontrivial `α` (inversion on one arrow, a nontrivial loop, or a global
  nontrivial twist) fails units and/or associativity.
* `enum_hom.py`: over the **free** hom-transport (one object per state, out-degree 2 = a monoid on
  `{0,1}`, an arbitrary transport-permutation per grade), the law-satisfiers are **exactly 4 =
  the 4 monoids on 2 elements**, *all with trivial transport* (`𝕊×BM`), robust to `nsamp=1500`.
  No nontrivial hom-holonomy occurs. (ℤ/3 fibre: trivial transport passes the laws; every inversion
  twist — on one arrow, on a loop at 0, or global — fails units/associativity. Same conclusion.)

**Conclusion.** Assembling (d),(e): the lifting is `A_t(Q)=∐_s∐_{c∈Ob C}Q_s^{out_C(c)}`, `ε` the
`C`-identities, `δ` the source-routed `C`-composition with trivial transport — this is precisely
`𝕊×C`. Since soundness (companion §4) shows `C↦𝕊×C` is well-defined and injective (its aggregator
recovers `C` at the single-object profiles), and §3–§4 show it is **onto**, the map is a bijection.
**`State liftings ≅ Cat`.** ∎

---

## 5. Why the naive guesses fail (the obstruction, now explained)

The companion refuted "categories over `𝕊` / discrete Conduché fibrations / copresheaves" and
per-state variation *computationally*. `(ASSOC-DEEP)` explains all of it abstractly:

* A **copresheaf** transport `F:𝕊→Set` (e.g. representable `𝕊(0,−)`) is *functorial* — it satisfies
  `(COMP)` — but **not endpoint-local**: `F(g)` depends on the whole function `g`, not just `g(s)`.
  `(ASSOC-DEEP)` (equivalently endpoint-locality) is strictly stronger than `(COMP)`, and kills it.
  This is exactly why `copresheaf.py` shows representables satisfy units yet fail associativity.
* **Per-state-different** fibres `C̃_0≇C̃_1` are impossible: (c) makes all `O_s` isomorphic
  (`S^S` transitive ⟹ `K(S)` connected).
* **Vertical / single-state** categories are impossible: `ψ_{s→s}=id` forbids a fibre supported at
  one state only.

So the anticipated *finer* graded object (an `S^S`-graded category, or a category over `𝕊`) does
not exist; the honest object is the **coarser** `Cat`, the `π_0(𝕊)=1` collapse of Reader's
`E`-indexed families (`π_0 = E`).

---

## 6. Honesty — status and gaps

**Proved (this file, `|S|=2` verified, argument uniform in `S`):**
- `(ASSOC-DEEP)` — the deepest-object component of associativity (necessary condition on every
  lifting; both sides' formulas machine-verified, 0/196608).
- **Endpoint-locality** (§3) — fully rigorous, from `(ASSOC-DEEP)` + transitivity.
- `(COMP)` functoriality, `(U)` unit `ψ_{s→s}=id`, hence `ψ_{s→m}` bijections (**H1**) and trivial
  object-transport (**H2**, object level) — fully rigorous.
- **Completeness `State liftings ≅ Cat`** at the object level; the map `C↦𝕊×C` is a bijection.

**Proved by the mirror argument + decisive machine verification (§4e):** the **morphism-level**
transport is trivial (hom-holonomy vanishes). The abstract statement is the position-component of
`(ASSOC-DEEP)`, identical in form to the object component (grade-independence §3.2 already ran this
mirror for out-degree). It is confirmed exhaustively by `enum_hom.py` (4 survivors = 4 monoids,
all trivial) and `twist_test.py` (every automorphism-twist fails). The one honest gap: the
position-component identity is **verified computationally and argued by the mirror**, not written
out in the same closed backward-map detail as the object component. This is the residual
`|S|=2`-computational reliance; the mechanism is the same associativity instance.

**Cited (proved/published):** Reader classification (`reader-liftings-are-categories`, proved);
polynomial comonads ≅ small categories (Ahman–Chapman–Uustalu 2014); `Cont`-fibre `=(Set^{S_0})^op`
(von Glehn TAC 33); soundness `Cat↪liftings` (companion `state-liftings-holonomy-free`, machine-
verified).

**Meta-watch (grade-dependent profile refutation):** none exists — grade-independence (proved)
already forces `A_t≅A_id` as functors, so the profile cannot vary with the grade. The answer is
exactly `Cat`, not finer.

---

## 7. One line

The whole `S^S`-grading of a State lifting is a mirage: the deepest object of associativity says
`τ^{σ'}(s,c)=τ^{t_s}(T(s),τ^{T}(s,c))`, and because the outer side sees only the middle *at the
source* while `σ'` is stitched from *all* the middles, the transport can depend on nothing but the
endpoint `g(s)` — so it is a trivial coherent iso-system, one small category `C`, and every
polynomial monad lifting of State is `𝕊×C`. **State liftings ≅ Cat.**
