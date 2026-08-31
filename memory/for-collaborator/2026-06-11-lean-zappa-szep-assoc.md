# Lean: Zappa–Szép product of monoids — ZS1–ZS4 ⟺ associativity (DONE)

**Date:** 2026-06-11 (lean session)
**File:** `lean/Containers/Containers/ZappaSzep.lean` (core-only, no Mathlib)
**PR:** https://github.com/RaggedR/ghani-containers/pull/8 (`lean-zappa-szep-assoc`)
**Status:** builds with zero errors / zero warnings; `#print axioms zs_iff_assoc` → `[propext]` only.

## What is formalised

The algebraic core of the pairwise-ZS criterion
(`proofs/2026-06-10-zs-criterion-cocycle.tex`, Thm "Axioms ⟺ associativity"),
in the **monoid (single-object) form** stated in `state/LEAN.md`.

`MatchedPair`: two monoids `L`, `G` (multiplications + units + the three monoid
laws each), a left action `lact : G → L → L` (`▷`), a restriction
`ract : G → L → G` (`◁`), and the **four unit-compatibility fields**
`lact_oneG, ract_oneG, lact_oneL, ract_oneL` (= U1a,U1b,U2a,U2b) that make
`(oneL, oneG)` a two-sided unit of the product.

Product: `mul (a,g) (b,h) = (a · (g ▷ b), (g ◁ b) · h)`.

Cocycle predicates `ZS1`–`ZS4` and `Assoc` are separate `Prop`-valued defs.

**Main theorem** `MatchedPair.zs_iff_assoc :`
`(P.ZS1 ∧ P.ZS2 ∧ P.ZS3 ∧ P.ZS4) ↔ P.Assoc`.

## Proof shape (matches the informal proof coordinate-for-coordinate)

- `assoc_of_zs` (⟸): rintro the three pairs, `simp only [mul, Prod.mk.injEq]`
  to split into the two coordinate goals.
  - L-coordinate: `rw [mulL_assoc, ZS1 g b (h▷c), ZS2 (g◁b) h c]` → `rfl`.
  - G-coordinate: `rw [ZS3 (g◁b) h c, mulG_assoc, ZS4 g b (h▷c)]` → `rfl`.
  - **Uses NO unit laws** — exactly as the informal proof notes.
- `zs_of_assoc` (⟹): for each axiom, instantiate `H : Assoc` at a triple of
  pairs whose free slots are units, `simp only [mul, <relevant unit fields>,
  Prod.mk.injEq] at e`, then `exact e.1` / `e.2` (or `.symm`).
  - ZS1: `H (1,g) (a,1) (b,1)`, L-coord, units `oneL_mul, mul_oneG, lact_oneG`.
  - ZS2: `H (1,g) (1,h) (a,1)`, L-coord, units `lact_oneL, ract_oneL, oneL_mul`.
  - ZS3: `H (1,g) (1,h) (a,1)`, G-coord, units `ract_oneL, oneL_mul, mul_oneG`.
  - ZS4: `H (1,g) (a,1) (b,1)`, G-coord, units `mul_oneG, lact_oneG, ract_oneG`.

`natDirect` (direct product over `(Nat,+,0)`, trivial actions) is included as a
concrete witness that `MatchedPair` is inhabited and the axioms are
non-vacuously satisfiable; an `example` derives its `Assoc` via `zs_iff_assoc`.

## Reusable Lean techniques (logged for next lean session)

- **Coordinate split without Mathlib `ext`:** `simp only [mul, Prod.mk.injEq]`
  turns a `Prod.mk = Prod.mk` goal/hyp into a conjunction of the two coordinate
  equations. `simp` iota-reduces `(a,b).1`/`.2` automatically after unfolding the
  pair-valued def, so no manual `Prod.fst`/`Prod.snd` lemmas are needed.
- **Extracting an equational axiom from a universally-quantified law:**
  instantiate at unit values, then `simp only [mul, <unit lemmas>, Prod.mk.injEq]
  at e` collapses the specialised instance to exactly the axiom. Orientation:
  the left-bracket coordinate lands on the LHS of the conjunct, so half the
  axioms need `.symm`.
- Applying a `def`-wrapped `Prop` (`P.ZS1`) as a function (`h1 g a b`) works
  directly by defeq — no `unfold` needed.

## Grant relevance

ZS products are the *composition* tool of the equivalence-chain story (how
compositional systems combine). A machine-checked ZS ⟺ assoc is the verified
foundation under the pairwise-ZS criterion and the supply-chain / blockchain
composition narrative. Complements the object-level M2b iso
(`2026-06-10-lean-m2b-comonad-converse.md`).

## Not done / possible next Lean targets

- The **many-object (categorical) version** (vertex monoids `M_x`, hom-sets
  `T(a,b)`) — needs dependent typing; this monoid version is the honest scope
  for now and is what `LEAN.md`'s "standard form" asked for.
- Packaging the product as an actual `Monoid` instance (`oneL,oneG` unit proofs)
  — the unit halves are easy from the same unit fields; only assoc was the
  interesting part. Could be a short follow-up.
- SECONDARY from `LEAN.md`: a clean Mathlib `Cofunctor` contribution.
