# Double comonoids in the duoidal category (Poly, ◁, ⊗) are exactly the *sets of commutative monoids*

**MacBeth — 2026-07-15 (PROVE deep-work session)**

> **Headline.** The PROVE target ("double comonoids = degenerate polynomials `y^A` or `Ay`") is
> **false in both directions.** The correct classification is:
>
> **A directed container `c` is a double comonoid in the normal duoidal category `(Poly, ◁, ⊗)`
> if and only if its underlying category is a coproduct of one-object categories on *commutative*
> monoids** — a *set of commutative monoids* `c = ∑_{I} y^{M_I}`, each `M_I` a commutative monoid.
> When it exists, the `⊗`-comonoid structure is **unique**, with comultiplication induced by the
> category composition.
>
> The mechanism is a fibrewise **Eckmann–Hilton** collapse. The degenerate polynomials are strict
> special cases: `y^A` is a double comonoid **iff `A` is commutative** (target wrongly allows all
> monoids), and multi-object examples like `2y² = {ℤ/2, ℤ/2}` are double comonoids the target
> wrongly excludes.

---

## 1. Setup and conventions

A **polynomial functor** is `p = ∑_{I ∈ p(1)} y^{p[I]}`: a set of *positions* `p(1)`, and for each
position `I` a set of *directions* `p[I]`. A morphism `f : p → q` in `Poly` is a *forward* map on
positions `f₁ : p(1) → q(1)` together with, for each `I`, a *backward* map on directions
`f^# : q[f₁ I] → p[I]`.

**Substitution product `◁`** (`p ◁ q := p ∘ q`):
- positions: pairs `(I, j)` with `I ∈ p(1)` and `j : p[I] → q(1)`;
- directions at `(I,j)`:  `(p◁q)[I,j] = ∑_{a ∈ p[I]} q[j(a)]`.
- Unit: `y`.

**Dirichlet tensor `⊗` = Day(Set, ×, 1)**:
- positions: `(I, J) ∈ p(1) × q(1)`;
- directions: `(p⊗q)[I,J] = p[I] × q[J]`.
- Unit: `y` (the representable at `1`).

`(Poly, ◁, ⊗)` is **normal duoidal**: same unit `y`, with interchange
`ζ : (p₁◁p₂) ⊗ (q₁◁q₂) → (p₁⊗q₁) ◁ (p₂⊗q₂)` (Spivak, *Reference: Categorical Structures on Poly*,
arXiv:2202.00534, Eq. (29)).

**The comparitor** `Indep_{p,q} : p ⊗ q → p ◁ q` (2202.00534 Eq. (32); Niu–Spivak Ex. 6.85):
- on positions `(I,J) ↦ (I, const_J)`, where `const_J : p[I] → q(1)` is the constant map at `J`;
- on directions, at `(I,J)`, the identity
  `(p◁q)[I, const_J] = ∑_{a∈p[I]} q[J] = p[I]×q[J] = (p⊗q)[I,J]`.

So `Indep` is the *inclusion of the order-independent positions*: those `(I,j) ∈ (p◁q)(1)` whose
second component `j : p[I] → q(1)` is **constant**. Eq. (33): `Indep_{p,q}` is an isomorphism iff
`p = Ay` (linear) or `q = y^A` (representable); on the diagonal `p=q=c`, iff `c = Ay` or `c = y^A`.

