# Lean session 2026-07-22 — ×-monoid converse target was already done; re-verified clean

## TL;DR
The LEAN.md target for today (**×-monoid classification converse + both round-trips**,
`TimesMonoid c ≅ ShapeMonoidOplaxFibresCoproduct c`) was **already fully formalised on
2026-07-20** in `lean/Containers/Containers/TimesMonoidConverse.lean`. The 2026-07-22 LEAN.md
was stale — it re-requested completed work. No new formalisation was needed. I re-verified the
existing artefact end-to-end from a clean build and confirmed nothing rotted.

## Verification performed this session
- `lake build` (full library): **35 jobs, exit 0**, zero errors.
- Rebuild of `Containers.TimesMonoidConverse` in isolation: **zero warnings**.
- `#print axioms` on the three headline declarations:
  - `Container.ShapeMonoidOplaxFibresCoproduct.toTimesMonoid`
  - `…toTimesMonoid_toShapeMonoidOplaxFibresCoproduct` (fwd∘rev = id)
  - `Container.TimesMonoid.toShapeMonoidOplaxFibresCoproduct_toTimesMonoid` (rev∘fwd = id)
  → all **`[Quot.sound]` only** (enters solely via `funext` packaging the pointwise shape law
  for `ext'`). No `sorryAx`, no `Classical.choice`.
- Registry `proofs/registry/dirichlet-monoid-classification.json`: node `lean-times-converse`
  already `trust: lean-verified`, `lean` field set; `registry_validate.py` → **OK (status: proved)**.

## Why there was no fresh in-scope target
The (co)monoid table's Lean coverage is now complete on all **nondegenerate** cells:
- ◁ (Sequential/DCont): `Comonoid` + `ComonoidConverse` — both sides.
- ◁-monoid: `Free.lean` (free monad).
- ⊗ (Dirichlet): `DirichletMonoid`(+Converse), `DirichletComonoid`(+Converse) — both sides.
- × (product): `TimesMonoid`(+Converse) — both sides. ← re-verified today.

There is **no ×-comonoid file, and there should not be one**: `×` is the *categorical product*
in Cont (Cont is CCC, not LCC; `× = Day(Set, ⊔, ∅)` is the cartesian product), and comonoids for a
cartesian-product tensor are degenerate — every object is uniquely a comonoid via the diagonal, so
`Comon(Cont, ×, 1) ≅ Cont` with nothing to classify. The bare-comonoid PROVE note
(`2026-07-17-bare-dirichlet-comonoid.md`) accordingly covers only ⊗-comonoids (= families of
monoids). Formalising the degenerate × case would be trivial and is not a proved theorem worth
promoting.

The LEAN.md stretch (`⋊` left-closed via `Adjunction.mkOfHomEquiv`) is off-priority this week
(touches the deferred Dialectica line, Ch4+, and Neil's steer is close chapters 1–3, no moonshots),
so I did not pursue it.

## Suggested next LEAN target (for a future wake-session to set)
None within the Ch1–3 (co)monoid table — it is closed in Lean. If more Lean is wanted this week,
the honest candidates are OUTSIDE the table and would each first need a paper proof confirmed:
either bundle the existing four table isos as explicit `Equiv`-style records (cosmetic; low value),
or pick a fresh proved Ch1–3 result. Recommend: leave Lean here and spend effort on the Ch1–3
prose/close-out that Neil asked for.

— MacBeth
