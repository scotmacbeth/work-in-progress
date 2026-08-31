# Lean: comonad → monad transfer (the dual) — DONE, sorry-free

**Date:** 2026-07-25 (LEAN session)
**File:** `lean/Containers/Containers/DualTransfer.lean` (wired into root `Containers.lean`)
**Status:** ✅ Sorry-free, zero warnings, full `lake build` green (38 jobs, Lean v4.30.0).
`#print axioms` = `[Quot.sound]` only for all seven results (no `sorry`, no `Classical`).

## What was formalised

The **exact dual** of `MonadComonadTransfer.lean`. For a comonad `W = (W, ε, δ)` on
`Set` (= `Type`), the assignment `H(S,P) = (S, W∘P)` — apply `W` to every fibre, leave
shapes alone — is a **monad** on `Cont`. Its unit and multiplication are `W`'s counit and
comultiplication read backward through the position-contravariance, and its three monad
laws are *literally* `W`'s three comonad laws applied pointwise in the fibre `W(P s)`:

| H monad law | reduces to | W comonad law |
|---|---|---|
| `unit_left`  `μ ∘ η_{HX} = id`   | `ε (δ p) = p`         | left-counit  |
| `unit_right` `μ ∘ H η = id`      | `W ε (δ p) = p`       | right-counit |
| `mult_assoc` `μ_{HX} ∘ μ = Hμ ∘ μ` | `δ (δ p) = W δ (δ p)` | coassoc      |

Every proof is `ContainerMorphism.ext' rfl` (shapes agree definitionally — **no transport**)
followed by `exact W.<law> p`. Same idiom as the done direction; the mirror is perfect.

## Declarations

- `SetComonad` — bundled comonad on `Type` (dual of `SetMonad`): `obj/map`, `map_id/map_comp`,
  counit `ε`, comult `δ`, `ε_natural/δ_natural`, and `left_counit/right_counit/coassoc`.
- `SetComonad.H` (objects), `SetComonad.onMor` (morphisms) + `onMor_id`, `onMor_comp`.
- `SetComonad.unit` (bwd = `ε`), `SetComonad.mult` (bwd = `δ`).
- `unit_natural` (via `ε_natural`), `mult_natural` (via `δ_natural`).
- The three monad laws: `unit_left`, `unit_right`, `mult_assoc`.

## Why this instead of the primary LEAN.md target

LEAN.md's primary target was the **MULT-backward node step** of `FreeUniversal.lean`
(`freeExtPos_mult`). This was the **4th** session on that position half; per the standing
"do NOT bash" discipline and LEAN.md's own instruction, I gave it one look, judged it
still infra-heavy (needs the `split`-reassociation fibre transport threaded through
`mult_assoc_pos`; both `mult_left_unit_pos`/`mult_assoc_pos` inputs already landed but the
node assembly remains), and pivoted to the guaranteed-tractable fallback LEAN.md itself
specified. The MULT-backward node step and backward-uniqueness are **still open** —
see `free-monad-mult-backward-lean.md` for the assembly sketch.

## Grant / book value

Closes Neil's Ch4 ("Monads and Comonads") item-2 transfer in Lean in **both directions**.
Bankable Ch7 artifact. Registry: `monad-comonad-transfer.json` → new child
`lean-dual-transfer` under `coordinate-proof`, `trust: lean-verified`,
`lean: Containers.SetComonad.mult_assoc`. Paper companion:
`proofs/2026-07-25-monad-comonad-transfer.md`; coordinate identifications in
Niu–Spivak arXiv:2312.00990 §6.
