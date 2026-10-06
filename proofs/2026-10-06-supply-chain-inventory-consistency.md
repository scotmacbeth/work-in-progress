# Supply-chain inventory consistency is a degree-1 class — and is *independent* of the Zappa–Szép weld obstruction

**MacBeth — deep-work prove session, 2026-10-06**

**Status: REFUTATION of the stated conjecture + PROVED dividing-line theorem.**
Target grade: `proved` (the separation theorem and the degree-1 characterization are
proved; they rest on `g-obstruction-is-h2-class` [proved], the no-λ-correction lemma
[proved + brute-checked here], and standard Mayer–Vietoris/descent [cited]).

---

## 1. The conjecture under test

From `state/PROVE.md` (SEED Open Question #4). Model a supply chain as a directed
container ≅ small category `𝒮`: objects = nodes, morphisms out of `a` = admissible
logistics operations, composition = sequencing. A composite chain is a **Zappa–Szép
product** `𝒮 = 𝒞 ⋈ 𝒟` (procurement ⋈ logistics). The conjecture:

> **(C)** Global inventory is consistent (the resource presheaf glues over the sub-chain
> cover / a global section exists) **iff** the ZS global-closure obstruction
> `[ω] ∈ H²(Sk(𝒮); ℤ/n)` vanishes.

The PROVE.md brief flagged the exact danger (its "critical caveat"): *is inventory
consistency genuinely the weld's `H²`, or a different `H¹`/torsor class?* The honest first
task — writing the resource presheaf explicitly and comparing its gluing obstruction to
`[ω]` — settles it. **The two are different classes.** (C) is false in both directions.
What survives is a sharper, more useful dividing-line theorem.

This is the same "rhyme, not identity" trap as `two-omega-sites-not-isotropy-restriction`
(there, two `H²` classes with the same cyclic group but different sites) — except here the
two classes differ even in **degree** (`H¹` vs `H²`) and in **coefficient system**, making
them *more* obviously distinct, not less. Check the support, the coefficients, and the
degree before identifying two cyclic obstructions.

---

## 2. Setup: two obstructions, stated precisely

Throughout `𝒮 = 𝒞 ⋈ 𝒟` is a strict factorization (Zappa–Szép) of small categories: `𝒞, 𝒟`
are wide subcategories, `𝒞 ∩ 𝒟 = O` is the discrete category on the shared object set, and
every morphism factors **uniquely** as `f = c · d` (`c ∈ 𝒞`, `d ∈ 𝒟`). The matched-pair
law is the distributive rewriting `λ : 𝒟𝒞 ⇒ 𝒞𝒟`, `d·c = (c▷d)·(c◁d)` (Rosebrugh–Wood).

**Crucial modelling choice.** A supply chain in which two routes `a → d` are *genuinely
different operations* (distinct cost/stock transforms) is the **free category on the
operation quiver**, modulo only the imposed ZS relations — **not** a thin poset. In a
poset `rp = sq` is forced and route-discrepancy is invisible by fiat; that is not a supply
chain, it is the statement that all routes are already identified. We model the honest
object: distinct routes are distinct morphisms.

### 2.1 The weld obstruction `[ω] ∈ H²(Sk_𝒮; 𝒟)`

This is the `(G)`-closure class of `g-obstruction-is-h2-class` (proved). It measures
whether the transversal closes into a wide subcategory, i.e. whether `𝒮` **decomposes at
all** as the claimed `𝒞 ⋈ 𝒟`. Its defect cochain `ω_T(c₂,c₁) ∈ 𝒟` satisfies
`c₂∘c₁ = ⌊c₂c₁⌋_T ∘ ω_T(c₂,c₁)`; under the abelian regime (H) it is a normalized
Baues–Wirsching 2-cocycle on the orbit category `Sk_𝒞` with coefficients the vertex-group
presheaf `𝒟 : Sk_𝒞^op → Ab`, and `(G) ⟺ [ω]=0`. **Three facts to hold onto:**

1. `[ω]` depends only on the **category** `𝒮` and the chosen right factor `𝒟`. No resource
   data enters its definition.
2. Its **coefficient system is `𝒟`** (vertex groups of the invertible/weld part).
3. It is a **degree-2** class.

### 2.2 The inventory obstruction `[θ_R] ∈ H¹(𝒮; R)`

Inventory is *resource data on top of the category*: a presheaf `R : 𝒮^op → Ab` (a local
system of stock-groups; fibre `R(a)` = stock configurations at node `a`, and `R(f)` the
transport along operation `f`). This is a section of the container-logic fibration
`Cont(cod)=Fam(cod^op)` (`logic-of-containers-cont-cod-fibration`, proved): fibrewise, a
choice of stock object and its reindexing along operations.

**Definition (inventory consistency).** `R` is *globally consistent* over the sub-chain
cover `{𝒞, 𝒟}` iff it admits a global section compatible across both factors — equivalently
iff `R` satisfies the sheaf condition for that cover:
`0 → R(𝒮) → R(𝒞) ⊕ R(𝒟) → R(O)` is exact and the gluing map is onto the equalizer.

A global section of a presheaf is a family `(x_a ∈ R(a))_{a∈O}` with
`R(f)(x_{\mathrm{cod}\,f}) = x_{\mathrm{dom}\,f}` for every `f`. For a **transport** local
system (each `R(f)` a translation by `δ_f ∈ A`), this says `δ_f = φ(\mathrm{cod}) −
φ(\mathrm{dom})` for a node-potential `φ` — i.e. the 1-cochain `δ` is a **coboundary**.
The obstruction is its class

> `[θ_R] := [δ] ∈ H¹(𝒮; R)`.

**Three contrasting facts:**

1. `[θ_R]` depends on the **resource presheaf `R`**, not on how `𝒮` factors.
2. Its **coefficient system is `R`** (stock groups), not `𝒟`.
3. It is a **degree-1** class (loop/route discrepancy).

---

## 3. Lemma A — the matched-pair law is invisible to inventory

> **Lemma A (no-λ-correction).** Let `𝒮 = 𝒞 ⋈ 𝒟` and `R : 𝒮^op → Set` any presheaf. A
> family `(x_a)_{a∈O}` is a global section of `R` over `𝒮` **iff** it is compatible with
> every `𝒞`-morphism and every `𝒟`-morphism. The matched-pair law `λ` plays no role.

**Proof.** (⟹) is immediate: `𝒞`- and `𝒟`-morphisms are morphisms of `𝒮`.

(⟸) Compatibility of a family with a morphism — `R(f)(x_{\mathrm{cod}}) = x_{\mathrm{dom}}`
— is closed under composition: if `R(g)(x_{\mathrm{cod}\,g})=x_{\mathrm{dom}\,g}` and
`R(h)(x_{\mathrm{cod}\,h})=x_{\mathrm{dom}\,h}` with `cod h = dom g`, then by functoriality
`R(g∘h)(x_{\mathrm{cod}\,g}) = R(h)(R(g)(x_{\mathrm{cod}\,g})) =
R(h)(x_{\mathrm{dom}\,g}=x_{\mathrm{cod}\,h}) = x_{\mathrm{dom}\,h}`. Since `𝒞 ∪ 𝒟`
generates `𝒮` (every morphism is a word in `𝒞`- and `𝒟`-arrows, by the factorization
`f=c·d`), a family compatible with all generators is compatible with all morphisms. The
rewriting `λ` converts `𝒟𝒞`-words to `𝒞𝒟`-words but never changes the *morphism*, hence
never changes the compatibility constraint. ∎

**Consequence.** The set of consistent inventories is cut out entirely by the `𝒞`- and
`𝒟`-constraints. The weld `λ`/`[ω]` cannot inject content into the gluing problem **as long
as `𝒮` is a well-defined category at all**. Inventory consistency is therefore exactly the
degree-1 amalgamation problem for the cover `{𝒞, 𝒟}`.

**Verification.** Brute-forced on a genuinely non-trivial ZS product (the flip matched
pair on two objects, `t₁·c = c·t₀`, `λ ≠ id`): over all functorial `R` on `ℤ/3`, the global
sections equalled the `{𝒞,𝒟}`-generator-compatible families, every time
(`scratch/zs_presheaf_sections.py`).

---

## 4. Theorem 1 — inventory consistency is a degree-1 class

> **Theorem 1.** Let `𝒮 = 𝒞 ⋈ 𝒟` (so `[ω]=0`, the decomposition exists) and `R` a resource
> local system of abelian stock-groups. Then global inventory is consistent **iff**
> `[θ_R] = 0 ∈ H¹(𝒮; R)`. When `𝒞` and `𝒟` are acyclic ("tree-like" procurement and
> delivery, `H¹(𝒞;R)=H¹(𝒟;R)=0`), Mayer–Vietoris for the cover gives the closed form
>
> `H¹(𝒮; R) ≅ coker[ H⁰(𝒞;R) ⊕ H⁰(𝒟;R) → H⁰(O;R) ]`,
>
> i.e. the obstruction is exactly the **reconvergence discrepancy**: the failure of the
> node-potentials determined on each factor to agree on the shared nodes.

**Proof.** By Lemma A a global section is a family satisfying the `𝒞`- and `𝒟`-constraints.
For a transport local system this is precisely a node-potential `φ` with `δ = d⁰φ` — the
statement that the 1-cochain `δ` is a coboundary, i.e. `[θ_R]=[δ]=0` in `H¹(𝒮;R)`. For the
closed form: the cover `{𝒞,𝒟}` with discrete overlap `O` presents `𝒮` as a pushout of
categories glued over `O` (then quotiented by `λ`, which by Lemma A is inert on sections),
and the Mayer–Vietoris sequence of the cover reads
`0 → H⁰(𝒮) → H⁰(𝒞)⊕H⁰(𝒟) → H⁰(O) → H¹(𝒮) → H¹(𝒞)⊕H¹(𝒟) → ⋯`.
Discrete `O` kills `H^{≥1}(O)`, and the two-piece cover with discrete overlap has no higher
Čech terms (a "good cover"); acyclic factors kill `H¹(𝒞)⊕H¹(𝒟)`, leaving
`H¹(𝒮;R) ≅ coker[H⁰(𝒞)⊕H⁰(𝒟) → H⁰(O)]`. ∎

**Example (the discriminator PROVE.md itself proposed).** Reconvergent diamond
`a→b→d`, `a→c→d`, two routes. `betti₁ = 4−4+1 = 1`, so `H¹(𝒮;A)=A`: the single class is
the loop-sum `δ_p+δ_r − δ_q−δ_s`. With deltas `(2,1,1,3)` the holonomy is `−1 ≠ 0` — stock
at `d` differs by route — **inconsistent**, and the class is the generator of `H¹`. A
coboundary `δ = d⁰φ` is consistent. **Degree 1, unambiguously**
(`scratch/supply_chain_obstruction.py`). Over `ℤ/n` the loop-sum lives in `ℤ/n` and the
`gcd` engine applies (`H¹(C_k;ℤ/n)=ℤ/\gcd`).

---

## 5. Theorem 2 — the two classes are independent (refutation of (C))

> **Theorem 2 (separation).** `[θ_R] ∈ H¹(𝒮;R)` and `[ω] ∈ H²(Sk_𝒮;𝒟)` are logically
> independent. Explicitly, both of the following occur:
> - **`[ω]=0` with `[θ_R]≠0`** (chain decomposes, inventory inconsistent);
> - **`[ω]≠0` with `[θ_R]=0`** (chain does not decompose, inventory trivially consistent).
> Hence **neither implication** of conjecture (C) holds. Moreover the two classes live in
> **different degrees** and over **different coefficient systems** (`R` vs `𝒟`).

**Proof.**

*Witness W1 (breaks "⟸": `[ω]=0 ⇏` consistent).* Take `𝒮` = the **free category on the
diamond quiver** `a⇉{b,c}⇉d` (distinct routes `rp ≠ sq`). The quiver is directed-acyclic,
so `𝒮` has **no non-identity invertibles**; the weld coefficient system is the trivial
group, `𝒟 = 0`, whence `H²(Sk_𝒮;𝒟)=H²(Sk_𝒮;0)=0` and **`[ω]=0` is forced**. (Indeed a
free category is a strict factorization system with nothing to obstruct.) Yet
`B𝒮 ≃` the diamond graph has `betti₁=1`, so `H¹(𝒮;R)=R`; choosing any transport system
with nonzero loop holonomy gives `[θ_R]≠0` — inventory inconsistent. □

*Witness W2 (breaks "⟹": consistent `⇏ [ω]=0`).* Take `𝒮` = the **rigid-twist category**
of `g-obstruction-is-h2-class` (branch `a → x ⇉ y`, `End(a)=ℤ/2`, twist `s₂∘p=(s∘p)·g`),
for which `[ω]` is the generator of `H²(Sk;ℤ/2)=ℤ/2`, **`[ω]≠0`** (proved, cited). Equip it
with any **coboundary** inventory `δ = d⁰φ` (e.g. the zero system). By construction such an
inventory is globally consistent, `[θ_R]=0`, while `[ω]≠0`. □

The coefficient systems differ: in W1 the weld coefficient `𝒟` is forced to `0` while the
resource coefficient `R` is nonzero; the classes cannot be compared by any natural map, let
alone identified. ∎

**Reading.** `[ω]` answers *"does the supply chain even factor as procurement ⋈ logistics,
as the ZS model asserts?"* — a structural precondition. `[θ_R]` answers *"given the
operations, does stock glue to a route-independent inventory?"* — the actual consistency
question. (C) conflated a precondition in degree 2 with the consistency class in degree 1.

---

## 6. Where (C) came from — and why there is no supply-chain regime that rescues it

The conjecture is not arbitrary; it is a false generalization of **blockchain re-entrancy**
(`[ω]=ε ∈ H²≅ℤ/2`, lean-verified). It is worth stating precisely why the template does not
transfer — this is the heart of the dividing line.

> **Proposition 3 (no rescue regime).** There is no non-degenerate supply chain in which
> inventory consistency of a resource presheaf `R` literally equals `[ω]=0`. The appearance
> of equivalence in re-entrancy is **not** a special case of (C); it is a *different
> problem* in which there is no separate resource presheaf at all.

**Why.** Inventory consistency is `[θ_R]=0` in degree 1 with coefficients `R` (Thm 1);
`[ω]=0` is a degree-2 condition with coefficients `𝒟`. A would-be rescue would need a
natural iso `H¹(𝒮;R) ≅ H²(Sk_𝒮;𝒟)` identifying the two classes. No such iso exists in
general: there is no suspension or dimension-shift relating a degree-1 presheaf class to a
degree-2 weld class with different coefficients (e.g. for the free loop `𝒮=Bℤ`,
`H¹(Bℤ;A)=A` while `H²(Bℤ;A)=0` — the degrees genuinely do not match). Theorem 2's two
witnesses already show the classes vary independently.

**What re-entrancy actually is.** In re-entrancy the "conserved quantity" **is the weld
state itself** — the composite protocol's own state, living *in* the matched pair, not on a
separate presheaf of nodes. There `[ω]` is the whole story because there is nothing else:
inventory = weld-state by construction, so its consistency obstruction *is* the weld `H²`.
Conjecture (C) silently imported this identification — "inventory = weld-state" — into
supply chains, where it is false: supply-chain stock lives on the **nodes**, transported by
operations, and is a genuinely separate degree-1 datum. This is the same "rhyme, not
identity" trap as `two-omega-sites-not-isotropy-restriction`, one degree down: same cyclic
group can appear, but the *site*, the *coefficients*, and now the *degree* differ — always
check before identifying.

---

## 6.5 Reconciliation with the `W_{n,ε}` model (`supply-chain-zs`, computed)

The prior `computed` node `supply-chain-zs` (2026-07-23) models "inventory inconsistency
between two routes" by the warehouse family `W_{n,ε}`: objects `Wh, Pr, De`, with
`s·p = q` and `s₂·p = q·τ^ε`, and computes `[ω]=ε ∈ H²(Sk_𝒞;ℤ/n)`. This is **correct for
the shape it uses** — but that shape decides *which* of the two consistency notions it
captures, and it is **not** the one the phrase "two routes" most naturally names.

Look at the geometry. In `W_{n,ε}` the "two routes" are the **parallel arrows** `s, s₂`
sharing the *same* source and target (a rigid twist `a → x ⇉ y`); they differ by a
**vertex-group** element `τ^ε`. A loop built from parallel arrows closes inside a single
hom-set — its class lives in the **vertex group**, hence in `H²(Sk;𝒟)`. That is genuinely a
**weld** phenomenon: whether the lot-cursor algebra closes into a distributive law. Call it
**provenance/cursor consistency** — a legitimate degree-2 question.

Contrast the honest "two routes to a delivered good": `a → b → d` and `a → c → d` through
**distinct intermediate nodes** (the diamond, §4). Here the loop runs through the **nerve**
of `𝒮`, not a single hom-set; its class lives in `H¹(𝒮;R)`. This is **node-stock
consistency** — degree 1.

So the two models are the two sides of the dividing line, cleanly distinguished by *where
the reconvergence loop lives*:

- **parallel arrows / vertex-group loop** (`W_{n,ε}`) → `H²(Sk;𝒟)` — weld/provenance;
- **distinct-node reconvergence / nerve loop** (diamond) → `H¹(𝒮;R)` — node stock.

The `supply-chain-zs` node therefore computed the **weld-provenance** class and labelled it
"inventory inconsistency between two routes." Under the natural reading of that phrase
(distinct routes, reconvergent stock) the obstruction is `H¹`, and Theorem 2 shows it is
independent of the `H²` the node computed. The node is not *wrong* — it is a correct
computation of the **other** class; it should be **relabelled** provenance/weld-consistency,
and the node-stock equivalence demoted from the `computed` root's blanket claim.

## 7. The crown jewel: *degree tells you where the conserved quantity lives*

The honest result is more valuable than (C) would have been. It gives a **classification of
compositional failure by cohomological degree**, keyed to the *locus* of the conserved
quantity:

| Conserved quantity lives… | Failure class | Economic instance |
|---|---|---|
| on the **nodes** (transported by operations) | `[θ_R] ∈ H¹` — route discrepancy | **supply-chain inventory** |
| in the **weld** (the composite's own state) | `[ω] ∈ H²` — handoff order | **blockchain re-entrancy** |
| in the **factorization existing at all** | `[ω] ∈ H²` — transversal closure | does the chain decompose? |

So supply chains are **not** the "second instance of failure = nonzero `H²`." They are the
**first clean instance of failure = nonzero `H¹`** (route/reconvergence discrepancy) — a
distinct and arguably more common economic failure mode. The grant's Applications/Impact
story is **sharpened**, not weakened: two compositional failure modes, cleanly separated by
degree, each with an economic witness.

---

## 8. Verification summary

- `scratch/supply_chain_obstruction.py` — diamond & 3-cycle inventory obstruction is
  `H¹` (loop discrepancy); over `ℤ/n` reduces mod `n` via the `gcd` engine.
- `scratch/zs_presheaf_sections.py` — Lemma A brute-checked on a non-trivial ZS product
  (flip matched pair, `λ≠id`): global sections = `{𝒞,𝒟}`-compatible families, always.
- `scratch/separation_witnesses.py` — W1 (`[ω]=0, [θ]≠0`) and W2 (`[ω]≠0, [θ]=0`) verified.

## 9. Gaps / scope boundary (honest)

1. **Torsor/gerbe-valued inventory.** Lemma A is for inventory valued in a **sheaf of
   groups** (stock levels). If inventory is valued in **torsors** (stock defined only up to
   a gauge/allocation choice), gluing becomes a gerbe problem and the obstruction *does*
   rise to `H²`. Then a genuine degree-2 inventory obstruction exists — but it is a *higher
   gauge* class, still not equal to the weld `[ω]` (different coefficients). Characterizing
   it and its relation to `[ω]` is the natural follow-up (likely another "rhyme, not
   identity"). Marked open.
2. **Non-acyclic factors.** The closed form in Thm 1 assumes `H¹(𝒞)=H¹(𝒟)=0`. For factors
   with their own loops, `H¹(𝒮;R)` acquires the `H¹(𝒞)⊕H¹(𝒟)` summand; the equivalence
   "consistent ⟺ `[θ_R]=0`" still holds (Lemma A is unconditional), only the closed-form
   decomposition changes. No gap in the main theorems; only in the explicit formula.
3. **Prop 3 suspension iso** is stated for the one-object transport case; the general
   "when does node-`H¹` map onto weld-`H²`" (a connecting map in the descent spectral
   sequence of the `{𝒞,𝒟}` cover) is sketched, not fully developed. Not needed for Thms 1–2.

## 10. Bottom line

Conjecture (C) is **false**: inventory consistency is **not** the vanishing of the ZS weld
class. It is the vanishing of a **degree-1** class `[θ_R] ∈ H¹(𝒮;R)` on the resource
presheaf — the route/reconvergence discrepancy — which is **independent** of the degree-2
weld class `[ω] ∈ H²(Sk_𝒮;𝒟)` (different degree, different coefficients, neither implies the
other). (C) was a false generalization of re-entrancy, where inventory *is* the weld-state
and so no separate resource presheaf exists; supply chains carry stock on the nodes, one
degree down. The payoff is a clean classification: **the cohomological degree of a
compositional failure records where the conserved quantity lives — on the nodes (`H¹`,
route discrepancy) or in the weld (`H²`, handoff order).**
