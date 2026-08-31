# LEAN done — the general `T^Σ_M = M ◁ −` identity + "◁-monoid ⟹ monad on Cont", generically

**MacBeth, LEAN session 2026-08-09.** For Robin / Neil.

## What was formalised

`lean/Containers/Containers/SigmaLift.lean` (wired into the root `Containers.lean`;
**full `lake build` green, zero warnings, axiom-clean — only `Quot.sound`, same as
`Free.lean`; no `sorryAx`, no `Classical`**).

Formalises the headline of `proofs/2026-08-08-sigma-monad-is-triangle-monoid.md`
(Thm 3.1, direction `2 ⟹ 1`), the unit the 08-08 dream flagged as "LEAN the
general identity once."

1. **Prop 2.1 — `Container.sigmaLift_eq_seq`**: `T^Σ_M(C) = M ◁ C`, a **definitional
   equality** (`rfl`, depends on *no* axioms). `Container.sigmaLift` is the Σ-lifting
   written in the informal coordinates (shapes `M(S_C)`, positions
   `∐_{b ∈ lv(m)} P_C(x_b)`); once `M` is a container its leaves at `(s,g)` are
   `M.Pos s`, so the leaf-indexed sum *is* the composite-polynomial position sum.
   No ContainerIso needed — it is literally `Container.seq M C`.

2. **The general theorem — `Container.sigmaMonad`**: every `◁`-monoid `M`
   (`Container.Monoid`, from `Free.lean`) makes `M ◁ −` a **monad on `Cont`**.
   - `η^Σ_C = η_M ◁ C` through the left unitor (`Container.sigmaUnit`);
     `μ^Σ_C = μ_M ◁ C` through the associator (`Container.sigmaMult`).
   - Naturality of both families in `C` is `rfl` (`sigmaUnit_natural`,
     `sigmaMult_natural`).
   - The three monad laws (`sigma_monad_left_unit`, `..._right_unit`, `..._assoc`)
     each reduce to `M`'s `◁`-monoid law (`hM.left_unit` / `right_unit` / `assoc`)
     **whiskered by `C`** — via `congrArg (whiskerRight · C)` — glued with the
     monoidal coherence of `(Cont, ◁, I)`, which is transport-free here so every
     non-monoid-law step is `rfl`. The associativity proof is the pentagon corner:
     both sides normalise (associator naturality) to a common `μ_M`-tail, the
     pure-associator prefixes coincide by the pentagon, and `hM.assoc` bridges the
     two orderings of the two `μ_M`'s.
   - Packaged as a lightweight `Container.SigmaMonad` record (unit, mult, 3 laws).

3. **Reader & State corollaries — the rung-collapse.**
   - `Container.readerMonoid E` : the **diagonal `◁`-monoid on `E`**
     (`Reader = y^E = (Unit, fun _ => E)`; μ backward = `e ↦ (e,e)`). All three
     `◁`-monoid laws by `rfl`.
   - `Container.stateMonoid S` : the **store `◁`-monoid on `S`**
     (`State = (S^S, fun _ => S)`; μ forward `s ↦ g s (t s)`, backward
     `s ↦ (s, t s)` — threading). All three laws by `rfl`.
   - `Container.readerSigmaMonad` / `stateSigmaMonad` : the Σ-lifting monads,
     **one-line specialisations** `sigmaMonad (readerMonoid E)` /
     `sigmaMonad (stateMonoid S)`.

   This is the genuine consolidation the LEAN.md asked for: the two bespoke
   per-monad rungs in `ReaderStateOutsidePiMendler.lean` §§7–10 are now *corollaries*
   of one general theorem, welding the proof-relevance survivor onto the
   directed-container / composition-monoid spine as a machine-checked identity of
   endofunctors.

## Registry

Added `lean-sigma-triangle-monoid-general` (**trust `lean-verified`**,
`lean = Containers.Container.sigmaMonad`) under `sigma-monad-iff-container-monad`
in `proofs/registry/effect-coeffect-arrows.json`. `registry_validate.py` reports
no problems referencing this node (the other 14 warnings are pre-existing
`computed`/`speculative` children under `proved` parents, untouched by me).

## Nothing left open in this unit

No sorries. The only thing NOT done (and out of scope for a lean session) is
retiring the old bespoke `ReaderStateOutsidePiMendler.lean` §§7–10 declarations —
they still stand and are still `lean-verified`; the general theorem now subsumes
them, so a future cleanup could delete them and repoint
`sigma-reader-diagonal-coherent` / `sigma-state-threading-coherent` at the
corollaries. I left them in place to avoid touching a green file mid-session.

## One design note for Neil's Ch7 lead-ordering question

The Lean bears out the "lead with `T^Σ_M = M ◁ −`" framing: the identity is *defeq*
(`sigmaLift_eq_seq` needs no axioms at all), and every hard step is just monoidal
coherence being `rfl` in `Cont` plus one whiskered monoid law. The monad-ness of
the Σ-lifting genuinely *is* "`M` is a `◁`-monoid," nothing more — exactly the
book claim.
