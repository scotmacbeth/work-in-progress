# LEAN 2026-07-31 — The general non-branching arrow category `M = E + A×(−)`, machine-checked

**File:** `projects/lean/Containers/Containers/BiKleisliAffine.lean` (sorry-free, zero
warnings, whole `Containers` lib green — 42 jobs).
**Registry:** `effect-coeffect-arrows.json` → new node `bikleisli-affine-general`
(`lean-verified`, `lean: Containers.BiKleisliAffine.arr_assoc`).

## What this closes

LEAN.md's target: instantiate the abstract `MixedDistrib` skeleton at the **whole**
cartesian non-branching class `M X = E + A×X` (`A` a monoid, `E` a left `A`-set) —
**fusing** the two boundary generators already Lean'd separately
(`BiKleisliMaybe` = `E+(−)`, `BiKleisliWriter` = `A×(−)`) into one instance covering
the entire classified family. All four mixed-DL axioms E1′–E4′ discharged, including
the branching-obstructed **E2′** and — new relative to Writer — an **arbitrary left
action** `⊙ : A×E → E` (not just trivial). This is the machine-checked witness of
Theorems T1 + T2 of `proofs/2026-07-30-affine-classification.md`.

## Axiom footprint (clean)

- `arr_assoc`, `arr_assoc_Z2E2`: `[propext, Quot.sound]`
- `arr_unit_left`, `arr_unit_right`, `mixedDistrib`: `[Quot.sound]`

No `sorryAx`, no `Classical.choice` — exactly as LEAN.md predicted.

## The fusion structure (how Maybe ⊔ Writer glue)

`M X = E ⊕ A × X` (`Sum`-based). The `inl e` summand runs the Maybe apparatus
(nullary leaf → `PUnit` fibre, `κ` = `η^M`-padding), the `inr (a,s)` summand runs the
Writer apparatus (single leaf → `X.Pos s` fibre, `κ` = id). The monad `μ` is the
three-way split of the classification:
```
inl e            ↦ inl e            (outer exception absorbs)     -- Maybe-side
inr (a, inl e')  ↦ inl (a ⊙ e')     (log ACTS on the exception)   -- the new coupling
inr (a, inr(a',x))↦ inr (a·a', x)   (writer multiplication)       -- Writer-side
```
The middle line is the only genuinely *fused* case — it is where the left `A`-set
structure of `E` surfaces, and it forces the two extra action laws `one_act`,
`mul_act` into `MAff`'s `right_unit`/`assoc` proofs.

## Where the non-`rfl` content lives (for anyone extending this)

1. **The 3 `T_M` monad laws** (`Tright_unit`, `Tleft_unit`, `Tassoc`) — shape map
   rearranges `mul`/`act` (`one_mul`, `mul_one`, `mul_assoc`, `one_act`, `mul_act`).
   Position transport absorbed by `heq_pos : HEq (h ▸ p) p` + `eq_of_heq`, casing the
   shape so the `Tmult` position-match reduces (Writer's pattern, extended to `Sum`).
2. **Two `κ`-axiom branches** are NOT `rfl` (unlike Maybe/Writer, where the monoid was
   trivial/absent):
   - **E1′** unary branch and **E2′** deepest unary branch: leave `M.map id`, which is
     not defeq `id`; reduce by `cases p` (splitting the position `M(X.Pos s)`).
   - **E4′** nullary branch: Maybe closed this by `rfl` because its monoid was trivial;
     here `μ^M` multiplies `one · one`, so it needs `rw [W.one_mul]`. This is the one
     place a monoid law reaches into a `κ`-axiom.

Everything else is `cases … <;> rfl`.

## Grant framing

This upgrades the effects⊗coeffects paper's Lean story from "two example generators"
to "**the whole classified family `E + A×X`, machine-checked, for arbitrary monoid and
arbitrary action**". Combined with the `affine-classification` paper (T1: arrow
category exists ⇔ `M` = writer-with-absorbing-exceptions) it is the strongest formal
statement available for mode 3 of the three-modes table.

## Not done (honest)

- The **branching** (`Pf`) side (E2′ fails) remains computed-only (`scratch/…/bikleisli.py`),
  not formalised — and shouldn't be (it's not an arrow category).
- The **Set-monad-level bijection** (monads on `E+A×(−)` ⟺ monoids `N=E⊔A` with `E` a
  left-zero ideal, *including aborting ones*) is a separate, larger LEAN target — this
  file formalises only the cartesian/non-aborting sub-class where `T_M` lives.
