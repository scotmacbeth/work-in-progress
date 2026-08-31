# ⊗-monoid classification is now a full machine-checked isomorphism (Lean)

*2026-07-20. For Rick (and Neil). Registry: `dirichlet-monoid-classification`, child `lean-converse` = lean-verified.*

Completes the ⊗-monoid column. Yesterday I had the FORWARD map `DirichletMonoid c → ShapeMonoidOplaxFibres c`
(zero axioms). Today the CONVERSE + both round-trips, so it's a genuine iso
`DirichletMonoid c ≅ ShapeMonoidOplaxFibres c`:

- **Statement:** a ⊗-monoid in Poly on a container `c` is exactly a monoid `(S,·,e)` on the shape set
  plus an **oplax** monoidal functor `(S,·,e) → (Set,×,1)` on the fibres.
- **File:** `lean/Containers/Containers/DirichletMonoidConverse.lean` (new; imports `DirichletMonoid`).
- **Decls:** `unitMor`, `mulMor`, `left/right_unit_law`, `assoc_law`, `toDirichletMonoid`, and both
  round-trips `toDirichletMonoid_toShapeMonoidOplaxFibres` / `toShapeMonoidOplaxFibres_toDirichletMonoid`.
- **Verification (re-checked by me, not just the build):** `lake build` green (29 jobs), no `sorry`/`admit`,
  `#print axioms` on both round-trips = `[Quot.sound]` only (enters via `funext` for `ext'`).
- **Method note:** each law goes through `ContainerMorphism.ext'` with the shape equality = the monoid
  axiom (`one_smul`/`smul_one`/`smul_assoc`) and the fibre goal = the oplax coherence
  (`phi_one_smul`/`phi_smul_one`/`phi_assoc`) matched on the nose by `Eq` proof irrelevance — the clean
  mirror of the forward `onPosOfEq`. Both round-trips are `rfl` (data defeq up to `Prod`/`Unit` η, laws
  Prop-irrelevant). No bespoke transport lemmas.

The ⊗-comonoid column's converse is still open (the `bare-dirichlet-comonoid` sibling); this is the
monoid side closed. Whole ⊗ row: forward both sides + monoid iso done.
