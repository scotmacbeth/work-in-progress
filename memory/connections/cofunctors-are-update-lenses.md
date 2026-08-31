# Connection: DCont morphisms = cofunctors = (delta) lenses → Path 5 applications

**Bridges:** Path 2 (directed containers, morphism level) ↔ Path 5 (data/update,
supply chains) ↔ Path 3 (Poly comonoid morphisms).

## The claim
Today's result **DCont ≅ Cof** (directed-container maps are *cofunctors*, not
functors — see [[equivalence-chain]] and the proof note) is not just a variance
correction. **Cofunctors are the native morphisms of the bidirectional-update /
lens world.** So directed-container maps ARE update-lenses. That hands the
morphism-level theory directly to the applied paths.

## Why I believe it
- A cofunctor `D ⇸ D'` is: object map `f: S→S'` *forward*, plus for each `s` a
  lift `f♯_s : P'(fs) → P(s)` pulling D'-morphisms-out-of-fs *back* to
  D-morphisms-out-of-s, preserving identities (M1/C1) and composites (M2/C2),
  over the codomain-compatibility M0/C0. (Exactly our (M0,M1,M2).)
- This "objects forward, moves backward, with a chosen lift" signature is the
  delta-lens signature: a get on states + a chosen lift/put on transitions.
- Bryce Clarke ("Internal lenses as functors and cofunctors", ACT 2019/20;
  "Delta lenses as coalgebras for a comonad") shows delta lenses and cofunctors
  are tightly linked (a delta lens = a functor + a cofunctor sharing one object
  map; well-behaved lenses ↔ cofunctors). Ahman–Uustalu use cofunctors for
  exactly the "update" reading of directed containers.

## Why it matters (grant)
- **Supply chain (SEED Q4):** a map between two supply-chain models is a
  *cofunctor/lens*: shapes (inventory states) push forward, but a downstream
  transition pulls back to an upstream transition — i.e. how a delivery event
  *propagates back* to procurement. The sheaf/consistency condition we wanted is
  the lens' put-compatibility. The variance the grant must get right is the lens
  variance.
- **Agent orchestration:** a meta-agent over sub-agents is a cofunctor: it routes
  request-shapes down, and lifts a sub-agent's response-move back up to a
  meta-level move. "Meta-agent = functor" (our applied notes) is the wrong gadget;
  "meta-agent = cofunctor/lens" is right and *changes the count of valid maps*
  (the 20/36 hom-count gap from the proof note).

## The chase (precise breadcrumb for a wake/prove cycle)
1. Pin the exact cofunctor↔delta-lens statement from Clarke (which extra data,
   if any, upgrades a cofunctor to a delta lens). Cite it in our terms.
2. Re-read our applied `.tex`/markdown with the lens lens: every "functor between
   directed containers" → cofunctor → lens. State the put/get for the supply-chain
   example explicitly.
3. Tie to Path 3: comonoid morphisms in (Poly,◁) are cofunctors — so the Poly
   picture already says "lens." Libkind–Spivak cofree comonad = the matter a lens
   acts on.

## UPDATE 2026-06-09 (wake 2): cite-ready Clarke / Ahman–Uustalu statement

Do **not** overclaim — the slogan "delta lens = cofunctor" is **FALSE** without a
qualifier. The precise correspondence:

- A **delta lens** `(f,φ): A→B` = a **FUNCTOR** `f: A→B` (the **Get**) PLUS a
  **COFUNCTOR** `(f₀,φ): A→B` (the **Put**) on the **same object map**, satisfying
  the three delta-lens axioms — the key one being **PutGet**: `f·φ(a,u) = u`
  (the Get of a lifted update returns the *original* update `u`), plus PutId
  `φ(a,1)=1` and PutPut (φ preserves composition). [Ahman–Uustalu, "Taking
  Updates Seriously," CEUR-WS 1827, 2017; Clarke, arXiv:2108.00390, Def. 4;
  diagrammatic form `f₁∘φ₁ = φ̄₁` in Clarke arXiv:2009.06835 Cor. 20.]
  **CORRECTION (2026-06-10):** the earlier wording "`f∘φ = id` (axiom L1)" was
  WRONG — the section condition is PutGet `f·φ(a,u)=u`, NOT a bare `f∘φ=id`.
  See `reading/2026-06-10-cofunctor-delta-lens-citeready.md`.
- A **cofunctor** `(f,φ): C→D` = an object map `f: C₀→D₀` + a lifting: each
  D-morphism `u: fc→b ↦ φ(c,u): c→p(c,u)` in C, with axioms **C1**
  (`f p(c,u) = cod u`), **C2** (`φ(c,1)=1`), **C3** (`φ` preserves composition).
  Equivalently: a **span of functors**, left leg **bijective-on-objects**, right
  leg a **discrete opfibration**.
- Every lens **FORGETS** to its underlying cofunctor (Clarke thesis Lemma 2.3);
  the cofunctor is precisely the **PUT** half. A bare cofunctor lacks the
  functorial **Get**.
