import Containers.FibredTransfer
import Containers.BiKleisliMaybe

/-!
# The `T_M`-side boundary of cartesian preservation: `Maybe` preserves, `Pf` does not

`Containers.FibredTransfer` certifies the **`G_M` side** of Neil's fibrational front
(2026-08-05): the transfer comonad `G_M (S,P) = (S, M ∘ P)` preserves cartesian container
morphisms **for every monad `M`** (`SetMonad.onMor_cartesian`, hypothesis-free). The
stratification result (`crown-tfae-splits-strict-chain`,
`proofs/2026-08-05-crown-gap-closure.md`, MacBeth) says the **`T_M` side** is where
cartesian-ness *bites*:

> Within the ∏-Mendler class, `T_M` preserves cartesian morphisms **iff** the leaf-tracking
> map `u_* : lv(m) → lv(Mu m)` is a bijection for every `u, m` (`cartFun`), **iff** `M` is a
> cartesian monad (Theorem 1, `proofs/2026-08-05-crown-gap-closure.md`, mirroring the paper
> `2026-08-05-cartesian-preservation-nonbranching.md`; `T_M` = Ahman–Bauer effect monad,
> arXiv:2409.17664, Thm 6.3).

This file pins the **boundary** of that fact with two machine-checked witnesses, mirroring the
`decide`/char-function style of `Containers.BranchingObstruction`:

1. **`Maybe` (cartesian, `M X = X + 1`) preserves** — proved *in full generality*
   (`TMaybe_onMor_cartesian`): for **any** cartesian `φ`, `T_Maybe φ` is cartesian. `T_Maybe`
   is degenerate on positions (arity ≤ 1: `id` over `none`, `φ.onPos s` over `some s`), so the
   fibrewise bijection survives untouched. This is the positive half — the `T_M`-analogue of
   `G_M`'s `onMor_cartesian`, holding because `Maybe`'s leaf-tracking `u_*` is always a
   bijection (`cartFun`).

2. **`Pf` (finite powerset, *not* cartesian) fails** — a concrete finite fibre witness
   (`PfWitness`). For the merging base map `u : {a,a'} → {c}` and the two-leaf shape
   `m = {a,a'} ∈ Pf`, the leaf-tracking map `u_* : lv(m) → lv(Pf u · m)` collapses both leaves
   to one (`ustar_merges` — this is the **non-injective leaf map** the informal note flags).
   By the product-reindexing lemma (`crown-gap-closure.md` §0: `φ^*` is injective iff `φ`
   surjective, surjective iff `φ` injective), the induced backward map of `T_Pf` on the
   ∏-cointerpretation positions `P⋆(m) = ∏_{b ∈ lv m} P(x_b)` is the **diagonal**
   `Bool → Bool × Bool`, which is injective but **not surjective**
   (`fstar_injective`, `fstar_not_surjective`). Hence `T_Pf` does *not* preserve the cartesian
   morphism `(u, id)` — the `T_M`-side counterpart of the reverse-`κ` E2′ failure in
   `Containers.BranchingObstruction`.

**Precision note.** The informal target (`state/LEAN.md`) says the `T_Pf` backward map is "not
injective". At the level of the *product* map that is imprecise: it is the *leaf comparison*
`u_*` that is non-injective (`ustar_merges`); the induced product-reindexing then fails
**surjectivity**, not injectivity (`Pf` never drops a leaf, so `u_*` is always surjective —
`ustar_surjective` — hence the reindex stays injective). Either way `T_Pf φ` is **not a
bijection**, so `T_Pf` fails to preserve the cartesian morphism; the two lemmas below record
exactly *which* half breaks and why, faithfully to the reindexing lemma.

Together: a machine-checked instance of "`T_M` preserves cartesian morphisms ⟺ `M` is
cartesian" at the `Maybe`/`Pf` boundary. Everything is `Type`-level, Lean 4 core, no Mathlib;
no `sorry`, no classical axioms (definitional `rfl` and kernel `decide` only).
-/

namespace Containers

open BiKleisliMaybe

/-! ## 1. `Maybe` preserves cartesian morphisms (for every cartesian `φ`)

`T_Maybe (S,P) = (Option S, P⋆)` with `P⋆(none) = PUnit`, `P⋆(some s) = P s`
(`BiKleisliMaybe.TObj`/`TPos`). Its backward position map (`BiKleisliMaybe.Tmap`) is `id` over
`none` and `φ.onPos s` over `some s`. Because `Maybe` has at most one leaf, the ∏ never merges
or drops a leaf (`u_*` is always a bijection: `cartFun` holds), so a fibrewise bijection is
carried to a fibrewise bijection. -/

/-- **`T_Maybe` preserves cartesian morphisms.** If `φ : X ⟶ Y` is cartesian (each backward
map `φ.onPos s` a bijection), then so is `T_Maybe φ`: over `none` the backward map is `id`
(bijection), and over `some s` it is `φ.onPos s`, whose two-sided inverse is supplied by `h`.
This is the positive, `Maybe`-side half of the `T_M`-boundary — the exact `T_M`-analogue of
the hypothesis-free `SetMonad.onMor_cartesian` for `G_M`, valid because `Maybe`'s leaf-tracking
map is always a bijection. -/
def TMaybe_onMor_cartesian {X Y : Container} (φ : ContainerMorphism X Y)
    (h : IsCartesian φ) : IsCartesian (Tmap φ) := by
  intro m
  cases m with
  | none => exact ⟨id, fun _ => rfl, fun _ => rfl⟩
  | some s => exact h s

