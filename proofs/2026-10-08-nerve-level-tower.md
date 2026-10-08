# The nerve-level tower: composition is a nerve-level-2 datum (cohomological degree ONE)

**Date:** 2026-10-08
**Author:** MacBeth
**Status:** proved (with one honestly-flagged open question and one cited input)
**Context:** Referee-driven correction (Rick, UID 209; findings E1/W3/W7) of the shipped synthesis note
*"Composition is a degree-two datum"* (commit ae9d67a). Feeds the WRITE re-cut this heartbeat; built
for Neil's Strathclyde mini-course (Oct 13–16).

---

## 0. The problem and the error being corrected

The note *"Composition is a degree-two datum"* claimed: **no cohomological invariant below degree two
can detect composition.** This is FALSE. Its own degree-one invariant separates `ℤ/2` from the
two-element monoid `{1,e}` (`e²=e`). The root cause (Rick E1, W3) is a conflation of two distinct
simplicial indices attached to a cohomology class. This note isolates those indices, proves the
correct regrade, and rebuilds the tower honestly.

**Convention.** `C` is a small category; equivalently a directed container, equivalently a polynomial
comonoid. Its **nerve** `N(C)` is the simplicial set with
- `N_0` = objects,
- `N_1` = arrows,
- `N_k` = composable `k`-tuples (strings `a_0 →^{f_1} a_1 → ⋯ →^{f_k} a_k`),

with face maps `d_i : N_k → N_{k-1}` (the inner faces compose adjacent arrows; `d_1 : N_2 → N_1` is
composition `(f,g) ↦ g∘f`) and degeneracies `s_i` (inserting identities). For an abelian coefficient
system `A` (a functor `C → Ab`; constant unless noted), `H^n(C;A)` is the cohomology of the
**normalized bar/cochain complex**
```
    C^n(C;A) = { functions on the nondegenerate n-simplices N_n },
    (d^n c)(f_1,…,f_{n+1}) = f_1·c(f_2,…,f_{n+1})
        + Σ_{i=1}^{n} (−1)^i c(…, f_{i+1}∘f_i, …) + (−1)^{n+1} c(f_1,…,f_n).
```
This is the standard cohomology of `C` (= cohomology of the classifying space `BC = |N(C)|`); for a
one-object category (a monoid/group) it is monoid/group cohomology.

**Two truncations.** Write `tr_k N(C)` for the `k`-truncated nerve: the sets `N_0,…,N_k` together
with all face and degeneracy maps among them. `tr_1 N(C)` is exactly the **underlying reflexive
graph** of `C` (objects, arrows, source, target, identities) — equivalently the image of `C` under
the forgetful functor `U : Cat → Poly` (positions-and-directions). `tr_2 N(C)` adds the composition
map `d_1 : N_2 → N_1`.

---

## 1. The regrade lemma — the heart of the correction

Every cohomology class carries **two** simplicial indices, which the old slogan fused into one:

> **(cochain level)** an `n`-cochain is a function on `N_n` — its data lives at simplicial level `n`;
>
> **(cocycle-condition level)** the cocycle condition `d^n c = 0` is a system of equations indexed by
> `N_{n+1}` — the constraint is tested at simplicial level `n+1`.

**Lemma 1 (Regrade).** *For every `n ≥ 0`: the cocycle condition defining an `H^n`-class is a
condition read on `N_{n+1}`. Consequently the cohomological degree `n` equals the cocycle-condition
simplicial level minus one:*
```
            cohomological degree  =  (nerve level of the cocycle condition) − 1.
```

*Proof.* `d^n : C^n → C^{n+1}` sends a function on `N_n` to a function on `N_{n+1}`, by the displayed
formula: `(d^n c)(f_1,…,f_{n+1})` is an alternating sum of `c` evaluated on the `n`-faces of the
`(n+1)`-simplex `(f_1,…,f_{n+1}) ∈ N_{n+1}`, together with the coefficient action along `f_1`. The
cocycle condition `d^n c = 0` is therefore the family of equations `{(d^n c)(σ) = 0 : σ ∈ N_{n+1}}`,
indexed precisely by `N_{n+1}`. The coboundary relation `c ∼ c + d^{n-1}b` reads `N_n` (lower), so the
*binding* simplicial level — the highest one that enters the definition of the class — is `N_{n+1}`. ∎

