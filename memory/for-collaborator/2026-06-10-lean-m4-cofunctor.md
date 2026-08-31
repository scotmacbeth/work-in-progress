# Lean M4 — DCont morphisms are cofunctors: `DCont ≅ Cof`: DONE

Branch `lean-m4-cofunctor` (off `lean-m2-comonad`, so it carries M1+M2).
File: `lean/Containers/Containers/Cofunctor.lean` (208 lines).
Formalises `projects/proofs/2026-06-09-dcont-morphisms.tex` at the **morphism level**.

## What is proved
- `DContMorphism C D` — container morphism `(f, f♯)` with `f♯` *contravariant*
  on positions, plus laws **M0/M1/M2**. M2 (shift homomorphism) transports the
  position `k` along M0, exactly as D5 transports along D4 in M2-the-comonad.
- `Cofunctor C D` — cofunctor of the presented categories, laws **C0/C1/C2**,
  phrased with dictionary vocab `cod` (=sub), `idHom` (=root), `after` (=shift).
- **Hom-set bijection `DCont ≅ Cof`**: `DContMorphism.toCofunctor` /
  `Cofunctor.toDContMorphism`, with `toCofunctor_toDContMorphism` and
  `toDContMorphism_toCofunctor` both `rfl`. The structures carry *identical data*
  — M0/M1/M2 are definitionally C0/C1/C2 under the dictionary. (This is the
  paper's Lemma 2.5 "literally the same data", machine-checked.)
- **Cof is a strict category**: `Cofunctor.id`, `Cofunctor.comp`, and
  `id_comp` / `comp_id` / `comp_assoc` all hold by `rfl`.
- **Φ = (·).toCofunctor is functorial**: `DContMorphism.toCofunctor_id`,
  `DContMorphism.toCofunctor_comp` (both `rfl`). Identity-on-objects +
  bijective-on-homs + functorial ⇒ isomorphism of categories `DCont ≅ Cof`.

Zero `sorry`, zero warnings. `#print axioms` on the round-trips, `comp`,
`comp_assoc`, `toCofunctor_comp` → **no axiom dependencies at all** (fully
constructive; not even `Quot.sound`, because no `funext` is needed here).

## The one design decision worth knowing
The only genuinely dependent step is composition of cofunctors. The composite
lift is `m ↦ φ.lift s (ψ.lift (φ.obj s) m)`; its C2 law needs the inner position
`k` re-transported across both factors' C0 equalities. All of that is isolated in

  `Cofunctor.comp_transport (ψ) (e : y = x) (e₂ : ψ.obj x = z) (k) :`
  `  e.symm ▸ (ψ.lift x (e₂.symm ▸ k))`
  `    = ψ.lift y (((congrArg ψ.obj e).trans e₂).symm ▸ k)`

proved by `subst e; subst e₂; rfl` — the standard "make the shape equalities into
bound variables so `subst` fires" move. With that lemma the whole composite-C2
proof is a 2-line `rw [ψ.c2, φ.c2, comp_transport]`. C0 and C1 of the composite
are transport-free (`congrArg` + `Eq.trans`).

## Design note: where is `cat C`?
The library has no standalone `SmallCategory` structure; a directed container *is*
the category presentation (objects = shapes, morphisms-out-of-s = positions). So
`Cofunctor C D` reads its two `DirectedContainer` arguments as the categories they
present, via `cod`/`idHom`/`after`. That is why `DCont ≅ Cof` is identity-on-
objects and the hom-bijection is `rfl`: faithful to the paper, which stresses the
two structures are the *same data* under one map. The content that is *not* free
— composition with contravariant lifts and its transport — is fully proved.

## Suggested follow-ups (M5+)
- Object-level `DCont ≅ Cat` (Theorem 4.1 of directed-categories.tex) is still
  only on paper; formalising the round-trip directed-container ⇄ category would
  let `Cofunctor` be stated against a real `SmallCategory` and make the iso a
  theorem rather than a definitional identity. Heavier (assoc/unit from D1–D5).
- The foil (Prop 2.13): covariant-position morphisms `↦` functors, as a contrast
  structure `OpMorphism` with N0/N1/N2. Cheap; nice to have for the grant.
