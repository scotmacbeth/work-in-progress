# Supply-chain composition = Zappa–Szép product (computed worked example, Z/n obstruction)

**For:** Robin (applications infrastructure) and Neil (applications turn next week).
**Grade:** COMPUTED domain instantiation. Commits nothing to the book. Object-level fidelity
("a real supply chain *is* this category") stays OPEN (SEED Q4) — this is a faithful minimal
abstraction, exactly as `orchestration_zs*` was for agents.
**Artifacts:** `proofs/2026-07-23-supply-chain-zs.tex` (5pp, compiles) · `scratch/supply_chain_zs.py`
(all claims machine-checked) · `proofs/registry/supply-chain-zs.json` (validates clean).

## The one-line result

Two supply-chain flows sharing a warehouse serialize into a Zappa–Szép product `C ⋈ D` **iff the two
routes to the same delivered good agree on provenance**. The obstruction is a class
`[ω] = ε ∈ H²(Sk_C; Z/n) ≅ Z/n`, and `ε` is the *quantitative unit-mismatch* between the routes.
`ε = 0` composes; `ε ≠ 0` is an inventory inconsistency and no serialization exists.

## What is genuinely new vs. the orchestration note

1. **Object level (new).** The orchestration proof worked only at the category level. Here I write
   out the base chain `procure→manufacture→ship` as an explicit **directed container** `(S,P,o,↓,⊕)`
   — shapes = stages, positions = outgoing operations, `o` = stay-put identity, `s↓p` = destination,
   `p⊕q` = do-then-do — and machine-check the five Ahman–Uustalu D-laws. This is the tangible payoff
   of the lean-verified DCont≃Cat hinge in the applications domain, and it is greenfield in our corpus.

2. **Z/2 → Z/n generalization (new).** Agent orchestration needed one bit (a turn token). **Inventory
   is a counter**, so I replaced the token group by a cyclic lot-cursor `Z/n` (bin index / FIFO
   position mod n). The whole obstruction machine goes through verbatim (Z/n is abelian, so (T3)
   applies): `H² = (Z/n)²/diagonal ≅ Z/n`, and the class `[ω] = ε` now tells you *by how many units*
   the two provenance routes disagree — not just yes/no. The parity case `n = 2` **is** the proved
   orchestration re-entrancy bit (cited, not re-derived).

3. **Olog sibling (new instance).** `Book→Author→Name` as a directed container; merging along a
   shared `Author` type is the same ZS composition; a naming-convention clash is the nonzero class.
   Ontology-merge consistency and supply-chain consistency are literally the same `H²` bit.

## The grant line (honest version)

Supply-chain composability, ontology-merge consistency, and agent-orchestration re-entrancy are
**instances of one degree-two obstruction theorem** on the handoff category. The applications are not
new mathematics — they are new *instances*, and in the supply-chain case the invariant is refined
from a bit to a `Z/n`-valued count of the discrepancy. That is the Path-5 Impact spine, and it is
defensible precisely because the general theorem is already proved and lean-verified.

## What I did NOT claim (honesty ledger)

- Not that any real supply chain presents a category on the nose (SEED Q4, open).
- Not any new cohomology (Baues–Wirsching / Rosebrugh–Wood, cited).
- Not that the ε≠0 regime is "usually" what happens — it is the *checkable* failure mode; which
  regime a real chain is in is an empirical/modelling question, downstream of Q4.

## Suggested next steps (for discussion, not done here)

- Earn the object-level modelling criterion (SEED Q4): *when* does a real supply chain present a
  category? The morphism level is already ours (supply-chain map = cofunctor/update-lens).
- A non-cyclic token: if two warehouses each carry a lot-cursor and interact non-commutatively, the
  vertex group is non-abelian and (T3) no longer applies directly — that is the genuinely open
  non-abelian `H²` frontier (do NOT attempt to prove it; it is cited-tower territory).
