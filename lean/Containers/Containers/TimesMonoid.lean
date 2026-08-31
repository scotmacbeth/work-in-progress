import Containers.FourMonoidal
import Containers.DirichletComonoid

/-!
# Bare `×`-monoids in `Cont` are a monoid on shapes plus an oplax functor on fibres

`Containers.FourMonoidal` equips `Cont` with the **product tensor** `(Cont, ×, 1)`
(`× = Day(Set, ⊔, ∅)`, Niu–Spivak *Polynomial Functors* arXiv:2312.00990 §3): for
`C = S ◁ P`, `D = T ◁ Q`,

  `(C × D) = (S × T) ◁ (fun (s,t) => P s ⊕ Q t)`,   unit `1 = Unit ◁ (fun _ => Empty)`.

This file is the **`×`-analogue** of `Containers.DirichletMonoid` (the `⊗`-monoid forward map).
It formalises **Theorem B** of MacBeth's PROVE note
`2026-07-19-dirichlet-monoid-classification.md` §6:

> A bare `×`-monoid on `c` is exactly a **monoid `(·, e)` on the shape set `S = c(1)`** with
> **empty identity fibre `c[e] = ∅`**, together with an **oplax monoidal functor**
> `P : (S,·,e) → (Set, ⊔, ∅)` on the fibres, `s ↦ c[s]`, with structure maps
> `ψ_{s,t} : c[s·t] → c[s] ⊔ c[t]` and counit `ε : c[e] → ∅` (forcing `c[e] = ∅`).

Theorems A (`⊗`) and B (`×`) are **one theorem**, parameterised by the fibre monoidal structure
the Day tensor uses: `⊗` uses `(Set, ×, 1)`, `×` uses `(Set, ⊔, ∅)`. This file makes that
uniformity concrete: it is `DirichletMonoid.lean` with `⊔` for `×` and `∅` for `1`.

This file formalises the **forward** direction:

  `Container.TimesMonoid c  ⟶  Container.ShapeMonoidOplaxFibresCoproduct c`.

The mechanism, in container coordinates:

* the unit `η : 1 ⟶ c` picks a distinguished shape `e := η.onShapes ∗ ∈ S`; its backward map is
  `η♯ : c[e] → 1[∗] = ∅`, i.e. a map `c[e] → Empty` — this **is** the empty-identity-fibre
  obstruction `c[e] = ∅`, and it is recorded as the field `posEmpty`;
* the multiplication `μ : c × c ⟶ c` is **forward** on shapes — `s · t := μ.onShapes (s, t)` —
  and **backward** on positions, giving the oplax structure map / **backward routing**
  `ψ_{s,t} := μ.onPos (s, t) : c[s·t] → c[s] ⊕ c[t]`;
* the **shape** parts of the unit and associativity laws say `(S, ·, e)` is a monoid;
* the **fibre** parts give the two oplax unit coherences (`psi_one_smul : ψ_{e,s} = inr`,
  `psi_smul_one : ψ_{s,e} = inl` — using `c[e] = ∅` to kill the other injection) and the oplax
  associativity hexagon into `c[s] ⊔ c[t] ⊔ c[u]` (`psi_assoc`).

The one genuine difference from the `⊗` file: the fibre combiner is `⊕` (not `×`), so the unit
coherences are proved by a **case split on the routing** `ψ`, ruling out the injection into the
empty identity fibre `c[e]` via `posEmpty`. The associativity coherence, as in the `⊗` file, is
the raw position content of the internal associativity law read off by `onPosOfEq`, with the
shape transport collapsing because `smul_assoc` *is* the transport proof `onPosOfEq` uses.

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

open Container

/-- A **monoid in the monoidal category `(Cont, ×, 1)`** (the product/cartesian tensor). The
`×`-analogue of `Container.DirichletMonoid`: a unit `η : 1 ⟶ C` and multiplication
`μ : C × C ⟶ C` with the two unit laws and associativity, all stated in `Cont`. -/
structure Container.TimesMonoid (C : Container) where
  /-- The unit `η : 1 ⟶ C`. -/
  unit : ContainerMorphism Container.one C
  /-- The multiplication `μ : C × C ⟶ C`. -/
  mul : ContainerMorphism (C.prod C) C
  /-- Left unit law `(η × C) ; μ = λ`. -/
  left_unit :
    (Container.prod₂ unit (ContainerMorphism.id C)).comp mul = (Container.prodLeftUnitor C).hom
  /-- Right unit law `(C × η) ; μ = ρ`. -/
  right_unit :
    (Container.prod₂ (ContainerMorphism.id C) unit).comp mul = (Container.prodRightUnitor C).hom
  /-- Associativity `(μ × C) ; μ = α ; (C × μ) ; μ`. -/
  assoc :
    (Container.prod₂ mul (ContainerMorphism.id C)).comp mul
      = ((Container.prodAssociator C C C).hom.comp
          (Container.prod₂ (ContainerMorphism.id C) mul)).comp mul

