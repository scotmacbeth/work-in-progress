# Liftings of container monads along `cod`: the general-M reduction, the monoid/comonoid unification, and a companion corroboration of "Reader = small categories"

**MacBeth — PROVE session, 2026-08-09 (deep-work), afternoon.**

**Relation to prior work.** The Reader case of `state/PROVE.md` was *already settled* this morning in
`2026-08-09-reader-liftings-are-categories.md` (node target `pi-sigma-dichotomy-exhaustive`): the
∏/Σ/mix conjecture is **false**, and the fibred polynomial monad liftings of Reader `y^E` are exactly
**`E`-indexed small categories** (polynomial comonads ≅ `Cat`). This file does **not** re-claim that.
It contributes three things the morning file did not:
1. an **independent corroboration** of the refutation, via *different* computations (genuine
   container-monad-law checks on weighted-Σ; certification of the `Q^M` comonad and a monad-morphism;
   an empty-preservation necessary-condition search);
2. the **general-M object-level reduction** (Prop A′: liftings of *any* container monad `M` ↔ a
   *family* of aggregator functors, one per `M`-shape) — the first step of the morning file's OPEN
   §7 (State / general container monads);
3. two reusable lemmas — the **monoid/comonoid unification** ("∏ needs a monoid, Σ needs nothing")
   and the **pullback-along-a-monad-morphism** construction — and a **precise reduction of the
   State/general-M problem** to a shape-monoid-graded "threaded category," with the forward
   construction and the coupling formula pinned down. State itself remains **open** (flagged).

Registry: node `pi-sigma-dichotomy-exhaustive` (target, shared with the morning file); this file adds
child `general-M-reduction` and `monoid-comonoid-unification`.

---

## 0. Headline

> **Monad liftings are comonads, and the comonad needs an algebra on its index.** A monad lifting's
> multiplication is a *backward* container map, hence a **comultiplication**; so an aggregator is a
> monad lifting iff it carries a **comonad** structure. The two "canonical" aggregators are comonads
> exactly when the relevant index has the needed algebra:
> * **Σ = coproduct** — a comonad for **every** index (the free/discrete comonoid). *Always lifts.*
> * **∏ = product over `I`** — a comonad **iff `I` is a monoid**. *Lifts iff a monoid exists.*
>
> This single law explains the morning file's classification (Reader survivors = small categories:
> products appear only *within one leaf*, as the hom-set of a possibly-non-discrete category, never
> *across* leaves) **and** all six prior "polynomial-not-analytic / cartesian / monoid" boundaries,
> and it is `T_M`-monad-⟺-`M`-cartesian (`proof-relevance-boundary`) read one categorical level down.
>
> **General M (new).** A fibred lifting of a container monad `M=(S_M,P_M)` along `cod:Cont→Set` is a
> **family of aggregators** `(A_σ:Set^{P_M σ}→Set)_{σ∈S_M}` (Prop A′). The monad structure **threads
> the family through `M`'s multiplication**: for State, shapes `S^S` form the transformation
> **monoid** under composition and the comultiplication couples `A_t` via `σ_μ(s)=t_s(T(s))` — an
> `S^S`-graded "threaded category." Reader is the special case `S_M=1` (a *single* aggregator ⟹ plain
> `E`-indexed categories). This makes precise, and gives the forward construction for, the morning
> file's conjecture "monad liftings of `M` ↔ categories fibred over `M`."

---

## 1. Setup (shared with the morning file)

Containers `C=(S,P)`, `P:S→Set`, `⟦C⟧X=∐_s X^{P s}`; morphism `(u,φ)` forward `u`, **backward**
`φ_s:P'(us)→P s`; cartesian iff each `φ_s` bijective. `Cont≃Poly` monoidally (`◁`=comp, unit `y`).
The **codomain fibration** `cod:Cont→Set`, `(S,P)↦S`, has fibre `(Set^S)^{op}` over `S`
(`contravariance-is-fibrewise-op`, von Glehn TAC 33); reindexing = precomposition, strict/split. A
**fibred lifting** of `M:Set→Set` is a cartesian-arrow-preserving `L:Cont→Cont` with `cod L=M cod`;
a **monad lifting** adds `(η^L,μ^L)` projecting to `(η,μ)`. "Proof-relevant" = `Type`-valued
positions.

---

## 2. Object level: fibred liftings ↔ aggregator functors (general M — new)

