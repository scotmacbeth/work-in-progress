# Lean: bare ⊗-comonoid → family of monoids (FORWARD direction — COMPLETE, sorry-free)

**2026-07-18 LEAN session (continued).** Target from `state/LEAN.md`: forward direction of the bare
Dirichlet-comonoid classification (`proofs/2026-07-17-bare-dirichlet-comonoid.md`, registry
`bare-dirichlet-comonoid`). Module: `lean/Containers/Containers/DirichletComonoid.lean`
(wired into root `Containers.lean`; full `lake build` green).

## Status: DONE

`toFamilyOfMonoids : DirichletComonoid c → FamilyOfMonoids c` is **fully machine-checked, sorry-free**.
`#print axioms Container.DirichletComonoid.toFamilyOfMonoids = [Quot.sound]` (no `sorry`, no
`Classical`/`propext`). Registry `bare-dirichlet-comonoid` now carries child `lean-forward` at
`lean-verified` (lean=`Container.DirichletComonoid.toFamilyOfMonoids`); `registry_validate.py` clean
for that node.

Everything that was already done earlier this session stands: `DirichletComonoid`/`FamilyOfMonoids`
structures; shape-diagonal forcing `fst_diag`/`snd_diag`/`hdiag`; `mul`/`one`/`mul_apply`; both unit
laws `one_mul_law`/`mul_one_law`.

## The one remaining piece — associativity — is now closed

The earlier plan (a `depFunTransport`-style "double-transport lemma" over `fun a => comult.onPos a`)
was the wrong shape and would have been ~40 lines of transport bookkeeping. **Discarded.** The clean
proof instead lifts associativity out of the comonoid entirely:

```lean
theorem Container.dirichlet_mul_assoc {C} (δ : ContainerMorphism C (C ⊗ C))
    (hd : ∀ a, δ.onShapes a = (a, a))
    (hco : (δ.comp (dir₂ δ (id C))).comp (dirAssociator C C C).hom = δ.comp (dir₂ (id C) δ))
    (s) (x y z : C.Pos s) :
    dirMulOf δ hd s (dirMulOf δ hd s x y) z = dirMulOf δ hd s x (dirMulOf δ hd s y z) := by
  obtain ⟨fS, fP⟩ := δ                       -- δ's shape/pos maps become FREE variables
  have hfS : fS = fun a => (a, a) := funext hd
  subst hfS                                  -- now δ.onShapes s is LITERALLY (s,s)
  exact onPosOfEq hco s ⟨x, ⟨y, z⟩⟩          -- coassoc read at ⟨x,⟨y,z⟩⟩ IS associativity
```

`D.mul` is **definitionally** `Container.dirMulOf D.comult D.hdiag`, so `mul_assoc_law` is a bare
application `dirichlet_mul_assoc D.comult D.hdiag D.coassoc s x y z`.

**Why it works.** The whole difficulty was that `δ.onShapes s` is diagonal only *propositionally*,
and coassociativity reads the comult at *three* indices (`s` and the two shifted `(δ.onShapes s).i`).
Making `δ` a free variable lets `cases` split its maps; `funext hd` upgrades the pointwise diagonal
law to the *function* equation `δ.onShapes = fun a => (a,a)`, which `subst` eliminates. After that
every shape index is syntactically `(s,s)`, all three comult applications are the same `fP s`, and
every residual shape transport is `rfl` by **definitional proof irrelevance for `Eq`**. The associator
`α.hom` re-brackets `⟨x,⟨y,z⟩⟩ ↦ ⟨⟨x,y⟩,z⟩` definitionally, so `onPosOfEq` on `hco` at `⟨x,⟨y,z⟩⟩`
literally states `fP s ⟨fP s ⟨x,y⟩, z⟩ = fP s ⟨x, fP s ⟨y,z⟩⟩`.

## Transferable principle (worth remembering)

> When a dependent index `f s` blocks `subst` because `s` occurs inside `f s`, don't build
> per-occurrence transport lemmas. **Generalise / `cases` the whole `f`** (here: the morphism `δ`
> supplying `f = δ.onShapes`), then `subst` the *function-level* law. All the propositional-transport
> pain evaporates because the index becomes syntactically concrete.

This is strictly cleaner than the `dirPosTransport`/`depFunTransport`/`castSymmCast` family used for
the unit laws — those are still fine and still in the file, but for a multi-index law the free-morphism
lift is the move.

## Follow-ups (natural, not started)
- **Converse** `FamilyOfMonoids → DirichletComonoid` (assemble ε from `one`, δ diagonal-on-shapes with
  backward map `mul`; §§3–4 of the note read backwards). Good next LEAN target.
- **Category level** `Comon(Cont,⊗,y) ≅ Fam(Monᵒᵖ)` (Appendix of the proof note) — needs the
  morphism/naturality layer.
