# M3b machine-checked: a `◁`-comonoid is a directed container

**File:** `projects/lean/Containers/Containers/ComonoidConverse.lean` (new, sorry-free,
`Quot.sound` only — the funext footprint, identical to the forward direction).
**Registry:** `m3b-comonoid-converse` → `lean-verified`,
`lean = Containers.Container.Comonoid.toDirectedContainer`.

## What landed

`Container.Comonoid.toDirectedContainer : (M : Comonoid C) → DirectedContainer` — the converse of
M3. This closes M3 into (most of) an equivalence, matching M1/M2/M2b.

**The key move — reduce the comonoid to a comonad and reuse M2b.** The counit `ε` and comult `δ`
of a `◁`-comonoid *are already* the combinatorial data of a `ContainerComonad` (the M2b object):
`e s = ε.onPos s ()`, and `(cShape, cSub, cVal) = (δ.onShapes ·).1 / .2 / δ.onPos`. Because the
extension functor sends `◁` to composition (`Container.seqExt`), the comonad counit/comult built
from that data are **definitionally** `ε.toNat` / `δ.toNat` repackaged through `seqExt`
(`toContainerComonad_comult_eq` is literally `rfl`). So I only had to prove the three `IsComonad`
laws, then hand the result to the already-verified `ContainerComonad.toDirectedContainer`. All the
`cShape`-transport bookkeeping that produces D1–D5 was done once, in `ComonadConverse`, and is reused.

## Two techniques worth reusing

1. **Counit laws by iso-cancellation.** A comonoid counit law `δ ; (C ◁ ε) = ρ⁻¹` is a morphism
   equality into `C ◁ I`, whose position transports are ugly. **Compose both sides with the unitor's
   `hom`**: `(δ ; (C◁ε)) ; ρ = ρ⁻¹ ; ρ = id_C`. Now it is a `C ⟶ C` morphism, and projecting its
   `onShapes`/`onPos` (via a one-line destructor `ContainerMorphism.congr_onPos`, `subst h; rfl`)
   gives exactly `cShape s = s` and the D3/D2 value equations with **only the intrinsic `cShape`
   transport left**. No `C ◁ I` position gymnastics.

2. **Coassociativity for free, transport-free.** Both sides of the comonad coassoc law are the *same*
   repackaging `tripleSeqExt` of the two sides of the comonoid coassoc law — **crossed**: comonad-LHS
   ≡ comonoid-RHS, comonad-RHS ≡ comonoid-LHS, each by `rfl` (I lost ten minutes getting the pairing
   uncrossed — the double-comult's outer shape is `cShape(cShape s)`, which matches the
   *associator-composed* side, not the naive one). So the whole coassoc law is one `rw [M.coassoc]`.

## What is NOT done — one round trip

- **DONE:** `DirectedContainer.toComonoid_toDirectedContainer` (directed → comonoid → directed = id) —
  `rfl`, because the recovered `ContainerComonad` is defeq to `DirectedContainer.toContainerComonad`.
- **OUTSTANDING:** `toDirectedContainer_toComonoid` (comonoid → directed → comonoid = original). Counit
  matches definitionally; comult matches on **shapes** (`Container.seq_shape_norm`, which is in the
  file). The **position** half needs a transport whose change is in the *outer* shape of `C ◁ C`
  (`s` vs `(δ.onShapes s).1`) — so `Container.seq_pos_transport` (which fixes the outer shape) does
  **not** apply. My bespoke lemma for it would not elaborate: stating `⟨hcs.symm ▸ u, q⟩ : (C◁C).Pos ⟨cs,f⟩`
  against the nested dependent `Sigma` confuses the motive. This is the one remaining piece for a full
  `DirectedContainer C ≃ Comonoid C`. Likely fix: an `HEq`-based statement or a `Sigma`-level congruence
  lemma proved by `cases hcs` on generalised `s, cs` before touching positions.

## Housekeeping (also this session)

Root `Containers.lean` now imports `ComonadConverse` + `ComonoidConverse`. The other loose modules are
**not** a mere import gap and stay orphaned (each breaks `lake build`): `Composition` redefines
`Container.I`; `Cofunctor` redefines `DContMorphism` (clash with `DContCat`); `CoKleisli` has an
unsolved strength/counit goal; `TrajectoryComposition` has a malformed `import Trajectory`. Neil's
"which files are missing" (uid 56) was about *these* — the answer is they conflict, not that they're
absent. Repairing them is a separate task.

**Fibrational note for the book (SS23, arXiv:2305.00167 Rmk 3.16):** Lean confirms at the Set level
that the converse reaches for `Π` only in the *packaging* (`◁`/`seqExt`), never in the correspondence
itself — once `seqExt` unfolds `◁`, coassoc is `rfl`-repackaging. Honest evidence for "composition,
not Π."
