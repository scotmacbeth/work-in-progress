import Containers.Comonoid
import Containers.Dirichlet
import Containers.Monoidal
import Containers.StateComonad

/-!
# The Workers `⊗`-grading is a retract of the BHM `◁`-grading

This file formalises the surviving half of MacBeth's prove note
`2026-08-29-workers-retract-of-bhm-grading.md` (registry node
`workers-retract-of-bhm-grading`). The *parent* conjecture there — that the
Workers grading is a **fibre** of the Behr–Heunen–McDermott `◁`-grading — was
refuted; what survived is a **retract**.

Write `ΔS` for the store container `deltaS S` (`Containers.StateComonad`), and put

* `A := ΔS ⊗ ΔT` — the Dirichlet tensor, which is `Δ(S × T)` on the nose
  (`deltaS_tensor`); this is the Workers `(Set, ×)`-grading, and
* `B := ΔS ◁ ΔT` — the composition product, i.e. the BHM grading.

They are genuinely different: at `|S| = |T| = 2`, `A` has `4` shapes and `B` has
`|S| · |T|^{|S|} = 8`. The content of this file is that `A` is nevertheless a
**non-trivial retract** of `B`, and that the store comultiplication is a *lift of
the `⊗`-diagonal* along the retraction.

## What is actually being checked

A `ContainerMorphism p q` is a forward map on shapes together with a map
`q[φ s] → p[s]` running **backward** on positions, and `comp` composes the
backward maps in the **reverse** order (`Containers.Cont`). The informal proof
asserts that both backward maps here "are the identity, because all fibres
involved are literally `S × T`". That is the one step a shape-only argument would
fumble, and it is why this is worth machine-checking rather than trusting.

Machine-checking it turns up a (harmless) correction to that phrasing. In this
development the two fibres are

* `A.Pos (s, t) = S × T`, a `Prod`, but
* `B.Pos ⟨s, g⟩ = (q : S) × (ΔT).Pos (g q) = (q : S) × T`, a `Sigma`,

and `Sigma (fun _ : S => T)` is *isomorphic but not definitionally equal* to
`Prod S T`. So the backward maps are the canonical `Sigma ↔ Prod` swaps rather
than literal identities. They are mutually inverse by structure η, so the
retract theorem is unaffected — but the fibres are not "literally" the same
type, and the composite really does have to be checked.

## Results

* `storeSection` / `storeRetraction` (**L1**) — `σ : A ⟶ B` (branch on the
  constant map at `t`) and `r : B ⟶ A` (**self-evaluation** `(s, g) ↦ (s, g s)`),
  as genuine container morphisms. That these elaborate at all is the variance
  claim.
* `storeRetraction_storeSection` (**L2**) — `r ∘ σ = id_A`, by `rfl`.
* `storeSection_storeRetraction_ne` (**L3**) — `σ ∘ r ≠ id_B`, as a concrete
  `Bool` witness (the non-constant branch map `id : Bool → Bool` is collapsed).
* `storeRetraction_coComult` (**L4**) — the **collapse identity** `r ∘ δ = Δ(d)`,
  by `rfl`: the store comultiplication `δ` is a lift of the `⊗`-diagonal along
  `r`. Read backwards, this is the precise sense in which **`⊗` is the diagonal
  of `◁`**.
* `storeDiagSection_ne_coComult`, `storeDiagSection_coassoc`,
  `storeDiagSection_not_right_counital` (**L5**) — the impossibility:
  `δ' := σ ∘ Δ(d)` is coassociative but **not counital**, hence not a `◁`-comonoid
  (`Container.Comonoid`). This is what forces `Δ : (Set, ×) → (Cont, ◁)` to be
  lax/oplax only on the **core groupoid** `(Set_≅, ×)`.

This file is the composition-product companion of
`Containers.StateComonadTensor`, whose `deltaDC_prod : ΔS ⊗ ΔT = Δ(S × T)` sits on
the tensor side of the same story; it is written in that file's idiom.

Everything is `Type`-level, Lean 4 core, no Mathlib. Every result is `rfl` or a
`Bool` case analysis, so nothing here depends on any axiom.
-/

namespace Containers

open Container

variable (S T : Type)

/-! ## L1: the section and the retraction

