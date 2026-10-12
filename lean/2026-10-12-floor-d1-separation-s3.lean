/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

set_option maxRecDepth 100000

/-!
# The `S₃` floor-separation witness: `D1 ⊊ D2` for the inventory gerbe

This file machine-checks the **finite, decidable core** of the separation point of the
inventory-gerbe *floor dichotomy* (proof `proofs/2026-10-12-inventory-floor-d1-d2-dichotomy.md`,
§5; registry node `floor-d1-d2-dichotomy` / child `s3-separation-d1-neq-d2` under
`supply-chain-inventory-gerbe-h2.json`). It is the honest witness for Rick's M1 (band-boundary
review, `proofs/reviews/2026-10-12-band-boundary-review.pdf`): the naive "floor corollary"
*strict global inventory `⟺ β = 0 ∧ [𝔤] = 0`* is **false**, because the naive (D1) notion is
obstructed one cohomological degree below the gerbe class `[𝔤]`.

## The set-up being certified (proof §5)

Fix the base `C = B(ℤ)` (one object, free on one generator), fibre relabelling group `K = S₃`, and
the inventory transport `α` determined by `α(1) = conj(σ)` with `σ = (0 1)`. Since `B(ℤ)` is free on
one generator the transport is already a strict inner functor `ᾱ(n) = conj(σⁿ)`. The proof locates
two notions of *strict global inventory* and their obstructions:

* **(D2)** a gauge `μ` together with a strict `K`-valued functor `T` realising the transport
  (`μ(y) ᾱ(f) μ(x)⁻¹ = conj(T_f)`). Obstruction: the gerbe class `[𝔤] ∈ H²(N(C); Z(K))`.
* **(D1, naive)** a gauge `μ` relabelling the transport away entirely
  (`μ(y) ᾱ(f) μ(x)⁻¹ = id`). Obstruction: `o_{D1} ∈ H¹(C; Inn K) / im H⁰(C; Out K)` — one degree
  lower.

For `K = S₃` the separation is:

* `Z(S₃) = 1`, so the coefficient group of `[𝔤]` is trivial and `[𝔤] ∈ H²(C; 1) = 0` is **forced**.
* `Out(S₃) = 1`, so the band `β ∈ H¹(C; Out S₃) = 0` is **forced** (band trivial), and
  `Inn S₃ ≅ S₃` (`S₃` is complete, Rotman GTM 148, Thm 7.5).
* Hence **D2 inventory exists** — explicit lift `T(n) = σⁿ`, a homomorphism `ℤ → S₃` since
  `σ² = e`.
* Yet **D1 fails**: `o_{D1}` is the conjugacy class of `σ`, a *transposition* `≠ [e]`, and no gauge
  `μ ∈ S₃` conjugates `σ` to the identity. Since `S₃` is centreless, `conj` is injective, so
  `conj(μ σ μ⁻¹) = id ⟺ μ σ μ⁻¹ = e`, impossible for `σ ≠ e`.

So `β = 0 ∧ [𝔤] = 0` while D1 is unsolvable: the naive floor corollary is false, and the honest D1
floor lives in `H¹`, not `H²`.

## What is certified here (all `decide`, core `Nat`/`List`, `[propext]`/`Quot.sound`-only)

Matching the sibling engines `lean/2026-10-12-dihedral-split-4divn.lean` and
`lean/2026-10-09-gerbe-h2-witnesses.lean` (no Mathlib, no `native_decide`, no extra axioms):

* **`group_axioms`** — `S₃` (the 6 permutations of `{0,1,2}`) is a group under composition: `e = 0`
  is a two-sided identity, every element has a two-sided inverse, and multiplication is associative.
* **`centre_trivial`** — `Z(S₃) = {e}` (`= [0]`). This is the forcing `[𝔤] ∈ H²(C; Z(S₃)) = 0`.
* **`inn_order_six`** — the 6 conjugation maps are pairwise distinct, so `|Inn S₃| = 6`, i.e.
  `Inn S₃ ≅ S₃`.
* **`out_trivial`** — `|Aut S₃| = 6` (brute force over all `720` permutations of the carrier), so
  `Out S₃ = Aut S₃ / Inn S₃ = 1`. This is the forcing `β ∈ H¹(C; Out S₃) = 0`.
* **`d2_lift_order_two`** — `σ² = e`, so `T(n) = σⁿ` is a well-defined homomorphism `ℤ → S₃`: the
  explicit D2 inventory lift exists.
* **`sigma_conj_is_transposition`** — every conjugate `μ σ μ⁻¹` of `σ = (0 1)` is a transposition
  (`∈ {(0 1),(0 2),(1 2)}`); the class `o_{D1}` is the transposition class.
