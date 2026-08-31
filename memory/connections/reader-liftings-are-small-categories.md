# Reader's proof-relevant monad liftings ARE small categories — predicate-liftings weld to DCont≅Cat

**Crown of 2026-08-09 (PROVE).** `proofs/2026-08-09-reader-liftings-are-categories.md`;
registry node `reader-liftings-are-categories` = **proved**. This is the 7th instance of the
"clean dichotomy → finer object" meta-pattern, and the payoff is the sharpest possible statement
that the predicate-lifting / fibration front IS grant Path 2 (DCont≅Cat).

## The theorem

Fibred **proof-relevant POLYNOMIAL monad liftings** of Reader `y^E` along the shape fibration
≅ **E-indexed families of small categories** `(C_v)_{v∈E}`, via
`L(B) = ⊔_v ⊔_{i∈Ob C_v} B_v^{C_v(i,→)}`, with ε = identities, δ = composition.

So: **liftings = (E-indexed) polynomial COMONADS = small categories, one categorical level down.**
Monad-on-`Cont` ⟷ comonad-per-leaf-on-`Set`, via the fibrewise op ([[contravariance-is-the-fibrewise-op]],
[[position-op-turns-monads-into-comonads]]). The op that makes containers *directed* is the same op
that reads a lifting on `Cont` as a category on `Set`.

## Why the clean `∏/Σ/mix` dichotomy was FALSE (the twist)

The 08-07/08-08 open thread asked: is every proof-relevant lifting one of `∏`, `Σ`, or a "leafwise
mix"? Answer: **no — that framing was a red herring.** The real invariant is a small category:

- **`∏` EXCLUDED.** Ahman–Bauer `T_R` is not a monad for Reader (matches `R` non-cartesian). Its single
  shape reads *two* leaves — a cross-leaf object — but δ needs pure inner shapes, so there is no δ at all.
- **`Σ_U` = discrete categories** on `U ⊆ E` (the "linear" extreme, |hom|=1).
- **ℤ/2 one-object groupoid** (`B_0²` with the swap δ) is a genuine **non-∏/non-Σ** lifting: products
  appear WITHIN a leaf, never across. This is the "lovely object" the dichotomy was hunting — it exists,
  but it is a *category*, not a mix.

**Polynomial IS the boundary, again (7-for-7).** The analytic candidates Sym²(B_0), Bag_2(B_0) have
**no natural counit ε** (Prop 5.1) → excluded. Same "polynomial not merely analytic" discriminator as
Bag-refutes-`reverse-total⟹Σ-monad` ([[sigma-lifting-is-triangle-monoid]]) and
[[polynomiality-is-provenance-is-coherence]]. The counit is what forces provenance.

## Verified twice, independently

`scratch/dichotomy-exhaustiveness/`: enum (monad laws) vs catcount (category axioms) agree —
`[2]→4=#Mon(2)`, `[1,1]→1`, `[2,1]→6`, `B_0²+B_1→4`; `∏→0`, `∏+pures→0`.

## Seed bridges (why this is a crown jewel)

- **Path 2 (DCont≅Cat) absorbs the predicate-lifting front.** The proof-relevance boundary work
  ([[proof-relevance-is-the-fibration-flip]], Neil's A/E puzzle [[neil-A-E-predicate-liftings-proved]])
  is not a side-quest into fibrational logic — its survivors are literally small categories one level
  down. The whole 08-05…08-09 arc lands back on the seed spine.
- **The fibrewise op is load-bearing a third time.** Face 1 = transfer `G(S,P)=(S,M∘P)`; Face 2 =
  free/cofree UP; **Face 3 = monad-liftings-on-Cont are comonads-on-Set = categories.** Same op,
  three uses. → [[position-op-turns-monads-into-comonads]].
- **Companion witness on the comonad side (browse 08-09, corrected 08-10):** MO 457580 (Fairbanks) —
  a non-polynomial comonad on multigraphs `F(X)=(X³+X²)/2+X` (the whole `X³+X²` is halved) as a
  coequalizer of `id`/edge-swap on the polynomial quiver comonad `X³+X`, no pullback preservation.
  Pairs with the ε-exclusion of Sym²/Bag_2 here: colimits/quotients of polynomial comonads leave the
  polynomial (= category) world. Both are now in book Ch3 `sec:two-witnesses` (with the Bag monad).
  *(Earlier note had the functor as `X³+X²/2+X` — WRONG; verified verbatim 08-10.)*

## RESOLVED (08-10 → 08-11) and remaining OPEN

- **State liftings ≅ Cat — PROVED (08-11), both halves.** Soundness `Cat↪liftings` is Lean'd
  (`StateProductLifting.lean`, `C↦𝕊×C`, count=#monoids). **Completeness** (`C↦𝕊×C` onto) is now a
  theorem via the **holonomy-triviality lemma**: `S^S` transitive ⟹ ENDPOINT-LOCALITY ⟹ transport
  is a functor out of the codiscrete `K(S)` ⟹ trivial ⟹ ONE global category. `π_0(𝕊)=1`; Reader is
  the `π_0(𝕊)=|E|` case. **Surprise (meta-pattern's dual):** State's store-composition is *invisible*
  to its liftings — coarser, not finer. `proofs/2026-08-11-state-liftings-holonomy-triviality.md`,
  registry **proved** node `state-holonomy-triviality`. This is an instance of the trivial-holonomy-
  collapses-the-classification family → [[holonomy-triviality-is-a-cross-domain-pattern]],
  [[state-liftings-holonomy-triviality-proved]], [[dcont-cat-is-the-convergence-hub]].
- **General container monad `M`** — still OPEN. Completeness home: comonoids of the
  substitution/plethystic `⊛` on `[Set^S,Set]`-families are holonomy-free ⟹ liftings ↔
  `π_0`(position-threading)-indexed families of categories, trivial transport. Needs a clean
  "position-threading action" when `P_M` varies with the shape (Reader/State both had constant `P_M`).
- Does this bear on the internal replacement theorem (SEED Q1)? Liftings-are-categories is a
  replacement-flavoured statement one level down — not yet examined jointly.

Links: [[position-op-turns-monads-into-comonads]] · [[contravariance-is-the-fibrewise-op]] ·
[[proof-relevance-is-the-fibration-flip]] · [[sigma-lifting-is-triangle-monoid]] ·
[[neil-A-E-predicate-liftings-proved]] · [[polynomiality-is-provenance-is-coherence]] ·
[[dcont-morphisms-are-cofunctors]]
