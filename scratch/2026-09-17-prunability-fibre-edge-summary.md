# Prunability lives on the fibre edge; the ZS holonomy is dead on the base edge

**Date:** 2026-09-17  **Script:** `2026-09-17-prunability-fibre-edge.py` (runnable, self-contained; imports `qskb_task2`).

Empirical core of the PROVE.md target: a **connected, non-prunable** QSKB witness with the
two LHS edges **decoupled** — `[ω]=0` on the base edge, `[π]≠0` on the fibre edge — plus a
prunable connected **control** where both edges die.

## The witness and control

Both are `G = Z/2 × Coarse({0,1})` (arrows `(i,j,q)`, `i,j∈{0,1}`, `q∈Z/2`; 8 arrows, 4 loops),
differing only in the additive star structure. Both are machine-verified valid QSKBs (truss
distributivity (5)) drawn from the exhaustive family of 48 `Z/2` QSKBs.

| | star `(St(0),+)` | loop set `L_0` | additive subgroup? | prunable? |
|---|---|---|---|---|
| **WITNESS** | `Z/4` (loop gen at order-4 slot) | `{(0,0,0),(0,0,1)}` = `{0,1}` | **No** (`1+1=2∉L_0`) | **No** |
| **CONTROL** | Klein `V4` | `{(0,0,0),(0,0,1)}` | **Yes** | **Yes** |

## The two structures (`D`, `Γ`, `M`)

Two *different* extensions are in play — this separation is the whole point.

- **Multiplicative ZS extension** `1 → D → π → Γ → 1` governing `[ω]`:
  - `D` = full loop bundle; vertex group `L_i ≅ Z/2` under composition.
  - `Γ = Sk_C` = orbit base = **coarse groupoid on {0,1} ≃ point** (connected ⟹ codiscrete),
    so `Γ ≃ 1`.
  - `π = L_0 ≅ Z/2`; the extension is `1→Z/2→Z/2→1→1`, split.
- **Additive (skew-brace) star extension** `0 → A → St → Q → 0` governing `[π]`:
  - `A` = the (unique for `Z/4`) additive order-2 subgroup `{(0,0,0),(0,1,0)}` = `{0,2} ≅ Z/2`.
  - `Q = St/A ≅ Z/2`.
  - `M = A ≅ Z/2` (trivial `Q`-module, `St` abelian).

## Base edge `E₂^{2,0}=H²(Γ; M^D)` — the holonomy `[ω]`

`Γ ≃ 1` (coarse), so `H^{≥1}(Γ; −)=0` for any coefficients. Hence
`dim H²(Γ; M^D)=0` and **`[ω]=0`** for **both** witness and control. This is Prop. A of the
09-16 separation paper. **Fully rigorous, coefficient-independent.**

## Fibre edge `E₂^{0,2}=H²(D;M)^Γ` — the prunability class `[π]`

Computed as the additive Schreier class of the star extension `0→A→St→Q→0`
(`Γ`-invariants are everything since `Γ≃1`). `H²(Q;A)=H²(Z/2;Z/2)=Z/2` (bar-complex,
`dim_{F₂}=1`). Split/nonsplit decided by exhaustive coboundary search:

- **WITNESS (`Z/4`):** extension **nonsplit**; Schreier cocycle `f(1,1)=(0,1,0)=2∈A`,
  not a coboundary ⟹ **`[π]` = nonzero generator of `Z/2`.**
- **CONTROL (`V4`):** extension **split** (complement exists) ⟹ **`[π]=0`.**

## Ferri's REAL K_{2,3} (arXiv:2410.10717, JPAA 229 (2025), Ex. 4.29 / Table 3)

Upgrade of the decoupling from the synthetic stand-in to Ferri's actual witness. Underlying
set `A = ℤ/4`, two objects `S2, S3`, connected degree-2 groupoid. Loop bundle
`loops(S2)={0,3}`, `loops(S3)={0,1}`.

**Additive group structure (the delicate point, machine-checked).** The star tables `•_S2, •_S3`
are **left quasigroups, NOT groups**: rows are permutations but columns are not (`•_S2` col 1 =
`1,2,1,2`); both are **non-commutative** and **non-associative** (explicit witnesses: `•_S2`
`(1·1)·1=1≠3=1·(1·1)`; `•_S3` `(2·1)·1=0≠2`). Since every order-4 group is abelian, `•_λ` cannot
be a group. So `•_λ` is *not* itself the additive group `+_λ`. The skew brace's genuine additive
group on `A` is **ordinary `(ℤ/4,+)`** (paper: `a·b=a+b`). Both stars therefore carry the
**same** additive group `(ℤ/4,+)` as the synthetic `Z/4` witness — the additive orders are
`{0:1, 1:4, 2:2, 3:4}`.

