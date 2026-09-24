# Dossier — Theory pillar assembled (WRITE, 2026-09-24)

Robin,

Neil's "complete write-up of everything" dossier now has its **entire Theory pillar (Part I)
written in full**. This session assembled the four chapters that were still scaffolds:

- **Ch. 4 — The equivalence chain** (Cont ⊇ DCont ≃ Comod(Poly) = Cat^#). The chapter-head
  slogan "≃ Cat" is corrected in the open: it is an equivalence *on objects*, and the native
  morphisms are **cofunctors**, not functors. M2/M4 lean-verified; M5/M6 flagged open.
- **Ch. 5 — Zappa–Szép products & distributive laws** (the pairwise (L)∧(G) criterion, proved;
  holonomy/ZS bridge carried at **peer-reviewed**, not proved).
- **Ch. 6 — The correctness criterion (L)∧[ω]=0∈H²** (the thesis equation; the two-ω-sites
  result; [ω]=ε machine-checked, with the verification boundary drawn honestly — last mile
  Lean, first mile pen-and-paper).
- **Ch. 8 — Change-of-base, Fam(C^op), the {Id} collapse** (m-containers peer-reviewed; the Vec
  denotation stated at its honest strength — **neither full nor faithful**; {Id} core lean-verified).

**Stats.** 48 → **69 pages**, clean `pdflatex`, 0 undefined references, 0 multiply-defined
labels. 28 bibitems merged and deduped.

**How it's built.** Each chapter body lives in `papers/dossier/staging/{eqchain,zs,crit,cob}.tex`
and is pulled into `dossier.tex` via `\input` — so you can iterate on a chapter without touching
the master. Assembled by four parallel subagents (one per chapter), each told to pull from the
source papers, reconcile notation to the preliminaries chapter, carry trust grades inline, and
**match the sources' qualifiers exactly** (no hedged→clean upgrades). I did the integration,
notation-collision fixes, and bib merge.

**Pushed:** `work-in-progress` main, commit `ac3b917`.
https://github.com/scotmacbeth/work-in-progress/blob/main/papers/dossier/dossier.pdf

**One thing for a browse session (not this one):** the only citation below the deep-read floor is
**arXiv:2009.06835** (Clarke, *Internal lenses as functors and cofunctors*) — currently
UNREGISTERED in `sources.json`. It's a supplementary attribution in Ch. 4 (the cofunctor
definition is also anchored by Aguiar and Spivak, both fine), so I kept it but flagged it. It
wants a deep-read + registration before this dossier is anything more than an internal draft.

**Next (P4b, logged in WRITE.md):** the remaining `[ASSEMBLE]` chapters — Applications
(blockchain, agent orchestration), Formalisation (Lean H²-engines, change-of-base, the M1–M6
table), and the Impact economic-consequences chapter — then the STUB/GAP ones framed honestly.
Same subagent-per-chapter method; the dossier preamble now carries the shared macros they'll need.

If you want to send any single chapter to Rick, Ch. 4 (equivalence chain) and Ch. 8 (change-of-base)
are the most self-contained.

— MacBeth
