# Left adjoint to `(−)◁q` over `Fam(C^op)`: the gate is `|T|=1`, and the invariant is UNIT-CONNECTEDNESS

**PROVED 2026-08-30** — `proofs/2026-08-30-left-adjoint-over-vec.md`, registry
`left-adjoint-over-vec.json` (validates, `proved`), code `scratch/left-adjoint-vec/verify.py`.
Successor to `pra-vs-probe-method` (the `Set` case). Answers the brief's (A), (B), (C).

## The three theorems

**Theorem 1 (base-general, presentation-independent).** `C` closed symmetric monoidal with small
coproducts and **connected unit** `I` (`C(I,−)` preserves ∐). Then for **every** `q`,
`F_q = Fam(⟦q⟧^op) ⊣ (−)◁q`, `F_q(R,U)=(R,⟦q⟧U_ρ)`.
*Proof:* `Fam(r,p◁q) = ∏_ρ∐_d C(N_d,U_ρ) = ∏_ρ∐_d C(I,[N_d,U_ρ]) =γ⁻¹= ∏_ρ C(I,⟦p⟧⟦q⟧U_ρ)
= ∏_ρ C(I,∐_s[P_s,⟦q⟧U_ρ]) =γ= ∏_ρ∐_s C(P_s,⟦q⟧U_ρ) = Fam(F_q r, p)`. **`γ` twice, nothing else.**

**Theorem 2 (the characterisation).** Wherever `p◁q = p⊗q` (collapse locus: all positions tiny —
T4 Prop 2.1 — **or** `T` finite and `C` additive, Lemma 2.0(ii), new):
> **left adjoint exists ⟺ `|T| = 1`**, and then `F_q(R,U)=(R,[Q,U_ρ])` (closedness only, no
> dualizability).
Necessity, two independent proofs: (a) right adjoints preserve the terminal object `1=⟨0_C⟩`, and
`1⊗q=(T,0_C)≅⟨0_C⟩` iff `|T|=1`; (b) binary products force `|T|=|T|²` — **no zero object used**.

**Theorem 3 (p.r.a. separates).** `Fam(C^op)/(T,0_C) ≅ ∏_{t∈T}Fam(C^op)`, `(L_q)_1 p = (p⊗Q_t)_t`,
left adjoint `(r_t)_t ↦ ∐_t F_{Q_t}(r_t)`. So **`L_q` is a parametric right adjoint for every `q`
over `Vec` too**, while having an honest left adjoint only at `|T|=1`.

## What died, and what replaced it

- **DEAD: the summability prediction.** The gate is `|T|=1`. The comparison map fails at
  `dim P_s = 1`, `|T|=2`, `T` finite — where **both sides have 4 elements** but `κ` double-counts
  the zero map and misses `e_0+e_1`. *A cardinality check would have missed this.* Over `Vec_fd`,
  left-adjointness (`|T|=1`) **strictly implies** the closure/summability condition — the two are
  ordered, not merely different.
- **DEAD: "`(†)` = distributivity is the load-bearing step"** (the brief's ★, and my own predecessor
  §4.2). The adjunction needs only `γ`. Distributivity of `Set` is used in *constructing* `◁` over
  `Set` (it makes `Σ_s T^{P_s}` the shape set), never in the adjunction.
- **NEW: unit-connectedness is the invariant on the LEFT too.** `γ` is verbatim T1's map, so
  **T1 (fullness of `⟦−⟧`) and the `◁`-coclosure are the same lemma applied twice.** Extensivity is
  not it: `Set×Set` is lextensive with disconnected unit. See [[fullness-unit-connectedness]].

## The anti-diagonal (why this is crown material)

| | left adjoint to `L_q` | right adjoint (`◁`-closure) |
|---|---|---|
| `Fam(Set^op)` | **always** (Thm 1; = Niu–Spivak Prop 6.57/Meyers) | iff `|T|=1` (Workers Thm 2) |
| `Fam(Vec_fd^op)` | iff **`|T|=1`** | iff `#{t:Q_t≠0}<∞` (T4 Thm 3.1) |

**The conditions swap sides.** And in the `(V)⊊(C)⊊(F)` chain of `fibredness-vs-left-closure`:
over `Vec_fd`, **left-adjointness ⟺ verticality (V)** — the *bottom* rung; over `Set`,
`(V)=(C)=(F)={|T|=1}` and left-adjointness is unconditional. **The chain inverts end to end.**

## Two sharp secondary observations

1. **The empty product is the binding probe.** For `q=(ℕ,(k))` over `Vec_fd`, `L_q` preserves all
   *binary* products (positions don't depend on `t` and `ℕ≅ℕ²`) but **not** the terminal object.
   Necessity proof (b) is genuinely inconclusive there. Cf. [[containers-preserve-connected-not-empty]].
2. **`1◁q` is the exact measure of the p.r.a./left-adjoint gap.** Over `Set` it is terminal (gap 0);
   over `Vec` it is `(T,0)` and the slice `Fam^T` absorbs the whole `T`-fold branching. The
   responsible structural feature: **`Set` has no zero object**; `Vec` does.

## By-product: `◁` does not exist over `Set×Set` (Prop 9.1)

`⟦E,N⟧(1_C) = E·1_C` is a copower of the terminal object, hence *diagonal* in `Set×Set`; but
`⟦p⟧(T·1_C) = (T^A,T^B)` is not, for `p=⟨(1,2)⟩`, `|T|=2`. So `Fam((Set×Set)^op)` is **not closed
under `◁`**, and the intended separator base for the converse to Theorem 1 is **unavailable**.
Criterion exposed: `◁` needs `⟦p⟧(T·1_C)` to be a copower of `1_C`. `Set` passes because `1_C=1` is
a *generator*; `Vec` passes because `1_C=0` is a *zero object* (and that invisibility is exactly
T1's failure of faithfulness). **Conjecture (`speculative`):** those are the only two poles, in
which case Theorems 1 and 2 are jointly exhaustive.
⚠ **Scope:** this is about *my* external `Fam(C^op)` (one shape set, positions in `C`). DJN
`2305.05655` may use an indexed category where the two components carry independent index sets —
**UNVERIFIED**. Flagged for browse together with T4-left Gap 2.

## Caveats and open

- **`◁ := ⊗` on the collapse locus is a DEFINITION**, not a deduction: over `Vec`, `⟦−⟧` is not
  faithful (T1 correction 2), so `(T,0)` and `({∗},0)` present the same constant-`0` functor.
  Necessity proof (b) is independent of it for finite `T`; proof (a) is not.
- **Novelty gate OPEN** on Theorem 1's general-base form. The `Set` instance is KNOWN
  (Niu–Spivak `2312.00990` Prop 6.57/(6.59), Meyers; gate closed 2026-08-30). Next browse: grep DJN
  for "coclosure" / "left adjoint".
- **Converse to Theorem 1** (`I` connected *necessary*?) open — and possibly only vacuously, by
  Prop 9.1.
- `◁` on `Fam(Vec^op)` for **infinite** `T` and non-tiny positions: still undefined (T4 Gap 2).
- Naturality of `F_q` in `q`: unchecked (also unchecked in the predecessor).
