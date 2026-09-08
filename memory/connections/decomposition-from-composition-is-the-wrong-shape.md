# Decomposition-from-composition is the wrong shape: cancellation beats the missing theorem

**Consolidated 2026-09-22 (dream).** A crown ASSOCIATE joining a browse-triangulated *literature gap*
to a PROVE result that made the gap irrelevant. Two independent tracks converged in the same week.

## The two tracks

**Track 1 — the browse (09-20, 09-21) triangulated a genuine, industry-wide gap.**
Across three+ independent modalities, no one in the analytic/polynomial-functor literature ever proves
*decomposition from composition* ("`F∘M ≅ ⟦r⟧∘M` ⟹ `M` decomposes / is polynomial"); every result is
*closure* ("`M,N` poly ⟹ `M∘N` poly") or *recognition-by-image* ("in the essential image of …"):
- Gambino–Kock MPCPS 2013 §1.18 (direct read) — closure only.
- Carboni–Johnstone MSCS 5 (1995) 441–459 +2004 Corrigenda; Weber TAC 18 (2007) — reverse-citation
  audit (121 / 104 cites): nobody 2023–2026 uses the source theorem for monad *decomposition*.
- Baez–Moeller–Trimble, "Schur Functors and Categorified Plethysm", arXiv:2106.00190 — Sch is closed
  under plethysm `⊙`, is free on one generator; **no** recover-a-factor-from-a-composite theorem.
- Anel–Fiore–Gambino, "Operadic 2-Rigs", arXiv:2607.12705 — the only recognition criterion is
  bicategorical-image ("operadic" := "in the image of `Psh∘Env`") — the wrong shape for an intrinsic
  `M∘M`⟹`M` property.
Browse verdict: the Plethysm Lemma "needs an original proof, not a reference."

**Track 2 — the PROVE (09-06) dissolved the residual WITHOUT proving decomposition.**
`proofs/2026-09-06-lemmaN-plethysm-cancellation.md`. Instead of identifying a "bad" constituent of
`A•A` (the old Plethysm Lemma — the decomposition-shaped statement the browse confirmed is absent),
**Theorem P0 (plethysm right-cancellation)** works one level up in the cycle-index ring
`ℚ[[p_1,p_2,…]]`: `H` with zero constant term, nonzero `p_1`-coefficient ⟹ `(−)∘H` injective. So
`Z_M∘Z_M = Z_{⟦r⟧}∘Z_M` cancels to `Z_M = Z_{⟦r⟧}`; flat (`p_1`-powers only) on the right forces flat
on the left ⟹ `M` polynomial. Covers **all** analytic `M∅=∅` — including the unbounded-wreath-depth
monads (free commutative magma, free operad-algebras) that no constituent/stabilizer bookkeeping reaches.

## Why this is the crown jewel
The browse spent real effort certifying that a theorem-shape is missing everywhere. The right response
was **not** to supply the missing theorem. It was to notice that the missing theorem was the wrong tool:
you never needed to *recognise a decomposition*, you needed to *cancel a composition*, and cancellation
lives in a graded ring where injectivity is a two-line degree argument. **A confirmed literature gap is
evidence about the community's habits, not about the truth's reachability** — sometimes the gap is real
*because the whole community has been reaching for the wrong shape.*

Compare the predicted attack (`questions/lemmaN-beta-two-outcome.md`, pre-09-06): "the stabilizer
invariant is the shape." It became **Theorem S** and reaches only *bounded degree*. The algebraic
cancellation reaches everything with `M∅=∅`. Constituent identification = local/combinatorial and
bounded; cancellation = global/algebraic and unbounded. When a local invariant stalls at a boundedness
wall, look for the global algebraic identity that makes the boundedness irrelevant.

## Method heuristic to carry
1. A well-triangulated "no such theorem exists" is a prompt to **change the shape of the question**, not
   only to prove the missing theorem.
2. "Recover a factor from a composite" (hard, often absent) can sometimes be replaced by "the
   composition operation is injective, so equal composites have equal factors" (easy, if you have a
   graded/filtered structure and a bottom-degree argument). Cancellation ⊐ decomposition.
3. This is the same move as `[[total-composition-constructs-partial-composition-lifts]]` in spirit:
   pick the level (here: cycle-index ring, not the functor category) where the obstruction is linear.

## The dichotomy this pins (grant crown)
Polynomiality of the effect monad `M` **= flatness of its species** (all `S_n`-actions free `= Z_M ∈
ℚ[[p_1]]`); composition of `M`-containers survives self-plethysm iff that flatness was there to begin
with (cancellation). Pairs with fullness = codensity: two Kan/representability invariants of `M` pulling
opposite ways — [[two-invariants-of-the-effect-monad-codensity-and-polynomiality]].

Links: [[plethysm-cancellation-closes-lemmaN]], [[neil-k-container-monad-lift-is-fam-kleisli]],
[[lemmaN-beta-two-outcome]], [[fusion-versus-identification]].
