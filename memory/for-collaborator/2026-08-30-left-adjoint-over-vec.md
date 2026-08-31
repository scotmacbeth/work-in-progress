# For Neil / Robin — the `◁`-coclosure off `Set`: three verdicts, two of them against my own brief

**MacBeth, 2026-08-30 (second PROVE session of the day).**
Full proof: `proofs/2026-08-30-left-adjoint-over-vec.md`. Registry `left-adjoint-over-vec`
(validates, `proved`). Code: `scratch/left-adjoint-vec/verify.py`.

## The question

This morning I proved that over `Set` the endofunctor `L_q = (−)◁q` has a left adjoint for every
container `q=(T,Q)` — which is Meyers' `◁`-coclosure, Niu–Spivak Prop 6.57, known. I isolated the
single step using distributivity of `Set` and predicted that over `Fam(Vec^op)` it would die and be
replaced by the *summability* gate that already appears in T2(B), T4-left Thm 3.1(2) and clause (C)
of `fibredness-vs-left-closure`. That would have been a fourth occurrence of the same gate, and the
first on the left-adjoint side.

**Both halves of the prediction are wrong, and the corrections are worth more than the prediction
was.**

## 1. The gate is `|T| = 1`, not summability

Wherever `◁` collapses to `⊗` (positions tiny — T4 Prop 2.1 — or `T` finite over an additive base,
which is a small new lemma), `(−)◁q` has a left adjoint **iff `q` is a monomial**. Two independent
proofs of necessity:

* a right adjoint preserves the terminal object, and `1 = ⟨0⟩` while `1◁q = (T,0)`;
* a right adjoint preserves binary products, and `(p×p')⊗q` lives over `S×S'×T` while
  `(p⊗q)×(p'⊗q)` lives over `S×T×S'×T` — forcing `|T|=|T|²`. This one uses no zero object.

The obstruction bites at **`dim P_s = 1` with `|T| = 2`**, both finite, where summability is
automatic. At that point the two sides of the comparison map even have the **same cardinality**
(4 and 4 over `F_2`) — the map is simply not a bijection: it double-counts the zero map and misses
`e_0 + e_1`. *I want to flag that a cardinality-only check would have passed this instance.* Over
`Vec_fd`, left-adjointness (`|T|=1`) **strictly implies** the closure/summability condition, so the
two conditions are ordered, not independent.

## 2. The load-bearing hypothesis was misidentified — it is CONNECTEDNESS OF THE UNIT (T1's condition)

This is the part I would most like your eyes on. The step `(†)` I singled out is genuine
`Set`-distributivity, but the adjunction does not need it. Here is the whole proof, over an
arbitrary closed symmetric monoidal cocomplete base, writing `p◁q = (D,N)` and using only that
`C(I,−)` preserves coproducts:

```
Fam(r, p◁q) = ∏_ρ ∐_d C(N_d,U_ρ) = ∏_ρ ∐_d C(I,[N_d,U_ρ])
            = ∏_ρ C(I, ∐_d[N_d,U_ρ]) = ∏_ρ C(I, ⟦p⟧⟦q⟧U_ρ) = ∏_ρ C(I, ∐_s[P_s,⟦q⟧U_ρ])
            = ∏_ρ ∐_s C(P_s, ⟦q⟧U_ρ) = Fam( (R, ⟦q⟧U_ρ), p ).
```

`γ` used twice and nothing else — no distributivity, and no choice of presentation for `◁`. And `γ`
is *verbatim* the comparison map of T1 (`⟦−⟧` full and faithful ⟺ `I` connected).

> **T1 and the `◁`-coclosure are the same lemma applied twice.** One condition, two theorems.

Two consequences. (i) Distributivity of `Set` is what makes `Σ_s T^{P_s}` the correct shape set of
`p◁q` — it belongs to the *construction* of `◁`, not to the adjunction. (ii) **Extensivity is not
the invariant on the left side**: `Set×Set` is lextensive with a disconnected unit. So the standing
slogan "extensivity fuses the seams" needs a caveat wherever the statement concerns `⟦−⟧` or the
left adjoint; unit-connectedness is strictly finer and is the honest invariant.

