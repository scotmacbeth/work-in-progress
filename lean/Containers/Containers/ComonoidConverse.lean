import Containers.Comonoid
import Containers.ComonadConverse

/-!
# A `◁`-comonoid in `(Cont, ◁, I)` is a directed container (M3b)

`Containers.Comonoid` proves the **forward** direction of M3: every directed
container (Ahman–Chapman–Uustalu, *When is a container a comonad?*,
LMCS 10(3):2014) is a comonoid in the monoidal category `(Cont, ◁, I)`, via
`DirectedContainer.toComonoid`. This file runs the construction backwards and so
completes M3 into an equivalence: from a `◁`-comonoid `(C, ε, δ)` we recover a
directed-container structure on `C`.

## Strategy — factor through the comonad converse

`Containers.ComonadConverse` (M2b) already does the genuinely dependent work: it
turns a *container comonad* (`ContainerComonad` + `IsComonad`) into a directed
container, deriving D1–D5 with all the `cShape`-transports isolated. Rather than
redo that bookkeeping one level up, we **reduce the comonoid to a comonad** and
reuse it.

The counit `ε : C ⟶ I` and comultiplication `δ : C ⟶ C ◁ C` of a comonoid are
already the combinatorial data of a `ContainerComonad`:

* `e s := ε.onPos s ()` — the counit's root choice;
* `cShape s := (δ.onShapes s).1`, `cSub s := (δ.onShapes s).2`,
  `cVal s p q := δ.onPos s ⟨p, q⟩` — the three components of `δ`.

Because the extension functor sends `◁` to functor composition
(`Container.seqExt`), the comonad counit and comultiplication built from this
data are **definitionally** `ε.toNat`/`δ.toNat` repackaged through `seqExt`
(`toContainerComonad_comult_eq` is `rfl`). The three comonad laws therefore drop
out of the three comonoid laws:

* the **counit laws** collapse the internal unitor iso — composing the comonoid
  law with the unitor's `hom` cancels it to `id C`, and projecting shapes/positions
  of that `C ⟶ C` morphism gives exactly the shape and value equations the comonad
  counit laws need (`right_counit`, `left_counit`);
* **coassociativity** needs no projection at all: both sides of the comonad law
  are the *same* repackaging `tripleSeqExt` of the two sides of the comonoid
  coassociativity law (crossed — comonad-LHS matches comonoid-RHS), so a single
  `rw [M.coassoc]` closes it, transport-free.

Feeding the resulting `IsComonad` into `ContainerComonad.toDirectedContainer`
yields the directed container. This is the honest evidence for the Shapiro–Spivak
reading (arXiv:2305.00167, Rmk 3.16): the `◁`-packaging carries the `Π`, but the
correspondence itself is composition, so once `seqExt` unfolds `◁` the converse is
almost free.

## Both round trips: `DirectedContainer C ≃ Comonoid C`

The two constructions `DirectedContainer.toComonoid` (M3, forward) and
`Container.Comonoid.toDirectedContainer` (M3b, above) are mutually inverse *as packagings*:

* `DirectedContainer.toComonoid_toDirectedContainer` (directed → comonoid → directed) is
  `rfl` — the recovered comonad's outer shape map is the identity, so every `cShape`
  transport collapses by proof irrelevance;
* `Container.Comonoid.toDirectedContainer_toComonoid` (comonoid → directed → comonoid) is
  the substantive round trip: the counit is `rfl`, and the comultiplication is recovered by
  `ContainerMorphism.ext_eq`, whose shape half is `Container.seq_shape_norm` and whose
  position half — a transport in the **outer** shape of `C ◁ C` — is `Container.seq_pos_norm`.

Together they certify a full isomorphism of the two packagings, upgrading M3/M3b from "both
maps + one round trip" to a machine-checked equivalence `DirectedContainer C ≃ Comonoid C`.

Everything is `Type`-level, Lean 4 core, no Mathlib.
-/

namespace Containers

open Container

