# The Complete Dossier — narrative spine (MacBeth, draft 2026-09-23)

> Neil asked for "the complete write up of everything." This is the connective tissue —
> the single thesis that turns a stack of papers into one document. The inventory agent
> supplies the section→artifact map; this supplies the story that orders it.

## The one thesis

**Composition of heterogeneous computational systems is governed by a single equation,
and that equation is checkable.**

    a composite is correct  ⟺  (L) ∧ [ω] = 0 ∈ H²

- **(L)** — the *local* condition: each part is a directed container (equivalently a small
  category / polynomial comonoid). This is the Containers ≃ Directed Containers ≃
  Polynomial Comonoids ≃ Small Categories equivalence chain. It says each part composes
  *with itself* coherently.
- **[ω] = 0** — the *global* condition: the parts weld into a whole. The weld is a
  Zappa–Szép product (equivalently a distributive law); it exists iff a degree-2
  cohomology class [ω] ∈ H² vanishes. This is the pairwise ZS criterion.

Everything in the program is either (i) a *proof* that this equation holds and is the right
one, (ii) an *application* where a real system's failure mode is exactly [ω] ≠ 0, or
(iii) a *formalisation* that makes the check machine-executable.

## Why this is the correct foundation (not just a slogan)

Three independent research programs — container theory (Nottingham: Abbott–Altenkirch–Ghani),
directed containers (Tallinn: Ahman–Uustalu), and Poly (Topos: Spivak) — developed the same
mathematics in three dialects and converge on the equivalence chain. The convergence is the
evidence: when three groups reach the same object from three directions, the object is real.
The dossier's Theory pillar makes the convergence explicit and then does something none of
the three did: it turns the *composition* question (when do two of these things compose?)
into the checkable cohomological criterion above.

## The four movements

**I. THEORY — the equation and its domain of validity.**
1. The equivalence chain (the (L) side). Four dialects, one object.
2. Zappa–Szép / distributive laws as *the* composition tool; the pairwise criterion
   (L) ∧ (G), and (G) ⟺ [ω] = 0 ∈ H². This is the correctness equation.
3. The H²-cluster: three genuinely distinct H² obstruction theories live on DCont ≃ Cat
   (ZS holonomy, Ferri prunability, the direction-functor H²_Cat_B). Not one theorem wearing
   three hats — a structured family. (Honest: the protomodular unifier was REFUTED.)
4. How far does the equation generalize? The Fam(C^op) / change-of-base story. Sharp
   negative: the self-enriched full-and-faithful change-of-base container semantics collapses
   to {Id} — no nontrivial effect monad supports it. Knowing the boundary IS the result.
5. **The deepest boundary — the equation's domain is set-theoretic.** Vec-admissibility /
   Gap-S: whether Vec is ◁-admissible reduces to a projectivity question over the full linear
   ring, and its generation number μ_S(M) = 𝔡, the dominating number. So the conjecture is
   FALSE under CH/MA/Cohen and the residual is a single crux in the random real model. The
   composability boundary of a categorical semantics is a *cardinal characteristic of the
   continuum*. This is the crown jewel: a container-theoretic question answered by the
   Cichoń diagram.

**II. APPLICATIONS — where [ω] ≠ 0 costs money.**
The equation earns its keep because real systems fail exactly when the weld obstruction is
nonzero. Same mathematics, five domains:
- GA composition: migration topology = the distributive law; diversity dynamics determined
  by whether the ZS product exists (Kendall's W = 1.0 empirical).
- Blockchain: re-entrancy is a *failed distributive law*; smart contracts are coalgebras for
  p(X) = (O×X)^I; the DAO-class bug is [ω] ≠ 0.
- Security audits: state-divergence bugs (Trail-of-Bits class) are failed distributive laws.
- Agent orchestration: the harness is a worker (store-comonad); composing stateful workers
  needs a comonad distributive law; a wrong interleaving is the re-entrancy class again.
- Tax computation (Catala): ontology DAG + scope composition + comonadic event-sourced
  projections. HONEST GAP: no formal artifact yet.

**III. FORMALISATION — the check is executable.**
The Lean milestones M1–M3 and the sorry-free results (ZS associativity, [ω]=ε, the {Id}
collapse core, the union-of-subspaces counting lemma, VecCollapse not-faithful). What is
lean-verified vs proved-on-paper, stated honestly. This is the deliverable that distinguishes
the grant from hand-waving.

**IV. IMPACT — and a note on honesty.**
Compositional correctness has economic consequences precisely in the Application domains.
Plus the AI+Lean-pipeline honesty cluster: the recent public evidence that AI-authored Lean
proofs are real (Köthe refutation, GPT-6/Astra) AND that "verified ≠ reusable / correctly-
stated" — the grant's credibility rests on walking that line, which this program does (see
the Lean statement self-audits).

## The honest ledger (must be in the dossier, up front, not buried)
- The Gap-S / Vec-admissibility wall is OPEN. We have FALSE-under-CH/MA/Cohen and the μ=𝔡
  invariant; the full ZFC status (independence) is unproved. Residual = random real model.
- Tax computation has NO formal artifact.
- Nothing is externally published (ACM authorship rule; Robin holds the queue). Strongest
  grade is Rick-refereed / peer-reviewed (mcontainers).
- The H²-cluster protomodular unifier was refuted; the three theories are distinct, not one.

## Ordering principle for assembly
Lead with the equation (Theory §2), because it is the thesis. Put the equivalence chain
first as its (L) foundation. Put the set-theory arc LAST in Theory (it is the frontier, and
it is open — end the Theory pillar on the live edge, not a solved one). Applications second
(they justify the theory). Formalisation third (they verify it). Impact + honest ledger last.
