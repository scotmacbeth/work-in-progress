# Lean: Monoidal coherence of (Cont, ◁, I) — pentagon + triangle

Source proof: `~/projects/proofs/2026-06-13-monoidal-coherence-four-structures.tex` Part (A).
Base: `Composition.lean` (PR #13) — has `comp` (◁), `I`, `leftUnitor`, `rightUnitor`,
`associator` (all `ContainerIso`, transport-free). `Cont.lean` has `ContainerMorphism`,
`.comp`, `.id`, `ext'`, hand-rolled `Category`.

## Dependency audit
- NO Mathlib. Pure Lean 4 core. So NO `CategoryTheory.MonoidalCategory` — cannot use it
  without pulling Mathlib (repo deliberately Mathlib-free, mirrors `Category` by hand).
  ⇒ Prove pentagon + triangle as standalone equalities of `.hom` morphisms, mirroring
  how `Cont.lean` hand-rolls `Category`. Optionally bundle a minimal `MonoidalCategory`
  hand-rolled class at the end if clean.
- Need: bifunctorial action of ◁ on morphisms `comp₂ : (G⟶G') → (F⟶F') → (G◁F ⟶ G'◁F')`,
  then whiskerings `whiskerLeft G ν = comp₂ (id G) ν`, `whiskerRight μ F = comp₂ μ (id F)`.
- `◁` = `Container.comp G F`, G OUTER, F INNER. Matches tex `C1 ◁ C2` (C1 outer).
- associator H G F : ((H◁G)◁F) ≅ (H◁(G◁F)).

## comp₂ worked out (transport-free, see tex §whisker)
onShapes (t,f) = ⟨μ.s t, fun q' => ν.s (f (μ.p t q'))⟩
onPos (t,f) ⟨q',r'⟩ = ⟨μ.p t q', ν.p (f (μ.p t q')) r'⟩
fibre check OK.

## Pentagon statement (diagrammatic comp; a then b = a.comp b)
a = whiskerRight α123 C4 : ((C1◁C2)◁C3)◁C4 ⟶ (C1◁(C2◁C3))◁C4
b = α_{1,(23),4}        : (C1◁(C2◁C3))◁C4 ⟶ C1◁((C2◁C3)◁C4)
c = whiskerLeft C1 α234 : C1◁((C2◁C3)◁C4) ⟶ C1◁(C2◁(C3◁C4))
d = α_{(12),3,4}        : ((C1◁C2)◁C3)◁C4 ⟶ (C1◁C2)◁(C3◁C4)
e = α_{1,2,(34)}        : (C1◁C2)◁(C3◁C4) ⟶ C1◁(C2◁(C3◁C4))
GOAL: (a.comp b).comp c = d.comp e

## Triangle
GOAL: (associator C1 I C2).hom.comp (whiskerLeft C1 (leftUnitor C2).hom)
        = whiskerRight (rightUnitor C1).hom C2
   : (C1◁I)◁C2 ⟶ C1◁C2

## Strategy
Everything transport-free ⇒ try `ext'` + `rcases` shape/pos + `rfl`, like associator's
hom_inv proof. If shapes defeq, shape-eq hyp is `rfl`.

## Log

### RESULT — SUCCESS (2026-06-13)
- Toolchain not installed at session start; installed elan + lean v4.30.0 (repo is pure
  Lean core, NO Mathlib, so no `cache get`). Baseline + full build pass.
- comp₂, whiskerings, comp₂_id, comp₂_comp: all `rfl`.
- associator/leftUnitor/rightUnitor naturality: all `rfl`.
- pentagon, triangle: all `rfl` (better than the predicted "Quot.sound of a Sigma
  rearrangement" — the coherence STEP is pure defeq).
- Bundled minimal hand-rolled `MonoidalCategory` class (extends `Category`) + `CatIso`
  + `ContainerIso.toCatIso` coercion + instance `ContMonoidal`. Every field rfl/proven.
- Gotcha: class field `tensorHom_comp` arg order is (f₁ g₁ f₂ g₂) = (μ μ' ν ν'); my
  `comp₂_comp` takes (μ μ' ν ν') too — first wired (f₁ f₂ g₁ g₂), fixed to (f₁ g₁ f₂ g₂).
- #print axioms: pentagon/triangle/ContMonoidal depend ONLY on Quot.sound (via funext,
  inherited from Composition.lean's iso-law proofs). comp₂_comp: no axioms. No sorry.
- Zero warnings. PR #17 (base lean-composition-product / PR #13), fork scotmacbeth.
