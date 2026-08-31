/-!
# The Disjointness Lemma for internal exact factorisations

This file machine-checks the **general** group-theoretic backbone of the
emergent-holonomy meeting-points theorem
(`proofs/2026-08-13-emergent-holonomy-meeting-points.md`, Lemma 1; registry
node `disjointness-lemma` in `holonomy-composition-zs-bridge.json`).

**Lemma 1 (disjointness of `P` from every conjugate of `Q`).** For an internal
exact factorisation `G = P·Q` (subgroups `P`, `Q` with `P ∩ Q = {e}` and every
`g` factoring as `p·q`) and **every** `g ∈ G`,
```
        P ∩ g Q g⁻¹ = {e}.
```

The proof uses *only* that `P, Q` are subgroups with `P ∩ Q = {e}` and that `g`
factors as `p·q` — nothing about the group action or the fixed point. It is the
one genuinely general, Mathlib-friendly step underneath "emergent reentrancy is
an honest positive-integer count of orbit-crossings": it forces every
`(A,B)`-double coset to have uniform size `|A|·|B|`, so `|U|/(|A|·|B|)` is a
positive integer.

This project deliberately carries no Mathlib dependency (cf.
`EmergentHolonomy.lean`, where `S₃` is hand-rolled), so we hand-roll a minimal
`Group` class and `Subgroup` structure and prove the lemma in full generality
over an arbitrary group. A Mathlib port would replace these by
`Subgroup`/`IsComplement` and derive the double-coset size formula from
`Doset`; the mathematical content is identical.

No `sorry`, no `decide`; depends only on `propext` (see the axiom-footprint
note at the foot of the file).

References: MacBeth PROVE `proofs/2026-08-13-emergent-holonomy-meeting-points.md`
§1 (Lemma 1, Corollary 1.1); verified across every exact factorisation of
`S₃, S₄, A₄, D₄, D₆, A₅` (41 064 checks, 0 violations, `zs_holonomy_L3.py`).
The internal-exact-factorisation ↔ Zappa–Szép correspondence is Brin; see also
Ahman–Uustalu, *Distributive Laws of Directed Containers*, TYPES 2013.
-/

universe u

namespace Containers
namespace Disjointness

/-! ## 1. A minimal group -/

/-- A group, hand-rolled to keep this file Mathlib-free (project convention). -/
class Group (G : Type u) extends Mul G, One G, Inv G where
  mul_assoc : ∀ a b c : G, a * b * c = a * (b * c)
  one_mul : ∀ a : G, 1 * a = a
  mul_one : ∀ a : G, a * 1 = a
  inv_mul_cancel : ∀ a : G, a⁻¹ * a = 1
  mul_inv_cancel : ∀ a : G, a * a⁻¹ = 1

namespace Group

variable {G : Type u} [Group G]

attribute [simp] one_mul mul_one inv_mul_cancel mul_inv_cancel

/-- Left-cancellation of an inverse: `a⁻¹ * (a * b) = b`. -/
@[simp] theorem inv_mul_cancel_left (a b : G) : a⁻¹ * (a * b) = b := by
  rw [← mul_assoc, inv_mul_cancel, one_mul]

/-- Left-cancellation the other way: `a * (a⁻¹ * b) = b`. -/
@[simp] theorem mul_inv_cancel_left (a b : G) : a * (a⁻¹ * b) = b := by
  rw [← mul_assoc, mul_inv_cancel, one_mul]

/-- If `a * b = 1` then `a` is the inverse of `b`. -/
theorem inv_eq_of_mul_eq_one_left {a b : G} (h : a * b = 1) : a = b⁻¹ := by
  calc
    a = a * (b * b⁻¹) := by rw [mul_inv_cancel, mul_one]
    _ = a * b * b⁻¹ := by rw [mul_assoc]
    _ = 1 * b⁻¹ := by rw [h]
    _ = b⁻¹ := by rw [one_mul]

/-- The reversal law `(a * b)⁻¹ = b⁻¹ * a⁻¹`. -/
@[simp] theorem mul_inv_rev (a b : G) : (a * b)⁻¹ = b⁻¹ * a⁻¹ := by
  refine (inv_eq_of_mul_eq_one_left ?_).symm
  rw [mul_assoc, inv_mul_cancel_left, inv_mul_cancel]

end Group

/-! ## 2. Subgroups -/

variable {G : Type u} [Group G]