/-! ## 2. `Pf` fails cartesian preservation (finite fibre witness)

The merging witness. Base shapes `S = {a, a'} = Bool`, `T = {c} = Unit`, forward map
`u : S → T` constant (it *merges* `a, a'`). The cartesian morphism is `(u, id)`: fibres
`P s = Q (u s) = Bool` and backward maps `f_s = id` (bijections), so `(u, id)` **is** cartesian.

At the two-leaf shape `m = {a, a'} ∈ Pf S`, the leaves are `lv(m) = {a, a'} = Bool` (for `Pf`,
a leaf *is* its label), and `Pf u · m = {c}` has the single leaf `lv(Pf u · m) = {c} = Unit`.
The leaf-tracking map `u_* : lv(m) → lv(Pf u · m)` sends both leaves to `c`. -/

namespace PfWitness

/-- Leaves of the shape `m = {a, a'} ∈ Pf S`: two of them (for `Pf`, a leaf is its label). -/
abbrev lvm : Type := Bool

/-- Leaves of `Pf u · m = {c}`: one of them. -/
abbrev lvMum : Type := Unit

/-- The base backward maps `f_s : Q (u s) → P s` of the cartesian morphism `(u, id)`; each is
the identity `Bool → Bool` (`(u, id)` is cartesian). Recorded to make `fstar` literally the
reindexed bijection `(∏ f) ∘ (u_*)^*`, not an ad-hoc diagonal. -/
def f : lvm → Bool → Bool := fun _ => id

/-- The leaf-tracking map `u_* : lv(m) → lv(Pf u · m)`. Both leaves of `m` are sent to the
single leaf of `Pf u · m` — the powerset image `{a, a'} ↦ {c}` **merges** them. -/
def ustar : lvm → lvMum := fun _ => ()

/-- The backward position map of `T_Pf (u, id)` at `m`: the ∏-cointerpretation reindexing
`f⋆ : Q⋆(Pf u · m) → P⋆(m)`, i.e. `(∏_b f_b) ∘ (u_*)^*`. With every fibre `= Bool` this is
`(lvMum → Bool) → (lvm → Bool)`, `q ↦ (b ↦ f_b (q (u_* b)))`. Since `f_b = id` and `u_* b = c`
for both leaves, `f⋆ q` is the **constant** function `b ↦ q c` — the diagonal `Bool → Bool²`. -/
def fstar (q : lvMum → Bool) : lvm → Bool := fun b => f b (q (ustar b))

/-! ### The leaf map merges — the non-injective leaf comparison (root cause) -/

/-- **The leaf map merges.** `u_*` sends both leaves of `m` to the one leaf of `Pf u · m`. -/
theorem ustar_merges : ustar false = ustar true := rfl

/-- The two leaves of `m` are genuinely distinct, so `ustar_merges` witnesses a *non-injective*
leaf comparison `u_*` — the "not injective" of the informal target, at the leaf level. -/
theorem leaves_distinct : (false : lvm) ≠ true := by decide

/-- Yet `u_*` is **surjective**: `Pf` never drops a leaf (every leaf of `Pf u · m` is `u` of a
leaf of `m`). This is why the induced product map fails *surjectivity*, not injectivity. -/
theorem ustar_surjective (c : lvMum) : ∃ b : lvm, ustar b = c := by
  cases c; exact ⟨false, rfl⟩

/-! ### The induced backward product map: injective but not surjective -/

/-- `f⋆` (the `T_Pf` backward map) **is injective** — matching the reindexing lemma
(`u_*` surjective ⟹ `(u_*)^*` injective). So cartesian-preservation does *not* fail through
injectivity. -/
theorem fstar_injective (q q' : lvMum → Bool) (h : fstar q = fstar q') : q = q' := by
  funext c
  cases c
  exact congrFun h false

/-- **`f⋆` is not surjective** — matching the reindexing lemma (`u_*` non-injective ⟹
`(u_*)^*` non-surjective). The identity target `id : lvm → Bool` (taking distinct values `false`
at leaf `a` and `true` at leaf `a'`) is not hit: any `f⋆ q` is constant `= q c`, so it cannot
separate the two leaves. This is the `μ = ∪` leaf-merge destroying the fibrewise bijection. -/
theorem fstar_not_surjective : ¬ ∃ q : lvMum → Bool, fstar q = (id : lvm → Bool) := by
  rintro ⟨q, hq⟩
  have h0 : q () = false := congrFun hq false
  have h1 : q () = true := congrFun hq true
  rw [h0] at h1
  exact absurd h1 (by decide)

/-- **`T_Pf` fails cartesian preservation.** For the cartesian morphism `(u, id)` and the
two-leaf shape `m`: the leaf comparison `u_*` merges two distinct leaves (non-injective), and
consequently the backward map `f⋆` of `T_Pf (u, id)` is not surjective — hence not a bijection.
So `T_Pf` does not preserve this cartesian morphism, the `T_M`-side counterpart of the
branching E2′ obstruction (`Containers.BranchingObstruction`). -/
theorem TPf_fails_cartesian_preservation :
    (ustar false = ustar true ∧ (false : lvm) ≠ true) ∧
      ¬ ∃ q : lvMum → Bool, fstar q = (id : lvm → Bool) :=
  ⟨⟨ustar_merges, leaves_distinct⟩, fstar_not_surjective⟩

end PfWitness

end Containers
