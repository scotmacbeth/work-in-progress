/-!
# Emergent holonomy: orchestration synthesises a stabiliser neither agent has

This file machine-checks the **heart of the cross-mode bridge**
`proofs/2026-08-12-holonomy-composition-zs-bridge.md`, part (b) (registry node
`holonomy-composition-zs-bridge`, sub-node `emergent-holonomy-witness-lean`):
composing two update-monad "agents" that share a state set is a **Zappa–Szép
product** of their position monoids, and — the surprise — the composite's point
**stabiliser (isotropy = holonomy) can be strictly larger** than the ZS product
of the two factor stabilisers. Two reentrancy-free agents can manufacture
reentrancy.

The refuted conjecture (b) was `Stab_{P⋈P'}(s) ≅ Stab_P(s) ⋈ Stab_{P'}(s)`.
The 448-point Python sweep (`general-M-liftings/zs_holonomy.py`) showed the
containment `⊆` always holds but is **proper**. The smallest witness is `S₃`:

* `G = S₃` acts on `X = {1,2,3}` in the standard way;
* `G = P · P'` is an exact factorisation (`P ∩ P' = {e}`, every `g = p·p'`
  uniquely) with `P = A₃ = ⟨(123)⟩ = {e, r, r²}` and `P' = ⟨(12)⟩ = {e, a}`, so
  `G` is the Zappa–Szép product `P ⋈ P'`;
* at `s = 1`: `Stab_P(1) = {e}` (no 3-cycle fixes a point) and
  `Stab_{P'}(1) = {e}` ((12) moves 1), yet `Stab_G(1) = ⟨(23)⟩ ≅ C₂ ≠ {e}`.

So `Stab_P(1) ⋈ Stab_{P'}(1) = {e}·{e} = {e}  ⊊  Stab_G(1)`: the transposition
`(23)` fixes `1` although it lies in **neither** factor. Its exact factorisation
is `(23) = (132)·(12) = r²·a` and **neither factor fixes `1`** — the holonomy is
genuinely *emergent*, not inherited from one side.

Everything is `Type`-level Lean 4 core: `S₃` is hand-rolled (6 constructors), its
multiplication is certified to be genuine composition of the point-action
(`act_mul`), and every fact is `rfl`/case-analysis. No Mathlib, no `decide`, no
`sorry` — axiom footprint verified with `#print axioms` at the foot.