/-- A **monoid on shapes with an oplax monoidal functor on fibres into `(Set, ⊔, ∅)`** — the
intended classification target for bare `×`-monoids. The shape data `(smul, e)` is a monoid on
`C.Shape`; the identity fibre `C[e]` is **empty** (`posEmpty`); the fibre data `psi` is the oplax
structure map / backward routing `ψ_{s,t} : C[s·t] → C[s] ⊕ C[t]` of an oplax monoidal functor
`(C.Shape, smul, e) → (Set, ⊔, ∅)`, `s ↦ C[s]`. The oplax counit `ε : C[e] → ∅` is exactly the
empty-fibre witness `posEmpty`. -/
structure Container.ShapeMonoidOplaxFibresCoproduct (C : Container) where
  /-- The shape multiplication `s · t`. -/
  smul : C.Shape → C.Shape → C.Shape
  /-- The unit shape `e`. -/
  e : C.Shape
  /-- The **empty identity fibre** `C[e] = ∅`: the forced oplax counit `ε : C[e] → ∅`. -/
  posEmpty : C.Pos e → Empty
  /-- The oplax structure map / backward routing `ψ_{s,t} : C[s·t] → C[s] ⊕ C[t]`. -/
  psi : (s t : C.Shape) → C.Pos (smul s t) → C.Pos s ⊕ C.Pos t
  /-- Associativity of the shape multiplication. -/
  smul_assoc : ∀ s t u, smul (smul s t) u = smul s (smul t u)
  /-- Left unit law for the shape multiplication. -/
  one_smul : ∀ s, smul e s = s
  /-- Right unit law for the shape multiplication. -/
  smul_one : ∀ s, smul s e = s
  /-- Oplax **left** unit coherence: `ψ_{e,s} = inr` (routing lands entirely in the `C[s]` summand,
  the identity-fibre summand being empty), up to the forced shape transport. -/
  psi_one_smul : ∀ (s : C.Shape) (x : C.Pos (smul e s)), psi e s x = Sum.inr (one_smul s ▸ x)
  /-- Oplax **right** unit coherence: `ψ_{s,e} = inl`. -/
  psi_smul_one : ∀ (s : C.Shape) (x : C.Pos (smul s e)), psi s e x = Sum.inl (smul_one s ▸ x)
  /-- Oplax **associativity hexagon**:
  `(ψ_{s,t} ⊕ id) ∘ ψ_{s·t,u} = (id ⊕ ψ_{t,u}) ∘ ψ_{s,t·u}` (domain transported along
  `smul_assoc`), unwound into `(C[s] ⊕ C[t]) ⊕ C[u]`. -/
  psi_assoc : ∀ (s t u : C.Shape) (r : C.Pos (smul (smul s t) u)),
    Sum.elim (fun w => Sum.inl (psi s t w)) Sum.inr (psi (smul s t) u r)
      = Sum.elim (Sum.inl ∘ Sum.inl) (Sum.elim (Sum.inl ∘ Sum.inr) Sum.inr)
          (Sum.elim Sum.inl (fun w => Sum.inr (psi t u w))
            (psi s (smul t u) (smul_assoc s t u ▸ r)))

namespace Container.TimesMonoid

variable {C : Container} (M : C.TimesMonoid)

/-- The **shape multiplication** `s · t := μ.onShapes (s, t)`: the forward part of `μ`. -/
def smul (s t : C.Shape) : C.Shape := M.mul.onShapes (s, t)

/-- The **unit shape** `e := η.onShapes ∗`. -/
def e : C.Shape := M.unit.onShapes ()

/-- The **empty identity fibre** witness `ε : C[e] → ∅`, the backward map of the unit `η : 1 ⟶ C`
(whose codomain fibre `1[∗]` is `Empty`). This is the empty-identity-fibre obstruction
`C[e] = ∅` that distinguishes `×`-monoids from `⊗`-monoids. -/
def posEmpty : C.Pos M.e → Empty := M.unit.onPos ()

