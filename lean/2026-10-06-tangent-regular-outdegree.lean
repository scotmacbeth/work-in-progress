/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# Out-degree homogeneity ⟺ tangent-regularity (the Lanfranchi-refutation salvage)

This file machine-checks the **surviving positive** of the refutation
"the Lanfranchi parallelizability port fails for polynomial comonoids"
(proof note `proofs/2026-10-05-lie-parallelizable-poly-comonoid.md`;
registry `lie-parallelizable-poly-comonoid`; refutation of `state/PROVE.md` Conjecture P).

Lanfranchi's Lie-group↔Lie-algebra correspondence (arXiv:2609.03449, Def. 4.18, Thm 4.20)
lives in a **Cartesian** tangent category; the AAGM container derivative `∂` is representable
(`T = (−) ◁ D`), hence **not** Cartesian, so the literal port is ill-posed (Theorem I of the
note). What survives is a single fibre-rank dividing line (Theorems II–III of the note):

For a polynomial comonoid `p = Σ_{a ∈ Ob} y^{E_a}` (= a small category, `E_a` = the out-morphisms
at object `a`, `|E_a|` = out-degree), the representable tangent bundle `Tp = p ◁ D = p + εv·∂p`
has, over a point of shape `a`, tangent space the free module `W^{E_a}` of rank `|E_a|` (note,
Lemma 1). Two free modules are isomorphic iff their ranks agree, so **all fibres are isomorphic to
a single object `m` ("tangent-regular") iff the out-degrees `|E_a|` are constant in `a`**
("out-degree homogeneous") — note, Theorem 2.

The honest punchline (note, Theorem 3) is **composition-blindness**: tangent-regularity reads only
the underlying polynomial functor `U(p)` — equivalently the *multiset* `{|E_a|}` of out-degrees —
and is therefore blind to the comonoid structure `δ : p → p ◁ p` (the composition). So it can never
be equivalent to a composition-level property such as "groupoid":
* **tangent-regular ⇏ groupoid**: the group `ℤ/2` and the idempotent monoid `{1, e}` (`e² = e`)
  have the *same* underlying functor `y²` (one object, out-degree `2`), hence the same tangent
  bundle; both are tangent-regular, but `ℤ/2` is a groupoid and `{1, e}` is not.
* **groupoid ⇏ tangent-regular**: the groupoid `ℤ/2 ⊔ ℤ/3` has out-degrees `{2, 3}`, not constant,
  so it is not tangent-regular.

## What this file certifies (and what it does not)

Certified here, in core Lean (`Nat`/`Fin`/`List`, no `Classical`):

1. `tangentRegular_iff` — the multiplicity-uniformity core: for out-degrees `d : Fin k → Nat`,
   `TangentRegular d ↔ ∀ i j, d i = d j` (homogeneity). This is note Theorem 2 as pure arithmetic.
2. `allPairsEq_ofFn` — the indexed form `∀ i j, d i = d j` agrees with the list form
   `allPairsEq (List.ofFn d)`, so (1) is literally a statement about the list of out-degrees.
3. `tregB_perm` — **composition-blindness, formalised**: the decidable tangent-regularity test
   `tregB : List Nat → Bool` is invariant under permutation of the out-degree list, i.e. it descends
   to the *multiset* `Multiset = List/Perm`. A `◁`-comonoid's composition is extra data not
   recoverable from this multiset, so `tregB` cannot see it.
4. `treg_blind_to_composition`, `groupoid_not_tangentRegular` — the two explicit witnesses as
   `decide`-able facts on a minimal `FinCat` model that carries out-degrees plus an *opaque*
   composition label `isGroupoid`. `treg` reads only the out-degrees; varying the label (the
   composition) leaves it fixed.

