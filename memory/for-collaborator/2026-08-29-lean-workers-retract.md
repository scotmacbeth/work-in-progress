# LEAN 2026-08-29 — Workers/BHM retract: L1–L5 all landed, sorry-free

**File:** `lean/Containers/Containers/WorkersRetract.lean` (wired into root `Containers.lean`).
**Build:** `lake build` — 0 errors, 0 warnings, 0 `sorry`. Lean 4 core v4.30.0, no Mathlib.
**Source proof:** `proofs/2026-08-29-workers-retract-of-bhm-grading.md`.
**Registry:** `proofs/registry/workers-retract-of-bhm-grading.json` — `P2-retract`,
`P3c-diagonal-collapse`, `P3d-not-oplax-full-set` upgraded to `lean-verified`; new child
`L-lean-workers-retract`. Both `trustcheck.py` and `registry_validate.py` pass.

## Axiom audit (verbatim)

```
'Containers.storeRetraction_storeSection' does not depend on any axioms
'Containers.storeSection_storeRetraction_ne' does not depend on any axioms
'Containers.storeRetraction_coComult' does not depend on any axioms
'Containers.storeDiagSection_ne_coComult' does not depend on any axioms
'Containers.storeDiagSection_coassoc' depends on axioms: [Quot.sound]
'Containers.storeDiagSection_not_right_counital' does not depend on any axioms
```

`Quot.sound` enters `storeDiagSection_coassoc` only through `Container.associator`
(`Sequential.lean`). No `sorryAx`, no `Classical.choice`, no `propext`.

## What landed

| target | declaration | proof |
|---|---|---|
| L1 σ, r as morphisms | `storeSection`, `storeRetraction` | elaborate — this *is* the variance claim |
| L2 `r ∘ σ = id_A` | `storeRetraction_storeSection` | `rfl` |
| L3 `σ ∘ r ≠ id_B` | `storeSection_storeRetraction_ne` | `Bool` witness `⟨true, id⟩` |
| L4 `r ∘ δ = Δ(d)` | `storeRetraction_coComult` | `rfl` |
| L5(1) `δ' ≠ δ` | `storeDiagSection_ne_coComult` | `Bool` witness |
| L5(2+) δ' coassoc | `storeDiagSection_coassoc` | `rfl` |
| L5(2−) δ' not counital | `storeDiagSection_not_right_counital` | `Bool` witness `⟨false,()⟩` at shape `true` |

L5 was flagged optional in `state/LEAN.md`. It went through, including the positive
coassociativity half, so the full "coassociative but not counital" dichotomy is now
machine-checked rather than only computed at `n = 2, 3`.

## The one correction the type checker surfaced

The paper proof (§1, "Definition") says of σ♯ and r♯:

> Both are well-typed: all fibres involved are literally `S×T`, so the identity
> position maps typecheck.

**"Literally" is wrong in `Cont`.** With `◁ = Container.seq`:

- `A.Pos (s,t) = (ΔS).Pos s × (ΔT).Pos t = S × T` — a `Prod`;
- `B.Pos ⟨s,g⟩ = (q : (ΔS).Pos s) × (ΔT).Pos (g q) = (q : S) × T` — a `Sigma`.

`Sigma (fun _ : S => T)` is isomorphic but **not definitionally equal** to `Prod S T`,
so the backward maps are the canonical swaps `p ↦ (p.1, p.2)` and `p ↦ ⟨p.1, p.2⟩`, not
`id`. They are mutually inverse by structure η, which is exactly why L2 still closes by
`rfl` — **the theorem is unaffected.** But the justification in the note is not the one
Lean accepts, and this is the sort of elision that a shape-only argument makes. Worth a
one-line amendment to the paper proof if it is ever written up.

Everything else matched the informal argument step for step, including the reversal in
`comp` (`(r∘σ)♯ = σ♯ ∘ r♯_{σ₁(s,t)}`) — which is what made the retract, rather than only
the shape-level collapse, come out `rfl`.

## Stale pointer in `state/LEAN.md`, for next time

LEAN.md directed me to `Containers/Composition.lean` for `Container.comp` (`◁`). That
module is **deliberately orphaned** — it redefines `Container.I` and hard-clashes with
`Sequential.lean`, per the note at the foot of the root `Containers.lean`. The live `◁`
is `Container.seq` (`Sequential.lean:49`). No harm done; caught in the dependency audit
before any Lean was written.

## Not attempted (by instruction)

The P3a/P3b oplax/lax hexagons. Registry node `P3ab-coherence` remains at `proved`
(verified computationally to `(2,3,2)`), not `lean-verified`.
