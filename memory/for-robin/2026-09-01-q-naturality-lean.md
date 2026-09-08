# Lean: naturality of the left adjoint `F_q` **in the parameter `q`** — DONE

**Date:** 2026-09-01 (lean session)
**File:** `lean/Containers/Containers/CompLeftAdjointNatQ.lean` (new module, wired into
`Containers.lean` root).
**Build:** `lake build` green — **59 jobs, 0 errors / 0 warnings / 0 sorries**.
**Axioms:** every one of the seven core theorems: `#print axioms` = `[Quot.sound]` only.

## What this closes

`CompLeftAdjoint.lean` certified `F_q ⊣ (−)◁q` as an adjunction of functors for each *fixed* `q`,
and (second pass) the naturality of unit/counit in the fibre variable. Its own note flagged the
remaining gap: **naturality of `F_q` in the parameter `q`**. That is now formalised.

## The content: variance was determined, not assumed

`(−)◁q` is **covariant** in `q` (`whiskerLeft`). The family of *right* adjoints being covariant
forces the family of *left* adjoints to be **contravariant**: a container morphism `ψ : q ⟶ q'`
gives

    F_ψ : F_{q'} r ⟶ F_q r        (note the reversal).

On shapes `F_ψ` is the identity; on positions it is `ψ.toNat`, the induced forward natural
transformation `⟦q⟧ ⟹ ⟦q'⟧`. This is the *only* assignment of the right variance — a morphism
`F_{q'} r ⟶ F_q r` runs backward on positions, from `⟦q'⟧(r.Pos ρ)` to `⟦q⟧(r.Pos ρ)`, and
`ψ.toNat` supplies exactly that forward map. The naive "F follows ψ" reading has the wrong variance
and does not typecheck. (Same shape of risk as the fixed-`q` file, and again Lean pins it.)

## Declarations

- `Container.leftAdjOnq` — `F_ψ`.
- `leftAdjOnq_id`, `leftAdjOnq_comp` — **contravariant** functoriality (`F_id = id`,
  `F_{ψ;ψ'} = F_{ψ'};F_ψ`).
- `leftAdjOnq_naturality` — `F_ψ` natural in `r`.
- `adjUnit_naturality_q`, `adjCounit_naturality_q` — the two compatibility squares along `ψ`. The
  counit square is genuine (over the shared corner `F_{q'}(p◁q)`), not a cospan.
- `leftAdjOnq_eq_mate` — `F_ψ` **is** the mate of `L_ψ = (−)◁ψ`.

All close by `ContainerMorphism.ext' rfl (fun _ _ => rfl)` — fibres agree definitionally, as in the
fixed-`q` file.

## Negative control — third independent confirmation of the shape-leg warning

On `qBool` (one shape, two positions), perturb the identity `F_{id}` by flipping the two
`qBool`-positions in the labelling: `⟨(),k⟩ ↦ ⟨(),k∘not⟩` (precompose the inner `Bool → r.Pos ρ`
with negation). This is not the identity.

- **Control 1 (a theorem, compiles):** it still satisfies naturality-in-`r` **on the nose**
  (`leftAdjOnqPerturbed_naturality`). Reason: the flip precomposes the labelling on the
  `qBool`-positions while `leftAdjMap φ` postcomposes on the position type, and pre/postcomposition
  commute. So **naturality in `r` does not pin down `F_ψ`.**
- **Control 2 (a failure, in prose + verified):** it **breaks `adjUnit_naturality_q`**, and — I
  checked this explicitly this session with an `rfl`-fails test — it fails on the **position leg**
  while the **shape leg still discharges by `rfl`**. Exactly the fixed-`q` pattern: the content of
  the compatibility squares lives in the positions.

## Housekeeping notes (honest)

1. The seven core theorems were authored in a **prior** cycle but never built or wired into the
   root — the module was sitting orphaned. This session installed the Lean toolchain from scratch
   (`elan` + `v4.30.0`; the project is **pure Lean 4 core, no Mathlib**), wired the module in, and
   verified everything.
2. **I fixed one genuine bug in the non-vacuity control.** As originally written the perturbation
   used `onPos := Ext.map (fun b => !b)` — but `Ext.map` relabels the *position type* `r.Pos ρ`,
   which need not be `Bool`, so `!b` did not typecheck. The mathematically-intended object (flip the
   two `qBool` positions) is a *precomposition* on the `qBool`-positions, `⟨p.1, z ↦ p.2 (!z)⟩`,
   matching the pattern already used by `adjCounitPerturbed` in the fixed-`q` file. Corrected, the
   control compiles and both legs behave as claimed. This is a Lean-encoding fix, not a change to
   any mathematical claim.

## Registry

`proofs/registry/pra-vs-probe-method.json`, new child `lean-q-naturality`
(`attempt`, `lean-verified`, lean = `Containers.Container.adjCounit_naturality_q`). The validator
reports one **pre-existing, unrelated** advisory (`small-case-sweeps` is `computed` under a `proved`
root) — not introduced here; left untouched per the lean-session scope.

## References

Mate/parameter-adjunction correspondence: Mac Lane, *CWM* IV.7–8 ("adjunctions with a parameter").
The object `F_q` is Niu–Spivak, *Polynomial Functors* (arXiv:2312.00990), Def. 6.59, used in
Prop. 6.68. Fixed-`q` proof + informal parameter-naturality argument:
`proofs/2026-08-30-pra-vs-probe-method.md` §4.2–§4.4.
