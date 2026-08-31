import Containers.DirichletComonoid

/-!
# Bare `⊗`-monoids in `Cont` are a monoid on shapes plus an oplax functor on fibres

`Containers.Dirichlet` equips `Cont` with the **Dirichlet tensor** `(Cont, ⊗, y)`
(`⊗ = Day(Set, ×, 1)`, Niu–Spivak *Polynomial Functors* arXiv:2312.00990 Prop. 3.79). The
sibling file `Containers.DirichletComonoid` classified the **comonoids** for that tensor
(families of monoids). This file is the **arrow-reversed dual**: it cashes out the **monoid**
structure. A `⊗`-monoid is a container `c` with a unit `η : y ⟶ c` and multiplication
`μ : c ⊗ c ⟶ c` obeying the two unit laws and associativity, *stated internally to `Cont`*.

The theorem (MacBeth, PROVE note `2026-07-19-dirichlet-monoid-classification.md`, answering the
`Poly/⊗`-monoid slice flagged as future work in **Niu–Spivak Remark 3.78**):

> A bare `⊗`-monoid on `c` is exactly a **monoid `(·, e)` on the shape set `S = c(1)`** together
> with an **oplax monoidal functor** `P : (S,·,e) → (Set, ×, 1)` on the fibres, `s ↦ c[s]`, with
> structure maps `φ_{s,t} : c[s·t] → c[s] × c[t]` and counit `ε : c[e] → 1` (the unique map).

This file formalises the **forward** direction:

  `Container.DirichletMonoid c  ⟶  Container.ShapeMonoidOplaxFibres c`.

The mechanism, in container coordinates (dual to the comonoid case):

* the unit `η` picks a distinguished shape `e := η.onShapes ∗ ∈ S`; its backward map is the forced
  `ε : c[e] → y[∗] = 1`, carrying no data, so it is **omitted** from the target;
* the multiplication `μ` is **forward** on shapes — an arbitrary binary operation
  `s · t := μ.onShapes (s, t)` — and **backward** on positions, giving the oplax structure map
  `φ_{s,t} := μ.onPos (s, t) : c[s·t] → c[s] × c[t]`;
* the **shape** parts of the unit and associativity laws say `(S, ·, e)` is a monoid
  (`one_smul`, `smul_one`, `smul_assoc`);
* the **fibre** parts give the two oplax unit coherences (`phi_one_smul : φ²_{e,s} = id`,
  `phi_smul_one : φ¹_{s,e} = id`) and the oplax associativity hexagon (`phi_assoc`).

The asymmetry with the comonoid is structural, not accidental: comultiplication maps *into* the
cartesian product of shapes and is forced to the diagonal, whereas multiplication maps *out of*
it and is unconstrained beyond being a monoid (PROVE note §5). So the comonoid trivialises the
shape layer (diagonal) and enriches the fibres (a monoid on each), while the monoid liberates the
shape layer (any monoid) and makes the fibres *oplax*.

STATUS (2026-07-19). The forward map `toShapeMonoidOplaxFibres` is **complete and sorry-free**.
Every law is read off the internal monoid laws with `onPosOfEq` (reused from
`DirichletComonoid`): the shape laws are plain `congrArg` of the law equations, and the fibre
coherences are the position content of the same equations, with the induced shape transports
collapsing by definitional proof irrelevance for `Eq`. No transport toolkit beyond `onPosOfEq` is
needed here, because the shape multiplication is a *free* forward map (there is no forced diagonal
to `subst`, so no `dirichlet_mul_assoc`-style manoeuvre): the associativity transport is the
proof `smul_assoc`, and `onPosOfEq` produces exactly that transport.

The **converse** and the category-level statement `Mon(Cont, ⊗, y) ≅ ∫_{Mon} OplaxMon(-, (Set,×))`
are natural follow-ups, not done here.

Everything is `Type`-level, Lean 4 core, no Mathlib. The forward map and its supporting lemmas
`#print axioms`-report as depending on **no axioms at all** (not even `Quot.sound`): the whole
extraction closes by `congrArg`/`onPosOfEq` and definitional proof irrelevance for `Eq`. No
`sorry`, no classical axioms.
-/

namespace Containers

open Container

