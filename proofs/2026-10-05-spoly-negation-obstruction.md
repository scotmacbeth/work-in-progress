# The container tangent structure has no fiberwise negation: SPoly/∂ carries no scalar ring object, and the Cartan calculus does not descend

**MacBeth (Kodamai / Ghani group) — 2026-10-05**

## Problem

The existence and uniqueness of the container tangent structure are settled:
the AAGM one-hole derivative `∂` is the unique nontrivial representable first-order
tangent structure `T = (−)◁D`, `D = y+εv`, on finite-support polynomial functors
(`proofs/2026-10-02-tangent-container-cdc.md`, `proofs/2026-10-03-tangent-uniqueness-spoly.md`;
`[[tangent-container-derivative-is-cdc]]`, `[[tangent-uniqueness-spoly-finite-support]]`).

This note **delimits** the differential geometry of containers. The
Aintablian–Blohmann program (arXiv:2607.11169, 2609.05963) builds the full Cartan
calculus — exterior differential `d`, inner/contraction derivative `ι`, Lie
derivative `L`, and the Lie–Rinehart / Chevalley–Eilenberg assembly — from a tangent
category **plus a scalar ring object** `R`. Their decisive structural fact is that an
`R`-module structure on the tangent bundle forces **fiberwise additive inverses**,
i.e. forces a *Rosický* tangent category. So the entire program for containers hinges
on one question:

> **Do tangent vectors in SPoly have negatives?**

**Main theorem (negative).** The additive bundle of the tangent structure
`T = (−)◁D` on finite-support polynomial functors is a bundle of commutative monoids
that does **not** admit fiberwise additive inverses. Consequently `SPoly/∂` is **not**
a Rosický tangent category and carries **no** scalar ring object `R` in the sense of
arXiv:2607.11169; the Aintablian–Blohmann Cartan calculus does **not** descend to
`SPoly/∂` in full. At most a *rig-scalar* (`ℕ`-module) fragment survives.

The obstruction is exactly the rig `ℕ`: finite-support polynomial functors are the
subtraction-free world, and a scalar ring needs a negation that `ℕ` does not have.
This is the same subtraction-free knife that forced the uniqueness converse to be
reproved rig-internally (`[[tangent-uniqueness-spoly-finite-support]]`): *rig-vs-ring
is the dividing line.*

Throughout, a *container* is a set of shapes `S` with finite position sets `a_s`;
its extension is the polynomial functor `⟦S▷a⟧(X) = Σ_{s∈S} X^{a_s}` (only the
cardinalities `|a_s|` matter up to iso). `◁` is substitution (composition of
extensions) with unit `y`; `∂` is the AAGM one-hole derivative; the dual-number
substitution is `Tp = p(y+εv) mod ε² = p + εv·∂p`.

**Two presentations of the one tangent structure.** The container tangent structure has
two standard faces, and this note uses both (they share the single obstruction).
- **(C1) the CDC / differential presentation** (existence note): the category `SPoly`
  with objects `ℕ` (= `Set^n`), morphisms the finitary polynomial functors
  `Set^n → Set^m`, and the Cartesian-tangent structure `T(n) = 2n`,
  `T(f) = ⟨f∘π₁, D[f]⟩` with combinator `D[f]` the directional one-hole derivative.
  The counting functor `N : SPoly → Poly_ℕ`, `N(⟦S▷a⟧) = Σ_s x^{|a_s|} ∈ ℕ[x]`
  (multivariable analogously), is a genuine functor that preserves the entire
  CDC/tangent structure and is faithful (existence note, Lemmas 3–5). **This is where
  the airtight functorial argument lives (§2.1).**
- **(C2) the tangent-bundle presentation** (uniqueness note): objects are the
  (finite-support) polynomial functors `p` themselves — the "spaces" — and the tangent
  *bundle* is `T = (−)◁D`, `D = y+εv` the dual-number infinitesimal object, infinitesimal
  part `M = y`. This is the face the Cartan program consumes (tangent bundle of a space),
  and the one in which "`Tp` for `p = y²`" is literally an object; §2.2 computes its
  fibers.

