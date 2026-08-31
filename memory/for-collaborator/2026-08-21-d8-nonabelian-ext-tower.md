# D₈: the first non-abelian Mackey/Shapiro Ext tower — with a correction for Rick

**For:** Rick (this was your 08-23 D₈ request), Neil.
**TL;DR:** The formula `Ext^n_{kD₈}(k[G/A],k[G/B]) = ⊕_{g∈A\G/B} H^n(A∩gBg⁻¹)` is confirmed
in the genuine non-abelian regime by an *independent* minimal free resolution over `k[D₈]`
(6/6 cases, degrees 0..6, resolutions validated exact). But **the proposed test case does not
exhibit non-collapse**, and the real non-abelian example is more interesting than either of us
predicted.

## The correction (important)

The brief said: use the **two Klein-four subgroups** `A=⟨r²,s⟩`, `B=⟨r²,rs⟩`. These are **both
normal** (index 2). For normal `A`, `AgB = g·AB` and `AB = G`, so there is a **single double
coset** — the tower just collapses to `H*(A∩B) = H*(Z/2) = [1,1,1,…]`. Two normal subgroups can
*never* give a multi-coset example. So the Klein-four choice is a collapse case, not the
per-coset non-collapse we wanted.

## The genuine non-abelian example: A = B = ⟨s⟩ (a non-normal reflection)

Three double cosets (`g = e, r, r²`), intersections `⟨s⟩, {e}, ⟨s⟩`:
```
    Ext^n_{kD₈}(k[G/⟨s⟩], k[G/⟨s⟩]) = [1,1,1,…] + [1,0,0,…] + [1,1,1,…] = [3, 2, 2, 2, …].
```
**This is the phenomenon you were betting on, and it's sharper than the abelian case.**
`deg 0 = 3 = h` (the meeting count), but the higher tower stabilises at `2 < 3`. In the abelian
non-transverse regime the multiplicity is *uniform across all degrees* (`Ext^n = h·dim H^n(A∩B)`,
so deg-0 equals the higher value). Here **deg-0 strictly exceeds the higher-degree dimension**,
because one of the three meetings (`g=r`, where `A∩gAg⁻¹ = ⟨s⟩∩⟨r²s⟩ = {e}`) is *transverse* —
it lives only in degree 0. Reading:

- **`dim Ext⁰ = h` = total meeting count** (Hom is Mackey-blind to conjugation).
- **higher tower is supported only on the NON-transverse meetings.**
- when nontrivial intersections are rank-1 (`≅Z/2`): **`dim Ext⁰ − dim Ext¹ = #{transverse
  cosets}`**. Here `3 − 2 = 1`. *The gap between the meeting count and H¹ literally counts the
  perfectly-aligned-away meetings.*

This resolves your Ext-detects-alignment question in the non-abelian setting: it is **not** that
a higher class appears (the holonomy/exact-factorization setting kills the whole tower — see
`emergent-holonomy-is-ext-degree0`); rather, **when meetings are NOT all transverse, alignment
shows up as the deg-0-minus-higher-tower gap**, i.e. how many meeting points fail to persist into
positive degree.

## One more subtlety worth knowing

`A=⟨r²,s⟩, B=⟨s⟩` gives 2 cosets with intersections `⟨s⟩` and `⟨r²s⟩` — **distinct subgroups**,
both `≅Z/2`, so the tower is `[2,2,2,…]` and *looks* collapsed even though the double cosets and
their intersections genuinely differ. Cohomological collapse is coarser than subgroup-equality:
the tower only sees the *isomorphism type* of each `A∩gBg⁻¹`.

## Provenance

- Formula `(⋆)`: classical Shapiro+Mackey (proof assembled in the write-up §2). Not new.
- D₈ computations: `computed`, two independent methods agree. Engine
  `scratch/rick-d8-ext/gen_d8.py` (general finite-group F₂ engine). `run_d8.py`,
  `validate_resolution.py`. Sanity: `A=B=G` betti `[1,2,3,4,5,6,7,8] = dim H^n(D₈;F₂)=n+1`.
- Full write-up: `proofs/2026-08-21-d8-nonabelian-ext-tower.md`.
- Registry: node `d8-nonabelian-crosscheck` under `emergent-holonomy-is-ext-tower` (computed).

**Ask for you, Rick:** is the "deg-0 minus higher-tower = #transverse cosets" gap the invariant
you wanted alignment to be measured by? If so we have a clean non-abelian meeting-point statistic.
