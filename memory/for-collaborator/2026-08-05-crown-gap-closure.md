# Crown stratification: both computed children closed (for Neil / Robin)

**MacBeth, 2026-08-05 (heartbeat-3).** Follow-up to the crown refutation. The two remaining
`computed` joints of the strict 4-level chain are now **proved** and validator-clean.
Full write-up: `proofs/2026-08-05-crown-gap-closure.md`. Harness:
`scratch/fibrational-crown/gap_closure.py`.

## What was open
The refutation (that the fibrational "crown TFAE" is a *strict* chain
`writer ⊊ writer+exc ⊊ cartesian ⊊ polynomial`, only `(4)⟺(5)` a biconditional) stood on
explicit splitters, but two supporting implications were only computed:
1. **(1)⟺(2)** — `T_M` preserves cartesian morphisms iff `M` is a cartesian monad.
2. **(3)⟹(5)** — `λ`-invertibility ⟹ non-branching, at arity ≥2.

## Theorem 1 (the `T_M`-mirror of your `G_M` fact)
`T_M(u,f)`'s backward map at `m` is `(∏_b f_{x_b})∘(u_*)^*`: the cartesian bijections `f`
applied leafwise, **after reindexing the product along the leaf-tracking map**
`u_*:lv(m)→lv(Mu\,m)`. So it is a bijection **iff `u_*` is** (product-reindexing lemma).
That is precisely the shadow of your Lean `onMor_cartesian`: `G_M` reindexes along the
identity of a single fibre (always iso), `T_M` reindexes along `u_*` — which `M` may
collapse. Hence **(1) ⟺ cartFun** (M polynomial), cleanly, with a pullback square.

The monad half: cartFun + ∏-Mendler ⟹ cartesian monad, because the support comparison
`κ_μ:I ↠ lv(μ\,mm)` is **surjective** by parametricity (no leaf created) and **injective**
because cartFun makes labels *free* while `κ_μ` is label-preserving — so a merge would put
two distinct labels on one leaf. **The whole role of the ∏-Mendler hypothesis is to exclude
Reader/State**: Reader is a polynomial functor (cartFun ✓) whose `μ`=diagonal is *not*
cartesian — the honest general witness that **(1)≠(2)**. It is thrown out by the missing
`i_P` (its unit shape has `K` leaves, not 1). So "(1)⟺(2)" is genuinely a ∏-Mendler
statement, not a universal one — worth a sentence in the book.

## Theorem 2 (cleaner than my own sketch)
Forget the cross-term computation. One line does it: `str(w)=(Mπ_b\,w)_b` has **every
component of the same shape** `M!(w)` (since `!∘π_b=!`). So at arity `k≥2`, any codomain
tuple with two *different* component-shapes is outside the image — `str` is **not
surjective** as soon as `|M1|≥2`. And `|M1|≥2` is automatic: the unit shape has 1 leaf
(`i_P`), the offending shape has `k≥2`, so they differ. Therefore (3) ⟹ no arity ≥2.
Reader survives (3) only because `|M1|=1` — and that is exactly the non-∏-Mendler case.

Corollary, pinning the top level: (3) ⟺ arity ≡ 1 ⟺ **pure writer `A×(−)`**, strictly
inside non-branching `E+A×(−)`.

## Status
Registry `effect-coeffect-arrows.json`: `crown-tfae-splits-strict-chain` proved;
`crown-boundary-table` and `lambda-inv-implies-nonbranching-general` **now proved**;
`trustcheck` OK. No gaps remain at these joints. The book/grant stratification is now
fully load-bearing. Natural next Lean target: `u_*`-reindexing bijection ⟹ (1)⟺cartFun,
which would sit right next to `FibredTransfer.onMor_cartesian` as its `T_M`-dual.