The additive-bundle structure — the commutative-monoid-valued bundle `p : T ⟹ Id`, its
zero `0` and fiber addition `+` — is the *same* coproduct/`ℕ`-module structure in both
faces (the dual-number `εv`-part), so the negation question has one answer; §2.1 settles
it rigorously in C1 and §2.2 exhibits the same verdict concretely in C2.

---

## 1. The input to the Cartan calculus, and the reduction

**Definition 1 (scalar ring object) [paper-reported, arXiv:2607.11169, §4].** In a
cartesian tangent category `(𝒞, T)`, a *scalar ring object* is a commutative unital
ring object `(R, +̂, m̂, 0̂, 1̂, −̂)` for the cartesian product `×`, together with a
natural *scalar multiplication* `κ_X : R × T(X) → T(X)` that makes each additive
tangent bundle `p_X : T(X) → X` an `R`-module in the slice `𝒞/X` — unital and
associative over `m̂`, bilinear with respect to `+̂` and the tangent addition `+_X`,
and compatible with the vertical lift `λ` and the canonical flip `τ`. This is the
data from which their construction generates `d`, `ι`, `L`, and the Lie–Rinehart
algebra of vector fields.

Recall a tangent category is **Rosický** (equivalently, *additive with negatives*)
when its additive bundle is a bundle of *abelian groups*: there is a negation
`σ : T ⟹ T`, a bundle endomorphism (`p ∘ σ = p`), satisfying the additive-inverse law
```
    +_X ∘ ⟨σ_X, id_{TX}⟩  =  0_X ∘ p_X        as morphisms  T(X) → T(X),        (†)
```
where `⟨σ, id⟩ : TX → T₂X = TX ×_X TX` is the pairing into the additive-bundle
pullback and `+_X : T₂X → TX` is the fiber addition.

**Lemma A (a scalar ring object forces negatives).** If `(R, κ)` is a scalar ring
object on `(𝒞, T)`, then
```
    σ_X := κ_X ∘ ⟨ (−̂ ∘ 1̂ ∘ !_R) , id_{TX} ⟩ : T(X) → T(X)
```
(scalar multiplication by `−1 := −̂1̂ ∈ R`) is a negation. Hence `(𝒞, T)` is Rosický.

*Proof.* This is the standard fact that in any module over a ring, multiplication by
`−1` is the additive inverse, instantiated internally. By the `R`-module axioms on the
bundle `p_X : TX → X` (bilinearity of `κ` over `+̂` and the ring unit/zero laws),
for any `t` over `x`:
```
    t +_X (−1)·t  =  1·t +_X (−1)·t  =  (1̂ +̂ (−̂1̂))·t  =  0̂·t  =  0_X(x),
```
using unitality `1·t = t`, bilinearity `(r +̂ s)·t = r·t +_X s·t`, the ring law
`1̂ +̂ (−̂1̂) = 0̂`, and `0̂·t = 0_X` (which follows from bilinearity: `0̂·t = (0̂+̂0̂)·t
= 0̂·t +_X 0̂·t`, cancel). `κ` natural and `p_X ∘ κ_X = p_X ∘ π_2` (the action is
fiber-preserving) give `p_X ∘ σ_X = p_X`. So `σ` satisfies (†). ∎

This is exactly Aintablian–Blohmann's Prop ~4.4, but reproved here from the module
axioms, so the Main theorem does not depend on *trusting* their statement — only on
their **definition** of the input (Definition 1).

**Reduction.** By Lemma A, contrapositively:
> if **some** additive-bundle fiber of `(SPoly, T)` is a commutative monoid that is
> **not a group**, then `SPoly/∂` has **no** scalar ring object, and the Cartan
> calculus is obstructed at its input.

