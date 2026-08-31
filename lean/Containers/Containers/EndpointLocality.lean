import Containers.DContCat
import Containers.StateComonad

/-!
# Endpoint locality: a functor out of the codiscrete category is a trivial iso-system

This file formalises the reusable abstract engine of the "liftings ≅ Cat"
completeness proofs (MacBeth, prove notes `2026-08-11-state-liftings-holonomy-triviality.md`
and `2026-08-11-update-monad-liftings-holonomy-full.md`, §4(B)): the *collapse*
mechanism that both the Reader/State classifications and the cross-domain
"trivial holonomy ⟹ one global object" pattern (Categorical Belief Propagation,
Thm 6.14) share.

## The statement

Let `K(S)` be the **codiscrete** (a.k.a. chaotic / indiscrete) category on a
type `S`: objects are elements of `S`, and there is **exactly one** morphism
`a ⟶ b` for every ordered pair `(a, b)` (`Hom a b := PUnit`). Let `C` be any
small category and `F : K(S) ⥤ C` a functor. Then:

1. `F` sends **every** morphism to an **isomorphism** (`mapIso`,
   `mapIso_hom_eq`): the unique arrow `b ⟶ a` provides the inverse, because in
   `K(S)` every composite `a ⟶ b ⟶ a` is the identity.
2. Hence a **coherent iso-system** `ι a b : F.obj a ≅ F.obj b` (`endpointIso`)
   with `ι a a = id` (`endpointIso_refl`) and `ι a b ⬝ ι b c = ι a c`
   (`endpointIso_comp`) — the *trivial holonomy* datum.
3. **Collapse:** every `F.obj a` is isomorphic to a single object `F.obj a₀`
   (`collapse`), so a classification that factors through `K(S)` collapses to a
   single category — `π₀(K(S)) = 1`.

The codiscrete category is precisely `deltaDC S` under the Ahman–Chapman–Uustalu
correspondence DCont ≅ Cat (arXiv:1408.5809), formalised in
`Containers.StateComonad`; the specialisation `Codiscrete Bool` at the end
connects this abstract collapse to `StateProductLifting.lean`'s
`stateProduct = ΔBool × ℤ/2` (State's transport factors through `K(Bool)`).

Everything is `Type`-level, Lean 4 core, no Mathlib. `PUnit`'s definitional
eta keeps every coherence proof `rfl`-clean.
-/

namespace Containers

namespace SmallCat

/-- An **isomorphism** `a ≅ b` in a small category: a morphism with a two-sided
inverse. -/
structure Iso (C : SmallCat) (a b : C.Obj) where
  hom : C.Hom a b
  inv : C.Hom b a
  hom_inv : C.comp hom inv = C.id a
  inv_hom : C.comp inv hom = C.id b

/-- A **functor** between (hand-rolled) small categories: an object map and a
morphism map preserving identities and diagrammatic composition. -/
structure Functor (C D : SmallCat) where
  obj : C.Obj → D.Obj
  map : {a b : C.Obj} → C.Hom a b → D.Hom (obj a) (obj b)
  map_id : ∀ a : C.Obj, map (C.id a) = D.id (obj a)
  map_comp : ∀ {a b c : C.Obj} (f : C.Hom a b) (g : C.Hom b c),
    map (C.comp f g) = D.comp (map f) (map g)

end SmallCat

/-- The **codiscrete** (chaotic) category `K(S)` on a type `S`: one morphism
between any two objects. All category laws hold by `PUnit`-eta (`rfl`). -/
def Codiscrete (S : Type) : SmallCat where
  Obj := S
  Hom := fun _ _ => PUnit
  id := fun _ => PUnit.unit
  comp := fun _ _ => PUnit.unit
  id_comp := fun _ => rfl
  comp_id := fun _ => rfl
  assoc := fun _ _ _ => rfl

namespace SmallCat

variable {S : Type} {C : SmallCat} (F : Functor (Codiscrete S) C)

/-- **The endpoint iso-system.** For every ordered pair `a b : S`, the image
under `F` of the unique arrow `a ⟶ b` in `K(S)` is an isomorphism
`F.obj a ≅ F.obj b`, with inverse the image of the unique arrow `b ⟶ a`.

Both triangle identities reduce, via functoriality, to `F.map_id`: in `K(S)`
the round trip `a ⟶ b ⟶ a` *is* the identity at `a` (both are `PUnit.unit`). -/
def endpointIso (a b : S) : Iso C (F.obj a) (F.obj b) where
  hom := F.map (a := a) (b := b) PUnit.unit
  inv := F.map (a := b) (b := a) PUnit.unit
  hom_inv :=
    (F.map_comp (a := a) (b := b) (c := a) PUnit.unit PUnit.unit).symm.trans
      (F.map_id a)
  inv_hom :=
    (F.map_comp (a := b) (b := a) (c := b) PUnit.unit PUnit.unit).symm.trans
      (F.map_id b)

/-- **(1) Every morphism is sent to an isomorphism.** Since `K(S)` has a unique
arrow `a ⟶ b`, its image is exactly `endpointIso F a b`. -/
def mapIso {a b : S} (_ : (Codiscrete S).Hom a b) : Iso C (F.obj a) (F.obj b) :=
  endpointIso F a b

/-- The witnessing iso's forward map is literally `F.map f`. -/
theorem mapIso_hom_eq {a b : S} (f : (Codiscrete S).Hom a b) :
    (mapIso F f).hom = F.map f := rfl

/-- **(2a) Reflexivity of the iso-system:** `ι a a` is the identity. -/
theorem endpointIso_refl (a : S) : (endpointIso F a a).hom = C.id (F.obj a) :=
  F.map_id a

/-- **(2b) Coherence of the iso-system:** `ι a b ⬝ ι b c = ι a c`. The composite
of the two forward maps is the forward map of `endpointIso F a c`, because in
`K(S)` the composite `a ⟶ b ⟶ c` is the unique arrow `a ⟶ c`. -/
theorem endpointIso_comp (a b c : S) :
    C.comp (endpointIso F a b).hom (endpointIso F b c).hom
      = (endpointIso F a c).hom :=
  (F.map_comp (a := a) (b := b) (c := c) PUnit.unit PUnit.unit).symm

/-- **(3) Collapse.** Every object in the image of `F` is isomorphic to a single
chosen object `F.obj a₀`; the classification through `K(S)` has `π₀ = 1`. -/
def collapse (a₀ a : S) : Iso C (F.obj a) (F.obj a₀) :=
  endpointIso F a a₀

end SmallCat

/-! ## Specialisation: State's transport factors through `K(Bool)`

`StateProductLifting.lean` builds the sound half of the State classification as
`stateProduct = ΔBool × ℤ/2`, whose state factor `ΔBool` is the codiscrete
directed container `deltaDC Bool` (`Containers.StateComonad`). Under DCont ≅ Cat
that directed container **is** `Codiscrete Bool`, so State's transport — a functor
out of it into any fibre category — is a trivial iso-system by `collapse`: both
states `false`, `true` name the same object up to canonical iso. -/

/-- The State transport on `Bool` collapses: for any fibre category `C` and any
functor `F : K(Bool) ⥤ C`, the two states are canonically isomorphic. This is
the concrete `π₀(K(Bool)) = 1` witnessed at `StateProductLifting`'s `S = Bool`. -/
example {C : SmallCat} (F : SmallCat.Functor (Codiscrete Bool) C) :
    SmallCat.Iso C (F.obj false) (F.obj true) :=
  SmallCat.endpointIso F false true

end Containers
