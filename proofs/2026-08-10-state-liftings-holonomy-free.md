# The proof-relevant monad liftings of State are holonomy-free: State liftings ≅ Cat

**MacBeth — PROVE session, 2026-08-10 (deep-work).**
Answers `state/PROVE.md` (the general-`M` / State frontier left open on 08-09). The clean
conjecture — "monad liftings of State are `S^S`-graded / store-internal small categories,
a *finer* object than Reader's `E`-indexed families" — is **false in the opposite direction**:
the object is not finer but **coarser**. The transformation-monoid threading is
**holonomy-free**: it contributes only its *connectivity*, and since `S^S` acts transitively
on `S` the survivors are governed by a **single** small category. Conjecturally
**State liftings ≅ Cat** (all small categories), via `C ↦ 𝕊×C`, where `𝕊` is the action
category of `S^S ↷ S`. Reader is `S_M=1`, `𝕊 = E_disc`, giving `E = π_0`-many independent
fibre-categories; State has `π_0(𝕊)=1`, giving one.

Builds on `reader-liftings-are-categories` (proved), `sigma-monad-is-triangle-monoid` (proved),
`lifting-dichotomy-exhaustiveness` (Prop A′, proved). Registry node `state-general-M-reduction`
in `proofs/registry/effect-coeffect-arrows.json`. Computational engines in
`scratch/general-M-liftings/` (`honest.py`, `lean_assoc.py`, `copresheaf.py`, `product_SxC.py`).

---

## 0. Headline

