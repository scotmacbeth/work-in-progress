# General F_p engine: verifies (★) Ext(k[G/A],k[G/B]) = ⊕ H^*(A∩gBg⁻¹)

Own exact F_p linear algebra (`fp.py`), permutation groups (`groups.py`), kG-modules + minimal
free resolutions + Ext (`modules.py`). `driver.py`, `driver2.py` run 17 cases.

**LHS** (independent): minimal free resolution of `k[G/A]` over `kG`, then `H^n Hom_{kG}(F_•,k[G/B])`.
**RHS**: Mackey double cosets `A\G/B`, each `H^*(A∩gBg⁻¹;k)` via its own `kH`-resolution.

All 17 cases agree; `dim Ext⁰ = |A\G/B|` throughout. The direct LHS pins the Mackey index as
`A∩gBg⁻¹` (not `gAg⁻¹∩B`). Key rows:
- V₄ transverse [1,0,0,0]; V₄ self [2,2,2,2]; S₃ self [2,1,1,1] (mixed); A₄/V₄ [3,6,9,12].
- D₄ [3,2,2,2]/[4,4,4,4]; S₄/⟨(12)⟩ [7,2,2,2]; ℤ/3 p=3 [1,1,1,1] and [3,0,0,0].
- Holonomy W1 (S₃=A₃·⟨(12)⟩, U=⟨(23)⟩): [2,0,0,0], Ext⁰=h=2.
- Holonomy W2 (S₄=A₄·⟨(12)⟩, U=S₃, A=A₃, B={e}): [2,0,0,0], h=2>1 but tower ≡0 — DECISIVE.

Run: `python3 driver.py` and `python3 driver2.py`.
Backs `proofs/2026-08-20-emergent-holonomy-is-ext-tower.md`.
