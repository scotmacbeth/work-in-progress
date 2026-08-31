# The logic of containers: `Cont(cod)` is a fibration, and its quantifiers are the A/E liftings (dualised)

**MacBeth — PROVE session, 2026-08-28 (deep work).**
Answers Neil's UID-132 (2026-08-27): *"turn `cod : Set^→ → Set` into a logic of containers; apply
`Cont` to a fibration to get `Cont(Set^→) → Cont(Set)` as a fibration, where `Cont C = Fam(C^op)`."*

Registry: node `cont-cod-predicate-fibration` (proposed). Builds on the proved
`neil-A-E-predicate-liftings` (UID-94) and the reference fact `contravariance-is-fibrewise-op`
(von Glehn, TAC 33, 2018).

---

## 0. Headline

Write `Cont(C) := Fam(C^op)` (the category of containers with objects in `C`; `Cont(Set)` is the
usual category of containers). Then:

> **(Structural.)** `Fam(−)` preserves fibrations: for any fibration `p : E → B`,
> `Fam(p) : Fam(E) → Fam(B)` is a fibration, with cartesian morphisms characterised componentwise.
> Since `cod : Set^→ → Set` is an **opfibration**, `cod^op` is a **fibration**, and hence
> `Cont(cod) := Fam(cod^op) : Cont(Set^→) → Cont(Set)` is a fibration — in fact a **bifibration**,
> because `cod` is a bifibration (`Set` has pullbacks). Its fibre over a container `(S,{P_s})` is
> `∏_{s∈S}(Set/P_s)^op` = **proof-relevant predicates on positions, fibrewise-dualised**.

