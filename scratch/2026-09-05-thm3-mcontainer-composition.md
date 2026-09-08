# THM 3 — Do M-containers compose? The criterion is POLYNOMIALITY, not "commutative + affine"

**MacBeth — 2026-09-05 (scratch, THM 3 work).**
Input facts (proved, `proofs/2026-09-04-m-containers-codensity.md`): `M-Cont ≃ Fam(Kl(M)^op)`;
`⟦S,P⟧_M = ⟦S,P⟧ ∘ M` (ordinary polynomial functor post-composed with `M`); `⟦−⟧_M` always
faithful, full ⟺ `M` codense ∧ each `(M−)^A` connected.

> **Headline.** The PROVE.md/sketch heuristic **"M-containers compose ⟺ M commutative and
> affine" is REFUTED.** The honest, computed criterion is:
> **`M-Cont` is closed under a composition product `◁_M` compatible with the extension
> `⟦−⟧_M` iff `M` is a *polynomial functor*** (`M ≅ Σ_{i∈I}(−)^{B_i}`; equivalently `M`
> preserves connected limits / is familially representable / is itself an ordinary
> container's extension).
> This is a *different axis* from affine/commutative:
> - **Maybe `X+1` COMPOSES** (polynomial) — even though it is **non-affine**.
> - **`D`, powerset `P`, nonempty powerset `P⁺` DO NOT compose** (non-polynomial) — even
>   though `P⁺` and `D` are **affine AND commutative**.
>
> The distributive-law route the sketch proposed (`M∘⟦q⟧ ⇒ ⟦q⟧∘M`) is a **red herring**:
> it forces the two `M`'s to merge via `μ` and yields only a lax/monad composite, not the
> honest "composite of two M-extensions is again an M-extension". The correct route needs no
> `μ` at all.

---

## 1. The one structural computation that settles it

Write `p=(S,A)`, `q=(T,B)`; `⟦p⟧(Y)=Σ_s Y^{A_s}`, `⟦q⟧(Y)=Σ_t Y^{B_t}` (ordinary
polynomials). Then, using `⟦−⟧_M = ⟦−⟧∘M`,

```
(⟦p⟧_M ∘ ⟦q⟧_M)(X) = ⟦p⟧_M( ⟦q⟧(MX) ) = ⟦p⟧( M( ⟦q⟧(MX) ) ) = G(MX),
        where   G := ⟦p⟧ ∘ M ∘ ⟦q⟧ : Set → Set.
```

So the composite of two M-extensions is **always of the form `G ∘ M`**, `G = ⟦p⟧∘M∘⟦q⟧`.
It is an M-container extension `⟦r⟧_M = ⟦r⟧∘M` **iff `G` is (naturally iso to) a polynomial
functor** `⟦r⟧`. (`G` polynomial ⟹ `G∘M = ⟦r⟧∘M = ⟦r⟧_M`; sufficient, and — see §4 — the
finite counting shows it is also necessary for the non-polynomial monads.)

**`G` is polynomial for every `p,q` iff `M` is polynomial.**
- (⟸) Polynomial functors are closed under composition and contain every `⟦p⟧,⟦q⟧`; so `M`
  polynomial ⟹ `G=⟦p⟧∘M∘⟦q⟧` polynomial. **No `μ`, no strength, no commutativity used.**
- (⟹) Take `p=q=Id`-container: `G=M`, must be polynomial. (Sharper witness: `p=q=` squaring,
  §4, gives the finite counterexamples.)

**The product.** When `M` is polynomial, let `⌈M⌉` be *the* container with `⟦⌈M⌉⟧=M`. Then
```
        p ◁_M q  :=  p ◁ ⌈M⌉ ◁ q          (ordinary container composition, M inserted in the middle),
        ⟦p ◁_M q⟧_M  ≅  ⟦p⟧_M ∘ ⟦q⟧_M.
```
`r = p ◁ ⌈M⌉ ◁ q` — the left `M` of `G` is *absorbed into the polynomial part* `⟦r⟧`; the
rightmost `M` is the extension's own `∘M`.

---

## 2. Why the distributive-law framing is the WRONG route (correction to the sketch)

The sketch (and PROVE.md §4/THM 3) said: to move the middle `M` past `⟦q⟧` we need a
distributive law `λ: M∘⟦q⟧ ⇒ ⟦q⟧∘M`, whose existence is a "commutative/affine → Zappa–Szép/`H²`"
question. That route computes
```
⟦p⟧∘M∘⟦q⟧∘M  --λ-->  ⟦p⟧∘⟦q⟧∘M∘M  --μ-->  ⟦p⟧∘⟦q⟧∘M = ⟦p◁q⟧∘M,
```
which **(i)** requires `μ` (merging the two `M`'s, generally NOT a natural iso — information
is lost), so it is a **lax** composite, not the honest closure; and **(ii)** measures
whether `⟦q⟧` *lifts to `Kl(M)`* — a question about making the composite a **monad**
(update-monad flavour), which is a genuinely different question from "is the composite of two
M-extensions again an M-extension".

The honest route (§1) needs **no `λ` and no `μ`**: it keeps both `M`'s, absorbing the left
one into the polynomial coefficient functor. That is why the criterion is **polynomiality of
`M`**, not commutativity/affineness. This is the *same species of error* as the THM 2
correction (there: "preserves coproducts" was the criterion for a coarser Kleisli-enriched
target; the honest `[Set,Set]` target wanted codensity). Here: "commutative + affine" is the
criterion for the distributive law / Kleisli lift, but the honest closure question wants
polynomiality.

**The two named obstructions, resolved.** For `M(Σ_t X^{B_t}) → Σ_t (MX)^{B_t}`:
- *Power `(−)^{B_t}`.* `M(X^B)→(MX)^B` (tuple of projections) always exists but is generally
  not iso. Irrelevant on the honest route: if `M` is polynomial, `M∘(−)^B` is automatically
  polynomial — no map is needed.
- *Coproduct `Σ_t`.* `M(Σ_t Z_t)` vs `Σ_t MZ_t`. On the honest route we do NOT push `M`
  through the coproduct; `M(Σ_t Z_t)` is simply *re-expanded as a polynomial* when `M` is one
  (`M=Σ_i(−)^{B_i}` ⟹ `M(Σ_t Z_t)=Σ_i(Σ_t Z_t)^{B_i}`, still polynomial). Non-polynomial `M`
  (`D`, `P⁺`) cannot be re-expanded — that is the true break.

---

## 3. Structure of `◁_M`: associative, but NON-unital (semigroupal, not monoidal)

For polynomial `M`, `◁_M` inherits associativity from `◁`:
```
(p ◁_M q) ◁_M s = p◁⌈M⌉◁q◁⌈M⌉◁s = p ◁_M (q ◁_M s).      [◁ associative]  ✓
```
But there is **no unit** unless `M=Id`: a unit `e` would need `e◁⌈M⌉ = y` (the `◁`-unit),
impossible for `⌈M⌉≠y`. Equivalently, functor-composition's unit is `Id_Set`, which is not in
the image of `⟦−⟧_M` (every `⟦−⟧_M(X)=⟦−⟧(MX)` factors through `M`). So:

> `(M-Cont, ◁_M)` is an **associative, non-unital (semigroupal)** structure for polynomial
> `M`; it is genuinely **monoidal only when `M=Id`**.

**Obstruction is NOT `H²`/Zappa–Szép.** The associativity here is on-the-nose (inherited from
`◁`); the obstruction to composing *at all* is the sharp **representability (polynomiality)
dichotomy** of §1, not a cohomology class. (Contrast the ZS/`[ω]∈H²` story, which governs
partial/directed composition of a *single* container over its own base; here we are asking a
closure question about the effect monad, a different phenomenon. Do not conflate.)

---

## 4. The examples (all `computed`, exact integer counting)

Test container `p=q=` squaring (`⟦q⟧(Y)=Y²`). Then
`(⟦p⟧_M∘⟦q⟧_M)(X) = ( M((MX)²) )²`; with `|X|=n`, `u=mc(n):=|M(n)|`, the count is
`comp_n = mc(u²)²`. It is an M-extension iff `comp_n = P(mc(n))` for a **fixed** nonneg-integer
polynomial `P` (the coefficients are the shape-counts of `r`). Code:
`scratch/2026-09-05-thm3-compose-check.py` (ran clean).

| `M` | poly? | affine? | comm? | verdict | witnessed `r = p◁_M q` |
|---|---|---|---|---|---|
| `Id` | ✓ | ✓ | ✓ | **COMPOSES** | `Y⁴` (1 shape, 4 pos) |
| `Maybe` `X+1` | ✓ | **✗** | ✓ | **COMPOSES** | `Y⁴+2Y²+1` |
| exception `X+2` | ✓ | ✗ | ✓ | **COMPOSES** | `Y⁴+4Y²+4` |
| writer `2X` | ✓ | ✗ | ✓ | **COMPOSES** | `4Y⁴` |
| reader `X²` | ✓ | ✓ | ✓ | **COMPOSES** | `Y⁸` (=2·2·2 pos) |
| list `X*` | ✓ | ✗ | ✗ | composes (structural) | poly ∘ poly |
| `P⁺` nonempty pow. `2^n−1` | **✗** | **✓** | **✓** | **FAILS** | none exists |
| `P` powerset `2^n` | **✗** | ✗ | ✓ | **FAILS** | none exists |
| `D` distributions | **✗** | ✓ | ✓ | **FAILS** (structural) | none exists |

**Maybe (COMPOSES, exact).** `mc(k)=k+1`; `G(Y)=((Y²)+1)²=Y⁴+2Y²+1`. Checked at
`n=0..5`: `comp = 4,25,100,289,676,1369 = ⟦r⟧(mc(n))` for `r` with shape-counts `[1,0,2,0,1]`.
Break point of the *old* heuristic: Maybe is **non-affine** (`M1=2`) yet composes cleanly.

**`P⁺` (FAILS, exact — this is the clean refutation of "affine+commutative").**
`mc(k)=2^k−1`, so `u=(0,1,3,7,15,31,…)` and `comp_n=(2^{u²}−1)²`. Forcing a fixed polynomial:
`⟦r⟧(0)=comp_0=0 ⟹ a_0=0`; `⟦r⟧(1)=comp_1=1 ⟹` exactly one shape with `j₀≥1` positions,
`⟦r⟧(k)=k^{j₀}`; then `⟦r⟧(3)=3^{j₀}=comp_2=261121`, but `3^{11}=177147`, `3^{12}=531441` —
**not a power of 3. No `r` exists.** Robustness: `comp_n` has digit-count
`6,30,136,579,2390,9711,…` (quadruples each step ⟹ doubly-exponential in `n` ⟹ super-polynomial
in `u`), so **no polynomial of any degree** can fit. `P⁺` is affine *and* commutative, so the
"commutative+affine" heuristic is decisively **false**.

**`D` (FAILS, structural `computed`).** `D` is not polynomial (does not preserve connected
limits — `D(A×B)≠DA×DB`, joints ≠ product of marginals). The would-be reabsorption needs
`D((DX)²) ≅ Σ_c (DX)^{C_c}`; but the canonical `D(Y²)→(DY)²` (pair of marginals) is neither
injective (a joint is not determined by its marginals) nor an iso, and `D∘(−)²` is not a
coproduct of powers. `P⁺` is the exact finite shadow of this failure and settles it by
counting; `D` inherits the verdict structurally.

---

## 5. The honest criterion (what the computation forces)

> **CRITERION (computed).** `M-Cont` carries a composition `◁_M` with
> `⟦p◁_M q⟧_M ≅ ⟦p⟧_M∘⟦q⟧_M` (naturally) **iff `M` is a polynomial functor**. Then
> `p◁_M q = p ◁ ⌈M⌉ ◁ q`, which is **associative** and **non-unital** (monoidal only for `M=Id`).

- **Coproduct (shape) direction** — the operative one: `M` must be *re-expressible* as
  `Σ_i(−)^{B_i}` so that `M(Σ_t Z_t)` stays polynomial. This is exactly "`M` polynomial".
- **Power (position) direction** — free once `M` is polynomial (`M∘(−)^B` polynomial); needs
  no separate strength/commutativity condition.
- Affineness and commutativity are **orthogonal** to this: Maybe (non-affine) composes; `P⁺`,
  `D` (affine + commutative) do not. Those properties govern the *distributive law / Kleisli
  lift / update-monad* question, which is a different question that the sketch conflated in.

**Slogan.** *M-containers compose exactly when the effect `M` is itself shape-and-position
data (polynomial); probabilistic/powerset effects are too "quotient-y" to reabsorb.* Note the
neat independence from THM 2: **writer composes but is not full; `D` is full but does not
compose** — fullness (codensity) and composability (polynomiality) are genuinely different
invariants of `M`.

---

## 6. Grades

- `⟦p⟧_M∘⟦q⟧_M = G∘M`, `G=⟦p⟧∘M∘⟦q⟧` (structural identity): **`proved`** (one line from THM 1b).
- `M` polynomial ⟹ composes, with `p◁_M q = p◁⌈M⌉◁q`; associative; non-unital unless `M=Id`:
  **`proved`** (composition-closure of polynomial functors; associativity from `◁`).
- Maybe / exception / writer / reader **compose**; `P⁺`, `P` **fail**: **`computed`** (exact
  integer counting, `p=q=` squaring, ran clean).
- `D` **fails**: **`computed`** (structural — via non-polynomiality + the `P⁺` finite shadow;
  no direct count since `D(finite)` is infinite).
- General necessity "composes for ALL `p,q` ⟹ `M` polynomial": **`computed`** for the tested
  monads; a fully general ⟹ (every non-polynomial `M` fails the squaring test) is
  **`speculative`** pending a uniform argument — see gap below.
- "Commutative + affine" heuristic is the WRONG criterion: **`proved`** (`P⁺` refutes ⟸,
  Maybe refutes ⟹).

## 7. Gap for a full PROVE session

One clean lemma remains for the sharp `iff`: **for every non-polynomial monad `M`, the
squaring test fails** — i.e. `M∘(−)²` is never a coproduct of powers when `M` is not
polynomial. Route: use the Carboni–Johnstone / Weber characterisation ("`Set→Set` functor is
a coproduct of representables ⟺ preserves connected limits / wide pullbacks"); show
`M∘(−)²` polynomial forces `M` polynomial (precompose with the diagonal / a mono `X↪X²` and
use that polynomial functors are closed under the relevant restriction). That closes THM 3 to
`proved` and turns "polynomiality" into a full theorem, with the codensity story (THM 2) as
its exact sibling: **two different Kan/representability invariants of `M` — codensity for
fullness, polynomiality for composition.**

## Verification artifacts
`scratch/2026-09-05-thm3-compose-check.py` (exact integer test, ran clean): all polynomial
monads fit a fixed nonneg-int polynomial `P` (COMPOSE); `P⁺`, `P` admit no polynomial of any
degree (FAIL). Robustness note: `P⁺` composite digit-counts `6,30,136,579,2390,9711` grow
doubly-exponentially.
