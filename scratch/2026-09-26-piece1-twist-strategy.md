# Piece 1 — [ν] ⟂ [Ω] converse as a THEOREM: strategy

Date: 2026-09-26 (WAKE deep-work). Target from PROVE.md.

## Goal
Fix D (ideal, (D,+),(D,∘) abelian), H, outer data (μ,σ). Show the map
  Φ_ext : {skew-brace extensions 0→D→G→H→0 with fixed (μ,σ)}  →  {residue [ν]} × {split?}
is SURJECTIVE (a product). The [Ω]=0 (split) side is PROVED (bicrossed H⋈D realizes all [ν]).
Gap = converse: realize [Ω]≠0 WITH prescribed residue [ν'].

## Already proved (take as given — 2026-09-25 nu-variation-direct-factor.tex)
- L1: fixing (μ,σ,β,τ̄), the ν-orbit is a FREE TRANSITIVE torsor under L^{H∖0},
      L = im(λ|_D) ≤ Aut(D,+). Moving within the torsor changes ν_h by L-elements ⟹ residue [ν_h]=ν_h L FIXED.
- L2: residue [ν_h] ∈ Aut(D)/L section-independent.
- L3: [β],[τ̄] and the splitting predicate are ν-FREE and CONSTANT on the ν-torsor.

## The proof strategy (converse)
1. Start from a SPLIT (bicrossed) extension E₀ with prescribed residue [ν'] — exists by the proved [Ω]=0 side.
   Its (β,τ̄) block is the trivial (coboundary) class.
2. "Add obstruction at fixed ν": perturb the (β,τ̄, ambient-defect) block by a NON-TRIVIAL
   skew-brace 2-cocycle representing [Ω]≠0, leaving ν (hence residue [ν']) UNCHANGED.
3. By L3, [β],[τ̄] are ν-free, so such a perturbation does not disturb the residue.
   Result: a NON-split extension carrying the SAME residue [ν'].  ⟹ converse.

## THE CRUX (where a coupling could hide = potential refutation)
Step 2 requires: for the FIXED ν (residue [ν']), the set of valid (β,τ̄) cocycles is a
NON-TRIVIAL group mod coboundaries — i.e. the obstruction group
  H²_{[ν']} := {valid (β,τ̄) at fixed ν} / coboundaries
is NONZERO, and (for a clean product) INDEPENDENT of [ν'].

The danger: the generalized (moving-ν) brace-compatibility (RY eq 3.10 extended to
non-trivial kernel — UNPUBLISHED, must build natively) may make the (β,τ̄)-constraint
ν-DEPENDENT. Need to show eq 3.10 is affine in (β,τ̄) with a solution space whose
cohomology is ν-independent (residue only enters the μ,σ block, not the β,τ̄ differentials).

### Decisive check (computational, Z2×Z4 has full data; Piece 2 agent extends to |D|≥8)
For each residue class [ν'], compute H²_{[ν']} = group of valid (β,τ̄) mod cob. at fixed ν.
- If nonzero for all [ν'] and residue-independent as a group ⟹ THEOREM (product), converse holds.
- If it VARIES with [ν'] (e.g. zero for some residue) ⟹ genuine coupling ⟹ REFUTATION (also valuable).

Existing Z2×Z4 data: all 6 combos (3 ν-classes × {split,nonsplit}) OCCUR ⟹ strongly suggests
H²_{[ν']}≠0 residue-independent on Z2×Z4. Need the GROUP-structure form, not just occurrence,
to make it a theorem. And Piece 2's |D|≥8 witness tests the GENUINE L⊊Aut(D) regime.

## Reduction to a clean lemma
THEOREM (target): H²_{[ν']} ≅ H²_{[ν'']} for all admissible residues, via the additive-forgetful
splitting. Because β (additive cocycle) is verbatim the additive extension's own H²(H;D,+_μ)
cocycle (RY, proved 09-25 phiPlus_welldef), which depends ONLY on μ, NOT on ν. And τ̄
(circle cocycle) depends on σ. Residue [ν] is the outer-action datum, orthogonal to both
differentials. ⟹ the obstruction group is literally ν-independent by construction of the
forgetful maps. This is essentially COROLLARY of the proved diagonal-coboundary-map fact
(θ↦(dθ|₊,dθ|∘) diagonal) PLUS L3 (β,τ̄ ν-free).

## Plan
- Await Piece 2 construction (|D|≥8, genuine L⊊Aut(D)) + its cross-tab.
- Then formalize the reduction above as a short proof: converse = "add a nontrivial (β,τ̄)
  to a split extension at fixed ν, valid because the β,τ̄ differentials are ν-free (L3) and
  the coboundary map is diagonal (proved 09-25)".
- Write proofs/2026-09-26-nu-omega-independence-theorem.tex; register upgrade of
  cross-independence-nu-omega [computed]→[proved].
