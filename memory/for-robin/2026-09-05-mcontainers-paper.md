# Draft paper: M-containers — codensity governs fullness, polynomiality governs composition

**2026-09-05 (WRITE session). MacBeth.**

**File:** `~/projects/papers/mcontainers-codensity-polynomiality.tex` (+ compiled `.pdf`, 16pp).
Compiles clean with `pdflatex` (two passes), 0 undefined refs, 0 overfull hbox.
Citation footprint: **floor deep-read** (all four refs; dropped an orphan Ahman–Uustalu bibitem),
no `agent-summary` source cited.

**STATUS 2026-09-05 (WRITE): SENT TO RICK for review** (PROTOCOL §2, PDF attached, CC Robin),
pushed to `scotmacbeth/work-in-progress` commit `b94bc32` (stamped commit `40ff1f4`). Do NOT push
to `publishable-result` or email Robin the §4.3 note until Rick has reviewed. Asked Rick: is THM 2's
codensity criterion clean, and does THM 3's honesty split convince (esp. the trailing-M inertness Prop)?

## What it is
The wrap-up note for Neil's UID-147 ("probability") / UID-148 ("K-containers, change of base
Cont→M-Cont") emails, and a clean brick for the containers-over-a-base line. It assembles the
M-container trio proved 09-04/09-05:

- **THM 1 (identification).** `M-Cont = Fam(Kl(M)^op)`, and the extension factors as
  `⟦S,P⟧_M = ⟦S,P⟧ ∘ M` — an M-container functor is an ordinary polynomial functor with a
  trailing effect monad. Neil's "change of base" is precomposition with the Kleisli inclusion.
- **THM 2 (fullness = codensity).** `⟦−⟧_M : M-Cont → [Set,Set]` is ALWAYS faithful; full ⟺
  M is codense (`M ⇒ Ran_M M` iso) and each `Set(A,M−)` connected (affine ⟹ connected). So
  probability (D, affine+codense) KEEPS fullness; error/partiality/reader/nondet LOSE it.
  The naive "M preserves coproducts" guess is refuted (writer `E×−` preserves coproducts yet
  fails for `|E|≥2`).
- **THM 3 (composition = polynomiality).** M polynomial ⟹ `⟦−⟧_M`-image closed under ∘, with
  `p ◁_M q = p ◁ ⌈M⌉ ◁ q` (associative, non-unital unless M=Id). Necessity: a cardinality
  growth law that already kills P⁺, P, D at p=q=Id and buries the "commutative+affine" folklore.
- **Corollary (the punchline).** Fullness and composition are two INDEPENDENT invariants of M
  that trade oppositely: probability is faithful but not composable, error is composable but
  not faithful.

## Honesty boundaries (all marked in the text)
1. **THM 3 is now a biconditional-in-practice** (updated this WRITE cycle to match the 09-05 prove
   session, `proofs/2026-09-05-lemmaN-retract-and-beta.md`). New §5 typesets: Lemma R0 (M poly ⟺
   M∘M preserves connected limits, PROVED); Prop (single self-composite `M∘M≅⟦r⟧∘M` categorically
   INERT — the sharpened trailing-M obstruction, PROVED); stabilizer invariant + Thm (𝕄∘𝕄≇P∘𝕄 via
   Young-vs-D₄-wreath, PROVED); dichotomy Thm (necessity for EVERY monad that arises: super-poly by
   cardinality, analytic by stabilizer); residual = **Plethysm Lemma, OPEN** (general non-free
   analytic; no known monad inhabits it). So the converse is proved for every monad that arises;
   only the species plethysm statement is unconditional-blocking.
2. **D full-faithfulness is conditional** on the rigidity lemma `Nat(D,D)={id}` (isolated as
   Lemma, assumed not reproved). The reduction to it is unconditional.
3. **Kleisli-bifunctoriality of `◁_M`** is flagged open (= codensity again — the exact meeting
   point of THM 2 and THM 3).
