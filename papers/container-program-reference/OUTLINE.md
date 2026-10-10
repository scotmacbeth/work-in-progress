# Container Program — Full Reference Document: SKELETON + GAP LIST

**Purpose.** A comprehensive, topic-by-topic reference on the whole container program,
written for Neil Ghani. This is explicitly NOT the 7pp summary he rejected
(`papers/2026-10-06-container-program-summary.tex`) — it is the long-form treatment, each
topic developed in full with definitions, the key theorems (stated, with proof sketches or
pointers to our proof files), and worked examples.

**How to use this skeleton.** Each section below gives (i) a proposed title, (ii) required
subsection bullets, (iii) a STATUS line — EXISTS / PARTIAL / MISSING with source paths,
(iv) the MISSING delta to write fresh. Drive one `/write` session per section (or per gap).
Most of the mathematical content already exists somewhere in `projects/`; the dominant task
is **consolidation and uniform notation**, not fresh proving. The genuinely thin spots are
flagged `>>> BIG GAP`.

All source paths below are absolute-relative to `/home/agent/`.

---

## §0. Front matter / orientation

- Thesis: a container is a family of sets, `Cont ≅ Fam(Set^op)`; composition is a
  degree-two datum; the equivalence-chain hub `DCont ≃ Cat`.
- Reading map and notation table (`⟦−⟧`, `◁`, `⊗`, `×`, `+`, `y`, `I = (1,1)`).
- STATUS: **EXISTS** — reuse orientation prose from
  `projects/papers/2026-10-07-program-overview.tex` (§Orientation) and
  `projects/papers/2026-10-06-container-program-summary.tex` (§Thesis, §The spine).
- MISSING: a notation table unifying the (often clashing) conventions across source files.

---

## §1. The category Cont

**Title:** *Containers, their morphisms, and the extension functor.*

- Container = `(S, P: S → Set)`; extension `⟦S,P⟧(X) = Σ_{s:S} X^{P(s)}`.
- Morphisms with variance: `(f: S→T, f♯: P(f s) ← Q...)` — the contravariant position map;
  `Cont ≅ Fam(Set^op)` as the free coproduct completion of `Set^op`.
- The representation theorem: which endofunctors are containers (preserve wide pullbacks /
  are familially representable); naturality = cartesianness.
- Limits and colimits in `Cont`; the Yoneda/representables backdrop.
- Worked example: `List`, `Maybe`, `tail` as a container morphism.
- STATUS: **EXISTS (scattered)** —
  `projects/papers/which-functors-are-containers.tex` (the test, reading positions back,
  limits/colimits, boundary);
  `projects/papers/category-of-containers.SEED-COPY.tex` ch.1–2 (containers, representation
  theorem, morphism variance, `tail` example);
  `projects/expository/preliminaries-representables-yoneda-day-kan.tex` (representables,
  Yoneda, density).
- MISSING: a single clean merged chapter in uniform notation; the SEED copy is Neil's own
  prose — rewrite in MacBeth's voice rather than lift.

---

## §2. The monoidal structures on Cont / Poly

**Title:** *Four canonical tensors: `+`, `×`, `⊗` (Dirichlet), `◁` (sequential).*

- The four tensors with units: `+/0`, `×/1`, `⊗/y`, `◁/y`; **shapes always multiply, the
  base's monoidal structure shows up only in positions**.
- The classification theorem (Thm A): Day is an equivalence {monoidal structures on `Set`}
  ≃ {convolutional structures on `Cont`} = (D1) coproduct-preserving + (D2) representables
  closed.
- Thm B⁺: the categorical product is the UNIQUE pointwise monoidal structure (no Day
  hypothesis). Thm C: the comparitor `p⊗q → p◁q` is a coreflection counit, so `⊗` is the
  Day-ification of `◁`.
- Cor 5.5 sharpness: a proper class of convolutional structures all sharing the product's
  unit — no cheap invariant singles out `×`.
