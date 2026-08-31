# Transfer novelty — three neighbours engaged (2026-07-25 wake)

**Task:** clear/narrow the novelty of the monad→comonad transfer `G(S,P)=(S,M∘P)` (Neil's Ch4 item 2,
registry `monad-comonad-transfer` = **proved**) against the three neighbours the 07-25 browse surfaced
but left unengaged. Two research agents; verdicts below. **Outcome: novelty NARROWED, not scooped.**

## 1. Topos-PLTL blog — ADJACENT, no scoop
"Free PLTL algebras and a coalgebraic extension of hyperdoctrines," Topos Institute blog, 2025-09-26
(https://topos.institute/blog/2025-09-26-free-pltl-algebras-and-hyperdoctrines/). Byline not confirmed —
**confirm author before citing.**

- Their `λ: MP → PI^op` is a nat. transf. between functors **into Pos**, not endofunctors on Poly.
  `M` = monad on **Pos** from the free⊣forgetful PLTL-algebra adjunction (acts on *predicates*);
  `P` = a **hyperdoctrine** `C^op→Pos` (running case `Sub`); `I` = a comonad on Set (stream comonad
  `A^ℕ`, presented as the cofree comonad on a polynomial). Stream coordinate:
  `λ_A = v^{Sub(A^ℕ)} ∘ M(cur^A)`.
- **They never apply `M` to position/direction-sets;** never form `(S, M∘P_s)`. "left Kan
  extension"/"coclosure" do NOT appear.
- Their open Q (verbatim): for which comonad interfaces `I` does `λ` making `P` a map of monads exist;
  conjecture: only unary `p = B×X` (degree 1) — branching (degree≥2) obstructs → suggests CTL.
- **Same "upgrade fails at branching" slogan, different theorem.** Disjoint underlying math.

## 2. Hinze WG2.8 pearl "Monads from Comonads, Comonads from Monads" (~2010) — UNRELATED
- Built on an adjunction `L⊣R`. Central: *if a left adjoint `L` is also a comonad, its right adjoint `R`
  is a monad* (and dually). Laws transported across the adjunction ("flip laws"); key example product
  comonad `−×X ⊣ (−)^X` reader monad.
- Relates a comonad on `L` to a monad on the **different** functor `R`. **Not** `C↔C^op`, **not**
  fibrewise apply-to-positions. Purely abstract (co)monads/adjunctions; all examples in **Set**;
  **no containers/polynomials.** At most an optional "related mechanisms" cite.

## 3. Ahman–Bauer 2409.17664 — MANDATORY nearest-neighbour cite, NOT a scoop ★
"Comodule Representations of Second-Order Functionals," arXiv:2409.17664 v4 (Jun 2025; JLAMP 146, 2025).
This is in the exact territory — read in full.

- Same category **Cont** (shapes forward, positions backward; morphism `f◁g`), same interpretation
  `⟦A◁P⟧X = Σ_a(Pa→X)`, and — crucially — the **contravariant cointerpretation**
  `⟪A◁P⟫ = ∏_{a:A}(Pa×X) : Cont^op→Type` (attributed to **Ahman–Uustalu update monads**). This IS the
  position-op / fibrewise op the transfer factors through. So the *machinery* (Cont convention +
  cointerpretation) is prior art — memory already flags these as not-mine (AU / von Glehn).
- **Prop 4.1 / 4.2** (their monad↔comonad statement): for a monad `T` on `C`, right monad `T`-comodule
  ⟺ right comonad `T^op`-comodule ⟺ right monad `T`-module in `C^op`. Proof text: *"passing between
  monads on C and comonads on C^op is just a matter of taking opposites."* → **the trivial `C↔C^op`
  duality**, NOT the fibrewise transfer.
- **Thm 6.3** (their monad-on-Cont recipe): from a Set-monad `M` + a weak Mendler-style `M`-algebra on
  positions, `T(A◁P) = MA ◁ P⋆` — `M` applied to the **SHAPES**, positions merely extended, result a
  **MONAD**. Remark p.26: *"…produce monads … because the shape part is always independent of the
  position part."*
- **Mirror image of the transfer:** ours leaves shapes fixed, applies `M` to **positions**, yields a
  **COMONAD** = `Lan_{(S,P)}M` (◁-left-coclosure). Neither `(S,M∘P)` nor "monad-on-positions⇒comonad"
  appears in the paper.

## Combined verdict (what to write)
- **Novelty NOT "already published" — but materially NARROWED.** The general framing "monads & comonads
  on containers" and the cointerpretation op are **Ahman–Bauer 2409.17664 + Ahman–Uustalu** prior art.
- **What remains genuinely MacBeth's:** the specific construction *apply a Set-monad to the **positions**,
  `G(S,P)=(S,M∘P)`, giving a **comonad** on Cont, identified as the ◁-left-coclosure `Lan_{(S,P)}M`* —
  statement, direction, and coclosure identification in NEITHER paper.
- **Ch7 Novelty Remark rewrite (WRITE task):** lead with Ahman–Bauer 2409.17664 (adopt their `A◁P`
  notation where sensible), cite AU for the cointerpretation, Topos-PLTL as the parallel branching-slogan
  line (byline TBC), Hinze as optional related-mechanism. Pin the contribution to the **shapes-vs-positions
  / monad-vs-comonad dichotomy + coclosure identity**. Add the two-ways-to-feed-a-monad paragraph
  (shapes→monad `MA◁P⋆`, positions→comonad `S,M∘P`).

**Grade discipline:** theorem stays **proved** (unchanged). This is a novelty/attribution refinement, not
a re-grade. Ahman–Bauer PDF at `/home/agent/papers/ahman-bauer-2409.17664.pdf`.
Connection updated: [[position-op-turns-monads-into-comonads]].
