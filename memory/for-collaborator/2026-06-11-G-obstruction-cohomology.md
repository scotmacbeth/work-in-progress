# The (G) closure obstruction IS a cohomology class: holonomy = H²(Sk_C; 𝒟)

**Date:** 2026-06-11 (deep-work prove session)
**For:** Robin, Neil
**Builds on:** the two-level criterion (`2026-06-10-zs-criterion-cocycle.tex`,
`2026-06-10-pairwise-zs-criterion.tex`) and the rigid-twist holonomy
([[zs-closure-holonomy]], [[pairwise-zs-criterion-proved]]).
**Artifact:** `projects/proofs/2026-06-11-G-obstruction-cohomology.tex` (7pp, compiles).
**Script:** `projects/scratch/cohomology_holonomy.py` (all claims machine-checked).

## TL;DR

Last cycle I proved (G) — the closure of the free bases into a wide subcategory C —
is "a global holonomy obstruction" but only *described* it. **This cycle I
classified it.** Under a clean hypothesis it is a genuine **abelian degree-2
cohomology class** of an explicit small-category complex, and

> **(G) holds  ⟺  [ω] = 0  ∈  H²(Sk_C ; 𝒟).**

The rigid twist computes **H² ≅ Z/2 with [ω] = the nonzero generator** — fully
explicit, by hand and by machine. The SEED-Q2 conjecture's "cohomological holonomy"
framing is therefore **correct in the abelian regime**, and I found the exact line
past which it goes nonabelian.

## What's proved (Theorem, under hypothesis (H))

(H) = (i) D a disjoint union of **abelian** vertex groups G_a = Aut_D(a) [= the
single-category case, D=E with invertible endos]; (ii) **trivial left action**:
postcomposition by any target automorphism preserves D-orbits.

The objects:
- **Sk_C** = the *orbit category*: objects = ob K, morphisms = free D-orbits, with
  composition o₂∗o₁ = orbit(c₂∘c₁). It is a genuine category **exactly because**
  (H)(ii) makes orbit-composition rep-independent.
- **𝒟 : Sk_C^op → Ab**, a ↦ G_a — a presheaf of abelian groups (the residual torsor
  of basis choices), restriction maps φ_c from the right-action.
- **Defect ω_T** (general, no hypothesis): fix a transversal T; for composable
  generators, c₂∘c₁ = ⌊c₂c₁⌋_T ∘ ω_T(c₂,c₁), ω ∈ D. **(G) ⟺ ω ≡ id** (pure
  unwinding of "C closed").

The theorem:
1. ω_T is a normalized **2-cocycle** (δ²ω=0). Proof = factor c₃c₂c₁ two ways, read
   off the D-part by uniqueness. The cocycle identity is literally
   ω(c₃,⌊c₂c₁⌋)+ω(c₂,c₁) = ω(⌊c₃c₂⌋,c₁)+φ_{c₁}(ω(c₃,c₂)).
2. Re-choosing the transversal: **ω_{T·h} = ω_T + δ¹h** (a coboundary). The gauge
   group IS C¹(Sk_C;𝒟) acting freely transitively on transversals.
3. ⟹ [ω] ∈ H²(Sk_C;𝒟) is **transversal-independent**, and **(G) ⟺ [ω]=0**.
4. The set of SFS (C,D), when nonempty, is a **torsor under Z¹**; modulo inner
   relabelings B⁰, a **torsor under H¹**. (Exactly the H¹/H² pattern Neil's
   trigger conjectured.)

## The rigid twist, fully explicit

Sk_C = the branch  a →[p] x ⇉[s,s₂] y  with [s][p]=[q]=[s₂][p]; 𝒟 = Z/2 at a, 0
elsewhere; all restriction maps 0. Then C³=0 (y is a sink), Z²=(Z/2)², B²=diagonal
⟨(1,1)⟩ (image of δ¹: δ¹h([s],[p])=h([p])−h([q])=δ¹h([s₂],[p])), so

> **H²(Sk_C;𝒟) = (Z/2)² / ⟨(1,1)⟩ ≅ Z/2**, and ω_T = (0,1) ∉ B² ⟹ [ω] = generator.

This is the seed obstruction, now a bona fide H² class. The **pairwise 4-object**
enlargement (cross arrow d: w→a, so D is *not* a groupoid) sits outside (H)(i) but
gives the **identical Z/2 class** — strong evidence (H)(i) can be relaxed to
"defect group-valued + trivial left action."

## The honest boundary (the next theorem)

(H)(ii) is the real line. Two-morphism witness (a→b, G_b=Z/2={1,h}, Hom(a,b)={t,ht}):
the target automorphism h **swaps the two orbits**, h∘t = ht ∉ orbit(t). There
orbit-composition doesn't descend, Sk_C is not a category, 𝒟 doesn't exist, and the
gauge transformation of ω mixes the left and right actions → **genuinely nonabelian**.

**Conjecture (nonabelian holonomy):** in general the SFS are classified by a
*nonabelian* H² of the Rosebrugh–Wood distributive law λ — band = the
left-action-twisted presheaf-of-groups, obstruction in H² of that band, torsor of
λ's acted on by H¹. This is the categorical **Kac/Masuoka** matched-pair extension
story. That's the clean open continuation.

## Computational confirmations (cohomology_holonomy.py)

- Rigid twist: (L)✓, no closure, H²=Z/2, all 4 transversals = same nonzero class.
- Triple chain a→x→y→z (no twist): C³≠∅, **δ²∘δ¹=0 verified**, H²=0, closure exists;
  KEY — 6/8 transversals have ω≠0 but [ω]=0: **the obstruction is [ω], not ω**.
- Pairwise 4-obj (non-groupoid D): H²=Z/2, same class — robustness beyond (H)(i).
- Nonabelian witness: h∘t ∉ orbit(t) exhibited.

## Grant hook

(G) is upgraded from "a search" to "a computable invariant": after the cheap local
test (L), strict factorization exists **iff one cohomology class vanishes**;
dim H² measures *how* obstructed; H¹ enumerates the factorizations. In ga-containers:
"diversity collapse W=1.0" = "the cohomology class vanishes," now literal.

## Where to push back / what I want eyes on

- Is the relaxation of (H)(i) to "group-valued defect + trivial left action" clean?
  The pairwise example says yes; I haven't written the general proof.
- The nonabelian conjecture — is the right object Baues–Wirsching cohomology of
  Sk_C with a *nonabelian band*, or genuinely the Kac exact sequence of λ? Neil,
  this is your matched-pair territory.
