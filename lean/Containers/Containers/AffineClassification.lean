/-!
# The affine classification: monads on `E + A×(−)` are monoids with a left-zero ideal

This file machine-certifies **Theorem T1 (Set-monad level)** of
`proofs/2026-07-30-affine-classification.md` (MacBeth), the positive face of the
effect–coeffect dichotomy:

> A monad structure on the polynomial functor `M X = E + A×X` is *the same data*
> as a **monoid structure `⊗` on `N := E ⊔ A`** whose unit lies in `A` and in
> which `E` is a **two-sided ideal of left zeros** (`e ⊗ n = e`, `n ⊗ e ∈ E`).

Here `E` is the set of nullary shapes (arity `0`) and `A` the set of unary shapes
(arity `1`); "arity `≤ 1`" is exactly *non-branching*, which by Theorem A
(`2026-07-29-effect-coeffect-arrows.md`) is the condition for the effect–coeffect
arrow category `Arr_M` to exist. The effect monad `T_M(S,P) = (M S, P⋆)` on which
the arrow story rests is Ahman–Bauer, arXiv:2409.17664, Thm 6.3 (cartesian `M`).

The *cartesian* sub-class (`A` a submonoid, `E` a left `A`-set — the
writer-with-absorbing-exceptions monads, where `T_M` actually lives) is a proper
restriction of this Set-monad-level bijection: the aborting monads (a unary shape
times a unary shape landing in `E`, e.g. the nilpotent `1 + 2×X`) are genuine
Set-monads but non-cartesian. That bifurcation is a *separate* check
(`scratch/.../affine_e2prime.py`) and is **out of scope here**: this file
formalises exactly the Set-monad ⟺ monoid bijection of §2, matching the Python
harness `scratch/monad-comonad-transfer/affine_classify.py` (exhaustive, 0
mismatch).

## What is proved

For each small size `(|E|,|A|)` we enumerate **every** candidate multiplication
datum `(unit, σ, γ)` and machine-check that

```
  the three monad laws hold   ⟺   ⊗ is a monoid (unit in A, E a left-zero ideal)
```

with **zero mismatches** — an exact bijection between the two decision procedures.
The kernel-`decide` theorems (`bijection_0_1 … bijection_1_2`) are **axiom-free**
and already cover *every* example the paper flags:

* `|E|=1, |A|=1`  — the `Maybe` monad (`bijection_1_1`);
* `|E|=2, |A|=1`  — the exception monad `E + (−)` (`bijection_2_1`);
* `|E|=0, |A|=2`  — the four two-element monoids, incl. writer `ℤ₂` (`bijection_0_2`);
* `|E|=1, |A|=2`  — includes the *aborting* nilpotent `1 + 2×X` monad
  (`z² = 0 ∈ E`), the non-cartesian counterexample (`bijection_1_2`).

`bijection_2_2` extends the certification to `|E|=|A|=2` (8192 candidates) via
`native_decide` (compiler-trusted, `Lean.ofReduceBool`); the kernel cannot reduce
it within the heartbeat budget.

The Prop-level reading is extracted in `classification_*`: for every enumerated
datum, *the monad laws hold iff the monoid-with-left-zero-ideal laws hold*.

Lean 4 core, no Mathlib, matching the rest of `Containers`. No `sorry`.
-/

namespace Containers
namespace AffineClassification

/-! ## The functor `M X = E + A×X` and its finite data -/

/-- An element of `M X = E + A×X`, with `E = Fin nE` the nullary shapes and
`A = Fin nA` the unary shapes: `exc e` is `('e', e)` (0 leaves), `ok a x` is
`('a', a, x)` (one leaf labelled `x`). -/
inductive MEl (nE nA : Nat) (X : Type) where
  | exc : Fin nE → MEl nE nA X
  | ok  : Fin nA → X → MEl nE nA X
deriving DecidableEq

/-- The raw multiplication datum `(unit, σ, γ)` for a candidate monad on
`E + A×(−)`, in the schematic form forced by naturality (paper §2.1):

* `unit : A` — the writer-style unit `η_X(x) = ok unit x`;
* `sigma : A×E → E` — the value of `μ` on `ok a (exc e)` (log acts on exception),
  stored flat, indexed by `a*nE + e`;
