# THM 3 promoted: M-containers compose ⟺ M polynomial (sufficiency PROVED, necessity partial)

**MacBeth → Robin/Neil, 2026-09-05 (PROVE session).**
Proof: `proofs/2026-09-05-thm3-composition-polynomiality.md`. Registry
`proofs/registry/m-containers.json` node `thm3-composition-polynomiality` **computed → proved**,
validator green.

## What landed
Completes the M-container brick (answers Neil's UID-147/148 probability/K-container thread; sibling
of THM 1/2 codensity, `2026-09-04-m-containers-codensity.md`).

- **Sufficiency (PROVED).** If the effect monad `M` is a **polynomial functor**
  (`M ≅ Σ_i (−)^{B_i}`, container `⌈M⌉`), then M-containers compose:
  `p ◁_M q := p ◁ ⌈M⌉ ◁ q` (ordinary `◁` with `M`'s container spliced in the middle) satisfies
  `⟦p ◁_M q⟧_M ≅ ⟦p⟧_M ∘ ⟦q⟧_M`, natural in X. One line: `⟦p⟧_M∘⟦q⟧_M = (⟦p⟧∘M∘⟦q⟧)∘M`, and
  `⟦p⟧∘M∘⟦q⟧` is a composite of polynomial functors, hence `= ⟦r⟧`. **Associative** (from `◁`),
  **non-unital unless `M=Id`** (exact-cardinality argument: a unit forces `⟦e⟧∘M≅Id ⟹ M≅Id`).
  So `(Cont, ◁_M)` is semigroupal, monoidal only at `M=Id`.
- **Necessity (PARTIAL, but the useful half is proved).** Closure forces a **cardinality growth
  law**: `|M(M n)| = R(|M n|)` for a fixed polynomial `R` (and `|M(N(M n))|=R_N(|M n|)` for every
  polynomial `N`). This **already at `p=q=Id`** kills `P⁺`, `P`, `D` (their `m∘m` is
  doubly-exponential — no polynomial fits). This is *cleaner* than the sub-agent's squaring test.

## The headline correction (for the WRITE / grant)
**"M-containers compose ⟺ M commutative + affine" is DEAD.** The honest axis is **polynomiality**:
- `Maybe (X+1)` and `writer (2X)` are **non-affine** yet **compose** (polynomial).
- `P⁺`, `D` are **affine + commutative** yet **fail** (not polynomial).

The old distributive-law / Zappa–Szép-`H²` framing measured a *different* question (does `⟦q⟧` lift
to `Kl(M)`, merging the two M's via `μ` — lossy/lax). Retired in the registry.

## Crown (two independent invariants of the effect monad M)
- **Fullness of `⟦−⟧_M` ⟺ codensity** (`Ran_M M` iso), THM 2.
- **Composition of M-containers ⟺ polynomiality**, THM 3.
They genuinely diverge: **writer composes but isn't full; `D` is full but doesn't compose.** Two
distinct Kan/representability invariants — a clean bridge to Leinster-style codensity worth a WRITE.

## The one honest gap (Neil — is this a known lemma?)
The **full** categorical converse "closure ⟹ `M` polynomial (preserves connected limits)" is
**open**. The obstruction has a name: **trailing-`M`**. Every M-extension is `(−)∘M`, so closure
only ever yields `F∘M ≅ ⟦r⟧∘M`, and precomposition `M^*=(−)∘M` is *not conservative* — you cannot
cancel the trailing `M`. Three attempts (connected-limit reflection; monad-unit retract; diagonal
`Id`-retract-of-`Sq`) all die on this. The intended finish is **Carboni–Johnstone / Diers**
("`Set→Set` preserves connected limits ⟺ familially representable") run on the *family* of
cardinality identities for all polynomial `N` — converting cardinal rigidity into
limit-preservation. **Question for you: is there a slick way to strip the trailing `M`, or a known
result "`M∘N` polynomial for enough `N` ⟹ `M` polynomial"?** If so, THM 3 closes to a full iff.

Sufficiency + the sharp exclusions are enough to ship the composition section solidly; the gap is
precisely delimited for the wrap-up paper's "future work" or a quick kill if you know the lemma.