- The four-structure coherence (pentagon/triangle), and `⟦−⟧` as a (strong/lax) monoidal
  functor for each.
- **The four-monoidal table** (tensor | unit | Day? | pointwise?).
- STATUS: **EXISTS (strong)** —
  `projects/papers/four-monoidal-chapter.tex` (103KB — census, Day family, Thms A/B/C,
  coherence, duoidal, closures; the backbone);
  `projects/papers/four-monoidal-structures.tex` (earlier version);
  `projects/memory/topics/monoidal-structures-on-cont.md` (the compressed map + table);
  `projects/proofs/2026-07-14-day-family-classification.md`,
  `2026-07-19-dirichlet-monoid-classification.md`.
- MISSING: little — mainly trimming `four-monoidal-chapter` to reference length and merging
  the table. This section is near-publishable already.

---

## §3. Day convolution  `>>> NEIL CALLED THIS OUT — but it is NOT a gap`

**Title:** *Day convolution and the coend-free degeneration on containers.*

- Day convolution definition (coend formula) `(F ⊛ G)(c) = ∫^{c1,c2} C(c, c1⊗c2) × Fc1 × Gc2`.
- Day's universal property: `([C,Set], ⊛, y^I)` is the unique monoidal structure making
  `y^{(−)}` strong monoidal; cocontinuous in each variable.
- **The key degeneration:** because `Cont ≅ Fam(Set^op)` is a free coproduct completion and
  Day is cocontinuous, Day on `Cont` needs NO coend — `p ⊙_⋆ q = (S_p×S_q, (s,t)↦ p[s]⋆q[t])`,
  determined on representables `y^a ⊙ y^b = y^{a⋆b}`.
- Day over a general base: the `Fam(C^op)` symmetric tensor IS the Day convolution for the
  pointwise tensor of `C`; Dirichlet multiplication of species as the `Set`-instance.
- Relation to the §2 tensors: `×` = Day of `(Set,+,0)`; `⊗` = Day of `(Set,×,1)`; `+` is NOT
  Day (annihilates `0`); `◁` is not Day but `⊗` is its Day-ification.
- References: Day 1970; Loregian (coend calculus); Niu–Spivak arXiv:2312.00990 Prop 3.79
  (states only EXISTENCE — our Thm A supplies the converse/equivalence).
- STATUS: **EXISTS (strong, but scattered)** — the full treatment Neil wants to be reminded
  of is already written:
  `projects/expository/preliminaries-representables-yoneda-day-kan.tex` §Day convolution
  (def, universal property, degeneration — the primary source, with `\cite{Day1970}`,
  `\cite{Loregian}`);
  `projects/papers/four-monoidal-chapter.tex` §"The Day family and its classification"
  (Thm A);
  `projects/papers/2026-10-07-program-overview.tex` §(b′) (the Day reminder + T2 closedness);
  `projects/memory/topics/monoidal-structures-on-cont.md`;
  `projects/proofs/2026-07-14-day-family-classification.md`,
  `2026-07-15-uniform-closure-day-tensors.md`,
  `2026-08-26-t2-day-closedness-famcop.md`;
  `projects/scratch/day-family-draft.md`, `scratch/day-family/NOVELTY-AUDIT.md`;
  `projects/memory/for-robin/2026-08-27-day-lifts-kan-and-six-confusions.md`.
- **FINDING for Neil:** MacBeth has a complete, citeable Day-convolution treatment. The only
  work is to lift the preliminaries §Day section + Thm A into one self-contained reference
  section and state the degeneration prominently. NOT a priority gap — the priority is
  *surfacing* it so Neil sees it exists.
- MISSING: nothing mathematical; one consolidation pass + the "six confusions" cleanup note.

---

## §4. The closed structures

**Title:** *Internal homs: which tensors are closed, which are not, and why.*

- `(Poly, ×)` is cartesian closed; `Cont` is CCC but NOT locally cartesian closed (poly has
  three closed structures).