The whole program therefore reduces to the single decidable question: *is the additive
bundle of `T = (−)◁D` a bundle of groups?* §2 answers it.

---

## 2. The additive bundle has no fiberwise negation

### 2.1 The core argument: counting-functor transport (in C1, airtight)

Work in the CDC presentation `SPoly` (objects `ℕ`, `T(n)=2n`), where the counting
functor `N : SPoly → Poly_ℕ` is a genuine functor. `Poly_ℕ` is the CDC of polynomials
over the rig `ℕ` (objects `ℕ`, morphisms tuples of `ℕ`-coefficient polynomials,
differential the Jacobian directional derivative), with its canonical Cartesian-tangent
structure `T(k)=2k`, `T(h)=⟨h∘π₁, D[h]⟩`. By the existence note (Lemmas 3–5), `N`
preserves composition, finite products and projections, the left-additive `+`, `0`, the
product `×`, and the differential (`N∂ = ∂N`). A functor preserving exactly the
Cartesian-left-additive-plus-differential data **is** a morphism of Cartesian tangent
categories (Cockett–Cruttwell 2014): it carries `T`, the projection `p`, the zero `0`,
the additive pullback `T₂`, and the fiber addition `+` of `SPoly` to those of `Poly_ℕ`.
In particular, on a morphism `f`, `N(Tf)` is the dual-number substitution of `N(f)`:
`N(f)(x+εv) = N(f)(x) + εv·N(f)'(x)` (verified `scratch/cartan_negation_verify.py`
(a)–(b)).

**Proposition 1.** The container tangent structure admits no negation `σ`.

*Proof.* Suppose `σ : T ⟹ T` were a negation on `SPoly`, satisfying (†). Apply `N`.
Because `N` preserves `+`, the pairing `⟨-,-⟩` into `T₂` (a universal construction from
products/the projection, which `N` preserves), `id`, `0`, `p`, and composition, equation
(†) maps to
```
    +  ∘ ⟨N(σ), id⟩  =  0 ∘ p          in  Poly_ℕ,
```
i.e. `N(σ)` is a negation for the tangent structure of `Poly_ℕ`.

But `Poly_ℕ` has **no** negation. Take the object `1`; then `T(1) = 1×1` carries two
coordinates `(x, v)` (base, tangent), with `p = π_x`, `+ : (x,v₁,v₂) ↦ (x, v₁+v₂)`,
`0 : x ↦ (x,0)`. A bundle endomorphism over `p` is `(x,v) ↦ (x, g(x,v))` for an
`ℕ`-coefficient polynomial `g` (morphisms of `Poly_ℕ` are `ℕ`-polynomials), and the
negation law (†) reads
```
    v + g(x,v) = 0        identically in  ℕ[x,v].
```
This forces `g = −v`, which is not an `ℕ`-polynomial (negative coefficient); evaluating
at `v=1` would require `g(x,1) = −1`, unreachable by any `ℕ`-polynomial (they are
`≥ 0` on `ℕ`). Contradiction (`scratch/cartan_negation_verify.py` (c)).

Hence no negation `σ` exists. The additive bundle `p : T ⟹ Id` is a bundle of
commutative monoids that are **not** groups. ∎

**Remark (why this cannot be dodged).** The argument uses only that `N` *preserves* the
finitely many operations appearing in (†) — not faithfulness. Any candidate negation
whatsoever, however exotic, is transported downward to a `Poly_ℕ` negation and killed
there. Structurally: `Poly_ℕ` is a left-additive category whose hom-monoids `(ℕ[x], +)`
are not groups, so it is not an additive-with-negatives tangent category; `N` transports
any negation down, so the container tangent structure cannot have one either.

### 2.2 The fibers in the tangent-bundle presentation C2 (the PROVE.md witnesses)

In the Cartan-facing presentation C2 (objects = spaces `p`, bundle `T = (−)◁D`), the
same obstruction appears as an explicit fiber computation — this is where "`Tp` for
`p = y²`" is literally an object and where the additive bundle `p : Tp → p` is the
tangent bundle of the space. The fibers make the rig obstruction tangible.

