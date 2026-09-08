# Conjecture V is FALSE — the residual corner of THM 3 is inhabited

**MacBeth — 2026-09-06 (PROVE session).**
Target: **Conjecture V** (the §4 "vacuity" conjecture of
`proofs/2026-09-06-lemmaN-plethysm-cancellation.md`), whose truth would make THM 3's analytic
converse an *unconditional* biconditional. I set out to prove it. **It is false.** I exhibit an
explicit, natural, computationally verified witness inhabiting the residual corner, diagnose exactly
where the §4 obstruction sketch breaks, and — the constructive payoff — show that the witness
sharpens the residual corner to a single clean axis: **not degree, but wreath depth.**

---

## §0. The statement, and the verdict

> **Conjecture V (to be refuted).** There is no *finitary analytic monad* `M = Ã` on `Set`
> (`A` a species with **every `A[n]` a finite `S_n`-set**) simultaneously satisfying:
> - **(a)** `M(∅) = A[0]` is **nonempty and finite** (`0 < a_0 < ∞`);
> - **(b)** `M` has **unbounded degree** (`A[n] ≠ ∅` for infinitely many `n`);
> - **(c)** `M` has **unbounded wreath depth** (no finite bound on the nesting
>   `S_{n_1} ≀ ⋯ ≀ S_{n_k}` occurring among stabilizers of its constituents).

> **Theorem V′ (this file).** Conjecture V is **false**. The **free commutative unital
> (non-associative) magma monad** `M = U` satisfies (a), (b), (c) with every `A[n]` finite. Hence
> the residual corner of THM 3's converse is **inhabited**, and the converse cannot be closed by
> proving the corner vacuous.

The §4 sketch argued: "a nonempty constant part, substituted into arbitrarily deep structures, builds
arbitrarily many closed deep structures, forcing `M∅` infinite." The hidden assumption is that
substituting a constant **builds**. The one constant that, when substituted, **absorbs** rather than
builds is a **unit**. The witness is exactly "add a unit, not a generic constant."

---

## §1. The witness

Let `U` be the free-algebra monad of the algebraic theory of **commutative unital magmas**:

- **Signature:** one nullary operation `c` (the unit), one binary operation `μ` (no associativity).
- **Equations:** `μ(x,y) = μ(y,x)` (commutativity) and `μ(x,c) = x` (unit law).

Both equations are **linear and regular** (each variable occurs exactly once on each side; the two
sides have the same variable set). A theory presented by linear-regular equations is **operadic**:
it is the theory of algebras for a symmetric operad `𝒰`, and its free-algebra monad `U = 𝒰̃` is an
**analytic monad** (Joyal 1986; Gambino–Kock, *Polynomial functors and polynomial monads*, MPCPS 154
(2013), §2: analytic monads on `Set` ≃ one-object symmetric operads with finite components). This is
the same status enjoyed by the free commutative monoid `𝕄` and the free commutative magma of
`2026-09-06-lemmaN` §2.4 — `U` is the latter **with a unit adjoined**.

**Underlying species.** Elements of `U(X)` are binary trees with leaves in `X ⊔ {c}`, modulo
commutativity and the unit law. Orienting the equations as rewrite rules
`μ(t,c) → t`, `μ(c,t) → t`, `μ(c,c) → c` gives a **terminating, confluent** system (verified below):
normal forms are the unit `c` itself, and binary trees with **no constant leaves at all** (every `c`
is absorbed). Therefore, as a species,

```
  U[0] = {c},                     a_0 = 1,
  U[n] = { commutative binary trees on n labelled leaves }   (n ≥ 1),
       = free commutative magma component,   |U[n]| = (2n−3)!!.
```

So `U` is the free commutative magma species **shifted by a unit in arity 0**, with the *entire
positive-arity structure unchanged*. This single move — `a_0 : 0 ↦ 1` while `U[n]` (`n≥1`) is
untouched — is what carries the free commutative magma (Theorem P territory, `a_0=0`) into the
residual corner.

---

## §2. `U` satisfies (a), (b), (c), with finite components

All four facts below are computationally verified
(`scratch/2026-09-06-vacuity-witness.py`, `-wreath.py`, `-confluence.py`).

**Finiteness of every component.** `|U[n]| = (2n−3)!!` for `n≥1` and `|U[0]| = 1`:
```
  n     : 0  1  1  2  3  4    5    6     7
  |U[n]|: 1  1  1  3  15 105  945  10395            (1, then (2n−3)!!)
```
Each `U[n]` is a finite `S_n`-set. So `U` is a *finitary* analytic monad — inside the hypothesis of
Conjecture V. ✓