**Prunability (rigorous).** Under `(ℤ/4,+)`: `loops(S2)={0,3}` is not a subgroup (`3+3=2∉`);
`loops(S3)={0,1}` is not a subgroup (`1+1=2∉`). Both loop sets contain an additive order-4
element (the "order-4 slot"). ⟹ **NON-prunable** = Ferri Counterexample 5.2. *(Honest twist:
the loop sets ARE closed under the quasigroup `•_λ` — sub-left-quasigroups — but `•_λ` is not a
group, so "additive subgroup" is only meaningful w.r.t. `(ℤ/4,+)`.)*

**Base edge (rigorous).** `K_{2,3}` connected ⟹ orbit base coarse ≃ point ⟹ `Γ≃1` ⟹
`H²(Γ;M^D)=0` ⟹ **`[ω]=0`**.

**Fibre edge (rigorous computation, additive-twin reading).** For each star `(St,+)=(ℤ/4,+)`,
`A={0,2}`, `Q=ℤ/2`, `H²(Q;A)=ℤ/2`. Extension `0→{0,2}→ℤ/4→ℤ/2→0` is **nonsplit** at BOTH
`S2` and `S3` (Schreier cocycle `f(1,1)=2∈A`, not a coboundary) ⟹ **`[π]_{S2}=[π]_{S3}=`
nonzero generator of `ℤ/2`**.

**Verdict: Ferri's real `K_{2,3}` exhibits the SAME decoupling as the synthetic witness —
`[ω]=0` and `[π]≠0`** — now on Ferri's actual numbers, at both stars.

## Result table

| case | prunable | base `H²` | `[ω]` | star split | `[π]` |
|---|---|---|---|---|---|
| SYNTH WITNESS | No  | 0 | **0** | No  | **≠0** |
| SYNTH CONTROL | Yes | 0 | 0 | Yes | 0 |
| **FERRI `K_{2,3}`** | **No** | 0 | **0** | No (both S2,S3) | **≠0 (both)** |

**Decoupling confirmed (witness):** `[ω]=0` (base coarse) yet `[π]≠0` (Z/4 nonsplit).
**Control:** `[ω]=0` and `[π]=0` — both edges dead, isolating the fibre edge as the genuine
detector of prunability. The dividing line is exactly the `Z/4`-vs-Klein additive twin of the
multiplicative Schreier line.

## Honest status

**Rigorous:**
- QSKB validity and (non)prunability of both examples (exhaustive over 48 `Z/2` QSKBs).
- `[ω]=0` on the base edge: `Γ` coarse ⟹ `H^{≥1}(Γ;−)=0`, any coefficients.
- `H²(Q;A)=Z/2` as a group, and the star extension class computed nonsplit (`Z/4`) / split
  (`V4`) by exhaustive coboundary search. So `[π]≠0` (witness), `[π]=0` (control) are rigorous
  facts *about the additive star extension*.

**Heuristic / modelling choice (the separately-tracked open node):**
- Identifying this additive star extension class `[π]∈H²(Q;A)` with the categorical LHS
  **fibre edge** `E₂^{0,2}` and with the Ferri "prunability defect" is the **additive-twin
  reading** of the separation paper. It is exact for this two-object `Z/2` family (Prop.
  "family" there), but a structural proof that the fibre edge of the categorical LHS sequence
  literally receives Ferri prunability for general twisted groupoids is **not** given here
  (the h2cluster-transgression paper's explicit "Not claimed" node).
- Subtlety kept in view: the multiplicative loop set is `{0,1}`, *not* the additive subgroup
  `A={0,2}`. The defect is precisely that a nonsplit `Z/4` has **no complemented `Z/2`** to
  host the loops as an additive subgroup; `[π]≠0` **is** that non-splitting. In `V4` a
  complement exists, the loops are a subgroup, and `[π]=0`.

**Ferri `K_{2,3}`-specific — the quasigroup subtlety:**
- *Rigorous:* `•_S2, •_S3` are left quasigroups, not groups (machine-checked non-comm /
  non-assoc); with the genuine additive group `(ℤ/4,+)` the loops are not subgroups
  (non-prunable, = Counterexample 5.2); `[ω]=0` by connectedness; `[π]≠0` at both stars
  (`(ℤ/4,+)` nonsplit over `{0,2}`, `H²(Q;A)=ℤ/2`, cocycle `f(1,1)=2`).
- *Open/heuristic:* the verdict rests on reading `+_λ` as the genuine additive group `(ℤ/4,+)`
  — Ferri's own convention in Counterexample 5.2. In the *dynamical* skew-brace framework
  (2410.10717) the star can be quasigroup-only; whether the categorical LHS fibre edge
  `E₂^{0,2}` literally hosts this class for a genuinely dynamical (non-group) star is the same
  tracked-open node as in the synthetic case, and here additionally rests on the `(ℤ/4,+)`
  additive-group reading. The loops being closed under `•_λ` (sub-left-quasigroups) but not
  under `(ℤ/4,+)` is the precise locus of that ambiguity.
