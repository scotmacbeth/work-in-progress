/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# The container tangent bundle has no fiberwise negation (arithmetic core)

This file machine-checks the **decidable arithmetic core** of MacBeth's PROVE result
*"The container tangent structure has no fiberwise negation: `SPoly/∂` carries no scalar ring
object, and the Cartan calculus does not descend"*
(`proofs/2026-10-05-spoly-negation-obstruction.md`; registry node
`spoly-no-scalar-ring-object`). The structural theorem is: the additive bundle of the container
tangent structure `T = (−)◁D`, `D = y + εv`, on finite-support polynomial functors is a bundle
of commutative monoids with **no** fiberwise additive inverse; hence `SPoly/∂` is not a Rosický
tangent category and admits no scalar ring object in the sense of the Aintablian–Blohmann
Cartan-calculus program (arXiv:2607.11169, §4). That structural statement — which routes through
Lemma A (scalar ring object ⟹ negation) and the structure-preserving counting functor
`N : SPoly → Poly_ℕ` — is **not** itself `decide`-able.

What **is** finite/arithmetic, and is certified here, are the three witnesses the proof rests on:

1. **The fiber monoids are not groups.** Over a shape with `k` holes the additive-bundle fiber is
   the free `ℕ`-module `Fin k → ℕ` (iterated fiber addition = the codiagonal `∇` on the
   infinitesimal part `M = y`), with pointwise addition. For `k ≥ 1` it has an element with no
   additive inverse (`no_negation_free_module`). The two PROVE witnesses are the specialisations:
   * `p = y` (the line): fiber `ℕ`, unit tangent `1` has no inverse (`fiber_line_not_group`);
   * `p = y²` (`∂(y²) = 2y`): fiber `ℕ²`, element `(1,0)` has no inverse (`fiber_y2_not_group`).

2. **The transport-killing step (Proposition 1, §2.1).** A negation on `(SPoly, T)` would
   transport along `N` to a negation on `Poly_ℕ`, i.e. a bundle endomorphism over object `1` — an
   `ℕ`-coefficient polynomial `g(x,v)` — with `v + g(x,v) = 0` identically. No such polynomial
   exists (`no_poly_negation`, modelled with a genuine Horner evaluator), and in fact **no
   function** `ℕ × ℕ → ℕ` does (`no_function_negation`) — matching the proof's remark that *any
   candidate negation whatsoever* is killed. The knife is the rig `ℕ`: `1 + n = 0` is unsolvable.

3. **Genuine commutative monoid, only `0` invertible** (`fiber_line_cancellative`,
   `fiber_line_only_zero_invertible`): the fiber `ℕ` is a commutative, associative, unital,
   cancellative monoid in which exactly the zero element has an inverse — the signature of a free
   `ℕ`-module, one subtraction short of the free `ℤ`-module a group would require.

Modelled in **core Lean 4, Mathlib-free** (same style as
`lean/2026-10-03-tangent-container-bridge-finite.lean`): `ℕ`-polynomials are coefficient lists
with Horner evaluation; fibers are `Fin k → ℕ` / `ℕ` / `ℕ × ℕ` with explicit pointwise addition.
`decide` handles the concrete finite facts; `omega` the `ℕ`-quantified ones (so those carry
`propext, Quot.sound`, reported honestly at the end). This certifies the ARITHMETIC obstruction
(the rig has no inverses), **not** the structural claim that `T` is non-Rosický as a functor —
exactly the scope line of the companion oracles `lean-spoly-solid-idempotent`,
`lean-universality-rank-rigidity`, `lean-tangent-bridge-finite`.
-/

namespace SPolyNegationObstruction

/-! ### 1. The additive-bundle fiber over a `k`-hole shape: the free `ℕ`-module `Fin k → ℕ`

The additive tangent bundle of `T = (−)◁D` has, over a shape with hole-set of size `k`, the fiber
`(ℕ^k, +, 0)` — one `ℕ`-multiplicity per hole-direction, added pointwise (there is no addition of
`Set`-values; the only addition is the `ℕ`-codiagonal on the infinitesimal part). We model it as
`Fin k → ℕ` with pointwise addition (`t i + σ t i` below) and prove it is not a group as soon as
there is a hole. -/