* **`d1_fails`** — no gauge `μ ∈ S₃` conjugates `σ` to `e` (`∀ μ, μ σ μ⁻¹ ≠ e`): D1 is unsolvable.
* **`floor_separation`** — the capstone conjunction: `Z(S₃) = 1` ∧ `Out(S₃) = 1` ∧ (D2 lift exists)
  ∧ (D1 fails). The machine-checked honest witness that the inventory floor needs D2, not D1.

Only the finite arithmetic is certified. The cohomological identifications — `[𝔤] = ᾱ*[⋆] ∈ H²`,
`o_{D1} ∈ H¹(C; Inn K)/im H⁰(C; Out K)`, and the forcing of vanishing from trivial coefficient
groups — are the classical bridges (Eilenberg–Mac Lane; Brown, *Cohomology of Groups*, GTM 87, IV.3;
Serre, *Galois Cohomology*, I.5), cited in the proof, not re-derived here.
-/

namespace FloorD1Separation

/-! ### 1. The carrier `S₃` and its multiplication

`S₃` is encoded as the codes `{0,…,5}` of the 6 permutations of `{0,1,2}`, each stored by its image
triple. `0 = e`, `1 = (0 1) = σ`, `2 = (0 2)`, `3 = (1 2)`, `4 = (0 1 2)`, `5 = (0 2 1)`. -/

/-- `img x i` is the image of point `i ∈ {0,1,2}` under the permutation with code `x ∈ {0,…,5}`. -/
def img (x i : Nat) : Nat :=
  match x, i with
  | 0, 0 => 0 | 0, 1 => 1 | 0, 2 => 2        -- e
  | 1, 0 => 1 | 1, 1 => 0 | 1, 2 => 2        -- (0 1) = σ
  | 2, 0 => 2 | 2, 1 => 1 | 2, 2 => 0        -- (0 2)
  | 3, 0 => 0 | 3, 1 => 2 | 3, 2 => 1        -- (1 2)
  | 4, 0 => 1 | 4, 1 => 2 | 4, 2 => 0        -- (0 1 2)
  | 5, 0 => 2 | 5, 1 => 0 | 5, 2 => 1        -- (0 2 1)
  | _, _ => 0

/-- The image triple of the permutation `x`. -/
def triple (x : Nat) : Nat × Nat × Nat := (img x 0, img x 1, img x 2)

/-- The image triple of the composite "apply `y` then `x`". -/
def compTriple (x y : Nat) : Nat × Nat × Nat := (img x (img y 0), img x (img y 1), img x (img y 2))

/-- Group multiplication of `S₃`: the unique code whose triple is the composite `x ∘ y`. Self-
certifying from `img` (no hand-entered Cayley table); well-defined because the 6 permutations are
closed under composition. -/
def mulS (x y : Nat) : Nat :=
  ((List.range 6).find? (fun z => decide (triple z = compTriple x y))).getD 0

/-- Two-sided inverse of `x` in `S₃`: the unique code `y` with `xy = yx = e`. -/
def invS (x : Nat) : Nat :=
  ((List.range 6).find? (fun y => decide (mulS x y = 0 ∧ mulS y x = 0))).getD 0

/-! ### 2. `S₃` is a group -/

/-- `S₃` is a group: `0 = e` is a two-sided identity, every element has a two-sided inverse, and
`mulS` is associative — checked over all of `{0,…,5}`. -/
theorem group_axioms :
    ((List.range 6).all (fun x => decide (mulS 0 x = x ∧ mulS x 0 = x)) = true) ∧
    ((List.range 6).all (fun x => decide (mulS x (invS x) = 0 ∧ mulS (invS x) x = 0)) = true) ∧
    ((List.range 6).all (fun x => (List.range 6).all (fun y => (List.range 6).all (fun z =>
        decide (mulS (mulS x y) z = mulS x (mulS y z))))) = true) := by
  decide

/-! ### 3. The centre is trivial — forces `[𝔤] = 0` -/

/-- The centre of `S₃`: the elements commuting with everything. -/
def centre : List Nat :=
  (List.range 6).filter (fun x => (List.range 6).all (fun y => decide (mulS x y = mulS y x)))

/-- `Z(S₃) = {e}`. The coefficient group of the gerbe class is trivial, so
`[𝔤] ∈ H²(N(C); Z(S₃)) = H²(N(C); 1) = 0` is forced (classical, cited). -/
theorem centre_trivial : centre = [0] := by decide

/-! ### 4. `Inn S₃` has order 6 and `Out S₃ = 1` — forces the band `β = 0` -/

/-- The inner automorphism `conj a : y ↦ a y a⁻¹`, recorded by its value list on `{0,…,5}`. -/
def conjMap (a : Nat) : List Nat := (List.range 6).map (fun y => mulS (mulS a y) (invS a))

