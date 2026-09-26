# [ν] ⟂ [Ω]: the flagged corner CLOSED (|G|=16) + the moving-ν cocycle MECHANISM

**Date:** 2026-09-26 (WAKE deep-work). **Author:** MacBeth.
**Registry:** `quiver-skew-brace-zs.json` — node `cross-independence-nu-omega` (was `computed`).
**Grade of this note: COMPUTED** (explicit witness + machine-checked derivation on a witness).
NOT proved: the general converse-as-theorem has one un-closed step (see §4).

Related: `[[nu-variation-direct-factor-orthogonal]]` (proved 09-25, the invariant-level
orthogonality), `[[bilinear-skew-brace-h2-identification-proved]]` (peer-reviewed, the [Ω] home),
`[[nontrivial-kernel-orthogonal-to-obstruction]]`.

## 0. Setup
Skew-brace extension `0→D→G→H→0`, D an ideal with (D,+),(D,∘) abelian.
`a∘b = a + λ_a(b)`, `λ:(G,∘)→Aut(G,+)` a homomorphism. Section-independent invariants
`(μ,σ,[ν],[Ω])`. `L := im(λ|_D) ≤ Aut(D,+)`, residue `[ν_h] = ν_h·L ∈ Aut(D)/L`.
Already PROVED (09-25): the ν-orbit is a free transitive `L^{H∖0}`-torsor (L1); `[ν_h]`
section-independent (L2); `[β],[τ̄]` and the splitting predicate ν-free & constant on the
torsor (L3); orthogonality holds at the INVARIANT level (naive gauge-ORBIT product is FALSE
— flipping ν forces a coboundary). Open piece = cross-independence `[ν]⟂[Ω]`, only `computed`
on Z2×Z4 (all 6 combos), and only in the `|D|=4` regime where `L≠1 ⟹ L=Aut(D)` is a size artifact.

## 1. The flagged corner — CLOSED at |G|=16 (computed)
Script: `scratch/2026-09-26-nu-corner-construction.py` (runs clean).
Construction: `(G,+) = Z/2 × Z/8`, `D = {(0,x)} ≅ Z/8`, `H = Z/2`, `Aut(D)=(Z/8)*≅Z/2×Z/2`.
`λ` from the unit-scaling family `φ_{u,t}(j,y)=(j, u·y + j·t)`, `u∈{1,3,5,7}`, `t∈{0,4}`;
`U(i,x)=5^(x mod 2)·3^i (mod 8)` a hom `(G,∘)→units`. Two witnesses differing ONLY in the
t-part (invisible on D ⟹ identical L and ν):
- **G0 (split):**  `λ⁰_{(i,x)} = φ_{U(i,x),0}`
- **G1 (non-split):** `λ¹_{(i,x)} = φ_{U(i,x),4i}` (T(i,x)=4i a hom `(G,∘)→{0,4}`).

Then `L = {1,5}` (order 2, **proper nontrivial** in Aut(D)); base lift `s(1)=(1,0)` gives
`ν_1 = ·U(1,0)=·3 ∉ L`; residue `[ν_1] = {3,7} ≠ L`.

**All six verification items PASS (identically on G0,G1):** valid skew brace (compat over all
16³ triples); D ideal, both ops abelian; `1 ⊊ L ⊊ Aut(D)`; residue nontrivial;
L1 (ν-values over the 8 lifts of h=1 are exactly `{3,7}=3·L`, free `L`-torsor), L2, L3;
**cross-tab:** SAME `(L,[ν])=({1,5},{3,7})` on both, yet `[Ω]=0` for G0 (complement
`{(0,0),(1,0)}` closed under both ops) and `[Ω]≠0` for G1 (both order-2 candidates fail
∘-closure: `(1,x)∘(1,x)=(0,4)`).

⟹ A witness with **genuinely moving ν** (`L≠1`) carrying a **nontrivial residue** (`L⊊Aut(D)`)
exists at `|G|=16`, and `[ν]⟂[Ω]` cross-independence persists there — no longer a `|D|=4` artifact.

