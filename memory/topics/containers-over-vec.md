# Topic: Containers over Vec (the linear-container front)

**Opened:** 2026-08-15 by Neil (email steer). Monads/comonads declared "done enough"; pivot to
**containers over a linear base `Fam(Vec^op)`**. First rigorous result 08-18.
**STATUS (08-20): front CLOSED.** All three faces proved (08-18/19), Schur situated (08-19), crown
algebroid resolved as a `Mat(Vec)` matrix comonoid (08-20, classical → EXPOSITORY Part 4, 22pp). The
only live sequel is the **obstruction layer** (linear-ZS `[ω]`), scaffolded but HELD pending a direct-
read pass. See "Crown target — RESOLVED" and "NEXT LAYER" below.

## The object

A **linear container** `(S,(P_s))`: a set `S` of shapes, each with a vector-space position
`P_s ∈ Vec_k`. Extension
```
⟦S,P⟧ W  =  ⊕_{s∈S} Vec_k(P_s, W)  ≅  ⊕_s W^{n_s}     (n_s = dim P_s)
```
an additive polynomial (degree-1) endofunctor `Vec→Vec`. Fibrewise map `h_k = Id`.
Question Neil posed: how much of Set container theory (representation theorem, `DCont≅Cat`,
Day-convolution monoidal structures) survives over `Vec`?

## Established (PROVE 08-18 — `proofs/2026-08-18-linear-containers-vec.md`, registry `linear-containers-vec.json`, proved)

**Part 1 — the biproduct collapse (PROVED).** Vec's terminal is `0`, so `⟦S,P⟧(0)=0`: the Set
slogan `F(1)=S` DIES. Finite `S` + finite-dim positions ⟹ `⊕=Π=biproduct` ⟹ `⟦S,P⟧≅Id^N`,
`N=Σ dim P_s = dim(⊕_s P_s)`; a finite linear container is classified by the single number `N`.
`End(Id)=k` (field) ⟹ Krull–Schmidt makes `Id^N` the unique indecomposable decomposition —
recovers `N`, nothing about the shape partition. Shapes reappear only as **indecomposable direct
summands** of `F=⊕_s F_s`.

**Part 2 — the extensivity crux (PROVED, negative-with-remedy).**
`Nat(⟦S,P⟧,⟦T,Q⟧)=∏_s ⊕_t Vec(Q_t,P_s)` vs container-hom `∏_s ∐_t Vec(Q_t,P_s)`; the extension
`⟦−⟧` induces `∐_t ↪ ⊕_t`, so it is faithful but **NOT full**. In Set the hom-formula coproduct
IS the disjoint union (`⊕=∐`) ⟹ full+faithful (classical Diers). The ONLY thing that changes
Set↝Vec is `∐ ⊊ ⊕` = **failure of extensivity**. Object-collapse (Σ→biproduct) and
morphism-collapse (∐→⊕) are ONE phenomenon — the claimed novelty delta. See
[[extensivity-is-the-container-boundary]].

**Part 3 — the `◁`-comonoid (PROVED 2026-08-19, was COMPUTED).**
`proofs/2026-08-19-vec-comonoids-algebras.md`, registry node `part3-comonoid-algebras` (proved).
F.d. `(S,P)◁(T,Q)=(S×T,(P_s⊗Q_t))`, unit `({*},k)`; NOT the Set dependent sum (linearity kills
dependency). **`◁`-comonoid = a FAMILY `(A_s)` of unital associative `k`-algebras**, one per shape,
no cross-shape composition. Functorially **`Comon_◁(Fam(Vec_fd^op)) ≅ Fam(Alg_k^op)`**
(cocommutative ↔ `Fam(CAlg_k^op)`). Position-contravariance does the work:
`δ♯_s=μ_s:P_s⊗P_s→P_s`, `ε♯_s=η_s:k→P_s` — a *co*monoid over Vec is an *algebra* (same fibrewise
op as monad→comonad transfer). This is the exact `◁`/Vec analogue of the Set result
[[bare-dirichlet-comonoid-proved]] (`⊗`-comonoid in Poly = family of monoids), one enrichment up
(monoid ⤳ k-algebra). **Crown algebroid guess REFUTED in f.d.:** counit forces `δ_shape=diagonal`
(S is the unique `(Set,×)`-comonoid) ⟹ δ never reaches an off-diagonal block `P_a⊗P_b` (a≠b) ⟹
disjoint one-object k-linear cats = algebras, not a multi-object algebroid. Hypotheses SHARPENED:
f.d. positions only, **S arbitrary** (finite S not needed). Real algebroids need a
dependency-carrying (lax/bimodule) `◁` — the honest sequel.

## ★★ The one collapse, THREE faces (all proved as of 08-19)

