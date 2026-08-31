# LEAN done: the monad→comonad transfer comonad is machine-checked

**Date:** 2026-07-25 (LEAN session). **For:** Robin / Neil.

## What landed

`lean/Containers/Containers/MonadComonadTransfer.lean` — sorry-free, wired into
the root `Containers.lean`, full `lake build` green (37 jobs, zero warnings,
Lean v4.30.0). This is the Lean formalisation of Neil's Chapter 4 item 2 (the
transfer `G(S,P) = (S, M∘P)`), paper proof
`proofs/2026-07-25-monad-comonad-transfer.md`.

## The shape of the formalisation

- **`SetMonad`** — a monad on `Type` bundled as a structure with no Mathlib
  dependency: `obj`/`map` + functor laws, `η`/`μ`, their naturality squares, and
  the **three monad laws as fields** in pointwise form
  (`right_unit : μ (η x) = x`, `left_unit : μ (map η x) = x`,
  `assoc : μ (μ x) = μ (map μ x)`).
- **`SetMonad.G`** (objects) and **`SetMonad.onMor`** (morphisms) — the transfer
  functor; `onMor_id`/`onMor_comp` reduce to `M`'s functor laws.
- **`SetMonad.counit`** (backward = `η`) and **`SetMonad.comult`** (backward =
  `μ`) as `ContainerMorphism`s; `counit_natural`/`comult_natural` reduce to
  `η`/`μ` naturality.
- **The three comonad laws** — `counit_left`, `counit_right`, `coassoc`.

## The one thing worth seeing

Every comonad law proof is three lines:

```lean
refine ContainerMorphism.ext' rfl ?_
intro s p
exact M.right_unit p        -- resp. left_unit, assoc
```

`ext'` with `rfl` on shapes (all of `G`, `ε`, `δ` are identity-on-shapes, so
**no transport appears** — unlike the ◁-comonad / directed-container story) drops
each law straight onto a single fibre `M (P s)`, where it is *definitionally* the
correspondingly-named monad law:

| comonad law   | Lean name       | monad law field |
|---------------|-----------------|-----------------|
| counit-left   | `counit_left`   | `right_unit` (`μ ∘ ηM = id`) |
| counit-right  | `counit_right`  | `left_unit`  (`μ ∘ Mη = id`) |
| coassociativity | `coassoc`     | `assoc`      (`μ ∘ μM = μ ∘ Mμ`) |

This is the paper's §1.3 made literal: the position-contravariance is doing all
the work of "reversing arrows," so a monad law read backward is a comonad law.
It mirrors `DirichletComonoid.lean` — all seven results are `Quot.sound`-only
(`#print axioms`), no `sorry`, no `Classical`.

## Scope / what is NOT formalised

Only the coordinate proof (paper §1). Deliberately paper-only for now:
- the coclosure / left-Kan identification `G = {M/-} = Lan_{(-)} M` (§3) — needs
  the `◁`-left-coclosure object, a bigger port;
- the `Poly` descent (§4) and the fibred-mechanism reformulation (§2).

The converse (comonad `W` on `Set` → monad `H(S,P)=(S,W∘P)`) is the formal dual
and would be a near-copy of this file with `(η,μ) ↝ (ε_W, δ_W)` — cheap next
target if wanted, but I left it since the flagship is the monad→comonad direction
Neil asked for.

## Registry

`proofs/registry/monad-comonad-transfer.json`: added child
`lean-coordinate-proof` under `coordinate-proof`, `trust = lean-verified`,
`lean = Containers.SetMonad.counit_left`. Validates with trustcheck.
