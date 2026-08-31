# For Neil/Robin — the general-M liftings conjecture is FALSE: liftings are holonomy-FULL

**MacBeth, PROVE deep-work 2026-08-11.** File: `proofs/2026-08-11-update-monad-liftings-holonomy-full.md`.

## The headline (a refutation that gives a better theorem)

`state/PROVE.md` asked me to prove: *general-M container-monad liftings ≅ π₀-indexed families of
small categories, holonomy-free*, with Reader (π₀=|E|) and State (π₀=1) as the poles.

**It's false.** I took the canonical varying-`P` test class — the **update monad**
`Upd_{(S,P,↓)}` (Ahman–Uustalu, TYPES 2013), the cointerpretation-dual of DCont≅Cat — and computed
its degree-1 polynomial monad liftings. They are classified by
```
        Upd_{(S,P,↓)} liftings   ≅   Fun( 𝔸(↓), Cat )
```
where `𝔸(↓)` is the **action category** of the monoid `P` acting on `S` (objects `S`, arrows
`s --p--> s↓p`). This is **holonomy-FULL**: the isotropy groups of `𝔸(↓)` act on the fibre
categories, and that action is genuine, non-collapsible data.

## The counterexample (exhaustive, airtight)

`S={0,1}`, `P=ℤ/2` acting **trivially** (`s↓p=s`). Then `𝔸(↓)=Bℤ/2 ⊔ Bℤ/2`. On the 2-object fibre
there are **exactly 4 law-satisfying liftings** — a `ℤ/2`-action (identity or swap) chosen
independently on each orbit — and they are **pairwise non-isomorphic** as liftings. Verified
**exhaustively** over all 16384 `Upd³` shapes plus an explicit iso-class check. So `π₀=2`, but the
answer is not "2 categories": each orbit carries a `ℤ/2` **holonomy**.

**`π₀` is not even the invariant.** Reader (`P=1`, π₀=2) admits **1** transport; this example
(π₀=2) admits **4**. Same π₀, different classification.

## Why Reader and State fooled us (the real mechanism)

Holonomy-freeness is a *special* property of `𝔸(↓)`, and I pinned exactly when it holds:
- **Reader** (`P=1`): `𝔸(↓)` is **discrete** — no arrows, no transport. Trivially holonomy-free.
- **State** (`P=`overwrite): the monoid has **reset elements** `w_m` (`s↓w_m=m` for *all* `s`).
  In the associativity instance a reset middle **erases the update label**, forcing
  *endpoint-locality*, which collapses each component to the **codiscrete** category — exactly the
  step that made `State liftings ≅ Cat` (`state-holonomy-triviality`, still correct). So State is
  holonomy-free *because overwrite has resets*, not for any general reason.
- A **generic** monoid (`ℤ/2`) has neither a trivial action nor resets — so the isotropy acts and
  holonomy survives. (A **free** action, e.g. `s↓1=1-s`, is a third holonomy-free case: trivial
  isotropy ⟹ codiscrete ⟹ single `Cat`.)

## Why this is good news for the grant

The corrected theorem *subsumes both proved poles as corollaries* and identifies the **exact
obstruction to holonomy-freeness**: the isotropy of the position-threading action. It ties the whole
liftings zoo to Ahman–Uustalu's update-monad / directed-container cointerpretation — the
varying-structure class the grant wanted — and it gives orchestration a crisp new phenomenon:

> **A coeffectful agent monad whose threading monoid has nontrivial isotropy composes with genuine
> holonomy — the composite carries a *representation of the isotropy group*, not merely a family of
> behaviours.** (A second-order composition datum, sibling to the `[ω]∈H²` reentrancy obstruction of
> the directed/ZS mode — different invariant, same lesson: composition remembers a group.)

## Honest gaps
- Degree-1 (discrete-opfibration) objects only — same restriction as the Reader/State proofs, so this
  *extends* their scope. Higher/branching degree not treated.
- Morphism-level transport with simultaneously-nontrivial fibre morphisms *and* isotropy: argued by
  the `𝔸(↓)`-functoriality mirror + discrete-fibre census, not written in closed backward-`β` detail.
- Beyond `Upd`: general container monads where positions vary but not via a monoid action — conjecture
  `Fun(𝒜,Cat)` for a threading category `𝒜`, holonomy-free iff `𝒜` holonomy-trivial. Open.

## Suggested next steps
1. **Lean the counterexample** — the 4 non-iso `ℤ/2`-holonomy liftings of `Upd(ℤ/2, triv)` — as a
   sorry-free witness that the conjecture is false. Small, decisive, grant-quotable.
2. **Book Ch7**: reframe the classification climax as `Fun(𝔸(↓),Cat)`; Reader/State are the discrete
   and reset-collapse degeneracies. The "isotropy = holonomy" table is one clean figure.
3. Novelty-check vs **Uustalu, TTCS 2017** ("container combinatorics: monads and lax monoidal
   functors") and **Ahman–Uustalu, "Distributive Laws of Directed Containers"** — deferred (no browse
   this session).

— MacBeth
