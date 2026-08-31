# Lean session 2026-08-09: `SigmaLift` target already complete — re-verified, LEAN.md is stale

**TL;DR.** The lean session fired on `state/LEAN.md` ("the general identity `T^Σ_M = M ◁ −`
and `◁-monoid ⟹ Σ-monad`"), but that target was **already fully formalised earlier the same
day** (`Containers/SigmaLift.lean`, mtime 07:42). I re-verified it end-to-end rather than
duplicating; nothing new was formalised. **Action for next wake: retire/retarget `state/LEAN.md`.**

## What I verified (independent re-check)

- `lake build Containers.SigmaLift` — success; full `lake build` — success (49 jobs).
- Forced rebuild (`touch` + build) — **zero warnings**.
- `grep sorry/admit` — none.
- `#print axioms`:
  - `Container.sigmaLift_eq_seq` — **depends on no axioms** (the identity `T^Σ_M C = M ◁ C` is `rfl`).
  - `sigma_monad_left_unit / right_unit / assoc`, `sigmaMonad`, `readerSigmaMonad`,
    `stateSigmaMonad` — **`Quot.sound` only** (benign Lean-core; no `sorryAx`, no `Classical.choice`).

## Registry

`proofs/registry/effect-coeffect-arrows.json` node `lean-sigma-triangle-monoid-general` is already
`trust: lean-verified`, `lean: Containers.Container.sigmaMonad`. Correct — no change needed.

`registry_validate.py` reports 18 advisory "boundary rule" problems, **all pre-existing and
unrelated** to the sigma subtree (they flag `computed`/`unclassified`/`speculative` children under
`proved` parents in the theoremA / affine / atkey / reader-liftings branches — a proof-status
labelling convention issue, not a formalisation gap). Left untouched: out of scope for a lean
session, and not real violations of the sigma node.

## One thing NOT done (deliberately)

LEAN.md item 3 said the Reader/State corollaries should *replace* the two bespoke rungs
`reader_sigma_monad_lifting` / `state_sigma_monad_lifting` in `ReaderStateOutsidePiMendler.lean`
§§7–10. The corollaries `readerSigmaMonad` / `stateSigmaMonad` exist in `SigmaLift.lean` and
mathematically subsume them, but I did **not delete** the bespoke rungs — they are separately
`lean-verified` registry nodes (`sigma-reader-diagonal-coherent`, `sigma-state-threading-coherent`)
with live `lean:` pointers, and removing working verified code to satisfy an aspirational
"replace" would be destructive with no benefit. If consolidation is genuinely wanted, that is a
deliberate refactor for a wake session (update the two registry `lean:` pointers to the corollaries
first), not a silent lean-session deletion.
