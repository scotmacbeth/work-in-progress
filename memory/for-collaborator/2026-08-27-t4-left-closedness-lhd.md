# T4-left: the ◁-closure exists exactly where ◁ collapses to ⊗ (Neil UID 125)

**For Neil / Robin. 2026-08-27 PROVE. Full proof:
`proofs/2026-08-27-t4-left-closedness-lhd-famcop.md`. Registry
`t4-left-closedness-lhd-famcop.json` (proved, validator-clean).**

## The one-line answer to "left closedness too, if possible"
**Yes — but only because over a linear base the substitution product degenerates.**
The left internal hom of the non-symmetric `◁` (= the `◁`-closure = right adjoint to `(−)◁q`,
the thing `Cont` provably lacks) **exists on `Fam_fin(Vec_fd^op)`**, and there it *is* the T2
Dirichlet-rigid hom `[(T,Q)◁(R,M)]=(R^T,(⊕_t M_{ρ(t)}⊗Q_t^*)_{ρ:T→R})`. It fails on
`Fam(Vec_fd^op)` (infinite shapes) and `Fam(Vec^op)` (infinite-dim positions) for T2's two dual
reasons.

## Why (the mechanism, in one breath)
Over `Vec_fd` the internal hom `[Z,−]` is **additive**, so it preserves coproducts, so the
substitution `⟦p◁q⟧=∐_s[P_s,∐_t[Q_t,X]]` collapses to `∐_{s,t}[P_s⊗Q_t,X]=⟦p⊗q⟧`.
**`◁ = ⊗`** — my proved Prop 4.1. `◁` becomes *symmetric*, its left/right homs merge, and the
closure is just T2's `⊗`-hom. Over `Set`, `[Z,−]=(−)^Z` branches a coproduct `∐_t` into `T^Z`
(the extensive distributive law), so `◁≠⊗`, `◁` is genuinely non-symmetric, and its closure is
non-polynomial (my Workers Thm 2). The `◁`-closure exists **iff `◁` stops being `◁`**.

## The part I think you'll like (the inversion)
**Extensivity is *opposed* to `◁`-left-closedness.** In T1 non-extensivity broke fullness
(`∐⊊⊕`); in T2 it broke `⊗`-closedness (only the finite-fd corner survives). Here the *same*
`∐⊊⊕` seam **buys** the `◁`-closure: the villain becomes the hero. One distributive law
`[Z,∐_t B]=∐_{τ:Z→T}∏ B`, two opposite valuations — it branches over extensive bases
(obstruction) and degenerates over linear ones (repair).

## Your hint landed exactly
"left Kan preserves representability, then it's just coproducts" = T2's rigid dualization
`C(M_r,Z⊗Q_t)=C(M_r⊗Q_t^*,Z)` (left adjoint `(−)⊗Q_t^*` preserves corepresentability) then
`∏_t ⤳ ⊕_t` (coproducts). I now read that as computing the `◁`-closure through the collapse.
(This also discharges the secondary reading of your ask — a clean left-Kan account of the `⊗`
closedness — as the §4 remark; the substantive new content is the `◁` verdict.)

## Honesty
- Disambiguated first, as PROVE.md demanded: the target is the `◁`-**closure** (right adjoint
  to `(−)◁q`), NOT the known `◁`-**coclosure** (= directed containers, right adjoint to
  `q◁(−)`, a genuine `Lan`). I did not re-prove the coclosure.
- The result is a **synthesis** of three of my own `proved` theorems (Prop 4.1, T2, Workers
  Thm 2), not a new hard lemma. The positive verdict holds only where `◁` degenerates; the
  genuinely non-symmetric `◁` is NOT left-closed. That honesty is the point.
- Verified: 20000/20000 collapse dims, 3000/3000 closure adjunction cardinality over `F_2`.
- **Open (flagged):** the general "iff" for the collapse (converse `◁`-closed ⟹ positions
  tiny) is proved only over `Set` and `Vec`; and what `◁` even *is* over full `Vec` (off the
  tiny locus) is the same infinite-dim gap as in `vec-comonoids-algebras`.

## Grant reading (applications)
Higher-order substitution of resource-graded processes (agent orchestration = `◁`-composition)
admits currying/an internal hom **only** over a finite-dimensional-linear resource base — where
substitution coincides with parallel product — and is structurally impossible over any set-like
(extensive) resource base. With T1/T2 this closes the "which closed structure over which base"
map for `Fam(C^op)`.
