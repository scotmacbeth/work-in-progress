# Lean: `⊗/+` Hedges cell machine-checked — `Container.dirCoprodDistrib`

**Date:** 2026-07-17 (lean session 2)
**File:** `lean/Containers/Containers/TensorCoprodDistrib.lean`
**Declaration:** `Container.dirCoprodDistrib`
**Registry:** `hedges-interchange-table.cell-ox-plus` → `lean-verified`
**Status:** sorry-free, `#print axioms` = `[Quot.sound]` only, full `lake build` green (26 jobs, 0 warnings).

## What was formalised

The `⊗/+ = D` cell of Jules Hedges' 4×4 interaction table:

    (P + P') ⊗ Q  ≅  (P ⊗ Q) + (P' ⊗ Q)   in Cont

as a full `ContainerIso` (both round-trips), where `⊗` = `Container.dirichlet`
(Dirichlet tensor: shapes `S × T`, positions the *product* `P s × Q t`) and `+` =
`Container.coprod` (shapes `S ⊕ S'`, positions `Sum.elim`).

## Why it is clean (no transport)

This is the sibling of `seqCoprodDistrib` (the `◁/+` cell) with `⊗` swapped in for
`◁`. The coproduct shape is already a `Sum`, so the bijection just pushes the
`inl`/`inr` tag across `⊗`. On the `inl` branch the LHS fibre
`Sum.elim P.Pos P'.Pos (inl s) × Q.Pos t` is *definitionally* `P.Pos s × Q.Pos t`,
which is the RHS fibre — the second Dirichlet factor `Q.Pos t` is untouched. So:
- both `onShapes` maps are a `match` on the tag,
- both `onPos` maps are the identity (`fun w => w`),
- both round trips = `ContainerMorphism.ext_id` + `cases <;> rfl` on shapes and
  `cases <;> exact HEq.refl _` on positions.

No `Sum.elim`-η rule, no transport — contrast `seqProdDistrib` (`◁/×`), whose shape
map curries a sum-*domain* function and carries one transport. Reused the helpers
`ContainerMorphism.ext_id` and `heq_sigma_mk` verbatim (imported from
`SeqProdDistrib`; `⊗` from `Dirichlet`).

## First two-sided cell

Unlike the two `◁`-based cells (one-sided only — Niu–Spivak Ex 6.56), `⊗` is
**symmetric**, so this distributive law is genuinely two-sided: the mirror
`Q ⊗ (P + P')` follows by the same argument or by composing with the Dirichlet
symmetry. Only the left law is formalised here; it already witnesses the cell.

## Registry note

The registry node id is `cell-ox-plus` (LEAN.md called it `cell-tensor-plus` — that
id does not exist). Set `trust: lean-verified`, `lean: Containers.Container.dirCoprodDistrib`.
`registry_validate.py` reports one **pre-existing, unrelated** gripe (root claims
`proved` but child `computational-verification` is `computed`); not introduced by
this change, left as-is.

## State of the table in Lean

Three D-cells now machine-checked: `◁/×` (`seqProdDistrib`), `◁/+`
(`seqCoprodDistrib`), `⊗/+` (`dirCoprodDistrib`). Natural next Lean targets:
- `×/+` — the other genuinely two-sided cell; should be equally clean (both shape
  sets `Sum`, positions `Sum.elim`), reuse the same skeleton.
- `⊗/◁`, `×/⊗` — the harder cells (lax / corrected-sign), likely transport-heavy.

STRETCH target from LEAN.md (define ⋉/⋊ Dialectica tensors in Lean and prove ⋊
associative) was **not** attempted — banked the clean cell instead, per the
"one target formalised honestly beats three sorried" rule. The exponentials over
shape sets `S_q → p[s]` in ⋉/⋊ are the flagged transport risk; that is a fresh
session's work.
