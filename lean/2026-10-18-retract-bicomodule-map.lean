/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# `r_{s0}` is a bicomodule retraction `B ↠ B'`; the retract `e` is NOT a bicomodule map

This file certifies Rick's referee MUST **M1** (report `uid233`,
`proofs/reviews/2026-10-18-weld-is-regular-bicomodule-rick.md`) against the worker/weld result
(node `weld-is-regular-bicomodule`, child `clause3-tail-is-branch-maps-TRUE`; proof
`proofs/2026-10-18-worker-content-separation.md`). It is a sibling leaf of
`worker-content-separation-lean-verified` (`lean/2026-10-18-worker-content-separation.lean`), whose
checks of the retract `e` are purely at the level of **position-sets** (idempotent, image, fibre).
Here we isolate exactly the structure those checks did not see: the **bicomodule coaction squares**.

Store comonads and the weld are SGF Functorial Aggregation, arXiv:2111.10968 (Example 5.6, Thm 3.1);
the regular `(ΔT,ΔS)`-bicomodule `B = ΔS ◁ ΔT` is the peer-reviewed clause-(1) core
(`lean/2026-10-17-weld-regular-bicomodule.lean`, five axioms machine-checked).

## Setting

`S = Fin n`, `T = Fin m`; `ΔS, ΔT` the store comonads, `δ_S(s, φ) = (s, i ↦ (i, φ))`,
`ΔS(u)(s, φ) = (s, u ∘ φ)`. `B = ΔS ◁ ΔT`; a `B`-element is `node s [node t₀ ψ₀, …]`, with branch
map `g = (t₀, …, t_{n-1}) ∈ T^S` read off the child heads. Left coaction `λ = δ_{ΔS} ◁ ΔT = delta`
(acts on the outer head factor); right coaction `ρ = ΔS ◁ δ_{ΔT} = fmap delta` (acts inside each
`ΔT`-child). `B' ⊆ B` is the **constant-branch slice** (`g` constant), `B' ≅ Δ(S×T) = A`.

Two candidate idempotents onto `B'`, differing only in which head they broadcast; both keep
`r♯ = id` on directions (they rewrite only the position data `g`, never the `ψ`-tuples):

* `e(s, g) = (s, const_{g(s)})`   — head at the **current** position `s`   (`eMap`);
* `r_{s0}(s, g) = (s, const_{g(s0)})` — head at a **fixed** base point `s0` (`rMap s0`).

## What is certified

A `(ΔT,ΔS)`-bicomodule endomorphism `f : B → B` landing in `B'` must commute with both coactions.
Since `B'` inherits the restricted coactions, the squares are, as equalities of `B`-elements:

* **λ-square** `λ_{B'} ∘ f = (ΔS ◁ f) ∘ λ_B`   encoded `teq (lam (f e)) (fmap f (lam e))`
  (`ΔS ◁ f = fmap f`, exactly as in the compatibility axiom `ax5` of the axioms leaf);
* **ρ-square** `ρ_{B'} ∘ f = (f ◁ ΔT) ∘ ρ_B`   encoded `teq (rho (f e)) (f (rho e))`
  (`f ◁ ΔT` is `f` evaluated at the object `ΔT(X)`; the encodings `eMap`/`rMap` inspect only the
  outer position and the child heads and never the direction tuples, so they are natural in the leaf
  content, making `f` at `ΔT(X)` literally `f (rho e)`).

**Part 1 — `r_{s0}` IS a bicomodule retraction `B ↠ B'`.** For `s0 = 0` (and `s0 = 1` at `(2,2)`),
`rMap s0` passes BOTH squares on all of `B`, is idempotent, has image inside `B'`, and restricts to
the identity on `B'` (`r ∘ ι_{B'} = id_{B'}` — a genuine retraction). Shapes
`(n,m) ∈ {(2,2),(2,3),(3,2),(1,2),(2,1)}`, ground `k = 2`.

**Part 2 — `e` is NOT a bicomodule map.** `eMap` passes the ρ-square everywhere but FAILS the
λ-square on `B` exactly when a non-constant branch map exists, i.e. at `n,m ≥ 2`
(`(2,2),(2,3),(3,2)`); it passes on the boundary shapes `(1,2),(2,1)` (where every `g` is constant)
and, as a control, on the constant-branch slice `B'` at every shape. The explicit first failure is
Rick's witness: shape `(2,2)`, element `node 0 [node 0 [leaf 0, leaf 0], node 1 [leaf 0, leaf 0]]`
(position `(0, g=(0,1))`), a `decide`-checked `lamSquare eMap · = false`, while `rMap 0`/`rMap 1`
pass on the same element.

