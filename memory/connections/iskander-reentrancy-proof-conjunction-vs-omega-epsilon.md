# Industrial reentrancy verification gets composability for FREE — a contrast case for [ω]=ε

**Surfaced:** 2026-09-19 browse (`reading/2026-09-19.md`). **Source:** Iskander,
"Tridirectional Discriminating-Power Formal Verification of Smart Contract Reentrancy Defense"
(arXiv:2606.01794, June 2026) — **deep-read** this session (arXiv agent + WebFetch HTML/PDF).
Grade: `agent-summary` until logged in `sources.json`; the mathematical claim below rests on my
own proved [ω]=ε result, the Iskander paper only supplies the contrast.

## The two accounts of "reentrancy-safe composition"
- **Mine ([[lean-reentrancy-omega-equals-epsilon]], `lean-verified`):** composability of guarded
  contracts is a *categorical obstruction* — the class `[ω]=ε ∈ H²≅𝔽₂`. Composition is a
  distributive-law / entwining question; the obstruction can be nonzero.
- **Iskander (industrial, Lean 4, propext-only, zero sorry):** the OpenZeppelin reentrancy-guard
  pattern is verified against a source-level state-machine model of production Solidity (DAO,
  Compound, Aave), and the capstone theorem is the **literal conjunction** `⟨h_dao, h_compound,
  h_aave⟩` of three independently sealed proofs under a "no-retrofit discipline". Composability
  here is **pure proof conjunction** — no distributive law, no entwining, no coalgebra, no H².

## Why this is a real ASSOCIATE finding, not just two papers on reentrancy
A real-dollar-stakes verification achieves composition with **none** of the obstruction-theoretic
machinery my account treats as essential. Two honest readings, and they are a fork worth stating to
Neil rather than filing silently:
- **(a) The obstruction is trivially absent.** The three guards don't structurally interact — each
  contract's guard state is independent — so the entwining is trivial and `[ω]=0` by construction.
  Proof conjunction is exactly what composition looks like *when H² vanishes*. This would make
  Iskander a **confirming boundary instance** of my theory (the degenerate, zero-class corner), and
  the "no-retrofit discipline" would be the informal name for "keep the guard states disjoint so no
  cocycle can form".
- **(b) A real gap.** The "no-retrofit discipline" is silently doing the distributive-law work — it
  *is* the side condition that forces `[ω]=0` — and the categorical account should be able to
  *derive* that discipline as the vanishing criterion but currently doesn't state it operationally.

Either way the lesson is the same: **my [ω]∈H² account predicts WHEN proof-conjunction suffices**
(iff the class vanishes), which is precisely the content an industrial verifier assumes implicitly.
That is the grant-relevant framing — the categorical obstruction is the *decision procedure* for
whether the cheap (conjunction) composition is sound.

## Seed placement
Path 5 (blockchain/smart contracts as coalgebras, reentrancy as failed distributive law) meets the
orchestration/ZS thread ([[orchestration-composition-is-zappa-szep]], [ω]∈H²). Confirms the
standing browse verdict: **the categorical framing of smart-contract composability is a literature
gap** (reading logs, multiple cycles: ethereum.SE treats reentrancy only as checks-effects-
interactions engineering, never categorically). Kodamai would be *creating* this connection.

## Action (WAKE, not this dream)
Flag 2606.01794 to Neil as the contrast case; short comparison read on the next PROVE/WRITE touch of
the reentrancy line — settle fork (a) vs (b) by checking whether the three guard state-machines are
literally independent in Iskander's model.

Related: [[lean-reentrancy-omega-equals-epsilon]], [[cohomological-obstruction-family]],
[[three-modes-of-composition]], [[total-composition-constructs-partial-composition-lifts]].
