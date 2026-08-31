import Containers.Free

/-!
# The `Σ`-container lifting is `M ◁ −`: a `◁`-monoid makes it a monad on `Cont`

This file formalises the headline of `~/projects/proofs/2026-08-08-sigma-monad-is-triangle-monoid.md`
(node `sigma-monad-is-triangle-monoid` in `proofs/registry/effect-coeffect-arrows.json`,
Thm 3.1, direction `2 ⟹ 1`): the **`Σ`-container lifting** `T^Σ_M` of a container
`M` is nothing but **left `◁`-multiplication by `M`**,

    T^Σ_M (C) = M ◁ C            (`Container.sigmaLift_eq_seq`, Prop 2.1)

and consequently, whenever `M` carries a `◁`-monoid structure (a *container monad*,
`Container.Monoid M`), the endofunctor `T^Σ_M = M ◁ −` on `Cont` is a **monad**:
its unit and multiplication are `η_M` and `μ_M` whiskered by `C`, and the three
monad laws are exactly the `◁`-monoid unit/associativity laws whiskered by `C`
and glued with the monoidal coherence of `(Cont, ◁, I)` (which is transport-free
here, so every coherence step is `rfl`).

## What is proved

* **`Container.sigmaLift`** — the `Σ`-lifting written in the coordinates of the
  informal proof: shapes `M(S_C)` (= `⟦M⟧ C.Shape`), positions `∐_{b ∈ lv(m)} P_C(x_b)`.
  **`Container.sigmaLift_eq_seq`** proves `M.sigmaLift C = M ◁ C` — a definitional
  equality (Prop 2.1): once `M` is a container, its "leaves" are `M.Pos s` and the
  Σ-positions *are* the `◁`-positions.
* **`Container.sigmaUnit`, `Container.sigmaMult`** — `η^Σ_C = η_M ◁ C` (through the
  left unitor) and `μ^Σ_C = μ_M ◁ C` (through the associator).
* **`Container.sigmaUnit_natural`, `Container.sigmaMult_natural`** — `η^Σ`, `μ^Σ`
  are natural in `C`, i.e. `Id ⟹ T^Σ_M` and `T^Σ_M ∘ T^Σ_M ⟹ T^Σ_M` are natural
  transformations (both `rfl`, from bifunctoriality of `◁`).
* **`Container.sigma_monad_left_unit`, `..._right_unit`, `..._assoc`** — the three
  monad laws. Each reduces to the corresponding `◁`-monoid law of `M`
  (`hM.left_unit` / `hM.right_unit` / `hM.assoc`) whiskered by `C`, the remaining
  coherence bookkeeping (unitors, associator, pentagon, triangle, their inverse
  laws) being definitional in `Cont`.
* **`Container.sigmaMonad`** — the three laws packaged as a `Container.SigmaMonad`
  record: the machine-checked statement that `M ◁ −` is a monad on `Cont`.

This is the general theorem that subsumes the two bespoke per-monad rungs
(`Reader`, `State`) of the `Σ`-lifting story: they are the special cases where the
`◁`-monoid `M` is the diagonal comonad on `E` (Reader) or the store monad (State).