/-- A subgroup as a membership predicate closed under the group operations. -/
structure Subgroup (G : Type u) [Group G] where
  /-- The underlying membership predicate. -/
  mem : G → Prop
  /-- The identity belongs. -/
  one_mem : mem 1
  /-- Closure under multiplication. -/
  mul_mem : ∀ {a b : G}, mem a → mem b → mem (a * b)
  /-- Closure under inversion. -/
  inv_mem : ∀ {a : G}, mem a → mem a⁻¹

/-! ## 3. The Disjointness Lemma

`p⁻¹ · a · p` is the pivot: it lies in `P` because `a, p⁻¹, p` do, and it equals
`q · z · q⁻¹ ∈ Q` after cancelling `g = p·q` against its inverse. Living in
`P ∩ Q = {e}` it must be the identity, whence `a = e`. -/

open Group

/-- The conjugation identity that makes the pivot land in `Q`:
`p⁻¹ · ((p·q)·z·(p·q)⁻¹) · p = q·z·q⁻¹`. Pure group calculation. -/
theorem conj_pivot (p q z : G) :
    p⁻¹ * (p * q * z * (p * q)⁻¹) * p = q * z * q⁻¹ := by
  simp only [mul_inv_rev, mul_assoc, inv_mul_cancel_left, inv_mul_cancel,
    mul_one]

/-- Recover `a` from its pivot: `p · (p⁻¹ · a · p) · p⁻¹ = a`. -/
theorem pivot_recover (p a : G) : p * (p⁻¹ * a * p) * p⁻¹ = a := by
  simp only [mul_assoc, mul_inv_cancel_left, mul_inv_cancel, mul_one]

/-- **The Disjointness Lemma.** For an internal exact factorisation `G = P·Q`
(trivial intersection `htriv` and factorisation `hfact`) and every `g ∈ G`, any
element lying both in `P` and in the conjugate `g·Q·g⁻¹` is the identity — i.e.
`P ∩ g Q g⁻¹ = {e}`. -/
theorem disjointness (P Q : Subgroup G)
    (htriv : ∀ x : G, P.mem x → Q.mem x → x = 1)
    (hfact : ∀ g : G, ∃ p q : G, P.mem p ∧ Q.mem q ∧ g = p * q)
    (g a : G) (ha : P.mem a) (haC : ∃ z : G, Q.mem z ∧ a = g * z * g⁻¹) :
    a = 1 := by
  obtain ⟨z, hz, haz⟩ := haC
  obtain ⟨p, q, hp, hq, hg⟩ := hfact g
  -- The pivot `p⁻¹ * a * p` lies in `P` (all three factors do).
  have hwP : P.mem (p⁻¹ * a * p) := P.mul_mem (P.mul_mem (P.inv_mem hp) ha) hp
  -- It equals `q * z * q⁻¹`, hence lies in `Q`.
  have hwEq : p⁻¹ * a * p = q * z * q⁻¹ := by rw [haz, hg, conj_pivot]
  have hwQ : Q.mem (p⁻¹ * a * p) := by
    rw [hwEq]; exact Q.mul_mem (Q.mul_mem hq hz) (Q.inv_mem hq)
  -- In `P ∩ Q = {e}`, so the pivot is `1`; recovering `a` gives `a = 1`.
  have hw1 : p⁻¹ * a * p = 1 := htriv _ hwP hwQ
  calc
    a = p * (p⁻¹ * a * p) * p⁻¹ := (pivot_recover p a).symm
    _ = p * 1 * p⁻¹ := by rw [hw1]
    _ = 1 := by rw [mul_one, mul_inv_cancel]

/-- Clean set-theoretic restatement: `P ∩ g Q g⁻¹ = {e}`. The forward direction
is `disjointness`; the reverse says the identity always lies in the
intersection. -/
theorem disjointness_iff (P Q : Subgroup G)
    (htriv : ∀ x : G, P.mem x → Q.mem x → x = 1)
    (hfact : ∀ g : G, ∃ p q : G, P.mem p ∧ Q.mem q ∧ g = p * q)
    (g a : G) :
    (P.mem a ∧ ∃ z : G, Q.mem z ∧ a = g * z * g⁻¹) ↔ a = 1 := by
  constructor
  · rintro ⟨ha, haC⟩
    exact disjointness P Q htriv hfact g a ha haC
  · rintro rfl
    refine ⟨P.one_mem, 1, Q.one_mem, ?_⟩
    rw [mul_one, mul_inv_cancel]

end Disjointness
end Containers

/-! Axiom footprint: the development is `rfl`/simp over the hand-rolled group
laws, so it depends only on `propext` (proposition extensionality) and never on
`Classical.choice` or `sorry`. To inspect, uncomment the following and rebuild:
`#print axioms Containers.Disjointness.disjointness`. -/
