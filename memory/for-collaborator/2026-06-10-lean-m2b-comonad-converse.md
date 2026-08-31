# Lean M2b — the CONVERSE: comonad ⟹ directed container (DONE)

**Status:** ✅ Compiles, **zero sorry, zero warnings**. Axioms: only `Quot.sound`
(via `funext`/`eq_of_heq`); the linchpin `cShape_eq` is **axiom-free**. Lean
v4.30.0, no Mathlib.

**File:** `lean/Containers/Containers/ComonadConverse.lean` (added to `Containers.lean`).

## What this closes
M2-forward (`Directed.lean`) proved *directed container ⟹ comonad laws*. This is the
missing converse — the conceptually harder **extraction** direction. Together they
make the container⇔comonad half of the equivalence chain a machine-checked **iso**,
not one implication.

## The result, precisely
- `ContainerComonad extends Container` bundles the **represented** comonad data:
  `e : (s)→Pos s` (counit root), `cShape : S→S`, `cSub`, `cVal` (the comult's
  defining morphism `C ⇒ C∘C`). Justified by the representation theorem (M1,
  `Basic.lean`): every nat-trans of extensions is a container morphism.
- `IsComonad` = the three genuine comonad-law equalities on the defined
  `counit`/`comult` (stated exactly dual to `Directed.lean`).
- `cShape_eq` (**the linchpin**): right counit law ⟹ `cShape s = s`. The comult
  cannot change the outer shape. Proof: probe `(map ε)∘δ = id` at `⟨s,id⟩`, take
  `Sigma.fst`. One line, no axioms.
- `toDirectedContainer : IsComonad → DirectedContainer` with D1–D5 proved.
- **Both round-trips**: `toDirectedContainer_counit`/`_comult` (forward∘recover = id
  on the comonad) and `toContainerComonad_toDirectedContainer` (recover∘forward = id
  on directed containers, **by `rfl`** — the cShape transports vanish by proof
  irrelevance). This is the `DirectedContainer ≃ container comonad` packaging the
  trigger asked for.

## The two ideas that made it tractable
1. **`comult_norm`** — normalise the comult into cShape-free form *once*, absorbing
   every `cShape` cast. Proved via `Ext.norm_aux`, a lemma with **free** `t,s,sub,val`
   that `cases hc` closes — sidestepping the occurs-check that blocks `subst`bing
   `cShape s = s` directly (s occurs in `cShape s`). After this, D1–D5 derive exactly
   like the forward proof run backwards, with only the intrinsic D1/D4 transports.
2. **`Ext.mk_inj`** — the destructor dual to `Ext.ext_eq`: a `Sigma` equality yields a
   shape eq + a transported value eq (`injection` + `subst` + `eq_of_heq`). D1/D4 read
   the shape half, D2/D3/D5 the value half. Nested mk_inj peels coassoc 3 levels deep.

Gotcha worth remembering: `simp only [Ext.map, comult_norm]` got **stuck** — simp
unfolded `Ext.map` into `Sigma` projections *before* rewriting the inner comult, so
comult_norm never fired on the LHS. Fix: a `rfl`-lemma `Ext.map_mk` that only matches
`Ext.map f ⟨s,g⟩`, forcing comult_norm (which produces the pair) to fire first.

## Honest scoping note (one gap to flag, not a bug)
`ContainerComonad` is the **represented** form of the comonad data, not wired to an
abstract `Comonad`/`CategoryTheory`-style object. Faithfulness rests on M1's
representation theorem (naturality of the induced maps is automatic;
`ExtNatTrans ≅ ContainerMorphism` gives completeness). Closing the last inch — stating
`IsComonad` over arbitrary `ExtNatTrans` and extracting the data via
`ExtNatTrans.toMorphism` — is a mechanical refactor I deliberately skipped to keep the
proof focused; the mathematical content (cShape_eq + D1–D5) is unaffected. Worth doing
if/when we want the statement to read "comonad on the endofunctor" with no appeal to
the rep theorem in the reader's head.

## Grant framing
The equivalence chain is the theory spine; a one-directional Lean proof was a visible
gap in the "theory is machine-checked" claim. M1 + M2 (both directions) + M4 now stand
verified. Next Lean targets (see updated LEAN.md): ZS1–ZS4 ⟺ associativity, or a
Mathlib `Cofunctor` contribution.
