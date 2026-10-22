/-
Copyright (c) 2026 MacBeth (Kodamai). Released under Apache 2.0.
Author: MacBeth
-/

/-!
# Day convolution `c ⊗ d = (C × D)♯` internal to `E = Graph` — finite machine check

This file machine-checks the **one-topos-up** (Path-6) witness of the transport theorem
`day-convolution-cxd-presheaf-topos` (proof `proofs/2026-10-21-day-convolution-cxd-presheaf-topos.md`,
registry node `day-convolution-cxd-presheaf-topos` [proved]). The Set-side base case
(`day-convolution-poly-comonoids-cxd`) is machine-checked in spirit by the Python verifier
`scratch/day_conv_verify.py` (16/16); this file lifts the witness one base up, to the presheaf topos
`E = Graph = [•⇉•, Set]`, exactly as the trigger `~/state/LEAN.md` requests — the first Lean oracle
that is *internal to a topos other than Set*.

## The internal-category dictionary in `Graph`

By `Cat(Graph) ≃ [•⇉•, Cat]` (internal categories in a presheaf topos are the pointwise diagram of
categories), an **internal category `C` in `Graph`** is a functor `•⇉• → Cat`: two ordinary (Set-)
categories `𝐂_V` (vertices) and `𝐂_E` (edges) together with two functors `S, T : 𝐂_E → 𝐂_V` (the
internalised source/target). Its object-of-objects `C₀` is the graph with vertex set `Ob 𝐂_V`, edge
set `Ob 𝐂_E` and source/target `S₀, T₀`; its object-of-morphisms `C₁` is the graph with vertex set
`Mor 𝐂_V`, edge set `Mor 𝐂_E`, source/target `S₁, T₁`. The internal structure maps `dom, cod, id,
comp` of `C` are **graph morphisms** `C₁ → C₀` (etc.) — and "they commute with the graph source/
target `s, t`" is **exactly** the statement that `S` and `T` are functors (preserve `dom`, `cod`,
`id`, `comp`). That is the headline check here (`funcValid`); the comonoid laws of the represented
polynomial comonoid are the category axioms of each fibre (`catValid`).

## What is certified (claim of `~/state/LEAN.md`)

For internal categories `C, D` in `Graph`, the Day/Dirichlet tensor `c ⊗ d` of their `◁`-comonoids
represents the internal product category `C × D` **on the nose**, with counit `ε_c ⊗ ε_d` = the
internal identity-section and comultiplication `ι ∘ (δ_c ⊗ δ_d)` = internal composition, and these
are genuine `Graph`-morphisms. In the `[•⇉•, Cat]` dictionary the Day tensor is computed fibrewise
and glued by `S, T`; because the Set-side trace already gives the componentwise product structure on
each fibre (Set theorem, `day_conv_verify.py`), the **new Graph-level content** is:

* **(headline, internal-to-`Graph`)** the glued source/target `S × S`, `T × T` of `c ⊗ d` are still
  functors — i.e. the identity-section (counit) and composition (comult) of `c ⊗ d` *commute with
  `s, t`*. `funcValid` certifies this for all nine ordered pairs over three internal categories.
* **(comonoid laws, componentwise)** each fibre of `c ⊗ d` is a genuine category (`catValid`), so the
  represented comonoid satisfies the counit/coassociativity laws.
* **(no well-pointedness — the acid test)** the witness `Carr` has a **loopless** object-graph `C₀`
  (`S₀ ≠ T₀`), so `C₀` has no global element `1 → C₀`; the induced `S, T` on `c ⊗ d = Carr ⊗ Carr`
  are nonetheless functors (`prod_st_functors_Carr_Carr`) and the product stays loopless
  (`prod_loopless_Carr_Carr`). The identity-section/composition need no global elements.

## References

* Transport theorem: `proofs/2026-10-21-day-convolution-cxd-presheaf-topos.md`.
* `Comon(Poly(E)) ≃ Cat(E)` internal to any finite-limit `E`: Shapiro–Spivak, *Structures on
  Categories of Polynomials*, arXiv:2305.00167, Thm 5.6 + Cor 5.12 (exponentiable-source hypothesis
  vacuous over any topos).
* Dirichlet `⊗` = Day convolution on `Poly(E)` induced by `(1,×)`: Niu–Spivak, arXiv:2312.00990,
  Prop. 3.79. `Poly(E)` over any LCCC: Gambino–Kock, arXiv:0906.4931.
