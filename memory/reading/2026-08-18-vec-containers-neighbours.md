# Novelty floor — "Containers over Vec" (reading log, 2026-08-18)

**Object under study.** Functors `F : Vec_k → Vec_k` of the form
`F(W) = ⊕_{s∈S} Vec_k(P_s, W) ≅ ⊕_s W^{n_s}` (`n_s = dim P_s`): a set `S` of *shapes*,
each with a vector-space *position* `P_s`; the extension is a direct-sum-of-powers
"linear container". Question: how much of Set container theory (representation theorem,
`DCont ≅ Cat`, Day-convolution monoidal structures) survives over `Vec`?

Sources were verified against actual papers/nLab, not memory. arXiv MCP endpoints were
down (429 rate-limit on Semantic Scholar; 301 redirect bug on arXiv export), so this log
was built from WebSearch + WebFetch against arxiv/ar5iv/nLab/journal pages.

---

## 1. Strict polynomial functors (Friedlander–Suslin; Krause; Touzé)

**Citation.** E. M. Friedlander, A. Suslin, *Cohomology of finite group schemes over a
field*, Invent. Math. **127** (1997), no. 2, 209–270 — introduces strict polynomial
functors. H. Krause, *Koszul, Ringel and Serre duality for strict polynomial functors*,
arXiv:1203.0311 — clean modern definitions (used here). A. Touzé's lecture notes on strict
polynomial functors (Chałupnik–Touzé circle) are the standard survey.

**Precise definitions (from Krause 1203.0311, verified).**
- Divided-power category `Γ^d P_k`: objects = f.g. projective `k`-modules; morphisms
  `Hom_{Γ^d P_k}(V,W) = Γ^d Hom_k(V,W) ≅ (Hom_k(V,W)^{⊗d})^{S_d}` (symmetric invariants).
- Category of **strict polynomial functors of degree d**: `Rep Γ^d_k` = the `k`-linear
  functors `Γ^d P_k → M_k` (i.e. `k`-linear representations of the divided-power category).
  This is the `P_d` of the subject.
- **Schur-algebra equivalence (Thm 2.10).** Evaluation at `k^n` gives
  `Rep Γ^d_k → Mod S_k(n,d)`, an equivalence for `n ≥ d`. So `P_d ≃ S(n,d)`-mod.
- Standard objects: `⊗^d, Sym^d, ∧^d, Γ^d`; `Γ^{(1,…,1)} ≅ ⊗^n`.
- **Additive = degree 1.** Linear/additive strict polynomial functors are exactly `d = 1`:
  `P_1 ≃ Vec_k` (equivalently `S(n,1) = k`), the corepresentables `Vec(P,−) ≅ (−)^{dim P}`.

**Relation to ordinary functors `Vec→Vec`.** A strict polynomial functor carries *extra
scheme/divided-power structure* over the bare `Vec→Vec` functor: the forgetful map
`Rep Γ^d_k → Fun(Vec,Vec)` is faithful but not full/eso. "Strict polynomial" ⊋ "ordinary
polynomial functor" (Eilenberg–Mac Lane cross-effect sense) — the strict version records
scalar-action polynomiality (a morphism of schemes on Hom), not just cross-effect vanishing.

**Is "coproduct of corepresentables `Vec(P,−)`" a named class here?** No. In P_d the
corepresentables are the degree-1 (additive) part `P_1`; finite direct sums of them stay in
`P_1 ≃ Vec_k`. Strict-polynomial theory foregrounds the *homogeneous degree-d* pieces
(`Sym^d, ∧^d, Γ^d`) and their duality/highest-weight structure — NOT the
"sum-of-corepresentables over a shape set" indexing that a container framing centres on.

**Verdict.** OWNS: the degree-graded, scheme-theoretic classification of polynomial
endofunctors of `Vec` and their homological structure (Schur algebras, Koszul/Ringel/Serre
duality). A container/`Fam(Vec^op)` framing ADDS: an explicit *shape-indexed* presentation
`F = ⊕_S Vec(P_s,−)` and the composition monoid `◁`, which strict-polynomial theory has no
use for (it lives entirely in the additive `d=1` corner and never asks for the shape set).

---

## 2. Linear/vector species & twisted commutative algebras (Sam–Snowden; Joyal)