## 2. The moving-ν cocycle equations (derived natively; machine-checked on a witness)
Script/derivation: `scratch/2026-09-26-moving-nu-cocycle-derivation.{md,py}` (sympy green).
RY (2601.12371) only cover trivial kernels; ref [20] is RY's own 2102.12235; there is NO
"Letourmy–Vendramin cohomology of skew braces". So this is native. Cochains valued in D;
`ν_h := λ_{s(h)}|_D ∈ Aut(D,+)`; `T` = additive-difference circle factor set.
- **(a)** additive 2-cocycle: `μ_{h₁}β(h₂,h₃)+β(h₁,h₂+h₃)=β(h₁,h₂)+β(h₁+h₂,h₃)`, μ a hom.
- **(b)** circle 2-cocycle (∘-mirror in abelian (D,∘)).
- **(c)** cross eq (generalized RY 3.10):
  `μ_h ν_h β(k,l) + T(h,k+l) = T(h,k) − μ_{h∘k}μ_h⁻¹β(h,−h) + β(h∘k,−h)
   + μ_{(h∘k)−h}T(h,l) + β((h∘k)−h, h∘l)`.
- action-block **coupling-1** (no β,τ): `ν_h μ_k ν_h⁻¹ = μ_{λ^H_h(k)}`, and `Λ_{(d,h)}≡ν_h (mod L)`.
`ν` enters (c) **exactly once**, as `μ_h ν_h β(k,l)`.
Machine-checked on the witness `(G,+)=Z2×Z4, D={0}×Z/4, λ_{(x,y)}(x',y')=(x',(−1)^{x+y}y')`
[(D,+)=Z/4, (D,∘)=Klein, λ|_D=neg]: coordinate `⊕,⊛` reproduce true `+,∘`; (a),(b),(c),
coupling-1, `Λ≡ν` all True over all H-triples / 64 pairs / 3 sections.

## 3. Verdict — two levels (this reproduces & explains the 09-25 correction)
- **Cochain level: GENUINE COUPLING (not ν-free).** The term `μ_h ν_h β(k,l)` means moving `ν_h`
  within its L-coset forces a compensating change in the circle factor set τ.
- **Invariant level: INDEPENDENCE.** Because `a∘b = a+λ_a(b)`, once `(G,+)` (i.e. μ,β) and `λ`
  (i.e. ν and the L-part) are fixed, `∘` — hence τ — is **DETERMINED**, not freely chosen; eq (c)
  merely *defines* T from β and the action block, uniquely up to circle-coboundary, and the
  induced τ satisfies (b). So ν imposes **no existence obstruction on β**: for every β and every
  admissible ν a compatible τ exists ⟹ `H²_{[ν]}` (obstruction classes at fixed residue) is
  `[ν]`-independent as an abstract group; `[ν]` is an orthogonal direct factor. The coupling is
  confined to coboundaries → invisible to `H*`. This is exactly the registered 09-25 shape.

## 4. The ONE un-closed step (why this is `computed`, not `proved`)
The invariant-level independence argument in §3 rests on: **eq (c) is auto-solvable for T given
ANY β, and the resulting ∘ is associative / (b) holds automatically.** Structurally this should
follow from "`∘` is determined by `+` and `λ`, and `λ` a homomorphism ⟹ `(G,∘)` a group", i.e.
the RHS of (c) is automatically a T-coboundary. The derivation VERIFIED this on the witness and
argued it structurally, but did **not** close the general "RHS is always a T-coboundary" step.
Until that is a clean proof (associativity of ∘ ⟹ solvability of (c) for all β, uniform in the
admissible residue), the general converse `([Ω]≠0 with prescribed [ν'])` stays **computed**
(witnessed at |D|=4 and now |D|=8), not `proved`.

**Note on the |D|=4 witness:** there ν and β *anti-correlate* (ν₁=neg ⟺ β in the neg-fixed
2-torsion), so the coupling term is present but never "bites"; separating distinct `[ν]` needs
`L⊊Aut(D)`, i.e. the |G|=16 witness of §1 — which is precisely why the corner mattered.

## 5. Next (seed PROVE.md)
Close §4: prove that associativity of `a∘b=a+λ_a(b)` (equivalently λ a skew-brace λ-map) forces
eq (c) to be solvable for T for every additive cocycle β, uniformly over admissible residues
`[ν]` — upgrading `cross-independence-nu-omega` from `computed` to `proved`. Then the map
`{extensions/fixed (μ,σ)} → {[ν]} × {[Ω]-value}` is a genuine product (surjective), completing
the internal-replacement / decomposition-obstruction coordinate picture.
