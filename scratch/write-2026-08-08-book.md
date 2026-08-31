# Write session 2026-08-08 — Book Ch (Monads & comonads), fibrational subsection

Target: `books/category-of-containers.tex`, subsection "The fibrational picture"
(§sec:moncomon-fibration), the teachbox "The fibration stratifies the monad zoo"
(lines ~2819–2912). Revision, three folds from WRITE.md.

## Status of the three folds (audited against current tex)

- **(A) Three fibred-monad terminology verdicts — ALREADY CORRECT, no change.**
  - T_M = lifting always, fibred monad (Hermida Def 5.4.1) iff M cartesian — present (line ~2776–2782).
  - G_M = vertical fibred comonad ∀M, Jacobs Ex 1.7.9 — present (2748, 2773).
  - λ = mixed distributive law / entwining (Beck69), NOT Beck–Chevalley; strict-BC a consequence — present (2790–2817).
  Verdict: leave as is. Confirmed cites Hermida93, Jacobs99, Beck69, Katsumata13 all in bib.

- **(B) Σ-monad now proved (Lean-verified for Reader) — small prov tweak.**
  Current prov already says "proved". Add "Lean-verified for Reader". Keep the
  honest OPEN caveat (general reverse-total ⟹ Σ-monad; exhaustiveness of parity dichotomy).

- **(0) Reframe to Neil's subobject-vs-codomain fibration language — MAIN REWRITE.**
  Rewrite the block from `\smallskip \textbf{One rung further out ...}` through `\end{teachbox}`.

## Structural decisions for fold (0)

1. Lead the rung with the TWO FIBRATIONS in Neil's words:
   - subobject fibration Sub(Set)→Set — leaf carries a truth value (Prop).
   - codomain/families fibration Cont→Set — leaf carries actual positions (Type).
   Cite Hermida–Jacobs 1998 (Inf. Comput. 145(2), DOI 10.1006/inco.1998.2725) — deep-read
   in reading/2026-08-07-fibred-monad-citations.md.
2. HEADLINE = the FAILURE: "every Set monad lifts to a container monad via T_M" is FALSE
   (Reader, State drop leaves); true for cartesian M.
3. Lead intuition = the ∀-ROW (hold ∀ fixed, flip the fibration): a "for all leaves"
   proposition gets EASIER on a drop ⟹ □ survives; a Type-valued datum at EVERY leaf can't
   reindex through a drop ⟹ ∏ = T_M dies. This is the sentence that landed for Neil (UID-92).
4. Concrete 2×2 Reader witness: E={0,1}, diagonal μ keeps (0,0),(1,1), drops (0,1),(1,0).
5. Then the FULL 2×2 ℤ/2 grading (array table): direction = is-limit XOR records-data.
   {∏,◇} forward → die on drop; {□,Σ} reverse → survive.
   State plainly: NEITHER fibration survives uniformly. Survivor = □ (∀ in subobject world)
   AND Σ (∃ in codomain world). Merge keeps all four; drop kills the two forward ones.
6. Σ-container = the concrete codomain survivor / grant payoff ("Reader HAS a positions-recording
   monad lifting after all — the Σ one"). Keep "proof-relevant" ONCE, parenthetically, as the
   type-theorist's synonym.
7. Orestis Agda as INDEPENDENT machine-checked witness: CoLift.agda:163–184 forces pr
   split-surjective (= no drop), Reader named at :175. HONEST CAVEAT: he is entirely Type-valued,
   so his □/◇ are my ∏/Σ (both codomain column) — witnesses ∏-dies/Σ-survives WITHIN the codomain
   leg, NOT the subobject box. State this accurately.

## Citation decisions
- Add bibitem `HermidaJacobs98` — deep-read, DOI present.
- Add bibitem `OrestisAgda` — attribution is FIRST NAME ONLY ("Orestis"); Neil forwarded the
  zip. Do NOT invent a surname. Cite as unpublished Agda dev / personal communication via Ghani.
- No new external arXiv cites; browse forbidden this session (fine — all backing already read).

## Tone gate
WRITE.md: gate the reframe's tone on Neil's UID-92 reply (may not have arrived — no email this
session). Mitigation: the frame is Neil's OWN language (he named "subobject vs codomain"), math is
solid, so proceed; flag in collaborator note that final tone is subject to his confirmation.
