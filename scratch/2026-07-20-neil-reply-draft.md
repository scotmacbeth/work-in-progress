# Draft — daily email to Neil (folds in reply to UID 70), 2026-07-20

## Structure
1. Status line (⊗ row now full iso both sides Lean-verified; scoop checks clean)
2. Literature sweep [FOLD sweep agent]
3. Orchestration via containers — the substantive response
4. Theorem proving as the same model
5. Harnesses & comonads
6. Wrap-up checklist for chapters 1–3 [FOLD audit agent]
7. Draft email to Nelson Niu (separate block he can forward)
8. Anything else

---

## §3 ORCHESTRATION — the response (grounded in proved / Lean-verified results)

Your model — agent = container (S = prompts, P(s) = potential replies), a morphism to y = an
oracle/LLM call resolving each prompt to a reply, morphisms between agents = delegation — is exactly
the right primitive, and the four monoidal structures we just classified ARE the language of
orchestration. Concretely, each structure is a distinct orchestration combinator:

- **◁ (sequential):** the agent whose reply feeds the next agent's prompt. This is *the* composition
  of orchestration. Its free monad (which I Lean-verified in Free.lean as a ◁-monoid, grafting laws
  and all) is precisely the tree of nested delegated calls — a workflow is an element of the free
  monad on the agent-container, and grafting = substituting a sub-workflow's replies into the parent.
- **× (product):** run two agents, keep both interfaces (a joint prompt is a pair, a reply is a
  reply to each). The categorical product — the *only* pointwise structure (Thm B⁺).
- **⊗ (Dirichlet):** run two agents in parallel over a shared prompt schedule; positions multiply.
- **+ (coproduct):** offer a choice of agent.
- **Closed structure = higher-order orchestration.** This is the unexplored part you flag, and we
  already have it machine-checked. The internal hom [q, r] is the agent whose prompts are
  *q-agents* and whose replies are *r-agents* — i.e. an orchestrator that consumes an agent and
  emits an agent. [q,r]'s shapes are literally the delegations Cont(q,r). Currying
  Cont(p ⊗ q, r) ≅ Cont(p, [q,r]) says: a joint orchestration of p-and-q is the same as a
  p-agent that returns a q→r orchestrator. That is meta-orchestration / delegation-as-data, and
  DirichletClosed.lean proves (Cont, ⊗, y) is a closed monoidal category with zero axioms. We also
  have the uniform closure formula [p,q]_⋆ = ∏_{i∈p(1)} q ◁ (p[i] ⋆ y), proved, so the closed
  structure is understood for every convolutional combinator, not just ⊗.

**The genuinely new grant-Impact claim — composing two orchestrations = a Zappa–Szép product.**
When two orchestrations share resources (two supervisors dispatching to the same worker pool),
the joint agent is NOT a plain product — it is a Zappa–Szép product C ⋈ D, i.e. a distributive law
between the two directed containers. Whether the joint orchestration EXISTS and is coherent is
governed by the pairwise-ZS criterion (L)∧(G) I proved. A re-entrancy / re-dispatch cycle
(w_i → sup → w_j → sup → w_i that can't close coherently — the orchestration analogue of the
Ethereum re-entrancy bug in the seed) is exactly a (G)-failure, a nonzero obstruction class
[ω] ∈ H²(Sk_C; 𝒟). I have a computed 4-regime table for the smallest shared-worker case:
independent supervisors compose (K = C×D); coherent interleave composes (K = S₃, non-abelian);
state-protected re-entry composes; **unprotected re-entry is obstructed** — and the single bit that
flips composable ↔ obstructed is *does a worker mutate shared supervisor state?*

The differentiator for the grant: the multi-agent-systems literature puts *generic* sheaf/cochain
machinery (H⁰/H¹ Laplacians) on the *communication* graph to study consensus. We put H² on the
*handoff* category to study *composability* — and it comes from the polynomial-functor structure of
the agents themselves, not a generic Laplacian. Nobody models orchestration through Poly/containers
specifically; zero scoop risk. This is a paper-shaped Impact contribution, and the container view
predicts a concrete failure mode (unprotected shared state) rather than merely measuring one.

## §4 THEOREM PROVING AS THE SAME MODEL
Your theorem/lemma container is the same object as the tactic tree, and we've already formalised its
algebra. Shapes = theorems, P(theorem) = the lemmas needed. A proof is an element of the FREE MONAD
on this container — a tree whose nodes are theorems and whose children are the lemmas, bottoming out
at axioms (morphisms to y). Tactic composition = grafting = the ◁-monoid multiplication I proved and
Lean-verified (Free.lean, all three grafting-monoid laws, zero sorry). So "the structure of
containers is the structure of tactics" is literally the free-monad-on-a-container structure, and it
is machine-checked. A tactic that reduces a goal to subgoals is a container morphism; a complete
proof is a morphism all the way down to y. This is a clean worked instance of the orchestration model
where "agent" = "prover" and "oracle call" = "close a leaf goal."

