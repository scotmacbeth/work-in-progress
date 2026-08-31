# The uniform closure formula for Day-convolutional tensors on Cont

MacBeth — 2026-07-15. Deep-work session.

**Status.** Both directions proved. The sufficiency direction (the formula *is* a right
adjoint) and the necessity direction (closed ⟹ the polynomial condition) both close, and the
necessity turns out to be *easy* once phrased correctly — it is a one-line consequence of
co-Yoneda applied to a single representable. This settles both registry grades in one stroke:
`uniform-closure-formula` → **proved**, `closed-convolutional-classification` → **proved**
(it was graded `speculative` only because nobody had written the two lines).

**Two honest corrections to the PROVE brief, recorded up front:**

1. **Handedness.** PROVE.md pairs the *formula* `[p,q]_⋆(A) = Π_i q(A ⋆ p[i])` (the varying
   argument `A` sits in the **left** slot of `⋆`) with the *condition* "`R ⋆ (−)` is
   polynomial for every `R`" (varying argument in the **right** slot). These do not match.
   The condition that goes with that formula is **`(−) ⋆ B` is polynomial for every set `B`**
   — the left slot. For symmetric `⋆` (which includes both `+` and `×`, hence the cartesian
   and Dirichlet instances) the two are the same and the mismatch is invisible; I flag it
   because the theorem is stated for possibly-non-symmetric `⋆` and the mirror version (right
   closure) carries the *other* condition. §4.

2. **No classical/EM step materialises.** PROVE.md expected "the same pointed-domain split as
   the chain rule (classical EM); expect it here too." It does not appear. The sufficiency
   proof uses only co-Yoneda, hom-out-of-a-coproduct, and closure of `Poly` under composition
   and (small) products. The single infinitary ingredient is the distributive law
   `Π_i Σ_t (−) ≅ Σ_φ Π_i (−)`, which is the ordinary dependent-product/dependent-sum
   distributivity in `Set` — constructively valid, no excluded middle. I say so rather than
   manufacture a split that isn't there. §5, Remark 5.2.

**Verification.** `scratch/day-family/task6_closure.py`: the core isomorphism holds on
**2704/2704** cases (`⋆ ∈ {+, ×, ∨_S(|S|=1), ∨_S(|S|=2)}`, all `p, q` with ≤ 2 shapes and
≤ 2 positions/shape, `|R| ≤ 3`), the necessity witness `⟦[y^B,y]⟧R = R ⋆ B` on **64/64**,
and a teeth check confirms a wrong formula (Σ for Π) breaks on 269/351 of the eligible cases.

---

## 0. Setup and conventions

I work inside the framework of `proofs/2026-07-14-day-family-classification.md` (Theorem A),
whose notation I inherit:

* `Cont ≅ Fam(Set^op)` is the category of containers; an object `p` is a set of shapes
  `S_p := p(1)` together with a position set `p[s]` for each `s ∈ S_p`. A morphism
  `p → q` is a pair `(u : S_p → S_q, (g_s : q[u s] → p[s])_s)` — contravariant on positions.
* The extension `⟦p⟧X = Σ_{s ∈ S_p} X^{p[s]}` is fully faithful `Cont ↪ [Set, Set]`
  (Abbott–Altenkirch–Ghani); its essential image is the category `Poly` of **polynomial
  functors**. I call a functor `Set → Set` *polynomial* if it is isomorphic to some `⟦c⟧`.
* Representables: `y^R` has one shape and position set `R`; `y := y^1`, `1 := y^∅`.
* `⊙_⋆` is the Day convolution of a monoidal structure `(⋆, I)` on `Set` (Def. 2.1):
  `p ⊙_⋆ q := (S_p × S_q, (s,t) ↦ p[s] ⋆ q[t])`, unit `J_⋆ = y^I`. Prop. 2.2: it is
  monoidal, preserves coproducts in each variable **(D1)**, sends representables to
  representables `y^A ⊙_⋆ y^B = y^{A⋆B}` **(D2)**, and is exactly Day convolution
  (Niu–Spivak Prop. 3.79).

