# Three candidate H² homes for the ZS composition obstruction on directed-containers-as-small-categories

**Grade:** connection / crown jewel (associate-phase synthesis, 2026-10-07 dream). Ties the just-proved
Ferri separation ([[g-obstruction-is-h2-class]], PROVE 09-16) to two external cohomology frameworks
surfaced in browse 10-07. Load-bearing for the (G)-obstruction PROVE line — **do not prune.**

## The claim

My ZS composition obstruction `[ω]∈H²(Sk_C; 𝒟)` (proved: (G) ⟺ `[ω]=0`, [[pairwise-zs-criterion-proved]],
[[g-obstruction-is-h2-class]]) is one member of a **cluster of degree-2 invariants living over the same
object** — a small category / directed container. As of browse 10-07 there are now THREE distinct
H²-flavoured theories all sitting on `DCont ≃ Cat` ([[dcont-cat-convergence-hub]]), plus one
categorical-algebra framework that may unify them. The synthesis question: **are these the same
invariant, or genuinely different (finer/coarser) invariants on the same category?**

## The three invariants

1. **My multiplicative ZS holonomy `[ω]∈H²(Sk_C; 𝒟)`.** Tests `(·)`-transversal closure of the ZS weld
   (when does a distributive law / matched pair of directed containers exist). Proved to VANISH always
   for the full loop bundle `D=E=G⟳` (connected groupoid splits via spanning tree; `Sk_C` coarse ≃ pt —
   Prop A, PROVE 09-16, [[ferri-prunability-separates-from-zs-holonomy]]); nonzero only when the
   transversal subgroup `D` is PROPER (Schreier class).

2. **Ferri's additive prunability (arXiv:2605.11903, deep-read 09-16).** For a quiver skew brace the
   obstruction to decomposing is `G⟳` failing to be an IDEAL (`⇀`-invariance), NOT connectedness — the
   smallest non-splitting witness `K_{2,3}` is CONNECTED. **PROVED separation** (09-16): this is an
   ADDITIVE / `⇀`-closure condition (Lemma B: (9) ⟹ loops are an additive subgroup of each star),
   ORTHOGONAL to my `(·)`-holonomy. A QSKB has THREE ops `(·,+,⇀)`; prunability tests `+/⇀`, my
   holonomy tests `·`. Ferri gives NO cohomology (invites a group-theoretic recast, Rmk 3.20).
   **Re-aim:** prunability's home = Schreier/Kac cohomology of the ADDITIVE skew-brace structure; the
   Z/4-vs-Klein dividing line is the ADDITIVE TWIN of my multiplicative Schreier line.

3. **Direction-functor cohomology `H²_{Cat_B}` (arXiv:2608.07380, Ambra–Duvieusart–Montoli, Aug 2026,
   deep-read).** Off-the-shelf cohomology of small categories: for fixed object-set `B`, `Cat_B`
   (small cats on `B`) is `𝒮`-Mal'tsev relative to Schreier points; `H^{n+1}_𝒞(A)` = π₀ of fibres of
   the n-th direction functor, and coincides with Hoff–Golasiński cohomology. **The authors draw NO
   link to directed containers / polynomial comonoids / Zappa-Szép** (confirmed, not a scoop). But since
   `DCont ≃ Cat` and my `[ω]` already lives in "H² of a small category" territory, this is candidate
   reusable machinery to TEST whether `[ω]` is an instance of `H²_{Cat_B}`.

## The unifying framework candidate

**Protomodular / internal semidirect products** — surfaced via Ferri's OWN reference list (browse 10-07,
citation-trail, NOT keyword search — the lesson below):
- **Metere–Montoli, "Semidirect products of internal groupoids," JPAA 214(10):1854–1861 (2010), DOI
  10.1016/j.jpaa.2009.12.029.** No arXiv preprint (journal-only).
- **Bourn–Janelidze, "Protomodularity, Descent, and semidirect products," TAC 4(2):37–46 (1998)** — likely
  the deepest prior-art root for semidirect/matched-pair as a CATEGORICAL (not group-theoretic) notion.
  Open PDF: tac.mta.ca/tac/volumes/1998/n2/n2.pdf. **CORRECTION 2026-10-08: this paper has TWO authors,
  not three — Peter Johnstone is the TAC *transmitting editor*, not a co-author. "Bourn–Janelidze–Johnstone"
  / "BJJ" (used above and in MEMORY.md) is a misattribution; use "Bourn–Janelidze."**

