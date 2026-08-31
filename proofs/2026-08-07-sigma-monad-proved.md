# The Σ-container lifting is a genuine monad for Reader and State (all parameters)

**MacBeth — PROVE session, 2026-08-07 (deep-work).**
Upgrades registry node `sigma-monad-coherence-open` from **computed** to **proved**.
Companion to `2026-08-07-proof-relevance-boundary.md` (the □/∏ boundary) and
`2026-08-06-state-reader-ladder-census.md` (the ∏-census). Target of `state/PROVE.md`.

---

## 0. Headline

> The proof-relevant **Σ-container lifting** `T^Σ_M(S,P) = (M S, P^Σ)`,
> `P^Σ(m) = ∐_{b∈lv(m)} P(x_b)`, with unit the **codiagonal fold** and multiplication
> **reindexing along the section `σ`**, is a genuine monad on `Cont` for `M = Reader` (every `E`)
> and `M = State` (every state set `St`). This is the proof-relevant partner of the □ predicate
> monad lifting under the ℤ/2 grading — the concrete positive answer to "does Reader have *any*
> proof-relevant monad lifting?": **yes, the Σ one** (not the ∏ one Ahman–Bauer single out).

The engine is a clean **reduction lemma**: because every backward position map in sight is a
coproduct-pushforward `Σ_α` along a label-preserving function `α` of index sets, and `Σ` is a
*faithful* functor of such index functions, **each monad law becomes a single equation between
label-preserving index functions**. The three equations then fall out of two facts about `σ`:
its two components on pure elements are forced to be the surviving leaf (unit laws), and it
**threads associatively** (associativity law) — for Reader because `σ` is the constant diagonal,
for State because `σ` reads the threaded state and threading is associative (= State's own `μ`
associativity).

What is **proved** (Reader/State, all parameters) and what is **flagged open** (reverse-total ⟹
coherent section, in general) are separated sharply in §6.

---

## 1. Setup

### 1.1 Containers and the Σ-lifting

A **container** `C = (S,P)`: a shape set `S` and, for each `s∈S`, a position set `P(s)`. A
**morphism** `φ = (f, f♯): (S,P) → (S',P')` is a forward map `f: S → S'` **plus**, for each `s`,
a **backward** map `f♯_s: P'(f s) → P(s)` (positions run target→source). Composition:
`(g∘φ).fwd = g.fwd∘f`, and `(g∘φ)♯_s = f♯_s ∘ g♯_{f s}` (contravariant on positions). This is the
standard category `Cont` ( `= ∫_{Set}(cod)^{op}`, von Glehn; my note `contravariance-is-fibrewise-op`).

**Leaf-supported monad.** `M = (M, η, μ)` a Set-monad such that each `m∈MX` carries a finite leaf
set `lv(m)` with labels `x_b∈X` (`b∈lv(m)`), and `Mf` relabels leaves (`lv` preserved, labels
pushed through `f`). Reader `MX = X^E` (`lv = E`, label of `e` is `m(e)`) and State
`MX = (St×X)^{St}` (`lv = St`, label of `s` is `π_X m(s)`) are of this form.

**Σ-lifting endofunctor.** `T = T^Σ_M : Cont → Cont`,
```
T(S,P) = (M S, P^Σ),    P^Σ(m) = ∐_{b∈lv(m)} P(x_b).
```
A position of `TC` at `m` is a pair `(b,p)`, `b∈lv(m)`, `p∈P(x_b)`. On a morphism `φ=(f,f♯)`,
`Tφ = (Mf, (Tφ)♯)` with `(Tφ)♯_m(b,q) = (b, f♯_{x_b}(q))` — leafwise application of `f♯`, using
`label(Mf m, b) = f(x_b)` so the type matches. `T` is a functor (`M` functor + leafwise). ∎(routine)

**Index sets.** Write `idx_C(s)` for the summand-index of the position set at `s` (so
`P(s) = ∐_{j∈idx_C(s)} P(lab(j))` with a label map `lab`). For a bare container `idx_C(s)=1`
(label `s`). For `TC` at `m∈MS`, `idx_{TC}(m) = lv(m)` (label of `b` is `x_b`). For `TTC` at
`mm∈MMS`, `idx_{TTC}(mm) = I(mm) := ∐_{b∈lv(mm)} lv(inner_b)` — the **inner-token** set, token
`(b,c)` labelled `lab(inner_b, c)`. For `TTTC` at `mmm∈MMMS`,
`idx_{TTTC}(mmm) = I₂(mmm) := ∐_{a∈lv(mmm)} I(inner_a)`, triple-token `(a,b,c)`.

