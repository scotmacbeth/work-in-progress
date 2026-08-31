# Orchestration composition = Zappa–Szép product (the weld)

*Connection banked 2026-07-20. Scratch note: `scratch/2026-07-20-orchestration-obstruction-note.md`.*

**The connection.** My corpus had two disjoint universes that never touched:
- **Orchestration-as-container** (seed notes `ORCHESTRATION_ANALOG`, `COMPOSABLE_ORCHESTRATION_PATTERNS`,
  `AGENT_INTERFACE`): agent = container `(S,P)`; handoff topology = directed container; orchestration =
  **functor** over Cont. Zero cohomology / distributive-law content.
- **ZS ⇒ H² obstruction** ([[cohomological-obstruction-family]], [[g-obstruction-is-baues-wirsching]]):
  `K = C ⋈ D` exists ⟺ (L)∧(G); `(G) ⟺ [ω]=0 ∈ H²(Sk_C;𝒟)`. Zero mention of agents.

The weld: **the orchestrator's handoff graph IS the skeleton `Sk_C`; composing two agents/orchestrations
into one interleaved system IS a Zappa–Szép product `C ⋈ D` (a distributive law), not merely a functor;
and the obstruction to that composition IS the known H²(Sk;𝒟) class.**

**Where the novelty actually is (survey-confirmed):** NOT the cohomology (established: Rosebrugh–Wood /
Baues–Wirsching / Pirashvili; Neil *demoted* the H² thread — cite, don't reprove). The genuinely
unstaked claim is **link (2): agent composition = distributive law / ZS product `C ⋈ D`.** Every prior
note modelled composition as a *functor* (composes *along* one topology); a ZS product *interleaves two*
topologies — which is what concurrency / supervisor-over-workers / re-entrant tool-calls actually need.
The SEED already reads Ethereum re-entrancy as a *failed* distributive law, so the "re-entrancy = nonzero
[ω]" reading has backing.

**Differentiator vs MAS literature (degree-axis, exact):** sheaf-Laplacian crowd puts `H⁰` (consensus /
Nash, 2606.01663) and `H¹` (identifiability, Anwer–Riess–Hale 2605.11204; swarm 2605.01879) on the
*communication* graph — *state* questions. Directed-container view puts `H²` on the *handoff* category —
*structural composability* (existence of the joint agent). Complementary, not competing.

**Status.** T1 (DCont≅Cat, Lean), T2 (pairwise-ZS), T3 (H² obstruction) all **proved**; the
orchestration instantiation is **computed** (4-regime table, `orchestration-zs.json`,
`proofs/2026-07-19-orchestration-zs-instantiation.tex`). Verify-first hinge: Fairbanks "Comonads as
Spaces" 2607.15091 (comonads generalise both DCont AND sheaves) — only held at agent-summary depth.

**★ 2026-07-20: NEIL ENDORSED THE DIRECTION (UID 70).** He described Kodamai's own model — agent =
container (prompts=shapes, replies=positions), morphism to `y` = oracle/LLM call, container morphisms
= delegation, monoidal structure = orchestration language, **closed structure = higher-order
orchestration (his explicit "unexplored" flag)**, and theorem-proving-as-container (theorems=shapes,
lemmas=positions, tactics=◁-monoid/free-monad — which I've Lean-verified in Free.lean), harness=comonad
(→ (co)monads chapter). Replied 2026-07-20 with the full dictionary + the ZS/H² composability claim.
**WRITE trigger now set:** `papers/containers-for-orchestration.tex` (grant-Impact note). Closest prior
art surfaced by sweep = **Aberlé arXiv:2604.01303** (poly interfaces + free-monad implementations, Agda)
— read before writing. Grade the dictionary rows honestly: interface=container is Neil's/Spivak's; the
ZS-product composability reading is the delta (still `computed`).

**★ 2026-07-20 (browse): the differentiator now has a NAMED rival — and it lands on a different axis.**
**ArchAgents — "Harness Engineering as Categorical Architecture", Bogdan Banu, arXiv:2605.12239 (2026).**
Surfaced *independently by two blind browse agents* (arXiv + community) — the cross-corroboration signal
worth acting on (cf. the Stone-Duality two-trail hub). It is the **closest live categorical treatment of
multi-agent orchestration found to date**: a category of "Architecture triples" `(G, Know, Φ)` — `G` =
wiring graph of modules/ports, `Know` = structural invariants/certificates, `Φ` = deployment map from
abstract capability slots to concrete implementations — with **memory as coalgebraic state, skills
composed via operads**, protocols = wiring graph, and "compiler functors" into concrete runtimes
(LangGraph, Swarms, Ralph) preserving certificates. **NO scoop:** its composition axis is
**operads + coalgebraic state**, NOT distributive laws / polynomial functors / Zappa–Szép products.
That is genuinely orthogonal — **parallel skill-assembly within one harness** vs. my **sequential /
interleaved two-party interaction via `C ⋈ D` with re-entrancy as the H² obstruction**. So it both
(1) reconfirms the Path-5 gap is open, and (2) hands the grant Impact section a clean, citable
*differentiator sentence*: "the other live CT-for-agents proposal models parallel skill composition;
mine models sequential two-party interaction and its composability obstruction." CITE as related-work
in `containers-for-orchestration.tex`; light-watch for follow-ups that reach for distributive laws.
Source: `reading/2026-07-20-browse.md` (agent-summary depth — abstract-level read, deep-read before any
load-bearing comparison claim).

**★★ 2026-08-25 (browse): the BASE ZS/distributive-law link may be AHMAN'S OWN — direct-read pi13 before
any novelty claim on the core story.** Web agent surfaced **Danel Ahman, "Distributive laws of directed
containers"** (`danel.ahman.ee/papers/pi13.pdf`; personal-site PDF, NO arXiv ID yet; `agent-summary` only —
full-text extraction FAILED, binary parse error). Search-engine summary indicates it studies distributive
laws `D∘C → C∘D` of comonads in Poly and shows the resulting comonoid **recovers the Zappa–Szép product of
monoids** when `C,D` are monoids — *exactly* the `λ:N×P→P×N` combinator this weld's **link (2)** ("agent
composition = distributive law / ZS product `C⋈D`") is built on, tied to strict factorization systems.
Ahman is a **core Path-2 author I already cite for D1–D5**, so this is almost certainly the *source* of
ZS-in-Poly, NOT an independent co-discovery I can claim. **Honesty consequence:** link (2) — which the note
above calls "the genuinely unstaked claim" — is likely re-attributable to Ahman. The **surviving novel
layer** is the *obstruction* `[ω]∈H²(Sk_C;𝒟)` to that composition (re-entrancy = nonzero class), which the
summary gives no sign Ahman builds. This *sharpens* the stake (novelty = obstruction theory, not the base
combinator) but only AFTER a direct read confirms what pi13 contains. **BLOCKS the next `/write` on
ZS/orchestration** per the standing "READ POLY BEFORE CLAIMING" rule. → open question
[[../questions/ahman-pi13-zs-attribution]]. Source: `reading/2026-08-25.md`.

**★ 2026-07-21: ABERLÉ arXiv:2604.01303 READ IN FULL — the mechanism is prior art; the ZS/H² layer is
the surviving novelty.** ("Compositional Program Verification with Polynomial Functors in DTT", Agda.)
Full note: `reading/2026-07-21-aberle-2604.01303.md`. Verdict, precisely:
- **SCOOPED (cite, do NOT claim as new):** poly functors `(A,B)` as program/agent INTERFACES;
  implementations = free-monad-on-Poly Kleisli arrows `p ⇒ Free q`, composed along Spivak wiring
  diagrams (Thm 3.1); dependent-poly `(C,D)` as pre/post SPECIFICATIONS / Hoare triples with a
  "dependent free monad" for assume-guarantee (Thm 5.3); the whole thing abstracted as a strictly
  monoidal forgetful functor `π:Spec→Int` + a lax-monoidal presheaf of systems + a monoidal nat.
  transf. (Def 7.1); parallel-sum monoidal structure for concurrency (App A). ⟹ "theorem-proving-as-
  container" and "orchestration-as-workflow with poly interfaces" are a DOMAIN REINTERPRETATION of
  Aberlé's mechanism, not a new mechanism. He even flags tactics/automation as future work.
- **NOT scooped (the delta survives):** Aberlé has NO Zappa–Szép product, NO distributive law of two
  monoids, NO interaction obstruction, NO cohomology. His ONLY two-system construct is the
  UNOBSTRUCTED parallel sum. ⟹ the claim "composing two shared-resource orchestrations = `C ⋈ D`,
  obstructed by `[ω]∈H²(Sk_C;𝒟)`; unprotected re-entrancy = nonzero gen Z/2" is the surviving
  defensible novelty. Reframe `containers-for-orchestration.tex` as THAT obstruction layer sitting on
  top of Aberlé's (cited) framework — do not reinvent the framework. (Drives WRITE.md + PROVE.md,
  set 2026-07-21: prove the obstruction theorem → promote `orchestration-zs` computed→proved.)
