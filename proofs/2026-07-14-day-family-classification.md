# The Day family on Poly: classification, the unique pointwise member, and the comparitor as a coreflection

MacBeth — 2026-07-14. Deep-work session.

**Status.** Three theorems, all proved; computationally verified (§8), including a negative
control that gives the coherence check teeth. Two things deliberately **not** claimed:
symmetry of `∨_S` (Remark 5.2.1 — hexagon unverified, and I decline to assume it) and the
naturality-free form of Theorem B (Question 5.6 — a precisely stated open gap). Neither is
load-bearing.

A novelty audit against the seed is at §7, and it is bracing: the *existence* of the Day
family, the formula, `× = Day(+)`, `⊗ = Day(×)`, the `∨_S` family, **and the comparitor
`⊗ → ◁` itself** are all prior art — the comparitor six times over. What is new is the
**classification** (the literature has only the existence direction), the **uniqueness of the
pointwise member**, and the **universal property of the comparitor**.

---

## 0. Conventions

Fix a Grothendieck universe; "set" means small set. `Cont` is the category of containers:
an object is a pair `(S, P)` with `S` a set and `P : S → Set`; a morphism `(S,P) → (T,Q)`
is a pair `(f, g)` with `f : S → T` and `g : Π s. Q(f s) → P s`. Write `S_p := p(1)` for
the shapes of `p` and `p[s]` for its positions at `s`.

The **extension** is `⟦p⟧ X = Σ_{s ∈ S_p} X^{p[s]}`; it is fully faithful into `[Set, Set]`
(Abbott–Altenkirch–Ghani), and it identifies `Cont` with the category `Poly` of polynomial
functors. I use `Cont` and `Poly` interchangeably and write `p = Σ_{s} y^{p[s]}`.

`p` is **representable** if it has exactly one shape, i.e. `p ≅ y^A` with `⟦y^A⟧X = X^A`.
Write `y := y^1`, `1 := y^∅` (the terminal object), `0` for the empty container.
`p` is **linear** if every `p[s]` is a singleton, i.e. `p ≅ A · y`.

The four monoidal structures at issue:

| | shapes of `p ⊙ q` | positions at that shape | unit |
|---|---|---|---|
| product `×` | `S_p × S_q` | `p[s] + q[t]` | `1 = y^∅` |
| Dirichlet `⊗` | `S_p × S_q` | `p[s] × q[t]` | `y = y^1` |
| coproduct `+` | `S_p + S_q` | inherited | `0` |
| sequential `◁` | `Σ_{s ∈ S_p} (p[s] → S_q)` | `Σ_{i ∈ p[s]} q[f i]` at `(s,f)` | `y` |

`⟦p ◁ q⟧ = ⟦p⟧ ∘ ⟦q⟧`, `⟦p × q⟧ = ⟦p⟧ × ⟦q⟧`, `⟦p + q⟧ = ⟦p⟧ + ⟦q⟧` (pointwise).
There is **no** pointwise description of `⟦p ⊗ q⟧`. That fact is the seed of this note.

---

## 1. Poly is the free coproduct completion of Set^op

This is the only structural input, and it makes everything else mechanical.

**Lemma 1.1.** `y^{(−)} : Set^op → Cont`, `A ↦ y^A`, is fully faithful.

*Proof.* A morphism `y^A → y^B` is a pair (`f : 1 → 1`, `g : B → A`); `f` is forced, so
`Cont(y^A, y^B) ≅ Set(B, A) = Set^op(A, B)`, naturally. ∎

**Lemma 1.2.** `Cont ≅ Fam(Set^op)`, the free coproduct completion of `Set^op`, with
`y^{(−)}` as the universal embedding.

*Proof.* `Fam(C)` has objects: families `(A_i)_{i ∈ I}` of objects of `C`; morphisms
`(A_i)_I → (B_j)_J`: a function `u : I → J` together with morphisms `A_i → B_{u i}` in `C`.
Take `C = Set^op`. An object is a set `I` together with `I`-indexed sets `A_i` — that is
exactly a container `(I, i ↦ A_i)`. A morphism is `u : I → J` together with `Set^op`-maps
`A_i → B_{u i}`, i.e. `Set`-maps `B_{u i} → A_i` — exactly a container morphism. This is an
isomorphism of categories, not merely an equivalence. ∎

*(Prior art: Spivak–Garner–Fairbanks, Functorial Aggregation, Prop. 3.6, in the generalized
form `Set[c] ≃ Fam((c-Set)^op)`; Kondyrev–Spivak, eq. (5), `Poly ≃ Set[{y}]`. I record the
elementary proof because I use the universal property explicitly and repeatedly.)*

**Lemma 1.3 (universal property).** Let `E` have small coproducts. Restriction along
`y^{(−)}` is an equivalence
```
    Fun_⊔(Cont, E)  ≃  Fun(Set^op, E),
```
where `Fun_⊔` denotes coproduct-preserving functors. The inverse sends `G` to
`Ĝ(p) = Σ_{s ∈ S_p} G(p[s])`. More generally, for each `n ≥ 1`, restriction is an
equivalence
```
    Fun_{⊔,…,⊔}(Cont^n, E)  ≃  Fun((Set^op)^n, E)
```
between functors preserving coproducts **separately in each of the `n` variables** and
arbitrary `n`-ary functors on `Set^op`.

*Proof.* The `n = 1` case is the universal property of `Fam` (Lemma 1.2). For `n = 2`:
`Fun_⊔(Cont, E)` has small coproducts, computed pointwise. Currying, a bifunctor
`Cont × Cont → E` preserving coproducts in the second variable is a functor
`Cont → Fun_⊔(Cont, E)`; it additionally preserves coproducts in the first variable iff
that functor is coproduct-preserving. Hence
```
Fun_{⊔,⊔}(Cont², E) ≃ Fun_⊔(Cont, Fun_⊔(Cont, E)) ≃ Fun(Set^op, Fun_⊔(Cont, E))
                    ≃ Fun(Set^op, Fun(Set^op, E)) ≃ Fun((Set^op)², E),
```
each step by the `n = 1` case. Induct for general `n`. ∎

> **Consequence I will use without comment.** A functor `Cont^n → Cont` preserving
> coproducts in each variable is *determined up to canonical isomorphism* by its restriction
> to representables — and so are the natural transformations between two such. Equations
> between such natural transformations (pentagon, triangle, …) hold iff they hold on
> representables.

**Remark 1.4 (the size worry dissolves).** The usual definition of Day convolution on Poly
(Niu–Spivak (3.80)) is a coend over `Set²`, which is large. I never form a coend: Lemma 1.3
is a *freeness* statement, and the extension it produces is a coproduct indexed by `S_p × S_q`,
which is small. Nothing in this note needs the coend to exist; co-Yoneda (Niu–Spivak (3.81))
says the two agree when it does.

---

## 2. The Day family, explicitly

**Definition 2.1.** Let `(⋆, I)` be a monoidal structure on `Set`. Define on `Cont`:
```
    p ⊙_⋆ q  :=  ( S_p × S_q ,  (s,t) ↦ p[s] ⋆ q[t] )        J_⋆ := y^I.
```
Equivalently `p ⊙_⋆ q = Σ_{(s,t)} y^{p[s] ⋆ q[t]}`.

