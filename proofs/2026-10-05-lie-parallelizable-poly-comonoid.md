# The Lanfranchi parallelizability port fails for container comonoids — and the groupoid conjecture is refuted; what survives is an out-degree fiber-rank dividing line

**MacBeth (Kodamai / Ghani group) — 2026-10-05**

## Problem

`state/PROVE.md` (Conjecture P) proposed porting Lanfranchi's Lie-group↔Lie-algebra
correspondence (arXiv:2609.03449, Thm 4.20) to polynomial comonoids. A polynomial
comonoid `p = Σ_{a∈Ob} y^{E_a}` (= a small category `𝒞`, `E_a` = morphisms out of
object `a`) was conjectured to be **parallelizable** in `(Poly, T=(−)◁D)` iff `𝒞` is
**out-degree homogeneous** (`|E_a|` constant), and conjecturally iff `𝒞` is a
**groupoid**.

`PROVE.md` flagged, as the caveat to resolve first, that Lanfranchi's group objects
live in a **Cartesian** structure (`×`) while containers are comonoids for
**composition** (`◁`), and warned: *"If the two structures can't be reconciled, the
result may be a REFUTATION (the port fails) — which is itself a publishable
dividing-line."* That is exactly what happens.

> **Main result (two theorems).**
>
> **(I) The literal port is ill-posed — a structural refutation.** There is no
> Cartesian tangent category on the category of polynomial *functors* in which the
> AAGM derivative `∂` is the tangent bundle and Lanfranchi's parallelizability
> (Def. 4.18) is a nontrivial condition:
> - In the representable species structure `(Poly, T=(−)◁D)` — the only one making `∂`
>   a tangent *bundle* of functor-objects — the tangent functor does **not** preserve
>   the categorical product (a spurious `ε²` cross-term), so it is **not a Cartesian
>   tangent category**; and with the categorical product as trivial bundle, **no
>   non-constant object is parallelizable** (even the terminal object `y` fails:
>   `Ty = y+εv ≇ y×m`). The port returns a degenerate "nothing is parallelizable."
> - The genuine *Cartesian* tangent category of containers is the arity CDC
>   `SPoly`/`Poly_ℤ`, where `∂` is the differential *combinator* on morphisms,
>   `T(n)=2n`, and (Lanfranchi Cor. 4.22, GCDC) **every object is parallelizable** —
>   vacuous; moreover a comonoid `p` is a *morphism* there, so "`p` parallelizable"
>   does not even typecheck.
>
> Hence "parallelizable ⟺ groupoid" cannot be stated as intended.
>
> **(II) What survives, proved — the out-degree fiber-rank dividing line.** The
> representable tangent bundle `Tp = p◁D` has, over a point of shape `a`, tangent
> space the free module `W^{E_a}` of rank `|E_a|`. So its fibres are all isomorphic to
> a single object `m` **iff `|E_a|` is constant** (out-degree homogeneous). This
> "constant tangent rank" condition — the honest residue of parallelizability
> available in the representable setting — depends **only on the underlying polynomial
> functor**, hence is **blind to the comonoid (composition) structure**, and therefore
> **cannot be equivalent to "groupoid."** The groupoid conjecture is refuted both ways;
> connected groupoids satisfy it (the positive shadow of Lanfranchi).

Notation as upstream: a container is `S▷(P^i_s)`, extension
`⟦S▷P⟧(X⃗)=Σ_s∏_iX_i^{|P^i_s|}`; one variable, `p=Σ_a y^{E_a}`, `E_a` the direction
(out-morphism) set at object `a`; `◁` substitution, unit `y`; `∂` the AAGM one-hole
derivative, `∂p = Σ_a Σ_{e∈E_a} y^{E_a∖{e}} = Σ_a |E_a|·y^{E_a−1}`; `Tp = p◁D =
p+εv·∂p` (Weil base change along `ℤ→ℤ[ε]/ε²`, `tangent-restricts-to-dcont-base-change`,
`virtual-container-cartan` Prop. 2).

---

## 0. The type confusion (why the naive `∂p ≅ p×V` is a non-starter)

`PROVE.md` writes the trivialization `∂p ≅ p × V` with `∂p` the bundle and `×` a
product of *objects*. No product on `Poly` can realize this: categorical `×` sends
`y^A×y^B=y^{A⊔B}` (**adds** directions), Dirichlet `⊗` sends `y^A⊗y^B=y^{A×B}`
(**multiplies**), while `∂(y^A)=Σ_{a}y^{A∖a}` (**removes one**). So `∂p ≅ p×V` as
total objects is a cardinality contradiction for every nontrivial `p`. Parallelizability
is not an object iso; it is (Lanfranchi Def. 4.18, folklore Cruttwell–Ikonicoff–Lemay–
Van Der Linden) a *linear iso of additive bundles over the base*,
```
    ν : TM ≅ M × m   over M,   m a differential object,   ν ∘ (z_M×λ_m) = l_M ∘ Tν.  (∗)
```
The correct object of study is thus the tangent **bundle** `p_p : Tp → p`,
`Tp = p + εv·∂p`, with `∂p` only the *fibre data*. §1–§3 establish that even this
correctly-posed version fails as a Cartesian notion, and extract what remains.

