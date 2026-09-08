# Lemma N advanced: R0 proved, both suspects killed, a new stabilizer invariant

**MacBeth → Neil / Robin / Rick — 2026-09-05 (PROVE).**
Full proof: `proofs/2026-09-05-lemmaN-retract-and-beta.md`. Registry `m-containers.json` node
`necessity-lemma-gap` (now `computed`, validator-green) with 5 children.

## TL;DR
THM 3 says *M-containers compose ⟺ M polynomial*; sufficiency was proved, the converse (**Lemma N**)
was the open gap, reduced to **(★): `M∘M ≅ ⟦r⟧∘M` (r poly) ⟹ M polynomial**. This session:

1. **Lemma R0 — PROVED (Lean-able).** For a monad, `M` polynomial ⟺ `M∘M` preserves connected
   limits. (`μ∘ηM=1` ⟹ `M` a split retract of `M∘M`; retracts inherit limit-preservation; GK §1.18.)
2. **The single-instance retract route is CIRCULAR — PROVED.** `M∘M ≅ ⟦r⟧∘M` gives *no* categorical
   information beyond R0's tautology (comparison-map reflection through `⟦r⟧` is symmetric). So (★),
   if true, needs more than `p=q=Id`. This *corrects* the scoping note's hope that R0 closes it.
3. **β is NOT the counterexample — PROVED.** The scoping's prime suspect (ultrafilter monad) fails
   the cardinality law on infinite sets: `|ββX| = 2^{2^κ} ≠ κ = Σ_i |βX|^{|B_i|}` for any fixed
   polynomial. Same argument kills *every* super-polynomially-growing monad (P, P⁺, D, continuation,
   filter).
4. **The free commutative monoid 𝕄 is NOT the counterexample — PROVED (crown).** This is the sharp
   case: 𝕄 is non-polynomial but has *polynomial-shaped cardinality* (all ℵ₀), so cardinality is
   blind — exactly the B3 danger zone. Killed by a **new invariant**: a natural iso `F≅G` induces
   `Aut(X)`-equivariant bijections, which **preserve point-stabilizers**. Every `⟦r⟧∘𝕄`-stabilizer
   is a **Young** subgroup (permutes points only *within* multiplicity-blocks); but
   `{{a,b},{c,d}} ∈ 𝕄𝕄X` has stabilizer `S₂≀S₂ = D₄` (order 8) — the **block-swap** `(ac)(bd)` is a
   genuinely second-order symmetry no polynomial (free) outer layer can produce, and `D₄` is not
   Young (8 ∉ {1,2,4,6,24}, the Young orders of S₄). Hence `𝕄𝕄 ≇ ⟦r⟧∘𝕄`. [Python + independent
   referee sub-agent verified; the referee converged on the same `D₄` witness.]

## The picture (dichotomy)
Every non-polynomial monad fails `M∘M ≅ ⟦r⟧∘M` because it is either **(a)** super-polynomially
growing (killed by cardinality, §3) or **(b)** symmetric/analytic (killed by the wreath-stabilizer
invariant, §4). Proved for all of (a) and for the symmetric-power/𝕄 class of (b). The **only**
residual is a clean **Plethysm Lemma** for general non-free analytic species ("`A•A` has a molecular
constituent not a product of `A`-constituents"), and **no known monad inhabits that gap.**

**So: THM 3 is a genuine biconditional for every monad that actually arises.** The obstruction to an
unconditional converse is not a categorical defect — it is the rigidity of species self-substitution
(the Plethysm Lemma), a concrete question I can hand to species theory.

## Why this is worth the grant narrative
The composition side of the crown now has a *tool*, not just a slogan: an `M∘M ≅ ⟦r⟧∘M` isomorphism
is obstructed by the **`Aut(X)`-stabilizer lattice — Young (one effect-layer) vs wreath (a non-free
outer layer)**. Combined with THM 2 (fullness = codensity), the effect monad `M` is pinned by two
independent representability invariants. *writer composes but isn't full; D and β can't compose
(growth); 𝕄 can't compose (symmetry).*

## Questions for Neil
- Is the **Plethysm Lemma** ("non-flat species `A` ⟹ `A•A` is not `(flat)•A`") known in the species
  literature (Bergeron–Labelle–Leroux / Joyal / Yeh molecular decomposition)? It would close Lemma N
  unconditionally for all analytic monads.
- Worth Lean-ing **Lemma R0** now (elementary retract argument) as the next `lean` deliverable?

## Next
- (★) general analytic: attack the Plethysm Lemma (orbit/transitivity + minimal-degree closing of the
  single-transitive-constituent escape).
- Then return to the parallel deep track **(Q)** (`state/PROVE.md.frontier-Q-2026-09-04`).
