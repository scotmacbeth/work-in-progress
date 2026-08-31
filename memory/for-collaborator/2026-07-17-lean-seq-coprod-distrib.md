# Lean: `◁/+` left-distributive cell machine-checked (`Container.seqCoprodDistrib`)

**Date:** 2026-07-17 (lean session)
**File:** `lean/Containers/Containers/SeqCoprodDistrib.lean`
**Registry:** `hedges-interchange-table.cell-comp-plus` → `lean-verified`

## Result

`(P + P') ◁ Q ≅ (P ◁ Q) + (P' ◁ Q)` in `Cont`, as a full `ContainerIso` (both
round-trips), sorry-free, `#print axioms` = `[Quot.sound]` only. Full `lake build`
green (25 jobs, no warnings). This is the **second** cell of Hedges' four-structure
interaction table to be formalised, sibling of `Container.seqProdDistrib` (the
`◁/×` cell).

## Why it was cleaner than the product cell

The LEAN.md prediction held exactly. The product cell (`seqProdDistrib`) needed the
`Sum.elim`-η rule (`sumElim_eta`) and one transport (`heq_sigma_mk`), because its
shape map **curried a sum-domain function** `f : (P.Pos s ⊕ P'.Pos s') → Q.Shape`.

The coproduct cell has **no such currying**: the left shape is `⟨t, f⟩` with
`t : P.Shape ⊕ P'.Shape` already a `Sum`, so the bijection just **pushes the
`inl`/`inr` tag outward across `◁`**. The fibre `Sum.elim P.Pos P'.Pos (inl s)` is
`P.Pos s` definitionally, so `f` is reused verbatim; positions are definitionally
equal in each summand, so both position maps are `fun w => w`. Both round trips are
`ContainerMorphism.ext_id` with `funext; cases <;> rfl` on shapes and
`cases <;> exact HEq.refl _` on positions. **No transport, no η-rule.**

Reused `ContainerMorphism.ext_id` from `SeqProdDistrib.lean` verbatim (imported it,
not `Sequential`, to get that lemma). `sumElim_eta` and `heq_sigma_mk` were *not*
needed here.

## Note on registry validator (pre-existing, NOT introduced here)

`python3 code/registry_validate.py proofs/registry/hedges-interchange-table.json`
reports one problem, **pre-existing and unrelated to this change**:

> root: claims 'proved' but child 'computational-verification' is 'computed'
> (boundary rule: non-dead-end children must be at least 'proved')

My edit only *upgraded* `cell-comp-plus` (`proved` → `lean-verified`), which cannot
create a downgrade violation. The flagged node is `root`/`computational-verification`
(a different subtree, line ~137). Left as-is — this is a prove/curation call about
whether the computational-verification child should be marked `proved`, not a lean
problem.

## Remaining table cells (for whoever picks up next)

The two D-cells on the LEFT variable are now both Lean (`◁/×`, `◁/+`). The harder
cells — `⊗/◁` = L (Spivak's lax interchanger, `cell-ox-comp-L`) and the `⊗`-row —
are not formalised. `⊗/◁` is genuinely lax (one-directional), so it needs a plain
`ContainerMorphism`, not a `ContainerIso`.
