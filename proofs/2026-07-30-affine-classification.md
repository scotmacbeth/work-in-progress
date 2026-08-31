# Which monads give an effect–coeffect arrow category? The non-branching class is *writer + absorbing exceptions*, and E2′ holds throughout it

**MacBeth — PROVE session, 2026-07-30.** Sequel to `2026-07-29-effect-coeffect-arrows.md`
(Theorem A: the arrows `p ⇝ q := Cont(G_M p, T_M q)` form the biKleisli category **iff `M`
is non-branching**) and `...-arrows-first.md` (Theorem B: genuine Hughes arrow / Freyd
category iff non-branching). Those give the *negative* face — branching is the obstruction.
This session supplies the **positive** face Neil asked for: **a clean, named class of monads
that DO give the arrow category**, and closes the inherited **E2′ general-`j`** gap for the
whole class.

---

## Answer in one line

> **The polynomial (∏-cointerpretation) non-branching monads are exactly `M X = E + A×X`
> where `A` is a monoid and `E` is a left `A`-set — the *writer monad `A` with a set `E` of
> absorbing exceptions on which the log acts*. For every such `M`, the compositor `κ`
> satisfies all four mixed-distributive-law axioms (in particular the associativity axiom
> E2′), so the effect–coeffect arrow category exists. Thus the mode-3 obstruction acquires a
> positive statement: *the arrow calculus exists iff the effect monad is exception–writer.***

A second, strictly larger classification appears one level up: **at the level of arbitrary
Set-monads**, the functors `E + A×(−)` that carry a monad structure are exactly the **monoids
`N = E ⊔ A` with unit in `A` and `E` a two-sided ideal of left zeros** — the multiplication
of two unary shapes is allowed to *abort* into `E`. These aborting monads are genuine Set-
monads but are **not cartesian** (their `μ` destroys a leaf), so Ahman–Bauer's `T_M` is not
defined for them and they fall outside the arrow story. The cartesian ones are precisely the
non-aborting ones = writer + absorbing exceptions.

---

## 0. Setup and statement

Fix a polynomial (container) Set-monad, presented as `M X = Σ_{s ∈ M1} X^{ar(s)}` with shape
set `M1` and arity `ar : M1 → Set`. "**Non-branching**" means `|ar(s)| ≤ 1` for every shape
`s` (equivalently every `m ∈ M X` has support `|lv(m)| ≤ 1`). Recall the two `Cont`-liftings
of `2026-07-25`/`2026-07-27`:

* coeffect comonad `G_M(S,P) = (S, M∘P)`;
* effect monad `T_M(S,P) = (M S, P^⋆)`, `P^⋆(m) = ∏_{b ∈ lv(m)} P(x_b)` (Ahman–Bauer,
  arXiv:2409.17664, Thm 6.3), defined for `M` in the **∏-cointerpretation / cartesian** class.

An **effect–coeffect arrow** `p ⇝ q` is a `Cont`-morphism `G_M p → T_M q`; composition is the
biKleisli composite with compositor `κ : G_M T_M ⇒ T_M G_M` (the lax product-comparison on
positions). Theorem A (07-29): the arrows form a category iff `κ` satisfies E1′–E4′ iff `M`
is non-branching, with **E2′ (the mult-`T`/associativity axiom) the sole obstruction**.

**Theorem T1 (positive classification).** For a cartesian Set-monad `M` the following are
equivalent:
1. the arrow category `Arr_M` exists;
2. `M` is non-branching;
3. `M ≅ E + A×(−)` as a functor, for some sets `E`, `A`;
4. `M` is a **writer-with-absorbing-exceptions** monad: `M X = E + A×X` with `(A,·,e)` a
   monoid, `(E, ⊙)` a left `A`-set, `η_X(x) = (e, x)` (writer unit), and multiplication
   ```
      μ_X : E + A×(E + A×X) → E + A×X,
      inl e'                ↦ inl e'                        (outer exception absorbs)
      inr(a, inl e')        ↦ inl (a ⊙ e')                 (log acts on the exception)
      inr(a, inr(a', x))    ↦ inr(a·a', x)                 (writer multiplication).
   ```

`(1)⇔(2)` is Theorem A. This note proves `(2)⇔(3)⇔(4)`.

---

