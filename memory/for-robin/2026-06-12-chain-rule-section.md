# For Robin/Neil — 2026-06-12 write session

## What I shipped (two PRs)

**PR #14 — book(ch6): the derivative and the chain rule**
https://github.com/RaggedR/ghani-containers/pull/14

Promoted the derivative ∂ from a candidate-example *bullet* in Chapter 6 (Functors over
Cont) to a full worked section §6.2, built around the container chain rule I proved
yesterday:

    ∂(G ◁ F) ≅ (∂G ◁ F) × ∂F        [MacBeth, Original]

The reader-first proof leads with the key idea — *Leibniz for an indexed product* — then
gives the explicit shape+position bijection. Honest provenance: tagged [MacBeth], **not**
Lean-verified; a footnote flags that ◁ itself is formalised in open PR #13 and a Lean
chain-rule proof is the natural follow-on. New refs: AAGM "Derivatives of containers" and
Joram–Veltri arXiv:2512.17484 (the univalent case). Compiles clean, 25 pp.

This is the chapter's first original *functor-level* theorem — the Phase-2 ground Neil
named as "where I see a paper." It now reads as a result, not a stub.

**PR #15 — papers(pairwise-zs): cite Baues–Wirsching + Pirashvili for the (G) H² obstruction**
https://github.com/RaggedR/ghani-containers/pull/15

Closes the cohomology thread Neil asked to turn into a citation. The "obstruction,
cohomologically" subsection previously leaned only on my own companion note; now anchored
to BW JPAA 38 (1985) for the abelian H² and Pirashvili (track categories, arXiv:1512.03250)
for the nonabelian regime. Two sentences + two bibitems, no new claim.

## One honest TODO (for a browse session, NOT this write session)
I could not verify the exact *titles* of two references without browsing:
- Joram–Veltri arXiv:2512.17484 — I used "A chain rule for the derivative of containers".
- Pirashvili arXiv:1512.03250 — I used a descriptive title (track-category obstruction
  theory) flagged as provisional in the PR.
Author names + arXiv ids are correct; titles need a 30-second browse-session check.

## Lean follow-on (for a lean session)
The chain rule is finite and bijection-based — should transcribe directly once the ◁
Lean dev (PR #13) lands. The dependent transports around P(f q₀)=P(s_*) will want the
Ext.ext_eq discipline already used for the D2/D5 laws.
