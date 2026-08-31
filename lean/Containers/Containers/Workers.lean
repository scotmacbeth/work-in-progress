import Containers.StateComonad
import Containers.Cont

/-!
# The category of Workers, graded by `(Set, ×)`

This file formalises **Theorem T3** of MacBeth's prove note
`2026-07-28-delta-state-object-and-workers.md`: the category of **Workers**
whose composition is graded by the monoidal category `(Set, ×, 1)`, built on the
state object `ΔS` and Lemma 3.1 (`ΔS ⊗ ΔT = Δ(S × T)`) from
`Containers.StateComonad`.

A **Worker** from `p` to `q` with **state `S`** is a container morphism
`w : ΔS ⊗ p ⟶ q` (Dirichlet tensor `⊗`). Unpacking, with `q = (C, D)` and
`ΔS ⊗ p = (S × A, (s, a) ↦ S × B a)`:

* forward `f : S × A → C` — from state `s` and input shape `a`, an output shape;
* backward split in two: a **writeback** `D (f (s, a)) → S` of a new state per
  output position, and the ordinary back-map `D (f (s, a)) → B a`.

**Composition multiplies the state.** A state-`S` worker `p ⟶ q` followed by a
state-`T` worker `q ⟶ r` is a state-`(S × T)` worker `p ⟶ r` (`Worker.comp`).
Written directly in coordinates it is *defeq-shaped*: the associativity and
unitality laws hold on the nose, once the grades are transported along the
associator / unitors of `(Set, ×)`. That transport is `Worker.reGrade` — the
reindexing of a worker's state along a bijection of grades (over the core
groupoid `Core(Set)`, the level at which `S ↦ ΔS` is genuinely functorial).

The three graded-category laws are:

* `Worker.unit_left`  — `(id ∘ w)` transported along `1 × T ≅ T` is `w`;
* `Worker.unit_right` — `(w ∘ id)` transported along `S × 1 ≅ S` is `w`;
* `Worker.assoc`      — `((u ∘ v) ∘ w)` transported along `(S×T)×U ≅ S×(T×U)`
  is `u ∘ (v ∘ w)`.

Each is `ext'` + `rfl`: no genuine transport slog, exactly as Lemma 3.1 being
`rfl` predicted. This is the grant's "processes with state" object (Neil's Ch4)
machine-checked, and promotes the T3 core (`state-object-delta.json`) to
`lean-verified`. Compare `Containers.CoKleisli` (Workers is the coKleisli
category of the `(Set,×)`-graded comonad `S ↦ ΔS ⊗ (−)`).

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

/-- A **Worker** from `p` to `q` with **state `S`**: a container morphism
`ΔS ⊗ p ⟶ q`. Its extension reads a current `S`-state and a `p`-input, produces
a `q`-output shape, and per output position writes back a new `S`-state and pulls
an input position back. -/
abbrev Worker (S : Type) (p q : Container) : Type :=
  ContainerMorphism (deltaS S ⊗ p) q

/-- **Composition of Workers multiplies the state.** Given `w₁ : ΔS ⊗ p ⟶ q` and
`w₂ : ΔT ⊗ q ⟶ r`, the composite is a state-`(S × T)` worker `p ⟶ r`.

In coordinates (`sta = ((s, t), a)`): run `w₁` on `(s, a)` for an intermediate
`q`-shape `e`, run `w₂` on `(t, e)` for the output shape; backwards, `w₂`'s
writeback supplies the new `T`-state and a `q`-position, which `w₁` pulls back to
the new `S`-state and a `p`-position. Written directly, so the category laws are
defeq up to grade coherence. -/
def Worker.comp {S T : Type} {p q r : Container}
    (w₁ : Worker S p q) (w₂ : Worker T q r) : Worker (S × T) p r where
  onShapes := fun sta =>
    w₂.onShapes (sta.1.2, w₁.onShapes (sta.1.1, sta.2))
  onPos := fun sta d =>
    let gd := w₂.onPos (sta.1.2, w₁.onShapes (sta.1.1, sta.2)) d
    let fd := w₁.onPos (sta.1.1, sta.2) gd.2
    ((fd.1, gd.1), fd.2)

/-- The **identity Worker** on `p`, in grade `1` (recall `Δ1 = y`). It reads the
`p`-input and passes it through, writing back the unique `Unit`-state. -/
def Worker.id (p : Container) : Worker Unit p p where
  onShapes := fun ua => ua.2
  onPos := fun _ pos => ((), pos)

/-- **Grade reindexing.** Transport a state-`S` worker to a state-`S'` worker
along maps `to : S → S'` (applied to the writeback) and `fro : S' → S` (applied
to the incoming state). When `(to, fro)` is a bijection this is an isomorphism of
hom-sets — the action of `Δ` on the core groupoid `Core(Set)`. The graded-category
laws transport composites along the `(Set, ×)` coherence isos this way. -/
def Worker.reGrade {S S' : Type} {p q : Container}
    (to : S → S') (fro : S' → S) (w : Worker S p q) : Worker S' p q where
  onShapes := fun s'a => w.onShapes (fro s'a.1, s'a.2)
  onPos := fun s'a d =>
    let sr := w.onPos (fro s'a.1, s'a.2) d
    (to sr.1, sr.2)

/-! ## The graded-category laws

All three hold by `ext'` + `rfl`: `Worker.comp` is written in direct coordinates
and `Worker.reGrade` along a `(Set,×)` coherence iso is a `Prod` shuffle, so the
two legs agree definitionally (`Prod`/`Unit` η). -/

/-- **Left unitality.** The composite `id ∘ w`, of grade `1 × T`, transported
along the left unitor `1 × T ≅ T`, is `w`. -/
theorem Worker.unit_left {T : Type} {p q : Container} (w : Worker T p q) :
    ((Worker.id p).comp w).reGrade (fun ut => ut.2) (fun t => ((), t)) = w := by
  refine ContainerMorphism.ext' rfl ?_
  intro s d
  rfl

/-- **Right unitality.** The composite `w ∘ id`, of grade `S × 1`, transported
along the right unitor `S × 1 ≅ S`, is `w`. -/
theorem Worker.unit_right {S : Type} {p q : Container} (w : Worker S p q) :
    (w.comp (Worker.id q)).reGrade (fun su => su.1) (fun s => (s, ())) = w := by
  refine ContainerMorphism.ext' rfl ?_
  intro s d
  rfl

/-- **Associativity.** Both bracketings of a triple composite agree once the
grade `(S × T) × U` is transported along the associator to `S × (T × U)`. -/
theorem Worker.assoc {S T U : Type} {p q r z : Container}
    (u : Worker S p q) (v : Worker T q r) (w : Worker U r z) :
    ((u.comp v).comp w).reGrade
        (fun stu => (stu.1.1, (stu.1.2, stu.2)))
        (fun stu => ((stu.1, stu.2.1), stu.2.2))
      = u.comp (v.comp w) := by
  refine ContainerMorphism.ext' rfl ?_
  intro s d
  rfl

end Containers
