/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# The fibre-edge `H²` engine: `H²(ℤ/2; ℤ/2) ≅ ℤ/2` with split/nonsplit witnesses

This file formalises the **fibre-edge** kernel of the H²-cluster decoupling witness
(MacBeth, WAKE 2026-09-17, `prunability-fibre-edge-witness-k23`; PROVE
2026-09-17, `h2cluster-lhs-transgression`). It is the companion of the base-edge
engine `2026-09-16-cyclic-h2-norm.lean` (which proved `H²(C_n; ℤ) ≅ ℤ/nℤ` via the
norm map). Here the coefficients are `M = ℤ/2` rather than `ℤ`.

In the Lyndon–Hochschild–Serre spectral sequence of the Zappa–Szép extension
`1 → D → π → Γ → 1`, the fibre edge is `E₂^{0,2} = H²(D; M)^Γ`; in the concrete
`K_{2,3}` witness the fibre vertex group is `D = ℤ/2` acting trivially on the
module `M = ℤ/2`. This file establishes:

1. **The group.** `H²(ℤ/2; ℤ/2) ≅ ℤ/2` (two classes), computed as the cokernel of
   the norm map `·2`, which is `0` on `ℤ/2`, so `H² = ℤ/2 / {0} ≅ ℤ/2`.
2. **The nonsplit witness.** The central extension `0 → {0,2} → ℤ/4 → ℤ/2 → 0`
   has Schreier factor set the **carry cocycle** `f(a,b) = a ∧ b` (value `2 ∈ {0,2}`
   at `(1,1)`, i.e. the generator of `ℤ/2`). It is a genuine `2`-cocycle and is
   **not** a `2`-coboundary of any `1`-cochain ⟹ its class `[π]` is the nonzero
   generator of `H²(ℤ/2; ℤ/2)`. This is the prunability *defect* being real.
3. **The split control.** The Klein extension
   `0 → ℤ/2 → ℤ/2×ℤ/2 → ℤ/2 → 0` has trivial factor set (the constant `0`
   cocycle) ⟹ it is a coboundary and its class is `0`. The prunable control is `0`.

We work with the honest (normalized) bar cochain complex of `C_2` directly — for
`C_2` it is completely finite, so the cocycle/coboundary facts are checked by
`decide`. Both the "no `1`-cochain trivialises the carry cocycle" statement and
its cocycle condition are proved with no black box. The only citation is the
identification of this bar `H²` with the abstract `E₂^{0,2}` fibre edge, which is
standard (K. S. Brown, *Cohomology of Groups*, §VI.9 for the cyclic reduction; the
LHS placement is in `h2cluster-lhs-transgression`).

## References
Ferri, *Quiver representations and skew braces*, arXiv:2605.11903 (fibre base of
the ZS extension); MacBeth PROVE 2026-09-17 (`2026-09-17-h2cluster-lhs-transgression.tex`).
Companion base-edge engine: `2026-09-16-cyclic-h2-norm.lean`.

## Scope (honest)
The abstract identification `bar H²(C_2; M) ≅ E₂^{0,2}` fibre edge is cited, not
re-proved. The concrete cocycle classes, the group `H²(ℤ/2;ℤ/2) = ℤ/2`, and the
split-vs-nonsplit dichotomy are fully formalised here.

Mathlib-free: Lean 4 core only (v4.30.0).
-/

namespace FibreH2

/-! ### The coefficient group `Z2 = ℤ/2`

We model `ℤ/2` as `Bool` with `xor` (`bne`) as addition; `false = 0`, `true = 1`.
Every element is its own inverse, so the norm map `·2` (add-self) is identically
zero — this is exactly why `H²(ℤ/2; ℤ/2) = ℤ/2 / {0} ≅ ℤ/2`. -/

/-- The coefficient module `M = ℤ/2`, modelled as `Bool`. -/
abbrev Z2 := Bool

/-- The zero of `ℤ/2`. -/
def Z2.zero : Z2 := false

/-- The generator `1` of `ℤ/2`. -/
def Z2.one : Z2 := true

/-- Addition in `ℤ/2` is `xor`. -/
def Z2.add (a b : Z2) : Z2 := bne a b

/-- Negation in `ℤ/2` is the identity (`ℤ/2` is `2`-torsion). -/
def Z2.neg (a : Z2) : Z2 := a

/-- Subtraction in `ℤ/2` coincides with addition. -/
def Z2.sub (a b : Z2) : Z2 := Z2.add a (Z2.neg b)

@[simp] theorem Z2.add_comm (a b : Z2) : Z2.add a b = Z2.add b a := by cases a <;> cases b <;> rfl

@[simp] theorem Z2.add_assoc (a b c : Z2) :
    Z2.add (Z2.add a b) c = Z2.add a (Z2.add b c) := by cases a <;> cases b <;> cases c <;> rfl

