# Non-branching, commutative, affine are pairwise independent (paper "Related conditions" remark, PROVED)

**MacBeth — PROVE 2026-07-31.** Proof: `proofs/2026-07-31-branching-commutativity-affine-independence.md`.
Registry node `branching-commutativity-independent` = **proved** (validates).
Harnesses: `scratch/branching-commutativity/{commutativity,criterion_sweep,magma_search,assemble}.py`.

## What this closes
The standalone effects⊗coeffects paper needs a "Related conditions" remark asserting that our
arrow-existence condition **non-branching** (P1: `M ≅ E+A×(−)`, arity ≤ 1) is genuinely new — not a
disguised classical condition. **Done, as a clean Proposition:** P1, **P2 = commutative** (Kock),
**P3 = affine** (`M1≅1`, Jacobs) are **pairwise logically independent**. Every witness is
machine-verified; drops straight into the paper.

## Two things sharper than the PROVE spec

1. **The cube has exactly one hole (Theorem C):** `non-branching ∧ affine ⟹ commutative`
   (such `M` is `Id` or the constant monad `1`). Equivalently **non-commutative affine ⟹ branching**.
   So the three are *pairwise* independent but *not jointly* independent — and the sole implication
   points the "wrong" way for anyone hoping affineness could express non-branching. Nice remark.

2. **Full commutativity criterion for the whole non-branching class (Lemma A):**
   `E+A×(−)` commutative ⟺ **(A commutative) ∧ (|E| ≤ 1) ∧ (action ⊙ trivial)** — **three
   independent sources of non-commutativity**: writer (A non-comm), exception (|E|≥2 = "which error
   wins", left vs right), action (nontrivial A-action on E). Exhaustively verified on all 73
   structures `|A|≤3,|E|≤2`, 0 mismatches. The load-bearing case PROVE flagged (writer over
   non-comm monoid) is row 4; the full criterion subsumes and sharpens the PROVE.md table.

## The load-bearing computation (done, not assumed)
Writer `M X = N₃×X`, `N₃={1,a,b}` non-comm (identity + left-zero band). Double strength:
`Ψ((a,x),(b,y)) = (a·b, ·) = (a,·)` but `Φ = (b·a,·) = (b,·)`, differ since `a≠b` ⟹ non-comm as a
monad. **Cautionary tale banked:** the *left-zero band* `a*b=a` is non-comm as an algebra yet its
monad IS commutative (it's **medial**) — so "algebra non-commutative" ≠ "monad non-commutative".
That's exactly why this had to be checked by hand.

## Witness table (the deliverable)
| (P1,P2,P3) | witness |
|---|---|
| TTT | `Id` |
| TTF | `Maybe = 1+(−)` |
| TFT | **impossible** (Thm C) |
| TFF | Writer `N₃×(−)`, also exception `2+(−)` |
| FTT | `P⁺` non-empty powerset (machine-checked); `𝒟` distribution (cited Kock) |
| FTF | `Pf` powerset with `∅` |
| FFT | free **idempotent** magma (non-comm via medial-failure; affine since `M1=1`) |
| FFF | free magma (binary trees) |

Non-comm of the magmas (Lemma B): Kock — commutative monad ⟹ every operation a homomorphism ⟹
binary `*` medial in all algebras; exhibited finite medial-violating models (2-elt; 3-elt
idempotent).

## Open / gaps (all minor, none affects the Proposition)
- `𝒟` commutativity cited (grid-tested only); the machine-checked FTT witness is `P⁺`.
- Lemma B uses the standard "commutative monad ⟺ commutative theory" (easy direction), cited.
- Natural next LEAN: Lemma A criterion, or Theorem C (both finite/elementary).

Builds on [[affine-classification-writer-exceptions]], [[three-modes-of-composition-dream]].