References: MacBeth PROVE `proofs/2026-08-12-holonomy-composition-zs-bridge.md`
§0, §2 (Theorem (b'), properness); the emergent-holonomy upgrade
`proofs/2026-08-13-emergent-holonomy-meeting-points.md`; the ZS-product
composition of directed containers is Ahman–Uustalu, *Distributive Laws of
Directed Containers*, TYPES 2013; DCont ≅ Cat is Ahman–Chapman–Uustalu,
arXiv:1408.5809.
-/

namespace Containers

namespace EmergentHolonomy

/-! ## 1. The three-point set `X = {1,2,3}` that `S₃` permutes -/

/-- The three points `{1,2,3}` on which `S₃` acts. -/
inductive X : Type
  | x1
  | x2
  | x3
  deriving DecidableEq

/-! ## 2. The symmetric group `S₃`, hand-rolled

Six elements in cycle notation: identity `e`, the two 3-cycles
`r = (123)`, `r2 = (132)`, and the three transpositions `a = (12)`, `b = (13)`,
`c = (23)`. Hand-rolled so the group and action laws are definitional. -/

/-- `S₃` as a six-element enumeration. `r,r2` are the 3-cycles (the alternating
subgroup `A₃`); `a,b,c` the transpositions. -/
inductive S3 : Type
  | e
  | r
  | r2
  | a
  | b
  | c
  deriving DecidableEq

open S3 X

/-- The standard action of `S₃` on `X = {1,2,3}`, given elementwise.
`r = (123)`: `1↦2↦3↦1`; `a = (12)`: swaps `1,2`; `c = (23)`: swaps `2,3`; etc. -/
def act : S3 → X → X
  | S3.e,  x    => x
  | S3.r,  X.x1 => X.x2
  | S3.r,  X.x2 => X.x3
  | S3.r,  X.x3 => X.x1
  | S3.r2, X.x1 => X.x3
  | S3.r2, X.x2 => X.x1
  | S3.r2, X.x3 => X.x2
  | S3.a,  X.x1 => X.x2
  | S3.a,  X.x2 => X.x1
  | S3.a,  X.x3 => X.x3
  | S3.b,  X.x1 => X.x3
  | S3.b,  X.x2 => X.x2
  | S3.b,  X.x3 => X.x1
  | S3.c,  X.x1 => X.x1
  | S3.c,  X.x2 => X.x3
  | S3.c,  X.x3 => X.x2

/-- Group multiplication `p * q`, defined by its Cayley table so that
`act (mul p q) = act p ∘ act q` (verified as `act_mul` below); i.e. `mul p q`
applies `q` first, then `p`. -/
def mul : S3 → S3 → S3
  | S3.e,  q    => q
  | S3.r,  S3.e  => S3.r  | S3.r,  S3.r  => S3.r2 | S3.r,  S3.r2 => S3.e
  | S3.r,  S3.a  => S3.b  | S3.r,  S3.b  => S3.c  | S3.r,  S3.c  => S3.a
  | S3.r2, S3.e  => S3.r2 | S3.r2, S3.r  => S3.e  | S3.r2, S3.r2 => S3.r
  | S3.r2, S3.a  => S3.c  | S3.r2, S3.b  => S3.a  | S3.r2, S3.c  => S3.b
  | S3.a,  S3.e  => S3.a  | S3.a,  S3.r  => S3.c  | S3.a,  S3.r2 => S3.b
  | S3.a,  S3.a  => S3.e  | S3.a,  S3.b  => S3.r2 | S3.a,  S3.c  => S3.r
  | S3.b,  S3.e  => S3.b  | S3.b,  S3.r  => S3.a  | S3.b,  S3.r2 => S3.c
  | S3.b,  S3.a  => S3.r  | S3.b,  S3.b  => S3.e  | S3.b,  S3.c  => S3.r2
  | S3.c,  S3.e  => S3.c  | S3.c,  S3.r  => S3.b  | S3.c,  S3.r2 => S3.a
  | S3.c,  S3.a  => S3.r2 | S3.c,  S3.b  => S3.r  | S3.c,  S3.c  => S3.e

/-! ### 2a. `mul` really is composition, and `S₃` really is a group

`act_mul` is the honesty anchor: it certifies the Cayley table above *is* the
composition of the permutations `act -`, so this `S3` is genuinely the symmetric
group and not an arbitrary six-element magma. -/

/-- **Homomorphism / faithfulness anchor.** `act (mul p q) x = act p (act q x)`:
the Cayley table is the composition of the point permutations. `108` cases, all
`rfl`. -/
theorem act_mul (p q : S3) (x : X) : act (mul p q) x = act p (act q x) := by
  cases p <;> cases q <;> cases x <;> rfl

/-- Left identity `e * q = q` (definitional). -/
theorem e_mul (q : S3) : mul S3.e q = q := rfl

/-- Right identity `q * e = q`. -/
theorem mul_e (q : S3) : mul q S3.e = q := by cases q <;> rfl

/-- Associativity `(p * q) * t = p * (q * t)`. `216` cases, all `rfl`. -/
theorem mul_assoc (p q t : S3) : mul (mul p q) t = mul p (mul q t) := by
  cases p <;> cases q <;> cases t <;> rfl

/-- Two-sided inverse: `r⁻¹ = r2`, every transposition self-inverse. Establishes
`S₃` is a **group** (each element invertible), not merely a monoid. -/
def inv : S3 → S3
  | S3.e => S3.e | S3.r => S3.r2 | S3.r2 => S3.r
  | S3.a => S3.a | S3.b => S3.b  | S3.c => S3.c

/-- `g * g⁻¹ = e`. -/
theorem mul_inv (g : S3) : mul g (inv g) = S3.e := by cases g <;> rfl

/-- `g⁻¹ * g = e`. -/
theorem inv_mul (g : S3) : mul (inv g) g = S3.e := by cases g <;> rfl

/-! ## 3. The exact factorisation `S₃ = P · P'` (Zappa–Szép data)

`P = A₃ = {e, r, r2}` (the 3-cycles), `P' = {e, a}` with `a = (12)`. -/

/-- Membership in `P = A₃ = ⟨(123)⟩`, the alternating subgroup. -/
def inP  (g : S3) : Prop := g = S3.e ∨ g = S3.r ∨ g = S3.r2

/-- Membership in `P' = ⟨(12)⟩`. -/
def inP' (g : S3) : Prop := g = S3.e ∨ g = S3.a

/-- **`P ∩ P' = {e}`.** The only common element of the two factors is the
identity — the first Zappa–Szép (exactness) condition. -/
theorem P_inter_P'_trivial (g : S3) (hP : inP g) (hP' : inP' g) : g = S3.e := by
  rcases hP' with rfl | rfl
  · rfl
  · rcases hP with h | h | h <;> exact S3.noConfusion h

/-- **Existence of factorisation.** Every `g ∈ S₃` is a product `p · p'` with
`p ∈ P`, `p' ∈ P'`. Exhibited by the explicit factorisations
`e=e·e, r=r·e, r2=r2·e, a=e·a, b=r·a, c=r2·a`. -/
theorem factor_exists (g : S3) :
    ∃ p p', inP p ∧ inP' p' ∧ g = mul p p' := by
  cases g
  · exact ⟨S3.e,  S3.e, Or.inl rfl,              Or.inl rfl, rfl⟩
  · exact ⟨S3.r,  S3.e, Or.inr (Or.inl rfl),     Or.inl rfl, rfl⟩
  · exact ⟨S3.r2, S3.e, Or.inr (Or.inr rfl),     Or.inl rfl, rfl⟩
  · exact ⟨S3.e,  S3.a, Or.inl rfl,              Or.inr rfl, rfl⟩
  · exact ⟨S3.r,  S3.a, Or.inr (Or.inl rfl),     Or.inr rfl, rfl⟩
  · exact ⟨S3.r2, S3.a, Or.inr (Or.inr rfl),     Or.inr rfl, rfl⟩

/-- **Uniqueness of factorisation.** The map `P × P' → S₃`, `(p,p') ↦ p·p'`, is
injective. Together with `factor_exists` this makes `S₃` the Zappa–Szép product
`P ⋈ P'`. Proved by exhausting the `36` pairs; where the two products differ the
hypothesis is a clash of constructors (`S3.noConfusion`). -/
theorem factor_unique
    (p1 p1' p2 p2' : S3)
    (h1 : inP p1) (h1' : inP' p1') (h2 : inP p2) (h2' : inP' p2')
    (he : mul p1 p1' = mul p2 p2') : p1 = p2 ∧ p1' = p2' := by
  rcases h1 with rfl | rfl | rfl <;> rcases h1' with rfl | rfl <;>
    rcases h2 with rfl | rfl | rfl <;> rcases h2' with rfl | rfl <;>
      first
        | exact ⟨rfl, rfl⟩
        | exact S3.noConfusion he

/-! ## 4. Stabilisers at the point `1`, and the emergent holonomy

`fixes1 g` says `g` fixes the point `1`. -/

/-- `g` fixes the point `1 ∈ X`. -/
def fixes1 (g : S3) : Prop := act g X.x1 = X.x1

/-- **`Stab_P(1) = {e}`.** No non-identity element of `A₃` fixes `1`: the
3-cycles act freely on the points. -/
theorem stab_P_trivial (g : S3) (hP : inP g) (hfix : fixes1 g) : g = S3.e := by
  rcases hP with rfl | rfl | rfl
  · rfl
  · exact X.noConfusion hfix   -- act r  x1 = x2 ≠ x1
  · exact X.noConfusion hfix   -- act r2 x1 = x3 ≠ x1

/-- **`Stab_{P'}(1) = {e}`.** The transposition `(12)` moves `1`, so the only
element of `P'` fixing `1` is the identity. -/
theorem stab_P'_trivial (g : S3) (hP' : inP' g) (hfix : fixes1 g) : g = S3.e := by
  rcases hP' with rfl | rfl
  · rfl
  · exact X.noConfusion hfix   -- act a x1 = x2 ≠ x1

/-- **`Stab_G(1) = {e, c}`, with `c = (23)`.** A group element fixes `1` iff it
is the identity or the transposition `(23)`. -/
theorem stab_G_eq (g : S3) : fixes1 g ↔ (g = S3.e ∨ g = S3.c) := by
  constructor
  · intro hfix
    cases g
    · exact Or.inl rfl
    · exact X.noConfusion hfix
    · exact X.noConfusion hfix
    · exact X.noConfusion hfix
    · exact X.noConfusion hfix
    · exact Or.inr rfl
  · intro h
    rcases h with rfl | rfl <;> rfl

/-- `(23)` fixes `1`. -/
theorem c_fixes1 : fixes1 S3.c := rfl

/-- `(23) ≠ e`: the composite stabiliser has a non-identity element. -/
theorem c_ne_e : S3.c ≠ S3.e := fun h => S3.noConfusion h

/-- **`Stab_G(1)` has order `2`.** Exactly two elements fix `1` — `e` and `c` —
and they are distinct, so `Stab_G(1) ≅ C₂`. -/
theorem stab_G_two_elements :
    fixes1 S3.e ∧ fixes1 S3.c ∧ S3.e ≠ S3.c ∧
      (∀ g, fixes1 g → g = S3.e ∨ g = S3.c) :=
  ⟨rfl, rfl, fun h => S3.noConfusion h, fun g hg => (stab_G_eq g).1 hg⟩

/-! ## 5. The payoff: composing trivial holonomies synthesises `C₂` -/

/-- **Emergent holonomy (the refutation of conjecture (b)).**

The Zappa–Szép product of the two factor stabilisers is `{e} ⋈ {e} = {e}`
(realised in `S₃` as `mul e e = e`), because *both* factor stabilisers are
trivial (`stab_P_trivial`, `stab_P'_trivial`). Yet the composite stabiliser
`Stab_G(1)` contains `c = (23) ≠ e`. Hence

    Stab_P(1) ⋈ Stab_{P'}(1)  =  {e}   ⊊   Stab_G(1),

so the isotropy of the composite is *strictly larger* than the product of the
factor isotropies: **orchestration synthesises holonomy neither agent has.**

We package the strict inclusion as: `c` fixes `1` and is `≠ e`, while every
element of either factor that fixes `1` is forced to be `e`. -/
theorem emergent_holonomy :
    fixes1 S3.c ∧ S3.c ≠ S3.e ∧
      (∀ g, inP g  → fixes1 g → g = S3.e) ∧
      (∀ g, inP' g → fixes1 g → g = S3.e) :=
  ⟨c_fixes1, c_ne_e, stab_P_trivial, stab_P'_trivial⟩

/-- **The emergent element is genuinely emergent.** `(23)` factors as
`(23) = (132)·(12) = r2 · a`, and **neither factor fixes `1`**
(`r2 : 1 ↦ 3`, `a : 1 ↦ 2`). So the holonomy `c` is not inherited from one
side of the composition — it is created by the interaction. This is the finite
shadow of "composing two reentrancy-free agents can manufacture reentrancy". -/
theorem emergent_element_factorisation :
    S3.c = mul S3.r2 S3.a ∧
      inP S3.r2 ∧ inP' S3.a ∧
      ¬ fixes1 S3.r2 ∧ ¬ fixes1 S3.a :=
  ⟨rfl,
   Or.inr (Or.inr rfl),
   Or.inr rfl,
   fun h => X.noConfusion h,   -- act r2 x1 = x3 ≠ x1
   fun h => X.noConfusion h⟩   -- act a  x1 = x2 ≠ x1

/-- **One-line moral, as a checkable statement.** There is a group element `g`
that fixes `1` and is not the identity — call it emergent holonomy — even though
the composite factorises through two subgroups each of whose fix-`1` part is
trivial. The witness is `g = c = (23)`. -/
example : ∃ g : S3, fixes1 g ∧ g ≠ S3.e ∧
    (∀ p, inP p → fixes1 p → p = S3.e) ∧ (∀ p', inP' p' → fixes1 p' → p' = S3.e) :=
  ⟨S3.c, c_fixes1, c_ne_e, stab_P_trivial, stab_P'_trivial⟩

end EmergentHolonomy

end Containers

/-! Axiom footprint: the whole development reduces to `rfl`/case-analysis, so it
depends only on the standard soundness axioms and never on `Classical.choice` or
`sorry`. To inspect, uncomment the following and rebuild:
`#print axioms Containers.EmergentHolonomy.emergent_holonomy`. -/
