# Containers-over-a-base survey — hostile-referee revision pass (2026-08-29)

**File:** `projects/papers/containers-over-a-base.tex` (compiles clean, 16pp, 0 undefined refs).
**Session type:** revision only (no new content). The draft was already complete and twice-polished
on 08-28; this was a read-as-referee pass for clarity, consistency, and honesty.

## What changed (3 targeted fixes)
1. **Intro "connected" overload (real clarity bug).** Theorem 1.1's Vec clause called $k$ "a
   connected object" one clause after stating "ff iff the unit is connected" — two senses of
   "connected" in adjacent sentences, before Definition 2.5 gives the reader either. Rewrote to say
   only that the underlying-set functor $\C(k,-)$ fails to preserve $\oplus$, hence the unit is
   disconnected in our sense. The two-senses nuance stays in Remark 2.6 (rem:vecbad), where the
   definition is in hand.
2. **Prop 4.13 (the Set ◁-obstruction) tightened.** Was: "forces the representing container to carry
   double-exponential data, which is not polynomial." Made the logical spine explicit — a right
   adjoint would be a container representing $(-)\lhd q$ generator-wise, but its shape-count grows
   double-exponentially ($n^{2^n}$) whereas every container extension is polynomial, so no container
   carries the data. Faithful to the Workers-Thm-2 growth argument in the proof file; no new proof.
3. **Abstract grammar:** "two properties … are the axis of divergence" → "the two axes."

## What I deliberately did NOT do
- **No forced 10% cut.** The survey's recapitulation (thesis blockquote → landscape organizing-fact →
  synthesis → conclusion) is deliberate scaffolding for a reader tracking four approaches. Cutting it
  would hurt navigation, not help. The "cut 10%" rule is for bloated first drafts; this isn't one.

## Verified sound, no change
- Intro ↔ conclusion consistent. Fibre logic of Thm 5.11 (∧=⊔ witnesses, ∨=∏ witnesses, ⊤=∅→P,
  ⊥=id) checks against (Set/P_s)^op. Reindexing-trap remark consistent with the quantifier theorem.
  Honesty guardrails all intact (Walker verdict = reading; §5 scope gaps stated; δ/Φ = a reading).

## Still open (external-submission TODOs — not blocking the internal draft)
- **FGHW** (JLMS 2008) sits at `agent-summary` in sources.json; used only for a census-table row.
  Deep-read before any arXiv submission. **WeberFamilial** (TAC 18, 2007) not in sources.json
  (canonical, stable) — confirm pages. `citation_check` keys on arXiv IDs only, so both are silent
  there; this note is the honest record. All 6 arXiv-ID sources are at deep-read/verified-quote.
- **Prove-session targets the survey surfaces** (unchanged): Q5.1 — does the 4-level branching chain
  ($\lambda$-inv ⊊ non-branch ⊊ cartesian ⊊ Π-Mendler) lift index-wise to DPUV's $\mathrm{IC}_I$?
  Plus the §5 logic gaps (shape-level quantifiers; joint BC/Frobenius; intrinsic BC-square class).

Robin — you can read the PDF directly from the projects volume. Nothing here needs action; it's the
change log for the referee pass.