The construction is the classical "a monoid `A` in a monoidal category `(V,⊗,I)`
makes `A ⊗ −` a monad", specialised to `(V,⊗,I) = (Cont, ◁, I)`. The
provenance of the *identity* `T^Σ_M = M ◁ −` and the `◁`-monoid characterisation is
the proof file above; the monoidal category `(Cont, ◁, I)` and its coherence are
`Containers.Monoidal` (PR #17), and the `◁`-monoid structure is `Container.Monoid`
of `Containers.Free`.

Everything is `Type`-level, Lean 4 core, no Mathlib — matching the rest of the
development.
-/

namespace Containers

open Container

variable {M : Container} (hM : Container.Monoid M) (C : Container)

/-! ## Prop 2.1 — the `Σ`-lifting is `M ◁ −` -/

/-- **The `Σ`-container lifting** `T^Σ_M(C)`, in the coordinates of the informal
proof: a shape is an `M`-shape `s` with a labelling `g : M.Pos s → C.Shape` of its
leaves by `C`-shapes (this is `⟦M⟧ C.Shape = M(S_C)`); a position at `(s, g)` is a
*dependent sum* `∐_{b : M.Pos s} C.Pos (g b)` — one `C`-position under *some*
leaf. This is where `Σ` differs from the `∏` predicate lifting `All`
(`Container.actionAll`), which uses the dependent product there. -/
def Container.sigmaLift (M C : Container) : Container where
  Shape := (s : M.Shape) × (M.Pos s → C.Shape)
  Pos := fun sg => (b : M.Pos sg.1) × C.Pos (sg.2 b)

/-- **Proposition 2.1**: the `Σ`-lifting *is* left `◁`-multiplication by `M`,
`T^Σ_M(C) = M ◁ C`. A definitional equality: shapes `M(S_C) = ⟦M⟧ S_C` are the
`◁`-shapes, and the `Σ`-positions `∐_{b} C.Pos (g b)` are the `◁`-positions. Once
`M` is a container, its "leaves" at `m = (s, g)` are `M.Pos s`, so the informal
leaf-indexed sum is literally the composite-polynomial position sum. -/
theorem Container.sigmaLift_eq_seq (M C : Container) : M.sigmaLift C = M ◁ C := rfl

/-! ## The monad structure maps `η^Σ = η_M ◁ −` and `μ^Σ = μ_M ◁ −` -/

/-- **The `Σ`-lifting unit** `η^Σ_C : C ⟶ M ◁ C`. It is `η_M` whiskered by `C`,
read through the left unitor: `C ≅ I ◁ C ⟶ M ◁ C`. -/
def Container.sigmaUnit : ContainerMorphism C (M ◁ C) :=
  (Container.leftUnitor C).inv.comp (Container.whiskerRight hM.unit C)

/-- **The `Σ`-lifting multiplication** `μ^Σ_C : M ◁ (M ◁ C) ⟶ M ◁ C`. It is `μ_M`
whiskered by `C`, read through the associator:
`M ◁ (M ◁ C) ≅ (M ◁ M) ◁ C ⟶ M ◁ C`. -/
def Container.sigmaMult : ContainerMorphism (M ◁ (M ◁ C)) (M ◁ C) :=
  (Container.associator M M C).inv.comp (Container.whiskerRight hM.mult C)

/-! ## Naturality: `η^Σ` and `μ^Σ` are natural transformations

`T^Σ_M = M ◁ −` is an endofunctor of `Cont` (its action on morphisms is
`Container.whiskerLeft M`). The families `η^Σ` and `μ^Σ` are natural in `C` — the
naturality squares hold by `rfl`, from the bifunctoriality of `◁` and naturality
of the structural isomorphisms. -/

/-- **Naturality of `η^Σ`**: `η^Σ` is a natural transformation `Id ⟹ M ◁ −`. For
`f : C ⟶ D`, `f ; η^Σ_D = η^Σ_C ; (M ◁ f)`. -/
theorem Container.sigmaUnit_natural {C D : Container} (f : ContainerMorphism C D) :
    f.comp (Container.sigmaUnit hM D)
      = (Container.sigmaUnit hM C).comp (Container.whiskerLeft M f) := rfl

/-- **Naturality of `μ^Σ`**: `μ^Σ` is a natural transformation
`(M ◁ −) ∘ (M ◁ −) ⟹ M ◁ −`. For `f : C ⟶ D`,
`(M ◁ (M ◁ f)) ; μ^Σ_D = μ^Σ_C ; (M ◁ f)`. -/
theorem Container.sigmaMult_natural {C D : Container} (f : ContainerMorphism C D) :
    (Container.whiskerLeft M (Container.whiskerLeft M f)).comp (Container.sigmaMult hM D)
      = (Container.sigmaMult hM C).comp (Container.whiskerLeft M f) := rfl

/-! ## The three monad laws

Each law reduces to the corresponding `◁`-monoid law of `M`, whiskered by `C`. The
whiskered law `hL`/`hR`/`hA` is `congrArg (whiskerRight · C)` of the monoid law
(using that `whiskerRight` is `rfl`-functorial). The surrounding coherence — the
unitors, the associator, the pentagon, the triangle, and their inverse laws — is
definitional in `Cont`, so the `calc` steps that are not the monoid rewrite close
by `rfl`. -/

/-- **Monad left-unit law** `η^Σ_{TC} ; μ^Σ_C = id`. Reduces to `M`'s left `◁`-unit
law `hM.left_unit` (whiskered by `C`) glued with the coherence
`λ⁻¹ ; (η ◁ −) ; α⁻¹ = (λ⁻¹_M ◁ C) ; ((η ◁ M) ◁ C)` and `(leftUnitor M).inv_hom`. -/
theorem Container.sigma_monad_left_unit :
    (Container.sigmaUnit hM (M ◁ C)).comp (Container.sigmaMult hM C)
      = ContainerMorphism.id (M ◁ C) := by
  have hL : (Container.whiskerRight (Container.seq₂ hM.unit (ContainerMorphism.id M)) C).comp
              (Container.whiskerRight hM.mult C)
            = Container.whiskerRight (Container.leftUnitor M).hom C :=
    congrArg (fun φ => Container.whiskerRight φ C) hM.left_unit
  calc (Container.sigmaUnit hM (M ◁ C)).comp (Container.sigmaMult hM C)
        = (Container.whiskerRight (Container.leftUnitor M).inv C).comp
            ((Container.whiskerRight (Container.seq₂ hM.unit (ContainerMorphism.id M)) C).comp
              (Container.whiskerRight hM.mult C)) := rfl
    _ = (Container.whiskerRight (Container.leftUnitor M).inv C).comp
            (Container.whiskerRight (Container.leftUnitor M).hom C) := by rw [hL]
    _ = Container.whiskerRight
            ((Container.leftUnitor M).inv.comp (Container.leftUnitor M).hom) C := rfl
    _ = Container.whiskerRight (ContainerMorphism.id M) C := by
          rw [(Container.leftUnitor M).inv_hom]
    _ = ContainerMorphism.id (M ◁ C) := rfl

/-- **Monad right-unit law** `(T η^Σ_C) ; μ^Σ_C = id`. Reduces to `M`'s right
`◁`-unit law `hM.right_unit` (whiskered by `C`) glued with the triangle identity,
`(associator M I C).inv_hom` and `(leftUnitor C).inv_hom`. -/
theorem Container.sigma_monad_right_unit :
    (Container.whiskerLeft M (Container.sigmaUnit hM C)).comp (Container.sigmaMult hM C)
      = ContainerMorphism.id (M ◁ C) := by
  have hR : (Container.whiskerRight (Container.seq₂ (ContainerMorphism.id M) hM.unit) C).comp
              (Container.whiskerRight hM.mult C)
            = Container.whiskerRight (Container.rightUnitor M).hom C :=
    congrArg (fun φ => Container.whiskerRight φ C) hM.right_unit
  calc (Container.whiskerLeft M (Container.sigmaUnit hM C)).comp (Container.sigmaMult hM C)
        = (Container.whiskerLeft M (Container.leftUnitor C).inv).comp
            ((Container.associator M Container.I C).inv.comp
              ((Container.whiskerRight (Container.seq₂ (ContainerMorphism.id M) hM.unit) C).comp
                (Container.whiskerRight hM.mult C))) := rfl
    _ = (Container.whiskerLeft M (Container.leftUnitor C).inv).comp
            ((Container.associator M Container.I C).inv.comp
              (Container.whiskerRight (Container.rightUnitor M).hom C)) := by rw [hR]
    _ = ContainerMorphism.id (M ◁ C) := rfl

/-- **Monad associativity law** `(T μ^Σ_C) ; μ^Σ_C = μ^Σ_{TC} ; μ^Σ_C`. Reduces to
`M`'s `◁`-associativity `hM.assoc` (whiskered by `C`) glued with the pentagon and
the inverse associator laws. -/
theorem Container.sigma_monad_assoc :
    (Container.whiskerLeft M (Container.sigmaMult hM C)).comp (Container.sigmaMult hM C)
      = (Container.sigmaMult hM (M ◁ C)).comp (Container.sigmaMult hM C) := by
  -- `M`'s `◁`-associativity, whiskered by `C` (functoriality of `whiskerRight` is `rfl`,
  -- so the reassociated composite form is defeq to `congrArg (whiskerRight · C) hM.assoc`).
  have hA : (Container.whiskerRight (Container.seq₂ hM.mult (ContainerMorphism.id M)) C).comp
              (Container.whiskerRight hM.mult C)
            = (Container.whiskerRight (Container.associator M M M).hom C).comp
                ((Container.whiskerRight (Container.seq₂ (ContainerMorphism.id M) hM.mult) C).comp
                  (Container.whiskerRight hM.mult C)) :=
    congrArg (fun φ => Container.whiskerRight φ C) hM.assoc
  -- Both sides normalise (associator naturality, all `rfl`) to a common tail carrying
  -- `μ_M`; the pure-associator prefixes coincide by the pentagon (`rfl`), and `hA` bridges
  -- the two orderings of the two `μ_M`'s.
  calc (Container.whiskerLeft M (Container.sigmaMult hM C)).comp (Container.sigmaMult hM C)
        = ((Container.associator M M (M ◁ C)).inv.comp
              (Container.associator (M ◁ M) M C).inv).comp
            ((Container.whiskerRight (Container.associator M M M).hom C).comp
              ((Container.whiskerRight (Container.seq₂ (ContainerMorphism.id M) hM.mult) C).comp
                (Container.whiskerRight hM.mult C))) := rfl
    _ = ((Container.associator M M (M ◁ C)).inv.comp
              (Container.associator (M ◁ M) M C).inv).comp
            ((Container.whiskerRight (Container.seq₂ hM.mult (ContainerMorphism.id M)) C).comp
              (Container.whiskerRight hM.mult C)) := by rw [← hA]
    _ = (Container.sigmaMult hM (M ◁ C)).comp (Container.sigmaMult hM C) := rfl

