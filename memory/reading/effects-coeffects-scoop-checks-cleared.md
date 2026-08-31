---
name: effects-coeffects-scoop-checks-cleared
description: Both pre-paper scoop-checks CLEAR (orthogonal, cite-as-neighbour) — Goncharov 2602.18295 (ICFP 2026) + Dumas–Duval–Reynaud 1310.0605; runway for effects⊗coeffects paper open
metadata:
  type: reference
---

Two scoop-checks owed before the effects-and-coeffects paper, both run 2026-07-30, both CLEAR.

**Goncharov–Peressotti–Tsampas–Urbat–Volpe, "Towards a Higher-Order Bialgebraic Denotational
Semantics", arXiv:2602.18295 (PACMPL ICFP 2026, DOI 10.1145/3828693).** ORTHOGONAL. Higher-order
Turi–Plotkin via **locally final coalgebras** (final for B(Z,−), Z fixed) as a syntax-decoupled
denotational domain; behaviour = mixed-variance bifunctor B:C^op×C→C. Zero occurrences of comonad /
distributive law / container / arrow / branching-classification. Their "bialgebra" = single carrier
that is Σ-algebra + B-coalgebra glued by a GSOS law (Turi–Plotkin sense), NOT a monad-over-comonad
mixed DL. ⟹ MANDATORY adjacent cite (shared "bialgebra"/"Plotkin–Turi" vocabulary, overlapping
Goncharov author group, hot top-venue) — distinguish: our "bialgebra face" = monad-over-comonad
mixed DL λ (PT-*style*) on containers, distinct from their GSOS bialgebras. No theorem overlap.

**Dumas–Duval–Reynaud, "Patterns for computational effects arising from a monad or a comonad",
arXiv:1310.0605 (Grenoble decorated/diagrammatic-logic school, Coq-checked).** ORTHOGONAL. Their
"associated comonad" = the SAME endofunctor M re-viewed as a comonad on M's own Kleisli category
(standard adjunction artifact), giving a 3-object tower C(0)→C(1)→C(2); NO distributive law / κ /
bialgebra between the two, NO containers. "Distributive" = distributive *category* only. Sanity-check
bonus: their state = **A×S comonad** (echoes my ΔS/Workers), exceptions = **A+E monad** (echoes the
E-summand of the affine E+A×(−) arrow class) — but they draw no classification. Cite-as-neighbour.

**2026-07-31 re-confirm (finer read, WebFetch):** verdicts hold. Drop-in cite sentence for the paper's
related work: *"Dumas–Duval–Reynaud pair a monad with its associated comonad as two dual but separate
equational proof-patterns (Kleisli vs coKleisli), whereas we entwine an independent shapes-monad T_M and
positions-comonad G_M on containers via a genuine mixed distributive law λ:T_M G_M ⇒ G_M T_M, with the
reverse arrow-compositor κ obstructed exactly when M branches."* Goncharov 2602.18295 = orthogonal
(behaviour-bifunctor coalgebras, no coeffect feed, no containers) — cite as the higher-order-semantics
sibling of the same GSOS lineage only.

Both PDFs downloadable via curl on /pdf/ (research MCP arxiv tools still 301-broken; curl route clean).
Links: [[neil-steer-2026-07-30-paper-reframe]] [[affine-classification-writer-exceptions]]
[[kru-interaction-laws-are-pairings-route-b-dead]]