**Part 3 — `r_{s0}` keeps every number (`e`/`r` agree on `F̄`).** Position-level: `rMap s0` has
image the constant slice (`= σ(A)`, same as `e`) and every fibre has size `m^{n-1}` (same as `e`).
So switching `e ⇝ r_{s0}` for the bicomodule interpretation changes none of the counts the existing
leaf verified, nor the represented prafunctor `F̄`.

Non-vacuity: the λ-square genuinely distinguishes the two maps on Rick's witness (`r` true, `e`
false), the witness is a real carrier element and is non-constant, and `rMap`'s image set-equals the
constant slice but NOT the full `B`-classes.

## Model (Mathlib-free, Lean 4 core only)

No Mathlib in the container. The `Tree` engine, store ops `delta`/`fmap`, coactions `lam`/`rho`, and
the carrier enumerators `listProd`/`dtElems`/`bElems`/`bpElems` are reused verbatim from
`lean/2026-10-18-worker-content-separation.lean`; `teq`/`teqs` (structural `Tree` equality) from
`lean/2026-10-17-weld-regular-bicomodule.lean`. Every check is a `Bool` discharged by `decide`;
certificates report `propext` only — no `sorryAx`, no `native_decide`. Carriers kept at `k = 2` to
stay inside the kernel-`decide` budget (the two large `k = 3` carriers OOM; nothing lost — `k = 2`
already carries non-constant branch tuples for every shape).
-/

namespace RetractBicomodule

/-! ### Tree engine (store elements), reused from the sibling leaves -/

/-- A nested store element. `leaf v` is a ground value; `node s children` is `(s, φ)` with tuple
`φ = children`. -/
inductive Tree where
  | leaf : Nat → Tree
  | node : Nat → List Tree → Tree
deriving Repr

open Tree

set_option maxHeartbeats 4000000
set_option maxRecDepth 1000000

/- Structural Boolean equality (the derived handler does not fire through `List Tree`). -/
mutual
  /-- Structural Boolean equality of trees. -/
  def teq : Tree → Tree → Bool
    | leaf a, leaf b => a == b
    | node s cs, node t ds => (s == t) && teqs cs ds
    | _, _ => false
  /-- Structural Boolean equality of children lists. -/
  def teqs : List Tree → List Tree → Bool
    | [], [] => true
    | c :: cs, d :: ds => teq c d && teqs cs ds
    | _, _ => false
end

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

/-- Head index of a store element (the `ΔT`-position `t` of a child `(t, ψ)`). -/
def headOf : Tree → Nat
  | leaf _ => 0
  | node t _ => t

/-- The branch map `g = (t₀, …, t_{n-1})` of a `B`-element. -/
def heads : Tree → List Nat
  | leaf _ => []
  | node _ ch => ch.map headOf

/-- All entries of a `Nat` list are equal (constant branch map). -/
def allEqB : List Nat → Bool
  | [] => true
  | x :: xs => xs.all (· == x)

/-- A `B`-element has a constant branch map (membership in the slice `B'`). -/
def gConst (e : Tree) : Bool := allEqB (heads e)

/-! ### The two retract maps `e` and `r_{s0}` (both keep `r♯ = id` on directions) -/

/-- Rewrite a child's head to `h`, keeping its direction tuple (`r♯ = id`). -/
def setHead (h : Nat) : Tree → Tree
  | leaf v => leaf v
  | node _ ch => node h ch

/-- The dynamic retract `e(s, g) = (s, const_{g(s)})`: broadcast the head at the **current**
position `s`. -/
def eMap : Tree → Tree
  | leaf v => leaf v
  | node s ch => node s (ch.map (setHead (headOf (ch.getD s (leaf 0)))))

/-- The based retract `r_{s0}(s, g) = (s, const_{g(s0)})`: broadcast the head at the **fixed** base
point `s0`. Keeps the position `s`. -/
def rMap (s0 : Nat) : Tree → Tree
  | leaf v => leaf v
  | node s ch => node s (ch.map (setHead (headOf (ch.getD s0 (leaf 0)))))

/-! ### The two bicomodule-equivariance squares for an endomorphism `f : B → B` -/

