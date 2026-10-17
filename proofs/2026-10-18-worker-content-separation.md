# Worker vs. weld content: the Σ-index separation (rework of clauses 2 & 3)

**MacBeth — PROVE session 2026-10-18**
Reworks the two demoted clauses of `2026-10-16-weld-is-regular-bicomodule.md` per Rick's referee
report uid231 (M1, M2, M3). The clause‑(1) core (`B` is the regular `(ΔT,ΔS)`‑bicomodule,
`F̄_B(V)=(T×V)^S=T^S·V^S`) is **peer‑reviewed** and is used here as an input, not re‑litigated.
Companion computation: `scratch/2026-10-18-worker-content-separation.py` (all checks pass).

---

## 0. Setting and what is being reworked

`S,T` finite nonempty sets; store comonoids `ΔS=S·y^S`, `ΔT=T·y^T` in `(Poly,◁,y)` (indiscrete
categories `I(S),I(T)`). The weld `B=ΔS◁ΔT`, the worker `A=ΔS⊗ΔT=Δ(S×T)`. Work in the collapse
`ΔS-Set≃Set`, `ΔT-Set≃Set` (both indiscrete, nonempty), under which the represented prafunctor of a
store‑bicomodule becomes an endofunctor `F̄` of `Set`.

**Peer‑reviewed input (Thm 3.1, Rick‑endorsed at 7 shapes).**
`F̄_B(V) = (T×V)^S = Σ_{g∈T^S} V^S`. As a polynomial endofunctor, `F̄_B = T^S·y^S`: **Σ‑index**
(= `F̄_B(1)`) the branch‑map set `T^S=Hom(S,T)`, **content power** `(−)^S` (directions `S`).

**What Rick demoted and why.**

- **M1 (clause 2, "worker = content FALSE").** The old argument compared `B` under a *nontrivial*
  right `ΔT`‑coaction against `A` under *no* right coaction (the `y`‑reading), concluding
  "content exponent `S` vs `A`‑exponent `S×T`, differ when `|T|≥2`." That is an **inconsistent
  comparison**: it would force worker ≠ content already at `|S|=1,|T|≥2`, where in fact
  `B=A=ΔT` on the nose. Under a consistent reading the exponents agree; the surviving separation
  is a **Σ‑index** phenomenon on the locus `|S|≥2 ∧ |T|≥2`.
- **M2 (clause 3, "discarded = Σ‑tail TRUE").** "`T^S` = precisely the non‑constant maps" is
  self‑contradictory: at `(2,3)`, `|T^S|=9` but there are only `6` non‑constant maps. Per position
  `s`, the retract forgets `g|_{S∖{s}}` (a fibre `T^{|S|−1}`), not "the non‑constant maps."
- **M3 (§5 σ‑display).** Two `S`'s conflated; correct form `σ(A)` = the sub‑bicomodule on
  `{(s,const_t)}`, `σ♯=id_{S×T}`, prafunctor `T×V^S`.

All three are **one** phenomenon, which this note isolates.

---

## 1. The worker as a consistent `(ΔT,ΔS)`-bicomodule: the constant-branch sub-bicomodule

The type error at the root of Conjecture 5.1 is that the worker `A=Δ(S×T)` is a priori a *0‑cell*
(a comonoid/category), while the weld content is a *1‑cell* (`ΔT→ΔS`). To compare them we must read
`A` as a `(ΔT,ΔS)`-bicomodule of the **same variance** as `B` — this is exactly the "consistent
reading" M1 demands. There is a canonical such structure, and it sits visibly inside `B`.

> **Definition 1.1 (constant-branch slice).** Let `B' ⊆ B` be the subset of positions whose branch
> map is constant: in the position description `B(X)=Σ_{(s,g)} X^{S×T}` with `g∈T^S`, take
> `B' = { (s,g) : g ∈ const(T) }`, where `const:T↪T^S`, `t↦const_t`. Directions are inherited
> (`S×T` per position). As a polynomial, `B'` has positions `S×const(T)≅S×T` and directions `S×T`,
> i.e. **`B' = (S×T)·y^{S×T} = Δ(S×T) = A`** on the nose.

> **Lemma 1.2 (`B'` is a sub-bicomodule).** `B'` is closed under the weld coactions
> `λ=δ_{ΔS}◁ΔT : B→ΔS◁B` and `ρ=ΔS◁δ_{ΔT} : B→B◁ΔT`; hence `(B',λ|,ρ|)` is a
> `(ΔT,ΔS)`-sub-bicomodule of `B`.

*Proof.* Both coactions leave the branch‑map coordinate `g=(t_s)_{s∈S}` **pointwise unchanged**,
only duplicating/reorganising positions:

