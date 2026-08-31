# For Robin — Ch3 non-closure is now two-sided (Bag + multigraph comonad)

**2026-08-10 write session.** File: `books/category-of-containers.tex`, Chapter 3
("Which functors are containers?"). Compiles clean (`pdflatex`, 83 pp, 0 undefined refs).

## What I added

A new section **§"Two witnesses that are genuine (co)monads"** (`sec:two-witnesses`),
inserted between the limits/colimits section and the closing "boundary of the theory".
The chapter already had the coequaliser witness (Pair/swap → unordered pairs), but that
was a *bare functor* leaving the container world. The new section shows the boundary
survives the algebra, symmetrically:

- **Monad side — the multiset monad `Bag`.** Leaf-supported, reverse-total (μ is a leaf
  *bijection*) — every pointwise reason to be a container — yet fails the connected-pullback
  test: `|Bag(2×2)|₂ = 10 ≠ 9`, the collision `{(0,0),(1,1)}` vs `{(0,1),(1,0)}`. A genuine
  monad on Set can sit outside Cont. Prop `prop:bag-not-container`. (My computation,
  `bag_not_container.py`; forward-refs the Ch7 `thm:bag-refutes`.)
- **Comonad side (NEW) — the undirected-multigraph comonad `F(X)=(X³+X²)/2 + X`** (Fairbanks,
  MO 457580). The coequaliser, *in comonads on Set*, of `id` and the edge-swap on the
  polynomial quiver comonad `X³+X`. Fails the SAME test — the kernel pair of `X→1` — by
  Fairbanks's own one-line computation: `((X³+X²)/2)² + X² ≠ (X⁶+X⁴)/2 + X² = F(X²)`,
  i.e. *squaring every summand ≠ substituting a squared variable*. Prop `prop:multigraph-comonad`.

- **Synthesis teachbox "The boundary is two-sided":** both are quotients of a container by a
  symmetry (ordered tuples mod Sₙ; the quiver comonad mod edge-reversal); the quotient discards
  *provenance* (the pairing; the orientation), which is exactly what a polynomial functor must
  remember. "Polynomial, not merely analytic" is one two-sided law detected by one test.
  Forward-refs the Ch7 counit obstruction (`rem:analytic-excluded`): the same functors (Sym²,
  Bag₂) are excluded as monad *liftings* for want of a natural counit — the same boundary one
  level up.

Also lightly amended the closing `sec:boundary` paragraph to name both new witnesses.

## Provenance note (important)

I **verified the Fairbanks MO answer verbatim** (research agent, StackExchange API) before
citing — my browse note had the functor **wrong** (`X³ + X²/2 + X`; the correct functor halves
the whole `X³+X²`). Upgraded `sources.json` entry `mo:457580` to `deep-read` with the corrected
details. The Bag half rests on my own computation, not on any agent-summary source. Added a
`\bibitem{Fairbanks25}` (MO answer, attributed with question/answer id + date).

## For you / Neil to sanity-check

- The concrete claim that `F_dir = X³+X`'s category (under DCont≅Cat) is exactly `·⇉·` — I
  checked it by counting outgoing arrows (source has 3, target has 1). Worth a glance.
- No new Lean or proof work here (write-only). Nothing was left as a TODO/gap.

— MacBeth
