# Note for Robin — "The rooted-tree normal form" shipped (WRITE, 2026-10-02)

**File:** `papers/rooted-tree-normal-form.tex` (+ `.pdf`, 12 pp, pdflatex clean, 0 undefined refs/cites).

## What it is
A bridge / expository paper — deliberately **not a single-theorem paper**. It isolates one recurring
move in container theory and shows it is the *same* move in four independently-developed settings:

> **Confine the data to a rooted tree; the operative backward/factoring map then reads only the unique
> root-path** (a unique prefix, a least element, a chain down-set). The branching that would obstruct
> the condition is forbidden by the tree shape.

Four instances, increasing in categorical sharpness:
1. **Directed-container root axiom** (Ahman–Uustalu, cited).
2. **Path-confinement of the branching free ◁-monoid** — my Lemma D1 (proved + 144,882 checks).
3. **Jakl–Reggio tree-connectedness** (the repair of the arboreal connectedness axiom, cited).
4. **Coalgebras of a polynomial comonad `c=C` = copresheaves `[C,Set]`** ⟹ *arboreal = C is a forest*
   — the load-bearing theorem (my Lemma 4.1 + Cor 4.2).

The punchline for the grant's Theory pillar: **the arboreal coalgebra categories that finite model
theory studies are exactly copresheaf categories of polynomial comonads** — a bridge the game-comonad
programme and the Poly programme have not drawn. Rick is the natural first reader (he has the Bridge-3
material; §4.4 / instance IV is his prompt). It closes with the refined-crown as an honestly-graded
open problem plus the usable `ρ*`-vs-`(Σ_ρ)^op` dictionary.

## Honesty notes (please sanity-check)
- Instance (II)'s **universal property is prior work** (Theorem A, 2026-07-24); the *new* content is
  Lemma D1 isolating the backward pass. General Lean of D1 is flagged, not done (the ◁-monoid laws are).
- Instance (IV) is framed as a **clean identification of folklore-adjacent facts**, not a new deep
  theorem. I state that explicitly in §1 and §4.4. I tightened the "arboreal ⟺ forest" claim to match
  exactly what the proof file supports (general forward direction + the EF/pebbling cases as
  equivalences), not an unproven universal iff over all small categories.

## Two things that need YOUR action before any submission
1. **Below-floor citations.** Abramsky–Shah (1806.09031) and Abramsky–Dawar–Wang (1704.05124) — the
   founding game-comonad papers — are **not in `sources.json` at deep-read**. I cited them only through
   the Jakl–Reggio survey (deep-read) and kept all load-bearing content off them. They must be
   deep-read directly before this goes anywhere public. (No browsing in a write session, so I could not
   upgrade them myself.)
2. **Attribution correction worth propagating.** The "Kleene star on containers" / bidirectional
   typechecker blog post is by **Jules Hedges**, not "Videla" — the proof file
   (`2026-10-01-branching-free-monoid-path-confinement.md`) mis-attributes it. The paper uses Hedges;
   the proof file should be corrected in a future session.

## Plumbing
Committed locally to `wip-sync`. Push is still **GH_TOKEN-blocked** (same as the o_ν capstone and the
coprime note). Files are readable on the projects volume; flag me if the token is fixed and I'll push.

— MacBeth
