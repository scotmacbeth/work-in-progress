# Theorem S′ proved — bounded wreath depth closes THM 3 necessity (Robin/Neil)

**2026-09-07, MacBeth.** Second result today. Full writeup:
`proofs/2026-09-07-theorem-S-prime-wreath-depth.md`. Registry: node
`theorem-S-prime-wreath-depth` in `m-containers.json` promoted **speculative → computed**
(math proof-complete; grade tracks the un-deep-read Joyal import, exactly as its siblings P/S/U).

## What it says
For an **analytic monad** `M = Ã` (species `A`), define the **wreath depth** `𝔥(A)` via a new
**imprimitivity-depth invariant** `h`. Then:

> **Theorem S′.** `A` non-flat **and bounded wreath depth** (`𝔥(A)<∞`) ⟹ `Ã∘Ã ≇ ⟦r⟧∘Ã` for every
> polynomial `⟦r⟧`. So closure ⟹ `M` polynomial. (M-containers compose ⟺ M polynomial.)

## The invariant (this is the piece the old note said was missing)
- `h_t(T)` for transitive `T` = max length of a strictly-refining chain of `T`-invariant **block
  systems** (equivalently, max subgroup chain from a point-stabilizer to `T`). Conjugacy-invariant,
  well-defined as a max over a finite lattice. Primitive ⟹ `h_t=1`; `S_2≀S_2` ⟹ `2`; triple wreath
  ⟹ `3`.
- `h(K) = max_{orbit O} h_t(K^O)`; `𝔥(A) = sup over constituents of h(H_l)`.
- **Two laws, both proved:** (Lemma 1) wreath is **superadditive**, `h_t(T_1≀T_2) ≥ h_t(T_1)+h_t(T_2)`
  (explicit concatenated chain); (Lemma 2) a **block-fixing product on disjoint supports has
  `h = max` of its factors**.

## The proof in one breath
Every `⟦r⟧∘Ã` stabilizer (each-label-once component) is a **block-fixing product** of single-`A`-
constituent aut groups (Meta-theorem, polynomial outer = rigid positions), so by Lemma 2 its depth is
`≤ 𝔥(A)=W`. But `Ã∘Ã` realises, via a **uniform substitution** (outer non-flat `c`, all slots filled
with one depth-`W` constituent `b`), the wreath `H_b≀H_c`, whose sub-orbit induces a transitive
sub-wreath of depth `≥ W+1` (Lemma 1). `W+1 > W` ⟹ not isomorphic (Lemma E: natural iso preserves the
per-component stabilizer profile, hence all `h`-values). ∎

## Why it matters for the grant / THM 3
It **subsumes Theorem S** (bounded degree ⟹ `𝔥 ≤ d-1`), **re-proves `𝕄`** (all `H_l=S_n` primitive,
`𝔥=1`; witness `D_4` at depth 2) and every primitive-constituent monad, and holds for **any**
`a_0=|M∅|` and **unbounded degree** — the plethysm engine (Thm P) needed `a_0=0`; this needs nothing
of the sort. Combined with P (`a_0=0`) and the U-corner (`a_0>0`, unbounded depth, closed today), the
residual of THM 3-necessity for analytic monads is now **exactly one row**:

    a_0 > 0  AND  unbounded wreath depth (𝔥(A)=∞),

and its one **named** inhabitant, the free commutative unital magma `U`, is already closed (NO). So
**every analytic monad we can name now has THM 3 as an unconditional biconditional.**

## The honest gap (next PROVE target: `theorem-general-stabilizer-necessity`)
`h` provably cannot separate the last row (depth `=∞` both sides). Unifying framework in §5: the escape
is a **support-indecomposable factor of `Ã∘Ã` outside `𝓕(A)`** (the factors realised by `A`'s own
constituents). `h` is the "greater depth" special case; the `U`-proof is the "same degree, a diagonal
not a wreath" case (peg-built `C_2`). Open: does such an escape **always** exist for non-flat `a_0>0`,
`𝔥=∞` — the hard sub-case being **wreath-closed** monads (free magmas), where the wreath escape is
absent and one must build a diagonal via the constant peg as for `U`.

**Suggested framing for the paper's §5.6:** state P, S′, U as three proved engines with the residual
table; §5's `𝓕(A)`-framework is the natural conjecture to headline as the remaining frontier. Happy to
draft the section on the `/write` trigger.

— MacBeth
