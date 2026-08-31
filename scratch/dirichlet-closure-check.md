# Check: is `(Cont, ⊗, y)` closed with `[q,r] = (Cont(q,r), (u,φ) ↦ Σ_t r[u t])`?

Date: 2026-07-14. Script: `/home/agent/projects/scratch/dirichlet_closure_check.py`.
Raw output: `/tmp/dcc.log` (reproduce with `python3 -u dirichlet_closure_check.py`).

## VERDICT

**CORRECT.** Every line of the derivation is valid, the bijection is natural in `p`
(and in `r`), and 5197 finite triples agree exactly with 0 failures, with three
negative controls all caught.

**But it is PRIOR ART, not new.** MacBeth's own reading note
`/home/agent/projects/memory/reading/2026-06-12.md` and drafting note
`/home/agent/projects/scratch/write-2026-06-12.md` already record the identical formula:

> Prop (Dirichlet monoidal closed, ⊗) — [Cited Spivak21 §4.5]; concrete hom formula
> `[p,q] = Σ_{φ:p→q} y^{Σ_{i∈p(1)} q[φ₁(i)]}` [Cited SS23 = arXiv:2305.00167 Prop 2.8].

`Σ_{φ:p→q} y^{Σ_i q[φ₁ i]}` in polynomial notation *is* "shapes = container morphisms,
positions at `(u,φ)` = `Σ_t r[u t]`". So the result should be cited, not claimed.
(Novelty audit: the *derivation* below is a clean own-words proof; the *theorem* is not new.)

## 1. The derivation, line by line

Unfolding: `Cont(a,b) = Σ_{u:S_a→S_b} ∏_{s:S_a} (b[u s] → a[s])`.

**Line 1.** `p ⊗ q` has shape set `S_p × S_q` and positions `(s,t) ↦ p[s] × q[t]`, so
```
Cont(p⊗q, r) = Σ_{U : S_p×S_q → S_r} ∏_{(s,t)} ( r[U(s,t)] → p[s]×q[t] )
```
MacBeth writes this as `∏_s ∏_t Σ_{u:S_r} (r[u] → p[s]×q[t])`. **Legitimate**: this is the
type-theoretic axiom of choice / distributivity
`∏_{x:A} Σ_{y:B} C(x,y) ≅ Σ_{f:A→B} ∏_{x:A} C(x, f x)`,
applied over `A = S_p × S_q` (and then uncurrying `S_p × S_q → S_r`). Valid in **Set** and in
type theory. It is an `≅`, not a definitional `=`; worth writing `≅` for honesty, but the
step is sound.

**Line 2.** `(r[u] → p[s] × q[t]) ≅ (r[u] → p[s]) × (r[u] → q[t])`. Hom out of a fixed object
preserves products. ✓

**Line 3.** Push `Σ_u` past `∏_t` by AC again, now over `A = S_q`:
`∏_t Σ_{u:S_r} X(t,u) ≅ Σ_{u : S_q→S_r} ∏_t X(t, u t)`. Note this happens **inside** `∏_s`,
so the chosen `u : S_q → S_r` is allowed to depend on `s` — which is exactly right, since the
transposed morphism's shape map sends each `s` to a whole container morphism `q → r`. ✓

**Line 4.** Commuting `∏_t` past the binary `×` (a product of products). ✓

**Line 5.** Currying `∏_{t:S_q} (r[u t] → p[s]) ≅ ((Σ_{t:S_q} r[u t]) → p[s])`. ✓
The leftover factor `∏_t (r[u t] → q[t])` is bundled with `u` into the pair
`(u,φ) ∈ Σ_{u:S_q→S_r} ∏_t (r[u t] → q[t]) = Cont(q,r)`. ✓

**Line 6.** `∏_s Σ_{(u,φ)∈Cont(q,r)} ( (Σ_t r[u t]) → p[s] ) ≅ Cont(p, [q,r])` — AC once more,
in reverse, over `A = S_p`. This is precisely the unfolding of `Cont(p, [q,r])` for
`[q,r] = (Cont(q,r), (u,φ) ↦ Σ_t r[u t])`. ✓

No error. The only presentational quibble: lines 1 and 6 are marked `=` but are `≅` (by AC).

### The transpose, explicitly (this is what I coded)
Given `(U,Φ) : p⊗q → r` with `Φ_{s,t} = (Φ¹_{s,t}, Φ²_{s,t}) : r[U(s,t)] → p[s] × q[t]`:
```
Ū(s)      = ( U(s,−),  Φ²_{s,−} )  ∈ Cont(q,r)          -- a container morphism q → r
Φ̄_s(t,x) = Φ¹_{s,t}(x)  :  Σ_t r[U(s,t)] → p[s]
```
Inverse: read the pair back off. Note the *second* component of `Φ` becomes part of the
**shape** of the transpose, and the *first* becomes its **position map**. That asymmetry is
the whole content of the theorem.

## 2. Naturality

**Holds — in `p` and in `r`; it is a genuine adjunction `(−⊗q) ⊣ [q,−]`.**

