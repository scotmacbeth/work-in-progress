# Lean: binary product of containers in Cont

Target: add `Container.prod`, `Container.fst`, `Container.snd`,
`ContainerMorphism.pair` + universal property to `Cont.lean`.
Dual of the coproduct already there. Pure Lean 4 core, no Mathlib.

## Definitions
- prod C D: Shape = C.Shape × D.Shape, Pos (s,t) = C.Pos s ⊕ D.Pos t.
- fst : prod ⟶ C: onShapes = Prod.fst, onPos = fun _ => Sum.inl
  (onPos type: C.Pos st.1 → C.Pos st.1 ⊕ D.Pos st.2 — injection backward ✓)
- snd : prod ⟶ D: onShapes = Prod.snd, onPos = fun _ => Sum.inr
- pair f g (f:R⟶C, g:R⟶D) : R ⟶ prod:
  onShapes r = (f.onShapes r, g.onShapes r)
  onPos r = Sum.elim (f.onPos r) (g.onPos r)
  (type: C.Pos(f r) ⊕ D.Pos(g r) → R.Pos r ✓)

## Computation rules — expect rfl (dual of inl_desc/inr_desc)
- pair f g ≫ fst = f:
  onShapes: r ↦ Prod.fst (f r, g r) = f r  [proj of ctor, +eta] rfl
  onPos: Sum.elim (f.onPos r) (g.onPos r) ∘ Sum.inl = f.onPos r  [iota+eta] rfl
- pair f g ≫ snd = g: dual rfl

## Uniqueness — pair_eta needs ext' (Sum has no defeq eta)
χ : R ⟶ prod ⟹ pair (χ≫fst) (χ≫snd) = χ
- shapes: (fst(χ r), snd(χ r)) = χ r by Prod structure eta (rfl per component)
- pos: Sum.elim (χ.onPos r ∘ inl) (χ.onPos r ∘ inr) = χ.onPos r
  NOT rfl (no Sum eta) → use ext', cases p <;> rfl
  transport trivial because shape maps agree definitionally (proof irrel).

## pair_unique: subst h₁ h₂; exact (pair_eta χ).symm  (dual of desc_unique)