/-! ## Packaging: `M ◁ −` is a monad on `Cont` -/

/-- A **monad on `Cont`** carried by `M ◁ −`, in the minimal data needed to record
the theorem: the unit and multiplication families and the three laws. (A
lightweight record mirroring `Container.Monoid`; naturality of the families is
`Container.sigmaUnit_natural` / `Container.sigmaMult_natural`.) -/
structure Container.SigmaMonad (M : Container) where
  /-- The unit `η^Σ_C : C ⟶ M ◁ C`, natural in `C`. -/
  unit : (C : Container) → ContainerMorphism C (M ◁ C)
  /-- The multiplication `μ^Σ_C : M ◁ (M ◁ C) ⟶ M ◁ C`, natural in `C`. -/
  mult : (C : Container) → ContainerMorphism (M ◁ (M ◁ C)) (M ◁ C)
  /-- Left-unit law. -/
  left_unit : ∀ C, (unit (M ◁ C)).comp (mult C) = ContainerMorphism.id (M ◁ C)
  /-- Right-unit law. -/
  right_unit : ∀ C, (Container.whiskerLeft M (unit C)).comp (mult C)
    = ContainerMorphism.id (M ◁ C)
  /-- Associativity law. -/
  assoc : ∀ C, (Container.whiskerLeft M (mult C)).comp (mult C)
    = (mult (M ◁ C)).comp (mult C)

