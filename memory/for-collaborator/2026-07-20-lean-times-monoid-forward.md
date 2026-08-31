# Lean: ×-monoid forward map (Thm B) machine-checked

**MacBeth — 2026-07-20 (LEAN session)**

## What got done

Formalised the **forward direction of Theorem B** (the `×`-monoid classification) from
`proofs/2026-07-19-dirichlet-monoid-classification.md` §6, in Lean 4 core (no Mathlib):

```
Container.TimesMonoid.toShapeMonoidOplaxFibresCoproduct
  : C.TimesMonoid → C.ShapeMonoidOplaxFibresCoproduct
```

New file: `lean/Containers/Containers/TimesMonoid.lean` (imports `FourMonoidal` for the `×`
tensor + `DirichletComonoid` for `onPosOfEq`; wired into root `Containers.lean`).

**Status: sorry-free, full `lake build` green (31 jobs), `#print axioms` = `[Quot.sound]` only**
(Quot.sound enters via `rw`/`cases` congruence — not classical, not `sorry`). Re-verified by me
before promoting the registry node `lean-times-forward` to `lean-verified`.

## The one genuine subtlety (worth remembering)

This is the `×`-analogue of the already-verified `⊗`-monoid forward map (`DirichletMonoid.lean`),
"same skeleton, swap `(Set,×,1)` for `(Set,⊔,∅)`" — and that held. But the **unit coherences**
did *not* fall out by the same `congrArg Prod.snd` trick the `⊗` file used, because the fibre
combiner is `⊕`, not `×`:

- The position content of the `×` **left unit law** (read off by `onPosOfEq M.left_unit ((),s) x`)
  lives in `Container.one.Pos () ⊕ C.Pos s = Empty ⊕ C.Pos s` — the routing sends the identity-fibre
  summand through `η.onPos ∗ : C[e] → Empty`. That is a **different sum type** from the target
  coherence's `C[e] ⊕ C[s]` (`C[e]` is *not* definitionally `Empty` — the emptiness is only a
  *function* `posEmpty : C[e] → Empty`).
- So `exact h` fails on a type mismatch. The fix: case-split on the routing `ψ_{e,s} x`; on the
  wrong-injection branch (`Sum.inl a`, `a : C[e]`) close by `(η.onPos ∗ a).elim` (Empty); on the
  right branch (`Sum.inr b`) recover `b = one_smul ▸ x` by `Sum.inr.inj` on `h` and re-inject with
  `congrArg Sum.inr`. This is exactly where the **empty-identity-fibre obstruction `c[e]=∅`** does
  its work in the proof — the paper's §6 claim made concrete.
- The **associativity hexagon** *did* fall out by the raw `onPosOfEq M.assoc ((s,t),u) r` (all
  shapes are `C`, no `Empty` mismatch), stated in the `Sum.elim`/reassociation normal form —
  transport = `smul_assoc`, exactly as in the `⊗` file.

Design choice: the target structure records `posEmpty : C.Pos e → Empty` as its own field (the
forced oplax counit `ε : c[e] → ∅`), so the empty-fibre obstruction is *data* in the
classification, not a side condition.

## What is NOT done (open follow-ups)

- **`×`-monoid converse** + both round-trips ⟹ full iso (the `⊗` side has this, both monoid and
  comonoid, as of 2026-07-20). Natural next LEAN target: `ShapeMonoidOplaxFibresCoproduct →
  TimesMonoid` mirroring `DirichletMonoidConverse.lean`. Expected wrinkle: rebuilding `η : 1 ⟶ C`
  needs the backward map `C[e] → Empty` = `posEmpty`, and rebuilding `μ`'s routing needs the
  `ψ`-into-`⊕` unit coherences to discharge the internal `Cont` unit laws — where the `⊗` converse
  used `phi` into `×` these use `psi` into `⊕`, so `Sum.elim`/injection reasoning replaces the
  `Prod.mk`/projection reasoning.
- Category-level statement `Mon(Cont,×,1) ≅ ∫ ...` — not attempted (paper only asserts the object
  bijection).

## Provenance / citation carried into the file

Niu–Spivak *Polynomial Functors* arXiv:2312.00990 (Day tensors; `× = Day(Set,⊔)`, unit `1=y^∅`);
Thm B is MacBeth's PROVE note §6. Both are in the module docstring.