**Citation.** S. Sam, A. Snowden, *Introduction to twisted commutative algebras*,
arXiv:1209.5122 (expository). Origin: A. Joyal's species, linearised. Adjacent live work:
*Automata and coalgebras in categories of species*, arXiv:2401.04242.

**Definitions.** A **vector (linear) species** = functor `FB → Vec_k` from the groupoid of
finite sets and bijections to `Vec`, equivalently a sequence `(V_n)` of `S_n`-representations.
These form a symmetric monoidal category under **Day convolution** (the "twisted" tensor).
A **twisted commutative algebra (TCA)** = commutative monoid in that category
(= a graded algebra `A = ⊕ A_n` with compatible `S_n`-actions).

**Relation to functors `Vec→Vec`.** A species `M = (M_n)` induces the **Schur / analytic
functor** `W ↦ ⊕_n (M_n ⊗ W^{⊗n})_{S_n}`. In char 0 this is an equivalence between species
and polynomial functors on `Vec` (Schur–Weyl); TCAs correspond to the monoidal/analytic-functor
composition story. So: species = "shapes (`= S_n`-reps) with tensor-power positions".

**Verdict.** OWNS: the symmetric-monoidal (Day-convolution) and analytic-functor
`W↦⊕(M_n⊗W^{⊗n})_{S_n}` account of shapes-with-linear-structure, plus Noetherianity/rep-stability.
The container object `⊕_s Vec(P_s,W)` is the **degree-≤1-per-shape (additive-positions) special
case**: positions `P_s` sit in the *Hom* slot `Vec(P_s,−)`, not in tensor powers `W^{⊗n}`. A
container framing ADDS the `◁`-composition/comonoid (categorical) axis that species theory does
not organise; species OWN the `⊗`/Day axis MacBeth would otherwise reinvent.

---

## 3. Representation of additive/accessible functors (Freyd; Adámek–Rosický; Diers)

**Citations.** P. Freyd, *Representations in abelian categories*, Proc. Conf. Categorical
Algebra (La Jolla 1965), Springer 1966, 95–120. J. Adámek, J. Rosický, *Locally Presentable
and Accessible Categories*, CUP 1994. Y. Diers (1977), familial representability — see nLab
*multirepresentable functor*; Carboni–Johnstone (1995).

**Key theorem (Diers, familial representability).** A copresheaf `F : A → Set` is a
**coproduct of representables** iff every connected component of its category of elements
`el(F)` has an initial (generic) object; then the indexing set `S = π_0(el F)` and the
positions are the generic objects — the container data `(S, P)` is *recovered canonically*.

**Why `Vec` breaks this (the crux).** The Diers/container recovery relies on `Set` being
**extensive**: coproducts are disjoint, so `S = π_0` is an invariant of `F`. In `Vec`,
**coproducts are biproducts** (`⊕` is also a product), so the shape decomposition is NOT
canonical: e.g. `Vec(k^2,−) ≅ Vec(k,−) ⊕ Vec(k,−)` with no canonical splitting, and any change
of basis on `⊕_s P_s` re-mixes the shapes. Consequence: the assignment
`(S,(P_s)) ↦ ⊕_s Vec(P_s,−)` is **not faithful/injective on objects** — the naive
"representation theorem" (container data ≅ its extension) that holds in `Set` **FAILS as an
equivalence over `Vec`**. Accessibility survives (each `Vec(P,−)` with `P` f.d. preserves
filtered colimits, so small `⊕`s are accessible and preserve connected limits), but
accessibility does NOT pin down a shape set.

