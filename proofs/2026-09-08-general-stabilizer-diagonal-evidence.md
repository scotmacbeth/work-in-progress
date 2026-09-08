# The peg-diagonal mechanism generalizes: parametric-H stabilizer escape (computed evidence)

**Date:** 2026-09-08 (system clock; real-clock naming per [[feedback_write_before_read_dated_logs]]).
**Grade:** `computed` (four brute-force checks with a validating control; the general theorem is not yet
proved — see PROVE.md target `theorem-general-stabilizer-necessity`).
**Registry:** `m-containers.json`, node `general-stabilizer-diagonal-evidence` under `necessity-lemma-gap`.
**Artifact:** `scratch/2026-09-08-C3-diagonal-witness.py` (stdlib only; brute-forces S_4 / S_6).
**Parent results:** `2026-09-07-U-corner-resolved-stabilizer.md` (the C_2 case + Meta-theorem),
`2026-09-07-theorem-S-prime-wreath-depth.md` (the depth invariant).

## Claim tested
The U-corner proof (09-07) closed THM-3 necessity at the single monad `U` (free commutative *unital*
magma) via a per-component stabilizer that no polynomial outer `⟦r⟧∘U` can realize: a lone correlated
diagonal swap `C_2 = ⟨(01)(23)⟩` of two rigid size-2 blocks. The question for the general residual
(`a_0>0 ∧ 𝔥=∞`): **does this mechanism generalize from `S_2` to an arbitrary outer-operation symmetry
group `H`?** If yes, it is the engine for the whole free-unital-non-flat-operad family, not one witness.

## The mechanism, stated parametrically
Let `O` be a symmetric operad with a distinguished operation `ω` of arity `k≥2` whose slot-symmetry is
`H ≤ S_k`, `H≠1`, and let there be a **rigid, label-free peg** (a nullary element that survives at the
level where it breaks symmetry). Build `k` *isomorphic rigid* inner blocks `b_1,…,b_k` on disjoint
label-pairs, using the peg to kill each block's internal symmetry (`Aut(b_i)=1`). Then
`w = ω(b_1,…,b_k) ∈ (M∘M)[k·ℓ]` has stabilizer equal to the **correlated diagonal copy of `H`** — `H`
acting simultaneously on the `k` rigid blocks and on their (isomorphically identified) internal labels.
That diagonal is *never a block-fixing product* whenever `H` does not fix the blocks pointwise, so by the
Meta-theorem (polynomial-outer stabilizers are block-fixing products) it lies outside `𝓕(M)`, and the
composition test fires: `M∘M ≇ ⟦r⟧∘M` for every polynomial `r`.

## Computed verification (all four checks pass)
1. **CONTROL (model validation) — binary commutative unital `U`.** Reproduced the published witness:
   `Aut(w) = ⟨(01)(23)⟩ ≅ C_2`, order 2, on interleaved blocks {0,2},{1,3}; each block rigid. The model
   matches `2026-09-07-U-corner-resolved-stabilizer.md`, so downstream results are trustworthy.
2. **EXTEND — cyclic-ternary `ω`, `H = C_3 = ⟨(123)⟩ ≤ S_3`.** `Aut(w) = {id, (0 2 4)(1 3 5),
   (0 4 2)(1 5 3)} ≅ C_3`, order 3 — exactly the predicted correlated diagonal 3-cycle on three rigid
   size-2 blocks {0,1},{2,3},{4,5}. Each inner block rigid (cyclic symmetry + peg kills internal symmetry).
3. **ESCAPE — `Δ = ⟨(0 2 4)(1 3 5)⟩ ∉ 𝓕(6)`.** `Δ` is support-indecomposable: its only invariant
   partition is the orbit partition {0,2,4}|{1,3,5}, whose restriction-product has order 3·3=9 ≠ |Δ|=3, so
   `Δ` is not the direct product of its restrictions; exhaustive search over all ≥2-part invariant
   partitions finds no block-fixing-product decomposition. **Composition test fires.**
4. **NEGATIVE CONTROL — flat non-commutative (ordered) binary magma.** Same peg construction with a
   trivial-symmetry operation gives `Aut(w) = {id}`; the diagonal `(01)(23)` is *not* an automorphism. No
   escape. This pins the escape on **non-flatness (`H≠1`)**, not on the peg alone.

## What the computation sharpens (honesty note)
The ternary operad has no binary operation, so the nullary `c` cannot carry the standard binary
absorption law `μ(x,c)=x`. It was modeled as a **rigid non-absorbing nullary peg** inside `ω`. This is
the faithful reading of "unit as peg": the mechanism only ever exploits that the peg is a *rigid,
label-free element that survives at the level where it breaks symmetry*. The C_2 control uses the genuine
binary absorption unit and behaves identically. **Consequence for the theorem statement:** the correct
hypothesis is not "`M` has a unit" but "`M` admits a rigid label-free peg element" — which *broadens*
the class (the scoping analysis flagged that a general `a_0>0` constant need not be a unit; the peg
abstraction is what actually carries the argument). This is the load-bearing refinement to carry into
the PROVE session.

## Status of the general theorem (NOT proved here)
This is `computed` evidence — two data points (`S_2`, `C_3`) plus a flat control, verified parametrically
in `H`. The general theorem (`theorem-general-stabilizer-necessity`) still needs the three lemmas proved
uniformly: (1) **Rigidification** — a peg makes any single block rigid (`Aut(b_i)=1`) — stated for a
general non-flat analytic `M`; (2) **Witness** — `Stab(ω(b_1,…,b_k)) = Δ_H` (the correlated diagonal);
(3) **Escape** — `Δ_H ∉ 𝓕_ind(M)` whenever `H` moves the blocks, ruling out that `M`'s own constituents
already realize `Δ_H` (the "`𝓕`-self-control" gap flagged in S′ §5 and the U-corner proof — the single
most likely point of failure for an over-broad claim). Brute force does not scale past small `k`; the
witness stabilizer must be computed *constructively* in the proof.

## Provenance cap
Inherits the P/S′/U cap: Meta-theorem is elementary, but the ambient "analytic monad ≃ symmetric operad"
frame rests on Joyal 1986 ff + Gambino–Kock MPCPS 154 (2013) §1.18–1.21, cited `agent-summary`
(Gambino–Kock is in-seed and covers the *correspondence*; the fully-faithfulness clause and the plethysm
substitution `Z_{A•B}=Z_A∘Z_B` are not in the seed — requested from Robin 2026-09-08).
See [[necessity-trichotomy-is-symmetry-resolution]], [[U-corner-closed-stabilizer-per-component]].
