# The Zappa–Szép criterion is two-level: freeness is not enough

**Date:** 2026-06-10 (deep-work prove session)
**For:** Robin, Neil
**Builds on:** the freeness criterion (`2026-06-09-two-atoms-zappa-szep.tex`) and
the airtight collage reconstruction (`2026-06-10-collage-reconstruction.tex`).
**Artifact:** `projects/proofs/2026-06-10-zs-criterion-cocycle.tex` (8pp, compiles).
**Scripts:** `zs_cocycle_check.py`, `zs_converse_check.py`,
`zs_closure_counterexample.py` (all in `projects/scratch/`).

## TL;DR

I set out to make the single-category Zappa–Szép criterion airtight and to extract
the explicit cocycle. Got both — and on the way found a **second broken
assumption**, mirroring the first.

- **First correction (last cycle):** a category is *not* a ZS product of
  poset + endo-monoids in general; the fix is **freeness** of each connecting
  biset `Hom(a,b)` over `End(a)`.
- **Second correction (this cycle):** even **freeness of every hom is not
  sufficient** for a ZS product. You also need the transversal to *close up into a
  subcategory*, and that closure carries a genuine **global holonomy obstruction**.

So SEED-Q2's natural reading — "C is a ZS product ⟺ every `Hom(a,b)` is free over
`End(a)`" — is **half false**. The ⟹ direction holds; the ⟸ direction fails.

## The good news: the cocycle and the matched-pair axioms

When `C = T ⋈ E` does hold (E = endomorphism subcategory, T a transversal
subcategory, unique factorization `f = t∘e` with `e ∈ End(src)`), the Zappa–Szép
mutual action is read straight off composition. For `e ∈ End(b)`, `t ∈ T(a,b)`:

    e ∘ t  =  ({}^e t) ∘ (e^t),     {}^e t ∈ T(a,b),   e^t ∈ End(a).      (★)

Postcomposing by a target loop `e` **permutes the transversal** (`{}^e t`) and
**twists the source loop part** (`e^t`). This `(T, {End(x)}, {}^e t, e^t)` is a
**matched pair of categories**, and the four Brin axioms

    ZS1: {}^e(t₂∘t₁) = {}^e t₂ ∘ {}^{e^{t₂}}t₁          (left action on a product)
    ZS2: {}^{e'e} t   = {}^{e'}({}^e t)                  (left action of End on T)
    ZS3: (e'e)^t      = (e')^{ {}^e t } · e^t            (restriction of a product)
    ZS4: e^{t₂∘t₁}    = (e^{t₂})^{t₁}                    (right action of T on End)

**hold if and only if C is associative.** The proof is clean: compute `e∘(t₂∘t₁)`
and `(e₂e₁)∘t` two ways each; uniqueness of factorization splits each associativity
instance into its T-coordinate (giving ZS1/ZS2) and its End-coordinate (giving
ZS3/ZS4). Conversely abstract matched-pair data assembles to a category (direct
associativity computation, both bracketings). Machine-verified on groupoid Z/2,
chains, the commutative square, Z/n, and source-loop torsors: every ZS axiom passes.

This is the explicit Brin/Zappa–Szép cocycle the roadmap wanted, and it gives the
sharp per-subcategory theorem: **`C ≅ T ⋈ E` ⟺ each `T(a,b)` is a free basis of
`Hom(a,b)` over `End(a)`** — note both sides presuppose T is a *subcategory*.

## The catch: the rigid-twist counterexample (10 morphisms)

The presupposition "T is a subcategory" is doing real work. Drop it and ask only
for objectwise freeness, and the criterion fails. Minimal witness:

    Objects a, x, y.   End(a) = {1, g}, g²=1.   End(x) = End(y) = trivial.
    Hom(a,x) = {p, pg=p·g}     (one free End(a)-orbit)
    Hom(x,y) = {s, s₂}          (two singleton orbits — End(x) trivial)
    Hom(a,y) = {q, qg=q·g}     (one free End(a)-orbit)
    RIGID TWIST:  s∘p = q,   s₂∘p = qg.    (⟹ s∘pg=qg, s₂∘pg=q)

This is a valid category (associativity machine-checked). **Every hom is free over
its source endomorphism monoid.** Yet there is **no closed transversal**: because
`End(x)` is trivial, `T(x,y) = {s, s₂}` is *forced* (both are their own orbit), and
closure demands both `s∘t` and `s₂∘t` land in `T(a,y)` — but those are `q` and `qg`
(the *whole* orbit, two elements), while `T(a,y)` holds only one. All four
admissible choices fail. The twist is **rigid**: re-choosing `p ↦ pg` shifts *both*
composites by `g` simultaneously, so no choice ever separates them. It is a
one-dimensional **Z/2 holonomy** around the branched path `a → x ⇉ y`.

Why this is the minimal shape: you need a nontrivial source endo (else no torsor of
choices — each `T(c,d)` is forced to the whole hom-set, trivially closed) and a
*branch* (two transversal arrows out of the middle object into the same target
orbit), hence ≥ 3 objects. Directed cycles in the shape don't help the obstruction:
a cycle forces its arrows to be mutually inverse isos (groupoid case), which always
splits. The obstruction is a genuine feature of **non-invertible, acyclic shape with
loop decorations**.

## Corrected SEED-Q2 (single category) — the decision procedure

`C` admits a source-oriented ZS decomposition over its endomorphisms **iff**

  **(L) local freeness:** every `Hom(a,b)` is free as a right `End(a)`-set
       — finitely checkable; quick pre-test `|End(a)| ∣ |Hom(a,b)|`; **AND**
  **(G) global closure:** the per-orbit representatives can be chosen to form a
       wide subcategory — i.e. the holonomy obstruction vanishes — decidable by
       searching the finite product of orbit-rep systems for a closed one.

Hierarchy of decompositions: **collage** (always, unconditional) ⊋ **free collage**
(L) ⊋ **Zappa–Szép product** (L ∧ G).

## Why this matters for the grant

- The "checkable criterion" promised for SEED-Q2 is real but **two-level**: cheap
  local freeness test + a global closure search. An honest decomposition algorithm
  must run both; reporting only (L) would wrongly accept the rigid-twist category.
- The rigid twist is the finite, computable shadow of the **laxator obstruction**
  in the ga-containers (ACT 2026) framing — freeness kills the fibrewise part, the
  residual holonomy is the genuinely global piece.
- The matched-pair calculus (ZS1–ZS4 = associativity in coordinates) is exactly the
  tool to state the **pairwise C ⋈ D distributive law** (the real Q2 prize). I
  conjecture the same two-level shape there: fibrewise freeness of the connecting
  biset between the two factors, plus global closure/holonomy on the mutual action.

## Open questions / next steps

- **Characterize (G) cohomologically.** The obstruction smells like an
  `H²`/torsor class for the source-endo action over the shape's branchings. Is
  there a clean cocycle whose class is the precise obstruction? (Likely a groupoid-
  /category-cohomology statement.)
- **Pairwise C ⋈ D.** Prove the monoid×monoid case recovers Brin/Ahman–Uustalu and
  the poset×monoid case, then state the sharpest two-level conjecture.
- **Lean.** ZS1–ZS4 ⟺ associativity is a crisp, self-contained formalization
  target (no Mathlib needed) — could be the next LEAN milestone after M2.
- Question for Neil: is the holonomy/closure obstruction already named in the
  distributive-law-of-categories literature (Rosebrugh–Wood strict factorization
  systems)? I suspect (G) = "this wide subcategory extends to a strict factorization
  system," which is known to be extra data — worth a citation rather than a reproof.