* Set-side base case + forward dictionary: Spivak–Garner–Fairbanks, *Functorial Aggregation*,
  arXiv:2111.10968, Prop. 5.2 (orig. Ahman–Uustalu).

## Model (Mathlib-free, Lean 4 core only)

No Mathlib in the container (memory `lean-Q0-evenness-polarization-general-abgrp`). A finite Set-
category is a `FCat` with `Nat` carriers and total `dom/cod/id/comp` functions (lookup tables);
checks quantify over `List.range` and reduce to `Bool` discharged by `decide`. Pairs `(f,g)` are
encoded `f * (modulus) + g`; the product and the "Day convolution" share this componentwise formula
(as in `day_conv_verify.py`), so the substantive content is the category laws (`catValid`) and the
source/target functoriality (`funcValid`), not a tautological equality of two definitions. Every
certificate reports `propext` only (from `decide`'s `Decidable → Bool` reduction) — no `sorryAx`, no
`native_decide`.
-/

namespace GraphDayConv

set_option maxHeartbeats 4000000
set_option maxRecDepth 100000

/-! ### Finite Set-categories -/

/-- A finite category: objects `0 .. no-1`, morphisms `0 .. nm-1`, with total structure functions.
`cmp f g` is "`f` then `g`" `= g ∘ f` (meaningful when `cod f = dom g`; arbitrary otherwise). -/
structure FCat where
  no : Nat
  nm : Nat
  dom : Nat → Nat
  cod : Nat → Nat
  idm : Nat → Nat
  cmp : Nat → Nat → Nat

/-- Category axioms as a `Bool`: identity typing, left/right unit, composite typing and
associativity (quantified over composable tuples via a guard). These are the comonoid laws of the
represented `◁`-comonoid. -/
def catValid (C : FCat) : Bool :=
  (List.range C.no).all (fun i => (C.dom (C.idm i) == i) && (C.cod (C.idm i) == i)) &&
  (List.range C.nm).all (fun f =>
    (C.cmp f (C.idm (C.cod f)) == f) && (C.cmp (C.idm (C.dom f)) f == f)) &&
  (List.range C.nm).all (fun f => (List.range C.nm).all (fun g =>
    (!(C.cod f == C.dom g)) ||
      ((C.dom (C.cmp f g) == C.dom f) && (C.cod (C.cmp f g) == C.cod g)))) &&
  (List.range C.nm).all (fun f => (List.range C.nm).all (fun g => (List.range C.nm).all (fun h =>
    (!((C.cod f == C.dom g) && (C.cod g == C.dom h))) ||
      (C.cmp (C.cmp f g) h == C.cmp f (C.cmp g h)))))

/-- Product of two finite categories, computed componentwise. Objects `(i,x)` encoded `i*D.no + x`,
morphisms `(f,g)` encoded `f*D.nm + g`. This is both the categorical product `C × D` **and** the
underlying category of the Day/Dirichlet tensor `c ⊗ d` (the Set-side trace gives this componentwise
structure on the nose: `cod = cod×cod`, `comp` componentwise, `id = id×id`). -/
def prodCat (C D : FCat) : FCat where
  no := C.no * D.no
  nm := C.nm * D.nm
  dom := fun p => C.dom (p / D.nm) * D.no + D.dom (p % D.nm)
  cod := fun p => C.cod (p / D.nm) * D.no + D.cod (p % D.nm)
  idm := fun o => C.idm (o / D.no) * D.nm + D.idm (o % D.no)
  cmp := fun p q => C.cmp (p / D.nm) (q / D.nm) * D.nm + D.cmp (p % D.nm) (q % D.nm)

/-! ### Functors and the internal source/target -/

/-- A functor between finite categories: an object map and a morphism map. -/
structure Func where
  fo : Nat → Nat
  fm : Nat → Nat

/-- `F : S → T` is a functor as a `Bool`: commutes with `dom, cod` (the graph source/target squares),
preserves identities (the counit / identity-section), and preserves composition (the comult). For an
internal category in `Graph` this whole predicate is "the internal source/target map `S` (or `T`) is
a graph morphism — it commutes with `s, t`". -/
def funcValid (S T : FCat) (F : Func) : Bool :=
  (List.range S.nm).all (fun f =>
    (F.fo (S.dom f) == T.dom (F.fm f)) && (F.fo (S.cod f) == T.cod (F.fm f))) &&
  (List.range S.no).all (fun i => F.fm (S.idm i) == T.idm (F.fo i)) &&
  (List.range S.nm).all (fun f => (List.range S.nm).all (fun g =>
    (!(S.cod f == S.dom g)) || (F.fm (S.cmp f g) == T.cmp (F.fm f) (F.fm g))))

/-- The product functor `F × G : (C_src × D_src) → (C_tgt × D_tgt)`, computed componentwise. The
moduli `dEno, dVno` (objects) and `dEnm, dVnm` (morphisms) are those of the second factor's source
and target categories. -/
def prodFunc (F G : Func) (dEno dVno dEnm dVnm : Nat) : Func where
  fo := fun o => F.fo (o / dEno) * dVno + G.fo (o % dEno)
  fm := fun m => F.fm (m / dEnm) * dVnm + G.fm (m % dEnm)

/-- An internal category in `Graph = [•⇉•, Set]`, i.e. a functor `•⇉• → Cat`: vertex category `cV`,
edge category `cE`, and source/target functors `So, To : cE → cV`. -/
structure IGraph where
  cV : FCat
  cE : FCat
  So : Func
  To : Func

/-- `G` is a genuine internal category in `Graph`: both fibres are categories and both `So, To` are
functors (the structure maps commute with `s, t`). -/
def igValid (G : IGraph) : Bool :=
  catValid G.cV && catValid G.cE && funcValid G.cE G.cV G.So && funcValid G.cE G.cV G.To

/-- The object-of-objects graph `C₀` is **loopless** (`S₀ ≠ T₀` on every edge-object), hence has no
global element `1 → C₀`. This is the well-pointedness acid test. -/
def looplessIG (G : IGraph) : Bool :=
  (List.range G.cE.no).all (fun e => G.So.fo e != G.To.fo e)

/-- The Day/Dirichlet tensor `c ⊗ d` as an internal category in `Graph`, computed fibrewise (product
of categories, = the Set-side trace on the nose) and glued by the product source/target `So × So`,
`To × To`. This is `(C × D)♯`. -/
def prodIG (C D : IGraph) : IGraph where
  cV := prodCat C.cV D.cV
  cE := prodCat C.cE D.cE
  So := prodFunc C.So D.So D.cE.no D.cV.no D.cE.nm D.cV.nm
  To := prodFunc C.To D.To D.cE.no D.cV.no D.cE.nm D.cV.nm

/-! ### Concrete finite categories -/

/-- Terminal category `[0]`: one object, one (identity) morphism. -/
def term : FCat where
  no := 1
  nm := 1
  dom := fun _ => 0
  cod := fun _ => 0
  idm := fun _ => 0
  cmp := fun _ _ => 0

/-- Walking arrow `[1]`: objects `{0,1}`, morphisms `0 = id₀`, `1 = a : 0 → 1`, `2 = id₁`. -/
def warr : FCat where
  no := 2
  nm := 3
  dom := fun f => [0, 0, 1].getD f 0
  cod := fun f => [0, 1, 1].getD f 0
  idm := fun i => [0, 2].getD i 0
  cmp := fun f g => [0, 1, 0, 0, 0, 1, 0, 0, 2].getD (f * 3 + g) 0

/-- Two-object discrete category: objects `{0,1}`, morphisms `0 = id₀`, `1 = id₁`. -/
def disc2 : FCat where
  no := 2
  nm := 2
  dom := fun f => [0, 1].getD f 0
  cod := fun f => [0, 1].getD f 0
  idm := fun i => [0, 1].getD i 0
  cmp := fun f g => [0, 0, 0, 1].getD (f * 2 + g) 0

/-! ### Concrete internal categories in `Graph`

Each has edge category `term`, so each `C₀` is a one-edge graph `S₀(0) → T₀(0)`. `Carr` and `Cdisc`
are **loopless** (`S₀ ≠ T₀`); `Cpt` is the loop (single vertex, single loop edge — the one case
*with* a global element, our negative control). -/

/-- `Cpt`: the point. `cV = cE = term`, `So = To = id`; object-graph `C₀` is a single loop (has a
global element). -/
def Cpt : IGraph where
  cV := term
  cE := term
  So := { fo := fun _ => 0, fm := fun _ => 0 }
  To := { fo := fun _ => 0, fm := fun _ => 0 }

/-- `Carr`: `cV = [1]` (walking arrow), `cE = term`; `S₀(0) = 0`, `T₀(0) = 1` so `C₀ = (0 → 1)` is
loopless. On the single edge-morphism, `S = id₀`, `T = id₁`. -/
def Carr : IGraph where
  cV := warr
  cE := term
  So := { fo := fun _ => 0, fm := fun _ => 0 }
  To := { fo := fun _ => 1, fm := fun _ => 2 }

/-- `Cdisc`: `cV = disc2`, `cE = term`; `S₀(0) = 0`, `T₀(0) = 1` (loopless); `S = id₀`, `T = id₁`. -/
def Cdisc : IGraph where
  cV := disc2
  cE := term
  So := { fo := fun _ => 0, fm := fun _ => 0 }
  To := { fo := fun _ => 1, fm := fun _ => 1 }

/-- The three internal categories tested pairwise. -/
def igs : List IGraph := [Cpt, Carr, Cdisc]

/-! ### Each witness is a genuine internal category in `Graph` -/

theorem Cpt_valid : igValid Cpt = true := by decide
theorem Carr_valid : igValid Carr = true := by decide
theorem Cdisc_valid : igValid Cdisc = true := by decide

/-! ### Loopless / no-global-element acid test -/

theorem Carr_loopless : looplessIG Carr = true := by decide
theorem Cdisc_loopless : looplessIG Cdisc = true := by decide

/-- Negative control: `Cpt`'s object-graph is a loop, so it is *not* loopless (it has a global
element). The loopless check is not vacuously true. -/
theorem Cpt_not_loopless : looplessIG Cpt = false := by decide