/-- **The free `ℕ`-module on `≥ 1` holes has no negation.** There is no map `σ` assigning to each
tangent vector an additive inverse: a negation would in particular invert the all-ones vector in its
first coordinate, requiring `1 + (σ …) = 0` in `ℕ`, which is impossible. This is the fiberwise
obstruction underlying Proposition 1 — strengthened to *arbitrary functions* `σ`, so no exotic
negation escapes. -/
theorem no_negation_free_module (k : Nat) (hk : 1 ≤ k) :
    ¬ ∃ σ : (Fin k → Nat) → (Fin k → Nat), ∀ t : Fin k → Nat, ∀ i, t i + σ t i = 0 := by
  rintro ⟨σ, h⟩
  have := h (fun _ => 1) ⟨0, hk⟩
  simp only at this
  omega

/-! ### 2. The two PROVE witnesses: `p = y` (fiber `ℕ`) and `p = y²` (fiber `ℕ²`) -/

/-- **`p = y` (the line), minimal witness.** `Ty = y + εv = D`; the fiber is `ℕ`. The unit tangent
`1 ∈ ℕ` has no additive inverse: already the tangent bundle of the identity functor is a non-group.
-/
theorem fiber_line_not_group : ∀ c : Nat, 1 + c ≠ 0 := by omega

/-- **`p = y²`, first non-linear (`∂(y²) = 2y`).** One shape, two holes; `T(y²) = y² + εv·2y`, fiber
`ℕ²`. The element `(1,0)` (one unit of tangent along the first hole) has no inverse: its first
coordinate cannot be cancelled in `ℕ`. Stated with explicit coordinates. -/
theorem fiber_y2_not_group : ∀ a b : Nat, ¬ (1 + a = 0 ∧ 0 + b = 0) := by
  intro a b; omega

/-! ### 3. The transport-killing step: `Poly_ℕ` has no negation over object `1`

In the counting target `Poly_ℕ` the tangent bundle of object `1` carries coordinates `(x, v)` with
projection `p = π_x`, fiber addition `(x, v₁, v₂) ↦ (x, v₁ + v₂)` and zero `x ↦ (x, 0)`. A bundle
endomorphism over `p` is `(x, v) ↦ (x, g(x, v))` for an `ℕ`-coefficient polynomial `g`, and the
negation law `(†)` reads `v + g(x, v) = 0` **identically** in `ℕ[x, v]`. We show no such `g`
exists — first for an arbitrary function (strongest form), then for a genuine `ℕ`-polynomial via a
Horner evaluator, matching the literal statement in the proof's §2.1(c). -/

/-- **No function negates** (strongest form of Proposition 1). Even allowing `g : ℕ × ℕ → ℕ` to be
an arbitrary function — not merely a polynomial — the law `v + g(x, v) = 0` is unsatisfiable:
evaluate at `v = 1`. -/
theorem no_function_negation : ¬ ∃ g : Nat → Nat → Nat, ∀ x v, v + g x v = 0 := by
  rintro ⟨g, h⟩
  have := h 0 1
  omega

/-- Horner evaluation of a univariate `ℕ`-polynomial (coefficient list, index = degree):
`peval [a₀, a₁, …] x = a₀ + x·(a₁ + x·(…))`. -/
def peval : List Nat → Nat → Nat
  | [], _ => 0
  | a :: t, x => a + x * peval t x

/-- Evaluation of a bivariate `ℕ`-polynomial `g(x, v)`, represented as a list of `v`-coefficient
rows indexed by the `x`-degree (outer index = power of `x`): `g(x, v) = ∑ᵢ xⁱ · rowᵢ(v)`. -/
def bpeval (g : List (List Nat)) (x v : Nat) : Nat :=
  peval (g.map (fun row => peval row v)) x

/-- **No `ℕ`-polynomial negates** (Proposition 1, literal form, §2.1(c)). For every bivariate
`ℕ`-polynomial `g`, the negation law `v + g(x, v) = 0` fails — witnessed at `x = 0, v = 1`, where
`g(0,1) ≥ 0` forces `1 + g(0,1) ≥ 1 > 0`. So `g = −v` (the only algebraic solution) is not an
`ℕ`-polynomial, and the container tangent structure admits no negation. -/
theorem no_poly_negation : ∀ g : List (List Nat), ¬ ∀ x v, v + bpeval g x v = 0 := by
  intro g h
  have := h 0 1
  omega

