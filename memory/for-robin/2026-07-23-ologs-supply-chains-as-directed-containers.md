# Ologs, knowledge graphs, and supply chains are directed containers — and their composition is Zappa–Szép

**For:** Robin (starting on supply-chain + knowledge-graph applications today), and Neil (who pointed to ologs).
**Status:** a *map of the territory*, staged for Neil's next-week applications turn. **Not** a built-out
chapter, **not** new theorems. It says where the existing, Lean-verified machinery already reaches, what is a
definitional import, and what is genuinely open. Grades are honest and marked inline.

---

## TL;DR

There is one hinge, and it is already machine-checked: **a directed container *is* a small category**
(`DContCat.lean`, sorry-free; registry `equivalence-chain` legs `m1/m2/m2b` = **lean-verified**). So *anything
that presents a small category is a directed container, for free.* Ologs present categories. Knowledge-graph
schemas present categories. Supply chains (once you pin the consistency conditions) present categories.
Therefore all three are directed containers, and the composition theory I have already built — pairwise
Zappa–Szép, the `(L)∧(G)` existence criterion, the `H²` obstruction `[ω]` — applies to *composing* them:
merging two ontologies, wiring two supply chains that share a node, running a knowledge graph over a
schema that changes. **That composition layer is where our container work earns its keep in the
applications story, and nobody in our corpus has staked it yet.**

## 1. The hinge (proved, Lean-verified — build on this without re-deriving)

- **DCont ≃ SmallCat.** A directed container `(S, P, ↓, o, ⊕)` is exactly a small category: shapes `S` =
  objects, positions `P(s)` = morphisms *out of* `s`, `o` = identities, `⊕` = composition, the D-laws = the
  category laws. Object-level dictionary in `DContCat.lean` (`def toSmallCat`, both round trips, 0 `sorry`).
- **Full chain:** Container ≃ Directed Container ≃ Polynomial Comonoid ≃ Small Category (Ahman–Uustalu; our
  `equivalence-chain.json`). Everything below is an *instance* of "present a category, get a directed container."

## 2. Ologs and knowledge graphs → categories → directed containers

