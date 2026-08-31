# M3b: comonoid converse — scratch

Target: `Container.Comonoid C` ⟹ `DirectedContainer C`, plus round-trips.
File: `projects/lean/Containers/Containers/ComonoidConverse.lean` (new).

## Strategy decision
Reuse `ComonadConverse` machinery. Build a `ContainerComonad M'` from the comonoid `M`,
prove `M'.IsComonad` from the three comonoid morphism laws, then
`M'.toDirectedContainer` gives D1–D5 + round-trips for free.

Extraction from comonoid `M : Container.Comonoid C`:
- `e s   := M.counit.onPos s ()`
- `cShape s := (M.comult.onShapes s).1`
- `cSub s   := (M.comult.onShapes s).2`
- `cVal s q r := M.comult.onPos s ⟨q, r⟩`

Key defeq claims to TEST:
1. `M'.comult t = seqExt (M.comult.toNat X t)`  — expect rfl
2. `M'.counit t = (M.counit.toNat X t).2 ()`     — expect rfl
3. `(φ.comp ψ).toNat X = ψ.toNat X ∘ φ.toNat X`   — expect rfl
4. right-counit shape projection ⟹ `cShape s = s` typechecks
5. IsComonad laws: can they be proved by funext + comonoid-law projection?

## Log