The whole Vec front is a single phenomenon — **linearity flattens the Set dependent sum** — seen
on three layers. Same root cause each time; only the layer differs.

| Face | Set structure | Vec collapse | Consequence |
|------|---------------|--------------|-------------|
| **Objects** (Part 1) | `F(1)=S`, `⟦S,P⟧=∐_s(−)^{P_s}` | terminal`=0`, `∐=⊕=Π` biproduct | `⟦S,P⟧≅Id^N`; shapes invisible |
| **Morphisms** (Part 2) | hom-`∐` = shape disjoint union | `∐ ⊊ ⊕` (non-extensive) | `⟦−⟧` faithful not full |
| **Comonoids** (Part 3) | comp-shapes `= Σ_s S^{P_s}` (dependent sum encodes composable arrows) | flattens to plain product `S×S` | `δ_shape` diagonal ⟹ algebroid dies ⟹ family of algebras |

The Set dependent sum `Σ_s S^{P_s}` is *exactly* what `DCont≅Cat` uses to record composable arrows;
linearity replaces it by `S×S`, so the multi-object (algebroid) structure cannot survive. Face 3 is
the deepest reading of extensivity-failure: not just "shapes invisible" (Face 1) or "hom not full"
(Face 2) but "**the composition data itself is destroyed**." → [[extensivity-is-the-container-boundary]].

## Neighbour ownership ledger (browse 08-18, `reading/2026-08-18-vec-containers-neighbours.md`)

Each moving part is individually owned; novelty is in the ASSEMBLY + the extensivity obstruction.

- **Strict polynomial functors** (Friedlander–Suslin Invent. Math. 127 (1997); Krause
  `arXiv:1203.0311`; Touzé `arXiv:2607.00631`). OWN the degree-graded scheme-theoretic
  classification (Schur algebras `P_d ≃ S(n,d)`-mod, Koszul/Ringel/Serre duality). Additive =
  degree 1 = `P_1 ≃ Vec_k` — my corepresentables `Vec(P,−)` live entirely in their `d=1` corner;
  they never ask for the shape set or the `◁`-monoid. `agent-summary` (abstract/definitions).
- **Linear species / TCA** (Sam–Snowden `arXiv:1209.5122`; Joyal). OWN the Day-convolution /
  analytic-functor `W↦⊕(M_n⊗W^{⊗n})_{S_n}` account. My `⊕_s Vec(P_s,W)` = additive-positions
  special case (positions in the Hom slot, not tensor powers). Species own the `⊗`/Day axis.
- **Familial representability** (Diers 1977, nLab *multirepresentable functor*; Carboni–Johnstone
  1995; Freyd 1966; Adámek–Rosický 1994). OWN "coproduct of representables ⟺ generic
  factorizations." The extensivity hypothesis is exactly what Vec violates — THE load-bearing
  fact. Read this before proving any Vec representation theorem.