**Not** certified here (cited framework, note §§1–3 and upstream): that the representable fibre at a
shape-`a` point really is `W^{E_a}` of rank `|E_a|` (note Lemma 1, `tangent-uniqueness-spoly`,
`virtual-container-cartan` Prop. 2); that `U : Cat ≃ Comon(Poly, ◁) → Poly` is the forgetful functor
(Ahman–Uustalu, `cat-hash-is-dcont-cof`); and that the abstract labels `isGroupoid` are realised by
the genuine categories `ℤ/2`, `{1, e}`, `ℤ/2 ⊔ ℤ/3`. Those are structural inputs, not `decide`-able.
What is machine-checked is the *arithmetic + multiset-factoring content* of the dividing line: it is
exactly out-degree homogeneity, and homogeneity is a permutation-invariant (multiset) property,
hence composition-blind.

Pattern reused from `lean/2026-10-05-two-model-distinction.lean` (the decidable-`↔` oracle for the
sibling refutation) and `lean/2026-10-04-universality-rank-rigidity.lean`.
-/

namespace TangentRegularOutDegree

/-! ### 1. The indexed form: tangent-regular ⟺ out-degree homogeneous (note Theorem 2)

Out-degrees of a comonoid `p = Σ_a y^{E_a}` are a map `d : Fin k → Nat`, `d a = |E_a|`. By note
Lemma 1 the tangent fibre over a shape-`a` point is the free module of rank `d a`; the bundle is
**tangent-regular** when all fibres are isomorphic to one module, i.e. all ranks are a common `m`. -/

/-- A polynomial comonoid (out-degree sequence `d`) is **tangent-regular** when the representable
tangent bundle `Tp = p ◁ D` has all fibres isomorphic to one module `m` — equivalently (note
Lemma 1) when the fibre ranks `d i = |E_i|` are all equal to a common value `m`. -/
def TangentRegular {k : Nat} (d : Fin k → Nat) : Prop := ∃ m, ∀ i, d i = m

/-- **Theorem 2 (note §3).** Tangent-regularity ⟺ out-degree homogeneity: all `|E_a|` equal.
Two free modules are isomorphic iff their ranks agree, so a common fibre module exists iff all
out-degrees coincide. -/
theorem tangentRegular_iff {k : Nat} (d : Fin k → Nat) :
    TangentRegular d ↔ ∀ i j, d i = d j := by
  constructor
  · rintro ⟨m, hm⟩ i j
    rw [hm i, hm j]
  · intro h
    cases k with
    | zero => exact ⟨0, fun i => i.elim0⟩
    | succ n => exact ⟨d ⟨0, Nat.succ_pos n⟩, fun i => h i ⟨0, Nat.succ_pos n⟩⟩

/-! ### 2. The list form and the bridge to the indexed form

"All out-degrees equal" written on the list `List.ofFn d` of out-degrees, so §3's multiset
statement is literally about the same property. -/

/-- All entries of a list are pairwise equal. On the out-degree list this is "out-degree
homogeneous"; it is manifestly symmetric in the entries, which is what makes it a multiset
property (§3). -/
def allPairsEq (l : List Nat) : Prop := ∀ a ∈ l, ∀ b ∈ l, a = b

/-- The indexed homogeneity `∀ i j, d i = d j` is exactly `allPairsEq` of the out-degree list. -/
theorem allPairsEq_ofFn {k : Nat} (d : Fin k → Nat) :
    allPairsEq (List.ofFn d) ↔ ∀ i j, d i = d j := by
  unfold allPairsEq
  constructor
  · intro H i j
    exact H (d i) (List.mem_ofFn.mpr ⟨i, rfl⟩) (d j) (List.mem_ofFn.mpr ⟨j, rfl⟩)
  · intro H a ha b hb
    rw [List.mem_ofFn] at ha hb
    obtain ⟨i, rfl⟩ := ha
    obtain ⟨j, rfl⟩ := hb
    exact H i j

/-! ### 3. Composition-blindness: tangent-regularity factors through the multiset (note Theorem 3)

The decidable test. `tregB l = true` iff every out-degree equals the first — equivalently all are
equal. The content of note Theorem 3 is that this value depends only on the *multiset* of
out-degrees (`Multiset = List / Perm`): it is invariant under permutation of `l`, hence blind to any
composition structure, which is not recoverable from the multiset. -/

