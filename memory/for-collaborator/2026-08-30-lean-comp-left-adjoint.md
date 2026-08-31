# LEAN 2026-08-30 — `F_q ⊣ (−)◁q` machine-checked, sorry-free

**File:** `lean/Containers/Containers/CompLeftAdjoint.lean`, wired into the `Containers.lean`
root. `lake build` green (58 jobs), zero errors, zero warnings, zero sorries.
`#print axioms` = `[Quot.sound]` only on all six declarations.

**Status: complete.** L1–L4 of the brief all landed; nothing outstanding, no sorries.

## What is verified

| brief | declaration | proof |
| L1 functor | `Container.leftAdj`, `Container.leftAdjMap`, `leftAdjMap_id`, `leftAdjMap_comp` | `ext' rfl (fun _ _ => rfl)` |
| L2 unit/counit | `Container.adjUnit`, `Container.adjCounit` | (definitions) |
| L3 triangles | `Container.triangle_leftAdj`, `Container.triangle_seq` | `ext' rfl (fun _ _ => rfl)` |
| L4 hom bijection | `adjTranspose`/`adjUntranspose` + both round trips | `ext' rfl (fun _ _ => rfl)` |

Unit and counit are transcribed **verbatim** from §4.4 of
`proofs/2026-08-30-pra-vs-probe-method.md`: `η` is the generic-choice/evaluation pair
`ρ ↦ ⟨ρ, fun w => w.1⟩`, `⟨w, z⟩ ↦ w.2 z`; `ε` is first-projection on shapes and the coproduct
injection `a ↦ ⟨c a, fun z => ⟨a, z⟩⟩` backwards.

## The variance — what the formalisation was for, and it checks out

A `ContainerMorphism` is forward on shapes and **backward** on positions. So `F_q`'s action on
a morphism `φ` cannot push `⟦q⟧` forward; it must run `⟦q⟧` over the backward leg:

    onPos ρ := Ext.map (φ.onPos ρ)  :  ⟦q⟧ (r'.Pos (φ.onShapes ρ)) → ⟦q⟧ (r.Pos ρ)

The forward reading — which the object formula `F_q(R,U) = (R, ρ ↦ ⟦q⟧(U_ρ))` genuinely invites,
and which the Yoneda argument of §4.3 hides entirely — **does not typecheck at all**. This is the
same class of error `WorkersRetract.lean` caught last cycle. Here the informal proof was right;
the formalisation confirms it rather than correcting it.

## The pleasant surprise, and one real piece of information

Every law is `ContainerMorphism.ext' rfl (fun _ _ => rfl)`. Shapes agree definitionally,
positions agree pointwise-definitionally, **no transport anywhere**. The triangles are not
"proved" so much as *observed*: with the variance set up correctly the two sides are the same
term up to η for functions and structures.

That could be suspicious, so I ran a **negative control**. Perturb `ε`'s backward map to inject
at a fixed position `a₀ : (s : p.Shape) → p.Pos s` rather than at `a`. Result: the shape leg
`hs := rfl` **still succeeds** (the perturbation is invisible on shapes) and the position leg
**fails** with a type mismatch. Two consequences worth recording:

1. The triangles are non-vacuous — `ext'`'s position hypothesis carries the content.
2. **The adjunction is a statement about positions, not shapes.** A shape-level argument would
   certify the wrong counit just as happily. This is the precise sense in which the two-line
   Yoneda proof is under-determined, and it is a reusable warning for the `Fam(C^op)` versions.

## Scope — deliberately NOT formalised
- Naturality of `F_q` **in `q`** — §4 Theorem B flags this as unchecked, so there is nothing
  settled to formalise. Cheap next target if wanted.
- The `Fam(Vec^op)` version — open PROVE target, not a theorem.
- The right adjoint / `◁`-left-closure — does not exist for `|T| ≥ 2`; formalising it would be
  formalising a falsehood.

## Notes for the repo
- **`Containers/Composition.lean` is orphaned** and the LEAN.md brief pointed at it. The live
  `◁` is `Container.seq` (`Sequential.lean`) with `seq₂`/`whiskerLeft`/`whiskerRight`
  (`Monoidal.lean`). Convention matches the paper (`G ◁ F` = `G` outside), so `L_q p` is
  `Container.seq p q` with no translation. `whiskerRight (adjCounit q p) q` *is* `ε_p ◁ q`.
  Worth fixing the brief template's pointer.
- This is the library's **first adjunction**. `leftAdj`/`leftAdjMap` + the two transposition maps
  are the natural nucleus if we ever want a general `Adjunction` structure over the hand-rolled
  `Category` class in `Cont.lean`.

## Registry
`proofs/registry/pra-vs-probe-method.json`, new child `lean-adjunction`, role `attempt`, trust
`lean-verified`, `lean: Containers.Container.triangle_leftAdj`.
`trustcheck.py --deployment code/macbeth.json validate` → **OK**.
`registry_validate.py` reports one problem, **pre-existing and not from this session**: root is
`proved` while child `small-case-sweeps` is `computed`. That node is deliberately `computed`
(house rule: script/sub-agent computation is `computed`, never higher). I did not upgrade it —
silencing the advisory by inflating trust would be exactly the thing the trust grades exist to
prevent. Flagging it as a validator-vs-house-convention tension for you to adjudicate.
