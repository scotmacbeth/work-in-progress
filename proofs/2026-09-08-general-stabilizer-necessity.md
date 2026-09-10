# THM 3 necessity for the free commutative unital magma family — and the correction of the peg abstraction

**MacBeth — 2026-09-08 (PROVE session).**
Target (`state/PROVE.md`, registry `theorem-general-stabilizer-necessity`): promote the U-corner
(`2026-09-07-U-corner-resolved-stabilizer.md`) from ONE witness to a FAMILY filling the residual
`a_0>0 ∧ 𝔥=∞` of THM 3 necessity, via the peg/diagonal mechanism whose parametric-`H` version was
graded `computed` on 2026-09-08.

**Two-part outcome.**

1. **Theorem (proved, family).** For every *free commutative unital magma monad* — the free-algebra
   monad `M=Ã` of a **fully-symmetric unital operad** `O` (every operation of arity `≥2` is fully
   symmetric `H_g=S_{arity}`, a universal absorbed unit `e`, no unary operations but the identity,
   some operation of arity `≥2`) — one has `M∘M ≇ ⟦r⟧∘M` for **every** polynomial `⟦r⟧`. Hence the
   essential image of `⟦−⟧_M` is not closed under composition; THM 3 necessity holds for the whole
   family. This includes the free commutative unital magmas of **every arity** `n≥2` (all `a_0=1`,
   `𝔥=∞`) — a named slice of the residual, generalizing `U=U_2`.

2. **Correction (the peg abstraction as stated is FALSE).** The 2026-09-08 "parametric-`H`" evidence
   (`2026-09-08-general-stabilizer-diagonal-evidence.md`, node `general-stabilizer-diagonal-evidence`)
   claimed the escape generalizes to a **rigid label-free peg without a unit** and to any symmetry `H`
   (e.g. cyclic `C_3`). **It does not.** The escape needs the diagonal `Δ_H` to be *outside* `𝓕(A)`,
   i.e. NOT the automorphism group of any single `O`-tree; the C_3 test only checked support-
   *indecomposability* (a `≥2`-part condition), never the `1`-part case (single-tree `Aut`), which is a
   legitimate `⟦r⟧∘M`-stabilizer (take `⟦r⟧=y`). In fact for the free ternary operad with a
   non-absorbing peg, `Δ_{C_3} = Aut(single tree)` **exactly** — the escape *fails*. Absorption (a
   genuine unit) and **full** symmetry are both essential; the correct hypothesis is not "peg" but
   "fully-symmetric operation + absorbed unit." All boundary claims below are computationally verified.

All computations: `.claude/scratch/verify-general-stabilizer.py`, `verify-boundary2.py`,
`verify-boundary3.py`.

---

## §0. Setup and reduction

Let `O` be a symmetric operad and `M = Ã` its free-algebra monad, where the species is `A = O`
(so `A[n]=O(n)` as an `S_n`-set). Then `M(X)=Σ_n O(n)×_{S_n}X^n` is the set of `O`-trees with
`X`-leaves, and `M∘M = \widetilde{O•O}` (plethysm): elements are two-level `O`-trees — an outer
`O`-operation whose arguments are inner `O`-trees. The monad multiplication `comp : M∘M → M` is
operadic composition (grafting).

**Class 𝒰 (free commutative unital magmas).** `O` satisfies:
- **(FS)** every operation of arity `≥2` is *fully symmetric*: `H_g := Stab(g) = S_{arity(g)}`;
- **(U1)** the only arity-`1` operation is the identity (no unary "colours");
- **(U0)** there is a nullary unit `e∈O(0)` absorbed by every operation
  (`g(x_1,…,x_{i-1},e,x_{i+1},…)=` the composite with that slot deleted); so `a_0=|M∅|≥1`;
- **(NT)** some operation has arity `≥2` (so `M` is non-flat: `H_g=S_{≥2}≠1`, hence non-polynomial).

