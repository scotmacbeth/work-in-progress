import Containers.Directed
import Containers.StateComonad
import Containers.ReaderGroupoidLifting

/-!
# The product of directed containers, and the store category `𝕊 × C`

This file certifies the **SOUND half** of the State-liftings classification
(MacBeth PROVE `proofs/2026-08-10-state-liftings-holonomy-free.md`, registry node
`state-grade-independence`; and `proofs/2026-08-11-state-liftings-holonomy-triviality.md`):

> **Every small category `C` yields a State proof-relevant monad lifting, via
> `C ↦ 𝕊 × C`**, where `𝕊` is the *store / costate category* — the codiscrete
> category `ΔS` on the state set `S` (already Lean-verified as `deltaDC` in
> `Containers.StateComonad`).

Under DCont ≅ Cat (Ahman–Chapman–Uustalu, *When is a container a comonad?*,
arXiv:1408.5809) a directed container **is** a small category, and the product of
directed containers realised below **is** the product category: objects are pairs
of objects, and a morphism out of `(s, t)` is a *pair* of morphisms — hence the
position fibre is a **product** `C.Pos s × D.Pos t` (contrast the categorical
product in `Cont`/`Poly`, `Container.prod` in `Containers.Cont`, whose fibre is a
*coproduct*). Composition, identities and codomains act componentwise.

## The reusable construction

`DirectedContainer.prod C D` (positions `C.Pos s × D.Pos t`) discharges D1–D5
componentwise. D1/D3/D4 are pairings of the factors' laws (`prodEq`); D2/D5 carry
a transport along a shape equality — handled once and for all by `transport_prod`,
which factors a transport over a *product of shapes* into the two component
transports (its proof is `subst` + definitional proof-irrelevance). Because the
comonad laws are already free from `Containers.Directed`, the product is
automatically a comonad — the State lifting attached to `𝕊 × C`.

## The distinguishing invariant (State vs Reader)

The classification separates the State side from the Reader side by `π₀`: the
store category `𝕊 = ΔS` is **codiscrete**, so *every* ordered pair of shapes is
connected by a morphism (`deltaDC_connected`) — a **single shape-orbit**,
`π₀(𝕊) = 1`. Reader's liftings instead have `π₀ = |E|` discrete components (a
morphism cannot change shape). We witness the single-orbit property for `ΔS` and,
for the concrete product `ΔBool × ℤ/2`, connectedness in the state coordinate.

## Concrete instance

`stateProduct := (deltaDC Bool).prod ReaderGroupoid.readerGroupoidLifting` — the
store category on two states crossed with the one-object ℤ/2 groupoid. All laws
hold, comonad laws are inherited, and the whole development is `Type`-level Lean 4
core, no Mathlib, no `sorry`.

References: MacBeth PROVE `proofs/2026-08-10-state-liftings-holonomy-free.md`
(§SOUND, `Cat ↪ liftings` via `𝕊 × C`) and
`proofs/2026-08-11-state-liftings-holonomy-triviality.md`; DCont ≅ Cat is
Ahman–Chapman–Uustalu arXiv:1408.5809; the store comonad is Uustalu–Vene 2008.
-/

namespace Containers

/-! ## 0. Transport over a product of shapes

Two small helpers isolate the only genuinely dependent content of the product
construction: how equalities and transports interact with `Prod`. Both are pure
Lean 4 core; `transport_prod` leans on definitional proof-irrelevance of `Eq`. -/

/-- Build an equality of pairs from equalities of components (core-Lean
`Prod.ext`). -/
theorem prodEq {A B : Type} {a a' : A} {b b' : B} (ha : a = a') (hb : b = b') :
    (a, b) = (a', b') := by
  cases ha; cases hb; rfl

/-- **Transport over a product factors componentwise.** For a position family of
product shape `fun p => F p.1 × G p.2`, transporting a pair `(x, y)` along an
equality `h : (a, b) = (a', b')` equals the pair of the componentwise transports.
The proof `subst`s the two component equalities and closes by definitional
proof-irrelevance of `Eq` (`h` becomes `rfl`, and `rfl ▸ z ≡ z`). -/
theorem transport_prod {A B : Type} {F : A → Type} {G : B → Type}
    {ab a'b' : A × B} (h : ab = a'b') (x : F ab.1) (y : G ab.2) :
    (h ▸ (⟨x, y⟩ : F ab.1 × G ab.2) : F a'b'.1 × G a'b'.2)
      = ⟨congrArg Prod.fst h ▸ x, congrArg Prod.snd h ▸ y⟩ := by
  cases h
  rfl