/-- Decidable tangent-regularity test on an out-degree list: every entry equals the head. -/
def tregB : List Nat → Bool
  | [] => true
  | x :: xs => xs.all (fun y => x == y)

/-- `tregB l = true` is exactly `allPairsEq l` (all out-degrees equal). -/
theorem tregB_true_iff : ∀ l : List Nat, tregB l = true ↔ allPairsEq l
  | [] => by simp [tregB, allPairsEq]
  | x :: xs => by
      simp only [tregB, List.all_eq_true, beq_iff_eq, allPairsEq, List.mem_cons]
      constructor
      · intro H a ha b hb
        rcases ha with rfl | ha <;> rcases hb with rfl | hb
        · rfl
        · exact H b hb
        · exact (H a ha).symm
        · exact (H a ha).symm.trans (H b hb)
      · intro H y hy
        exact H x (Or.inl rfl) y (Or.inr hy)

/-- Out-degree homogeneity is permutation-invariant: it depends only on the multiset of
out-degrees, not on their order. -/
theorem allPairsEq_perm {l₁ l₂ : List Nat} (h : l₁.Perm l₂) :
    allPairsEq l₁ ↔ allPairsEq l₂ := by
  unfold allPairsEq
  constructor
  · intro H a ha b hb; exact H a (h.mem_iff.mpr ha) b (h.mem_iff.mpr hb)
  · intro H a ha b hb; exact H a (h.mem_iff.mp ha) b (h.mem_iff.mp hb)

/-- **Composition-blindness (note Theorem 3), formalised.** The tangent-regularity test descends to
the multiset of out-degrees: permuting the out-degree list leaves `tregB` unchanged. Since a
`◁`-comonoid's composition `δ : p → p ◁ p` is not recoverable from the out-degree multiset,
`tregB` is blind to it — it is a property of the underlying functor `U(p)` alone. -/
theorem tregB_perm {l₁ l₂ : List Nat} (h : l₁.Perm l₂) : tregB l₁ = tregB l₂ := by
  have key : (tregB l₁ = true) ↔ (tregB l₂ = true) :=
    (tregB_true_iff l₁).trans ((allPairsEq_perm h).trans (tregB_true_iff l₂).symm)
  cases h1 : tregB l₁ <;> cases h2 : tregB l₂ <;> simp_all

/-- Sanity: concrete out-degree lists. `[]` (empty category), `[2]` (one object, out-degree `2`:
`y²`), `[2,2,2]` (out-regular) are tangent-regular; `[2,3]` (out-degrees `2` and `3`) and `[1,2,1]`
are not. `[0,0]` (two objects, no non-identity... zero out-degree each) is regular. -/
theorem treg_examples :
    tregB [] = true ∧ tregB [2] = true ∧ tregB [2, 2, 2] = true
      ∧ tregB [2, 3] = false ∧ tregB [0, 0] = true ∧ tregB [1, 2, 1] = false := by decide

/-! ### 4. The two refuting witnesses (note Theorem 3)

A minimal model of a finite category: the out-degree list `U(p)` the tangent bundle sees, plus an
*opaque* composition-level label `isGroupoid`. `treg` reads only `outDeg`. That `isGroupoid` is a
free field is the whole point: tangent-regularity cannot depend on it. (That these labels are
realised by the genuine categories `ℤ/2`, `{1,e}`, `ℤ/2 ⊔ ℤ/3` is cited, not formalised — see the
module docstring.) -/

/-- A finite category recorded by what the tangent bundle sees (`outDeg = U(p)`) and an opaque
composition-level label (`isGroupoid`), invisible to `∂`. -/
structure FinCat where
  /-- Out-degrees `|E_a|` of the objects — the underlying polynomial functor `U(p)`. -/
  outDeg : List Nat
  /-- A composition-level property (here: "is a groupoid"); data not recoverable from `outDeg`. -/
  isGroupoid : Bool