/-- **The `Σ`-lifting monad**: every `◁`-monoid `M` makes `M ◁ −` a monad on
`Cont` (Thm 3.1, `2 ⟹ 1`). -/
def Container.sigmaMonad : Container.SigmaMonad M where
  unit := Container.sigmaUnit hM
  mult := Container.sigmaMult hM
  left_unit := Container.sigma_monad_left_unit hM
  right_unit := Container.sigma_monad_right_unit hM
  assoc := Container.sigma_monad_assoc hM

/-! ## Corollary: `Reader` as an instance (the diagonal `◁`-monoid on `E`)

`Reader E = y^E = (Unit, fun _ => E)` is the container whose extension is
`X ↦ X^E`. Its `◁`-monoid structure is the **diagonal comonad on the set `E`**:
the unit `η_M` is the unique map to `Unit` on positions, and the multiplication
`μ_M` has backward position map the diagonal `e ↦ (e, e)`. Feeding this monoid to
`Container.sigmaMonad` recovers the bespoke `reader_sigma_monad_lifting` rung as a
one-line specialisation — the `Σ`-lifting of Reader is `Reader ◁ −`, a monad
because Reader is a container monad. -/

/-- The **Reader container** `y^E = (Unit, fun _ => E)`: one shape, positions `E`.
Its extension is `X ↦ X^E`. -/
def Container.reader (E : Type) : Container where
  Shape := Unit
  Pos := fun _ => E

