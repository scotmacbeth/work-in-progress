# Lean: container composition `◁` — unit, associator, extension law (PR #13)

**Date:** 2026-06-12 (lean session)
**Branch:** `lean-composition-product`, stacked on `lean-consolidate` (PR #12)
**PR:** https://github.com/RaggedR/ghani-containers/pull/13
**File:** `lean/Containers/Containers/Composition.lean` (new), wired into `Containers.lean`.
**Status:** clean `lake build`, zero warnings, zero `sorry`.

## What it adds
The composition product `◁` on `Cont` — the spine operation (`◁`-comonoids are
directed containers).

1. `Container.comp G F` written `G ◁ F` (scoped `infixr:70`), G outer / F inner:
   - `Shape := (t : G.Shape) × (G.Pos t → F.Shape)`
   - `Pos ⟨t,f⟩ := (q : G.Pos t) × F.Pos (f q)`
2. `Container.I := Unit ◁ (fun _ => Unit)` (the unit).
3. **Extension law (machine-checked):** `compExt`/`compExtInv` and both round-trip
   lemmas establish `Ext (G ◁ F) X ≅ Ext G (Ext F X)`, i.e. `⟦G◁F⟧ = ⟦G⟧∘⟦F⟧`.
   This is what pins the convention down — not just a docstring.
4. `ContainerIso C D` (hom, inv, two round-trip laws).
5. Coherences as isos:
   - `Container.leftUnitor  : ContainerIso (I ◁ F) F` — **axiom-free**, round trips `rfl`.
   - `Container.rightUnitor : ContainerIso (F ◁ I) F` — **axiom-free**, round trips `rfl`.
   - `Container.associator  : ContainerIso ((H ◁ G) ◁ F) (H ◁ (G ◁ F))` — uses only
     `Quot.sound` (via `ext'`/`funext`), matching the rest of the dev.

## The pleasant surprise (worth remembering)
I expected heavy dependent-cast work (cf. my D2/D5 note
`dcont-laws-need-dependent-casts`). It did **not** materialise. With G-outer/F-inner
variance and the curried shape map, every dependent type lines up *definitionally*:

- Unit laws collapse by `Unit`-η + `Sigma`-η → the round trips are literally `rfl`.
- The associator is pure re-association of a nested dependent sum,
  `(⟨u,v⟩, p) ↔ (u, ⟨v, p⟩)`, and the fibre `F.Pos ((m u).2 v)` is **defeq** to
  `F.Pos (k ⟨u,v⟩)`. So it is **transport-free**; the laws close by `rcases` + `rfl`.

Same phenomenon as the `rfl` category laws in `Cont.lean` — variance set up right
makes the bookkeeping definitional.

## Suggested follow-ons (not done here — would be prove/lean targets)
1. **`◁`-comonoid = directed container.** Formalise: a `Container.I`-counit +
   `C ⟶ C ◁ C` comult satisfying comonoid laws ⟺ the `Directed` axioms (D1–D5).
   This closes the loop with `ComonadConverse.lean`. The Lean home of the spine.
2. **Monoidal category proper.** Triangle + pentagon coherence for
   `(Cont, ◁, I, leftUnitor, rightUnitor, associator)`. Pentagon will be the real
   test — but if it stays transport-free like the associator, it may be `cases`+`rfl`.
3. **Chain rule.** The container chain rule `∂(G◁F) ≅ (∂G◁F)×∂F`
   (`proofs/2026-06-12-container-chain-rule.tex`) now has its `◁`, `×` substrate in
   Lean; the derivative `∂` is the only missing piece to formalise that next.

— MacBeth
