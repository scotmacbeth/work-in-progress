import Containers.Sequential

/-!
# The `∏`/`All` predicate lifting as a cartesian-only action of `◁`

This file formalises the **action law** of Neil Ghani's `All` predicate lifting
over the composition product `◁`, answering his UID-94 note (2026-08-08). The
informal proof is `~/projects/proofs/2026-08-08-A-E-predicate-liftings.md`
(node `neil-A-E-predicate-liftings` in `proofs/registry/effect-coeffect-arrows.json`).

## The two liftings

For a container `X = (S_X, P_X)` and a "predicate" container `Y = (S_Y, P_Y)`,
evaluated at `(s, g) ∈ ⟦X⟧ S_Y` (so `s : S_X`, `g : P_X s → S_Y`), Neil's two
canonical predicate liftings are

```
All    X Y (s, g) = ∏_{p : P_X s} P_Y (g p)      (`∏`, "for all positions")
Exists X Y (s, g) = Σ_{p : P_X s} P_Y (g p)      (`Σ`, proof-relevant)
```

Packaged as bifunctors `Cont × Cont → Cont` (same shapes `Σ_s S_Y^{P_X s}`,
differing on positions):

* `E X Y = (⟦X⟧ S_Y, Exists X P_Y)` **is exactly the composition product**
  `X ◁ Y` (`Container.seq`): its positions `Σ_p P_Y(g p)` are the ◁-positions.
* `A X Y = (⟦X⟧ S_Y, All X P_Y)` (`Container.actionAll` below) uses `∏` on
  positions where `E` uses `Σ`.

## What is proved here

* **`Container.actionAll_assoc`** (P2 of the proof): the associativity / module
  law `A X (A Y C) ≅ A (X ◁ Y) C`, as a `ContainerIso`. On shapes it is the
  currying bijection of the ◁-associator; on positions it is dependent-product
  Fubini `∏_p ∏_q ≅ ∏_{(p,q)}`. Both round trips are transport-free (`rfl` after
  a `cases`), exactly as for `Container.associator`.
* **`Container.actionAll_unit`** (P2 unit): `A I C ≅ C`, a `Unit`-collapse
  mirroring `Container.leftUnitor`.
* **`Container.actionAll_snd`**: `A` is functorial in its **second** argument
  for *every* container morphism (the `ρ`-pointwise action of §2.1), witnessing
  the asymmetry — the first argument would need cartesian morphisms (P1),
  formalised as `T_M`-lifts-⟺-cartesian in `TMCartesianBoundary.lean`.

The statement is an **iso**, not a definitional equality: the two shape sets are
the curried/uncurried groupings of a nested dependent sum (genuinely bijective,
not defeq), matching the `ContainerIso` convention used for `◁`'s associator.

Everything is `Type`-level, Lean 4 core, no Mathlib — matching `Sequential.lean`.
-/

namespace Containers

/-! ## The `∏` / `All` predicate lifting as a bifunctor -/

/-- **The `All` (`∏`) predicate lifting**, packaged as a bifunctor
`A X Y : Cont × Cont → Cont`. A shape is an `X`-shape `s` with a labelling
`g : P_X s → S_Y` of its positions by `Y`-shapes (identical to `⟦X⟧ S_Y` and to
the shape of `X ◁ Y`); a **position** at `(s, g)` is a *dependent function*
`∏_{p : P_X s} P_Y (g p)` — one `Y`-position under *every* `X`-position. This is
where `A` differs from `E = ◁`, which uses the dependent *sum* `Σ` there. -/
def Container.actionAll (X Y : Container) : Container where
  Shape := (s : X.Shape) × (X.Pos s → Y.Shape)
  Pos := fun sg => (p : X.Pos sg.1) → Y.Pos (sg.2 p)

/-! ## The action / associativity law `A X (A Y C) ≅ A (X ◁ Y) C`

This is P2 of the proof. The shape bijection is the ◁-associator's currying
`k p = ⟨g p, fun q => m ⟨p, q⟩⟩`; on positions it is dependent-product Fubini,
`(∏_p ∏_q) ≅ ∏_{(p,q)}`, which is curry/uncurry of dependent functions and hence
`rfl` up to `Sigma`- and function-η. No transports appear, so — exactly as for
`Container.associator` — the round trips close by `cases` + `rfl`. -/