/-- A **monoid in the monoidal category `(Cont, ⊗, y)`** (the Dirichlet tensor). The
arrow-reversed dual of `Container.DirichletComonoid`: a unit `η : y ⟶ C` and multiplication
`μ : C ⊗ C ⟶ C` with the two unit laws and associativity, all stated in `Cont`. -/
structure Container.DirichletMonoid (C : Container) where
  /-- The unit `η : y ⟶ C`. -/
  unit : ContainerMorphism Container.y C
  /-- The multiplication `μ : C ⊗ C ⟶ C`. -/
  mul : ContainerMorphism (C ⊗ C) C
  /-- Left unit law `(η ⊗ C) ; μ = λ`. -/
  left_unit :
    (Container.dir₂ unit (ContainerMorphism.id C)).comp mul = (Container.dirLeftUnitor C).hom
  /-- Right unit law `(C ⊗ η) ; μ = ρ`. -/
  right_unit :
    (Container.dir₂ (ContainerMorphism.id C) unit).comp mul = (Container.dirRightUnitor C).hom
  /-- Associativity `(μ ⊗ C) ; μ = α ; (C ⊗ μ) ; μ`. -/
  assoc :
    (Container.dir₂ mul (ContainerMorphism.id C)).comp mul
      = ((Container.dirAssociator C C C).hom.comp
          (Container.dir₂ (ContainerMorphism.id C) mul)).comp mul

/-- A **monoid on shapes together with an oplax monoidal functor on fibres** — the intended
classification target for bare `⊗`-monoids. The shape data `(smul, e)` is a monoid on `C.Shape`;
the fibre data `phi` is the oplax structure map `φ_{s,t} : C[s·t] → C[s] × C[t]` of an oplax
monoidal functor `(C.Shape, smul, e) → (Set, ×, 1)`, `s ↦ C[s]`. The oplax counit
`ε : C[e] → 1` is the forced unique map and carries no data, so it is not recorded. -/
structure Container.ShapeMonoidOplaxFibres (C : Container) where
  /-- The shape multiplication `s · t`. -/
  smul : C.Shape → C.Shape → C.Shape
  /-- The unit shape `e`. -/
  e : C.Shape
  /-- The oplax structure map `φ_{s,t} : C[s·t] → C[s] × C[t]`. -/
  phi : (s t : C.Shape) → C.Pos (smul s t) → C.Pos s × C.Pos t
  /-- Associativity of the shape multiplication. -/
  smul_assoc : ∀ s t u, smul (smul s t) u = smul s (smul t u)
  /-- Left unit law for the shape multiplication. -/
  one_smul : ∀ s, smul e s = s
  /-- Right unit law for the shape multiplication. -/
  smul_one : ∀ s, smul s e = s
  /-- Oplax **left** unit coherence: the second component of `φ_{e,s}` is the identity (up to the
  forced shape transport). -/
  phi_one_smul : ∀ (s : C.Shape) (x : C.Pos (smul e s)), (phi e s x).2 = one_smul s ▸ x
  /-- Oplax **right** unit coherence: the first component of `φ_{s,e}` is the identity. -/
  phi_smul_one : ∀ (s : C.Shape) (x : C.Pos (smul s e)), (phi s e x).1 = smul_one s ▸ x
  /-- Oplax **associativity hexagon**:
  `(φ_{s,t} × id) ∘ φ_{s·t,u} = (id × φ_{t,u}) ∘ φ_{s,t·u}` (with the domain transported along
  `smul_assoc`), unwound into `(C[s] × C[t]) × C[u]`. -/
  phi_assoc : ∀ (s t u : C.Shape) (r : C.Pos (smul (smul s t) u)),
    (phi s t (phi (smul s t) u r).1, (phi (smul s t) u r).2)
      = (((phi s (smul t u) (smul_assoc s t u ▸ r)).1,
          (phi t u (phi s (smul t u) (smul_assoc s t u ▸ r)).2).1),
         (phi t u (phi s (smul t u) (smul_assoc s t u ▸ r)).2).2)

namespace Container.DirichletMonoid

variable {C : Container} (M : C.DirichletMonoid)