Members: the free commutative unital magma `U=U_2` (`O=` binary `μ`, `H_μ=S_2`, unit `e`,
`μ(x,e)=x`); the free commutative unital `n`-ary magma `U_n` (`n≥2`); and any fully-symmetric unital
operad with several symmetric generators. Every non-associative member has unbounded wreath depth
`𝔥=∞`, and `a_0=1>0` — the exact regime where Theorems P (`a_0=0`) and S′ (`𝔥<∞`) are both blind.

**Reduction (THM 3 crux, `2026-09-05` §0; `proved`).** Closure of the essential image of `⟦−⟧_M`
under composition, applied to `p=q=Id`, yields the single natural isomorphism `M∘M ≅ ⟦r⟧∘M` for some
polynomial `⟦r⟧`. So it suffices to prove the **contrapositive**:

> **(★).** For `M=Ã` with `O∈𝒰`, `M∘M ≇ ⟦r⟧∘M` for every polynomial functor `⟦r⟧`.

---

## §1. The three inherited tools (proved in `2026-09-07`), and one splitting lemma

Read everything on **each-label-once species components** `[m]` (content `=[m]`, every label once).

> **Lemma E (stabilizer invariant; `2026-09-05` §4.1, `proved`).** A natural iso `F≅G` of analytic
> functors induces, on each component `[m]`, an `S_m`-set iso `F[m]≅G[m]`; hence the multiset of
> point-stabilizer conjugacy classes in `F[m]` is an isomorphism invariant. (Defined even when the
> component is infinite — it reads one subgroup per structure.)

> **Meta-theorem (rigidity of polynomial precomposition; U-corner §1, `proved`).** For a polynomial
> `⟦r⟧=Σ_{s}Set(B_s,−)` and any endofunctor `M`, every point-stabilizer of `(⟦r⟧∘M)[m]` is a
> **block-fixing product** `∏_{β∈π}Stab_M(u_β)` of automorphism groups of single `M`-elements
> `u_β` (single `O`-trees), over the partition `π` of `[m]` into the parts' disjoint supports.
> *(Content: a function is fixed iff fixed pointwise; each-label-once forces disjoint supports.)*

Define the family of **single-tree factors**
```
    𝓕(A) := { support-indecomposable factors of Aut(t) : t a single O-tree, each-label-once } ,
```
where a *support-indecomposable factor* is a part of the (unique, finest) splitting of a permutation
group `G≤Sym(Ω)` into invariant parts `Ω=⊔Ω_i` with `G=∏_iG|_{Ω_i}` (an internal direct product).

> **Lemma 1 (splitting of a disjoint product).** For groups `G_β≤Sym(β)` on pairwise disjoint
> supports, the support-indecomposable factors of `∏_βG_β` are exactly `⋃_β{`factors of `G_β}`.

*Proof.* `{β}` is a splitting of `∏_βG_β` (a direct product over disjoint supports), and each `G_β`
refines into its own finest splitting; no part may merge across two `β`'s, since an element of
`∏_βG_β` supported on `β` fixes every other `β'` — there is no group element correlating distinct
`β`'s. So the finest splitting is the common refinement. ∎

Combining: every stabilizer of `(⟦r⟧∘M)[m]` is `∏_βStab_M(u_β)`, and by Lemma 1 its
support-indecomposable factors all lie in `𝓕(A)`. Contrapositive:

> **(Escape test).** If `(M∘M)[m']` realizes, on some component, a point-stabilizer with a
> support-indecomposable factor `Γ ∉ 𝓕(A)`, then `M∘M ≇ ⟦r⟧∘M` for every polynomial `⟦r⟧`.

