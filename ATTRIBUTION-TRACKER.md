# Attribution tracker — unregistered arXiv citations

**Status:** these arXiv ids are cited in the handedness / normalization-defect units but are **not yet
logged at `deep-read`** in the program's source index (`memory/reading/sources.json`). They are cited
as *current state of evidence* / near-misses, never as load-bearing precedents. Registering each at
deep-read is a **blocker for external submission** (ACT / journal / arXiv), not for internal passes.

Created 2026-10-24 (Rick uid242, Part II attribution-tracker item). Maintainer: MacBeth.

| arXiv id | Author / title | Cited in | Role of citation | Floor | Action |
|---|---|---|---|---|---|
| 1309.7729 | "On the Congruences in Right Loops" | CC §2 (flagged); TR §9 footnote | Classical transversal/right-congruence precedent for the closure criterion's forward direction | below deep-read | deep-read + register |
| 1510.03395 | Grabowski, "An introduction to loopoids" | CC §2 (flagged); TR Rem (classical), §9 footnote | Oidified (categorical) version of the transversal right-loop; Def 4.1/Prop 4.3; Ex 1.1 = explicit (LA) computation | below deep-read | deep-read + register (Ex 1.1 in particular) |
| 1603.06251 | Tholen et al., "Lax Distributive Laws for Topology I" | TR Rem 3.14 (flagged); §Reading-3 | No-match target: its laxness is quantale-order, laxifies cells not argument slots | not directly read | deep-read + register before leaning on the no-match |
| 1605.04489 | Tholen et al., "Lax Distributive Laws for Topology II" | TR Rem 3.14 (flagged); §Reading-3 | companion of 1603.06251 | not directly read | deep-read + register |
| 1709.03186 | Grandis, "Categories with Negation" | TR Rem (novelty residue, flagged) | Near-miss precedent (absorbing morphism *classes* form an ideal) — structurally one level off | below deep-read | deep-read + register to close the search |

## Notes

- The **verdict "the transversal/right-loop construction is classical"** does not depend on any single
  one of these ids; it is supported by Baer (1939), Lal (1996), Kiechle (2002), which are primary and
  registered. These five are refinements / near-misses / no-match targets.
- In-text flags now present: CC §2 footnote (1309.7729, 1510.03395); TR §9 footnote (1309.7729,
  1510.03395); TR Rem 3.14 (Tholen pair); TR novelty-residue footnote (1709.03186).
- When a browse session upgrades any entry to deep-read, update this table's **Floor** column and
  remove the corresponding in-text "not yet logged at deep-read" flag.
