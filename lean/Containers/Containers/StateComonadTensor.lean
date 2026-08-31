import Containers.Directed
import Containers.Dirichlet
import Containers.StateComonad
import Containers.StateProductLifting

/-!
# Lemma 3.1 at the comonad level: the store comonad tensors

`Containers.StateComonad` records **Lemma 3.1** of MacBeth's prove note
`2026-07-28-delta-state-object-and-workers.md` as a *bare container* equality:
`deltaS_tensor : ΔS ⊗ ΔT = Δ(S × T)` and `deltaS_unit : Δ1 = y`, both `rfl`
(shape sets and position fibres coincide definitionally). Those underlie the
`(Set, ×)`-graded category of Workers (`Containers.Workers`).

The bare equality is the whole story only at the level of the *underlying
container*. This file supplies the **strictly stronger, comonad-level** statement
it does not see: that the same identity holds already for the **directed
containers** — equivalently, for the small categories they present under
`DCont ≅ Cat` (Ahman–Chapman–Uustalu, arXiv:1408.5809) — and therefore for the
**store comonads** the state objects induce, not merely their carriers.

Two facts assemble it, both reusing existing machinery:

* **The Dirichlet tensor is the product of categories.** The product of directed
  containers `DirectedContainer.prod` (`Containers.StateProductLifting`) has
  position fibre `C.Pos s × D.Pos t` — the *product* of the arrow-bundles, which
  is exactly the Dirichlet tensor on positions. So its underlying container *is*
  the Dirichlet tensor: `(C.prod D).toContainer = C.toContainer ⊗ D.toContainer`
  (`prod_toContainer_dirichlet`, `rfl`). This names the product category, in
  `Cont`, as `⊗` — the container-level companion of `deltaS_tensor`.

* **The codiscrete case is Lemma 3.1 with the comonad kept.** Because the
  codiscrete directed structure (`deltaDC`) is componentwise projections, the
  product of the two store categories is componentwise the codiscrete structure on
  `S × T`. Hence, as *directed containers*,

    `deltaDC_prod : (ΔS) ⊗ (ΔT) = Δ(S × T)`   (`rfl`),

  and the store comonad's counit and comultiplication on `S × T` are literally
  those of the product (`deltaDC_prod_counit`, `deltaDC_prod_comult`). This is the
  precise sense in which "the state multiplies under composition", now certified
  at the level that carries the comonad rather than only its carrier.

The unit is unchanged: `deltaDC Unit` is the trivial category `𝟙`, underlying
container `y` (`deltaDC_unit_toContainer`).

Everything is `Type`-level, Lean 4 core, no Mathlib. All results are `rfl`, so —
like the bare Lemma 3.1 — they depend on no axioms.
-/

namespace Containers

open Container

/-! ## The product of categories is the Dirichlet tensor `⊗` -/

/-- **The product of directed containers is the Dirichlet tensor, in `Cont`.** The
underlying container of the product category `C.prod D`
(`Containers.StateProductLifting`) is the Dirichlet tensor
`C.toContainer ⊗ D.toContainer`: both have shapes `S × T` and position fibre the
*product* `C.Pos s × D.Pos t`. Holds by `rfl`. This is the comonad-carrying
companion of `deltaS_tensor` — the `⊗` there is realised here as the product of
the underlying categories. -/
theorem prod_toContainer_dirichlet (C D : DirectedContainer) :
    (C.prod D).toContainer = C.toContainer ⊗ D.toContainer := rfl

/-! ## Lemma 3.1, comonad level: `ΔS ⊗ ΔT = Δ(S × T)` as directed containers

The codiscrete structure `deltaDC S` has `root s = s`, `sub s p = p`,
`shift s p q = q`. Under the product these compose componentwise to exactly the
codiscrete structure on `S × T`, so the whole directed container — hence the
store comonad it induces — is `deltaDC (S × T)`. -/

/-- **Lemma 3.1, comonad level.** `ΔS ⊗ ΔT = Δ(S × T)` as *directed containers*:
not merely the underlying containers agree (`deltaS_tensor`), but the codiscrete
directed-container structures — root, sub, shift — and therefore the store
comonads, agree too. Holds by `rfl`: every field of `deltaDC (S × T)` is,
componentwise, the corresponding field of `(deltaDC S).prod (deltaDC T)` (the data
by `Prod`/structure η, the five laws by definitional proof irrelevance for
`Eq`). -/
theorem deltaDC_prod (S T : Type) :
    (deltaDC S).prod (deltaDC T) = deltaDC (S × T) := rfl

/-- The **store counit multiplies**: the counit of the product store category is
the counit of `deltaDC (S × T)` — the store comonad's `ε` on `S × T`. A direct
corollary of `deltaDC_prod` (`rfl`). -/
theorem deltaDC_prod_counit {S T X : Type} :
    ((deltaDC S).prod (deltaDC T)).counit (X := X) = (deltaDC (S × T)).counit (X := X) := rfl

/-- The **store comultiplication multiplies**: the comultiplication of the product
store category is that of `deltaDC (S × T)`. Together with `deltaDC_prod_counit`,
the store comonad on the multiplied state `S × T` *is* the product of the two
store comonads. Holds by `rfl`. -/
theorem deltaDC_prod_comult {S T X : Type} :
    ((deltaDC S).prod (deltaDC T)).comult (X := X) = (deltaDC (S × T)).comult (X := X) := rfl

/-- **Lemma 3.1 unit, comonad level.** The store comonad on the terminal set is the
tensor unit: `deltaDC Unit` is the trivial category `𝟙`, with underlying container
`y` (`Container.y`). Holds by `rfl`. -/
theorem deltaDC_unit_toContainer : (deltaDC Unit).toContainer = Container.y := rfl

end Containers