- Dirichlet closure: the internal hom for `⊗`.
- Closure of a general convolutional (Day) tensor: left-closed iff `(−)⋆B` is polynomial for
  every `B`, with uniform `Π`-formula internal hom.
- `◁` (sequential): left-closure / non-closure; the `⋉/⋊` Dialectica tensors, one-sided
  closure (`⋊` left-closed), duoidal/LDC.
- Over a general base — T2 (Day-closedness criterion, familial representability) and
  T4 (left-closedness of `◁` on `Fam(C^op)`).
- Negative controls: `Workers × closed` but `◁` not closed; `Vec` not locally subcartesian
  closed (Walker).
- STATUS: **PARTIAL (needs assembly)** —
  `projects/papers/four-monoidal-chapter.tex` §"Closing the structures" (Dirichlet closure,
  general convolutional closure, sequential + cartesian closure — the core);
  `projects/papers/containers-over-a-base.tex` §T2, §T4;
  `projects/papers/ltimes-rtimes-dialectica-section.tex` and
  `projects/papers/dialectica-tensors-deferred.tex` (`⋉/⋊`, Dialectica, duoidal);
  `projects/proofs/2026-07-15-uniform-closure-day-tensors.md`,
  `2026-08-30-fibredness-vs-left-closure.md`,
  `2026-08-26-t2-day-closedness-famcop.md`.
- MISSING: a unifying "closedness ledger" — one table listing each tensor, left/right/both
  closed or not, the internal-hom formula, and the obstruction when not closed. The pieces
  exist but have never been collected into one accounting. **Moderate fresh writing.**

---

## §5. Effects: monads, comonads, and the effect zoo  `>>> BIG GAP (synthesis)`

**Title:** *Effects and coeffects: state, update, reader, store, writer via containers.*

- Monoids in `(Cont, ◁)` = monads on `Set` that are containers; comonoids = directed
  containers = comonads (the `D1–D5` laws).
- **The update monad** (Ahman–Uustalu): cointerpreting directed containers; `(S, P)` with a
  monoid action — THE canonical effect example; update lenses.
- State / store comonad / lens view; **state via the tensor `⊗`, not via composition `◁`**
  (`⊗ ≠ ◁`); the running-balance worked example.
- Reader, writer-with-absorbing-exceptions (the positive affine class), exceptions.
- Effect–coeffect entwining: the two feeds of one monad always entwine (bialgebra face); the
  biKleisli/Freyd arrow face; the branching obstruction; non-branching is the dividing line.
- Predicate liftings `∀/∃` = `Π/Σ`, `E = ◁`.
- STATUS: **PARTIAL — material exists but is NOT unified as "effects"** —
  `projects/papers/effects-coeffects-containers.tex` (entwining, biKleisli, branching
  obstruction, writer/exceptions class — the richest source);
  `projects/papers/workers-state-via-tensor.tex` (state object, store comonad, lens,
  `⊗≠◁`, running balance);
  `projects/papers/state-divergence-distributive-laws.tex`;
  `projects/papers/containers-monads-comonads-change-of-base.tex` §"Position-op transfer",
  §"Predicate liftings";
  SEED PDFs: Ahman–Uustalu *Update Monads* (2014), *Coalgebraic Update Lenses* (2014),
  *Distributive Laws of Directed Containers* (2013) — `git/ghani-containers/pdf/directed-containers/`.
- MISSING: **the update monad has no MacBeth write-up of its own** — it is only name-checked
  (`2026-10-07-program-overview.tex`, SEED book exercises). Needs a fresh subsection
  porting Ahman–Uustalu's update monad / update lens into our notation, then threading
  reader/state/writer/store into ONE "effect zoo" table keyed by container data. This is the
  biggest synthesis gap: the parts are strong but no single section presents "the standard
  effects, each as a container." **Substantial fresh writing.**

---

## §6. The free monad and the cofree comonad in Poly

**Title:** *Free monad and cofree comonad of a container: trees, grafting, paths.*

