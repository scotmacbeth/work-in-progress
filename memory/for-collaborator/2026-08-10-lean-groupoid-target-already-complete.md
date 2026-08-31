# Lean session 2026-08-10: `ReaderGroupoidLifting` target already complete — re-verified, LEAN.md is stale

**TL;DR.** The lean session fired on `state/LEAN.md` ("the ℤ/2 groupoid: a genuine non-∏/non-Σ
proof-relevant monad lifting of Reader, machine-checked"), but that target was **already fully
formalised earlier the same day** (`Containers/ReaderGroupoidLifting.lean`, mtime 07:33). I
re-verified it end-to-end rather than duplicating; nothing new was formalised.
**Action for next wake: retire/retarget `state/LEAN.md`.**

**This is the SECOND consecutive lean session to fire on an already-complete target** (cf.
`2026-08-09-lean-sigma-target-already-complete.md`). The trigger-file lifecycle is leaking:
the same day's earlier session finishes the formalisation but LEAN.md is not consumed/refreshed,
so the *next* lean heartbeat re-runs a done target. Worth a wake-session fix — e.g. have the lean
skill delete/rename `state/LEAN.md` on green build, or have wake stamp a target-hash it checks.

## What I verified (independent re-check)

- `lake build Containers.ReaderGroupoidLifting` — success (10 jobs). No Mathlib dep (pure Lean 4
  core), so `lake exe cache get` is N/A (`unknown executable cache`).
- Forced rebuild (`touch` + build) — **zero warnings, zero errors**.
- `grep sorry/admit/axiom` — only in docstrings ("no `sorry`"); none in code.
- `#print axioms` (namespace `Containers.ReaderGroupoid`):
  - `reader_groupoid_is_neither_pi_nor_sigma` (the packaged deliverable) — **depends on no axioms**.
  - `readerGroupoid_not_sigma`, `readerGroupoid_not_pi` — **no axioms**.
  - `readerGroupoid_left_counit / right_counit / coassoc` (the three comonad-law wrappers) —
    **`Quot.sound` only** (benign Lean-core funext; no `sorryAx`, no `Classical.choice`).

## The separations are genuine (not vacuous)

- **Not Σ.** `readerGroupoidLifting.Pos () = Z2` has two distinct elements (`Z2.e_ne_g`) with a
  nontrivial composite `g * g = e` (`Z2.g_mul_g`), contrasted against `discreteOneObject =
  deltaDC Unit`, whose `Pos ()` is `Unit` — a real subsingleton (`discrete_hom_subsingleton`,
  `rfl`). Non-discrete vs discrete: honest structural separation.
- **Not ∏.** Pairs `reader_kappa_not_total` (the DROP certificate from
  `ReaderStateOutsidePiMendler`, Ahman–Bauer arXiv:2409.17664 Thm 6.3 — Reader's ∏-lifting has no
  μ) with the groupoid's nontrivial `g * g = e`. Two liftings, one carrying multiplicative
  structure the other provably lacks.

## Registry

`proofs/registry/effect-coeffect-arrows.json` node `reader-groupoid-lifting-lean` (child of
`reader-liftings-are-categories`) is already `trust: lean-verified`,
`lean: Containers.ReaderGroupoid.reader_groupoid_is_neither_pi_nor_sigma`. Correct — no change.

`registry_validate.py` reports 19 advisory "boundary rule" problems, **all pre-existing and
unrelated** to the groupoid node (they flag `computed`/`unclassified`/`speculative` evidence
children under `proved` parents across the theoremA / affine / atkey / reader-liftings branches — a
proof-status labelling convention, not a formalisation gap). My node does not appear in the list.
Left untouched: out of scope for a lean session, and not real violations.
