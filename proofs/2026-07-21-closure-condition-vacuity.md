# Is "convolutional" strictly stronger than "left-closed"? (closure-condition vacuity)

MacBeth — 2026-07-21. Deep-work session.

**Status.** *Not fully resolved — but sharply reduced and heavily constrained, with rigorous
refutations of every natural counterexample.* Honest verdict: **strong evidence the condition
is vacuous** (every Day-convolutional tensor on `Cont` is left closed), with the residue
isolated to a single clean statement about `Set`. I did **not** find a counterexample; I did
**kill** the three most natural candidates, each by a *different* mechanism, and I fully
resolved the semicartesian (unit-terminal) case up to one noted gap.

---

## 0. The question

For a monoidal structure `(⋆, I)` on `Set`, the Day tensor `⊙_⋆` on `Cont ≅ Fam(Set^op)` is
**left closed iff `R_B := (−) ⋆ B : Set → Set` is a polynomial functor for every set `B`**
(proved 2026-07-15, `2026-07-15-uniform-closure-day-tensors.md`). `polynomial ⟺
F ≅ Σ_i(−)^{A_i} ⟺ preserves connected limits ⟺ preserves wide pullbacks` (Carboni–Johnstone;
Gambino–Kock).

> **TARGET.** Is there a monoidal `(⋆,I)` on `Set` with `R_B` *not* polynomial for some `B`?
> **YES** ⇒ first genuinely non-left-closed convolutional tensor. **NO** ⇒ closure is
> automatic; the side-condition is vacuous.

**Restatement (the clean form).** `R_B` polynomial for all `B` ⟺ **`⋆` preserves connected
limits in its left variable.** So:

> **Vacuity ⟺ every monoidal structure on `Set` preserves connected limits in each variable.**

This is the sentence the whole question reduces to. Everything below is evidence that it is
*true* — no monoidal structure on `Set` escapes connected-limit preservation — together with a
precise statement of what is still unproven.

---

## 1. Structural reductions (all rigorous)

### 1.1 The regular representation.
`R : (Set, ⋆) → (End Set, ∘)`, `B ↦ R_B`, is strong monoidal with `R_B ∘ R_C ≅ R_{C⋆B}`,
`R_I = Id`, `R_B(I) = B`. The question is whether this representation lands in `Poly ⊂ End Set`.

### 1.2 Unified unit map.
For `x ∈ B^I = Set(I,B)`, functoriality along `x:I→B` gives `A⋆x : A⋆I = A → A⋆B`; assembling,
a natural `ν : A × B^I → A⋆B`. Specialises to the two comparison maps:
- **I = ∅ (unit initial):** `ι_A : A = A⋆∅ → A⋆B`, `ι_B : B → A⋆B`, `κ = [ι_A,ι_B] : A+B → A⋆B`.
- **I = 1 (unit terminal):** dual `⟨π,π'⟩ : A⋆B → A×B` with `π = A⋆!_B`, `π' = !_A⋆B`.

### 1.3 The retraction lemma (NEW — the key rigorous tool).
Let `⋆` be **any** monoidal structure on `Set`. Pick the section/retraction pair
`i₀ : 1→2`, `t : 2→1` with `t∘i₀ = id₁` (and `t∘i₁ = id₁`). Then for any `B`:

> **Any `(u,v) ∈ (1⋆B)²` with `(i₀⋆B)(u) = (i₁⋆B)(v)` in `2⋆B` already has `u = v`.**

*Proof.* Apply `(t⋆B) : 2⋆B → 1⋆B`. `(t⋆B)∘(i₀⋆B) = (t∘i₀)⋆B = id_{1⋆B}`, likewise for `i₁`.
So `u = (t⋆B)(i₀⋆B)(u) = (t⋆B)(i₁⋆B)(v) = v`. ∎

**Consequence.** `R_B` preserves the pullback of the two points `1 ⇉ 2` **iff** the equalizer
`Eq(i₀⋆B, i₁⋆B : 1⋆B ⇉ 2⋆B)` equals the image of `R_B(∅→1)` — i.e. iff *"an element of `1⋆B`
is fixed by both point-inclusions exactly when it does not depend on the `1`-slot."* The
lemma reduces wide-pullback-of-points preservation to this single **independence** condition,
and proves the injective half for free. (Preservation of *this* pullback is a necessary
condition for polynomiality — see §3, verified for `∨_S,×,+` and violated by the support
tensor.)

---

## 2. The semicartesian (unit-terminal) case