Two facts I will use constantly.

**Fact 0.1 (co-Yoneda / density of representables).** For any container `q` and set `R`,
```
        Cont(y^R, q)  ≅  ⟦q⟧(R),        natural in R and in q.
```
*Proof.* A morphism `y^R → q` is a shape `t ∈ S_q` (the image of the unique shape of `y^R`)
together with a position map `q[t] → R`, i.e. an element of `Σ_{t ∈ S_q} R^{q[t]} = ⟦q⟧R`.
Naturality in `R` is covariance of `R^{q[t]}`; naturality in `q` is functoriality of `⟦−⟧`. ∎

**Fact 0.2 (hom sends coproducts to products).** Every container is the coproduct of its
shape-representables, `r ≅ Σ_{J ∈ S_r} y^{r[J]}` (coproduct in `Cont` = disjoint union of
shapes). Hence for any `b`,
```
        Cont(r, b)  ≅  Π_{J ∈ S_r} Cont(y^{r[J]}, b),        natural in r and b.
```
*Proof.* `Cont(Σ_J a_J, b) ≅ Π_J Cont(a_J, b)` is the universal property of the coproduct in
the first argument of a hom-functor, and `r ≅ Σ_J y^{r[J]}` is immediate from the description
of `Cont` as `Fam(Set^op)`. ∎

---

## 1. The theorem

**Theorem (uniform closure).** Let `(⋆, I)` be a monoidal structure on `Set`. The following
are equivalent:

1. `(Cont, ⊙_⋆)` is **left closed**: the functor `(−) ⊙_⋆ p : Cont → Cont` has a right
   adjoint for every container `p`;
2. `(−) ⋆ B : Set → Set` is a **polynomial functor** for every set `B`.

When they hold, the right adjoint (the internal hom) is `[p, −]_⋆`, the container-valued
functor determined on objects by its extension
```
        ⟦[p, q]_⋆⟧(R)  =  Π_{i ∈ S_p} ⟦q⟧(R ⋆ p[i]),                       (★)
```
i.e. `[p,q]_⋆ = Π_{i ∈ S_p}  q ◁ (p[i] ⋆ y)`, where `p[i] ⋆ y` denotes the container of the
polynomial functor `(−) ⋆ p[i]`, `◁` is composition of containers, and `Π` is the product in
`Cont`.

The **right-closed** mirror holds with `⋆` and its arguments swapped: `p ⊙_⋆ (−)` has a right
adjoint for every `p` iff `A ⋆ (−)` is polynomial for every `A`, with internal hom
`⟦[p,q]'_⋆⟧(R) = Π_i ⟦q⟧(p[i] ⋆ R)`.

**Corollary (classification).** Under the equivalence of Theorem A between monoidal
structures on `Set` and convolutional monoidal structures on `Cont`, "left closed" on the
`Cont` side corresponds exactly to "`(−) ⋆ B` polynomial ∀B" on the `Set` side. Restricting
Theorem A to these matching full sub-collections gives an equivalence
```
   { monoidal (⋆,I) on Set : (−)⋆B polynomial ∀B }  ≃  { left-closed convolutional
                                                          monoidal structures on Cont }.
```

The three named instances are the three known closures, side by side:

| `⋆` | `⊙_⋆` | `(−) ⋆ B` polynomial? | internal hom `⟦[p,q]⟧R` | known as |
|---|---|---|---|---|
| `(+, ∅)` | `×` (product) | yes: `X+B = y + B·y^∅` | `Π_i ⟦q⟧(R + p[i])` | cartesian closure (Niu–Spivak Thm 5.31; ALS `Π_s F(−+p[s])`) |
| `(×, 1)` | `⊗` (Dirichlet) | yes: `X×B = B·y` | `Π_i ⟦q⟧(R × p[i])` | Dirichlet closure (Ex. 4.79; `DirichletClosed.lean`) |
| `(∨_S, ∅)` | `▷_S` | yes: `X∨_S B = (1+S·B)·y + B·y^∅` | `Π_i ⟦q⟧(R ∨_S p[i])` | Spivak's third family (Eqs. 38–40) |

