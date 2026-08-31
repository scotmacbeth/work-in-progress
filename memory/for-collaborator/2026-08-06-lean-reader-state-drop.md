# LEAN cert — Reader/State outside ∏-Mendler (the DROP rung), machine-checked

**2026-08-06 LEAN session (MacBeth).** Target from `state/LEAN.md`. Status: **done, sorry-free,
axiom-free, wired into root, `lake build` green (47 jobs).**

## What was formalised

`lean/Containers/Containers/ReaderStateOutsidePiMendler.lean` — the finite combinatorial core of
`proofs/2026-08-06-state-reader-ladder-census.md` (registry node
`state-reader-outside-pi-mendler`, PROVE-refutation of the census claim). It certifies the **DROP**
rung of the non-cartesian-μ trichotomy: Reader and State have `κ_μ` **non-total**, so no
multiplication laxator `j` exists ⟹ they are **not ∏-Mendler**.

The machine-checked predicate is the pointwise Lemma-1 criterion "a total label-preserving
`κ_μ : I(mm) → lv(μ mm)` exists iff every inner-leaf token has some μ-leaf of matching label":

- `ReaderKappaTotal G := ∀ i : Bool×Bool, ∃ e : Bool, G e e = G i.1 i.2` (μ = diagonal).
- `reader_kappa_not_total` : `¬ ReaderKappaTotal Gw` for `Gw = ![![l0,l0],![l1,l0]]`
  (= `![![0,0],![1,0]]`, the LEAN.md witness). Explicit dropped token in `reader_diagonal_drops`:
  off-diagonal `(true,false)` has label `l1`, the diagonal `μGw` is all `l0`.
- `state_kappa_not_total` / `state_threading_drops` : same DROP for State (`S=Bool`, threading;
  inner token `(false,true)` label `l2` dropped, `μFw` all `l0`).
- `reader_kappa_total_of_const` : honest non-vacuity — constant `G` **is** total, so the failure is
  the *label choice* (census §2), not the diagonal structure itself.
- `reader_state_outside_pi_mendler` : bundles all four.

## Two deliberate choices (worth knowing)

1. **Bespoke `Lbl` (3-elt inductive, `deriving DecidableEq`) instead of `Fin 3`.** `Fin`'s
   `DecidableEq` routes `decide` through `propext`; the enumeration keeps every theorem
   **axiom-free** (`#print axioms` = no axioms, all six), matching the repo bar set by
   `BranchingObstruction.lean`. `Lbl ≅ Fin 3`, `l0/l1/l2 = 0/1/2`; documented in the file.
2. **Scope = the finite datum, not the Yoneda reduction.** Lemma 1 (Yoneda: `j` natural ⟺ `κ_μ`
   total) is `census` §1 / registry node `kappa-totality-yoneda` (paper-proved). The Lean file
   certifies the combinatorial core the reduction lands on — same division of labour as
   `TMCartesianBoundary.lean` (which certifies the fibre datum, not the container-level assembly).

## Boundary picture now Lean-covered

- cartesian rung: `TMaybe_onMor_cartesian` (Maybe) — `TMCartesianBoundary.lean`.
- MERGE rung: `PfWitness` (Pf, `κ_μ` total non-injective, INSIDE ∏-Mendler) — same file.
- **DROP rung: Reader/State (this file).** SYMMETRY rung (Bag) still paper-only.

## Registry

Added child `reader-state-drop-lean` (`trust: lean-verified`,
`lean: Containers.ReaderStateOutsidePiMendler.reader_state_outside_pi_mendler`) under
`state-reader-outside-pi-mendler`. `registry_validate.py` shows only the 9 **pre-existing**
advisory "computed child under proved parent" notes (incl. the sibling `kappa-totality-compute`);
my node introduced none.
