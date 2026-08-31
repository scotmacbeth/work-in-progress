# Pointer: "Containers over Vec" — expository note (new front)

**MacBeth → Neil, Robin — 2026-08-18**

**File:** `projects/expository/containers-over-vec.tex` (13pp, compiles clean with `pdflatex`).
**Companion proofs:** `projects/proofs/2026-08-18-linear-containers-vec.md`.
**Verification:** `projects/scratch/vec-containers/verify.py` (all checks pass).

## What this is
The first honest write-up of Neil's new front (email 08-15): *containers over Vec, answer space a
vector space*. A **linear container** is an object of `Fam(Vec^op)` — a set `S` of shapes, each with a
position **vector space** `P_s` — with extension `⟦S,P⟧ W = ⊕_s Vec(P_s, W) : Vec → Vec`. The note
measures how much of the Set container theory survives the base change `Set ↝ Vec`.

## The one-line result
**Everything is governed by one fact: `Set` is extensive, `Vec` is not.** The single inclusion
`∐ ⊊ ⊕` (disjoint union strictly inside biproduct) drives *both* failures at once:

- **Objects collapse.** `Vec`'s terminal object is `0`, so `⟦S,P⟧(0)=0` — no `F(1)=S`. For finite data
  `⟦S,P⟧ ≅ Id^N`, `N = Σ_s dim P_s`: the functor remembers only the total dimension, not the shapes,
  not even the partition. (Thm 4.1, Krull–Schmidt uniqueness.)
- **Morphisms lose fullness.** Natural transformations are indexed by the biproduct `⊕_t` (linear
  combinations across shapes); container morphisms by the disjoint union `∐_t` (one branch). The
  extension functor `⟦−⟧` is faithful but **not full**; the gap is exactly `∐ ⊊ ⊕`. (Thm 5.3.)

Same rivet. Object-collapse and morphism-collapse are one phenomenon: the failure of extensivity.

## Also inside
- **Composition** `⟦S,P⟧◁⟦T,Q⟧ = ⟦S×T, (P_s⊗Q_t)⟧` (finite-dim positions): the Set dependent-sum
  `∐_s T^{P_s}` **flattens** — linearity kills the branch-choice. (Prop 6.1.)
- **Comonoid probe (the crown target, honestly assessed):** a `◁`-comonoid gives only a *family of
  k-algebras*, NOT a full algebroid (`k`-linear category). The `DCont ≅ Cat` spine degrades to
  "comonoids = algebra-families" — a diagonal algebroid — because `◁` lost the dependent sum. Recovering
  a real algebroid needs a different (lax/bimodule) composition. **Marked `computed`, not proved** — the
  full comonoid-law check is a prove-session task. (Prop 6.3, Rmk 6.4.)
- **The carry-over table** (§7): the scorecard, each "fails" row tagged as an avatar of `∐ ⊊ ⊕`.
- **The neighbours ledger** (§8): strict polynomial functors (Friedlander–Suslin) own the *objects* —
  our functors are their degree-1 corner; vector species/TCA own the Day story; Diers owns "coproduct
  of representables + extensivity"; Mitchell owns "algebroid". **The container framing's delta is the
  assembly** — the shape index, and the identification of both collapses as one non-extensivity event.

## Honesty flags (please note)
1. **Prop 6.3 is `computed`, not fully proved.** The comonoid laws are verified on the diagonal; a
   complete coassociativity/counitality check across all shape components is owed. → next PROVE.
2. **Neighbour citations are attributions from general knowledge**, not yet deep-read into
   `sources.json` this cycle (no browsing in a write session). There is a boxed provenance caveat in §8.
   Before any external circulation, each primary source needs a browse-session deep-read.
3. **Gaps** (§9): general representation theorem (infinite `S`/∞-dim positions) is open; the right
   composition for genuine algebroids is open; ∞-dim composition not addressed.

## Grant framing
This is the first measurement of how the equivalence-chain spine
`Containers ≃ Dir.Cont ≃ Poly-comonoids ≃ Cat` **deforms under a base change to an abelian category**.
Two joints (shape-recovery, full faithfulness) snap at the same rivet (extensivity); composition
survives altered; comonoids-as-categories degrades pending a better composition. Diagnostic value: a
representation-theoretic version of the programme is possible but must route *around* non-extensivity,
and we now name the one obstruction to route around.

Neil — this directly answers your "start thinking about the categorical structure of Vec and how much
carries over." Happy to graduate the finite-collapse + extensivity-crux core into a book section once
the comonoid law-check lands. Robin can read the PDF straight off the projects volume.
