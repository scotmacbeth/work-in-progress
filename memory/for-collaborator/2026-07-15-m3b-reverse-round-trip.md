# Lean — M3b reverse round trip closed: `Comonoid C ≃ DirectedContainer` fully certified

**Date:** 2026-07-15 (lean session)
**File:** `Containers/ComonoidConverse.lean` — `lake build` green, **0 errors / 0 warnings**.
**Axioms:** `Quot.sound` only (no `sorryAx`, no `propext`). `seq_pos_norm` is axiom-free.

## What landed

The last gap in M3b — the **reverse round trip** `comonoid → directed → comonoid = id` —
is now machine-checked. New declaration:

```
theorem Container.Comonoid.toDirectedContainer_toComonoid {C : Container}
    (M : Container.Comonoid C) : M.toDirectedContainer.toComonoid = M
```

Together with the pre-existing `DirectedContainer.toComonoid_toDirectedContainer` (the other
round trip, `rfl`) this upgrades M3/M3b from "both maps + one round trip" to a **full verified
isomorphism of the two packagings**: a `◁`-comonoid in `(Cont, ◁, I)` *is* a directed container,
both ways, both round trips certified.

## How the blocker fell

Last session the outer-shape `C ◁ C` transport "would not elaborate." Diagnosis: the position
half of the comult equality needs a transport whose change is in the **outer** shape of `C ◁ C`
(`s` vs `(δ.onShapes s).1 = cShape s`), so it is *not* an instance of the existing
`seq_pos_transport` (which fixes the outer shape). Fix — exactly the recipe in
[[dcont-laws-need-dependent-casts]]: isolate the cast in a bespoke lemma, generalising
`cShape s` to a **free variable** so `cases` can collapse it (sidesteps the occurs-check that
blocks substituting `cShape s = s` directly, since `cShape s` mentions `s`).

New helper:

```
theorem Container.seq_pos_norm (hcs : cs = s) (f : C.Pos cs → C.Shape)
    (u : C.Pos s) (r : C.Pos (f (hcs.symm ▸ u))) :
    (seq_shape_norm hcs f ▸ (⟨u, r⟩ : (C ◁ C).Pos ⟨s, fun p => f (hcs.symm ▸ p)⟩))
      = ⟨(hcs.symm ▸ u : C.Pos cs), r⟩ := by cases hcs; rfl
```

It is the position sibling of the already-present `seq_shape_norm`. Both close by `cases hcs; rfl`.

### Two elaboration gotchas worth reusing

1. **Anonymous-constructor over-generalisation.** Writing the RHS as `⟨hcs.symm ▸ u, r⟩` made the
   elaborator build a wild `Eq.ndrec` motive for the transport, then compute `r`'s expected type
   from it → mismatch. Fix: **ascribe the first component's type inline** —
   `⟨(hcs.symm ▸ u : C.Pos cs), r⟩` — so `▸` gets a clean expected type and the motive is
   `fun x => C.Pos x`.
2. **`rw` won't match an applied-lambda transport.** In the `ext_eq` obligation the transport
   appears as `(fun s => seq_shape_norm …) s ▸ p`, which `rw [seq_pos_norm]` cannot see. Closed it
   with `exact congrArg (M.comult.onPos s) (seq_pos_norm …).symm` instead — defeq does the
   beta-reduction and the LHS-shift unfolding that `rw` refused.

Also added `Container.Comonoid.ext` (two comonoids agree iff counit + comult agree; the three law
fields are Props → definitional proof irrelevance). The counit round trip is `rfl` (via `Unit`-η on
`I`, whose `Shape` and `Pos` are `Unit`).

## Provenance (unchanged)

The *theorem* M3 is Ahman–Chapman–Uustalu / Dorta–Jarvis–Niu (arXiv:2305.05655, Thm 4.3) —
see [[dorta-jarvis-niu-neighbour]]. The **machine-checked both-directions-with-both-round-trips**
proof over `(Cont, ◁, I)` is the Lean contribution. Registry `equivalence-chain.json` node
`m3b-comonoid-converse` bumped to point at the round-trip theorem.

## Not touched (secondary task deferred)

The "add 5 orphaned modules to the root import" task: the root `Containers.lean` already documents
why CoKleisli / Cofunctor / ComonadConverse(imported) / Composition / TrajectoryComposition stay
orphaned (genuine clashes / compile errors, not import gaps). ComonadConverse *is* imported. Left
as-is — primary target consumed the session and the note there is already accurate.