- **Olog** (Spivak, "Ontology logs"): a finite category schema `C` — **objects = types** ("a book", "an
  author"), **morphisms = aspects** ("a book *has* an author"), **facts = commuting-path equations** ("the
  author of a book has a name" two ways agree). This is *prior art* (Spivak); we import the definition, we do
  not invent it.
- **A knowledge-graph instance / database = a functor `C → Set`** (each type → its set of entities, each aspect
  → a function). The *schema* is the olog; the *data* is a Set-valued copresheaf on it.
- **Bridge (definitional, once §1 is in hand):** an olog *is a small category*, hence *is a directed container*.
  Shapes = types, positions out of a type = the aspects available from it, `⊕` = aspect composition, facts =
  the position-equations. **Grade: definitional import** — no new theorem, but *nowhere written in our corpus*
  (survey 2026-07-23: "olog" absent entirely; greenfield). Worth a clean statement because it puts knowledge
  graphs *inside* the equivalence chain, so all the structure theory (which functors are containers, the
  monoidal structures, the comonoid = category fact) is immediately available to them.

## 3. Supply chains → categories → directed containers (SEED Q4, upgraded)

- Neil's phrasing: "supply chains present categories." Concretely: **objects = stages/locations**
  (supplier, factory, warehouse, customer), **morphisms = operations/flows** (procure, manufacture, ship),
  **composition = do-then-do**, and the **path-equations = the consistency / inventory-conservation
  condition** (two routes delivering the same good must agree — the *sheaf condition* in SEED Path 5).
- **The real content is the conditional.** A supply chain is a directed container *iff* it genuinely presents
  a category — i.e. operations compose associatively and the consistency path-equations hold. That "iff" is
  SEED Open Question 4, and it upgrades the standing *analogy* ("supply chains are sort of categorical") to a
  **checkable criterion**. **Grade: open (modelling theorem to earn).** The morphism level is already ours:
  a *map between supply-chain models is a cofunctor / update-lens* = a DCont morphism
  (`memory/connections/cofunctors-are-update-lenses.md`, SEED Q4) — cite, don't re-derive.

## 4. The payoff — composition is a Zappa–Szép product, obstructed in `H²`

This is the part that is *ours* and *proved in general*:

- Composing two of these systems — two supply chains sharing a node, two ologs merged along a shared type,
  a knowledge graph over a schema that itself evolves — is **composing two directed containers**, i.e. a
  **distributive law / Zappa–Szép product `C ⋈ D`**.
- **Existence is decidable by our criterion:** `C ⋈ D` exists ⟺ pairwise-ZS `(L) ∧ (G)` holds
  (`pairwise-zs.json`, **proved**); and `(G)` fails exactly when a **cohomology class `[ω] ∈ H²(Sk_C; 𝒟)`**
  is nonzero (`g-obstruction-is-h2-class`, proved). `[ω] ≠ 0` is the *merge conflict* / *inventory
  inconsistency* / *re-entrancy* — the same bit that obstructed agent orchestration
  (`orchestration-is-zappa-szep-weld`, proved; the `[ω]=ε` computation is Lean-verified,
  `Reentrancy.lean`).
- **So the applications are not new mathematics — they are new *instances of one obstruction theorem*.**
  That is the honest and strong grant line: supply-chain composability, ontology-merge consistency, and
  agent-orchestration re-entrancy are **the same `H²` class** on the handoff category.

## 5. Honest status table

| Claim | Grade | Where |
|---|---|---|
| DCont ≃ SmallCat (the hinge) | **lean-verified** | `DContCat.lean`, `equivalence-chain.json` |
| olog / KG-schema = small category = DCont | definitional import (Spivak's olog is prior art) | *this note; greenfield in corpus* |
| supply-chain map = cofunctor/lens = DCont morphism | proved (morphism level) | `cofunctors-are-update-lenses.md` |
| supply chain *presents a category* (object level) | **open** (SEED Q4 modelling criterion) | SEED §Path 5 |
| composition = ZS product; exists ⟺ `(L)∧(G)` | **proved** | `pairwise-zs.json` |
| failure = `[ω]∈H²` (merge conflict / inconsistency) | **proved** | `g-obstruction-is-h2-class`, `Reentrancy.lean` |
| a *concrete* supply-chain ZS instance | **not yet computed** | → next step (mirror `orchestration-zs`) |

## 6. Concrete next step (mirrors what worked for orchestration)

Pick the minimal honest instances and *compute*, exactly as `orchestration_zs*.py` did for agents:
1. **Supply chain:** `procure → manufacture → ship` as an explicit small category `C`; write out its directed
   container `(S, P, o, ⊕)`. Two chains sharing a warehouse → the ZS product `C ⋈ D`; enumerate the
   distributive law, check `(L)∧(G)`, and exhibit an inventory-inconsistency as a nonzero `[ω]`.
2. **Olog:** a two-type olog (`book —has→ author —has→ name`) as a directed container; merging with a second
   olog sharing `author` as the ZS composition.
This turns SEED Q4 from analogy into a *computed* worked example — the same move that promoted
orchestration=ZS from speculative to computed to proved. **I've teed this up as the PROVE target, framed as
staging for Neil's steer, presented at `computed` grade with the modelling-fidelity caveat explicit.**

---

### Provenance / what is whose
- **Prior art (import, cite):** ologs (Spivak); DCont ≃ Cat (Ahman–Uustalu); knowledge-graph-as-copresheaf
  is folklore categorical-database (Spivak, Patterson et al.).
- **Ours (proved):** pairwise-ZS criterion, the `(G) ⟺ [ω]∈H²` obstruction, orchestration=ZS.
- **New here (the delta):** running that obstruction theory *through* supply chains / ontologies / knowledge
  graphs — the corpus has only analogy today. This is the Path-5 Impact spine, staged for Neil.
