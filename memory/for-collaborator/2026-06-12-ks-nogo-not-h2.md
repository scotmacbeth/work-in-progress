# For Robin/Neil — The Karamlou–Shah no-go is NOT our H² obstruction (and why that's good)

**TL;DR.** I tested the conjecture that the Karamlou–Shah LICS-2024 no-go theorems
(list/stream/tree directed containers don't distribute over Δ or P) are instances of
our (G)-obstruction [ω] ∈ H²(Sk_C;𝒟). **They are not.** The conjecture was a level/
category error. But pinning down *why* sharpens the grant claim rather than denting
it. Write-up: `projects/proofs/2026-06-12-ks-nogo-level-analysis.tex` (compiles).

## The two-line refutation
Our criterion needs the right factor 𝒟 to be a **small category = directed container
= polynomial comonad**. The K–S monads **P (powerset) and Δ (distribution) are not
polynomial functors** — the two canonical non-polynomial monads. So they can't be a
wide subcategory 𝒟 at all: condition (L) isn't even defined for them, let alone (G).
The no-go lives one level *below* (L) — a non-representability obstruction, not a
cohomological closure class.

Elementary proofs (machine-checked, `ks_level_check.py`):
- P: P(1)=2, P(0)=1 force P(2)=1+2^k; but P(2)=4 ⇒ 2^k=3, impossible.
- Δ: Δ(1)=1 ⇒ Δ would be representable ⇒ preserve products; but marginals
  Δ(2×2)→Δ(2)×Δ(2) aren't injective (independent vs correlated coins).

## The deeper reason (independent)
K–S study a **mixed comonad–monad law** GT⟹TG in [Set,Set] — an *entwining/lifting*
(Beck; Brzeziński–Majid; Power–Watanabe), whose (co)algebras are bialgebras. Our H²
classifies distributive laws of **two categories** in Span(Set) ↔ strict
factorizations (Rosebrugh–Wood). Different bicategory, different kind of law. Even a
*good* comonad–monad law would not be a factorization. So there are TWO independent
reasons, each sufficient.

## What survives — the grant-safe statement
Among **directed-container-over-directed-container** no-go theorems the obstruction
really *is* [ω] ∈ H²(Sk_C;𝒟). The rigid twist is an explicit no-go: 𝒟 = ℤ/2 at a (a
directed container), (L) holds, (G) fails, [ω] = generator of ℤ/2 — no Zappa–Szép
complement. That's the honest in-Poly analogue of a K–S theorem *with* a computable
obstruction.

**Revised slogan for the grant:** "For directed-container distributive laws — the
polynomial/Cat# world — compositional correctness has a computable obstruction
[ω] ∈ H²(Sk_C;𝒟). The probability/nondeterminism no-go theorems are a *different*,
deeper phenomenon (the monad isn't even a directed container)." Claiming they were
the same H² class would have been an overclaim; the boundary is the contribution.

## Open / next
- Honest gap: I did not reprove K–S (no preprint; worked from the statement). I
  classified the *type* of their obstruction, not their mechanism.
- Real next question (for Neil): is there a **non-polynomial** analogue of our
  cohomology that *does* see the Δ/P no-go — e.g. an obstruction theory for mixed
  laws / entwinings, perhaps Zwart–Marsden's algebraic-identity obstructions cast
  cohomologically? That would be the true bridge, and it's a genuinely open program.
