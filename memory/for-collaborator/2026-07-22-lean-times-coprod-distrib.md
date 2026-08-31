# Lean: `×/+` distributive cell machine-checked (2026-07-22)

**Result.** `Container.prodCoprodDistrib` in
`lean/Containers/Containers/TimesCoprodDistrib.lean` — a full `ContainerIso`

    (P + P') × Q  ≅  (P × Q) + (P' × Q)

the LEFT-variable distributive law of the categorical product `×` over the
coproduct `+` on `Cont`. This is the **fourth** machine-checked cell of the
Hedges four-structure interaction table, after `seqProdDistrib` (`◁/×`),
`seqCoprodDistrib` (`◁/+`), and `dirCoprodDistrib` (`⊗/+`).

**Status.** Sorry-free; `#print axioms` = `[Quot.sound]`; full `lake build` green,
zero warnings. Registry node `hedges-interchange-table.cell-x-plus` set to
`lean-verified`, `lean` field = `Containers.Container.prodCoprodDistrib`.

**Why it was clean (as predicted in LEAN.md).** The categorical product's shape is
`(P.Shape ⊕ P'.Shape) × Q.Shape` and its positions are the *coproduct*
`Sum.elim P.Pos P'.Pos tag ⊕ Q.Pos t` (product of polynomials ⟹ positions add).
The RHS `inl ⟨s,t⟩` summand has positions `P.Pos s ⊕ Q.Pos t`. Since
`Sum.elim P.Pos P'.Pos (inl s)` reduces to `P.Pos s` *definitionally*, the entire
position coproduct matches on the nose — the position map is the identity
`fun w => w`, and both round trips close by `ContainerMorphism.ext_id` +
`cases <;> rfl` / `cases <;> HEq.refl`. **No transport.** The file is essentially
`TensorCoprodDistrib.lean` with `prod` for `dirichlet`; the only difference is that
the second factor beside the tag-pushed fibre is a `⊕` (product positions) rather
than a `×` (Dirichlet positions), and the identity position map handles both.

**Coverage note.** With this cell the "distributes over `+`" column is now fully
Lean-verified for three of the four operators: `◁/+`, `⊗/+`, `×/+`. (The `+/+`
diagonal is the coproduct's own associativity, not a distributive cell.) `×` is
symmetric, so the cell is genuinely two-sided; only the left law is formalised —
it already witnesses the cell, and the mirror follows by product symmetry.

**Contrast reminder.** The two *product-in-the-outer-variable* cells
(`seqProdDistrib`, and any `×/×`) curry a sum-*domain* shape function and carry one
`Sum.elim`-η transport (`Container.sumElim_eta`). The four *coproduct-in-the-outer-
variable* cells never do, because the coproduct shape is already a `Sum` and no η
rule fires. This `×/+` cell is of the clean (coproduct-outer) kind despite `×`
being a product — what matters is which structure is on the LEFT/outer factor.

No gaps found in the paper proof (`2026-07-16-hedges-distributive-table.md`); the
informal argument transferred verbatim.