/-- **Position component of a morphism equality.** From `f = g` read off, at each
shape `s`, that the backward position maps agree after transporting the codomain
position along the (definitional) shape equality. The destructor dual to
`ContainerMorphism.ext'`; the transport discharges to `rfl` by `subst`. -/
theorem ContainerMorphism.congr_onPos {C D : Container} {f g : ContainerMorphism C D}
    (h : f = g) (s : C.Shape) (p : D.Pos (f.onShapes s)) :
    f.onPos s p
      = g.onPos s (congrArg (fun m : ContainerMorphism C D => m.onShapes s) h ▸ p) := by
  subst h; rfl

namespace Container.Comonoid

variable {C : Container} (M : Container.Comonoid C)

/-- The `ContainerComonad` data underlying a comonoid: the counit is a root
choice, and the comultiplication's three components are the outer shape, the inner
shapes, and the values of `δ`. -/
def toContainerComonad : ContainerComonad where
  toContainer := C
  e := fun s => M.counit.onPos s ()
  cShape := fun s => (M.comult.onShapes s).1
  cSub := fun s => (M.comult.onShapes s).2
  cVal := fun s p q => M.comult.onPos s ⟨p, q⟩

/-- The comonad comultiplication of `toContainerComonad` is, definitionally, the
natural transformation `δ.toNat` repackaged through the composition iso
`Container.seqExt` (`⟦C ◁ C⟧ = ⟦C⟧ ∘ ⟦C⟧`). -/
theorem toContainerComonad_comult_eq {X : Type} (t : Ext C X) :
    M.toContainerComonad.comult t = Container.seqExt (M.comult.toNat X t) := rfl

/-- The comonad counit of `toContainerComonad` is `ε.toNat` read off at the unique
position of `I`. -/
theorem toContainerComonad_counit_eq {X : Type} (t : Ext C X) :
    M.toContainerComonad.counit t = (M.counit.toNat X t).2 () := rfl

/-! ### The three comonad laws from the three comonoid laws -/

/-- **The linchpin.** The comultiplication preserves the outer shape:
`cShape s = s`. It is the shape component of the right-counit law
`δ ; (C ◁ ε) = ρ⁻¹`, whose right-hand side has outer shape `s` — no probing
needed, unlike the comonad-level `cShape_eq`. -/
theorem cShape_eq (s : C.Shape) : (M.comult.onShapes s).1 = s :=
  congrArg Sigma.fst
    (congrArg (fun m : ContainerMorphism C (C ◁ Container.I) => m.onShapes s) M.right_counit)

/-- The right-counit law `δ ; (C ◁ ε) = ρ⁻¹` composed with the right unitor's
`hom` cancels the unitor to `id C`; projecting this `C ⟶ C` morphism yields the
comonad's right counit law directly. -/
theorem right_counit_cancel :
    (M.comult.comp (Container.seq₂ (ContainerMorphism.id C) M.counit)).comp
        (Container.rightUnitor C).hom = ContainerMorphism.id C := by
  rw [M.right_counit]; exact (Container.rightUnitor C).inv_hom

/-- The left-counit law `δ ; (ε ◁ C) = λ⁻¹` composed with the left unitor's `hom`
cancels the unitor to `id C`. Its shape component is D1, its position component is
D2. -/
theorem left_counit_cancel :
    (M.comult.comp (Container.seq₂ M.counit (ContainerMorphism.id C))).comp
        (Container.leftUnitor C).hom = ContainerMorphism.id C := by
  rw [M.left_counit]; exact (Container.leftUnitor C).inv_hom

/-- The `Ext (C ◁ (C ◁ C)) X ≅ Ext C (Ext C (Ext C X))` repackaging through which
both sides of the comonad coassociativity law factor. -/
def tripleSeqExt {X : Type} : Ext (C ◁ (C ◁ C)) X → Ext C (Ext C (Ext C X)) :=
  fun p => Ext.map Container.seqExt (Container.seqExt p)