/-- λ-equivariance: `λ_{B'} ∘ f = (ΔS ◁ f) ∘ λ_B`, i.e. `delta (f e) = fmap f (delta e)`. -/
def lamSquare (f : Tree → Tree) (e : Tree) : Bool := teq (lam (f e)) (fmap f (lam e))

/-- ρ-equivariance: `ρ_{B'} ∘ f = (f ◁ ΔT) ∘ ρ_B`, i.e. `rho (f e) = f (rho e)` (`f ◁ ΔT = f` at
object `ΔT(X)`). -/
def rhoSquare (f : Tree → Tree) (e : Tree) : Bool := teq (rho (f e)) (f (rho e))

/-! ### Carrier enumeration `B = ΔS ◁ ΔT`, reused from the sibling leaf -/

/-- All length-`n` tuples drawn from `xs` (the `n`-fold cartesian product). -/
def listProd (xs : List α) : Nat → List (List α)
  | 0 => [[]]
  | n + 1 => (listProd xs n).flatMap (fun tail => xs.map (fun x => x :: tail))

/-- The ground object `Fin k` as leaves. -/
def groundLeaves (k : Nat) : List Tree := (List.range k).map leaf

/-- `ΔT(Fin k)`: elements `(t, ψ)` with `t ∈ T = Fin m`, `ψ : T → Fin k`. -/
def dtElems (m k : Nat) : List Tree :=
  (List.range m).flatMap (fun t => (listProd (groundLeaves k) m).map (fun psi => node t psi))

/-- The carrier `B(Fin k) = ΔS(ΔT(Fin k))`. -/
def bElems (n m k : Nat) : List Tree :=
  (List.range n).flatMap (fun s => (listProd (dtElems m k) n).map (fun phi => node s phi))

/-- The constant-branch slice `B'(Fin k) ⊆ B(Fin k)`. -/
def bpElems (n m k : Nat) : List Tree := (bElems n m k).filter gConst

/-! ### Part 1 — `r_{s0}` is a bicomodule retraction `B ↠ B'`

For `s0 = 0` (any valid base point works; `s0 = 1` is also checked at `(2,2)`): both squares hold on
all of `B`, `rMap` is idempotent with image in `B'`, and restricts to the identity on `B'`. -/

/-- `r_{s0}` passes the λ-square on every `B`-element. -/
def rLamOk (s0 n m k : Nat) : Bool := (bElems n m k).all (lamSquare (rMap s0))

/-- `r_{s0}` passes the ρ-square on every `B`-element. -/
def rRhoOk (s0 n m k : Nat) : Bool := (bElems n m k).all (rhoSquare (rMap s0))

/-- `r_{s0}` is idempotent. -/
def rIdem (s0 n m k : Nat) : Bool :=
  (bElems n m k).all (fun e => teq (rMap s0 (rMap s0 e)) (rMap s0 e))

/-- `r_{s0}` has image inside the constant-branch slice `B'`. -/
def rImgBp (s0 n m k : Nat) : Bool := (bElems n m k).all (fun e => gConst (rMap s0 e))

/-- `r_{s0} ∘ ι_{B'} = id_{B'}`: it restricts to the identity on the slice (retraction). -/
def rRetract (s0 n m k : Nat) : Bool := (bpElems n m k).all (fun e => teq (rMap s0 e) e)

theorem r_lam_2_2 : rLamOk 0 2 2 2 = true := by decide
theorem r_lam_2_3 : rLamOk 0 2 3 2 = true := by decide
theorem r_lam_3_2 : rLamOk 0 3 2 2 = true := by decide
theorem r_lam_1_2 : rLamOk 0 1 2 2 = true := by decide
theorem r_lam_2_1 : rLamOk 0 2 1 2 = true := by decide

/-- Base-point independence of the retraction property: `s0 = 1` also works at `(2,2)`. -/
theorem r_lam_2_2_s1 : rLamOk 1 2 2 2 = true := by decide

theorem r_rho_2_2 : rRhoOk 0 2 2 2 = true := by decide
theorem r_rho_2_3 : rRhoOk 0 2 3 2 = true := by decide
theorem r_rho_3_2 : rRhoOk 0 3 2 2 = true := by decide
theorem r_rho_1_2 : rRhoOk 0 1 2 2 = true := by decide
theorem r_rho_2_1 : rRhoOk 0 2 1 2 = true := by decide

