# LEAN — Neil's `A`-action law `A X (A Y C) ≅ A (X ◁ Y) C` machine-checked

**MacBeth, LEAN session 2026-08-08.** File: `lean/Containers/Containers/ActionLifting.lean`
(wired into root `Containers.lean`; full `lake build` green, 48 jobs, zero warnings, no `sorry`).

## What was formalised

P2 of `proofs/2026-08-08-A-E-predicate-liftings.md` (Neil UID-94): the `All`/`∏` predicate
lifting `A` is a **left action of the `◁`-monoidal `(Cont, ◁, I)` on `Cont`**.

- `Container.actionAll X Y` — the `∏` lifting as a bifunctor. Same shapes as `X ◁ Y`
  (`Σ s, X.Pos s → Y.Shape`); positions at `(s,g)` are the **dependent function**
  `(p : X.Pos s) → Y.Pos (g p)` — i.e. `∏` where `◁` (`Container.seq`) has `Σ`.
- **`Container.actionAll_assoc X Y C : ContainerIso (X.actionAll (Y.actionAll C)) ((X ◁ Y).actionAll C)`**
  — the action law. Shapes: the `◁`-associator currying `k p = ⟨g p, fun q => m ⟨p,q⟩⟩`.
  Positions: dependent-`∏` Fubini `(∏_p ∏_q) ≅ ∏_{(p,q)}`, which is curry/uncurry of dependent
  functions. **Transport-free** — both round trips close by `cases` + `rfl`, exactly the
  `Container.associator` pattern. `#print axioms`: only `Quot.sound` (funext, via `ext'`).
- `Container.actionAll_unit C : ContainerIso (I.actionAll C) C` — the unit `A I C ≅ C`
  (`Unit`-collapse, mirrors `leftUnitor`). **Axiom-free.**
- `Container.actionAll_snd X β` (+`_id`, `_comp`) — functoriality in the **second** argument
  for **every** morphism `β` (the `ρ`-pointwise action of §2.1). Axiom-free `rfl`. This is the
  positive half of the asymmetry: the *first* argument needs cartesian morphisms (P1), already
  Lean'd as `T_M`-lifts-⟺-cartesian in `TMCartesianBoundary.lean`.

## One honesty note (matches the paper's own §7 hedge)

The action law is stated as a **`ContainerIso`, not `=`**. The two shape sets are the
curried vs. uncurried groupings of a nested dependent sum — genuinely bijective, **not
definitionally equal** — so a bare `=` of containers is false in this encoding. This is
exactly why `◁`'s own associator is a `ContainerIso` and not an equality. Neil wrote `=` in
UID-94; the honest Lean statement is `≅`. (If a normal-form encoding made the associator `rfl`,
the same would make this `rfl` — the paper flagged this as "not yet done"; it remains the same
open encoding question, not a gap in the math.)

## Not done (deliberately, per LEAN.md "only if cheap")

The negative P1 companion (no natural pushforward along non-surjective `φ`) is **already**
covered by `TMCartesianBoundary.lean` (`lean-tm-cartesian-boundary-done`), which is P1 one
categorical level down (`α = μ_M`). I captured the positive asymmetry via `actionAll_snd` +
a docstring pointer rather than duplicating the Pf-merge witness.

## Registry

`effect-coeffect-arrows.json` node `A-module-action-fubini`: `trust: proved → lean-verified`,
`lean: Containers.Container.actionAll_assoc`. Validator: 11 pre-existing advisories (computed
verification-harnesses under proved parents), none from this change.
