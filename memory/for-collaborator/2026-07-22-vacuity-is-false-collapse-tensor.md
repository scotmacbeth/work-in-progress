# Vacuity is FALSE — the collapse tensor (for Neil / Robin)

**Deep-work result, 2026-07-22.** Full write-up:
`proofs/2026-07-22-vacuity-resolved-collapse-tensor.md`. Registry node
`closed-day-structures.json → condition-vacuity` is now **proved (NO)**.

## The one-sentence answer
There **is** a symmetric monoidal structure on `Set` whose left-multiplication `(−)⋆B` is not a
polynomial functor — so its Day convolution on `Cont` is **convolutional but not left-closed**.
The side-condition of the 2026-07-15 closure biconditional is **not vacuous**:
**convolutional ⊋ left-closed**. Neil's "we were lucky with `⊗` and `×`" — you were.

## The counterexample: the collapse tensor
```
        ⎧ B   if A = ∅            unit ∅, symmetric.
A ⋆ B = ⎨ A   if B = ∅
        ⎩ 1   if A,B ≠ ∅   (collapse to a point)
```
- It is genuinely monoidal (natural associator, pentagon, triangle, unitors, braiding — proved by
  a finite emptiness-pattern analysis and checked exhaustively to size 3). I was a hostile referee
  here because of the support-tensor precedent (2026-07-21: cardinality-associative but *no*
  natural associator). Collapse is different — whenever two factors collapse the value is a single
  point, so there is no provenance to be inconsistent about. I re-implemented the delicate
  `∅→nonempty` functorial action myself (a naive version, like `support`, breaks there) and
  naturality + pentagon still hold.
- `R_2 = (−)⋆2` is **non-polynomial** in one line: `R_2(∅)=∅⋆2=2` (unit law) but `R_2(1)=1⋆2=1`,
  and every polynomial `F=Σ y^{a_i}` has `|F(∅)| ≤ |F(1)|`. Equivalently `R_2` sends the mono
  `∅↪1` to the non-mono `2→1`.

## Why we all missed it before
Every prior search (mine on 2026-07-21, the "3 killed candidates") hunted the **support**
mechanism: a *phantom extra* balanced element (`|1⋆B|` too big), which associativity forbids.
The collapse tensor fails by the **opposite** mechanism: the unit insertion `η_B:B≅∅⋆B→1⋆B` is
**non-injective** — "multiplying by 1 *shrinks*" (`|1⋆B|<|B|`). Nothing in the 2026-07-21 note
looked at that. The retraction lemma there is fine; it just never concerned `η_B`'s injectivity.

## A framework that predicted the mechanism (worth keeping)
This session I built an `η`-cartesian analysis of the point-pullback:
- **Lemma D (associativity):** balanced `u∈1⋆B` ⟹ `η_{1⋆B}(u)=(1⋆η_B)(u)`, proved via the two
  unit-insertion points `p_L,p_R:1→1⋆1` and left-unit/triangle coherence.
- **★' (structural, associativity-free):** `balanced⟹independent` ⟺ `η:Id⇒1⋆(−)` is a cartesian
  natural transformation ⟺ `⋆` preserves the corner pullback `(∅,C)=(1,C)×_{(1,1)}(∅,1)`. It
  *can fail* (non-injective / oversized fibre).

Exact dichotomy: **a monoidal counterexample needs Lemma D (guaranteed by associativity) AND ★'
to fail.** Collapse is precisely that (assoc + `η_2` non-injective). Support is the mirror (★'
holds, Lemma D fails, hence not monoidal). Two independent obstructions, each with its own witness
— which is exactly why a one-mechanism search couldn't find the collapse tensor.

## What this changes for the grant / book
- The 2026-07-15 biconditional is **unaffected** and now *more interesting*: closure is a real
  condition, and we have the extremal witness that it fails.
- Book Ch3 closed-structure section: state the biconditional, then give the collapse tensor as the
  example that the side-condition bites. Contrast with `⊗, ×, ▷_S` (all closed because their `⋆`
  is polynomial/linear in each variable).

## The question I'd like your steer on (refined target)
**Characterize the left-closed convolutional tensors** = monoidal `⋆` on `Set` preserving
connected limits in each variable. Necessary conditions in hand: (1) `η_B` injective (`⋆` taut /
mono-preserving — kills collapse); (2) ★' (`η` cartesian). Conjecture: the closed ones are exactly
the "sum-of-products in each variable" tensors (`×`, `+`, `∨_S`, combinations) — i.e. Day
convolutions of *polynomial* monoidal `⋆`. The Lemma D / ★' machinery is the tool to settle
sufficiency. Is this the right next PROVE target, or do you want the book section first?

— MacBeth
