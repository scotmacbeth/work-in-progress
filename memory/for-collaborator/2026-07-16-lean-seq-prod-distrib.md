# Lean: `◁/×` left-distributive law machine-checked (Hedges D-cell)

**Date:** 2026-07-16 (lean session)
**File:** `lean/Containers/Containers/SeqProdDistrib.lean` (wired into root `Containers.lean`)
**Declaration:** `Containers.Container.seqProdDistrib`
**Status:** sorry-free, `#print axioms` = `[Quot.sound]` only, full `lake build` green (24 jobs, no warnings).

## What is proved

```
Container.seqProdDistrib (P P' Q : Container) :
    ContainerIso ((P.prod P') ◁ Q) ((P ◁ Q).prod (P' ◁ Q))
```

i.e. the **left-variable** distributive law `(P × P') ◁ Q ≅ (P ◁ Q) × (P' ◁ Q)` in `Cont`,
as a full `ContainerIso` (hom, inv, and **both** round-trips). This is the **D-cell** of the
Hedges interchange table — registry node `hedges-interchange-table.cell-comp-times`, now bumped
to `trust: lean-verified`. First machine-checked cell of the four-structure interaction table.

`×` = `Container.prod` (Cont.lean, positions `P s ⊕ P' s'`); `◁` = `Container.seq`
(Sequential.lean). Both live in the root closure, so the module just imports `Sequential`.

## The one subtlety (for anyone who reuses this)

The shape bijection curries a **sum-domain** function: `f : (P.Pos s ⊕ P'.Pos s') → Q.Shape`
↔ `(f ∘ inl, f ∘ inr)`, inverted by `Sum.elim`. One round-trip (`inv_hom`) is **definitional** —
the recursor rule `Sum.elim g g' ∘ inl = g` makes the shapes agree, so `ext' rfl` closes it.
The other (`hom_inv`) needs the η-rule `Sum.elim (f ∘ inl) (f ∘ inr) = f` (`Container.sumElim_eta`,
by `funext`+cases), which is **not** definitional, so the shape map is only *propositionally* the
identity and a dependent transport appears.

Two reusable helpers handle the transport (both proven once, by `subst`):

- **`ContainerMorphism.ext_id`** — an endomorphism that is `id` on shapes and heterogeneously
  the identity on positions equals `𝟙`. Destructure `φ` *first* (`obtain ⟨sm, op⟩`) so the shape
  map is a local var; then `subst` the shape equation collapses the fibre dependency — no `▸`
  survives. This is the right tool whenever a round-trip shape map is only propositionally id
  (contrast the unitors/associator in Sequential.lean, which are all defeq → plain `ext' rfl`).
- **`heq_sigma_mk`** — `HEq`-congruence for `Sigma.mk` under a change of fibre family
  (`β = γ → HEq w w' → HEq ⟨i,w⟩ ⟨i,w'⟩`), proven `cases hβ; cases hw; rfl`. The `hom_inv`
  position goal is exactly this: same index, same payload, fibre families related by
  `sumElim_eta`. Discharge: `cases i <;> exact heq_sigma_mk (congrArg (fun g q => Q.Pos (g q))
  (Container.sumElim_eta f).symm) (HEq.refl w)`.

This is the FIRST iso in the container library whose shape map is not definitionally invertible
(the unitors/associator/comparitor were all defeq). The `ext_id` + `heq_sigma_mk` pair is the
template for the remaining table cells whose shape isos involve `Sum`/`Prod` η.

## Primary session task also done (root-import cleanup, Robin's request)

Added `Trajectory` + `TrajectoryComposition` to the root import. `TrajectoryComposition` needed a
one-line fix: `import Trajectory` → `import Containers.Trajectory` (malformed path). Three modules
stay **deliberately** orphaned — verified each is a genuine incompatibility, not an import gap:
- `Composition` — hard clash with `Sequential` (`environment already contains 'Container.I'`).
- `Cofunctor` — hard clash with `DContCat` (`... 'DContMorphism.ctorIdx'`).
- `CoKleisli` — genuine compile errors (unsolved strength/counit goals + a syntax error ~line 166).
Documented in the root file's note. No `sorry`/`admit` used anywhere.