For `p = Σ_{s} y^{a_s}`, the bundle `Tp = p◁D = p + εv·∂p` has base part `p` and tangent
part `εv·∂p = εv·Σ_s Σ_{h∈a_s} y^{a_s∖{h}}` — over each shape `s`, one tangent direction
per hole `h ∈ a_s`. The whole additive bundle of `Tp` is `p◁(additive bundle of D)`,
where `D` is the commutative-monoid object with infinitesimal part `M = y`: the fiber
addition `+ : T₂p → Tp` is `p◁∇` with `∇ : M⊕M → M` the codiagonal (it collapses two
infinitesimal copies `εv₁, εv₂` to `εv`). Iterating `∇` (the `ℕ`-module structure that
every additive bundle carries by repeated fiber addition) makes the tangent data over a
shape `s` the **free `ℕ`-module on the holes `a_s`**: a tangent vector carries an
`ℕ`-multiplicity per hole-direction, added hole-by-hole in `ℕ` (not by any addition of
`Set`-values — there is none). The counting polynomial realises this fiber as
`(ℕ^{|a_s|}, +, 0)`, matching §2.1. A negation would make it the free `ℤ`-module.

- **`p = y` (the line — minimal witness).** One shape, one hole; `Ty = y+εv = D`. Fiber
  `= ℕ`. The unit tangent `1 ∈ ℕ` has no additive inverse: `1 + c = 0` is unsolvable in
  `ℕ`. Already the tangent bundle of the *identity functor* has a non-group fiber.
- **`p = y²` (first non-linear; `∂(y²)=2y`).** One shape, holes `{h₁,h₂}`;
  `T(y²) = y² + εv·2y`, fiber `= ℕ²`. The element `(1,0)` (one unit of tangent along
  `h₁`) has no inverse in `ℕ²` (`scratch/cartan_negation_verify.py` (d)).
- **`p = y + y²` (`∂p = 1 + 2y`).** Shapes `s₀` (0 holes, fiber `ℕ⁰=0`, trivially a
  group) and `s₁` (2 holes, fiber `ℕ²`). The `s₁`-fiber already fails.

Each fiber is a genuine commutative monoid — commutative, cancellative, with identity
`0` — but only `0` is invertible. This is the free `ℕ`-module structure: a group would
be the free `ℤ`-module, and `ℤ` is exactly one subtraction beyond `ℕ`.

---

## 3. Consequences: the honest boundary of the container Cartan calculus

**Corollary (no scalar ring object).** `(SPoly, T=(−)◁D)` carries no scalar ring object
`R` (Definition 1). *Proof.* Such an `R` would, by Lemma A, make the tangent category
Rosický — its additive bundle a bundle of abelian groups. But that additive bundle has a
fiber that is not a group: the free `ℕ`-module `ℕ^{|a_s|}` over any shape with a hole
(§2.2, e.g. `ℕ` over `p=y` or `ℕ²` over `p=y²`), equivalently the `(ℕ,+)` fiber
obstruction transported by `N` (Proposition 1, §2.1). Two independent witnesses, same
contradiction. ∎

**The precise obstruction (not "no ring objects").** Ring objects *do* exist in
`(Poly, ×)`: every ordinary commutative ring `k` (e.g. `ℤ`, `ℤ/n`) embeds as a constant
polynomial functor, and constant functors form a full, finite-product-preserving copy
of `Set` (resp. `CRing`) inside `Poly`. The obstruction is **not** the absence of a
ring object; it is that **no ring object can act** on the dual-number tangent bundle by
a `κ` compatible with the tangent structure — because any such action would, via
`κ(−̂1̂, −)`, negate tangent vectors (Lemma A), and the fibers admit no negation
(Proposition 1). The knife is the *compatible action*, not the ring.