- Free monad `C* = (S*, P*)`: well-founded `C`-trees with variable leaves; `⟦C*⟧A = μX.(A+⟦C⟧X)`;
  unit = variable leaf, multiplication = grafting; monad laws = monoid laws of grafting.
- Cofree comonad `C^∞ = (S^∞, P^∞)`: M-type of possibly-infinite trees, positions = finite
  node-paths; `⟦C^∞⟧A = νX.(A×⟦C⟧X)`; counit = root, comultiplication = subtree-relabelling +
  path concatenation; `C^∞` is a directed container.
- The linear instance: free `◁`-monoid on a one-shape linear container = tensor algebra
  `T(A)`, `⟦C*⟧W = ⊕ A^{⊗n}⊗W` = O'Neill's free monad; the Adámek chain of partial sums (the
  residual/skip-connection as the pointing that repairs convergence).
- Signatures as containers; algebraic effects / effect trees; handler semantics (Grodin,
  Topos 2024 — browse-pending, not yet cited).
- STATUS: **EXISTS (strong)** —
  `projects/papers/category-of-containers.SEED-COPY.tex` §"The free monad and cofree
  comonad of a container" (full explicit shape/position data, laws via grafting/concat,
  `C^∞` directed — the primary source);
  `projects/papers/containers-monads-comonads-change-of-base.tex` §"The free monad on a
  container" (linear/tensor-algebra instance, Adámek chain);
  `projects/papers/rooted-tree-normal-form.tex` (the one-move normal form across 4 settings);
  SEED `git/ghani-containers/books/book.tex` cofree-comonad exercises;
  SEED Lynch–Shapiro–Spivak and Libkind–Spivak *Pattern Runs on Matter* (free monads/cofree
  comonads in Poly) — `pdf/spivak-poly/`, `pdf/spivak-orchestration/`.
- MISSING: little mathematically. SEED copy is Neil's prose — rewrite in MacBeth's voice,
  fold in the linear/tensor-algebra instance, and add the small worked cases (`Maybe`,
  binary). **Light fresh writing.**

---

## §7. Change of base

**Title:** *Containers over a general base: `Fam(C^op)`, M-containers, the fibrational view.*

- The ambiguity resolved: `Cont_C = Fam(C^op)` (external families) is the canonical reading;
  the quantitative face over `Vec`.
- Approach 1 external families: the hom formula; **T1 fullness = unit-connectedness** (`⟦−⟧`
  f&f iff monoidal unit `I` is connected, i.e. `C(I,−)` preserves coproducts — Neil's
  flagship, NOT extensivity); T2 Dirichlet closedness; T4 `◁` left-closedness.
- Approach 2: indexed / dependent-polynomial functors.
- Approach 3: the fibrational referee — `Fam` preserves fibrations; quantifiers = `All/Exists`
  liftings; containers = fibrewise-opposite hyperdoctrine (logic of containers = `Cont(cod)`
  bifibration).
- Approach 4: the subcartesian weakening.
- M-containers: `M`-containers as `Fam(Kl(M)^op)`, codensity, faithful always / full iff `M`
  codense ∧ connected; the three enriched extensions and the collapse of fullness.
- Containers over `Vec`: biproduct collapse, the extensivity crux, linear directed containers
  = algebroids = `Mat(Vec)`-comonoids; Schur-functor analytic lifting.
- STATUS: **EXISTS (very strong, the most-developed topic)** —
  `projects/papers/containers-over-a-base.tex` (76KB — the four approaches, T1/T2/T4, logic
  of containers — the backbone);
  `projects/papers/containers-monads-comonads-change-of-base.tex` (M-containers, codensity,
  three extensions, fullness collapse);
  `projects/papers/mcontainers-codensity-polynomiality.tex`;
  `projects/papers/vcont-treatment-2026-09-05.tex`,
  `projects/expository/containers-over-vec.tex`,
  `projects/expository/vcont-plain-note.tex`;
  `projects/papers/vec-admissibility-not-zfc.tex` (the admissibility / ZFC-independence edge);
  proofs: `2026-08-25-fullness-unit-connectedness.md`, `2026-08-30-fibredness-vs-left-closure.md`.
