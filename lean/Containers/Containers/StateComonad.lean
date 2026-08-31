import Containers.Directed
import Containers.Dirichlet

/-!
# The state object `ΔS`, the codiscrete category, and the store comonad

This file formalises the foundational object of the *category of Workers*
(MacBeth, prove note `2026-07-28-delta-state-object-and-workers.md`, Theorems
T1–T3): the **state container** `ΔS = (S, s ↦ S)`, whose shape set is `S` and
whose *every* position fibre is `S` again.

The content is the machine-checked backbone of that note's Theorem **T1**:

* `deltaS S` is a container whose extension is `⟦ΔS⟧ X = Σ s : S, X^S = S × X^S`.
* `deltaDC S` equips it with the **codiscrete-category** directed-container
  structure
  `root s = s`,  `sub s p = p`,  `shift s p q = q`  (the second projection),
  and all five directed-container laws **D1–D5 hold by `rfl`** — the codiscrete
  category is the simplest nontrivial small category, with a unique morphism for
  each ordered pair of objects (its position bundle `Σ_{s'} 𝒞(s,s') = Σ_{s'} 1`
  is exactly `S`).
* Consequently `Ext (deltaS S)` carries a comonad — the **store (costate)
  comonad** `Store_S X = S × X^S` (Uustalu–Vene, *Comonadic notions of
  computation*, 2008) — whose counit and comultiplication reduce to
  `ε ⟨s, v⟩ = v s`  and  `δ ⟨s, v⟩ = ⟨s, fun p => ⟨p, v⟩⟩`.
  The three comonad laws are inherited (for free) from `Containers.Directed`.

We also record Theorem **T3**'s multiplication lemma at the level of containers:
`ΔS ⊗ ΔT = Δ(S × T)` and `Δ1 = y`, both strict equalities (`rfl`). This is the
reason Neil's context tensor is the **Dirichlet** `⊗` (positions *multiply*) and
why, under composition, the state multiplies.

Everything is `Type`-level, Lean 4 core, no Mathlib.

The DCont ≅ Cat identification underlying "codiscrete category" is the
Ahman–Chapman–Uustalu correspondence (arXiv:1408.5809), machine-checked
elsewhere in this library (`Containers.DContCat`); the store comonad itself is
folklore (Uustalu–Vene 2008). What is formalised here is the *identification*:
that `ΔS` with the codiscrete structure induces exactly that comonad.
-/

namespace Containers

/-- The **state object** `ΔS := (S, s ↦ S)`: shape set `S`, and every position
fibre equal to `S`. Its extension is `⟦ΔS⟧ X = Σ s : S, X^S = S × X^S`. -/
def deltaS (S : Type) : Container where
  Shape := S
  Pos := fun _ => S

/-- `ΔS` as a **directed container**: the *codiscrete category* on `S`.

Under DCont ≅ Cat, `root s = s` is the identity arrow at `s`, a position
`p ∈ P s = S` names its target object so `sub s p = p` is the codomain map, and
`shift s p q = q` is the (unique) composite `s → p → q`, whose target is `q`. All
five laws D1–D5 hold definitionally (`rfl`) — codiscreteness is the simplest
nontrivial category. -/
def deltaDC (S : Type) : DirectedContainer where
  toContainer := deltaS S
  root := fun s => s
  sub := fun _ p => p
  shift := fun _ _ q => q
  d1 := fun _ => rfl
  d4 := fun _ _ _ => rfl
  d2 := fun _ _ => rfl
  d3 := fun _ _ => rfl
  d5 := fun _ _ _ _ => rfl

section StoreComonad

variable {S X : Type}

/-- The store **counit** reduces to evaluation at the current state:
`ε ⟨s, v⟩ = v s`. -/
theorem deltaDC_counit (s : S) (v : (deltaS S).Pos s → X) :
    (deltaDC S).counit (X := X) ⟨s, v⟩ = v s := rfl

/-- The store **comultiplication** reduces to
`δ ⟨s, v⟩ = ⟨s, fun p => ⟨p, v⟩⟩`: it keeps the current state `s`, and at each
position `p` produces the inner store re-focused at `p` carrying the same
labelling `v`. -/
theorem deltaDC_comult (s : S) (v : (deltaS S).Pos s → X) :
    (deltaDC S).comult (X := X) ⟨s, v⟩ = ⟨s, fun p => ⟨p, v⟩⟩ := rfl

/-- **Left counit law** for the store comonad, inherited from D1/D2. -/
theorem deltaDC_left_counit :
    (deltaDC S).counit ∘ (deltaDC S).comult
      = (id : Ext (deltaS S) X → Ext (deltaS S) X) :=
  (deltaDC S).left_counit

/-- **Right counit law** for the store comonad, inherited from D3. -/
theorem deltaDC_right_counit :
    Ext.map (deltaDC S).counit ∘ (deltaDC S).comult
      = (id : Ext (deltaS S) X → Ext (deltaS S) X) :=
  (deltaDC S).right_counit

/-- **Coassociativity** for the store comonad, inherited from D4/D5. -/
theorem deltaDC_coassoc :
    Ext.map (deltaDC S).comult ∘ (deltaDC S).comult
      = ((deltaDC S).comult ∘ (deltaDC S).comult :
          Ext (deltaS S) X →
            Ext (deltaS S) (Ext (deltaS S) (Ext (deltaS S) X))) :=
  (deltaDC S).coassoc

end StoreComonad

/-! ## Theorem T3, multiplication lemma: the state multiplies under `⊗`

The Dirichlet tensor multiplies position fibres, so tensoring two state objects
gives the state object on the product — this is exactly why the context tensor is
`⊗` and why the state multiplies under Worker composition. -/

/-- **Lemma 3.1 (state multiplies).** `ΔS ⊗ ΔT = Δ(S × T)`, a strict equality of
containers: shape sets and every position fibre coincide. -/
theorem deltaS_tensor (S T : Type) :
    deltaS S ⊗ deltaS T = deltaS (S × T) := rfl

/-- **Lemma 3.1 (unit).** `Δ1 = y`: the state object on the terminal set is the
Dirichlet/`◁` unit. -/
theorem deltaS_unit : deltaS Unit = Container.y := rfl

end Containers