---

## 1. The tangent space at a point is `W^{E_a}` — rank `|E_a|` (proved)

**Lemma 1.** For `T=(−)◁D`, the tangent space at a point of `p = Σ_a y^{E_a}` of shape
`a` is the free module `W^{E_a}`, of rank `|E_a|`.

*Proof.* `Tp = p(y+εv) = p + εv·∂p`. Reading the two sorts explicitly — base `X`,
tangent `W` (the generator `εv`) — and expanding `p(X+εX_v)` to first order,
```
    Tp(X,W) = p(X) + W·∂p(X) = Σ_a X^{E_a} + W·Σ_a Σ_{e∈E_a} X^{E_a∖{e}}.
```
A point of `p` over `X` is `(a, f:E_a→X)`. From the `W·∂p` summand, a point of `Tp`
over it is a choice of a direction `e∈E_a` to make infinitesimal, with a tangent value
`w∈W`: the fibre of `p_p` over `(a,f)` is `{(e,w):e∈E_a, w∈W} ≅ W^{E_a}`, the free
`W`-module on `E_a`, rank `|E_a|`. The additive-bundle structure (zero section = all
slots `0`, fibrewise addition) is the free-module structure.
(Verified: the `W`-linear part of `Tp` is `∂p`, and shape `a` carries exactly `|E_a|`
tangent generators; `scratch/lie_parallelizable_verify.py`.) ∎

This is a statement about the *fibres* of `Tp`; it needs no Cartesian/trivial-bundle
apparatus and is the robust kernel of the whole investigation.

---

## 2. Theorem I — the Cartesian port is ill-posed (refutation)

Lanfranchi Def. 4.18 requires a **Cartesian tangent category**: a tangent structure
whose `T` is compatible with finite products (`T(A×B)≅TA×TB`), so that the trivial
bundle `M×m` and the linearity condition `(∗)` make sense. We show no such home exists
for `∂`-as-tangent-bundle on functors, by examining both candidate structures.

**(2a) `(Poly, ×, (−)◁D)` is not a Cartesian tangent category.** View `Tp=p+εv∂p` as a
polynomial functor in the two sorts `(X,W)`. For the categorical product (pointwise),
```
    T(p×q) = pq + εv·(p'q+pq')    but    Tp × Tq = (p+εv p')(q+εv q') = pq + εv(p'q+pq') + ε²v²·p'q'.
```
These differ by the **`ε²` cross-term** `ε²v²·p'q'` — nonzero already for `p=q=y`
(coefficient `1`) and `p=q=y²` (coefficient `4X²`); verified
`scratch/lie_product_compat.py`. The categorical product of functors does **not**
impose `ε²=0`, so `T` does not preserve `×`: `(Poly,×,(−)◁D)` fails the Cartesian
tangent axiom. (The Leibniz rule holds only *modulo* `ε²`, i.e. in the based dual-number
setting — but that setting is `(Poly,◁)`-monoidal, not Cartesian; see 2c.)

**(2b) With the categorical product, nothing non-constant is parallelizable.** Suppose
`Tp ≅ p×m` over `p`, `×` categorical. As total objects `p×m = p(X)·m(X,W)` and
`Tp = p+εv·∂p = p(X)+W·p'(X)`, so `m = (p+Wp')/p = 1 + W·(p'/p)`. This is a polynomial
functor iff `p ∣ p'` in `ℤ[X]`; for a non-constant polynomial `p`, `deg p' = deg p − 1 <
deg p`, so `p ∤ p'` unless `p'=0`, i.e. `p` constant. Hence the **only** parallelizable
objects are the constants — even the terminal object `y` fails (`Ty = X+W`, and
`y×m=X·m` can never equal `X+W`). The port returns a degenerate answer with no
dependence on `𝒞` at all. In particular the four `PROVE.md` test cases are *all*
non-parallelizable here, flatly contradicting the conjecture's intended readings
(`y` "trivially parallelizable", `y²` parallelizable). (`scratch/lie_product_compat.py`.)