*(This is the correct, complete test. The `≥2`-part-partition check of the 09-08 evidence is only the
sub-case where `Γ`'s support has several parts; it misses the `1`-part case `Γ=Stab_M(u)`. See §6.)*

We use it with `Γ = Δ_{C_2} := ⟨(0\,1)(2\,3)⟩`, the correlated double swap.

---

## §2. The witness: `Δ_{C_2}` in `(M∘M)[4]` (the U-corner construction, verbatim)

Every `O∈𝒰` has a **commutative binary operation with unit** `μ`: either a primitive binary `μ`, or
the composite `μ(x,y):=ω(x,y,e,…,e)` of any arity-`n` operation `ω` with `n-2` unit slots — which is
binary, commutative (by (FS): `(1\,2)∈S_n` fixes it), and unital (`μ(x,e)=ω(x,e,e,…,e)=x` by (U0)).

Write `V_i` for the inner leaf on label `i`, and `E'` for the **inner unit element** `e∈M(X)` used as
an **outer leaf**. Crucially, at the *outer* level `E'` is an ordinary (non-unit) generator: only the
*outer* unit is absorbed, so `E'` is a **rigid, label-free peg** that survives outer operations. Form
```
    W_L = μ( V_0, μ(V_2, E') ) ,     W_R = μ( V_1, μ(V_3, E') ) ,     w = μ( W_L, W_R ) ∈ (M∘M)[4].
```

> **Witness Lemma.** `w` has content `{0,1,2,3}` (each label once), and `Aut_{M∘M}(w)=⟨(0\,1)(2\,3)⟩`.

*Proof.* `W_L` is rigid: its two `μ`-children `V_0` (a leaf) and `μ(V_2,E')` (a cherry) are
non-isomorphic, so the outer `μ`'s `S_2` cannot swap them; inside `μ(V_2,E')` the children `V_2` (a
label leaf) and `E'` (the peg, a distinct non-absorbed inner element) are non-isomorphic. Hence
`Aut(W_L)=1`, and likewise `Aut(W_R)=1`; `W_L≅W_R` via `0↦1,\ 2↦3`. The only symmetry of
`w=μ(W_L,W_R)` is the outer swap `W_L↔W_R`, realised on labels by `(0\,1)(2\,3)` (which sends
`V_0↦V_1, V_2↦V_3`, hence `W_L↦W_R`). No single transposition survives (e.g. `(0\,1)` sends `W_L` to
`μ(V_1,μ(V_2,E'))∉\{W_L,W_R\}`). ∎

Verified exactly for `U_3` (`μ` the *composite* `ω(x,y,e)`, `ω` ternary `S_3`) in
`verify-general-stabilizer.py` (B2): `|Aut(w)|=2`, `Aut(w)=⟨(0\,1)(2\,3)⟩`. The construction uses
only `μ` and `e`, so it is a valid `(M∘M)[4]` element for **every** `O∈𝒰`, with the same `Aut`
(adding operations to `O` cannot create isomorphisms between the specific `μ`-trees above).

---

## §3. `(R2)`: no rigid single `O`-tree on `≥2` labels

> **Lemma 2 (R2).** For `O∈𝒰`, every single `O`-tree `t` on `≥2` labels has `Aut(t)≠1`.

*Proof.* Put `t` in normal form; by (U0) the unit is absorbed everywhere, so **no leaf of `t` is a
unit** — every leaf is a label. As `t` has `≥2` labels it has at least one internal node; pick a node
`v` of maximal depth. All children of `v` are leaves (else a deeper node exists), hence all are
**label leaves**. By (U1) `v` is not unary, so `arity(v)≥2` and by (FS) `H_v=S_{arity(v)}`. Any
transposition of two of `v`'s (label) leaf-children lies in `H_v` and is a nontrivial relabelling
fixing `t`. So `Aut(t)≠1`. ∎

Verified for `U_3` (`verify-general-stabilizer.py` B1): the only `2`-label single tree of depth `≤3`
is the cherry `μ(V_0,V_1)` with `Aut=S_2` — zero rigid.

---

## §4. The Escape Lemma (the crux): `Δ_{C_2} ∉ 𝓕(A)`

We first record the shape of `Aut(t)` under full symmetry.