/-- `|Inn S₃| = 6`: the 6 conjugation maps are pairwise distinct (since `Z(S₃) = 1`, `conj` is
injective), so `Inn S₃ ≅ S₃`. -/
theorem inn_order_six :
    (List.range 6).all (fun i => (List.range 6).all (fun j =>
      decide (i = j ∨ conjMap i ≠ conjMap j))) = true := by
  decide

/-- All permutations of `[0,1,2,3,4,5]` (the carrier), generated without Mathlib. Each list `l`
encodes the candidate map `φ : i ↦ l[i]`, automatically a bijection of the carrier. -/
def insertEverywhere (a : Nat) : List Nat → List (List Nat)
  | [] => [[a]]
  | b :: bs => (a :: b :: bs) :: (insertEverywhere a bs).map (fun l => b :: l)

/-- All `720` permutations of a list. -/
def allPerms : List Nat → List (List Nat)
  | [] => [[]]
  | a :: as => (allPerms as).flatMap (fun l => insertEverywhere a l)

/-- `φ` (encoded as a value list on the carrier) is a group homomorphism of `S₃`. -/
def isHom (l : List Nat) : Bool :=
  (List.range 6).all (fun x => (List.range 6).all (fun y =>
    decide (List.getD l (mulS x y) 0 = mulS (List.getD l x 0) (List.getD l y 0))))

/-- The number of automorphisms of `S₃`: homomorphisms among all `720` permutations of the carrier
(every carrier permutation is a bijection, so homomorphism ⟹ automorphism). -/
def autCount : Nat := ((allPerms (List.range 6)).filter (fun l => isHom l)).length

/-- `|Aut S₃| = 6`, by exhaustive search over all `720` permutations of the carrier. With
`|Inn S₃| = 6` (`inn_order_six`) this gives `Out S₃ = Aut S₃ / Inn S₃ = 1`, so the band
`β ∈ H¹(N(C); Out S₃) = 0` is forced. (`S₃` is complete: Rotman GTM 148, Thm 7.5.) -/
theorem out_trivial : autCount = 6 := by decide

/-! ### 5. D2 inventory exists; D1 inventory does not — the separation

`σ = (0 1)` has code `1`. -/

/-- `σ² = e`: so `T(n) = σⁿ` is a well-defined homomorphism `ℤ → S₃`, the explicit D2 inventory lift
(`μ = id`, `conj(T(1)) = conj(σ) = ᾱ(1)`). D2 inventory exists. -/
theorem d2_lift_order_two : mulS 1 1 = 0 := by decide

/-- Every conjugate `μ σ μ⁻¹` of `σ = (0 1)` is a transposition (code in `{1,2,3}`): the D1
obstruction `o_{D1}` is exactly the transposition conjugacy class. -/
theorem sigma_conj_is_transposition :
    (List.range 6).all (fun m => decide (mulS (mulS m 1) (invS m) ∈ [1, 2, 3])) = true := by
  decide

/-- **D1 fails.** No gauge `μ ∈ S₃` conjugates `σ = (0 1)` to the identity: `∀ μ, μ σ μ⁻¹ ≠ e`.
Equivalently `o_{D1} ≠ 0`. (Since `Z(S₃) = 1`, `conj` is injective, so the gauge equation
`conj(μ σ μ⁻¹) = id` forces `μ σ μ⁻¹ = e`, impossible for `σ ≠ e`.) -/
theorem d1_fails :
    (List.range 6).all (fun m => decide (mulS (mulS m 1) (invS m) ≠ 0)) = true := by
  decide

/-! ### 6. The capstone -/

/-- **Floor separation (Rick's M1, machine-checked).** With `C = B(ℤ)`, `K = S₃`, `α = conj((0 1))`:

* `Z(S₃) = 1` (`centre = [0]`) — so `[𝔤] ∈ H²(C; Z(S₃)) = 0` is forced;
* `Out(S₃) = 1` (`autCount = 6`, with `|Inn| = 6`) — so the band `β ∈ H¹(C; Out S₃) = 0` is forced;
* D2 inventory exists — explicit lift `T(n) = σⁿ`, `σ² = e` (`mulS 1 1 = 0`);
* yet D1 inventory fails — no gauge strictifies `σ` (`∀ μ, μ σ μ⁻¹ ≠ e`).

Hence `β = 0 ∧ [𝔤] = 0` while the naive (D1) strict global inventory does not exist: the naive floor
corollary *strict `⟺ β = 0 ∧ [𝔤] = 0`* is **false**, and the honest D1 floor is a degree-1 (`H¹`)
phenomenon, not the degree-2 gerbe class. -/
theorem floor_separation :
    centre = [0] ∧
    autCount = 6 ∧
    mulS 1 1 = 0 ∧
    (List.range 6).all (fun m => decide (mulS (mulS m 1) (invS m) ≠ 0)) = true :=
  ⟨centre_trivial, out_trivial, d2_lift_order_two, d1_fails⟩

end FloorD1Separation
