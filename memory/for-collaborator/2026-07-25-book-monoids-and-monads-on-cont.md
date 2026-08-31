# Book refactor: Ch6 → "Monoids and Comonoids", new "Monads on Cont" section in Ch7

**Date:** 2026-07-25 (write session). **File:** `projects/books/category-of-containers.tex`
(`\author{MacBeth}`; seed off GitHub — read from the projects volume or ask me to email it).
Compiles clean with `pdflatex` (×2), **54 pages, 0 undefined references**.

For Neil (this executes his 2026-07-24 "Ch4 answers / tasks" email). CC framing: for Robin.

## What changed

**1. Chapter 6 is now "Monoids and comonoids in Cont: directed containers, categories, and the
free monoid."** The comonoid spine (directed containers ≅ small categories ≅ Cof) is untouched.
I added a closing section stating the **free ◁-monoid** on a container — statement only, per your
"state here, prove universal property in the Monads chapter":
`C* = (S', P')`, `S' = μY.(1 + Σ_{s:S}(P s → Y))`, `P' = leaves`, grafting monoid, three
◁-monoid laws (prior art Gambino–Kock Thm 4.5; Lean-verified `Free.lean`). Its universal property
is the free-monad Lemma in Ch7; the two are cross-linked both ways.

**2. New section in Ch7, "Monads on the base, comonads on Cont: the transfer"** (your item 2):
- **Proposition (proved + Lean-verified):** a monad `M` on Set transfers to a comonad
  `G(S,P)=(S, M∘P)` on Cont; counit backward = `η`, comult backward = `μ`; the three comonad
  laws are exactly `M`'s three monad laws read through position-contravariance
  (counit-left ⟺ right-unit, counit-right ⟺ left-unit, coassoc ⟺ assoc); biconditional; dual
  `H` from a Set-comonad. Machine-checked in `MonadComonadTransfer.lean` (Quot.sound only).
- **Your structural "why" is in, as a Remark:** `G = {M/(S,P)} = Lan_{(S,P)} M`, the ◁-left
  coclosure with `M` in the numerator, with the universal property `Poly(Gp,r) ≅ [Set,Set](⟦p⟧, r∘M)`.
- Novelty Remark distinguishes Ahman–Uustalu update monads (opposite direction) and Purdy–Damato.
- Worked `M = Maybe` example (adjoin a basepoint slot to every operation's arity).
- **Item 1 (higher-order trees):** left as a clearly-flagged **stub with a browse TODO** — I have
  not read Ghani–Kurz yet, so I did not invent its content. Flag me to prioritise that browse.
- **Items 3–5 (reader `ΔS ⊸ −`, Kleisli `ΔS ⊗ p → q`, oracle coalgebras `S → ⟦[p,q]⟧S`):** an
  "on the horizon" teachbox with your definitions, flagged **[to be developed]** — no results
  claimed.

**3. Small fix (Ch3):** the coequaliser-non-preservation result now cites the correct paper —
AAG **Categories of containers (FoSSaCS 2003)**, Prop 4.3 / Ex 4.4 — not the 2005 TCS paper.
Added the bib entry; kept the well-integrated Proposition (it is not in "further work").

## Open questions for you
- **Higher-order trees:** confirm the Ghani–Kurz paper you mean, and whether the initial-algebra
  example should sit in the free-monad section or the new transfer section.
- **Reader/Kleisli/oracle:** which of the three do you want worked first? The oracle
  (continuation) coalgebra question looks like the richest — is it meant to land as a monad on Cont?
- The Lean for the transfer is done; cofree comonad Lean still waits on Robin's `PFunctor.M`
  addition to the repo's Mathlib.

Chapter list now: 1 Preface · 2 Containers & extension · 3 The category Cont · 4 Which functors
are containers? · 5 Algebraic structure · 6 **Monoids and comonoids** · 7 **Monads and comonads**
(free/cofree + the new transfer section) · 8 Zappa–Szép · 9 Functors over Cont (Phase-2) · 10 Tracker.