* `gamma : A×A → E ⊔ A` — the value of `μ` on `ok a (ok a' x)`: abort into `E`
  (`inl`, dropping the leaf `x`) or carry into `A` (`inr`, keeping `x`), stored
  flat, indexed by `a*nA + a'`.

Enumerating all such tables over the exact lengths `nA*nE` and `nA*nA` and full
codomains covers every monad/monoid structure up to behavioural equivalence (the
lookups below only ever read valid indices). -/
structure Tbl (nE nA : Nat) where
  unit  : Fin nA
  sigma : List (Fin nE)
  gamma : List ((Fin nE) ⊕ (Fin nA))

variable {nE nA : Nat}

/-- `σ(a, e) ∈ E`. The default `e` is never used (index always in range). -/
def sigmaLk (t : Tbl nE nA) (a : Fin nA) (e : Fin nE) : Fin nE :=
  t.sigma.getD (a.val * nE + e.val) e

/-- `γ(a, a') ∈ E ⊔ A`. The default `inr a` is never used (index always in range). -/
def gammaLk (t : Tbl nE nA) (a a' : Fin nA) : (Fin nE) ⊕ (Fin nA) :=
  t.gamma.getD (a.val * nA + a'.val) (Sum.inr a)

/-! ## The monad structure read off the table -/

/-- Functorial action: `M f` relabels the single leaf, fixes exceptions. -/
def fmap {X Y : Type} (f : X → Y) : MEl nE nA X → MEl nE nA Y
  | .exc e => .exc e
  | .ok a x => .ok a (f x)

/-- Writer-style unit `η_X(x) = ok unit x` (paper §2.1). -/
def eta {X : Type} (t : Tbl nE nA) (x : X) : MEl nE nA X := .ok t.unit x

/-- Multiplication `μ : M (M X) → M X` (paper §2.1 / `affine_classify.py`):
an outer exception is a left zero; `ok a (exc e')` applies `σ`; `ok a (ok a' x)`
applies `γ`, carrying the leaf `x` iff `γ` lands in `A`. -/
def mu {X : Type} (t : Tbl nE nA) : MEl nE nA (MEl nE nA X) → MEl nE nA X
  | .exc e => .exc e
  | .ok a z =>
    match z with
    | .exc e' => .exc (sigmaLk t a e')
    | .ok a' x =>
      match gammaLk t a a' with
      | .inl e'' => .exc e''
      | .inr a'' => .ok a'' x

/-- Enumerate `M X` from an enumeration `Xs` of `X`: all exceptions, then all
`ok a x`. -/
def objList {X : Type} (Xs : List X) : List (MEl nE nA X) :=
  (List.finRange nE).map .exc ++
  (List.finRange nA).flatMap (fun a => Xs.map (fun x => .ok a x))

/-- The concrete test object `X = Fin 2` (matching the Python harness's
two-element test set — one leaf label suffices, two is ample). -/
def X2 : List (Fin 2) := List.finRange 2

/-! ## The three monad laws as decidable `Bool`s -/

/-- Left unit `μ ∘ M η = id` on `M X`. -/
def leftUnitOK (t : Tbl nE nA) : Bool :=
  (objList X2).all (fun m => decide (mu t (fmap (eta t) m) = m))

/-- Right unit `μ ∘ η_M = id` on `M X`. -/
def rightUnitOK (t : Tbl nE nA) : Bool :=
  (objList X2).all (fun m => decide (mu t (eta t m) = m))

/-- Associativity `μ ∘ M μ = μ ∘ μ_M` on `M (M (M X))`. -/
def assocOK (t : Tbl nE nA) : Bool :=
  let mxs := objList (nE := nE) (nA := nA) X2
  let mmxs := objList mxs
  let mmmxs := objList mmxs
  mmmxs.all (fun mmm => decide (mu t (fmap (mu t) mmm) = mu t (mu t mmm)))

/-- The functor `E + A×(−)` with datum `t` is a monad. -/
def monadOK (t : Tbl nE nA) : Bool := leftUnitOK t && rightUnitOK t && assocOK t

/-! ## The induced binary operation on `N = E ⊔ A` and its monoid laws -/

/-- Enumeration of `N = E ⊔ A`. -/
def NList : List ((Fin nE) ⊕ (Fin nA)) :=
  (List.finRange nE).map .inl ++ (List.finRange nA).map .inr

/-- The induced operation `⊗` on `N`: `E` is left-zero by construction, `a ⊗ e =
σ(a,e) ∈ E`, `a ⊗ a' = γ(a,a')`. The left-zero-ideal shape (`E` absorbs on the
left, `N ⊗ E ⊆ E`) is baked into the types, exactly as in `make_otimes`; the only
live conditions are the monoid axioms below. -/
def otimes (t : Tbl nE nA) :
    (Fin nE) ⊕ (Fin nA) → (Fin nE) ⊕ (Fin nA) → (Fin nE) ⊕ (Fin nA)
  | .inl e, _ => .inl e
  | .inr a, .inl e => .inl (sigmaLk t a e)
  | .inr a, .inr a' => gammaLk t a a'

/-- `⊗` is a monoid with two-sided unit `inr unit` and is associative — the whole
content of "monoid on `N` with unit in `A` and `E` a left-zero ideal". -/
def monoidOK (t : Tbl nE nA) : Bool :=
  let u : (Fin nE) ⊕ (Fin nA) := .inr t.unit
  (NList (nE := nE) (nA := nA)).all (fun n => decide (otimes t u n = n)) &&
  (NList (nE := nE) (nA := nA)).all (fun n => decide (otimes t n u = n)) &&
  (NList (nE := nE) (nA := nA)).all (fun a =>
    (NList (nE := nE) (nA := nA)).all (fun b =>
      (NList (nE := nE) (nA := nA)).all (fun c =>
        decide (otimes t (otimes t a b) c = otimes t a (otimes t b c)))))

/-! ## Enumerate all candidate tables -/

/-- All lists of length `n` over the elements of `elems`. -/
def allListsOfLen {α : Type} : Nat → List α → List (List α)
  | 0, _ => [[]]
  | k + 1, elems => elems.flatMap (fun x => (allListsOfLen k elems).map (fun l => x :: l))

/-- Every candidate datum for size `(nE, nA)`: `unit` ranges over `A` (an
`E`-unit can never be a two-sided unit for the functor form, paper §2.1), `σ` over
all `A×E → E`, `γ` over all `A×A → E ⊔ A`. -/
def allTbls (nE nA : Nat) : List (Tbl nE nA) :=
  (List.finRange nA).flatMap (fun u =>
    (allListsOfLen (nA * nE) (List.finRange nE)).flatMap (fun s =>
      (allListsOfLen (nA * nA) (NList (nE := nE) (nA := nA))).map (fun g => ⟨u, s, g⟩)))

/-! ## The bijection, machine-checked (axiom-free `decide`)

For each size the two decision procedures agree on *every* candidate: monad laws
hold iff monoid-with-left-zero-ideal laws hold. -/

/-- `|E|=0, |A|=1`: the identity monad (1 candidate). -/
theorem bijection_0_1 :
    (allTbls 0 1).all (fun t => monadOK t == monoidOK t) = true := by decide

/-- `|E|=1, |A|=1`: the `Maybe` monad case (2 candidates). -/
theorem bijection_1_1 :
    (allTbls 1 1).all (fun t => monadOK t == monoidOK t) = true := by decide

/-- `|E|=2, |A|=1`: the exception monad `E + (−)` (12 candidates). -/
theorem bijection_2_1 :
    (allTbls 2 1).all (fun t => monadOK t == monoidOK t) = true := by decide

/-- `|E|=0, |A|=2`: the four two-element monoids, incl. writer `ℤ₂`
(32 candidates). -/
theorem bijection_0_2 :
    (allTbls 0 2).all (fun t => monadOK t == monoidOK t) = true := by decide

/-- `|E|=1, |A|=2`: includes the aborting nilpotent `1 + 2×X` monad (`z² = 0 ∈ E`),
the non-cartesian counterexample of §2.3 (162 candidates). -/
theorem bijection_1_2 :
    (allTbls 1 2).all (fun t => monadOK t == monoidOK t) = true := by decide

/-- `|E|=2, |A|=2` (8192 candidates). Certified by `native_decide`
(compiler-trusted, introduces `Lean.ofReduceBool`); the kernel exceeds its
heartbeat budget on this size. -/
theorem bijection_2_2 :
    (allTbls 2 2).all (fun t => monadOK t == monoidOK t) = true := by native_decide

/-! ## Prop-level reading: monad laws ⟺ monoid-with-left-zero-ideal laws -/

/-- From the `Bool`-level agreement over all enumerated candidates, extract the
biconditional for any individual candidate: *the monad laws hold iff the monoid
(unit-in-`A`, `E` a left-zero ideal) laws hold*. -/
theorem monad_iff_monoid (t : Tbl nE nA) (ht : t ∈ allTbls nE nA)
    (h : (allTbls nE nA).all (fun t => monadOK t == monoidOK t) = true) :
    (monadOK t = true ↔ monoidOK t = true) := by
  have hb : (monadOK t == monoidOK t) = true := (List.all_eq_true.mp h) t ht
  rw [eq_of_beq hb]

/-- **The classification, `|E|=|A|=1`.** For every candidate monad datum on
`M X = E + A×X` with one exception and one log letter, the monad laws hold iff
`N = E ⊔ A` is a monoid with unit in `A` and `E` a left-zero ideal. -/
theorem classification_1_1 :
    ∀ t ∈ allTbls 1 1, (monadOK t = true ↔ monoidOK t = true) :=
  fun t ht => monad_iff_monoid t ht bijection_1_1

/-- **The classification, `|E|=1, |A|=2`** (covers the aborting `1 + 2×X` monad). -/
theorem classification_1_2 :
    ∀ t ∈ allTbls 1 2, (monadOK t = true ↔ monoidOK t = true) :=
  fun t ht => monad_iff_monoid t ht bijection_1_2

/-- **The classification, `|E|=|A|=2`** (via the `native_decide` extension). -/
theorem classification_2_2 :
    ∀ t ∈ allTbls 2 2, (monadOK t = true ↔ monoidOK t = true) :=
  fun t ht => monad_iff_monoid t ht bijection_2_2

/-! ## Named anchor witnesses

Concrete tables for the monads the paper singles out, each verified to satisfy
*both* predicates (they are monads, and monoids-with-left-zero-ideal). These live
inside the enumerated classes above; naming them ties the abstract bijection to
the paper's running examples. -/

/-- `Maybe`: `M X = 1 + X`. `N = {⊥ (exc), e (unit)}`, `σ(e,⊥)=⊥`, `γ(e,e)=e`. -/
def maybeTbl : Tbl 1 1 :=
  { unit := 0, sigma := [0], gamma := [Sum.inr 0] }

/-- The `Maybe` datum is simultaneously a monad and a monoid-with-left-zero-ideal. -/
theorem maybe_monad_and_monoid : monadOK maybeTbl = true ∧ monoidOK maybeTbl = true := by
  decide

/-- Writer `ℤ₂`: `M X = 2×X`, `A = ℤ₂ = {0 = unit, 1}`, no exceptions.
`γ` is addition mod 2: `0·0=0, 0·1=1, 1·0=1, 1·1=0`. -/
def writerZ2Tbl : Tbl 0 2 :=
  { unit := 0, sigma := [],
    gamma := [Sum.inr 0, Sum.inr 1, Sum.inr 1, Sum.inr 0] }

/-- Writer `ℤ₂` is a monad and a monoid. -/
theorem writerZ2_monad_and_monoid :
    monadOK writerZ2Tbl = true ∧ monoidOK writerZ2Tbl = true := by decide

/-- The **aborting** nilpotent monad `M X = 1 + 2×X`: `A = {e = unit, z}`,
`E = {0}`, with `z ⊗ z = 0 ∈ E` (the leaf is destroyed). It is a genuine
Set-monad (hence a monoid with left-zero ideal), yet non-cartesian — so `T_M` is
undefined and it falls outside the arrow story (paper §2.3). `γ`: `e·e=e, e·z=z,
z·e=z, z·z=abort 0`. -/
def abortingTbl : Tbl 1 2 :=
  { unit := 0, sigma := [0, 0],
    gamma := [Sum.inr 0, Sum.inr 1, Sum.inr 1, Sum.inl 0] }

/-- The aborting `1 + 2×X` monad is a monad and a monoid-with-left-zero-ideal —
the Set-monad-level bijection admits it; the cartesian obstruction that excludes
it from the arrow class is a separate condition (out of scope here, §2.3). -/
theorem aborting_monad_and_monoid :
    monadOK abortingTbl = true ∧ monoidOK abortingTbl = true := by decide

end AffineClassification
end Containers
