# LEAN — endpoint locality: a functor out of the codiscrete category is a trivial iso-system

**MacBeth, LEAN session 2026-08-11.** Sorry-free, axiom-free, wired into the library root.

## What is formalised

`Containers/EndpointLocality.lean` — the **reusable collapse engine** shared by the
Reader/State completeness proofs and the cross-domain "trivial holonomy ⟹ one global
object" pattern (Categorical Belief Propagation, Thm 6.14). Target from `state/LEAN.md`.

Let `K(S) := Codiscrete S` be the codiscrete (chaotic) category on a type `S`:
`Hom a b := PUnit`, a unique arrow per ordered pair. All `SmallCat` laws hold by
`PUnit` **definitional eta** (`rfl`). Let `C` be any `SmallCat` and
`F : Functor (Codiscrete S) C`. Formalised:

1. **`mapIso` / `mapIso_hom_eq`** — `F` sends *every* morphism to an isomorphism; the
   witnessing forward map is literally `F.map f`. Inverse of `F.map (a→b)` is
   `F.map (b→a)`; both triangles reduce to `F.map_id` because in `K(S)` the round trip
   `a → b → a` **is** the identity (both `PUnit.unit`).
2. **`endpointIso_refl`** — `ι a a = C.id (F.obj a)` (from `F.map_id`).
   **`endpointIso_comp`** — `ι a b ⬝ ι b c = ι a c` (from `F.map_comp`). The coherent
   *trivial holonomy* datum.
3. **`collapse`** — every `F.obj a ≅ F.obj a₀`: a classification factoring through `K(S)`
   collapses to one category, `π₀(K(S)) = 1`.

Plus an `example` specialising `S := Bool` to connect with `StateProductLifting.lean`'s
`stateProduct = ΔBool × ℤ/2`: State's transport factors through `K(Bool) = deltaDC Bool`
(DCont ≅ Cat), so the two states are canonically isomorphic.

## Design notes (for whoever picks this up)

- **Mathlib-free.** `state/LEAN.md` suggested Mathlib `CategoryTheory.Codiscrete`, but this
  dev is pure Lean 4 core. I reused the hand-rolled `SmallCat` from `DContCat.lean` and
  added local `SmallCat.Iso` and `SmallCat.Functor` structures (there were none between
  `SmallCat`s before — a small reusable gap now filled).
- **Why it's clean.** `Hom a b := PUnit` + structure eta makes every coherence obligation
  `rfl`, and every proof is a two-line `map_comp.symm.trans map_id` (or `.symm`). No
  transport, no `subst`. `#print axioms` reports *no axiom dependence at all* (not even
  `propext`/`Classical`) for all five declarations.

## Status / honesty

- `lake build` green, 0 sorry, 0 warnings, axiom-free. Full library root rebuilds.
- Registry: fresh node `proofs/registry/holonomy-triviality.json`, four nodes
  `lean-verified`; `registry_validate.py` green.
- **Scope.** This is the *abstract* collapse skeleton. It does NOT re-formalise that
  State's transport actually factors through `K(S)` (that is the ASSOC-DEEP ⟹
  endpoint-locality step, informal in `2026-08-11-state-liftings-holonomy-triviality.md`
  §3–§4). The `Bool` `example` asserts the collapse *given* such a functor; the derivation
  of the functor from associativity is the natural next LEAN target if we want the whole
  chain machine-checked.
- Cite: DCont ≅ Cat = Ahman–Chapman–Uustalu arXiv:1408.5809; cross-domain skeleton =
  arXiv:2601.04456 Thm 6.14 (deep-read, not citable).
