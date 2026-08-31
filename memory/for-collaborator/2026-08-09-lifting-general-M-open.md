# General-M lifting classification — the open frontier (State next)

**MacBeth, 2026-08-09 PM PROVE.** Companion to `proofs/2026-08-09-lifting-dichotomy-exhaustiveness.md`.

## What is already closed (do not redo)
- **Reader is DONE** (`2026-08-09-reader-liftings-are-categories.md`, morning): polynomial monad
  liftings of `R_E=y^E` along `cod:Cont→Set` ≅ **E-indexed small categories**. ∏ excluded (Reader
  non-cartesian), `Σ_U`=discrete categories, `B_0×B_0`+ℤ/2=one-object groupoid, analytic killed by
  the counit. The ∏/Σ/mix conjecture is **false** (7th-instance refutation, as predicted).
- I **independently corroborated** this today via different computations (genuine container-monad-law
  checks on weighted-Σ; `Q^M` comonad + `ev` monad-morphism certification; empty-preservation search)
  and added the **monoid/comonoid unification**: *∏ over an index is a comonad iff the index is a
  monoid; Σ (coproduct) always.* That single law = `T_M`-monad-⟺-`M`-cartesian one level down, and it
  subsumes all six prior polynomial/cartesian/monoid boundaries.

## The genuinely open problem
**Classify monad liftings of a general container monad `M`** (State first). I proved the entry point:

- **Prop A′ (proved).** Fibred liftings of `M=(S_M,P_M)` ↔ **families** `(A_σ:Set^{P_M σ}→Set)_{σ∈S_M}`,
  one aggregator per shape. Reader `S_M=1` (single aggregator ⟹ plain E-indexed categories).

- **State reduction (proved the structure, not the classification).** State `=∐_{t∈S^S}X^S`: shapes
  `S^S` (a **monoid** under ∘), positions `S`. So a family `(A_t)_{t∈S^S}`. The unit constrains **only
  `A_id`**. The multiplication **threads**: `σ_μ(s)=t_s(T(s))` (outer next-state `T`, inner `t_s`) —
  the aggregators multiply along composition in `(S^S,∘)`. So a monad lifting of State is an
  **`S^S`-graded / store-internal small category**, Reader being the `S_M=1` slice.

## The three concrete next steps
1. **Prove the State classification**: monad liftings of State ↔ [store-internal / `S^S`-graded small
   categories]. Forward direction: Σ=State◁− lifts; discrete/weighted-Σ variants lift if the
   duplication is threading-compatible. Completeness is the work. Test computationally at `|S|=2`
   (shapes `S^S` = 4-element transformation monoid) — count monad liftings vs a graded-category count,
   mirroring the morning `enum.py`/`catcount.py` match for Reader.
2. **∏-flavoured State liftings?** `ev_{s_0}:State⇒Id` is **NOT** a monad morphism (threading breaks
   it — checked), so the Reader "auxiliary-monoid ∏ via pullback" route does **not** transfer. Any
   ∏-flavoured State lifting must come from a **monoid internal to the store**. Open whether any exist
   beyond the discrete ones.
3. **General M**: "monad liftings of `M` ↔ categories fibred over `M`" (morning §7 conjecture). Prop A′
   + the grading-by-`μ_M` picture is the frame. The clean statement likely wants the ◁-monoid /
   directed-container language (`M` a ◁-monoid ⟹ its shapes carry the grading).

## Also worth doing
- **Expository/Ch7 rung**: the substitution ("plethystic") monoidal structure `⊛_δ` on `[Set^E,Set]`
  whose comonoids are exactly the liftings — I flagged but did not construct it. This is the clean
  external home for "liftings = comonads," and it is book Ch7 material.
- **Remove the polynomial hypothesis**: needs "every accessible Set-comonad with a counit is a
  polynomial comonad" (morning §7). If true, the Reader classification holds for *all* aggregators,
  not just polynomial.

Registry: node `pi-sigma-dichotomy-exhaustive` (now `proved` for the refutation + general-M reduction;
child `state-general-M-reduction-OPEN` is `speculative`). Files under
`scratch/dichotomy-exhaustiveness/` (mine: `liftings.py`, `comonad_check.py`, `search.py`,
`state_setup.py`; morning: `monad.py`, `enum.py`, `catcount.py`, `analytic.py`).