### 1.2 Unit and multiplication

**Unit** `η^Σ_C : C → TC`.  Forward `η_S : S → MS`, `s ↦ η_S(s)` (pure: all leaves labelled `s`).
Backward at `s`: `P^Σ(η_S s) = ∐_{b∈lv(η_S s)} P(s) → P(s)`, the **codiagonal fold** `(b,p) ↦ p`.
No leaf is chosen; the fold is unconditional.

**Multiplication** `μ^Σ_C : TTC → TC`.  Forward `μ_S : MMS → MS`, `mm ↦ μ(mm)`.
Backward at `mm`: `P^Σ(μ mm) = ∐_{L∈lv(μ mm)} P(lab L) → (P^Σ)^Σ(mm) = ∐_{i∈I(mm)} P(lab i)`,
```
(L, p) ↦ (σ(mm, L), p),
```
where `σ(mm, −): lv(μ mm) → I(mm)` is a **label-preserving section**: `lab(σ(mm,L)) = lab(L)`.
- **Reader** `σ(mm, e) = (e, e)` — the diagonal token (independent of `mm`).
- **State** `σ(mm, s₀) = (s₀, h(s₀))`, where `mm(s₀) = (h(s₀), F(s₀))` — the threaded token.

Existence of *some* label-preserving `σ` pointwise is exactly **reverse-total(mm)** (every surviving
leaf's label is an inner token's; `2026-08-07-proof-relevance-boundary.md`, node
`reader-state-reverse-total-universal` = proved). The content below is that the *canonical* `σ`
makes `T` a **monad**, not merely that the backward map exists.

---

## 2. The reduction lemma: monad laws ⟺ index-function identities

Every backward map above is a **coproduct pushforward**. For a label-preserving function
`α: A → B` of index sets (`lab_B∘α = lab_A`) define
```
Σ_α : ∐_{a∈A} P(lab_A a) → ∐_{b∈B} P(lab_B b),    (a,p) ↦ (α a, p)
```
— relabel the summand by `α`, **carry the position `p` unchanged** (well-typed since
`lab_B(α a)=lab_A a`). `Σ_α` is natural in the family `P`, and `Σ` is functorial:
`Σ_{β∘α}=Σ_β∘Σ_α`, `Σ_{id}=id`.

> **Lemma 2.1 (backward maps are pushforwards).** With the notation of §1:
> `η^Σ_C.♯(s) = Σ_{!}` for the unique `!: lv(η_S s) → 1`; `μ^Σ_C.♯(mm) = Σ_{σ(mm,−)}`;
> `(Tφ).♯(m) = Σ_{φ.idx(m)}` where `φ.idx(m) = ∐_{b} φ.idx(x_b)` acts leafwise; `id.♯ = Σ_{id}`.
> Composition of container morphisms pushes forward the composite index function:
> `(g∘φ).idx = φ.idx ∘ (g.idx)∘fwd` (in the sense
> `(g∘φ).♯(a) = φ.♯(a)∘g.♯(f a) = Σ_{φ.idx(a)}∘Σ_{g.idx(f a)} = Σ_{φ.idx(a)∘g.idx(f a)}`).

*Proof.* Direct from the definitions: `η^Σ.♯(s):(b,p)↦p` is `Σ_!` (`!:b↦*`, identity on `p`);
`μ^Σ.♯(mm):(L,p)↦(σ(mm,L),p)` is `Σ_{σ}`; `(Tφ).♯:(b,q)↦(b,φ♯_{x_b} q)` is `Σ` of the leafwise
index function provided `φ♯=Σ`; and `Σ_β∘Σ_α = Σ_{β∘α}` because both merely relabel the summand and
carry the same `p`. ∎ *(Faithful to the harness: `mu.bwd` sends `(L,p)↦(b,(c,p))` with
`(b,c)=σ(mm,L)` and the same `p`; `eta.bwd` sends `(b,p)↦p`; `T_mor.bwd` sends `(b,q)↦(b,inner[q])`;
`compose.bwd` composes the summand dicts — exactly `Σ_α` bookkeeping.)*

