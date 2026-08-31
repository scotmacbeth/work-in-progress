# LEAN note — the T_M-side cartesian-preservation boundary (Maybe preserves, Pf does not)

**MacBeth, LEAN session 2026-08-05.** Target from `state/LEAN.md`. Companion to the G_M-side
`FibredTransfer.lean` (which certifies `G_M` preserves cartesian morphisms ∀M). This closes the
"harder T_M-side" that file flagged as the next Lean target.

## What is now machine-checked

File: `lean/Containers/Containers/TMCartesianBoundary.lean` (wired into root `Containers.lean`;
`lake build` green, 46 jobs, **zero warnings**). Axioms: `TMaybe_onMor_cartesian`,
`TPf_fails_cartesian_preservation`, `fstar_not_surjective` = **no axioms**; `fstar_injective` =
`[Quot.sound]` only (funext). No `sorry`, no Choice/propext.

- **Positive (Maybe, cartesian).** `TMaybe_onMor_cartesian` : `IsCartesian φ → IsCartesian (Tmap φ)`
  — *fully general*, not a finite witness. Reuses `IsCartesian`/`TwoSidedInverse` (FibredTransfer)
  and `Tmap`/`TObj` (BiKleisliMaybe). Over `none` the backward map is `id`; over `some s` it is
  `φ.onPos s`, inverse from the hypothesis. This is the exact T_M-mirror of `onMor_cartesian`.

- **Negative (Pf, non-cartesian).** `PfWitness`: merging base map `u:{a,a'}→{c}`, shape
  `m={a,a'}∈Pf`. `ustar_merges` + `leaves_distinct`: the leaf-tracking `u_*` is **non-injective**.
  `ustar_surjective`: `u_*` is surjective (Pf drops no leaf). `fstar_injective` /
  `fstar_not_surjective`: the induced backward product map `f⋆ = (∏ f)∘(u_*)^*` is the diagonal
  `Bool→Bool²` — injective but **not surjective**. `TPf_fails_cartesian_preservation` bundles it.

Together: "`T_M` preserves cartesian morphisms ⟺ `M` cartesian" at the Maybe/Pf boundary
(Theorem 1, `proofs/2026-08-05-crown-gap-closure.md`).

## ⚠ One precision correction to the LEAN.md brief (not a math gap — a wording fix)

LEAN.md item 2 asks to show "`T_Pf(u,f)` backward map is **not injective**". **That is imprecise.**
By the product-reindexing lemma (`crown-gap-closure.md` §0: `φ^*` injective ⟺ `φ` surjective;
`φ^*` surjective ⟺ `φ` injective):

- it is the **leaf comparison** `u_*` that is non-injective (the merge) — proved as `ustar_merges`;
- the induced **product** map `f⋆` then fails **surjectivity**, *not* injectivity, because `Pf`
  never drops a leaf so `u_*` stays surjective ⟹ `f⋆` stays injective (`fstar_injective`).

So the honest statement of the obstruction is "`f⋆` **not surjective** (hence not a bijection)". I
proved both halves so the record pins exactly which one breaks. The conclusion LEAN.md wanted —
`T_Pf` fails to preserve the cartesian morphism — is unchanged and fully certified. Worth
propagating this "leaf-map non-injective ⇒ product-map non-surjective" phrasing into the book/paper
so the two levels aren't conflated (the same care as the `Bag` label-rigidity addendum in
`crown-gap-closure.md` §7).

## Scope / what is NOT here

- The Pf negative is a **finite fibre witness** (the reindexing map at one merging `(u,m)`), in the
  same style as `BranchingObstruction.lean` — not a full `T_Pf : Monad Cont` construction. Building
  the general ∏-cointerpretation `T_Pf` on `Cont` (∏ over a subset, well-defined only because Pf's
  leaves have distinct labels) remains the heavier next rung if we want the general
  `T_M cartesian ⟺ M cartesian` Lean'd rather than pinned at the boundary.
- Registry: `monad-comonad-transfer.json` → new child `lean-tm-cartesian-boundary` = `lean-verified`.
  (Validator still reports one **pre-existing** advisory: root 'proved' over the 'computed'
  `finite-check-both-directions` node — untouched by me.)
