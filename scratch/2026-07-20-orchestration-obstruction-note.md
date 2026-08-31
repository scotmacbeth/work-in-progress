# Agent orchestration as a directed container — the composition obstruction is cohomological

*Scratch draft, 2026-07-20. Grant-Impact scoping note (SEED Path 5 × the cohomological-obstruction
thread). This is a CONNECTION, graded honestly: the load-bearing theorems are proved and in my
registry; the orchestration DICTIONARY is a proposed application reading (speculative), to be
grounded, not asserted as a theorem about real agent frameworks.*

## 0. The one-sentence claim

An AI-agent orchestration is a **directed container** (the handoff topology) together with a functor
to agent interfaces; two orchestrations compose into one consistent interleaved system exactly when a
**distributive law / Zappa–Szép product** of the two directed containers exists; and the obstruction
to that composition is a **degree-2 cohomology class** `[ω] ∈ H²(Sk_C; 𝒟)` — a container-native,
polynomial-functor obstruction, categorically one level above the sheaf-Laplacian *state*-consensus
obstructions that the current multi-agent-systems literature uses.

## 1. The dictionary (proposed reading — grade: speculative, to be grounded)

| Orchestration concept | Container/Poly structure | Status of the identification |
|---|---|---|
| An agent's interface | polynomial functor `p = Σ_{s∈S} y^{P(s)}`: `S` = queries/states it can issue, `P(s)` = admissible responses | Spivak's interaction reading (prior art) |
| An agent's dynamics/policy | a `p`-coalgebra / Moore–Mealy lens realising the interface | prior art (Poly dynamical systems) |
| A handoff *topology* (who may hand off to whom; stay-put; concatenate handoffs) | a **small category = directed container** `(S◁P, o, ↓, ⊕)`: objects=agents/roles, `P(s)`=admissible handoff-paths out of `s`, `o`=stay, `⊕`=concatenate | **Ahman–Uustalu (proved, prior art)**; the identification "graph→free category→DCont" is the crown structure |
| The comonad on the topology | "a local plan at agent `s` extends coherently to all reachable downstream agents" | AU comonad = D1–D5 (Lean-verified, mine) |
| Composing two orchestrations / running two agents concurrently | a **distributive law** `δ : D◁C → C◁D` ⇒ the joint directed container `C ⋈ D` (Zappa–Szép product) | **my pairwise-ZS criterion (proved)** |
| Re-entrancy / deadlock / inconsistent shared state | a **failed** distributive law | already in the SEED (Ethereum re-entrancy = failed distributive law) |

## 2. The load-bearing theorems (proved — registry-backed, NOT speculative)

- **(T1)** Directed container ≅ small category (Ahman–Uustalu; my Lean M2/M3 both directions).
- **(T2) Pairwise Zappa–Szép criterion.** `K = C ⋈ D` over a wide `D` exists ⟺ **(L)** the hom-presheaf
  is free ∧ **(G)** a closing basis exists. `[pairwise-zs, proved]`.
- **(T3) The (G)-obstruction is an H² class.** `(G) ⟺ [ω] = 0 ∈ H²(Sk_C; 𝒟)` — coefficients in the
  direction (response) functor `𝒟`, cohomology of the skeleton `Sk_C`. Baues–Wirsching /
  Rosebrugh–Wood lineage. `[g-obstruction-is-h2-class, proved]`.

So the *composition-exists* question for two orchestrations reduces to a **degree-2 cohomology class of
the handoff skeleton with coefficients in the agents' response functor**. Nonzero `[ω]` = the two
agent-orchestrations cannot be interleaved into a single consistent joint agent (structurally — before
any question of what they compute).

## 3. The differentiator (grant Impact — the degree-axis contrast, citations from [[cohomological-obstruction-family]])

This is the note's strongest asset and it is already half-built in my memory. The multi-agent-systems
literature puts a **cellular sheaf** on the *communication* graph and measures obstructions at low degree:
- **`H^0`** — global sections = **consensus / Nash equilibria** (Hernández–Sánchez-Soto; 2606.01663).
- **`H^1`** — via a (nonlinear) **sheaf Laplacian** = **identifiability** of a multi-agent system
  (Anwer–Riess–Hale, 2605.11204); swarm-consensus sheaf-Laplacians (2605.01879).

These answer "**do the agents currently agree / can we identify them?**" — *state*-level questions,
generic linear-algebraic machinery on the communication graph.

The directed-container view puts **`H²`** on the **handoff category** `Sk_C`, coefficients in the
**direction (response) functor `𝒟`**, and answers a *structural* question one degree up: "**can these
agents be fused into a single consistent joint agent AT ALL?**" (existence of the composite, §2). The
axis contrast is exact and complementary — low-degree sheaf cohomology on the communication graph for
*agreement/identifiability*; degree-2 category cohomology on the handoff graph for *composability*. The
unstaked gap: everyone applies generic sheaf/cochain machinery to multi-agent graphs; **nobody routes it
through polynomial-functor / directed-container structure.** (Per [[cohomological-obstruction-family]]:
"None yet cite the categorical/Zappa–Szép literature; none yet state my exact theorem.")

**Framing constraint (from [[g-obstruction-is-baues-wirsching]]):** the H² tower is *established*
cohomology (Rosebrugh–Wood / Baues–Wirsching / Pirashvili), and Neil **demoted** the cohomology thread
as a possible rabbit-hole. So the note's novelty must NOT claim new cohomology — it lives entirely in
(a) the **identification** orchestration-handoff ⇒ ZS product ⇒ known H², and (b) this degree-axis
**contrast** with the MAS sheaf methods. Cite the cohomology, do not reprove it.

## 4. Honesty ledger

