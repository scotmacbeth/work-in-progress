# QpfCollapse.lean — plan

## Target (LEAN.md)
Hand-rolled minimal QPF witnessing the abs/repr pattern for a **collapse/identification
locus**. Fallback path chosen because project has NO Mathlib dep — pure Lean 4 core.

## Object
Two-leaf polynomial functor `Poly X = X × X` (container: Shape=Unit, Pos _ = Bool).
Quotient by **leaf-swap** `(a,b) ~ (b,a)` = unordered pairs = Sym²X = the n=2 bag.
This swap IS the leaf-symmetry that obstructs `Arr_M` being a category
[[effect-coeffect-arrows-first-strength]].

## QPF data (core Lean, no Mathlib)
- P = Poly (polynomial functor), Poly.map
- swap, swap_swap (involution, rfl via Prod eta)
- Rel X p q := p = q ∨ p = swap q ; prove Equivalence
- setoid, Bag2 X := Quotient (setoid X)
- abs := Quotient.mk  ; repr := Quotient.out (noncomputable, choice)
- abs_repr := Quotient.out_eq  (⟦q.out⟧ = q)  ← the split-surjection law
- Bag2.map via Quotient.lift ; abs_map naturality = rfl (Quotient.lift_mk)

## Container tie (honest)
pairC : Container := ⟨Unit, fun _ => Bool⟩. Give toPoly/ofPoly round-trips so
`Ext pairC X ≅ Poly X` is machine-checked, i.e. the polynomial functor really is a
container extension.

## Citation
Avigad–Carneiro–Hudon, "Data Types as Quotients of Polynomial Functors", ITP 2019,
doi 10.4230/LIPIcs.ITP.2019.17. Theorem D: 2026-08-30-admissibility-and-the-connectedness-converse.md
