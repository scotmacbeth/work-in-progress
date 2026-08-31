# Effect–coeffect arrows on Cont: the compositor is the *reverse* entwining, and it exists iff M doesn't branch

**MacBeth, PROVE 2026-07-29.** For Neil (07-29 steer) and Robin. Full proof:
`proofs/2026-07-29-effect-coeffect-arrows.md`; harness `scratch/monad-comonad-transfer/bikleisli.py`;
registry `effect-coeffect-arrows.json` (proved).

## The one-sentence result

The effect–coeffect arrows `f : G_M p → T_M q` (coeffect comonad on the source, effect monad on the
target — Neil's exact object) **form a category — the biKleisli category — iff the effect monad `M` is
non-branching (arity ≤ 1)**. And the compositor is **not** the entwining `λ:T_MG_M⇒G_MT_M` I proved on
07-27; it is the **opposite** law `κ:G_MT_M⇒T_MG_M`, the branching-obstructed one.

## Why this is the interesting answer (not the expected one)

Neil conjectured (and PROVE.md restated) that the proved entwining `λ` **is** the compositor. It isn't.
When you compose two arrows you must turn `G(Tq)` into `T(Gq)` — that is the arrow `GT⇒TG`, the *lax*
product-comparison `∏M→M∏` on positions, which is `κ`, the **reverse** of `λ` (whose backward map is the
*oplax* `str:M∏→∏M`). PROVE.md's orientation was off by the swap. And `κ` is exactly the direction I
showed on 07-27 **fails for branching `M`** (Pf: union-of-products ≠ product-of-unions, fails the
mult-`T` axiom E2′).

So the picture is a clean **dichotomy of two dual faces**:

| face | law | which M | what |
|---|---|---|---|
| **arrow / Freyd** (compose `Gp→Tq`) | `κ:GT⇒TG` lax | **non-branching only** | biKleisli of monad+comonad |
| **bialgebra / Turi–Plotkin** (`G` on `T`-alg, `T` on `G`-coalg) | `λ:TG⇒GT` oplax | **all M** | Beck EM distributive law |

They coincide for arity ≤ 1. For branching `M` the **bialgebra exists but the arrow category does not** —
effect and coeffect can be *paired* denotationally but not *sequentially composed*. **Branching is
exactly the obstruction separating the bialgebra from the arrow.**

## What's proved (honest grading)

- **Theorem A** (category ⟺ non-branching): the category axioms unwind as unit=E1′/E3′,
  associativity=E2′; and E2′ holds iff M non-branching (07-27). **Proved.**
- **Direct arrow-level confirmation** (not just the abstract law): built the biKleisli composite as a
  real Cont-morphism. `Maybe` → genuine category (1536/1536 assoc triples, unit laws, well-typed);
  `Writer/ℤ₂` → genuine category (4608/4608). `Pf` → **non-associative**, explicit witness triple
  (differs at shape `b`, pos `(1,0)`: `∅` vs `{0}`). Tellingly, for `Pf` the *unit laws still hold* —
  only associativity breaks, precisely E2′.
- **Neil's Plotkin–Turi question: YES**, for the `λ`-direction (EM bialgebra, all M); the `κ`/arrow
  face is the operational dual, obstructed by branching.

## Gaps

1. E2′ general index-chase (mechanical; inherited from 07-27, done for the ∏-Mendler examples).
2. Full **Arrow/Freyd** (`first`/premonoidal strength) needs `T_M` strong + `G_M` costrong for `⊗` or
   `×` on Cont — not checked. The *category* doesn't depend on it. **Natural next PROVE/LEAN target.**
3. Neil's `Cont(Set^→)→Set` predicate-lifting/logic angle: not addressed.

## Neighbour, different engine (novelty)

Katsumata–Rivas–Uustalu *Interaction Laws of Monads and Comonads* (1912.13477) unify effect/coeffect
via **Chu spaces / Day convolution** (interaction laws = monoids in Chu; greatest interacting comonad =
Sweedler dual) — a *pairing* `TX⊗DY→…`, **not** the biKleisli composition of `Gp→Tq`. Distinct;
cited as the alternative unification. My reading note 2026-07-29 already flagged the arrow-category
synthesis as genuinely open — nobody has assembled it, especially for containers, and the container
answer turns out to be a *conditional* one governed by branching.

## For the paper / book

This is paper-worthy in the "one canonical direction, with a named obstruction" style Neil likes — and
it's *two* dichotomies stacked: (i) `λ` vs `κ` orientation; (ii) bialgebra (all M) vs arrow
(non-branching). Sits on top of the Ch4 transfer + entwining. **Question for Neil:** own short paper
(ACT?), or a section folded into the entwining chapter? And do you want me to chase the (co)strength so
we can claim the full Arrow, or is "the biKleisli category, iff non-branching" the right stopping point?

— MacBeth
