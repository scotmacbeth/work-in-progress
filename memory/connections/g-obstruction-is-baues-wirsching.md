# Connection: my (G) = H² holonomy class IS Baues–Wirsching cohomology

**Bridges:** my own fresh proof (06-11 prove cycle, [[two-atoms-zappa-szep-decomposition]])
↔ the classical cohomology-of-small-categories literature ↔ ACT 2026 community
(Bumpus–Capucci presheaf cohomology). Path 2 ↔ Path 4 (laxator) ↔ grant impact.

## The convergence (why this is a crown jewel)
On **2026-06-11** two things happened on the same day, independently:

1. **PROVE cycle** — I proved the open "is (G) cohomological?" question:
   under hyp (H) [D = abelian vertex groups, trivial left action], the ZS-closure
   obstruction (G) ⟺ **[ω] ∈ H²(Sk_C; 𝒟)**, where Sk_C = category of free D-orbits,
   𝒟: Sk_C^op → Ab the vertex-group presheaf, ω_T the normalized defect 2-cocycle.
   Re-choosing the transversal shifts ω by a coboundary; the *set* of strict
   factorization systems is a torsor under Z¹ (mod inner: H¹). Rigid twist: H²≅Z/2,
   [ω] = generator. (`projects/proofs/2026-06-11-G-obstruction-cohomology.tex`.)

2. **BROWSE cycle** — surfaced, with no knowledge of (1):
   - **Baues–Wirsching cohomology of small categories** is THE classical H² tool
     (arXiv:2508.00727 "Baues–Wirsching Cohomology and Schwarz Genus").
   - **Bumpus, Capucci et al. "Algorithmic and Extremal Obstructions Through Presheaf
     Cohomology"** (ACT 2026) — presheaf cohomology as the obstruction to
     local-to-global patching. *Exactly* my (G) = local-freeness-holds-everywhere-but-
     fails-to-glue-globally shape.

## The claim
My hand-rolled H²(Sk_C; 𝒟) is almost certainly an instance of **Baues–Wirsching
cohomology** H²_BW(Sk_C; D) with coefficients in the natural system D built from 𝒟.
The Baues–Wirsching theory takes coefficients in a *natural system* (functor on the
factorization/twisted-arrow category F(Sk_C) → Ab), which is the right home for a
2-cocycle defined on composable pairs — precisely the shape of ω_T (defined on
c₂∘c₁). My presheaf 𝒟: Sk_C^op → Ab is a natural system supported on objects;
the general nonabelian case (my (H)(ii) boundary) wants the full F(Sk_C) coefficient.

**If this identification holds**, the move is the same one I made for (G)-existence:
> a reproof becomes a citation.
The (G)-existence statement is **Rosebrugh–Wood** ("DL ⟺ SFS"); the (G)-*classification*
becomes **Baues–Wirsching H²**. My delta is the *identification* + the directed-container
computation (rigid twist = Z/2 generator), not the cohomology machinery.

## Why it matters (grant + ACT)
- **Upgrades my result from ad-hoc to named theory.** "[ω] ∈ H²(Sk_C;𝒟)" reads as a
  one-off; "the ZS-closure obstruction is the Baues–Wirsching class of the defect
  natural system" reads as a theorem inside an established framework. Stronger paper,
  stronger grant narrative.
- **Direct ACT 2026 engagement target.** Bumpus & Capucci are in Tallinn (July 6–10)
  presenting *the same kind of obstruction*. Their presheaf-cohomology local-to-global
  framework may subsume my Sk_C construction — or I subsume their examples with the
  ZS/laxator reading. Either way: talk to them.
- **Path 4 closure.** (G) = the laxator (ga-containers); now the laxator has a
  cohomology class. Diversity collapse ⟺ [ω] ≠ 0. The empirical GECCO W=1.0 result
  becomes "[ω] = 0" — a cohomological prediction.

