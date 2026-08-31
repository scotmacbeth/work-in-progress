# Chain rule for the container derivative under composition

**Date:** 2026-06-12 (prove session)
**Status:** Proved, self-contained over Set, compiles. Computationally verified (23 finite containers).
**Output:** `projects/proofs/2026-06-12-container-chain-rule.tex` (+ .pdf, 8pp).
**Frame:** Phase-2 (operations on the category of containers — Neil's steer "that's where I see a paper").

## The result

For containers `F = S ◁ P`, `G = T ◁ Q`, with `◁` = composition (substitution,
`⟦G◁F⟧ = ⟦G⟧∘⟦F⟧`), `∂` = AAGM one-hole-context derivative, `×` = binary product:

> **∂(G ◁ F) ≅ (∂G ◁ F) × ∂F**   in **Cont**.

This is the container shadow of the Faà di Bruno / analytic-functor chain rule, but
with **substitution `◁`** as the composition operation. It is **NOT in AAGM 2003**
(they have the sum and product rules and a derivative *definition*, not the `◁` chain
rule). Closest prior art: **Joram–Veltri arXiv:2512.17484** (Dec 2024, Cubical Agda),
who prove it in univalent foundations and confirm the classical case holds — consistent
with our one classical lemma. So: **[Original]** container-language derivation; cite
Joram–Veltri for the univalent case and AAGM for `∂`'s definition.

## The proof in one breath

The composite's positions are the **dependent coproduct** `∐_{q:Qt} P(f q)` over the
`G`-positions `Qt`. To differentiate (choose a hole) you pick an index `q₀` **and** a
hole inside that block. The leftover splits:

```
∐_{q≠q₀} P(f q)        +        (P(f q₀) ∖ p₀)
  other inner blocks               this block, punctured
   = ∂G ◁ F                         = ∂F
```

Choosing `q₀` and keeping the other blocks full = `∂G` on the index, blocks substituted
by `F` = `∂G ◁ F`. The punctured block = `∂F`. Positions add ⇒ product. **The chain
rule is Leibniz for an indexed product.**

Explicit iso:
- **Shapes** `(t,f,q₀,p₀) ↦ ((t,q₀, f|_{Qt∖q₀}), (f q₀, p₀))`. Bijective by the
  **pointed-domain splitting** `(Qt → S) ≅ S × ((Qt∖q₀) → S)`, `f ↦ (f q₀, f|_{Qt∖q₀})`.
- **Positions** `(q,p) ↦ inl(q,p)` if `q≠q₀`, `↦ inr(p)` if `q=q₀` (then constraint
  forces `p≠p₀`, so it lands in `P(f q₀)∖p₀ = ∂F` positions).

## The one assumption (flag for Lean / HoTT)

The pointed-domain splitting needs `Qt ≅ 1 + (Qt∖q₀)`, i.e. every `q` is `q=q₀` or
`q≠q₀` — **classical EM on the proposition `q=q₀`**. Free over Set. This is *exactly*
the hinge Joram–Veltri handle carefully in univalent foundations (where `Qt∖q₀` is
`Σ_{q}(q≠q₀)` and it holds after set-truncation). For directed containers over Set: free.

## Warm-ups (all the same one move — splitting the hole-choice)

- `∂Id ≅ 1`, `∂K_A ≅ 0`
- `∂(F+G) ≅ ∂F + ∂G`
- Leibniz: `∂(F×G) ≅ (∂F×G) + (F×∂G)`
- `y²` check: both sides `2(F×∂F)` — fixes the convention.

## Next steps / asks

1. **Lean.** Natural follow-on: `Cont.lean` (PR #12) already has `×`, `+`, category.
   The proof is finite + bijection-based ⇒ should transcribe directly. Watch the
   dependent transports around `P(f q₀) = P s⋆` — use the `Ext.ext_eq` discipline from
   the D2/D5 laws. I'll set a LEAN.md trigger.
2. **Book / paper.** This is a clean phase-2 section. Slots next to free/cofree
   (`§sec:freecofree`). With the atoms + Leibniz it's a self-contained "calculus of
   containers" chapter. Faà di Bruno is a one-paragraph corollary (partitions = ways to
   distribute holes among inner blocks) — could expand.
3. **Neil question:** does he want this aimed at a standalone short note (it's original)
   or folded into the book's operations chapter? The Joram–Veltri overlap is only the
   univalent case, so a classical/directed-container note is defensible on its own.

## Forward pointer (not chased)

`∂F` carries a comonad structure (zippers); its interaction with `◁` and with the cofree
comonad `C^∞` (see free/cofree note) deserves its own session.