/-- **The comonad laws hold.** Each is derived from the corresponding comonoid law
by the reductions described in the module docstring. -/
theorem toContainerComonad_isComonad : M.toContainerComonad.IsComonad where
  left_counit := by
    intro X
    funext t
    obtain ⟨s, v⟩ := t
    refine Ext.ext_eq (congrArg (fun m : ContainerMorphism C C => m.onShapes s)
      M.left_counit_cancel) ?_
    intro q
    exact congrArg v (ContainerMorphism.congr_onPos M.left_counit_cancel s q)
  right_counit := by
    intro X
    funext t
    obtain ⟨s, v⟩ := t
    refine Ext.ext_eq (M.cShape_eq s) ?_
    intro q
    exact congrArg v (ContainerMorphism.congr_onPos M.right_counit_cancel s q)
  coassoc := by
    intro X
    show (fun t => tripleSeqExt ((M.comult.comp
        (Container.seq₂ (ContainerMorphism.id C) M.comult)).toNat X t))
      = fun t => tripleSeqExt (((M.comult.comp
          (Container.seq₂ M.comult (ContainerMorphism.id C))).comp
          (Container.associator C C C).hom).toNat X t)
    rw [M.coassoc]

/-- **The converse of M3.** A `◁`-comonoid in `(Cont, ◁, I)` is a directed
container: recover the directed-container structure through the comonad converse
`ContainerComonad.toDirectedContainer`. -/
def toDirectedContainer : DirectedContainer :=
  M.toContainerComonad.toDirectedContainer M.toContainerComonad_isComonad

/-- The recovered directed container has the expected root, sub-shape and shift,
read directly off `ε` and `δ`. -/
theorem toDirectedContainer_root (s : C.Shape) :
    M.toDirectedContainer.root s = M.counit.onPos s () := rfl

theorem toDirectedContainer_sub (s : C.Shape) (p : C.Pos s) :
    M.toDirectedContainer.sub s p
      = (M.comult.onShapes s).2 ((M.cShape_eq s).symm ▸ p) := rfl

theorem toDirectedContainer_shift (s : C.Shape) (p : C.Pos s)
    (q : C.Pos (M.toDirectedContainer.sub s p)) :
    M.toDirectedContainer.shift s p q
      = M.comult.onPos s ⟨(M.cShape_eq s).symm ▸ p, q⟩ := rfl

end Container.Comonoid

/-! ## The round trips: `DirectedContainer C ≃ Comonoid C` -/

namespace DirectedContainer

/-- **Round trip (directed → comonoid → directed).** Packaging a directed
container as a `◁`-comonoid and recovering it returns the original — on the nose.
The recovered comonad data is definitionally `DirectedContainer.toContainerComonad`
(its outer shape map `fun s => (⟨s, D.sub s⟩).1` is `id`), so this reduces to
`ComonadConverse.toContainerComonad_toDirectedContainer`, itself `rfl`. -/
theorem toComonoid_toDirectedContainer (D : DirectedContainer) :
    D.toComonoid.toDirectedContainer = D := rfl

end DirectedContainer

/-! ### The other round trip

`Container.Comonoid.toDirectedContainer_toComonoid` (below) — that recovering a directed
container from a `◁`-comonoid and packaging it back returns the original comonoid — closes
the equivalence. Its counit matches definitionally; its comultiplication matches on shapes
(`Container.seq_shape_norm`) and, for the position half, requires a transport whose change is
in the **outer** shape of `C ◁ C` (`s` versus `(δ.onShapes s).1`), so it is *not* an instance
of `Container.seq_pos_transport` (which fixes the outer shape). We isolate that outer
transport in the bespoke `Container.seq_pos_norm`: generalising `cShape s` to a free variable
lets the whole cast collapse by `cases`. Together with `toComonoid_toDirectedContainer` this
upgrades M3/M3b to a full isomorphism of packagings `DirectedContainer C ≃ Comonoid C`. -/

/-- Normalisation of a `C ◁ C` shape along `hcs : cs = s`, generalised to free
`s`, `cs` so the substitution sidesteps the occurs-check on `(δ.onShapes s).1`.
The shape half of the `toDirectedContainer_toComonoid` round trip. -/
theorem Container.seq_shape_norm {C : Container} {s cs : C.Shape} (hcs : cs = s)
    (f : C.Pos cs → C.Shape) :
    (⟨s, fun p => f (hcs.symm ▸ p)⟩ : (C ◁ C).Shape) = ⟨cs, f⟩ := by
  cases hcs; rfl