The morning file proved the Reader reduction (its Prop 2.1). I record the general-`M` version, which
it did not, as it is the entry point to the open State case.

> **Proposition A′ (general container monad).** For `M=(S_M,P_M)`, `MX=∐_{σ}X^{P_M σ}`, fibred
> liftings of `M` along `cod` are in bijection with **families of covariant functors**
> `(A_σ : Set^{P_M σ} → Set)_{σ∈S_M}`, via
> `L(C)(σ,x) = A_σ(x^*P)` for `(σ,x)∈MS`, `x:P_M σ→S`, `x^*P=P∘x`.

*Proof.* Given a lifting `L`, `L(S,P)=(MS, \tilde P)`. For `(σ,x)∈MS` (`x:P_M σ→S`), the morphism
`α:(P_M σ, P∘x)→(S,P)`, `α=(x, \mathrm{id})`, is **cartesian**. `L` preserves cartesian arrows, so
`Lα` is cartesian over `Mx:M(P_M σ)→MS`; its backward map at the "generic" shape
`(σ,\mathrm{id})∈M(P_M σ)` (which `Mx` sends to `(σ,x)`) is a bijection
`\tilde P(σ,x)≅\widetilde{(P∘x)}(σ,\mathrm{id})`. Define `A_σ(Q):=\tilde Q_{(P_M σ,Q)}(σ,\mathrm{id})`;
then `\tilde P(σ,x)=A_σ(x^*P)`. Reindexing (`Mu`, `u:S→S'`) fixes the shape `σ`, so the `A_σ` are
independent across `σ` and each is a functor by vertical functoriality of `L`. Conversely any family
`(A_σ)` yields a fibred `L` by the formula. Mutually inverse. ∎

Reader: `S_M=1`, one `A:Set^E→Set` (morning Prop 2.1). State `MX=(S×X)^S=∐_{t∈S^S}X^S`: shapes
`S^S`, positions `S`, so a family `(A_t:Set^S→Set)_{t∈S^S}`. **No dichotomy at the object level** —
every family lifts; the content is in the monad structure (§6).

---

## 3. The monad structure is a comonad structure

Unwinding `(η^L,μ^L)` (all backward maps) for Reader (`S_M=1`, aggregator `A:Set^E→Set`):
* **unit** = a **counit** `u:A∘Δ⇒Id` (`Δ:Set→Set^E` constant), `u_V:A(ΔV)→V`;
* **mult** = a **comultiplication** `m:A(−∘δ)⇒A(A∘\hat{−})` on `Set^{E×E}` (`δ:E→E×E` diagonal);
* **monad laws** = counit + coassociativity.

So monad liftings are **δ-comonoids** ("comonads"), not (co)limits. (This is the morning file's
"monad↔comonad twist," recorded here as the structural reason the whole classification is comonadic.)

---

## 4. Unification lemma: ∏ needs a monoid, Σ needs nothing (new framing)

> **Lemma U (Σ side).** For every `(K, e:K→E)`, `A(Q)=∐_{k∈K}Q(e_k)` is a monad lifting of `R_E`,
> with comonad data the canonical comonoid `(K,\mathrm{diag},!)`. (`= ∐_{e∈E}W_e×Q_e`, `W_e=e^{-1}(e)`.)

*Proof.* `u`=fold, `m:∐_k h(e_k,e_k)→∐_k∐_{k'}h(e_k,e_{k'})`, `(k,x)↦(k,k,x)`. The three monad laws
are the counit and coassociativity of `(K,\mathrm{diag},!)`, which hold for the unique comonoid on
any set; `e` is inert in the laws. ∎  *(In the morning file's terms these are the **discrete**
categories on the objects `K` with `λ=e`; `|W_e|≥2` is a discrete category with repeated objects —
outside Σ/∏/mix, corroborating the refutation.)*

> **Lemma U (∏ side).** For every **monoid** `M`, `A(Q)=Q(e_0)^M` is a monad lifting of `R_E`, via
> `ev_{e_0}:R_E⇒Id` (monad morphism) pulled back over the reader-comonad lift `C_M(S,P)=(S,P^M)`.

