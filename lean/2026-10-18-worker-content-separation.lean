/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# Worker = constant-branch slice of the weld — finite machine check

This file machine-checks the rework of clauses (2) and (3) of the worker/harness weld result
(proof `proofs/2026-10-18-worker-content-separation.md`, node `weld-is-regular-bicomodule`,
clauses now `proved`; Python oracle `scratch/2026-10-18-worker-content-separation.py`). It is a
sibling leaf of `bicomodule-axioms-lean-verified` (`lean/2026-10-17-weld-regular-bicomodule.lean`),
which already certifies the five regular-bicomodule axioms of `B = ΔS ◁ ΔT` for the clause-(1)
*existence* statement. Store comonads and the represented prafunctor are SGF Functorial Aggregation,
arXiv:2111.10968 (Example 5.6, Thm 3.1).

## Setting

`S = Fin n`, `T = Fin m` finite nonempty sets; `ΔS, ΔT` the store comonads (positions `S`,
directions `S`, with `δ_S(s,φ) = (s, i ↦ (i,φ))`, `ε_S(s,φ) = φ(s)`, `ΔS(u)(s,φ) = (s, u∘φ)`). The
weld is `B = ΔS ◁ ΔT`; a `B`-position is `(s, g)` with branch map `g ∈ T^S = Hom(S,T)` (read off the
heads of the `ΔT`-children). The worker is `A = Δ(S×T)`, read as a `(ΔT,ΔS)`-bicomodule of the same
variance as `B`.

## What is certified

**Part 1 — σ is a bicomodule iso onto the constant-branch slice `B' ⊆ B`.**
`B' = { (s,g) ∈ B : g constant }`.
* **(1b) `B'` is coaction-closed.** The weld coactions `λ = δ_{ΔS} ◁ ΔT` and `ρ = ΔS ◁ δ_{ΔT}`
  leave every branch value `g` pointwise unchanged, so `B'` is closed: for `ρ` the branch heads of
  `ρ(e)` equal those of `e`; for `λ` every inner `B`-copy of `λ(e)` reuses the children of `e`,
  hence has the same `g`. Checked on the `Tree` model at `(n,m) ∈ {(2,2),(2,3),(3,2),(1,2),(2,1)}`.
* **(1a) σ is injective with image exactly `B'`.** The map `σ₁(s,t) = (s, const_t)` (and `σ♯ = id`
  on directions) is a bijection `S×T ≅ B'`-positions; its image equals the set of constant-branch
  position-classes and has cardinality `n·m`.

**Part 2 — Σ-index separation (the counting core).** `F̄_B(V) = T^S·V^S` vs `F̄_A(V) = T·V^S`, so
`|F̄_B| = m^n·V^n` and `|F̄_A| = m·V^n`: the content power `(−)^S` is shared, the Σ-index differs
(`T^S` vs `T`). Equal (for all `V`) iff `m^n = m` iff `n=1 ∨ m=1`; proper iff `n≥2 ∧ m≥2`. Named
witness `(n,m)=(2,2)` at `V=2`: `8` vs `16`; boundary witnesses `(1,2),(1,3),(2,1)`: equal.

**Part 3 — M2 negative control (what the retract forgets).** `e(s,g) = (s, const_{g(s)})` is
idempotent with image the constant slice; its fibre over a fixed input `s` has size `m^{n-1}`
(it forgets `g|_{S∖{s}}`), which is NEITHER the non-constant maps (`m^n−m`) NOR the full Σ-index
(`m^n`). At `(n,m)=(2,3)` the three counts `3, 6, 9` are pairwise distinct — so "discarded =
non-constant maps" is FALSE.

Non-vacuity controls: `B' ⊊ B` is proper at `(2,2)` (a non-constant branch element exists), a bogus
σ-image does NOT set-equal the `B`-classes, and `gConst` rejects a genuine non-constant element.

## Model (Mathlib-free, Lean 4 core only)