## 1. `(2)⇔(3)`: non-branching = degree-≤1 polynomial

A polynomial functor is `M X = Σ_{s∈M1} X^{ar(s)} = Σ_{s} \mathrm{Set}(ar(s), X)`. Suppose
`|ar(s)| ≤ 1` for all `s`. Partition the shape set by arity,
```
      E := { s ∈ M1 : ar(s) = ∅ },    A := { s ∈ M1 : |ar(s)| = 1 }.
```
For `s ∈ E`, `X^{ar(s)} = X^∅ = 1`; for `s ∈ A`, `X^{ar(s)} = X^1 = X`. Hence
```
      M X ≅ Σ_{s∈E} 1  +  Σ_{s∈A} X  =  E + A×X,
```
naturally in `X`. Conversely `E + A×(−) = Σ_{s∈E} y^0 + Σ_{s∈A} y^1` has all arities `≤ 1`.
So `M1 = E ⊔ A`, `A` = the unary shapes, `E` = the nullary shapes. ∎

*(Remark on "affine".* This is **degree ≤ 1** = *affine in the polynomial-functor sense*
(constant term `E` + linear term `A×X`). It is **not** "affine" in Kock's sense `M1 ≅ 1`:
here `M1 = E + A` may be arbitrarily large. Indeed `M1 ≅ 1` forces `E = ∅, |A| = 1`, i.e.
`M = \mathrm{Id}`. The two senses coincide only trivially; I use "**linear/affine polynomial
monad**" for arity ≤ 1 and flag the clash. This resolves the concern flagged in `PROVE.md`.)*

---

## 2. `(3)⇔(4)`: the monad-structure pin

### 2.1 Every monad on `E + A×(−)` forces the writer unit and a monoid-shaped `μ`

Let `M X = E + A×X` carry a monad `(η, μ)`.

**Unit.** A natural transformation `η : \mathrm{Id} ⇒ M` has, by naturality (Yoneda for the
domain `\mathrm{Id}`), one of two forms: a constant `x ↦ inl e₀` (`e₀ ∈ E`), or `x ↦ inr(a₀,
x)` (`a₀ ∈ A`) — the `X`-component of the linear part must be the identity, and the `A`- and
`E`-labels must be constant. A constant unit `inl e₀` violates the left-unit law (`μ∘Mη = id`
would force `id` constant), so
```
      η_X(x) = inr(e₀, x)    for a distinguished  e₀ ∈ A.        (writer unit)
```

**Multiplication.** `M M X = E ⊔ A×E ⊔ A×A×X`. Naturality in `X` (again Yoneda: a natural
map into the constant part `E` is `X`-independent; a natural map into `A×X` fixes the `X`
coordinate) forces `μ` to have the schematic form
```
      inl e            ↦ inl (ρ e),                ρ : E → E
      inr(a, inl e)    ↦ inl (σ(a,e)),             σ : A×E → E
      inr(a, inr(a',x))↦ { inl(τ(a,a'))  or  inr(ν(a,a'), x) },   (a,a')↦γ(a,a')∈E+A
```
with `γ : A×A → E + A` (writing `γ(a,a') = inl τ(a,a')` or `inr ν(a,a')`). The variable `x`
is **carried** whenever the outer/inner `A`-labels multiply into `A`, and **dropped** when
they abort into `E`.

**Assemble a binary operation on `N := E ⊔ A`.** Define `⊗ : N×N → N` by
```
      e ⊗ n   = e            (e ∈ E : left absorbing, from μ(inl e)=inl ρe with ρ=id, below)
      a ⊗ e'  = σ(a,e')      (∈ E)
      a ⊗ a'  = γ(a,a')      (∈ E + A).
```

**Left unit law** `μ∘Mη = id` gives `ρ = id_E` and `γ(a, e₀) = inr(a)` (multiplying by the
unit on the right stays in `A` and returns `a`). **Right unit law** `μ∘ηM = id` gives
`σ(e₀, e) = e` and `γ(e₀, a) = inr(a)`. So `e₀` is a two-sided unit for `⊗`, lying in `A`.
**Associativity** `μ∘Mμ = μ∘μM` unwinds (the variable `x` being merely carried) to exactly the
associativity of `⊗`: for the deepest spine `(a₁,a₂,a₃,x)` both bracketings compute the same
`N`-product `a₁⊗a₂⊗a₃`, and — because `E` is a left-absorbing ideal (see below) — the variable
is carried by both iff that product lands in `A`. Conversely, given any monoid `(N,⊗,e₀)` with
`e₀ ∈ A` and `E` a two-sided ideal of left zeros, the displayed `η, μ` satisfy the monad laws.

Note `E` is automatically a **two-sided ideal of left zeros**: `e⊗n = e ∈ E` (left zero, hence
left ideal); and `n⊗e` is again a left zero (`(n⊗e)⊗m = n⊗(e⊗m) = n⊗e`), hence in `E` when `E`
is *all* left zeros — the codomain of `σ` records exactly this (`a⊗e ∈ E`).

**Theorem (Set-monad level).** *Monad structures on the functor `E + A×(−)` are in bijection
with monoid structures on `N = E ⊔ A` whose unit lies in `A` and in which `E` is a two-sided
ideal consisting of left zeros.*

> **Correction to PROVE.md.** This is **weaker** than "`A` is a monoid": `A` need **not** be a
> submonoid, because `γ : A×A → E + A` may *abort* — two unary shapes may multiply to an
> exception (e.g. the nilpotent monoid `{e, z, 0}` with `z² = 0 ∈ E`, giving `M X = 1 + 2×X`).

### 2.2 Verification (`affine_classify.py`)

Enumerating all candidate `(e₀, σ, γ)` and comparing the predicate "monad laws hold" with
"`⊗` is a monoid with unit in `A` and `E` a left-zero ideal":

| `\|E\|` | `\|A\|` | candidates | #monad-laws | #monoid-laws | mismatch |
|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 1 | 2 | 1 | 1 | 0 |
| 0 | 2 | 32 | 4 | 4 | 0 |
| 1 | 2 | 162 | 6 | 6 | 0 |
| 2 | 1 | 12 | 1 | 1 | 0 |
| 2 | 2 | 8192 | 14 | 14 | 0 |
| 3 | 2 | 911250 | 46 | 46 | 0 |
| 1 | 3 | 786432 | 75 | 75 | 0 |

**Exact bijection, zero mismatches.** (Sanity: `|E|=1,|A|=1` → 1 structure = `Maybe`;
`|E|=2,|A|=1` → 1 = exception monad `E+(−)`; `|E|=0,|A|=2` → 4 = the four 2-element monoids.)

### 2.3 `(3)/(4)⇔` cartesianness: why the arrow class is exactly *non-aborting*

Ahman–Bauer's `T_M(S,P) = (M S, P^⋆)` requires `M` to be **cartesian** (∏-cointerpretation):
the multiplication `μ^M` must be a cartesian natural transformation, equivalently it neither
creates nor destroys leaves. For `M = E + A×(−)`:

* **Non-aborting** (`γ : A×A → A`, i.e. `A` a submonoid): a unary-over-unary shape
  `(a,(a',s))` maps to `(a·a', s)` — the single leaf `s` is **preserved**. Every case
  preserves leaf-count. `μ^M` is cartesian; `T_M` is a monad.
* **Aborting** (`γ(a,a') ∈ E` for some `a,a' ∈ A`): `(a,(a',s)) ↦ inl(τ(a,a'))` **destroys**
  the leaf `s`. `μ^M` is not cartesian. Then `T_M`'s multiplication `μ^T` would need a
  backward map `P^⋆(μ^M mm) → P^⋆(mm)`, i.e. `1 → P(s)` at the aborting shape — **no canonical
  choice** (ill-defined unless `|P(s)| = 1`). `T_M` is not a monad.

Hence, **within the class where `T_M` exists (the arrow story's standing assumption), the
non-branching monads are exactly the non-aborting ones**: `A` a submonoid of `N`, `E` a
two-sided ideal of left zeros. For a submonoid `A`, `σ` restricts to an action
`⊙ : A×E → E` which is unital (`e₀⊙e = e`) and associative (`a⊙(a'⊙e) = (a·a')⊙e`) by the
monoid laws of `N` — i.e. **`E` is a left `A`-set**. This is statement (4). ∎

**Verification (`affine_e2prime.py`).** `mu_cartesian` is `True` for `M = 2+3×X` (`A=ℤ/3`) and
`M = 1+2×X` (`A=ℤ/2`); `False` (with the destroyed leaf printed) for the nilpotent `z²=0`
monad and an auto-found aborting `|E|=2` monoid, whose `μ^T` indeed crashes for want of a
backward value.

*(The recognisable instance: with trivial action `a⊙e = e`, `M X = E + A×X` is the **writer
transformer `WriterT_A` applied to the exception monad `Exc_E`**: `WriterT_A(Exc_E)(X) =
Exc_E(A×X) = E + A×X`, with exceptions discarding the log. General `⊙` twists the discard by a
left `A`-action on `E`.)*

---

## 3. T2 — E2′ holds across the whole non-branching class

**Theorem T2.** For every cartesian non-branching `M` (equivalently every writer-with-
absorbing-exceptions `M X = E + A×X`) and every container `A`, the compositor
`κ : G_M T_M ⇒ T_M G_M` satisfies all four mixed-distributive-law axioms E1′–E4′; in
particular the associativity axiom **E2′** holds. Hence `Arr_M` is a category for the entire
class, not only for `Maybe`/`Writer`.

**Proof.** Non-branching means every element of every `M`-object has `≤ 1` leaf, so **every
`P^⋆`-product occurring in `T_M`, `T_M T_M`, `G_M T_M`, … is a product over `≤ 1` factor.**
Consequently `κ`'s backward map (the lax comparison `∏_b M(Z_b) → M(∏_b Z_b)`) is, shape by
shape, one of only two things:

* at a **unary** shape (one leaf `b₀`): `∏_b M(Z_b) = M(Z_{b₀})` and `M(∏_b Z_b) = M(Z_{b₀})`
  are the *same* set, and `κ` is the **identity** (rewrap the single factor);
* at a **nullary** shape (no leaf): `∏_b M(Z_b) = 1` and `M(∏_b Z_b) = M(1)`, and `κ` is the
  monad unit `η^M : 1 → M(1)` (the empty-product comparison).

Now read each axiom E1′–E4′ as an equality of `Cont`-morphisms. On **shapes** all four reduce
to the monad/comonad shape-laws of `M` (`η^M`, `μ^M` unit/associativity), which hold. On
**positions**, the only non-trivial content sits at unary shapes, where `κ = id`; there the
axiom collapses to the corresponding structural law of `M` carried on the single leaf —
for **E2′** this is precisely the **associativity of `μ^M` on that leaf**, i.e. associativity
of `⊗` in `N`, which holds because `N` is a monoid (§2). At nullary shapes every position set
involved is `1` (an empty product), so the positional equation is between maps into/out of a
terminal set and holds automatically. The `≥ 2`-leaf product-comparison — the *union-of-
products ≠ product-of-unions* discrepancy that breaks E2′ for branching `M` (07-27 `Pf`
witness) — **never forms**, because non-branching caps every product at one factor. Therefore
E1′–E4′ all hold. ∎

This is the conceptual closure of the "**E2′ general-`j`**" gap: for non-branching `M` the
reindexing `j` in `μ^T` is always the trivial (≤1-leaf) restriction, so the associativity
chase degenerates to `N`'s associativity. (The argument above derives **all four** κ-axioms
uniformly for non-branching `M` from the ≤1-factor degeneracy — it does not rely on the
reverse-κ E1′/E3′/E4′ having been checked for arbitrary `M`; E2′ is the one that had been left
open for the general non-branching case, and it now joins the other three.)

**Verification (`affine_e2prime.py`).** For `M = 2+3×X` (`A = ℤ/3`, `|E| = 2`, `|A| = 3` — the
`|E|≥2, |A|≥2` case `PROVE.md` asked for) and `M = 1+2×X` (`A = ℤ/2`), the reverse-`κ` checker
reports **E1′, E3′, E4′, E2′ all PASS** on `U1`, `A1 = ({a,b}; a:2, b:1)` and
`A3 = ({a,b}; a:2, b:2)` (branching-*capable* containers), and the biKleisli arrow composite
is **associative with zero violations** (15625 triples for `2+3×X`, 729 for `1+2×X`) with the
identity laws holding. For the aborting monads the checks are correctly inapplicable (`T_M`
undefined, §2.3).

---

## 4. The finished mode-3 picture (for the paper / grant)

Combining with Theorems A and B:

> **Effect–coeffect arrows on containers.** For a cartesian Set-monad `M`, the arrows
> `p ⇝ q = Cont(G_M p, T_M q)` form a **category** — indeed a **Hughes arrow / Freyd
> category** over `(Cont, ×)` — **iff `M` is non-branching**, i.e. iff `M` is a
> **writer-with-absorbing-exceptions monad `E + A×X`** (`A` a monoid, `E` a left `A`-set).
> For such `M` the compositor `κ` satisfies E1′–E4′ everywhere (E2′ by §3). For branching `M`
> the arrow category fails (E2′/associativity breaks; and `T_M` even loses its natural
> strength — Theorem B). One level up, `E + A×(−)` is a *Set*-monad more generally — for any
> monoid on `E ⊔ A` with `E` a left-zero ideal — but the *aborting* ones are non-cartesian and
> carry no `T_M`, so the arrow calculus is genuinely a phenomenon of the *writer+exception*
> monads.

The mode-3 row of the three-modes table thus reads, with a positive class attached:

| mode | composition data | exists iff | the monads |
|---|---|---|---|
| directed / ZS | `C ⋈ D` | `[ω]=0 ∈ H²` | closing bases |
| state / Workers | `ΔS ⊗ p → q` | always (grade `S×T`) | any state `S` |
| **effect–coeffect** | arrow `G_M p → T_M q` | **`M` non-branching** | **`E + A×X` = writer `A` + absorbing exceptions `E`** |

---

## 5. Novelty / attribution

* **Degree-≤1 polynomial functors, `E + A×(−)`**: standard polynomial-functor material
  (Gambino–Kock; Kock, *Notes on polynomial functors*). **Cartesian = polynomial monad** =
  monad in `(Poly, ◁)` (Gambino–Kock). **Writer transformer / exception monad**: folklore.
* **`T_M`** = Ahman–Bauer arXiv:2409.17664 Thm 6.3 (cartesian `M`). **`G_M`, `κ`, Theorem A,
  B** = my 07-25/27/29 results (proved). **Affine-monad (`M1≅1`) vs arity-≤1** distinction:
  see Kock; Jacobs; Gavranović *Affine monads*. I use neither as the class — the arrow class
  is the *arity-≤1 cartesian* one, which is `M1`-unrestricted.
* **Contribution (MacBeth, this session):** (i) the **positive classification** — the arrow
  category exists iff `M = E + A×X` is a *writer-with-absorbing-exceptions* monad (`A` monoid,
  `E` left `A`-set); (ii) the **two-level pin**: at Set-monad level, monoids `N=E⊔A` with `E`
  a left-zero ideal (aborting allowed, correcting PROVE.md), and the identification of the
  cartesian sub-class (non-aborting) as exactly the arrow class, with the aborting ones excluded
  because they destroy leaves and kill `T_M`; (iii) **T2** — E2′ holds across the whole
  non-branching class (the product-comparison degenerates to a ≤1-factor rewrap, so E2′ = `N`'s
  associativity), closing the inherited `general-j` gap; (iv) the corrected "affine" terminology.

---

## 6. Gaps (precisely stated)

1. **Fully symbolic E1′/E3′/E4′ at nullary shapes.** §3 argues these collapse to trivial
   maps into/out of terminal sets; a line-by-line coordinate chase over an arbitrary container
   is not written out (it is degenerate — no ≥2-leaf product ever forms — and is machine-
   verified on `U1, A1, A3`). The mathematically live axiom, E2′, is given in full.
2. **`⊗`-Dirichlet tensor.** As in Theorem B, the Freyd base is cartesian `×`; the writer
   `A`-set structure interacts with `×` cleanly (Theorem B), but the non-cartesian Dirichlet
   `⊗` arrow story is a separate question, not a gap here.
3. **Non-`∏` cointerpretations.** Out of scope, as throughout the entwining program.
4. **Lean.** The Set-monad-level bijection (§2, `monad ⟺ monoid-with-left-zero-ideal`) and the
   cartesian bifurcation are natural next `LEAN` targets; the unit-law fragment of the arrow
   category is already Lean-verified (`BiKleisli.lean`).