4. **Carboni–Johnstone** (familial representability = polynomial) sits only at `agent-summary`
   in my sources, so I did **not** put it in the bibliography. It is attributed in prose for the
   OPEN Lemma N, and the load-bearing "polynomial ⟺ preserves connected limits" fact is cited to
   Gambino–Kock / Niu–Spivak (both deep-read). If we want C–J as a formal citation, it needs a
   deep-read in a future browse session first.

## Suggested next steps
- **Rick review DONE-sent 2026-09-05** (PROTOCOL §2). Await his restatement; act on it, then
  consider `publishable-result` (which triggers the §4.3 email to Robin).
- If a browse session upgrades Carboni–Johnstone to deep-read, add it as a formal \cite in §5.
- A LEAN session could formalise Lemma R0 (retract-of-limit-preserving; the 09-05 prove file flags
  it as Lean-able) and THM 1(b) `⟦−⟧_M = ⟦−⟧∘M` (defeq, cheap) as machine-checked anchors.

Grant framing: feeds Theory (container extension ↔ codensity / polynomiality) and Impact
(agent orchestration — "an agent may decline" composes but costs fullness, not composability).

---

## UPDATE 2026-09-06 (WRITE session) — THM 3 necessity now CLOSED; paper revised to 18pp

The 09-06 prove session (`proofs/2026-09-06-lemmaN-plethysm-cancellation.md`) **dissolved the OPEN
Plethysm Lemma** of honesty-boundary #1 above. I folded it into the paper this WRITE cycle. New §5.7
"Cycle-index cancellation, and the necessity trichotomy":

- **Lemma (plethysm right-cancellation):** `H∈ℚ[[p_1,p_2,…]]` with `a_0=0, a_1≠0` ⟹ `(−)∘H` injective.
  Elementary, self-contained, code-verified — no external cite needed.
- **Thm P:** analytic monad with `M∅=∅` ⟹ closure ⟹ polynomial, **at any degree and any nesting
  depth**. Route: `M∘M≅⟦r⟧∘M ⟹ ⟦r⟧ flat ⟹ Z_A∘Z_A=Z_B∘Z_A ⟹` cancel `⟹ Z_A=Z_B ⟹` A flat. Covers
  the free magma / free operad monads (`S_2≀…≀S_2` towers) the old D₄/Young stabilizer method could
  never reach. This is the real advance.
- **Thm S:** bounded-degree analytic (any `M∅`) via a support-indecomposable finest-splitting invariant;
  **subsumes** the old 𝕄/D₄ theorem (kept as the motivating example).
- **Necessity trichotomy** (super-poly / analytic-`M∅=∅` / bounded-degree) + the sole residual now a
  **Conjecture** (`M∅` nonempty-finite ∧ unbounded degree ∧ unbounded nesting — argued vacuous, NOT
  claimed proved). THM 3 is thus an **unconditional biconditional modulo one clearly-flagged conjecture**.

Nice structural point now in the paper: this cancellation is exactly the trailing-`M` cancellation that
Prop 5.x (inertness) forbade *at the level of limit preservation* — legitimate because it lives on the
finer, faithful cycle-index invariant, which the single self-composite does determine.

Compiles clean (18pp, 0 undefined refs), citation floor still **deep-read**. Joyal 1986 + BLL Ch.1–2 are
named **inline only** (same convention as Carboni–Johnstone, boundary #4) — both still `agent-summary`,
so a browse session should deep-read them before any arXiv/journal submission.

**Pushed:** `scotmacbeth/work-in-progress` — content commit `82e32d2`, self-ref hash fill `4675935`.
URL: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/mcontainers-codensity-polynomiality.tex

**Rick's copy (b94bc32) is now SUPERSEDED.** Because this is a WRITE session (no email), I did NOT re-send.
Next-cycle action: email Rick the corrected PDF (CC Robin) noting it supersedes b94bc32. Still holding at
"sent to Rick" — do NOT push `publishable-result` until Rick reviews.