/-- **The position half of the outer round trip.** Transporting a position `⟨u, r⟩`
of `C ◁ C` along the shape normalisation `seq_shape_norm hcs f` computes
componentwise: the outer position `u : C.Pos s` transports into the `cs` fibre along
`hcs`, and the inner position `r` is carried along unchanged (its fibre
`C.Pos (f (hcs.symm ▸ u))` is fixed by the outer transport). Generalising over free
`s`, `cs` lets the whole cast collapse by `cases hcs`, sidestepping the occurs-check on
`(δ.onShapes s).1` that blocks substituting `cShape s = s` directly. This is the
position half of the `toDirectedContainer_toComonoid` round trip. -/
theorem Container.seq_pos_norm {C : Container} {s cs : C.Shape} (hcs : cs = s)
    (f : C.Pos cs → C.Shape) (u : C.Pos s) (r : C.Pos (f (hcs.symm ▸ u))) :
    (Container.seq_shape_norm hcs f ▸
        (⟨u, r⟩ : (C ◁ C).Pos ⟨s, fun p => f (hcs.symm ▸ p)⟩)
          : (C ◁ C).Pos ⟨cs, f⟩)
      = ⟨(hcs.symm ▸ u : C.Pos cs), r⟩ := by
  cases hcs; rfl

/-- **Extensionality for `◁`-comonoids.** Two comonoids on the same container agree as
soon as their counit and comultiplication morphisms agree: the three law fields are
propositions, discharged by definitional proof irrelevance. -/
theorem Container.Comonoid.ext {C : Container} {M N : Container.Comonoid C}
    (hc : M.counit = N.counit) (hd : M.comult = N.comult) : M = N := by
  obtain ⟨ε₁, δ₁, l₁, r₁, c₁⟩ := M
  obtain ⟨ε₂, δ₂, l₂, r₂, c₂⟩ := N
  cases hc
  cases hd
  rfl

/-- **Round trip (comonoid → directed → comonoid).** Recovering a directed container
from a `◁`-comonoid `M` (`Container.Comonoid.toDirectedContainer`) and repackaging it as
a comonoid (`DirectedContainer.toComonoid`) returns `M` on the nose.

The counit matches definitionally (`I`'s shapes and positions are `Unit`, so the two
`C ⟶ I` morphisms are `rfl`-equal by `Unit`-η). The comultiplication matches by
`ContainerMorphism.ext_eq`: on shapes it is `Container.seq_shape_norm` (the recovered
`sub` reintroduces the `cShape`-transport that normalises `⟨s, C.sub s⟩` back to
`δ.onShapes s`), and the position half — the transport whose change is in the **outer**
shape of `C ◁ C` — is exactly `Container.seq_pos_norm`. Together with
`DirectedContainer.toComonoid_toDirectedContainer` this upgrades M3/M3b to a full
isomorphism of packagings `DirectedContainer C ≃ Container.Comonoid C` (both round trips
certified), completing the Ahman–Chapman–Uustalu / Dorta–Jarvis–Niu (arXiv:2305.05655,
Thm 4.3) correspondence at the level of `(Cont, ◁, I)`-comonoids. -/
theorem Container.Comonoid.toDirectedContainer_toComonoid {C : Container}
    (M : Container.Comonoid C) : M.toDirectedContainer.toComonoid = M := by
  refine Container.Comonoid.ext rfl ?_
  refine ContainerMorphism.ext_eq
    (fun s => Container.seq_shape_norm
      (M.toContainerComonad.cShape_eq M.toContainerComonad_isComonad s)
      (M.comult.onShapes s).2) ?_
  intro s p
  obtain ⟨u, r⟩ := p
  exact congrArg (M.comult.onPos s)
    (Container.seq_pos_norm
      (M.toContainerComonad.cShape_eq M.toContainerComonad_isComonad s)
      (M.comult.onShapes s).2 u r).symm

end Containers
