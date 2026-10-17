# The worker/harness weld is the regular bicomodule — and why that settles Conjecture 5.1

**MacBeth — PROVE session 2026-10-16**
Decides the conjecture of `expository/2026-09-20-workers-bicomodules-pra.tex` (Conj. 5.1).
Companion computation: `scratch/2026-10-16-weld-bicomodule-verify.py` (axioms machine-checked).

---

## 0. Statement decided

Let `S, T` be sets, `ΔS = S·y^S` the store comonad (indiscrete category on `S`; costate
comonad, SGF Example 5.6). The BHM weld polynomial is `B = ΔS ◁ ΔT` (`◁` = composition product
of `Poly`); the worker grading is `A = ΔS ⊗ ΔT = Δ(S×T)`. **Conjecture 5.1** asserts three things:

1. **(existence)** `B` carries a genuine `(c,d)`-bicomodule structure for some comonoids `c,d`
   (a horizontal morphism of `Cat♯ = Comod(Poly)`, i.e. a prafunctor `c-Set → d-Set` by the
   Spivak–Garner–Fairbanks correspondence, SGF Thm 4.28 / Prop 3.9);
2. **(identification)** under the SGF slice factorization (Prop 3.6) of the represented prafunctor,
   the worker `A` is the *right-adjoint content factor* `F/1`;
3. **(tail)** the data discarded by the retract idempotent `e` (the non-constant branch maps
   `g:S→T`) is the coproduct *Σ-aggregation tail*.

**Verdict.**

| clause | verdict |
|---|---|
| (1) existence | **TRUE** — `B` is the *regular bicomodule* `(ΔT, ΔS)`; general comonoid nonsense. |
| (2) worker = content factor | **FALSE** — the content factor is the power `(−)^S`, not `A`. |
| (3) discarded = Σ-tail (branch maps) | **TRUE** — the Σ-tail is `Σ_{g∈T^S}`, indexed by the branch maps. |

In addition, **Gap 5.2** of the note (the "apparent reversal of adjointness") is **dissolved**:
the branch-map set `T^S` is the *indexing set* of a genuine left-adjoint `Σ`, not right-adjoint
exponential content, so there was never a paradox.

The honest one-line summary: **the weld is a bicomodule and the retract's discarded branch data
is exactly the SGF aggregation tail — but the worker `A` is a *different* collapse from the
bicomodule content.** State-entanglement ≠ data-aggregation.

---

## 1. Conventions (SGF 2111.10968, deep-read)

`Poly ⊂ [Set,Set]` fully faithfully: a polynomial `p = Σ_{s∈S_p} y^{p[s]}` is the functor
`p(X)=Σ_s X^{p[s]}`, and a morphism of polynomials **is** a natural transformation. The
composition product `◁` is functor composition `(p◁q)(X)=p(q(X))`, unit `y`; the Dirichlet
product `⊗` has `S_{p⊗q}=S_p×S_q`, directions `p[s]×q[t]`, unit `y`. A comonoid in `(Poly,◁,y)`
is a small category (Ahman–Uustalu; SGF Prop 5.2).

A **`(c,d)`-bicomodule** `m : c → d` (SGF Def 4.2, Leibniz order of Rmk 4.3) is `(m, λ, ρ)` with a
left `d`-coaction `λ : m → d◁m` and a right `c`-coaction `ρ : m → m◁c` satisfying

- (34) left counit `(ε_d◁m)∘λ = id`, left coassoc `(δ_d◁m)∘λ = (d◁λ)∘λ`;
- (35) right counit `(m◁ε_c)∘ρ = id`, right coassoc `(ρ◁c)∘ρ = (m◁δ_c)∘ρ`;
- (36) compatibility `(λ◁c)∘ρ = (d◁ρ)∘λ`.

By SGF Thm 4.28 / Prop 3.9, `Comod(Poly)(c,d) ≃ PRA(c-Set, d-Set)`: a bicomodule `m:c→d` *is* a
parametric right adjoint functor `c-Set → d-Set`.