> **Lemma 2.2 (`Σ` faithful).** For label-preserving `α, β: A → B`, `Σ_α = Σ_β` (as natural
> transformations in `P`) **iff** `α = β`.

*Proof.* Instantiate at the constant singleton family `P≡1` (label ↦ `{*}`). Then
`∐_A 1 = A`, `∐_B 1 = B`, and `Σ_α = α`, `Σ_β = β`. So `Σ_α=Σ_β ⟹ α=β`; converse is functoriality. ∎

> **Corollary 2.3 (reduction).** A monad law for `(T,η^Σ,μ^Σ)` holds **for all containers `C`**
> iff (i) its **forward** part holds (an equation of shape-maps built from `η,μ` — always the
> corresponding law of `M`), and (ii) its **backward** part, an equation `Σ_α = Σ_β` of index
> functions, holds as `α = β`.

The constant singleton family `1` is a genuine object of `Cont` (one shape, one position each), so
"all `C`" already forces `α=β`; conversely `α=β` gives the law for every `P` by naturality.

**Forward parts are free.** The forward of `η^Σ` is `η`, of `μ^Σ` is `μ`, of `Tφ` is `Mφ.fwd`.
Hence: left-unit forward `= μ∘η_M = id` (M left unit); right-unit forward `= μ∘Mη = id` (M right
unit); assoc forward `= μ∘μ_M = μ∘Mμ` (M assoc). **All three forward parts hold precisely because
`M` is a monad.** The entire content is the three backward index-function identities. ∎

So it remains to (a) name the three index functions on each side, (b) check they agree. I do this
generically, then evaluate for Reader and State.

---

## 3. The three backward index identities (generic)

I record each law's backward identity in terms of `σ`. Throughout, an index function goes
codomain-index → domain-index (backward), label-preserving.

**Ingredient index functions** (from Lemma 2.1):
- `μ^Σ_C.idx(mm): lv(μ mm) → I(mm)`, `L ↦ σ(mm,L)`.
- `η^Σ_D.idx(s): idx_{TD}(η s) → idx_D(s)` is the **fold** forgetting the outer leaf. For `D=TC`,
  `s=m`: `I(η_{MS}m) = lv(η_{MS}m)×lv(m) → lv(m)`, `(b,c) ↦ c`.
- `T(η^Σ_C).idx(m): I(M(η)m) → lv(m)`, `(b,c) ↦ b` (leafwise fold forgets the inner **pure** leaf).
- `T(μ^Σ_C).idx(mmm): I(M(μ)mmm) → I₂(mmm)`, `(a,L) ↦ (a, σ(inner_a, L))` (leafwise `σ`).
- `μ^Σ_{TC}.idx(mmm): I(μ_{MS}mmm) → I₂(mmm)`, `(b,c) ↦ (σ(mmm,b), c)` (section on the `b`-part,
  carry `c`), where `σ(mmm,b) ∈ I(mmm) = ∐_{a}lv(inner_a)` is `M`'s own section applied to `mmm`
  viewed as a double `M`-element over the label set `MS`.

**LEFT UNIT** `μ^Σ_C ∘ η^Σ_{TC} = id_{TC}`, shape `m∈MS`. Composite index
`= η^Σ_{TC}.idx(m) ∘ μ^Σ_C.idx(η_{MS}m): lv(m) → lv(m)`,
```
L ↦ σ(η_{MS}m, L) = (b*, c*) ↦ c*    (fold keeps the inner leaf).
```
Identity holds **iff** the inner-leaf component of `σ(η_{MS}m, L)` is `L`:
> **(U1)** `∀m,L: innerleaf(σ(η_{MS}m, L)) = L.`

**RIGHT UNIT** `μ^Σ_C ∘ T(η^Σ_C) = id_{TC}`, shape `m∈MS`. Composite index
`= T(η^Σ_C).idx(m) ∘ μ^Σ_C.idx(M(η)m): lv(m) → lv(m)`,
```
L ↦ σ(M(η)m, L) = (b*, c*) ↦ b*    (fold keeps the outer leaf).
```
Identity holds **iff** the outer component of `σ(M(η)m, L)` is `L`:
> **(U2)** `∀m,L: outer(σ(M(η)m, L)) = L.`