- `ρ=ΔS◁δ_{ΔT}` applies `δ_{ΔT}` inside each of the `S` slots: `δ_T(t,ψ)=(t, j↦(j,ψ))` keeps the
  first coordinate `t`. So the `B`-layer of `ρ(s,g)` has the *same* `g`. If `g` is constant it stays
  constant.
- `λ=δ_{ΔS}` duplicates the whole `ΔT`-ground: `δ_S(s,φ)=(s, i↦(i,φ))`, and every inner `B`-copy is
  `(i,φ)` with the *same* `φ`, hence the same `g`. Constant stays constant.

The counit and (co)associativity laws restrict because they are the comonoid laws of `ΔS,ΔT`
whiskered, and `B'` is a full sub‑on‑positions with inherited directions. Machine‑checked
(`ρ`‑closed, `λ`‑closed) at `(|S|,|T|)∈{(2,2),(2,3),(3,2),(1,2),(2,1)}`. ∎

> **Definition/Proposition 1.3 (the worker's canonical reading, fixing M3).** The map
> `σ:A→B`, `σ_1(s,t)=(s,const_t)` on positions and `σ♯=id_{S×T}` on directions, is an isomorphism of
> `(ΔT,ΔS)`-bicomodules `A ≅ B'`. Equivalently, `A` carries the `(ΔT,ΔS)`-bicomodule structure
> obtained by cobase change of the regular `(A,A)`-bicomodule along the comonoid projections
> `π_S:A→ΔS` (left) and `π_T:A→ΔT` (right) — the indiscrete functors `I(S×T)→I(S), I(T)` induced by
> the set projections — and this structure coincides with `B'`.

*Proof.* `σ_1` is the bijection `S×T ≅ S×const(T)` = `B'`-positions, and `σ♯=id_{S×T}` matches
directions; since (Lemma 1.2) the coactions act on `B'` exactly as they do on `A` under this
identification (both leave the `g`-value alone), `σ` commutes with `λ,ρ` and is a bicomodule iso.
`σ_1` injective with `σ♯=id` ⟹ iso onto image `B'`. Position bijection `|S×T|=|B'|=n·m`
machine‑checked at the five shapes. (This is M3's corrected display: `σ(A)=`sub‑bicomodule on
`{(s,const_t)}`, `σ♯=id_{S×T}`.) ∎

---

## 2. Clause (2), corrected: worker vs. content is a Σ-index separation (M1)

> **Theorem 2.1 (corrected comparison).** Read `A` and `B` as `(ΔT,ΔS)`-bicomodules via §1
> (`A≅B'⊆B`). Then
> ```
>    F̄_B(V) = Σ_{g∈T^S}     V^S  = T^S · V^S ,
>    F̄_A(V) = Σ_{g∈const(T)} V^S  = T  · V^S .
> ```
> Both have the **same content power `(−)^S`** (directions `S`); they differ **only** in the
> Σ‑aggregation index, `T^S` (all branch maps) for the weld versus `T≅const(T)` (constant branch
> maps) for the worker. Consequently `F̄_A` is a sub‑prafunctor of `F̄_B`, with
> `F̄_A ≅ F̄_B` **iff `|S|=1` or `|T|=1`**, and a *proper* inclusion exactly on `|S|≥2 ∧ |T|≥2`.

*Proof.* `F̄_B=Σ_{g∈T^S}V^S` is the peer‑reviewed Thm 3.1; its Σ‑index is the set of `B`-positions
modulo the left `ΔS`-collapse, which is exactly `T^S` (the `g`'s; the `S`-head is killed by
indiscreteness), and the content exponent is the surviving direction `S` (the `T`-direction is
killed by the right `ΔT`-collapse). `A≅B'` (Prop 1.3) is `B` restricted on positions to
`const(T)⊆T^S` with directions unchanged; the same recipe therefore restricts the Σ‑index to
`const(T)` and leaves the content power `(−)^S` untouched, giving `F̄_A=Σ_{t∈T}V^S=T·V^S`.

Equality of the two functors for all `V` is equality of polynomials `T^S·y^S` and `T·y^S`, i.e.
`|T^S|=|T|`, i.e. `m^n=m`, i.e. (for `n,m≥1`) `n=1` or `m=1`. Otherwise `T⊊T^S` and the inclusion
`F̄_A↪F̄_B` is proper. ∎

**What this fixes (M1).** The exponents **agree** — both content powers are `(−)^S`. The old proof's
"`S` vs `S×T`" was the artefact of reading `A` *without* the right `ΔT`-coaction: with the coaction
(consistent with `B`), the `T`-directions of `A` collapse to the exponent `S`, not `S×T`. The true,
consistent separation is the **Σ‑index `T` vs `T^S`**, nonzero precisely where non‑constant branch
maps exist, i.e. **`|S|≥2 ∧ |T|≥2`**.

**At `|S|=1` (the case the old argument got wrong).** `T^S=T^1=T`, so `const(T)=T^S` and
`F̄_A=F̄_B=T·V`; moreover the carriers coincide, `B=ΔS◁ΔT=y◁ΔT=ΔT=Δ(1×T)=A`. **Worker = content**,
on the nose. The FALSE verdict must *not* be claimed here.

**Verdict for Conjecture 5.1 clause (2).** The identification "worker `A` = right‑adjoint content
factor `F/1` of the weld" is **FALSE on `|S|≥2 ∧ |T|≥2`** — but by a Σ‑index mismatch, not an
exponent mismatch — and **TRUE (worker = content, indeed `A=B`) when `|S|=1` or `|T|=1`**.
The content *power* `(−)^S` is in fact *shared* by worker and weld; what the worker fails to be is
the whole prafunctor, because it aggregates over only the constant branch maps.

**Witnesses (machine‑checked).** At `(|S|,|T|)=(2,2)`, `V=2`: `F̄_A=2·2^2=8`, `F̄_B=(2·2)^2=16`
(proper). At `(1,2)`: `F̄_A=F̄_B=4`; at `(1,3)`: `F̄_A=F̄_B=6` (equal). These are exactly the points
where MacBeth's old criterion (`|T|≥2`) and Rick's corrected criterion (`|S|≥2∧|T|≥2`) disagree —
and the computation sides with Rick.

---

## 3. Clause (3), restated and re-decided: what the retract forgets (M2)

Restate the Σ‑tail honestly. The weld's Σ‑aggregation index is the **full** branch‑map set, which
splits as
```
    T^S  =  const(T)  ⊔  NC ,     |const(T)| = m,   |NC| = m^n − m   (NC = non-constant maps).
```
The retract/idempotent of the workers theorem is `e : S×T^S → S×T^S`,
`e(s,g) = (s, const_{g(s)})` (collapse each branch map to the constant at its self‑evaluation).

> **Theorem 3.1 (the retract's keep/discard, corrected).** `e` is idempotent with image
> `S×const(T) ≅ S×T` (the worker positions `=σ(A)`). For each current input `s`, `e` **keeps** the
> value `g(s)∈T` (one `T`-coordinate, the diagonal) and **discards** the restriction
> `g|_{S∖{s}} ∈ T^{S∖{s}}`, a fibre of size `|T|^{|S|−1}=m^{n−1}`. Concretely the fibre of `e` over
> `(s,const_t)` is `{ g : g(s)=t } ≅ T^{S∖{s}}`.

*Proof.* `e∘e=e` since `const_{g(s)}` evaluated at `s` is `g(s)`. The image is `{(s,const_t)}`,
i.e. the constant slice. Two maps `g,g'` have `e(s,g)=e(s,g')` iff `g(s)=g'(s)`; fixing `g(s)=t`
leaves `S∖{s}` free, so the fibre is `T^{S∖{s}}`, of size `m^{n−1}`. Idempotency, image = constant
slice, and all fibre sizes `=m^{n−1}` machine‑checked at `(2,2),(2,3),(3,2),(1,2),(2,1)`. ∎

> **Re-decision of "discarded data = the Σ-aggregation tail (branch maps)".**
> As originally stated — "the discarded data is precisely the non‑constant branch maps, and that is
> the `Σ`-tail" — the claim is **FALSE**, for three independent reasons:
>
> 1. The `Σ`-tail index is **all** of `T^S = const(T)⊔NC`, not `NC`. "`T^S` = the non‑constant maps"
>    is a cardinality contradiction (`m^n ≠ m^n−m` for `m≥1`).
> 2. What `e` forgets per position is the fibre `T^{S∖{s}}` of size `m^{n−1}` — **neither** `NC`
>    (`m^n−m`) **nor** `T^S` (`m^n`). At `(2,3)`: `3` vs `6` vs `9`, all distinct (machine‑checked).
> 3. The fibre `{g:g(s)=t}` is not "the non‑constant maps": it contains one constant map
>    (`const_t`) and omits every non‑constant `g` with `g(s)≠t`.
>
> The **TRUE** residue (the corrected picture): the weld's Σ‑tail **is** the full branch‑map set
> `T^S=Hom(S,T)` — that half of the old clause stands — and the retract `e` realises the projection
> of this index onto the worker's constant slice `const(T)≅T` by "evaluate at the current input,
> then make constant." The genuinely discarded structure is, per position, the off‑diagonal
> dependence `g|_{S∖{s}}` (precisely as the workers paper's own body states: *"discards the branch
> map's dependence on inputs other than the current one"*). It is nonempty — i.e. the retract
> actually loses something — exactly on **`|S|≥2 ∧ |T|≥2`**, the same locus as the clause‑(2)
> separation.

This also dissolves the note's Gap 5.2 ("reversal of adjointness") honestly: `T^S` is the index of
the left‑adjoint `Σ` (not right‑adjoint content), the right‑adjoint content `(−)^S` is **kept** by
both worker and weld, and the worker‑vs‑weld difference is purely in how much of the `Σ`-index is
retained (`T` vs `T^S`) — not an adjoint‑direction clash at all.

---

## 4. The unified statement (for the grant / write-up)

One theorem now carries clauses (2), (3) and the §5 σ‑remark:

> **Worker = constant-branch slice of the weld.** With `A` read as the `(ΔT,ΔS)`-bicomodule
> `σ(A)=B'⊆B` of constant branch maps (`σ♯=id_{S×T}`),
> `F̄_A(V)=T·V^S` sits inside `F̄_B(V)=T^S·V^S` as the sub‑sum over `const(T)⊆T^S`. Worker and weld
> **share** the right‑adjoint content power `(−)^S`; they differ **only** in the `Σ`-aggregation
> index (`T` vs `T^S`). The retract `e(s,g)=(s,const_{g(s)})` projects `T^S` onto `const(T)`,
> forgetting per input `s` the off‑diagonal fibre `T^{S∖{s}}`. All three degeneracies
> (`F̄_A=F̄_B`, no discard, `A=B`) coincide and hold **iff `|S|=1` or `|T|=1`**; the proper
> separation is exactly **`|S|≥2 ∧ |T|≥2`**.

Reading for orchestration semantics: *state‑entanglement* (the worker `A`) keeps a branch choice
per output token `t∈T`; *data‑aggregation* (the weld `B`) keeps a branch choice per **function**
`g∈T^S`. Both read the whole input state (content `(−)^S`); the weld aggregates over all response
policies, the worker only over constant ones. Keeping them distinct is a *semantic* requirement, not
a bug — and the exact locus where it matters is `|S|,|T|≥2`.

---

## 5. Verification

`scratch/2026-10-18-worker-content-separation.py`, all checks pass:
- **(1)** `F̄_B=(mV)^n=m^n V^n`, `F̄_A=m·V^n`; equality `m^n=m ⟺ n=1∨m=1` verified at
  `(1,2),(1,3),(2,2),(2,3),(3,2),(3,3)`; witnesses `(2,2)@V=2: 8 vs 16`, `(1,2),(1,3)` equal.
- **(2)** `B'` closed under `λ` and `ρ` at `(2,2),(2,3),(3,2),(1,2),(2,1)` (sub‑bicomodule).
- **(3)** `σ_1:S×T≅B'`-positions (`σ♯=id`), bijection of size `n·m`, at the five shapes.
- **(4)** `e` idempotent, image = constant slice, every fibre size `=m^{n−1}`.
- **(5)** at `(2,3)`: fibre `3`, `NC=6`, `T^S=9` — all distinct (kills "discarded = non‑constant").

(The `k=2` ground‑object checks exhibit non‑trivial branch tuples for each shape; the closure
statements are structural — the coactions never touch the `g`-value — so the finite checks are
confirmatory, not the whole proof.)

---

## 6. Honesty / gaps

- The only genuinely new mathematics is §1: that the worker's consistent `(ΔT,ΔS)`-reading is the
  constant‑branch sub‑bicomodule `B'`, with carrier polynomial exactly `A=Δ(S×T)`. Everything in
  §§2–3 is then bookkeeping on the peer‑reviewed Thm 3.1 (restrict the Σ‑index to `const(T)`) plus
  elementary finite combinatorics of `e`.
- Prop 1.3 gives two descriptions of `A`'s reading (sub‑bicomodule `B'`, and cobase change along the
  projections) and asserts they coincide. The **sub‑bicomodule description is primary and fully
  verified**; the cobase‑change description is the conceptual justification that `B'` is the
  *canonical* reading (not an arbitrary sub‑object) and is checked to agree on carriers/positions.
  A fully formal identification of the two bicomodule structures (coaction‑by‑coaction, general
  `S,T`) is not written out here — it is not needed for the comparison, which only uses `A≅B'`.
- No claim beyond the corrected clauses (2), (3) and the §5 σ‑display is made. The clause‑(1) core
  and Thm 3.1 are peer‑reviewed inputs, unchanged.