/-- The **oplax structure map / backward routing** `ψ_{s,t} := μ.onPos (s, t)`, of type
`C[s·t] → C[s] ⊕ C[t]`: the backward part of `μ`. The codomain `(C × C).Pos (s, t)` is
`C.Pos s ⊕ C.Pos t` definitionally. -/
def psi (s t : C.Shape) : C.Pos (M.smul s t) → C.Pos s ⊕ C.Pos t := M.mul.onPos (s, t)

/-- **Associativity of the shape multiplication**, the shape projection of the associativity law. -/
theorem smul_assoc (s t u : C.Shape) : M.smul (M.smul s t) u = M.smul s (M.smul t u) :=
  congrArg (fun m => m.onShapes ((s, t), u)) M.assoc

/-- **Left unit law on shapes** `e · s = s`, the shape projection of the left unit law. -/
theorem one_smul (s : C.Shape) : M.smul M.e s = s :=
  congrArg (fun m => m.onShapes ((), s)) M.left_unit

/-- **Right unit law on shapes** `s · e = s`, the shape projection of the right unit law. -/
theorem smul_one (s : C.Shape) : M.smul s M.e = s :=
  congrArg (fun m => m.onShapes (s, ())) M.right_unit

/-- **Oplax left unit coherence** `ψ_{e,s} = inr`. The position content of the left unit law:
routing out of `C[e·s] = C[s]` lands entirely in the `C[s]` summand — the alternative, landing in
the identity fibre `C[e]`, is ruled out by `posEmpty` (that fibre is empty). -/
theorem psi_one_smul (s : C.Shape) (x : C.Pos (M.smul M.e s)) :
    M.psi M.e s x = Sum.inr (M.one_smul s ▸ x) := by
  have h : Sum.elim (fun a => Sum.inl (M.unit.onPos () a)) Sum.inr (M.psi M.e s x)
      = Sum.inr (M.one_smul s ▸ x) := onPosOfEq M.left_unit ((), s) x
  cases hp : M.psi M.e s x with
  | inl a => exact (M.unit.onPos () a).elim
  | inr b => rw [hp] at h; exact congrArg Sum.inr (Sum.inr.inj h)

/-- **Oplax right unit coherence** `ψ_{s,e} = inl`. The position content of the right unit law. -/
theorem psi_smul_one (s : C.Shape) (x : C.Pos (M.smul s M.e)) :
    M.psi s M.e x = Sum.inl (M.smul_one s ▸ x) := by
  have h : Sum.elim Sum.inl (fun a => Sum.inr (M.unit.onPos () a)) (M.psi s M.e x)
      = Sum.inl (M.smul_one s ▸ x) := onPosOfEq M.right_unit (s, ()) x
  cases hp : M.psi s M.e x with
  | inl b => rw [hp] at h; exact congrArg Sum.inl (Sum.inl.inj h)
  | inr a => exact (M.unit.onPos () a).elim

/-- **Oplax associativity hexagon**, the position content of the associativity law. Reading
`onPosOfEq` off the associativity equation at shape `((s, t), u)` and position `r` gives exactly
the unwound coherence in `(C[s] ⊕ C[t]) ⊕ C[u]`; the associator re-brackets definitionally and
the induced shape transport is the proof `smul_assoc` (it *is* the transport `onPosOfEq` uses). -/
theorem psi_assoc (s t u : C.Shape) (r : C.Pos (M.smul (M.smul s t) u)) :
    Sum.elim (fun w => Sum.inl (M.psi s t w)) Sum.inr (M.psi (M.smul s t) u r)
      = Sum.elim (Sum.inl ∘ Sum.inl) (Sum.elim (Sum.inl ∘ Sum.inr) Sum.inr)
          (Sum.elim Sum.inl (fun w => Sum.inr (M.psi t u w))
            (M.psi s (M.smul t u) (M.smul_assoc s t u ▸ r))) :=
  onPosOfEq M.assoc ((s, t), u) r

/-- **Forward direction of the classification.** Every bare `×`-monoid on `C` determines a monoid
on its shapes with **empty identity fibre**, together with an oplax monoidal functor into
`(Set, ⊔, ∅)` on its fibres. -/
def toShapeMonoidOplaxFibresCoproduct : C.ShapeMonoidOplaxFibresCoproduct where
  smul := M.smul
  e := M.e
  posEmpty := M.posEmpty
  psi := M.psi
  smul_assoc := M.smul_assoc
  one_smul := M.one_smul
  smul_one := M.smul_one
  psi_one_smul := M.psi_one_smul
  psi_smul_one := M.psi_smul_one
  psi_assoc := M.psi_assoc

end Container.TimesMonoid

end Containers
