# Lean: the category `Cont` of containers + binary coproduct (DONE)

**Date:** 2026-06-11 (lean session)
**File:** `lean/Containers/Containers/Cont.lean` (core-only, no Mathlib)
**PR:** NOT YET PUSHED — see "Pushing" below. New module, added to `Containers.lean` root.
**Status:** `lake build` zero errors / zero warnings; no line >100 chars.
Axiom check:
- `id_comp`, `comp_id`, `comp_assoc`, `inl_desc`, `inr_desc`, the `Cont` instance →
  **depend on NO axioms** (all `rfl`).
- `ext'`, `desc_eta`, `desc_unique` → `[Quot.sound]` only (via `funext`; unavoidable, honest).

## What is formalised (the `LEAN.md` target for this session)

The directive (2026-06-11 strategic pivot, Neil): **Cont as a `Category`** — the Lean
backbone of the book's Chapter 2. Reused the existing `Container` and `ContainerMorphism`
from `Basic.lean` (did NOT redefine; variance was already correct there).

### Core: Cont is a category
- `ContainerMorphism.id C` — identity-on-shapes, identity-on-positions.
- `ContainerMorphism.comp φ ψ` (diagrammatic order, `φ` then `ψ`): shape maps compose
  **forward** (`ψ.onShapes ∘ φ.onShapes`), position maps compose **backward**
  (`φ.onPos s ∘ ψ.onPos (φ.onShapes s)`).
- Law lemmas `id_comp`, `comp_id`, `comp_assoc` — **all `rfl`**.
- A minimal hand-rolled `Category` typeclass (Mathlib-free, mirrors
  `CategoryTheory.Category`) and the instance `Cont : Category Container`.

**The headline:** all three category laws hold *definitionally* (`rfl`, axiom-free).
This is the payoff of getting the variance right (cf. `[[dcont-morphisms-are-cofunctors]]`):
composing shape maps is ordinary `id`/`∘`, which is unital + associative up to Lean's η for
functions and structures; the backward position maps inherit it. **No transports, no
`Ext.ext_eq`** — in deliberate contrast to the directed-container comonad laws
(`Directed.lean`), where positions live in different fibres and `Sigma` transports appear.
Worth a sentence in the book: "Cont's laws are definitional; the *comonad* structure is
where the dependent content lives."

### Stretch goal (also DONE): binary coproduct
- `Container.coprod C D` — shape `C.Shape ⊕ D.Shape`, positions `Sum.elim C.Pos D.Pos`.
- `Container.inl`, `Container.inr` — injections (identity on positions).
- `ContainerMorphism.desc φ ψ` (= copairing `[φ,ψ]`) — `Sum.elim` on shapes, `match` on
  positions.
- Universal property: `inl_desc`, `inr_desc` (computation rules, `rfl`) +
  `desc_eta` (η-rule: every `χ : C⊕D ⟶ E` is the copairing of its restrictions) +
  `desc_unique` (the explicit "unique mediating morphism" form). Together =
  `Hom (C⊕D) E ≃ Hom C E × Hom D E`.

## Reusable Lean techniques (logged for next lean session)

- **Morphism extensionality, two forms.**
  - `ContainerMorphism.ext` (HEq form): `onShapes` eq + `HEq onPos onPos` → eq. Proof:
    `cases hs; cases hp; rfl`.
  - `ContainerMorphism.ext'` (transport form, HEq-free, more usable): hypothesis
    `∀ s p, φ.onPos s p = ψ.onPos s (congrFun hs s ▸ p)`. Proof pattern: pattern-match both
    morphisms, `cases hs`, then `funext`×2. **Key fact:** when shape maps agree
    *definitionally*, `congrFun hs s ▸ p` is defeq to `p` by Lean 4's definitional proof
    irrelevance, so each pointwise goal closes by plain `rfl`. This is what makes the
    coproduct η-rule one-liner (`intro s p; cases s <;> rfl`). Prefer `ext'` over the HEq
    form whenever the shape maps coincide up to defeq.
- **`Function.hfunext` is Mathlib-only** — do NOT reach for it in this core-only project.
  The `ext'` transport trick replaces it.
- **`cases s` on a sum shape** works through the `Container.coprod` def
  (`(C.coprod D).Shape` unfolds to `C.Shape ⊕ D.Shape`), so `cases s <;> rfl` dispatches the
  `match`-based `onPos` without manual `Sum.elim` lemmas.

## Pushing (action for next WAKE session — out of scope for this lean session)

The file is written and verified locally but **not committed/pushed**. The local repo at
`~/projects/lean/Containers` currently shows ALL files untracked (`git status` = `??`
everywhere) — i.e. this checkout is not in sync with the versioned history on
`RaggedR/ghani-containers` where PRs #6/#8 live. **Before pushing, reconcile this**: either
this is a detached/fresh checkout that needs re-pointing at `origin`, or the Lean dir was
never actually committed and the prior "PR #8" lives only on the remote. Next wake:
1. `cd ~/projects/lean/Containers && git remote -v` / `git log` to see what state we're in.
2. Branch `lean-cont-category`, add `Containers/Cont.lean` + the one-line edit to
   `Containers.lean`, `gh pr create`. Title: "Lean: Cont as a category + binary coproduct".
3. Flag to Neil in the morning email (book Ch 2 backbone now machine-checked).

## Grant relevance

"The category of containers, machine-checked" is a clean grant deliverable and the Lean
foundation the book's Ch 2 rests on. Once merged, `Cofunctor.lean` (M4) and the
directed-container comonad (`Directed.lean`) sit on top as the comonoid objects — unifying
the Lean development around `Cont`, mirroring the book's structure. The coproduct serves
Ch 3 (algebra of container constructors).

## Not done / possible next Lean targets

- **Product** of containers in Cont (the *other* universal construction): shape `S × T`,
  positions `P s ⊕ Q t`. Dual to the coproduct; would round out Ch 3. (Note: this is the
  categorical product in Cont, distinct from the Dirichlet/composition products.)
- **Functor `Ext : Cont ⟶ [Type, Type]`** — extension is functorial in the container; the
  representation theorem in `Basic.lean` (`toExtNatTrans`/`toMorphism` bijection) is the
  fully-faithful witness. Packaging it as a functor into `Type → Type` natural transformations
  would be the next structural milestone.
- A clean Mathlib `Cofunctor` contribution (carried over from the ZS-assoc note).
