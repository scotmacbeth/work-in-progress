# 2026-07-30 — The non-branching class is *writer + absorbing exceptions*, and E2′ holds throughout it

**For Neil / Robin.** PROVE session finishing the effect–coeffect arrows result (T1 + T2 of
07-30 PROVE.md). Full write-up: `proofs/2026-07-30-affine-classification.md`. TL;DR:

## What's new

The 07-29 theorems said the arrow category `Arr_M = Cont(G_M p, T_M q)` exists **iff `M` is
non-branching** — a *negative* statement. This session gives the **positive** class and closes
the last mechanical gap.

**T1 (positive classification).** For a cartesian (∏-cointerpretation) Set-monad `M`, TFAE:
(i) `Arr_M` exists; (ii) `M` non-branching; (iii) `M ≅ E + A×(−)`; **(iv) `M` is a
*writer-with-absorbing-exceptions* monad**: `M X = E + A×X` with `A` a monoid, `E` a **left
`A`-set**, writer unit `η(x)=(e,x)`, and `μ` = writer-multiply on the `A`-part, throw-and-
absorb on the `E`-part (the log `a` acts on the thrown exception, `a ⊙ e ∈ E`). So the mode-3
obstruction now has a *named class*: **the arrow calculus exists iff the effect monad is
exception–writer**.

**The subtlety worth knowing (corrects the PROVE.md guess).** There are TWO levels:
- *Set-monad level:* monad structures on the functor `E+A×(−)` = **monoids on `N = E ⊔ A`**
  with unit in `A` and `E` a two-sided ideal of **left zeros**. Here `A` need **not** be a
  submonoid — two unary shapes may *abort* into an exception (e.g. the nilpotent monoid
  `z²=0`, `M X = 1+2×X`). PROVE.md's "A a monoid" is the *non-aborting* special case.
- *Polynomial (cartesian) level = where `T_M` lives:* cartesian ⟺ **non-aborting** ⟺ `A` a
  submonoid + `E` a left `A`-set. The **aborting** monads are genuine Set-monads but their `μ`
  **destroys a leaf**, so it is not cartesian and Ahman–Bauer's `T_M` has no well-defined
  multiplication (the backward map `1 → P(s)` has no canonical value). They are outside the
  arrow story. *This is why the arrow class is exactly writer+exception and nothing more.*

**T2 (E2′ closed for the whole class).** For every non-branching `M`, every `P⋆`-product has
`≤ 1` factor, so `κ` is the identity at unary shapes and the unit `η^M` at nullary shapes. All
four mixed-DL axioms E1′–E4′ then hold: E2′ degenerates to **associativity of `N`**; the
`≥2`-leaf "union-of-products ≠ product-of-unions" obstruction never forms. This closes the
"E2′ general-`j`" gap flagged in every recent cycle — for non-branching `M`, `j` is always the
trivial ≤1-leaf restriction.

## Evidence (all in `scratch/monad-comonad-transfer/`)

- `affine_classify.py`: **exact bijection** monad-on-`E+A×(−)` ⟺ monoid-on-`N`-with-left-zero-
  ideal, 0 mismatches up to `|E|=3,|A|=2` (911250 candidates) and `|A|=3`.
- `affine_e2prime.py`: `mu_cartesian` True for `2+3×X` (`A=ℤ/3`) and `1+2×X` (`A=ℤ/2`), False
  (leaf destroyed) for aborting monads; **E1′,E3′,E4′,E2′ all PASS** for both on `U1, A1, A3`;
  biKleisli arrow-associativity **0 violations** (15625 / 729 triples).

## Honest grade / gaps

- (ii)⇔(iii)⇔(iv) and the monad pin: **proved** (bijection machine-verified).
- Cartesian bifurcation: **proved** (cartesianness = non-aborting, with the ill-definedness of
  `T_M` on aborting monads exhibited).
- T2 / E2′: **proved** conceptually (degeneracy to ≤1-factor) + verified; the line-by-line
  E1′/E3′/E4′ nullary chase over an arbitrary container is degenerate and left machine-checked
  rather than written out (Gap 1).
- Terminology: "affine" clash flagged — arity ≤ 1 (`M1` unrestricted) ≠ Kock-affine
  (`M1 ≅ 1`, which forces `M = Id`).

## For the paper / grant

Mode-3 row of the three-modes table now reads with a positive class:
**effect–coeffect | arrow `G_M p → T_M q` | exists iff `M` non-branching | `M = E + A×X` =
writer `A` + absorbing exceptions `E`.** Natural next steps: Lean the Set-monad⟺monoid
bijection; instantiate `MixedDistrib` at a concrete non-branching `M` (e.g. `Writer/ℤ₂`) to get
the first machine-checked *associative* arrow category on `Cont`.
