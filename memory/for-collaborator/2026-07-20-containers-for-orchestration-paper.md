# Paper drafted: "Composing Agent Orchestrations is a Zappa–Szép Product"

**File:** `projects/papers/containers-for-orchestration.tex` (compiles clean, 8 pp, amsart).
**Session:** write, 2026-07-20. **Grade:** synthesis/Impact note — computed, not overclaimed.
**For:** Neil (answers his UID-70 "what can be done here?") + grant Impact + book applications.

## What it is
The grant-Impact note grounding the **agent-orchestration = directed-container** dictionary.
Turns Neil's UID-70 framing into a self-contained note whose spine is the machine-checked
supervisor–worker instantiation (`proofs/2026-07-19-orchestration-zs-instantiation.tex`).

## Spine (one sentence)
Composing two shared-resource orchestrations is a **Zappa–Szép product `C ⋈ D`** of their
handoff categories — *not* a functor — and the obstruction to that composite existing is a
**degree-2 class `[ω] ∈ H²(Sk_C; 𝒟)`**; unprotected re-entrancy is the concrete nonzero
generator of `H² ≅ Z/2`. One degree above the MAS sheaf-Laplacian `H⁰/H¹` obstructions.

## Structure
1. Intro (problem → agents-as-containers [Neil/Spivak] → gap: composition-as-functor has no
   failure theory → result `C⋈D`+H² → method: worked minimal case → MAS degree contrast).
2. The dictionary, **honestly graded** (12-row table; every row attributed; the `★`
   interleaving row flagged as this note's delta).
3. Why composition is a ZS product not a functor (T1–T3 as black boxes; the functor-vs-
   distributive-law argument).
4. The worked instantiation (supervisor–worker; bug/ok regimes; Prop obstructed;
   Thm =rigid-twist [ω]=gen Z/2; 4-regime machine-checked table).
5. The degree axis (contrast table vs sheaf-Laplacian MAS).
6. Conclusion (validation ask — GA analogue; open: Fairbanks comonads-as-spaces as unifier; ∞).

## Honesty ledger (as delivered)
- Interface/dynamics/monoidal-vocabulary rows = **Spivak/Ghani prior art** — cited, not claimed.
- H² tower = **classical** (Rosebrugh–Wood, Baues–Wirsching, Pirashvili) — cited, not reproved
  (Neil demoted the cohomology thread; note respects that).
- **The delta** = the identification *interleaving = C⋈D* + the computed obstruction table +
  the degree-axis MAS contrast. Graded **computed** throughout; models stated as minimal
  faithful abstractions, not literal encodings of any named framework.
- MAS contrast claim ("nobody routes composability through directed-container structure")
  hedged "to our knowledge"; the three sheaf papers (2606.01663, 2605.11204, 2605.01879) are
  now deep-read, so the positioning is verified, not abstract-only.

## Citations
All at `deep-read` or classical-published grade (citation_check footprint floor = deep-read).
Fixed the AhmanUustalu title bug (1604.01187 = "Directed Containers as Categories", *not*
"When Is a Container a Comonad?" — the four-monoidal chapter's bib still has the old wrong
pairing; flagging for a later fix there).

## Open / TODO (not for this write session)
- **Empirical validation** (the note's ask): map one real framework's handoff graph onto
  `(S◁P,o,↓,⊕)` + exhibit one concurrency pattern as an explicit `δ`. This is the GA-analogue
  deliverable that would move the `★` row from *computed* to *demonstrated*.
- **Fairbanks "Comonads as Spaces" (2607.15091)**: the conjectured unifier of the H² and the
  H⁰/H¹ sheaf pictures — held deep-read; making the comonadic-invariant claim precise is a
  prove target, not asserted in the paper.
- **∞-version** flagged as open.

## Delivery
Via the projects volume (Robin reads it directly). No email sent (write-session rule).
No git push — no shared-repo checkout present in the container; if you want it on
`scotmacbeth/ghani-containers`, say so and I'll stage it next non-write session.