**Proposition 2.2.** `(⊙_⋆, J_⋆)` is a monoidal structure on `Cont`; it preserves coproducts
in each variable; and it sends representables to representables, `y^A ⊙_⋆ y^B = y^{A ⋆ B}`.
It is the Day convolution of `(⋆, I)`.

*Proof.* Functoriality and the coherence data are inherited componentwise from `⋆`: the
associator of `⊙_⋆` at `(p,q,r)` has identity shape-component (both sides have shapes
`S_p × S_q × S_r`) and position-component the associator `α_{p[s], q[t], r[u]}` of `⋆`
(reversed, positions being contravariant). Pentagon and triangle hold shapewise because
they hold in `Set`. Coproduct preservation in each variable: `S_p × (−)` preserves
coproducts of sets, including the empty one. Representables: immediate. The identification
with Day convolution is Niu–Spivak, Prop. 3.79 and eq. (3.81) — **cited, not mine**. ∎

**Example 2.3 (Niu–Spivak, Prop. 3.79 ¶2 — cited).**
`⊙_{(+,∅)} = ×` (the categorical product) and `⊙_{(×,1)} = ⊗` (the Dirichlet tensor).

**Lemma 2.4 (every Day tensor annihilates 0).** `p ⊙_⋆ 0 ≅ 0 ≅ 0 ⊙_⋆ p`.

*Proof.* `S_p × ∅ = ∅`. ∎

This trivial lemma is already enough to expel the coproduct from the family (§4).

---

## 3. Theorem A — the classification

**Definition 3.1.** A monoidal structure `(⊙, J)` on `Cont` is **convolutional** if

* **(D1)** `⊙` preserves coproducts in each variable (including the empty coproduct: `p ⊙ 0 ≅ 0`);
* **(D2)** the representables are closed under `⊙`.

**Lemma 3.2 (the unit comes for free).** (D1) and (D2) force `J` to be representable.

*Proof.* Decompose the unit canonically, `J = Σ_{t ∈ S_J} y^{J[t]}`. By (D1),
```
    y^A  ≅  J ⊙ y^A  =  Σ_{t ∈ S_J} ( y^{J[t]} ⊙ y^A ),
```
and by (D2) each summand `y^{J[t]} ⊙ y^A` has exactly one shape. So the right-hand side has
exactly `|S_J|` shapes while the left has one. Hence `|S_J| = 1`. ∎

So "convolutional" is a condition on the *tensor* alone; the unit has no choice in the
matter. (I had originally built representability of `J` into (D2). It is a consequence.)

**Theorem A.** The assignment `(⋆, I) ↦ (⊙_⋆, y^I)` is an **equivalence**
```
   { monoidal structures on Set }  ≃  { convolutional monoidal structures on Cont }
```
(both sides taken with monoidal isomorphisms over the identity functor as morphisms). In
particular every convolutional monoidal structure on `Cont` is a Day convolution, and the
monoidal structure on `Set` inducing it is unique up to monoidal isomorphism.

*Proof.*

**Well-defined.** Proposition 2.2.

**Essentially surjective.** Let `(⊙, J)` be convolutional. By (D2) the full subcategory of
representables is closed under `⊙`, and by Lemma 3.2 it contains `J`; by Lemma 1.1 it is
`Set^op`. To define
`⋆` I need a *canonical* choice, not merely "is isomorphic to some `y^C`": by (D2) the
container `y^A ⊙ y^B` has exactly one shape, so put
```
    A ⋆ B  :=  (y^A ⊙ y^B)[∗],     the position set at that unique shape,
```
and then `y^A ⊙ y^B = y^{A ⋆ B}` on the nose. Likewise `I := J[∗]`, so `J = y^I`.
Functoriality of `⋆` follows from that of `⊙` together with full faithfulness of `y^{(−)}`
(Lemma 1.1). The associator and
unitors of `⊙`, evaluated at representables, are isomorphisms between representables, hence
(Lemma 1.1) come from isomorphisms in `Set^op`; pentagon and triangle for these are the
pentagon and triangle of `⊙` at representables. So `(Set^op, ⋆, I)` is monoidal, i.e.
`(Set, ⋆, I)` is monoidal (a monoidal structure on `C` and on `C^op` are the same data, with
the coherence isomorphisms inverted).

Now `⊙` and `⊙_⋆` are both bifunctors `Cont² → Cont` preserving coproducts in each variable
— `⊙` by (D1), `⊙_⋆` by Prop. 2.2 — and they agree on representables by construction. By
Lemma 1.3 (`n = 2`) they are canonically isomorphic. By Lemma 1.3 (`n = 3`) their
associators agree under that isomorphism, since both are natural transformations between
coproduct-preserving-in-each-variable functors `Cont³ → Cont` restricting to the same thing
on representables; likewise the unitors (`n = 1`). Hence the isomorphism `⊙ ≅ ⊙_⋆` is
monoidal.

**Fully faithful.** A monoidal isomorphism `φ : ⊙_⋆ ≅ ⊙_{⋆'}` over `id_Cont` restricts at
representables to `y^{A ⋆ B} ≅ y^{A ⋆' B}`, hence (Lemma 1.1) to a natural isomorphism
`⋆ ≅ ⋆'`, monoidal because `φ` is. Conversely a monoidal isomorphism `⋆ ≅ ⋆'` extends by
Lemma 1.3. The two operations are mutually inverse: restriction after extension is the
identity on the nose; extension after restriction is the identity by the uniqueness half of
Lemma 1.3. ∎

**Remark 3.3.** (D1) and (D2) are exactly the two things Lemma 1.3 needs: (D1) says the
tensor is determined by its restriction to representables; (D2) says that restriction lands
in `Set^op` rather than merely in `Cont`. Drop (D2) and one gets not a monoidal structure on
`Set` but a *promonoidal-style* structure valued in `Cont`; that is a strictly larger family
and I do not classify it here.

---

## 4. Theorem B — the product is the unique pointwise member

**Definition 4.1.** A monoidal structure `⊙` on `Cont` is **pointwise** if there is an
isomorphism `θ_{p,q} : p ⊙ q ≅ p × q`, natural in `p` and `q`.

Because `⟦−⟧` is fully faithful and `⟦p × q⟧ = ⟦p⟧ × ⟦q⟧`, this says exactly that there is
an isomorphism `⟦p ⊙ q⟧X ≅ ⟦p⟧X × ⟦q⟧X` natural in `p, q, X` — i.e. that
`⟦−⟧ : (Cont, ⊙) → ([Set,Set], ×_pointwise)` is strong monoidal.

### 4.1 The unit already decides it — sometimes

**Proposition 4.2.** If `⊙` is pointwise then its unit is `1 = y^∅`, the terminal container.

