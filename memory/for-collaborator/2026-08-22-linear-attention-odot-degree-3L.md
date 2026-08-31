# Linear attention = ⊙ in Mat(Vec) — exactly at fixed context; the strong "stack = one matrix" is FALSE (degree 3^L)

**MacBeth, PROVE session 2026-08-22.** For Neil / Robin / Rick.
Proof: `proofs/2026-08-22-linear-attention-odot-composition.md`. Registry: `proofs/registry/vec-attention-composition.json` (validates, `proved`). Scripts: `.claude/scratch/attn_toy{,2,3}.py`.

## The one-paragraph version
Neil's "find a use for VCont" thread hoped a depth-L linear-attention stack would be a **single**
Vec-matrix (one ⊙-composite in Mat(Vec)), making §4's "pipeline = ⊙" a theorem for a real ML
primitive. **It isn't** — and the reason is clean and quantitative: a live (data-dependent) depth-L
linear-attention stack with identity feature map is a homogeneous polynomial map of degree **exactly
3^L** in its input tokens, while any ⊙-composite acts *linearly* (degree 1) on its argument. So the
stack is a single Vec-matrix only for L=0. What **is** true — and genuinely functorial — is the
**fixed-context** (frozen-KV, φ=id) picture, which is exactly the in-context / KV-cache regime. There
the wiring calculus holds with **two functors**: contexts compose by ⊕ (the §4 *menu* wiring), depths
compose by ⊙ (the §4 *pipeline* wiring).

## What's proved (all exact to machine eps; see the table in the proof file)
- **(A) one head's readout = one ⊙**, contracting over the **feature index** d_φ. This grounds §3's
  abstract "intermediate prompt b" as the concrete feature dimension. (Reassociation — translation-level.)
- **(B) context = ⊕-monoid-hom**: S(C·C') = S(C) ⊕ S(C'). This is linear-attention-as-linear-RNN
  (Katharopoulos 2006.16236), repackaged as the §4 menu wiring acting on *contexts*.
- **(C) frozen depth = ⊙**: frozen φ=id heads form a full sub-bicategory of Mat(Vec); depth = matrix
  product. (Low novelty; the content is that fixed-context is *exactly* the ⊙ regime.)
- **(D) THE result — degree 3^L**: Lemma D0 (one live layer is degree-3: S = W_K XᵀX W_Vᵀ is degree 2,
  times the query degree 1), induction ×3 per layer. Corollary: strong "stack = one Vec-matrix"
  **REFUTED** for L≥1. (D1) softmax is not a ⊙ at all (non-homogeneous + bounded/partition-of-unity).
  (D2) nonlinear φ keeps ⊙ only in feature space.

## The delightful part (flagged speculative — needs a deep-read)
**O'Neill 2501.02931** (I only have an agent-summary) independently models linear attention as a
parametric 1-morphism in Para(Vect) and models **stacking as the free monad on the induced
endofunctor** — a non-collapsing *tower*, not one morphism. **Theorem D is the quantitative reason
this is forced**: degree 3^L differs at every depth, so no single morphism represents the tower — you
*must* keep F, F², F³, … That is exactly a free monad. Para(Vect)'s fixed-parameter map = my
fixed-context regime; ⊙ in Mat(Vec) is its feature-axis shadow; the degree explosion is what happens
when the "parameters" (the KV-state) are themselves functions of the input. This also rhymes with my
own [[lean-free-monad-unit-laws-done]] (free monad = ◁-monoid). **Ask:** can someone deep-read
2501.02931 §on stacking so we can promote this from conjecture to a proved equivalence? It would be a
real cross-domain weld (attention stacking ↔ free monad ↔ ◁-monoid) for the grant.

## Honesty ledger
Single-layer-as-matrix is **not** novel (Vertechi parametric spans, O'Neill Para(Vect)). (A) is
reassociation, (B) is the known linear-RNN fact. The genuine deltas are **Theorem D (degree 3^L)** and
the **fixed-context = exact-⊙-regime framing with the ⊕/⊙ functor pair**. Sargsyan 2603.16123
(deep-read) corroborates the softmax boundary at the functoriality level; D1 is proved independently.

## Grant sentence
*The §4 compositional (⊙/⊕) calculus is a theorem for linear attention precisely in the in-context
regime — two functors, contexts by ⊕ and depths by ⊙ — and the obstruction to compressing a trained
network into one weight-matrix is a single clean invariant: a live depth-L stack has degree 3^L, which
is exactly why deep attention must be a non-collapsing tower (free monad), not a single matrix.*
