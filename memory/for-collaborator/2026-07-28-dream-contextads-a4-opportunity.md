# Dream breadcrumb (07-28): the Workers proof lands on an UNPROVEN published theorem

**For the next daily to Neil.** Two things the Workers pipeline surfaced that are
worth raising:

## 1. Capucci–Myers Theorem A.4 is left UNPROVEN — and it's on our territory
Deep-read "Contextads as Wreaths" (arXiv:2410.21889) App. A.2 this cycle.
**Theorem A.4 `Kl(T) ≅ Ctx(⊙)`** — a polynomial monad `T` transposing to a
dependently graded comonad whose grade multiplies by `seq` — is stated but
**explicitly left unproven** ("we want to give it an abstract proof in future work,
for any parametric right adjoint monad"). This is "close to verbatim" the Workers
shape (`ΔS⊗p→q`, grade multiplies via `Δ(S×T)`).

**Opportunity:** if our `S↦ΔS⊗−` is an instance of their `⊙` for a specific `T`,
then the coordinate proof I already have for the Workers graded-category laws
**proves a case of their open theorem**. If the grade shapes are incompatible
(our external `S` vs their dependent `X→S`), Workers is orthogonal and cites A.4 as
the nearest neighbour. This is the next Workers PROVE target — do you want me to
chase the instance identification, or keep Workers self-contained and cite A.4?

## 2. Two axes of agent composition (grant framing)
Workers = the **state axis** (context multiplies `S×T`, `(Set,×)`-graded, always
composes — no obstruction, grade accumulates), dual to the Zappa–Szép **directed
axis** (`[ω]∈H²`, composition may fail). Unobstructed-but-accumulating vs
obstructed-but-non-accumulating — a clean grant-Path-5 duality for stateful-agent
orchestration.

## 3. Two flags
- **Race risk:** Spivak's CT2026 talk "Categories by Kan extension" builds comonads
  "from distributive laws of monads over comonads" — on our entwining/transfer
  territory. Re-checking whether this is in the posted arXiv:2503.21974 or talk-only.
- **Ghani–Kurz CALCO 2007 Thm 3.2** (`X↦μY.X×FY` comonad) fills the empty 4th
  quadrant of the free/cofree table — but it's higher-**dimensional** (Rogers/
  linguistics) trees, not higher-**order** (HOAS). Which did you mean for Ch4 item-1?

Full analysis: `connections/workers-graded-and-contextads.md`.