*Proof.* Naturality gives `⟦J⟧X × ⟦p⟧X ≅ ⟦J ⊙ p⟧X ≅ ⟦p⟧X` for all `p, X`. Take `p = y`, so
`⟦p⟧X = X`: then `⟦J⟧X × X ≅ X` for all `X`. At `X = 2` this forces `|⟦J⟧2| = 1`. Writing
`⟦J⟧2 = Σ_{s ∈ S_J} 2^{J[s]}`, a sum of positive cardinals equal to 1 forces `|S_J| = 1` and
`2^{|J[*]|} = 1`, i.e. `J[*] = ∅`. So `J = y^∅ = 1`. ∎

**Corollary 4.3.** The Dirichlet tensor is not pointwise: its unit is `y ≠ 1`.

That is a one-line proof of a fact I had previously only witnessed by the example
`y³ ⊗ y³ = y⁹ ≠ y⁶`. But the unit is a *blunt* instrument — see §5, where a proper class of
non-pointwise Day tensors all share the product's unit.

### 4.2 The rigidity of the coproduct

**Lemma 4.4 (rigidity).** Let `α : (A+B)+C ⇒ A+(B+C)` be any natural transformation of
functors `Set³ → Set`. Then `α` is the canonical associator. Likewise the only natural
`∅ + A ⇒ A` and `A + ∅ ⇒ A` are the canonical unitors. Consequently `(+, ∅)` admits exactly
one monoidal structure on `Set`, and its coherence data are forced before coherence is even
imposed.

*Proof.* A map out of `(A+B)+C` is precisely its three components on `A`, `B`, `C`.

*The `A`-component.* It is a family `u_{A,B,C} : A → A+B+C` natural in all three variables.
Naturality in `B` and `C` along the unique maps `!_B : ∅ → B`, `!_C : ∅ → C` gives
```
        A  --u_{A,∅,∅}-->  A + ∅ + ∅
        |  id_A                     |  id_A + !_B + !_C
        A  --u_{A,B,C}-->  A + B + C
```
so `u_{A,B,C} = (id_A + !_B + !_C) ∘ u_{A,∅,∅}`. Now `A + ∅ + ∅ ≅ A` canonically and
naturally, so `u_{A,∅,∅}` is a natural endomorphism of `Id_Set`. The only one is the
identity: for `a ∈ A`, name it as `ā : 1 → A`; naturality against `ā` gives
`η_A(a) = η_A(ā(∗)) = ā(η_1(∗)) = a`, since `η_1 : 1 → 1` is the identity. Hence
`u_{A,B,C} = inl`.

*The `B`-component.* A family `v_{A,B,C} : B → A+B+C`. Setting `A = C = ∅` and running the
same argument gives `v_{∅,B,∅} : B → ∅+B+∅ ≅ B` equal to the canonical isomorphism; then
naturality in `A` and `C` along `∅ → A`, `∅ → C` gives `v_{A,B,C}` = the middle injection.
Symmetrically for `C`. So `α` is the canonical associator.

*Unitors.* A natural `λ_A : ∅ + A → A` has an `∅`-component (unique) and an `A`-component,
a natural endo of `Id_Set`, hence the identity. So `λ` is canonical. ∎

### 4.3 The theorem

**Theorem B.** For a monoidal structure `(⋆, I)` on `Set`, the following are equivalent:

1. `⊙_⋆` is pointwise;
2. `⋆ ≅ +` as bifunctors `Set × Set → Set`;
3. `(⋆, I) ≅ (+, ∅)` as monoidal structures on `Set`;
4. `⊙_⋆ ≅ ×` as monoidal structures on `Cont`.

Hence **the cartesian structure is the unique pointwise member of the Day family**, and by
Theorem A the unique pointwise convolutional monoidal structure on `Cont`.

*Proof.*

**(1) ⟹ (2).** Restrict the natural isomorphism `θ` to representables. By Prop. 2.2,
`y^A ⊙_⋆ y^B = y^{A ⋆ B}`; and `y^A × y^B = y^{A + B}` (shapes `1 × 1`, positions `A + B`).
So `θ` gives an isomorphism `y^{A ⋆ B} ≅ y^{A + B}` natural in `A, B ∈ Set^op`. The two
functors are `y^{F}` and `y^{G}` for `F = ⋆` and `G = +` viewed as functors
`(Set^op)² → Set^op`; since `y^{(−)}` is fully faithful (Lemma 1.1), the isomorphism comes
from a natural isomorphism `F ≅ G` in `[(Set^op)², Set^op]`, and taking opposites,
`⋆ ≅ +` in `[Set², Set]`.

**(2) ⟹ (3).** Let `φ : ⋆ ≅ +` be a natural isomorphism of bifunctors. The left unitor of
`⋆` gives `I ⋆ A ≅ A`; composing with `φ` gives `I + A ≅ A` for every set `A`. At `A = 1`:
`|I| + 1 = 1`, so `I = ∅`. Now transport the monoidal structure `(⋆, I, α, λ, ρ)` along the
isomorphisms `φ : ⋆ ≅ +` and `I ≅ ∅`: the result is a monoidal structure on `Set` whose
tensor is literally `+`, whose unit is literally `∅`, and whose coherence data `α', λ', ρ'`
are natural. By Lemma 4.4, `α' , λ', ρ'` are the canonical ones. So the transported
structure *is* `(+, ∅)`, i.e. `(φ, I ≅ ∅)` is a monoidal isomorphism `(⋆, I) ≅ (+, ∅)`.

**(3) ⟹ (4).** Theorem A (fully faithful half): a monoidal isomorphism `(⋆,I) ≅ (+,∅)`
extends to a monoidal isomorphism `⊙_⋆ ≅ ⊙_{(+,∅)} = ×` (Example 2.3).

**(4) ⟹ (1).** A monoidal isomorphism is in particular a natural isomorphism. ∎

### 4.3a The Day hypothesis is not needed

**Theorem B⁺.** Let `(⊙, J)` be **any** monoidal structure on `Cont`. Then `⊙` is pointwise
if and only if `(⊙, J) ≅ (×, 1)`, the cartesian structure. That is: **the categorical product
is the unique pointwise monoidal structure on `Cont`** — no convolutional hypothesis
required.

*Proof.* (⇐) is trivial. (⇒) Pointwise says `⊙ ≅ ×` as *bifunctors* `Cont² → Cont`. Both
conditions (D1) and (D2) are properties of the bifunctor alone and are invariant under
natural isomorphism of bifunctors; `×` satisfies both — (D1) because `Cont` is distributive
(`(p+q) × r ≅ p×r + q×r` and `0 × r ≅ 0`, immediate from the shape formula `S_p × S_q`), and
(D2) because `y^A × y^B = y^{A+B}`. Hence `⊙` satisfies (D1) and (D2), i.e. `(⊙, J)` is
convolutional. By Theorem A, `(⊙, J) ≅ (⊙_⋆, y^I)` monoidally for some monoidal `(⋆, I)` on
`Set`. Then `⊙_⋆` is pointwise, so by Theorem B `⊙_⋆ ≅ ×` monoidally, and therefore
`⊙ ≅ ×` monoidally. ∎

So pointwise-ness is not a condition one imposes *within* the Day family and then discovers
is rare; it is a condition on monoidal structures on `Cont` at large, and it is *categorical*
— it holds for the product and nothing else. The Day family is simply where one can *see*
this, because Theorem A makes the family surveyable.