/-! ## 1. The product of directed containers = the product category -/

/-- The **product of directed containers** `C × D` (= the product category under
DCont ≅ Cat). Objects are pairs of objects; a morphism out of `(s, t)` is a pair
of morphisms, so the position fibre is the **product** `C.Pos s × D.Pos t`.
Identities, codomains (`sub`) and composition (`shift`) act componentwise, and
each directed-container law D1–D5 is the pair of the factors' laws — D2 and D5
using `transport_prod` to split their shape-equality transport. -/
def DirectedContainer.prod (C D : DirectedContainer) : DirectedContainer where
  toContainer :=
    { Shape := C.Shape × D.Shape
      Pos := fun st => C.Pos st.1 × D.Pos st.2 }
  root := fun st => (C.root st.1, D.root st.2)
  sub := fun st p => (C.sub st.1 p.1, D.sub st.2 p.2)
  shift := fun st p q => (C.shift st.1 p.1 q.1, D.shift st.2 p.2 q.2)
  d1 := fun st => prodEq (C.d1 st.1) (D.d1 st.2)
  d4 := fun st p q => prodEq (C.d4 st.1 p.1 q.1) (D.d4 st.2 p.2 q.2)
  d2 := by
    intro st q
    obtain ⟨s, t⟩ := st
    obtain ⟨q1, q2⟩ := q
    rw [transport_prod]
    show (C.shift s (C.root s) q1, D.shift t (D.root t) q2) = _
    rw [C.d2, D.d2]
  d3 := fun st p => prodEq (C.d3 st.1 p.1) (D.d3 st.2 p.2)
  d5 := by
    intro st p q q'
    obtain ⟨s, t⟩ := st
    obtain ⟨p1, p2⟩ := p
    obtain ⟨q1, q2⟩ := q
    obtain ⟨q1', q2'⟩ := q'
    rw [transport_prod]
    exact prodEq (C.d5 s p1 q1 q1') (D.d5 t p2 q2 q2')

@[simp] theorem DirectedContainer.prod_root (C D : DirectedContainer)
    (st : (C.prod D).Shape) :
    (C.prod D).root st = (C.root st.1, D.root st.2) := rfl

@[simp] theorem DirectedContainer.prod_sub (C D : DirectedContainer)
    (st : (C.prod D).Shape) (p : (C.prod D).Pos st) :
    (C.prod D).sub st p = (C.sub st.1 p.1, D.sub st.2 p.2) := rfl

@[simp] theorem DirectedContainer.prod_shift (C D : DirectedContainer)
    (st : (C.prod D).Shape) (p : (C.prod D).Pos st) (q : (C.prod D).Pos ((C.prod D).sub st p)) :
    (C.prod D).shift st p q = (C.shift st.1 p.1 q.1, D.shift st.2 p.2 q.2) := rfl

/-- The extension of the product is the product of extensions' data: a pair of
shapes carrying a labelling of the **product** position fibre. -/
theorem DirectedContainer.prod_ext (C D : DirectedContainer) (X : Type) :
    Ext (C.prod D).toContainer X
      = ((st : C.Shape × D.Shape) × (C.Pos st.1 × D.Pos st.2 → X)) := rfl

/-! ## 2. Codiscreteness of `𝕊 = ΔS`: a single shape-orbit (`π₀ = 1`)

The distinguishing invariant of the State side. In `ΔS` a morphism `s → s'` is a
position `p ∈ Pos s = S` with `sub s p = s'`; taking `p := s'` connects *any*
ordered pair, so `ΔS` has one connected component. Reader's liftings instead have
`sub s p = s` (shape-preserving), giving `|E|` discrete components. -/