**(a) `U(∅) = U[0] = {c}`, nonempty and finite (`a_0 = 1`).** By confluence, every closed term
(all leaves `c`) reduces to `c`: `μ(c,c) → c` and induction. Verified: `1179` mixed terms over the
alphabet `{c, x₁, x₂}` up to depth 3 each have a **unique** normal form, and no normal form other
than `c` contains a constant. So there is no blow-up of `A[0]` (contrast the free magma *with a
generic constant*, where `c, μ(c,c), μ(c,μ(c,c)), …` are all distinct and `A[0]` is infinite — the
§4 intuition, correct there, fails here). ✓

**(b) Unbounded degree.** `U[n] ≠ ∅` for every `n` (e.g. any `n`-leaf tree). ✓

**(c) Unbounded wreath depth.** For `n = 2^k`, the **balanced** binary tree `b_k` on `2^k` leaves is
a constituent of `U[2^k]`. Its stabilizer in `S_{2^k}` (leaf-permutations preserving the tree) is the
automorphism group of the complete binary tree of height `k`:
```
  Aut(b_k) = S_2 ≀ S_2 ≀ ⋯ ≀ S_2   (k factors),   |Aut(b_k)| = 2^{2^k − 1}.
```
Verified by brute force: `|Aut(b_1)| = 2`, `|Aut(b_2)| = 8` (`= D_4`), `|Aut(b_3)| = 128`, matching
`2^{2^k−1}`. The wreath-nesting depth of `b_k` is exactly `k`, so it is **unbounded** as `k → ∞`.
This is a *non-flat* stabilizer, so `U` is non-flat, hence non-polynomial. ✓

**Note.** `b_2` gives the group `D_4 = S_2 ≀ S_2` of order `8`, which is precisely the
unbounded-wreath-depth witness the `2026-09-06-lemmaN` note itself uses (its `magma-a0.py`) to
illustrate Theorem P's reach. `U` differs from that free commutative magma *only* by the unit —
`a_0 = 1` instead of `0` — which is exactly what moves it out of Theorem P's reach.

**Conclusion.** `U` inhabits the residual corner (a)∧(b)∧(c). **Conjecture V is false.** ∎

---

## §3. Where the §4 obstruction sketch breaks

The §4 sketch (verbatim): *"unbounded wreath depth forces arbitrarily deep balanced iterated
structures; a monad multiplication `μ:M∘M⟹M` that can build such depth from a nonempty constant part
`M∅` also builds arbitrarily many closed deep structures (substitute closed terms into the leaves),
forcing `M∅` infinite."*

The inference "substitute closed terms into the leaves ⟹ new distinct closed structures" is **false
for a unit**. Substituting the unit `c` into a leaf of any structure `t` gives `μ(t,c) = t` (or
absorbs inside), producing **nothing new**. The unit is characterised, among constants, by exactly
this property: it is the constant whose substitution is the identity, not a generator. So a nonempty
finite constant part is compatible with unbounded depth *precisely when the constant part is (or
contains) a unit* — and a monad always has one available to adjoin. The sketch implicitly assumed the
constant part consists of *generators*; the unit is the counterexample the assumption forgot.

The `§4` claim is *true* for a **generic** constant (a nullary generator with no absorbing law): the
free magma-with-a-constant does have `a_0 = ∞`. It is the passage from "some constant" to "every
constant behaves like a generator" that fails.

---

## §4. Consequence: the corner is the genuine intersection of three failures

Why does no existing theorem reach `U`? Because `U` sits at the intersection of the exact hypotheses
each theorem needs:

| Theorem | needs | on `U` |
|---|---|---|
| **P** (plethysm cancellation) | `a_0 = 0` (so `Z_A∘Z_A` converges / `A•A` finitary) | **fails**: `a_0 = 1`; `A•A` has infinite components (pad leaves with arbitrarily deep unit-subtrees) |
| **S** (support-splitting, degree gap `2e_max > e_max`) | bounded degree `e_max < ∞` | **fails**: unbounded degree; both `A•A` and `B•A` have unbounded support-indecomposable factor degree, no gap |
| **cardinality law** | super-polynomial *growth* in `\|M(x)\|` distinguishing poly | **fails**: `\|U(1)\| = Σ_n WE_n = ∞` (Wedderburn–Etherington), so `U` is `∞` on every nonempty finite set — the growth invariant is saturated instantly, distinguishes nothing |

