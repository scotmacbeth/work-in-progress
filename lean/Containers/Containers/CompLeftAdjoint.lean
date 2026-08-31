import Containers.Monoidal

/-!
# The left adjoint to `(−) ◁ q`

This file builds on `Containers.Monoidal`. For a fixed container `q = (T ◁ Q)` write
`L_q p := p ◁ q` (`Container.seq p q`) for the endofunctor of `Cont` given by sequential
composition with `q` on the inside. This file exhibits an explicit **left adjoint**

    F_q (R ◁ U) = (R ◁ fun ρ => ⟦q⟧ (U ρ)),   where `⟦q⟧ X = Σ t : T, (Q t → X)`,

i.e. `F_q` is the *identity on shapes* and applies the extension of `q` to every position
set. We give the object map (`Container.leftAdj`), the action on morphisms
(`Container.leftAdjMap`) together with its functor laws, the unit and counit as explicit
container morphisms, and the two triangle identities. As a corollary we package the
hom-set bijection `Cont(F_q r, p) ≃ Cont(r, p ◁ q)` as a pair of mutually inverse
transposition maps.

**Where the content is.** The informal argument is a two-line Yoneda computation ("every
container is a coproduct of representables `y^U`, and `Cont(y^U, p ◁ q) ≅ Cont(y^{⟦q⟧ U},
p)`"), which hides the only step that can go wrong: a `ContainerMorphism` is forward on
shapes and **backward** on positions, so the action of `F_q` on morphisms must run `⟦q⟧`
over the *backward* leg — `Ext.map (φ.onPos ρ) : ⟦q⟧ (U' (h ρ)) → ⟦q⟧ (U ρ)`. Pushing
`⟦q⟧` forwards, as a shape-level reading of the formula suggests, does not even typecheck.
That variance is what this file certifies.

Everything is `Type`-level, Lean 4 core, no Mathlib — matching `Monoidal.lean`. All laws
below hold by `rfl` on shapes and pointwise `rfl` on positions: no transport appears,
because the fibres on the two sides of each triangle agree definitionally.

## References

The functor `F_q` is not new. It is Niu–Spivak, *Polynomial Functors: A Mathematical
Theory of Interaction* (arXiv:2312.00990), Definition 6.59 — the "left coclosure"
`⌜q/p⌝ := Σ_{i ∈ p(1)} y^{q(p[i])}` — used there in Proposition 6.68; the same object
appears in Ahman–Uustalu's coclosure work and in Spivak, arXiv:2202.00534 §5. See
`proofs/2026-08-30-pra-vs-probe-method.md` §4.2–§4.4 for the informal proof formalised
here and §7 for the attribution audit.
-/

namespace Containers

/-! ## The functor `F_q` -/

/-- The **left adjoint** `F_q r` to `(−) ◁ q`, on objects: identity on shapes, and on each
position set apply the extension `⟦q⟧`. Explicitly, a position of `F_q r` over the shape
`ρ` is a `q`-shape `t` together with a labelling of `Q t` by `r`-positions over `ρ`. -/
def Container.leftAdj (q r : Container) : Container where
  Shape := r.Shape
  Pos := fun ρ => Ext q (r.Pos ρ)

/-- The action of `F_q` on morphisms. On shapes it is `φ` unchanged; on positions it is
`⟦q⟧` applied to `φ`'s **backward** position map, which is the only way the types can fit:
`φ.onPos ρ : r'.Pos (φ.onShapes ρ) → r.Pos ρ`, hence
`Ext.map (φ.onPos ρ) : ⟦q⟧ (r'.Pos (φ.onShapes ρ)) → ⟦q⟧ (r.Pos ρ)`. -/
def Container.leftAdjMap (q : Container) {r r' : Container}
    (φ : ContainerMorphism r r') :
    ContainerMorphism (Container.leftAdj q r) (Container.leftAdj q r') where
  onShapes := φ.onShapes
  onPos := fun ρ => Ext.map (φ.onPos ρ)

/-- `F_q` preserves identities. -/
theorem Container.leftAdjMap_id (q r : Container) :
    Container.leftAdjMap q (ContainerMorphism.id r)
      = ContainerMorphism.id (Container.leftAdj q r) :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-- `F_q` preserves composition. Note the backward legs compose in the opposite order, and
`Ext.map` is functorial there, so the two sides agree pointwise by `rfl`. -/
theorem Container.leftAdjMap_comp (q : Container) {r r' r'' : Container}
    (φ : ContainerMorphism r r') (ψ : ContainerMorphism r' r'') :
    Container.leftAdjMap q (φ.comp ψ)
      = (Container.leftAdjMap q φ).comp (Container.leftAdjMap q ψ) :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-! ## Unit and counit -/

/-- The **unit** `η_r : r ⟶ F_q r ◁ q`, the "generic element" map. A shape of `F_q r ◁ q`
over `ρ` is a choice of `q`-shape for every position of `F_q r` at `ρ`, i.e. for every
`w = (t, k) : ⟦q⟧ (r.Pos ρ)`; the generic such choice is the first projection `w ↦ t`.
Backwards, a position is a pair `(w, z)` with `z : Q w.1`, and we *evaluate*: `w.2 z`. -/
def Container.adjUnit (q r : Container) :
    ContainerMorphism r (Container.seq (Container.leftAdj q r) q) where
  onShapes := fun ρ => ⟨ρ, fun w => w.1⟩
  onPos := fun _ z => z.1.2 z.2

/-- The **counit** `ε_p : F_q (p ◁ q) ⟶ p`. A shape of `F_q (p ◁ q)` is a shape `(s, c)` of
`p ◁ q`; forget the inner assignment `c`. Backwards, a position `a : p.Pos s` must be sent
to an element of `⟦q⟧ (Σ a' : p.Pos s, Q (c a'))`; take the `q`-shape `c a` sitting at `a`
together with the coproduct injection `ι_a : Q (c a) → Σ a', Q (c a')`. -/
def Container.adjCounit (q p : Container) :
    ContainerMorphism (Container.leftAdj q (Container.seq p q)) p where
  onShapes := fun sc => sc.1
  onPos := fun sc a => ⟨sc.2 a, fun z => ⟨a, z⟩⟩

/-! ## The triangle identities

These are the substantive content: they say `η` and `ε` really do exhibit `F_q ⊣ L_q`,
rather than merely being maps of the right type. -/

/-- **First triangle identity**: `ε_{F_q r} ∘ F_q η_r = id`. On shapes, `ρ ↦ (ρ, fst) ↦ ρ`.
On positions, `ε` sends `w = (t, k)` to `(t, fun z => (w, z))` and then `⟦q⟧` of the
evaluation map `η♯` reads `k` back off, returning `(t, k) = w`. -/
theorem Container.triangle_leftAdj (q r : Container) :
    (Container.leftAdjMap q (Container.adjUnit q r)).comp
        (Container.adjCounit q (Container.leftAdj q r))
      = ContainerMorphism.id (Container.leftAdj q r) :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-- **Second triangle identity**: `(ε_p ◁ q) ∘ η_{p ◁ q} = id`. On shapes, `(s, c)` goes to
`((s, c), fst)` and back to `(s, fun a => (c a, ι_a).1) = (s, c)`. On positions, `(a, z)`
goes to `((c a, ι_a), z)` and evaluation returns `ι_a z = (a, z)`. -/
theorem Container.triangle_seq (q p : Container) :
    (Container.adjUnit q (Container.seq p q)).comp
        (Container.whiskerRight (Container.adjCounit q p) q)
      = ContainerMorphism.id (Container.seq p q) :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-! ## `L_q` is a functor

`L_q p = p ◁ q` acts on morphisms by right whiskering. Its functor laws are immediate from
bifunctoriality of `◁` (`Container.seq₂_id`, `Container.seq₂_comp`), recorded here so that the
naturality statements below are statements about *functors*, not just about families. -/

/-- `L_q` preserves identities. -/
theorem Container.whiskerRight_id (p q : Container) :
    Container.whiskerRight (ContainerMorphism.id p) q
      = ContainerMorphism.id (Container.seq p q) :=
  Container.seq₂_id p q

/-- `L_q` preserves composition. -/
theorem Container.whiskerRight_comp {p p' p'' : Container} (φ : ContainerMorphism p p')
    (φ' : ContainerMorphism p' p'') (q : Container) :
    Container.whiskerRight (φ.comp φ') q
      = (Container.whiskerRight φ q).comp (Container.whiskerRight φ' q) :=
  Container.seq₂_comp φ φ' (ContainerMorphism.id q) (ContainerMorphism.id q)

/-! ## Naturality of the unit and counit

The triangle identities in the previous section say that `η` and `ε` are compatible *pointwise*.
They do **not** say that `η` and `ε` are natural transformations, and without that the pair
`(η, ε)` is only a family of morphisms satisfying two equations, not an adjunction of functors.
The two squares below supply the missing content: `η : Id ⟹ L_q ∘ F_q` and
`ε : F_q ∘ L_q ⟹ Id`. Together with `leftAdjMap_id`/`leftAdjMap_comp`,
`whiskerRight_id`/`whiskerRight_comp` and the two triangles, this is the full definition of an
adjunction `F_q ⊣ L_q`.

Both squares again hold by `rfl` on shapes and pointwise `rfl` on positions. That is not
automatic: the naturality of `η` is where `F_q`'s backward action `Ext.map (φ.onPos ρ)`
has to cancel against the evaluation map, and it is only the *first projection* of `Ext.map` being
independent of the relabelling that makes the shape legs agree. -/

/-- **Naturality of the unit.** For `φ : r ⟶ r'`, the square

    r  --η_r--> F_q r ◁ q
    |                  |
    φ                  F_q φ ◁ q
    v                  v
    r' --η_{r'}-> F_q r' ◁ q

commutes. On shapes, both routes send `ρ` to `⟨φ ρ, fun w => w.1⟩`: going right-then-down applies
`Ext.map (φ.onPos ρ)` to `w`, which leaves the `q`-shape `w.1` untouched. On positions, both
routes evaluate. -/
theorem Container.adjUnit_naturality {r r' : Container} (q : Container)
    (φ : ContainerMorphism r r') :
    φ.comp (Container.adjUnit q r')
      = (Container.adjUnit q r).comp
          (Container.whiskerRight (Container.leftAdjMap q φ) q) :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-- **Naturality of the counit.** For `φ : p ⟶ p'`, the square

    F_q (p ◁ q)  --ε_p--> p
    |                     |
    F_q (φ ◁ q)           φ
    v                     v
    F_q (p' ◁ q) --ε_{p'}-> p'

commutes. On shapes both routes are `⟨s, c⟩ ↦ φ s`. On positions, at `a : p'.Pos (φ s)` both
routes give `⟨c (φ.onPos s a), fun z => ⟨φ.onPos s a, z⟩⟩` — the left-hand route because
`(φ ◁ q)`'s inner shape assignment is `c ∘ φ.onPos s` by definition of `seq₂`. -/
theorem Container.adjCounit_naturality {p p' : Container} (q : Container)
    (φ : ContainerMorphism p p') :
    (Container.leftAdjMap q (Container.whiskerRight φ q)).comp (Container.adjCounit q p')
      = (Container.adjCounit q p).comp φ :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-! ## Naturality of the transposition -/

/-! ## The hom-set bijection

Transposition across the adjunction, `Cont(F_q r, p) ≅ Cont(r, p ◁ q)`, together with both
round trips. This is equivalent to the triangle identities but is the form one cites. -/

/-- Left-to-right transposition `Cont(F_q r, p) → Cont(r, p ◁ q)`: `k ↦ (k ◁ q) ∘ η_r`. -/
def Container.adjTranspose (q : Container) {r p : Container}
    (k : ContainerMorphism (Container.leftAdj q r) p) :
    ContainerMorphism r (Container.seq p q) :=
  (Container.adjUnit q r).comp (Container.whiskerRight k q)

/-- Right-to-left transposition `Cont(r, p ◁ q) → Cont(F_q r, p)`: `m ↦ ε_p ∘ F_q m`. -/
def Container.adjUntranspose (q : Container) {r p : Container}
    (m : ContainerMorphism r (Container.seq p q)) :
    ContainerMorphism (Container.leftAdj q r) p :=
  (Container.leftAdjMap q m).comp (Container.adjCounit q p)

/-- One round trip: transposing and untransposing recovers the original map. -/
theorem Container.adjUntranspose_adjTranspose (q : Container) {r p : Container}
    (k : ContainerMorphism (Container.leftAdj q r) p) :
    Container.adjUntranspose q (Container.adjTranspose q k) = k :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-- The other round trip: untransposing and transposing recovers the original map. -/
theorem Container.adjTranspose_adjUntranspose (q : Container) {r p : Container}
    (m : ContainerMorphism r (Container.seq p q)) :
    Container.adjTranspose q (Container.adjUntranspose q m) = m :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-- **Naturality of the transposition in `p`** (the codomain of the untransposed map): for
`k : F_q r ⟶ p` and `φ : p ⟶ p'`, transposing `k ≫ φ` is the transpose of `k` followed by
`φ ◁ q`. -/
theorem Container.adjTranspose_naturality_right {r p p' : Container} (q : Container)
    (k : ContainerMorphism (Container.leftAdj q r) p) (φ : ContainerMorphism p p') :
    Container.adjTranspose q (k.comp φ)
      = (Container.adjTranspose q k).comp (Container.whiskerRight φ q) :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-- **Naturality of the transposition in `r`.** Since `Cont(F_q −, p)` is contravariant in `r`,
the square is indexed by `φ : r' ⟶ r`: transposing `F_q φ ≫ k` is `φ` followed by the transpose
of `k`. -/
theorem Container.adjTranspose_naturality_left {r r' p : Container} (q : Container)
    (φ : ContainerMorphism r' r) (k : ContainerMorphism (Container.leftAdj q r) p) :
    Container.adjTranspose q ((Container.leftAdjMap q φ).comp k)
      = φ.comp (Container.adjTranspose q k) :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

/-! ## Non-vacuity: two negative controls

Every law in this file is proved by `ContainerMorphism.ext' rfl (fun _ _ => rfl)`, which
invites the worry that the statements are vacuous. They are not, and the two controls below
delimit exactly what each family of laws does and does not test.

**Control 1 (recorded as a theorem, since it compiles).** Fix `qBool`, the container with one
shape and two positions, and perturb the counit by flipping the `qBool`-position it injects:
`ε'_p a := ⟨c a, fun z => ⟨a, !z⟩⟩`. A previous cycle showed this perturbation *breaks the
triangle identity* (`triangle_seq` fails on its position leg). Yet
`adjCounitPerturbed_naturality` below shows it still satisfies the **naturality** square, on the
nose. So naturality and the triangles are genuinely **independent probes** of the counit: neither
subsumes the other, and certifying only one leaves the other free to be wrong.

**Control 2 (a failure, hence recorded in prose).** Post-composing the unit square with the
nontrivial automorphism of `F_q r ◁ qBool` given by `⟨w, z⟩ ↦ ⟨w, !z⟩` backwards on positions
makes `adjUnit_naturality` fail — and it fails on the **position** leg, the shape leg still
discharging by `rfl`. So the naturality squares here do have content, and, as with the triangles,
that content is located in the positions: a shape-level argument certifies a wrong unit just as
happily. -/

/-- The container with one shape and two positions, used only for the negative controls. -/
def Container.qBool : Container where
  Shape := Unit
  Pos := fun _ => Bool

/-- A **perturbed counit** for `qBool`: inject at the correct position `a` but flip the
`qBool`-position. This is *not* the counit — it fails the triangle identity `triangle_seq`. -/
def Container.adjCounitPerturbed (p : Container) :
    ContainerMorphism (Container.leftAdj Container.qBool (Container.seq p Container.qBool)) p where
  onShapes := fun sc => sc.1
  onPos := fun sc a => ⟨sc.2 a, fun z => ⟨a, !z⟩⟩

/-- **Control 1.** The perturbed counit is still natural in `p`, even though it fails the
triangle identity. Naturality therefore does not detect this error, and the triangle identities
are not implied by naturality. -/
theorem Container.adjCounitPerturbed_naturality {p p' : Container} (φ : ContainerMorphism p p') :
    (Container.leftAdjMap Container.qBool
        (Container.whiskerRight φ Container.qBool)).comp (Container.adjCounitPerturbed p')
      = (Container.adjCounitPerturbed p).comp φ :=
  ContainerMorphism.ext' rfl (fun _ _ => rfl)

end Containers