> **(Logic — the increment.)** Along the canonical *collapse* morphism `η : (S,{1}) → (S,{P_s})`
> the bifibration carries a two-sided adjoint string
> ```
>        A  ⊣  Δ_c  ⊣  E
> ```
> where `E = η^*` is the **cartesian reindexing** and equals **Exists** `= (Σ_!)^op = ◁`, the middle
> `Δ_c = η_!` is **weakening**, and `A =` **All** `= (Π_!)^op`. These are exactly Neil's proved
> `A`/`E` predicate liftings (UID-94). The fibrewise op is the whole story: it is the literal
> opposite of Set's LCCC string `Σ_! ⊣ !^* ⊣ Π_!` (`∃ ⊣ Δ ⊣ ∀`), so **relative to the common
> weakening `Δ_c`, the container logic's ∃ (left adjoint) is All (built from Set's Π) and its ∀
> (right adjoint) is Exists (built from Set's Σ)**. The op swaps the quantifier *roles* against the
> Set *operations*, and simultaneously swaps `∧↔∨`, `⊤↔⊥`: **the hyperdoctrine of containers is the
> fibrewise opposite of the standard `Set`-family hyperdoctrine.** Beck–Chevalley and Frobenius hold,
> dualised. The propositional (subobject) truncation is a **co-Heyting** (Brouwer/paraconsistent)
> predicate logic.

The orientation's guess *"reindexing = pullback `ρ_s^*`"* is the **trap**: the true cartesian
reindexing of `Cont(cod)` is `(Σ_ρ)^op` (dualised post-composition). `ρ_s^*` reappears only as the
weakening `Δ_c` of the *opfibration*, where the two-sided quantifier string sits.

---

## 1. Preliminaries

**`Fam(C)`** (free coproduct completion). Objects `(I,{X_i}_{i∈I})`, `I∈Set`, `X_i∈C`. A morphism
`(I,{X_i}) → (J,{Y_j})` is a pair `(u : I→J, {f_i : X_i → Y_{u(i)}}_{i∈I})`; composition
`(v,{g_j})∘(u,{f_i}) = (v∘u, {g_{u(i)}∘f_i})`. Freeness: a morphism is *exactly* an indexed family of
`C`-morphisms over a reindexing function; there is no cross-index datum beyond `u`.

**`Cont(C) := Fam(C^op)`.** Objects `(S,{P_s})`. A morphism `(S,{P_s}) → (S',{P'_{s'}})` is
`(u : S→S', {ρ_s : P'_{u(s)} → P_s}_{s∈S})` — the **backward position map** (a `C^op`-morphism
`P_s → P'_{u(s)}` is a `C`-morphism `P'_{u(s)} → P_s`). For `C=Set` these are ordinary containers /
polynomial functors and their morphisms.

**`Fam` on functors.** For `p : E → B`, `Fam(p)(I,{X_i}) = (I,{p X_i})`, `Fam(p)(u,{f_i}) = (u,{p f_i})`.
Note the codomain bookkeeping: `Fam(p^op) : Fam(E^op) → Fam(B^op)`, i.e.
`Fam(cod^op) : Cont(Set^→) → Cont(Set)`. This is `Cont(cod)`.

**`cod : Set^→ → Set`.** `Set^→` is the arrow category: objects `f : A→B`; morphisms `f→f'` are
commuting squares `(a:A→A', b:B→B')` with `f'a = bf`; `cod(f)=B`, `cod(a,b)=b`.
- Fibre over `B` is the slice `Set/B` (vertical morphism = square with `b=id_B` = `Set/B`-morphism).
- **`cod` is an opfibration** (always): the opcartesian lift of `β : B→B''` at `f:A→B` is
  `(id_A, β) : f → β∘f`; opreindexing `Σ_β : Set/B → Set/B''` is post-composition `f ↦ β∘f`.
- **`cod` is a fibration** iff the base has pullbacks; `Set` does, so `cod` is a **bifibration**.
  Reindexing `β^* : Set/B'' → Set/B` is pullback.
- `Set` is an LCCC, so `cod` is a **trifibration**: for `β : X→Y`,
  `Σ_β ⊣ β^* ⊣ Π_β`, with `Σ_β,Π_β : Set/X → Set/Y` and `β^* : Set/Y → Set/X`.

We use one standard duality repeatedly:

> **(Op-duality of (co)cartesianness.)** For any functor `p : E→B`, a morphism `m` of `E` is
> `p`-cartesian iff its reverse `m^op` is `p^op`-cocartesian, and dually. Hence `p^op` is a fibration
> iff `p` is an opfibration; `p^op` is a bifibration iff `p` is. *(The cartesian universal property
> is self-dual under reversing all arrows; see Jacobs, CLTT, §1.)*

---

## 2. Structural core: `Fam` preserves fibrations

The load-bearing fact. We first characterise `Fam(p)`-cartesian morphisms, then read off the lift.

### Lemma 2.1 (componentwise cartesianness)
Let `p : E → B` be any functor. A `Fam(p)`-morphism `(u,{φ_i}) : (I,{X_i}) → (J,{Y_j})` is
`Fam(p)`-cartesian **iff each `φ_i : X_i → Y_{u(i)}` is `p`-cartesian.**

*Proof.*

**(⇐)** Assume each `φ_i` is `p`-cartesian. Let `(w,{g_k}) : (K,{Z_k}) → (J,{Y_j})` be any morphism
of `Fam(E)`, and let `(v,{h_k}) : Fam(p)(K,{Z_k}) → (I,{pX_i})` be a factorisation of
`Fam(p)(w,{g_k})` through `Fam(p)(u,{φ_i}) = (u,{pφ_i})` in `Fam(B)`. Reading the base equation
componentwise: `w = u∘v`, and for each `k`, `p g_k = pφ_{v(k)} ∘ h_k` in `B`.

We must produce a unique `(t,{m_k}) : (K,{Z_k}) → (I,{X_i})` in `Fam(E)` with
`Fam(p)(t,{m_k}) = (v,{h_k})` and `(u,{φ_i})∘(t,{m_k}) = (w,{g_k})`. The first equation forces
`t = v` and `p m_k = h_k`; the second forces `u∘t = w` (automatic) and `φ_{v(k)}∘m_k = g_k`. So for
each `k` we need a unique `m_k : Z_k → X_{v(k)}` with `p m_k = h_k` and `φ_{v(k)}∘m_k = g_k`. The data
`g_k : Z_k → Y_{u(v(k))}` and `h_k : pZ_k → pX_{v(k)}` satisfy `p g_k = pφ_{v(k)}∘h_k`; since
`φ_{v(k)}` is `p`-cartesian, such `m_k` exists and is unique. Assembling `(v,{m_k})` gives the unique
factorisation. (No cross-index datum arises: `t` is forced to `v`, and components are independent by
freeness of the coproduct completion.)

**(⇒)** Assume `(u,{φ_i})` is `Fam(p)`-cartesian; fix `i₀` and show `φ_{i₀}` is `p`-cartesian. Given
`g : Z → Y_{u(i₀)}` in `E` and `h : pZ → pX_{i₀}` in `B` with `pg = pφ_{i₀}∘h`, form singleton
families `K={*}`, `Z_*=Z`; `w(*)=u(i₀)`, `g_*=g`; `v(*)=i₀`, `h_*=h`. Then `w=u∘v` and the base
equation holds, so `Fam(p)`-cartesianness yields a unique `(t,{m_*})` over `(v,{h_*})` with
`(u,{φ})∘(t,{m}) = (w,{g})`. It forces `t=v` (so `t(*)=i₀`), `p m_* = h`, and `φ_{i₀}∘m_* = g`.
Uniqueness of `m_*` is exactly `p`-cartesianness of `φ_{i₀}`. ∎

### Corollary 2.2 (`Fam` preserves fibrations)
If `p : E → B` is a fibration, so is `Fam(p) : Fam(E) → Fam(B)`.

*Proof.* Given a target `(J,{Y_j})` and a base morphism `(u,{ψ_i}) : (I,{b_i}) → (J,{pY_j})` (so
`ψ_i : b_i → pY_{u(i)}`), choose for each `i` the `p`-cartesian lift `χ_i : ψ_i^*(Y_{u(i)}) → Y_{u(i)}`
of `ψ_i`, and set `X_i := ψ_i^*(Y_{u(i)})`. Then `(u,{χ_i}) : (I,{X_i}) → (J,{Y_j})` lies over
`(u,{ψ_i})` and is `Fam(p)`-cartesian by Lemma 2.1. ∎

Dually (Lemma 2.1 has an opcartesian analogue by the same argument), **`Fam` preserves opfibrations
and bifibrations**, and reindexing/opreindexing in `Fam(p)` are computed componentwise from those of
`p`. In categorical language, `Fam` lifts to a 2-functor `Fib(B) → Fib(Fam B)` for each `B`; this is
the clean general statement, of which our theorem is the instance `p = cod^op`, `B = Set^op`.

---

## 3. `Cont(cod)` is a bifibration; its fibres

By §1 op-duality, since `cod` is a bifibration, `cod^op : (Set^→)^op → Set^op` is a bifibration; in
particular a fibration. By Corollary 2.2 (and its bifibration form),

> **Theorem 3.1.** `Cont(cod) = Fam(cod^op) : Cont(Set^→) → Cont(Set)` is a **bifibration**. ∎

*Independent cross-check.* `(Set^→)^op ≅ (Set^op)^→` carries `cod` to `dom`, and `dom` is a fibration
over any base — confirming `cod^op` is a fibration.

**The objects.** An object of `Cont(Set^→)` is `(S,{f_s : A_s → B_s}_s)`. `Cont(cod)` sends it to the
container `(S,{B_s})`. So a "predicate over the container `(S,{B_s})`" equips each shape `s` and each
position `b ∈ B_s` with a **witness set** `f_s^{-1}(b)` — a proof-relevant predicate on positions.

**Fibre over `(S,{P_s})`.** A vertical morphism `(S,{f_s}) → (S,{f'_s})` over `id_{(S,{P_s})}` is
(unwinding `Fam((Set^→)^op)`) a family, for each `s`, of `Set^→`-morphisms `f'_s → f_s` whose
codomain component is `id_{P_s}`, i.e. maps `a : A'_s → A_s` with `f_s∘a = f'_s` — a `Set/P_s`-morphism
`f'_s → f_s`, **backwards**. Hence

> **the fibre of `Cont(cod)` over `(S,{P_s})` is `∏_{s∈S}(Set/P_s)^op`** — the fibrewise opposite of
> the slice, exactly von Glehn's `Cont = ∫_{Set} cod^op` [`contravariance-is-fibrewise-op`].

---

## 4. Reindexing (the dualisation trap)

Let `(u,{ρ_s}) : (S,{P_s}) → (S',{P'_{s'}})` be a container morphism, `ρ_s : P'_{u(s)} → P_s`.
By Lemma 2.1, its cartesian lift is componentwise; each component is the `cod^op`-cartesian lift,
which by §1 op-duality is the `cod`-**co**cartesian lift, i.e. **post-composition** `Σ_{ρ_s}`,
dualised. Concretely the reindexing functor

> `(u,{ρ_s})^* : ∏_{s'}(Set/P'_{s'})^op → ∏_s (Set/P_s)^op`,
> componentwise `(Σ_{ρ_s})^op`, sending a predicate `g : C → P'_{u(s)}` to `ρ_s∘g : C → P_s`.

So the cartesian reindexing of `Cont(cod)` is **`(Σ_ρ)^op`, not `ρ^*`**. The pullback `ρ_s^*` is the
*opfibration* opreindexing (the left adjoint of the above, §5). This is the fibrewise op doing its
work: because container morphisms carry the backward map `ρ_s : P'→P`, the natural (covariant)
operation on predicates is post-composition, and the op makes it the cartesian direction.

---

## 5. The quantifiers are the A/E liftings; the dualisation theorem

Recall Neil's proved liftings (UID-94), for a container `X` (domain of quantification) and predicate
`Y` reindexed by `g : P_X s → S_Y`:
```
Exists X Y (s,g) = Σ_{p:P_X s} P_Y(g p)   (= total space; and Exists = ◁),
All    X Y (s,g) = ∏_{p:P_X s} P_Y(g p).
```
Both quantify a family `{P_Y(g p)}_{p:P_X s}` over the positions `P_X s` — i.e. along the **collapse**
`! : P_X s → 1`. In `Set`, the collapse gives the LCCC string
```
Σ_! ⊣ !^* ⊣ Π_!      ( ∃ ⊣ weakening ⊣ ∀ ),
```
with `Σ_!(f:A→P) = A` (total space), `!^*(Z) = (P×Z → P)` (constant family = weakening),
`Π_!(f:A→P) = ∏_p f^{-1}(p)` (sections). **Verified computationally** in `Set` for collapse,
injective, surjective and bijective maps (§7).

Now lift to `Cont(cod)`. The one **canonical** base morphism between `(S,{1})` and `(S,{P_s})` is the
collapse-unit `η : (S,{1}) → (S,{P_s})` with backward position map `ρ_s = ! : P_s → 1` (the reverse
direction would need a *choice* of point `1 → P_s` and is not canonical). Applying §4 and §1 duality:

- **cartesian reindexing** `η^* = (Σ_!)^op = E`. On objects: `η^*(f_s) = A_s` = total space =
  `Exists`. So **`E = Exists = η^*`, the reindexing itself**, and `E = ◁`.
- **opreindexing (weakening)** `η_! = (!^*)^op =: Δ_c`. On objects: `Δ_c(Z) = (P_s×Z → P_s)` =
  the position-independent predicate — genuine **weakening**.
- The bifibration gives `η_! ⊣ η^*`, i.e. `Δ_c ⊣ E`.

Opping the whole `Set` string (an adjunction `L⊣R` becomes `R^op ⊣ L^op`):
```
        (Π_!)^op   ⊣   (!^*)^op   ⊣   (Σ_!)^op
    =      A        ⊣     Δ_c      ⊣     E
```
where the outer left adjoint `A := (Π_!)^op` computes, on objects, `∏_p f^{-1}(p)` = **All**. Thus:

> **Theorem 5.1 (quantifiers = liftings).** Along the canonical collapse `η`, the bifibration
> `Cont(cod)` carries the adjoint string `A ⊣ Δ_c ⊣ E`, where `E = Exists` is the cartesian
> reindexing (`= ◁`), `A = All`, and `Δ_c` is weakening. These are precisely Neil's proved A/E
> predicate liftings. ∎

> **Theorem 5.2 (the dualisation).** The string is the *fibrewise opposite* of Set's `Σ_! ⊣ !^* ⊣ Π_!`.
> Consequently, **relative to the common weakening `Δ_c`**:
> - the container logic's **existential** (left adjoint of weakening) is `A = All`, built from Set's
>   dependent **product** `Π`;
> - the container logic's **universal** (right adjoint of weakening) is `E = Exists`, built from Set's
>   dependent **sum** `Σ`.
> The fibrewise op swaps the quantifier *roles* against the Set *operations*: container-∃ is Set-∀ and
> container-∀ is Set-∃. Moreover, in each fibre `(Set/P_s)^op`:
> - fibre **product** (= container `∧`) is the **coproduct** in `Set/P_s` = fibrewise disjoint union
>   of witness sets; fibre **coproduct** (`∨`) is the pullback (fibrewise product) of witnesses;
> - **⊤** (fibre terminal) is the *empty*-witness predicate `∅→P_s`; **⊥** (fibre initial) is the
>   full predicate `id : P_s→P_s`.
>
> Hence **the hyperdoctrine of containers is the fibrewise opposite of the standard `Set`-family
> hyperdoctrine**: same base, dualised fibres, with `∃↔∀`, `∧↔∨`, `⊤↔⊥` all exchanged. ∎

This answers Neil's increment (iv): *not* a new logic, but a known one read through von Glehn's op —
and that op is exactly the backward position map. Neil's names *All*/*Exists* track the Set operation
(`Π`/`Σ`); their logical role in the container hyperdoctrine is the reverse.

**Where the "subtractive" flavour lives.** The fibre `(Set/P_s)^op` is the **opposite of a topos** (a
"co-topos"): it is co-cartesian-closed, its internal logic is co-intuitionistic (Brouwerian /
*subtractive*) — `⊤` is the empty-witness predicate, `⊥` is the full predicate, and the natural
connective is *subtraction*, not implication. This dualisation is **genuine at the proof-relevant
level**. It is *not* visible in the crude Boolean truncation `Sub(P_s)=2^{P_s}` (a Boolean algebra is
self-dual), which is one reason the proof-relevant reading is the right home for the phenomenon; the
faithful propositional shadow is the subobject fibration `Sub(Set^→)→Set`, whose fibres are
`(Sub_{Set/P_s})^op`, and whose subtractive structure I state but do not develop here (§8).

---

## 6. Beck–Chevalley and Frobenius (dualised)

Both are properties of the `Set` functors `Σ_f, f^*, Π_f`; each transports through the fibrewise op
(which preserves isos and reverses `2`-cells) and through `Fam` (componentwise). We verified the
`Set` instances computationally (§7).

**Beck–Chevalley.** For a pullback square in `Set`
```
   P --k--> C
   |        |
  h|        |g
   v        v
   A --f--> B
```
the canonical mates are isos: `f^* Σ_g ≅ Σ_h k^*` and `f^* Π_g ≅ Π_h k^*`
(verified, all sample squares incl. non-surjective legs). Applying `(−)^op` fibrewise and `Fam`
componentwise gives:

> **Proposition 6.1.** `Cont(cod)` satisfies Beck–Chevalley for the squares in `Cont(Set)` that are
> componentwise the (op-image of) `Set` pullback squares; the isos for `E` and `A` are the
> fibrewise opposites of the `Set` `Σ`- and `Π`-BC isos above. In particular `Exists` and `All`
> commute with substitution, dualised. ∎

**Frobenius.** In `Set`, for `f : X→Y`, `Σ_f(φ × f^*ψ) ≅ Σ_f(φ) × ψ` (verified). Under the fibrewise
op, `Σ_f ↦ (Σ_f)^op` and fibre product `× ↦` fibre coproduct `∨`, giving:

> **Proposition 6.2 (co-Frobenius) — CORRECTED 2026-08-28.** The container universal
> `E = Exists = (Σ_!)^op` (the **right** adjoint of weakening `Δ_c`) satisfies Frobenius reciprocity
> **with `∧` replaced by the fibrewise coproduct `∨`**: `E(φ ∨ Δ_c ψ) ≅ E(φ) ∨ ψ`, the fibrewise
> opposite of Set's `Σ_!`-Frobenius. ∎
>
> **Correction.** An earlier version of this Proposition attributed the co-Frobenius to `A = (Π_!)^op`.
> That is **wrong**: the op of `Set`'s `Σ_!`-Frobenius is the `E`-co-Frobenius (op of `Σ_!`), and `Π_!`
> has no Frobenius in `Set` to dualise — `A` satisfies Frobenius for *no* fibre connective. This was
> asserted "by duality" and not checked at container level; the direct finite verification is in
> `proofs/2026-08-28-joint-bc-cont-cod.md` (§6) / `scratch/verify_joint_bc.py`
> (`test_position_frobenius`). The pattern — co-Frobenius/Beck–Chevalley on the **right-adjoint (∀)
> side only** — is uniform across the shape and position logics; see the joint-BC proof for the full
> co-hyperdoctrine statement.

The dualisation of `∧→∨` in Frobenius is not a defect: it is the same op that turns `∃/∀` around, and
it is forced — Frobenius pairs a quantifier with the fibre *product* of the ambient logic, and the
container ambient logic's product is Set's coproduct.

---

## 7. Computational verification

Scripts in `.claude/scratch/`:

- `verify_cont_cod.py` — brute-force hom-set cardinalities confirm `Σ_f ⊣ f^* ⊣ Π_f` for
  `f` collapse `{1,2,3}→1`, bijection, surjection `{1,2,3}→{a,b}`, and non-surjective inclusion
  `{1}↪{a,b}` (the non-surjective case exercises the empty-fibre `Π_!·= 1` corner). **All pass.**
- `verify_bc_frob.py` — `Beck–Chevalley` (`Σ` and `Π`) over pullback squares with surjective and
  non-surjective legs, and `Frobenius` for `Σ_f`. **All pass.**
- The op-reversal (`L⊣R ⇒ R^op⊣L^op`) and `Fam`-componentwise transport are formal once the `Set`
  facts hold; no computation is needed for them.

Every abstract step above was checked against a concrete finite instance: e.g. `η^*` on
`f : A→P_s` returns `A` (total space) = `Exists`, and `Δ_c(Z)` returns the constant family — matching
Theorem 5.1 on the nose.

---

## 8. Scope, honesty, and the delta

**What is folklore (assembled here, cited not claimed):** `Fam` preserves fibrations (Hermida PhD
1993; Jacobs CLTT Ch.1); `cod` a bifibration (Streicher fundamental fibration); `Cont = ∫_Set cod^op`
and the fibrewise op (**von Glehn, TAC 33 (2018)** — the ancestor; cited hardest); LCCC quantifiers,
BC, Frobenius (Jacobs). Aberlé 2604.01303 only *gestures* (Def 0.4 remark), with no `Fam`, no
fibration theorem, no quantifier calculus.

**The delta (novel, registrable):**
1. Explicit assembly of `Cont(cod) = Fam(cod^op)` as the **bifibration of proof-relevant predicates
   on positions**, with the full componentwise cartesian/opcartesian characterisation (Lemma 2.1).
2. Identification of the fibred quantifiers with the **proved A/E liftings** (Theorem 5.1), pinning
   `E = Exists = ` cartesian reindexing `= ◁` and `A = All`.
3. The **dualisation theorem** (5.2): the container hyperdoctrine is the fibrewise op of Set's, with
   `∃↔∀`, `∧↔∨`, `⊤↔⊥`; the proof-relevant fibre is a **co-topos** with subtractive internal logic.
   This is the precise answer to Neil's "op of a standard one or genuinely new?" — and it exposes the
   *trap* (reindexing is `(Σ_ρ)^op`, not `ρ^*`).
4. BC (6.1) and **co-Frobenius** (6.2) for `Cont(cod)`.

**Gaps / scope (stated precisely):**
- **Shape-level quantifiers — CLOSED 2026-08-28** in `proofs/2026-08-28-joint-bc-cont-cod.md`. The
  shape quantifiers `∃_j ⊣ j^* ⊣ ∀_j` (`Fam`-Kan `Lan_u/Ran_u`) exist unconditionally; the combined
  (shape × position) Beck–Chevalley/Frobenius is settled **exactly**: it holds on the right-adjoint
  (∀) side (co-Frobenius `∧↦∨`, ∀-BC over the exchange square, same-type shape BC) and **fails** on the
  left-adjoint (∃) side, obstructed uniformly by the co-topos non-distributivity
  (`sum-of-products ≠ product-of-sums`). Net: `Cont(cod)` is a **co-hyperdoctrine**, not a two-sided
  Lawvere one. (This also corrected §6.2, above.)
- **Propositional truncation stated, not fully developed.** `Sub(Set^→)` gives a strict Lawvere
  hyperdoctrine whose fibres are the (co-Heyting) `(Sub_{Set/P_s})^op`; I have identified the
  structure but not written the truncation functor's preservation properties. NB the crude
  position-only truncation `Sub(P_s)=2^{P_s}` is Boolean (self-dual) and does **not** exhibit the
  subtractive flavour — that requires the witness-level `Sub(Set^→)` or the full proof-relevant fibre.
- **BC square class.** Proposition 6.1 identifies BC squares as the op-image of `Set` pullback
  squares; a clean intrinsic characterisation of which `Cont(Set)`-squares these are (in terms of
  container pullbacks) is left open.

None of these gaps affect Theorems 3.1, 5.1, 5.2 or Propositions 6.1–6.2 as stated.

---

## 9. Grant / program placement

This populates the previously-empty **fibrational leg (approach 3)** of the Front D survey: the
"logic of containers" is a bifibration whose quantifiers are the A/E liftings, dualised. It welds
three strands — von Glehn's fibrewise op, Neil's A/E liftings, and the container hyperdoctrine — into
one statement: **`Cont` is the fibrewise-opposite endofunctor on the 2-category of `Set`-family
hyperdoctrines.** The co-topos fibre is a candidate for the grant's "compositional correctness" theme:
container predicate logic is intrinsically *subtractive/co-intuitionistic*, the formal shadow of
positions flowing backward.
