# For Robin — survey `containers-over-a-base.tex`: landscape section added (2026-08-28, 2nd write pass)

**File:** `projects/papers/containers-over-a-base.tex` → `.pdf` (now **16 pp**, compiles clean).

This is the second write pass of the day. The earlier pass (see
`2026-08-28-containers-survey-revision.md`) rewrote §5 into the proved logic-of-containers
(Cont(cod) bifibration). This pass added the two remaining WRITE.md inputs.

## What changed

1. **New §3 "The landscape of bases."** A census table of the ~10 base classes over which someone
   has actually run the polynomial/container construction — Set/topos, finite-limit (Shapiro–Spivak),
   pullbacks+exp-legs (Weber), LSCC (Walker), any monoidal V (Dorta–Jarvis–Niu), any fibration
   (von Glehn), Set^I (De Pascalis–Uustalu–Veltrì), Prof/generalised species (Fiore–Gambino–Hyland–
   Winskel), Vec/R-Mod (this survey), and the open Rel/Mod/Poly — ordered by decreasing base strength,
   with the two thesis axes (extensive? LCC?) as columns. Then the **weakening tower** as a totally
   ordered chain (LCCC ⊃ Weber ⊃ Walker ⊃ spans) and the **organising fact**: off the good zone a
   base fails for exactly one of two independent reasons, lost extensivity or lost internal Π. This
   is the survey's map of the territory — it makes the piece a genuine survey, not just the three
   theorems. It grounds the two-axis thesis in the actual literature.

2. **δ vs Φ re-filing remark** (`rem:weberrefile`). Honest placement of the two proved theorems in
   Weber's work: T4's tininess hypothesis = Weber's distributivity-δ (1106.1983); T2's familial
   representability = Weber's *separate* parametric-right-adjoint theory (TAC 18, 2007). Logically
   independent — a Vec witness with fd left / ∞-dim right positions makes δ iso while Φ is
   unrepresentable, and vice versa. So T2 does **not** sit on the weakening tower at all. Framed
   explicitly as `computed`-level ("a reading of the two Weber papers, not a theorem of our own").

Supporting: abstract gained a "we draw one" census clause; outline + what's-new updated; four
bibitems added (FGHW, Shapiro–Spivak, Weber ×2).

## Provenance (the honest bit)

- **Citation footprint floor: deep-read.** The arXiv-ID references all sit at deep-read or better
  (2305.00167 verified-quote).
- **von Glehn debt is discharged**: it's now in `sources.json` at deep-read — a browse session
  picked it up, as WRITE.md predicted.
- Two non-arXiv additions to double-check before any external submission: **FGHW** (JLMS 2008 — a
  landmark, but our sources entry is agent-summary; used only as a census pointer, non-load-bearing)
  and **Weber TAC 18 2007** (canonical, not yet in sources.json). Neither is load-bearing for a
  theorem; both bibliographically stable. Flagged only for arXiv hygiene.

## Still open (unchanged)

- §5's honest gaps: shape-level quantifiers, joint Beck–Chevalley/Frobenius, an intrinsic
  characterisation of the BC squares.
- The survey closes by naming the next PROVE target: **does the four-level branching hierarchy
  (λ-inv ⊊ non-branch ⊊ cartesian ⊊ Π-Mendler) lift index-wise to De Pascalis–Uustalu–Veltrì's
  indexed containers IC_I?** That's the first structural bridge between approaches (1) and (2) over
  a base richer than Set, and the recommended seed for the next PROVE.md.

You can read the PDF directly on the projects volume. No email sent (write session).
