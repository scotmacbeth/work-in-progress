# Branching obstruction lifts to a full container morphism (proved 2026-08-04)

**For Neil / Robin.** PROVE session hardening the book's headline dichotomy
"effect–coeffect arrow category ⟺ `M` non-branching."

## What was owed
The ⟸ direction (branching ⟹ not a category) was only **computed** at the full-morphism level
(`bikleisli.py` witness triple for `Pf`); the fibre-level `E2′` failure was Lean-verified. Gap:
does the fibre obstruction **necessarily lift** to genuine non-associative *full* `Cont`-morphisms,
or could it be an artefact of restricting to a fibre?

## What is now proved
For `M = Pf` over `A₁ = ({a,b},{a:2,b:1})` there is a triple `f,g,h : A₁ ⇝ A₁` with
`(h⋆g)⋆f ≠ h⋆(g⋆f)` **as full `Cont`-morphisms**. The two morphisms agree on shapes and on every
backward component except at source shape `b`, target position `(1,0)`, where they are `∅` vs `{0}`.
Proof = a **forced finite calculation** of both 5-stage backward chains (each of the ten
stage-values is one structural map's coordinate formula at one point; independently re-derived),
plus the **identification**: both bracketings pass through the *same* overlap shape `{{a,b},{a}}`
where `μ^T` merges leaf `a` — the exact fibre configuration of the `E2′` failure — and differ only
in the `κ`/`μ^T` order (product-then-merge vs merge-then-merge = the 4-vs-2-tuple gap). **No
downstream cancellation**: every transport map (`η^T` projection, `μ^T` restriction, `δ` union,
`Pf`-images) is a bijection at the single un-merged leaf, so the fibre inequality cannot be erased.

Conclusion: **"arrow category ⟺ non-branching" is an iff at the full container-morphism level, not
merely fibrewise.** (Registry `effect-coeffect-arrows.json` node `branching-full-morphism-lift`:
computed → **proved**.)

## A correction you should know about
`PROVE.md` proposed `M = 1 + X²` as "the simplest branching cartesian monad, max arity 2".
**No cartesian monad has max arity 2** (Proposition 0): a binary op self-plugs `2 ↦ 4` leaves under
cartesian `μ`, forcing unbounded arity — the arity gap `{≤1} ∪ {∞}`. So `1 + X²` is *not* a cartesian
monad; the honest minimal branching witness is `Pf`. (`Reader² = X²` is also excluded here: its unit
`x ↦ (x,x)` gives repeated leaf labels, which the `∏`-cointerpretation `μ^T` forbids.)

## Honest gaps
1. The abstract `assoc ⟺ E2′` equivalence is **cited** (Beck / Power–Watanabe); I use only the
   sufficiency direction `E2′ ⟹ assoc`, and only for *attribution* — the non-associativity itself is
   proved independently by the finite calculation.
2. The no-cancellation argument is proved for the specific maps in this composite; a uniform "every
   branching `∏`-monad lifts to an *explicit* triple" would add a detection/Yoneda step (the abstract
   equivalence already gives *existence* for any branching `M`).
3. Scope = `∏`-cointerpretation, commutative `M`.

## Book / Lean hooks
Goes straight into the Monads-and-Comonads chapter as the sharp form of the dichotomy. Sets up a
clean next Lean target: the `Finset` full-morphism `distrib_mult` non-associativity, one level up
from `BranchingObstruction.lean`.

Files: `proofs/2026-08-04-branching-full-morphism-lift.md`;
`scratch/monad-comonad-transfer/{bikleisli.py, trace_known.py, independent_check.py, reader_test.py}`.
