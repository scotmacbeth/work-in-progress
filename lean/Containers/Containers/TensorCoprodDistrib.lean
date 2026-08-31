import Containers.Dirichlet
import Containers.SeqProdDistrib

/-!
# Distributivity of the Dirichlet tensor over the coproduct

This file proves the **`⊗/+` = D cell** of Jules Hedges' interaction table for the
four monoidal structures on `Cont` (see
`projects/proofs/2026-07-16-hedges-distributive-table.md`, registry node
`hedges-interchange-table.cell-tensor-plus`): the Dirichlet tensor `⊗`
distributes over the categorical coproduct `+`,

  `(P + P') ⊗ Q  ≅  (P ⊗ Q) + (P' ⊗ Q)`   in `Cont`.

Here `+` is `Container.coprod` (`Containers.Cont`, shapes `S ⊕ S'`, positions
`Sum.elim` case-wise) and `⊗` is `Container.dirichlet` (`Containers.Dirichlet`,
shapes `S × T`, positions the *product* `P s × Q t`). This is the sibling of
`Container.seqCoprodDistrib` (the `◁/+` cell in `SeqCoprodDistrib.lean`): the same
container coproduct, with the Dirichlet tensor in place of the sequential
operator.

Unlike the two `◁`-based cells, `⊗` is **symmetric**, so this distributive law is
genuinely *two-sided* — the mirror law `Q ⊗ (P + P')` follows by the same argument
(or by composing with the Dirichlet symmetry). Only the left law is formalised
here; that already witnesses the cell.

## The bijection

Unfolding the two sides:

* `(P + P') ⊗ Q` has shapes `⟨tag, t⟩` with `tag : P.Shape ⊕ P'.Shape` and
  `t : Q.Shape`, and positions `Sum.elim P.Pos P'.Pos tag × Q.Pos t`.
* `(P ⊗ Q) + (P' ⊗ Q)` has shapes `inl ⟨s, t⟩` / `inr ⟨s', t⟩` and positions
  `P.Pos s × Q.Pos t` (resp. `P'.Pos s' × Q.Pos t`).

The bijection merely **transports the summand tag `inl`/`inr` across the `⊗`**.
On shapes, `⟨inl s, t⟩ ↦ inl ⟨s, t⟩` and `⟨inr s', t⟩ ↦ inr ⟨s', t⟩`; the fibre
`Sum.elim P.Pos P'.Pos (inl s)` *is* `P.Pos s` definitionally, so the second
tensor factor `Q.Pos t` is untouched and the position map is the identity. Both
round trips close by a case split on the sum tag followed by `rfl` — **no
transport**, exactly as in `SeqCoprodDistrib`: the coproduct's shape is already a
`Sum`, so no `Sum.elim`-η rule is invoked. (Contrast `SeqProdDistrib`, whose shape
map curries a sum-*domain* function and carries one transport.)

This is the third machine-checked cell of the four-structure interaction table,
and its first genuinely two-sided (symmetric) distributive cell.
-/

namespace Containers

open Container

/-- **Distributivity of `⊗` over `+`**:
`(P + P') ⊗ Q ≅ (P ⊗ Q) + (P' ⊗ Q)`.

`hom` pushes the coproduct tag `inl`/`inr` outward across `⊗`; `inv` pulls it back
in. Both position maps are the identity (the two sides are definitionally equal in
each summand — the untouched second Dirichlet factor `Q.Pos t` sits beside a fibre
`Sum.elim P.Pos P'.Pos (inl s) = P.Pos s`), and both round trips are a case split
on the tag followed by `rfl`: no transport appears, since the coproduct shape is
already a `Sum`. -/
def Container.dirCoprodDistrib (P P' Q : Container) :
    ContainerIso ((P.coprod P') ⊗ Q) ((P ⊗ Q).coprod (P' ⊗ Q)) where
  hom :=
    { onShapes := fun s => match s with
        | ⟨Sum.inl a, t⟩ => Sum.inl ⟨a, t⟩
        | ⟨Sum.inr b, t⟩ => Sum.inr ⟨b, t⟩
      onPos := fun s => match s with
        | ⟨Sum.inl _, _⟩ => fun w => w
        | ⟨Sum.inr _, _⟩ => fun w => w }
  inv :=
    { onShapes := fun X => match X with
        | Sum.inl ⟨a, t⟩ => ⟨Sum.inl a, t⟩
        | Sum.inr ⟨b, t⟩ => ⟨Sum.inr b, t⟩
      onPos := fun X => match X with
        | Sum.inl ⟨_, _⟩ => fun w => w
        | Sum.inr ⟨_, _⟩ => fun w => w }
  hom_inv := by
    refine ContainerMorphism.ext_id ?_ ?_
    · funext s; rcases s with ⟨tag, t⟩; cases tag <;> rfl
    · intro s p; rcases s with ⟨tag, t⟩; cases tag <;> exact HEq.refl _
  inv_hom := by
    refine ContainerMorphism.ext_id ?_ ?_
    · funext X; rcases X with ⟨a, t⟩ | ⟨b, t⟩ <;> rfl
    · intro X p; rcases X with ⟨a, t⟩ | ⟨b, t⟩ <;> exact HEq.refl _

end Containers