## §5 HARNESSES & COMONADS
Agreed, and it fits: a harness = the *context* an agent runs in = a comonad. A directed container is
exactly a comonad (D1–D5, both directions Lean-verified), and reading it as a harness: ε = read the
current context, δ = how the context extends along each reply. The cofree comonad on an agent-container
is the "maximal harness" — every possible run-context, i.e. the full interaction tree the harness can
present. That is the (co)monads chapter (Ch 4), and it dovetails with the orchestration story: the
Zappa–Szép obstruction lives on the *category* (= directed container = comonad) side, so harness
composability and orchestration composability are the same H². I'll develop this there.

---

## §6 WRAP-UP CHECKLIST — chapters 1–3

**Ch 1 (intro + preliminary CT):**
- Integrate the "Machinery" preliminaries write-up (representables/Yoneda/Day/Kan,
  preliminaries-representables-yoneda-day-kan.tex — verified, proves your two observations:
  ⟦−⟧ = Lan_Y y^(−), and closure determined on representables by density) as the preliminary chapter.

**Ch 2 (category of containers):**
- which-functors-are-containers.tex is drafted and referee-passed (Cont ≅ Fam(Set^op),
  container ⟺ preserves connected limits, position recovery, the honest F(2)→F(1) = 2^{P(s)}
  correction). One open citation: pin the Abbott-thesis coequaliser reference. Otherwise complete.

**Ch 3 (monoidal structures):**
- Confirm the classification chapter (Thms A / B⁺ / C, + closed structures) is slotted as Ch 3, with
  the DJN arXiv:2305.05655 neighbour cite and the Niu–Spivak Prop 3.79 attribution (their forward
  direction) both in place.
- GOOD NEWS: the ⊗ (co)monoid row is now closed as full machine-checked isomorphisms BOTH sides
  (comonoid + monoid converses landed, all four Lean files sorry-free, Quot.sound-only). So every
  Lean-verified claim the monoidal/(co)monoid material makes is now two-sided.
- Dialectica ⋉/⋊ pulled out into the held Cont(C) file per your steer (done).

**Cross-cutting:**
- Literature sweep result: [FOLD sweep agent].
- One editorial call for you: the (co)monoid classification table (◁/⊗/×/+ each giving categories /
  families-of-monoids / oplax-functors) is currently drafted as §4.x — does it belong at the end of
  the monoidal chapter (Ch 3) or does it open the (co)monads chapter (Ch 4)? It's comonoid-*object*
  material, so I lean Ch 4, but it's a natural climax to Ch 3.
- Still unformalised (Ch 4 item, not blocking ch1–3): the ×-monoid classification (Thm B) has a paper
  proof but no Lean forward map yet — the sibling of DirichletMonoid.lean.

## §7 DRAFT EMAIL TO NELSON NIU (for Neil to send)

Subject: Polynomial functors for agent orchestration — and a note on your ⋉/⋊

Dear Nelson,

I hope you're well. At Kodamai we've been building agent orchestration directly on containers /
polynomial functors — an agent is a container (prompts as shapes, potential replies as positions), an
oracle/LLM call is a morphism to y, and the monoidal structures on Poly are the orchestration
combinators (◁ for sequential delegation, ⊗/× for parallel composition, and the closed structure for
higher-order "orchestrators of orchestrators"). We're writing this up as a book, and a few of your and
David's results sit right at the centre of it, so I wanted to open a line.

Two things you might find interesting:

1. We've classified the monoidal structures on the category of containers Cont ≅ Fam(Set^op): Day
   convolution gives an equivalence between monoidal structures on Set and the "convolutional"
   structures on Cont, with the categorical product characterised as the unique *pointwise* one, and
   the Dirichlet–to–sequential comparitor ⊗ → ◁ exhibited as the counit of a coreflection (⊗ is the
   Day-ification of ◁). Prop 3.79 in your Poly book gives the forward direction; we have the converse
   and the classification.

2. In Dorta–Jarvis–Niu (arXiv:2305.05655 §6) you list two further monoidal structures ⋉ and ⋊ that
   you note you can't yet interpret. We think ⋉ is de Paiva's Dialectica tensor extended off the
   homogeneous fragment Hmg(2) ≃ Dial(Set) to all of Poly, and ⋊ is its directed (triangular)
   variant — non-convolutional, so genuinely outside the Day family, and ⋊ turns out to be
   one-sided (directed) closed. We'd love your read on whether that matches what you had in mind.

If any of this is useful we'd be glad to share drafts, and we'd welcome your thoughts on the
closed-structure-as-orchestration angle, which seems under-explored.

Warm regards,
Neil (on behalf of the Kodamai team)

---
NOTE: keep the Niu email calibrated — Niu is a DJN co-author and Poly-book co-author, so the ⋉/⋊ line
is a genuine hook (we answered their own open problem). Do NOT overclaim novelty of the Day forward
direction (theirs). Flag to Neil that ⋉/⋊=Dialectica is registry `computed` and not yet browse-cleared
for novelty against de Paiva/Trotta/Hedges — so it's offered as "we think", not "we proved first".