## The chase (precise, for a wake/prove cycle)
1. **Pin the identification.** Write Baues–Wirsching H²_BW with the *defect natural
   system* and check term-by-term it equals my H²(Sk_C;𝒟) under (H). Read 2508.00727
   for the modern statement; the original is Baues–Wirsching, J. Pure Appl. Algebra 38
   (1985). Expected: my cocycle is the BW cocycle for a natural system concentrated on
   identities-and-composites.
2. **Nonabelian boundary.** When the left action is nontrivial ((H)(ii)), Sk_C is no
   longer a category and the obstruction goes nonabelian = Kac/Masuoka H² of the
   Rosebrugh–Wood matched-pair law. Does Baues–Wirsching's *non-abelian* extension
   (gerbe / H² with nonabelian coefficients) cover it? Cross-check Baaj–Skandalis–Vaes
   (Trans. AMS 357, 2005) group-level H²(matched pair) for the analogy.
3. **ACT engagement.** Email Bumpus/Capucci after their abstract is public; offer the
   ZS-closure / rigid-twist family as test cases for their presheaf-cohomology
   obstruction machinery.

## UPDATE 2026-06-12 (browse): the identification is CONFIRMED — and it's a CITATION, both abelian AND nonabelian

The 06-12 browse pinned it. It is **established theory**, not my conjecture:

- **Abelian classification (the (H) case I proved).** Baues–Wirsching, JPAA 38 (1985):
  **H²_BW(C; D) classifies linear extensions of the small category C by the natural
  system D.** A ZS product `C ⋈ D_•` with abelian fibre (D_c an abelian vertex group,
  C acting) **IS** a linear extension of C by D. Therefore `[ω] ∈ H²_BW(Sk_C; 𝒟) ⟺ (G)
  fails`. My "(G) ⟺ [ω]=0" is a *corollary of the BW classification theorem*, not a new
  result. **Cite Baues–Wirsching 1985 in the pairwise ZS paper.** (Modern restatement:
  arXiv:2508.00727; also Ikebuchi 2510.00488 BW = Quillen cohomology for CCCs.)

- **Nonabelian boundary — ALSO a citation (this is the surprise).** Pirashvili,
  "Schreier Theory of Track Categories," arXiv:1512.03250, **Theorem 7**:
  `Tracks(π, G) ≅ H²(π, G)` for a pre-track category with G a *centralised* natural
  system — the **nonabelian Schreier theorem**, holding for ALL small categories, not
  just groupoids. This is exactly the nontrivial-left-action case where Sk_C stops being
  a category and the obstruction goes nonabelian. **So the nonabelian (G) — which I had
  queued as my next PROVE target — is also established theory.** Do NOT prove it; cite
  Pirashvili (and cross-check Baaj–Skandalis–Vaes for the group-level matched-pair
  analogy).

**The meta-pattern fired a THIRD time.** The whole ZS-cohomology tower is now citations:
> existence = **Rosebrugh–Wood** · abelian classification = **Baues–Wirsching** ·
> nonabelian classification = **Pirashvili (track categories)**.
My genuine delta is the *identification* (ZS-closure ↔ linear extension / track) plus the
**directed-container computation** (rigid twist = explicit Z/2 generator; pairwise 4-obj
realizes the same class) plus the Lean/container packaging. This is connective + concrete,
not new cohomology — state it that way.

**Strategic read (aligns with Neil's 06-11 steer).** Neil demoted the cohomology/ZS
threads as possible "rabbit holes." The 06-12 browse *vindicates* that call: there is no
new theorem to chase here — it is citations all the way down. Bank it, cite it in the
pairwise paper's remark, move on to the book. Do NOT re-open nonabelian (G).

## Honest status (superseded — kept for the record)
- ~~The *identification* H²(Sk_C;𝒟) ≅ H²_BW is a strong conjecture, not checked yet.~~
  **RESOLVED 2026-06-12: it is established theory (Baues–Wirsching 1985, abelian;
  Pirashvili 2015, nonabelian). A citation, not a conjecture.**
- This does NOT change the proof I have — it relabels and embeds it in a named framework.

Links: [[two-atoms-zappa-szep-decomposition]] · [[duplicate-is-futures-with-provenance]] ·
[[distributive-law-landscape]]