> **Lemma 3 (tree automorphisms are iterated symmetric wreaths).** For `O∈𝒰` and a single `O`-tree
> `t=ρ(c_1,…,c_n)` (root `ρ`, `H_ρ=S_n`), group the children into isomorphism classes
> `K_1,…,K_r` with representative subtrees `s_1,…,s_r` and multiplicities `m_1,…,m_r`. Then
> ```
>     Aut(t) = ∏_{j=1}^{r} ( Aut(s_j) ≀ S_{m_j} ) ,
> ```
> a direct product over classes; and its support-indecomposable factors are exactly the wreaths
> `Aut(s_j)≀S_{m_j}` with `m_j≥2` (each on `m_j·|s_j|` labels), together with the factors of `Aut(s_j)`
> for the classes with `m_j=1` (recursion).

*Proof.* An automorphism of `t` chooses `σ∈H_ρ=S_n` with `c_i≅c_{σ(i)}` — i.e. `σ` preserves the
class partition, so `σ` ranges over the Young subgroup `∏_jS_{m_j}` — together with, for each moved
child, an isomorphism `c_i→c_{σ(i)}`; the isomorphisms of a class-representative to itself are
`Aut(s_j)`. This is precisely `∏_j(Aut(s_j)≀S_{m_j})`. Because `H_ρ=S_n` is the *full* symmetric
group, the Young subgroup is a genuine **direct product** over classes — distinct classes are never
correlated (each class-transposition is independently available). A wreath `Aut(s_j)≀S_{m_j}` with
`m_j≥2` is support-indecomposable (the top `S_{m_j}` mixes the `m_j` copies, so no invariant proper
splitting of their union); Lemma 1 assembles the product; recursion handles `m_j=1`. ∎

> **Escape Lemma.** For `O∈𝒰`, no single `O`-tree `t` has a support-indecomposable factor
> permutation-isomorphic to `Δ_{C_2}=⟨(0\,1)(2\,3)⟩` (a fixed-point-free involution on `4` points).
> Hence `Δ_{C_2}∉𝓕(A)`.

*Proof.* By Lemma 3 every support-indecomposable factor of `Aut(t)` is a wreath `Γ=Aut(s)≀S_m`
(`m≥2`) on `m·ℓ` points, `ℓ=|s|` the number of labels of the class-representative `s`. Suppose `Γ`
is permutation-isomorphic to `Δ_{C_2}`. Permutation-isomorphic groups have equal order and act on the
same number of points, so
```
    |Γ| = |Aut(s)|^m · m! = 2       and       m·ℓ = 4 .
```
`m!·|Aut(s)|^m=2` forces `m=2` and `|Aut(s)|=1` (i.e. `s` **rigid**); then `m·ℓ=4` gives `ℓ=2`. So
`s` is a **rigid single `O`-tree on `2` labels** — contradicting Lemma 2 (R2). Therefore no such `Γ`
exists. ∎

Two independent confirmations at `n=4` (`verify-boundary2.py` D): an **exhaustive** search over all
`25` single `O`-trees on `4` labels (depth `≤4`) for `U_3` finds **none** with a `Δ_{C_2}` factor
(the detector is verified non-vacuous on the abstract group `⟨(0\,1)(2\,3)⟩`); and `comp(w)` — the
graft of the witness — is `μ(μ(V_0,V_2),μ(V_1,V_3))` with `Aut=D_4` (order `8`), the peg having been
**absorbed** on descent to a single tree, gaining the two cherry-swaps that `Δ_{C_2}` lacks.

---

## §5. Theorem and reach

> **Theorem (free commutative unital magma necessity).** Let `O∈𝒰` and `M=Ã`. Then `M∘M≇⟦r⟧∘M`
> for every polynomial `⟦r⟧`; the essential image of `⟦−⟧_M` is not closed under composition. As `M`
> is non-flat (NT) hence non-polynomial, **THM 3 is an unconditional biconditional for every `O∈𝒰`**:
> `M`-containers compose ⟺ `M` polynomial.

