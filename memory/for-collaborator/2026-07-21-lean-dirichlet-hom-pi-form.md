# Lean: Dirichlet internal hom, Π-form ≅ morphism-form — DONE (sorry-free, axiom-free)

**Date:** 2026-07-21 (lean session)
**File:** `projects/lean/Containers/Containers/DirichletHomPi.lean` (wired into root `Containers.lean`)
**Status:** ✅ compiles clean (`lake build`, 0 errors, 0 warnings); `ihomPiIso` depends on **no axioms**.

## What was formalised

The exact gap the 2026-07-21 audit flagged. `DirichletClosed.lean` verifies the closed
structure on `(Cont, ⊗, y)` via the **morphism form** of the internal hom
(`Container.ihom q r`, Shape = `ContainerMorphism q r`, NS Eq 4.79). The **Π-form** I quote
to Neil — `[q,r] = Πᵢ₌ₛq (r ◁ q[i]·y)` — was paper-only. This file proves the two
presentations are the *same container*:

```
Container.ihomPiIso (q r : Container) :
    ContainerIso (Container.ihom q r) (Container.ihomPi q r)
```

where `Container.ihomPi q r := Container.piCont q.Shape (fun i => r ◁ Container.monomialY (q.Pos i))`.

New supporting defs (both reusable):
- `Container.monomialY (A) := ⟨A, fun _ => Unit⟩` — the monomial `A·y`.
- `Container.piCont (I) (C : I → Container)` — the **arbitrary-index** container product
  (Shape = `Πᵢ (C i).Shape`, Pos = `Σᵢ (C i).Pos (s i)`). Binary `Container.prod` = the `Bool` case.
  **No Fintype needed** — the index type `q.Shape` is arbitrary.

## The surprise (worth recording)

LEAN.md predicted the shape bijection would be "only PROPOSITIONALLY invertible (choice)" and
budgeted for the `SeqProdDistrib`/`heq_sigma_mk` transport template. **It didn't materialise.**
Both round trips are literally `rfl`, and `#print axioms` reports *no axiom dependency at all*
(not even `funext`/`propext`). Reason: the `ΠΣ≅ΣΠ` shape choice is definitional under Lean 4's
eta for **structures** (`ContainerMorphism`), **`Sigma`**, and **functions**; the position
regrouping closes by **`Unit`-eta** (`x.2.2 : Unit ≡ ()`). Same pleasant register as the
morphism-form closure and the `◁` associator — the Dirichlet/`◁` data are definitionally well
behaved in a way the directed-comonad laws are not.

## Scope / honesty

- This proves the **container identity** `ihom ≅ ihomPi`. It does **not** reformalise the
  adjunction — that remains `Container.dirichlet_closure` in `DirichletClosed.lean`. Together they
  say: the uniform Π-formula denotes the same right adjoint as the morphism form, so the closed
  structure may be read off the uniform formula.
- Only the `⋆ = ×` (Dirichlet ⊗) instance is formalised. The general Day-tensor closure
  `⟦[p,q]_⋆⟧R = Πᵢ ⟦q⟧(R⋆p[i])` (proof `2026-07-15-uniform-closure-day-tensors.md`) is paper-only
  for `⋆ ≠ ×`; the vacuity sub-question is still open (`2026-07-21-closure-condition-vacuity.md`).

## Registry

Added child node `pi-form-equals-morphism-form` under `uniform-closure-formula` in
`proofs/registry/closed-day-structures.json`, `trust: lean-verified`, `lean: Container.ihomPiIso`.
(The validator still reports the *pre-existing* boundary violation on the `condition-vacuity`
in-progress node — that is honest open state from the 07-21 prove session, not mine to paper over.)
