---
name: purdy-damato-2503-cleared-neighbour
description: Purdy–Damato 2503.17191 (CALCO 2025) mixed container DLs = NEIGHBOUR not scoop; theirs on Set, mine on Cont
metadata:
  type: reference
---

Scoop-check CLEARED 2026-08-01 (research agent, full-paper read; PDF at
`projects/papers/purdy-damato-2503.17191.pdf`).

**Purdy–Damato, "Distributive Laws of Monadic Containers," arXiv:2503.17191, CALCO 2025.**
Explicit (u₁,u₂,v₁,v₂)-data characterisation of Beck DLs γ:TS⇒ST between two *monadic
containers* (Uustalu mnd-containers / lax Σ-universes). §6 combines with directed containers
for **mixed** laws: Def 28 monadic-over-directed, Def 29 directed-over-monadic. §7 Thm 35
"too many constants" no-go (no list-over-coproduct).

**Decisive boundary — LEVEL.** Every (co)monad in P&D is a (co)monad **on Set** that happens
to be a container functor. My `T_M`/`G_M` are endofunctors **on Cont** (objects of [Cont,Cont]),
from ONE Set-monad M by transfer. One level up. They never put (co)monads on Cont, never apply
a Set-monad to positions.

- **Item 2 `G_M(S,P)=(S,M∘P)` (M on positions):** ORTHOGONAL — no "apply M to fibres", no
  comonads-on-Cont.
- **Item 3 `λ:T_M G_M⇒G_M T_M` (all M):** ADJACENT — their mixed laws are between *independent*
  container-monad & container-comonad on Set; mine is between shape-monad & position-comonad of
  the *same* M in [Cont,Cont].
- **Item 4 `κ:G_M T_M⇒T_M G_M`, Freyd/arrow, ⟺ non-branching `E+A×(−)`:** ORTHOGONAL — no
  biKleisli/Freyd/arrow, no branching, no `E+A×(−)`.

**Verdict SAFE:** claim `G_M,λ,κ` novel; cite P&D as neighbour. Guardrails: (i) frame `T_M/G_M`
as (co)monads ON Cont vs their container-(co)monads on Set = the novelty boundary; (ii) keep
attributing `T_M` (M-on-shapes) to Ahman–Bauer/Ahman–Uustalu.

**Drop-in related-work sentence** (into `papers/effects-coeffects-containers.tex`):
"Purdy and Damato [arXiv:2503.17191, CALCO 2025] characterise distributive laws between
container-monads and container-comonads on Set, including mixed monadic-over-directed laws; by
contrast our T_M and G_M are a monad and a comonad on the category Cont itself, obtained from a
single Set-monad M by transferring it to shapes and to positions respectively, so our mixed law
λ and its arrow-orientation κ live one level up in [Cont,Cont] and are not instances of their
classification."

**Aside:** their Example 22 links monadic-container laws to matching pairs of monoid actions /
Zappa–Szép — adjacent to [[orchestration-is-zappa-szep-weld]] / [[supply-chain-zs-computed]] but
monad–monad and monoid-level, not the entwining. See [[effects-coeffects-scoop-checks-cleared]],
[[branching-obstruction-is-atkeys-index]].
</content>
</invoke>
