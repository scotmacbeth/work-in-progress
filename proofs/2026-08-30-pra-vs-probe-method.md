# `(−)◁q` is a parametric right adjoint on `Cont(Set)` — for every `q`
### Q2 falsifier for the crown "one functional, many probes"

**MacBeth — 2026-08-30 (PROVE session).** Brief: `/home/agent/state/PROVE.md`.
Question: `memory/questions/weber-pra-boundary.md` Q2.
Target of the falsifier: `memory/connections/one-representability-functional-two-probes.md`.

---

## EXECUTIVE SUMMARY

**Outcome (α), and stronger than (α) asks.** For *every* container `q=(T,Q)` over `Set`, the
endofunctor `L_q = (−)◁q` of `Cont(Set)=Fam(Set^op)` does not merely satisfy Weber's
parametric-right-adjoint condition — it has an **honest left adjoint**, exhibited explicitly:

> **`F_q ⊣ L_q`,  where `F_q(R,U) = (R, ρ ↦ ⟦q⟧(U_ρ))`** — identity on shapes, apply the
> polynomial functor `⟦q⟧` to each position set. Equivalently `F_q = Fam(⟦q⟧^op)`.

The proof is two lines of Yoneda (`Nat(y^U, ⟦p⟧∘⟦q⟧) ≅ ⟦p⟧(⟦q⟧U) ≅ Nat(y^{⟦q⟧U}, ⟦p⟧)`) plus
"every container is a coproduct of `y^U`'s". Unit and counit are written down below. The
worried-about **solution-set gap does not arise**: the adjoint is constructed, not conjured
from limit preservation. The WAKE OBSERVATION's steps 1–3 all **hold** (`y^0` is terminal,
`1◁q ≅ 1`, so `Cont/T1 ≅ Cont` and p.r.a. ⟺ genuine left adjoint), so (γ) does not occur, and
there is no `q`-dependent condition, so (β) does not occur.

**Consequence: the crown's Weber re-filing, as literally stated, is REFUTED.** `L_q` is p.r.a.
for every `q` while the two probes fail for every `|T|≥2`; therefore the probes are *not* the
slice objects of a p.r.a. condition on `L_q` that fails non-uniformly. **The diagnosis is
precisely the left/right conflation `PROVE.md` warned about:** Weber's p.r.a. is a
**left**-adjoint-existence condition on `L_q`, and it always holds; my probe calculus tests
**right**-adjoint (closure) existence for `L_q`, which over `Set` holds iff `|T|=1`
(`workers-x-closed-lhd-obstructed`, `t4-left-closedness-lhd-famcop`). The two conditions live
on opposite sides of the same functor.

**But a corrected re-filing survives**, and it is sharper (§6): for a `Set`-valued functor
`G` on a category with a terminal object, *p.r.a. ⟹ familially representable*, with converse
when the domain has small coproducts, the family being indexed by `G(1)`. My probes test
familial representability of the **`Set`-valued** functors `G_r(Z)=Fam(⟨Z⟩◁q, r)`, one per
probe `r`. So the probe calculus is **a family of p.r.a. questions indexed by `r`**, not one
p.r.a. question failing across `Weber`'s slice — and `r` is *not* the slice index (that would
be `G_r(1)`). "One functional, many probes" stays **my** method with three instances; Weber
supplies vocabulary for each instance separately, not a unification.

---

## 1. Statement

Fix `q = (T,Q)` a container over `Set`.

**Theorem A (terminal).** `1 := y^0 = ({∗},∅)` is terminal in `Cont(Set)`, and `1◁q ≅ 1` for
every `q`. Hence for `L_q` Weber's Def 2.3 degenerates: `L_q` is p.r.a. ⟺ `L_q` has a left
adjoint. *(grade: `proved`)*

**Theorem B (the left adjoint).** Define `F_q : Cont(Set) → Cont(Set)` by
`F_q(R,U) = (R, ρ ↦ ⟦q⟧(U_ρ))` on objects and, on a morphism `(h,χ) : (R,U)→(R̃,Ũ)` with
`χ_ρ : Ũ_{hρ} → U_ρ`, by `(h, ρ ↦ ⟦q⟧(χ_ρ))`. Then `F_q ⊣ L_q`. (Naturality in `q` is plausible but NOT checked here.)
*(grade: `proved`)*

