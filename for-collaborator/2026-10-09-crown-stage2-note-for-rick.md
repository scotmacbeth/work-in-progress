# Covering note for Rick — branching is not a coproduct of branches (crown Stage 2)

**TO DELIVER (WAKE phase):** email Rick (grandparick20@gmail.com), CC Robin
(langer.robin@gmail.com). WRITE phase cannot send mail
([[feedback-wake-must-deliver-unsent-write-covering-emails]]) — this note is the owed
family-share; Rick is my only neighbour, so the result reaches the family through him.

**Attach / link:** `papers/crown-stage2-unfolding-vs-descent.pdf` (9 pp).
- Repo `scotmacbeth/work-in-progress`, content commit **`4136ecf`** (stamped p.1).
- PDF: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/crown-stage2-unfolding-vs-descent.pdf

---

## Draft covering note (3–4 sentences, per PROTOCOL §2.1)

> Rick — Stage 2 of the arboreal↔container ("crown") bridge, off the path base. The natural guess
> for reaching branching trees — make each branch a container *shape* and take their coproduct Ψ —
> turns out to be exactly wrong, and the way it is wrong is the whole note: Ψ computes the colourings
> of the *branch-unfolding* ⊔_b chain_b, over-counting the tree's colourings by the exact factor
> 2^{Σ_v(λ(v)−1)} (first at the V-tree, 8⊊16), because Fam=Σ is a coproduct and reconstructing the
> tree from its branch-cover is a *descent/gluing* datum of the opposite variance — the arboreal
> fibre is precisely the prefix-consistent (descent) sub-poset. The faithful encoding keeps **one**
> shape with positions = the whole node set (Ψ'), and a separate, higher obstruction (k-ary
> relations invisible to Cont(cod) for k≥2) caps the bridge at the unary fragment.
> **Grading, honestly:** the Ψ over-count (Thm, clause 2) and the k≥2 collapse (clause 3) are
> **proved** (exact finite counts, V/Y witnesses). The positive one-shape extension over the full
> tree base (clause 1) is **computed, conditional** on one input I did *not* re-prove — that arboreal
> cartesian lifts = preimage at *subtree* (non-path) embeddings (the pathwise-embedding
> characterisation at that generality; Remark 4.4 flags it). That conditional step is what I'm least
> sure about and would most value your eye on: is my V-tree verification + tree-independent sketch
> enough, or does the non-path cartesian case genuinely need the arboreal-axioms machinery?

## Provenance / registry housekeeping (for me, next cycles)
- Source of truth: `proofs/2026-10-09-crown-stage2-multishape-branch-extension.md`; builds on
  Stage 1 `proofs/2026-10-02-crown-stage1-orientation.md`.
- **Registry TODO (lean/registry session):** node `crown-stage2-multishape-branch-extension` does
  not yet exist as a `.json` in `proofs/registry/` — create it, grade **computed** (clause 1
  conditional; clauses 2,3 proved). Do not grade `proved` while (∗) is open.
- **Browse TODO:** the Jakl–Reggio "cartesian = pathwise embedding" theorem (prove-notes cite an
  arXiv id NOT in sources.json) is not deep-read; deep-read it to discharge (∗) / upgrade clause 1.
  Paper deliberately cites it only by author/title (no fabricated locator) and flags it as an
  unverified input.
- **Lean TODO:** the finite counts (V 8⊊16, Y 16⊊64, Ψ' 8=8, k≥2 4 vs 16) are a natural oracle in
  the nerve-level/gerbe-engine style. Scripts: `scratch/crown_stage2_{witness,more,positive}.py`.
- Not pushed to `publishable-result` this cycle — must go through Rick first (PROTOCOL §4.2).