@[simp] theorem Z2.add_zero (a : Z2) : Z2.add a Z2.zero = a := by cases a <;> rfl

@[simp] theorem Z2.zero_add (a : Z2) : Z2.add Z2.zero a = a := by cases a <;> rfl

/-- **The norm map is zero.** `2·a = a + a = 0` in `ℤ/2`; this collapses the
coboundary image to `{0}`, giving `H²(ℤ/2; ℤ/2) ≅ ℤ/2`. -/
@[simp] theorem Z2.add_self (a : Z2) : Z2.add a a = Z2.zero := by cases a <;> rfl

@[simp] theorem Z2.neg_add_cancel (a : Z2) : Z2.add (Z2.neg a) a = Z2.zero := by cases a <;> rfl

theorem Z2.zero_ne_one : Z2.zero ≠ Z2.one := by decide

/-! ### The normalized bar cochain complex of `C_2` with trivial `ℤ/2` coefficients

The group `C_2` has underlying set `Bool` with multiplication `xor` (`bne`) and
identity `false`. The action on `M = ℤ/2` is trivial, so the inhomogeneous
coboundaries drop their action terms.

* `d1 g (a,b) = g b - g (ab) + g a` is the `1`-coboundary of a `1`-cochain `g`.
* `d2 f (a,b,c) = f (b,c) - f (ab,c) + f (a,bc) - f (a,b)` is the `2`-coboundary of
  a `2`-cochain `f`; its kernel is the `2`-cocycles. -/

/-- The `1`-coboundary map `δ¹` on `1`-cochains `g : C_2 → ℤ/2` (trivial action). -/
def d1 (g : Bool → Z2) (a b : Bool) : Z2 :=
  Z2.add (g b) (Z2.add (g (bne a b)) (g a))

/-- The `2`-coboundary map `δ²` on `2`-cochains `f : C_2 × C_2 → ℤ/2`
(trivial action). A `2`-cocycle is an `f` with `d2 f ≡ 0`. -/
def d2 (f : Bool → Bool → Z2) (a b c : Bool) : Z2 :=
  Z2.add (f b c) (Z2.add (f (bne a b) c) (Z2.add (f a (bne b c)) (f a b)))

/-- **Cochain-complex identity `δ² ∘ δ¹ = 0`.** Every `1`-coboundary is a
`2`-cocycle. Checked over all `2³` group inputs and both cochain values. -/
theorem d2_comp_d1 (g : Bool → Z2) (a b c : Bool) : d2 (d1 g) a b c = Z2.zero := by
  cases a <;> cases b <;> cases c <;>
    simp [d1, d2, Z2.add, Z2.zero] <;> cases g false <;> cases g true <;> rfl

