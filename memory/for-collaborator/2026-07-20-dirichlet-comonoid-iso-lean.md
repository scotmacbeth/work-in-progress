# ⊗-comonoid classification is now a full machine-checked isomorphism (Lean)

*2026-07-20. For Rick (and Neil). Registry: `bare-dirichlet-comonoid`, child `lean-converse` = lean-verified.*

Closes the ⊗-comonoid column — the sibling of yesterday's ⊗-monoid iso. I already had the FORWARD map
`DirichletComonoid c → FamilyOfMonoids c` (2026-07-18, `DirichletComonoid.lean`, Quot.sound only).
Today the CONVERSE + both round-trips, so it's a genuine iso
`DirichletComonoid c ≅ FamilyOfMonoids c`:

- **Statement:** a bare ⊗-comonoid in Poly on a container `c` is exactly a **family of monoids** —
  an *arbitrary* monoid `(mul s, one s)` on every direction set `c[s]`. (Answers the Poly/⊗-comonoid
  slice of Niu–Spivak Ch.9 Q5, open in the book. Paper: `2026-07-17-bare-dirichlet-comonoid.md`.)
- **File:** `lean/Containers/Containers/DirichletComonoidConverse.lean` (new; imports `DirichletComonoid`).
- **Decls:** `counitMor`, `comultMor`, `left/right_counit_law`, `coassoc_law`, `toDirichletComonoid`;
  `DirichletComonoid.ext` (law fields are Prop); round trips
  `toDirichletComonoid_toFamilyOfMonoids` (rfl) and `toFamilyOfMonoids_toDirichletComonoid` (the harder one).
- **Verification (re-checked by me, not just the build):** `lake build` green (30 jobs, no warnings),
  no `sorry`/`admit`; `#print axioms` on every new decl = `[Quot.sound]` only (via `funext` for `ext'`),
  and `DirichletComonoid.ext` depends on NO axioms.

**Method note — one prediction was wrong, in our favour.** LEAN.md warned the comonoid converse would
be HARDER than the monoid one: the comult maps *into* `S×S`, so the diagonal is forced, and it expected
a `seq_pos_norm`-style position transport. That's true of the FORWARD direction (where `δ.onShapes` is
only propositionally diagonal, `hdiag`). But the CONVERSE *chooses* `δ` diagonal on the nose, so the
three comonoid laws are **transport-free**: each is `ContainerMorphism.ext' rfl` followed by
`one_mul`/`mul_one`/`mul_assoc` directly (the Dirichlet associator re-brackets the diagonal
definitionally — same as the monoid converse). The only place the transport survives is round-trip 2:
there the recovered `mul` unfolds to `D.comult.onPos` post-composed with the `hdiag`-transport, and I
match it to what `ext'` inserts via shape equality `funext (fun s => (D.hdiag s).symm)`, the two
transports agreeing by `Eq` proof irrelevance and `Prod`/`Unit` η. So `rfl` in the fibre goal.

Whole ⊗ row is now closed as verified isomorphisms both columns: monoid (`DirichletMonoidConverse`) and
comonoid (`DirichletComonoidConverse`). Natural next Lean targets: the category-level statements
`Comon(Cont,⊗,y) ≅ Fam(Mon^op)` / `Mon(Cont,⊗,y) ≅ ...` (morphism side), or the ◁/⊗ double-comonoid
layer.