/-- **`𝕊 = ΔS` is codiscrete: `π₀ = 1`.** For any two states `s, s'` there is a
morphism `s → s'` (a position `p` with codomain `s'`) — witnessed by `p := s'`.
Hence every ordered pair of objects is connected: a single shape-orbit. -/
theorem deltaDC_connected (S : Type) (s s' : S) :
    ∃ p : (deltaDC S).Pos s, (deltaDC S).sub s p = s' :=
  ⟨s', rfl⟩

/-! ## 3. The concrete State lifting `stateProduct = ΔBool × ℤ/2` -/

/-- The **State lifting for `C = ℤ/2`**: the store category on two states `Bool`
crossed with the one-object ℤ/2 groupoid, `𝕊 × C = ΔBool × ℤ/2`. A directed
container by `DirectedContainer.prod`; its comonad laws are inherited from
`Containers.Directed`. This is the concrete image of `C ↦ 𝕊 × C` at `S = Bool`,
`C = ℤ/2` — the Lean certificate of the sound embedding `Cat ↪ State-liftings`. -/
def stateProduct : DirectedContainer :=
  (deltaDC Bool).prod ReaderGroupoid.readerGroupoidLifting

section StateProductLaws

variable {X : Type}

/-- **Left counit law** for `stateProduct`, inherited (from D1/D2). -/
theorem stateProduct_left_counit :
    stateProduct.counit ∘ stateProduct.comult
      = (id : Ext stateProduct.toContainer X → _) :=
  stateProduct.left_counit

/-- **Right counit law** for `stateProduct`, inherited (from D3). -/
theorem stateProduct_right_counit :
    Ext.map stateProduct.counit ∘ stateProduct.comult
      = (id : Ext stateProduct.toContainer X → _) :=
  stateProduct.right_counit

/-- **Coassociativity** for `stateProduct`, inherited (from D4/D5). -/
theorem stateProduct_coassoc :
    Ext.map stateProduct.comult ∘ stateProduct.comult
      = (stateProduct.comult ∘ stateProduct.comult :
          Ext stateProduct.toContainer X → _) :=
  stateProduct.coassoc

end StateProductLaws

/-- **Connectedness in the state coordinate** for `stateProduct`. From object
`(b, o)` one can reach `(b', o)` for *any* target state `b'` — moving in the
codiscrete `ΔBool` factor while staying at the identity in the ℤ/2 factor. This is
the single-orbit invariant of the store factor surviving into the product; it is
what makes `stateProduct` a *State* lifting (`π₀ = 1` in the state direction)
rather than a Reader one. -/
theorem stateProduct_state_connected (b b' : Bool) (o : Unit) :
    ∃ p : stateProduct.Pos (b, o), stateProduct.sub (b, o) p = (b', o) :=
  ⟨(b', ReaderGroupoid.Z2.e), rfl⟩

/-- **The packaged sound-embedding certificate.** For every small category `C`
(here `C = ℤ/2`), the store construction `𝕊 × C` is a directed container — a
comonad, hence a State proof-relevant monad lifting — and it is genuinely a
*State* lifting: its state factor `𝕊 = ΔBool` is codiscrete (`π₀ = 1`, every
ordered pair of states connected), unlike Reader's `|E|` discrete components. -/
theorem stateProduct_is_sound_state_lifting :
    -- it is a comonad (the three inherited laws, here at `X = Bool`)
    (stateProduct.counit ∘ stateProduct.comult
        = (id : Ext stateProduct.toContainer Bool → _))
      ∧ (Ext.map stateProduct.counit ∘ stateProduct.comult
          = (id : Ext stateProduct.toContainer Bool → _))
      ∧ (Ext.map stateProduct.comult ∘ stateProduct.comult
          = (stateProduct.comult ∘ stateProduct.comult :
              Ext stateProduct.toContainer Bool → _))
    -- single shape-orbit in the state direction (`π₀(𝕊) = 1`)
      ∧ (∀ b b' : Bool, ∀ o : Unit,
          ∃ p : stateProduct.Pos (b, o), stateProduct.sub (b, o) p = (b', o)) :=
  ⟨stateProduct.left_counit, stateProduct.right_counit, stateProduct.coassoc,
   fun b b' o => stateProduct_state_connected b b' o⟩

end Containers