- **Variance confirmed:** the cofunctor lifts D-morphisms-out-of-`fc` *back* to
  C-morphisms-out-of-`c` — the opfibration/Put direction, contravariant on
  morphism-lifting, matching MacBeth's DCont position map `f♯_s: P'(fs) → P(s)`.

**Citations.**
- Bryce Clarke, "Internal lenses as functors and cofunctors," EPTCS 323 (2020)
  183–195, doi:10.4204/EPTCS.323.13, arXiv:2009.06835.
- Clarke thesis PDF:
  bryceclarke.github.io/other/the-double-category-of-lenses.pdf.
- Ahman–Uustalu, "Taking Updates Seriously," CEUR-WS 1827 (2017).
- Ahman–Uustalu, "Directed Containers as Categories," EPTCS 207 (2016),
  doi:10.4204/EPTCS.207.5 (cofree lens on a cofunctor).

**Consequence for the grant.** Under **DCont ≅ Cof**, a map of directed
containers IS the **Put** of a delta lens; to obtain a full lens you additionally
need the object map to extend to a compatible **functor** (the **Get**).
Supply-chain / agent-orchestration reading: **Get = forward state propagation**,
**Put = consistent backward update propagation**.

## UPDATE 2026-06-11 (browse): cofunctors are FUNDAMENTAL — three new sightings

The cofunctor/retrofunctor is not a niche directed-container artifact; it keeps
appearing across unrelated fields. Three new independent occurrences:

1. **Stone duality (Garner–Renata–Wu, arXiv:2603.25710, 2026)** — biggest surprise of
   the session. **Retrofunctors (= cofunctors) appear in a contravariant adjunction
   between ranked Set-monads and internal categories + retrofunctors in locales.** Fixed
   points: hyperaffine-unary monads ↔ ample localic categories. A completely independent
   domain (classical topology / locale theory) validating cofunctors as fundamental — and
   possibly a *new topological handle* on the holonomy/H² question
   ([[g-obstruction-is-baues-wirsching]]): does the ample-localic-category side see the
   (G) obstruction as a locale-theoretic invariant?

2. **Paré "Retrocells" (TAC 2024)** — cofunctors are **retrocells** in a double category
   with companions; this is the **2-categorical home** for cofunctor *morphisms* (the
   2-cells of Cof / Cat#). Topos blog "Retrotransformations" (2023): a retrotransformation
   into Span = exactly a cofunctor. Pins how DCont ≅ Cof sits inside OrgTr as a
   bicategory ([[orgtr-dcont-constant-trees]]).

3. **Aberlé "Compositional Program Verification with Polynomial Functors"
   (arXiv:2604.01303, Agda; ACT 2026)** — the lens reading becomes a *verification*
   framework. Mealy machine = cofree comonad on p at 1 = exact bridge to Lean M2b.
   **Dependent polynomials** (C preconditions, D postconditions) = specs over interfaces.
   Idea: **dependent directed containers** carrying pre/postcondition data → a lens =
   (monad implementation = Put, comonad observer = Get) bidirectional *correctness*
   framework. This is the grant's applications arm (compositional correctness with
   economic consequences) meeting the morphism-level lens theory. Thm 0.6: verifications
   compose along wiring diagrams. Aberlé will be in Tallinn — Agda, complementary to my Lean.

**nLab gaps to fill (after PRs publish):** retrofunctor page lacks directed-container
language + the Lean M4 citation; delta-lens page is 2yr stale (no Clarke 2025
Grothendieck construction arXiv:2502.21288, no poly-functor subsection).

## UPDATE 2026-06-12 (browse): the structural chain extends one link further

The equivalence chain now reaches into **double-categorical lens geometry**:

> **DCont ≅ Cat ≅ Cof ≅ Δ-lenses ≅ lax double functors B → DblSMF.**

- **Clarke, "The Grothendieck Construction for Delta Lenses," arXiv:2502.21288 (2025,
  to appear *Higher Structures*).** Delta lenses `A→B` correspond exactly to **lax double
  functors `B → DblSMF`** (the double category of sets, functions, split multivalued
  functions). So a directed-container morphism (= cofunctor = Put of a lens) is a
  *section-selection of a lax double functor* — "consistently choose images in DblSMF."
  This is the geometric/double-categorical home for the lifting data `φ(c,u)`.
- **Clarke, "Lifting Twisted Coreflections Against Delta Lenses," arXiv:2401.17250
  (TAC 41:26, 2024).** The AWFS for delta lenses is **cofibrantly generated** by a small
  double category; left class = "twisted coreflections." Consequence: **cofunctors acquire
  a universal property via the AWFS.** A fourth independent angle on "cofunctors are
  fundamental" (after Cat#, Stone duality, Paré retrocells).
- **Book action:** Ch4 should eventually capture the full chain
  DCont↔Cat↔Cof↔Δ-lens↔lax-double-functor-into-DblSMF. The right-coclosure of ◁
  (`Poly([q◁p],p')≅Poly(p,p'◁q)`, Niu–Spivak / Spivak–Srinivasan) is the *Poly-internal*
  home for the same lifting data — worth reconciling with the DblSMF picture (open Q3 in
  reading/2026-06-12).

**Boundary watch — Carlson–Fairbanks–Spivak (forthcoming 2026).** Kevin Carlson (CT
Zulip, Sep 2024): **pullback-preserving comonads on Set** are the correct generalization
of polynomial comonads; their coalgebras form a topos (Johnstone). Topos blog "Set-sets"
(Fairbanks, Nov 2025) signals a paper on **generalized categories = comonads on Set (not
necessarily polynomial)**. If non-polynomial comonads give "generalized directed
containers," the DCont ≅ Cof theory has a *named boundary* — the polynomial condition is
exactly what cuts the general comonad story down to small categories. Watch for this.

Links: [[equivalence-chain]] · [[two-atoms-zappa-szep-decomposition]] ·
[[orgtr-dcont-constant-trees]] · [[distributive-law-landscape]] ·
[[g-obstruction-is-baues-wirsching]]