*Proof.* Suppose `M∘M≅⟦r⟧∘M`. On component `[4]`, Lemma E makes them realize the same stabilizer
conjugacy classes. The witness `w` (§2) gives a stabilizer `Δ_{C_2}∈(M∘M)[4]`, whose sole
support-indecomposable factor is `Δ_{C_2}`. By the Escape Lemma `Δ_{C_2}∉𝓕(A)`, so by the Escape
test (§1) `Δ_{C_2}` cannot occur as a stabilizer of `(⟦r⟧∘M)[4]`. Contradiction; hence `(★)`. The
reduction (§0) gives the biconditional. ∎

**Reach.** The family `𝒰` contains, for every arity `n≥2`, the free commutative unital `n`-ary
magma `U_n` (`a_0=1`, unbounded wreath depth `𝔥=∞`), plus all multi-generator fully-symmetric unital
operads. The single `C_2` witness dispatches the entire family uniformly — the mechanism never needs
a larger diagonal.

**The residual, updated.** Combining the four proved engines:

| regime | tool | status |
|---|---|---|
| non-analytic, super-poly growth | cardinality law | proved (`2026-09-05` §B) |
| analytic, `a_0=0`, any depth | plethysm cancellation (Thm P) | proved (`2026-09-06`) |
| analytic, bounded wreath depth, any `a_0` | depth invariant (Thm S′) | proved (`2026-09-07`) |
| analytic, `a_0>0`, `𝔥=∞`, **free comm. unital magma** | `C_2` escape (**this file**) | **proved** |
| analytic, `a_0>0`, `𝔥=∞`, **not in `𝒰`** | — | **open** (see §6 for what breaks) |

The residual is now sharpened from "`a_0>0 ∧ 𝔥=∞`" to "`a_0>0 ∧ 𝔥=∞` **and not a free commutative
unital magma monad**." The named inhabitants of the old residual (free commutative unital magmas /
algebras) are exactly `𝒰` — **all closed**. What remains open is the *non*-fully-symmetric part
(cyclic/partial-symmetry operations, pegs without absorption), which §6 shows genuinely needs a
different tool: the `C_2`/diagonal witness provably does **not** reach it.

---

## §6. The boundary: why the peg abstraction fails, and the correction of the 09-08 evidence

The 2026-09-08 `computed` note proposed the hypothesis "**M admits a rigid label-free peg**" (no
unit) and claimed the escape generalizes to any symmetry `H` (with a `C_3` "extend" check). Both the
hypothesis and the check are wrong at the crux. The Escape test requires `Δ_H ∉ 𝓕(A)`; the note's
Task 3 only tested that `Δ` is *support-indecomposable* — its `is_block_fixing_product` explicitly
skips `1`-part partitions (`if len(part) < 2: continue`). But a `1`-part stabilizer is exactly
`Stab_M(u)=Aut(single\ O\text{-tree})`, a legitimate stabilizer of `(⟦r⟧∘M)[m]` (take `⟦r⟧=y`,
giving `M`). So support-indecomposability is **not** escape; one must also rule out that `Δ_H` is a
single-tree `Aut`. It isn't ruled out — indeed it fails:

- **Non-absorbing peg / cyclic symmetry (`verify-general-stabilizer.py` A).** For the free ternary
  operad with `H_ω=C_3` and a **non-absorbing** peg `c`, the *single* `O`-tree
  `t=ω(ω(0,1,c),ω(2,3,c),ω(4,5,c))` has `Aut(t)=⟨(0\,2\,4)(1\,3\,5)⟩=Δ_{C_3}` **exactly** (order 3).
  The cyclic peg pins each inner block rigid *at a single level* (`Aut(ω(0,1,c))=1`), so
  `Δ_{C_3}∈𝓕` and the escape **fails**. Contrast (FS): with `H_ω=S_3` the peg does **not** rigidify
  (`Aut(ω(0,1,c))=S_2`), and with an **absorbed** unit (as in `𝒰`) the block collapses on descent to
  a single tree — which is the whole point.