/-- The **shape multiplication** `s · t := μ.onShapes (s, t)`: the forward part of `μ`. Unlike the
comonoid's shape comultiplication (forced to the diagonal), this is an *arbitrary* binary
operation — the source of the comonoid/monoid asymmetry. -/
def smul (s t : C.Shape) : C.Shape := M.mul.onShapes (s, t)

/-- The **unit shape** `e := η.onShapes ∗`. -/
def e : C.Shape := M.unit.onShapes ()

/-- The **oplax structure map** `φ_{s,t} := μ.onPos (s, t) : C[s·t] → C[s] × C[t]`: the backward
part of `μ`. The codomain `(C ⊗ C).Pos (s, t)` is `C.Pos s × C.Pos t` definitionally. -/
def phi (s t : C.Shape) : C.Pos (M.smul s t) → C.Pos s × C.Pos t := M.mul.onPos (s, t)

/-- **Associativity of the shape multiplication**, the shape projection of the associativity law
`(μ ⊗ C) ; μ = α ; (C ⊗ μ) ; μ`. -/
theorem smul_assoc (s t u : C.Shape) : M.smul (M.smul s t) u = M.smul s (M.smul t u) :=
  congrArg (fun m => m.onShapes ((s, t), u)) M.assoc

/-- **Left unit law on shapes** `e · s = s`, the shape projection of the left unit law. -/
theorem one_smul (s : C.Shape) : M.smul M.e s = s :=
  congrArg (fun m => m.onShapes ((), s)) M.left_unit

/-- **Right unit law on shapes** `s · e = s`, the shape projection of the right unit law. -/
theorem smul_one (s : C.Shape) : M.smul s M.e = s :=
  congrArg (fun m => m.onShapes (s, ())) M.right_unit

/-- **Oplax left unit coherence** `φ²_{e,s} = id`. The position content of the left unit law: at
shape `(∗, s)`, its second coordinate says the `C[s]`-side of `φ_{e,s}` returns its argument (up
to the forced transport along `one_smul`). The first coordinate lands in `y[∗] = 1` and is
vacuous. -/
theorem phi_one_smul (s : C.Shape) (x : C.Pos (M.smul M.e s)) :
    (M.phi M.e s x).2 = M.one_smul s ▸ x :=
  congrArg Prod.snd (onPosOfEq M.left_unit ((), s) x)

/-- **Oplax right unit coherence** `φ¹_{s,e} = id`. The position content of the right unit law. -/
theorem phi_smul_one (s : C.Shape) (x : C.Pos (M.smul s M.e)) :
    (M.phi s M.e x).1 = M.smul_one s ▸ x :=
  congrArg Prod.fst (onPosOfEq M.right_unit (s, ()) x)

/-- **Oplax associativity hexagon**, the position content of the associativity law. Reading
`onPosOfEq` off the associativity equation at shape `((s, t), u)` and position `r` gives exactly
the unwound coherence in `(C[s] × C[t]) × C[u]`; the associator re-brackets definitionally and the
induced shape transport is the proof `smul_assoc` (by proof irrelevance for `Eq`). -/
theorem phi_assoc (s t u : C.Shape) (r : C.Pos (M.smul (M.smul s t) u)) :
    (M.phi s t (M.phi (M.smul s t) u r).1, (M.phi (M.smul s t) u r).2)
      = (((M.phi s (M.smul t u) (M.smul_assoc s t u ▸ r)).1,
          (M.phi t u (M.phi s (M.smul t u) (M.smul_assoc s t u ▸ r)).2).1),
         (M.phi t u (M.phi s (M.smul t u) (M.smul_assoc s t u ▸ r)).2).2) :=
  onPosOfEq M.assoc ((s, t), u) r

/-- **Forward direction of the classification.** Every bare `⊗`-monoid on `C` determines a monoid
on its shapes together with an oplax monoidal functor on its fibres. -/
def toShapeMonoidOplaxFibres : C.ShapeMonoidOplaxFibres where
  smul := M.smul
  e := M.e
  phi := M.phi
  smul_assoc := M.smul_assoc
  one_smul := M.one_smul
  smul_one := M.smul_one
  phi_one_smul := M.phi_one_smul
  phi_smul_one := M.phi_smul_one
  phi_assoc := M.phi_assoc

end Container.DirichletMonoid

end Containers