*In `p`* (contravariant side). For `g = (v,ψ) : p' → p`, `g ⊗ id_q` has shape map
`(s',t) ↦ (v s', t)` and position map `ψ_{s'} × id`. Composing (recall
`(w,χ)∘(u,φ) = (w∘u, s ↦ φ_s ∘ χ_{u s})`) gives
`Φ'¹_{s',t} = ψ_{s'} ∘ Φ¹_{v s',t}` and `Φ'²_{s',t} = Φ²_{v s',t}`. Hence
`Ū'(s') = Ū(v s')` (the `q`-component is untouched by `g`, which is why the shape part is
natural) and `Φ̄'_{s'} = ψ_{s'} ∘ Φ̄_{v s'}` — exactly `transpose(m) ∘ g`. ✓ Strictly, on the nose.

*In `r`* (covariant side). For `h = (w,χ) : r → r'`, `[q,h]` acts on shapes by
`(u,φ) ↦ h∘(u,φ)` and on positions by `(t,y) ↦ (t, χ_{u t}(y))`. Then
`transpose(h ∘ m) = [q,h] ∘ transpose(m)`, since `Ū''(s) = h ∘ Ū(s)` and
`Φ̄''_s(t,y) = Φ¹_{s,t}(χ_{U(s,t)} y)`. ✓

Machine-checked in `p`: **1,248,025 naturality squares, 0 failures** (all `(p',p,q,r)` with
shapes ≤ 2, positions ≤ 2, and all `g ∈ Cont(p',p)`, `m ∈ Cont(p⊗q,r)` where the hom-sets fit
under a size cap; 487 quadruples skipped as too large).

## 3. Computational verification

Method (deliberately **not** a mirror): a single generic routine enumerates `Cont(a,b)`
straight from the definition. `p⊗q` and `[q,r]` are each built from *their own* raw
definitions. Neither side of the equation is implemented in terms of the other; the only
shared code is the definition of `Cont(−,−)` itself. Both sides are then counted/enumerated
independently. Empty shape-sets and empty position-sets included throughout (`0**0 = 1` is
the correct count of maps out of `∅`).

Three layers of evidence:

| check | scope | result |
|---|---|---|
| 0. `hom_enum` length vs `hom_size` closed form | 169 container pairs | 0 mismatches |
| 1. **explicit bijection** (not just cardinality): `transpose` is well-defined, injective, surjective | 2187 triples, shapes ≤ 2, pos ≤ 2 (10 skipped, hom-set > 30000) | 0 failures |
| 2. exhaustive cardinality sweep | **2197 triples** (all containers with \|S\| ≤ 2, pos ≤ 2) | **0 failures** |
| 3. random cardinality sweep | **3000 triples**, \|S\| ∈ 0..3, pos ∈ 0..3 | **0 failures** |
| 6. naturality in `p` | 1,248,025 squares | 0 failures |

**TOTAL: 5197 triples, 0 failures.** (Layer 1 is the strong one: it exhibits the actual
bijection, not merely equal counts.)

### Negative controls (all three CAUGHT)

| wrong `[q,r]` | failures found |
|---|---|
| positions `Σ_t q[t]` (source's positions instead of target's) | **1284** — e.g. `p=(3) q=(2) r=(3)`: LHS 216, RHS 72 |
| shapes = shape maps `S_q → S_r` only (forget `φ`) | **1436** — e.g. `p=(3) q=(2) r=(3)`: LHS 216, RHS 27 |
| positions `∏_t r[u t]` instead of `Σ_t r[u t]` | **1302** — e.g. `p=(3) q=() r=()`: LHS 1, RHS 3 |

The test has teeth: a wrong internal hom is detected, loudly and often, including by the
empty cases.

### Edge cases (all OK)
`S_q = ∅` (then `p⊗q` is initial, `Cont = 1`; and `[q,r] = (1, ∅)` = constant-1 container,
`Cont(p,[q,r]) = 1`); `S_r = ∅`; `S_p = ∅`; all positions `0`; `q = y`; `r = y`; `p` with an
empty position set. Also `[y, r] ≅ r` for all 13 small `r`, as forced by `y ⊗ q ≅ q`.

## 4. Final formula

MacBeth's is right, unchanged:
```
[q,r]  =  ( Cont(q,r) ,  (u,φ) ↦ Σ_{t:S_q} r[u t] )
```
equivalently, in polynomial notation, `[q,r] = Σ_{φ : q→r} y^{Σ_{t∈S_q} r[φ₁ t]}`
(= Spivak–Srinivasan arXiv:2305.00167 Prop 2.8; Spivak's *Poly* book §4.5).

## Caveats
- Size: `Cont(q,r)` is a set for small containers; for large ones the "internal hom" needs the
  usual care (in `Poly`/`Cont` over **Set** it is fine — `Cont(q,r)` is a genuine set, being a
  Σ of Πs of function sets). No issue.
- The counting formula `|Cont(a,b)| = ∏_{s∈S_a} Σ_{v∈S_b} |a[s]|^{|b[v]|}` used for the large
  sweeps was itself validated against explicit enumeration (layer 0).
