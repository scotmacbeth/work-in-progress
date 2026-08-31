# For Robin — Vec landscape note now has the Schur resolution folded in (2026-08-19)

**File:** `projects/expository/containers-over-vec.tex` (recompiles clean, 17 pp, was 13 pp).
**Type:** revision/merge of an existing internal expository note — NOT a new arXiv paper.

## What I did
Merged the standalone Schur-coincidence resolution
(`expository/2026-08-19-vec-schur-coincidence.md`) into the main Vec-front landscape so the front
is now ONE self-consistent document. Three concrete changes:

1. **New §8 "The analytic lifting: Schur functors and the degree-one corner"** (`sec:schur`,
   inserted between the carry-over table and the neighbours ledger; neighbours→§9, open→§10).
   - Two liftings side by side: additive/Hom (ours, degree 1) vs analytic/tensor (Schur–species,
     degree |λ|). One-line fork: `S_λ(λ·id)=λ^|λ|·id` ⟹ k-linear-on-homs iff |λ|=1.
   - Prop 8.1: the additive lifting IS the degree-one slice `M_(1)⊗Id = Id^N`; multiplicity space
     `M_(1)` is the single number N that survives the collapse.
   - Worked example 8.2: degree-1 vs degree-2 table on k², with the `Sym²(V⊕W)` cross-term `V⊗W`
     killing additivity ⟹ Sym²/Λ²/W⊗² are not containers (not even Vec-functors).
   - Verdict + what Schur does NOT touch: (a) morphism-layer extensivity crux invisible to species;
     (b) the ◁-comonoid axis (plethysm = analytic ◁; ours is its degree-1 shadow).
   - Remark 8.4: char-p trap (Speyer: S_(2)≅S_(1,1) pointwise in char 2; collapse itself is
     char-independent).

2. **Fixed the additive→cocontinuous correction.** New Remark 4.x (`rem:cocont`) right after the
   collapse theorem: additivity alone does NOT force Id^N (`Vec(P,−)` dim∞ = product functor ∏W;
   `W↦W**` additive but not Id^N). The right hypothesis is **cocontinuous**; Eilenberg–Watts ⟹
   F ≅ F(k)⊗− ≅ Id^{⊕dim F(k)}. Finite linear containers ARE cocontinuous. This is now the single
   clean E–W statement; Cor (recovery) and the §9 ledger stay consistent with it. Also fixed the §2
   non-example line ("additive functor built from Id" → "cocontinuous ... built from Id under ⊕").

3. **Sharpened the provenance caveat box.** Now explicitly covers the new §8 rep-theory facts
   (Schur–Weyl, char-0 "Schur = polynomial species", the semisimple ⊕S_λ decomposition, degree
   bookkeeping) as general-knowledge, NOT deep-read. Nothing upgraded to load-bearing — the content
   rests on the proofs + the elementary degree calc. No `\cite`/bibliography in the doc; all inline.

## Honest status
- Verdict trust grade = **computed** (facts textbook; the degree-1-corner placement is a conceptual
  synthesis on the proved 08-18 collapse result, not itself a new theorem). Framed that way.
- No novelty claimed over Schur/species/strict-poly. The delta is the assembly: shape index +
  carry-over + the ◁-comonoid axis + identifying object-collapse & morphism-collapse as ONE
  extensivity failure.
- Prop (comonoid) still carries its "computed, not fully proved" caveat — unchanged (prove-session
  task, the full coassociativity/counitality verification across all shape components).

You can read the compiled PDF directly on the projects volume:
`projects/expository/containers-over-vec.pdf`.
