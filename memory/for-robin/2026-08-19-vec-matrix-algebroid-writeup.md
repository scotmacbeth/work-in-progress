# Note for Robin — the linear-container arc is closed (write-up done)

**2026-08-19 WRITE session.** No email this session (write-session rules), so leaving this here;
you can read the file directly from the host.

## What I did
Added **Part 4** to `expository/containers-over-vec.tex` (§`sec:algebroid`, "the correct home:
linear directed containers are Vec-matrices"). The note is now **22 pages, compiles clean** with
`pdflatex` (no undefined refs). This closes the linear-container / `Fam(Vec^op)` front Neil opened
on 08-15.

## The punchline (one paragraph)
Part 3 of the note found that `◁`-comonoids over `Fam(Vec^op)` are only **families of k-algebras**,
not algebroids — an apparent defeat. Part 4 shows this was a **modelling error, not Vec's fault**.
A single-index container offers *one* position space per shape, but a Vec-enriched category
(algebroid) needs a hom-space per *ordered pair* of objects. Correct the data to a **matrix of
vector spaces** `(S,(P_{a,b}))` — a Vec-graph, i.e. a 1-cell of the matrix bicategory `Mat(Vec)` —
and the composition writes itself as the **matrix product** `(P⊙Q)_{a,c}=⊕_b P_{a,b}⊗Q_{b,c}`. Its
monoids are algebroids (Bénabou); its comonoids-via-the-fibrewise-op are algebroids too. The strict
single-index `◁` is exactly the **diagonal degeneration** (`P_{a,b}=0` for a≠b), which is *why* the
counit-forced shape-diagonal in the comonoid classification gave only one-object categories. The
whole four-part note now reads as one obstruction: **Vec is not extensive** (`∐⊊⊕`); the algebroid
reappears precisely when the matrix `⊕_b` puts the coproduct back on the *composition* index instead
of the shape index.

## Honesty status (important)
The mathematics of Part 4 is **classical** — Bénabou 1967 (monad in a matrix/span bicategory =
enriched category), Mitchell 1972 (algebroid = ring with several objects), arXiv:1704.00329 (the
monad/comonad-in-V-Mat variance). I present it strictly as a **container-theoretic diagnosis**, with
a boxed provenance caveat in the section, not as a new theorem. The only thing that is *mine and
proved* is the identification "single-index = diagonal fragment of the Vec-matrix bicategory," which
is an elementary corollary of the (now proved) §7 comonoid classification. I did **not** upgrade the
classical equivalences to "proved" in the registry — they stay cited.

## Collateral changes
- Prop `prop:comonoid` (comonoid = family of algebras) upgraded **computed → proved**, citing the
  companion `proofs/2026-08-19-vec-comonoids-algebras.md`.
- Carry-over table: comonoid row now "proved"; new row for the `Mat(Vec)` resolution.
- Open question 2 rephrased "resolved, then sharpened" (the classical part is settled; live
  questions are: is `Mat(Vec)` the extension of a clean container-style structure? does it survive
  dropping finite-dimensionality? is the diagonal embedding unique?).
- Abstract + "why this matters for the grant" paragraph updated to carry the resolution.

## One TODO before this goes anywhere external
Direct-read **D. Lin, "Enriched Polynomial Functors"** to confirm it doesn't already state this exact
framing (it's the closest existing enriched-polynomial program). And keep disambiguating from
arXiv:1209.0940 / 1403.0833, where "linear" means linear *logic*, not Vect-enrichment. Both flagged
in the provenance box; neither is a browse-session I can run here.

## Grant angle
This links the container program to **representation theory** (algebroids = k-linear categories) and
gives the "extensivity is the container boundary" chapter its cleanest statement: the categorical
spine `DCont ≅ Cat` *does* lift to Vec, provided you move the coproduct from the shape index to the
composition index. That's a quotable one-liner for the theory section.

Files: `expository/containers-over-vec.{tex,pdf}`. Memory `[[vec-lax-matrix-crown-resolved]]`.
— MacBeth
