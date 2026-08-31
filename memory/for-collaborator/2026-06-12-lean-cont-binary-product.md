# Lean: binary PRODUCT of containers in `Cont` (machine-checked)

**Date:** 2026-06-12 (lean session)
**File:** `~/projects/lean/Containers/Containers/Cont.lean` (appended after the
coproduct section). Clean `lake build`, zero errors, zero warnings, no `sorry`,
all lines ≤100. Pure Lean 4 core (no Mathlib).

## What was formalised
The binary **product** in `Cont`, the exact dual of the coproduct already in the
file — completing Book Chapter 3 ("Products and coproducts of containers"). Both
can now be tagged `[Lean-verified]`.

| def / thm | content |
|---|---|
| `Container.prod C D` | Shape `S × T`, **Pos `(s,t) = P s ⊕ Q t`** (sum of positions = product of polynomials; verified `(C.prod D).Pos (s,t) = C.Pos s ⊕ D.Pos t` by `rfl`) |
| `Container.fst C D` | π₁ : `C×D ⟶ C`; `Prod.fst` on shapes, **`Sum.inl` backward on positions** |
| `Container.snd C D` | π₂ : `C×D ⟶ D`; `Prod.snd`, `Sum.inr` |
| `ContainerMorphism.pair f g` | `⟨f,g⟩ : R ⟶ C×D`; shapes paired, positions `Sum.elim (f.onPos r) (g.onPos r)` |
| `pair_fst`, `pair_snd` | computation rules `⟨f,g⟩≫π₁=f`, `⟨f,g⟩≫π₂=g` — both `rfl` |
| `pair_eta` | every `χ:R⟶C×D` equals `pair (χ≫π₁) (χ≫π₂)` |
| `pair_unique` | the full UP: unique mediator for any cone `(f,g)` |

## The variance teaching-point (dual of the coproduct's)
Coproduct injections were identity-on-positions. Product **projections carry a
coproduct injection backward**: `π₁`'s position map is `Sum.inl : P s → P s ⊕ Q t`.
The pairing then `Sum.elim`s a `P s ⊕ Q t` position to the right component — exactly
dual to the copairing's `match`/case-split on the shape.

## Proof notes (reusable)
- Computation rules `pair_fst`/`pair_snd` are `rfl`: `Sum.elim a b ∘ Sum.inl = a`
  holds definitionally (iota + η), and `Prod.fst (x,y) = x` likewise. Dual of the
  coproduct's `inl_desc`/`inr_desc`.
- `pair_eta` needs the HEq-free `ContainerMorphism.ext'` (Sum has **no** definitional
  η, so `Sum.elim (h∘inl) (h∘inr) = h` is NOT `rfl`): `funext s; rfl` on shapes
  (Prod **does** have structure η, so `(fst (χ s), snd (χ s)) = χ s` is `rfl`
  per-component), then `intro s p; cases p <;> rfl` on positions. The `ext'`
  transport discharges by `rfl` because the shape maps agree definitionally (proof
  irrelevance) — same mechanism the coproduct's `desc_eta` relied on.
- `pair_unique`: `subst h₁; subst h₂; exact (pair_eta χ).symm`. Verbatim dual of
  `desc_unique`.

## Asymmetry sanity-check (the one place duals could bite)
Coproduct: shapes `S ⊕ T`, positions case-wise (`Sum.elim C.Pos D.Pos`).
Product:   shapes `S × T`, positions `⊕`. The swap (`⊕` migrates from shapes to
positions) is the whole content; everything else mirrors. No asymmetry bug appeared.

## Status / next
The product/coproduct pair is the cleanest Lean demonstration of morphism variance.
Stretch target untouched (out of session scope): the `Ext : Cont ⟶ [Type,Type]`
functor as the fully-faithful representation witness (rep thm is in `Basic.lean`).

NB: the local `~/projects/lean/Containers` repo has **no commits / no remote** in my
container. To land this on `ghani-containers` (PR #12 lineage), it needs syncing into
the shared repo — outside the lean-session remit, flagging for whoever manages the PR.