**Corollary 4.5 (why the strictness dead end was forced).** `⟦−⟧ : (Cont, ⊙) →
([Set,Set], ×)` is strong monoidal iff `⊙` is the cartesian structure. In particular no
reformulation of `⊗` could ever have made `⟦−⟧` monoidal into the pointwise product.
*(This retro-explains the `dirichlet-strict-monoidal` dead end: the failure was structural,
not a bookkeeping error. There was no version of that claim that could have been true.)*

### 4.4 An effective test

**Definition 4.6.** Let `(⋆, I)` be monoidal on `Set` with `I ≅ ∅` (i.e. the unit is
initial). The **comparison map** `κ_{A,B} : A + B → A ⋆ B` is the copairing of
```
    A ≅ A ⋆ ∅  --(A ⋆ !_B)-->  A ⋆ B      and      B ≅ ∅ ⋆ B  --(!_A ⋆ B)-->  A ⋆ B,
```
using the unitors and functoriality of `⋆` along `! : ∅ → X`. It is natural in `A, B`.

**Theorem B′ (test form).** `⊙_⋆` is pointwise **iff** `I ≅ ∅` and `κ_{A,B}` is a bijection
for all `A, B`.

*Proof.* (⇐) `κ` is a natural isomorphism `+ ≅ ⋆`, so Theorem B(2) applies.

(⇒) Suppose `⊙_⋆` is pointwise. Then `I ≅ ∅` (Prop. 4.2 plus `J_⋆ = y^I`), so `κ^⋆` is
defined; and by Theorem B there is a *monoidal* natural isomorphism
`(φ, ι) : (⋆, I) → (+, ∅)`. I claim `φ ∘ κ^⋆ = id_{A+B}`, whence `κ^⋆ = φ^{-1}` is a
bijection.

It suffices to check the two components. On the `A`-summand, `κ^⋆|_A` is
`A --(ρ^⋆)^{-1}--> A ⋆ I --(A ⋆ !_B)--> A ⋆ B` (using `I ≅ ∅` to get `!_B : I → B`). Now:

* naturality of `φ` in the second variable gives `φ_{A,B} ∘ (A ⋆ !_B) = (A + !_B) ∘ φ_{A,I}`;
* monoidality of `(φ, ι)` — compatibility with the right unitors — gives
  `φ_{A,I} ∘ (ρ^⋆)^{-1} = (ρ^{+})^{-1}` modulo `ι`, i.e. the canonical `A ≅ A + ∅`.

Composing, `φ_{A,B} ∘ κ^⋆|_A = (A + !_B) ∘ (A ≅ A + ∅) = inl`. Symmetrically (using the left
unitor) `φ_{A,B} ∘ κ^⋆|_B = inr`. So `φ ∘ κ^⋆ = [inl, inr] = id`. ∎

*(The content of the check: `κ` is built out of unitors and functoriality only, so any
monoidal isomorphism carries `κ^⋆` to `κ^{+}`, and `κ^{+}` is visibly the identity.)*

This is what makes Theorem B *usable*: `κ` is computable from the definition of `⋆`, and
pointwise-ness is decided by inspecting it. §5 runs the test on a proper class.

---

## 5. The family is a proper class, and the unit sees nothing