*Proof.* (1) `ev_{e_0}:(1,E)→(1,1)` (backward `e_0:1→E`) gives `ev_{e_0}:X^E→X`, `m↦m(e_0)`; it is a
monad morphism `R_E⇒Id` (unit `const_x↦x`; mult `μ g↦g(e_0)(e_0)` matches `ev∘R_E ev`). (2) `Q↦Q^M`
is a comonad on `Set` iff `M` is a monoid (counit `f↦f(1_M)`, comult `f↦(m↦m'↦f(m·m'))`); a fibred
comonad is a monad lifting of `Id` (§3, `E=1`). (3) Reindexing a monad lifting along a monad morphism
is a monad lifting; along `ev_{e_0}` this gives `A(Q)=Q(e_0)^M`. ∎ *(Morning file's terms: the
**one-object category = monoid `M`** on leaf `e_0`; `M=ℤ/2` is the one-object groupoid `B_0×B_0`.)*

> **The slogan.** Σ (coproduct) is a comonad for any index — the free comonoid; ∏ (product over `I`)
> is a comonad **iff `I` is a monoid**. Reader's leaf-set carries the canonical *comonoid* (diagonal)
> but generally no *monoid*, so **Σ lifts and full-∏ over `E` does not** — cross-leaf products need a
> map `E×E→E`. An *auxiliary* monoid supplies its own multiplication, so ∏-over-`M` (at a single
> leaf) lifts. This **is** `T_M`-monad-⟺-`M`-cartesian one level down (`proof-relevance-boundary`,
> `lean-tm-cartesian-boundary`): cartesian `μ_M` = a bijective, monoid-like law on positions;
> non-cartesian = leaves drop = no monoid = ∏ fails. Six prior boundaries, one law.

---

## 5. Independent corroboration (computation)

`scratch/dichotomy-exhaustiveness/` — my files this session, independent of the morning engines:
* `liftings.py` — implements `L^A` as a genuine `Cont`-endofunctor for the weighted-Σ family and
  checks the monad laws: **left/right unit as actual container-morphism backward-map composites**
  (`=id`), **associativity as coassociativity of the position-comonoid**. Pass for `Σ`, `W_0=2`,
  projection `Q_0`, `W_0=2,W_1=3`. ✓ (Lemma U, Σ side.)
* `comonad_check.py` — `Q↦Q^M` comonad laws hold for `M∈{ℤ/2, AND-monoid}`, **fail** for a non-unital
  table (the check discriminates monoids); `ev_{e_0}:R_E⇒Id` is a monad morphism (`E=2,3`). ✓
  (Lemma U, ∏ side.)
* `search.py` — necessary condition (multiplication empty-preserving) over polynomial aggregators
  `∐_i Q_0^{a_i}Q_1^{b_i}` (`E=2`): `Q_0·Q_1` (∏ over distinct leaves = All) **fails** (witness
  `h_{00}=h_{11}≠∅, h_{01}=h_{10}=∅`); `Q_0` (proj), `Q_0+Q_1` (Σ), `Q_0^2` (∏-over-monoid at a leaf)
  **pass**. Cross-leaf products die; single-leaf powers/coproducts survive — matching the morning
  classification. ✓
* `state_setup.py` — State container form `∐_{t∈S^S}X^S`; the threading `σ_μ(s)=t_s(T(s))`; `η`-shape
  `=id` (unit constrains only `A_{id}`). ✓ (feeds §6.)

These reach the same verdict as the morning `monad.py`/`enum.py`/`catcount.py`/`analytic.py` by
different routes — genuine independent confirmation.

---

## 6. The open frontier: State and general M as a shape-monoid-graded threaded category (new reduction)

By Prop A′, a lifting of `M` is a family `(A_σ)_{σ∈S_M}`. Unwinding `(η^L,μ^L)` for general `M`:

* **Unit.** `η^L` lies over `η_M`, which hits a *single* distinguished shape (the unit shape `η_S`).
  For State `η_{S_0}(s_0)=(\mathrm{id}, \mathrm{const}_{s_0})`: the unit therefore gives a counit
  **only for `A_{\mathrm{id}}`**; the `A_t` (`t≠\mathrm{id}`) are untouched by the unit. (Verified,
  `state_setup.py`.)
* **Multiplication.** `μ^L` lies over `μ_M`, whose backward map is the ◁-monoid section. For State,
  `μ` **threads**: with outer next-state `T∈S^S` and inner next-states `(t_s)_{s∈S}`, the composite
  shape is `σ_μ(s)=t_s(T(s))`, and the comultiplication couples
  `A_{σ_μ} ⟶ A_T(\,s↦A_{t_s}(\,·\,)\,)` — the aggregator family multiplied along **composition in the
  transformation monoid `(S^S,∘)`**. (Coupling formula verified, `state_setup.py`.)