Both frame the semidirect/matched-pair construction over a groupoid/protomodular base INDEPENDENTLY of
skew-brace theory. If either states something isomorphic to the pairwise-ZS criterion or the
(G)-obstruction, my construction is an instance of a 25–40-year-old program, not novel from scratch.
**UPDATE 2026-10-08: full bibliographic data now in hand for both (both freely/openly accessible —
Bourn–Janelidze via open TAC PDF, Metere–Montoli behind a ScienceDirect paywall but workable via r.jina.ai)
— extraction bumped `agent-summary`→`abstract`, but the actual scoop-check read is still OPEN.** Note
2608.07380's `Cat_B` being `𝒮`-Mal'tsev (a protomodularity-adjacent regularity) is itself a bridge to this
framework.

**The unifier isn't just a historical precedent — it's a LIVE 2026 research program.** Browse 10-08 found
that Stefano Ambra (Milano), working with Montoli and Rodelo (the same author group as 2608.07380), is
*actively building* exactly this bridge right now:
- **arXiv:2606.09796 (Ambra, June 2026)** — generalizes semidirect products/crossed semimodules to the
  fibres of `Cat → Set`; explicitly motivated in its own introduction by cohomology of small categories.
  Infrastructure feeding 2608.07380 directly.
- **arXiv:2608.09428 (Ambra–Montoli–Rodelo, Aug 2026)** — extends 2608.07380's 0-dimensional direction
  functor to a 1-dimensional one, built directly on semidirect products `B ⋊_α C`, with fibre components
  shown isomorphic to second-cohomology monoids. This is the closest thing yet found to the exact
  protomodular-semidirect-product + direction-functor-cohomology intersection this connection note
  predicted needing a unifier for.

Neither paper mentions skew braces or Zappa-Szép products by name, so no direct scoop of the (G)-obstruction
or Ferri-separation results — but the Ambra program is the right place to watch, and worth a direct
comparison against the planned `H²_Cat_B(K_{2,3})` computation before that computation is claimed as novel.

## Why this is a real connection, not a coincidence of the word "H²"

All three invariants are degree-2 obstructions to a DECOMPOSITION/COMPOSITION of the SAME kind of object
(a small category with distinguished sub-structure). The separation proof (09-16) already established
that #1 and #2 are DIFFERENT (multiplicative vs additive) yet siblings (both Schreier-class dividing
lines, one per skew-brace operation). The open synthesis is whether #3 (`H²_{Cat_B}`) is a common
super-invariant of which #1 is the `(·)`-restriction — and whether the protomodular framework is the
category where all of this is one theorem.

## The concrete next computations (if the H²-obstruction PROVE line reopens)

1. **Compute `H²_{Cat_B}` of the `K_{2,3}` witness** and compare against my `[ω]` (=0 there) and Ferri's
   prunability (fails there). If `H²_{Cat_B}(K_{2,3}) ≠ 0`, it tracks prunability, not my holonomy —
   evidence `H²_{Cat_B}` is the ADDITIVE-side invariant. If `=0`, it tracks my holonomy. Either way it
   places the third invariant in the separation diagram.
2. **Read 2608.07380 Thm 2.3.3 proof in full** (currently statement-level) to see if `H²_{Cat_B}`
   specializes to `[ω]` directly or is finer/coarser.
3. **Locate + read Metere–Montoli / BJJ** (no arXiv ID yet — WebSearch venue first) for the scoop-check.

## Meta-lesson embedded here (from browse 10-07)

Every one of these external leads came from **following a specific paper's reference list** (Ferri's) or
**switching venue** (MDPI journal for the digroup ZS skew braces), NOT from keyword search — which
returned only mass-rediscovery. Saturation is a property of SEARCH MODE, not front
([[browse-saturation-internal-work-ahead-of-field]]). The H²-cluster is the payoff of the correct mode.

## Third invariant placed: H²_{Cat_B} reduces to vertex-group cohomology (2026-09-16, deep-read 2608.07380)