- **Proved & mine to cite:** T1 (Lean), T2, T3. The dictionary rows for "interface = container" and
  "dynamics = coalgebra" are Spivak's prior art.
- **Speculative (this note's proposal):** that real orchestration frameworks *instantiate* this
  structure — that a supervisor/worker pattern, a hand-off graph, a tool-calling loop literally presents
  as a directed container and its concurrency as a ZS product. This is an application *reading*; it needs
  a worked instantiation (one concrete framework mapped onto `(S◁P,o,↓,⊕)` + one concurrency pattern
  exhibited as a `δ`), mirroring how Robin's GA work *empirically* validated "composition determines
  dynamics." Until then: grade speculative.
- **Positioning claim to verify:** §3's contrast requires the three sheaf-Laplacian papers actually read
  (abstracts only so far). Do NOT publish the "nobody uses poly-functor obstructions" line until that
  read confirms it. Zero H² scoop risk was already checked (those papers use generic Laplacians).

## 5. What a first deliverable looks like — and the concrete COMPUTE target that grounds it

A 4–6pp note / grant-Impact subsection: §1 dictionary, §2 the three theorems stated (proofs cited),
§3 the worked instantiation, §4 the sheaf-Laplacian contrast, §5 the re-entrancy = nonzero-[ω] example
(borrow the Ethereum failed-distributive-law case, retold for agents calling back into a supervisor).
Ends with the empirical-validation ask (the GA analogue for orchestration).

**The instantiation must be COMPUTED, not asserted** (honesty — do not hand-wave the dictionary into a
theorem). Smallest non-trivial case to hand a compute session:
- **Handoff category `C` = free category on the supervisor–worker graph** `sup ⇄ {w₁, w₂}` (sup dispatches
  to each worker; each worker returns to sup). Objects = {sup, w₁, w₂}; `P(sup)` = directed paths out of
  sup (infinite: dispatch/return cycles). One round of map-reduce = the wiring lens
  `sup-interface → w₁-interface ⊗ w₂-interface` (fan-out = ⊗ of worker interfaces; fan-in = the lens
  back). This is a genuine directed container `(S◁P, o, ↓, ⊕)`.
- **Two orchestrations `C`, `D` sharing the workers** (e.g. two supervisors over the same `{w₁,w₂}`, or a
  hierarchical sup-of-sups). **COMPUTE:** enumerate candidate distributive laws `δ : D◁C → C◁D`; check the
  pairwise-ZS criterion **(L)** (free hom-presheaf) ∧ **(G)** (closing basis). Exhibit a case where
  **(G) FAILS** — a worker re-dispatch cycle `wᵢ → sup → wⱼ → sup → wᵢ` that cannot close coherently — and
  read off the nonzero `[ω] ∈ H²(Sk_C;𝒟)`. That single computed example turns the whole dictionary from
  speculative into a demonstrated instance (mirrors how Robin's GA work computed migration-topology cases
  to validate "composition determines dynamics").
- Deliverable of the compute session: a `computed`-grade registry node + a table (which shared-worker
  topologies admit a joint agent, which are obstructed). THAT is the note's spine; everything else is
  framing around it.

## 6. What this note ADDS (survey-confirmed — it is a weld between two disjoint universes)

My corpus splits cleanly: the **orchestration** notes (`ORCHESTRATION_ANALOG`,
`COMPOSABLE_ORCHESTRATION_PATTERNS`, `AGENT_INTERFACE`) model agents-as-containers and orchestration-as-
**functor**, with **zero** cohomology / distributive-law content; the **cohomology** notes
(`cohomological-obstruction-family`, `g-obstruction-is-baues-wirsching`) carry the ZS ⇒ H² machinery and
the MAS-sheaf contrast, with **zero** mention of agents/orchestration. The two never touch. This note is
the missing weld. Precisely what it adds, link by link:

- **(1) handoff-topology = directed container:** prior notes say agents-are-directed-containers, but
  **never weld the handoff graph to the `Sk_C` that carries `[ω]`.** The weld sentence — *"the
  orchestrator's handoff graph IS the skeleton `Sk_C` whose H² obstructs composition"* — is new here.
- **(2) agent composition = distributive law / ZS product `C ⋈ D`:** **genuinely unstaked.** Every prior
  note models composition as a *functor* (or sequential = monoidal); **no note writes "joint agent =
  `C ⋈ D`."** This is the core new claim, and it upgrades the prior "orchestration = functor" reading —
  a functor composes *along* one topology; a ZS product *interleaves two* topologies, which is what
  concurrency / supervisor-over-workers / re-entrant tool-calls actually require.
- **(3) composition obstruction = H²(Sk;𝒟):** proved abstractly (T3) but **never stated as an
  orchestration claim.** New here as the orchestration theorem-shape.
- **(4) contrast with sheaf-Laplacian MAS methods:** the degree-axis contrast + citations exist in
  `cohomological-obstruction-family` but only against my abstract ZS theorem; **framing it in
  orchestration terms** (§3) is the new join.

**Theoretical hinge to verify before leaning on it:** Fairbanks "Set-sets" / "Comonads as Spaces"
(2607.15091) — comonads generalise *both* directed containers *and* sheaves — is the natural reason these
two universes should meet, but I only hold it at agent-summary depth. Read before using it as
justification.

## GAP / status

Links (2), (3), (4)-in-orchestration-terms and the (1) weld are all NEW to my corpus. Grade: the
scaffolding theorems T1–T3 are **proved**; the orchestration dictionary is **speculative** (needs one
worked instantiation, §5). Not for a big Neil email yet (one-email/day used today; he's overloaded).
Fold a one-line mention into tomorrow's plan; candidate WRITE target pending Neil's interest.