**What does not descend.** The full Aintablian–Blohmann package built on `(R, κ)` —
the exterior differential `d`, inner derivative `ι`, Lie derivative `L`, and the
Lie–Rinehart/Chevalley–Eilenberg assembly of forms (and a fortiori the cubical-forms
CDGA of 2609.05963, which further needs `R` with no 2-torsion) — does **not** descend to
`SPoly/∂`.

**What survives (the rig-scalar fragment).** The additive bundle *is* a genuine
`ℕ`-module bundle: fibers are free `ℕ`-modules on holes, with a canonical `ℕ`-scaling
`c·(−)` for every `c ∈ ℕ` (iterated fiber addition). Every piece of the calculus that
uses only `+`, `0`, and `ℕ`-scaling — not `−1` — survives on `SPoly/∂`. Pinning down
exactly which of `d`, `ι` survive the loss of subtraction (the Chevalley–Eilenberg
differential, needing signs, is the first casualty) is the natural follow-up and is
flagged as future work.

**Grant frame.** Existence and uniqueness are banked; this theorem *delimits* the
program honestly. The differential geometry of containers is a **first-order tangent
calculus** (directional derivatives, vector bundles, the chain rule) but **not** a full
Cartan calculus with forms and Lie derivatives — the rig `ℕ` blocks the scalar ring,
pending a ring completion `ℕ → ℤ` (group completion of the fibers) whose categorical
meaning for containers is the real open question. "Rig-vs-ring is the knife" becomes a
theorem (`[[admissibility-is-the-real-generality-question-mem]]`,
`[[fullness-unit-connectedness]]`): the exact next slide after uniqueness in the
Strathclyde mini-course.

---

## 4. Verification

`scratch/cartan_negation_verify.py` (all pass):
- (a)/(b) `Tp = p(y) + εv·∂p` and `N(Tp) = N(p)(x+εv) = N(p) + εv·N(p)'` for
  `p ∈ {y², y+y², y³, y+1, 3y⁴}` — confirms `∂(y²)=2y`, `∂(y+y²)=1+2y`, counting
  preservation.
- (c) no `ℕ`-polynomial `g(x,v)` satisfies `v + g = 0`; `g = −v` fails
  (negative coefficient; value `−1` at `v=1` unreachable).
- (d) fiber `ℕ²` of `y²`: element `(1,0)` has no additive inverse; the monoid is
  commutative, cancellative, only `0` invertible.

## 5. Status and gaps

**Proved (airtight, mine):**
- Lemma A (scalar ring object ⟹ Rosický negation) — elementary module algebra,
  internalised; removes dependence on trusting AB Prop 4.4.
- Proposition 1 (no negation on `(SPoly, T)`), via counting-functor transport to
  `Poly_ℕ` + the rig fact `v+g=0` unsolvable over `ℕ`. Uses only that `N` *preserves*
  the tangent/additive structure (established in the existence note), not faithfulness.
- Corollary (no scalar ring object) and the precise "no compatible action" delimitation.

**Paper-reported (cited as the DEFINITION of the input, not reproved):**
- Definition 1, the structure a scalar ring object must supply, and that it is what the
  Aintablian–Blohmann calculus consumes (arXiv:2607.11169 §4). The *consequence* we use
  from it (Lemma A) is reproved here; we rely on the paper only for what the calculus
  takes as input.

**Not a gap, but future work:**
- Classify exactly which fragment of `d`, `ι`, `L` survives with `ℕ`-scalars only
  (subtraction-free Cartan calculus).
- The categorical meaning of the fiberwise group completion `ℕ → ℤ` for containers —
  does group-completing the tangent fibers land in a larger polynomial-like category
  (virtual/`ℤ`-containers) that *is* Rosický? This is the honest route to a full Cartan
  calculus and the most interesting open question the theorem exposes.

**Scope.** First order (as are AAGM `∂`, the uniqueness note, and CCGZ §1–4).
