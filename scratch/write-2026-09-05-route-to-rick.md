# WRITE 2026-09-05 — route VCont + M-container drafts through Rick

## Task (from state/WRITE.md)
Route two complete drafts to Rick (PROTOCOL §4.2: one neighbour before publishable-result).
For EACH: add §2.3 title-page header (For: Rick; date; wip commit hash via two-commit pattern),
push src+PDF to scotmacbeth/work-in-progress, email Rick a §2.1 covering note (3–4 sentences,
PDF attached), CC Robin.

## Honesty guards done
- **T1 verified** against topics/fullness-unit-connectedness.md: source states
  "⟦−⟧ fully faithful ⟺ monoidal unit I connected (C(I,−) preserves coproducts)". The VCont
  paper §3.2 T1 bullet states exactly this. MATCH. (Note source correction #2: "faithful always"
  is false over Vec — only faithful-on-nonzero; VCont Thm 3.3 already phrases it "injective away
  from the zero maps". This is precisely the point WRITE.md wants Rick to check — leave as is,
  flag in covering note.)
- **Lemma N resolved 09-05** (proofs/2026-09-05-lemmaN-retract-and-beta.md). THM 3 in the
  m-container paper currently says "sufficiency proved; converse reduced to Lemma N [open]".
  This is now STALE and must be updated before Rick sees it (WRITE.md honesty guard). New state:
    - Lemma R0 PROVED: M poly ⟺ M∘M preserves connected limits.
    - Prop C PROVED: single instance M∘M≅⟦r⟧∘M is categorically inert (sharpens trailing-M).
    - Stabilizer invariant + Thm F PROVED: 𝕄∘𝕄 ≇ P∘𝕄 (Young vs wreath D₄); β killed by cardinality.
    - Dichotomy: every non-poly monad fails via (a) super-poly growth OR (b) symmetric/wreath.
      Necessity PROVED for every monad that arises.
    - Residual: Plethysm Lemma [open] — general non-free analytic; no known monad inhabits it.
  Honest headline: THM 3 is a biconditional for every monad that arises; unconditional converse
  blocked only by the species Plethysm Lemma.

## m-container edits (transcription of proved results, NOT new proofs)
1. Abstract: sufficiency stmt stays true; strengthen to note near-complete converse honestly.
2. Thm 3 necessity paragraph (l.179-184): rewrite to dichotomy + residual.
3. Method (l.204): "forces M polynomial" — now backed for every monad that arises; soften slightly.
4. Provenance/honesty (l.219-223): update Lemma N status.
5. §5.4 "The remaining gap" (l.633-660): REPLACE with "The categorical converse":
   R0, Prop-inert, stabilizer invariant, Thm F, dichotomy thm, Plethysm Lemma[open], final headline.
6. Conclusion item (1) (l.693-697): update.
Keep §5.3 cardinality-growth-law subsection (prop:cardlaw + cor:folklore) unchanged.

## VCont edits
- Complete + honest already. Add §2.3 header (recipient Rick + commit hash). Change title-page
  "Prepared for: Neil Ghani / external requester" → keep provenance but add "For (review): Rick
  Langer? no — Rick" line + hash. Actually PROTOCOL §2.3 needs recipient=Rick + hash on first page.

## Two-commit hash pattern (per paper)
commit src (H1) → put H1 on title page → recompile PDF → commit again (H2). H1 stamps the source.

## Covering-note questions (from WRITE.md)
- VCont: is faithful-but-not-full framing (Thm 3.3, "faithful on nonzero") correct; is
  (Q)-independence appropriately hedged for an external reader?
- M-containers: is THM 2 codensity criterion + THM 3 honesty split (sufficiency proved / residual
  Plethysm open) convincing; does trailing-M obstruction read as a real gap not a hand-wave?

## Scope discipline
Ends at "sent to Rick for review." Do NOT push publishable-result, do NOT email Robin §4.3 note.

## COMPLETED 2026-09-05
- m-container THM 3 §5 rewritten to biconditional-in-practice (R0, inertness Prop, stabilizer
  invariant, dichotomy, Plethysm residual open). Abstract/method/provenance/conclusion/outline
  updated. Orphan Ahman-Uustalu-DL bibitem dropped. 13pp -> 16pp. Compiles clean, 0 undef refs,
  0 overfull. Citation floor deep-read.
- VCont header updated (For review: Rick + hash); T1 verified vs source; content unchanged; 8pp.
- Two-commit push to scotmacbeth/work-in-progress: source b94bc32, stamped 40ff1f4. Both PDFs
  carry hash b94bc32 on p.1.
- Emailed Rick both PDFs (CC Robin) with the WRITE.md review questions.
- Memory: routing-2026-09-05-...md + MEMORY.md pointer; for-robin note + PROGRESSIVE_DISCLOSURE updated.
- SCOPE ENDS HERE: no publishable-result push, no §4.3 Robin note, until Rick replies.
