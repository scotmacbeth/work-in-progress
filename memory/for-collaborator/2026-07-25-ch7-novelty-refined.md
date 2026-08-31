# Ch7 novelty refinement — transfer now leads with Ahman–Bauer (write session, 2026-07-25)

**File:** `projects/books/category-of-containers.tex` (`\author{MacBeth}`, no PRs — seed off GitHub).
Compiles clean: **54 pages, 0 undefined refs, 0 errors** (`pdflatex` ×2). Backup at
`/tmp/coc-backup-novelty.tex`.

## What changed (attribution/novelty only — the theorem did NOT change grade)

The monad→comonad transfer `G(S,P)=(S,M∘P)` stays **proved + Lean-verified** (registry
`monad-comonad-transfer`, `MonadComonadTransfer.lean`). This cycle only made its Ch7 Novelty Remark
honest and precise, per the 07-25 wake verdict.

1. **Rewrote the Novelty Remark (`rem:transfer-novelty`, §7.… "the transfer") to LEAD with
   Ahman–Bauer, *Comodule Representations of Second-Order Functionals*, arXiv:2409.17664 (JLAMP
   146, 2025).** The remark now:
   - concedes the *framing + machinery* to them: same category `Cont`, same contravariant
     cointerpretation `∏_a(Pa×X)` (attributed to Ahman–Uustalu update monads = the fibrewise op);
   - distinguishes their **Prop 4.1/4.2** (trivial `C↔C^op` duality, relabels not applies) and
     their **Thm 6.3** (`M` on the **shapes** → `MA◁P⋆`, a **monad**);
   - pins the contribution to the **mirror image**: `M` on the **positions** → **comonad**
     `(S,M∘P) = Lan_{(S,P)}M`, a statement/direction/identity in **neither** paper;
   - adds two non-scoop pointers: the Topos-Institute PLTL blog (parallel "obstructs at
     branching" slogan, disjoint math) and Hinze's WG2.8 adjunction-transport pearl.

2. **Added a teachbox "Two ways to feed a Set-monad into a container"** — the honest silver lining
   of the Ahman–Bauer overlap: along **shapes** (`MS◁P⋆`, their Thm 6.3, a **monad**) or along
   **positions** (`S,M∘P`, the transfer, a **comonad**), with the shape/position and
   monad/comonad axes welded by the fibrewise `(−)^op`. No third axis, no free choice in outcome.

3. **Bibliography:** added `\bibitem{AhmanBauer24}` and `\bibitem{ToposPLTL}` (byline confirmed:
   Q. Le, J. Siqueira, K. Kremnitzer). Added both to the reading tracker table (Ch.7).

## Carry-over hygiene (Task 3 — verified, both already correct)
- **Ch3 Abbott coequaliser:** cited as AAG *Categories of containers* (FoSSaCS 2003) `\cite{AAGcat}`,
  Prop 4.3 + Ex 4.4 in the `\prov` note; not claimed as MacBeth's, not in further-work. ✓
- **Free ◁-monoid `C*`:** STATED in Ch6 (`prop:free-monoid-stmt`), UP PROVED in Ch7
  (`thm:free-monoid` + universal-property theorem, FreeUniversal.lean anchor). ✓

## Provenance
Both new cites are `deep-read` in `reading/sources.json` (2409.17664; topos-blog byline confirmed) —
above the whole-book `agent-summary` floor. No new sub-deep-read cites introduced.

## Exact new Novelty Remark (as compiled)
Leads: "The nearest neighbour is Ahman–Bauer's *Comodule representations of second-order
functionals*… same category Cont… same contravariant cointerpretation ∏_a(Pa×X)… the framing and
the machinery are prior art, and we claim neither." → itemises Prop 4.1/4.2 (trivial op-duality) and
Thm 6.3 (M on shapes → monad) → "The transfer is the mirror image… applies M to the positions…
forced to be a comonad, namely G(S,P)=(S,M∘P)=Lan_{(S,P)}M… appears in neither… is what is new
here." → Topos-PLTL + AU + Purdy–Damato + Hinze pointers.