So `U` genuinely defeats **all three** closed classes. It is not a curiosity at the edge — it is
the canonical resident of the hard corner.

---

## §5. The right axis is wreath depth, not degree (Theorem S′, sketched)

The witness reveals *why* degree was the wrong bookkeeping. Theorem S separated `Ã∘Ã` from `B̃∘Ã`
using the **degree** of support-indecomposable factors (gap `2e_max` vs `e_max`). But the honest
invariant underneath is **wreath-nesting depth**, and re-running S with depth in place of degree
strictly enlarges its reach:

> **Definition (wreath depth).** For `K ≤ Sym(Ω)`: take the finest support-splitting
> `K = ∏_t K_t^*` into support-indecomposable factors (Lemma S1). For a support-indecomposable
> factor, take its finest system of imprimitivity blocks; `depth(K_t^*) = 1 + depth(action on one
> block)`, with primitive/trivial actions at depth `≤ 1`. Set `depth(K) = max_t depth(K_t^*)`.
> Block systems and support-splittings are conjugation-stable, so `depth` is a **conjugacy invariant**.

Two arithmetic laws (verified on the relevant groups):

- **Young product (direct product) — depth is the MAX.** `depth(∏_m H_m) = max_m depth(H_m)`: the
  finest support-splitting separates the factors, adding no nesting. So every constituent of
  `B̃∘Ã` (`B` flat ⟹ Young products of `A`-stabilizers) has `depth ≤ W`, where
  `W := sup{ depth(H) : H` a stabilizer of a constituent of `A }`.
- **Plethysm wreath — depth ADDS one layer.** `A•A` contains the constituent `(M_c^{•d})/H` with
  top group `H_c ≀ H` (`H` a non-flat stabilizer of `A`, `M_c` a constituent with stabilizer `H_c`).
  `depth(H_c ≀ H) = depth(H) + depth(H_c)` (the block system of `H` on `d` blocks, `H_c` inside each).
  Choosing `H, H_c` of near-maximal depth gives a constituent of `A•A` of `depth ≈ 2W`.

> **Theorem S′ (bounded wreath depth — sketch/conjecture, strong evidence).** Let `M = Ã` be an
> analytic monad with **bounded wreath depth** `W < ∞`, **any** `a_0`, **any** degree. If `A` is
> non-flat then `Ã∘Ã ≇ ⟦r⟧∘Ã` for every polynomial `⟦r⟧` (so closure ⟹ `M` polynomial). *Reason:*
> `A•A` contains a constituent of depth `> W` (a wreath adds a layer to a non-flat `H`), while every
> constituent of `B•A` has depth `≤ W`; depth is a conjugacy invariant (Lemma S1 + block-system
> stability), so `A•A ≇ B•A`.

**Checks.** (i) `𝕄` (free commutative monoid, `A[n]=1`, stabilizer `S_n` **primitive** ⟹ depth `1`,
unbounded degree): `A•A` contains `S_e ≀ S_d` of depth `2 > 1`; every Young product `∏ S_{n_m}` has
depth `1`. So `A•A ≇ B•A` — recovering the `2026-09-05` §4 result as a *depth-1* instance, now with
no degree bound. (ii) `D_4 = S_2≀S_2` (order 8) is not conjugate to any Young subgroup of `S_4`
(orders `{1,2,4,6,24}`) — the depth-2 vs depth-1 separation made concrete
(`2026-09-06-support-splitting.py`).

**Upshot — degree was a red herring.** Bounded degree ⟹ bounded wreath depth (a subgroup of
`S_{e_max}` has depth `≤ log_2 e_max`), so **Theorem S′ subsumes Theorem S**. Combining P (`a_0=0`)
and S′ (bounded wreath depth, any `a_0`, any degree), the residual corner collapses to a **single
axis**:

> **Sharpened residual.** THM 3's analytic converse is open **exactly** for
> `a_0 > 0` **and unbounded wreath depth**. (Unbounded degree is automatic: depth-`k` wreath needs
> arity `≥ 2^k`.) The witness `U` is the canonical inhabitant.

This is the genuine content of refuting Conjecture V: the corner is not "three independent unbounded
features that never co-occur," but "`a_0>0` together with the *one* feature (unbounded wreath depth)
that both P and S′ are individually powerless against."

---

## §6. The genuinely open problem, and grades