**Novelty gate is OPEN on this general-base statement.** The `Set` case is Meyers/Niu–Spivak, gate
closed. (⚠ 2026-08-31: any DJN comparison here has to name *which* `◁` — their composition product
is weighted, `∏_a∏_b(u_{i,a}·v_{ja,b})`, Def 3.5/Lemma 3.6 p. 89, and coincides with mine only at
`C=1`; their `⊗` does coincide with mine.)
Whether "connected unit ⟹ `◁`-coclosure over any base" is in DJN `2305.05655` or the
enriched-container literature I have **not** checked — please treat it as unclaimed.

## 3. p.r.a. and left-adjointness come apart off `Set`

The caveat I flagged in advance fired. `Vec` has a **zero object**, so `1 = ⟨0⟩` and
`1◁q = (T,0) ≇ 1` when `|T| ≥ 2`; Weber's slice does not collapse. But it does not need to:
`Fam/(T,0) ≅ ∏_{t∈T}Fam(C^op)`, `(L_q)_1 p = (p⊗Q_t)_t`, whose left adjoint is
`(r_t)_t ↦ ∐_t F_{Q_t}(r_t)`. So

> `L_q` is a parametric right adjoint for **every** `q` over `Vec` as well, while having an honest
> left adjoint only for `|T|=1`.

This morning's "p.r.a. ⟺ has a left adjoint" was **base-specific**; the responsible feature is that
`Set` has no zero object, and the exact measure of the gap is the object `1◁q`. It *strengthens*
this morning's refutation of the Weber re-filing: p.r.a. of `L_q` holds on both bases for every `q`,
so it discriminates nothing anywhere, while the probe conditions separate on both.

## What I think the actual crown is

| | left adjoint to `L_q` | right adjoint (`◁`-closure) |
|---|---|---|
| `Fam(Set^op)` | always | iff `\|T\|=1` |
| `Fam(Vec_fd^op)` | iff `\|T\|=1` | iff `#{t : Q_t≠0} < ∞` |

The conditions **swap sides**. And placing it in the `(V) ⊊ (C) ⊊ (F)` chain of
`fibredness-vs-left-closure`: over `Vec_fd`, left-adjointness ⟺ **verticality (V)**, the bottom
rung; over `Set`, `(V)=(C)=(F)={|T|=1}` and left-adjointness is unconditional above all three. **The
chain inverts end to end when you change base.**

Two smaller things I would not want lost:

* **The empty product is the binding probe.** For `q = (ℕ, k)` over `Vec_fd`, `L_q` preserves *all
  binary products* (`ℕ ≅ ℕ²`, and the positions do not depend on `t`) but fails to preserve the
  terminal object. The binary-product argument is genuinely inconclusive there.
* **`◁` does not exist over `Set×Set`.** `⟦E,N⟧(1_C) = E·1_C` is a copower of the terminal object,
  hence diagonal, but `⟦p⟧(T·1_C) = (T^A,T^B)` is not, for `p=⟨(1,2)⟩`, `|T|=2`. So the base I
  wanted as a separator for the converse to Theorem 1 is unavailable. `Set` and `Vec` both pass the
  criterion, for *opposite degenerate* reasons: `1_C` is a generator, versus `1_C = 0`. **Caveat:
  this is about my external `Fam(C^op)`; DJN may work in an indexed setting where it does not
  arise, and I have not read them closely enough to say.**

## Standing caveat

`◁ := ⊗` on the collapse locus is a **definition**, not a deduction: over `Vec`, `⟦−⟧` is not
faithful (T1's honest correction #2), so `(T,0)` and `({∗},0)` present the same constant-`0`
functor and `⟦p◁q⟧ = ⟦p⟧⟦q⟧` does not pin `p◁q` down. The binary-product necessity proof is
independent of the convention for finite `T`; the terminal-object one is not.

## Open, in priority order

1. Is unit-connectedness **necessary**? Prop 9.1 removed the obvious separator base; it may be open
   only vacuously.
2. Novelty gate on Theorem 1's general-base form (DJN, Shapiro–Spivak, enriched containers).
3. `◁` on `Fam(Vec^op)` for infinite `T` and non-tiny positions — still undefined (T4-left Gap 2).
4. Naturality of `F_q` in `q` — unchecked in both sessions.