/-- The **diagonal `◁`-monoid on `E`** carried by `Container.reader E`. Unit:
the unique map on positions (`E → Unit`); multiplication: the diagonal
`e ↦ (e, e)` on positions. All three `◁`-monoid laws hold by `rfl` (`Unit`- and
`Sigma`-η with definitional `Unit` eta). This is the `◁`-monoid witness that makes
`T^Σ_{Reader} = Reader ◁ −` a monad. -/
def Container.readerMonoid (E : Type) : Container.Monoid (Container.reader E) where
  unit :=
    { onShapes := fun _ => ()
      onPos := fun _ _ => () }
  mult :=
    { onShapes := fun _ => ()
      onPos := fun _ e => ⟨e, e⟩ }
  left_unit := rfl
  right_unit := rfl
  assoc := rfl

/-- **Reader corollary** (subsumes the bespoke rung): the `Σ`-lifting of `Reader`
is the monad `Reader ◁ −` on `Cont`. A one-line specialisation of the general
theorem `Container.sigmaMonad` to the diagonal `◁`-monoid on `E`. -/
def Container.readerSigmaMonad (E : Type) :
    Container.SigmaMonad (Container.reader E) :=
  Container.sigmaMonad (Container.readerMonoid E)

/-! ## Corollary: `State` as an instance (the store `◁`-monoid on `S`)

`State S = (S → S) ◁ ... = (S^S, fun _ => S)` is the container whose extension is
`X ↦ (S → S × X)`: a shape is a state transition `t : S → S`, a leaf is a query
state `s : S`, labelled by the output at `s`. Its `◁`-monoid structure is the
**store / state monad**: the unit is the identity transition, and the
multiplication *threads* the state — the composite transition of `(t, g)` is
`s ↦ g s (t s)` and its backward leaf map is `s ↦ (s, t s)` (query outer at `s`,
inner at the threaded state `t s`). -/

/-- The **State container** `(S^S, fun _ => S)`: shapes are state transitions
`S → S`, positions are query states `S`. Its extension is `X ↦ (S → S × X)`. -/
def Container.state (S : Type) : Container where
  Shape := S → S
  Pos := fun _ => S

/-- The **store `◁`-monoid on `S`** carried by `Container.state S`. Unit: the
identity transition. Multiplication: threading — forward the composite transition
`s ↦ g s (t s)`, backward the leaf map `s ↦ (s, t s)`. All three `◁`-monoid laws
hold by `rfl` (function-, `Sigma`- and `Unit`-η). This is the `◁`-monoid witness
that makes `T^Σ_{State} = State ◁ −` a monad. -/
def Container.stateMonoid (S : Type) : Container.Monoid (Container.state S) where
  unit :=
    { onShapes := fun _ => fun s => s
      onPos := fun _ _ => () }
  mult :=
    { onShapes := fun tg => fun s => tg.2 s (tg.1 s)
      onPos := fun tg => fun s => ⟨s, tg.1 s⟩ }
  left_unit := rfl
  right_unit := rfl
  assoc := rfl

/-- **State corollary** (subsumes the bespoke rung): the `Σ`-lifting of `State` is
the monad `State ◁ −` on `Cont`. A one-line specialisation of the general theorem
`Container.sigmaMonad` to the store `◁`-monoid on `S`. -/
def Container.stateSigmaMonad (S : Type) :
    Container.SigmaMonad (Container.state S) :=
  Container.sigmaMonad (Container.stateMonoid S)

end Containers
