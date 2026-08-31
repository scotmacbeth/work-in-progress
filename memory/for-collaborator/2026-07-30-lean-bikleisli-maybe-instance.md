# LEAN 2026-07-30 — biKleisli skeleton instantiated at Maybe; abstract associativity proved

**Status: DONE, sorry-free, zero warnings, full `lake build` green.**

Files: `Containers/BiKleisliMaybe.lean` (new, wired into root `Containers.lean`),
plus one addition to `Containers/BiKleisli.lean`.

## What is now machine-checked

1. **`Maybe : SetMonad`** — `Option` as a `SetMonad` (all laws `rfl`/`cases`-clean).
   `GMaybe := SetMonad.toComonad Maybe` is the transfer comonad `G(S,P)=(S,Option∘P)` for free.

2. **`TMaybe : Monad Container`** — the Ahman–Bauer effect monad `T_Maybe(S,P)=(Option S, P⋆)` with
   the **degenerate arity-≤1 Π-cointerpretation**: `P⋆(none)=PUnit` (empty product), `P⋆(some s)=P s`.
   Functor laws + η/μ naturality + the 3 monad laws, all `ext'`-based, transport-free.

3. **`kappa` + all four mixed-DL axioms E1′–E4′** discharged for Maybe → `mixedDistrib : MixedDistrib
   GMaybe TMaybe`. In particular **E2′ (`distrib_mult`)** — the branching-obstructed axiom — closes,
   because the Π is over ≤1 leaf (`κ` = id on `some`, empty-product η-padding `1→Option 1` on `none`).

4. **`MixedDistrib.acomp_assoc` (ABSTRACT, in BiKleisli.lean)** — general biKleisli associativity from
   the full axiom set E1′–E4′. 7-rewrite chase: E2′@r, μ-nat@h, monad-assoc@s, coassoc@p, δ-nat@f,
   E4′@q, κ-nat@g. **This did not previously exist** — the BiKleisli.lean docstring claimed
   "`BiKleisli.assoc` is also proved" but only the T=Id coKleisli case was there. Docstring corrected.

5. **`arr_unit_left`, `arr_unit_right`, `arr_assoc`** — the full associative arrow category for Maybe,
   the machine-checked half of Theorem A ("Maybe is a genuine category, 1536/1536").

Axioms: `arr_assoc` → `[propext, Quot.sound]`; `mixedDistrib` → `[Quot.sound]`. No `sorry`, no
`Classical.choice`.

## Registry

`proofs/registry/effect-coeffect-arrows.json`: new node `bikleisli-maybe-lean` (`lean-verified`,
lean=`Containers.BiKleisliMaybe.arr_assoc`) under `theoremA-forward-noncrossbranch`; note on
`lean-bikleisli-unit-laws` updated. Validator shows 6 problems — **all pre-existing** (`computed`/
`unclassified` harness leaves under `proved` parents); my additions introduce none.

## Two reusable Lean tricks (for the next instance, e.g. Writer/ℤ₂)

- **Proof irrelevance absorbs non-`rfl` shape identities.** `ext'` leaves a position goal with transport
  `congrFun hs m ▸ p`. When after `cases m` the two shape maps reduce to *definitionally equal* terms
  (e.g. `Option.join (some (some s))` and `some s`), the transport type is `a = a` up to defeq, and Lean's
  definitional proof irrelevance for `Eq` (a `Prop`) makes `congrFun hs m` defeq `rfl`, so the transport
  vanishes. This is why `funext m; cases m <;> rfl` for `hs` composes cleanly with `intro m p; cases m …`.
- **`Option.map id p` needs `cases p`**, not `rfl` (`Option.map id ≠ id` definitionally). The `some`
  branches of E2′/E4′ each need an inner `cases p <;> rfl`.

## What is NOT here (honest boundary)

The **branching** side of Theorem A (Pf/List non-associativity) is still computed-only
(`scratch/monad-comonad-transfer/bikleisli.py`), not formalised — as intended; LEAN.md scoped this to a
single non-branching instance. Writer/ℤ₂ would be the natural next `MixedDistrib` instance (positive
arity-1, non-trivial `A`).
