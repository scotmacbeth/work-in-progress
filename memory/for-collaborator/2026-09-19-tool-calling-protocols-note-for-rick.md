# Covering note — "Tool-calling protocols are directed containers" (for Rick; CC Robin)

**Status:** DRAFTED + pushed to wip; **email dispatch PENDING** (this was a write-session; email is
disallowed here, so the actual send-to-Rick is a wake-session action — see bottom).

**Paper:** `papers/tool-calling-protocols-directed-containers.tex` (8 pp, amsart).
**Repo:** `scotmacbeth/work-in-progress`, content-commit `6a66fe3`, stamped+PDF commit `05ad03c`.
**URL:** https://github.com/scotmacbeth/work-in-progress/blob/main/papers/tool-calling-protocols-directed-containers.pdf
**Grade gate:** work-in-progress. Do **not** promote to publishable-result without your review.

## What it is (one paragraph)
A short positioned note turning the Doc #4 "Harness is a Worker" core into an external-facing
research note. The thesis, in five identifications: an agent tool-calling protocol (MCP-style) is a
**container** (shapes = request schemas, positions = admissible responses); its **harness is the same
container realized as a comonad**, so the protocol is a directed container → small category →
polynomial comonad (Ahman–Uustalu equivalence chain does all the lifting); the **cofree comonad** on
the tool functor is the **interaction trace**; stateful context is a **store-comonad worker** (single
agent: buys nothing, = curried threading); and **multi-agent compositional correctness** — whether
two interacting stateful protocols admit a consistent interleaving — is a **comonad distributive law
/ Zappa–Szép weld**, existing iff (L) holds and `[ω]=0 ∈ H²`. Smallest re-entrant model: `[ω]=ε∈ℤ/2`,
Lean-checked.

## Why I'd like your eyes on it specifically (you're the H²/obstruction referee)
1. **Theorem 1 is IMPORTED, labelled as such.** It bundles the pairwise-ZS criterion + the
   (G)-obstruction=H² result + reentrancy `[ω]=ε`. I state it at the directed-container level and
   flag (Remark 3) that a **store-comonad-level restatement + the categorical→cochain reduction are
   NOT formalised** (open problem 1). Is the import stated at the right strength, or am I eliding the
   (L)/(G) split anywhere? I tightened the abstract to say "once (L) holds, weld ⟺ [ω]=0" — please
   check §5 and the abstract agree with how you'd state it.
2. **The `H²` coefficient module is left abstract** in the general Theorem (only ℤ/2 pinned at the
   smallest model). Deliberate — I don't want to overclaim the module in the general categorical
   case beyond the registry. Flag if you think even that is too strong.
3. **Lean boundary (Remark 3):** I claim Reentrancy.lean certifies `φ(ω ε)=ε` and
   `InB2(ω ε)⟺ε=false`, and WorkersRetract.lean the `r∘σ=id` retract; the reduction of the
   categorical obstruction to that F₂ complex is pen-and-paper, NOT formalised. Accurate to what you
   remember of the files?

## Novelty boundary (the load-bearing part — please sanity-check the concession)
- **CONCEDE + cite** Keizer–Basold–Pérez "Session Coalgebras" (arXiv:2011.05712, TOPLAS 2021,
  deep-read): "one protocol STEP = a container `∐ X^{B_a}`" is theirs (they cite Gambino–Kock). But
  they have NO comonad, cofree trace, `◁`/`⊗` protocol algebra, store state, or obstruction; their
  composition is π-calculus `P|Q`. Everything downstream is staked as ours. Is the concession
  correctly drawn, or too generous / not generous enough?
- **Segura** (Computing 108, 2026) — effect-handler precedent, protocol-agnostic; **abstract-level
  provenance only**, and the bibitem SAYS SO ("known to the author at abstract level only"). Citation
  footprint floor is therefore not deep-read (see below).
- **Zhang–Wang** 2512.22431 cited only as **withdrawn negative evidence**, with the withdrawal
  caveat, per the sources.json correction note.

## Citation footprint (ran `citation_check.py --report footprint`)
All *load-bearing* refs are deep-read/verified-quote (Gambino–Kock, Ahman–Uustalu ×2, Niu–Spivak,
Spivak, Keizer–Basold–Pérez, Katsumata–Rivas–Uustalu). **Reported floor = agent-summary**, driven
*solely* by the deliberately-caveated withdrawn-paper negative citation (2512.22431). Segura
(abstract) is cited by DOI with an explicit in-bibitem provenance caveat, not as load-bearing. I
judged both acceptable because both are flagged in-text; tell me if you'd rather I drop the
withdrawn-paper mention to clear the floor to deep-read.

## Honest scope
No new theorem. Contribution = the identification + positioning. Single result specific to the
running model (the `[ω]=ε` bit) is the only Lean-verified invocation. Open problems: (1) store-level
restatement + formalise the reduction; (2) beyond ℤ/2 / many-agent (L); (3) protocol morphisms
(reformulate Schlapbach process-calculus bisimulation as dcont morphisms).

## Pending action (wake session)
Email this PDF + note to Rick (grandparick20@gmail.com), CC Robin (langer.robin@gmail.com). Do NOT
promote to publishable until Rick replies. If Neil's steer on framing/scope has arrived by then, fold
it in before sending.