**(2c) The nontrivial `∂`-tangent structure is representable/monoidal, not Cartesian.**
`∂` becomes a genuine (non-degenerate) tangent *bundle* only as right-`◁`-tensoring by
the infinitesimal object `D=y+εv` in the monoidal category `(Poly,◁,y)`
(`tangent-uniqueness-spoly` §1; Lanfranchi–Lemay / Leung representable tangent
structures). That is a **monoidal** tangent setting; `◁` is not Cartesian (it has no
diagonal `p→p◁p` natural in `p`; the comonoids `p→p◁p` are *extra* structure — the
categories). Lanfranchi's parallelizability lives only in *Cartesian* tangent
categories, so it does not apply here.

**(2d) The Cartesian home is the arity GCDC — vacuous, and mistyped.** The genuine
Cartesian tangent category of containers is the CDC `SPoly` (and its ℤ-completion
`Poly_ℤ`): objects = arities `n`, morphisms = polynomial maps, `T(n)=2n=n×n`, `∂` the
differential *combinator* (`tangent-container-cdc`, `virtual-container-cartan`). A CDC
is a GCDC, so by **Lanfranchi Cor. 4.22 every object is parallelizable** — the notion
carries no information. Worse for the conjecture: here `p = Σ_a y^{E_a}` is a
*morphism* `1→1`, not an object, so "`p` is parallelizable" does not typecheck.

**Conclusion (Theorem I).** Every way of making `∂` a tangent structure places us in a
setting where Lanfranchi's parallelizability is either undefined (not Cartesian, 2a/2c),
degenerate (nothing parallelizable, 2b), or vacuous and mistyped (GCDC, 2d). The literal
port of Thm 4.20 to container comonoids is **ill-posed**. ∎

---

## 3. Theorem II — the surviving dividing line, and the groupoid refutation

What *is* well-posed and nontrivial is the fibre-rank condition of Lemma 1, intrinsic to
the representable bundle.

**Definition.** Call `p = Σ_a y^{E_a}` **tangent-regular** if the fibres of `Tp=p◁D` are
all isomorphic to a single module `m` — equivalently (Lemma 1) if the tangent spaces
`W^{E_a}` are mutually isomorphic.

**Theorem 2.** `p` is tangent-regular iff the out-degree `a↦|E_a|` is constant on `Ob`.

*Proof.* The fibre over shape `a` is the free module `W^{E_a}` (Lemma 1); two free
modules are isomorphic iff their ranks are equal; a common `m` exists for all `a` iff all
`|E_a|` are equal. ∎

**Theorem 3 (blindness to composition; groupoid conjecture refuted).** Tangent-regularity
depends only on the underlying polynomial functor `U(p)` (equivalently the multiset
`{|E_a|}`), hence factors through the forgetful `U : Cat ≃ Comon(Poly,◁) → Poly`
(Ahman–Uustalu). Consequently "tangent-regular ⟺ groupoid" is false both ways:

- *(tangent-regular ⇏ groupoid.)* The underlying functor of the idempotent monoid
  `{1,e}`, `e²=e`, is `y²`, identical to that of the group `ℤ/2`. The two have the
  **same** tangent bundle; `ℤ/2` is a groupoid, `{1,e}` is not; both are tangent-regular
  (one object ⇒ constant out-degree). Tangent-regularity cannot tell them apart.
- *(groupoid ⇏ tangent-regular.)* The disjoint groupoid `ℤ/2 ⊔ ℤ/3` has objects of
  out-degrees `2` and `3`, so `U=y²+y³` is **not** tangent-regular (Theorem 2), though it
  is a groupoid. This direction is airtight from Lemma 1 alone.

(`scratch/lie_parallelizable_verify.py`: tangent-regularity tracks constant out-degree
exactly across ten categories, mismatching the groupoid property on `{1,e}`, `ℤ/2⊔ℤ/3`.)

**Why the conjecture was doomed.** `∂` reads only the *directions* `E_a` (how many
morphisms leave each object), never the composition `δ:p→p◁p`. "Groupoid",
"connected", "invertible" are properties of `δ`, invisible to `∂`. No such property can
be equivalent to a condition on `U(p)`. The groupoid half of Conjecture P was unprovable
in principle, not merely unproved. ∎

**Corollary 4 (positive shadow of Lanfranchi).** A **connected** groupoid with object set
`Ob` and vertex group `G` (so `Hom(a,b)≅G` for all `a,b`) has `|E_a|=Σ_b|Hom(a,b)|=
|Ob|·|G|`, constant; hence it is tangent-regular. More generally every *out-regular*
category (codiscrete categories, `|E_a|=|Ob|`; any one-object category/monoid) is
tangent-regular. This is the faithful residue of "Lie group ⟹ parallelizable":
homogeneity is exactly the left-translation regularity (composing with a connecting
iso `b→a` bijects `Hom(a,−)≅Hom(b,−)`) that a groupoid supplies — but, by Theorem 3, it
is strictly weaker than being a groupoid. ∎

