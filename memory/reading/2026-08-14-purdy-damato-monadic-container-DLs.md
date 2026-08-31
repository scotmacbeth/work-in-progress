# Reading log — 2026-08-14 — Purdy–Damato, Distributive Laws of Monadic Containers (arXiv:2503.17191v2, 2025)

Seed PDF: `pdf/directed-containers/Purdy-Damato_Distributive-Laws-of-Monadic-Containers_2025.pdf`.
Direct-read (research agent) aimed at the flagged Purdy–Damato collaboration idea + the DL landscape.

## The one-line placement
**Monad-side DUAL of Ahman–Uustalu 2013** ("Distributive laws of directed containers", Progress in
Informatics). Monadic container (Def 8) = Uustalu mnd-container = lax Σ-universe (Altenkirch–Pinyo);
⟦S◁P⟧ is a *monad* on Set. Directed container (Def 15) is the *comonad* side. My ZS/H² work lives on
the **directed (comonad) corner** = AU's corner; Purdy–Damato add the monad–monad corner + the two
mixed corners. **Orthogonal/dual, NOT a specialization** — the four theories meet only through the
shared bridge "matching pairs of monoid actions ≅ ZS product of monoids" (Brin).

## The bridge to my world
Example 22 + Prop 24/25: a matching pair of monoid actions gives a DL of two **writer** monadic
containers whose composite is the writer on the **Zappa–Szép product A⋈B**. Same Brin ZS target I
hit, from the monad corner. Cite as the monad-side realization of "orchestration = ZS weld."

## The collaboration niche (why this matters)
- **No cohomology anywhere.** Existence/uniqueness by direct equational analysis; the §7 no-go
  (**Thm 35 "Too many constants"**, via (S3)/Def 33/Lemma 34, Cor/Ex 36: no DL of list over a
  coproduct monad) is **Zwart–Marsden-style counting**, not H². So my `[ω]∈H²(Sk_C;𝒟)` obstruction
  has **no analogue there** → clean open niche: a cohomological existence/no-go criterion
  complementary to their counting argument. Note they cite Karamlou–Shah [20] (my `ks-nogo-not-h2`)
  as an application — adjacent to my "KS no-go is NOT H²" observation.
- **§6 "functional monoid action"** (p.14): the exotic gadget in the MIXED cell (writer-monadic over
  reader-directed) — maps α:(A→B)→A→A with 4 equations; "counterintuitively NOT a matching pair."
  Table: only that one of the four cells is exotic; they flag the asymmetry as unexplained and
  suspect it's known to algebraists. **Candidate for the skew-brace/H² lens** (cf.
  `g-obstruction-is-h2-class`, Rick's Ψ). NOT a specialization of my pure-directed ZS (that's the
  ordinary "matching pairs" cell).

## Formalization
Cubical Agda (h-sets, no univalence); 🌸-linked statements. Repos: chrisjpurdy/distr-laws-of-monadic-containers,
stefaniatadama/cubical (distr-laws branch). **First** Cubical-Agda formalization of directed
containers AND their DLs. Not formalized: assoc half of Prop 24 (Appendix A), §7 no-go (Appendix B).
My Lean 4 ↔ their Cubical Agda = a concrete cross-prover deliverable for a collaboration.

## Caveat for my notes
The "ZS/matching-pairs generalizes" claim (p.10) is Ahman–Uustalu **2013** ("Distributive laws of
directed containers", Progress in Informatics), distinct from AU16 "Directed Containers as Categories".
Both in seed; keep the citation straight (see `mnd-containers-and-update-monads-citations`).

→ feeds [[distributive-law-landscape]] (Purdy–Damato = closest technical neighbour, Agda) and the
collaboration idea raised with Neil in today's daily.
