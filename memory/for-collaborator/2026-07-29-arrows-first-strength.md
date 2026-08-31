# For Neil — the effect–coeffect arrows are a genuine Hughes arrow / Freyd category (iff non-branching)

**2026-07-29 (pm), following the morning's Theorem A.** Full write-up:
`proofs/2026-07-29-effect-coeffect-arrows-first.md`. Harness:
`scratch/monad-comonad-transfer/arrows_first.py`.

## What I proved
The morning gave the biKleisli **category** `Arr_M` (arrows `Gp→Tq`, category iff `M`
non-branching). This session supplies the arrow interface and closes the identification:

> **With the cartesian product `×` on `Cont` as tensor, `Arr_M` is a genuine Hughes arrow /
> Freyd category — with `arr(φ)=η^T∘φ∘ε` and `first(f)=τ∘(f×id)∘σ` — iff `M` is non-branching.**

Two clean structural lemmas underneath:

- **Lemma 2 — coeffects are always costrong.** `σ_G:G_M(p×c)→G_M p×c` is natural for **every**
  `M` (its positions are a single `M`-structure, no product-over-leaves — `M(inl)`+`η∘inr`).
- **Lemma 3 — effects are strong iff non-branching.** A **natural** tensorial strength
  `τ_T:T_M(-)×(=)⇒T_M(-×=)` for `×` exists **iff `M` non-branching**. The backward map is the
  distributivity `∏_b(A_b⊔C)→(∏_b A_b)⊔C`; Yoneda forces it to a *single leaf-projection* on the
  all-`inr` slice, and a leaf-transposition (`Pf`) or reindexing (`List`) then contradicts that
  fixed choice.

## The one subtlety I want to flag (I corrected myself mid-session)
I first claimed "no *total* strength for branching `M`". **Wrong** — a *total* strength exists
(the "priority"/leftmost-leaf rule), and it even satisfies the strength **multiplication** axiom.
What it fails is **naturality** (leaf-symmetry). So the honest obstruction is a *symmetry*
obstruction, and — this is the nice part — it is **genuinely distinct from the associativity/`E2′`
obstruction** (which is `μ^T`-merging). Branching disables the arrow through **two independent
axioms**: `>>>`-associativity via merging, and the effect strength via leaf-symmetry. Redundant
obstruction, two different arguments, same threshold `|lv|≤1`.

## Why this is (I think) paper-shaped for you
It sharpens your "genuine unification of effects and coeffects" into a crisp asymmetry:
*coeffect comonads thread past an untouched wire unconditionally; effect monads thread past it iff
they don't branch.* And the KRU Thms 1/2/3 degeneracy (extensive-category collapse) is the same
boundary by a different engine — convergent evidence that **branching is the universal obstruction
to sequentially composing effects with coeffects on containers**.

## Status / honest gaps
- Lemmas 2, 3 and the main iff: **proved** (Yoneda + explicit constructions + machine witnesses;
  registry `arrow-freyd-costrength` promoted speculative→proved, validator green).
- Hughes laws L3–L8: **exhaustive** for `Maybe` (exception/`E`) and `Writer/ℤ₂` (writer/`A`) —
  the two spans of the affine normal form `MX≅E+A×X`; packaging cites the standard biKleisli-arrow
  theorem. A symbolic L3–L8 for arbitrary affine `M` is mechanical and not written out.
- `(⇒)` done by two symmetry-types (`Pf` transposition, `List` merge); a single uniform argument
  for every branching monad is not spelt out.

## Questions for you
1. Do you want the **Dirichlet `⊗`** story too (a non-cartesian *monoidal* arrow), or is the
   cartesian Freyd reading the one for the book/paper? I fixed `×` because Freyd wants a cartesian
   base.
2. Is the "two faces of branching" (merging vs symmetry) worth its own subsection, or a remark?
3. Lean target: `σ_G` costrength and the `τ_T` non-branching strength look very Lean-able (defeq-ish,
   like the transfer). Worth a `LEAN.md`?
