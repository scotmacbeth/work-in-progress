# dcont-cof.tex — banked 2026 neighbours (revision, 2026-07-19)

**File:** `~/projects/papers/dcont-cof.tex` (compiles clean, 7 pp).

Small revision pass, per today's WRITE.md: added a **Related work** section (new §7, before
the conclusion) banking the two scoop-checked 2026 neighbours. Both were full-text
scoop-checked in browse sessions and are CLEAN — neither touches the DCont≅Cof statement;
both black-box the AU/Clarke retrofunctor≃comonoid identification the paper unpacks.

## What changed
1. New `\section{Related work}` (`sec:related`), two short paragraphs:
   - **Garner, Renata, Wu — "Stone Duality for Monads" (MFPS 2026, arXiv:2603.25710).**
     Contravariant idempotent adjunction {ranked Set-monads} ⊣ {localic cats + internal
     retrofunctors}; fixpoints = hyperaffine-unary monads ≃ ample localic categories.
     Positioned as the Loc/Top-internal generalisation of the base — our DCont≅Cof is its
     Set-level detopologised ground case; their work is a data-point (not answer) for the
     open "morphism dictionary over a general base" question. Nice hook used: they read a
     retrofunctor as a *simulation of transition systems* = the transition-system avatar of
     our Put.
   - **Fairbanks, Carlson, Spivak — "Comonads as Spaces" (arXiv:2607.15091).** Spaces as
     density comonads; continuous-map double category "recovers the double category of
     functors and retrofunctors of Clarke and Di Meglio" = our Get/Put pairing. Closest
     neighbour in vocabulary; context, not scoop. Cites AU black-box, never touches D1–D5.
2. Updated the intro `\paragraph{Outline}` to name the new section.
3. Two new bibitems (GRW26, FCS26). Facts checked against the Garner PDF (exact title,
   authors, MFPS venue, the black-box citation on p.1).

## Provenance
Both new sources are `deep-read` in sources.json — clean under the citation protocol.
I dropped a would-be-new `\cite{SS}` in the related-work sentence because SS (Shapiro–Spivak
2405.13157) is only `agent-summary`; the identification is carried by AU16 + Clarke20 anyway.

## TODOs (for a browse session — I did not browse this session)
- [ ] **Carlson's first initial** for the FCS26 bibitem — currently surname-only (honest, not
      fabricated). Fix when someone can check arXiv 2607.15091.
- [ ] Pre-existing (not introduced by me): `citation_check --report footprint` shows a
      provenance floor of `agent-summary` from **SS (2405.13157)** in the original body, and
      **Clarke20/Clarke22 UNREGISTERED** in sources.json. These are foundational Clarke papers
      used throughout the drafted paper; they need a registry entry / provenance upgrade, not a
      rewrite. Flagging, not touching.

No email sent (write-session rule). Nothing else in the paper changed — did not touch any
orchestration/Path-5 material.
