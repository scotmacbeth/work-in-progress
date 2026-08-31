# Lean: ×-monoid classification CONVERSE + round-trips — full iso (2026-07-20)

**Module:** `lean/Containers/Containers/TimesMonoidConverse.lean` (new; imports `TimesMonoid`,
wired into root `Containers.lean`). **Sorry-free**, `lake build` green (32 jobs), zero warnings.

## What is now machine-checked

The converse of the ×-monoid (cartesian/product tensor) classification, plus **both round trips**,
upgrading the forward map (`lean-times-forward`, 2026-07-20) to a genuine isomorphism:

    Container.TimesMonoid c  ≅  Container.ShapeMonoidOplaxFibresCoproduct c

The reverse map `toTimesMonoid` rebuilds
- `η : 1 ⟶ C` — `onShapes = fun _ => e`, `onPos = posEmpty : C[e] → Empty = 1[∗]`;
- `μ : C × C ⟶ C` — `onShapes = smul`, `onPos = psi : C[s·t] → C[s] ⊕ C[t]`;

from a monoid `(smul, e)` on shapes with **empty identity fibre** + an oplax monoidal functor on
fibres into `(Set, ⊔, ∅)`. The three internal `Cont`-laws come off via `ContainerMorphism.ext'`:
shape eq = monoid axiom (`one_smul`/`smul_one`/`smul_assoc`), fibre goal = oplax coherence
(`psi_one_smul`/`psi_smul_one`/`psi_assoc`). Both round trips are pure `rfl`.

`#print axioms` on `toTimesMonoid`, `left_unit_law`, `right_unit_law`, `assoc_law`, and **both**
round-trip lemmas = `[Quot.sound]` only (enters solely via `funext` packaging the pointwise shape
law for `ext'`). No `sorryAx`, no `Classical`.

## Milestone

**The entire (co)monoid table now has both Day-MONOID columns (⊗ and ×) machine-checked as full
isos on both sides.** Status:
- ⊗-monoid: forward + converse + iso ✓ (`DirichletMonoid` / `DirichletMonoidConverse`)
- ×-monoid: forward + converse + iso ✓ (`TimesMonoid` / `TimesMonoidConverse`) ← **this session**
- ⊗-comonoid: forward + converse + iso ✓ (`DirichletComonoid...`)
- Still open: nothing on the Day-monoid/⊗-comonoid slices; the ×-comonoid slice is degenerate
  (product comonoids) and not separately targeted.

## The LEAN.md predicted wrinkle did NOT recur

LEAN.md warned the ⊗ file's `congrArg Prod.snd` unit-coherence shortcut FAILS for × (unit content
lands in `Empty ⊕ C[s]`) and expected the converse round trips to hit its mirror. It didn't: the
converse routes unit coherence through `psi_one_smul`/`psi_smul_one` and a **defeq `Sum.elim`
collapse** (`Sum.elim f Sum.inr (Sum.inr x) ≡ Sum.inr x`), so no empty-fibre `.elim` was needed on
the converse side at all — that only appeared in the *forward* map. The port from the ⊗ converse
was essentially verbatim with `(Set,⊔,∅)` for `(Set,×,1)`.

## One-line gotcha for reuse

After `rw [F.psi_one_smul …]` / `rw [F.psi_smul_one …]` the goal is defeq but NOT syntactically
`a = a` (the two `▸`-transports carry different proof terms, equal only by proof irrelevance), so
`rw`'s auto-`rfl` does **not** fire — you must append an explicit `rfl`. Cost me one build cycle.

## Verification done by MacBeth

`lake build` full green, `grep -n "sorry\|admit"` = none, `#print axioms` = `[Quot.sound]` on every
declaration. Registry `dirichlet-monoid-classification.json` child `lean-times-converse` set to
`lean-verified`; `registry_validate.py` OK.
