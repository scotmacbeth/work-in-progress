# The entwining is now in the book — Ch7 §"The two feeds entwine"

**Write session, 2026-07-28. For Robin / Neil.**
Working copy: `projects/books/category-of-containers.tex` (58 pp, compiles clean, 0 undefined refs).
No PRs — the seed is off GitHub. Read it from the projects volume, or ask me to email the section.

## What went in

The proved **entwining of the two feeds** (`proofs/2026-07-27-monad-comonad-entwining.md`, registry
`monad-comonad-entwining.json` = proved) is now written into Chapter 7, as a new subsection
`\subsection{The two feeds entwine}` (`\label{sec:moncomon-entwine}`), placed right after the
`Maybe` example in the transfer section and **before** the two forward-looking teachboxes, so the
proved material precedes the stubs.

The subsection, in order:
- names the two liftings of one monad `M` — the shape-monad `T=(MS,P⋆)` (Ahman–Bauer Thm 6.3) and the
  position-comonad `G=(S,M∘P)` (the transfer);
- computes the two composites' positions at a shape `m`: `GT ↦ M(∏_b Z_b)`, `TG ↦ ∏_b M(Z_b)`;
- identifies the oplax product-comparison `str:M(∏Z)→∏MZ` as the backward map of `λ:TG⇒GT`
  (the standard mixed-distributive-law orientation);
- **Theorem `thm:entwine`** — `(T,G,λ)` is an entwining structure; four axioms = naturality of
  `η`, `μ`, `str`, and the Mendler `i`; consequences (`G` lifts to `T`-algebras, `T` to `G`-coalgebras);
- teachbox "what `λ` is" — the Beck–Chevalley 2-cell "M oplax-preserves products, on positions";
- **the branching obstruction** (featured): `Example ex:entwine-branching` shows `Pf` breaks the reverse
  orientation `GT⇒TG` via *union-of-products ≠ product-of-unions*; dichotomy table (arity≤1: both
  orientations; genuine branching: one way only);
- `Remark rem:entwine-scope` — honest scope: ∏-cointerpretation class only, general Mendler case open.

## Neil's 07-27 additions (all Ch7), status

1. **Literature sentences** — already landed in `rem:transfer-novelty` on 07-25 (Topos-PLTL, Hinze
   disambiguated, Ahman–Bauer first-named). Verified they still read correctly and don't duplicate the
   new subsection. Nothing to add.
2. **Ghani–Kurz higher-order trees** — teachbox upgraded from "browse TODO" to a generic **decode of the
   free-monad formula**: reading `C=(S,P)` as a signature, `C^*` IS the finite-term type; "higher-order"
   = arities `P(s)` are function types, so `C^*` becomes the higher-order tree type. The **exact GK
   n-dimensional-tree signature is left as `[signature TODO — ask Neil]`** — GK is still not in the reading
   set and this was a write session (no browsing), so I did not guess it. *Please point me at the paper id
   and the signature and I'll fill it in a browse/prove cycle.*
3. **Position-op "two faces" paragraph** — written into the "Syntax and behaviour" outlook: the transfer
   applies the fibrewise `(−)^op` to the fibre **object** (`M↦(M^op)_*`, monad→comonad); the free/cofree
   pair applies the same op to the recursion **scheme** (initial→final, syntax `μ` → behaviour `ν`).
   One op, two faces; the entwining is what happens when the first face meets a second copy of `M`.
4. **Predicate-lifting language** — adopted. `P⋆:MS→Set` is called a predicate lifting; the
   ∏-cointerpretation is the *universal* (Π-based) lifting.
5. **Workers forward-pointer** — a one-line "category of Workers `[to be developed]`" item added to the
   "on the horizon" teachbox (it's being developed now — see `proofs/2026-07-28-delta-state-object-and-workers.md`).

## One honesty fix (referee pass, worth flagging)

My first draft's dichotomy table said, for arity-≤1 monads, that the reverse orientation works "because
`str` is an isomorphism." That is **wrong**: for `Maybe`, the exception shape (zero leaves) gives
`str:M(1)→1`, which is not iso (`M(1)=1+1`). The correct reason is that arity ≤ 1 means no two leaves are
ever *shared*, so `μ` can identify none and mult-`T` holds trivially. Fixed in the table and prose. (The
proof file's shorthand "str=iso" is the same imprecision; the file's *mechanism* — "no overlap possible" —
is right, and that's what I used.)

## Chapter numbering — still pending your call

My book has 10 fine-grained chapters; your "Ch4 Monads&Comonads" = my Ch6+Ch7. I asked in the 07-28 daily
whether to consolidate to your coarser numbering. I did **not** renumber unilaterally; cross-refs all
resolve either way.

## Standalone note? — my verdict (you asked, 07-26)

**Yes, eventually.** The entwining wants its own short (4–5 pp) note: a distributive law is the seed's
core composition tool, and the two genuinely interesting facts — the *forced orientation* and the
*branching obstruction* (`Pf`, union-of-products ≠ product-of-unions) — make a crisp, self-contained
story that the book can only give a subsection to. But I'd write it **after** either the general-`j`
index-chase is spelled out or the Lean lands, so it's a note about a fully-closed result rather than one
carrying a "mechanical gap." Flagged, not started — tell me if you want it prioritised.

## Still open (unchanged from the proof file)
- E2 general index-chase over an arbitrary weak Mendler `j` (mechanical, not conceptual).
- Whether a canonical `λ` exists for a non-∏ Mendler algebra (open).
- A named Set-level free-monad-over-cofree-comonad descent (open).
- Lean: `str`-entwining extending `MonadComonadTransfer.lean` (next formalisation target).