**Directed containers = `◁`-comonoids = small categories** (Ahman–Uustalu; Spivak's `Cat#`). A
`◁`-comonoid `(c, ε^◁ : c → y, δ^◁ : c → c◁c)` is a small category `𝓒`:
- objects `O = c(1)`; for each object `I`, `c[I] =` the set of arrows *out of* `I`
  (`c[I] = ∐_X 𝓒(I,X)`);
- `ε^◁` picks the identity `id_I ∈ c[I]`;
- `δ^◁` has position component `I ↦ (I, cod_I)` where `cod_I : c[I] → O` is the codomain map, and
  direction component the **composition**
  `∑_{a∈c[I]} c[cod(a)] → c[I], (a,b) ↦ a·b` (do `a`, then `b`; diagrammatic order).

Coassociativity/counit of `δ^◁` are exactly associativity/unitality of composition.

---

## 2. The structural reduction: double comonoid = `⊗`-comonoid in `Cat#`

In any duoidal category `(𝓥, ◁, y, ⊗, y)` the second tensor `⊗` lifts to a monoidal structure on
the category `Comon_◁(𝓥)` of `◁`-comonoids, via the interchange `ζ`; a **double comonoid** is a
`⊗`-comonoid object in `(Comon_◁(𝓥), ⊗)` (Aguiar–Mahajan, *Monoidal Functors, Species and Hopf
Algebras*, "comonoids in comonoids"; this is the load-bearing structural identification — see §7).

For `Poly`, `Comon_◁(Poly) = Cat#` (categories + **cofunctors**), and the lifted tensor is the
**product of categories**: for `◁`-comonoids `c, d` the object `c⊗d` carries the `◁`-comonoid
structure of `𝓒 × 𝓓` — positions `O_𝓒 × O_𝓓`, fibre at `(I,J)` equal to `c[I]×d[J]` = arrows out of
`(I,J)` in `𝓒×𝓓` (Niu–Spivak arXiv:2312.00990 Prop. 8.79). Its `◁`-unit `y` is the terminal
category `𝟙`.

> **So: `c` is a double comonoid ⟺ the category `𝓒` carries a cofunctor comultiplication
> `δ^⊗ : 𝓒 → 𝓒 × 𝓒` and cofunctor counit `ε^⊗ : 𝓒 → 𝟙` satisfying the comonoid laws in `(Cat#, ×)`.**

Recall a **cofunctor** `F : 𝓐 → 𝓑` (= `◁`-comonoid morphism) is: a forward object map
`F : ob 𝓐 → ob 𝓑`, and a *lifting* — for each `a ∈ 𝓐` and each `𝓑`-arrow `g` out of `Fa`, a
`𝓐`-arrow `g|_a` out of `a` — subject to
- **(cod)** `F(cod(g|_a)) = cod(g)`;
- **(id)** the lift of an identity is an identity;
- **(comp)** `(h∘g)|_a = h|_{a'} ∘ g|_a`, where `a' = cod(g|_a)` (lift of a composite = composite of
  lifts).

We now run the three cofunctor axioms.

---

## 3. Step 1 — the counit and the diagonal force *every arrow to be an endomorphism*

**Counit `ε^⊗ : 𝓒 → 𝟙`.** `𝟙` has one object `⋆` and one arrow `id_⋆`. The lifting sends, for each
`I`, `id_⋆` to some arrow `e^⊗_I ∈ c[I]` out of `I`. Axiom **(id)**: `id_⋆` is an identity, so its
lift is an identity of `𝓒`, i.e. `e^⊗_I = id_I`. **The `⊗`-counit is forced and unique:
`e^⊗_I = id_I`.** (In particular the two counits share the unit `id_I` — this is exactly the
*normal* in "normal duoidal".)

**Comultiplication `δ^⊗ : 𝓒 → 𝓒 × 𝓒`.** The `⊗`-counit law `(ε^⊗ ⊗ id)∘δ^⊗ = id` fixes the object
map to the **diagonal** `I ↦ (I,I)`. Now axiom **(cod)** applied to `δ^⊗`: for any arrow `(g₁,g₂)`
of `𝓒×𝓒` out of `(I,I)`, its lift `δ^⊗(g₁,g₂)|_I =: m_I(g₁,g₂) ∈ c[I]` must satisfy
`(cod, cod)(m_I(g₁,g₂)) = (cod g₁, cod g₂)`, i.e.

  `cod(m_I(g₁,g₂)) = cod(g₁) = cod(g₂)`   for **all** `g₁, g₂` out of `I`.

But `g₁, g₂` range over *all* arrows out of `I`. Taking `g₂ = id_I` (`cod = I`) forces
`cod(g₁) = I` for every `g₁ ∈ c[I]`. **Every arrow out of every object is an endomorphism.**

A category in which every arrow is an endomorphism has no arrows between distinct objects: it is a
**coproduct of one-object categories**, i.e. a **set of monoids**
`c = ∑_{I ∈ O} y^{M_I}` with `M_I = 𝓒(I,I)` a monoid (composition `μ_I`, unit `id_I =: e`). ∎(Step 1)

*Remark (option (a), factoring only).* Exactly the same position-level computation shows: `δ^◁`
factors through `Indep_{c,c}` **iff `cod_I` is constant for every `I` iff `c` is a set of monoids**
(any monoids, possibly noncommutative, possibly many objects), and then the factor is forced to be
the `⊗`-comultiplication `m_I = μ_I`. So the *weak* reading already contradicts "degenerate";
commutativity is the price of the *full* double-comonoid axioms, obtained next.

---

## 4. Step 2 — the composition axiom is a fibrewise Eckmann–Hilton interchange

Assume now `c` is a set of monoids (Step 1). Fix an object `I`; all arrows out of `I` are endos, so
`𝓒×𝓒`-arrows out of `(I,I)` are exactly `M_I × M_I`, and the lift is a map

  `m_I : M_I × M_I → M_I`.

The remaining cofunctor axioms and comonoid laws read, on this fibre (writing `·` for `μ_I`, unit
`e`):

- **(id)** `m_I(e,e) = e`.                                                                    …(C1)
- **(comp)** for the composite of `(g₁,g₂)` then `(h₁,h₂)` in `𝓒×𝓒`, which is the *componentwise*
  composite `(g₁·h₁, g₂·h₂)` (product-category composition keeps the two slots separate):
  `m_I(g₁·h₁, g₂·h₂) = m_I(g₁,g₂) · m_I(h₁,h₂)` — i.e. **`m_I` is a monoid homomorphism from the
  *product monoid* `(M_I × M_I, ·×·) → (M_I, ·)`.**                                            …(C2)
  ⚠️ *This is the genuine crosswise interchange, NOT the vacuous same-pairing law.* On the RHS the
  first slot collects `g₁,h₁` and the second collects `g₂,h₂`; the LHS composes slotwise
  (`g₁·h₁`, `g₂·h₂`). Setting `m=·` this demands `(g₁h₁)(g₂h₂) = (g₁g₂)(h₁h₂)`, i.e. `h₁g₂ = g₂h₁`
  — commutativity — which is exactly the content, and exactly why `y^{S_3}` fails. (Contrast the
  degenerate misreading `m(a·b, a'·b') = m(a,b)·m(a',b')` pairing `a` with `b`: that one is a
  tautology for `m=·` and carries no information — a trap worth flagging.)
- **counit** of `δ^⊗`: `m_I(a, e) = a = m_I(e, a)` — `e` is a two-sided unit for `m_I`.        …(C4)
- **coassoc** of `δ^⊗`: `m_I` is associative.                                                 …(C3)

**Lemma (Eckmann–Hilton).** Two binary operations `·` and `m` on a set `S` with a common two-sided
unit `e`, such that `m` is a `·`-homomorphism (C2), coincide and are commutative: `m = ·` and `·` is
commutative.

*Proof.* Using (C2) then the unit (C4)/(C1):
`m(a,b) = m(a·e, e·b) = m(a,e)·m(e,b) = a·b`, so `m = ·`. And
`a·b = m(a,b) = m(e·a, b·e) = m(e,b)·m(a,e) = b·a`. ∎

Applying the Lemma to `(M_I, μ_I)` and `m_I` (common unit `e = id_I`): `m_I = μ_I` and **`M_I` is
commutative.** Associativity (C3) is then automatic (redundant), and `m_I` is uniquely determined.
∎(Step 2)

---

## 5. Step 3 — converse: every set of commutative monoids *is* a double comonoid

Let `c = ∑_{I∈O} y^{M_I}` with each `M_I` commutative. Define
`ε^⊗ : c → 𝟙` by the identities `e^⊗_I = id_I`, and `δ^⊗ : c → c×c` by the diagonal object map
`I ↦ (I,I)` and fibre lift `m_I = μ_I` (category composition). We check the cofunctor axioms:
- **(cod)**: all endos, both sides land at `I`. ✓
- **(id)**: `μ_I(id, id) = id`. ✓
- **(comp)**: `μ_I(g₁·h₁, g₂·h₂) = μ_I(g₁,g₂)·μ_I(h₁,h₂)` is precisely
  `(g₁h₁)(g₂h₂) = (g₁g₂)(h₁h₂)`, which holds **because `M_I` is commutative**
  (`g₁h₁g₂h₂ = g₁g₂h₁h₂`). ✓  *(This is the one place commutativity is used — the same equation that
  Eckmann–Hilton extracted.)*

The comonoid laws (coassoc, counit) for `δ^⊗` are associativity/unitality of `μ_I`. Everything is
per-fibre — the diagonal object map only ever lifts arrows out of `(I,I)`, which stay at `(I,I)` —
so there is no cross-object obstruction. Hence `(c, δ^⊗, ε^⊗)` is a `⊗`-comonoid in `Cat#`, i.e. a
double comonoid. ∎(Step 3)

---

## 6. Theorem and corollaries

**Theorem.** For a directed container `c` (`◁`-comonoid / small category `𝓒`) in the normal duoidal
category `(Poly, ◁, ⊗)` with comparitor `Indep`:

1. **(weak / factoring)** `δ^◁` factors through `Indep_{c,c}` ⟺ `𝓒` is a *set of monoids* (a
   coproduct of one-object categories). The factor is unique, with fibre map the composition.
2. **(strong / double comonoid)** `c` is a **double comonoid** ⟺ `𝓒` is a *set of commutative
   monoids*. The `⊗`-comonoid structure is then **unique**: counit = identities, comultiplication =
   composition, and `m_I = μ_I` on every fibre.

**Corollary (the target, corrected).** The degenerate polynomials are strict special cases:
- `y^A` (one object, monoid `A`) is a double comonoid **iff `A` is commutative** — so
  `y^{S_3}`, `y^{T_2}` are *not* double comonoids, contradicting the target's "all `y^A`".
- `Ay` (discrete, all fibres trivial) is always a double comonoid (trivial monoids are commutative).
- Multi-object examples such as `2y² = {ℤ/2, ℤ/2}` are double comonoids **excluded** by the target.

Hence `{degenerate}  ⊊  {sets of commutative monoids} = {double comonoids}  ⊊  {sets of monoids} =
{factoring}`; the target's identification of the middle class with `{degenerate}` fails on both
containments.

**Why the intuition ("comonoids run against the lax map, so descend only when `Indep` is iso")
was too crude.** `Indep_{c,c}` iso *is* the degenerate diagonal locus (Eq. 33). But *descent does
not require `Indep` invertible* — only that `δ` land in the order-independent image (the constant-`j`
positions). That image is available for **any** set of monoids, so the boundary is not Eq. (33).
The genuine cut is one level deeper: the *interchange* between composition and the descended
comultiplication is an Eckmann–Hilton square, and it collapses precisely to commutativity. *Fair is
foul: the invertibility locus was a decoy; the real gate is Eckmann–Hilton.*

---

## 7. Honesty ledger — gaps, load-bearing facts, novelty

**Load-bearing structural fact (§2).** "Double comonoid in a duoidal `𝓥` = `⊗`-comonoid object in
`(Comon_◁ 𝓥, ⊗)`" (Aguiar–Mahajan; comonoids-in-comonoids) and "the lift of `⊗` to `Cat#` is the
product of categories" (Niu–Spivak Prop. 8.79). I use these as cited; both are standard. The entire
argument is then elementary cofunctor bookkeeping + Eckmann–Hilton. If one instead *defines* a
double comonoid by the four Aguiar–Mahajan diagrams directly in `Poly`, Steps 1–3 reproduce the same
equations (C1)–(C4) on each fibre (the interchange `ζ` restricted to constant-`j` positions is the
homomorphism law (C2)); I have checked this by hand on `y^A` and it agrees. This is the only place a
skeptical reader should double-check; I flag it rather than hide it.

**Computational verification (done, 2026-07-15).** Exhaustive brute-force over
`m : A×A → A` for a monoid library — ℤ/2, ℤ/3, ℤ/4, V₄, the min/AND monoid (all commutative), and
`T_2` (transformation monoid, order 4), the order-3 left-zero-plus-identity monoid, and `S_3`
(order 6, via C2-pruned backtracking — a genuine exhaustive negative, not a spot-check) — confirms
under the correct interchange (C2) [= homomorphism from the *product* monoid]:

| monoid | commutative? | valid `m` exists? | #valid `m` | forced `m=μ`? |
|---|---|---|---|---|
| ℤ/2, ℤ/3, ℤ/4, V₄, min | yes | **yes** | 1 | yes |
| `T_2`, LZ₃, `S_3` | no | **no** | 0 | — |

So a solution exists **iff** the monoid is commutative, and then `m = μ` uniquely. (C1)+(C2)+(C4)
alone already force this — dropping associativity (C3) never enlarges the solution set, in every
library case — matching the Lemma. *Guardrail recorded:* the check also verified that the
same-pairing misreading of (C2) is a tautology satisfied by every monoid, confirming the interchange
grouping in §4 is the load-bearing one. Scripts: `scratch/double_comonoid*.py`, `scratch/s3_correct.py`,
`scratch/lz3.py`.

**Novelty (scoped, per the audit).** Spivak owns: `Indep` (Eq. 32), its iso-locus (Eq. 33 = the
degenerate diagonal), the `⊗`-comonoid classification ("sets of monoids"), and footnote 16
(`Poly_cart` no-go). The **delta is**: (i) the *converse/descent* analysis, (ii) the identification
of the compatibility as a **fibrewise Eckmann–Hilton** law, hence (iii) the corrected classification
**"double comonoids = sets of commutative monoids"** and the explicit refutation of the "degenerate"
target in both directions. This is a genuine correction, not a reproof. Registry
`comparitor-comonoid-nogo`: promote to `proved` with the **restated** theorem; keep the original
"degenerate" phrasing marked as a dead end (`reason`: false both directions — see §6).

**No remaining mathematical gap** for the `Cat#`-internal definition of double comonoid (§2). The
only caveat is the definitional one above, which I have cross-checked on `y^A`.
