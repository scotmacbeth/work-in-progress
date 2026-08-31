# Bare ⊗-comonoids in Poly are exactly the *families of monoids*

**MacBeth — 2026-07-17 (PROVE deep-work session)**

> **Headline.** A container `c` is a comonoid for the **Dirichlet (parallel) tensor**
> `(Cont, ⊗, y)` — with *no* `◁`/directed-container structure imposed — **if and only if every
> direction set `c[s]` carries a monoid structure**. The comultiplication is forced on shapes (the
> diagonal `s ↦ (s,s)`) and *is* a fibrewise binary operation on directions; coassociativity =
> associativity, counitality = unitality. So
>
> **⊗-comonoids in Poly = containers `c = Σ_{s∈S} y^{M_s}` with each `M_s` a monoid = *sets of
> monoids* = an `S`-indexed family of monoids.** Cocommutative ⊗-comonoids = families of *commutative*
> monoids. Categorically: `Comon(Cont, ⊗, y) ≅ Fam(Mon^op)`, mirroring `Cont ≅ Fam(Set^op)`.
>
> This answers the **Poly/⊗-comonoid slice of Niu–Spivak Chapter 9, Question 5** (verbatim: "Consider
> the ×-(co)monoids and ⊗-(co)monoids in three categories: Poly, Cat♯, and Mod. … perhaps
> characterize them or create a theory of them"), which is *open* in the book. It also **completes and
> corrects** the `comparitor-double-comonoid` result: the *bare* ⊗-comonoid is strictly larger than
> the double comonoid — all monoids, not just commutative ones, over an arbitrary shape set — exactly
> as `comparitor-comonoid-nogo` predicted the bare problem would be "strictly larger and cleaner."

---

## 1. Setup and conventions

A **container / polynomial functor** is `c = Σ_{s ∈ S} y^{c[s]}`: a set of **shapes** `S = c(1)` and
for each `s` a set of **directions** `c[s]`. A **Poly morphism** `f : p → q` is a *forward* map on
shapes `f₁ : S_p → S_q` together with, for each `s`, a *backward* map on directions
`f♯_s : q[f₁ s] → p[s]`. Composition of `p --f--> q --g--> r` is `(gf)₁ = g₁∘f₁` and
`(gf)♯_s = f♯_s ∘ g♯_{f₁ s}` (backward maps compose contravariantly). This is `Cont ≅ Fam(Set^op)`
(Spivak–Garner–Fairbanks Prop. 3.6; my note `2026-07-14-day-family-classification.md` Lemma 1.2).

**Dirichlet tensor `⊗ = Day(Set, ×, 1)`** (Niu–Spivak Prop. 3.79):
```
    (p ⊗ q) = Σ_{(s,t) ∈ S_p × S_q} y^{p[s] × q[t]},        unit  y = y^1.
```
For morphisms `f : p→p'`, `g : q→q'`: `(f⊗g)₁(s,t) = (f₁ s, g₁ t)` and
`(f⊗g)♯_{(s,t)} = f♯_s × g♯_t : p'[f₁ s]×q'[g₁ t] → p[s]×q[t]`. The tensor is symmetric.

**Definition.** A **⊗-comonoid** is `(c, ε, δ)` with `ε : c → y`, `δ : c → c⊗c` Poly morphisms
satisfying counitality `(ε⊗id)∘δ = id = (id⊗ε)∘δ` and coassociativity `(δ⊗id)∘δ = (id⊗δ)∘δ`
(modulo the canonical associator/unitors of `⊗`, which are identities on shapes/positions up to the
evident re-bracketing). **No `◁` structure is assumed.** Contrast the *double* comonoid of
`2026-07-15-comparitor-double-comonoid.md`, which is a ⊗-comonoid *object in `Cat♯ = Comon_◁(Poly)`*.

---

## 2. Unpacking the data

Write the two morphisms in coordinates.

**Counit `ε : c → y`.** The shape map `S → 1` is forced. The backward map is, for each `s`, a map
`ε♯_s : y[∗] = 1 → c[s]`, i.e. **a distinguished element `e_s ∈ c[s]`**. (In particular `ε` exists iff
every `c[s] ≠ ∅` — automatic once each fibre is a monoid.)

**Comultiplication `δ : c → c⊗c`.** The shape map is a function `δ₁ : S → S×S`, say
`δ₁(s) = (l s, r s)`. The backward map is, for each `s`,
`δ♯_s : (c⊗c)[δ₁ s] = c[l s] × c[r s] → c[s]`.

So a ⊗-comonoid is exactly the data `(δ₁ = (l,r),  {δ♯_s},  {e_s})`. The three comonoid laws pin
this down completely, as follows.

---

## 3. The counit laws force the diagonal on shapes and unit elements on directions

Compute `(ε⊗id)∘δ : c → y⊗c ≅ c` and demand it equal `id_c`.

*Shapes.* `s ↦ (l s, r s) ↦ (∗, r s) ≅ r s`. Identity ⟹ **`r = id`**. Symmetrically
`(id⊗ε)∘δ` gives shape map `l`, so **`l = id`**. Hence

> **`δ₁(s) = (s, s)` — the diagonal.** This is the "shapes always carry the unique cartesian comonoid
> structure" of the conjecture: `×` on `Set` is cartesian, so its Day-image on shapes admits only the
> diagonal comultiplication.

With `δ₁` diagonal, `δ♯_s` is now a binary operation
```
    m_s := δ♯_s : c[s] × c[s] → c[s].
```

*Directions.* Under `δ₁ = diag`, the morphism `ε⊗id : c⊗c → y⊗c ≅ c` has, at shape `s`, backward map
`c[s] → c[s]×c[s]`, `v ↦ (e_s, v)` (this is `ε♯_s × id`). Composing with `δ♯_s = m_s` and demanding
`= id` gives **`m_s(e_s, v) = v`**. Symmetrically `(id⊗ε)∘δ = id` gives **`m_s(v, e_s) = v`**. So

> **`e_s` is a two-sided unit for `m_s`.**

---

## 4. Coassociativity is associativity, fibrewise

With `δ₁` diagonal, both `(δ⊗id)∘δ` and `(id⊗δ)∘δ` are morphisms `c → c⊗c⊗c` with shape map
`s ↦ (s,s,s)` and backward map at `s` valued in `(c⊗c⊗c)[s,s,s] = c[s]³ → c[s]`. Composing
Poly-morphisms coordinatewise (`δ⊗id` has backward `m_s × id`; `id⊗δ` has backward `id × m_s`):
```
   (δ⊗id)∘δ  at s :  (x,y,z) ↦ m_s(m_s(x,y), z),
   (id⊗δ)∘δ  at s :  (x,y,z) ↦ m_s(x, m_s(y,z)).
```
Coassociativity ⟺ **`m_s(m_s(x,y),z) = m_s(x,m_s(y,z))` — `m_s` is associative.**

There is **no cross-shape condition** (a Poly morphism is a shape map plus an *independent* family of
backward maps), and **no cocommutativity** is forced (symmetry of `⊗` makes ⊗-comonoids a symmetric-
monoidal notion, but a comonoid need not be cocommutative). Hence each `(c[s], m_s, e_s)` is an
*arbitrary* monoid.

**Converse.** Given any container `c` with a chosen monoid `(c[s], m_s, e_s)` on every fibre, define
`ε` by `e_s` and `δ` by the diagonal shape map and backward maps `m_s`. §§3–4 read backwards show all
three laws hold. ∎

---

## 5. Theorem

**Theorem.** For a container `c = Σ_{s∈S} y^{c[s]}`, the following data are in natural bijection:

1. ⊗-comonoid structures `(ε, δ)` on `c` in `(Cont, ⊗, y)`;
2. choices, for every shape `s ∈ S`, of a monoid structure `(m_s, e_s)` on the direction set `c[s]`.

The correspondence is: `δ₁ =` diagonal, `δ♯_s = m_s`, `ε♯_s = e_s`. Consequently the **⊗-comonoids in
Poly are exactly the *families of monoids*** — containers `Σ_{s∈S} y^{M_s}` with each `M_s` a monoid
("sets of monoids"). The structure is *not* unique on a given `c` (a fibre of size `n` has as many
comonoid structures as there are monoids on an `n`-element set).

**Categorical form.** A ⊗-comonoid morphism `h : c → d` is a Poly morphism commuting with `ε, δ`;
unwinding (§Appendix), that is exactly a forward shape map `h₁ : S_c → S_d` together with, for each
`s`, a **monoid homomorphism** (backward) `h♯_s : M^d_{h₁ s} → M^c_s`. Hence
```
    Comon(Cont, ⊗, y)  ≅  Fam(Mon^op),
```
the free-coproduct completion of `Mon^op` — the *exact* monoid-enriched upgrade of `Cont ≅ Fam(Set^op)`.
The full subcategory of **cocommutative** ⊗-comonoids is `Fam(CMon^op)` (commutative monoids).

**Corollaries.**
- `y^A` (one shape) is a ⊗-comonoid iff `A` carries a monoid structure, and the ⊗-comonoids on `y^A`
  are exactly the monoids on `A` — *all* of them, including non-commutative (e.g. `y^{S_3}` via the
  group law). Contrast the *double* comonoid, where `y^A` requires `A` **commutative**
  (`comparitor-double-comonoid` §6).
- `A·y` (linear, all fibres singletons) has a unique ⊗-comonoid structure (the trivial monoid on each
  singleton) — for *every* `A`.
- The three layers, side by side, over the same carrier `c`:

  | structure on `c` | is | reference |
  |---|---|---|
  | ⊗-comonoid (bare) | family of **monoids** | **this note** |
  | ◁-comonoid (bare) | small **category** | Ahman–Uustalu; Niu–Spivak Thm 7.28 |
  | double (⊗ **and** ◁) | set of **commutative** monoids | `comparitor-double-comonoid` |

  The bare ⊗ layer is strictly larger than the double layer (drops both commutativity *and* the
  single-fibre-per-object rigidity that the category structure would add). This is precisely the
  "strictly larger and cleaner" the PROVE brief and `comparitor-comonoid-nogo` anticipated.

---

## 6. Verification (computation is conviction)

`scratch/bare-comonoid/verify.py` enumerates *all* candidate `(δ₁, {δ♯_s}, {e_s})` on a container and
checks the comonoid laws by **direct composition of Poly-morphisms** — with no reference to the word
"monoid" — then compares the surviving set against an *independent* brute-force enumeration of
associative-unital operations on the fibres.

| container | ⊗-comonoids found (direct law-check) | monoids on fibres (independent) | match |
|---|---|---|---|
| `y^1` | 1 | 1 | ✓ |
| `y^2` | 4 | 4 | ✓ |
| `y^3` | 33 | 33 | ✓ |
| `[1,2]` (fibres of size 1, 2) | 4 = 1·4 | 1·4 | ✓; all `δ₁` diagonal |

Two things the run *confirms independently of the hand-proof*: (i) `δ₁` is forced to the diagonal in
every solution; (ii) the count matches the **unfiltered** monoid count — the law-check imposes
associativity only, never commutativity — so **no cocommutativity is forced** (order-3 monoids include
non-commutative ones, and they all appear). Had cocommutativity been forced, the comonoid count would
be strictly below the monoid count.

---

## 7. Honesty ledger — novelty, attribution, and a correction

**Cited, not mine.**
- `⊗ = Day(Set, ×)`, the formula `(p⊗q)[s,t] = p[s]×q[t]`, distributivity over `+` — **Niu–Spivak
  arXiv:2312.00990 Prop. 3.79** (full-PDF deep-read today, §3.5). The `Cont ≅ Fam(Set^op)` framing —
  SGF Prop. 3.6; my `day-family-classification` Lemma 1.2.
- The *question*: **Niu–Spivak Ch. 9, Question 5** (New Horizons, p. 349, verbatim above) explicitly
  asks to characterize ⊗-comonoids in Poly (and Cat♯, Mod) — i.e. it is **open** in the book.

**What the book does *not* contain (checked in the full PDF today).** There is **no** classification
of ⊗-comonoids in Poly. The two nearby items are different:
- **Remark 3.78** flags ⊗-**monoids** in Poly ("collective semantics … aggregate contributions") as
  *future work* — monoids, the dual notion, not comonoids.
- **§8.2.4 / Prop. 8.79** ("Parallel product comonoids") shows `⊗` extends to a monoidal structure
  **on `Cat♯`** with `U : Cat♯ → Poly` strong monoidal (the ⊗-of-categories = product of categories).
  That is the ingredient of the *double*-comonoid analysis, **not** a classification of bare
  ⊗-comonoids in Poly. The section title is a false friend.

**Correction to a prior note (recorded honestly).** `comparitor-double-comonoid.md` §7 wrote "Spivak
owns … the ⊗-comonoid classification ('sets of monoids')." That attribution is **wrong**: the book
classifies neither ⊗-comonoids nor ⊗-monoids in Poly (Q5 is open; Rmk 3.78 is future work). The phrase
"set of monoids" there is *MacBeth's own* Step-1 conclusion inside the `Cat♯` computation, not a cited
Spivak result. I have flagged this in the registry and memory.

**Novelty of this note (scoped).** The delta is the explicit, proved characterization **"bare
⊗-comonoids in Poly = families of monoids," `Comon(Cont,⊗,y) ≅ Fam(Mon^op)`**, answering the Poly/⊗
slice of Q5, together with the three-layer comparison (bare-⊗ / bare-◁ / double). The *argument* is
elementary — an unwinding of the comonoid axioms in container coordinates — so I grade the theorem
**`proved`** and describe it as *"answers an explicitly open question by an elementary computation,"*
not as a deep theorem. Dorta–Jarvis–Niu (2305.05655) classify ◁-comonoids in `ΣΠ`-containers but give
**no** classification of Day/⊗-comonoids (sources.json note, deep-read), so the Poly/⊗ answer is not
theirs either.

**No remaining mathematical gap.** The one abstract cross-check worth stating: the result is the
comonoid instance of the folklore "(co)monoids in a Day convolution over a fibrewise-cartesian base
are fibrewise (co)monoids." Because `× : Set²→Set` is cartesian, the shape-level comonoid is forced
(diagonal) and *all* content is a fibrewise comonoid in `Set^op` = a monoid in `Set`. I derived it by
hand rather than invoke a general Day-comonoid theorem I have not written down; §6 corroborates.

---

## Appendix — ⊗-comonoid morphisms are backward monoid homomorphisms

Let `c, d` be ⊗-comonoids (fibre monoids `M^c_s`, `M^d_t`). A morphism of ⊗-comonoids is a Poly
morphism `h = (h₁ : S_c → S_d, {h♯_s : d[h₁ s] → c[s]})` making the counit and comultiplication
squares commute.

*Counit square* `ε_c = ε_d ∘ h`, on directions at `s`: `1 → d[h₁ s] → c[s]` sends `∗ ↦ e^d_{h₁ s} ↦
h♯_s(e^d_{h₁ s})`, and this must equal `e^c_s`. So **`h♯_s` preserves the unit**.

*Comultiplication square* `δ_d ∘ h = (h⊗h) ∘ δ_c`, on directions at `s` (both sides have shape
`h₁ s ↦ (h₁ s, h₁ s)`):
```
   δ_d ∘ h      :  (u,v) ↦ h♯_s( m^d_{h₁ s}(u,v) )          [multiply in d, then pull back]
   (h⊗h) ∘ δ_c  :  (u,v) ↦ m^c_s( h♯_s u, h♯_s v )          [pull back, then multiply in c]
```
Equality for all `u,v ∈ d[h₁ s]` says **`h♯_s` preserves multiplication**. Hence each `h♯_s` is a
monoid homomorphism `M^d_{h₁ s} → M^c_s`, *backward* along `h₁`. That is exactly a morphism in the
free coproduct completion `Fam(Mon^op)`: a reindexing forward on the base, a homomorphism backward on
each fibre. Together with §5.2 this gives the isomorphism of categories `Comon(Cont, ⊗, y) ≅
Fam(Mon^op)` (and `Fam(CMon^op)` on the cocommutative full subcategory). ∎

