# Applications outlook drafted & compiling — staged for Neil's applications turn

**File:** `projects/papers/applications-outlook.tex` (6pp, compiles clean, `applications-outlook.pdf`).
**Status:** STAGING. Standalone grant-Impact outlook. **Not committed to the book; nothing here touches
`books/category-of-containers.tex`.** Neil-gated: this is ready to slot in when he steers the applications
turn (he had it slated for "next week" as of 2026-07-22/23).

## What it is
The Path-5 Impact spine, written honestly as a *program*. One argument in six pages:

1. **The hinge** — a directed container *is* a small category, machine-checked (`DContCat.lean`).
   → anything presenting a category is a directed container, for free.
2. **Three domains present categories** — orchestration [proved], supply chains ([open] object-level,
   [proved] morphism-level = cofunctor/lens), ologs/KG ([definitional import], Spivak).
3. **The payoff** — composing any two is a Zappa–Szép product `C⋈D`; it exists iff `(L)∧(G)` [proved],
   and the only obstruction is one class `[ω]∈H²(Sk_C;𝒟)` [proved]. That one class is simultaneously
   supply-chain inventory inconsistency, ontology-merge conflict, and agent re-entrancy.
4. **Computed illustration** — folds in the PROVE-session worked example
   (`proofs/2026-07-23-supply-chain-zs.tex`): `[ω]=ε ∈ ℤ/n`, where the orchestration *bit* refines to a
   *unit-count* of how badly two provenance routes disagree; olog `n=2` sibling.
5. **Honest status table** — every row graded; the one [open] row (does a real supply chain present a
   category? SEED Q4) is marked and never fudged.

## Grade discipline (the point of the note)
- A boxed grade-key sits on page 1; the whole note is built so a reader can't mistake a [computed]
  illustration for a [proved] theorem or an [open] modelling claim for a settled one.
- General theorems cited at registry grade ([lean-verified]/[proved]); domain instances at [computed];
  the fidelity claim [open]. Nothing about a domain rises above [computed].

## Provenance flags (for your eyes / a future browse session)
- **Ahman–Uustalu "Directed Containers as Categories" (1604.01187): deep-read ✓** — the hinge cite, solid.
- **Spivak–Kent "Ologs" (1102.1889): agent-summary only.** I cite it *by name for the definition of an
  olog* — a definitional import, no theorem number claimed — and put an explicit **deep-read TODO** in a
  footnote and the bibliography. Same discipline as the Abbott coequaliser rework. **Please flag for a
  browse session to deep-read the primary Spivak olog paper before this is promoted beyond staging.**
- Morphism-level "supply-chain map = cofunctor / lens" cites my own connection note
  `cofunctors-are-update-lenses` (registry-graded proved), with Clarke EPTCS 323 as named prior art —
  I did *not* lean on the un-graded Clarke arXiv as a load-bearing reference.

## Two TODOs it hands forward (NOT this session)
- **PROVE/browse:** deep-read Spivak ologs; upgrade sources entry; then the [definitional import] row can
  carry a real citation.
- **PROVE:** the honest open frontier — a *fidelity criterion* (SEED Q4: when does a real supply-chain
  network genuinely present a category?), and the obstruction *beyond abelian vertex groups* (drop
  hypothesis (H)). Both are stated as open questions in §5.

## Delivery
Write-session rules forbid email, so I have **not** emailed it. Please either read the PDF from the
projects volume, or I'll attach it to the next wake daily to Neil (CC you), respecting one-email/day.
