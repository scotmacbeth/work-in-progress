# THM 3's last corner is closed: `U∘U ≇ ⟦r⟧∘U`. The unit is the weapon.

**MacBeth, 2026-09-07 (PROVE).** For Neil / Rick / whoever picks up the M-container thread.

## One line
The open question **(★)** — does `U∘U ≅ ⟦r⟧∘U` for some polynomial `⟦r⟧`, where `U` = free
commutative **unital** magma monad — is answered **NO**. THM 3 (M-containers compose ⟺ M polynomial)
now holds, necessity included, for `U`: the canonical `a_0>0 ∧ unbounded-wreath-depth` inhabitant that
refuted Conjecture V's vacuity. Full writeup: `proofs/2026-09-07-U-corner-resolved-stabilizer.md`.

## The idea in three moves
1. **Both prior engines are dead at `U`**: plethysm cancellation needs `Z_M` constant-term `0`
   (`Z_U` has `a_0=1`, and `Z_U∘Z_U` doesn't even converge); the wreath-depth gap needs bounded depth
   (`U` has `W=∞`). So I used the **stabilizer invariant** (Lemma E of `2026-09-05` §4), read on
   **species components** — it is `a_0`-agnostic and never sums anything, so the divergence is irrelevant.
2. **Meta-theorem (the crux, elementary).** On the each-label-once component `[m]`, every stabilizer of
   `(⟦r⟧∘M)[m]` is a **block-fixing product** `∏Stab(u_β)` of single-`M`-element stabilizers — because a
   polynomial outer layer has rigid positions (a function is fixed iff fixed pointwise), so it can never
   **swap two parts**. `⟦r⟧∘M` only sees within-part symmetry, assembled by direct product.
3. **The witness (`n=4`, minimal).** `w = μ(μ(V_0,μ(V_2,E')), μ(V_1,μ(V_3,E'))) ∈ (U∘U)[4]` has
   `Stab(w) = ⟨(0 1)(2 3)⟩ = C_2`, a lone fixed-point-free (correlated) swap. It is **not** a
   block-fixing product (any product containing `(0 1)(2 3)` contains `(0 1),(2 3)` separately →
   order ≥ 4; single 4-leaf tree-groups are `D_4`/`S_2`). So it is an orbit-type of `(U∘U)[4]` absent
   from every `(⟦r⟧∘U)[4]`. Contradiction with any iso. ∎

## Why this is satisfying (and counter-intuitive)
The **unit `E'` is the weapon.** At the *inner* level it absorbs (`μ(t,E')=t`), which is exactly what
refuted Conjecture V (the unit *absorbs* rather than *builds*, so `M∅` stays finite). But at the
*outer* level of `U∘U`, that same inner unit appears as a **generator** (not the outer unit) and is
**not** absorbed — so it acts as a label-free peg that makes the block `μ(V_i,μ(V_j,E'))` **rigid**
(no internal symmetry). Two equal rigid blocks then swap with the swap as their *only* symmetry. A
polynomial layer can never produce a lone correlated swap. **`a_0>0` does not save the corner — it
supplies the counterexample.** The feature that put `U` in the corner is the feature that breaks
composition there.

## Bonus: the free magma (`a_0=0`) falls too, by the same invariant
There is also a **unit-free** witness at `n=8`: `Stab = (S_2×S_2)≀S_2` (order 32,
support-indecomposable ⟹ not a single tree-group since indecomposable 8-leaf tree-group orders are
`{8,128}` ⟹ not a product). Being unit-free it lives in `A∘A` for `A` = free commutative *non-unital*
magma — so it **re-proves Theorem P's conclusion for the free magma by the stabilizer method alone**,
no plethysm. Two witnesses, two regimes (`a_0=1` needs `C_2`; `a_0=0` needs the depth-2 wreath), one
invariant.

## The one caveat I had to get right (worth knowing)
`⟨(0 1)(2 3)⟩` *is* an intersection of single-`U`-stabilizers over the **all-content** set at `X=[4]`
(via overlapping-support trees) — so the naïve "compare raw stabilizer sets" argument FAILS (the sets
coincide). The point is that those realizations **reuse labels**, so they live in *higher* species
components, not in `[4]`. The invariant must be read **per species component** (multilinear part),
where each-once forces disjoint parts. This is the whole game; `scratch/2026-09-07-Hstar.py` and
`-percomponent-confirm.py` pin it down.

## What's left (the general grant statement)
The Meta-theorem holds for **any** monad `M`, reducing THM 3-necessity to: *does `M∘M` realize, on some
component, a stabilizer outside `𝒫_M` = block-fixing products of single-`M`-element stabilizers?* Proved
here for `U` and the free magma. A **uniform** "for every non-flat analytic `M` the swap escapes `𝒫_M`"
theorem is the clean next target (registry node `theorem-general-stabilizer-necessity`, to create). I'd
bet it's true and closes the entire converse for analytic monads via one group-theoretic lemma —
retiring the plethysm/degree machinery entirely.

**Crown for the grant.** Composition of `M`-containers is obstructed *exactly* by a symmetry that
**correlates two equal sub-computations**. Polynomial `=` flat `=` no within-`M` symmetry to correlate
`=` the property that survives self-composition iff it was there to begin with. Codensity governs
fullness; this correlated-swap obstruction governs composition — and for `U` the unit sits on both
sides of the dichotomy.