- **Correlated symmetry, `(R2)` alone insufficient (`verify-boundary3.py`).** An operad whose only
  operation `ρ` has arity `4` and symmetry `H_ρ=⟨(0\,1)(2\,3)⟩` (a correlated double swap, *not* full
  `S_4`, with no individual swaps) gives `Aut(ρ(V_0,V_1,V_2,V_3))=Δ_{C_2}` on four single leaves — so
  `Δ_{C_2}∈𝓕` and the escape **fails**, even though no rigid `≥2`-block need exist. Full symmetry
  (`H_ρ=S_4`) instead gives `Aut=S_4` (order 24), which has no lone-correlated-swap factor.

These pin down the *exact* content of the escape: it needs **(R2)** (no rigid `≥2`-label single tree)
**and** the absence of any operation with a correlated fixed-point-free symmetry — and **full
symmetry `H_g=S_{arity}`** delivers both (a full symmetric group contains every individual
transposition, so no correlated-but-not-individual element survives, and Lemma 3's factors are pure
symmetric wreaths). The honest hypothesis is therefore **"fully-symmetric operations + absorbed
unit,"** not "rigid label-free peg." The `computed` node `general-stabilizer-diagonal-evidence` is
demoted accordingly (its `S_2` control was sound; its `C_3` extension and the peg-without-unit
generalization are refuted). The peg is a **unit** — a nullary element absorbed at one level and
surviving at two — and that two-level asymmetry, not label-free rigidity, is the mechanism.

---

## Grades / registry

| Claim | Grade |
|---|---|
| Reduction; Lemma E; Meta-theorem; composition test | **proved** (inherited, `2026-09-05/07`) |
| Lemma 1 (splitting of disjoint product) | **proved** (elementary) |
| Witness Lemma: `Aut(w)=⟨(01)(23)⟩`, `w∈(M∘M)[4]` | **proved** (structural + brute-forced, `U_3`) |
| Lemma 2 (R2): no rigid `≥2`-label single `O`-tree in `𝒰` | **proved** (deepest-node) + exhaustive `n≤4` |
| Lemma 3 (tree Aut = iterated symmetric wreath) | **proved** (standard; full symmetry ⟹ direct product over classes) |
| **Escape Lemma: `Δ_{C_2}∉𝓕(A)`** | **proved** (order argument) + exhaustive `n=4` search |
| **Theorem: `M∘M≇⟦r⟧∘M` for all `O∈𝒰`** (THM 3 necessity for free comm. unital magmas) | **proved** |
| Correction: peg-without-unit / non-full symmetry escape FAILS | **proved** (explicit single-tree witnesses) |
| General `a_0>0 ∧ 𝔥=∞`, `O∉𝒰` | **open** (different tool required; §6) |

**Provenance cap.** Inherits the P/S′/U cap: the internal argument is proof-complete and
computationally verified, but the ambient "analytic monad ≃ symmetric operad" frame (Joyal 1986 ff.;
Gambino–Kock MPCPS 154 (2013) §1.18–1.21, in-seed for the *correspondence*; the full-faithfulness
clause is cited `agent-summary`) is not fully deep-read. Registry node graded **`computed`**
accordingly; the mathematics above is `proved`-quality modulo that standard import.

## Verification artifacts
- `.claude/scratch/verify-general-stabilizer.py` — Scenario A (C_3/S_3 non-absorbing → `Δ_{C_3}∈𝓕`,
  escape fails); Scenario B (`U_3`: commutative unital composite `μ`, R2 at `2` labels, `Aut(w)=C_2`,
  `comp(w)=D_4`).
- `.claude/scratch/verify-boundary2.py` — exhaustive `n=4` for `U_3`: no `Δ_{C_2}` single-tree factor
  (`Δ_{C_2}∉𝓕`), detector non-vacuous.
- `.claude/scratch/verify-boundary3.py` — correlated-swap operad `⟨(01)(23)⟩` → `Δ_{C_2}∈𝓕` (escape
  fails); full `S_4` → `Aut=S_4` (safe). Shows full symmetry, not merely (R2), is required.

See [[U-corner-closed-stabilizer-per-component]], [[theorem-S-prime-proved-wreath-depth]],
[[plethysm-cancellation-closes-lemmaN]], [[conjecture-V-refuted-unital-magma]].
