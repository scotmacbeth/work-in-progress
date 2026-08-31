# Workers = (Set,×)-graded category, and the Contextads A.4 gap it lands on

**Crown jewel of the 2026-07-28 dream.** Bridges Path 2 (comonads/DCont), Path 5
(agent orchestration), and the Zappa–Szép thread. Two claims: (I) the Workers
construction proved today sits almost exactly on an **unproven theorem in the
published literature**, and (II) it is the *second axis* of a duality with the
H² obstruction.

> **★★ RESOLVED 2026-07-29 (verdict on claim I): ORTHOGONAL — Workers settles NO
> fragment of A.4.** Their grade is DEPENDENT (`X→S`, Def A.3(1)) over a FIXED `S`,
> multiplying via one monad's `seq` (Eq A.2.2, codomain the same `S`) — structurally
> incapable of `S×T`. Mine is EXTERNAL `S` ranging over all `(Set,×)`, multiplying
> cartesianly. Their State_S (Def 3.36/Thm 3.37) is the *state monad* `(X×S)^S` at
> fixed `S`; mine is the *store comonad* `S×X^S` — different functor. **Clean
> positioning (my extension, not in the paper): by their Example 3.24 ("every
> M-graded comonad = a trivially-fibred contextad / colax action `C×M→C`"), Workers
> with `M=(Set,×)` IS the trivially-fibred corner of the general `Ctx` framework —
> the OPPOSITE corner from A.2/A.4's dependency-essential case (line 6922: "neither
> used dependent types essentially").** So: cite A.4 as nearest neighbour + self-
> identify via Ex 3.24; do NOT claim to prove a case of A.4. Claim (II) [two axes]
> is unaffected and stands. Neil (07-29) independently agreed "cite as neighbour."

## The two objects, in coordinates

**Workers (PROVED today — `proofs/2026-07-28-delta-state-object-and-workers.md`,
registry `state-object-delta.json` = proved).**
- `ΔS = (S, s↦S)` = codiscrete category (DCont≅Cat); `⟦ΔS⟧X = S×X^S` = store/costate comonad.
- A **Worker** `p→q` with state `S` = container map `ΔS⊗p → q` (Dirichlet ⊗).
- `ΔS⊗ΔT = Δ(S×T)` **strict** (Lean'd, rfl) ⟹ composition **multiplies context to `S×T`**.
- **Workers = category graded by `(Set,×)`** = coKleisli of the graded comonad `S ↦ ΔS⊗−`.
- Grade = **external, non-dependent** (a plain set `S`); multiplies via **Cartesian ×**.

**Capucci–Myers, "Contextads as Wreaths" (arXiv:2410.21889, App. A.2 — DEEP-READ
today via `download_pdf`+`pdftotext -layout`; sources.json → deep-read).**
- A **polynomial monad** `T` (container `P:S→Type`) transposes to a *dependently
  graded comonad* ("contextad" `⊙`): grade of `X` is a **map `X→S`**;
  action `X⊙s = (x:X)×P(s(x))`; composition multiplies the grade via the monad's
  `seq`: `(s⊗t)(x) := seq(s, t(x))`.
- **Theorem A.4: `Kl(T) ≅ Ctx(⊙)`** — **left UNPROVEN by the authors**: "we leave
  this theorem unproven because we want to give it an abstract proof in future
  work … for any parametric right adjoint monad." A genuine open theorem in the
  published literature, squarely on the Workers territory. Zero Zappa–Szép content
  in 82pp (grepped).

## (I) The relationship — sharp OPEN question, NOT resolved here

Both are graded comonads whose grade multiplies on composition. But:
- **Grade shape differs.** Workers: external plain set `S` via `ΔS`. Contextads:
  dependent `X→S` tied to a specific monad `T`.
- **Multiplication differs.** Workers: Cartesian `×` (from `Δ(S×T)`). Contextads:
  the monad's `seq`. Is Workers' `×` the *degenerate `seq`* of a specific choice
  of `T` (the store/state structure)?
- **Distinct from my OWN transfer** `G(S,P)=(S,M∘P)` (arbitrary Set-monad pushed
  onto *positions* → comonad; [[position-op-turns-monads-into-comonads]]).
  Contextads is a *self*-transpose of ONE container-monad's Kleisli category.
  **Three different constructions in one neighbourhood** — keep them separate.

**The load-bearing question (→ next Workers PROVE):** is `S↦ΔS⊗−` an instance of
Capucci–Myers `⊙` for a specific polynomial monad `T`? If yes, **does my coordinate
proof of the Workers graded-category laws already prove the special case of the
UNPROVEN Theorem A.4?** That would be a real contribution — proving a case of a
stated-but-unproven published theorem. If the grade shapes are genuinely
incompatible (external vs dependent), Workers is *orthogonal* and cites A.4 as a
neighbour. **Do not assume either — this is exactly what PROVE must settle.**
Honest novelty status: the Workers *mathematics* is proved; its *positioning*
against A.4 is open. Ch4/Workers writeup must lead with 2410.21889 App. A.2.

## (II) Two axes of agent composition — the grant duality

From the collaborator note (`for-collaborator/2026-07-28-workers-graded-category.md`):
Workers is the **state axis** of compositional correctness, dual to the
Zappa–Szép **directed axis**.

| axis | object | composition | obstruction |
|---|---|---|---|
| **State** (Workers, proved 07-28) | `ΔS⊗p→q`, store comonad | context **multiplies** `S×T`, graded by `(Set,×)` | **none** — always composes, grade accumulates |
| **Directed** (ZS, proved earlier) | `C⋈D`, directed container | may **fail to exist** | `[ω]∈H²(Sk_C;𝒟)` ([[orchestration-composition-is-zappa-szep]]) |

The state axis is **unobstructed-but-accumulating**; the directed axis is
**obstructed-but-non-accumulating**. Both are how two directed-container/agent
systems compose — one grows a `(Set,×)`-grade, the other clears an H²-class.
Grant Path-5 line: stateful-agent composition (context grows) and orchestration
re-entrancy (composition may fail) are the two orthogonal failure/growth modes of
compositional correctness. → [[applications-are-directed-containers]],
[[orchestration-composition-is-zappa-szep]].

## Real-world traction (grant data point)
Sannier–Baillot, "Dependent Coeffects for Local Sensitivity Analysis" (PACMPL 2026,
DOI:10.1145/3776670, no arXiv) — a differential-privacy type system explicitly
"leverages the recently introduced construction of a dependently graded comonad"
(the Contextads apparatus). Independent uptake of the graded-comonad/wreath toolkit
outside pure CT — worth one grant sentence.

## Breadcrumbs
- **Para** (Neil's "S might change"): `Para(p,q)=Σ_{S:Set}Cont(ΔS⊗p,q)`, the
  `(Set,×)`-action `S·p=ΔS⊗p` (Gavranović). Δ is functorial only on **bijections**
  ⟹ literal Para over `Core(Set)`; strict `(Set,×)`-actegory reading is `computed`,
  not proved (registry `para-identification`). Primary cites (no nLab "Para" page):
  arXiv:2105.06332 (Capucci–Gavranović–Hedges–Rischel, ACT 2021), Gavranović thesis
  2403.13001, blog. The Para↔Poly↔graded-monad bridge is **genuinely unwritten**
  (checked 3 angles 07-28) — novelty upside, no shortcut citation.
- Std anchor "ZS = distributive law between `T=H×−`, `S=K×−`" = Myers' n-Café
  comment (monad-monad; my entwining is monad-comonad — distinguishing sentence owed).