The general biconditional and the necessity reduction are the new content; the three
instances and formula (★) itself are prior art (Spivak's Eqs. 38/39/40, written side by side
but never unified). See §6.

---

## 2. Sufficiency: the formula is a right adjoint

Assume (2): `(−) ⋆ B` is polynomial for every set `B`.

**Step 1 — `[p,q]_⋆` is a container.** Fix `p, q`. Consider the endofunctor of `Set`
```
        H(R)  :=  Π_{i ∈ S_p} ⟦q⟧(R ⋆ p[i]).
```
For each fixed `i`, `R ↦ R ⋆ p[i]` is `(−) ⋆ p[i]`, polynomial by (2); and `⟦q⟧` is
polynomial; so `R ↦ ⟦q⟧(R ⋆ p[i])` is a composite of polynomial functors, hence polynomial
(`Poly` is closed under composition — that is the operation `◁`, with
`⟦q ◁ c⟧ = ⟦q⟧ ∘ ⟦c⟧`). Finally `H` is the `S_p`-indexed product of these, and `Poly` is
closed under small products (§5, Lemma 5.1). So `H` is polynomial: there is a container,
which I name `[p,q]_⋆`, with `⟦[p,q]_⋆⟧ = H`, unique up to canonical iso by full
faithfulness of `⟦−⟧`. This is formula (★). Functoriality in `q` is inherited from `⟦q⟧`
(a morphism `q → q'` induces `⟦q⟧ → ⟦q'⟧`, hence `H → H'`, hence `[p,q] → [p,q']`); so
`[p, −]_⋆ : Cont → Cont` is a functor.

**Step 2 — the hom-isomorphism at a representable domain.** For any set `R` and container
`q`,
```
   Cont(y^R ⊙_⋆ p,  q)
     =  Cont( Σ_{i ∈ S_p} y^{R ⋆ p[i]},  q )      [y^R ⊙_⋆ p = Σ_i y^{R⋆p[i]}, by Def. 2.1]
     ≅  Π_{i ∈ S_p} Cont( y^{R ⋆ p[i]}, q )        [Fact 0.2]
     ≅  Π_{i ∈ S_p} ⟦q⟧( R ⋆ p[i] )                [Fact 0.1, at each i]
     =  H(R)  =  ⟦[p,q]_⋆⟧(R)
     ≅  Cont( y^R, [p,q]_⋆ ).                       [Fact 0.1 again]
```
The first line uses `y^R ⊙_⋆ p = (S_p, i ↦ R ⋆ p[i])` (shapes `1 × S_p ≅ S_p`, positions
`R ⋆ p[i]`), which is the coproduct `Σ_i y^{R⋆p[i]}`. Every iso in the chain is natural in
`R` (Facts 0.1, 0.2 are natural, and `⊙_⋆`, `⟦q⟧` are functorial) and in `q`.

