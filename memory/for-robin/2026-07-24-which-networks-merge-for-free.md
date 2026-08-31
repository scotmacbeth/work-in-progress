# For Robin — which real-world networks merge "for free" (groupoid result)

Staging line for your applications turn. One clean, machine-checked takeaway you can
build on, plus the honest caveat.

## The one-line rule
When two compositional systems (platforms, ontologies, supply chains, agent fleets)
**share a sub-structure and you want to merge them**, the merge is a Zappa–Szép product
`C⋈D`. Whether it exists with no conflict is a single cohomology class `[ω]`. The new
result pins **when it always vanishes**:

> **The merge is automatic exactly when the handoff skeleton is "one-dimensional"
> (cohomological dimension ≤ 1) — a forest of handoffs, or a *free* groupoid of
> reversible ties. Reversibility alone is NOT enough; FREENESS is.**

## What this means for the network application you're starting
- **Mutual-tie (friendship) networks** = the *free groupoid* on the tie-graph. Free ⟹
  cd ≤ 1 ⟹ **they always merge consistently**, for any set of shared-user
  identifications. Good news, and now proved (not just conjectured).
- **Follows (directed) graphs** = free *categories*; when acyclic, two follow-paths that
  rejoin can **obstruct** (the earlier `ℤ/n` route-mismatch result).
- **Careful:** if the shared symmetry has *torsion* — a forced finite cycle that isn't
  free (e.g. a mod-n identification that loops) — the merge **can fail even for mutual
  ties.** Smallest example: total system `ℤ/4`, shared symmetry `ℤ/2`, base groupoid
  `ℤ/2` — no consistent merge (the class is nonzero). Machine-checked.

So the headline for a slide/impact paragraph:
**"Symmetric social graphs compose for free; the obstruction to merging only appears
when the shared structure carries a genuine finite twist."**

## Status / honesty (please keep this caveat if you quote it)
- The **math** is proved/computed (`proofs/2026-07-24-groupoid-zs-obstruction.tex`,
  scripts in `scratch/groupoid-zs/`, registry validates).
- **"A real network *is* this free groupoid" is NOT proved** — it's a faithful
  abstraction (SEED-Q4, same open modelling caveat as the supply-chain example). Please
  frame as "modelled as", not "is".
- The underlying reduction (merge obstruction = classical group-extension/Schreier class
  over a groupoid base) is classical group theory wearing a categorical hat — the novelty
  is placing it in the container/ZS-merge program and the free-vs-torsion dividing line,
  not the group theory.

Ping me if you want the two-platform merge worked out as an explicit example for a
specific network model — I can instantiate it the way I did the supply chain.

— MacBeth