- MISSING: trimming to reference length and reconciling the `Vec` corrections (per MEMORY:
  VCont "faithful" was wrong over `Vec`; use the corrected statement). Mostly editorial.

---

## §8. The equivalence chain (connective spine)

**Title:** *`Cont ≃ DCont ≃ Poly-comonoid ≃ Cat` — the convergence hub.*

- `DCont ≅ Cat` (directed containers = small categories); `Cat# = DCont ≅ Cof` in `Poly`.
- Comonoids in `(Cont, ◁)` = directed containers = `Set`-comonads satisfying `D1–D5`.
- The chain M1–M6 with honest status (M5 = Clarke–Di Meglio, M5/M6 OPEN/conjectural per
  MEMORY and `projects/proofs/registry/equivalence-chain.json`).
- Composition as a degree-two datum; the degree ladder (0/1/2) and composition-blindness
  (a PROGRAM, not a theorem).
- STATUS: **EXISTS** —
  `projects/papers/convergence-hub.tex` (the hub paper);
  `projects/papers/composition-is-a-degree-two-datum.tex`;
  `projects/papers/2026-10-07-program-overview.tex` §(a), §(e);
  `projects/proofs/registry/equivalence-chain.json` (status of each link).
- MISSING: honest restatement of which links are proved vs conjectural (M5/M6).

---

## §9. (Optional appendices)

- Zappa–Szép / orchestration and the `H²` obstruction (`(G)⟺[ω]=0`); skew-brace arc —
  EXISTS: `papers/pairwise-zappa-szep`, `onu-solvability-obstruction.tex`, SEED ch.5.
- Tangent / Cartan-calculus arc — EXISTS: `container-derivative-tangent-structure.tex`,
  `container-derivative-uniqueness.tex`, `container-cartan-boundary.tex`.
- Applications (supply chain, blockchain, GA, tax, orchestration) — EXISTS in SEED + papers.
- Lean formalisation inventory — `projects/lean/`, SEED `lean/Containers/`.
- These are beyond Neil's seven named topics; include only if the reference is meant to be
  the whole program.

---

## PRIORITY GAP SUMMARY (for the first write sessions)

**Biggest fresh-writing gaps (do these first):**

1. **§5 Effects — the effect zoo (BIGGEST).** Strong pieces (entwining, state-via-tensor,
   branching obstruction) but NO unified "each standard effect as a container" section, and
   **the update monad has no MacBeth write-up at all** — only name-checks. Needs a fresh
   port of Ahman–Uustalu update monads/lenses + a one-table synthesis (state/update/reader/
   store/writer/exceptions keyed by container data).

2. **§4 Closed structures — the closedness ledger.** All results exist but are scattered
   across `four-monoidal-chapter`, `containers-over-a-base` (T2/T4), and the Dialectica
   notes. Needs one consolidated accounting table (per tensor: left/right/both closed,
   internal-hom formula, obstruction).

3. **§1 Cont foundations — de-duplication.** The content is complete but split across
   `which-functors-are-containers`, the SEED category-of-containers copy (Neil's prose), and
   the preliminaries file. Needs a single clean chapter in MacBeth's voice and uniform
   notation (the SEED copy should be rewritten, not lifted).

**Day convolution (§3): NOT a gap.** Contrary to the risk Neil flagged, MacBeth already has
a full, citeable treatment — definition, Day's universal property, and the coend-free
degeneration on `Cont` — in
`projects/expository/preliminaries-representables-yoneda-day-kan.tex` §Day convolution, plus
Thm A in `four-monoidal-chapter.tex`. The task is surfacing/consolidating, not writing. One
clean self-contained section lifted from the preliminaries + Thm A will satisfy the reminder.

**Everything else (§2, §6, §7, §8): EXISTS strong** — reference-quality material already
written; work is trimming, uniform notation, and honest status flags (M5/M6 open; `Vec`
faithfulness correction).
