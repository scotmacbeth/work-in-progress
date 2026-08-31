# Σ-container lifting is a genuine monad for Reader/State — PROVED (all params)

**MacBeth → Neil / Robin. 2026-08-07 PROVE deep-work.**
Full writeup: `proofs/2026-08-07-sigma-monad-proved.md`. Registry node
`sigma-monad-reader-state-proved` = **proved** (validated). Companion to the 08-07 □/∏ boundary.

## What is proved
The proof-relevant **Σ-container lifting** `T^Σ_M(S,P) = (MS, P^Σ)`, `P^Σ(m)=∐_{b∈lv(m)}P(x_b)`,
with unit = **codiagonal fold** and multiplication = **reindex along the section `σ`**, is a genuine
monad on `Cont` for **Reader (every E)** and **State (every state set St)**. So Reader/State **do**
carry a proof-relevant monad lifting — the Σ one — even though they fail the ∏ (Ahman–Bauer) one.
Both halves of the ℤ/2 grading are now proved: □ (08-07 morning) and Σ (this).

## The engine (this is the reusable idea — the dual of the ∏-census's Yoneda reduction)
Every backward position map here is a **coproduct-pushforward** `Σ_α` along a label-preserving index
function `α` (relabel the summand, carry the position). `Σ` is a **faithful** functor of such
functions — test at the constant singleton family `P≡1`, where `Σ_α = α`. Therefore **each monad law
collapses to a single index-function identity**, and the forward parts are just `M`'s own unit/assoc.
All content = three backward identities:
- **(U1)** `inner(σ(η_{MS}m, L)) = L`  — left unit
- **(U2)** `outer(σ(M(η)m, L)) = L`   — right unit
- **(A)**  section pentagon: `σ` threads associatively — associativity

**Reader** (σ = constant diagonal `e↦(e,e)`): both components are `L` ⟹ U1,U2 free; diagonal∘diagonal
= triple-diagonal ⟹ A.  **State** (σ = threaded `s↦(s,h(s))`): outer is always `s` ⟹ U2 free; the
unit's next-state is the identity ⟹ U1; threading is associative = **State's own μ-associativity** ⟹ A.

This mirrors the ∏-census exactly: ∏ reduces a *function into a product* (needs forward-total,
Reader/State fail); Σ reduces a *function out of a coproduct* (needs reverse-total, Reader/State
satisfy) — and in **both** the monad laws collapse to `M`'s unit/assoc via the (co)diagonal/threading
section. Good candidate for a unified book-Ch7 lemma.

## Honest scope — what I did NOT prove (important, please read)
The **general** claim "reverse-total M ⟹ Σ-monad" is **NOT** established, and I now see why:
reverse-total gives the section `σ` only **pointwise** (enough to *define* the multiplication), but
monadhood needs the sections to **cohere** — (U1),(U2),(A) — which is strictly stronger. Reader/State
supply coherence canonically (diagonal/threading); a bare pointwise reverse-total choice need not.

So the honest general statement is **Theorem 3.1**: `T^Σ_M` is a monad **iff** `M` admits a
shape-natural label-preserving section satisfying (U1),(U2),(A). Open child node
`reverse-total-implies-coherent-section-OPEN` (speculative): I expect coherence needs a
directed/threading structure on `M`, of which Reader (diagonal) and State (threading) are the two
motivating instances. **Neil — is this the right level of generality to chase, or is Reader/State
enough for the grant's proof-relevant-lifting narrative?**

## Verification
Exhaustive where feasible: **State St=2, all 16 384 depth-3 nestings PASS**; Reader E=2 over the
2-shape base (256) PASS; Reader E=4 / State St=3 sampled PASS; negative control (constant
non-matching section) fails. Symbolic §§4–5 make the checks conclusive for general E, St.

## Suggested next
1. **Lean rung** — the reduction Lemma is very Lean-friendly (`Σ`-reindex then `rfl`); do
   `reader_sigma_*` / `state_sigma_*` to complete the triptych ∏✗ / □✓ / Σ✓ at one base monad,
   extending `ReaderStateOutsidePiMendler.lean`.
2. **Structural characterization** — pin "coherent section ⟺ [condition on M]" to close the general
   theorem (the open child).
3. **Book Ch7** — fold in §2's reduction lemma as the Σ-dual of the Yoneda ∏-reduction.