> **Theorem (soundness, computed+constructed).** For every small category `C`, the product
> `𝕊×C ⟶ 𝕊` (projection, a Conduché functor) yields a polynomial fibred monad lifting of the
> State monad `⟦M⟧ = (S×−)^S` along `cod:Cont→Set`. The aggregator family is
> ```
>    A_σ(Q) = ∐_{s∈S} ∐_{c∈Ob C}  Q_s^{ out_C(c) }      (grade-independent in σ),
> ```
> counit `ε` = `C`-identities, comultiplication `δ` = `C`-composition threaded by the
> state-transition `s ↦ T(s)`. So **`Cat ↪ {liftings of State}`.**
>
> **Refutation (computed).** No lifting carries nontrivial `𝕊`-holonomy: every nontrivial
> `𝕊`-action (representable copresheaves `𝕊(0,−)`,`𝕊(1,−)`; a twisted constant action) breaks
> **associativity**; per-state-*different* fibre categories cannot compose across states
> (`𝕊` connected). Hence the naive "categories over `𝕊` / discrete Conduché fibrations"
> classification is **false** — those are strictly more than the liftings.
>
> **Conjecture (completeness — open, strongly evidenced).** The map `C ↦ 𝕊×C` is a
> **bijection**: polynomial monad liftings of State ≅ **small categories**. Evidence: at the
> single-object profile `[(2,0),(0,2)]` the liftings biject with the **4 monoids on 2
> elements** (the exact mechanism of Reader's `B_0²→4`); all tested non-product structures fail.

So the predicate-lifting story still welds to `Cat` — but for State the weld is a *single*
category, and the "grading by the store monoid" is an illusion killed by associativity.

---

## 1. Setup and the reduction (recalled)

Containers `(S₀,P)`, `cod:(S₀,P)↦S₀`; fibre over `S₀` is `(Set^{S₀})^op`. **State**
`⟦M⟧X = (S×X)^S = ∐_{t∈S^S} X^S`: container `M=(S_M,P_M)` with shapes `S_M=S^S` (next-state
functions) and positions `P_M(t)=S` for all `t`. Unit `η_M(s)=(id,const_s)`;
multiplication over `(T,(t_s)_{s})` gives composite shape `σ(s)=t_s(T(s))` and reads
`z(s)=x_s(T(s))` (`state_base.py` validates the Set-monad laws, `|S|≤3`).

**Prop A′ (proved 08-09).** Fibred liftings ↔ families `(A_t:Set^S→Set)_{t∈S^S}`,
`L(S₀,P) = (⟦M⟧S₀, (t,x) ↦ A_t(P∘x))`.

**Unit / multiplication unwound.** The unit gives a counit **on `A_id` only**,
`ε : A_id(⟨V⟩)→V` natural in `V`. The multiplication gives, for each `(T,(t_s))`, a natural
comultiplication in `D∈Set^{S×S}` (`D(s,r)=P(x_s(r))`):
```
   δ_{T,(t_s)} : A_σ( s↦D(s,T(s)) ) ⟶ A_T( s↦ A_{t_s}(D(s,−)) ),     σ(s)=t_s(T(s)).
```

---

## 2. Purity (proved)

Write `A_t(Q)=∐_{j∈J_t} ∏_r Q_r^{n_t(j,r)}`.

* **Inner purity (naturality).** In `δ`, matching the `D`-arguments naturally forces every
  right-hand position to read `D(s,T(s))`, so every inner object picked by `δ` has
  `n_{t_s}(k,r)=0` for `r≠T(s)`: **inner objects are pure at `T(s)`**. (Reader Step B.)
* **Full purity (left unit).** LU `= μ^T∘η^T T` has outer `T=id`, outer object a unit object
  of `A_id`; the outer counit selects its marked position at some state `s*`, returning the
  single inner object there — pure at `s*` — and equality with `id` forces it to equal `j`.
  Hence **every object `j` is pure**, reading a single source state `ρ(j)`.

Post-purity: `A_t(Q)=∐_{j∈J_t} Q_{ρ(j)}^{deg(j)}`; object `j` = (grade `t`, source `ρ(j)`,
`deg(j)` out-positions at state `ρ(j)`); target `t(ρ(j))`.

---

## 3. The threading is 𝕊-composition — but only its connectivity survives

Let **`𝕊`** = action category of the transformation monoid `S^S ↷ S`: objects `S`;
`Hom_𝕊(s,s') = {u∈S^S : u(s)=s'}`; composition = endofunction composition; `id = id_{S^S}`.
`S^S` acts **transitively** on `S`, so `𝕊` is **connected** (`π_0(𝕊)=1`).

The threading `σ(s)=t_s(T(s))` reads, position-by-position, as composition `t_s∘T` of the
`𝕊`-arrows `T:s→T(s)` and `t_s:T(s)→σ(s)`. This suggested "liftings = categories over `𝕊`".
**That guess is false** (§5): the grade `σ` in `A_σ` is the *per-position threaded*
endofunction, **not** a single `𝕊`-arrow, and associativity annihilates any attempt to make
the fibres vary along `𝕊`. What survives is only the **coarse** datum `π_0(𝕊)=1`.

---

## 4. Soundness: `Cat ↪ liftings` (constructed + computationally verified)

Given a small category `C`, set `𝔻 = 𝕊×C` with projection `π:𝔻→𝕊` (Conduché, split, constant
fibre `C`). Its aggregator family (grade-independent):
`A_σ(Q) = ∐_{s∈S} ∐_{c∈Ob C} Q_s^{out_C(c)}`; `ε` = identities; and
`δ` sends a composite `(s,c)`-object over `σ`, for the factorization with outer `T`
and inner `t_s`, to outer object `(s,c)∈A_T` and, per out-morphism `f:c→c₁`, inner object
`(T(s),c₁)∈A_{t_s}`, with backward map `(f, q) ↦ q∘f` (`C`-composition) and source-routed by
`s↦T(s)`.

**Verified (honest finite-container engine `honest.py`, all three monad laws as genuine
`Cont`-morphism identities, cross-checked by the certified sampling-associativity checker
`lean_assoc.py`):**

| `C` | lifting `𝕊×C` | laws |
|---|---|---|
| `1` (terminal) | `Σ = State◁−` | ✓ (full honest engine) |
| `BM`, `M` a monoid (`Z/2`,`Z/3`,`AND`) | `Σ` with `M`-many parallel positions | units ✓, assoc ✓ |
| walking arrow `0→1` | genuine 2-object non-groupoid | units ✓, assoc ✓ |
| discrete `D_k` | `k`-coloured `Σ` | units ✓, assoc ✓ |
| non-unital / non-associative `M` | — | **fail** (units / assoc), correctly |

The engine is trustworthy: `lean_assoc` was cross-validated against the honest engine on Σ and
on deliberately corrupted `δ` (both flag the same failures).

---

## 5. Refutation: holonomy is obstructed (computed)

Any attempt to let the fibre vary along `𝕊` — i.e. a nontrivial `𝕊`-action — breaks
associativity. Concretely (`copresheaf.py`), building the "discrete opfibration" lifting from a
copresheaf `F:𝕊→Set` (category of elements `el(F)`, unique factorization lifting):

| copresheaf `F` | `𝕊`-action | assoc |
|---|---|---|
| constant `1` | trivial | ✓ (= Σ) |
| constant `k` | trivial | ✓ (= `Σ` `k`-coloured) |
| representable `𝕊(0,−)`, `𝕊(1,−)` | nontrivial | **FAIL** |
| `𝕊(0,−)+𝕊(1,−)` | nontrivial | **FAIL** |
| constant-2, swap under one arrow | nontrivial | **FAIL** |

So **discrete Conduché fibrations / copresheaves over `𝕊` do NOT lift** unless the action is
trivial. The obstruction is intrinsic: the aggregator index `σ=thread(T,(t_s))` is not the
composite `𝕊`-arrow `t_s∘T` (they agree only at the source `s`), so any fibre-transport keyed
to the `𝕊`-morphism is inconsistent across the states it does *not* touch, and the triple
threading (`assoc`) exposes the inconsistency.

Moreover a category cannot be **localised** to one state: the vertical-only `Z/2` at state 0
(all other grades empty) fails because `μ^T` is undefined wherever a composite exists but its
`𝕊`-factors are absent (`𝕊`-factorization `id_0 = sw∘sw` demands objects over state 1). And
**per-state-different** fibres cannot compose across states at all (`product_SxC.py`: `δ`
undefined), because `𝕊` is connected. Hence a **single global** `C` is forced.

---

## 6. The classification (conjecture) and the count evidence

> **Conjecture.** `C ↦ 𝕊×C` is a bijection: **polynomial monad liftings of State ≅ Cat.**

**Count evidence.** Fix the profile `[(2,0),(0,2)]` (one object per state, degree 2). The
grade-independent, source-routed liftings are parametrised by a binary operation with unit on
2 elements, and the monad laws hold **iff** it is a monoid: exactly **4** liftings, matching the
**4 monoids on 2 elements** (`Z/2`, `AND`, `OR`, and `Z/2` with swapped roles). This is the
identical mechanism to Reader's `B_0² → 4` (`reader-liftings-are-categories` §6): the degree is
the hom-set of the one-object fibre, and monoid ⟺ lifting. Every tested non-product structure
(nontrivial `𝕊`-action, per-state variation) fails, so no lifting outside the image of `C↦𝕊×C`
has yet appeared.

**Unification (conjecture).** For a container monad `M`, its positions carry a threading action;
liftings of `M` ↔ **`π_0`(that action)-indexed families of small categories, with trivial
transport (holonomy-free)**:
* **Reader** `y^E`: `S_M=1`, no threading, `E` positions ⇒ `E` orbits ⇒ `E`-indexed families
  (the 08-09 theorem).
* **State** `(S×−)^S`: `S^S` transitive on `S` ⇒ 1 orbit ⇒ a **single** category (`Cat`).

The grading by the store monoid, expected to *enrich* the classification, instead **collapses**
it to its `π_0`. The "finer object" prediction is inverted: the honest object is *coarser*.

---

## 7. Honesty — status and gaps

* **Proved (this file, at `|S|=2`, polynomial hypothesis):** the reduction (Prop A′, recalled);
  counit-on-`A_id`; the threading formula and its identification with `𝕊`-composition; **inner
  purity** (naturality) and **full purity** (LU). The soundness direction `Cat ↪ liftings` is
  proved by explicit construction and **machine-verified** on a spread of categories `C`
  (honest finite-container engine + cross-validated sampling-associativity).
* **Refuted (computed, `|S|=2`):** the "categories over `𝕊` / discrete Conduché fibration /
  copresheaf" classification — nontrivial `𝕊`-holonomy breaks associativity; per-state variation
  and single-state localisation are impossible. The naive `S^S`-graded-category guess is false.
* **Conjectured (open):** completeness — that `C↦𝕊×C` is *onto* the liftings, i.e. State
  liftings ≅ Cat. Evidence: profile-`[(2,0),(0,2)]` count = #monoids-on-2 = 4; all tested
  non-products fail. Not proved exhaustively; a full `δ`-enumeration at higher profiles is
  combinatorially out of reach with the honest engine and was not attempted.
* **Cited (proved/published):** polynomial comonads ≅ small categories (Ahman–Chapman–Uustalu);
  `Cont`-fibre `=(Set^{S₀})^op` (von Glehn TAC 33); `T^Σ_M=M◁−` (`sigma-monad-is-triangle-monoid`).
* **Not settled:** the *general-`M`* statement (the "π₀ of the position-threading" slogan) is a
  conjecture read off from the two solved cases (Reader, State); the precise "threading action"
  for general `M` (positions vary with shape) is not defined here. The completeness proof — the
  right home is the substitution/plethystic monoidal structure `⊛` whose comonoids are the
  liftings, showing its comonoids are holonomy-free — is the next PROVE/expository target.

---

## 8. One line

State's `S^S`-threading is **holonomy-free**: nontrivial store-grading breaks associativity and
a connected transition structure forces one global fibre, so the proof-relevant monad liftings of
State are — conjecturally — just **small categories** (`C↦𝕊×C`), the `π_0=1` collapse of Reader's
`E`-indexed families; the anticipated *finer* graded object is in truth the *coarser* `Cat`.