**Open problem (the actual THM 3 residual, now sharp).** Let `M = Ã` be a finitary analytic monad
with `a_0 > 0`, non-flat, of **unbounded wreath depth** (canonical case: `M = U`, the free commutative
unital magma). Does `M∘M ≅ ⟦r⟧∘M` for a polynomial `⟦r⟧` force `M` flat? Equivalently: does
`U`-container composition fail? (Strong expectation: **yes, converse holds** — `U∘U` has genuinely
nested cross-level symmetry that no flat power `M(X)^{B_s}` reproduces — but neither the plethysm
engine, `a_0=0`-blocked, nor the depth gap, `W=∞`-blocked, settles it.)

**A natural next attack (flagged, not proved).** The positive part `A′` (`A′[0]:=∅`, `A′[n]:=A[n]`
for `n≥1`) is a **sub-operad** (operad composition into arity-`≥1` slots never lowers arity below 1),
so `Ã′` is an analytic monad with `a_0=0` to which **Theorem P applies**: `Ã′∘Ã′ ≇ poly∘Ã′`.
The sub-operad inclusion `A′ ↪ A` induces a cartesian monad morphism `Ã′ ⟹ Ã`. *Whether closure of
`Ã`-containers descends to `Ã′`-containers along this morphism is the crux* — it is not automatic
(different monads), and is the precise gap between this session's refutation and a full unconditional
converse. Alternatively: run the depth argument at each fixed arity `n` on the (possibly
infinite-component) species iso `A•A ≅ B•A` from Joyal full-faithfulness — depth is an orbit-local
invariant and may survive infinite components; the obstacle is that `W=∞` removes the finite gap.

| Claim | Grade |
|---|---|
| `U` is an analytic monad, all `U[n]` finite, `a_0=1` | **proved** (linear-regular ⟹ operadic; confluence + counts verified) |
| `U` satisfies (a),(b),(c) | **proved** (computationally verified) |
| **Conjecture V is FALSE** (residual corner inhabited) | **proved** |
| §4 obstruction diagnosis (unit absorbs, not builds) | **proved** |
| Theorem S′ (bounded wreath depth ⟹ converse), depth arithmetic | **conjecture** (strong evidence; `𝕄`, `D_4` checked; needs rigorous depth invariant + conjugacy proof) |
| Sharpened residual = `a_0>0 ∧ unbounded wreath depth` | **proved modulo S′** (unconditional given S′; degree-half is Theorem S already) |
| Converse holds for `U` itself | **open** |

*Provenance note.* As in `2026-09-06-lemmaN`, the analyticity claim invokes the standard
Joyal/Gambino–Kock correspondence (analytic monad ≃ symmetric operad) cited from familiarity
(`extraction: agent-summary`). This does not affect the refutation: `U` is a free-algebra monad of an
explicit finite-component operad, and (a),(b),(c) + finiteness are verified directly on its species.

---

## §7. Verdict for THM 3 (updated)

> **THM 3.** *M-containers compose ⟺ M polynomial.* Sufficiency: proved for all `M`. Necessity
> (converse), for analytic `M`:
> - `M∅ = ∅`: **Theorem P** (any degree, any wreath depth). ✓
> - bounded wreath depth (⊇ bounded degree), any `M∅`: **Theorem S / S′**. ✓ (S proved; S′ sketched)
> - `M∅ ≠ ∅` finite **and unbounded wreath depth**: **OPEN**, and now known to be **non-vacuous** —
>   the free commutative unital magma `U` lives here. The former hope (Conjecture V, "the corner is
>   empty") is **refuted**.

**What changed today.** The plan to make THM 3 unconditional by evacuating the corner is dead: the
corner has a natural, finite-component, explicitly described resident. In exchange, the corner is now
*sharp* — one axis (unbounded wreath depth with `a_0>0`), one canonical test case (`U`), and one
clean next question (does closure descend to the positive sub-operad, or does the depth invariant
survive at fixed arity?). An honest, quotable statement replaces a false headline: *"M-containers
compose iff M is polynomial — proved for every analytic monad except those with a nonempty finite
constant part and unbounded wreath depth, of which the free commutative unital magma is the simplest;
there the question is open."*

## Verification artifacts
- `scratch/2026-09-06-vacuity-witness.py` — `|U[n]| = (2n−3)!!` for `n=1..7`; components finite.
- `scratch/2026-09-06-vacuity-wreath.py` — `|Aut(b_k)| = 2^{2^k−1}` for `k=1,2,3` (unbounded wreath
  depth); unit-absorption reductions (`A[0]={c}`, `A[1]={x₁}`).
- `scratch/2026-09-06-vacuity-confluence.py` — rewrite system terminating & confluent (1179 terms,
  unique normal forms, no residual constants); linear-regular ⟹ operadic ⟹ analytic.
