# Groupoid-base Zappa–Szép merge obstruction — REFUTATION + correct criterion

**Date:** 2026-07-24 (deep-work PROVE)
**Artifacts:** `proofs/2026-07-24-groupoid-zs-obstruction.tex` (7pp, compiles) ·
`scratch/groupoid-zs/groupoid_zs.py`, `dcont_check.py` (all machine-checked) ·
registry `proofs/registry/groupoid-zs-obstruction.json` (valid, computed).

## The question
Every prior ZS-merge obstruction `[ω]∈H²(Sk_C;𝒟)` was over an **acyclic** base
(orchestration, supply chain, olog) → finite `ℤ/2`/`ℤ/n`. Open: when the base is a
**groupoid** (all morphisms invertible), is `[ω]` forced to vanish? Seed conjecture:
*connected groupoid ⟹ Sk_C contractible ⟹ H²=0 ⟹ always merges.*

## The answer: the conjecture is REFUTED (its reason is wrong)
A connected groupoid is **not contractible** — it is a `K(Γ,1)` for its vertex group
`Γ`. So `H²(Sk_C;𝒟) ≅ H²(Γ;M)` is honest **group cohomology**, generally nonzero.

**The broken assumption:** "every object iso to every other" (true in a connected
groupoid — collapses the *objects*) was silently equated with "classifying space is a
point" (needs the *vertex group* trivial too). Invertibility collapses objects, not loops.

## The exact identification (this is the pretty part)
Over a **one-object groupoid base** (K a group, D≤K abelian) under (H):
- (L) always holds; (H)(ii) ⟺ **D normal**; then `Sk_C = K/D =: Γ`, `𝒟 = D` as a
  Γ-module by conjugation.
- The ZS defect `ω_T` **is the Schreier factor set** of `1→D→K→Γ→1`, so
  `[ω]∈H²(Γ;D)` is the **group-extension class**.
- `K = C⋈D` exists ⟺ the extension **splits** ⟺ D has a **complement** ⟺ `[ω]=0`.
- `#(strict factorizations) = #(complements of D in K)`.

So over a groupoid base, **ZS-merge obstruction = classical group-extension obstruction**.
(D normal ⟹ the ZS product is the internal semidirect product; the holonomy is Schreier's H².)

## Machine-checked witnesses (`groupoid_zs.py`)
| K | base Sk_C | D | dim H² | #compl | verdict |
|---|---|---|---|---|---|
| codiscrete •⇄• | 1 (contractible) | id | 0 | 1 | merges |
| **ℤ/4** | **B(ℤ/2)** | ℤ/2 | 1 | **0** | **OBSTRUCTED** |
| ℤ/2×ℤ/2 | B(ℤ/2) | ℤ/2 | 1 | 2 | merges (split) |
| **Q8** | **B((ℤ/2)²)** | ℤ/2 | 3 | **0** | **OBSTRUCTED** |
| ℤ/6 | B(ℤ/2) | ℤ/3 | — | 1 | merges (Schur–Zassenhaus) |

`ℤ/4 ⊇ ℤ/2` is the headline: connected groupoid base, `[ω]` = generator of
`H²(ℤ/2;ℤ/2)=ℤ/2`, **no merge**. (C) shows same base groupoid + *split* total ⟹ merges:
`[ω]` depends on K, not on the base alone. The F2 bar complex uses the **correct**
restriction maps `φ = conjugation` (Lemma: over a groupoid `φ_c` is an *isomorphism*, not
the acyclic `φ=0`); it reproduces `H²(ℤ/2;ℤ/2)=ℤ/2` and `H²((ℤ/2)²;ℤ/2)=(ℤ/2)³`.

## The CORRECT positive theorem (rescues the application)
`cd(Sk_C) ≤ 1 ⟹ [ω]=0 for every D ⟹ merge always exists`. In particular **free
groupoids** (free vertex groups) always merge, because `cd(free group) ≤ 1`
(**Stallings–Swan**: cd≤1 ⟺ free), so `H^{≥2}(free;M)=0` for *all* M.

**Dividing line is cohomological dimension (freeness), NOT invertibility.**
- Γ free (cd≤1): always merges. [PROVED, general]
- Γ=1 (contractible, e.g. codiscrete): merges — the conjecture's *true* subcase.
- Γ torsion: can obstruct (ℤ/4, Q8). [COMPUTED witnesses]

## Grant / social-network line (grade: computed)
Mutual-tie network = **free groupoid** on the friendship graph (π₁ of a graph is free)
⟹ cd≤1 ⟹ **always merges** — but for the right reason (dimension 1, not contractibility).
Follows-graph = free *acyclic category* ⟹ earlier `[ω]=ε∈ℤ/n` can obstruct. A **torsion
identification** (finite non-free loop) can obstruct even mutual ties.
**Corrected Impact headline:** *reversibility alone does not guarantee two platforms merge —
**freeness** does.*

## Honesty / firewall
- Group extensions + H² classification are **classical** (Schreier; Mac Lane/Brown).
  BW `H²(BΓ;M) = ` group cohomology is standard. Cited, not claimed.
- Groupoid ZS products **exist** (Mundey–Sims, self-similar groupoids) on the
  *completeness* axis — cited adjacent, **not scooped**. Our axis is existence/obstruction.
- Contribution = placing the groupoid case in the ZS-merge program + the refutation +
  isolating `cd≤1` (freeness) as the trivialising condition.
- Object-level "a real network *is* this groupoid" stays **OPEN (SEED Q4)**.

## Open next
Nonabelian regime (D non-normal = genuine two-sided matched pair, not semidirect) →
nonabelian H² of the matched pair (Kac/Pirashvili, already cited). Not entered.
