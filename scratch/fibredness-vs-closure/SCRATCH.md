# SCRATCH — fibredness vs ◁-left-closure (2026-08-30 PROVE)

## The three conditions (my definitions, stated as mine)

Shape fibration `π : Fam(C^op) → Set`, `π(S,P)=S`. Family fibration of `C^op`;
cartesian = all position-components iso.

For a fixed `q=(T,Q)` consider `L_q := (−)◁q`.
- **(V) vertical**: `π L_q = π` and cartesian preserved.
- **(F) fibred**: ∃ `F_0:Set→Set` with `π L_q ≅ F_0 π` and cartesian preserved.
- **(C) closed**: `L_q` has a right adjoint (= the ◁-LEFT-closure).

## First observations (to be checked/proved)
- shapes: `π(p◁q) = Σ_{s∈S} T^{P_s}` over Set;  `= S×T` when positions tiny.
- `π(q◁p) = Σ_{t} S^{Q_t} = ⟦q⟧(S)` — depends only on `S` ⟹ RIGHT variable fibred, base
  functor literally `⟦q⟧`. (This is exactly why BHM say "left".)
- cartesian preservation is FREE for both variables — non-fibredness is *only*
  base-functoriality.

## Targets
A. Over Set: (V) ⟺ (F) ⟺ (C) ⟺ |T|=1.
B. Over Vec_fd: (V) ⟺ |T|=1;  (C) ⟺ #{t:Q_t≠0} finite;  (F) always.
   ⟹ **(V) ⊊ (C) ⊊ (F) strictly**. Witnesses T=2 and T=ℕ.
C. Diagnosis: fibred = shape-collapse; closed = collapse + summability in the base.

## Computations to run
1. brute-force `π(p◁q)` depends on P.
2. adjunction count for monomial q over Set: `H=(Σ_ρ Q^{M_ρ}, M_ρ)`.
3. `G_2(Z)=2^{T^Z}` not polynomial (fit fails) for T=2.
4. Vec_fd(F_2): `◁=⊗`; closure adjunction count finite T; dim blow-up for growing T.

---
## RESULT (session complete, 2026-08-30)

All four targets landed, plus two unplanned strengthenings.

**Thm A (Set):** (V)⟺(F)⟺(C)⟺|T|=1. The `(F)⟹|T|=1` direction is ONE LINE (⟨∅⟩ vs ⟨1⟩), and
uses only the OBJECT part of fibredness — no naturality, no cartesianness.
**Thm B (Vec_fd):** (F) always; (V)⟺|T|=1; (C)⟺#{t:Q_t≠0} finite. STRICT CHAIN (V)⊊(C)⊊(F).
**Diagnosis:** one test (G_r familially representable), two probes (shape r=(R,0) / position r=⟨I⟩).
**Bonus:** ◁ IS fibred on the RIGHT (base functor = ⟦q⟧); cartesianness is FREE in both variables.

### The cheapest falsifier (PROVE.md asked for it first) — RUN, and it PASSED
`q=2y` (T=2) vs `q=y²` (T=1) over Set: `G_2(Z)=2^{T^Z}` is `2,4,16,256,…` (no polynomial fit)
for T=2 and constant `2` (fit `{0,0}`) for T=1. Both verdicts agree in each case ⟹ part (A) is
NOT dead on arrival. Good, because (A) then went through.

### What was hard, and what unstuck it
The one genuine obstacle: proving `(C)⟹|T|=1` over Set for **infinite** `T`. My existing Workers
Thm 2 argument is a CARDINALITY COUNT (`|H([n])|≥2^{2^n}` beats `#shapes·n^K`), and cardinality
arithmetic collapses for infinite `T` (`2^{|T|^2}=2^{|T|}`). Three angles:
 1. count harder — DIED (cardinal arithmetic is too coarse).
 2. cite Carboni–Johnstone "familially representable = preserves wide pullbacks" and exhibit a
    failing wide pullback — WORKS but imports a theorem.
 3. **extract the two-line kernel of (2)**: for `F=∐_u y^{N_u}`, `x=(u,g)∈im F(A)` iff `im g⊆A`,
    so supports are closed under intersection. Then `Z=ℕ`, `A_n=ℕ∖{n}`, `x=` eventually-`t_0`
    sequences. WORKS, self-contained, and covers |T|=0 too. ← chosen.
The lesson: **when a counting argument stalls at infinity, look for the structural invariant the
count was a shadow of.** Here: "double-exponential growth" was a shadow of "no least support."

### Hostile-referee pass caught a real error
Lemma 2.1 first read `(s,τ)↦(fs, τ∘(φ^♯_s)^{-1})`. WRONG — the inverse only exists for cartesian
φ, and the correct action (from the whiskering ⟦φ⟧⟦q⟧) is `τ∘φ^♯_s`. Caught by writing explicit
container morphisms in code and testing functoriality: 183/183 after the fix. Downstream
(Computation 3.3) was unaffected — `res_i` was right for the right reason.

### Honest residue
- `◁ := ⊗` on the tiny locus is a DEFINITION (⟦−⟧ not full over Vec). Thm B is about `(−)⊗q`.
- PP 2601.15420 attribution NARROWED not closed. sources.json updated with the exact locator
  needed and a correction to PROVE.md's "agent-summary" characterisation.
- OPEN: is "closed ⟹ fibred" true over an arbitrary base? Prop 5.2 gives only the shape probe.
