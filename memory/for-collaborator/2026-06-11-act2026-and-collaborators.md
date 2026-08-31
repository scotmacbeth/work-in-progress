# For Neil & Robin — ACT 2026 (urgent) + collaboration map

*Drafted in dream cycle 2026-06-11. Source: browse-session reading log. Turn into the
next morning email to Neil, CC Robin.*

## URGENT — act before June 15
- **ACT 2026 financial assistance deadline is June 15, 2026 (4 days).** If anyone
  (me-via-Robin, Robin, or a student) needs travel support for Tallinn (July 6–10),
  the application must go in now. Decision needed: are we attending, and does anyone
  need funding?
- **Neil's own ACT paper**: "**Snoc Trees**" (Ghani, Nordvall Forsberg, Fish — paper #8
  in the programme). No preprint is posted. **Can you send me the draft?** It's
  container-theoretic (snoc-list generalisations) and almost certainly touches our
  equivalence-chain work — I want to cite/align with it.

## ACT 2026 is unusually on-target for our program
Adjacent accepted papers we should engage in Tallinn:
- **Bumpus, Capucci et al. — "Algorithmic and Extremal Obstructions Through Presheaf
  Cohomology."** This is *directly* our open question. On 06-11 I proved the
  Zappa–Szép closure obstruction (G) is a cohomology class [ω] ∈ H²(Sk_C;𝒟). Their
  presheaf-cohomology local-to-global obstruction framework looks like the same
  machinery. **Highest-value conversation at the conference.**
- **Aberlé — "Compositional Program Verification with Polynomial Functors"** (Agda).
  Mealy machines = cofree comonad = bridges straight to my Lean comonad work. His
  dependent-polynomial specs suggest "dependent directed containers" for the grant's
  verification arm.
- **Braithwaite–Hedges–Mihejevs — "Polylang" + "Substructural Type Theories Modelled
  by Polynomial Functors."** Hedges is your former student; active Poly/lens program.
- **Sargsyan — categorical holonomy as a cubical presheaf** (quantum chemistry, but the
  same holonomy idea); **Albert–Dubut–Goubault — homology in abelian framed bicategories.**

**Strategic read:** there is *no* accepted ACT 2026 paper on delta lenses, cofunctors,
directed containers, or ZS-for-categories. Our DCont ≅ Cof + ZS-for-categories +
(G)=H² results are a **strong ACT 2027 submission** — and the people whose tools we
need (Bumpus/Capucci on cohomology, Clarke on lenses) will all be in the room in 2026.

## Collaboration / competition map (who to talk to, why)
- **Bryce Clarke — now at Strathclyde, your group.** In-house collaborator for the
  cofunctor/delta-lens paper. His Feb-2025 Grothendieck-construction-for-delta-lenses
  (arXiv:2502.21288) is the natural companion to our PR #7.
- **Purdy & Damato (CALCO 2025, arXiv:2503.17191).** They did the **monad side** of the
  container distributive-law zoo (Cubical Agda); their Example 4.9 explicitly cites
  Zappa–Szép. My pairwise (L∧G) criterion is the **small-category side** of the same
  structure. **Proposed joint paper:** "The Zappa–Szép Distributive Law: from Monadic
  Containers to Small Categories." They are also potential *competition* (could extend
  to categories first) — worth reaching out early. Our Lean vs their Agda = complementary.
- **Spivak / Topos.** His new **OrgTr** (arXiv:2602.17917) has directed containers as the
  constant-tree (stable-interface) special case — he didn't name it. A one-page note
  positions our verified core inside his adaptive-interface frontier; good grant story.

## My state (for the email's "what changed" section)
- **PR #9** opened: pairwise Zappa–Szép criterion written up self-contained
  (`papers/pairwise-zappa-szep.tex`). The SEED-Q2 prize is now in the shared repo.
- **PR #8** (Lean ZS: ZS1–ZS4 ⟺ associativity) and **PR #6** (Lean M4) still await
  review. (#3, #5, #7 merged.) The self-merge-vs-gate question is still open — please
  advise whether I should merge my own PRs or wait for a human.
- **(G) = H² proved** (local proof note; not yet a PR — `2026-06-11-G-obstruction-
  cohomology.tex`). Plan to identify it with Baues–Wirsching cohomology, then write up.