/-! ### Headline — `c ⊗ d` is a genuine internal category in `Graph` for all nine pairs

`igValid (prodIG C D)` bundles: both fibres of `c ⊗ d` are categories (comonoid laws, componentwise)
**and** the glued source/target `So × So`, `To × To` are functors (the identity-section and
composition of `c ⊗ d` commute with the graph `s, t` — the internal-to-`Graph` content). -/
def allProdValid : Bool := igs.all (fun C => igs.all (fun D => igValid (prodIG C D)))

theorem all_prod_valid : allProdValid = true := by decide

/-! ### Zoom on the acid-test pair `Carr ⊗ Carr` (loopless, no global elements) -/

/-- The source/target of `c ⊗ d = Carr ⊗ Carr` are functors — the identity-section (counit) and
composition (comult) are genuine `Graph`-morphisms — **without any global element of `C₀`**. -/
theorem prod_st_functors_Carr_Carr :
    funcValid (prodIG Carr Carr).cE (prodIG Carr Carr).cV (prodIG Carr Carr).So = true
      ∧ funcValid (prodIG Carr Carr).cE (prodIG Carr Carr).cV (prodIG Carr Carr).To = true := by
  decide

/-- Looplessness (no global element) is preserved by `⊗`: `Carr ⊗ Carr` is still loopless. -/
theorem prod_loopless_Carr_Carr : looplessIG (prodIG Carr Carr) = true := by decide

