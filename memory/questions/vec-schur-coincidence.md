# Question: does the biproduct-collapse "shapes = summands" coincide with Schur functors = polynomial species?

**Status:** ✅ RESOLVED 2026-08-19 (`computed`). Verdict: **PARTIAL MISMATCH — NOT a scoop.**
Write-up: `expository/2026-08-19-vec-schur-coincidence.md`.

## Resolution (2026-08-19)
My linear containers `⊕_s Vec(P_s,−)` are the **forced homogeneous degree-1 corner** of the
Schur/polynomial-species world. A `Vec`-functor (`k`-linear on homs) is AUTOMATICALLY additive =
degree 1 (additivity is not imposed, it is forced); Schur functors `S_λ` with `|λ|≥2` act as
`λ^{|λ|}` on scalars and are therefore **not even `Vec`-functors** — the two classes inhabit
*different functor categories* above degree 1. The only degree-1 Schur functor is `S_(1)=Id`, so in
my corner the whole Young-diagram classification degenerates to "the only indecomposable is `Id`,
the functor is `Id^N`" — and that degeneration IS the biproduct collapse. Horn 2 (additive vs
analytic) is the answer, sharpened: my additive lifting is exactly the `n=1` term `M_1⊗W` of the
analytic expansion (a degree-1 truncation, not a disjoint world); equivariance (horn 1) is a facet
of the same degree fact (`S_1` trivial ⟹ invisible in degree 1). Schur does NOT touch my real
content: the morphism-layer extensivity crux `∐⊊⊕` and the `◁`-comonoid = family-of-`k`-algebras
result. (Adversarial catch: species DO carry plethystic substitution = analytic `◁`, and my `◁` is
its degree-1 shadow — but the shape-indexed comonoid classification is mine.)

**Correction banked:** the object-collapse theorem needs **cocontinuous** (Eilenberg–Watts), not
merely "additive/finitary" — `Vec(P,−)` with `dim P=∞` and `W↦W**` are additive but NOT `Id^N`.
Cor 3.4 of the proof already uses this. **Nuance:** "shapes = indecomposable summands" is the same
Krull–Schmidt meta-principle as the semisimple `S_λ`-decomposition — partially anticipated in
spirit, though it degenerates to counting `N` in the additive corner. Grant line: "Schur =
polynomial species" classifies the *analytic* lifting and does NOT scoop the linear-container
program; the crown target's classification half is de-risked.

---
## (original question below)

## The question

My 08-18 biproduct-collapse observation: over Vec, a finite linear container's shapes are not
recoverable from the extension `⟦S,P⟧≅Id^N`; they reappear only as **indecomposable direct
summands** of `F=⊕_s Vec(P_s,−)`.

The classical (char 0) fact (nLab *Schur functor*; Baez "Schur functors I"): **Schur functors =
polynomial species = functors `core(FinSet)→FinVect` vanishing on large sets**, forming a
symmetric-monoidal abelian category, each decomposing into a finite `⊕` of Young-diagram-indexed
irreducibles `S_λ`. Read as: shapes = irreducible `S_n`-reps, positions = multiplicity spaces.

**Do these literally coincide for `S` finite, or is there a genuine mismatch?**

## The two horns

- **If exact coincidence:** the classification half of the crown target
  ([[../topics/containers-over-vec]]) is a KNOWN theorem — cite Schur/species and connect to the
  container/comonoid framing. Much faster than reproving a classification. But then "shapes =
  indecomposable summands" is a *partial scoop* — honesty demands flagging it.
- **If partial mismatch:** the difference is exactly where the new content lives. Candidate
  mismatches:
  1. Schur functors assume `S_n`-equivariance (functor on `core(FinSet)`); my linear container is
     plain shape-indexing at fixed finite `S` (no symmetric-group symmetry imposed).
  2. Schur functors are analytic (`W↦⊕(M_n⊗W^{⊗n})_{S_n}`, positions in tensor powers); mine are
     additive-per-shape (positions in the Hom slot `Vec(P_s,−)`, degree 1). My objects may be the
     `d=1`/multiplicity-free corner of the Schur world.
  3. Schur classification is over all of `FinSet`; mine is fixed finite `S`.

## How to resolve

Direct comparison (no new literature): nLab Schur-functor page + Baez "Schur functors I" against
`scratch/vec-containers-orientation.md` and `proofs/2026-08-18-linear-containers-vec.md`. Ask:
is the decomposition of `⊕_s Vec(P_s,−)` into indecomposables the same statement as the
`S_λ`-decomposition, or only its additive shadow?

## Sources (all `agent-summary`, abstract/nLab level — verify before load-bearing)

- nLab *Schur functor*; John Baez "Schur functors I" (personal nLab).
- Sam–Snowden `arXiv:1209.5122` (species/TCA — owns the Day/⊗ axis).
- Background: Krause `arXiv:1203.0311`; Djament–Touzé `arXiv:2407.10522`; Touzé `arXiv:2607.00631`.

## Related

[[../topics/containers-over-vec]] · [[extensivity-is-the-container-boundary]] · char-p caution:
David Speyer trap (`S_(2)≅S_(1,1)` pointwise, distinct as functors).
