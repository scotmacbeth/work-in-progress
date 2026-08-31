# Write session 2026-08-07 — book Ch6 §6.6.2 fibrational fixes

Target: `books/category-of-containers.tex` §6.6.2 (Ch6, "The fibrational picture").
NOT Ch7 (WRITE.md said Ch7 but the material lives in Ch6 §6.6.2; the WWM daily/steer
called it "Ch7 monads-and-comonads" loosely). Chapter 7 is Zappa–Szép/dist-laws.

## Four edits

**A2 (G paragraph, ~L2744):** `fibred comonad in Jacobs's sense` →
`vertical fibred comonad (Jacobs Ex 1.7.9, base = id)`. Verdict 2 MATCH. Sets up T contrast.

**A1 (T paragraph, ~L2760):** current text WRONGLY says "'fibred monad' means vertical,
belongs to G". Fix: two grades —
 - vertical fibred monad = Jacobs Ex 1.7.9 (base id) = G's home.
 - fibred monad over nontrivial base M = Hermida Def 5.4.1 (2-cat **Fib**) = T's home,
   demands total functor be fibred (preserve cartesian) ⟹ holds iff M cartesian.
 Honest: T_M is a lifting (Street) always; fibred monad over M (Hermida 5.4.1) iff M cartesian.
 "fibred" bakes in the cartesian boundary. Ref crown boundary = stratification box below (no \ref, descriptive).

**A3 (λ paragraph, ~L2774):** title `the oplax Beck--Chevalley mate` → `a mixed
distributive law, not a Beck--Chevalley square`. Verdict 3: λ IS entwining (Beck69,
already Thm entwine); BC (Jacobs Def 1.9.4) is Σ/Π-vs-reindexing mate — different concept.
Keep the oplax/pure-writer invertibility analysis but demote "BC" to "BC-STYLE invertibility
condition", not λ's nature. Reconnect to Thm~\ref{thm:entwine}.

**B (proof-relevance box, ~L2827-2849):** add ℤ/2 grading paragraph + upgrade Σ from
"multiplication survives, coherence unchecked" → PROVED for Reader (all E) / State (all St)
[proofs/2026-08-07-sigma-monad-proved.md; registry trust=proved].
 - Parity = (is-limit) XOR (is-proof-relevant). parity 0 = {∏,◇} forward-total;
   parity 1 = {Σ,□} reverse-total. Reader/State reverse-total ⟹ both □ and Σ survive.
 - HONEST OPEN: general "reverse-total ⟹ Σ-monad" (coherence ⊋ pointwise section;
   registry trust=speculative); exhaustiveness of ∏/Σ/mix.
 - fourfold.py = brute-force artifact for grading.

## Honesty note
WRITE.md said hedge Σ at "computed" — but that was written BEFORE the 18:15 PROVE file
landed. Registry now trust=proved for Reader/State (general still speculative). Write
session rule: "state verified things plainly." So: PROVED for Reader/State, general OPEN.
Scope precisely — neither over- nor under-claim.

All cites exist in bib: Jacobs99, Hermida93, Street72, Beck69, PowerWatanabe02,
AhmanBauer24, Katsumata13. Adding def/ex numbers inline (Ex 1.7.9, Def 5.4.1, Def 1.9.4).

---

## DONE — 2026-08-07 (all four edits landed, compiles clean 70pp, no undefined refs)

**A2** L2744 — G: `vertical fibred comonad (Jacobs Ex 1.7.9, base id)`. ✓
**A1** L2761 — T: two-grade box. Lifting always (Street); fibred monad over M
  (Hermida Def 5.4.1, 2-cat **Fib**) iff M cartesian; "fibred" bakes in the boundary. ✓
**A3** L2790 — λ: retitled "a mixed distributive law, not a Beck--Chevalley square";
  λ = entwining (Beck69, = Thm entwine); BC (Jacobs Def 1.9.4) = Σ/Π-vs-reindexing,
  different; invertibility demoted to "BC-*style* coherence". ✓
**B**  L2872 — new "parity" paragraph: ℤ/2 grade = (is-limit)⊕(is-proof-relevant);
  {∏,◇} fwd, {Σ,□} rev; Reader/State reverse-total ⟹ Σ-monad. Upgraded from
  "coherence unchecked" → **PROVED** for Reader (all E)/State (all St)
  [proofs/2026-08-07-sigma-monad-proved.md, registry trust=proved]. General
  reverse-total⟹Σ + exhaustiveness flagged OPEN in \prov. Also softened earlier
  "boundary IS proof-relevance" → "at first cut" so the parity refinement isn't a
  contradiction.

## Honesty resolution (recorded)
WRITE.md said hedge Σ at "computed" — but that predates the 18:15 PROVE file.
Registry `sigma-monad-reader-state-proved` trust=**proved**;
`reverse-total-implies-coherent-section-OPEN` trust=speculative. So the draft states
Reader/State Σ-monad as PROVED (scoped) and the general implication as OPEN — matches
the proof file's own §6 and the write-session rule "state verified things plainly."
WRITE.md gate explicitly permits tightening to "proved" once the Σ PROVE lands. It did.

## Provenance note (for a future BROWSE session, out of scope here)
citation_check footprint on the book = floor `agent-summary`, from **2405.13157
(SS2405, Shapiro–Spivak Cat#)** — cited ELSEWHERE in the book, NOT in §6.6.2, NOT
touched by this revision. Needs a deep-read upgrade sometime. My four fixes cite only
Hermida93/Jacobs99/Street72/Beck69 (deep-read via local PDF grep, 08-07 audit) and
AhmanBauer24 (2409.17664, deep-read). Sound.

## Not done (deliberately — other sessions)
- Lean: no code touched. The □ and Σ Lean rungs are separate (LEAN session).
- The general reverse-total⟹Σ-monad structural criterion (PROVE session).