- **Polynomial functors over a base** (Gambino–Kock `arXiv:0906.4931`; Weber `arXiv:1106.1983`
  "Polynomials in categories with pullbacks", 2011). OWN poly functors over LCC/extensive bases.
  Vec is neither LCC nor extensive ⟹ machinery does not transfer — the same obstruction. **Weber
  weakens GK from LCCC down to mere categories-with-pullbacks** (a rung between GK and Walker in the
  weakening tower — see [[../connections/weakenings-of-sigma-pi-delta-vec-fails-all]]). **DEEP-READ
  2026-08-28 (Q3 RESOLVED, branch b):** "categories with pullbacks" is shorthand — Weber actually
  requires each polynomial's **middle leg exponentiable**, via **distributivity pullbacks** (comparison
  **δ iso**). Vec has pullbacks but NOT exponentiable legs, so it fails Weber same as GK/Walker; the
  abelian-pullbacks hope was a red herring. **Spinoff (live):** Weber's δ-iso ≟ my proved T2 Φ
  familial-representability — same "canonical comparison iso" shape → [[../questions/weber-delta-vs-t2-phi]].
  Companion fibrational/comprehension source cluster
  (all from Walker's bibliography, browse `2026-08-27-browse2`): Street "Polynomials as spans"
  `1903.03890`; Street–Verity comprehensive factorization (TAC 2010); Najmaei–van der Weide–Ahrens–
  North "Type Theory for Comprehension Categories" `2503.10868` (non-full/non-split fibrations);
  Arkor–Fiore `2006.16949`. This is Front D approach (3), previously empty, now sourced.
- **Locally subcartesian closed categories / subcartesian polynomials** (Walker `arXiv:2607.10242`,
  2026; lineage Street protocalibrations / Weber distributivity pullbacks — INDEPENDENT of
  Gambino–Kock). A *fourth weakening* (added 2026-09-01 browse, `agent-summary` depth): affine
  base-change `∇_f ⊣ ⊠_f` via **subpullbacks** exists even when `Σ⊣Δ⊣Π` fails; slice tensor
  `g⊗_Y f≅Σ_f∇_f(g)` right-closed-not-cartesian; motivating tensor `A+B−X` (Lawvere quantale) is
  structurally Vec's additive `⊗/⊕`. Thm 5.2.8 = bicategory of subcartesian polynomials ≃ poly
  functors with "bunched strength" (Street-span framing vs my family-`∐`). **Owns nothing about Vec**
  — the open question "does Vec/`Fam(Vec^op)` carry a subpullback structure it can't carry an LCCC
  structure?" is unclaimed → [[../questions/vec-subcartesian-closure]]. Direct-read owed before
  load-bearing.
- **k-linear categories / algebroids** (Mitchell, *Rings with several objects*, Adv. Math. 8
  (1972); nLab *algebroid*). The TARGET vocabulary: "poly-comonoid over Vec = k-linear category
  (algebroid)" is the Vec-analogue of `DCont≅Cat`. Not a scoop — the identification is what would
  be NEW if proved.
- **Schur functors = polynomial species** (nLab; Baez "Schur functors I"). ✅ RESOLVED 08-19
  ([[../questions/vec-schur-coincidence]], `expository` §8): **NOT a scoop.** My additive lifting is
  the *forced homogeneous degree-1 corner* — a `Vec`-functor is automatically additive (degree 1);
  `S_λ` with `|λ|≥2` act as `λ^{|λ|}` on scalars so are not even `Vec`-functors. The only degree-1
  Schur functor is `S_(1)=Id`, so in my corner the Young-diagram classification *degenerates to
  `Id^N`* — and that degeneration IS Face 1 of the collapse. My additive lifting = the `n=1` term
  `M_1⊗W` of the analytic expansion `⊕(M_n⊗W^{⊗n})_{S_n}`. Schur does NOT touch the morphism-crux
  (Face 2) or the `◁`-comonoid classification (Face 3) — those are mine.

**SCOOPING VERDICT:** "Containers over Vec" is genuinely open as a framing; no source assembles
these into a container/directed-container theory over Vec, and none confronts the non-extensivity
gap. That gap is both the risk (naive theorem false) and the opening (coordinate-free
reformulation is new).

## Crown target — RESOLVED 08-20 (the algebroid lives in Mat(Vec); front CLOSED)

**Poly-`◁`-comonoid over Vec = k-linear category (algebroid).** Mirrors Set-side `DCont≅Cat/Cof`.
The *strict* single-index `◁` guess is **REFUTED** (Part 3, proved: strict `◁`-comonoid = family of
algebras = disjoint one-object algebroids). **RESOLUTION (08-20 WAKE, [[vec-lax-matrix-crown-resolved]],
registry `lax-matrix-crown-resolved`, computed):** the genuine algebroid lives NOT in single-index
`Fam(Vec^op)` but in the **bicategory of Vec-matrices `Mat(Vec)`** — objects = Vec-enriched graphs
`(S,(P_{a,b})_{S×S})`, composition the **matrix product `(P◁Q)_{a,c}=⊕_b P_{a,b}⊗Q_{b,c}`** (the `⊕_b`
is exactly the extensivity coproduct whose absence `∐⊊⊕` caused the collapse). A (co)monoid there IS a
k-linear category = algebroid (classical **Bénabou 1967 / Mitchell 1972 / `arXiv:1704.00329`** variance);
the strict single-index `◁` is its **DIAGONAL degeneration**. So the crown guess was RIGHT — it just
needed double-indexing. **But the mathematics is CLASSICAL ⟹ novelty LOW ⟹ routed to EXPOSITORY, not
PROVE.** The container-theoretic contribution is the **diagnosis** only (which extensivity step kills the
naive linear `DCont≅Cat`, and where the coproduct must move to restore it). Written up as **Part 4 of
`expository/containers-over-vec.tex` (22pp, compiles clean, 08-20 WRITE)**. This CLOSES the linear-container
front Neil opened: all three faces + the algebroid resolution + the single non-extensivity obstruction.
**TODO before circulation:** direct-read D. Lin, *Enriched Polynomial Functors*, to confirm it doesn't
already state this Mat(Vec) framing (flagged in the 08-20 write log).

## NEXT LAYER (scaffolded 08-20 browse, HELD — not a trigger) — the obstruction layer

With the algebroid *object* resolved, the natural sequel is the **obstruction to composing two linear
containers**: a "Zappa–Szép / smash product of algebras" carrying a degree-2 class, the exact one-
enrichment-level-up mirror of the group ZS `[ω]∈H²(B;A)` spine. **Front #1 now has a literature
scaffold AND is a genuinely open niche** (browse `reading/2026-08-20.md`):
- **Mastnak `math/0210123`** — five-term exact sequence for low-degree cohomology of a **smash product
  of cocommutative Hopf algebras**, *explicitly generalizing Tahara 1972* (the exact group-side citation
  MacBeth already uses for `[ω]`). This is one level up (Hopf algebras vs groups) — where a linear-ZS
  obstruction class would live. **Direct-read before any PROVE.**
- **`math/0212003`** — Hochschild cohomology *ring* of a **group crossed product** (closest to the
  algebroid/matrix setting already resolved); nLab *crossed product algebra* + *cocycled crossed products*
  gives the multiplication shape `(a⊗h)(a'⊗h')=Σ a(h₁▹a')⊗h₂h'` to match against `Mat(Vec)`'s `⊕_b`.
- **Genuinely open:** direct arXiv phrase search "Zappa–Szép product [of] algebras" returns only 5 papers,
  all 2004–2020, all group-theoretic or self-similar C\*-algebraic — **zero 2025–26**. First-mover niche
  (same "unclaimed territory" signal that cleanly closed past fronts) — flag to Neil.
- Banerjee–Kour(–Paik) **measurings** program (`2607.17470`, `2504.06873`) is the recurring active hub
  around Mitchell `1704.00329` — Hochschild homology of enriched-over-algebras categories; standing watch.
→ [[cohomological-obstruction-family]] sighting #8; all `agent-summary` depth.

## Traps

- **David Speyer char-2 trap** (n-Café 2007): `S_(2)≅S_(1,1)` pointwise yet distinct as functors.
  Biproduct collapse `⟦S,P⟧W=W^N` says functors *evaluate* the same, NOT that shapes collapse to
  one functor. Flag in any char-p extension.
- Provenance caveat: the expository `containers-over-vec.pdf` §8 neighbour citations are
  general-knowledge attributions, NOT deep-read into `sources.json` — verify before circulation.

## Deliverables

- PROVE: `proofs/2026-08-18-linear-containers-vec.md` (proved). Expository:
  `expository/containers-over-vec.pdf`. Orientation: `scratch/vec-containers-orientation.md`.
  Collaborator note: `for-collaborator/2026-08-18-linear-containers-vec-biproduct-collapse.md`.
- Auto-memory: [[vec-containers-new-front]], [[vec-biproduct-collapse-proved]].

## Gaps / next

1. ~~Schur-coincidence check~~ ✅ RESOLVED 08-19 (degree-1 corner, not a scoop).
2. ~~Prop 6.3 comonoid-law verification~~ ✅ PROVED 08-19 (`part3-comonoid-algebras`).
3. ~~The lax/bimodule `◁` for genuine algebroids~~ ✅ RESOLVED 08-20 (= `Mat(Vec)` matrix comonoid,
   classical → EXPOSITORY Part 4). **Front CLOSED.** See Crown section above.
4. **NEXT (obstruction layer, HELD)** — linear-ZS / smash-product `[ω]` (Mastnak `math/0210123`,
   `math/0212003`). Needs a direct-read pass first; genuinely open niche. See "NEXT LAYER" above.
5. General (infinite / inf-dim) representation theorem — open (Diers extensivity obstructs).
   Djament–Touzé `2407.10502` (Fp-linear additive base) may or may not route around `∐≠⊕` — full read.
## Applied face landed (WRITE 08-24) — either-prompt = biproduct

`containers-over-vec.tex` now 27pp (compiles clean). Two Neil-requested pieces added:
- **§2 "The structure of Vec, for the container-minded"** — Set/Vec side-by-side recap, no proofs, each
  fact forward-points. Vec HAS: zero object, finite biproducts, kernels/cokernels (KS), self-enrichment.
  Vec LACKS: extensivity (`∐⊊⊕`, CLW 1993), disjoint injections, subobject classifier, shape-detecting
  terminal. Punchline: the single failure of extensivity is the whole note.
- **§9 "Application: handling either prompt is the biproduct"** — Prop 9.2 `h_A⊕h_B≅h_{A⊕B}`; the
  either=both reading; ties forward to §8 algebroid via the shared `⊕`. See
  [[../connections/extensivity-is-the-container-boundary]] "two valuations" section. NO new math/citations.
- §9 prose written to lift cleanly into the separate applied section (Workers/Vec) Neil flagged.

6. Provenance debts: `containers-over-vec.pdf` §8 neighbour citations still general-knowledge, not
   deep-read into `sources.json`. **nLab "extensive category" IS now indexed** (browse 08-19) — "Vect
   is not even finitely extensive" (Carboni–Lack–Walters 1993) is the primary citable anchor for Face 2.
   Part 4 provenance box names Bénabou/Mitchell/`1704.00329` — also general-knowledge, verify + D. Lin
   *Enriched Polynomial Functors* direct-read before circulation.
