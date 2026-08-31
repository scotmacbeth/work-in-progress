# Book section written: "Which liftings, all of them: monad liftings are comonads over the base"

**MacBeth — write session, 2026-08-09 (second).** For Neil and Robin.

## What landed

A new subsection `\subsection{Which liftings, all of them: monad liftings are comonads over the
base}` (`sec:liftings-are-categories`) in **Ch7** (`ch:moncomon`), inside `sec:moncomon-fibration`.
It is the **climax** of the fibration section: it sits right after the "both legs of the codomain
fibration" teachbox (the ∏/∐ criteria) and before the two closing forward-glances.

File: `books/category-of-containers.tex`. Compiles clean, **81 pages** (was 77), 0 undefined refs,
0 new bibitems. It reads directly from the host projects volume, so no email attachment — the source
is on disk.

## The result, in one breath

We had already shown (previous section) that of Reader's two named liftings, ∐ survives and ∏ dies.
This section asks the honest question — **what is the *complete* list of Reader's data-valued monad
liftings?** — and the answer welds the whole boundary story back onto the book's spine:

> **The proof-relevant monad liftings of Reader `y^E` are exactly `E`-indexed families of small
> categories.** (∏ is excluded; `Σ_U` are the *discrete* categories; a ℤ/2 groupoid is a genuine
> non-∐, non-∏ lifting; analytic aggregators die on the counit.)

The mechanism is the astonishment I wanted the section to turn on: **a monad lifting is secretly a
comonad**. Its multiplication `μ^T : TT → T` is a *container morphism*, so the load-bearing half is a
*backward* map — a *comultiplication*. Monad upstairs, comonad downstairs; and comonads, Chapter 5
already taught us (`thm:objdict`, Ahman–Uustalu), are small categories. So the directed-container ≅
`Cat` equivalence reappears one categorical level up, for the same reason.

The governing one-liner, proved as a lemma: **∏ needs a monoid, ∐ needs nothing.** Coproduct is a
comonad for free; product over an index `I` is a comonad iff `I` is a monoid. Reader's leaves carry
the diagonal comonoid but no monoid, so ∐ lifts and full-∏ over `E` cannot — which *is*
`T_M`-lifts-iff-cartesian read one level down.

## Structure of the subsection

1. `Prop prop:reader-reduction` — liftings over `R=y^E` ↔ aggregators `L:Set^E→Set`; monad structure
   ↔ (counit ε, comultiplication δ) + three laws.
2. The astonishment paragraph (monad = comonad, via the fibrewise op; forward-ref to the transfer §).
3. `Lemma lem:monoid-comonoid` — ∏ needs a monoid, ∐ needs nothing.
4. `Thm thm:reader-classification` — Reader's liftings ≅ E-indexed small categories, with a
   decode-table of what the clean points become.
5. `Remark rem:analytic-excluded` — polynomial is the boundary; the counit kills Sym²/Bag.
6. Teachbox "The whole boundary lands on Cat".
7. Teachbox "The open frontier: State and general container monads" (honest: reduction only).

## Two honesty flags (please keep in mind if you read it as a referee)

- **Classification hypothesis:** `L polynomial`. A full removal needs "every accessible Set-comonad
  with a counit is polynomial", which is *not* proved — flagged in the Remark. The natural
  non-polynomial rivals (Sym², Bag) are excluded by the counit.
- **State / general M is OPEN.** The reduction runs (a fibred lifting of a container monad `M` is a
  *family* of aggregators `(A_σ)_{σ∈S_M}`, threaded through `M`'s shape monoid; State ⟹ an
  `S^S`-graded / store-internal category), but I do **not** prove completeness. One warning sign:
  `ev_{s₀} : State ⇒ Id` is not a monad morphism, so the auxiliary-monoid-∏ route does not transfer.
  This is the live next PROVE target — a clean "liftings of M = categories fibred over M".

## One thing I did to respect the citation floor

The load-bearing "polynomial comonads ≅ small categories" step routes through the book's own
`thm:objdict` (deep-read Ahman–Uustalu 2016, `AU16`), **not** through the abstract-only `ACU14`
(arXiv:1408.5809, "When Is a Container a Comonad?"). If someone wants `ACU14` cited at load-bearing
strength, it needs a deep-read first — flag for a browse session.

## For the grant

This is grant Path 2 at full strength: the proof-relevance / predicate-lifting story does not merely
*touch* the directed-container `Cat` spine — its liftings **are** small categories. Objects,
morphisms (cofunctors), and now liftings all fall into `Cat`. Neil's two feeds and the ℤ/2 grading
were the map; `Cat` is the destination.

## One question for Neil

The Ch7 lead-ordering is still your call. As written, the classification stands as a theorem
regardless of ordering. But if you want Ch7 to *lead* with the fibrational payoff, this
classification — "the liftings are categories" — is arguably a stronger opener than the identity
`T^Σ_M = M◁−`, because it lands the reader straight back on `Cat`. Happy to promote it if you agree.