**Step 3 — extend to arbitrary domain.** For a general container `r ≅ Σ_{J ∈ S_r} y^{r[J]}`,
apply Fact 0.2 twice and Step 2 pointwise:
```
   Cont(r ⊙_⋆ p, q)  ≅  Cont( Σ_J (y^{r[J]} ⊙_⋆ p),  q )     [(D1): ⊙_⋆ preserves the coproduct in r]
                      ≅  Π_J Cont( y^{r[J]} ⊙_⋆ p, q )        [Fact 0.2]
                      ≅  Π_J Cont( y^{r[J]}, [p,q]_⋆ )         [Step 2, natural in R = r[J]]
                      ≅  Cont( Σ_J y^{r[J]}, [p,q]_⋆ )         [Fact 0.2]
                      =  Cont( r, [p,q]_⋆ ).
```
This is a natural isomorphism `Cont(− ⊙_⋆ p, q) ≅ Cont(−, [p,q]_⋆)` of functors
`Cont^op → Set`; combined with naturality in `q` from Step 2 it is a natural isomorphism of
functors `Cont^op × Cont → Set`. A functor `[p, −]_⋆` together with such a natural
isomorphism is precisely a right adjoint to `(−) ⊙_⋆ p` (the hom-iso form of an adjunction;
the unit/counit and triangle identities are then forced). Hence `(−) ⊙_⋆ p ⊣ [p, −]_⋆`, and
`(Cont, ⊙_⋆)` is left closed. ∎

*(Why (D1) is exactly what Step 3 needs: for a right adjoint to `(−)⊙_⋆ p` to exist at all,
that functor must preserve colimits, in particular coproducts — which is (D1). Sufficiency
shows (D1) plus condition (2) is enough; §3 shows (2) is also necessary.)*

---

## 3. Necessity: closed forces the polynomial condition

Assume (1): `(−) ⊙_⋆ p` has a right adjoint `[p, −]_⋆ : Cont → Cont` for every `p`. I do not
need this for all `p` — one representable suffices.

Fix a set `B` and take `p = y^B`. Let `G := [y^B, −]_⋆` be the given right adjoint, so
`Cont(a ⊙_⋆ y^B, b) ≅ Cont(a, G b)` naturally. Evaluate the extension of `G(y)` (recall
`y = y^1`, `⟦y⟧ = Id`) using Fact 0.1 and the adjunction:
```
   ⟦G(y)⟧(R)  ≅  Cont( y^R, G(y) )                 [Fact 0.1]
              ≅  Cont( y^R ⊙_⋆ y^B, y )            [adjunction]
              =  Cont( y^{R ⋆ B}, y )              [(D2): y^R ⊙_⋆ y^B = y^{R⋆B}]
              ≅  ⟦y⟧(R ⋆ B)  =  R ⋆ B.             [Fact 0.1]
```
All isos are natural in `R`. So the functor `R ↦ R ⋆ B`, i.e. `(−) ⋆ B`, is isomorphic to
`⟦G(y)⟧`, the extension of a container. Therefore `(−) ⋆ B` is polynomial. Since `B` was
arbitrary, condition (2) holds. ∎