**Reading off the degrees (the table the old note needed):**

| degree `n` | cochain on | cocycle condition on | the structural datum it reads |
|:---:|:---:|:---:|:---|
| 0 (`H^0`, out-degree-type, `U`-blind) | `N_0` objects | `N_1` arrows | the reflexive graph; constancy along arrows |
| **1** (`H^1`, δ-translation, inventory `[θ_R]`) | `N_1` arrows | **`N_2` composable PAIRS** | **composition as a binary operation** |
| 2 (`H^2`, weld `[ω]`, ZS obstruction) | `N_2` pairs | `N_3` composable TRIPLES | associativity coherence |

**Corollary 1.1 (the slogan, corrected).** *Composition — the datum of composable pairs — is the
`N_2` level of the nerve. By Lemma 1, `N_2` is the cocycle-condition level of cohomological degree
`ONE`. Hence the first cohomological degree at which composition can be read is degree 1, not degree
2.* The old "2" was the simplicial level `N_2` of the two-fold composite `p◁p`, mislabelled as
cohomological degree 2. (This is Rick W3 verbatim: "the 2 of `p◁p` is simplicial level 2, not
cohomological degree 2.")

---

## 2. Rung 1 ⊊ Rung 2 is strict: detection of composition begins at nerve level 2 (degree 1)

**Notation for invariants.** For `k ≥ 0` let `F_k` be the set of isomorphism-invariants of small
categories that *factor through the `k`-truncated nerve*: `I ∈ F_k` iff `tr_k N(C) ≅ tr_k N(C')`
implies `I(C) = I(C')`. Truncation retains more information at higher `k`, so trivially
`F_0 ⊆ F_1 ⊆ F_2 ⊆ ⋯`. `F_1` is exactly the invariants factoring through `U` (the reflexive graph) —
out-degree, position/direction counts, tangent-regularity. These are the "composition-blind"
invariants.

**Theorem 2 (strict `F_1 ⊊ F_2`).** *There are two small categories with isomorphic `tr_1` nerves
(hence agreeing on every `F_1`-invariant, in particular on out-degree) but a nerve-level-2 invariant
— namely `dim_{𝔽₂} H^1(−;𝔽₂)` — that distinguishes them. Hence detection of composition begins at
nerve level 2 = cohomological degree 1.*

*Witnesses.* The two one-object categories on arrow-set `{1,a}` (`1` the identity):
`M₁ = ℤ/2` with `a·a = 1`, and `M₂ = {1,e}` with `a·a = a` (`e := a` idempotent).

*Step 1 — `tr_1` agree.* Each has one object, arrow set `{1,a}`, source = target = the unique object,
identity loop `1`. The relabelling `1↦1, a↦a` is an isomorphism of reflexive graphs. So `M₁, M₂` agree
on every `F_1`-invariant. Concretely as polynomial comonoids `U(M₁) = U(M₂) = y²` (one position, two
directions): out-degree is **blind**.

*Step 2 — `tr_2` differ.* The only nondegenerate composable pair is `(a,a)`, with inner face
`d_1(a,a) = a·a`: it is `1` in `M₁`, `a` in `M₂`. Any isomorphism of `tr_2` nerves must send `a↦a` on
`N_1` (it fixes `1`), hence `(a,a)↦(a,a)` on `N_2`, hence must carry `d_1(a,a)=1` to `d_1(a,a)=a` — but
`1 ≠ a`. So no isomorphism of `tr_2` nerves exists.

*Step 3 — a nerve-level-2 invariant separates them.* Compute `H^1(−;𝔽₂)` from the normalized complex.
For `M₂ = {1,e}`: the only normalized 1-cochain is `c(e) = t ∈ 𝔽₂`; its coboundary on the pair `(e,e)`
is `(d^1 c)(e,e) = c(e) − c(e·e) + c(e) = c(e) − c(e) + c(e) = c(e)`, so the cocycle condition forces
`t = 0`; `Z^1 = 0`, hence `H^1(M₂;𝔽₂) = 0`. For `M₁ = ℤ/2`: `(d^1 c)(a,a) = c(a) − c(a·a) + c(a) =
2c(a) − c(1) = 0` over `𝔽₂` (normalized `c(1)=0`), so every `c(a) ∈ 𝔽₂` is a cocycle; coboundaries
vanish (trivial action), giving `H^1(M₁;𝔽₂) = 𝔽₂`. Thus `dim H^1(−;𝔽₂) = 1 ≠ 0`. This invariant is
by construction a function of `tr_2` (the coboundary uses `d_1`) and not of `tr_1` (Step 1), so it
lies in `F_2 ∖ F_1`. ∎

*Structural confirmation.* `M₂` has a two-sided zero: `e·x = e = x·e` for all `x` (`e·1=e`, `e·e=e`).
A monoid with a two-sided zero has contractible classifying space — the element `e` is a natural
transformation from the constant endofunctor to the identity of `𝐁M₂` (naturality `e·f = e = f·e`),
giving a homotopy `id ≃ const`. Hence `H̃^*(M₂; A) = 0` for all trivial `A`, in particular
`H^{≥1}(M₂;𝔽₂)=0`. (Computed: `H̃_1 = H̃_2 = 0`; whereas `N(ℤ/2) = ℝP^∞`, `H_1 = ℤ/2`.)

**Remark 2.1 (why DEGREE is the wrong grade — the coefficient test).** The *degree* at which this
single `N_2` distinction surfaces depends on the coefficients:

| coefficients | `H^1` separates? | `H^2` separates? |
|:--|:--:|:--:|
| `𝔽₂` | **YES** (1 vs 0) | yes (1 vs 0) |
| `ℤ`  | no (0 vs 0) | **YES** (`ℤ/2` vs 0) |

The underlying feature is coefficient-independent: `a·a = 1` creates a 1-cycle, `H_1(ℤ/2) = ℤ/2`,
living at nerve level `N_2`. The universal-coefficient / Bockstein machinery moves this `ℤ/2` of
torsion between cohomological degree 1 (with `𝔽₂`) and degree 2 (with `ℤ`). So "which degree detects
composition here" has no coefficient-free answer — but "which **nerve level**" always does: `N_2`.
*This is the thesis in one example: nerve level is the invariant grade; cohomological degree is a
coefficient-dependent shadow of it.* It also shows the old "degree two" was not even wrong-but-stable:
over `𝔽₂` the detection is degree one.

---

## 3. The truncation tower COLLAPSES at level 2 — there is no third truncation rung

The naive reading of a "three-rung nerve-level tower" asks for a strict `F_2 ⊊ F_3`. There is none.

**Theorem 3 (2-coskeletal collapse).** *For isomorphism-invariants of a small category,
`F_2 = F_3 = ⋯ =` (all isomorphism-invariants). Equivalently: a small category is determined, up to
isomorphism, by its 2-truncated nerve.*

*Proof.* From `tr_2 N(C)` recover: objects `= N_0`; arrows `= N_1`; source and target `= d_1, d_0 :
N_1 → N_0`; identities `= s_0 : N_0 → N_1`; composition `= d_1 : N_2 → N_1` (and `N_2` is the set of
composable pairs, i.e. the pullback `N_1 ×_{N_0} N_1`, forced by the face maps). These are *all* the
data of a category. An isomorphism `tr_2 N(C) ≅ tr_2 N(C')` of truncated simplicial sets is exactly a
bijection on objects and arrows commuting with source, target, identity and composition — i.e. an
isomorphism of categories `C ≅ C'`. Hence any isomorphism-invariant is determined by `tr_2 N(C)`:
`F_2 =` everything. Since `F_2 ⊆ F_3 ⊆ ⋯ ⊆` everything, all are equal. ∎

**Corollary 3.1.** PROVE.md's proposed third rung — a strict `N_2 ⊊ N_3` separation of
*fixed-category invariants by truncation* — **does not exist.** The nerve of a category is
2-coskeletal (`N_k`, `k≥3`, is forced by `tr_2` via the Segal condition), so no invariant of a
category needs `N_3`. "Nerve level = truncation level" is a genuine grade only up to level 2.

**The reconciliation with Lemma 1.** For a category, `H^n` is determined by `tr_{min(n+1,2)}`: its
cocycle condition reads `N_{n+1}`, but for `n ≥ 1` that `N_{n+1}` is itself forced by `tr_2`. So:
- the **truncation level** (Notion A) of `H^n` is `min(n+1, 2)` — it **collapses** to 2 for all `n≥1`;
- the **cocycle-condition level** (Notion B, Lemma 1) of `H^n` is `n+1` — it **never collapses**.

The old slogan's "2" is *neither* of these correctly applied. It took the simplicial level `N_2` of
composition (right object) and read it as cohomological degree 2 (`H^2`, wrong), when `N_2` is the
condition-level of degree **1**.

---

## 4. The genuine strict `N_2 ⊊ N_3`: associativity is a triple-level condition, not a pair-level one

Theorem 3 says the third rung is not a truncation separation of *fixed* categories. The third rung is
real, but it lives in the **assembly/obstruction** problem — grading the obstruction to *building* a
category — where the object varies and 2-coskeletal collapse does not apply.

**Definition.** A **unital magmoid** is a reflexive graph equipped with a unital composition on
composable pairs (`tr_2`-level Segal data: a chosen filler `d_1 : N_2 → N_1` of every inner horn,
with the degeneracies as two-sided units) — but with **no associativity assumed**. Categories are
exactly the associative unital magmoids. Associativity is the equation `(h∘g)∘f = h∘(g∘f)` indexed by
composable **triples** `N_3`.

**Theorem 4 (associativity is an `N_3`-predicate, strictly above `N_2`).** *The predicate "is
associative" on unital magmoids is a condition on `N_3` that is not expressible on `tr_2` data alone:
there is a unital magmoid whose full `N_2` composition is defined and unital, yet which is not
associative. Hence the datum "does this `N_2`-composition assemble to a category?" genuinely lives at
nerve level 3, one above where composition itself (`N_2`) lives.*

*Elementary self-contained witness.* On `{1, x, y}` with `1` the two-sided unit, define
```
        x·x = y,     x·y = x,     y·x = y,     y·y = y   (any unital completion).
```
This is a unital magma (the unit laws hold by construction). But
```
        (x·x)·x = y·x = y,        x·(x·x) = x·y = x,       and  y ≠ x.
```
So the triple `(x,x,x) ∈ N_3` witnesses non-associativity. Every `N_2` datum (the full table) is
present and unital; the obstruction is purely at `N_3`. ∎

**The cohomological refinement (the on-brand `[ω] ∈ H^2`).** When the unital magmoid arises as a
**weld** (a Zappa–Szép / matched-pair assembly of two subcategories `C, D`, every arrow factoring as
`c∘d`), the associativity obstruction is a 2-cochain on composable pairs whose cocycle condition is
the `N_3` associativity equation — i.e. precisely a class
```
        [ω] ∈ H^2,        [ω] = 0  ⟺  the weld is associative (a category).
```
By Lemma 1 this `H^2` class is exactly a degree-2 = `N_3`-condition datum, consistent with the table
in §1. This is the proved two-level Zappa–Szép criterion
`K = C ⋈ D ⟺ (L) ∧ (G)`, where `(L)` is a pair-level (`N_2`) existence/compatibility condition on the
matched actions and `(G) ⟺ [ω] = 0` is the triple-level (`N_3`) associativity condition
[registry: `pairwise-zs`, `groupoid-zs-obstruction` — (G)⟺[ω]=0; memory
`g-obstruction-is-h2-class`, `zs-criterion-is-two-level`, both *proved*].

**Strictness of the assembly rung.** The separation `N_2 ⊊ N_3` is strict because there is welding
data satisfying the pair-level `(L)` yet with `[ω] ≠ 0`: the re-entrancy witness `[ω] = ε ≠ 0` in
`H^2 ≅ 𝔽₂` [`lean-reentrancy-omega-equals-epsilon`, **lean-verified**] is a well-defined `N_2`
composition that fails `N_3` associativity. The elementary magma above is its coefficient-free shadow.

---

## 5. The honest tower (synthesis)

Two gradings, agreeing at the bottom, diverging above:

```
   nerve level        1                    2                          3
   (cocycle cond.)   N_1                  N_2                        N_3
   coh. degree        0                    1                          2         (degree = level − 1)
   ───────────────────────────────────────────────────────────────────────────────────────────
   invariant        U(p), out-degree   H^1, δ-translations,       H^2 weld [ω],
                     H^0                 inventory [θ_R]            ZS obstruction (G)
   reads             reflexive graph    COMPOSITION (pairs)        ASSOCIATIVITY (triples)
   ───────────────────────────────────────────────────────────────────────────────────────────
   fixed-C truncation:   F_1    ⊊    F_2  =  F_3  =  ⋯   (collapse, Thm 3)
   assembly/obstruction: graph  ⊊   (L) pairs  ⊊  (G) triples   (strict, Thm 4)
```

- **Strict and proved:** `N_1 ⊊ N_2` for fixed-category invariants (Thm 2): composition is first
  detectable at **nerve level 2 = degree 1**, refuting "degree two."
- **Collapse, proved:** the truncation tower stops at 2 (Thm 3); a category *is* its `tr_2` nerve.
  There is no third *truncation* rung.
- **Strict and proved, in the assembly problem:** `N_2 ⊊ N_3` as the pair-level (composition exists)
  vs triple-level (it is associative) distinction (Thm 4); the degree-2 class `[ω] ∈ H^2` reads the
  `N_3` condition.
- **Independence (not a detection order), proved:** `[θ_R] ∈ H^1` and `[ω] ∈ H^2` are independent —
  neither determines the other and no natural family of homomorphisms carries either class to the
  other [the note's Thm 4; supply-chain witnesses W1/W2, registry `supply-chain-zs`, *proved*;
  memory `supply-chain-inventory-h1-vs-weld-h2`]. They are two independent cohomological anchors in
  the composition-sensitive band, differing in **coefficients and condition-level**, not in *whether*
  they see composition.

**OPEN (flagged, per Rick).** Does cohomological *degree* stratify *detection power* above degree 0?
As a detection statement this is open and the naive form ("higher degree detects strictly more") is
**false as stated**: §2 gives a degree-1 invariant (over `𝔽₂`) detecting composition, and `H^1`/`H^2`
are independent (not ordered). The honest claim is the *condition-level* strictness of Thm 4, not a
detection-power tower.

---

## 6. Verification

- **Lemma 1:** the coboundary degree-count is the definition of the normalized bar complex; the
  indexing of `d^n c = 0` by `N_{n+1}` is immediate from the formula. GREEN.
- **Theorem 2:** `tr_1` iso (relabel), `tr_2` non-iso (fixed-point argument on `d_1(a,a)`), and the
  `H^1` computation are all finite and checked by hand *and* by the agent script
  `scratch/nerve-level-tower-verify.py` (`𝔽₂`: `(1,1,1)` vs `(1,0,0)`; `ℤ`: `H^2 = ℤ/2` vs `0`;
  reduced homology of `N({1,e})` vanishes). GREEN.
- **Theorem 3:** reconstruction of `C` from `tr_2 N(C)` is the standard 2-coskeletality of nerves of
  categories; the invariance argument is a one-line consequence. GREEN.
- **Theorem 4:** the 3-element unital non-associative magma is checked by hand on `(x,x,x)`. The
  `[ω] ∈ H^2` refinement cites proved/lean-verified registry nodes, not re-proved here (role: cited
  input). GREEN for the elementary statement; the cohomological refinement is CITED.
- **Boundary cases:** terminal category (`*`): all three rungs trivial (one object, one arrow,
  `H^{≥1}=0`); consistent. The degenerate `tr_0` level (objects only) sits below rung 1 and is blind
  to arrows, as expected.

## 7. Gaps / scope

- The strict `N_2 ⊊ N_3` is proved as a **condition-level / assembly** separation (Thm 4), NOT as a
  detection-power separation of fixed-category invariants (which §3 shows cannot be a truncation
  separation, and §5-OPEN shows is open/false as a degree-detection claim). This scoping is the
  substance of the correction and must survive into the WRITE.
- "Composition is a degree-two datum" is **retired**. Replacement slogan, proved:
  **"Composition is a nerve-level-two datum — cohomological degree one; associativity is the
  nerve-level-three datum, cohomological degree two."**
```
