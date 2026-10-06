# For Robin — new note: supply-chain inventory is a degree-1 class (2026-10-06)

Shipped a 9-page applications note this write session.

**Title:** *Supply-chain inventory consistency is a degree-one class, and is independent of the
Zappa–Szép weld obstruction.*

**Where:** `papers/supply-chain-inventory-degree-one.tex` (+ `.pdf`), pushed to
github.com/scotmacbeth/work-in-progress — commits `33ce5c9` (content) and `6f1fbd2` (PDF stamp).

**The one sentence.** Inventory consistency is *not* the vanishing of the Zappa–Szép weld class
`[ω]∈H²(Sk;𝒟)` (which governs whether the chain factors at all). It is the vanishing of a
**degree-1** class `[θ_R]∈H¹(𝒮;R)` on the resource presheaf — the route-reconvergence
discrepancy — and the two are **independent** (different degree, different coefficients, neither
implies the other). The payoff for the grant: **the cohomological degree of a compositional
failure records *where* the conserved quantity lives** — on the nodes (H¹, route discrepancy,
= supply chains) or in the weld (H², handoff order, = blockchain re-entrancy). Two economic
failure modes, cleanly separated by degree.

This *refutes* the obvious conjecture (C) "inventory consistent ⟺ `[ω]=0`" in both directions,
with explicit witnesses (free diamond: `[ω]=0` yet inconsistent; rigid-twist: `[ω]≠0` yet
consistent). It is honest about scope: torsor-valued inventory would rise to a genuine H²
(gerbe), still ≠ `[ω]`; object-level fidelity of the model remains SEED Q4. I also relabelled
the old `W_{n,ε}` worked example — it correctly computed the *weld/provenance* class, not the
node-stock class the phrase "two routes" names. Nobody made an error; the phrase was overloaded.

**For Strathclyde / the grant.** This is the Applications-pillar complement to the tangent/Cartan
theory arc. Slot it next to the re-entrancy note: same H²-obstruction machine, but supply chains
are the *first clean H¹ instance*, not a second H² instance.

**One flag for you (plumbing, not urgent).** The `state/WRITE.md` trigger for this cycle was
**stale** — it pointed at the Lanfranchi parallelizability note, which was already shipped
earlier the same day (commit `e154282`). I detected it via MEMORY.md + the existing PDF and fell
through to the most significant unwritten proof (this one), per the standing
check-registry-before-dispatch discipline. Worth having the wake phase clear `WRITE.md` after a
note ships so it doesn't re-fire. I have **not** touched the trigger files this session (that's
the wake phase's job).

— MacBeth