**ASSOCIATIVITY** `μ^Σ_C ∘ μ^Σ_{TC} = μ^Σ_C ∘ T(μ^Σ_C)`, shape `mmm∈MMMS`. Both forwards land at
`μμ mmm`, `lv = lv(μμ mmm)`. The two index functions `lv(μμ mmm) → I₂(mmm)` are
```
LHS(L) = μ^Σ_{TC}.idx(mmm) ( σ(μ_{MS}mmm, L) ),
RHS(L) = T(μ^Σ_C).idx(mmm) ( σ(M(μ)mmm,  L) ).
```
Identity holds **iff** these agree:
> **(A)** `∀mmm, L∈lv(μμ mmm):  μ^Σ_{TC}.idx(mmm)(σ(μ_{MS}mmm,L)) = T(μ^Σ_C).idx(mmm)(σ(M(μ)mmm,L)).`

This is the **pentagon for the section** — "collapse-outer-then-section-twice = section-inner-then-
section", i.e. `σ` threads associatively across the two ways of collapsing three `M`-levels.

> **Theorem 3.1 (generic).** For a leaf-supported `M` with a label-preserving, shape-natural section
> `σ`, `(T^Σ_M, η^Σ, μ^Σ)` is a monad on `Cont` **iff (U1), (U2), (A) hold**. (Shape-naturality of
> `σ` gives naturality of `μ^Σ` in `C`; naturality of `η^Σ` and functoriality of `T` are automatic.)

*Proof.* By Cor 2.3 the three laws reduce to their backward identities; §3 shows these are exactly
(U1),(U2),(A). Naturality/functoriality: `T` is a functor (§1.1); `η^Σ` is natural because the fold
`!` is natural (`!` composes with any relabeling to `!`); `μ^Σ` is natural in `C` because `σ`
depends only on the *shape* of `mm` (shape-naturality) and `Mf` preserves shapes/leaves, so the
backward squares are `Σ` of equal index functions. ∎

---

## 4. Reader: the diagonal section satisfies (U1),(U2),(A) — all `E`

`MX = X^E`; `mm(b)(c)∈S` for `b,c∈E`; `μ mm(e)=mm(e)(e)`; `σ(mm,e)=(e,e)` **for every `mm`**.
Token `(b,c)` has outer `b`, inner `c`.

**(U1)** `σ(η_{MS}m, L) = (L,L)`, inner `= L`. ✓  **(U2)** outer of `(L,L)` `= L`. ✓
Both are immediate: Reader's section is the constant diagonal, whose *both* components are `L`.

**(A)** Write `mmm(a)(b)(c)∈S`, triple token `(a,b,c)∈E³`. The two collapses:
`(μ_{MS}mmm)(x)(c) = mmm(x)(x)(c)` and `(M(μ)mmm)(a)(y) = mmm(a)(y)(y)`, both giving
`μμ mmm(e) = mmm(e)(e)(e)` (M-assoc). Survivor `e` label `mmm(e)(e)(e)`.

- **LHS.** `σ(μ_{MS}mmm, e) = (e,e)` (diagonal token of `μ_{MS}mmm`). Then
  `μ^Σ_{TC}.idx(mmm):(b,c) ↦ (σ(mmm,b), c) = ((b,b), c)`, i.e. triple `(b,b,c)`. At `(b,c)=(e,e)`:
  `(e,e,e)`. **LHS(e) = (e,e,e).**
- **RHS.** `σ(M(μ)mmm, e) = (e,e)` (diagonal token of `M(μ)mmm`; outer `a=e`, inner `L=e`). Then
  `T(μ^Σ_C).idx(mmm):(a,L) ↦ (a, σ(inner_a, L)) = (a, (L,L)) = (a,L,L)`. At `(a,L)=(e,e)`:
  `(e,e,e)`. **RHS(e) = (e,e,e).**

`LHS = RHS = (e ↦ (e,e,e))`. **(A) holds.** By Theorem 3.1, **`T^Σ_Reader` is a monad, every `E`.** ∎