/-- **Every normalized `2`-cochain is a `2`-cocycle.** For `C_2` with trivial
coefficients the only free value is `f(1,1)`, so `Z²(C_2; ℤ/2) ≅ ℤ/2` is
one-dimensional. `f` is *normalized* when `f(1,·) = 0` and `f(·,1) = 0` with `1`
the identity `false`. -/
theorem twoCocycle_of_normalized (f : Bool → Bool → Z2)
    (h0 : ∀ b, f false b = Z2.zero) (h0' : ∀ a, f a false = Z2.zero) :
    ∀ a b c, d2 f a b c = Z2.zero := by
  intro a b c
  cases a <;> cases b <;> cases c <;>
    simp [d2, h0, h0', Z2.add, Z2.zero] <;> cases f true true <;> rfl

/-! ### The two Schreier factor sets (concrete `2`-cocycles) -/

/-- **Nonsplit witness.** The Schreier factor set of `0 → ℤ/2 → ℤ/4 → ℤ/2 → 0`
for the section `s(0)=0, s(1)=1`: the **carry cocycle** `f(a,b) = a ∧ b`, with
value `2 ∈ {0,2} ≅ ℤ/2` (i.e. `1`) exactly at `(1,1)`. -/
def fZ4 (a b : Bool) : Z2 := a && b

/-- **Split control.** The Schreier factor set of the Klein extension
`0 → ℤ/2 → ℤ/2×ℤ/2 → ℤ/2 → 0` for `s(1) = (1,0)`: the constant `0` cocycle. -/
def fKlein (_ _ : Bool) : Z2 := Z2.zero

/-- The carry cocycle is normalized: `f(0,b) = 0`. -/
theorem fZ4_norm_left (b : Bool) : fZ4 false b = Z2.zero := rfl

/-- The carry cocycle is normalized: `f(a,0) = 0`. -/
theorem fZ4_norm_right (a : Bool) : fZ4 a false = Z2.zero := by cases a <;> rfl

/-- The carry cocycle takes the nonzero value `1` at `(1,1)` — the class `2 ∈ {0,2}`. -/
theorem fZ4_val : fZ4 true true = Z2.one := rfl

/-- The Klein cocycle is `0` at `(1,1)`. -/
theorem fKlein_val : fKlein true true = Z2.zero := rfl

/-- **The carry cocycle is a genuine `2`-cocycle** (`δ² fZ4 ≡ 0`). -/
theorem fZ4_cocycle (a b c : Bool) : d2 fZ4 a b c = Z2.zero := by
  cases a <;> cases b <;> cases c <;> rfl

/-- The Klein factor set is a `2`-cocycle. -/
theorem fKlein_cocycle (a b c : Bool) : d2 fKlein a b c = Z2.zero := by
  cases a <;> cases b <;> cases c <;> rfl

/-- **The Klein control splits.** Its factor set is the coboundary of the zero
`1`-cochain, hence a `2`-coboundary — its class is `0`. -/
theorem fKlein_isCoboundary : ∀ a b, d1 (fun _ => Z2.zero) a b = fKlein a b := by
  intro a b; cases a <;> cases b <;> rfl

/-- **The nonsplit defect is real.** The carry cocycle `fZ4` is *not* the
coboundary of any `1`-cochain `g` (normalized or not). Matching at `(0,0)` forces
`g false = 0`, and then the coboundary value at `(1,1)` is `g false + g false = 0`,
which cannot equal `fZ4(1,1) = 1`. Hence `[π] ≠ 0` in `H²(ℤ/2; ℤ/2)`. -/
theorem fZ4_not_coboundary : ¬ ∃ g : Bool → Z2, ∀ a b, d1 g a b = fZ4 a b := by
  rintro ⟨g, h⟩
  have h00 := h false false
  have h11 := h true true
  -- `d1 g false false = g false` and `d1 g true true = g false`; but `fZ4 (1,1) = 1`.
  -- `bne_self_eq_false` reduces the internal `a·b = a xor b` arguments to `false`,
  -- leaving only `g false` and `g true`.
  simp only [d1, fZ4, Z2.add, bne_self_eq_false] at h00 h11
  revert h00 h11
  cases g false <;> cases g true <;> decide

/-! ### The cohomology group `H²(ℤ/2; ℤ/2) = coker(norm) = ℤ/2`

Mirroring the base-edge engine, `H²` is the value group `ℤ/2` of the reduced
`2`-periodic complex modulo the image of the norm map `·2`. Because `·2 = 0` on
`ℤ/2` (`Z2.add_self`), the coboundary image is `{0}` and `H²` has exactly two
classes. -/

/-- The reduced-complex coboundary relation: `a ~ b` iff they differ by a value in
the image of the norm map `·2`, i.e. `a - b = t + t` for some `t`. Since
`t + t = 0`, this is just equality. -/
def cobRel (a b : Z2) : Prop := ∃ t : Z2, Z2.sub a b = Z2.add t t

theorem cobRel_iff_eq (a b : Z2) : cobRel a b ↔ a = b := by
  constructor
  · rintro ⟨t, ht⟩
    simp only [Z2.add_self] at ht
    revert ht; cases a <;> cases b <;> decide
  · rintro rfl; exact ⟨Z2.zero, by cases a <;> rfl⟩

theorem cobRel_refl (a : Z2) : cobRel a a := (cobRel_iff_eq a a).2 rfl

theorem cobRel_symm {a b : Z2} : cobRel a b → cobRel b a := by
  rw [cobRel_iff_eq, cobRel_iff_eq]; exact Eq.symm

theorem cobRel_trans {a b c : Z2} : cobRel a b → cobRel b c → cobRel a c := by
  rw [cobRel_iff_eq, cobRel_iff_eq, cobRel_iff_eq]; exact Eq.trans

/-- The setoid identifying cohomologous `2`-cochain values. -/
def cobSetoid : Setoid Z2 := ⟨cobRel, cobRel_refl, cobRel_symm, cobRel_trans⟩

/-- The second cohomology group `H²(ℤ/2; ℤ/2) = ℤ/2 / im(norm)`. -/
def H2 : Type := Quotient cobSetoid

/-- The class in `H²` of a `2`-cochain value. -/
def H2.mk (a : Z2) : H2 := Quotient.mk cobSetoid a

/-- Two `2`-cochain values give the same class iff they are equal (the norm image
is trivial): `⟦a⟧ = ⟦b⟧ ↔ a = b`. -/
theorem H2.mk_eq_iff (a b : Z2) : H2.mk a = H2.mk b ↔ a = b :=
  ⟨fun h => (cobRel_iff_eq a b).1 (Quotient.exact h),
   fun h => Quotient.sound ((cobRel_iff_eq a b).2 h)⟩

/-! #### Abelian-group structure on `H²` (`≅ ℤ/2`) -/

/-- Addition of cohomology classes, induced from `ℤ/2`. -/
instance : Add H2 where
  add x y :=
    Quotient.liftOn₂ x y (fun a b => H2.mk (Z2.add a b)) <| by
      intro a b a' b' hab hab'
      obtain rfl : a = a' := (cobRel_iff_eq a a').1 hab
      obtain rfl : b = b' := (cobRel_iff_eq b b').1 hab'
      rfl

