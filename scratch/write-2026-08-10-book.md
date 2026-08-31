# Write session 2026-08-10 — Ch3 non-closure, two-sided boundary

## Target
`books/category-of-containers.tex`, Chapter 3 "Which functors are containers?" (`ch:which`).
Extend the non-closure material so the boundary is SYMMETRIC: a monad witness AND a comonad witness.

## What's already there
- `sec:limits` (L563): products/coproducts preserved; teachbox "what Ext preserves & where it stops";
  coequaliser fails (Prop `prop:coeq-fail`, L647): Pair/swap → unordered pairs, cited AAGcat Ex 4.4.
  Closes with: quotienting by swap introduces a position automorphism; unordered-pair = analytic.
- `sec:boundary` (L682): synthesis "containers = summing representables; you leave the moment you quotient."

## The gap WRITE.md wants filled
The current witness (unordered pairs via coequaliser) is a FUNCTOR leaving the world.
Two upgrades:
  (M) **Bag** — a genuine MONAD on Set that is leaf-supported, reverse-total (μ a leaf-bijection),
      every reason to hope, yet |Bag(2×2)|₂ = 10 ≠ 9. A monad need not be a container monad.
      Mine (computed, bag_not_container.py) + Fiore et al (analytic over groupoids) + Lumsdaine MO corrob.
  (C) **Multigraph comonad** (Fairbanks, MO 457580) — a genuine COMONAD on Set, functor X³+X²/2+X,
      the coequalizer of the polynomial quiver comonad X³+X by edge-swap; fails pullback preservation,
      hence not a container. A comonad need not be a polynomial comonad = small category.
      [AWAITING research-agent verification of exact functor / construction / pullback claim.]

## Structural decision
Insert ONE new section between `sec:limits` and `sec:boundary`:
  `\section{Two witnesses that are (co)monads: Bag and the multigraph comonad}` label `sec:two-witnesses`
Then lightly amend `sec:boundary`'s final paragraphs to name both sides.

Why a new section not folded into sec:limits: sec:limits is about Ext preserving/failing (co)limits.
The new point is different and sharper: the failure survives even when you carry ALGEBRAIC structure
(monad/comonad) along — the object that leaves the world is not a bare functor but a bona fide
(co)monad. That deserves its own promise.

## Section arc (compute → generalise → synthesise)
1. Hook: the coequaliser witness was a functor. Does any genuine *monad* fall outside? Symmetric q for comonads.
2. Bag: define; show it looks like a container (leaf-supported, reverse-total, μ leaf-bijection);
   then the multiplicity swap w₁={(0,0),(1,1)}, w₂={(0,1),(1,0)} → same (π_A,π_B); 10≠9. Not a container.
   The obstruction = Sₙ symmetry = provenance (the pairing) lost. Analytic-over-groupoids (Fiore).
3. Multigraph comonad: the mirror. functor, coequalizer-of-quiver construction, pullback fails.
4. Synthesis box: both = provenance lost under a quotient (symmetrisation / edge-merging).
   "Polynomial not analytic" is TWO-SIDED. Forward-ref `rem:analytic-excluded` (Ch7): one level up the
   same boundary is "no natural counit" — Sym²/Bag₂ can't even be liftings.

## Citation status
- Bag: my computation (bag_not_container.py) = [MacBeth, computed]; Fiore et al = need bibitem;
  Lumsdaine MO 302631 = agent-summary → use as "see also", NOT load-bearing (I have my own proof).
- Multigraph: Fairbanks MO 457580 = agent-summary → research agent verifying now; add bibitem once confirmed.
- Forward ref target exists: `rem:analytic-excluded` (L3528).

## Voice
One monad, one comonad, one slogan. Concrete before abstract (Neil's pref). Bag first (the reader can
hold a multiset), then the comonad mirror. Don't over-claim the comonad details until verified.

## TODO after draft
- pdflatex compile clean
- citation_check.py footprint on the file
- push + note for Robin

## DONE (2026-08-10)
- Section written: `sec:two-witnesses` inserted before `sec:boundary`. Bag (prop:bag-not-container),
  multigraph comonad (prop:multigraph-comonad), two-sided teachbox. sec:boundary amended.
  bibitem Fairbanks25 added.
- Fairbanks MO 457580 VERIFIED verbatim by research agent (StackExchange API). CORRECTION:
  functor is (X³+X²)/2+X, not X³+X²/2+X (browse note wrong). Pullback fails on kernel pair of X→1:
  ((X³+X²)/2)²+X² ≠ (X⁶+X⁴)/2+X²=F(X²). Upgraded sources.json mo:457580 → deep-read.
- Compile: exit 0, 83pp, 0 undefined refs, no errors. (38 overfull hboxes = pre-existing book-wide.)
- citation_check footprint: clean; the one agent-summary floor (2405.13157) is PRE-EXISTING, not in
  my section. My Fairbanks cite is a MO \href (not arXiv), now deep-read; Bag = own computation.
- PROGRESSIVE_DISCLOSURE.md updated; memory `book-ch3-two-sided-boundary-done` + MEMORY.md pointer;
  note `for-robin/2026-08-10-ch3-two-sided-boundary.md`.
- No git repo for book (Robin reads projects volume). No email (write-session rule).
- No gaps/TODOs left in the math. No Lean/prove work needed.

## Refinements made in revision pass
- Replaced unsafe "free-monoid functor of §sec:test" cross-ref with inline list-functor description.
- Made F_dir's category identification concrete+verified (·⇉·, source 3 arrows→X³, target 1→X).
