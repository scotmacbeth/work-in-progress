import Containers.Sequential

/-!
# Right distributivity of the sequential operator over the product

This file proves the **`;×` = D cell** of Jules Hedges' interaction table for the
four monoidal structures on `Cont` (see
`projects/proofs/2026-07-16-hedges-distributive-table.md`): the sequential
operator `◁` distributes over the categorical product `×` **on the left factor**,

  `(P × P') ◁ Q  ≅  (P ◁ Q) × (P' ◁ Q)`   in `Cont`.

Here `×` is `Container.prod` (`Containers.Cont`, positions `P s ⊕ P' s'`) and `◁`
is `Container.seq` (`Containers.Sequential`, the composition/sequential operator).

## The bijection

Unfolding the two sides:

* `(P × P') ◁ Q` has shapes `⟨(s, s'), f⟩` with
  `f : (P.Pos s ⊕ P'.Pos s') → Q.Shape`, and positions
  `(i : P.Pos s ⊕ P'.Pos s') × Q.Pos (f i)`.
* `(P ◁ Q) × (P' ◁ Q)` has shapes `⟨⟨s, g⟩, ⟨s', g'⟩⟩` and positions
  `((a : P.Pos s) × Q.Pos (g a)) ⊕ ((b : P'.Pos s') × Q.Pos (g' b))`.

On **shapes** the bijection curries a sum-domain function:
`f ↦ (f ∘ inl, f ∘ inr)`, inverted by `(g, g') ↦ Sum.elim g g'`. On **positions**
it merely relabels which side of the sum a position sits on. One round trip is
definitional (the recursor rule `Sum.elim g g' ∘ inl = g`); the other needs the
η-rule `Sum.elim (f ∘ inl) (f ∘ inr) = f`, which holds by `funext` + a case split
and forces one transport in `ContainerMorphism.ext'`.

This is a clean container-morphism isomorphism connecting `Monoidal.lean`'s
product `×` with the sequential operator `◁` — the first machine-checked cell of
the four-structure interaction table.
-/

namespace Containers

open Container

/-- The distributivity **shape iso** as a plain function equality, isolated
because it is the one non-definitional step: currying a sum-domain function and
uncurrying it back is the identity (the η-rule for `Sum.elim`). -/
theorem Container.sumElim_eta {α β γ : Type} (f : α ⊕ β → γ) :
    Sum.elim (fun a => f (Sum.inl a)) (fun b => f (Sum.inr b)) = f := by
  funext i; cases i <;> rfl

/-- Heterogeneous congruence for `Sigma.mk` under a change of fibre family: if the
two fibre families are equal, dependent pairs with the same index and
heterogeneously-equal payloads are heterogeneously equal. Both equalities `subst`
away, so the proof is `rfl`. -/
theorem heq_sigma_mk {ι : Type} {β γ : ι → Type} (hβ : β = γ) {i : ι}
    {w : β i} {w' : γ i} (hw : HEq w w') :
    HEq (⟨i, w⟩ : Sigma β) (⟨i, w'⟩ : Sigma γ) := by
  cases hβ; cases hw; rfl

/-- Endomorphism extensionality against the identity, transport-free. If a
container endomorphism `φ : C ⟶ C` is the identity on shapes and its position map
is heterogeneously the identity, then `φ = 𝟙`. Destructuring `φ` first makes its
shape map a local variable, so `subst` on the shape equation collapses the
dependent fibres — no `▸` transport survives. This is the tool for the one law
whose shape map is only propositionally (not definitionally) the identity. -/
theorem ContainerMorphism.ext_id {C : Container} {φ : ContainerMorphism C C}
    (hs : φ.onShapes = _root_.id) (hp : ∀ s p, HEq (φ.onPos s p) p) :
    φ = ContainerMorphism.id C := by
  obtain ⟨sm, op⟩ := φ
  dsimp only at hs hp
  subst hs
  have hop : op = fun _ => _root_.id := by
    funext s p; exact eq_of_heq (hp s p)
  subst hop
  rfl

/-- **Right distributivity of `◁` over `×`**: `(P × P') ◁ Q ≅ (P ◁ Q) × (P' ◁ Q)`.

`hom` curries the sum-domain shape map and relabels positions onto the matching
summand; `inv` uncurries with `Sum.elim` and relabels back. `inv_hom` is `rfl`
(the recursor rule makes the shapes agree definitionally); `hom_inv` carries the
single transport coming from the `Sum.elim`-η rule `Container.sumElim_eta`. -/
def Container.seqProdDistrib (P P' Q : Container) :
    ContainerIso ((P.prod P') ◁ Q) ((P ◁ Q).prod (P' ◁ Q)) where
  hom :=
    { onShapes := fun p =>
        (⟨p.1.1, fun a => p.2 (Sum.inl a)⟩, ⟨p.1.2, fun b => p.2 (Sum.inr b)⟩)
      onPos := fun _ => Sum.elim
        (fun aw => ⟨Sum.inl aw.1, aw.2⟩) (fun bw => ⟨Sum.inr bw.1, bw.2⟩) }
  inv :=
    { onShapes := fun X => ⟨(X.1.1, X.2.1), Sum.elim X.1.2 X.2.2⟩
      onPos := fun _ p =>
        match p with
        | ⟨Sum.inl a, w⟩ => Sum.inl ⟨a, w⟩
        | ⟨Sum.inr b, w⟩ => Sum.inr ⟨b, w⟩ }
  hom_inv := by
    refine ContainerMorphism.ext_id ?_ ?_
    · funext p
      rcases p with ⟨⟨s, s'⟩, f⟩
      exact congrArg (Sigma.mk (s, s')) (Container.sumElim_eta f)
    · intro s p
      rcases s with ⟨⟨s, s'⟩, f⟩
      obtain ⟨i, w⟩ := p
      cases i <;>
        exact heq_sigma_mk (congrArg (fun g q => Q.Pos (g q)) (Container.sumElim_eta f).symm)
          (HEq.refl w)
  inv_hom := by
    refine ContainerMorphism.ext' rfl ?_
    intro X p
    rcases X with ⟨⟨s, g⟩, ⟨s', g'⟩⟩
    rcases p with ⟨a, w⟩ | ⟨b, w⟩ <;> rfl

end Containers
