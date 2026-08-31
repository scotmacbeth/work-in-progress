# Does `(−)◁q` keep its LEFT adjoint over `Fam(Vec^op)`?
### The gate is `|T|=1`, not summability — and the invariant is CONNECTEDNESS OF THE UNIT

**MacBeth — 2026-08-30 (PROVE session, second of the day).**
Brief: `/home/agent/state/PROVE.md`. Predecessor: `proofs/2026-08-30-pra-vs-probe-method.md`
(the `Set` case, `proved`). Registry node target: `left-adjoint-over-vec`.
Companion code: `scratch/left-adjoint-vec/verify.py` (all green, output in §7).

---

## EXECUTIVE SUMMARY

**Three verdicts, one of them against the brief's own prediction.**

**(1) The predicted answer is REFUTED. It is not summability.** Over the linear base the left
adjoint to `L_q := (−)◁q` exists **iff `|T| = 1`** — iff `q` is a monomial. The obstruction bites
already at `dim P_s = 1` with `|T| = 2` (§3, the brief's cheapest falsifier), so the finite/infinite
character of `T` is *irrelevant*. **There is no fourth occurrence of the summability gate.**

**(2) The load-bearing hypothesis in the `Set` proof was misidentified — by me, in the
predecessor, and by this brief.** The brief's ★ says step `(†)` is "distributivity of `Set`, used
exactly once". That is true of `(†)` *as written*, but `(†)` is not what the adjunction needs. The
adjunction needs only

> **`C(I,−) : C → Set` preserves small coproducts** — i.e. **the monoidal unit `I` is CONNECTED**,

and given that, `F_q = Fam(⟦q⟧^op) ⊣ (−)◁q` for **every** `q`, over **any** closed symmetric
monoidal cocomplete `C`, with a four-line proof that never mentions distributivity and never
touches the presentation of `◁` (**Theorem 1**, §4). Distributivity of `Set` is used in
*constructing* `◁` over `Set`, not in the adjunction.

Unit-connectedness is exactly the **T1 flagship condition** (`fullness-unit-connectedness`,
`proved` 2026-08-25: `⟦−⟧` full and faithful ⟺ `I` connected), and the comparison map is literally
T1's `γ : ∐^{Set}_d C(I,X_d) → C(I,∐^C_d X_d)`. So:

> **T1 (fullness of `⟦−⟧`) and the existence of the `◁`-coclosure are the same lemma applied
> twice.** One condition, two theorems. `Vec` fails both for the same reason: `∐ ⊊ ⊕`.

**(3) p.r.a. and left-adjointness COME APART off `Set` — the brief's clause (C) fires.** Over
`Fam(Vec^op)` the terminal object is `1 = ⟨0⟩` and

    1 ◁ q  =  (T, 0)  ≇  ⟨0⟩ = 1        whenever |T| ≥ 2,

so Weber's slice does **not** collapse. And it does not need to: `Fam/(T,0) ≅ ∏_{t∈T}Fam(C^op)`,
`(L_q)_1(p) = (p⊗Q_t)_{t∈T}`, whose left adjoint is `(r_t)_t ↦ ∐_t F_{Q_t}(r_t)` — so

> **`L_q` is a parametric right adjoint for every `q` over `Vec` too, while it has an honest left
> adjoint only for `|T|=1`.** The predecessor's identification "p.r.a. ⟺ left adjoint" was
> **base-specific**, an artefact of `∅` being initial-but-not-terminal in `Set`.

**The anti-diagonal (the actual crown).** Put the left-adjoint verdict beside the right-adjoint
(closure) verdicts already `proved`:

| | left adjoint to `L_q` exists | right adjoint (`◁`-closure) exists |
|---|---|---|
| `Fam(Set^op)` | **always** (Thm 1; = Niu–Spivak Prop 6.57) | iff `\|T\|=1` (Workers Thm 2) |
| `Fam(Vec_fd^op)` | iff **`\|T\|=1`** (Thm 2, new) | iff `#{t : Q_t≠0}<∞` (T4 Thm 3.1) |

The two conditions **swap sides**. And inside the `(V) ⊊ (C) ⊊ (F)` chain of
`fibredness-vs-left-closure` (over `Vec_fd`: vertical ⊊ closed ⊊ fibred), the new condition lands
exactly on the *bottom* rung:

> **`L_q` has a left adjoint ⟺ `L_q` is vertical (V) ⟺ `|T|=1`, over `Vec_fd`.**
> Over `Set` the same condition `(V)=(C)=(F)=|T|=1` sits at the *bottom* and left-adjointness is
> unconditional at the top. The chain is inverted end to end by passing `Set → Vec`.

---

## 1. Conventions, and the one standing caveat

`C` is closed symmetric monoidal and cocomplete; `I` its unit, `[−,−]` its internal hom,
`0_C` its initial object. `Fam(C^op)` has objects `p=(S,P)` (`S` a small set, `P_s ∈ C`) and

> `Fam((A,X),(B,Y)) = ∏_{a∈A} ∐_{b∈B} C(Y_b, X_a)`.                                    (H)

Forward on shapes, **backward** on positions (`contravariance-is-the-fibrewise-op`). Generators
`⟨Z⟩ := ({∗},Z)`; every object is `∐_{s∈S}⟨P_s⟩`. The **extension** is
`⟦S,P⟧X = ∐_{s∈S}[P_s,X]`; over `Set` this is `Σ_s X^{P_s}`. Substitution `◁` is any operation
with `⟦p◁q⟧ = ⟦p⟧∘⟦q⟧` (DJN `2305.05655`); Dirichlet/Day tensor `p⊗q = (S×T, P_s⊗Q_t)`.
`⟦q⟧Z = ∐_t[Q_t,Z]`.

**Definition 1.1 (connected unit).** `I` is **connected** if `C(I,−):C→Set` preserves small
coproducts, i.e. the canonical comparison

> `γ_{(X_d)} : ∐^{Set}_{d∈D} C(I,X_d) ⟶ C(I, ∐^C_{d∈D}X_d)`                            (γ)

is a bijection for every small family. `Set`: `I=1`, `C(1,−)=Id`, connected ✓.
`Vec`: `I=k`, `C(k,V)=V`, and `γ : ⊔_d V_d → ⊕_d V_d` is neither injective (every summand
contains `0`) nor surjective (support ≥ 2 is missed) — **not connected** ✗. *Any base with a zero
object has a disconnected unit*, since the zero map lies in every summand.

**⚠ STANDING CAVEAT (carried from the brief, and it is load-bearing in §5 only).**
Over `Vec`, `⟦−⟧` is **not faithful** — T1's second honest correction: distinct shape maps with
zero positions induce the same natural transformation. Consequently `⟦p◁q⟧=⟦p⟧⟦q⟧` does **not**
pin down `p◁q` as an object: `(T,0)` and `({∗},0)` present the same (constant `0`) functor. I
therefore fix, as a **definition** and not a deduction, the Day/T4 presentation on the collapse
locus:

> **(D)** `p ◁ q := p ⊗ q = (S×T, P_s⊗Q_t)` wherever `⟦p⊗q⟧ = ⟦p⟧⟦q⟧`.

This is T4-left Prop 2.1's formula and the one under which all of T2/T4/`fibredness-vs-left-closure`
are stated, so it is the consistent convention. §5.2 gives a **second, zero-object-free** proof of
Theorem 2 that does not depend on (D) at zero positions.

**Lemma 1.2 (isos in a free coproduct completion).** `(S,P) ≅ (S',P')` in `Fam(D)` iff there is a
bijection `β:S→S'` with `P_s ≅ P'_{βs}` in `D`.
*Proof.* If `(f,φ)` and `(g,ψ)` are mutually inverse then on shapes `gf=id`, `fg=id`, so `f` is a
bijection with `g=f^{-1}`; the position legs of the two composites read
`φ_s∘ψ_{fs}=id_{P_s}` and `ψ_{s'}∘φ_{gs'}=id_{P'_{s'}}`, so `φ_s : P'_{fs}→P_s` is an iso.
Converse clear. ∎ *(grade: `proved`)*

**Lemma 1.3 (terminal object).** `1 := ⟨0_C⟩` is terminal in `Fam(C^op)`.
*Proof.* By (H), `Fam((R,U),({∗},0_C)) = ∏_ρ C(0_C,U_ρ) = ∏_ρ 1 = 1`. ∎
Over `Set` this is `y^0=({∗},∅)`; over `Vec` it is `({∗},0)`. *(grade: `proved`)*

---

## 2. (A) The comparison map, in house style: one functional, probes varying

`L_q` preserves coproducts in `p` (`⟦∐_ip_i⟧⟦q⟧ = ∐_i⟦p_i⟧⟦q⟧`), and `Fam(⟨Z⟩,−)` preserves
coproducts (a map out of a generator lands in one summand, by (H)). Hence `L_q` has a left adjoint
iff for every `Z∈C` the functor

> **`Φ^Z_q : C^op → Set,   Φ^Z_q(B) := Fam( ⟨Z⟩, ⟨B⟩◁q )`**                            (Φ)

is **representable**, say `Φ^Z_q ≅ C(−,N_Z)`; and then `F_q(R,U) = (R, N_{U_ρ})`.

*This is the house form: one functional `Φ_q`, the probe `Z` varying.* Writing `⟨B⟩◁q = (D_B,N)`,
(H) gives `Φ^Z_q(B) = ∐_{d∈D_B}C(N_{B,d},Z)`, and the candidate representing object is always
`⟦q⟧Z`. So **the comparison map that `(†)` would invert is**

> **`κ_{B,Z} : ∐_{d∈D_B} C(N_{B,d}, Z) ⟶ C(B, ⟦q⟧Z)`**                                 (κ)

— *"is the substitution's decoration set `D_B` big enough to name every map `B → ⟦q⟧Z`?"*

- **Over `Set`**: `D_B = T^B` and `N_{B,c}=Σ_{a∈B}Q_{c(a)}`, so
  `κ : ⊔_{c:B→T}∏_{a∈B}Set(Q_{ca},Z) → Set(B, ⊔_t Set(Q_t,Z))` — a bijection; this **is** `(†)`.
- **On the collapse locus** (`◁=⊗`): `D_B = T`, `N_{B,t}=B⊗Q_t`, so
  `κ : ⊔_t C(B,[Q_t,Z]) → C(B, ⊕_t[Q_t,Z])` — *"a map into a direct sum lies in one summand"*,
  which is `∐ ⊊ ⊕` verbatim, and fails for `|T|≥2` at every `B ≠ 0_C`.

**The slogan.** *Over an extensive base the decoration set `T^{P_s}` names all of them; the linear
collapse shrinks the decoration set to `T`, and it can no longer name a map whose support moves.*

---

## 3. The brief's cheapest falsifier — RUN FIRST, and it fires against the prediction

`C=Vec_fd`, `T=ℕ`, all `Q_t=k`, `Z=k`, `k=F_2`, `B=k^n`. Both sides of `κ`:

| `\|T\|` | `dim B` | `\|LHS\|=∐_t C(B,[Q_t,Z])` | `\|RHS\|=C(B,⊕_t[Q_t,Z])` | `\|im κ\|` | κ injective? | κ surjective? |
|---|---|---|---|---|---|---|
| 1 | 1 | 2 | 2 | 2 | ✓ | ✓ |
| 1 | 2 | 4 | 4 | 4 | ✓ | ✓ |
| **2** | **1** | **4** | **4** | **3** | **✗** | **✗** |
| 2 | 2 | 8 | 16 | 7 | ✗ | ✗ |
| 3 | 1 | 6 | 8 | 4 | ✗ | ✗ |
| 5 | 3 | 40 | 32768 | 36 | ✗ | ✗ |

**Recorded verdict, as the brief demands.** The failure appears at **`dim P_s = 1`** as soon as
`|T| ≥ 2`, with `T` finite. `∐_{t∈ℕ}` leaving `Vec_fd` plays **no role**. Note the `|T|=2, dim B=1`
row: the two sides have the *same cardinality* (4 = 4) yet `κ` is not a bijection — it double-counts
the zero map and misses `e_0+e_1`. **A cardinality-only check would have missed this**; the
canonical map had to be examined. *(grade: `computed`; the general statement is §5.)*

> **So: the summability prediction is WRONG, and (B) must be characterised from scratch. It is.**

---

## 4. Theorem 1 — the `Set` proof, correctly generalised: connected unit, no distributivity

**Theorem 1.** Let `C` be closed symmetric monoidal with small coproducts and **connected unit**
`I`. Let `q=(T,Q) ∈ Fam(C^op)` and suppose `p◁q` exists for every `p` (any object presenting
`⟦p⟧∘⟦q⟧`). Then

> `F_q ⊣ (−)◁q`,   `F_q(R,U) := (R, ρ ↦ ⟦q⟧(U_ρ))`,  i.e.  `F_q = Fam(⟦q⟧^op)`,

with no condition whatsoever on `q`.

*Proof.* Write `p◁q = (D,N)`, so `∐_{d∈D}[N_d,X] ≅ ⟦p⟧⟦q⟧X = ∐_{s∈S}[P_s,⟦q⟧X]` naturally in `X`.
Fix `r=(R,U)`. Using (H), then `C(N,U)≅C(I,[N,U])` (closedness), then `γ` twice:

```
Fam(r, p◁q) = ∏_ρ ∐_{d∈D} C(N_d, U_ρ)
            = ∏_ρ ∐_{d∈D} C(I, [N_d, U_ρ])
            = ∏_ρ C(I, ∐_{d∈D}[N_d, U_ρ])            γ⁻¹,  I connected
            = ∏_ρ C(I, ⟦p⟧(⟦q⟧U_ρ))                  the presenting iso at X = U_ρ
            = ∏_ρ C(I, ∐_{s∈S}[P_s, ⟦q⟧U_ρ])
            = ∏_ρ ∐_{s∈S} C(I, [P_s, ⟦q⟧U_ρ])        γ,  I connected
            = ∏_ρ ∐_{s∈S} C(P_s, ⟦q⟧U_ρ)
            = Fam( (R, ρ↦⟦q⟧U_ρ), p )  =  Fam(F_q r, p).                 ∎
```

Every step is a natural isomorphism (`γ` is the canonical comparison, natural in the family and in
`I`), so the composite is natural in `r` and in `p`. *(grade: `proved`)*

**Four remarks, and they are the point of this session.**

1. **Distributivity is gone.** The proof uses `γ` twice and nothing else. Over `Set`, `γ` is the
   identity (`Set(1,−)=Id`), so the `Set` theorem is the degenerate case. **The `(†)` of the
   predecessor is not the hypothesis; it is an artefact of the explicit `Set` formula for `◁`.**
   Distributivity of `Set` is what makes `Σ_s T^{P_s}` the correct shape set of `p◁q` — it is used
   in *constructing* `◁`, not in the adjunction.
2. **Presentation-independent.** Theorem 1 never chooses a presentation of `p◁q`; it uses only that
   *some* family presents `⟦p⟧⟦q⟧`. So the standing caveat (D) does **not** infect it.
3. **T1 is the same lemma.** `γ` is verbatim T1's comparison map
   (`fullness-unit-connectedness`, `proved`). Hence: **`⟦−⟧` full and faithful ⟺ `I` connected ⟹
   `(−)◁q` has a left adjoint for every `q`.** Two theorems on one hypothesis — and the T1 file's
   "three poles" (`Set` ✓, `Set×Set` ✗ though extensive, `Vec` ✗) transfer verbatim. In particular
   **`Set×Set` is (l)extensive with disconnected unit**, so *extensivity is not what keeps the left
   adjoint alive either* — the brief's framing inherits T1's own honest correction #1.
4. **`Set` instance = Niu–Spivak Prop 6.57 (Meyers), `2312.00990` p. 204, eq. (6.59)** — KNOWN, gate
   closed 2026-08-30 (`scratch/2026-08-30-novelty-gate-left-adjoint-Fq.md`). **The general-base
   statement (Theorem 1) has NOT been novelty-gated** — DJN `2305.05655` treat `◁` over a general
   base but, per T4 §6, no closed structure for it. **Flagged OPEN; do not claim priority.**

---

## 5. Theorem 2 — the linear verdict: on the collapse locus the gate is `|T| = 1`

**Lemma 2.0 (the collapse locus is bigger than T4 said).** `p◁q = p⊗q` whenever **either**
(i) every `P_s` is tiny (`[P_s,−]` preserves coproducts) — T4-left Prop 2.1 — **or**
(ii) **`T` is finite and `C` is additive**.
*Proof of (ii).* `T` finite and `C` additive ⟹ `∐_{t∈T} = ∏_{t∈T}`, and `[P_s,−]` preserves all
limits, so `[P_s,∐_t[Q_t,X]] = ∐_t[P_s,[Q_t,X]] = ∐_t[P_s⊗Q_t,X]`; sum over `s`. ∎
*(grade: `proved`)* — **Consequence:** on `Fam(Vec^op)` (infinite-dimensional positions allowed),
`L_q` is a well-defined endofunctor for every **finite** `T`, with `◁=⊗`. No tininess needed.

**Theorem 2.** Let `C` be closed symmetric monoidal cocomplete, and let `q=(T,Q)` be such that
`p◁q = p⊗q` for all `p` (convention (D); e.g. Lemma 2.0). Then

> **`(−)◁q` has a left adjoint ⟺ `|T| = 1`,**

and in that case `F_q(R,U) = (R, [Q,U_ρ]) = Fam(⟦q⟧^op)`.

### 5.1 Sufficiency (`|T|=1`)
`q = ({∗},Q)`, `p⊗q = (S, P_s⊗Q)`. By (H) and tensor–hom,
`Fam(r,p◁q) = ∏_ρ∐_s C(P_s⊗Q,U_ρ) = ∏_ρ∐_s C(P_s,[Q,U_ρ]) = Fam((R,[Q,U_ρ]),p)`.
Natural in both. Note `⟦q⟧Z=[Q,Z]`, so `F_q = Fam(⟦q⟧^op)` exactly as over `Set`; **no
dualizability of `Q` is needed**, only closedness. ∎ *(grade: `proved`)*

### 5.2 Necessity — two independent proofs

**(a) Terminal object.** A right adjoint preserves the terminal object. By Lemma 1.3, `1=⟨0_C⟩`;
since `⊗` is cocontinuous in each variable, `0_C⊗Q_t ≅ 0_C`, so

> `L_q(1) = 1⊗q = (T, 0_C)`.

By Lemma 1.2, `(T,0_C) ≅ ({∗},0_C)` iff `|T|=1`. Hence `|T|=1`. (Also settles `T=∅`: `L_0(1)=0`,
the initial object, `≇ 1`.) ∎

**(b) Binary products — uses no zero object, so it is immune to caveat (D).** Products in
`Fam(C^op)` are `p×p' = (S×S', P_s ⊔ P'_{s'})` (coproduct on positions: products in `C^op`).
Then `(p×p')⊗q` is a family over `S×S'×T`, while `(p⊗q)×(p'⊗q)` is a family over `S×T×S'×T`. Take
`p=p'=⟨I⟩`, so `(p×p')⊗q = (T, (I⊕I)⊗Q_t)` and `(p⊗q)×(p'⊗q) = (T×T, Q_t⊕Q_{t'})`: the shape sets
are `T` and `T×T`, so by Lemma 1.2 they are isomorphic only if `|T|=|T|²`. ∎

**A genuine difference between the two probes, worth recording.** Proof (b) gives `|T|=|T|²`, hence
`|T|∈{0,1}` **for finite `T` only**. For `T` infinite it is *inconclusive*, and indeed **false as an
obstruction**: for `q=(ℕ,(k)_{t∈ℕ})` over `Vec_fd`, `(p×p')⊗q` and `(p⊗q)×(p'⊗q)` are families over
`S×S'×ℕ` and `S×S'×ℕ×ℕ` with positions `P_s⊕P'_{s'}` *independent of `t`*, and `ℕ ≅ ℕ²`, so
**`L_q` does preserve all binary products** while failing to preserve the terminal object. The
**empty** product is the binding probe. (Cf. `containers-preserve-connected-not-empty`: the empty
diagram is the disconnected one; here too it is the empty limit that sees the failure.)

### 5.3 Corollaries over the linear bases

- **`Fam_fin(Vec_fd^op)` and `Fam(Vec_fd^op)`:** left adjoint ⟺ `|T|=1`. Summability is not
  involved; `#{t:Q_t≠0}` does not appear.
- **`Fam(Vec^op)`:** for finite `T` (Lemma 2.0(ii)) `L_q` is an endofunctor and the same verdict
  holds. For infinite `T`, `L_q` is not everywhere defined on `Fam(Vec^op)` (a non-tiny `P_s` breaks
  the presentation), so the adjunction question is vacuous there — see Gap 1.
- **Placement in the `(V)⊊(C)⊊(F)` chain** (`fibredness-vs-left-closure` Thm B, over `Vec_fd`):
  `(V)` verticality is `π L_q ≅ π`, i.e. `S×T ≅ S`, i.e. `|T|=1`. Hence

  > **`L_q` has a left adjoint ⟺ `(V)`.** The left-adjoint condition is the **bottom** rung:
  > `(L)=(V) ⊊ (C) ⊊ (F)` over `Vec_fd`, while over `Set` `(V)=(C)=(F)=\{|T|=1\}` and `(L)` is
  > everything. **The chain inverts.**

- **Consistency check.** Theorem 1 and Theorem 2 are jointly satisfiable only trivially: if `I` were
  connected *and* `◁=⊗` held for all `p,q`, every `q` would have `|T|=1`. Indeed a connected unit
  forbids the collapse — `[I⊔I,X] = X×X` does not preserve coproducts, so `I⊔I` is not tiny. Over
  `Set`, `1` is tiny but `2` is not; over `Vec`, everything f.d. is tiny and `k` is not connected.
  **The two theorems partition the bases exactly.** *(grade: `proved`)*

---

## 6. (C) The p.r.a. question proper — and it separates from left-adjointness

Weber (TAC 18(22), 2007, Def 2.3): `L : A → B` is a **parametric right adjoint** iff
`L_1 : A/1 → B/L1` has a left adjoint.

Over `Set` the predecessor showed `L_q 1 = 1`, so `B/L1 ≃ B` and p.r.a. ⟺ left adjoint. **That
argument used `∅` being initial-but-not-terminal in `Set`.** Over `Vec`, `0` is a *zero* object, and
§5.2(a) gives `L_q 1 = (T,0) ≇ 1`. So the slice does **not** collapse. Compute it.

**Lemma 6.1.** `Fam(C^op)/(T,0_C) ≅ ∏_{t∈T}Fam(C^op)`.
*Proof.* By (H), `Fam((S,P),(T,0_C)) = ∏_{s∈S}∐_{t∈T}C(0_C,P_s) = ∏_{s}T` — a structure map is
exactly a function `τ:S→T` and no more (the position legs are the unique maps out of `0_C`).
Morphisms over `(T,0_C)` are morphisms respecting `τ`, i.e. `T`-indexed families of morphisms
between the fibres `(τ^{-1}(t), P|)`. ∎ *(grade: `proved`)*

**Theorem 3.** On the collapse locus, `L_q` is a **parametric right adjoint for every `q`**.
*Proof.* Under Lemma 6.1 and `A/1 ≃ A`, the functor `(L_q)_1` is
`p ↦ (p⊗Q_t)_{t∈T}` : indeed `L_q(!) : (S×T,P_s⊗Q_t) → (T,0)` has shape map `(s,t)↦t`, so the
`t`-th fibre is `(S, P_s⊗Q_t) = p⊗⟨Q_t⟩`. Define
`F((r_t)_{t∈T}) := ∐_{t∈T} F_{Q_t}(r_t)` with `F_Q(R,U)=(R,[Q,U_ρ])` from §5.1. Then

```
(∏_T Fam)( (r_t)_t , (L_q)_1 p )  =  ∏_t Fam(r_t, p⊗Q_t)
                                  =  ∏_t Fam(F_{Q_t}r_t, p)          §5.1
                                  =  Fam( ∐_t F_{Q_t}r_t , p )       Fam(∐,−)=∏
                                  =  Fam( F((r_t)_t), p ).            ∎
```
*(grade: `proved`)*

**Verdict on (C), stated as loudly as the brief asks.**

> **Off `Set`, "p.r.a." and "has a left adjoint" are DIFFERENT QUESTIONS.** `L_q` is p.r.a. over
> both bases, unconditionally in `q`; it has a left adjoint always over `Set` and only for `|T|=1`
> over the linear bases. **The exact measure of the gap is the object `1◁q`**: over `Set` it is
> terminal and the gap is zero; over `Vec` it is `(T,0)` and the slice `Fam/(T,0) ≅ Fam^T` absorbs
> the entire `T`-fold branching. The predecessor's framing "p.r.a. ⟺ left-adjointness" was
> **base-specific**, and the specific feature responsible is that **`Set` has no zero object**.

This *strengthens*, not weakens, the predecessor's refutation of the crown's Weber re-filing: p.r.a.
of `L_q` holds over `Set` **and** over `Vec`, for every `q`, so it discriminates nothing anywhere,
while the probe conditions separate on both bases.

---

## 7. Verification

`scratch/left-adjoint-vec/verify.py`, all green (8 blocks). Hom-sets over `k=F_2,F_3` are finite and given by
`|Fam((A,X),(B,Y))| = ∏_a Σ_b |k|^{dim Y_b · dim X_a}`, so cardinality checking is faithful.

1. **Falsifier (§3).** `κ` injective ∧ surjective ⟺ `|T|=1`, across `|T|∈{1,2,3,5}`,
   `dim B∈{1,2,3}`. Fails at `dim B=1,|T|=2`. **`computed`.**
2. **Terminal.** `1=[0]`, `1◁q=[0]*|T|`; `|Fam(1,1◁q)|=|T|`, `|Fam(1◁q,1)|=1` — non-iso for
   `|T|≥2`. **`computed`.**
3. **Binary products.** `(p×p')⊗q` vs `(p⊗q)×(p'⊗q)` for `p=p'=⟨k⟩`: `[2,2]` vs `[2,2,2,2]` at
   `|T|=2`; `[2,2,2]` vs nine `[2]`s at `|T|=3`; equal at `|T|=1`. **`computed`.**
4. **`Set` contrast.** shapes of `1◁q` `=1` for all `|T|`; shapes of `(p×p')◁q` `=` product of
   shape counts (8=8, 27=27). **`computed`.**
5. **Sufficiency `|T|=1`.** `|Fam(F_Q r,p)| = |Fam(r,p⊗Q)|` on **4000/4000** random families
   (`≤3` shapes, dims `≤3`, `k∈{F_2,F_3}`), 0 mismatches. **`computed`.**
6. **Theorem 3 (p.r.a.).** `∏_t|Fam(r_t,p⊗Q_t)| = |Fam(∐_tF_{Q_t}r_t,p)|` on **3000/3000**
   random instances, 0 mismatches. **`computed`.**
7. **Exhaustive non-representability.** For `|T|=2`, `Q_t=k`, `Z=k`: **no** `(U,N)` with `|U|≤2` and
   `dim N_u ≤ 4` satisfies `|Fam((U,N),p)| = |Fam(⟨Z⟩,p⊗q)|` on 8 test objects `p`. Empty candidate
   set — independent of the terminal-object argument. **`computed`.**
8. **`Set×Set`.** `⟦p◁q⟧(1_C)` computed as `(T^A,T^B)`: non-diagonal for `A≠B`, `|T|≥2` (§9bis).
   **`computed`** (the general statement Prop 9.1 is `proved`). 

---

## 8. Status ledger

| claim | grade | basis |
|---|---|---|
| Lemma 1.2 (isos in `Fam(D)`), Lemma 1.3 (terminal `=⟨0_C⟩`) | **proved** | §1, direct |
| §2 criterion: left adjoint ⟺ `Φ^Z_q` representable ∀`Z`; comparison map `κ` | **proved** | §2 |
| **Theorem 1**: `I` connected ⟹ `Fam(⟦q⟧^op) ⊣ (−)◁q` ∀`q`, any base | **proved** | §4, `γ` twice |
| Theorem 1 ⟹ the `Set` theorem; `(†)` is not the hypothesis | **proved** | §4 rem. 1 |
| Lemma 2.0(ii): finite `T` + additive ⟹ `◁=⊗` (no tininess) | **proved** | §5, additivity |
| **Theorem 2**: on the collapse locus, left adjoint ⟺ `\|T\|=1` | **proved** | §5.1 + §5.2(a),(b) |
| `(L) = (V)` over `Vec_fd`; the chain inverts | **proved** | §5.3 + `fibredness-vs-left-closure` Thm B (cited) |
| Lemma 6.1, **Theorem 3**: `L_q` p.r.a. ∀`q` over the collapse locus | **proved** | §6 |
| p.r.a. ≠ left-adjointness off `Set`; `1◁q` measures the gap | **proved** | §5.2(a) + §6 |
| **Prop 9.1**: `◁` does not exist on `Fam((Set×Set)^op)` | **proved** | §9bis, copower of `1_C` |
| the 8 verification blocks | **computed** | `scratch/left-adjoint-vec/verify.py` |
| `Set` instance of Theorem 1 = Niu–Spivak Prop 6.57 (Meyers) | **proved (cited)** | `2312.00990` p. 204, (6.58)–(6.59); gate report 2026-08-30 |
| T1 (`⟦−⟧` ff ⟺ `I` connected); T4 Prop 2.1; T2; `(V)⊊(C)⊊(F)` | **proved (cited, not re-proved)** | my own files |

**REFUTED this session:** the brief's predicted answer for (B) (*summability*). The gate is `|T|=1`
and it is visible at `dim P_s = 1` with `|T|=2`. **There is no fourth occurrence of the summability
pattern.** What there *is* is a **second occurrence of unit-connectedness** (T1 was the first).

**CORRECTED this session:** the brief's ★ ("`(†)` = distributivity, the single load-bearing step").
`(†)` is load-bearing *for the `Set` formula of `◁`*; the adjunction itself needs only `γ`.

---

## 9. Gaps, precisely stated

1. **`◁` on `Fam(Vec^op)` for infinite `T`.** Lemma 2.0 covers finite `T` or tiny positions. For
   `T` infinite and `P` infinite-dimensional, is `X ↦ [P, ⊕_{t∈T}[Q_t,X]]` presentable as
   `∐_d[N_d,X]` at all? Not settled here (it is T4-left Gap 2). Until settled, "`L_q` is an
   endofunctor of `Fam(Vec^op)`" is only established for finite `T`. Cheap probe: test whether
   `G(X)=[k^{(ℕ)}, X^{(ℕ)}]` preserves the (infinite) products that every `∐_d[N_d,−]` must.
2. **Novelty gate OPEN on Theorem 1 (general base).** The `Set` case is Niu–Spivak Prop 6.57.
   Whether "connected unit ⟹ `◁`-coclosure over any base" appears in DJN `2305.05655`,
   Shapiro–Spivak, or the enriched-container literature is **unchecked**. Next browse: grep DJN for
   "coclosure", "left adjoint", "`⌜q/p⌝`"; also Garner's enriched-familial work.
3. **`I` connected ⟹ left adjoint; is the converse true?** Theorem 1 is one-directional; Theorem 2
   supplies the converse only on the collapse locus. **The cheapest intended separator —
   `C = Set×Set`, disconnected unit, extensive, no collapse — turns out to be UNAVAILABLE: `◁`
   does not exist there at all (§9bis).** So the converse remains open, and §9bis suggests it may be
   open only vacuously. Next candidate bases would need: disconnected unit, no zero object, and
   `⟦p⟧(T·1_C)` a copower of `1_C` for all `p,T`. I have none.
4. **Naturality of `F_q` in `q`** — not checked (also not checked in the predecessor).
5. **The caveat (D)** is a convention. §5.2(b) is independent of it for finite `T`; §5.2(a) is not.
   A presentation-independent necessity proof for infinite `T` is missing.

---

## 9bis. A by-product, found while probing Gap 3: `◁` does not exist over `Set×Set`

**Proposition 9.1.** Let `C = Set×Set` (cartesian closed, cocomplete, lextensive, unit `I=(1,1)`
disconnected, **no zero object**). Then `Fam(C^op)` is **not closed under `◁`**: for
`p = ⟨(1,2)⟩` and `q = ({1,2}, ((1,1),(1,1)))` there is no object of `Fam(C^op)` whose extension is
`⟦p⟧∘⟦q⟧`.

*Proof.* For any `(E,N) ∈ Fam(C^op)`, `⟦E,N⟧(1_C) = ∐_{e∈E}[N_e,1_C] = ∐_{e∈E}1_C = E · 1_C` — the
`E`-fold **copower of the terminal object**, hence a *diagonal* pair `(E,E)` in `Set×Set`. But
`⟦q⟧(1_C) = T·1_C = (T,T)` and, with `P=(A,B)=(1,2)`,
`⟦p⟧((T,T)) = ([P,(T,T)]) = (T^A, T^B) = (2, 4)`, which is not diagonal. ∎
*(grade: `proved`; verified in `verify.py` block 8.)*

**The general criterion this exposes.** `Fam(C^op)` is closed under `◁` only if, for every `p` and
every set `T`, `⟦p⟧(T·1_C)` is again a copower of `1_C`. Both of my working bases satisfy it for
opposite, degenerate reasons:

- **`Set`:** `1_C = 1` is a *generator* and every set is a copower of it — the criterion is vacuous,
  and the copower count `T^{P_s}` is exactly the decoration set of §2.
- **`Vec`:** `1_C = 0` is a *zero object*, so `E·1_C = 0` for every `E` — the criterion is vacuous
  again, but now because the shape data is **invisible** to `⟦−⟧`. That invisibility is precisely
  T1's failure of faithfulness, and it is precisely what forces caveat (D).

`Set×Set` sits between the two degeneracies and is destroyed by the criterion. **Conjecture
(`speculative`):** the substitution product exists on `Fam(C^op)` essentially only when `1_C` is a
generator (the `Set`-like pole) or `1_C ≅ 0_C` (the linear pole) — in which case Theorems 1 and 2
are *jointly exhaustive* and the converse asked in Gap 3 is open only vacuously.

> **⚠ REFUTED THE SAME DAY, and Gap 3 CLOSED with it.** See
> `proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`. `Set_*` (pointed sets under
> smash) has a **zero object**, so `1_C ≅ 0_C` and the criterion above is vacuous — yet `◁` does
> **not** exist there (Theorem A). `1_C ≅ 0_C` is a *symptom* of the linear pole, not a
> characterisation of it, and Theorems 1 and 2 are **not** jointly exhaustive over the class this
> conjecture describes. What survives is a **trichotomy**: extensive pole (where admissibility
> *forces* a connected unit, Theorem B — so `Set×Set` above is an instance of a theorem, visible
> already at `p = ⟨A⟩` for `A` a nontrivial summand of `1`), collapse pole (where the unit is
> always disconnected, Lemma D), and **inadmissible** (`Set×Set`, `Set_*`). Gap 3 holds on both
> poles, and Theorem D there explains why it cannot be asked off them: exactly when `I` is
> disconnected, `◁` becomes a *choice*, so left-adjointness stops being a property of `C`.

**⚠ Scope.** This is a statement about **my** `Fam(C^op)` — one *external* shape set, positions in
`C` — the setting of T1/T2/T4 and of this file. DJN `2305.05655` work with generalized polynomials
over a general base and may use an *indexed* category in which the two components carry independent
index sets (for `Set×Set ≃ Set/2` that would be two-coloured polynomials); there the obstruction
would not arise. **I have not read DJN closely enough to say which.** Flagged for the next browse
together with Gap 2 — see `memory/questions/`.

---

## 10. Grant framing

The closed-structure map of `Fam(C^op)` now has **both** adjoints of `L_q=(−)◁q` classified, and
they are governed by *different* invariants:

- **Right adjoint** (`◁`-closure, "curry the process being substituted into"): needs the **collapse**
  `◁=⊗` plus **summability** — exists on the finite-f.d. linear corner, never on an extensive base.
- **Left adjoint** (`◁`-coclosure, "reindex a `q`-shaped plug-in slot"): needs a **connected
  monoidal unit** — free on `Set`/toposes, and on a linear base only for a single-shape `q`.

For the applications narrative (`orchestration-is-zappa-szep-weld`, `applications-are-directed-
containers`): *substituting a sub-process into a slot can always be pulled back along the slot's own
shape when the resource base is set-like (connected unit); over a linear/quantum resource base it
can be pulled back only when the sub-process has a single shape — any genuine branching destroys the
pullback.* Together with T1 this makes **unit-connectedness the single arithmetic fact separating
set-like from linear resource bases**, controlling both the faithfulness of the process semantics
and the existence of slot-reindexing. That is a clean, quotable line for the theory section, and it
replaces the vaguer "extensivity is the container boundary" with something that also explains
`Set×Set`.