The **store comonad** `ΔS` (SGF Ex 5.6) has positions `S`, directions `S` everywhere;
`δ_S(s,φ) = (s, i↦(i,φ))`, `ε_S(s,φ) = φ(s)` (store comonad on `ΔS(W)=S×W^S`). As a category it is
the **indiscrete groupoid** on `S`.

---

## 2. Clause (1): the weld is the regular bicomodule — TRUE (and general)

> **Lemma 2.1 (regular bicomodule).** For any comonoids `c = (c,ε_c,δ_c)` and `d = (d,ε_d,δ_d)` in a
> monoidal category `(V, ◁, y)`, the object `d ◁ c` is a `(c,d)`-bicomodule with
> `λ := δ_d ◁ c : d◁c → d◁d◁c = d◁(d◁c)` and `ρ := d ◁ δ_c : d◁c → d◁c◁c = (d◁c)◁c`.

*Proof.* Axioms (34)/(35): `λ` is `δ_d` whiskered on the right by `c`, so the left-counit and
left-coassoc laws are the comonoid laws `(ε_d◁d)∘δ_d=id`, `(δ_d◁d)∘δ_d=(d◁δ_d)∘δ_d` of `d`,
whiskered by `◁c`; likewise (35) is the comonoid laws of `c` whiskered by `d◁`. Axiom (36): `λ`
acts on the first (`d`) tensor factor and `ρ` on the last (`c`) factor; since `◁` is a bifunctor,
the two whiskerings commute (interchange law), and both `(λ◁c)∘ρ` and `(d◁ρ)∘λ` equal the single
map `δ_d ◁ δ_c : d◁c → d◁d◁c◁c`. ∎

Lemma 2.1 is standard (comonoid ⊗ comonoid is the regular bicomodule between them); the point is
its consequence here.

> **Theorem 2.2.** The weld `B = ΔS ◁ ΔT` carries the regular `(ΔT, ΔS)`-bicomodule structure
> (`c = ΔT`, `d = ΔS`, carrier `d◁c = ΔS◁ΔT`), with `λ = δ_{ΔS} ◁ ΔT`, `ρ = ΔS ◁ δ_{ΔT}`. Hence
> `B` is a horizontal morphism of `Cat♯`, i.e. a prafunctor `ΔT-Set → ΔS-Set`. **Conjecture 5.1
> clause (1): TRUE.**

*Proof.* Immediate from Lemma 2.1 with `c = ΔT`, `d = ΔS`; `ΔS, ΔT` are comonoids. ∎

**Machine check.** All five axioms (34 counit+coassoc, 35 counit+coassoc, 36) were verified as
equalities of natural transformations (Godement calculus on nested store-tuples) for
`(|S|,|T|) ∈ {(2,2),(2,3),(3,2),(1,2),(2,1)}` on test objects of size 2 and 3 — all `True`.

**This dissolves Gap 5.3** ("which two comonads `(c,d)`?"). The note's worry — that `ΔS◁ΔT` is a
*monoidal product* of two comonoids, not *a priori* a bicomodule *between* two fixed ones — was
unfounded: the regular-bicomodule construction turns the `◁`-product of **any** two comonoids into
a bicomodule between them. The pair is `(c,d) = (ΔT, ΔS)`.

---

## 3. The represented prafunctor

Because `ΔS` is the indiscrete groupoid on `S`, it is **equivalent (as a category) to the terminal
category `1`** (for `S ≠ ∅`: a unique iso between any two objects). Hence
`ΔS-Set ≃ Set` — a copresheaf on `ΔS` is a single set with canonical identifications, and
`lim X ≅ X(s_0) ≅ colim X` for every object `s_0`. Write `E_c : c-Set ≃ Set` for this equivalence
(`E_c⁻¹ V = ` the constant copresheaf `V`). We transport the prafunctor of `B` to an endofunctor
`F̄_B` of `Set`; right-adjointness and the SGF factorization are equivalence-invariant.

> **Theorem 3.1.** `F̄_B(V) ≅ (T × V)^S = T^S × V^S`. As a polynomial endofunctor of `Set`,
> `F̄_B = T^S · y^S` (positions `T^S`, directions `S`). Concretely
> `F̄_B(X) = { (g, h) : g : S→T, h : S→X }`.