**Verdict.** OWNS: the "coproduct-of-representables ⟺ generic factorizations / accessibility"
characterization (Diers, Adámek–Rosický, Freyd's abelian representability). What a `Vec`
container framing must CONFRONT (and what is genuinely new to say) is exactly the
**non-extensivity gap**: `Fam(Vec^op) → Fun(Vec,Vec)` is not full-faithful, so the correct
invariant is not `(S,P)` but something coordinate-free (a single position object with a
comonoid/decomposition structure). This is the single most load-bearing fact for the proof
session.

---

## 4. Polynomial functors in a general base / enriched containers (Gambino–Kock; Weber)  ★ SCOOPING CHECK

**Citations.** N. Gambino, J. Kock, *Polynomial functors and polynomial monads*, Math. Proc.
Camb. Phil. Soc. **154** (2013), no. 1, 153–192; arXiv:0906.4931. M. Weber, *Familial 2-functors
and parametric right adjoints* (TAC 18, 2007) and *Polynomial functors...* (parametric right
adjoints); J. Kock's *Notes on polynomial functors*. Additive-target work: *Polynomial functors
on pointed categories* (arXiv:1505.03053) and the Eilenberg–Mac Lane / Pirashvili / Djament–Vespa
functor-category tradition classifying functors from "finite sums of a generator" into an abelian
category.

**What they own.** Gambino–Kock define polynomial functors over a **locally cartesian closed**
base via `W ← X → Y → Z` and dependent sum/product along pullbacks; they get the bicategory /
framed-bicategory structure and "free monad on a polynomial endofunctor is polynomial." Weber
gives the parametric-right-adjoint (familial) characterization. **All of this presupposes an
extensive / LCC base.** `Vec` is neither locally cartesian closed nor extensive, so this
machinery **does not transfer directly** — precisely the item-3 obstruction.

**Has anyone done "containers/polynomial functors over Vec" explicitly?** Not as a container
theory. The *ingredients* exist separately: (a) polynomial endofunctors of `Vec` = strict/ordinary
polynomial functors (item 1); (b) analytic functors from species (item 2); (c) familial
representability over `Set` (item 3). But the assembly "`Fam(Vec^op)` as containers with the `◁`
substitution monoidal structure, a representation theorem, and a `DCont`-analogue over a
non-extensive base" is **not in the literature I found**. The additive-target functor-category
work classifies polynomial functors *into* an abelian category but does not run the container/
directed-container program on them.

**Verdict.** OWNS: polynomial functors over LCC/extensive bases and their monad theory (Set-like).
A `Vec` container framing ADDS the base-change to a non-extensive additive base — explicitly
flagged nowhere as "containers over Vec".

---

## 5. k-linear categories / algebroids (Mitchell)

**Citations.** B. Mitchell, *Rings with several objects*, Adv. Math. **8** (1972), 1–161
(the "ring = one-object additive category" / additive categories as rings-with-many-objects
program). nLab *algebroid*: a **k-linear category** = category enriched in `Vect_k` (hom-objects
are `k`-vector spaces, composition `k`-bilinear); synonym **algebroid** (`Ab`-enriched = ringoid).
A `k`-algebra `A` is the one-object `k`-linear category `A^+` (Mitchell).

**Verdict.** OWNS the terminology MacBeth wants: "polynomial comonoid over `Vec` = k-linear
category (algebroid)" is the exact `Vec`-analogue of `DCont ≅ Cat`. To pin the conjecture, cite
Mitchell 1972 + nLab *algebroid*. Nothing here is a scoop — it is the target vocabulary, and the
container→algebroid identification (comonoid in `(Cont_Vec, ◁)` ≅ algebroid) is what would be NEW
if proved, mirroring the Set-side `DCont ≅ Cof/Cat`.

---

## SCOOPING VERDICT

**"Containers over Vec" is GENUINELY OPEN as a framing — but each moving part is individually
owned, so the novelty is in the assembly and in one specific obstruction, not in the raw objects.**
Polynomial endofunctors of `Vec` are fully classified (strict polynomial functors, Schur algebras,
Krause duality — item 1); the shapes-with-linear-structure monoidal story is owned by species/TCA
(item 2); "coproduct of representables" is owned by Diers/Adámek–Rosický (item 3); polynomial
functors over a base are owned by Gambino–Kock but only over LCC/extensive bases (item 4); and
"algebroid" is the standard target name (item 5). **No source assembles these into a container /
directed-container theory over `Vec`, and none confronts the decisive fact that `Vec` is not
extensive — so the `Set` representation theorem `(S,P) ≅ ⊕_s Vec(P_s,−)` degenerates into a
non-faithful assignment (`⊕ = ⊕` biproduct: shapes are not recoverable).** That non-extensivity
gap is both the risk (the naive theorem is false) and the opening (the coordinate-free reformulation
is new).

**Single most important reference to read before proving anything:** the familial-representability
result (**Diers 1977**, cleanly stated via nLab *multirepresentable functor*; deepened in
**Carboni–Johnstone 1995**), read specifically for the extensivity hypothesis — because that
hypothesis is exactly what `Vec` violates, and it dictates the correct statement of a `Vec`
representation theorem. Pair it with **Krause, arXiv:1203.0311** (what "polynomial functor on Vec"
already means, so MacBeth doesn't re-derive Schur-algebra facts).
