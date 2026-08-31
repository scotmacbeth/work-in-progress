# LEAN done 2026-08-12 — HolonomyWitness.lean: ℤ/2-holonomy survival, axiom-free

**File:** `projects/lean/Containers/Containers/HolonomyWitness.lean` (wired into root
`Containers.lean`; full `lake build` green; `#print axioms` = **none** on all payload
declarations). Dual of the already-verified `EndpointLocality.lean` (collapse engine).

## What it certifies
The DUAL of the collapse engine: a classifier whose transport does **not** factor through
a codiscrete category refuses to collapse — holonomy survives. Machine-checks the
`update-Z2-triv-holonomy` node (the ≥2 non-isomorphic liftings of the update monad over the
same action category `Bℤ/2`) from `2026-08-11-update-monad-liftings-holonomy-full.md`.

- `BZ2 : SmallCat` — one object, `Hom = Z2`, comp = group mult (reuses `Z2` and its group
  axioms from `ReaderGroupoidLifting.lean`). This is the action category `𝔸(↓)` for a single
  **free** ℤ/2 orbit — but with the **trivial** action it is `Bℤ/2`.
- `DiscreteBool` — 2-object discrete target `D`; `Hom a b := PLift (a = b)` so all
  category/functor laws are `rfl` by definitional Prop-proof-irrelevance.
- `idF`, `swapF : D ⥤ D`; `swapF_involutive : not (not b) = b` certifies the only nontrivial
  functor law (`g·g ↦ swap∘swap = id`), so both actions are honest functors `Bℤ/2 ⥤ Cat`.
- `actTriv`, `actSwap : Z2 → Functor D D` — the two liftings `F_triv`, `F_swap`.
- **Payoff `no_natTrans_triv_to_swap`**: there is NO natural transformation `F_triv ⟹ F_swap`
  (stronger than "not iso"). Naturality at `g` gives `swap ∘ α = α`, i.e. on objects
  `not (α b) = α b`, impossible in `Bool` (`Bool.noConfusion`, no `decide`/`propext`).
  `no_natIso_triv_swap` follows.
- `BZ2_hom_not_subsingleton : ∃ a b : BZ2.Hom () (), a ≠ b` — `Bℤ/2` is NOT codiscrete
  (endo-hom-monoid `ℤ/2` has 2 elements ≠ `PUnit`), which is exactly why
  `EndpointLocality.collapse` (needs unique parallel arrows) does not apply.
- `holonomy_survives` — packaged deliverable of all three.

## Grant story (two-sided, both machine-checked)
- **codiscrete action ⟹ collapse** — `EndpointLocality.lean` (2026-08-11, verified).
- **non-codiscrete action ⟹ holonomy survives** — this file (2026-08-12, verified).

## Design notes for reuse
- New generic combinators added in `namespace Containers.SmallCat`: `Functor.id`,
  `Functor.comp` (diagrammatic). Reusable by any later SmallCat-functor development.
- The clean trick: state functor laws **pointwise on the (cased) object** rather than as
  functor equalities — avoids needing functor extensionality entirely. `actSwap_mul_obj`
  closes by `cases z <;> cases w <;> cases b <;> rfl` because `not (not true)` reduces.
- Non-iso stated as `→ False` (not Mathlib `IsEmpty`; project is core-only, no Mathlib).

## Registry
`effect-coeffect-arrows.json`: added child `holonomy-full-witness-lean`
(trust `lean-verified`, `lean = Containers.HolonomyWitness.holonomy_survives`) under
`update-monad-liftings-holonomy-full`. `registry_validate.py` shows only the 19 pre-existing
`computed`-child advisories — none from this node.
