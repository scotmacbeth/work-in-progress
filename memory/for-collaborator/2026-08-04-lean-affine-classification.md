# Lean: the affine classification (T1, Set-monad level) is machine-checked

**2026-08-04 LEAN session.** Target from `state/LEAN.md`: machine-check the
**positive classification** of `proofs/2026-07-30-affine-classification.md`.

## Result

`lean/Containers/Containers/AffineClassification.lean` (module
`Containers.AffineClassification`, in the root build, 44 jobs, **zero warnings,
no sorry**). It certifies **Theorem T1 at the Set-monad level**:

> A monad structure on the functor `M X = E + A×X` is *the same data* as a
> **monoid `⊗` on `N = E ⊔ A`** with unit in `A` and `E` a two-sided ideal of
> left zeros.

This is the faithful Lean port of the Python harness
`scratch/monad-comonad-transfer/affine_classify.py`. For each small size
`(|E|,|A|)` it enumerates **every** candidate datum `(unit, σ, γ)` and
machine-checks, with **0 mismatches**, that

```
  the three monad laws hold  ⟺  ⊗ is a monoid (unit in A, E a left-zero ideal).
```

## How it is modelled (Mathlib-free, Lean 4 core, matching the rest of Containers)

- `MEl nE nA X` = elements of `E + A×X` (`exc e` / `ok a x`), `deriving DecidableEq`.
- `Tbl nE nA` = the raw datum: `unit : Fin nA`, `sigma : List (Fin nE)` (flat
  `A×E→E` table), `gamma : List (Fin nE ⊕ Fin nA)` (flat `A×A→E⊔A` table).
- `mu` reads μ off the table exactly as `make_monad.mu` does: outer `exc` is a
  left zero; `ok a (exc e')` applies σ; `ok a (ok a' x)` applies γ, **carrying the
  leaf `x` iff γ lands in `A`** (drops it on abort into `E`).
- `monadOK` = the three monad laws on the test object `X = Fin 2` (matching the
  Python 2-element test set); `monoidOK` = two-sided unit + associativity of the
  induced `otimes` on `N` (the left-zero-ideal shape is baked into `otimes`'s
  type, exactly as in `make_otimes`).
- `allTbls nE nA` enumerates all `(unit ∈ A, σ, γ)` — complete up to behavioural
  equivalence (lookups only read valid indices).

## What is axiom-free vs. compiler-trusted

- **Axiom-free kernel `decide`** (`#print axioms` → `propext` only):
  `bijection_0_1, bijection_1_1, bijection_2_1, bijection_0_2, bijection_1_2`.
  These already cover **every example the paper flags**:
  - `Maybe` `1+X` — `bijection_1_1` / witness `maybeTbl`;
  - exception `E+(−)` — `bijection_2_1`;
  - the four 2-element monoids incl. writer `ℤ₂` — `bijection_0_2` / `writerZ2Tbl`;
  - the **aborting nilpotent `1+2×X`** (`z²=0∈E`), the non-cartesian
    counterexample — `bijection_1_2` / `abortingTbl`.
- **`native_decide`** (adds `Lean.ofReduceBool`): `bijection_2_2` (8192
  candidates); the kernel exceeds its heartbeat budget at that size. Clearly
  flagged in the docstring. `(3,2)`/`(1,3)` from the Python table are not
  included (enumeration cost); the Python harness remains the record for those.
- Prop-level `classification_1_1/_1_2/_2_2 : ∀ t ∈ allTbls .., monadOK t = true ↔
  monoidOK t = true` (adds `Quot.sound`, from `List.all_eq_true`/`eq_of_beq`).

## Scope (honest)

Only the **Set-monad ⟺ monoid** bijection of §2 is formalised — exactly what
`affine_classify.py` checks. The **cartesian bifurcation** of §2.3 (writer +
absorbing exceptions = non-aborting = where `T_M` lives; aborting = non-cartesian,
`T_M` undefined) is a *separate* condition, checked by `affine_e2prime.py`, and is
**out of scope** here. In particular `abortingTbl` passes *both* predicates (it is
a Set-monad and a monoid-with-left-zero-ideal); it is only excluded from the arrow
class by the cartesian test, which this file does not run. A follow-up LEAN target
could formalise `mu_cartesian` (leaf-count preservation) to complete the §2.3
bifurcation.

## Registry

`proofs/registry/effect-coeffect-arrows.json`, node
`affine-monad-monoid-bijection`: `computed → lean-verified`, `lean:
Containers.AffineClassification.classification_1_1`. Validator's 8 remaining
advisories are all pre-existing (`computed` children under `proved` parents); this
change adds none.