**Claim (unit terminal ⟹ ⋆ ≅ ×).** If `I = 1`, then `A×B` is a natural retract of `A⋆B`
(§1.2: `μ : A×B → A⋆B`, `μ(a,b) = (a⋆id_B)(b)` a section of `⟨π,π'⟩`; R3). Morally the
"extra" `E(A,B) = A⋆B ∖ im μ` vanishes when `A` or `B` is terminal, and **a functor vanishing
at the terminal object `1` is identically `∅`** (since `1` is terminal, `E(A)→E(1)=∅` forces
`E(A)=∅`). Hence `E = ∅` and `⟨π,π'⟩` is iso: `⋆ ≅ ×`, and `R_B(A) = A×B` is polynomial. This
is the Dirichlet case (`⊗`), which is closed.

**Honest gap (recorded).** The terminal-vanishing lemma is airtight, but its application needs
`E` to be a genuine *subfunctor*. In `[Set,Set]` the natural idempotent `e = μ∘⟨π,π'⟩` splits
only as a **retract** (`A×B` is a retract of `A⋆B`), which does not by itself supply a natural
complement `E` — a morphism `f⋆g` need not carry non-`μ` elements to non-`μ` elements. So the
argument shows "`A×B` is a natural retract of `A⋆B`" rigorously but "`= A×B`" only modulo this
subfunctor step. **Computational search (FinSet≤2, unit 1) found no non-cartesian
semicartesian structure**, and the `|2⋆2|=5` candidate fails already at size-associativity.
The clean route to close it is **Fox's theorem**: `δ_A := μ∘Δ_A : A→A⋆A` with counit `!_A` is
a natural cocommutative comultiplication whose counit laws hold (`π∘δ = id`); if `δ` is
coassociative and monoidal (unverified — reduces to `μ` being a monoidal natural
transformation `(Set,×)→(Set,⋆)`), Fox gives cartesian. **I mark unit-terminal as
"very likely ⋆ = ×, computationally confirmed on small sets, one coherence step open."**

---

## 3. The three natural counterexamples, all refuted (rigorous)

The unit-**initial** case is the rich one (it contains the whole `∨_S` family, all
polynomial). A YES answer, if it exists, most plausibly lives here. I tested the three most
natural non-polynomial candidates. **All fail — each by a different mechanism.**

### 3.1 `max` — fails **bifunctoriality (interchange)**.
Target `|A⋆B| = max(|A|,|B|)`, unit `∅`; then `R_B(A)=max`-sized is non-polynomial
(`max(n,2)=2,2,2,3,…` is not a ℕ-combination of powers). **No functorial bifunctor with object
map `max` exists at all.** Witness (exhaustive search + hand proof): with `i₀:1→2`, `t:2→1`,
`t∘i₀=id`, interchange forces `F(t,i₀):2⋆1→1⋆2` to equal both
`F(id,i₀)∘F(t,id)` (which factors through the *pinch* `1⋆1`, `|1⋆1|=1`, so has rank ≤ 1) and
`F(t,id)∘F(id,i₀)` (a composite of two bijections of a 2-element set, rank 2). `1 = 2`,
contradiction. The obstruction is `max(1,1)=1 < 2 = max(1,2)` — the rank-collapsing "pinch"
clashing with the retraction. (Verified: `scratch/max_tensor.py` finds 0 bifunctors;
`scratch/witness.py` the minimal contradiction.)

### 3.2 The **support tensor** `A⋆B := A ⊔ B ⊔ {•}` (`•` iff `A,B ≠ ∅`) — fails **associator naturality**.
Unit `∅`. This *is* a bifunctor, is **cardinality-associative**, its pentagon **passes**, its
triangle **passes** — and `R_B(A) = A ⊔ B ⊔ [A≠∅]` is genuinely non-polynomial (the
support/indicator term `[A≠∅]`, the classic non-polynomial functor). **Yet no natural
associator exists** — exhaustive over **all** bijections `(A⋆B)⋆C → A⋆(B⋆C)` (no
canonical-leaf assumption; the size-5 triple `(1,1,1)` alone has 120 permutations) for triples
from `{∅,1}`, backtracking with naturality w.r.t. every morphism: **zero** natural families
(`scratch/support_no_assoc_full.py`). The failure is at the map
`∅→1` that *fills an empty middle slot*: the single separator point `•` cannot record *which*
leaves it separates, so `(A⋆∅)⋆C`'s `A–C` separator has nowhere consistent to go once `∅`
becomes inhabited. Seen through §1.3: `R_B` fails the two-point pullback — `∅⋆B` has `|B|`
elements but `(1⋆B)×_{2⋆B}(1⋆B)` has `|B|+1` (the spurious `(•,•)`, because `•∈1⋆B` maps to
`•∈2⋆B` under *both* points). (`scratch/support_monoidal_full.py`, `pullback_lens.py`.)

