# LEAN session 2026-08-30 — `F_q ⊣ (−)◁q`

## Dependency audit (Lean 4 core, NO Mathlib)
- `Containers.Basic`: `Container`, `Ext C X = (s : Shape) × (Pos s → X)`, `Ext.map`,
  `ContainerMorphism` (forward shapes / BACKWARD positions).
- `Containers.Cont`: `.id`, `.comp` (φ then ψ), `ext'` (shapes by rfl, positions pointwise).
- `Containers.Sequential`: `Container.seq G F` = `G ◁ F`, G OUTSIDE. Shapes
  `(t : G.Shape) × (G.Pos t → F.Shape)`; `Pos (t,f) = (q : G.Pos t) × F.Pos (f q)`.
  => `L_q p = p ◁ q = Container.seq p q`. Matches the informal convention exactly.
- `Containers.Monoidal`: `seq₂`, `whiskerLeft`, `whiskerRight μ F : G ◁ F ⟶ G' ◁ F`.
  `whiskerRight (ε p) q` is literally `ε_p ◁ q`. Nothing to build.
- NOTE: `Containers.Composition` (named in LEAN.md) is ORPHANED — it clashes with
  `Sequential` over `Container.I`. Use `Sequential`/`Monoidal`. Same `◁`, live in root.

## Objects (translation table)
| informal | Lean |
| `F_q r = (R, ρ ↦ ⟦q⟧(U_ρ))` | `leftAdj q r = ⟨r.Shape, fun ρ => Ext q (r.Pos ρ)⟩` |
| `F_q(h,χ) = (h, ρ ↦ ⟦q⟧(χ_ρ))` | `onShapes := φ.onShapes`, `onPos ρ := Ext.map (φ.onPos ρ)` |
| `η_r : ρ ↦ (ρ, c_ρ)`, `c_ρ(t,k)=t`; pos `((t,k),z) ↦ k z` | `⟨ρ, fun w => w.1⟩` / `z.1.2 z.2` |
| `ε_p : (s,c) ↦ s`; pos `a ↦ (c a, ι_a)` | `sc.1` / `fun a => ⟨sc.2 a, fun z => ⟨a, z⟩⟩` |

**The variance point (L1).** `onPos` runs `r'.Pos (h ρ) → r.Pos ρ`, so `F_q`'s action must be
`Ext.map` applied to the BACKWARD leg: `Ext q (r'.Pos (h ρ)) → Ext q (r.Pos ρ)`. A shape-only
reading would try to push `⟦q⟧` forward and fail to typecheck. This is the check LEAN.md asked for.

## Hand-computation of the triangles before touching Lean
- (B) `(ε_p ◁ q) ∘ η_{p◁q}`: shapes `⟨s,c⟩ ↦ ⟨⟨s,c⟩, fst⟩ ↦ ⟨s, fun a => (ε.onPos ⟨s,c⟩ a).1⟩
  = ⟨s, fun a => c a⟩ = ⟨s,c⟩` (η for functions). Positions: `⟨a,z⟩ ↦ ⟨⟨c a, fun z'=>⟨a,z'⟩⟩, z⟩
  ↦ (eval) ⟨a,z⟩`. Should be `rfl`.
- (A) `ε_{F_q r} ∘ F_q(η_r)`: shapes `ρ ↦ ⟨ρ,fst⟩ ↦ ρ`. Positions at `w = ⟨t,k⟩`:
  `ε.onPos ⟨ρ,fst⟩ w = ⟨t, fun z => ⟨w,z⟩⟩`, then `Ext.map (η.onPos ρ)` gives
  `⟨t, fun z => k z⟩ = w` (structure η). Should be `rfl`.

## Log

**No stuck protocol needed.** The file compiled on the FIRST `lake build`, zero errors, zero
warnings, every law `ContainerMorphism.ext' rfl (fun _ _ => rfl)`. That is itself the result:
the fibres on both sides of both triangles agree *definitionally* — no transport, no `funext`
beyond what `ext'` already does pointwise. My pre-Lean hand-computation above predicted exactly
this, and it held.

## Negative control (guarding against vacuous `rfl`)
Worry: is `ext' rfl (fun _ _ => rfl)` provable for *anything*? No. Perturbed the counit to
inject at a FIXED position `a₀ : (s : p.Shape) → p.Pos s` instead of at `a`:

    onPos := fun sc _ => ⟨sc.2 (a₀ sc.1), fun z => ⟨a₀ sc.1, z⟩⟩

The shape leg (`hs := rfl`) still succeeds — the perturbation is invisible on shapes — but the
POSITION leg fails:

    error: Type mismatch; rfl has type ?m = ?m but is expected to have type
      ((q.adjUnit (p ◁ q)).comp (whiskerRight (badCounit q p a₀) q)).onPos x₁ x
        = (ContainerMorphism.id (p ◁ q)).onPos x₁ (⋯ ▸ x)

So `ext'`'s position hypothesis is doing the real work and the triangles are non-vacuous. It
also localises the content nicely: **the triangles are a statement about positions, not shapes.**
A shape-only argument would "prove" both triangles for the wrong counit.

## Axioms
All six declarations: `[Quot.sound]` only. No `sorryAx`, no `Classical.choice`, no `propext`.
House norm met.

## Deviations from LEAN.md
- LEAN.md points at `Containers/Composition.lean` for `comp`/`I`/`associator`. That module is
  **orphaned** (documented in `Containers.lean`: it redefines `Container.I`, hard clash with
  `Sequential`). The live `◁` is `Container.seq` in `Sequential.lean`, with `seq₂`/`whiskerRight`
  in `Monoidal.lean`. Used those. Same operator, same convention (`G ◁ F` = G outside), so
  `L_q p = Container.seq p q` translates the informal `p ◁ q` verbatim.
- `lake exe cache get` NOT run and not needed: this project has **no Mathlib dependency** (empty
  `lake-manifest`), Lean 4 core only. Full root build is 58 jobs in well under a second.
- L4 (the hom-set bijection) was reached, since L1–L3 landed immediately. Packaged as two
  mutually-inverse transposition `def`s plus both round-trip theorems rather than as a bundled
  `Equiv` — the repo is Mathlib-free and has no `Equiv`, and inventing one for a single use is
  worse than two named round-trip lemmas.

## NOT formalised (honest scope)
- Naturality of `F_q` **in `q`** — the informal Theorem B explicitly flags this as unchecked.
- The `Fam(Vec^op)` version (open PROVE target).
- The right adjoint / `◁`-left-closure: does NOT exist for `|T| ≥ 2`, so there is nothing to
  formalise; attempting it would be formalising a falsehood.

## Registry
Added child `lean-adjunction` (role `attempt`, trust `lean-verified`) under root of
`pra-vs-probe-method.json`. `trustcheck.py validate` → OK. `registry_validate.py` reports ONE
problem, PRE-EXISTING and not mine: root `proved` vs child `small-case-sweeps` `computed`. That
node is deliberately `computed` (its own note: "Sub-agent/script computation: computed, never
higher"). Upgrading it to silence the advisory would be falsifying trust. Left as is.