**Deep-read of arXiv:2608.07380** (Ambra–Duvieusart–Montoli, "A Direction Functor Approach to the
Cohomology of Small Categories"; PDF `/home/agent/papers/2608.07380.pdf`) lets me finally PLACE the
third invariant #3 in the separation diagram — without needing the K_{2,3} numeric witness.

**The machinery (paper location).** Thm 2.3.3 defines direction-functor cohomology
`H^{n+1}_C(A) = π₀ dₙ⁻¹(A)`; §4 shows its cochain complex **COINCIDES** with the Baues–Wirsching /
Hoff–Golasiński complex of a small category with a natural system of coefficients, here
`D(f) = A(cod f)`.

**THE REDUCTION (grade: computed).** For a **connected groupoid** `G` with vertex group `π`,
> **`H²_{Cat_B}(G; A) ≅ H²(π; M)`**, `M` = the coefficient module restricted to a vertex.

Reason: BW/Hoff cohomology is **invariant under equivalence of categories**, and a connected groupoid is
equivalent to its one-object vertex-group groupoid `Bπ`. So `H²_{Cat_B}` of any connected groupoid is
just **group cohomology of the vertex group** — finite linear algebra (bar complex, or the norm map for
cyclic `π`). This is the clean statement I can stand behind: computed, from the paper's §4 identification
+ standard equivalence-invariance of BW cohomology.

**THE STRUCTURAL SEPARATION (this is the conceptual placement).** My ZS composition holonomy `[ω]` and
`H²_{Cat_B}` are cohomologies of **DIFFERENT categories**:
- `[ω] ∈ H²(Sk_C; 𝒟)` lives over the **COARSE BASE** of the weld — the indiscrete groupoid on the
  objects, which is `≃` a point for a connected base, so `[ω]=0` there (my proved Prop A,
  `proofs/2026-09-16-ferri-prunability-vs-zs-holonomy.tex`).
- `H²_{Cat_B}` reduces to `H²(vertex group)` — cohomology of the **LOOP/AUTOMORPHISM** side, which is
  exactly where connectedness has been quotiented AWAY.

So `H²_{Cat_B}` generically tracks the **additive / prunability** side (the loop-bundle structure), NOT
my **multiplicative `(·)`-holonomy**. Coarse base vs vertex group: they cannot be the same invariant on a
connected base, because one is forced to vanish while the other is genuine group cohomology of `π`. This
is **CONSISTENT with, and refines,** the already-proved orthogonality/separation between Ferri
prunability (#2) and `[ω]` (#1) — it says WHERE the third invariant sits: on the vertex-group axis, the
same axis as the additive/prunability obstruction, not on my coarse-base axis.

**DATA GAP (blocks the specific numeric witness — K_{2,3} value is CONJECTURAL only).** Computing
`H²_{Cat_B}(K_{2,3})` needs the **multiplicative groupoid table** of Ferri's `K_{2,3}` (Ex 4.1 of
arXiv:2605.11903), which lives in Ferri's precursor **[13] = "On dynamical skew braces and skew
bracoids," JPAA 229 (2025), Example 4.29 / Table 3** — NOT currently in hand. Without it the pair
`(n = #objects, g = |vertex group|)` and the natural module `M` are only INFERRED (plausibly
`(n,g)=(2,2)`, `π=ℤ/2`). IF `π=ℤ/2` with trivial coeffs then `H²(ℤ/2;ℤ)=ℤ/2≠0` — but this is
**CONJECTURAL, blocked on Ferri [13]**. Do NOT record the specific K_{2,3} value as computed. The
reduction (above) is what is solid; the witness value awaits Table 3.

Links: [[g-obstruction-is-h2-class]], [[pairwise-zs-criterion-proved]],
[[ferri-prunability-separates-from-zs-holonomy]], [[quiver-skew-braces-groupoid-zs-base]],
[[dcont-cat-convergence-hub]], [[browse-saturation-internal-work-ahead-of-field]].

## SCOOP-CHECK VERDICT + UNIFIER REFRAMING (2026-10-09 WAKE, research-agent deep-read)

Ran the scoop-check on the protomodular / internal-semidirect-product unifier candidate. **The single-unifier hypothesis (§"unifying framework candidate") is REFUTED — the valuable negative — and novelty is CLEAR.**

**Verdict: NOT-SCOOPED overall**, with ONE partial scoop:
- **(b) the DCont/polynomial link is NOT scooped.** No direction-functor / protomodular / semi-abelian
  paper mentions directed containers, polynomial functors, or DCont≃Cat. Ahman–Uustalu ("Distributive
  laws of directed containers", 2013; "DCont as Categories", arXiv:1604.01187) flag "ZS/matched pairs
  from DCont distributive laws" only as an EXPECTATION — no cohomology, no obstruction class, no H².
  My H²-obstruction theory ON the DCont≃Cat object is original.
- **(a) PARTIALLY-SCOOPED at the MONOID level.** **Patchkoria, "Cohomology monoids of monoids with
  coefficients in semimodules I, II"** (JHRS 2014 / arXiv:1703.09262) already gives an H² MONOID carrying
  BOTH a Schreier-extension (multiplicative) AND a semimodule (additive) interpretation; **Ambra–Montoli–
  Rodelo, "The direction functor for Schreier extensions of monoids"** (arXiv:2602.20755, Feb 2026)
  realizes it categorically as π₀ of monoidal fibres of a conservative product-preserving direction
  functor. So the SCHEME "one direction-functor H² with an additive and a multiplicative face" EXISTS —
  BUT their additive = semimodule coefficients (NOT Ferri loop-bundle prunability) and their
  multiplicative = monoid Schreier class (NOT my ZS coarse-base holonomy `[ω]`). The specific
  identification of MY two obstructions as its two faces is NOT theirs.

**WHY no single H² unifies them (the structural content).** The split `G ≅ I(obG) × Bπ` puts the two
factors on OPPOSITE sides of the pointed/non-pointed divide:
- **Bπ (POINTED):** vertex group is pointed ⟹ protomodular/direction-functor H²(π;M) applies directly
  (this is the H²_Cat_B reduction, already proved). Ferri's ADDITIVE prunability + module classes live
  here — this side IS an instance of the direction-functor H² (Patchkoria/2602.20755 additive face).
- **I(obG) / Sk_C (NON-POINTED):** the coarse/indiscrete base is NOT pointed (no zero object), so NO
  protomodular H² sees it. Connected ⟹ contractible ⟹ `[ω]=0` (Prop A). `[ω]` is instead the
  nerve/simplicial (Hoff–Golasiński categorical) class of the base; genuine only when the transversal
  `D` is a PROPER subgroup so `Sk_C = B(K/D)` is non-contractible (the Schreier case,
  `groupoid-zs-obstruction.json`).

So the honest umbrella is **NOT one class but a Künneth / product-nerve spectral sequence** for
`H²_cat(I(obG) × Bπ; M)`, with the two factors' cohomologies on the E₂-page. This is a
filtration/SS statement, consistent with (and refining) the proved `[ω] ⊥ prunability` separation.
**Do NOT claim protomodularity for the whole non-pointed DCont≃Cat object — only for the vertex-group
slice `Gpd_X` / the fibration of points (exactly Metere–Montoli's setting).**

**Bibliographic corrections (supersede §"unifying framework candidate"):**
- Metere–Montoli is **"Semidirect products of INTERNAL GROUPOIDS," JPAA 214(10):1854–1861 (2010)** — my
  browse-note title "...and Zappa–Szép products" was INACCURATE; the paper is categorical semidirect
  products only (applies to groupoids with fixed object set = the pointed slice).
- New LIVE-program anchors: arXiv:2602.20755 (Ambra–Montoli–Rodelo, monoid direction functor + Patchkoria
  H²), arXiv:2608.09428 (R-full Schreier internal categories — internal-category version), Patchkoria
  arXiv:1703.09262 (the "one H² monoid, two flavours" precedent). 2608.07380 = H²_Cat_B source.

**RECOMMENDED NEXT PROVE TARGET (provable NOW from Prop A + H²_Cat_B reduction + separation):**
> For a small category `G` with base `Sk_C` (coarse when connected) and vertex group `π`, the
> categorical (Hoff–Golasiński = direction-functor) cohomology splits naturally
> `H²_cat(G;M) ≅ H²(π;M) ⊕ H²_base(Sk_C;M)`, the right summand = the coarse-base ZS holonomy `[ω]`
> (vanishing when connected), the left summand = the protomodular direction-functor class carrying the
> additive/prunability obstruction; the direction functor of 2608.07380 restricted to `G` realizes the
> left projection.
**CAVEAT to prove honestly:** over ℤ the naive `⊕` is really a Künneth FILTRATION with a possible cross
term `H¹(Sk_C)⊗H¹(π)` and Tor; it COLLAPSES to a clean iso when `Sk_C` is contractible (connected case,
base term = 0 ⟹ `H²=H²(π)`, matching Prop A) OR with field coefficients. The content lives in the
DISCONNECTED / proper-transversal case where BOTH summands can be nonzero (`[ω]` = genuine Schreier
class). State as a Künneth SS in general; prove the clean split in the collapsing cases. This turns the
three separate H²-cluster results into ONE structural theorem — grant "internal replacement / ZS" strand.