> **Reduction (State/general M).** A monad lifting of `M` is the aggregator family `(A_σ)_{σ∈S_M}`
> made into a comonoid **graded over the shape-structure of `M`**: for Reader `S_M=1` (trivial
> grading) this is a single δ-comonoid = an `E`-indexed small category (morning theorem); for State
> the grading is the monoid `(S^S,∘)` and the comultiplication threads through it — an
> "`S^S`-graded / store-internal category." Reader = the `S_M=1` slice.

**Forward construction (what definitely gives State liftings).** Since State is a container
(triangle-)monoid, **Σ = State◁− lifts** (`sigma-monad-is-triangle-monoid`); the discrete/weighted-Σ
variants (duplicate state-positions) lift by Lemma U applied fibrewise per shape, provided the
duplication is carried consistently by the threading (`A_t(Q)=∐_{k∈K}Q(κ(t,k))` with `κ` compatible
with composition) — these are the "discrete store-internal categories." I give the construction but
**do not** prove it exhausts the liftings.

**What is NOT settled.** (i) A clean statement and proof that monad liftings of State ↔ [store-internal
/ `S^S`-graded small categories], analogous to Reader's. (ii) Whether the auxiliary-monoid-∏ transfers
to State — note `ev_{s_0}:State⇒Id` is **not** a monad morphism (state threading breaks it,
`state_setup.py`), so the Lemma-U(∏) route does not transfer verbatim; the ∏-flavoured State liftings,
if any, must come from monoids *internal to the store*. (iii) The general-M statement (categories
"fibred over `M`"). These are the live PROVE targets; §6 reduces them to a precise
shape-monoid-grading question but does not close them.

---

## 7. Honesty — status and gaps

* **Proved (this file):** Prop A′ (general-M object reduction); Lemma U both sides (weighted-Σ for all
  `(K,e)`; `Q_{e_0}^M` for all monoids `M`), giving an *independent* proof of the refutation;
  §3 (monad lifting = δ-comonoid, data correspondence); the State coupling formula `σ_μ(s)=t_s(T(s))`
  and the unit-touches-only-`A_{id}` fact.
* **Deferred to (proved, morning file `reader-liftings-are-categories`):** the *sharp* Reader
  classification — polynomial monad liftings of `R_E` ≅ `E`-indexed small categories; ∏ excluded;
  Σ_U = discrete categories; analytic excluded by the counit. I corroborate; I do not re-derive.
* **Cited (proved/published elsewhere):** `T^Σ_M=M◁−`, Σ ⟺ container-monad, Bag refutation
  (`sigma-monad-is-triangle-monoid`); `T_M`-monad ⟺ cartesian (`proof-relevance-boundary`,
  `lean-tm-cartesian-boundary`); polynomial comonads ≅ small categories (Ahman–Chapman–Uustalu);
  `Cont`-fibre `=(Set^S)^{op}` (von Glehn TAC 33). Standard: `Q^M` comonad ⟺ `M` monoid; reindexing a
  monad lifting along a monad morphism is a monad lifting (used only for `Id`-target).
* **Open / gaps:** the **State and general-M classifications** (§6) — reduced to a shape-monoid-graded
  threaded-category question, forward construction given, completeness NOT proved; the auxiliary-∏
  transfer to State (no `ev` monad morphism); a full removal of the *polynomial* hypothesis (needs
  "every accessible Set-comonad with a counit is polynomial", per the morning file's §7). These are
  the next PROVE targets, and the natural expository/Ch7 rung is the substitution-monoidal structure
  whose comonoids are these liftings.

---

## 8. One line

A monad lifting's multiplication is a *backward* map, hence a **comultiplication** — so liftings of a
container monad `M` along `cod:Cont→Set` are **comonads graded over `M`'s shapes**: for Reader this is
the morning theorem (survivors = `E`-indexed small categories), governed by the one law **∏ needs a
monoid, Σ needs nothing** (= the cartesian boundary, one level down); the general-M reduction (Prop A′
+ the State threading `σ_μ(s)=t_s(T(s))`) turns "liftings of State" into a store-internal graded
category and is the open frontier this session pins down but does not close.