`A = ΔS ⊗ ΔT` has shapes `S × T` and every fibre `S × T`. `B = ΔS ◁ ΔT` has shapes
`(s : S) × (S → T)` — an outer state together with a *branch map* choosing an
inner `ΔT`-state at each position — and fibre `(q : S) × T` over `⟨s, g⟩`. -/

/-- **The section `σ : ΔS ⊗ ΔT ⟶ ΔS ◁ ΔT`.** On shapes, `(s, t) ↦ (s, const t)`:
the tensor's single `T`-state is spread over the composition product as the
*constant* branch map. On positions it is the `Sigma → Prod` swap. -/
def storeSection : ContainerMorphism (deltaS S ⊗ deltaS T) (deltaS S ◁ deltaS T) where
  onShapes := fun st => ⟨st.1, fun _ => st.2⟩
  onPos := fun _ p => (p.1, p.2)

/-- **The retraction `r : ΔS ◁ ΔT ⟶ ΔS ⊗ ΔT`.** On shapes, `(s, g) ↦ (s, g s)` —
**self-evaluation**: the branch map is collapsed by feeding it the outer state. On
positions it is the `Prod → Sigma` swap. -/
def storeRetraction : ContainerMorphism (deltaS S ◁ deltaS T) (deltaS S ⊗ deltaS T) where
  onShapes := fun sg => (sg.1, sg.2 sg.1)
  onPos := fun _ p => ⟨p.1, p.2⟩

/-! ## L2 and L3: `A` is a non-trivial retract of `B` -/

/-- **L2 (the retract).** `r ∘ σ = id_A`. On shapes, `(s, t) ↦ (s, const t) ↦
(s, const t s) = (s, t)`; on positions the two swaps compose to the identity.
Both halves hold by `rfl` (`Prod`/`Sigma` structure η). Note the reversal: in the
`comp`-order of `Containers.Cont`, "`r` after `σ`" is `σ.comp r`. -/
theorem storeRetraction_storeSection :
    (storeSection S T).comp (storeRetraction S T)
      = ContainerMorphism.id (deltaS S ⊗ deltaS T) := rfl

/-- **L3 (non-triviality).** `σ ∘ r ≠ id_B`. The idempotent `e := σ ∘ r` collapses
each branch map `g` to the constant at its self-evaluation `g s`, so it fixes only
the constant branch maps. Witnessed at `S = T = Bool` by the shape `⟨true, id⟩`:
`e` sends it to `⟨true, const true⟩`, and the two branch maps disagree at `false`.
Together with `storeRetraction_storeSection` this makes `ΔS ⊗ ΔT` a *proper*
retract of `ΔS ◁ ΔT` — the two gradings are not the same. -/
theorem storeSection_storeRetraction_ne :
    (storeRetraction Bool Bool).comp (storeSection Bool Bool)
      ≠ ContainerMorphism.id (deltaS Bool ◁ deltaS Bool) := by
  intro h
  exact Bool.noConfusion
    (congrArg (fun z : (deltaS Bool ◁ deltaS Bool).Shape => z.2 false)
      (congrFun (congrArg ContainerMorphism.onShapes h)
        (⟨true, id⟩ : (deltaS Bool ◁ deltaS Bool).Shape)))

/-! ## L4: the collapse identity — `⊗` is the diagonal of `◁` -/

/-- **The `⊗`-diagonal `Δ(d) : ΔS ⟶ ΔS ⊗ ΔS`**, the store image of the set
diagonal `d : S → S × S`: shapes `s ↦ (s, s)`, backward map the second projection.
(`Δ` is not a functor on all of `Set` — the backward map has to be supplied by
hand, and only does so for maps like `d` that admit one. That failure is exactly
what `storeDiagSection_not_right_counital` below turns into an obstruction.) -/
def storeDiag : ContainerMorphism (deltaS S) (deltaS S ⊗ deltaS S) where
  onShapes := fun s => (s, s)
  onPos := fun _ p => p.2

/-- **L4 (the collapse identity).** `r ∘ δ = Δ(d)`, where `δ = (deltaDC S).coComult`
is the store comultiplication `ΔS ⟶ ΔS ◁ ΔS` (`Containers.Comonoid`) and `d` the
diagonal. On shapes: `s ↦ ⟨s, id⟩ ↦ (s, id s) = (s, s)`; on positions, `δ`'s
backward map is already the second projection and `r`'s is the swap, so the
composite is `π₂`. Holds by `rfl`.