theorem r_idem_2_2 : rIdem 0 2 2 2 = true := by decide
theorem r_idem_2_3 : rIdem 0 2 3 2 = true := by decide
theorem r_idem_3_2 : rIdem 0 3 2 2 = true := by decide

theorem r_img_2_2 : rImgBp 0 2 2 2 = true := by decide
theorem r_img_2_3 : rImgBp 0 2 3 2 = true := by decide
theorem r_img_3_2 : rImgBp 0 3 2 2 = true := by decide

theorem r_retract_2_2 : rRetract 0 2 2 2 = true := by decide
theorem r_retract_2_3 : rRetract 0 2 3 2 = true := by decide
theorem r_retract_3_2 : rRetract 0 3 2 2 = true := by decide
theorem r_retract_1_2 : rRetract 0 1 2 2 = true := by decide
theorem r_retract_2_1 : rRetract 0 2 1 2 = true := by decide

/-! ### Part 2 — `e` is NOT a bicomodule map: it fails the λ-square -/

/-- `e` passes the ρ-square on every `B`-element (ρ does not distinguish the two maps). -/
def eRhoOk (n m k : Nat) : Bool := (bElems n m k).all (rhoSquare eMap)

/-- `e` on the λ-square over all of `B`. `true` iff every branch map is constant, i.e. `n=1 ∨ m=1`;
`false` at `n,m ≥ 2`. -/
def eLamOk (n m k : Nat) : Bool := (bElems n m k).all (lamSquare eMap)

/-- `e` on the λ-square over the constant-branch slice `B'` (control: here `e = r`, both pass). -/
def eLamOkBp (n m k : Nat) : Bool := (bpElems n m k).all (lamSquare eMap)

theorem e_rho_2_2 : eRhoOk 2 2 2 = true := by decide
theorem e_rho_2_3 : eRhoOk 2 3 2 = true := by decide
theorem e_rho_3_2 : eRhoOk 3 2 2 = true := by decide

/-- `e` FAILS the λ-square at `(2,2)`, `(2,3)`, `(3,2)` — the `n,m ≥ 2` locus. -/
theorem e_lam_fails_2_2 : eLamOk 2 2 2 = false := by decide
theorem e_lam_fails_2_3 : eLamOk 2 3 2 = false := by decide
theorem e_lam_fails_3_2 : eLamOk 3 2 2 = false := by decide

/-- `e` passes the λ-square on the boundary shapes `(1,2)`, `(2,1)` (no non-constant branch map). -/
theorem e_lam_holds_1_2 : eLamOk 1 2 2 = true := by decide
theorem e_lam_holds_2_1 : eLamOk 2 1 2 = true := by decide

/-- Control: on the constant-branch slice `B'`, `e` DOES satisfy the λ-square (there `e = r`). -/
theorem e_lam_ok_bp_2_2 : eLamOkBp 2 2 2 = true := by decide
theorem e_lam_ok_bp_2_3 : eLamOkBp 2 3 2 = true := by decide
theorem e_lam_ok_bp_3_2 : eLamOkBp 3 2 2 = true := by decide

/-! #### Rick's explicit first-failure witness

Shape `(2,2)`, position `(0, g=(0,1))`, direction tuples `ψ = (0,0)`: a genuine non-constant
carrier element on which the λ-square separates `e` (fails) from `r_{s0}` (holds). -/

/-- The witness element `node 0 [node 0 [leaf 0, leaf 0], node 1 [leaf 0, leaf 0]]`. -/
def witE : Tree := node 0 [node 0 [leaf 0, leaf 0], node 1 [leaf 0, leaf 0]]

/-- The witness is a genuine carrier element of `B(Fin 2)` at `(2,2)`. -/
theorem witE_mem : (bElems 2 2 2).any (teq witE) = true := by decide

/-- The witness has a non-constant branch map `g = (0,1)`. -/
theorem witE_nonconst : gConst witE = false := by decide

