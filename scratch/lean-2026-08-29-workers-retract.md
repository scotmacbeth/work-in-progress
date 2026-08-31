# LEAN scratch — Workers/BHM retract (L1–L5)

## Dependency audit (Lean 4 core, NO Mathlib; toolchain v4.30.0)

| need | where | note |
|---|---|---|
| `Container`, `ContainerMorphism` | `Containers/Basic.lean` | `onPos : (s) → D.Pos (onShapes s) → C.Pos s` — BACKWARD |
| `ContainerMorphism.id/comp/ext'` | `Containers/Cont.lean` | `comp φ ψ` = "φ then ψ"; `onPos s = φ.onPos s ∘ ψ.onPos (φ.onShapes s)` |
| `◁` = `Container.seq` | `Containers/Sequential.lean:49` | **NOT** `Composition.lean` — that module is deliberately ORPHANED (redefines `Container.I`, clashes with `Sequential`). LEAN.md's pointer is stale. |
| `⊗` = `Container.dirichlet` | `Containers/Dirichlet.lean:53` | |
| `deltaS`, `deltaDC`, `deltaS_tensor` | `Containers/StateComonad.lean:46,57,114` | |
| `DirectedContainer.coComult` | `Containers/Comonoid.lean:127` | δ : C → C ◁ C as a container MORPHISM. This is the δ of L4. |
| `deltaDC_prod` (model file) | `Containers/StateComonadTensor.lean:81` | idiom to match |

## The variance bookkeeping, spelled out

`A := ΔS ⊗ ΔT`  : Shape `S × T`,  `Pos (s,t) = S × T`   (a `Prod`)
`B := ΔS ◁ ΔT`  : Shape `(s : S) × (S → T)`, `Pos ⟨s,g⟩ = (q : S) × T`  (a `Sigma`)

**Deviation from the informal proof, found before writing a line of Lean.** The note
says "both backward maps are the identity, because all fibres involved are literally
`S × T`". In this repo `B`'s fibre is `(q : S) × (ΔT).Pos (g q)` = `Sigma (fun _ : S => T)`,
which is *isomorphic but not definitionally equal* to `Prod S T`. So the backward maps are
the canonical `Sigma ↔ Prod` swaps, not `id`. This is cosmetic (`p ↦ (p.1,p.2)` both ways,
inverse by structure-η) but it is exactly the sort of thing the shape-only argument elides,
so record it.

## Conventions to fix
- `◁` here is "G outside, F inside", so `ΔS ▷ ΔT` of the note = `deltaS S ◁ deltaS T`. Shape
  `⟨s, g⟩` = outer state + branch map `S → T`. Matches the note's `(s,g)`. ✓
- "r ∘ σ = id" in usual (diagrammatic-reversed) notation is `σ.comp r = id` in this repo.

## Log
- Statements-with-`sorry` typechecked first try ⟹ **L1 confirmed**: σ and r ARE well-typed
  container morphisms, backward maps included. That was the whole question.
- L2 `rfl`. L4 `rfl`. L3 via `congrArg onShapes` + `Bool.noConfusion` at `⟨true, id⟩`.
- L5 attempted (marked optional): `storeDiagSection_ne_coComult` and
  `storeDiagSection_not_right_counital` both first try; coassoc probed in `/tmp/co.lean` — `rfl`.
- No stuck episodes; no three-strike escalations. Clean rebuild `rm -rf .lake/build && lake build`:
  57 jobs, 0 errors, 0 warnings.