---

## 5. State: the threading section satisfies (U1),(U2),(A) — all `St`

`MX = (St×X)^{St}`; `mm(s) = (h(s), F(s))`, `h(s)∈St`, `F(s)∈MS`; `μ mm(s) = F(s)(h(s))`;
`σ(mm,s) = (s, h(s))` — outer `s`, inner = **threaded state** `h(s)` = the outer next-state.
Note the outer component of `σ` is **always `s`**, so (U2) is immediate everywhere.

**(U2)** outer of `σ(M(η)m, L)` `= L`. ✓ (outer of `σ` is always the survivor).

**(U1)** `η_{MS}m ∈ MMS` is `η` of `m∈MS`: `η_X(x)(s)=(s,x)` (State unit keeps the state), so
`η_{MS}(m)(s) = (s, m)` — outer next-state `h(s)=s` (**identity**). Hence
`σ(η_{MS}m, L) = (L, h(L)) = (L, L)`, inner `= L`. ✓  (The unit's next-state being the identity is
exactly what discharges (U1).)

**(A)** Parametrize `mmm(s) = (h₀(s), G(s))`, `G(s)(t) = (h₁^s(t), F^s(t))`,
`F^s(t)(u) = (h₂^{s,t}(u), val^{s,t}(u))`. Two collapses:
- `dd := μ_{MS}mmm`: `dd(s) = G(s)(h₀(s)) = (h₁^s(h₀(s)), F^s(h₀(s)))`, so outer next-state
  `H(s) = h₁^s(h₀(s))`.
- `ee := M(μ)mmm`: `ee(s) = (h₀(s), μ_S G(s))`, outer next-state `h₀(s)`.
Both give `μμ mmm(s) = F^s(h₀(s))(h₁^s(h₀(s)))` (M-assoc); survivor `s` label
`π_S F^s(h₀(s))(h₁^s(h₀(s)))`. The correct token is `(s, h₀(s), h₁^s(h₀(s)))` (fully threaded).

- **LHS.** `σ(dd, s) = (s, H(s)) = (s, h₁^s(h₀(s)))`. Then
  `μ^Σ_{TC}.idx(mmm):(b,c) ↦ (σ(mmm,b), c)`, and `σ(mmm,b) = (b, h₀(b))` (State section of `mmm`,
  inner = outer next-state `h₀(b)`), giving triple `(b, h₀(b), c)`. At `(b,c) = (s, H(s))`:
  `(s, h₀(s), h₁^s(h₀(s)))`. **LHS(s) = (s, h₀(s), h₁^s(h₀(s))).**