No Mathlib in the container (memory `lean-Q0-evenness-polarization-general-abgrp`). The `Tree`
engine, store ops `delta`/`fmap`, coactions `lam`/`rho`, and the carrier enumerators
`listProd`/`groundLeaves`/`dtElems`/`bElems` are reused verbatim from
`lean/2026-10-17-weld-regular-bicomodule.lean`. Parts 2–3 and the σ-bijection are pure finite
combinatorics over `Nat`/`List`. Every check is a `Bool` discharged by `decide`; certificates report
`propext` only (from `decide`'s `Decidable → Bool` reduction) — no `sorryAx`, no `native_decide`.
-/

namespace WorkerSep

/-! ### Tree engine (store elements), reused from the axioms leaf -/

/-- A nested store element. `leaf v` is a ground value; `node s children` is `(s, φ)` with tuple
`φ = children`. -/
inductive Tree where
  | leaf : Nat → Tree
  | node : Nat → List Tree → Tree
deriving Repr

open Tree

set_option maxHeartbeats 4000000
set_option maxRecDepth 1000000

/-- Store comultiplication `δ (s, φ) = (s, i ↦ (i, φ))`. -/
def delta : Tree → Tree
  | leaf v => leaf v
  | node s ch => node s ((List.range ch.length).map (fun i => node i ch))

/-- Functor action `ΔS(u)(s, φ) = (s, u ∘ φ)`. -/
def fmap (u : Tree → Tree) : Tree → Tree
  | leaf v => leaf v
  | node s ch => node s (ch.map u)

/-- Left `ΔS`-coaction `λ = δ_{ΔS} ◁ ΔT`, acting on the outer (head) store factor. -/
def lam (e : Tree) : Tree := delta e

/-- Right `ΔT`-coaction `ρ = ΔS ◁ δ_{ΔT}`, acting on the inner (`ΔT`) store factor. -/
def rho (e : Tree) : Tree := fmap delta e

/-! ### Branch map and the constant-branch predicate -/

/-- Head index of a store element (the `ΔT`-position `t` of a child `(t, ψ)`). -/
def headOf : Tree → Nat
  | leaf _ => 0
  | node t _ => t

/-- The branch map `g = (t₀, …, t_{n-1})` of a `B`-element `node s [node t₀ ψ₀, …]`. -/
def heads : Tree → List Nat
  | leaf _ => []
  | node _ ch => ch.map headOf

/-- All entries of a `Nat` list are equal (constant branch map). -/
def allEqB : List Nat → Bool
  | [] => true
  | x :: xs => xs.all (· == x)

/-- A `B`-element has a constant branch map. -/
def gConst (e : Tree) : Bool := allEqB (heads e)

/-- Children of a node (the inner `B`-copies of `λ(e) = δ(e)`). -/
def innerOf : Tree → List Tree
  | leaf _ => []
  | node _ ch => ch

/-! ### Carrier enumeration `B = ΔS ◁ ΔT`, reused from the axioms leaf -/

/-- All length-`n` tuples drawn from `xs` (the `n`-fold cartesian product). -/
def listProd (xs : List α) : Nat → List (List α)
  | 0 => [[]]
  | n + 1 => (listProd xs n).flatMap (fun tail => xs.map (fun x => x :: tail))

/-- The ground object `Fin k` as leaves. -/
def groundLeaves (k : Nat) : List Tree := (List.range k).map leaf

/-- `ΔT(Fin k)`: elements `(t, ψ)` with `t ∈ T = Fin m`, `ψ : T → Fin k`. -/
def dtElems (m k : Nat) : List Tree :=
  (List.range m).flatMap (fun t => (listProd (groundLeaves k) m).map (fun psi => node t psi))

/-- The carrier `B(Fin k) = ΔS(ΔT(Fin k))`: elements `(s, φ)` with `s ∈ S = Fin n` and
`φ : S → ΔT(Fin k)`. -/
def bElems (n m k : Nat) : List Tree :=
  (List.range n).flatMap (fun s => (listProd (dtElems m k) n).map (fun phi => node s phi))

/-- The constant-branch slice `B'(Fin k) ⊆ B(Fin k)`. -/
def bpElems (n m k : Nat) : List Tree := (bElems n m k).filter gConst

/-! ### Part 1b — `B'` is closed under the weld coactions `λ`, `ρ` -/

/-- `ρ`-closure: the branch heads of `ρ(e)` equal those of `e`, so `ρ` preserves `B'`. -/
def rhoClosed (n m k : Nat) : Bool := (bpElems n m k).all (fun e => gConst (rho e))

/-- `λ`-closure: every inner `B`-copy of `λ(e) = δ(e)` reuses the children of `e`, hence lies in
`B'`. -/
def lamClosed (n m k : Nat) : Bool :=
  (bpElems n m k).all (fun e => (innerOf (lam e)).all gConst)

theorem rho_closed_2_2 : rhoClosed 2 2 2 = true := by decide
theorem rho_closed_2_3 : rhoClosed 2 3 2 = true := by decide
theorem rho_closed_3_2 : rhoClosed 3 2 2 = true := by decide
theorem rho_closed_1_2 : rhoClosed 1 2 2 = true := by decide
theorem rho_closed_2_1 : rhoClosed 2 1 2 = true := by decide

theorem lam_closed_2_2 : lamClosed 2 2 2 = true := by decide
theorem lam_closed_2_3 : lamClosed 2 3 2 = true := by decide
theorem lam_closed_3_2 : lamClosed 3 2 2 = true := by decide
theorem lam_closed_1_2 : lamClosed 1 2 2 = true := by decide
theorem lam_closed_2_1 : lamClosed 2 1 2 = true := by decide

/-! ### Part 1a — σ is injective with image exactly `B'` (position-class level)

`B`-positions modulo direction fillers are the classes `(s, g)` with `s ∈ S`, `g ∈ T^S`. The worker
map is `σ₁(s,t) = (s, const_t)` with `σ♯ = id`; its image is the constant-branch classes. -/

/-- Equality of `Nat` lists (branch maps), hand-rolled to avoid instance surprises. -/
def natListEq : List Nat → List Nat → Bool
  | [], [] => true
  | x :: xs, y :: ys => (x == y) && natListEq xs ys
  | _, _ => false

/-- Equality of position-classes `(s, g)`. -/
def pEq (a b : Nat × List Nat) : Bool := (a.1 == b.1) && natListEq a.2 b.2

/-- Membership of a position-class in a list of classes. -/
def pMem (x : Nat × List Nat) (l : List (Nat × List Nat)) : Bool := l.any (pEq x)

/-- `a ⊆ b` for lists of position-classes. -/
def pSubset (a b : List (Nat × List Nat)) : Bool := a.all (fun x => pMem x b)

/-- Set-equality for lists of position-classes. -/
def pSetEq (a b : List (Nat × List Nat)) : Bool := pSubset a b && pSubset b a

/-- `T^S = Hom(S,T)` as length-`n` tuples over `Fin m`. -/
def allMaps (n m : Nat) : List (List Nat) := listProd (List.range m) n

/-- `B`-position-classes `(s, g)`. -/
def bClasses (n m : Nat) : List (Nat × List Nat) :=
  (List.range n).flatMap (fun s => (allMaps n m).map (fun g => (s, g)))

/-- `B'`-position-classes: the constant-branch classes. -/
def bpClasses (n m : Nat) : List (Nat × List Nat) := (bClasses n m).filter (fun p => allEqB p.2)

/-- Image of `σ`: `{ (s, const_t) : s ∈ S, t ∈ T }`. -/
def sigmaImg (n m : Nat) : List (Nat × List Nat) :=
  (List.range n).flatMap (fun s => (List.range m).map (fun t => (s, List.replicate n t)))

/-- `σ` is a bijection onto `B'`-positions: image set-equals the constant-branch classes, and both
have cardinality `n·m` (so `σ₁` is injective, `σ♯ = id`). -/
def sigmaIso (n m : Nat) : Bool :=
  pSetEq (bpClasses n m) (sigmaImg n m)
    && ((sigmaImg n m).length == n * m)
    && ((bpClasses n m).length == n * m)

theorem sigma_iso_2_2 : sigmaIso 2 2 = true := by decide
theorem sigma_iso_2_3 : sigmaIso 2 3 = true := by decide
theorem sigma_iso_3_2 : sigmaIso 3 2 = true := by decide
theorem sigma_iso_1_2 : sigmaIso 1 2 = true := by decide
theorem sigma_iso_2_1 : sigmaIso 2 1 = true := by decide

/-! ### Part 2 — Σ-index separation (the counting core) -/

/-- `|F̄_A(V)| = |T| · |V|^|S| = m · V^n`. -/
def faCard (n m V : Nat) : Nat := m * V ^ n

/-- `|F̄_B(V)| = |T|^|S| · |V|^|S| = m^n · V^n`. -/
def fbCard (n m V : Nat) : Nat := m ^ n * V ^ n

/-- Named witness `(n,m) = (2,2)` at `V = 2`: worker `8`, weld `16` (proper). -/
theorem card_witness_2_2 : faCard 2 2 2 = 8 ∧ fbCard 2 2 2 = 16 := by decide

/-- Boundary witnesses `(1,2), (1,3), (2,1)` at `V = 2`: worker `=` weld. -/
theorem card_boundary_equal :
    faCard 1 2 2 = fbCard 1 2 2 ∧ faCard 1 3 2 = fbCard 1 3 2 ∧ faCard 2 1 2 = fbCard 2 1 2 := by
  decide

/-- The equality locus: `F̄_A ≅ F̄_B` for all `V` iff `m^n = m` iff `n = 1 ∨ m = 1`. Checked on a
grid including the proper corner `n,m ≥ 2`. -/
def locusCheck : Bool :=
  [(1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3), (2, 1), (1, 1)].all
    (fun p => (p.2 ^ p.1 == p.2) == (p.1 == 1 || p.2 == 1))

theorem locus_grid : locusCheck = true := by decide

/-- For `V ≥ 1` the two cardinalities agree exactly on the equality locus (checked at `V = 1,2,3`
over the grid). -/
def cardLocusCheck : Bool :=
  [(1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (2, 1)].all (fun p =>
    [1, 2, 3].all (fun V =>
      (faCard p.1 p.2 V == fbCard p.1 p.2 V) == (p.1 == 1 || p.2 == 1)))

theorem card_locus_grid : cardLocusCheck = true := by decide

/-! ### Part 3 — M2 negative control: what the retract forgets -/

/-- The retract's branch output `e(s,g) = const_{g(s)}` (position stays `s`). -/
def retr (n s : Nat) (g : List Nat) : List Nat := List.replicate n (g.getD s 0)

/-- `e` is idempotent: `e ∘ e = e`. -/
def retrIdem (n m : Nat) : Bool :=
  (List.range n).all (fun s =>
    (allMaps n m).all (fun g => natListEq (retr n s (retr n s g)) (retr n s g)))

/-- Image of `e` is exactly the constant slice `σ(A) = B'`-positions. -/
def retrImg (n m : Nat) : Bool :=
  pSetEq ((List.range n).flatMap (fun s => (allMaps n m).map (fun g => (s, retr n s g))))
    (sigmaImg n m)

/-- Every fibre of `e` over a fixed input `s` has size `m^{n-1}` (it forgets `g|_{S∖{s}}`). -/
def fibreOk (n m : Nat) : Bool :=
  (List.range n).all (fun s =>
    (List.range m).all (fun t =>
      ((allMaps n m).filter (fun g => g.getD s 0 == t)).length == m ^ (n - 1)))

theorem retr_idem_2_2 : retrIdem 2 2 = true := by decide
theorem retr_idem_2_3 : retrIdem 2 3 = true := by decide
theorem retr_idem_3_2 : retrIdem 3 2 = true := by decide

theorem retr_img_2_2 : retrImg 2 2 = true := by decide
theorem retr_img_2_3 : retrImg 2 3 = true := by decide
theorem retr_img_3_2 : retrImg 3 2 = true := by decide

theorem fibre_2_2 : fibreOk 2 2 = true := by decide
theorem fibre_2_3 : fibreOk 2 3 = true := by decide
theorem fibre_3_2 : fibreOk 3 2 = true := by decide

/-- The three cardinalities are pairwise distinct. -/
def allDistinct3 (a b c : Nat) : Bool := (a != b) && (b != c) && (a != c)

/-- At `(n,m) = (2,3)`: discard fibre `m^{n-1} = 3`, non-constant maps `m^n − m = 6`, full Σ-index
`m^n = 9` — pairwise distinct, so "discarded = non-constant maps" is FALSE. -/
theorem m2_distinct_2_3 : allDistinct3 (3 ^ (2 - 1)) (3 ^ 2 - 3) (3 ^ 2) = true := by decide

/-- The named triple itself, for the record. -/
theorem m2_triple_2_3 : (3 ^ (2 - 1), 3 ^ 2 - 3, 3 ^ 2) = (3, 6, 9) := by decide

/-! ### Non-vacuity controls -/

/-- `B' ⊊ B` is a proper inclusion at `(2,2)`: there is a non-constant branch element. -/
theorem bp_proper_2_2 : (bpElems 2 2 2).length < (bElems 2 2 2).length := by decide

/-- `gConst` genuinely rejects a non-constant branch element. -/
theorem gConst_rejects : gConst (node 0 [node 0 [], node 1 []]) = false := by decide

/-- A bogus σ-image (the full `B`-classes at `(2,2)`) does NOT set-equal `B'`: the counting checks
are not vacuously true. -/
theorem sigma_not_vacuous_2_2 : pSetEq (sigmaImg 2 2) (bClasses 2 2) = false := by decide

end WorkerSep