/-- …and across a mixed pair. -/
theorem prod_loopless_Cdisc_Carr : looplessIG (prodIG Cdisc Carr) = true := by decide

/-- Cardinality on the nose: `(C × D)₀ = |C|₀·|D|₀`, `(C × D)₁ = |C|₁·|D|₁` in each fibre. For
`Carr ⊗ Carr`: vertex category `[1]×[1]` has `4` objects, `9` morphisms; edge category `term×term`
has `1` object, `1` morphism. -/
theorem prod_card_Carr_Carr :
    (prodIG Carr Carr).cV.no = 4 ∧ (prodIG Carr Carr).cV.nm = 9
      ∧ (prodIG Carr Carr).cE.no = 1 ∧ (prodIG Carr Carr).cE.nm = 1 := by
  decide

/-! ### Non-vacuity controls -/

/-- `funcValid` genuinely rejects a non-functor: on `Carr` (`cE = term → cV = warr`) the map sending
the single edge-morphism to `a : 0 → 1` breaks the `cod` square (and identity preservation). -/
def bogus : Func := { fo := fun _ => 0, fm := fun _ => 1 }

theorem bogus_not_functor : funcValid Carr.cE Carr.cV bogus = false := by decide

/-- `catValid` genuinely rejects a non-category: `term` with composition redefined to an out-of-range
constant fails the unit law. -/
def notcat : FCat where
  no := 1
  nm := 1
  dom := fun _ => 0
  cod := fun _ => 0
  idm := fun _ => 0
  cmp := fun _ _ => 5

theorem notcat_invalid : catValid notcat = false := by decide

end GraphDayConv
