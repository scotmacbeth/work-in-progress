# Comonoids in `(Cont, ◁, I)`: forward done, converse scoped

**Date:** 2026-07-14 (lean session)
**File:** `lean/Containers/Containers/Comonoid.lean` — builds clean, zero errors, zero
warnings, zero `sorry`. `#print axioms DirectedContainer.toComonoid` → `[Quot.sound]`.

## What landed

`Containers.Container.Comonoid C` — counit `ε : C ⟶ I`, comultiplication `δ : C ⟶ C ◁ C`,
and the three comonoid laws **stated internally to `Cont`**, built from `Container.seq₂`
(the action of `◁` on morphisms) and the unitors/associator of `Monoidal.lean`. No `Ext`,
no `[Set, Set]`, anywhere in the statement.

`Containers.DirectedContainer.toComonoid` — **every directed container is a `◁`-comonoid.**
Machine-checked. The axioms fell out exactly as the informal argument predicted:

| comonoid law | directed-container axiom |
|---|---|
| right counit `δ ; (C ◁ ε) = ρ⁻¹` | **D3** — *and it is transport-free* |
| left counit `δ ; (ε ◁ C) = λ⁻¹` | **D1** (shapes) + **D2** (positions) |
| coassoc `δ ; (δ ◁ C) ; α = δ ; (C ◁ δ)` | **D4** (shapes) + **D5** (positions) |

Same partition `Directed.lean` finds at the *comonad* level. That is the content: the
correspondence is an artifact of the monoidal structure on `Cont`, not of passing through
functors.

The right-counit line is worth seeing, because it is the whole thesis in one line — both
sides have *definitionally equal* shape maps, so the law simply **is** D3:

```lean
right_counit := ContainerMorphism.ext' rfl (fun s pu => D.d3 s pu.1)
```

## What did NOT land: the converse

**Not attempted in Lean.** `Comonoid C ⟹ DirectedContainer` and the two round-trips are
still open. This is an honest stop, not a hidden gap: the forward direction is a complete
theorem on its own, and I ran out of session before starting the converse. Registry:
`m3-comonoid-forward` = `lean-verified`, `m3b-comonoid-converse` = `in-progress`.

**It is fully scoped, and the linchpin is *cheaper* than at the comonad level.** In
`ComonadConverse.lean`, `cShape_eq` (the fact that comultiplication cannot change the outer
shape) had to be extracted by probing the right counit law at the generic element
`⟨s, id⟩ : Ext C (P s)`. Internally to `Cont` there is nothing to probe — the law is already
an equation of *morphisms*, so its shape component gives the result directly:

- write `δ.onShapes s = ⟨u s, m s⟩`;
- `(seq₂ (id C) ε).onShapes ⟨t, f⟩` reduces to `⟨t, fun _ => ()⟩`, so the left side of the
  right-counit law has shape map `s ↦ ⟨u s, fun _ => ()⟩`, while `(rightUnitor C).inv` has
  shape map `s ↦ ⟨s, fun _ => ()⟩`;
- `congrArg Sigma.fst` on the shape component therefore yields **`u s = s`** on the nose.

Once the outer shape collapses, `(ε.onPos s (), m s, δ.onPos s)` are exactly root, sub-shape
and shift, and `ComonadConverse.lean`'s template (`rSub`/`rShift` with transports along the
linchpin, then `rD1`–`rD5`) transfers verbatim. Expect the round-trip
`toComonoid ∘ toDirectedContainer = id` to be `rfl`, as it was for M2b.

## Two Lean lessons that cost me the converse's budget — read before you continue

1. **`ContainerMorphism.ext'` is the wrong ext lemma for this job.** It transports along
   `congrFun (funext hs) s`, which is only *propositionally* `hs s` — so `rw` can never match
   the transport in the resulting goal. I added `ContainerMorphism.ext_eq`, which takes a
   **pointwise** shape equality `hs : ∀ s, f s = g s`; then `hs s` appears literally in the
   position obligation. Use it. (Both are proved by `funext` + `cases`; definitional proof
   irrelevance collapses the residual casts.)

2. **`exact` succeeds where `rw` fails on transports.** Goal proof terms print as `⋯` and
   their implicit arguments are not in normal form, so `rw`'s syntactic matcher misses them.
   But *any two proofs of the same `Eq` are definitionally equal* (Prop proof irrelevance), so
   `exact h.trans (congrArg f ht).symm` typechecks against a goal whose transport is written
   with a different proof term. Also: **`congrArg Sigma.snd` does not typecheck** — `Sigma.snd`
   is a dependent projection. When the fibre is constant (e.g. over `I.Pos ()`), use an
   explicitly-typed lambda `fun z : (_u : A) × B => z.2`.

The transport machinery is already in the file and is reusable for the converse:
`Container.seq_pos_transport` computes the induced transport on `(E ◁ C).Pos` componentwise
(outer position fixed, inner transported along the pointwise shape equality); apply it twice,
nested, for anything involving `C ◁ (C ◁ C)`.