/-! ### 4. The fiber `ℕ` is a genuine commutative monoid — but only `0` is invertible

To certify that the obstruction is "not a group" and not some pathology (the fiber is a perfectly
good commutative, cancellative, unital monoid — the free `ℕ`-module on one hole), we record the
monoid laws and that exactly `0` has an additive inverse. -/

/-- Fiber addition is commutative. -/
theorem fiber_line_add_comm : ∀ a b : Nat, a + b = b + a := by omega

/-- Fiber addition is associative. -/
theorem fiber_line_add_assoc : ∀ a b c : Nat, (a + b) + c = a + (b + c) := by omega

/-- `0` is the additive unit. -/
theorem fiber_line_add_zero : ∀ a : Nat, a + 0 = a := by omega

/-- The fiber monoid is cancellative. -/
theorem fiber_line_cancellative : ∀ a b c : Nat, a + b = a + c → b = c := by omega

/-- **Exactly `0` is invertible.** An element of the fiber `ℕ` has an additive inverse iff it is
`0`. A group would require every element invertible; this is a free `ℕ`-module, where only the
identity is. -/
theorem fiber_line_only_zero_invertible : ∀ a : Nat, (∃ b, a + b = 0) ↔ a = 0 := by
  intro a
  constructor
  · rintro ⟨b, hb⟩; omega
  · rintro rfl; exact ⟨0, rfl⟩

/-! ### 5. Packaged -/

/-- **The negation-obstruction arithmetic oracle, packaged.** Certifies the decidable core of
`proofs/2026-10-05-spoly-negation-obstruction.md` (registry node `spoly-no-scalar-ring-object`):

1. the free-`ℕ`-module fiber over any shape with a hole has no negation (`no_negation_free_module`),
   with the two PROVE witnesses `p = y` (fiber `ℕ`) and `p = y²` (fiber `ℕ²`);
2. the transport-killing step — `Poly_ℕ` has no negation over object `1`: no function, and a
   fortiori no `ℕ`-polynomial `g`, satisfies `v + g(x,v) = 0` (`no_function_negation`,
   `no_poly_negation`);
3. the fiber `ℕ` is a genuine cancellative commutative monoid in which only `0` is invertible.

This is the arithmetic heart of "`SPoly/∂` carries no scalar ring object; the Cartan calculus does
not descend" — the rig `ℕ` has no additive inverses. It does **not** certify the structural
functorial claim (Lemma A and the `N`-transport), which is the proved result it backs. -/
theorem spoly_negation_obstruction :
    (∀ c : Nat, 1 + c ≠ 0)
    ∧ (∀ a b : Nat, ¬ (1 + a = 0 ∧ 0 + b = 0))
    ∧ (∀ k : Nat, 1 ≤ k →
        ¬ ∃ σ : (Fin k → Nat) → (Fin k → Nat), ∀ t : Fin k → Nat, ∀ i, t i + σ t i = 0)
    ∧ (¬ ∃ g : Nat → Nat → Nat, ∀ x v, v + g x v = 0)
    ∧ (∀ g : List (List Nat), ¬ ∀ x v, v + bpeval g x v = 0)
    ∧ (∀ a : Nat, (∃ b, a + b = 0) ↔ a = 0) :=
  ⟨fiber_line_not_group, fiber_y2_not_group, no_negation_free_module,
    no_function_negation, no_poly_negation, fiber_line_only_zero_invertible⟩

end SPolyNegationObstruction

/-
Axiom audit (`#print axioms`):
  `spoly_negation_obstruction`, `no_poly_negation`, `no_negation_free_module`,
  `fiber_line_only_zero_invertible` all depend on `[propext, Quot.sound]` only — introduced by
  `omega` on the `ℕ`-quantified goals. No `sorry`, no classical choice. The concrete finite facts
  reduce by pure arithmetic. This matches the sibling oracles (`lean-spoly-solid-idempotent`,
  `lean-universality-rank-rigidity`), which also carry `[propext]`.
-/
