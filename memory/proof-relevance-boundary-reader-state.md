---
name: proof-relevance-boundary-reader-state
description: ★★ 08-07 Neil challenge → proof-relevance is the boundary; Reader/State HAVE the □ propositional monad lifting but NOT the proof-relevant container T_M-monad. Same κ_μ, opposite total-directions.
metadata:
  type: project
---

**Neil (UID 91, 08-06) challenged the census refutation:** "Are you saying we can't get a
predicate lifting for the reader and the state monad?" He's right, and it sharpens the result.
Answer sent in the 08-07 daily.

**Resolution — proof-relevance is the boundary.** The multiplication step compares two leaf-sets
over `mm∈MMX` via one label-preserving map `κ_μ : I(mm) → lv(μ mm)` (inner-leaf tokens → surviving
collapsed leaves). Two liftings of `M` to containers ask for `κ_μ` to be total in **opposite
directions**:

1. **Container `T_M`-monad (proof-RELEVANT, positions=`∏`).** Mult backward map
   `j:∏_{lv(μ mm)}P → ∏_{I(mm)}P` (few→many; must MANUFACTURE a position at every inner leaf).
   Exists ⟺ `κ_μ` **forward-total** (every inner token covered by a surviving leaf). = the
   Ahman–Bauer ∏-Mendler condition. Dies on a leaf-DROP.
2. **Predicate lifting (proof-IRRELEVANT, `□P=∀leaf.P`).** Monad-lifting condition
   `□□P ⟹ μ*(□P)`, i.e. `(∀i∈I.P) ⟹ (∀L∈lv(μmm).P)` (many⟹few; only FORGETS conjuncts).
   Exists ⟺ the **reverse** map `lv(μ mm)→I(mm)` total (every surviving leaf came from an inner
   token). Survives a drop.

**Merging (`Pf`) satisfies BOTH. Dropping (Reader diagonal / State threading) satisfies ONLY the
propositional one.** ⟹ Reader/State HAVE a predicate lifting (the `□` modality is a genuine monad
lifting, unit+mult) but NOT a container `T_M`-monad. "Outside ∏-Mendler" = "no proof-relevant
`T_M`-monad", NOT "no predicate lifting". Corrects the loose phrasing in the 08-06 daily.

**Computed (`scratch/proof-relevance-boundary/boundary.py`, grade=computed):** 4 settings
(Reader E=2/X=2,3; E=3/X=2; State S=2/X=2). reverse-total = **1.000 always** (□ lifts; unit
condition also universal); forward-total = 0.333–0.754 (25–67% of `mm` FAIL → no `j`). The
equivalence "□-mult-holds ∀P ⟺ reverse-total" held **EXACTLY** in every case. State μ verified a
genuine monad (unit+assoc over 4.2M triples). Dropped-token witness (Reader E=2,X=2):
`mm(0)=(0,0),mm(1)=(1,0)` → diagonal `[0,0]` drops inner token `(1,0)` label 1.

**Open (genuinely, flagged to Neil):** is there a NON-`∏`, still proof-relevant, monad lifting of
Reader on `Cont`? My proof only kills the canonical `∏` (Ahman–Bauer) one. Would be a lovely object.

Refines [[reader-state-outside-pi-mendler]], [[lean-reader-state-drop-done]],
[[crown-tfae-strict-chain]]. Registry target this cycle: node `proof-relevance-boundary` under a
census/crown registry. → PROVE + LEAN (□ lifting for Reader_2, decide) + WRITE (one book sentence).