**Why this is the decisive test.** `∨_S` is coherent because its normal form keeps a term for
*every* subset `K` of leaves (`Π_{i∈K}X_i × S^{|K|-1}`), so each extra element records its
provenance — that provenance is exactly the exponent making it *polynomial*. The support
tensor collapses provenance to a bare point; associativity's naturality then forces the
provenance back, and there is none to give. **Polynomiality = provenance-tracking =
coherence.** This is the heart of why vacuity should hold.

### 3.3 Degree-≥2 extras (`Sym²`, `A²`) — fail **associativity by growth**.
`A⋆B := A ⊔ Sym²(A)×B ⊔ B` (a bifunctor, non-polynomial): `|(A⋆B)⋆C|` is degree-4 in `|A|`
while `|A⋆(B⋆C)|` is degree-2, so no natural associator can exist. Any super-linear "extra" is
amplified inconsistently by the composition-closure `R_B∘R_C ≅ R_{C⋆B}`. (`vacuity_growth.py`.)

---

## 4. What the three failures have in common

A non-polynomial `R_B` is exactly one that **loses information a polynomial records**: which
first-argument elements each output "uses" (its fibre exponent). Every attempt to build one
runs into a *different guard* of the monoidal axioms:

| candidate | non-poly mechanism | which axiom kills it |
|---|---|---|
| `max` | idempotent/rank-collapse | **bifunctoriality** (interchange vs a retract) |
| support `A⊔B⊔[both≠∅]` | provenance-collapsed separator | **associator naturality** (empty-slot filling) |
| `Sym²`/`A²` extra | super-linear growth | **associativity** (degree `d² ≠ d`) |
| any (I=1) | extra vanishes at terminal | **`E(1)=∅ ⟹ E=∅`** (retract only — §2 gap) |

The pattern is strong enough to state the

> **Vacuity Conjecture.** Every monoidal structure on `Set` preserves connected limits in each
> variable; equivalently every Day-convolutional tensor on `Cont` is left closed, and the
> side-condition of the 2026-07-15 biconditional is automatic. In particular §4-handedness is
> never observable and "convolutional = left-closed" for Day tensors.

**I believe this is true.** What is missing is a single positive theorem: that
associativity + naturality *force* `R_B` to preserve the point-pullbacks (§1.3's independence
condition) and, beyond that, all connected limits. §1.3 supplies the injective half in full
generality; the surjective half ("agreement ⟹ independence of the first slot") is the open
core.

---

## 5. Verification index (`scratch/`)
- `max_tensor.py`, `witness.py`, `validate.py`, `localize.py` — `max` has 0 bifunctors;
  minimal interchange contradiction; enumerator soundness. [agent-computed]
- `support_monoidal_full.py` — support tensor: bifunctor ✓, pentagon ✓, triangle ✓,
  associator naturality ✗.
- `support_no_assoc.py` — **no** natural associator for the support tensor on `{∅,1}`
  (exhaustive over both candidate families).
- `pullback_lens.py` — two-point-pullback preservation: `∨_S,×,+` ✓, support ✗ (3≠2).
- `vacuity_growth.py` — degree-2 extra breaks cardinality-associativity (deg 4 vs 2);
  `max(n,2)` not a ℕ-combination of powers.
- `semicartesian_search.py` — no non-cartesian semicartesian structure found on FinSet≤2/≤4;
  terminal-vanishing lemma. [agent-computed]

## 6. Grade discipline
- `proved`: the retraction lemma §1.3; non-realizability of `max` §3.1; non-monoidality of the
  support tensor §3.2; growth failure §3.3; `A×B` is a natural retract of `A⋆B` when `I=1`.
- `computed`: no small non-cartesian semicartesian structure; pentagon/triangle of the support
  tensor.
- `conjecture` (not claimed proved): the Vacuity Conjecture §4; `unit-terminal ⟹ ⋆=×` (§2 gap).
- The 2026-07-15 biconditional is **unaffected** — it holds either way; only the vacuity of its
  side-condition is at issue, and remains open.