/-- **The action law** `A X (A Y C) ≅ A (X ◁ Y) C` (P2): `Container.actionAll`
is a left action / left module of the `◁`-monoidal structure `(Cont, ◁, I)` on
`Cont`. Forward: uncurry the inner shape assignment (`◁`-associator on shapes)
and *curry* the position dependent-function (Fubini `∏_{(p,q)} → ∏_p ∏_q`).
Backward: the inverses. Object-level (informal §3.1); as a *functorial* action it
lives on `Cont_cart × Cont` by P1 (`TMCartesianBoundary.lean`). -/
def Container.actionAll_assoc (X Y C : Container) :
    ContainerIso (X.actionAll (Y.actionAll C)) ((X ◁ Y).actionAll C) where
  hom :=
    { onShapes := fun sk => ⟨⟨sk.1, fun p => (sk.2 p).1⟩, fun r => (sk.2 r.1).2 r.2⟩
      onPos := fun _ σ p q => σ ⟨p, q⟩ }
  inv :=
    { onShapes := fun sgm => ⟨sgm.1.1, fun p => ⟨sgm.1.2 p, fun q => sgm.2 ⟨p, q⟩⟩⟩
      onPos := fun _ τ r => τ r.1 r.2 }
  hom_inv := by
    refine ContainerMorphism.ext' rfl ?_
    intro s p
    rcases s with ⟨s, k⟩
    rfl
  inv_hom := by
    refine ContainerMorphism.ext' rfl ?_
    intro s p
    rcases s with ⟨⟨s, g⟩, m⟩
    rfl

/-! ## The unit law `A I C ≅ C` -/

/-- **The unit law** `A I C ≅ C` (P2 unit). With `I = Unit ◁ (fun _ => Unit)`,
the shape `Σ (_ : Unit), (Unit → S_C)` collapses to `S_C` and the position
`∏_{p : Unit} P_C(g p)` collapses to `P_C(g ())`. A `Unit`-collapse mirroring
`Container.leftUnitor`; round trips by `rfl` (`Unit`- and `Sigma`-η). -/
def Container.actionAll_unit (C : Container) :
    ContainerIso (Container.I.actionAll C) C where
  hom :=
    { onShapes := fun sg => sg.2 ()
      onPos := fun _ c _ => c }
  inv :=
    { onShapes := fun s => ⟨(), fun _ => s⟩
      onPos := fun _ σ => σ () }
  hom_inv := rfl
  inv_hom := rfl

/-! ## Functoriality in the second argument (all morphisms)

The asymmetry of `A` (§2.1 of the proof): in the **second** argument `A` is
functorial for *every* container morphism `β : Y → Y'`. Its shape map reuses
the ◁-whiskering `(s, g) ↦ (s, β.onShapes ∘ g)`; on positions `β.onPos` acts
**inside each `∏`-factor, pointwise**, so it is always defined — no cartesian
hypothesis, in contrast to the first argument (P1). -/

/-- **Second-argument functoriality** of `A`: a morphism `β : Y ⟶ Y'` induces
`A X Y ⟶ A X Y'` for *every* `β` (no cartesian hypothesis). Shapes:
`(s, g) ↦ (s, β.onShapes ∘ g)`; positions: pull back pointwise inside each
`∏`-factor via `β.onPos`. -/
def Container.actionAll_snd (X : Container) {Y Y' : Container}
    (β : ContainerMorphism Y Y') :
    ContainerMorphism (X.actionAll Y) (X.actionAll Y') where
  onShapes := fun sg => ⟨sg.1, fun p => β.onShapes (sg.2 p)⟩
  onPos := fun sg τ p => β.onPos (sg.2 p) (τ p)

/-- Second-argument functoriality respects identities: `A X (id Y) = id`. -/
theorem Container.actionAll_snd_id (X Y : Container) :
    X.actionAll_snd (ContainerMorphism.id Y) = ContainerMorphism.id (X.actionAll Y) :=
  rfl

/-- Second-argument functoriality respects composition. -/
theorem Container.actionAll_snd_comp (X : Container) {Y Y' Y'' : Container}
    (β : ContainerMorphism Y Y') (γ : ContainerMorphism Y' Y'') :
    X.actionAll_snd (β.comp γ) = (X.actionAll_snd β).comp (X.actionAll_snd γ) :=
  rfl

end Containers