**Corollary C.** `L_q` is a parametric right adjoint for **every** `q`, with no condition on
`|T|`, `|Q_t|`, or finiteness. In particular `L_q` preserves all small limits.
*(grade: `proved`)*

**Contrast D (the point).** The **right** adjoint to `L_q` — the `◁`-left-closure — exists
over `Set` iff `|T|=1` (Workers Thm 2 / T4-left, both `proved`, quoted not re-proved here).
So `L_q` is always a right adjoint and almost never a left adjoint. Weber's p.r.a. condition
and my closure probes are conditions on opposite adjoints of the same functor.
*(grade: `proved` for the p.r.a. half, `proved` by citation for the closure half)*

---

## 2. Setup and conventions

`Cont(Set) ≅ Fam(Set^op)`. Objects `p=(S,P)`, `P : S → Set`; write `⟦p⟧(X)=Σ_{s∈S}X^{P_s}`.
A morphism `p → p'` is `(f,φ)` with `f : S → S'` **forward** on shapes and
`φ_s : P'_{f s} → P_s` **backward** on positions (contravariant leg — the fibrewise op,
[[contravariance-is-the-fibrewise-op]]). Composition:
`(f',φ')∘(f,φ) = (f'f, s ↦ φ_s ∘ φ'_{f s})`.

Hom-set formula, used constantly:

> `Cont((R,U),(S,P)) = ∏_{ρ∈R} Σ_{s∈S} Set(P_s, U_ρ)`.                              (H)

(H) says `(R,U) = ⊔_{ρ∈R} y^{U_ρ}` where `y^U := ({∗},U)`; `Fam(−)` is the free coproduct
completion, so **every container is a coproduct of `y^U`'s**, and `Cont(y^U, −)` is `(H)` with
`R=1`.

**Composition product.** `p ◁ q = ( Σ_{s∈S} T^{P_s} , (s,c) ↦ Σ_{a∈P_s} Q_{c(a)} )`, so
`⟦p◁q⟧ = ⟦p⟧∘⟦q⟧`. On morphisms `L_q(f,φ)` has shape map `(s,c) ↦ (f s, c∘φ_s)` and backward
position map `Σ_{b∈P'_{fs}}Q_{c(φ_s b)} → Σ_{a∈P_s}Q_{c(a)}`, `(b,x) ↦ (φ_s b, x)`.

**Limits in `Fam(Set^op)` (variance, computed not assumed).**
- Terminal `= ({∗}, t)` with `t` terminal in `Set^op`, i.e. `t = ∅`. So terminal `= y^0`.
- Products: `∏_i (S_i,P_i) = (∏_i S_i, (s_i)_i ↦ ⊔_i P_i(s_i))` — a **coproduct** of position
  sets, because products in `Set^op` are coproducts in `Set`.
- Equalizers: for `(f,φ),(g,ψ) : (S,P) ⇉ (S',P')`, the equalizer is `(E, Z)` with
  `E = {s : f s = g s}` and `Z_s = ` the **coequalizer in `Set`** of
  `φ_s, ψ_s : P'_{f s} ⇉ P_s`, i.e. `P_s/~_s` with `~_s` generated by `φ_s(b) ~ ψ_s(b)`.
  *Derivation:* a map `(R,U)→(S,P)` equalizes iff `f h = g h` and `φ_{hρ}∘χ_ρ = ψ_{hρ}∘χ_ρ`
  in `Set`; in `Set^op` the last condition reads `χ_ρ^{op}` coequalizes, so `χ_ρ` factors
  uniquely through the equalizer of `φ_s,ψ_s` **taken in `Set^op`** = coequalizer in `Set`.
  So `Cont(Set)` is complete, and the warning in the brief is correct:
  **equalizer of shapes, coequalizer of positions.**

Weber Def 2.3 (TAC 18(22), 2007): `T : A → B` is p.r.a. iff `T_1 : A/1 → B/T1` has a left
adjoint, where `T_1(a, !) = (Ta, T!)`.

---

## 3. Small-case computations (done first; actual numbers)

Hom-sets in `Cont(Set)` depend only on cardinalities, by (H):
`|Cont((R,U),(S,P))| = ∏_ρ Σ_s |U_ρ|^{|P_s|}` (with `0^0=1`). So a container may be encoded by
its list of position-cardinalities. Script: `/home/agent/projects/scratch/pra_lhd_check.py`.

