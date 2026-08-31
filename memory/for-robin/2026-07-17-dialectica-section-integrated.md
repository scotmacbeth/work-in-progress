# ⋉/⋊ Dialectica section integrated into the four-monoidal chapter (2026-07-17)

**File:** `projects/papers/four-monoidal-chapter.tex` (compiles clean, 30 pp, EXIT 0,
no undefined refs). Readable from the host projects volume.

## What happened this write session
The standalone draft `papers/ltimes-rtimes-dialectica-section.tex` (the discovery that
Dorta–Jarvis–Niu's two uninterpreted tensors ⋉/⋊ are de Paiva's Dialectica tensors,
extended off the homogeneous slice) is now **§10 "Beyond the census: ⋉ and ⋊ as
Dialectica products"** of the four-monoidal chapter, sitting after the duoidal
interaction section and before Provenance. It is framed as the honest outer boundary
of the Day-family classification: these are the structures Theorem A does **not** reach.

Four fixes applied on integration (per state/WRITE.md):
- **(a)** Rewrote the grade/novelty remark. The 2026-07-17 novelty sweep RAN; verdict
  **(C) CLEAR**. The claim is now framed under the framing rule — *we identify a known
  tensor (de Paiva's) with DJN's uninterpreted ⋉*, NOT "first Dialectica-on-Poly"
  (which would be false). Trust grade stays **[computed / an identification]**.
- **(b)** Bibliography — see the honest caveat below.
- **(c)** Integrated: preamble stripped, macros (\Dial \Hmg \dtens) added to the chapter,
  citation keys unified (djn2305→DJN23, niuspivak→NiuSpivak), cross-refs to Theorem A
  (thm:A), the closures, and the closest-neighbour discussion wired up. Abstract, the
  "two further movements" intro, and the Plan now mention the coda.
- **(d)** Added Remark ("A lead on closure, not a refutation"): ⋉ is conjecturally
  non-closed (our argument only rules out a *left* adjoint via coproduct-non-preservation);
  Lucatelli Nunes–Vákár's Dialectica hom ⊸ is a *lead* for a twisted internal hom on Cont,
  not a refutation.

Also updated the chapter's provenance (New-here bullet for the identification; a
"Cited, not ours" bullet for the Hmg≅Dial and de Paiva-tensor ingredients) and the
closest-neighbour paragraph (DJN §6 is now *answered*, not flagged open).

## ⚠️ HONEST CAVEAT — three citations need a source-level check (browse session)
This was a no-browse write session. Three bib entries were **not deep-read from source**
and are flagged in a footnote in the chapter's §Provenance:
- `depaiva89` — de Paiva, *The Dialectica Categories* (Contemp. Math. 92, 1989 /
  Cambridge Tech. Report 213, 1991). Standard foundational reference; not in sources.json.
- `lnv2405` — Lucatelli Nunes–Vákár, arXiv:2405.07724. **Title discrepancy** between the
  old draft ("Dialectica Logical Principles…") and the novelty-sweep registry ("Monoidal
  closure of Grothendieck constructions via Σ-tractable monoidal structures and Dialectica
  formulas"). I used the **registry title** (it matches the substantive claim I cite it
  for — tensor = fibred product, twist in the hom ⊸). Needs verification; possibly two
  distinct LNV papers share the theme.
- `capucci2024` — Capucci–Gavranović–Malik–Rios–Weinberger, MFPS 2024. Registry title used.

`lnv2405` and `capucci2024` are **distinguishing (defensive) citations only** — no theorem
rests on them; they exist to separate our result from neighbouring work. So the pending
flag is safe: the mathematics is unaffected. `citation_check.py --report footprint`
confirms 2405.07724 is UNREGISTERED and the registered sources floor at deep-read.

## Not done / next
- **Browse TODO:** deep-read + register de Paiva, LNV (2405.07724), Capucci (MFPS 2024);
  resolve the LNV title; upgrade sources.json; then drop the pending-verification footnote.
- No GitHub push (policy — shared via projects volume). Book integration into
  `category-of-containers.tex` remains Neil's call; this chapter is drop-in ready.
