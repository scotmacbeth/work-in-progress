# Does invertibility kill the Zappa–Szép merge obstruction? (the groupoid case)

**Deep-work PROVE, 2026-07-24.** Companion to the full write-up
`2026-07-24-groupoid-zs-obstruction.tex` (7pp). Scripts: `scratch/groupoid-zs/`.

## Problem
All prior instances of the ZS-merge obstruction `[ω]∈H²(Sk_C;𝒟)` were computed over
**acyclic** bases → finite `ℤ/2`, `ℤ/n`. Open question: when the base category presented
by the directed container is a **groupoid** (every morphism invertible), is `[ω]` forced
to vanish? Seed conjecture: *connected groupoid ⟹ Sk_C contractible ⟹ H²=0 ⟹ always
composes.*

## Solution (verdict: conjecture REFUTED; corrected criterion PROVED)

**1. The reason is broken.** A connected groupoid is **not contractible** — it is a
`K(Γ,1)` for its vertex group `Γ`. Hence `H²(Sk_C;𝒟) ≅ H²(Γ;M)` is genuine **group
cohomology**. (The tacit error: "all objects isomorphic" collapses the *objects* of the
skeleton but not the *loops*; the loops are the `H^{≥1}`.) Over a groupoid the restriction
maps `φ_c` become **isomorphisms** (Lemma), so `𝒟` is a true local system/module — unlike
the acyclic case where `φ=0`.

**2. Exact identification (one-object groupoid base).** Take `K` a group, `D≤K` abelian.
Then (L) holds automatically; (H)(ii) ⟺ **D normal**; and `Sk_C = K/D =: Γ`, with `𝒟=D`
the Γ-module by conjugation. The ZS **defect `ω_T` is precisely the Schreier factor set**
of the extension `1→D→K→Γ→1`, so `[ω]∈H²(Γ;D)` is its **extension class**. Therefore
```
K = C⋈D exists  ⟺  extension splits  ⟺  D has a complement  ⟺  [ω]=0,
#(strict factorizations) = #(complements of D in K).
```
So **over a groupoid base the ZS-merge obstruction = the classical group-extension
obstruction.** (D normal ⟹ the ZS product is the internal semidirect product.)

**3. Refutation (witnesses).**
- `K=ℤ/4, D=⟨2⟩≅ℤ/2`: base `Sk_C=B(ℤ/2)` is a connected groupoid, but the only order-2
  subgroup is `D` itself → **no complement → `[ω]` = generator of `H²(ℤ/2;ℤ/2)=ℤ/2` ≠ 0
  → OBSTRUCTED.**
- `K=Q8, D=Z(Q8)≅ℤ/2`: base `B((ℤ/2)²)`, every subgroup contains `-1` → no complement →
  `[ω]≠0` in `H²((ℤ/2)²;ℤ/2)=(ℤ/2)³` → OBSTRUCTED.
- `K=ℤ/2×ℤ/2, D=⟨(1,0)⟩`: **same** base groupoid `B(ℤ/2)`, but split → `[ω]=0`, merges.
  (So `[ω]` depends on `K`, not on the base groupoid alone.)

**4. Correct positive theorem.** `cd(Sk_C) ≤ 1 ⟹ [ω]=0 for every D ⟹ merge always
exists.` In particular **free groupoids** always merge: `cd(free group) ≤ 1`
(**Stallings–Swan**: cd≤1 ⟺ free) ⟹ `H^{≥2}(free;M)=0` for all `M`.

**Dividing line = cohomological dimension (freeness), not invertibility:**
- Γ free (cd≤1): always merges [PROVED, general].
- Γ=1 (contractible, e.g. codiscrete •⇄•): merges — the conjecture's *true* subcase.
- Γ torsion: can obstruct [COMPUTED: ℤ/4, Q8].

**5. Application (grade: computed).** Mutual-tie network = free groupoid on the friendship
graph (π₁ of a graph is free) ⟹ cd≤1 ⟹ **always merges** — but by *dimension 1*, not
contractibility. Follows-graph = free acyclic category ⟹ earlier `[ω]=ε∈ℤ/n` can obstruct.
A torsion identification can obstruct even mutual ties. Corrected Impact line:
**reversibility alone doesn't guarantee a merge — freeness does.**

## Verification
`scratch/groupoid-zs/groupoid_zs.py`: builds each K, checks (L),(H), computes
`Sk_C=K/D`, `#complements` (= #strict factorizations, cross-check), and an F2 bar complex
with the **correct** `φ=conjugation`. Reproduces `dim H²`: 0 (codiscrete), 1 (ℤ/4 ✱, ℤ/2²),
3 (Q8, i.e. `|H²|=8` matching `ℤ/2[x,y]`); `#complements` 1/0/2/0/1; `δ²δ¹=0` on the
now-nonvacuous C³. `dcont_check.py`: D1–D5 for all bases (DCont≃Cat). All pass.

## Gaps / scope
- **Classical core, cited not claimed:** group extensions ↔ H² (Schreier; Mac Lane/Brown);
  `H²(BΓ;M)=`group cohomology (standard). Novelty = placing groupoid case in the ZS-merge
  program + refutation + `cd≤1` criterion.
- **Adjacent, not scooped:** groupoid ZS products exist (Mundey–Sims, self-similar
  groupoids) on the *completeness* axis; ours is the *existence/obstruction* axis.
- **OPEN (SEED Q4):** object-level fidelity ("a real network *is* this free groupoid").
- **Not entered:** nonabelian regime (D non-normal = genuine two-sided matched pair) →
  nonabelian H² of the matched pair (Kac/Pirashvili, cited).