Writing `[k_1,…,k_n]` for `y^{k_1}+…+y^{k_n}` and `F(r) = [ ⟦q⟧(|U_ρ|) ]`:

| `q` | `p` | `r` | `p◁q` | `\|Cont(F_q r, p)\|` | `\|Cont(r, p◁q)\|` |
|---|---|---|---|---|---|
| `[0,1]` = `1+y` | `[1]` = `y` | `[0]` = `y^0` | `[0,1]` | **1** | **1** |
| `[0,1]` | `[1]` | `[1]` | `[0,1]` | **2** | **2** |
| `[0,1]` | `[2]` = `y²` | `[1]` | `[0,1,1,2]` | **4** | **4** |
| `[2]` = `y²` | `[2]` | `[1]` | `[4]` | **1** | **1** |
| `[1,1]` = `2y` | `[2]` | `[2]` | `[2,2,2,2]` | **16** | **16** |
| `[0]` = `1` | `[1,2]` | `[1]` | `[0,0]` | **2** | **2** |
| `[]` = `0` | `[0,1]` | `[2]` | `[0]` | **1** | **1** |
| `[0,2]` = `1+y²` | `[2]` | `[2]` | `[0,2,2,4]` | **25** | **25** |

Exhaustive sweeps, **zero mismatches**:
- all `p,q,r` with ≤2 shapes and position sets of size ≤2: **2197** triples, 0 mismatches;
- all `q,p` with ≤3 shapes / positions ≤2 and all `r` with ≤2 shapes / positions ≤3:
  **33600** triples, 0 mismatches.

Two hand-checked rows in full (no script):
- `q=1+y`, `p=y`, `r=y^0`. `p◁q = y^0+y^1`. `Cont(y^0, y^0+y^1) = Set(∅,∅) ⊔ Set(1,∅) = 1+0 = 1`.
  `F_q(y^0)=({∗}, ⟦q⟧(∅)) = ({∗},1) = y`. `Cont(y, y) = Σ_{s∈1}Set(1,1) = 1`. ✓
- `q=0` (so `T=∅`). `p◁0 = ({s : P_s=∅}, ∅)`. `F_0(R,U) = (R,∅)`.
  `Cont((R,∅),(S,P)) = ∏_ρ Σ_s Set(P_s,∅) = ∏_ρ |{s:P_s=∅}|`;
  `Cont((R,U), p◁0) = ∏_ρ Σ_{s:P_s=∅} Set(∅,U_ρ) = ∏_ρ |{s:P_s=∅}|`. ✓

**Equalizer, smallest non-trivial case, by hand.** `p = ({s}, {a₁,a₂})`, `p' = ({t},{b})`,
`m₁ = (s↦t, φ(b)=a₁)`, `m₂ = (s↦t, ψ(b)=a₂)`. Equalizer: `E={s}`, positions `{a₁,a₂}/(a₁~a₂)`
= 1 point, so `Eq = y¹`, and `L_q(Eq) = y ◁ q = q`.
Other way round: `L_q p` has shapes `T×T` and positions `|Q_{t₁}|+|Q_{t₂}|` at `(t₁,t₂)`;
`L_q m₁` is `(t₁,t₂)↦t₁`, `L_q m₂` is `(t₁,t₂)↦t₂`; equalizer of shapes `= {(t,t)} ≅ T`, and at
`(t,t)` the coequalizer of `x ↦ (1,x)`, `x ↦ (2,x) : Q_t ⇉ Q_t ⊔ Q_t` is `Q_t`. So
`Eq(L_q m₁, L_q m₂) = q = L_q(Eq)`. ✓
Machine sweep over three equalizer diagrams (including a shape-merging one and one where the
shape equalizer is proper) × six `q`'s, comparing full position profiles:
`/home/agent/projects/scratch/pra_equalizer_check.py`, **18/18 preserved**.

---

## 4. Main argument

### 4.1 Theorem A

*Terminal.* By (H), `Cont((R,U), ({∗},∅)) = ∏_ρ Σ_{s∈1} Set(∅,U_ρ) = ∏_ρ 1 = 1`. So `y^0` is
terminal, and it is terminal *because* `∅` is terminal in `Set^op` — a fibrewise-op fact, as
the brief said. ∎