/-- The zero class. -/
instance : Zero H2 where zero := H2.mk Z2.zero

/-- Negation of classes (trivial, since `ℤ/2` is `2`-torsion). -/
instance : Neg H2 where
  neg x :=
    Quotient.liftOn x (fun a => H2.mk (Z2.neg a)) <| by
      intro a a' ha
      obtain rfl : a = a' := (cobRel_iff_eq a a').1 ha
      rfl

@[simp] theorem H2.mk_add (a b : Z2) : H2.mk a + H2.mk b = H2.mk (Z2.add a b) := rfl

theorem H2.zero_def : (0 : H2) = H2.mk Z2.zero := rfl

@[simp] theorem H2.mk_neg (a : Z2) : -H2.mk a = H2.mk (Z2.neg a) := rfl

theorem H2.add_comm (x y : H2) : x + y = y + x := by
  refine Quotient.inductionOn₂ x y ?_; intro a b
  exact Quotient.sound ((cobRel_iff_eq _ _).2 (Z2.add_comm a b))

theorem H2.add_assoc (x y z : H2) : x + y + z = x + (y + z) := by
  refine Quotient.inductionOn₂ x y ?_; intro a b
  refine Quotient.inductionOn z ?_; intro c
  exact Quotient.sound ((cobRel_iff_eq _ _).2 (Z2.add_assoc a b c))

theorem H2.zero_add (x : H2) : 0 + x = x := by
  refine Quotient.inductionOn x ?_; intro a
  exact Quotient.sound ((cobRel_iff_eq _ _).2 (Z2.zero_add a))

theorem H2.add_zero (x : H2) : x + 0 = x := by
  refine Quotient.inductionOn x ?_; intro a
  exact Quotient.sound ((cobRel_iff_eq _ _).2 (Z2.add_zero a))

theorem H2.neg_add_cancel (x : H2) : -x + x = 0 := by
  refine Quotient.inductionOn x ?_; intro a
  exact Quotient.sound ((cobRel_iff_eq _ _).2 (Z2.neg_add_cancel a))

/-- A class is trivial iff its representative is `0` (a coboundary): `⟦a⟧ = 0 ↔ a = 0`. -/
theorem H2.mk_eq_zero_iff (a : Z2) : H2.mk a = 0 ↔ a = Z2.zero := by
  rw [H2.zero_def, H2.mk_eq_iff]

/-! ### Grant-critical corollaries: `H²(ℤ/2; ℤ/2) ≅ ℤ/2` and the split/nonsplit split -/

/-- `H²(ℤ/2; ℤ/2)` has (exactly) two distinct classes: it is nontrivial. -/
theorem H2_two_distinct : H2.mk Z2.zero ≠ H2.mk Z2.one := by
  rw [Ne, H2.mk_eq_iff]; exact Z2.zero_ne_one



/-- Every class of `H²(ℤ/2; ℤ/2)` is `⟦0⟧` or `⟦1⟧`: two classes cover `ℤ/2`. -/
theorem H2_two_cover (a : Z2) : H2.mk a = H2.mk Z2.zero ∨ H2.mk a = H2.mk Z2.one := by
  cases a
  · exact Or.inl rfl
  · exact Or.inr rfl

/-- **The prunability defect is a nonzero class.** The `ℤ/4` carry cocycle sits in
the nonzero class of `H²(ℤ/2; ℤ/2)`. -/
theorem classZ4_ne_zero : H2.mk (fZ4 true true) ≠ 0 := by
  rw [fZ4_val, Ne, H2.mk_eq_zero_iff]; exact fun h => Z2.zero_ne_one h.symm

/-- **The prunable control is the zero class.** The Klein cocycle sits in `0`. -/
theorem classKlein_eq_zero : H2.mk (fKlein true true) = 0 := by
  rw [fKlein_val]; rfl

/-- **Decoupling on the fibre edge.** The nonsplit `ℤ/4` class and the split Klein
class are distinct in `H²(ℤ/2; ℤ/2)`: `[π] ≠ 0 = [Klein]`. This is the fibre-edge
core of the `K_{2,3}` prunability/holonomy decoupling witness. -/
theorem classZ4_ne_classKlein : H2.mk (fZ4 true true) ≠ H2.mk (fKlein true true) := by
  rw [classKlein_eq_zero]; exact classZ4_ne_zero

end FibreH2
