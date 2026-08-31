# D₈ non-abelian Ext tower — computation record

Engine: `gen_d8.py` (general finite-group F₂ homological engine). Driver `run_d8.py`,
resolution validator `validate_resolution.py`. `k=F₂`, `D₈=⟨r,s|r⁴=s²=e,srs=r⁻¹⟩`.

Method: TWO independent computations per case.
1. **Direct** — minimal free resolution of `k[G/A]` over `k[D₈]` (syzygies via Nakayama:
   minimal generators = lift of a basis of `M/JM`, `J`=augmentation ideal), then
   `H^n Hom_{kD₈}(P_•, k[G/B])`.
2. **Mackey/Shapiro** — double cosets `A\G/B`, each `A∩gBg⁻¹`, sum `⊕_g H^n(A∩gBg⁻¹)`.

## Results (Ext^0..6), all MATCH:

| A | B | #cosets h | intersections | Ext^0..6 |
|---|---|---|---|---|
| G | G | 1 | D₈ | [1,2,3,4,5,6,7]  (= dim H*(D₈;F₂)=n+1) |
| ⟨r²,s⟩ | ⟨r²,rs⟩ | 1 | Z=⟨r²⟩ | [1,1,1,1,1,1,1]  (COLLAPSE: both normal) |
| ⟨s⟩ | ⟨s⟩ | 3 | ⟨s⟩,{e},⟨s⟩ | **[3,2,2,2,2,2,2]** (deg0=3 > tower=2) |
| ⟨s⟩ | ⟨rs⟩ | 2 | {e},{e} | [2,0,0,0,0,0,0] |
| ⟨r²,s⟩ | ⟨s⟩ | 2 | ⟨s⟩,⟨r²s⟩ | [2,2,2,2,2,2,2] |
| ⟨r⟩=C4 | ⟨s⟩ | 1 | {e} | [1,0,0,0,0,0,0] |

`run_d8.py`: 6/6 direct == Mackey. `validate_resolution.py`: all resolutions exact
(`d∘d=0`, `ker dₙ = im dₙ₊₁` in positive degrees). D₈ mult table verified a group.

Full analysis: `proofs/2026-08-21-d8-nonabelian-ext-tower.md`.
