# LEAN 2026-07-31 — The branching obstruction (negative witness), machine-checked

**File:** `lean/Containers/Containers/BranchingObstruction.lean` (wired into
`Containers.lean` root; full `lake build` green, 43 jobs, zero warnings).
**Registry:** node `branching-obstruction-lean` under
`theoremA-reverse-branching-nogo` in `effect-coeffect-arrows.json`, trust
`lean-verified`.

## What this completes

The paper dichotomy (`proofs/2026-07-29-effect-coeffect-arrows.md`) is an **iff**:
`Arr_M` an associative arrow category ⟺ `κ` a mixed DL (E1′–E4′) ⟺ `M`
non-branching. Lean previously owned only the **⟹** half (positive class
`E+A×X`, `BiKleisliAffine.lean`, all four axioms incl. E2′). This file adds the
**⟸** half: for a *branching* `M`, `κ` **fails E2′** — machine-checked.

## Three declarations (all axiom-free — pure kernel `decide`, not even `propext`)

- `kappa_distrib_mult_fails` — the negative witness: with the powerset compositor
  `κ` = cartesian `ρ(A,B)=A×B` and multiplication `μ` = union, the E2′ coherence
  `ρ(A₁∪A₂)(B₁∪B₂) = ρA₁B₁ ∪ ρA₂B₂` is **false**, differing at the off-diagonal
  `(0,1)`: product-of-unions (full 2×2) ⊋ union-of-products (its diagonal).
- `kappa_not_distributive_over_union` — same, as a `¬∀` statement.
- `oneLeaf_E2_holds` — the non-branching mirror: at an arity-≤1 leaf `κ`
  degenerates to `id` and E2′ holds by `rfl`.

## Honest scope (please read before citing as "the iff is fully Lean'd")

This machine-checks the **position-fibre content** of E2′-failure — the
`product-of-unions ≠ union-of-products` obstruction that the full-container E2′
diagram inflates at a branching leaf (exactly the datum `entwine.py` /
`bikleisli.py` locate for `Pf` on `{a↦2,b↦1}`). It does **not** build the
full container-level `MixedDistrib.distrib_mult` inequality — that needs `Pf` as
a `Cont`-monad (= `Finset`), unavailable in Lean-core (the whole `Containers`
dev is Mathlib-free). The full-morphism non-associativity stays computed-only
(`bikleisli-pf-nonassoc`).

## Two modelling decisions worth knowing

1. **`Pf` by characteristic functions** `Pf T := T → Bool` (Mathlib-free). Over a
   `Fintype` this *is* the covariant powerset: `μ` = pointwise `or`, `κ` =
   pointwise `and` of projections. The failure is then a closed `Bool` term,
   closed by `decide` with no axioms.
2. **Why `Pf`, not `1+X²`.** `Pf` is the *minimal* branching monad whose
   Ahman–Bauer `T_M` even exists: `μ`=union is idempotent+commutative ⇒ leaf
   labels of `μ(mm)` are distinct ⇒ the `∏`-cointerpretation `μ^T` backward map
   is well-defined. For bounded-arity branching (`1+X²`) `μ^T`'s backward map is
   already ill-defined (the diagonal `μ` forgets the `A₁,B₀` slots), so the
   obstruction surfaces *earlier* and is not a clean `κ`-level E2′ inequality.
   (PROVE.md suggested `1+X²`; this is why I went with `Pf`'s fibre instead —
   flagging in case you want the bounded-arity story told separately.)

## Next Lean increment (if wanted)

To upgrade to the *full* container-level negative witness one would need a
Mathlib-free finite-powerset-as-`Cont`-monad (`Pf` via sorted-dedup lists or
char-functions over `Fintype`), then `T_M`/`μ^T`/`κ` on it, then
`¬ (mixedDistrib_Pf).distrib_mult` at the witness `X`. Sizeable; the fibre
result above already certifies the mathematical heart.