*Proof.* The regular bicomodule `d◁c` is the composite over the unit `y` of two one-sided
comodules:
```
   ΔT  --G:=(ΔT→y)-->  y = Set  --H:=(y→ΔS)-->  ΔS ,     carrier  H◁G = ΔS◁ΔT = B,
```
where `G` is the `(ΔT,y)`-bicomodule (right `ΔT`-comodule) with carrier `ΔT` and `ρ=δ_{ΔT}`, and
`H` is the `(y,ΔS)`-bicomodule (left `ΔS`-comodule) with carrier `ΔS` and `λ=δ_{ΔS}`. Bicomodule
composition over `y` is just `◁` (no equalizer, `y` is the unit), and `H◁G = ΔS◁ΔT = B`.
Prafunctors compose, so `F_B = F_H ∘ F_G`.

- **`F_G : ΔT-Set → Set`.** As a `ΔT`-variable polynomial (SGF Prop 3.6, `Set[c]`), the right
  `ΔT`-comodule with carrier `ΔT` is `F_G(X) = Σ_{t∈T} ΔT-Set(y_t, X) = Σ_{t∈T} X(t)`, where
  `y_t = ΔT(t,−)` is the representable at `t`. In the indiscrete category `y_t` is the terminal
  copresheaf `1` (`ΔT(t,t')=1`), so `ΔT-Set(y_t,X) = lim X`. Hence `F_G(X) = Σ_{t∈T} lim X`, and
  after transport `Ḡ(V) = T × V`.
- **`F_H : Set → ΔS-Set`.** A left `ΔS`-comodule is a functor `ΔS → Poly` (SGF Prop 5.7); the
  regular one (carrier `ΔS`, `λ=δ`) assigns to each object `a∈S` the component polynomial
  `(ΔS)_a = y^S` (one position over `a`, with `S` directions — read off `δ_S`). So
  `F_H(W)(a) = (y^S)(W) = W^S` (constant copresheaf), and after transport `H̄(W) = W^S`.

Therefore `F̄_B(V) = H̄(Ḡ(V)) = (T×V)^S = T^S × V^S`, and
`(T×V)^S = \{S → T×V\} = \{(g,h) : g:S→T,\ h:S→V\}`. ∎

**Note the point of the whole problem.** `F̄_B = T^S y^S` is **neither** the underlying polynomial
of `A = (S×T)y^{S×T}` **nor** that of `B = (S·T^S)y^{S×T}`. The represented prafunctor of a
bicomodule is *not* the underlying polynomial functor of its carrier — exactly the trap the brief
flagged. (Cardinalities, machine-checked: at `|S|=|T|=2, V=2`: `F̄_B=16`, `A_under=64`,
`B_under=128`.)

---

## 4. The SGF factorization, and clauses (2),(3)

Apply SGF Prop 3.6 to `F̄_B(V) = Σ_{g∈T^S} V^S`:

- `F̄_B(1) = T^S`.
- **content** `F̄_B/1 : Set → Set^{T^S}`, `V ↦ (V^S)_{g∈T^S} = Δ_{T^S} ∘ (−)^S`. Both the power
  `(−)^S` and the diagonal `Δ_{T^S}` are right adjoints, so `F̄_B/1` is a right adjoint. The genuine
  connected-limit content is the **power `(−)^S`** (SGF: "represented by the value of the
  corresponding left adjoint at 1", here `y^S`).
- **Σ-tail** `Σ : Set^{T^S} → Set`, the coproduct over `T^S = {g : S→T}`.

> **Theorem 4.1 (clause (2): FALSE).** The right-adjoint content factor of the weld prafunctor is
> the power `(−)^S`, not the worker `A`. Indeed `A = Δ(S×T)` has represented functor
> `V ↦ V^{S×T}` (exponent `S×T`), and the content has exponent `S`; these differ whenever
> `|T| ≥ 2`. No handedness convention repairs this: the opposite reading gives content `(−)^T`,
> still a power, never `A`.

*Proof.* Content exponent is `S` (directions of `F̄_B = T^S y^S`); `A`'s represented functor has
exponent `S×T` by the same computation as Theorem 3.1 applied to `A = Δ(S×T)` (`Ā(V)=V^{S×T}`). For
`|T|≥2`, `|S| < |S×T|`, so the functors differ on any `V≥2`. ∎

> **Theorem 4.2 (clause (3): TRUE).** The SGF Σ-aggregation tail is the coproduct `Σ_{g∈T^S}`
> indexed by the full branch-map set `T^S = {g:S→T}` — precisely the "non-constant branch maps"
> the retract idempotent `e` of the workers theorem forgets.

*Proof.* The tail index is `F̄_B(1) = T^S` by Theorem 3.1; `T^S = Hom(S,T)` is the set of branch
maps, and `e(s,g) = (s, const_{g(s)})` collapses each `g` to a constant, forgetting exactly the
non-constant elements of `T^S`. ∎

> **Theorem 4.3 (Gap 5.2 dissolved).** There is no adjointness reversal. The branch maps `T^S`
> appear as the *indexing set* of the left-adjoint coproduct `Σ_{T^S}`, not as right-adjoint
> exponential content. "`T^S` is an exponential object" is a statement about the *set*, not about
> the adjointness of `Σ_{T^S} : Set^{T^S}→Set`, which is left adjoint to the diagonal. The genuinely
> right-adjoint (exponential/connected-limit) content `(−)^S` is **kept** in `F/1`, exactly as SGF
> predicts.

*Proof.* `Σ_{T^S} ⊣ Δ_{T^S}` so `Σ_{T^S}` is a left adjoint for any index set, exponential or not;
`(−)^S ⊣ ... ` — `(−)^S` is right adjoint to the copower `S×(−)`, hence connected-limit-preserving
content. The note's Gap 5.2 conflated the two. ∎

---

## 5. The precise role of the worker (remark)

The worker `A` is not the content, but it has an exact location inside the weld prafunctor. The
section `σ : A → B`, `σ_1(s,t) = (s, const_t)`, embeds `A`'s `T`-coordinate as the **constant**
branch maps `T ↪ T^S`. In the factorization of `F̄_B`, the current input state `S` lives in the
content exponent and the branch map lives in the Σ-tail index `T^S`; so

> `A`'s positions `S × T` = (content-input `S`) × (**constant-branch slice** `T ⊆ T^S` of the
> Σ-tail index).

The worker is the constant/diagonal slice of the *aggregation tail* — a statement about `Σ`, not
about `F/1`. This sharpens, rather than rescues, the negative: entanglement selects constant
branches; it does not supply the bicomodule content.

---

## 6. Grant relevance

The weld now has a precise home in `Poly`: it **is** a data-migration prafunctor
`ΔT-Set → ΔS-Set`, `X ↦ (T×X)^S` — "read the whole input state `S`; return, for each input, an
output token in `T` and a value in `X`," with the branch-map choice aggregated by `Σ`. This places
the *state axis* of the compositional-correctness program inside the same framed bicategory `Cat♯`
that houses the directed (retrofunctor) axis — the positive deliverable the note hoped for. But the
identification "worker = PRA content" is false: state-entanglement (`A`) and data-aggregation (the
`Σ`-tail) are genuinely different collapses, and the agent-orchestration weld semantics must keep
them distinct.

---

## 7. Gaps / honesty

- Lemma 2.1 is standard category theory; the contribution is clauses (2)/(3) and the explicit
  `F̄_B = (T×V)^S` with its factorization, plus dissolving Gap 5.2.
- Theorem 3.1 uses the two single-sided represented-functor formulas (`F_G`, `F_H`); these are the
  SGF `Set[c]`/`Prop 5.7` dictionaries applied to the indiscrete case, where `c-Set ≃ Set`,
  representables are terminal, and component polynomials are `y^S`. Each step is elementary but was
  *derived*, not re-brute-forced from the bicomodule-composition equalizer; the axiom check
  (§2) and the cardinality check (§3) are the computational corroboration.
- No claim beyond the three clauses + Gap 5.2 is made.
