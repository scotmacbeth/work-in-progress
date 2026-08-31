# Reader Σ-container monad lifting — Lean-verified (2026-08-08)

**File:** `lean/Containers/Containers/ReaderStateOutsidePiMendler.lean`, §§7–8 (new).
**Certifies:** `proofs/2026-08-07-sigma-monad-proved.md` §4 (Reader, diagonal section).
**Builds:** `lake build Containers.ReaderStateOutsidePiMendler` — 0 errors, 0 warnings.
**Axioms:** `reader_sigma_monad_lifting`, `reader_sigma_assoc`, `reader_proof_relevance_triptych`
all report **"does not depend on any axioms"** (no `decide`, no `propext`, no `sorry`).

## What is now machine-checked

The proof-relevant **Σ-container lifting** of Reader (`E = Bool`) is a **monad** on `Cont`, for an
**arbitrary** base container `(S, P)` with `P : S → Type` (genuinely proof-relevant — `Type`, not
`Prop`). Keeping `S, P` general realises the "all containers `C`" quantifier of the reduction
Corollary 2.3, so this is stronger than fixing the base to `Lbl`.

Declarations:
- `RSig P m` / `RSigSig P mm` / `RSig3 P mmm` — the `Sigma` position functors `P^Σ`, `(P^Σ)^Σ`, its
  triple.
- `rEtaBwd` — unit backward = **codiagonal fold** `⟨b,p⟩ ↦ p` (unconditional, no chosen leaf).
- `rMuBwd` — mult backward = reindex along the diagonal section `σ(mm,L)=(L,L)`, `⟨L,p⟩ ↦ ⟨L,L,p⟩`.
- `etaSigTC` / `TetaSig` / `muSigTC` / `TmuSig` — the four lifted backward maps (`η^Σ_{TC}`,
  `T(η^Σ)`, `μ^Σ_{TC}`, `T(μ^Σ)`) needed for the law composites.
- `reader_sigma_left_unit` **(U1)**, `reader_sigma_right_unit` **(U2)**, `reader_sigma_assoc`
  **(A)** — each the backward composite equated by `rfl` (Reader's diagonal is constant, so
  everything is definitional). `reader_sigma_monad_lifting` bundles all three.
- `reader_proof_relevance_triptych` — the payoff: at the **same** Reader monad, `∏` fails
  (`reader_kappa_not_total`), `□` holds (`reader_box_mult`), `Σ` holds (`reader_sigma_*`).

## Honest scope / what remains

1. **State Σ side not yet Lean'd.** Paper §5 (threading section `σ(mm,s)=(s,h(s))`, and (U1) via
   `η`'s next-state = identity). It is the natural next LEAN rung; expect it to need one non-`rfl`
   step (threading assoc = State's own `μ`-assoc) but still axiom-free over `Bool`.
2. **This is the concrete-per-monad certificate, not the general Thm 3.1.** As in the existing DROP
   / □ sections, we verify the reduced index identities directly for Reader rather than rebuilding
   the 2-category `Cont` + the faithfulness Lemma 2.2 abstractly. The `rfl` proofs *are* the index
   identities (U1)/(U2)/(A) instantiated at Reader's diagonal — faithful to the paper, but the
   general "reverse-total + coherent section ⟹ Σ-monad" statement (paper §6, open) is not formalised.
3. No registry node `sigma-monad-coherence` exists as a JSON file, so nothing was flipped to
   `lean-verified` there. If one is created, this file is its `lean` witness
   (`reader_sigma_monad_lifting`).
