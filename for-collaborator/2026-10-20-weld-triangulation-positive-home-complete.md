# Weld-obstruction triangulation — POSITIVE home folded in, complete (held for Rick)

**Status:** complete draft, pushed. **NOT yet sent** — per dream 2026-10-19, hold until Rick is off
the weld-paper (uid234) thread. This is the version to send him for review once that clears.

**File:** `expository/2026-10-19-weld-obstruction-triangulation.tex` (+ `.pdf`, 10pp)
**Repo:** https://github.com/scotmacbeth/work-in-progress
**Content commit:** `ac07a05` (stamped on page 1); stamp commit `909b616`.

## What changed since the 6pp version (56310ea)

The note was "four homes it is NOT" with a weak, evidence-grade handedness section and an *open*
fourth lead. It is now a two-movement grant unit — **"four homes it is NOT, and the one it IS"**:

**Movement I (§§3–6) — the refutations.** Promoted the lax-distributive-law lead from OPEN to
**REFUTED** (wrong locus): Schoen/Tholen laxness is a fixed-direction ≤ on a coherence cell, but the
associator defect compares two mass-1 bracketings, which are order-*incomparable* (elementary lemma),
so it is provably not a laxness. Record now **three refutations of three distinct kinds** — no
receptacle (cocycle), vacuous (Karoubi), wrong locus (lax-DL) — plus the EXISTS corner (bicomodule).

**Movement II (§§7–11) — the home.** The constructed positive home from the 2026-10-19 prove session:
- **Def.** a *normalizer* `K` (idempotent hom-operator, `(LA)`: `K(K(x)·c)=K(x·c)`); magmoid
  `N_K`, `f#g:=K(f·g)`.
- **Thm A** `(LA) ⟹ (f#g)#h = K(f·g·h)`; **Thm B** `N_K` assoc ⟺ `K` two-sided `(RA_#)` ⟹
  handedness `=(LA)∧¬(RA_#)` genuine & non-vacuous.
- **Instance** `Norm` (row-normalization) with the exact witness `[8/11,3/11] ≠ [2/3,1/3]`.
- **Prop 5.1 minimality** (the sharp bit): a principal normalizer by an idempotent *element* is
  *always* associative — so the near-semiring's one-sided-absorbing *zero* is the **fourth** refuted
  map (element locus inert). Triple-elimination (morphism / cell / element all inert) ⟹ the binary
  operation's argument slots are the unique home.
- **Lean leaf** `lean-positive-home-oracle` cited: the abstract smallest monoid-with-normalizer
  `M={e,z,a,b}` machine-checks `(LA)` universal, Thm A, `¬(RA_#)`, non-assoc, Thm B pointwise,
  non-principality, and the Prop 5.1 control — `#print axioms` = `[propext]` only, axiom-free.

## Honest-scope flags for the referee
- Load-bearing citations all **deep-read** (DLRS 2510.01131, SGF 2111.10968, BLS 1102.4931, Schoen
  2307.16552).
- **Tholen** (1603.06251/1605.04489) is *not* deep-read; §6's honest-scope remark says so and the
  lax-DL verdict does not rest on Tholen detail (family-level coherence-cell laxness only).
- **Fritz** (2308.00651, agent-summary) dropped as a formal citation; the second (probabilistic)
  generic-confirmation now appears only as a flagged reading-log aside pending deep-read.
- `Norm` matrix instance stays Python-only (rational ÷ not kernel-decidable); the axiom-free Lean
  certificate is on the abstract finite monoid model instead — stated plainly in §10.

## TODO for a browse/registry session (not this write session)
- Register **Tholen** 1603.06251/1605.04489 and **Grandis** 1709.03186 in `reading/sources.json`
  (both currently UNREGISTERED; cited only in honest-scope/evidence remarks). Deep-read **Fritz**
  2308.00651 if we want the second generic-confirmation back as a formal citation.
