# Write session 2026-08-08 (second) — Book: A/E predicate liftings, containers-chapter HOME

Target file: `books/category-of-containers.tex`.
Task (WRITE.md): Neil GREENLIT (UID-95) a section led by HIS A/E predicate liftings (UID-94 source
note). Home = "containers chapter, usable later in monads/comonads chapter." Retire "proof-relevant"
from prose (keep once, parenthetically).

## Placement decision
New section at the END of the "Algebraic structure on Cont" chapter (`ch:algebra`), inserted
immediately before `\chapter{Monoids and comonoids...}` (line ~1559).
Rationale:
- Needs ◁ (composition product) to state E=◁ — ◁ introduced in this same chapter (menagerie, §751).
- "Usable later in monads/comonads chapter" = A=T_M + the two fibrations, which the DEEP teachbox
  at `sec:moncomon-fibration` (ch:moncomon) already develops (the 08-08a rewrite). So this section
  FORWARD-references that; it must NOT duplicate the 2×2 grade / Σ-monad / Orestis derivation.
- Ends the structural-on-Cont chapter on a bridge into monoids/comonoids and monads.

## What this section adds that the deep teachbox does NOT
1. Neil's A/E predicate liftings by name (All / Exists), defined from the extension functor +
   positions — his UID-94 starting point, in his words.
2. E = ◁ proved cleanly, with the prompts/replies reader hook.
3. THE NEW RESULT (this cycle, proofs/2026-08-08-A-E-predicate-liftings.md P2):
   the action law  A X (A Y C) = A (X◁Y) C  — A is a left module of (Cont,◁,y). Fubini
   ∏_p∏_q=∏_{(p,q)}. Contrast E X(E Y C)=E(X◁Y)C = ◁-associativity. Neil's "debate prep" intuition.
   TAG [MacBeth, proved].
4. The cartesian-only boundary stated crisply as Neil's flag ("can't define A on polynomial
   functors") = variance of ∏ (needs φ⁻¹) — with a pointer to sec:moncomon-fibration for T_M.

## Provenance
- E=◁ monoidal: [MacBeth, Lean-verified] (lean-monoidal-coherence-done); identification immediate.
- Boundary (A cartesian-only): [MacBeth, proved] proofs/2026-08-07 + this cycle P1.
- Action law P2: [MacBeth, proved] proofs/2026-08-08-A-E-predicate-liftings.md.
- Cites: Spivak21 (◁), HermidaJacobs98 (two fibrations), AhmanBauer24 (∏=T_M), all in bib.

## Honesty caveats to carry (from proof file §7)
- P2 stated as canonical iso; strict-`=`/`rfl` is a flagged next LEAN rung (not claimed here).
- Module pentagon/triangle coherence NOT verified — say "the two equations (assoc + unit)"; do not
  claim full coherence. Object-level associativity + unit only.
- Functorial action lives on Cont_cart × Cont (P1); object-level law unconditional.

## Notation (match book)
- Container = `\cont SP` = $S\triangleleft P$ (book convention; positions as the ◁-argument).
- Extension `\Ext X`. Filled shape $(s,g)\in\Ext X{S_Y}$, $g:P_X s\to S_Y$.
- Bifunctors $\mathsf A$, $\mathsf E$; liftings written $\prod$/$\coprod$ over positions.
- Composition product of two containers: $X\triangleleft Y$.
- Tone gate: frame is Neil's OWN language; proceed, flag final tone in collaborator note.