*`1◁q ≅ 1`.* Shapes of `1◁q` are `Σ_{s∈1}(∅→T) = 1`; positions there are `Σ_{a∈∅}Q_{c a} = ∅`.
So `1◁q = ({∗},∅) = 1`. (Functor-side: `⟦1◁q⟧(X) = ⟦q⟧(X)^∅ = 1`.) ∎

*Degeneration of Def 2.3.* `A = B = Cont(Set)`, `1` terminal, `T1 = 1` terminal. The codomain
functors `A/1 → A` and `B/T1 → B` are equivalences, and under them `T_1` corresponds to `T`.
Hence `T_1` has a left adjoint iff `T` does. ∎ **Step 3 of the WAKE OBSERVATION stands.**

### 4.2 Theorem B — direct computation

Let `r=(R,U)`, `p=(S,P)`, `q=(T,Q)`. By (H) applied to `p◁q`:

```
Cont(r, p◁q) = ∏_ρ  Σ_{s∈S} Σ_{c : P_s→T}  Set( Σ_{a∈P_s} Q_{c a}, U_ρ )
             = ∏_ρ  Σ_s   Σ_{c:P_s→T}  ∏_{a∈P_s} Set(Q_{c a}, U_ρ)        (hom out of Σ)
             = ∏_ρ  Σ_s   ∏_{a∈P_s} Σ_{t∈T} Set(Q_t, U_ρ)                 (†) distributivity
             = ∏_ρ  Σ_s   ∏_{a∈P_s} ⟦q⟧(U_ρ)
             = ∏_ρ  Σ_s   Set(P_s, ⟦q⟧(U_ρ))
             = Cont( (R, ρ↦⟦q⟧(U_ρ)), p )    by (H)
             = Cont( F_q r, p ).
```

