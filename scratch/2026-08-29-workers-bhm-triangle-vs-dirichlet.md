# Workers ⊗-grading vs BHM ▷-grading on the ΔS family

**Date:** 2026-08-29 · **Grade:** computed · **Verdict:** REFUTED (with a canonical retract; nuance below)

## Setup

- State polynomial: `ΔS(X) = Σ_{s∈S} X^S = S·X^S`. Shapes `S`, each with position set `S`.
- Composition product: `(p ▷ q)(X) = p(q(X))`.
- Dirichlet/Day tensor: `(p⊗q)` has shapes `S_p×S_q`, positions `P_s×Q_t`.
- BHM (ACT 2026) grade Poly's composition product as a graded monad `T_P(X)=X▷P`; grades compose by `▷`.
- Workers (MacBeth, proved) form a `(Set,×)`-graded category, grades compose by `⊗` with `ΔS⊗ΔT ≅ Δ(S×T)`.

**Conjecture under test:** Workers' `ΔS`-grading is the `P=ΔS` fibre of BHM's `▷`-grading, i.e. `ΔS ▷ ΔT ≅ ΔS ⊗ ΔT = Δ(S×T)`.

## 1. General `p ▷ ΔS`

Let `p = Σ_i y^{A_i}`. Then `ΔS(X) = S·X^S`, and

```
(p ▷ ΔS)(X) = p(ΔS(X)) = Σ_i (ΔS(X))^{A_i}
            = Σ_i (S·X^S)^{A_i}
            = Σ_i (functions A_i → S·X^S)
            = Σ_i S^{A_i} × (X^S)^{A_i}
            = Σ_i Σ_{f: A_i→S} X^{S×A_i}.
```

So shapes are pairs `(i, f)` with `f: A_i→S` — that is, `S^{A_i}` shapes for each original shape `i` — and every such shape carries position set `S×A_i`. **This matches the target shape in the task statement.** Note the shape count *blows up* by a factor `S^{A_i}`: composition with `ΔS` is not shape-preserving.

## 2. `ΔS ▷ ΔT` explicitly

`ΔT(X) = T·X^T`. Then

```
(ΔS ▷ ΔT)(X) = ΔS(ΔT(X)) = S·(ΔT(X))^S = S·(T·X^T)^S
             = S × T^S × (X^T)^S
             = S × T^S × X^{T×S}
             = Σ_{s∈S} Σ_{g: S→T} X^{T×S}.
```

- **Shapes:** `S × T^S`, indexed by `(s, g)` with `s∈S`, `g:S→T`. Count `= |S|·|T|^{|S|}`.
- **Positions:** `T×S` for every shape. Count `= |T|·|S|`.

Compare `Δ(S×T)(X) = Σ_{(s,t)∈S×T} X^{S×T}`:
- **Shapes:** `S×T`, count `|S|·|T|`.
- **Positions:** `S×T`, count `|S|·|T|`.

**Position sets agree** (both `S×T`, up to swap iso). **Shape sets do NOT agree**: `S×T^S` vs `S×T`. Equal only when `|T|^{|S|}=|T|`, i.e. `|S|=1` or `|T|≤1` (degenerate).

## 3. Small case |S|=|T|=2 (concrete counts)

| Polynomial | shape count | position set size (each shape) |
|---|---|---|
| `ΔS ▷ ΔT` | `|S|·|T|^{|S|} = 2·2² = ` **8** | `|T|·|S| = ` **4** |
| `ΔS ⊗ ΔT` | `|S|·|T| = ` **4** | `|S|·|T| = ` **4** |
| `Δ(S×T)`   | `|S×T| = ` **4** | `|S×T| = ` **4** |

- `ΔS ⊗ ΔT = Δ(S×T)`: **4 shapes, each `y⁴`** — literally equal. ✓ (This is Workers' proved fact.)
- `ΔS ▷ ΔT`: **8 shapes, each `y⁴`** — a *different, larger* polynomial (`8·y⁴` vs `4·y⁴`).

So on the ΔS family, **`▷ ≠ ⊗`**. The composition product doubles the shape count here (in general multiplies shapes by `|T|^{|S|-1}`).

## 4. The canonical relating map (why it's not a random miss)

There is a canonical retract `Δ(S×T) ◁— ΔS▷ΔT` (poly morphism = forward on shapes, backward on positions):

- **Section** (inclusion) `Δ(S×T) → ΔS▷ΔT`: on shapes `(s,t) ↦ (s, const_t)` (constant `g≡t`); on positions the iso `T×S ≅ S×T`.
- **Retraction** (evaluation) `ΔS▷ΔT → Δ(S×T)`: on shapes `(s,g) ↦ (s, g(s))` (evaluate `g` at its own `s`); on positions the iso `S×T ≅ T×S`.

Composite `retraction ∘ section = id`: `(s,t) ↦ (s,const_t) ↦ (s, const_t(s)) = (s,t)`. ✓

So `Δ(S×T) = ΔS⊗ΔT` sits inside `ΔS▷ΔT` as a canonical retract — the "diagonal/evaluation" copy. This is exactly the store-comonad phenomenon: `ΔS` is the costate comonad carrier, whose comultiplication `ΔS → ΔS▷ΔS` is NOT invertible precisely because `▷` grows shapes.

## Verdict: (b) REFUTED — different monoidal products — with a clean (c)-flavoured relating map

The conjecture as literally stated is **false**. BHM grade by the **composition product `▷`**; Workers grade by the **Dirichlet tensor `⊗`**. On the ΔS family these genuinely differ: at `|S|=|T|=2`, `ΔS▷ΔT = 8·y⁴` while `ΔS⊗ΔT = Δ(S×T) = 4·y⁴`. The shape counts (8 vs 4) are unequal, so `ΔS⊗ΔT` is *not* the `P=ΔS` fibre of `X↦X▷ΔS`. Workers' grading monoid `(ΔS, ⊗, Δ(S×T))` is a **distinct** monoidal structure from BHM's `(P, ▷)`-grading.

This is the *more interesting* outcome: it lets MacBeth draw a sharp distinction rather than claim a citation subsumption. The honest refinement (the (c) part) is that the two are not unrelated — `Δ(S×T) = ΔS⊗ΔT` is a **canonical retract** of `ΔS▷ΔT` via the constant-inclusion / self-evaluation pair, reflecting that `⊗` on `ΔS` is the "diagonal" collapse of the shape-blowup that `▷` produces. So: **Workers' ⊗-grading is a retract of, not a fibre of, BHM's ▷-grading.** That retract is the precise, publishable relationship.
