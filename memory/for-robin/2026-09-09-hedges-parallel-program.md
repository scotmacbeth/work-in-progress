# For Neil & Robin — Jules Hedges is running a parallel program, and it has now happened four times

**Date:** 2026-09-09 (dream consolidation). **Requested by** the 2026-09-08 browse log's follow-up:
stop flagging these piecemeal, send one note.

## The short version

Four of Jules Hedges' 2026 outputs land, independently, next to results I have already proved.
None of them cite containers-over-a-base, none cite me, and I do not think any of them knows about
the others as a group. This is **corroboration, not competition** — but it is now frequent enough
that it should shape where we publish and whom we talk to.

## The four

1. **"A first look at programming in Poly"** (julesh.com, 2026-06-29). A language where *types are
   containers*, *functions are lenses*, and the compiler targets a **noncommutative graded monad
   modelling a stack**. That is my Workers/BHM front — `T_P(X) = X ◁ P` graded by an arbitrary
   polynomial — arrived at from the implementation side.
   ⇒ Touches `workers-grading-is-fibre-of-bhm-polynomial-grading` (`proved`; the grading is a
   **retract**, not a fibre — `r∘σ = id`, `r∘δ = Δ(d)`, machine-checked in `WorkersRetract.lean`,
   sorry-free, 5/6 theorems axiom-free).
2. **"Sequents for sequence" I & II** (julesh.com, 2026-03-13 / 2026-03-23). A System L type system
   combining the **tensor and sequence products** of polynomial functors, citing Spivak–Srinivasan's
   linearly-distributive result for `(Poly, ⊗, ◁)`.
   ⇒ Same duoidal/LDC territory as my `proved` `(Poly, ⋉, ⋊, y)` normal-duoidal + LDC result
   ([[ltimes-rtimes-duoidal-ldc-proved]]). **Almost certainly a different pairing** (tensor/sequence
   vs. the two Dialectica tensors — mine are de Paiva's `⋉` and the directed `⋊`, DJN `2305.05655`
   §6), but "almost certainly" is not good enough. **Ask: is his pair mine?** One session.
3. **"Autodiff through function types"** (cybercat.institute, 2026-02-20). Proves the category of
   **additive lenses is cartesian closed**, via "additive containers = families of commutative
   monoids."
   ⇒ Sits directly on my `proved` Vec biproduct-collapse result ([[vec-biproduct-collapse-proved]],
   [[bare-dirichlet-comonoid-proved]]: `⊗`-comonoids in `Poly` = families of monoids). **Ask: is
   his CCC result new, or does it reduce to the collapse?**
4. **Applicative transformers** (cybercat, 2025-02-12) — already on file as one of the five
   independent categorical accounts of an attention layer ([[vec-attention-precedents-need-unification]]).

## What I think this means

- **My Front B thesis is generalising.** Front B was "five independent categorical accounts of
  attention, none citing another." The Hedges pattern says the same thing one level up: *the
  container/Poly account of a construction gets rediscovered from the implementation side, and the
  rediscoverers do not find each other.* That is the market gap the survey
  (`containers-over-a-base.tex`) exists to fill, and it is a stronger motivation paragraph than the
  one currently in it.
- **He is the natural first reader for the BHM note.** Robin and I had an open question about
  whether the BHM/`fibredness-vs-left-closure` note should go to Hedges. Item 1 answers it: he is
  building the graded-monad structure my Workers result classifies. I'd send items 1 and 3 as the
  hook, not the fibredness theorem.
- **Two concrete compare-passes are worth doing** (items 2 and 3 above), and both are cheap: read
  one post each, check whether the construction is mine under other names. If either *is* mine,
  that is a citation and possibly a collaborator. If neither is, that is two clean adjacent results
  to cite in the survey's landscape section.

## What I am NOT claiming

I have read these as blog posts via a browse pass, not as refereed sources. Nothing above is a
priority claim in either direction, and none of it is load-bearing for any registry node. The
`sources.json` entries carry the URLs and dates.

Related: [[workers-grading-retract-not-fibre-of-bhm]], [[ltimes-rtimes-duoidal-ldc-proved]],
[[vec-biproduct-collapse-proved]], [[hedges-table-proved]],
[[categorical-cybernetics-is-applications-frontier]], [[vec-attention-precedents-need-unification]].
