# Lean note — Emergent holonomy witness (S₃), axiom-free

**File:** `lean/Containers/Containers/EmergentHolonomy.lean` (wired into `Containers` root).
**Registry:** `holonomy-composition-zs-bridge.json`, new node `emergent-holonomy-witness-lean`
under `part-b-prime`, `trust: lean-verified`, `lean: Containers.EmergentHolonomy.emergent_holonomy`.
**Status:** `lake build` green (54 jobs), 0 warnings, 0 `sorry`. `#print axioms` = **NONE** on every
key declaration (no `Classical`, no `propext`, no `Quot.sound` — pure `rfl`/case-analysis).

## What it certifies

The 08-12 bridge part (b) REFUTED `Stab_{P⋈P'}(s) ≅ Stab_P(s) ⋈ Stab_{P'}(s)`, with the S₃ witness:
composing two agents whose factor stabilisers at `s=1` are BOTH trivial nevertheless produces a
composite stabiliser `≅ C₂`. This Lean file is that witness as a machine-checked fact — the grant's
"orchestration synthesises holonomy" headline downgraded from computation to theorem.

- `S₃` hand-rolled (no Mathlib), acting on `X = {1,2,3}`.
- `act_mul` (108 rfl): the Cayley table `mul` genuinely IS composition of the point permutations, so
  this is honestly the symmetric group — the honesty anchor.
- Exact ZS factorisation `S₃ = P·P'`, `P = A₃ = {e,r,r2}`, `P' = {e, a=(12)}`:
  `P_inter_P'_trivial`, `factor_exists`, `factor_unique`.
- Stabilisers at 1: `stab_P_trivial`/`stab_P'_trivial` (both `{e}`), `stab_G_two_elements`
  (`Stab_G(1) = {e, c} = ⟨(23)⟩ ≅ C₂`).
- `emergent_holonomy`: the strict inclusion `Stab_P(1) ⋈ Stab_{P'}(1) = {e} ⊊ Stab_G(1)`.
- `emergent_element_factorisation`: `c = (23) = r2·a = (132)(12)`, and **neither factor fixes 1** —
  the holonomy is created by the interaction, not inherited from either side.

Completes the three-file bridge Lean story: `HolonomyWitness` (single-agent holonomy survives) +
`EndpointLocality` (trivial holonomy ⟹ collapse) + `EmergentHolonomy` (composition synthesises it).

## Heads-up for Robin (infrastructure)

The Lean toolchain was **absent** from the container at session start — no `lean`/`lake`/`elan` on
`PATH` (only stale `.lake/build` oleans from earlier sessions). I reinstalled elan non-interactively:

```
curl -sSL https://elan.lean-lang.org/elan-init.sh | sh -s -- -y --default-toolchain none
export PATH="$HOME/.elan/bin:$PATH"
cd ~/projects/lean/Containers && lake build   # fetched leanprover/lean4:v4.30.0 on first use
```

If elan keeps disappearing between sessions, it may be worth baking it into the image or the
`agent-loop.sh` env so `/lean` sessions don't spend budget reinstalling.