**Remark 3.1 (why this was the "speculative" half, and why it shouldn't have been).** The
necessity looks like it should require analysing the whole internal-hom functor. It does not:
the right adjoint's value at the *unit representable* `y`, read off through co-Yoneda, is
literally the functor `(−) ⋆ B`. Closedness is a statement about *all* homs; but to extract
the obstruction you only interrogate one — `[y^B, y]_⋆`. The polynomial condition is not an
extra hypothesis bolted onto closure; it is closure, evaluated at a point.

---

## 4. Handedness (correcting the brief)

The derivation pins the handedness unambiguously. In `y^R ⊙_⋆ p`, the position at shape `i`
is `(y^R\text{-position}) ⋆ (p\text{-position}) = R ⋆ p[i]`: the varying object `R` occupies
the **left** slot of `⋆`, the fixed `p[i]` the right. Since Step 2 tensors `p` on the *right*
of the varying domain, the internal hom `[p,−]_⋆` is the right adjoint of `(−) ⊙_⋆ p`, and it
is governed by `(−) ⋆ p[i]`, i.e. by left-slot polynomiality `(−) ⋆ B`.

The mirror is exact: `p ⊙_⋆ y^R` has positions `p[i] ⋆ R`, so `p ⊙_⋆ (−)` has right adjoint
`⟦[p,q]'⟧R = Π_i ⟦q⟧(p[i] ⋆ R)`, governed by right-slot polynomiality `A ⋆ (−)`. PROVE.md's
formula (`A ⋆ p[i]`, left slot) belongs to the first; its condition (`R ⋆ (−)`, right slot)
belongs to the second. I keep the pair consistent: **formula (★) with `R ⋆ p[i]` ↔ condition
`(−) ⋆ B` polynomial.**

For `⋆ ∈ {+, ×}` (symmetric) left and right slots agree and the distinction is vacuous — this
is why the cartesian and Dirichlet instances never exposed it. Spivak's `∨_S` is *not*
symmetric as a bifunctor on the nose (`A ∨_S B = A + A×S×B + B` vs `B + B×S×A + A` differ
functorially, though they share cardinality — which is why a cardinality check cannot see the
handedness either; `task6` confirms the *formula*, not the slot). But `∨_S` is polynomial in
**both** slots, so `▷_S` is bi-closed and the handedness has no observable consequence for it.
An observable difference would need a monoidal `⋆` polynomial in exactly one slot; whether one
exists is exactly the open sub-question of §6.

---

## 5. The two lemmas Step 1 leans on

**Lemma 5.1 (`Poly` is closed under small products).** Let `(c_i)_{i ∈ I}` be an `I`-indexed
family of containers, `I` a small set. Then `R ↦ Π_{i ∈ I} ⟦c_i⟧(R)` is polynomial, with
container `Π_{i∈I} c_i` having shapes `Π_{i∈I} S_{c_i}` and, at `σ ∈ Π_i S_{c_i}`, position
set `Σ_{i∈I} c_i[σ(i)]`.

*Proof.* Compute, using the distributive law `Π Σ ≅ Σ Π` in `Set`:
```
   Π_{i∈I} ⟦c_i⟧(R) = Π_{i∈I} Σ_{s∈S_{c_i}} R^{c_i[s]}
                    ≅ Σ_{σ ∈ Π_i S_{c_i}} Π_{i∈I} R^{c_i[σ(i)]}
                    = Σ_{σ ∈ Π_i S_{c_i}} R^{Σ_{i∈I} c_i[σ(i)]},
```
which is the extension of the stated container. The middle iso is
`Π_i Σ_{s} T_{i,s} ≅ Σ_{σ: (i↦s)} Π_i T_{i,σ(i)}` — the choice-function reindexing, valid in
`Set`. ∎

**Remark 5.2 (the constructive status of Lemma 5.1).** The reindexing set `Π_i S_{c_i}` is
the set of choice functions; the iso `Π Σ ≅ Σ Π` is dependent-product/dependent-sum
distributivity, which is the *type-theoretic axiom of choice* and is **constructively
provable** (it is the shuffling `(Πx.Σy.φ) → (Σf.Πx.φ[f x])`, a theorem of intuitionistic
type theory, and a plain isomorphism in `Set`). No excluded middle, no pointed-domain split.
This is where PROVE.md anticipated a classical hinge "as in the chain rule"; the honest report
is that none appears — the chain rule's EM split was forced by a case analysis on
empty-vs-inhabited domains, and formula (★) has no such analysis. The infinitary content here
is choice-function reindexing, and it is benign.

**Lemma 5.2 (composition).** If `F, G : Set → Set` are polynomial then so is `G ∘ F`, with
container `g ◁ f` where `⟦f⟧ = F, ⟦g⟧ = G`. *This is Niu–Spivak's `◁` on `Poly`
(`⟦g ◁ f⟧ = ⟦g⟧∘⟦f⟧`); machine-checked in my `Composition.lean` (PR #13).* ∎

Together: `R ↦ ⟦q⟧(R ⋆ p[i]) = ⟦q ◁ c_{p[i]}⟧(R)` (Lemma 5.2, with `c_{p[i]}` the container of
`(−)⋆p[i]`), and `Π_i` of these is polynomial (Lemma 5.1). Hence `[p,q]_⋆` exists as claimed
in Step 1, and `[p,q]_⋆ = Π_{i∈S_p} (q ◁ c_{p[i]})`.

---

## 6. What is new, what is prior art, and the one thing left open

**Prior art (cited, not mine).**
* Formula (★) in each of its three instances: Spivak *Reference* Eqs. (38) (cartesian),
  (39) (Dirichlet), (40) (`∨_S`); the cartesian case is Niu–Spivak Thm 5.31 and the
  Altenkirch–Levy–Staton exponential `Π_s F(− + p[s])`; the Dirichlet case is Niu–Spivak
  Ex. 4.78/Eq. (4.79) ("the Dirichlet closure"), machine-checked in my `DirichletClosed.lean`.
* Day convolution `⊙_⋆`, coproduct-preservation (D1), representable-closure (D2): Niu–Spivak
  Prop. 3.79, Eqs. (3.80)–(3.81).
* `Poly` closed under `◁` (composition) and under products: Niu–Spivak (the polynomial
  calculus). "Polynomial ⟺ preserves connected limits (wide pullbacks)" for
  `Set → Set`: Carboni–Johnstone / Gambino–Kock — a citable equivalent of condition (2),
  though the proof above never needs it.

**New, so far as the seed shows** (novelty pre-audited in
`memory/closed-structures-are-spivaks.md`, which named formula (★) as "the one genuinely
unstated thing … a remark, not a paper"):
* The **general biconditional** *(Cont, ⊙_⋆) left closed ⟺ `(−)⋆B` polynomial ∀B*, uniform in
  `⋆` — the three instances unified, with the honest condition. Spivak writes the three
  closures side by side; the equivalence is never stated.
* The **necessity reduction** (§3): closure evaluated at `[y^B, y]_⋆` *is* the functor
  `(−)⋆B`. This is what makes the classification corollary immediate rather than open.
* The **handedness correction** (§4) and the **retirement of the corepresentable criterion**:
  the old "closed ⟺ `Set(R,−)` preserves `⋆`" is dead (refuted 2026-07-14: `×` = Day-of-`+`
  is closed yet `Set(R,−)` does not preserve `+`); `(−)⋆B` polynomial is the correct replacement.

**Bolt-on to Theorem A.** The value of this is structural: Theorem A made the convolutional
family surveyable; this note carves out the closed sub-family by a condition living entirely
on the `Set` side. It is a *remark* on Theorem A, not a standalone paper — as the memory note
insisted, and I hold to that grading.

**Open sub-question 6.1 (is the condition vacuous?).** Every monoidal structure I can name on
`Set` (`+`, `×`, `∨_S`, and finite iterates) is polynomial in each slot, so its Day tensor is
closed. **Is there a monoidal structure `(⋆, I)` on `Set` with `(−) ⋆ B` *not* polynomial for
some `B`** — equivalently, a convolutional monoidal structure on `Cont` that is genuinely
*not* left closed? If none exists, the classification collapses to "every convolutional tensor
is closed" and the condition, though correct, is automatic; if one exists, the closed family
is a proper sub-family and §4's handedness becomes observable. A natural place to look:
a `⋆` whose left partial application fails to preserve wide pullbacks (e.g. built from a
non-polynomial functor like full powerset), checked against associativity + unit. I have not
resolved this and flag it as the honest residue. **Nothing above depends on the answer** — the
biconditional holds either way.

---

## 7. The sentence for the book

> Every monoidal structure on `Set` induces one on containers by Day convolution — and it is
> closed exactly when tensoring by a fixed set is a polynomial operation. The internal hom is
> then always the same shape: hold `q`, run the shapes of `p`, feed each position of `p`
> through `⋆` into `q`, and take the product. Cartesian closure, Dirichlet closure, and
> Spivak's third family are one formula read three times. And you learn whether closure holds
> without ever leaving `Set`: ask whether `(−) ⋆ B` is a polynomial — closure on containers is
> polynomiality on sets, seen through the extension.
