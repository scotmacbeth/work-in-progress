# Emergent holonomy = the meeting points of the two factor orbits

**MacBeth — PROVE session, 2026-08-13 (deep-work).**
Upgrades the 448-check computational backbone of `2026-08-12-holonomy-composition-zs-bridge.md`
(parts (b)/(b')) into a clean, fully general structural theorem, and thereby proves *when* the
part-(c') "aligned" hypothesis holds.

> **One line.** For an exact factorisation `G = P·P'` acting on `S`, the emergent holonomy at a point
> `s` — the reentrancy that orchestration synthesises but neither factor possesses — is measured by a
> single geometric integer: **the number of points at which the two factor orbits `P·s` and `P'·s`
> cross.** Precisely, the "dispatch-and-return" loops at `s` are in bijection with the double cosets
> `Stab_P(s)\Stab_G(s)/Stab_{P'}(s)`, and this double-coset space is in canonical bijection with the
> meeting set `(P·s) ∩ (P'·s)`. Alignment (part-(c')'s hypothesis) holds **iff the two orbits meet
> only at `s`.**

This closes the honest gap flagged in the 08-12 file (§4, gap 2): the emergent invariant is now a
single, general, positive integer with a geometric meaning — no abelian, no normality, no subgroup
hypothesis — and it computes as all three of:
```
        h(s)  =  |Stab_P(s) \ Stab_G(s) / Stab_{P'}(s)|                     (double cosets)
              =  |Stab_G(s)| / ( |Stab_P(s)| · |Stab_{P'}(s)| )            (the naive ratio — an integer!)
              =  |(P·s) ∩ (P'·s)|.                                         (meeting points — geometry)
```

---

## 0. Setup and conventions

`G` is a finite group with an **exact factorisation** `G = P·P'`: `P, P' ≤ G` are subgroups such that
every `g ∈ G` is uniquely `g = p·p'` with `p ∈ P`, `p' ∈ P'` (equivalently `P ∩ P' = {e}` and
`|P|·|P'| = |G|`). This is the internal realisation of the Zappa–Szép product `P ⋈ P'` — every ZS
product is such a factorisation and conversely (Brin; Ahman–Uustalu 2013). `G` acts on a finite set `S`
on the **left**, `g·s`; the composite update-monad action of the 08-12 bridge is
`s ↓_⋈ (p,p') = s·(p·p')`, so its isotropy at `s` is `Stab_G(s)` and the two factor isotropies are the
intersections with `P`, `P'`.

Fix `s ∈ S`. Write
```
    U := Stab_G(s),        A := Stab_P(s) = U ∩ P,        B := Stab_{P'}(s) = U ∩ P'.
```

**Lemma 0 (identifications).** `U ∩ P = Stab_P(s)` and `U ∩ P' = Stab_{P'}(s)`.
*Proof.* `p ∈ P` fixes `s` ⟺ `p ∈ Stab_G(s) ∩ P = U ∩ P`; identically for `P'`. ∎

These are the identifications the target theorem's (L2) rests on; they are immediate but load-bearing,
so I state them once.

---

## 1. The disjointness (uniformity) lemma

Everything downstream — that the double cosets are uniform, that the naive ratio is an integer — falls
out of one short, general fact about exact factorisations.

**Lemma 1 (disjointness of `P` from every conjugate of `P'`).** For an exact factorisation `G = P·P'`
and **every** `g ∈ G`,
```
        P ∩ g P' g⁻¹ = {e}.
```

*Proof.* Let `a ∈ P ∩ gP'g⁻¹`, say `a = g p'' g⁻¹` with `p'' ∈ P'`. Factor `g = p p'` (`p ∈ P`,
`p' ∈ P'`), so `g⁻¹ = p'⁻¹ p⁻¹` and
```
    p⁻¹ a p  =  p⁻¹ (p p')·p''·(p'⁻¹ p⁻¹) p  =  p'·p''·p'⁻¹.
```
The right-hand side lies in `P'` (all three of `p', p'', p'⁻¹` do). The left-hand side lies in `P`
(all three of `p⁻¹, a, p` do). Hence `p⁻¹ a p ∈ P ∩ P' = {e}`, so `a = e`. ∎

Note the proof uses *only* that `P, P'` are subgroups with `P ∩ P' = {e}` and that `g` factors as
`p p'` — nothing about the action or the point `s`. In particular it applies to the sub-conjugation we
need:

**Corollary 1.1.** For every `g ∈ U`, `A ∩ g B g⁻¹ = {e}` (since `A ⊆ P`, `B ⊆ P'`). Consequently the
double coset `A g B` has cardinality
```
    |A g B| = |A|·|B| / |A ∩ g B g⁻¹| = |A|·|B|      for every g ∈ U.
```
*(The middle equality is the standard double-coset size formula.)* Every `(A,B)`-double coset in `U`
has exactly `|A|·|B|` elements. **The naive ratio `|U| / (|A|·|B|)` is therefore a positive integer**,
equal to the number of double cosets `|A\U/B|`.

*Verification.* `P ∩ gP'g⁻¹ = {e}` was checked for **all** `g ∈ G` across every exact factorisation of
`S₃, S₄, A₄, D₄, D₆, A₅` — 41 064 checks, 0 violations (`zs_holonomy_L3.py`).

---

## 2. (L1) Containment and (L2) the alignment criterion

**Proposition 2 (L1, containment).** `A·B ⊆ U` as subsets of `G`.
*Proof.* For `a ∈ A`, `b ∈ B`: `(ab)·s = a·(b·s) = a·s = s`. ∎

**Proposition 3 (L2, alignment criterion).** The following are equivalent:
1. `U = A·B` (the set product fills the stabiliser);
2. `U` is **ZS-compatible**: `U = (U ∩ P)·(U ∩ P')`;
3. the exact factorisation `G = P·P'` **restricts** to an exact factorisation `U = A·B` of `U` — i.e.
   every `s`-fixing `g = p p'` has *both* legs `s`-fixing (`p ∈ A` and `p' ∈ B`).

*Proof.* (1)⟺(2) is Lemma 0 (`U ∩ P = A`, `U ∩ P' = B`), so these are literally the same equation.
For (1)⟹(3): if `U = A·B` then by Corollary 1.1 `|A·B| = |A|·|B|`, and since `A ∩ B ⊆ P ∩ P' = {e}`
the product map `A × B → A·B` is a bijection; as `A·B = U` is a group of order `|A||B|` with `A, B`
subgroups intersecting trivially and `AB = U`, this *is* an internal exact factorisation of `U`.
For the "both legs fix `s`" phrasing: `g = p p' ∈ U`; its unique global factorisation must, by
uniqueness of factorisation in `G` and `U = A·B`, coincide with a factorisation `a·b` (`a∈A, b∈B`),
whence `p = a ∈ A`, `p' = b ∈ B`. (3)⟹(1) is immediate. ∎

So (L2) is near-definitional *once Lemma 0 is in hand* — as the target file anticipated. The value is in
the next section, and in the observation just made: **alignment automatically upgrades the set product
`A·B` to a subgroup** (namely all of `U`). Off alignment, `A·B` is a proper subset of `U` of size
`|A||B|`, and it need not be a subgroup.

---

## 3. (L3) The main theorem: emergent holonomy = meeting points

The content is a canonical bijection between the "dispatch-and-return loops" at `s` and the crossing
points of the two factor orbits.

**Definition (intermediate point).** For `g ∈ U` with unique factorisation `g = p p'`, define
```
    int(g) := p'·s  ∈ S.
```
Interpretation: `g·s = s` reads `p·(p'·s) = s`, i.e. the loop `s ─p'→ t ─p→ s` with waypoint
`t = int(g) = p'·s`. The loop is "aligned" (both legs individually fix `s`) iff `t = s`.

**Lemma 4 (image lands in the meeting set).** `int(g) ∈ M := (P·s) ∩ (P'·s)` for all `g ∈ U`.
*Proof.* `int(g) = p'·s ∈ P'·s`; and from `p·(p'·s) = s` we get `p'·s = p⁻¹·s ∈ P·s`. ∎

**Lemma 5 (constant on double cosets).** For `a ∈ A`, `b ∈ B`, `g ∈ U`: `int(a g b) = int(g)`.
*Proof.* Write `g = p p'`. Then `a g b = (ap)(p'b)` with `ap ∈ P`, `p'b ∈ P'`, so this *is* the unique
factorisation of `agb`, and `int(agb) = (p'b)·s = p'·(b·s) = p'·s = int(g)`, using `b·s = s`. ∎

Thus `int` descends to a well-defined map `int̄ : A\U/B → M`.

**Theorem 6 (the bijection).** `int̄ : A\U/B → M = (P·s) ∩ (P'·s)` is a bijection.

*Proof.* **Surjectivity.** Let `t ∈ M`, so `t = r·s` with `r ∈ P` and `t = q'·s` with `q' ∈ P'`. Put
`g := r⁻¹ q'` (its unique factorisation, since `r⁻¹ ∈ P`, `q' ∈ P'`). Then
`g·s = r⁻¹·(q'·s) = r⁻¹·t = r⁻¹·(r·s) = s`, so `g ∈ U`, and `int(g) = q'·s = t`.

**Injectivity.** Suppose `int(g₁) = int(g₂) = t`, `g_i = p_i p_i'`. From `p_1'·s = p_2'·s` we get
`p_2'⁻¹ p_1' ∈ Stab_G(s) ∩ P' = B`, so `p_1' = p_2' b` for some `b ∈ B`. Then
```
    g₁ b⁻¹ = p_1 p_1' b⁻¹ = p_1 p_2'        (unique factorisation: p_1 ∈ P, p_2' ∈ P').
```
Both `g₁ b⁻¹` and `g₂ = p_2 p_2'` lie in `U` (as `b ∈ B ⊆ U`), so
```
    g₁ b⁻¹ g₂⁻¹ = (p_1 p_2')(p_2 p_2')⁻¹ = p_1 p_2'·p_2'⁻¹ p_2⁻¹ = p_1 p_2⁻¹ ∈ U ∩ P = A.
```
Call it `a := p_1 p_2⁻¹ ∈ A`. Then `g₁ b⁻¹ = a g₂`, i.e. `g₁ = a g₂ b ∈ A g₂ B`. Hence
`A g₁ B = A g₂ B`. ∎

**Corollary 7 (the emergent-holonomy invariant).** Define `h(s) := |A\U/B|`. Then
```
    h(s) = |Stab_G(s)| / (|Stab_P(s)|·|Stab_{P'}(s)|)   =   |(P·s) ∩ (P'·s)|,
```
a positive integer. The first equality is Corollary 1.1 (all double cosets have size `|A||B|`, so their
number is `|U|/(|A||B|)`); the second is Theorem 6. Moreover:
```
    h(s) = 1   ⟺   M = {s}   ⟺   U = A·B   ⟺   s is aligned (Prop. 3).
```
*Proof of the equivalences.* `h(s) = 1` ⟺ a single double coset ⟺ `A·e·B = U` ⟺ `U = A·B`; and
`h(s) = |M| = 1` with `s ∈ M` forces `M = {s}`. ∎

*Verification.* Theorem 6, Corollary 7, and Prop. 3's biconditional were checked with **0 mismatches**
across `S₃, S₄, A₄, D₄, ℤ/2×ℤ/2, D₆, A₅` and an `S₃`-with-fixed-points action — 2594 point-checks over
all their exact factorisations, confirming `|A\U/B| = |M|`, `image(int) = M`, `int` constant on double
cosets, and `aligned ⟺ |M| = 1 ⟺ M = {s}` (`zs_holonomy_L3.py`).

### 3.1 Reading the theorem

- **The waypoint is the whole story.** Every `s`-fixing composite move is a two-step loop
  `s ─(P′-leg)→ t ─(P-leg)→ s`. It is a *genuine* orchestration artefact — reentrancy neither factor
  possesses — exactly when the waypoint `t` is a crossing point of the two orbits *other than* `s`.
  The `S₃` witness (`P = A₃`, `P' = ⟨(12)⟩`, `s = 1`): `P·1 = {1,2,3}`, `P'·1 = {1,2}`, so `M = {1,2}`,
  `h(1) = 2`. The non-identity loop is `1 ─(12)→ 2 ─(132)→ 1`; its waypoint is `2 ≠ 1`, and neither
  `(12)` nor `(132)` fixes `1`. Both factor holonomies are trivial (`A = B = {e}`); the composite
  holonomy is `C₂`. The surplus meeting point *is* the emergent generator.

- **`h(s) − 1` counts the emergent loops up to the factor symmetries.** The single aligned double coset
  `A·e·B` (waypoint `s`) is the "honest" part where both legs fix `s`; the other `h(s) − 1` double
  cosets are the emergent reentrant loops, each pinned to a distinct extra crossing point of the two
  orbits.

- **Why the naive ratio is honest here.** The target file (`state/PROVE.md`) proposed
  `|Stab_G(s)|/(|Stab_P(s)||Stab_{P'}(s)|)` as the invariant. A priori that is the cardinality of a
  *subset* divided by a subgroup size and need not be an integer. Lemma 1 rescues it: the disjointness
  `A ∩ gBg⁻¹ = {e}` forces every double coset to have the uniform size `|A||B|`, so the ratio is exactly
  the (integer) double-coset count. The geometric identity `= |M|` is the payoff.

---

## 4. Connection to part (c'): when the `[ω] ∈ H²` analysis applies

Part (c') of the 08-12 bridge analysed the *aligned* regime — where the composite isotropy `E := U`
is an extension `1 → A → E → B → 1` and a degree-2 class `[ω] ∈ H²(B;A)` decides whether the composite
holonomy splits as an *unentangled* product of the two factor holonomies. That analysis was stated
under the hypothesis "containment (b') is an equality." Corollary 7 turns that hypothesis into a proved,
checkable, geometric condition:

> **The part-(c') hypothesis holds at `s` iff `h(s) = 1`, i.e. iff the two factor orbits `P·s` and
> `P'·s` meet only at `s`.** In that case (Prop. 3) `U = A·B` is automatically an internal exact
> factorisation `U = A ⋈ B` — a genuine Zappa–Szép sub-product of the vertex group by its two factor
> isotropies — so the extension `1 → A → E → B → 1` and its class `[ω] ∈ H²(B;A)` are well-defined and
> the (c') dichotomy runs. When `h(s) > 1` the vertex group is strictly larger than any ZS product of
> the factor isotropies; there is no single `[ω]` splitting it into `A` and `B`, and the invariant is
> the full meeting set `M` (equivalently the double-coset space `A\U/B`), not a class in `H²(B;A)`.

This is exactly the honest boundary the guardrails demanded: alignment ⟹ no emergent holonomy ⟹
`H²`-extension analysis applies; misalignment ⟹ the emergent holonomy is the surplus meeting points,
and its invariant is combinatorial (a double-coset space), not (in general) a single cohomology class.
The two descriptions agree on their overlap: `h(s) = 1` ⟺ single double coset ⟺ `E = A ⋈ B` with the
trivial extension being the aligned baseline.

**Aligned-abelian consistency.** In the `ℤ/2` reentrancy witness (`A = B = ℤ/2`, trivial action,
`H²(ℤ/2;ℤ/2) ≅ 𝔽₂`), alignment holds (`h = 1`, single meeting point) at the relevant `s`, `E = U` is
`ℤ/2×ℤ/2` or `ℤ/4` according to `[ω] ∈ {0, ε}`, and Corollary 7 gives `|U| = |A||B| = 4`,
consistent with a single double coset. The (c') entanglement dichotomy is orthogonal to `h`: it lives
*inside* the aligned fibre `h = 1`, deciding the internal structure of the one double coset, whereas
`h > 1` detects emergence *before* any extension class is even defined. Two distinct invariants at two
distinct places, cleanly separated by `h(s) = 1`.

---

## 5. Status ledger (honesty)

**Proved (this file), fully general — any finite exact factorisation, any action, any point `s`:**
- **Lemma 1** `P ∩ gP'g⁻¹ = {e}` (∀ `g ∈ G`) — 3-line proof, no action/point used; verified 41 064
  checks, 0 violations. ⟹ all `(A,B)`-double cosets in `U` have size `|A||B|`; the naive ratio is an
  integer.
- **(L1)** `A·B ⊆ U` (one line).
- **(L2)** alignment `U = A·B` ⟺ ZS-compatibility of `U` ⟺ the factorisation restricts to `U`
  (near-definitional via Lemma 0; plus: alignment ⟹ `A·B` is the subgroup `U`).
- **(L3) Theorem 6** the intermediate-point map induces a bijection
  `A\U/B ≅ (P·s) ∩ (P'·s)`; **Corollary 7**
  `h(s) = |A\U/B| = |U|/(|A||B|) = |(P·s)∩(P'·s)|`, with `h(s) = 1 ⟺` aligned. Verified 2594
  point-checks over 9 groups incl. `A₅`, 0 mismatches.
- **§4** the part-(c') "aligned" hypothesis `⟺ h(s) = 1 ⟺` the factor orbits cross only at `s` — this
  proves *when* the `[ω] ∈ H²(B;A)` analysis applies, resolving the 08-12 file's gap 2.

**Scope / not claimed:**
1. **Degree-1, proof-relevant polynomial liftings** — the classification this feeds
   (`Upd` liftings ≅ `Fun(𝔸(↓),Cat)`) is degree-1; higher/branching liftings untouched. Inherited scope,
   unchanged.
2. **The `[ω] ∈ H²` refinement of the aligned fibre** stays in the abelian-normal regime of the 08-12
   file (heeding `g-obstruction-is-h2-class`: no nonabelian ZS obstruction claimed). What is *new and
   general* here is `h(s)` and its geometric meaning, which needs no such hypothesis.
3. **Finite** throughout (orbit-stabiliser counting). The bijection Theorem 6 is set-theoretic and would
   survive infinitely, but the cardinality identities in Corollary 7 are finite statements.

**Grant framing.** The emergent holonomy of unprotected orchestration now has a one-number diagnostic
with an operational reading: *count the states where the two agents' reachable-state orbits cross.*
`h(s) = 1` everywhere ⟺ the composite is holonomy-clean at every state (and only then does the
cohomological entanglement question even arise); `h(s) > 1` localises exactly which states carry
synthesised reentrancy and how much. A supply-chain / smart-contract auditor can compute `h` directly
from the two agents' state actions — no cohomology required to *detect* emergence, only to classify the
aligned case.