/-- Tangent-regularity of a finite category reads only its out-degrees. -/
def treg (C : FinCat) : Bool := tregB C.outDeg

/-- The group `ℤ/2`: one object, two morphisms, out-degree `2`; a groupoid. -/
def Zmod2 : FinCat := ⟨[2], true⟩

/-- The idempotent monoid `{1, e}` with `e² = e`: one object, two morphisms, out-degree `2`;
*not* a groupoid. Same underlying functor `y²` as `Zmod2`. -/
def Idem2 : FinCat := ⟨[2], false⟩

/-- The groupoid `ℤ/2 ⊔ ℤ/3`: two objects of out-degrees `2` and `3`. -/
def ZmodSum : FinCat := ⟨[2, 3], true⟩

/-- **tangent-regular ⇏ groupoid, and blindness made concrete.** `Zmod2` and `Idem2` have the same
out-degree list `[2]` (same underlying functor `y²`), so `treg` gives them the *same* value — even
though one is a groupoid and the other is not. Tangent-regularity cannot tell them apart. -/
theorem treg_blind_to_composition :
    treg Zmod2 = treg Idem2 ∧ Zmod2.isGroupoid ≠ Idem2.isGroupoid := by decide

/-- **groupoid ⇏ tangent-regular.** `ZmodSum = ℤ/2 ⊔ ℤ/3` is a groupoid, but its out-degrees `2, 3`
are not constant, so it is not tangent-regular. (Airtight from note Lemma 1 alone.) -/
theorem groupoid_not_tangentRegular :
    ZmodSum.isGroupoid = true ∧ treg ZmodSum = false := by decide

/-- General form of blindness: any two finite categories with the same out-degree multiset (e.g.
differing only in composition) receive the same tangent-regularity verdict. -/
theorem treg_factors_through_multiset {C D : FinCat} (h : C.outDeg.Perm D.outDeg) :
    treg C = treg D := tregB_perm h

/-! ### 5. The dividing line, packaged -/

/-- **The out-degree / tangent-regularity dividing line, packaged.** The surviving positive of the
Lanfranchi-port refutation:

1. **tangent-regular ⟺ out-degree homogeneous** (note Theorem 2): `TangentRegular d ↔ ∀ i j, d i = d j`;
2. this is literally a property of the out-degree *list*: `allPairsEq (List.ofFn d) ↔ ∀ i j, d i = d j`;
3. **composition-blind** (note Theorem 3): the test `tregB` is permutation-invariant, so it factors
   through the multiset of out-degrees and cannot see the comonoid composition;
4. **refuting witnesses**: tangent-regular `⇏` groupoid (`ℤ/2` vs `{1,e}`, same `[2]`) and
   groupoid `⇏` tangent-regular (`ℤ/2 ⊔ ℤ/3`, `[2,3]`). -/
theorem tangent_regular_outdegree :
    (∀ (k : Nat) (d : Fin k → Nat), TangentRegular d ↔ ∀ i j, d i = d j)
      ∧ (∀ (k : Nat) (d : Fin k → Nat), allPairsEq (List.ofFn d) ↔ ∀ i j, d i = d j)
      ∧ (∀ (l₁ l₂ : List Nat), l₁.Perm l₂ → tregB l₁ = tregB l₂)
      ∧ (treg Zmod2 = treg Idem2 ∧ Zmod2.isGroupoid ≠ Idem2.isGroupoid)
      ∧ (ZmodSum.isGroupoid = true ∧ treg ZmodSum = false) :=
  ⟨fun _k d => tangentRegular_iff d, fun _k d => allPairsEq_ofFn d,
    fun _ _ h => tregB_perm h, treg_blind_to_composition, groupoid_not_tangentRegular⟩

-- Axiom audit: expected `propext` only (core `Nat`/`Fin`/`List` + `decide`) — free of
-- `sorryAx`, `Quot.sound`, and `Classical.choice`.
#print axioms tangent_regular_outdegree

end TangentRegularOutDegree