Read backwards this says the store comultiplication is a **lift of the
`⊗`-diagonal along the retraction** — the precise form of "`⊗` is the diagonal
collapse of `◁`". It is the companion, on the composition-product side, of
`deltaDC_prod` in `Containers.StateComonadTensor`. -/
theorem storeRetraction_coComult :
    ((deltaDC S).coComult).comp (storeRetraction S S) = storeDiag S := rfl

/-! ## L5: the impossibility — `σ ∘ Δ(d)` is not a comonad

`δ' := σ ∘ Δ(d)` is the image of the set diagonal under the comparison `σ`. If `Δ`
were oplax monoidal into `(Cont, ◁)` with comparison `σ`, then `ΔS` would carry
`δ'` as a comultiplication. It does not: `δ'` is coassociative but fails the right
counit law. -/

/-- `δ' := σ ∘ Δ(d) : ΔS ⟶ ΔS ◁ ΔS`. On shapes `s ↦ ⟨s, const s⟩`; on positions
`⟨i, j⟩ ↦ j`. By L4 it is also `e ∘ δ` for the idempotent `e = σ ∘ r`, i.e. `δ`
with its branch component collapsed. -/
def storeDiagSection : ContainerMorphism (deltaS S) (deltaS S ◁ deltaS S) :=
  (storeDiag S).comp (storeSection S S)

/-- **L5(1).** `δ' ≠ δ` for `|S| ≥ 2`: the store comultiplication has branch
component `id_S`, the comparison-image has `const_s`. Witnessed at `S = Bool` and
shape `true`, where the branch maps disagree at `false`. -/
theorem storeDiagSection_ne_coComult :
    storeDiagSection Bool ≠ (deltaDC Bool).coComult := by
  intro h
  exact Bool.noConfusion
    (congrArg (fun z : (deltaS Bool ◁ deltaS Bool).Shape => z.2 false)
      (congrFun (congrArg ContainerMorphism.onShapes h) true))

/-- **L5(2), positive half.** `δ'` *is* coassociative — it satisfies the
`coassoc` field of `Container.Comonoid` verbatim. Holds by `rfl`: both composites
send `s` to the fully constant nested shape and both backward maps read off the
innermost position. So coassociativity is not where the obstruction lives. -/
theorem storeDiagSection_coassoc :
    ((storeDiagSection S).comp
        (Container.seq₂ (storeDiagSection S) (ContainerMorphism.id (deltaS S)))).comp
        (Container.associator (deltaS S) (deltaS S) (deltaS S)).hom
      = (storeDiagSection S).comp
          (Container.seq₂ (ContainerMorphism.id (deltaS S)) (storeDiagSection S)) := rfl

/-- **L5(2), the obstruction.** `δ'` fails the **right counit law** of
`Container.Comonoid` against the store counit `ε = (deltaDC S).coCounit`, so
`(ΔS, ε, δ')` is not a `◁`-comonoid — equivalently, not a comonad.

The mechanism: the law's backward map should be `⟨q, ()⟩ ↦ q`, but `δ'`'s backward
map discards the outer position and `ε`'s inserts the root, so the composite is the
constant `⟨q, ()⟩ ↦ s`. Witnessed at `S = Bool`, shape `true`, position `⟨false, ()⟩`:
the law demands `false` and delivers `true`.

Hence `Δ : (Set, ×) → (Cont, ◁)` cannot be oplax with comparison `σ`: the set
diagonal is a comonoid in `(Set, ×)`, but its `σ`-image is not one in `(Cont, ◁)`.
This is what confines `(Δ, σ)`/`(Δ, r)` to the **core groupoid** `(Set_≅, ×)`,
where there is no diagonal to obstruct. -/
theorem storeDiagSection_not_right_counital :
    (storeDiagSection Bool).comp
        (Container.seq₂ (ContainerMorphism.id (deltaS Bool)) (deltaDC Bool).coCounit)
      ≠ (Container.rightUnitor (deltaS Bool)).inv := by
  intro h
  exact Bool.noConfusion
    (congrArg (fun z : Ext (deltaS Bool ◁ Container.I) Bool => z.2 ⟨false, ()⟩)
      (congrFun (congrArg (fun φ => ContainerMorphism.toNat φ Bool) h)
        (⟨true, id⟩ : Ext (deltaS Bool) Bool)))

end Containers