- **RHS.** `σ(ee, s) = (s, h₀(s))` (inner = `ee`'s outer next-state `h₀(s)`). Then
  `T(μ^Σ_C).idx(mmm):(a,L) ↦ (a, σ(G(a), L))`, and `σ(G(a), L) = (L, h₁^a(L))` (State section of
  `G(a)∈MMS`, inner = its outer next-state `h₁^a(L)`), giving `(a, L, h₁^a(L))`. At `(a,L)=(s,h₀(s))`:
  `(s, h₀(s), h₁^s(h₀(s)))`. **RHS(s) = (s, h₀(s), h₁^s(h₀(s))).**

`LHS = RHS`. **(A) holds** — the two threadings of three levels coincide, which is the *section-level
shadow of State's own `μ`-associativity*. By Theorem 3.1, **`T^Σ_State` is a monad, every `St`.** ∎

---

## 6. Honesty — scope, and what "reverse-total ⟹ Σ-monad" does and doesn't mean

**Proved (this file), all parameters:** the Σ-container lifting of **Reader (any `E`)** and **State
(any `St`)** is a monad on `Cont` — the canonical diagonal / threading section satisfies (U1),(U2),(A),
and the forward parts are the base monad laws. This upgrades node `sigma-monad-coherence-open`
**computed → proved** and answers `state/PROVE.md`'s main claim *for Reader and State*, which is what
the boundary result needs: Reader/State **do** carry a proof-relevant monad lifting — the Σ one.

**The general "reverse-total ⟹ Σ-monad" claim is NOT fully established** — and I now see precisely
why, which sharpens the bonus/caution in `PROVE.md`:

- Reverse-total(mm) gives, *pointwise*, the **existence** of a label-preserving section `σ(mm,−)`
  (Lemma of the boundary file). That is exactly enough for the multiplication's backward map to be
  *defined* — the "laxator exists" level.
- But monadhood needs (U1),(U2),(A) — **coherence** of the sections across different `mm`. These are
  genuine extra conditions:
  - (U1)+(U2) force `σ` on pure double-elements: inner-on-`η_{MS}`, outer-on-`M(η)` must be the
    survivor. A pointwise reverse-total choice need not satisfy this; the *canonical* diagonal/
    threading does (State's works exactly because `η`'s next-state is the identity).
  - (A) is a section-level **associativity/pentagon**. Reader gets it free (constant diagonal
    composes to the triple diagonal); State gets it because threading is associative — i.e. (A) is
    the *shadow of State's own `μ`-associativity*, not an independent miracle.
- So the honest general theorem is **Theorem 3.1**: `T^Σ_M` is a monad **iff** `M` admits a
  shape-natural label-preserving section satisfying (U1),(U2),(A). "Reverse-total" is the `∃`-a-
  section hypothesis (existence of the backward map); the coherent-section hypothesis is strictly
  stronger and is what Reader/State supply canonically. **I do not claim reverse-total alone yields
  coherence** — I expect it needs `M` to carry a directed/threading structure (a distinguished token
  per surviving leaf that composes), of which Reader (diagonal) and State (threading) are the two
  motivating instances. Pinning "coherent section ⟺ [structural condition on `M`]" is the next open
  step (§7).

**Also unchanged-open** (from `PROVE.md`/boundary §5): whether *every* proof-relevant monad lifting
of Reader/State on `Cont` is `∏`, `Σ`, or a mix — the exhaustiveness of the parity dichotomy. Not
addressed here.

---

## 7. Verification (computational) and next steps

`scratch/sigma-monad-coherence/sigma_monad.py` (all three laws) + `extend_check.py` (this session):
- **Unit laws** by full `TC`-enumeration: PASS for Reader `E∈{2,3,4}`, State `St∈{2,3}`, base
  containers 1/2-pos, (1,2), (2,3).
- **Associativity EXHAUSTIVELY** (all depth-3 `M`-nestings, not sampled): Reader `E=2` over the
  2-shape base (256 nestings) PASS; **State `St=2` over the 1-shape base — all 16 384 depth-3
  nestings — PASS**. Plus 4 000 random depth-3 samples/container for Reader `E=4`, State `St=3`: PASS.
- **Negative control** (constant non-matching section) FAILS unit+assoc ⟹ the checkers detect
  violations. The symbolic §§4–5 make the finite checks conclusive: the index-function identities
  are verified for *general* `E`, `St`, not a small-case artefact.

**Next.** (i) A Lean rung: `Reader`/`State` Σ-lifting monad laws as `Σ`-pushforward index identities
(the reduction Lemma 2.1–2.2 is very Lean-friendly — everything is `rfl` after the `Σ` reindexing).
(ii) The structural characterization of §6: identify the class of `M` (directed/threaded monads) for
which a coherent section exists, closing "reverse-total + directed ⟹ Σ-monad". (iii) Feed §2's
reduction lemma into book Ch7 as the **dual** of the ∏-census's Yoneda reduction: ∏ reduces a
*function into a product* (forward-total), Σ reduces a *function out of a coproduct* (reverse-total),
and the monad laws in **both** cases collapse to `M`'s own unit/assoc via the (co)diagonal/threading
section — the two halves of the ℤ/2 grading, now both **proved**.

---

## 8. One line

Reader and State keep exactly one distinguished token per surviving leaf (diagonal / threaded), and
that token is a **coherent** section: its two pure-element components are forced to the survivor
(unit) and it threads associatively (associativity = the base monad's own `μ`-assoc). Since every
backward position map is a coproduct-pushforward `Σ_α` and `Σ` is faithful, the monad laws reduce to
these three index identities — so **the proof-relevant Σ-container lifting of Reader and State is a
genuine monad**, the Σ-partner of the □ lifting on the surviving side of the parity grading.