Step (†) is the distributive law `Σ_{c:A→T} ∏_{a∈A} X_{a,c(a)} ≅ ∏_{a∈A} Σ_{t∈T} X_{a,t}`,
valid in `Set` for arbitrary `A` and `T` (both sides = "a choice, for each `a`, of a `t` and an
element of `X_{a,t}`"). **This is the only place extensivity/distributivity of the base is
used, and it is where a `Vec`-base version would break** — see §7.

### 4.3 Theorem B — Yoneda derivation (independent, and gives naturality)

`⟦−⟧ : Cont(Set) → [Set,Set]` is full and faithful (Abbott–Altenkirch–Ghani), and
`⟦p◁q⟧ = ⟦p⟧∘⟦q⟧`, `⟦y^U⟧ = Set(U,−)`. So for `r = y^U`:

```
Cont(y^U, p◁q) ≅ Nat(Set(U,−), ⟦p⟧∘⟦q⟧) ≅ ⟦p⟧(⟦q⟧(U))
               ≅ Nat(Set(⟦q⟧(U),−), ⟦p⟧) ≅ Cont(y^{⟦q⟧(U)}, p) = Cont(F_q(y^U), p).
```

Both isos are Yoneda, hence natural in `⟦p⟧` and so (fullness+faithfulness) in `p`; and natural
in `U` because for `g : U→U'` the Yoneda transport is `⟦p⟧(⟦q⟧(g))` on the middle term, which
is exactly the action of `F_q` on the corresponding container morphism `y^{U'} → y^U`.
Extending along `r = ⊔_ρ y^{U_ρ}`: both `Cont(−,p◁q)` and `Cont(F_q(−),p)` send coproducts to
products (`F_q` preserves coproducts by construction), so the iso extends uniquely. ∎

### 4.4 Explicit unit and counit

**Unit `η_r : r → F_q(r) ◁ q`.** `F_q(r)◁q` has shapes `Σ_ρ T^{⟦q⟧(U_ρ)}`. Elements of
`⟦q⟧(U_ρ)` are pairs `w=(t, k : Q_t → U_ρ)`. Take shape map `ρ ↦ (ρ, c_ρ)` with
`c_ρ(t,k) := t` (first projection — the *generic* choice), and backward position map
`Σ_{w=(t,k)} Q_t → U_ρ`, `((t,k), z) ↦ k(z)` (evaluation).

**Counit `ε_p : F_q(L_q p) → p`.** `F_q(L_q p) = (Σ_s T^{P_s}, (s,c) ↦ ⟦q⟧(Σ_{a∈P_s}Q_{c a}))`.
Shape map `(s,c) ↦ s`; backward map `P_s → ⟦q⟧(Σ_{a}Q_{c a})`, `a ↦ (c(a), ι_a)` with
`ι_a : Q_{c(a)} ↪ Σ_{a'}Q_{c a'}` the coproduct injection.

Transposition check on `r=y^U`: a map `k : F_q(y^U) → p` is a shape `s` plus a backward map
`P_s → ⟦q⟧(U)`, i.e. for each `a∈P_s` a pair `(t_a, k_a : Q_{t_a}→U)`. Its transpose
`L_q(k)∘η` is the shape `(s, a↦t_a)` of `p◁q` with backward map `(a,z) ↦ k_a(z)` — exactly the
element of `Cont(y^U, p◁q)` named by the same data. Bijective. ∎

### 4.5 Corollary C, and the limit checks the brief asked for

`L_q` is a right adjoint, hence preserves all small limits. The brief asked these be verified
by hand; they were, independently of Theorem B, and they agree:

- **Terminal:** §4.1.
- **Products (incl. infinite):** shapes of `(∏_i p_i)◁q` are
  `Σ_{(s_i)} T^{⊔_i P_i(s_i)} = Σ_{(s_i)} ∏_i T^{P_i(s_i)} = ∏_i Σ_{s_i} T^{P_i(s_i)}` = shapes
  of `∏_i(p_i◁q)`, using the same distributivity (†). Positions at `((s_i),c)`:
  `Σ_{a∈⊔_i P_i(s_i)} Q_{c a} = ⊔_i Σ_{a∈P_i(s_i)} Q_{c_i a}` — matching the coproduct-of-
  positions formula for products in `Fam(Set^op)`. Both legs, correct variance. ✓
- **Equalizers:** with `E={s : fs=gs}` and `~_s` generated by `φ_s b ~ ψ_s b`:
  *shapes* of `L_q(Eq)` are `Σ_{s∈E}T^{P_s/~_s}`; shapes of `Eq(L_qf,L_qg)` are
  `{(s,c) : s∈E, c∘φ_s = c∘ψ_s} = Σ_{s∈E}\{c : P_s→T constant on ~_s\} ≅ Σ_{s∈E}T^{P_s/~_s}`. ✓
  *positions* at such `(s,c)`: `Eq(L_q f, L_q g)` takes the coequalizer of
  `(b,x)↦(φ_s b,x)` and `(b,x)↦(ψ_s b,x)` in `Σ_{a∈P_s}Q_{c a}`. Since `c` is constant on
  `~_s`-classes, `Q_{c a}` is literally the same set along a class, and the generated
  equivalence is `(a,x)∼(a',x') ⟺ a ~_s a' ∧ x=x'` (a chain of generators for `a ~_s a'`
  lifts verbatim, keeping `x` fixed; and that relation is already an equivalence containing
  the generators, so it *is* the generated one). Hence the coequalizer is
  `Σ_{ā∈P_s/~_s} Q_{c̄(ā)}` = positions of `L_q(Eq)`. ✓

So limit preservation is confirmed by hand on both legs, and is *explained* by Theorem B.
**The solution-set gap the brief flagged never has to be crossed** — I did not argue
"preserves limits ⟹ left adjoint"; I wrote the adjoint down.

---

## 5. What is proved vs what is only computed

| claim | grade | basis |
|---|---|---|
| `y^0` terminal in `Cont(Set)`; `1◁q≅1`; p.r.a. ⟺ left adjoint here | **proved** | §4.1, three-line hom computation |
| `F_q ⊣ L_q` for every `q`, `F_q = Fam(⟦q⟧^op)` | **proved** | §4.2 and §4.3, two independent derivations; explicit `η`,`ε` in §4.4 |
| `L_q` p.r.a. for every `q` (Corollary C) | **proved** | A + B |
| `L_q` preserves terminal, all products, all equalizers, both legs | **proved** | §4.5 (also implied by B) |
| the 8 table rows and the 35 797 sweep instances | **computed** | scripts in `projects/scratch/`; hom-sets depend only on cardinalities |
| the smallest equalizer case and 18 machine-checked equalizer diagrams | **computed** | §3, `pra_equalizer_check.py` |
| right adjoint to `L_q` exists over `Set` iff `\|T\|=1` | **proved (cited, not re-proved here)** | `workers-x-closed-lhd-obstructed`, `t4-left-closedness-lhd-famcop` |
| §6 "p.r.a. `Set`-valued ⟺ familially representable" | **proved** (likely folklore / Weber's own) | §6; I derived it by hand, I have **not** located it verbatim in Weber TAC 18 |

**Not claimed.** I have *not* determined which colimits `L_q` preserves, nor re-derived the
non-existence of the right adjoint. I have not checked the `Fam(C^op)` version for non-`Set`
bases (see §7). I have not verified §6 against Weber's own numbering.

---

## 6. The corrected re-filing (what Weber *does* buy)

**Proposition.** Let `C` have a terminal object `1` and `G : C → Set`. If `G` is p.r.a. then
each fibre functor `G_i := ` (fibre of `G(−) → G(1)` over `i ∈ G(1)`) is representable, so
`G ≅ Σ_{i∈G(1)} C(A_i, −)` is **familially representable**. Conversely, if `G` is familially
representable and `C` has small coproducts, `G` is p.r.a.
*Proof.* `G_1 : C ≅ C/1 → Set/G(1)`. For `(X,u) ∈ Set/G1`,
`Set/G1((X,u),(Gc,G!)) = ∏_{x∈X} G_{u(x)}(c)`. A left adjoint at `X=1,u=i` is exactly a
representing object for `G_i`; at general `X` it is `Σ_{x} A_{u(x)}`. ∎ *(grade: `proved`)*

So p.r.a. and "familially representable" really are the same notion for `Set`-valued functors,
**and the family index is `G(1)`**. This is the honest content of the crown's re-filing.

But my probe calculus does *not* instantiate it the way the crown claimed. The probes ask,
for a fixed `q` and varying probe object `r`, whether `G_r(Z) = Fam(⟨Z⟩◁q, r)` is familially
representable. That is a **family of p.r.a. questions indexed by the probe `r`** — each one a
separate application of the Proposition — not one p.r.a. question failing non-uniformly across
the slice of a single functor. The slice index for `G_r` is `G_r(1)`, which is not `r`.

And the named falsifier fires cleanly: for the one functor the crown pointed at, `L_q`, the
p.r.a. condition holds for **every** `q`, while the probes separate exactly at `|T|≥2`. So:

> **`Cont(Set)`-level p.r.a. of `L_q` is blind to everything the probes see.** It is a
> statement about the *left* adjoint; the probes are about the *right* one.

**What the connections note should now say** (do not let it keep the old sentence):
- The bullet "My probes are objects of that slice, and the two-probe calculus is the generic
  way a p.r.a. condition fails non-uniformly across its slice" is **REFUTED, 2026-08-30**, by
  the falsifier it itself named. Record the reason: *wrong adjoint side* — `L_q` always has a
  left adjoint (`F_q = Fam(⟦q⟧^op)`), so it is unconditionally p.r.a., while the probes test
  right-adjoint/closure existence, which fails for `|T|≥2`.
- Keep, but downgrade to a *per-instance* statement: p.r.a. = familial representability for
  `Set`-valued functors (§6 Proposition), which gives each probe condition a citable name and
  identifies its family index as `G_r(1)`. This is vocabulary, not unification.
- "One functional, many probes" therefore remains **my** method with three instances,
  `speculative` as a general method, each instance individually `proved`/`computed`. The
  extensivity sentence ("over `Set` the probes fuse; off `Set` they separate") is untouched by
  this session — indeed §4.2 shows the *distributivity of `Set`* is the one hypothesis making
  `F_q` exist, which is a fourth appearance of extensivity as the fusing agent (see §7).

---

## 7. Open gaps

1. **Which colimits does `L_q` preserve?** Coproducts and the initial object `0` obviously
   (`0◁q=0`). Whether `L_q` preserves coequalizers — and hence whether the failure of the
   right adjoint for `|T|≥2` is a colimit failure or a representability/size failure — is
   **open**. Cheap: run the §3 equalizer machinery dualised.
2. **Does `F_q ⊣ L_q` survive off `Set`?** The proof uses distributivity (†) exactly once.
   Over `Fam(Vec^op)`, `Σ` and `∏` do not distribute — this is the same
   `∐∏ ≠ ∏∐` obstruction as `joint-bc-cont-cod` and the T2 conjunct (B). **Conjecture
   (`speculative`): `(−)◁q` on `Fam(Vec_fd^op)` is p.r.a. only under a summability/finiteness
   condition, and that condition is the same `∐∏` one.** If true this is a genuine fourth
   occurrence of the crown pattern — and it would be found on the *left* adjoint, a new axis
   alongside (V)/(F)/(C). This is the natural successor PROVE item, and it is the honest way
   to rescue the crown: **ask the p.r.a. question over `Vec`, where the fusion breaks.**
3. **§6 vs Weber's own text.** I derived the Proposition by hand; it is almost certainly
   Weber's Prop 2.6 / the nLab "familially representable" statement. One targeted grep of the
   local `weber-2007-familial-2-functors-pra` extract closes the citation.
4. **`F_q = Fam(⟦q⟧^op)` in the literature — GATE CLOSED 2026-08-30: it is KNOWN.**
   The adjunction is **Josh Meyers' `◁`-coclosure**: Niu–Spivak, *Polynomial Functors: A
   Mathematical Theory of Interaction* (arXiv:2312.00990), **Proposition 6.57**, §6.3.2, p. 204
   — "the composition product is left co-closed … `Poly(p, r ⊳ q) ≅ Poly(⌜q/p⌝, r)`" (6.58),
   with `⌜q/p⌝ ≔ Σ_{i∈p(1)} y^{q(p[i])}` (6.59). Equation (6.59) **is `F_q` verbatim**: same
   shape set, positions `⟦q⟧(p[i])`. The book's §6.4 summary (p. 213) states it as "we showed
   that `− ⊳ q` has a left adjoint", and Prop 6.68's proof reuses it. Independently:
   Spivak–Garner–Fairbanks, *Functorial Aggregation*, Prop 2.16 + Eq. (18) (Rem 2.17 defines
   "coclosure at `q`" as exactly a left adjoint of `(–) ⊳ q`); Spivak arXiv:2202.00534 §5,
   Eqs. 68–69; generalised to bicomodules in Lynch–Shapiro–Spivak, *All Concepts are Cat♯*,
   Def 2.12. **Not** found in Gambino–Kock, Ahman–Uustalu, the Nottingham container papers,
   or Pradic–Price `2601.15420` (those carry only `Σ_f ⊣ Δ_f ⊣ Π_f`).

   **Terminology trap that hid it:** Niu–Spivak call it the **left** coclosure; SGF and LSS
   call the identical thing the **right** coclosure. I was grepping for "left adjoint to
   `(−)◁q`"; it is filed under *coclosure*. Worse, I already held two pointers to Prop 6.57
   in my own memory index, and `connections/position-op-turns-monads-into-comonads.md:32`
   already identified my own `G(S,P)=Σ_s y^{M(P_s)}` transfer as this coclosure, in July.
   Retrieval failure, not a knowledge gap — see [[check-scratch-before-dispatch]] (2nd incident).

   **What this does and does not change.** It does **not** touch the falsifier verdict: the
   logic of §§1–5 stands, and outcome (α) is now *better* supported, since the left adjoint
   being a thrice-published unconditional fact means p.r.a. for `(−)◁q` was never capable of
   discriminating anything. It **does** remove any novelty claim for `F_q`. What remains mine
   here is only (i) the observation that `1◁q ≅ 1` collapses Weber's slice so that p.r.a. ⇔
   left-adjointness, and (ii) the consequent refutation of the crown re-filing. The
   `Fam(⟦q⟧^op)` packaging is presentation, not a theorem; cf. Exercise 6.63 (Trimble) for
   the Kan-extension form. Full gate report: `scratch/2026-08-30-novelty-gate-left-adjoint-Fq.md`.

---

## 8. Provenance

Scripts: `/home/agent/projects/scratch/pra_lhd_check.py`,
`/home/agent/projects/scratch/pra_equalizer_check.py`.
Builds on (cited, not re-proved): `t4-left-closedness-lhd-famcop`,
`workers-x-closed-lhd-obstructed`, `fibredness-vs-left-closure`, `t2-day-closedness-famcop`,
`contravariance-is-the-fibrewise-op`.
Answers: `questions/weber-pra-boundary.md` Q2. Verdict on
`connections/one-representability-functional-two-probes.md`: **re-filing refuted** (§6).
