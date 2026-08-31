# Ext deg-0 − Ext¹ table: the aligned (zero-transverse) regime + the rank≥2 negative stratum

**Date:** 2026-08-27 (material-increment; system clock ~08-23).
**Engine:** `/home/agent/projects/scratch/ext-mackey-general/` (`groups.py`, `modules.py`, `fp.py`, drivers).
**Reproduce:** `cd /home/agent/projects/scratch/ext-mackey-general && python3 table_driver.py`
**Cross-check:** every row computes Ext two independent ways — direct minimal `kG`-resolution (LHS)
vs Mackey/Shapiro sum `⊕_g H*(A∩gBg⁻¹)` (RHS). **All rows MATCH=True.** All over F₂.

Answers Rick's corrected ask (email 2026-08-23, uid 117): does my side give `(deg-0 − dim Ext¹) = 0`
in the aligned / no-transverse-coset regime, matching his 0 top-weight cancellations for b=2,3,4?
**Yes.**

## Required cases (tower to degree 4)

| G  | A | B | h=\|A\G/B\| | Ext⁰ | Ext¹ | Ext⁰−Ext¹ | #transverse | tower Ext⁰‥⁴ |
|----|---|---|------------|------|------|-----------|-------------|--------------|
| D₈ | ⟨s⟩ (refl) | ⟨s⟩ | 3 | 3 | 2 | **1** | 1 | [3,2,2,2,2] |
| D₈ | G | G | 1 | 1 | 2 | −1 | 0 | [1,2,3,4,5] |
| V₄ | G | G | 1 | 1 | 2 | −1 | 0 | [1,2,3,4,5] |
| V₄ | ⟨a⟩ | ⟨a⟩ | 2 | 2 | 2 | **0** | 0 | [2,2,2,2,2] |
| V₄ | ⟨a⟩ | ⟨b⟩ | 1 | 1 | 0 | 1 | 1 | [1,0,0,0,0] |

## Zero-difference (fully aligned) witnesses — the answer to Rick

Every double coset has a nontrivial rank-1 (order-2) intersection ⟹ Ext¹ = Ext⁰, #transverse = 0.

| G  | A | B | h | Ext⁰ | Ext¹ | Ext⁰−Ext¹ | #trans |
|----|---|---|---|------|------|-----------|--------|
| D₈ | ⟨(13)(24)⟩ = **center** | center | 4 | 4 | 4 | **0** | 0 |
| D₈ | ⟨(24)⟩ | ⟨(24),(13)⟩ (ord4) | 2 | 2 | 2 | 0 | 0 |
| D₈ | G | ⟨(13)⟩ | 1 | 1 | 1 | 0 | 0 |
| V₄ | ⟨a⟩ | ⟨a⟩ | 2 | 2 | 2 | 0 | 0 |
| V₈ | ⟨(56)⟩ | ⟨(56)⟩ | 4 | 4 | 4 | 0 | 0 |

**Sharpest 0:** D₈, A=B=center: h=4, tower **[4,4,4,4,4]**, diff=0 — the central involution sits in
the intersection of ALL four double cosets ("shared involution across every coset").

## Sweep summary (all MATCH=True)

Full unordered subgroup-pair sweeps: D₈ (55 pairs), V₄ (15), V₈=(Z/2)³ (120). `(Ext⁰−Ext¹)` partitions
cleanly by intersection rank:
- **diff = #transverse > 0** — at least one transverse (trivial-intersection) coset. (All
  `A=B=⟨reflection⟩` give diff=1; `A=B={e}` gives diff=|G|, the regular rep, fully transverse.)
- **diff = 0** — every coset has a rank-1 nontrivial intersection (tables above).
- **diff < 0** — some intersection has rank ≥ 2 (order-4 subgroup or full G), so dim Ext¹ ≥ 2 > Ext⁰.
  These rows are **outside the rank-1 dictionary hypothesis**.

**Dictionary confirmed on every rank-1 row:** `dim Ext⁰ = h = |A\G/B|` universally, and
`(dim Ext⁰ − dim Ext¹) = #{transverse double cosets}` wherever the nontrivial intersections are rank-1.

## The discriminating test proposed to Rick

Match-at-zero can be coincidence. The correspondence #{cancelling weight-b pairs} = #{transverse
double cosets} is only genuinely tested on a **nonzero** witness. On my side, one transverse coset
(e.g. D₈ A=B=⟨s⟩) gives diff=1. Test: Rick constructs a `b` with exactly one top-weight cancelling
pair; I supply the (G,A,B) with exactly one transverse coset; check the counts track (1,2,…). Match on
nonzero = real correspondence; disagreement = analogy dies cleanly.
