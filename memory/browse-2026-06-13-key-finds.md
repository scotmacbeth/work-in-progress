---
name: browse-2026-06-13-key-finds
description: 2026-06-13 browse — Ch4 free/cofree citations, duoidal (⊗,◁) structure, Weihrauch surprise, cofree comonoid original
metadata:
  type: project
---

Key finds from 2026-06-13 browse. Full log at `reading/2026-06-13.md`.

**WRITE target (free monad/cofree comonad chapter):**
- **Gambino-Kock arXiv:0906.4931** (Math. Proc. Cambridge 2013) is THE citation for "free monad on a polynomial is polynomial." Positions = P-trees, directions = leaves. Construction: C* = Σ_{n≥0} C^{◁n} = initial algebra of X↦y+C◁X. Cite centrally in Ch4. UNREAD — priority.
- **Uustalu "Container Combinatorics: Monads and Lax Monoidal Functors" (TTCS 2017)** is the HUB paper every 2024-2026 container-monoidal paper cites. Characterises monads on containers via lax monoidal functors for ◁. Currently missing from MacBeth's citation list. UNREAD — read before WRITE session.
- **De Pascalis-Uustalu-Veltri arXiv:2509.25879** (2025) — proves monoid in (I-Cont,◁,y) = monad on Set^I, with free monad example. The non-indexed (I=1) case is MacBeth's book chapter. Comonoid side absent.
- **Cofree comonad = comonoid in (Cont,◁,y) is ORIGINAL to MacBeth.** No paper (De Pascalis, Uustalu TTCS 2017, Gambino-Kock, Libkind-Spivak) covers the cofree comonad as a comonoid with a universal property. This is MacBeth's genuine contribution to Ch4.

**PROVE target (coherence for four monoidal structures):**
- **(Poly, y, ⊗, ◁) is a NORMAL DUOIDAL CATEGORY** (Spivak-Srinivasan arXiv:2407.01849; also Shapiro-Spivak arXiv:2305.00167). "Normal" = ⊗ and ◁ share the unit y. ◁ distributes over ⊗ in a lax sense via the duoidal interchange. Pentagon/triangle for ◁ are instances of normal duoidal coherence. This is the right structural frame for the PROVE session.
- **Garner-López Franco duoidal coherence theorem** supplies the coherence equations MacBeth needs. Look this up before PROVE session.

**Most surprising: Weihrauch complexity = containers**
- Pradic-Price LICS 2026 (arXiv:2601.15420) — Weihrauch degrees from closed choice to parity game determinacy = ζ-fixpoints of container endofunctors. Free polynomial monad is the technical entry point. Completely new application domain for the grant narrative. Read before the next grant section write.

**Other new papers (unread):**
- arXiv:2409.02603 (Damato-Altenkirch-Ljungström, ITP 2025) — UIP-free formalisation of W-types and M-types for containers (Cubical Agda). Lean comparison point.
- arXiv:2502.10811 (Lamiaux-Ahrens 2025) — unifies Matthes-Uustalu heterogeneous substitution with monoidal framework.
- Purdy-Damato arXiv:2503.17191 (CALCO 2025) — completes the container DL zoo: all four monad/comonad combinations. Ch5 direction.

**New researcher:** Stefania Damato (Nottingham, Altenkirch group) — two container papers 2024-2025, Cubical Agda formalizer.

**Why:** These shape Ch4 (free/cofree) and Ch3 coherence — both active writing/proving targets.
**How to apply:** Read Gambino-Kock + Uustalu TTCS 2017 before WRITE session. Use duoidal frame for PROVE session. Cite Pradic-Price in grant impact section.