---

## 4. Status, grades, and the one genuinely open refinement

**Proved (mine, airtight):**
- **Lemma 1** — tangent space at a shape-`a` point is `W^{E_a}`, rank `|E_a|` (fibre
  computation; point-level; computationally checked).
- **Theorem I (2a–2d)** — the literal Cartesian port is ill-posed: `T` does not preserve
  `×` (explicit `ε²` cross-term); with `×`, only constants are parallelizable; the
  nontrivial `∂`-structure is `◁`-monoidal not Cartesian; the Cartesian home is a GCDC
  (Cor. 4.22, vacuous) in which `p` is a morphism. Each clause is a short, verified fact.
- **Theorem 2** — tangent-regular ⟺ out-degree homogeneous.
- **Theorem 3** — tangent-regularity factors through `Cat→Poly`; groupoid conjecture
  refuted both ways (explicit `{1,e}`, `ℤ/2⊔ℤ/3`; the second airtight from Lemma 1).
- **Corollary 4** — connected groupoid ⟹ out-regular ⟹ tangent-regular.

**Cited (input spec / standard background, not reproved):**
- Lanfranchi 2609.03449 Def. 4.18 (parallelizable object), Thm 4.20, Cor. 4.22 — the
  parallelizability notion and the GCDC vacuity; used to *diagnose* the port, not as a
  load-bearing step. (sources.json level: deep-read of the relevant §4.3–4.4; the
  diagnosis uses only the definitions and Cor. 4.22, which are quoted verbatim.)
- `tangent-uniqueness-spoly` §1 (`T=(−)◁D` representable first-order tangent structure),
  `tangent-restricts-to-dcont-base-change`, `virtual-container-cartan` Prop. 2
  (`Tp=p+εv∂p`, Weil base change), `tangent-container-cdc` (the arity CDC) — all `proved`
  upstream; supply the two tangent structures.
- Ahman–Uustalu (`[[cat-hash-is-dcont-cof]]`): polynomial comonoids ≃ small categories.

**The one genuinely open refinement (a *different*, sharper question — not a gap above).**
Theorem I kills *bare* Cartesian parallelizability. The honest remaining analogue of
Lanfranchi's Lie object is the **canonical left-translation trivialization built from the
comonoid structure** (which *does* see composition):

> **Open.** For a `◁`-comonoid `p` (category `𝒞`), does the comultiplication `δ` induce a
> canonical trivialization of the (vertical part of the) representable tangent bundle —
> "translate every tangent direction to a basepoint by composition"? Characterize when it
> exists. Conjecture: this requires invertibility of the translations, so it is where
> **groupoids** (and connectedness) genuinely enter — the composition-sensitive layer that
> tangent-regularity (Theorem 3) provably cannot see.

This needs the differential-bundle/vertical structure of `Tp` and the comonoid maps
worked out together; it is the correct home for the groupoid intuition and is left to a
future session.

**Overall grade.** The refutation (Theorem I) and the dividing line (Theorems 2–3,
Cor. 4) are `proved`. The target node `lie-parallelizable-poly-comonoid` should be opened
and **closed as a refutation-with-salvage**, not as the conjectured positive theorem.

**Scope.** First order throughout; finite support.

## 5. Verification (computational)

- `scratch/lie_parallelizable_verify.py` — computes `Tp=p+W∂p` and fibre ranks on ten
  categories; confirms fibre rank over shape `a` = `|E_a|`; tangent-regularity ⟺ constant
  out-degree on all four `PROVE.md` cases; the two refuting counterexamples; the connected
  groupoid and the poset.
- `scratch/lie_product_compat.py` — `T` does not preserve the categorical product (`ε²`
  cross-term `1` for `y×y`, `4X²` for `y²×y²`); only constant `p` admit `Tp≅p×m`.

## 6. Grant frame

A sharp dividing-line for the Strathclyde tangent-containers mini-course (Oct 13–16),
and an honest cautionary tale about porting Cartesian-tangent theory to the
*representable/monoidal* `◁`-tangent structure of containers. The geometry the AAGM
derivative supports is **fibre-rank geometry over the discrete set of objects**: it reads
the out-degree sequence (the *shape* of a category) and is **blind to composition**.
"Parallelizable ⟺ Lie object" does not survive the move from the Cartesian affine world
to containers; what survives is "tangent-regular ⟺ out-regular," with the genuine
Lie-theoretic (groupoid) content pushed into a strictly finer, composition-sensitive
left-translation layer. Same "representability is the dividing line" moral as the
fullness⟺unit-connectedness flagship and the derivative-uniqueness rigidity — here in its
cautionary, boundary-drawing form.
