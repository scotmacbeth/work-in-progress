# The `Bag` witness: the ∏-Mendler hypothesis in the crown Theorem 1 does *real* work

**MacBeth — PROVE session 2026-08-05 (heartbeat-4, adversarial re-audit of the gap closure).**
For Neil/Robin. One paragraph if you're busy; the rest is the receipts.

## TL;DR

Re-auditing my own heartbeat-3 gap closure (`proofs/2026-08-05-crown-gap-closure.md`,
Theorem 1: *within ∏-Mendler, `T_M` preserves cartesian morphisms ⟺ `M` cartesian monad*),
I found the injectivity step of Lemma 1.4 rests on an **unstated and generally-false**
inference: *"`M` is a polynomial functor (cartFun)."* **cartFun ⇏ polynomial.** The witness is
the flagship analytic monad `Bag` = free commutative monoid (finite multisets):

- `Bag` **is cartFun** (`u_*` leaf-bijective — multiset map keeps multiplicity), and
- `Bag` **is leaf-cartMu** (flatten never merges/creates a leaf), yet
- `Bag` is **not a cartesian monad**: it fails the connected pullback
  `{a,a'}→z₀←{b,b'}` — at size 2, `|Bag(P)|=10` but `|Bag(X)×_{Bag(Z)}Bag(Y)|=9`, comparison
  non-injective (computed, `scratch/fibrational-crown/bag_probe.py`).

So the *leaf* conjunction `cartFun ∧ cartMu` is **strictly weaker** than *(2) cartesian
monad* — the gap is a **connected-limit** phenomenon that the leaf calculus is blind to. `Bag`
would be a genuine counterexample to *(1)⟹(2)* **if it were ∏-Mendler.**

**It isn't — and *why* it isn't is the real content.** `Bag ∉ ∏-Mendler` because the
∏-lift `P⋆(m)=∏_{b∈lv(m)}P(x_b)` is **ill-defined** on it: a repeated element `{a,a}` has a
leaf-swap that *fixes the labels* (both are `a`) but permutes the two factors of `P(a)×P(a)`
non-trivially when `|P(a)|≥2`. Multiplicity symmetry ⟹ no ∏-cointerpretation. `Pf` escapes
because a set's elements are distinct (label map injective, no label-fixing leaf symmetry);
`List` escapes because its positions are free/ordered.

## The fix (now in the proof file, §7)

**Lemma 1.4′ (label-rigidity).** ∏-Mendler leaves admit no non-trivial label-fixing
automorphism (else `P⋆` is not invariant, contradicting well-definedness). Hence within
∏-Mendler, **cartFun ⟹ polynomial** genuinely holds, and the tautological element
`(σ, id_{I(σ)})∈MM(I(σ))` exists — which is exactly what the relabeling move in Lemma 1.4
needs. Theorem 1's conclusion is **unchanged**; only its justification is now complete.

## Why I think this is worth your two minutes

1. **It corrects a real overclaim in my own record**, not the theorem — honesty ledger stays
   clean. The registry node `crown-boundary-table` keeps trust `proved` (conclusion holds,
   proof now complete), with the caveat logged in its `approach`.
2. **`Bag` is a *sharper* boundary witness than `Reader`/`State`.** Those fail visibly
   (cartFun without cartMu — `μ` merges). `Bag` passes **both** leaf tests; it is the
   analytic level, sitting *outside* ∏-Mendler on the **opposite side** of the leaf-vs-monad
   split:
   ```
   Reader/State : polynomial functor,  μ merges           → not cartesian monad (fails cartMu)
   Bag          : cartFun AND leaf-cartMu, but ANALYTIC    → not cartesian monad (fails a connected limit)
   ```
3. **It re-reads the ∏-Mendler hypothesis.** In the paper/book we've been treating "∏-Mendler"
   as "the class where `T_M` is defined (has the Mendler `i,j`)." The `Bag` audit shows it is
   *also* precisely **label-rigidity = the exclusion of analytic/symmetric functors**, and that
   this is what upgrades cartFun to polynomial. For the grant's polynomial-monad framing this
   is the clean statement: *∏-Mendler ∩ cartFun = polynomial monads; the symmetric monads
   (`Bag`, and any free-commutative/`S_n`-quotient) are exactly the ones label-rigidity throws
   out.*

## Grant/book hook

The corrected slogan for the cartesian level of the stratification:
> "*Within the ∏-Mendler class, `T_M` preserving cartesian morphisms is equivalent to `M`
> being a polynomial (cartesian) monad — and the ∏-Mendler hypothesis is doing this work by
> **label-rigidity**: it excludes the analytic monads like `Bag`, whose leaf-level data looks
> cartesian but whose connected-limit behaviour is not.*"

Files: `proofs/2026-08-05-crown-gap-closure.md` §7; `scratch/fibrational-crown/bag_probe.py`,
`bag_pimendler_obstruction.py`. Registry: `effect-coeffect-arrows.json` node
`crown-boundary-table` (approach updated, trust `proved`, validator green).

— MacBeth
