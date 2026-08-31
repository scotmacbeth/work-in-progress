import Containers.SeqProdDistrib

/-!
# Left distributivity of the sequential operator over the coproduct

This file proves the **`;+` = D cell** of Jules Hedges' interaction table for the
four monoidal structures on `Cont` (see
`projects/proofs/2026-07-16-hedges-distributive-table.md`, registry node
`cell-comp-plus`): the sequential operator `◁` distributes over the categorical
coproduct `+` **on the left factor**,

  `(P + P') ◁ Q  ≅  (P ◁ Q) + (P' ◁ Q)`   in `Cont`.

Here `+` is `Container.coprod` (`Containers.Cont`, shapes `S ⊕ S'`, positions
case-wise) and `◁` is `Container.seq` (`Containers.Sequential`, the
composition/sequential operator). This is the sibling of `Container.seqProdDistrib`
(the `;×` cell in `SeqProdDistrib.lean`): the same distributor `◁`, with the
container coproduct in place of the product.

Distributivity is **one-sided only**: the right-variable law `P ◁ (Q + Q')` fails
(Niu–Spivak Ex 6.56, witness `(y + 1) ◁ (1 + 0) = 2 ≇ 3`), so only the left law is
an isomorphism.

## The bijection

Unfolding the two sides:

* `(P + P') ◁ Q` has shapes `⟨t, f⟩` with `t : P.Shape ⊕ P'.Shape` and
  `f : (Sum.elim P.Pos P'.Pos t) → Q.Shape`, and positions
  `(q : Sum.elim P.Pos P'.Pos t) × Q.Pos (f q)`.
* `(P ◁ Q) + (P' ◁ Q)` has shapes `⟨s, g⟩` (on either summand) and positions
  `(q : P.Pos s) × Q.Pos (g q)` (resp. with `P'`).

The bijection merely **transports the summand tag `inl`/`inr` across the `◁`**.
On shapes, `⟨inl s, f⟩ ↦ inl ⟨s, f⟩` and `⟨inr s', f⟩ ↦ inr ⟨s', f⟩`; the fibre
`Sum.elim P.Pos P'.Pos (inl s)` *is* `P.Pos s` definitionally, so `f` needs no
adjustment. On positions the two sides are definitionally equal in each summand,
so the position maps are the identity. Both round trips close by a case split on
the sum tag followed by `rfl` — **no `Sum.elim`-η rule and no transport**, in
contrast to the product cell, whose shape map curried a sum-*domain* function and
carried one transport. The coproduct's shape is already a `Sum`, so the currying
collapses to a plain case split, exactly as anticipated.

This is the second machine-checked cell of the four-structure interaction table.
-/

namespace Containers

open Container

/-- **Left distributivity of `◁` over `+`**:
`(P + P') ◁ Q ≅ (P ◁ Q) + (P' ◁ Q)`.

`hom` pushes the coproduct tag `inl`/`inr` outward across `◁`; `inv` pulls it back
in. Both position maps are the identity (the two sides are definitionally equal in
each summand), and both round trips are a case split on the tag followed by `rfl`:
no transport appears, since — unlike the product cell — the coproduct shape is
already a `Sum` and no `Sum.elim`-η rule is invoked. -/
def Container.seqCoprodDistrib (P P' Q : Container) :
    ContainerIso ((P.coprod P') ◁ Q) ((P ◁ Q).coprod (P' ◁ Q)) where
  hom :=
    { onShapes := fun s => match s with
        | ⟨Sum.inl a, f⟩ => Sum.inl ⟨a, f⟩
        | ⟨Sum.inr b, f⟩ => Sum.inr ⟨b, f⟩
      onPos := fun s => match s with
        | ⟨Sum.inl _, _⟩ => fun w => w
        | ⟨Sum.inr _, _⟩ => fun w => w }
  inv :=
    { onShapes := fun X => match X with
        | Sum.inl ⟨a, g⟩ => ⟨Sum.inl a, g⟩
        | Sum.inr ⟨b, g⟩ => ⟨Sum.inr b, g⟩
      onPos := fun X => match X with
        | Sum.inl ⟨_, _⟩ => fun w => w
        | Sum.inr ⟨_, _⟩ => fun w => w }
  hom_inv := by
    refine ContainerMorphism.ext_id ?_ ?_
    · funext s; rcases s with ⟨t, f⟩; cases t <;> rfl
    · intro s p; rcases s with ⟨t, f⟩; cases t <;> exact HEq.refl _
  inv_hom := by
    refine ContainerMorphism.ext_id ?_ ?_
    · funext X; rcases X with ⟨a, g⟩ | ⟨b, g⟩ <;> rfl
    · intro X p; rcases X with ⟨a, g⟩ | ⟨b, g⟩ <;> exact HEq.refl _

end Containers
