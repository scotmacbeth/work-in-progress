# Community browse — 2026-07-30 (second pass)

## Method note — MO/cstheory are NOT actually dead, prior "confirmed dead" verdict was a wrong tool choice
Prior browse sessions concluded MathOverflow and cstheory.SE were unreachable: WebFetch hard-blocks
both domains, and WebSearch with `site:` filters silently substitutes arXiv/Wikipedia results instead
of real hits. **That conclusion was premature.** The public StackExchange API
(`api.stackexchange.com/2.3/search/advanced?...&site=mathoverflow.net` or `site=cstheory`) is NOT
blocked, works cleanly via plain curl, and returns full question+answer bodies with `filter=withbody`
(no auth needed, ~300 quota/session). Recommend this API as the standard method for future MO/cstheory
browse passes, replacing the HTML-scraping approach.

## 1. "When is a container a monad?" (MathOverflow, Jan 2024) — OPEN, 0 answers
https://mathoverflow.net/questions/461865/when-is-a-container-a-monad
Asked by Ben Sprott. Poses the *dual* of Ahman-Chapman-Uustalu's "When is a container a comonad?"
(the directed-container paper underlying DCont≅Cat). Zero answers after 1.5 years — genuinely open on
the public record. Adjacent to the free-monad-UP and ⊗-monoid/⊗-comonoid classification work
(`bare-dirichlet-comonoid-proved.md`, `free-monad-universal-property-proved.md`). Worth a line in the
book's further-work section; the ⊗-monoid classification is arguably already a partial answer and
could be posted as an MO answer.

## 2. "About Coreader Comonads" (MathOverflow, Sept 2024) — answered, score 5
https://mathoverflow.net/questions/478413/about-coreader-comonads
Same asker, citing Karamlou-Shah's LICS 2024 no-go paper (already cleared as orthogonal,
`ks-nogo-not-h2.md`). Top answer independently re-derives directed-container = small category from
scratch — no new content, but a nice "this is obviously the right definition" external signal.

## 3. "Examples of non-polynomial comonads on Set?" (MathOverflow, Oct 2023) — answered, 3 answers
https://mathoverflow.net/questions/457580/examples-of-non-polynomial-comonads-on-set
Useful for "which functors are containers" (`book-chapter3-which-functors.md`,
`containers-preserve-connected-not-empty.md`). Sharpest answer (score 6): a pullback-preserving
comonad on Set is the same thing as a Grothendieck topos with enough points; non-polynomial
pullback-preserving comonads correspond exactly to toposes that are NOT presheaf toposes. Clean
citable boundary statement: polynomial comonads = the presheaf-topos case.

## 4. Weihrauch-containers frontier: new arXiv sibling (surfaced via search)
"A topos for extended Weihrauch degrees" — Maschio & Trotta, arXiv:2505.08697. States: extended
Weihrauch degrees over a filtered PCA are isomorphic to the posetal reflection of the category of
containers over partitioned assemblies. Direct continuation of the frontier flagged in
`weihrauch-containers-frontier.md`. See citation-trail note for fuller content and the derivative-row
verdict.

## 5. Arrow category / Freyd category / commutative monads — no fresh community threads
Repeated cstheory.SE queries returned only old tangential threads. Nothing engaging Atkey's "Arrows
are not Freyd categories" or Jacobs-Hasuo "Freyd is Kleisli for Arrows" in Q&A form — that literature
lives entirely in papers. No scoop risk.

## 6. Bialgebraic semantics / Plotkin-Turi / effects-coeffects — no MO/cstheory hits
No threads found; only the standard paper trail already cleared as orthogonal/neighbour
(`effects-coeffects-scoop-checks-cleared.md`).

## 7. Zappa-Szép product / distributive law — MO has group-theory traffic only
Live MO threads on ZS products are pure finite-group-theory, no crossover into the container/comonad
framing. Nothing suggests anyone outside this line of work connects ZS products to directed
containers or [ω]∈H² obstructions. Territory looks clear.

## Blocked/dead sources
nForum, category-theory Zulip archive: no usable content via WebSearch. Direct WebFetch to
mathoverflow.net / cstheory.stackexchange.com hard-blocked; StackExchange API is the reliable
workaround.

## Bottom line
Nothing overturns or scoops current results. Two follow-ups worth noting: (a) the open "when is a
container a monad?" MO question is a free citable open problem, partially answered already by the
⊗-monoid classification; (b) the pullback-preserving-comonad = topos-with-enough-points
characterization is a clean citable boundary statement for Ch3. The Weihrauch topos paper should get
a dedicated scoop-check on container-derivative content (see citations note — already done this
session, verdict: derivative row stays open).
