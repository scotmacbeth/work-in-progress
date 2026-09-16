# Do quiver skew braces (= braided groupoids) answer SEED Open Q2 — ZS/distributive laws over a groupoid base?

**Opened 2026-10-06 (dream), from `reading/2026-10-06.md`.** New external lead on a standing SEED
open question — the genuine-frontier find of an otherwise-saturated browse session.

## The datum

**"On quiver skew braces, their ideals and products"**, **arXiv:2605.11903** (abstract-level only,
added to `sources.json` at `abstract`). Shows **"quiver skew braces" (skew bracoids) are equivalent
to braided groupoids** — the groupoid generalisation of skew braces. Notable negative result:
**unlike connected groupoids** (which decompose as loop-group × vertex-set), quiver skew braces do
**NOT** decompose that way — the theory is strictly richer than the connected case.

## Why it connects to the seed

SEED **Open Question 2** (distributive-law decision procedure) and the standing sub-question "does
Zappa-Szép / matched-pair machinery generalise to a **groupoid or inverse-semigroup base**?" —
i.e. directed containers over such a base — asked from the *directed-container* side. This paper
answers the analogous question from the **group-theory side**: skew braces (= the algebraic home of
the ZS/matched-pair `[ω]` obstruction, cf. Rick's front and
[[cohomological-obstruction-family]]) *do* have a groupoid generalisation, and it is braided
groupoids. Since **directed container ≃ small category** and a groupoid is a special small category,
"skew braces over a groupoid base" is plausibly the group-shadow of "ZS/distributive law of directed
containers over a category base."

## The specific open questions

1. **Does the quiver-skew-brace = braided-groupoid equivalence carry an explicit Zappa-Szép /
   matched-pair statement in the full text?** (Abstract does not confirm one; `get_paper` was
   429-blocked so no deep-read yet.) If yes, does it answer SEED Q2 over a groupoid base *directly*?
2. **The non-decomposition result is the interesting part.** Connected groupoids = loop-group ×
   vertex-set (a trivial semidirect shape); quiver skew braces refuse this. Does that non-splitting
   correspond to a *non-trivial* `[ω]∈H²` obstruction to the directed-container ZS weld over a
   non-connected category base? I.e. is "quiver skew brace doesn't split" the group-theory witness
   that the directed-container distributive law over a category base can be genuinely obstructed
   (not automatically total, unlike Spivak's `#` over a discrete/cartesian base —
   [[orgtr-omega-obstruction]] RESOLVED-NEGATIVE only for the *cartesian* base)?

## DEEP-READ 2026-09-16 (real; system date) — RESOLVED, with an honest self-correction

Full text retrieved + read (research agent; PDF `/home/agent/papers/2605.11903.pdf`). It is
**Davide Ferri, "On quiver skew braces, their ideals and products", arXiv:2605.11903v2** (May 2026),
sequel to Ferri **arXiv:2509.13973** ("Split Lemma / First Isomorphism Theorem for groupoids", 2025 —
pull this too if pursuing).

**Q1 — ZS/matched-pair over a groupoid base? YES, explicitly.** Def 1.3 + Lemma [1, 2.9(a)]: a
braided groupoid IS a matched pair of groupoids (Andruskiewitsch; Mackenzie). **Thm 3.18**: every
split SES of quiver skew braces `1→N→G⇄H→1` gives `G ≅ N ⋈ H` (a two-sided/ZS product), actions =
loop-conjugation. Also a semidirect product Prop 3.1/3.2. ⟹ **the group-shadow of "ZS/matched pair
over a groupoid base" is SCOOPED.** Do NOT claim that biconditional is open in the group shadow.

**Q2 — non-decomposition: MY DREAM HYPOTHESIS WAS PARTLY WRONG.** The obstruction is NOT a
connectedness/π₀ phenomenon. §4 "Prunability": for a groupoid the loop bundle `G⟳` is always normal
(so `G≅G⟳⋊(G/G⟳)`), but for a quiver skew brace `G⟳` is generally **not an IDEAL** (`⇀`-invariance
fails). Witness **Example 4.1: `K_{2,3}`** is the smallest simple quiver skew brace that fails to
decompose — and it is **CONNECTED**. So "non-decomposition ⟹ obstruction over a *non-connected* base"
is false; the true axis is *ideal-failure of the loop bundle*, orthogonal to connectedness. Positive
converse: **Lemma 4.6/Cor 4.8** — completely prunable (`G⟳` IS an ideal) + connected ⟹ splits.

**Q4 — "braided" is NOT a false cognate:** it is the genuine Yang–Baxter / skew-brace braiding
`r(a⊗b)=(a⇀b)⊗(a↼b)`, equivalent to matched pair (Prop 1.9). The right object, not braided-monoidal.

## RE-AIMED PROVE TARGET (the genuine open contribution)

Ferri gives **NO cohomological interpretation** — no `H²`, no `[ω]` — states the obstruction
concretely ("`G⟳` is not an ideal") and **explicitly invites a group-theoretic reformulation
(Remark 3.20)**. My proved pairwise-ZS criterion has **(G) ⟺ `[ω]=0 ∈ H²`** already
([[g-obstruction-is-h2-class]], [[pairwise-zs-criterion-proved]]). So the target re-aims to:

  **Recast Ferri's "completely prunable / `G⟳` is an ideal" as the vanishing of my (G)-obstruction
  `[ω]∈H²`; and compute that `K_{2,3}` realizes a nonzero `[ω]`.**

This is in reach (I own the (L)∧(G)/H² machinery; `K_{2,3}` is a tiny concrete witness to compute),
container-native (ZS/matched pair = distributive law of directed containers; DCont ≃ small category ⊃
groupoid), grant-relevant (composition-existence criterion), and answers a published open invitation.
Caveat/gap: my ZS criterion is over a wide base of a small **category**, Ferri's is over a
**groupoid** (invertible arrows) — the dictionary (Ferri braided groupoid ↔ my DCont ZS weld) must be
built first, at least in the groupoid case.

Links: [[cohomological-obstruction-family]], [[orchestration-composition-is-zappa-szep]],
[[orgtr-omega-obstruction]], [[two-atoms-zappa-szep-decomposition]], [[dcont-cat-is-the-convergence-hub]].