**Definition 5.1 (Spivak, *Reference*, eq. (9) — cited; he credits R. Garner, and notes it
is Haskell's `These`).** For a set `S`, define on `Set`:
```
    A ∨_S B  :=  A + (A × S × B) + B,        unit  ∅.
```
Spivak asserts this is monoidal; Niu–Spivak Exercise 3.82 asks the reader to verify the
`S = 1` case. I give the proof, because I need coherence and not merely associativity.

**Proposition 5.2.** `(∨_S, ∅)` is a monoidal structure on `Set`, and `∨_∅ ≅ +`.

*Proof (coherence by normal form).* For `n ≥ 1` define
```
    N(X_1, …, X_n)  :=  ⊔_{∅ ≠ K ⊆ [n]}  ( Π_{i ∈ K} X_i ) × S^{|K| − 1}.
```
Read an element as a **word**: choose a nonempty `K = {i_1 < ⋯ < i_k} ⊆ [n]`, a letter
`x_{i_j} ∈ X_{i_j}` for each, and a separator `s_j ∈ S` between each *consecutive pair* —
```
    x_{i_1} · s_1 · x_{i_2} · s_2 ⋯ s_{k−1} · x_{i_k} .
```
`N` is functorial in each `X_i`. For `n = 1`, `N(A) = A`; for `n = 2`,
`N(A,B) = A ⊔ (A × S × B) ⊔ B = A ∨_S B`, the three subsets being `{1}, {1,2}, {2}`.

**Step 1 (splitting).** For each `1 ≤ m < n` there is a bijection, natural in all `X_i`,
```
    c_m : N(X_1,…,X_m)  ∨_S  N(X_{m+1},…,X_n)  ⟶  N(X_1,…,X_n),
```
given by concatenation. Unfolding the left-hand side, it is
`N(X_{≤m}) ⊔ ( N(X_{≤m}) × S × N(X_{>m}) ) ⊔ N(X_{>m})`. Every word `w` of `N(X_1,…,X_n)`
falls into exactly one of three cases: `supp(w) ⊆ [1,m]`; `supp(w) ⊆ [m+1,n]`; or `supp(w)`
meets both. In the third case `w` has a **unique** separator straddling the cut `m | m+1`
(the separators sit between *consecutive* chosen indices, and exactly one such pair crosses
the cut), so `w` decomposes uniquely as `w_≤ · s · w_>`. That is precisely the middle
summand. So `c_m` is a natural bijection, with inverse "cut at the straddling separator".

**Step 2 (canonical map from every bracketing).** For a binary bracketing `β` of `X_1,…,X_n`
define `can_β : β(X_1,…,X_n) → N(X_1,…,X_n)` by induction: `can_{(1)} = id`, and if `β`
splits at `m` into `β_1` on `X_{≤m}` and `β_2` on `X_{>m}`, set
```
    can_β  :=  c_m ∘ ( can_{β_1} ∨_S can_{β_2} ).
```
Each `can_β` is a natural bijection (composite of bijections; `∨_S` preserves bijections).

**Step 3 (define the associator, and check whiskering).** Define
`α_{A,B,C} := can_{A∨(B∨C)}^{-1} ∘ can_{(A∨B)∨C}`. Both bracketings are over `N(A,B,C)`, so
this is a natural bijection. More generally, define the associator instance at *any* node of
*any* bracketing the same way. The key point is that this is consistent with whiskering: if
`γ : β_2 → β_2'` is `can_{β_2'}^{-1} ∘ can_{β_2}`, then
```
    can_{(β_1, β_2')} ∘ (id ∨_S γ)  =  c_m ∘ ( can_{β_1} ∨_S ( can_{β_2'} ∘ γ ) )
                                    =  c_m ∘ ( can_{β_1} ∨_S can_{β_2} )  =  can_{(β_1, β_2)},
```
using functoriality of `∨_S` and `can_{β_2'} ∘ γ = can_{β_2}`. Symmetrically for `γ ∨_S id`.

**Step 4 (coherence).** By Step 3, **every** morphism built by composing and whiskering
associators, from a bracketing `β` to a bracketing `β'`, equals `can_{β'}^{-1} ∘ can_β`.
(Induct on the composite: each generating move is `can^{-1} ∘ can` by definition, whiskering
preserves this by Step 3, and the composites telescope.) Hence **any two** such morphisms
`β → β'` are equal. The pentagon is exactly such a pair of morphisms
`((A∨B)∨C)∨D → A∨(B∨(C∨D))`, so it commutes. This is Mac Lane's coherence-by-normal-form,
and it proves the pentagon rather than assuming it.

**Step 5 (unitors and the triangle).** `∅ ∨_S B = ∅ + (∅ × S × B) + B ≅ B` and symmetrically;
these are the unitors. Substituting `X_i = ∅` into `N` deletes every word whose support
contains `i` (the factor `Π_{j∈K} X_j` is empty whenever `i ∈ K`), leaving exactly
`N` of the remaining arguments — so the unitors are also `can`-compatible, and the triangle
commutes by the Step 4 argument.

Finally `∨_∅` has `A × ∅ × B = ∅`, so `A ∨_∅ B = A + ∅ + B ≅ A + B`. ∎

**Remark 5.2.1 (I do NOT claim `∨_S` is symmetric).** There is an evident candidate braiding
(`A ⊔ (A×S×B) ⊔ B → B ⊔ (B×S×A) ⊔ A`, swapping the outer summands and sending `(a,s,b) ↦
(b,s,a)`), and Spivak's `⊙` construction is stated for *symmetric* monoidal structures on
`Set`. But I have **not** verified the hexagon, and I decline to assume it. The reason is
specific, not fastidious: a braiding must permute the arguments, and a permutation reorders
which pairs of chosen indices are *consecutive* — so it must re-match the `S`-separators, and
**re-matching separators is exactly where coherence fails**. The negative control in §8
exhibits a natural, associative bijection that differs from the true associator only by
swapping separator labels, and it **fails the pentagon**. So the separator bookkeeping is
load-bearing, and an unchecked hexagon is not a safe assumption. *Nothing below needs
symmetry* — Corollary 5.5 needs only that each `∨_S` be monoidal and that they be pairwise
non-isomorphic.

**Definition 5.3 (Spivak, *Reference*, eq. (12) — cited).**
`p ▷_S q := ⊙_{∨_S}(p, q) = Σ_{(s,t)} y^{p[s] ∨_S q[t]}`.

**Theorem 5.4.** For every set `S`, `▷_S` is a convolutional monoidal
structure on `Cont` with unit `y^∅ = 1`, the **terminal object** — the same unit as the
categorical product. The `▷_S` are pairwise non-isomorphic. And
```
    ▷_S  is pointwise   ⟺   S = ∅   ⟺   ▷_S = ×.
```

*Proof.* Convolutional and unit `y^∅`: Prop. 2.2 and 5.2. Pairwise non-isomorphic: by
Theorem A it suffices that the `∨_S` be pairwise non-isomorphic, and
`|1 ∨_S 1| = 1 + |S| + 1 = |S| + 2` separates them. Pointwise: apply Theorem B′. The unit is
already initial, and
```
    κ_{A,B} : A + B  ↪  A + (A × S × B) + B
```
is the inclusion of the two outer summands (compute: `A ≅ A ∨_S ∅` is the first summand, and
functoriality along `∅ → B` includes it into the first summand of `A ∨_S B`; symmetrically
for `B`). So `κ` is a bijection iff `A × S × B = ∅` for all `A, B` iff `S = ∅`. And
`▷_∅ = ⊙_{∨_∅} = ⊙_{+} = ×` by Prop. 5.2 and Example 2.3. ∎

**Corollary 5.5 (the sharp form of "unique").** `Cont` carries a **proper class** of pairwise
non-isomorphic convolutional monoidal structures **all of which have the terminal
object as unit** — and exactly one of them, the case `S = ∅`, is the categorical product.

So the product is *not* singled out among Day tensors by its unit, nor by
coproduct-preservation, nor by semicartesianness (unit terminal — every `▷_S` is
semicartesian). The property that singles it out is precisely pointwise-ness, and Theorem B′
is what detects it. This is the answer to PROVE.md's worry (2): the family is not merely
large, it is large *in a way that defeats every cheap invariant*.

**Question 5.6 (open; not load-bearing).** Theorem B assumes the pointwise isomorphism is
natural in `p, q`. Suppose only that for each `p, q` there *exists* an isomorphism
`⟦p ⊙_⋆ q⟧ ≅ ⟦p⟧ × ⟦q⟧` natural in `X` alone. Then `A ⋆ B ≅ A + B` for all `A, B` (bare
bijections), and the unit argument of Prop. 4.2 still gives `I = ∅`, so `κ` exists — but I
cannot show `κ` is bijective without naturality. **Is there a monoidal structure `(⋆, ∅)` on
`Set` with `A ⋆ B ≅ A + B` for all `A, B` but `⋆ ≇ +` as a bifunctor?** I believe not, but I
have no proof. Nothing else in this note depends on the answer.

---

## 6. Theorem C — the comparitor is a coreflection counit

Fix the notation `J := y^{(−)} : Set^op → Cont` for the representable embedding.

The four structures now sort themselves, and the sorting is the point:

| structure | (D1) coproducts in each variable | (D2) representables closed | Day? |
|---|---|---|---|
| `×` | ✓ | ✓ | yes, of `(+, ∅)` |
| `⊗` | ✓ | ✓ | yes, of `(×, 1)` |
| `+` | ✗ — `p + 0 ≅ p ≇ 0` (Lemma 2.4) | ✗ — `y^A + y^B` has two shapes | no |
| `◁` | ✗ in the **right** variable only (Niu–Spivak Ex. 6.56: `(y+1) ◁ (1+0) ≅ 2` but `((y+1)◁1) + ((y+1)◁0) ≅ 3`); ✓ in the left | ✓ — `y^A ◁ y^B = y^{A × B}`, unit `y = y^1` | no |

The coproduct fails both conditions, and fails (D1) for a triviality. **`◁` is the near
miss.** It satisfies (D2) *exactly*, and its restriction to representables is
`(A, B) ↦ A × B` with unit `1` — **the same restriction as the Dirichlet tensor `⊗`.**

That is not a coincidence. It is a theorem.

**Theorem C.** Fix `p ∈ Cont` and write `Φ_p := (p ◁ −)` and `Ψ_p := (p ⊗ −)`. Then:

1. `p ◁ y^B ≅ p ⊗ y^B` naturally, i.e. `Φ_p ∘ J ≅ Ψ_p ∘ J`. *(Prior art: Spivak,
   Reference eq. (33); Niu–Spivak Ex. 6.84(7).)*
2. `Ψ_p ≅ Lan_J (Φ_p ∘ J)`. That is, **`p ⊗ −` is the left Kan extension of `p ◁ −` along
   the representable embedding** — equivalently, the free coproduct-preserving functor
   agreeing with `p ◁ −` on representables.
3. The comparitor `o_{p,q} : p ⊗ q → p ◁ q` (Niu–Spivak Ex. 6.85; Spivak's `Indep`,
   Reference eq. (32); Shapiro–Spivak's *comparitor*, eq. (5)) is **the counit of the
   adjunction `Lan_J ⊣ res_J`** at `Φ_p`.
4. Hence `p ⊗ −` is the **coreflection** of `p ◁ −` into coproduct-preserving endofunctors
   of `Cont`: for every coproduct-preserving `F : Cont → Cont`, postcomposition with the
   comparitor is a bijection
   ```
        Nat(F, p ⊗ −)  ≅  Nat(F, p ◁ −).
   ```
   `p ⊗ −` is the terminal coproduct-preserving approximation to `p ◁ −`.

*Proof.*

**(1).** `p ◁ y^B` has shapes `Σ_{s} (p[s] → 1) ≅ S_p` and positions
`Σ_{i ∈ p[s]} B = p[s] × B`. `p ⊗ y^B` has shapes `S_p × 1 ≅ S_p` and positions
`p[s] × B`. The evident map is the identity on both. ∎

**(2).** `Lan_J G` along the free coproduct completion is "extend by coproducts":
`(Lan_J G)(q) = Σ_{t ∈ S_q} G(q[t])` (Lemma 1.3 — this is exactly the inverse equivalence).
Taking `G = Φ_p ∘ J`, i.e. `G(B) = p ◁ y^B ≅ p ⊗ y^B` by (1),
```
    (Lan_J (Φ_p ∘ J))(q) = Σ_{t ∈ S_q} (p ⊗ y^{q[t]})
                         = Σ_{t ∈ S_q} Σ_{s ∈ S_p} y^{p[s] × q[t]}
                         = Σ_{(s,t)} y^{p[s] × q[t]}  =  p ⊗ q.
```
(The middle step is the definition of `⊗` at a representable second argument.) So
`Ψ_p ≅ Lan_J(Φ_p ∘ J)`, naturally in `p`. ∎

**(3).** The counit `ε : Lan_J(Φ_p ∘ J) ⇒ Φ_p` of `Lan_J ⊣ res_J` is, at `q`, the map induced
on the coproduct `Σ_{t ∈ S_q} (p ◁ y^{q[t]})` by the family of maps `p ◁ ι_t`, where
`ι_t : y^{q[t]} → q` is the `t`-th coproduct injection (shape `∗ ↦ t`, positions
`q[t] → q[t]` the identity). Compute `p ◁ ι_t` on shapes: a shape of `p ◁ y^{q[t]}` is
`(s, f : p[s] → 1) ≅ s`, and it is sent to `(s, const_t : p[s] → S_q)`. On positions it is
`Σ_{i ∈ p[s]} q[t] → Σ_{i ∈ p[s]} q[t]`, the identity. Under the identification of (2), the
source is `p ⊗ q` with shape `(s,t)` and positions `p[s] × q[t]`. So `ε` is
```
    shapes:     (s, t)  ↦  (s, const_t)
    positions:  identity  p[s] × q[t]  =  Σ_{i ∈ p[s]} q[t].
```
That is precisely the comparitor `o_{p,q}` (Niu–Spivak's "inclusion of the order-independent
positions"; my Lean `Container.dirToSeq`). ∎

**(4).** `Lan_J ⊣ res_J` gives `Nat(Lan_J G, Φ) ≅ Nat(G, Φ ∘ J)`. Every coproduct-preserving
`F` satisfies `F ≅ Lan_J(F ∘ J)` (Lemma 1.3), and `Lan_J` is fully faithful (because `J` is —
`res_J ∘ Lan_J ≅ id`). Hence
```
  Nat(F, Φ_p) ≅ Nat(Lan_J(F∘J), Φ_p) ≅ Nat(F∘J, Φ_p∘J) ≅ Nat(Lan_J(F∘J), Lan_J(Φ_p∘J))
              ≅ Nat(F, Ψ_p),
```
and unwinding, the composite bijection is postcomposition with the counit `ε = o_{p,−}`. So
the inclusion `Fun_⊔(Cont, Cont) ↪ Fun(Cont, Cont)` has right adjoint `Φ ↦ Lan_J(Φ ∘ J)` at
`Φ_p`, with counit the comparitor. ∎

**Corollary 6.1 (what the comparitor *is*).** The Dirichlet tensor is the Day-ification of
the sequential operator: `⊗` is the unique convolutional tensor agreeing with `◁` on
representables (Theorem A), and the comparitor is the universal map from it. Two of the
three known facts about it are now explained rather than computed:

* *It exists at all.* It is a counit. (In the literature it is always **derived** by plugging
  `y` into the duoidal interchanger `(p◁p')⊗(q◁q') → (p⊗q)◁(p'⊗q')`. That derivation is a
  *consequence* of what the map is, not the reason it is there.)
* *It is an isomorphism when `q` is representable* (Spivak, *Reference* eq. (33)) — because
  the counit of `Lan_J ⊣ res_J` is invertible on the image of `J`, `J` being fully faithful.
  No computation needed.

The third fact — compatibility with the associators — I verify by hand rather than appeal to
a general monoidal-Kan-extension principle I have not checked.

**Proposition 6.1.1 (coherence of the comparitor; content due to Niu–Spivak Ex. 6.85 and
Spivak *Reference* eq. (32) — proof mine).** The family `o_{p,q} : p ⊗ q → p ◁ q` makes
`id_Cont` a lax monoidal functor `(Cont, ◁, y) → (Cont, ⊗, y)` — i.e. `o` commutes with the
associators and unitors.

> *A note on conventions.* Niu–Spivak (Ex. 6.85) write the source as `⊗` and the target as
> `⊳`; Spivak (*Reference* eq. (32)) writes it the other way. Only Spivak's direction
> type-checks under the usual definition of *lax* (a lax `F : (C,⊗_C) → (D,⊗_D)` has
> `μ : Fa ⊗_D Fb → F(a ⊗_C b)`, which for `F = id`, source `◁`, target `⊗` reads
> `p ⊗ q → p ◁ q` ✓). The mathematical content — "`o` commutes with associators and
> unitors" — is the same in both, and is what I prove.

*Proof.* The associator condition asks that the two composites `(a ⊗ b) ⊗ c → a ◁ (b ◁ c)`
agree:
```
   (a⊗b)⊗c --o⊗1--> (a◁b)⊗c --o--> (a◁b)◁c --α^◁--> a◁(b◁c)
   (a⊗b)⊗c --α^⊗--> a⊗(b⊗c) --1⊗o--> a⊗(b◁c) --o--> a◁(b◁c)
```
Both sides have source shapes `(s_a, s_b, s_c)` and source positions
`a[s_a] × b[s_b] × c[s_c]`, and every map in sight is the identity on positions (each `o` is,
by the computation in Theorem C(3); the associators are the canonical re-bracketings). So it
suffices to compare shape maps.

*Top.* `o ⊗ 1` sends `((s_a,s_b), s_c) ↦ ((s_a, λi. s_b), s_c)`; then `o` sends this to
`((s_a, λi. s_b), λ(i,j). s_c)`, a shape of `(a◁b)◁c`; then `α^◁`, which sends a shape
`((s_a, f), g)` of `(a◁b)◁c` to `(s_a, λi. (f i, λj. g(i,j)))`, yields
```
   ( s_a , λi. ( s_b , λj. s_c ) ).
```
*Bottom.* `α^⊗` gives `(s_a, (s_b, s_c))`; `1 ⊗ o` gives `(s_a, (s_b, λj. s_c))`; and `o`
gives `(s_a, λi. (s_b, λj. s_c))` — the same shape.

The unitors: `y ⊗ q = q = y ◁ q` with `o_{y,q} = id`, and `p ⊗ y = p = p ◁ y` with
`o_{p,y} = id` (the shape map `(s,∗) ↦ (s, !)` is the identity, `p[s] → 1` having a unique
element). ∎

**Proposition 6.2 (exactly when the comparitor is invertible).** The position component of
`o_{p,q}` is always the identity (Theorem C(3)). Hence `o_{p,q}` is an isomorphism iff its
shape map is a bijection. That shape map is the coproduct over `s ∈ S_p` of
```
    c_s : S_q ⟶ S_q^{p[s]},      t ↦ const_t,
```
so `o_{p,q}` is an isomorphism iff every `c_s` is a bijection. Working out `c_s`:

* `|p[s]| = 1` ⟹ `S_q^{p[s]} ≅ S_q` and `c_s` is the identity: **bijective, always**.
* `|p[s]| = 0` ⟹ `S_q^{∅} = 1` and `c_s : S_q → 1`: bijective iff `|S_q| = 1`.
* `|p[s]| ≥ 2` ⟹ `c_s` is surjective iff every `f : p[s] → S_q` is constant, i.e. iff
  `|S_q| ≤ 1`. (If `S_q = ∅` then `S_q^{p[s]} = ∅` too and `c_s : ∅ → ∅` is a bijection.)

Hence the **trichotomy**:

| | `o_{p,q}` is an isomorphism iff … |
|---|---|
| `q` representable (`\|S_q\| = 1`) | **always** |
| `q = 0` (`S_q = ∅`) | every `p[s] ≠ ∅` |
| `\|S_q\| ≥ 2` | **`p` is linear** (every `p[s]` a singleton) |

*(This recovers Spivak's eq. (33) — `Ay ⊗ q ≅ Ay ◁ q` and `p ⊗ y^A ≅ p ◁ y^A` — and shows
the list is exhaustive: for `|S_q| ≥ 2` linearity of `p` is not merely sufficient but
necessary. The `q = 0` row is a consistency check: `p ⊗ 0 = 0` by Lemma 2.4, while
`p ◁ 0 = |{s : p[s] = ∅}| · y^∅`, so the two agree precisely when no shape of `p` is
position-free.)*

The reading: **coproduct-preservation in the second variable is precisely non-dependence of
the inner shape on the outer position.** A shape of `p ◁ q` is `(s, f : p[s] → S_q)`; a shape
of `p ⊗ q` is `(s, t)`, i.e. the case where `f` is *constant*. A linear `p` has exactly one
position per shape, so there is nothing for `f` to depend on — and there the two agree.

**Proposition 6.3 (the comparitor is neither monic nor epic).** Take `p = 1 = y^∅`.
Then `1 ⊗ q = Σ_{t ∈ S_q} y^{∅ × q[t]} = S_q · y^∅`, the constant container at `S_q`, while
`1 ◁ q = ⟦1⟧ ∘ ⟦q⟧ = 1`. So `o_{1,q} : S_q · 1 → 1` collapses everything: for `|S_q| ≥ 2` it
is not injective on shapes. And for `p = y²`, `q = 2` the shape map `S_p × S_q → Σ_s S_q^{p[s]}`
is `2 → 4`, not surjective.

Both failures are informative, and they are informative in *opposite directions*:

* **Not surjective:** `◁` has genuinely dependent shapes that `⊗` cannot reach. This is the
  dependency `◁` has and `⊗` lacks — the slogan I wanted.
* **Not injective:** when an outer shape has *no positions*, `◁` cannot see the inner choice
  at all (there is nowhere to put it), but `⊗` still records it. The comparitor forgets it.

So the failure of `o` to be an isomorphism measures dependency in one direction and
*vacuity* in the other. (My earlier note recorded only the non-surjectivity. The
non-injectivity is the other half, and it is why `⊗` is a *coreflection* of `◁` rather than a
subobject of it.)

---

## 7. What is new here, and what is not

**Cited, not mine:**

* Day convolution on Poly; the formula `p ⊙ q ≅ Σ y^{p[i] ⋆ q[j]}`; "`⊙` distributes over
  coproducts" — **Niu–Spivak, arXiv:2312.00990, Prop. 3.79, eqs. (3.80)–(3.81)**, pp. 69–71.
* `× = Day(+, 0)` and `⊗ = Day(×, 1)` — **Niu–Spivak, Prop. 3.79 ¶2** (verbatim); Spivak,
  *Reference: Categorical Structures on Poly* (2022), p. 6.
* `A ∨_S B = A + A×S×B + B` and the induced `▷_S` on Poly — **Spivak, *Reference*, eqs. (9),
  (12)**; he credits Richard Garner (and MathOverflow for `S ≥ 2`); `S = 1` is Niu–Spivak
  Exercise 3.82. *(Spivak asserts monoidality; Prop. 5.2 supplies a coherence proof.)*
* The comparitor `p ⊗ q → p ◁ q`, its lax monoidality, and its invertibility for linear `p`
  or representable `q` — **Niu–Spivak Ex. 6.85, Prop. 6.87, Ex. 6.84**; **Spivak, *Reference*
  eqs. (32), (33)**; **Shapiro–Spivak, *Duoidal Structures for Compositional Dependence*,
  eq. (5)**; **Spivak–Garner–Fairbanks, *Functorial Aggregation*, Prop. 7.10**.
* `◁` not cocontinuous in the right variable — **Niu–Spivak Ex. 6.56**.
* `Poly ≃ Fam(Set^op)` — **Spivak–Garner–Fairbanks, Prop. 3.6**; **Kondyrev–Spivak, eq. (5)**.

**New, so far as a full search of the seed shows:**

* **Theorem A** — the classification. Every source states only the *existence* direction
  ("for any monoidal structure on `Set` there **is** one on `Poly`"). No converse, no
  essential image, no fullness. Theorem A says the Day construction is an **equivalence**
  onto the convolutional structures, and identifies the two conditions (D1), (D2) that cut
  them out.
* **Lemma 3.2** — the representability of the unit is a *consequence* of (D1) + (D2), not an
  assumption. "Convolutional" is a condition on the tensor alone.
* **Theorem B / B′** — the product is the **unique** pointwise Day tensor, with an effective
  test (`κ`). The mechanism (`y^{A+B} ≅ y^A × y^B` splits, `y^{A×B}` does not) I had already
  written, informally and unproved, in a doc-comment in my own `Dirichlet.lean`. This is the
  theorem that doc-comment was reaching for.
* **Theorem B⁺** — the Day hypothesis is removable: the cartesian structure is the unique
  pointwise monoidal structure on `Cont`, among *all* monoidal structures. This is the
  headline, and it is what Theorem A buys.
* **Lemma 4.4** — rigidity of the coproduct (its coherence data are forced *before*
  coherence is imposed). Surely folklore, but I have not found it stated and it is what makes
  (2) ⟹ (3) go through.
* **Corollary 5.5** — a proper class of convolutional structures on `Cont`, all
  sharing the terminal unit, exactly one cartesian. Spivak defines the `▷_S` family; nobody
  observes that it is *unit-blind* and that only `S = ∅` is pointwise.
* **Theorem C** — the comparitor is the **counit of a coreflection**, `p ⊗ − = Lan_J((p ◁ −)
  ∘ J)`. In the literature the comparitor is always *derived* from the duoidal interchanger.
  Theorem C says what it **is**, and the three known facts about it (existence, lax
  monoidality, invertibility locus) become corollaries.
* **Prop. 6.2** — the invertibility locus is *exactly* linear-or-representable (the
  literature gives the sufficient direction).
* **Prop. 6.3** — the comparitor is not injective either; the vacuous-shape phenomenon.

**Honest grading.** Theorems A, B, C are `proved` (elementary, complete). Prop. 5.2's
coherence argument is a normal-form argument of the kind I used for the `◁` pentagon; it is
complete but I would like it machine-checked. Question 5.6 is an open gap and is flagged as
such; nothing depends on it.

---

## 8. Verification

Code in `scratch/day-family/` (`core.py`, `task1`–`task5`, `run_all.sh`). Finite sets as
tagged Python sets; **bijections constructed and compared elementwise**, not by counting.

| Claim | Result |
|---|---|
| `⊙_{(+,∅)} = ×` and `⊙_{(×,1)} = ⊗` (Ex. 2.3) | PASS, structural equality, 169 container pairs each |
| `×` pointwise; `⊗` not (Cor. 4.3) | PASS — 676/676 pointwise for `×`; 376/676 violations for `⊗`. Honest witness: `⟦y ⊗ y⟧X = X^{1·1} = X` vs `⟦y⟧X · ⟦y⟧X = X²`; at `|X| = 2`, `2 ≠ 4` |
| `∨_S` unitors, associator are natural bijections | PASS, all `|A|,|B|,|S| ∈ {0..3}`; naturality over 3993 function-triples |
| **`∨_S` pentagon** (Prop. 5.2) | PASS — 243 size-tuples, the two composites equal **as functions**, elementwise; plus size-3 spot checks |
| **`∨_S` triangle** (Prop. 5.2) | PASS |
| `κ` iso iff `S = ∅` (Thm. 5.4) | PASS |
| `⊙_{∨_S}` pointwise iff `S = ∅` (Thm. 5.4) | PASS — witness `C = D = y`, `\|S\| = 1`: positions `1 + 1·1·1 + 1 = 3`, so `⟦y ⊙ y⟧X = X³` vs `X²`; at `\|X\|=2`, `8 ≠ 4` |
| comparitor is a well-typed morphism; not injective; not surjective (Prop. 6.3) | PASS, explicit witnesses |
| comparitor iso-criterion (Prop. 6.2) | PASS, exhaustive over all `C, D` with ≤2 shapes and ≤2 positions/shape — no counterexample |
| `C ⊗ y^B ≅ C ◁ y^B` (Thm. C(1)) | PASS, 244 pairs |

**The negative control is the most valuable output of the run — and it changes how I read
the literature.** A *label-swapping* variant `α'` of the `∨_S` associator was constructed: it
is a natural bijection, it has identical cardinalities, and it **is associative**. It
nonetheless **fails the pentagon** — 16 of 243 size-tuples, first at `|A|=|B|=|C|=|D|=1`,
`|S| = 2`:
```
  x       = ('m',(('m',(('m',(a,k0,b)),k1,c)),k1,d))
  path 1  = ('m',(a,k1,('m',(b,k0,('m',(c,k1,d))))))
  path 2  = ('m',(a,k1,('m',(b,k1,('m',(c,k0,d))))))     ← differ
```
Two consequences.

1. **The pentagon PASS on the true `α` is not vacuous** — the test has teeth. (Note it takes
   `|S| ≥ 2` to see the difference: a test suite with `|S| ≤ 1` would have blessed `α'`.)
2. **Prop. 5.2 was not pedantry.** Spivak (*Reference*, eq. (9)) *asserts* that `∨_S` is
   monoidal; Niu–Spivak (Ex. 3.82) ask the reader to verify **associativity** — a bijection
   `(A ∨ B) ∨ C ≅ A ∨ (B ∨ C)` — and unitality, and nothing more. The negative control
   exhibits a natural, associative bijection that is **not** a monoidal associator. So
   associativity-as-a-bijection genuinely does not suffice, and the coherence proof in
   Prop. 5.2 (which Cor. 5.5 depends on) is filling a real gap in the cited sources, not
   restating them.

**One sharpening, recorded honestly.** The claim "`κ_{A,B}` is a bijection iff `S = ∅`" is
false *for a fixed pair* `(A,B)`: if `A` or `B` is empty, the middle piece `A × S × B`
vanishes for trivial reasons and `κ_{A,B}` is bijective for every `S`. The correct statements
(both verified, and both what Theorem B′ and Theorem 5.4 actually assert, since each
quantifies over **all** `A, B`):

* `κ_{A,B}` is a bijection ⟺ `|A| · |S| · |B| = 0`;
* `κ` is a bijection for all `A, B` ⟺ `S = ∅`.

`κ` is *always* injective — it is the inclusion of the two outer summands — and its image
always misses exactly the middle piece `A × S × B`. **That middle piece is the whole
obstruction**, and it is the same obstruction in Theorem 5.4 as in Theorem B′.

*(A discrepancy worth recording: the verification run's own summary stated the comparitor
iso-criterion as "`|p[s]| = 1` or `|S_q| ≤ 1`". That is wrong in one corner — for `S_q = ∅`
and `p[s] = ∅` the map `c_s : ∅ → ∅^∅ = 1` is not surjective. Prop. 6.2's trichotomy has it
right, and it cross-checks against Lemma 2.4: `1 ⊗ 0 = 0` but `1 ◁ 0 = 1`, so the comparitor
is indeed not an isomorphism there.)*

---

## 9. The sentence for the book

> Shapes always multiply. The choice of monoidal structure on `Set` shows up only in the
> positions — and among the proper class of tensors this produces, exactly one, the
> coproduct on positions, gives back the categorical product. The Dirichlet tensor's failure
> to be pointwise is therefore not an accident of the definition. It is the generic case.
> Being pointwise is the rare thing — indeed the product is the *only* monoidal structure on
> containers whose extension is the pointwise product, and one can say this without ever
> mentioning Day convolution. Day convolution is merely how one gets to *see* it.

And, for the relation between two of Neil's four structures:

> `⊗` is `◁` with the dependency switched off — not by fiat, but universally: `p ⊗ −` is the
> terminal coproduct-preserving approximation to `p ◁ −`, and the comparitor is its counit.
> The comparitor fails to be surjective exactly where `◁` is dependent, and fails to be
> injective exactly where `◁` is vacuous.
