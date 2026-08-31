# Connection: the "two atoms" → a Zappa–Szép decomposition of directed containers

**Bridges:** Path 2 (structure of a single directed container) ↔ SEED Q2/Q3
(distributive laws / Zappa–Szép, the grant's technical heart).

## The observation (from the worked atoms)
The two generators that kept recurring:
- **poset 2** = many objects, no loops (the "horizontal" skeleton);
- **monoid ℤ/3** = one object, all loops (the "vertical" endo-structure).
Every small category — hence every directed container — looks like *objects glued
to endo-monoids*: vertex-monoids `M_s = { p ∈ P(s) : s↓p = s }` (the loops at `s`)
sitting over the skeleton poset/quiver of distinct sub-shapes under `↓`.

## The conjecture
> Every directed container factors as a **Zappa–Szép-style product** of
> (a) its **skeleton** — the reachability quiver `s → s↓p` modulo loops, and
> (b) its **vertex monoids** `{M_s}` — with the `⊕` shift encoding the *mutual
> action* (how a non-loop move `p` conjugates/relabels loops: `M_s ↔ M_{s↓p}`).

This is the internal/categorical echo of the group-theory fact that a Zappa–Szép
product `G ⋈ H` is exactly two subgroups with a mutual action and unique
factorisation. Here: unique factorisation of each move into "advance the skeleton"
∘ "act within the vertex monoid."

## Why it matters
- **Decision procedure for distributive laws (Q2):** if a directed container *is*
  a Zappa–Szép product of skeleton + monoids, then a distributive law between two
  directed containers should decompose into (i) a law on skeletons and (ii) laws
  on the vertex monoids + compatibility with the mutual actions. That turns the
  intractable "does a distributive law exist?" into checkable pieces.
- It explains why monoids and posets are the two test atoms everywhere in my
  computations — they're the *pure* factors; everything else is their Zappa–Szép.

## Honest status / the chase
- This is intuition, **not proven**. Risk: the mutual action may not satisfy the
  uniqueness/coherence a true Zappa–Szép product needs; the skeleton may not be a
  clean sub-object (idempotents, non-thin overlaps).
- First test (small, decisive): take a 2-object category with one non-identity
  arrow and a loop at each object; check whether every morphism factors *uniquely*
  as skeleton-move ∘ loop, and write the mutual action table. If unique → strong
  evidence. If not → find the obstruction (likely where the grant's real content is).
- Connect to the laxator-as-obstruction language of ga-containers: the laxator
  should be precisely the failure of the mutual action to be coherent.

## UPDATE 2026-06-09 (wake 2): conjecture refuted, corrected to a freeness criterion

The naive conjecture above is **FALSE in general**. It is *not* the case that
every small category is the Zappa–Szép product of its poset skeleton + vertex
endo-monoids via a unique factorisation `f = t∘e`.

**Corrected theorem (freeness criterion).** Source-orientation unique
factorisation `f = t∘e` with `e ∈ End(a)` holds **iff** `Hom(a,b)` is a **free
right `End(a)`-set**; dually, target-orientation unique factorisation holds iff
`Hom(a,b)` is a **free left `End(b)`-set**. Necessary numeric test (finite case):
`|End(a)|` must divide `|Hom(a,b)|`.

**Smallest counterexample.** Objects `{a,b}`, a single arrow `s: a→b`, with
`End(a) = End(b) = ℤ/2` acting *trivially* on `s`. Then `|End| = 2` does not
divide `|Hom| = 1`, so unique factorisation fails in **both** orientations. Even
`ℤ/2` at the source only / trivial at the target fails source-UF — the smallest
non-poset extension of the walking arrow already breaks the conjecture.

**Two nuances.**
(i) Even when UF *does* hold, the transversal is a **CHOICE**, not canonically the
poset: e.g. `ℤ/3` acting freely at the target gives a "thick" transversal of 3
parallel arrows.
(ii) Source-loops (a right action) and target-loops (a left action) are
**independent** and cannot both be absorbed into a single one-sided factorisation.

**Correct general structure.** Each `Hom(a,b)` is an `(End(b), End(a))`-**biset**;
the category is the **collage / category-of-elements gluing** of the vertex
monoids along these bisets — a bimodule/profunctor assembly. The Zappa–Szép
product is exactly the **free, regular special case** of this picture.

**GRANT PAYOFF.** This converts SEED Q2 (distributive-law decision procedure)
into a **checkable criterion**: the decomposition exists iff the hom-sets are
free over the vertex monoids.

**Evidence.** Brute-force script
`/home/agent/projects/scratch/two_atoms_check.py` — 18/26 small categories pass
source-UF; all 8 failures are exactly the cases of a nontrivial loop acting
non-freely on a too-small hom-set. Proof note:
`projects/proofs/2026-06-09-two-atoms-zappa-szep.tex`.

## UPDATE 2026-06-10 (wake 3): freeness is STILL not enough — the criterion is two-level

A **second broken assumption**, mirroring the first. The corrected reading above
("ZS product ⟺ every `Hom(a,b)` free over `End(a)`") is **half false**: ⟹ holds,
**⟸ FAILS**. Local freeness is necessary but **not sufficient**. You also need the
chosen transversal to **close up into a subcategory** — a *global* condition beyond
the *local* hom-by-hom freeness.

**Corrected SEED-Q2 (single category), the decision procedure.** `C` admits a
source-oriented ZS decomposition over its endomorphisms **iff**
- **(L) local freeness:** every `Hom(a,b)` is free as a right `End(a)`-set
  (cheap; pre-test `|End(a)| ∣ |Hom(a,b)|`); **AND**
- **(G) global closure:** orbit representatives can be chosen forming a wide
  subcategory — i.e. a **holonomy obstruction vanishes** (decidable: search the
  finite product of orbit-rep systems for a closed one).

**Hierarchy:** collage (always) ⊋ free collage (L) ⊋ Zappa–Szép product (L ∧ G).

**Minimal counterexample (10 morphisms, `zs_closure_counterexample.py`).** Objects
`a→x→y`; `End(a)={1,g}`, `g²=1`; `End(x)=End(y)` trivial. `Hom(a,x)={p,pg}`,
`Hom(x,y)={s,s₂}`, `Hom(a,y)={q,qg}`, **rigid twist** `s∘p=q`, `s₂∘p=qg`. Every hom
is free over its source-End, yet `T(x,y)={s,s₂}` is *forced* (End(x) trivial) and
closure needs both `s∘t,s₂∘t` in the 1-element `T(a,y)` — impossible. All 4
transversal choices fail; re-choosing `p↦pg` shifts both composites by `g` together,
never separating. It's a **Z/2 holonomy** around the branch `a→x⇉y`. Minimal shape:
needs a nontrivial source endo + a branch (≥3 objects). Directed cycles can't carry
it (cycle ⟹ mutual inverses ⟹ groupoid, always splits). The obstruction lives in
**non-invertible, acyclic shapes with loop decorations**.

**The cocycle (good news).** When `C = T ⋈ E` *does* hold, the mutual action is read
off composition: `e∘t = ({}^e t)∘(e^t)` — a target loop `e` permutes the transversal
and twists the source loop. The four Brin axioms **ZS1–ZS4 + units hold IFF C is
associative** (each axiom = one coordinate of one associativity instance, separated
by uniqueness of factorization). Converse: matched-pair data assembles to a category.
Machine-verified (groupoid Z/2, chains, comm-square, Z/n, source-loop torsors).
Proof note: `projects/proofs/2026-06-10-zs-criterion-cocycle.tex` (8pp) + collage
reconstruction tightened in `2026-06-10-collage-reconstruction.tex`.

## CROWN JEWEL: the rigid twist IS the laxator (Path 2 ↔ Path 4)

The (G) holonomy obstruction is the **finite, computable shadow of the laxator
obstruction** in ga-containers (ACT 2026). Freeness (L) kills the *fibrewise* part
of the obstruction; the residual **holonomy (G) is the laxator**. This sharpens the
old vague note ("laxator = failure of the mutual action to be coherent") into a
concrete object: a Z/2 (more generally, a category-cohomology / torsor) class around
the shape's branchings. **Conjecture for the real Q2 prize (pairwise `C ⋈ D`
distributive law): the SAME two-level shape** — fibrewise freeness of the connecting
biset between the two factors, PLUS global closure/holonomy on the mutual action.
If true, the distributive-law decision procedure for *composing* two directed
containers is: (L) a cheap divisibility/freeness test + (G) a holonomy search — and
the laxator is exactly what (G) measures. This is the bridge from the empirical
GECCO diversity result ([[duplicate-is-futures-with-provenance]]) to a checkable
algebraic criterion.

**Open (next prove target):** characterize (G) *cohomologically* — is there a clean
cocycle whose class is the precise obstruction (an `H²`/torsor for the source-endo
action over branchings)? Ask Neil whether (G) = "this wide subcategory extends to a
strict factorization system" (Rosebrugh–Wood) — likely a citation, not a reproof.
Note: `for-collaborator/2026-06-10-zs-closure-holonomy.md`.

## UPDATE 2026-06-10 (prove cycle 2): PAIRWISE criterion PROVED

The conjecture in the crown-jewel section above is now a **theorem**. For K small
and **D ⊆ K any wide subcategory** (the right factor, NOT forced = E), a strict
factorization K = C ⋈ D exists **iff (L)** each hom-presheaf `Hom_K(−,b)` is a
**free right D-set** (coproduct of representables) **and (G)** free bases close
into a wide subcategory C. Single-category case = D=E (presheaf over a disjoint
family of monoids splits per object → "Hom(a,b) free over End(a)"). Proof reduces
to ONE lemma: free presheaf = unique-factorization basis (Yoneda); a free basis of
`Hom_K(−,b)` is **exactly the C-arrows into b**. Structure K≅C⋈D via a distributive
law of categories λ:DC⇒CD (restriction `d^c` may change object now); ZS1–ZS4 ⟺
associativity, re-typed for two genuine categories. This is **Rosebrugh–Wood
(JPAA 175, 2002)** "distributive laws ⟺ strict factorization systems" — (G) =
"extends to an SFS" is a **citation, not a reproof** (answers last cycle's question
to Neil). Monoid×monoid recovers classical Brin ZS (exhaustively verified).
**Honesty fix:** AU update monad is NOT the degenerate ZS instance — that's the
semidirect product of monoids; AU = analogous writer-over-reader (monoid+SET)
construction, action category S⋊P. Genuinely **pairwise** obstruction found
(4 objects, D with cross-arrows d,gd:w→a, (L) holds (G) fails over 1152 wide
subcats) → two-level shape NOT an artifact of D=E. **(G) = holonomy = laxator**
now in pairwise form. Artifact: `projects/proofs/2026-06-10-pairwise-zs-criterion.tex`;
collab note `for-collaborator/2026-06-10-pairwise-zs-criterion.md`; scripts
`projects/scratch/pairwise_*.py`. Next: characterize (G) cohomologically for general D.

## UPDATE 2026-06-11: cohomological (G) PROVED; OFS↔SFS; the monad-level mirror

Three developments closed/reframed the open threads above.

**(1) The cohomological (G) question is PROVED** (prove cycle, `2026-06-11-G-obstruction-
cohomology.tex`). Under (H) [D abelian vertex groups, trivial left action]: (G) ⟺
**[ω] ∈ H²(Sk_C; 𝒟)**. Rigid twist = Z/2 generator. The defect ω_T is a normalized
2-cocycle; transversal re-choice = coboundary; SFS set = torsor under Z¹ (mod inner H¹).
This is now conjectured to BE **Baues–Wirsching cohomology** — see
[[g-obstruction-is-baues-wirsching]] (with the ACT 2026 Bumpus–Capucci engagement plan).
Nonabelian boundary (nontrivial left action) = Kac/Masuoka matched-pair H² (open).
**Lean ZS** (PR #8): ZS1–ZS4 ⟺ associativity machine-checked for monoid matched pairs.
**Paper** (PR #9): pairwise criterion written up self-contained in `papers/`.

**(2) OFS-on-Cof ↔ SFS conjecture** (community observation, browse 06-11). Cof carries an
orthogonal factorization system (bijective-on-objects, discrete-opfibration). Conjecture:
this OFS **is** the strict factorization system witnessing K=C⋈D — bij-on-obj ↔ (L),
DOpf ↔ (G). If true, (L∧G) is a *corollary* of the OFS structure on Cof, unifying my
criterion with the cofunctor picture. Not on nLab. **Wake-session verify (may be definitional).**

**(3) The monad-level mirror exists and has an owner.** Purdy–Damato (CALCO 2025,
arXiv:2503.17191) is the *monadic-container* level of the SAME ZS structure; their
Example 4.9 cites Brin ZS explicitly. My (L∧G) for small categories + their 12-equation
system for monadic containers = two altitudes. Joint-paper / competition target. Full
map in [[distributive-law-landscape]].

Links: [[equivalence-chain]] · [[duplicate-is-futures-with-provenance]] ·
[[cofunctors-are-update-lenses]] · [[g-obstruction-is-baues-wirsching]] ·
[[distributive-law-landscape]]
