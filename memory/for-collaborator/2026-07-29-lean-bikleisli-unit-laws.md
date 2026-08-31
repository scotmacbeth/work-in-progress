# Lean: biKleisli unit laws (effect–coeffect arrows), machine-checked

**LEAN session 2026-07-29.** File: `lean/Containers/Containers/BiKleisli.lean`
(sorry-free, zero warnings, wired into the `Containers` root). Registry:
`effect-coeffect-arrows.json` node `lean-bikleisli-unit-laws` → `lean-verified`,
`lean = Containers.MixedDistrib.unit_left`.

## What is formalised

The **abstract skeleton** of the effect–coeffect *arrow* composition
(`proofs/2026-07-29-effect-coeffect-arrows.md` §1–2), over the self-contained
`Containers.Category` typeclass (Mathlib-free):

- `Comonad`, `Monad`, `MixedDistrib G T` (κ : GT⇒TG, axioms E1′–E4′ + κ-naturality).
- biKleisli arrows `Hom p q = C(Gp, Tq)`, `arrId = ε ≫ η`,
  `acomp = δ ≫ Gf ≫ κ ≫ Tg ≫ μ`.
- **`MixedDistrib.unit_left`** (= paper's E1′) and **`unit_right`** (= E3′).

The two unit-law proofs consume **only** the (co)monad unit laws, ε/η naturality,
and the two *unit* distributive axioms `distrib_unit`/`distrib_counit`. They never
touch E2′/E4′ — this is the Lean witness of the paper's key claim that the unit
laws are the **unconditional** part (hold for all M), while associativity (E2′)
is the branching-obstructed part. `#print axioms`: unit_left/unit_right depend on
**no axioms at all** (pure).

## Anchoring to existing Lean

- `SetMonad.toComonad` repackages the already-verified transfer comonad `G_M`
  (`MonadComonadTransfer.lean`) as a `Comonad Container` — the comonad slot of the
  arrow is machine-checked, not assumed. (Axioms: `Quot.sound`, inherited.)
- `Monad.identity` + `Comonad.coKleisliDistrib` give the **T = Id coKleisli**
  category (the Workers / coeffect-only slice, §3.1), with a full associativity
  proof `coKleisli_acomp_assoc` (coassoc + δ-naturality; `propext` only). So the
  coKleisli category of *any* comonad — in particular `G_M` — is a genuine
  category, in Lean.

## What is NOT formalised (next Lean increment)

- The concrete Ahman–Bauer **`T_M`** (`T_M(S,P)=(MS,P⋆)`, ∏-cointerpretation leaf
  apparatus) and the reverse entwining **`κ`** as concrete `Cont` data. Building
  these is the large piece; the abstract theorem consumes them as the
  `MixedDistrib` interface.
- Hence the **(3)⇔(4) non-branching** step (E2′ holds iff M non-branching) is not
  in Lean — that is the computational result (`entwine.py`/`bikleisli.py`). The
  abstract file discharges the **(1)⇒(3) unit-law direction** of Theorem A.

## Gotchas hit (worth remembering)

1. `conv_lhs`/`conv_rhs` are **Mathlib-only**; core Lean uses `conv => lhs`/
   `conv => rhs`. Navigate into a nested comp with `conv => rhs; arg 2`.
2. `rw`'s keyed matching failed on `← Category.assoc` when the target's type
   index was `(Monad.identity Obj).obj q` (defeq to `q` but not syntactic) coming
   from the coKleisli hom-type. Fix: declare the coKleisli `f,g,h` with **plain**
   `Category.Hom (G.obj p) q` (defeq to `D.Hom p q`), so `G.map f`'s codomain is
   syntactically `G.obj q`. This is the transport-avoidance analogue for rw
   matching — the "reduce the projection in the index" trick.
