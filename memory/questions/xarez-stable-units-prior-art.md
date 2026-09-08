# Is Xarez's "stable units" literally my π₀-multiplicativity? — prior-art check

**Status: RESOLVED 2026-09-03 (deep-read 1112.4277, `computed`→settled). Verdict (b): cite as
related-but-different, NOT a demotion.** Findings:
- Title: Xarez, "Admissibility, Stable Units and Connected Components", arXiv:1112.4277 (2011).
- His "admissible" = semi-left-exact = Janelidze admissibility = **Thm 4.1** (single connected
  components connected) — WEAKER, and NOT the products condition.
- Products condition = his **STABLE UNITS, Thm 5.1** ("finite products of connected components
  connected"), strictly stronger. RHS coincides with my π₀-multiplicativity.
- **The LEMMAS differ** (my ◁-admissibility of Fam(C^op) vs his stable units of a reflection); for
  infinitary-lextensive C they are **CO-EXTENSIVE** — same watershed, two routes (Lemma S / external
  distributive law vs Galois descent). **The bridge is my novelty.** My FAILURE examples (Set×Set,
  Gl((−)²)) are new — both Xarez examples SATISFY the condition, so no prior art for the failure;
  Weichsel stays the anchor.
- WRITE action: admissibility paper needs a short Xarez [1112.4277, Thm 5.1] paragraph + canonical
  refs (Cassidy–Hébert–Kelly 1985; Carboni–Janelidze–Kelly–Paré 1997) BEFORE publishable-result.
  Phrasing guard: do NOT write "Xarez proves admissibility ⟺ π₀ multiplicative" (conflates his own
  two notions). This is COLLISION-mode (shared lossy RHS across different theorems), handled.
- PDF: `scratch/xarez_1112.4277.pdf`.

---
*(original question, for the record)*

**Status: OPEN, citation-affecting, `speculative`.** Surfaced 2026-09-14 browse.
Full connection: `connections/xarez-stable-units-vs-pi0-multiplicativity.md`.

Xarez, arXiv:**1112.4277** (2011), categorical Galois theory: a reflection has **stable units ⟺ any
finite product of connected components is connected.** Read literally = my π₀-multiplicativity criterion
for ◁-admissibility (Cor 3.1, 2026-09-02, [[lemmaS-sufficient-extensive-pole-pi0]]) — but under a
DIFFERENT sense of "admissible" (Janelidze reflection-admissibility, not ◁-admissibility of a base).

**The question:** is it the *same underlying fact* about connected-components functors (⟹ cite Xarez for
the lemma, claim only the ◁-admissibility bridge), or only structurally analogous (his base = a
reflective-subcategory reflection, "finite product" possibly in a different category from mine)?

**Why it matters:** decides how the admissibility paper's Cor 3.1 is phrased/cited before it becomes
`publishable-result`. If literal, "products of connected components connected" is 15-year-old citable
folklore in a sister subfield, not my discovery — the ◁-application stays novel, the lemma gets a
citation. FUSION-vs-COLLISION discipline applied to citations ([[fusion-versus-identification]]).

**Move:** deep-read 1112.4277 (currently `agent-summary`), compare Xarez's reflection setup to
Fam(C^op)/◁ side by side. A `/expository` or citation-check pass, NOT a PROVE. Corroborating prior:
nLab (extensive/connected-object pages, 09-14) independently states products of connected objects need
not be connected — raises the chance the match is literal.
