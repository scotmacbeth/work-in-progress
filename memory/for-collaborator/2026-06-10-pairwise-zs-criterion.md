# The pairwise Zappa–Szép criterion: same two-level (L∧G) shape, proved

**Date:** 2026-06-10 (deep-work prove session, second of the day)
**For:** Robin, Neil
**Builds on:** the single-category criterion `2026-06-10-zs-criterion-cocycle.tex`
(the (L∧G) theorem + cocycle) and its collaborator note
`for-collaborator/2026-06-10-zs-closure-holonomy.md`, whose closing conjecture
(lines 105–107: "pairwise C⋈D has the same two-level shape") is what this cycle
**proves**.
**Artifact:** `projects/proofs/2026-06-10-pairwise-zs-criterion.tex` (8pp, compiles).
**Scripts (all in `projects/scratch/`):** `pairwise_zs_check.py` (framework),
`pairwise_zs_tests.py` / `pairwise_zs_tests2.py` (axioms⟺assoc, exhaustive),
`pairwise_end_to_end.py` (criterion vs brute force),
`pairwise_counterexample_FOUND.py` (the genuinely pairwise obstruction).

## TL;DR

The pairwise prize is settled. **The conjecture was right: the same two-level
(L∧G) shape governs the pairwise distributive law.** Precise form:

> **Theorem (pairwise criterion).** Let K be a small category and D ⊆ K a wide
> subcategory (the prescribed *right factor* — no longer forced to be the
> endomorphisms E). Then K admits a strict factorization K = C ⋈ D (every f
> factors uniquely as c∘d, c∈C, d∈D, for some wide C) **iff**
> **(L)** for every object b, the hom-presheaf Hom_K(−,b) is a **free right
> D-set** (a coproduct of representables); **and**
> **(G)** free bases can be chosen, one per target b, that **close into a wide
> subcategory** C.

The single-category criterion is the case **D = E**: a presheaf over the
endomorphisms (a disjoint family of monoids) splits per object, so (L) becomes
"each Hom(a,b) free over End(a)" — exactly last cycle's local freeness.

## The one clean idea

Everything reduces to a single standard fact, stated in the form we need:

> **Lemma (free presheaf = unique factorization).** A right D-set M: D^op→Set is
> free iff there is a basis family B=(B_m⊆M(m)) such that every x∈M(a) is
> **uniquely** c·d for c∈B_m, d∈D(a,m). (Yoneda: free = coproduct of
> representables; basis = the chosen generators.)

Then the whole theorem is two lines of bookkeeping: **a free basis of Hom_K(−,b)
is forced to be exactly the set of C-arrows into b.** So (L) = "bases exist per
target" and (G) = "the bases assemble into a subcategory." The proof needs
nothing about associativity — K is already a category. This is the cleanest
possible generalization, and it is airtight (no gaps).

## The structure half (distributive law of categories)

When the SFS exists, K ≅ C ⋈ D is the Zappa–Szép product carried by a
**distributive law of categories** λ: DC ⇒ CD, rewriting d∘c = (^d c)∘(d^c) with
^d c ∈ C and **d^c ∈ D** (the restriction may now CHANGE OBJECT — the one genuine
generalization from the vertex-monoid case). The matched-pair axioms ZS1–ZS4 +
units **⟺ associativity of K**, by the same uniqueness-of-factorization splitting
as last cycle. I re-typed the axioms for two genuine categories and checked the
cross-object typing goes through verbatim (spelled out for ZS2/ZS3 in the paper;
the composability dom (d')^{^d c} = dom ^d c = cod d^c is the only new point, and
it matches). This is the classical "distributive laws ⟺ strict factorization
systems" of **Rosebrugh–Wood (JPAA 175, 2002)** and Street — so (G) IS "this wide
subcategory extends to a strict factorization system," answering the question I
flagged to Neil last cycle: it's a **citation, not a reproof**.

## Two anchors

**Monoid×monoid (classical ground truth).** One object: C=M, D=N monoids; the
matched pair is exactly Brin's classical Zappa–Szép of monoids (ZS1–ZS4), the
product is the classical one, and K = M⋈N ⟺ M×N→K bijective (exact
factorization). Verified exhaustively over ALL type-correct λ for Z2×Z2, Z3×Z2,
Z2×Z3 (axioms⟺assoc, zero disagreements).

**Honesty correction on Ahman–Uustalu.** The SEED said "AU update monad = the
degenerate instance." **This is an overclaim and I did NOT assert it.** The
genuine degenerate ZS instance is the **semidirect product of monoids** (one
trivial action). AU's update monad is an *analogous but different* construction:
the writer-monad-over-reader-monad composite of a **monoid P and a SET S** via one
one-sided action (distributive law θ(p,f)=λs.(p, f(s↓p))), whose category is the
**action category S⋊P**. ZS mixes two monoid multiplications; the update monad
mixes a monoid with a set. A bare action category need not have ANY nontrivial
strict factorization (S=P=Z/2 ⇒ codiscrete category, only trivial SFSs). The only
legitimate "degenerate/semidirect" reading of AU is internal to the
directed-container hierarchy (non-dependent = state-independent container). The
paper states this hedge explicitly (Remark 5.5 / `rem:au`).

## The genuinely pairwise obstruction (L holds, G fails, D has a cross arrow)

The rigid twist of last cycle is the D=E instance. **Is the two-level phenomenon
an artifact of D being the endomorphisms? No.** New machine-found-and-hand-checked
witness (4 objects w,a,x,y):

    End(a)={1a,g}, g²=1a; a→x⇉y rigid twist (s∘p=q, s2∘p=qg) as before;
    PLUS object w with D-cross-arrows d, gd: w→a (gd = g∘d).
    D = {1w,1a,1x,1y, g, d, gd}  — wide, closed, with genuine cross arrows d,gd.

Every Hom_K(−,b) is free over D (L holds); NO wide C closes (G fails), verified
over all **1152** wide subcategories. The cross arrow d is adjoined as a **free
⟨g⟩-torsor** {d,gd} into a — it enlarges D to a real many-object category and
keeps freeness, but is inert against the branch holonomy. **(G) = holonomy = the
laxator, in genuinely pairwise form.**

## Status of the grant deliverable

SEED-Q2 is now answered at BOTH levels:
- single category (D=E): `2026-06-10-zs-criterion-cocycle.tex`;
- **pairwise (general D): `2026-06-10-pairwise-zs-criterion.tex`** ← this cycle.

The decision procedure: (L) cheap fibrewise freeness test + (G) global holonomy
search; obstruction = computable holonomy class = finite shadow of the laxator.
The matched-pair calculus exhibits the mediating distributive law explicitly.

## Open / next

- **(G) cohomologically.** Still open and now sharper: the holonomy is a torsor
  class for the D-action over the branchings of the C-skeleton. A clean H²/cocycle
  description for general D (not just E) would be the natural next theorem — likely
  category-cohomology of the action presheaf. Good `/prove` target.
- **Lean.** "ZS1–ZS4 ⟺ associativity (two categories)" is self-contained, no
  Mathlib; strong LEAN milestone. The free-presheaf lemma is also formalizable.
- **Publish.** Single + pairwise notes together are an ACT-sized paper:
  "Strict factorization of small categories is local freeness plus holonomy."
  Rosebrugh–Wood is the anchor citation; the NEW content is the two-level decision
  procedure, the free-D-module criterion, and the holonomy = laxator bridge.
- **Question for Neil:** does the "free hom-presheaf over a wide subcategory"
  condition (L) appear in the factorization-system literature under another name
  (e.g. as a discreteness/normality condition on the right class)? Worth a citation.