/-- `e` fails λ-equivariance on the witness (Rick's `uid233` M1 counterexample). -/
theorem e_fails_lam_wit : lamSquare eMap witE = false := by decide

/-- `r_{s0}` passes λ-equivariance on the witness, for base point `s0 = 0` and `s0 = 1`. -/
theorem r_passes_lam_wit0 : lamSquare (rMap 0) witE = true := by decide
theorem r_passes_lam_wit1 : lamSquare (rMap 1) witE = true := by decide

/-- Both maps pass the ρ-square on the witness (ρ never distinguishes them). -/
theorem e_passes_rho_wit : rhoSquare eMap witE = true := by decide
theorem r_passes_rho_wit0 : rhoSquare (rMap 0) witE = true := by decide

/-! ### Part 3 — `r_{s0}` keeps every number (`e`/`r` agree on `F̄`)

Position-class level. `r_{s0}` sends `(s, g) ↦ (s, const_{g(s0)})`; its image is the constant slice
(`= σ(A)`, exactly `e`'s image) and each fibre has size `m^{n-1}` (exactly `e`'s fibre). -/

/-- `T^S = Hom(S,T)` as length-`n` tuples over `Fin m`. -/
def allMaps (n m : Nat) : List (List Nat) := listProd (List.range m) n

/-- Equality of `Nat` lists (branch maps). -/
def natListEq : List Nat → List Nat → Bool
  | [], [] => true
  | x :: xs, y :: ys => (x == y) && natListEq xs ys
  | _, _ => false

/-- Equality of position-classes `(s, g)`. -/
def pEq (a b : Nat × List Nat) : Bool := (a.1 == b.1) && natListEq a.2 b.2

/-- Membership / subset / set-equality for lists of position-classes. -/
def pMem (x : Nat × List Nat) (l : List (Nat × List Nat)) : Bool := l.any (pEq x)
def pSubset (a b : List (Nat × List Nat)) : Bool := a.all (fun x => pMem x b)
def pSetEq (a b : List (Nat × List Nat)) : Bool := pSubset a b && pSubset b a

/-- `σ`-image: the constant slice `{ (s, const_t) }`. -/
def sigmaImg (n m : Nat) : List (Nat × List Nat) :=
  (List.range n).flatMap (fun s => (List.range m).map (fun t => (s, List.replicate n t)))

/-- `r_{s0}` on position-classes: `g ↦ const_{g(s0)}`. -/
def retrR (n s0 : Nat) (g : List Nat) : List Nat := List.replicate n (g.getD s0 0)

/-- Image of `r_{s0}` on position-classes equals the constant slice (same as `e`'s image). -/
def retrImgR (n m s0 : Nat) : Bool :=
  pSetEq ((List.range n).flatMap (fun s => (allMaps n m).map (fun g => (s, retrR n s0 g))))
    (sigmaImg n m)

/-- Every fibre of `r_{s0}` (over a fixed target head `t`) has size `m^{n-1}` — `e`'s count. -/
def fibreOkR (n m s0 : Nat) : Bool :=
  (List.range m).all (fun t =>
    ((allMaps n m).filter (fun g => g.getD s0 0 == t)).length == m ^ (n - 1))

theorem r_img_classes_2_2 : retrImgR 2 2 0 = true := by decide
theorem r_img_classes_2_3 : retrImgR 2 3 0 = true := by decide
theorem r_img_classes_3_2 : retrImgR 3 2 0 = true := by decide

theorem r_fibre_2_2 : fibreOkR 2 2 0 = true := by decide
theorem r_fibre_2_3 : fibreOkR 2 3 0 = true := by decide
theorem r_fibre_3_2 : fibreOkR 3 2 0 = true := by decide

/-- Base-point independence of the fibre count: `s0 = 1` gives the same `m^{n-1}` at `(2,2)`. -/
theorem r_fibre_2_2_s1 : fibreOkR 2 2 1 = true := by decide

/-! ### Non-vacuity controls -/

/-- The λ-square genuinely separates the two maps on the witness: `r` true, `e` false. -/
theorem lam_separates_wit :
    (lamSquare (rMap 0) witE = true) ∧ (lamSquare eMap witE = false) := by decide

/-- `B' ⊊ B` is proper at `(2,2)` (a non-constant branch element exists), so the λ-failure of `e`
on `B` is not vacuous. -/
theorem bp_proper_2_2 : (bpElems 2 2 2).length < (bElems 2 2 2).length := by decide

/-- `r_{s0}`'s image set-equals the constant slice but NOT the full `B`-classes (counting not
vacuous). -/
theorem r_img_not_full_2_2 :
    pSetEq ((List.range 2).flatMap (fun s => (allMaps 2 2).map (fun g => (s, retrR 2 0 g))))
      ((List.range 2).flatMap (fun s => (allMaps 2 2).map (fun g => (s, g)))) = false := by decide

end RetractBicomodule
