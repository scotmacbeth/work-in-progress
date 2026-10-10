# The Container Program — Master Reference Document

## Detailed outline + section skeleton

**Date:** 2026-10-09
**Author:** MacBeth (for Neil Ghani)
**Purpose.** The comprehensive, detailed document Neil has repeatedly asked for: "a document
describing all our work in detail." This is the long-form, registry-grounded treatment of the
entire container program — theory, composition, differential structure, applications, and
formalisation — organised into six Parts. Every result below carries its **trust grade in
brackets**, taken verbatim from `/home/agent/projects/proofs/registry/*.json`. Grades are never
inflated: `[peer-reviewed]` > `[proved]` > `[lean-verified]` (machine-checked, scoped) /
`[computed]` (finite/example evidence, not a general proof) > `[peer-claimed]` /
`[in-progress]` / `[speculative]`.

**Companion skeleton.** `OUTLINE.md` (in this directory) is the *topic-by-topic* skeleton keyed to
existing LaTeX source files (where each section already exists on disk, what is MISSING). THIS
document is the *results-by-Part* master, keyed to the trust registry. Use them together:
`OUTLINE.md` tells you which `.tex` to lift prose from; this file tells you which theorems belong
where and at what grade you may state them.

**Registry scope.** 53 registry files inventoried (full table in Appendix A). Grade breakdown:
**3 peer-reviewed, 38 proved, 4 lean-verified, 5 computed, 2 in-progress, 1 peer-claimed, 0
explicitly speculative.** (The `[computed]` tier is the honest "evidence but no general proof"
tier; two `[in-progress]` roots — the equivalence chain M5/M6 and the infinite-arity closed-tensor
classification — are the program's two standing open fronts.)

---

# Part I — The equivalence chain (theory)

**Thesis of Part I.** A container is a family of sets, `Cont ≅ Fam(Set^op)`; the four canonical
tensors `(+, ×, ⊗, ◁)` all have the form "shapes multiply, the base's structure appears only in
positions"; and the sequential tensor `◁` is the one whose comonoids are small categories. This is
the convergence hub `Cont ⊇ DCont ≃ Poly-comonoid ≃ Cat`, developed with honest status on which
links are theorems and which are conjectural.

## I.1 The category Cont and the representation theorem
*Precis.* Containers `(S, P:S→Set)`, extension `⟦S,P⟧(X)=Σ_{s}X^{P(s)}`, contravariant position
maps, `Cont ≅ Fam(Set^op)` as the free coproduct completion of `Set^op`. Which endofunctors are
containers (familial representability / wide-pullback preservation). Limits/colimits; the
Yoneda/representable backdrop. This is the foundation on which everything else rests.
- (no standalone registry node — foundational; source `which-functors-are-containers.tex`,
  `category-of-containers.SEED-COPY.tex`). **Flag as a write gap: no registry node certifies the
  representation theorem itself.**

## I.2 The four monoidal structures on Cont / Poly
*Precis.* The tensors `+/0`, `×/1`, `⊗(Dirichlet)/y`, `◁(sequential)/y`, their units, and the Day
classification. The interchange/distributivity lattice among them. `⊗` is the Day-ification of `◁`
via the comparitor coreflection.
- Hedges 4×4 interchange table, all 16 cells, `×/⊗` corrected to non-distributing **[proved]**
  (`hedges-interchange-table`, `2026-07-16-hedges-distributive-table.md`; several cells also
  **[lean-verified]**: `SeqProdDistrib`, `SeqCoprodDistrib`, `TensorCoprodDistrib`,
  `TimesCoprodDistrib`).
- Bare `⊗`-monoids = shape monoid + oplax functor on fibres **[proved]**
  (`dirichlet-monoid-classification`).
- Bare `⊗`-comonoids (no `◁`) = families of monoids **[proved]** (`bare-dirichlet-comonoid`).
- Double comonoids in normal duoidal `(Poly, ◁, ⊗)` = sets of commutative monoids
  (Eckmann–Hilton collapse) **[proved]** (`comparitor-comonoid-nogo`).
- The two non-convolutional tensors `⋉/⋊` are the Dialectica tensors; `⋊` left-closed
  **[computed]** (`other-cont-monoidal-tensors`).

## I.3 Closed structures and Day convolution
*Precis.* Which tensors are closed, the internal-hom formulas, and the obstructions. `(Poly,×)` is
cartesian closed, `Cont` is CCC but not locally cartesian closed. Day convolution and its
coend-free degeneration on `Cont`.
- A Day/convolutional tensor `(Cont, ⊙_⋆)` is left-closed iff `(−)⋆B` is polynomial for every `B`;
  uniform `Π`-formula internal hom **[proved]** (`closed-day-structures`).
- Classification of left-closed convolutional tensors on `Set`: bounded arity ⟹ `×` or `∨_S`;
  **infinite-arity boundary OPEN** **[in-progress]** (`closed-tensor-classification`).
- Dirichlet internal hom, `(Cont,⊗,y)` closed **[lean-verified]** (`DirichletClosed.lean`,
  `DirichletHomPi.lean`; math = Niu–Spivak prior art, proof object ours).

## I.4 Change of base — containers over a general category
*Precis.* `Cont_C = Fam(C^op)`; the fullness criterion; closedness criteria T2/T4; the fibrational
reading; M-containers; containers over Vec.
- **T1 (flagship):** `⟦−⟧:Fam(C^op)→[C,C]` is full-and-faithful iff the monoidal unit `I` is
  **connected** (`C(I,−)` preserves coproducts) — NOT extensivity **[proved]**
  (`fullness-unit-connectedness`).
- **T2:** Dirichlet/Day closedness over a general base = familial representability **[proved]**
  (`t2-day-closedness-famcop`).
- **T4-left:** `◁` left-closedness on `Fam(C^op)` **[proved]** (`t4-left-closedness-lhd-famcop`).
- **M-containers:** M-Cont = `Fam(Kl(M)^op)`; extension faithful always, full iff M codense ∧
  connected; the three enriched extensions collapse to `{Id}` **[peer-reviewed]**
  (`change-of-base`; Rick-refereed).
- M-container trilogy THM1/THM2/THM3 (composition ⟺ polynomiality), necessity trichotomy
  **[proved]** (`m-containers`).
- Logic of containers: `Cont(cod)` is the bifibration `Fam(Set^op)`; shape-level Fam-Kan
  quantifiers **[proved]** (`cont-cod-predicate-fibration`, `joint-bc-cont-cod`).
- Containers over Vec: `LinCont = Fam(Vec^op)`, biproduct collapse, extension faithful-but-NOT-full
  over Vec **[proved]** (`linear-containers-vec`). **Correction flag (MEMORY):** the earlier VCont
  "faithful" claim over Vec was wrong — use the corrected statement.
- `(−)◁q` left-adjoint behaviour over `Fam(Vec^op)`; summability does not gate it as predicted
  **[proved]** (`left-adjoint-over-vec`); `L_q=(−)◁q` is a parametric right adjoint
  **[proved]** (`pra-vs-probe-method`); copowers/writer-monad gap (Q) reformulation **[proved,
  ZFC]** (`copowers-gap-writer-monad`).
- `fibredness-vs-left-closure` (BHM `▷` left-variable fibredness) **[proved]**.

## I.5 Free monad and cofree comonad in Poly
*Precis.* The free monad `C*` (well-founded trees, grafting) and cofree comonad `C^∞` (M-type,
node-paths) of a container; the linear/tensor-algebra instance.
- Free monad = `◁`-monoid `(S*◁P*, graft, lf)`; the three monoid laws **[lean-verified]**,
  Quot.sound-only (`free-monad-grafting`, `Free.lean`).
- Cofree comonad `C^∞` = `◁`-comonoid on the M-type of p-trees; counit = root, comult =
  subtree-relabel + path-concat **[proved]** (`cofree-comonad`).
- O'Neill's free monad on linear self-attention = free `◁`-monoid on a one-shape linear container =
  tensor algebra `T(A)`; Adámek chain / residual-as-pointing **[proved]**
  (`oneill-free-monad-linear-container`).

## I.6 The equivalence chain and its honest status
*Precis.* `Cont ⊇ DCont ≃ Poly-comonoid ≃ Cat`; the directed-container laws D1–D5; the Lean
milestone ladder M1–M6; what is proved vs conjectural.
- Equivalence chain M1–M6 **[in-progress]** (`equivalence-chain`): **M1–M4 are done and
  partly Lean-verified** (container library, comonad/directed-container equivalence, ZS
  characterisation, DCont ≃ Cat — see Part V); **M5 (bridge to Poly, four monoidal structures) =
  Clarke–Di Meglio, and M6 (double category Org, dynamic categories) are OPEN / conjectural.** Do
  not state M5/M6 as proved.
- `Cat# = DCont ≅ Cof` in Poly; DCont ≃ Cat as the convergence hub (source `convergence-hub.tex`,
  connection `dcont-cat-is-the-convergence-hub`).

---

# Part II — Composition: welds, distributive laws, the obstruction cluster

**Thesis of Part II.** Composing two directed containers (= small categories = systems) that share
an interface is a **Zappa–Szép product** `C ⋈ D`, equivalently a distributive law. When it exists
is governed by two checkable conditions; when the second fails the obstruction is a cohomology
class. The invariants are graded by **simplicial nerve level**, not cohomological degree.

## II.1 Orchestration = Zappa–Szép weld
*Precis.* Agent orchestration / supervisor–worker composition is a directed container; composing
two is a ZS product; re-entrancy is an unprotected shared position.
- Orchestration is a directed container; composition = ZS product `C ⋈ D`; re-entrancy as failed
  guard **[proved]** (`orchestration-zs`).
- Pairwise ZS criterion: a matched pair extends to a global ZS product iff **(L) freeness** AND
  **(G) global closure** **[proved]** (`pairwise-zs`).
- ZS associativity ZS1–ZS4 ⟺ assoc **[lean-verified]** (`ZappaSzep.lean`, Part V).

## II.2 The H² weld obstruction — WITH the 2026-10-09 correction
*Precis.* Condition (G) is governed by a class `[ω] ∈ H²`. **CRITICAL CORRECTION (2026-10-09, Rick
UID 211):** the cocycle *condition* IS associativity; the *class* `[ω]` measures the **SPLITTING**
of an already-associative weld, NOT non-associativity. The honest non-associativity separator is a
pointwise `N₃` magma condition (a condition, not a class).
- `(G) ⟺ [ω]=0` with `[ω] ∈ H²(Sk_C; 𝒟)` (connection `g-obstruction-is-baues-wirsching`,
  `h2-homes-for-zs-obstruction`). The class is the splitting obstruction of an associative weld.
- Groupoid case: connected groupoid = `K(Γ,1)`, ZS defect = Schreier factor set, merge ⟺ `[ω]=0`;
  `cd≤1 ⟹ [ω]=0` (free groupoids always merge) **[computed]** (`groupoid-zs-obstruction`).
- The two `[ω]` sites (handoff `[ω_h]` and stabiliser `[ω_st]`, both `≅ 𝔽₂`) are irreducibly
  distinct **[proved]** (`two-omega-sites`).
- **DEMOTED 2026-10-09:** the weld-`ω`-as-non-associativity gloss (and the re-entrancy-stub
  reading) went **proved → computed**; state `[ω]` only as a splitting obstruction.

## II.3 Holonomy and the Zappa–Szép bridge
*Precis.* Composing update monads sharing a state set is a ZS product that welds state/isotropy
holonomy; the emergent-holonomy meeting invariant is cohomological.
- Composing two update monads sharing `S` = ZS product on the position-threading monoid, welding
  holonomy; aligned-abelian `[ω] ∈ H²(B;A)` obstructs splitting **[peer-reviewed]**
  (`holonomy-composition-zs-bridge`; Rick-refereed).
- Holonomy-triviality collapse engine (liftings ≅ Cat completeness) **[proved]**
  (`holonomy-triviality`).
- Emergent-holonomy meeting count is `Ext^n_{kG}(k[G/A],k[G/B]) ≅ ⊕ H^n` — the Ext tower
  **[proved]** (`emergent-holonomy-is-ext-tower`).

## II.4 The nerve-level grading of compositional invariants
*Precis.* Grade an invariant of a small category by the **simplicial nerve level** it reads, not by
cohomological degree. Regrade lemma: cohomological degree `n` = nerve level `− 1`, so composition
(composable pairs `N₂`) is **degree ONE**, not two. This retires the shipped "composition is a
degree-two datum" slogan.
- Nerve-level tower **[proved]** (`composition-nerve-level`): (rung 1) `N₁` reflexive-graph /
  U-blind invariants (out-degree, `H⁰`); STRICTLY below (rung 2) `N₂` composition invariants (`H¹`,
  δ-translations, inventory `[θ_R]`); (rung 3) `N₃` associativity. **Thm 3:** a category is
  2-coskeletal so the truncation tower collapses at level 2 (no third truncation rung). **Thm 4:**
  the genuine strict `N₂ ⊊ N₃` lives in the ASSEMBLY/weld problem, where associativity is an `N₃`
  predicate not implied by `N₂` data.
- **Precision flag (Rick N1, 2026-10-09):** the shape invariant `U(p)` is strictly coarser than
  `tr₁ N` (both `[1]` and `B(ℤ/2)+pt` give `U = y²+y`) — do NOT call `U` "the nerve-level-1
  invariant." **Terminology flag (N3):** "nerve level" must be disambiguated (truncation level vs
  cocycle-condition level) throughout.

## II.5 Skew-brace / solvability obstruction arc
*Precis.* The deeper algebraic home of the ZS obstruction: skew braces, the residue-dependent
solvability obstruction `o_ν`, and Ferri prunability.
- `o_ν : H²₊ → C³/A(Z²_∘)` is a group homomorphism with `im φ⁺ = ker o_ν`; nontrivial ⟹ torsor
  **[proved]** (`solvability-obstruction-o-nu`). (Several finite slices **[lean-verified]** — Part
  V.)
- Ferri "completely prunable" quiver skew brace = vanishing of the ZS global obstruction; prunability
  = degree-1 descent/subfunctor, NOT Schreier; complete-prunability no-go **[computed]**
  (`quiver-skew-brace-zs`).

## II.6 Effects / coeffects and the composition of (co)monads
*Precis.* One Set-monad M gives two container feeds (effect monad `T_M`, coeffect comonad `G_M`);
they always entwine, the arrow face needs non-branching, and state lives on `⊗` not `◁`.
- Monad on Set transfers to comonad `G(S,P)=(S,M∘P)` **[proved]** (`monad-comonad-transfer`;
  **[lean-verified]** `MonadComonadTransfer.lean` / `DualTransfer.lean`).
- Effect/coeffect entwining: bialgebra face for all M; arrow/biKleisli face iff non-branching; the
  branching obstruction = Atkey's index **[proved]** (`monad-comonad-entwining`,
  `effect-coeffect-arrows`).
- State object `ΔS` = codiscrete category, store/costate comonad; **state via `⊗`, not `◁`**
  **[proved]** (`state-object-delta`).
- Workers `(Set,×)`-graded category; type hierarchy and the retract into the BHM `▷`-grading
  **[proved]** (`workers-type-hierarchy`, `workers-retract-of-bhm-grading`;
  **[lean-verified]** `WorkersRetract.lean`).

## II.7 Game comonads (adjacent)
*Precis.* The finite-model-theory game comonads factor through Poly, connecting the composition
story to logic/complexity.
- Ehrenfeucht–Fraïssé `E_k`, pebbling `P_k`, modal `M_k` comonads factor through Poly / are
  polynomial comonoids **[computed]** (`game-comonad-poly`).

---

# Part III — Differential structure

**Thesis of Part III.** The AAGM one-hole container derivative `∂` is not an ad-hoc operation: it
is the differential combinator of a Cartesian differential category, equivalently a tangent
structure realised by dual-number substitution `T(p) = p(y+εv) mod ε²`. The uniqueness is
peer-reviewed; the Cartan/negation boundary is the honest limit.

## III.1 The container derivative is a tangent structure
*Precis.* `SPoly` (finite-support polynomial functors, substitution) is a Cartesian differential
category with combinator `D = ∂`; hence a Cartesian tangent category.
- `∂` = differential combinator of a CDC of polynomial functors **[proved]**
  (`tangent-container-derivative`).
- `T(p)=p(y+εv) mod ε²` is a strict `◁`-monoidal base-change `DCont(k)→DCont(D)`, `D=k[ε]/ε²`,
  laxator = chain rule on the nose **[proved]** (`tangent-restricts-to-dcont`).

## III.2 Uniqueness of the container tangent structure
*Precis.* On finite-support polynomial functors, `∂` is the unique nontrivial representable tangent
structure. This is the strongest-graded differential result.
- Uniqueness (corrected statement per Rick referee 2026-10-05) **[peer-reviewed]**
  (`tangent-uniqueness-spoly`). State the corrected form, not the earlier unconditional slogan.

## III.3 The Cartan / negation boundary
*Precis.* The full Cartan calculus requires fiberwise negation, which `SPoly` lacks; ring-completion
`ℕ→ℤ` switches it on. This is the precise edge of the differential story.
- `SPoly/∂` has no fiberwise negation ⟹ no scalar ring object ⟹ Cartan calculus fails over `ℕ`
  **[proved]** (`cartan-scalar-object-spoly`).
- Fiberwise group completion `ℕ→ℤ` switches the full Cartan calculus ON (`SPoly_ℤ`) **[proved]**
  (`virtual-container-cartan`) — the far side of the "negation knife."
- Lie-parallelizability port: a poly comonoid is tangent-parallelizable ⟺ an out-degree condition;
  the Lanfranchi port is ill-posed / composition-blind **[proved]**
  (`lie-parallelizable-poly-comonoid`).

---

# Part IV — Applications

**Thesis of Part IV.** The same `DCont ≃ Cat` + ZS-weld machinery models real compositional systems
where correctness has economic consequences. Each application is a directed container; composition
is a ZS product; failure modes are obstruction classes.

## IV.1 Supply chains — inventory at H¹ and the gerbe at H²
*Precis.* A supply chain is a small category / directed container; composing flows sharing a
warehouse is a ZS product. Inventory consistency is a **degree-one** `H¹` datum, INDEPENDENT of the
weld class `[ω] ∈ H²`. A finer relabelling-group obstruction lives at `H²` as a gerbe.
- Supply chain as directed container; composing two flows = ZS product `C ⋈ D`; `[ω] ∈ H²`
  obstruction **[computed]** (`supply-chain-zs`).
- **Tier-2 inventory gerbe:** when local inventory charts agree only up to an iso of stock-states
  (relabelling group `K = Aut(F)`), the gluing obstruction is a gerbe class `[𝔤] ∈ H²(N(C); Z(Aut
  F))`; rectifiable ⟺ `[𝔤]=0`, independent of the weld, nonvacuous ⟺ `Z(Aut F)≠1` **[proved]**
  (`supply-chain-inventory-gerbe-h2`).
- **Inventory `[θ_R] ∈ H¹`, INDEPENDENT of the weld `[ω] ∈ H²`** — the degree-one consistency datum
  (proof file `supply-chain-inventory-degree-one.tex`; appears as the `N₂`/`H¹` rung of the nerve
  tower, `composition-nerve-level`). **Write gap:** this `H¹` result has no standalone registry
  node of its own — it is carried inside `composition-nerve-level`. Flag before citing it as an
  independent `[proved]` node.

## IV.2 Blockchain / smart-contract re-entrancy
*Precis.* Smart contracts as coalgebras; a re-entrancy bug is a failed distributive law / an
unprotected shared position in a ZS weld. The obstruction is machine-checkable.
- Re-entrancy = failed guard in the orchestration ZS weld **[proved]** (`orchestration-zs`); the
  `H²` class `[ω]=ε` is **[lean-verified]** (`reentrancy-machine-checked-obstruction.tex` /
  `fibre-h2-z2-engine`). **Correction flag:** per II.2, state `[ω]` as a splitting obstruction of an
  associative weld, not as "non-associativity."
- Security-audit framing: state-divergence bugs are failed distributive laws (connection
  `security-audit-bugs-are-failed-distributive-laws`; paper
  `state-divergence-distributive-laws.tex`).

## IV.3 GA composition / linear attention (adjacent)
*Precis.* Island-model GA migration topology and linear-attention composition are instances of the
same compositional algebra in `Mat(Vec)` / Poly.
- Linear attention as composition in the Vec-matrix bicategory `Mat(Vec)`, `(P⊕Q)(a,c)=⊕_b
  P(a,b)⊗Q(b,c)` **[proved]** (`vec-attention-composition`); "stack = one matrix" REFUTED (MEMORY).
- GA diversity-dynamics empirical result (Langer–Vega, GECCO 2026) and ga-containers (ACT 2026) —
  external/empirical, cite as published collaborator work, not a MacBeth registry node.

## IV.4 Agent orchestration and tax computation
*Precis.* Tool-calling protocols and meta-agent orchestration are directed containers; tax
computation (Catala-style) is a scope/supersession DAG with a comonadic event-sourced interface.
- Tool-calling protocols are directed containers (shipped note
  `tool-calling-protocols-directed-containers.tex`; grounded in `orchestration-zs` **[proved]**).
- Harness-is-a-worker / MCP formalisation (paper `harness-is-a-worker.tex`; connection
  `harness-worker-is-the-unscooped-mcp-formalization`).
- **Tax computation: write gap.** Named in SEED Path 5 but has NO registry node and no MacBeth
  write-up. Either produce the ontology-DAG / supersession-DAG / event-sourced-comonad model or mark
  it explicitly as future work in the master document.

---

# Part V — Formalisation in Lean 4

**Thesis of Part V.** The theorems are not hand-waving: the core equivalence-chain links and the
cohomological obstruction engines are machine-checked in Lean 4. Each oracle certifies a precise,
honestly-scoped statement; most are Mathlib-free (Lean 4 core) and axiom-minimal
(`propext`/`Quot.sound` only, several axiom-free via `decide`).

## V.1 The equivalence-chain milestones (M1–M4)
*Precis.* The container library and the directed-container ↔ comonad ↔ small-category equivalence,
plus the ZS associativity characterisation.
- `Basic`, `Directed`, `ComonadConverse`, `Cofunctor`, `DContCat`, `ZappaSzep` — M1/M2/M2b/M4 +
  ZS assoc (ZS1–ZS4 ⟺ assoc) **[lean-verified]**.
- `Comonoid.lean` / `ComonoidConverse.lean` — M3: directed container ⟺ `◁`-comonoid (both
  directions) **[lean-verified]**.
- `Cont.lean`, `Sequential.lean`, `Monoidal.lean`, `Dirichlet.lean`, `FourMonoidal.lean` — Cont as a
  category, the `◁` operator, all four monoidal structures + comparison isos **[lean-verified]**.

## V.2 The free monad
- Free monad on a container = `◁`-monoid; three monoid laws (assoc = `graft_assoc`),
  Quot.sound-only **[lean-verified]** (`free-monad-grafting`, `Free.lean`); partial universal
  property in `FreeUniversal.lean`. (Cofree comonad NOT core-formalisable — needs coinductive
  `PFunctor.M`.)

## V.3 The cohomological obstruction engines (H²)
*Precis.* Three standalone, Mathlib-free Lean files compute the group cohomology that homes the ZS
and inventory obstructions. Honest scope: each certifies a FINITE/explicit computation; the general
cohomology theory is cited as a black box (Brown VI.9).
- `H²(C_n; ℤ) ≅ ℤ/n` via the norm map **[lean-verified]** (`cyclic-h2-norm-engine`).
- `H²(ℤ/2; ℤ/2) ≅ ℤ/2`, fibre edge, with nonsplit-ℤ/4 vs split-Klein witnesses **[lean-verified]**
  (`fibre-h2-z2-engine`).
- **Unified:** `H²(C_n; ℤ/m) ≅ ℤ/gcd(n,m)`, subsuming both above, with a from-scratch Bézout
  **[lean-verified]** (`cyclic-h2-gcd-engine`).

## V.4 The gerbe / reduced-nerve engine and o_ν slices
*Precis.* Machine-checked witnesses for the supply-chain gerbe and the skew-brace solvability
obstruction.
- Reduced-nerve `𝔽₂` engine: `H²(B(ℤ/2))=1`, diamond `(1,1,0)`, `D₄` non-split — the three gerbe
  witnesses **[lean-verified]** (gerbe `H²`, MEMORY `lean-gerbe-h2-witnesses`; grounds
  `supply-chain-inventory-gerbe-h2`).
- Nerve-level separation oracle: `N₁⊊N₂` machine-checked, bar complex `𝔽₂`, Betti `(1,1,1)` vs
  `(1,0,0)` **[lean-verified]** (grounds `composition-nerve-level`).
- `o_ν` finite slices: `|G|=8` additive slice, `|G|=16` three-way lock + torsor dichotomy, the
  corrected `D=ℤ/8` torsor criterion — all `decide`-based, axiom-free or `propext`-only
  **[lean-verified]** (nodes under `solvability-obstruction-o-nu` / `quiver-skew-brace-zs`).
- Prunability degree-1 descent cochain: prunability ⟺ `δ≡0` on the `|L|=2` linearisation
  **[lean-verified]** (node under `quiver-skew-brace-zs`).

## V.5 Transfer and distributivity cells
- Monad→comonad transfer and dual, three laws each **[lean-verified]** (`MonadComonadTransfer.lean`,
  `DualTransfer.lean`).
- Dirichlet closed / `Π`-form internal hom, axiom-free **[lean-verified]**.
- Four Hedges distributivity cells (`◁/×`, `◁/+`, `⊗/+`, `×/+`) **[lean-verified]**.
- Workers retract `ΔS⊗ΔT` of `ΔS◁ΔT` **[lean-verified]**.

---

# Part VI — Open questions & frontier

**Thesis of Part VI.** The honest edge of the program: what is conjectural, what is refuted, and
what the next moves are. Distinguish standing open conjectures from results we have actively refuted
(a refutation is a `[proved]` negative, not an open question).

## VI.1 The two standing open registry fronts
- **Equivalence chain M5/M6** **[in-progress]** (`equivalence-chain`): M5 (bridge to Poly / four
  monoidal structures, = Clarke–Di Meglio) and M6 (double category Org, dynamic categories) are
  OPEN. The internal replacement theorem ("internal directed container ≃ internal category ≃ comonad
  in C" for general symmetric monoidal C) is conjectural (SEED open Q1).
- **Infinite-arity closed-tensor classification** **[in-progress]** (`closed-tensor-classification`):
  bounded arity is settled (`×` or `∨_S`); the infinite-arity boundary is an honest open problem.

## VI.2 SEED open questions (Path-level)
- Distributive-law decision procedure: for which pairs of directed containers does a distributive
  law exist? ZS (L)+(G) give checkable criteria; the general theory is incomplete (SEED Q2;
  `pairwise-zs` is the current best).
- q-calibration: what is `q` (braided structure) for real concurrent systems? Empirical, OPEN
  (SEED Q3).
- Density comonads = polynomial comonads (Spivak 2025 conjecture) — ORTHOGONAL to the seed per
  connection `density-comonads-orthogonal-seed-q5`; OPEN (SEED Q5).
- Coinductive polynomial trees (Spivak 2026) vs adaptive GA topologies — OPEN (SEED Q6).

## VI.3 Refuted / corrected (negative results — state as such, not as open)
- Crown Stage 2: branch-shape `Ψ` FAILS (over-counts by `2^{Σ(λ−1)}`); one-shape `Ψ'` positive over
  `𝒯`; `k≥2` separate — sharing = descent, not coproduct of branches **[proved]** (connection
  `crown-stage2-unfolding-vs-descent`; shipped note). State the refutation, not the original crown.
- Lanfranchi parallelizability port ILL-POSED (`lie-parallelizable-poly-comonoid`, III.3).
- Crown TFAE FALSE → strict 4-level chain (MEMORY `crown-tfae-strict-chain`).
- **The `[ω]`-as-non-associativity demotion (2026-10-09)** — carried in II.2; the corrected reading
  is splitting, not non-associativity.

## VI.4 Independence-flavoured / speculative frontier
- Conjecture 6.2 / Gap-S (is `F=Hom(E,⊕_ℕ−)` projective?): reformulated `Ext¹→Hom`, one
  non-liftable `φ` suffices in ZFC; Gap-S FALSE under CH; current bet `ℰ=0` in ZFC via
  automorphism-rigidity analogy — OPEN crux (`vec-admissibility-not-zfc.tex`, MEMORY
  `gapS-false-under-CH`).
- Clio's peer-claimed results (transfer operators ↔ container derivatives) **[peer-claimed]**
  (`clio-peer-claims`) — register at peer-claimed, do not promote without independent check.

---

# Appendix A — Full registry inventory (53 nodes)

Grade legend: PR = peer-reviewed, P = proved, LV = lean-verified, C = computed, IP = in-progress,
PC = peer-claimed.

| # | registry file | grade | one-line gist | root proof file |
|---|---|---|---|---|
| 1 | change-of-base | **PR** | M-container extension f&f classification; 3 enriched exts collapse to {Id} | 2026-09-15-enriched-ff-classification.md |
| 2 | holonomy-composition-zs-bridge | **PR** | update monads sharing S compose as ZS, welding holonomy; [ω]∈H²(B;A) | 2026-08-12-holonomy-composition-zs-bridge.md |
| 3 | tangent-uniqueness-spoly | **PR** | ∂ is the unique nontrivial representable tangent on SPoly (corrected stmt) | 2026-10-04-solid-correspondence-converse.md |
| 4 | free-monad-grafting | **LV** | free monad = ◁-monoid; 3 monoid laws machine-checked | 2026-07-16-free-monad-grafting-laws.md |
| 5 | cyclic-h2-norm-engine | **LV** | H²(C_n;ℤ)=ℤ/n via norm map | (loose lean file) |
| 6 | cyclic-h2-gcd-engine | **LV** | H²(C_n;ℤ/m)=ℤ/gcd(n,m), unified engine | (loose lean file) |
| 7 | fibre-h2-z2-engine | **LV** | H²(ℤ/2;ℤ/2)=ℤ/2, nonsplit-ℤ/4 vs Klein witnesses | (loose lean file) |
| 8 | equivalence-chain | **IP** | DCont=Poly-comonad=Cat; M1–M4 done, M5/M6 OPEN | (milestone tracker) |
| 9 | closed-tensor-classification | **IP** | left-closed convolutional tensors; infinite-arity OPEN | 2026-07-23-closed-convolutional-tensors-classification.md |
| 10 | clio-peer-claims | **PC** | Clio's asserted results (transfer operators etc.) | — |
| 11 | game-comonad-poly | **C** | EF/pebble/modal game comonads factor through Poly | 2026-10-01-game-comonads-poly.md |
| 12 | groupoid-zs-obstruction | **C** | groupoid ZS merge ⟺ [ω]=0; cd≤1 ⟹ merge | 2026-07-24-groupoid-zs-obstruction.tex |
| 13 | other-cont-monoidal-tensors | **C** | ⋉/⋊ are the Dialectica tensors; ⋊ left-closed | 2026-07-17-ltimes-rtimes-dialectica.md |
| 14 | quiver-skew-brace-zs | **C** | Ferri prunability = ZS global-obstruction vanishing; = descent | 2026-09-16-ferri-prunability-vs-zs-holonomy.tex |
| 15 | supply-chain-zs | **C** | supply chain = DCont; shared-warehouse composition = ZS; [ω]∈H² | 2026-07-23-supply-chain-zs.tex |
| 16 | bare-dirichlet-comonoid | P | bare ⊗-comonoids = families of monoids | 2026-07-17-bare-dirichlet-comonoid.md |
| 17 | cartan-scalar-object-spoly | P | SPoly tangent bundle = monoids, no negation ⟹ Cartan fails | 2026-10-05-spoly-negation-obstruction.md |
| 18 | closed-day-structures | P | Day tensor left-closed iff (−)⋆B polynomial; Π internal hom | 2026-07-15-uniform-closure-day-tensors.md |
| 19 | cofree-comonad | P | cofree comonad = ◁-comonoid on M-type of p-trees | 2026-07-25-cofree-comonad-universal-property.md |
| 20 | comparitor-comonoid-nogo | P | double comonoids in (Poly,◁,⊗) = sets of commutative monoids | 2026-07-15-comparitor-double-comonoid.md |
| 21 | composition-nerve-level | P | grade by nerve level; composition=N₂=degree 1; N₂⊊N₃ in assembly | 2026-10-08-nerve-level-tower.md |
| 22 | cont-cod-predicate-fibration | P | Cont(cod) = Fam(Set^op) bifibration; logic of containers | 2026-08-28-cont-cod-fibration.md |
| 23 | copowers-gap-writer-monad | P | (Q) copowers/writer-monad reformulation (ZFC) | 2026-08-26-copowers-gap-writer-monad.md |
| 24 | dirichlet-monoid-classification | P | bare ⊗-monoids = shape monoid + oplax functor on fibres | 2026-07-19-dirichlet-monoid-classification.md |
| 25 | effect-coeffect-arrows | P | effect/coeffect arrow face iff non-branching; class E+A×X | 2026-07-29-effect-coeffect-arrows.md |
| 26 | emergent-holonomy-is-ext-tower | P | meeting count = Ext^n_{kG} = ⊕H^n, the Ext tower | 2026-08-20-emergent-holonomy-is-ext-tower.md |
| 27 | fibredness-vs-left-closure | P | BHM ▷ left-variable fibredness result | 2026-08-30-fibredness-vs-left-closure.md |
| 28 | fullness-unit-connectedness | P | T1: ⟦−⟧ f&f ⟺ unit connected (NOT extensivity) | 2026-08-25-fullness-unit-connectedness.md |
| 29 | holonomy-triviality | P | liftings-≅-Cat collapse engine | 2026-08-11-state-liftings-holonomy-triviality.md |
| 30 | joint-bc-cont-cod | P | shape-level Fam-Kan quantifiers over Cont(Set)=Poly | 2026-08-28-joint-bc-cont-cod.md |
| 31 | left-adjoint-over-vec | P | (−)◁q left adjoint over Fam(Vec^op); summability doesn't gate | 2026-08-30-left-adjoint-over-vec.md |
| 32 | lie-parallelizable-poly-comonoid | P | poly comonoid parallelizable ⟺ out-degree; Lanfranchi port ill-posed | 2026-10-05-lie-parallelizable-poly-comonoid.md |
| 33 | linear-containers-vec | P | LinCont=Fam(Vec^op); biproduct collapse; faithful-not-full over Vec | 2026-08-18-linear-containers-vec.md |
| 34 | m-containers | P | M-Cont=Fam(Kl(M)^op); THM1/2/3; composition=polynomiality trichotomy | 2026-09-04-m-containers-codensity.md |
| 35 | monad-comonad-entwining | P | T_M effect + G_M coeffect entwine (bialgebra face all M) | 2026-07-27-monad-comonad-entwining.md |
| 36 | monad-comonad-transfer | P | Set-monad M → comonad G(S,P)=(S,M∘P) | 2026-07-25-monad-comonad-transfer.md |
| 37 | oneill-free-monad-linear-container | P | O'Neill free monad = free ◁-monoid = tensor algebra T(A) | 2026-08-23-oneill-free-monad-linear-container.md |
| 38 | orchestration-zs | P | orchestration = DCont; composition = ZS; re-entrancy = failed guard | 2026-07-20-orchestration-reentrancy-obstruction-analytic.tex |
| 39 | pairwise-zs | P | pairwise matched ⟹ global ZS iff (L) freeness ∧ (G) global closure | 2026-06-10-pairwise-zs-criterion.tex |
| 40 | pra-vs-probe-method | P | L_q=(−)◁q is a parametric right adjoint (Weber) | 2026-08-30-pra-vs-probe-method.md |
| 41 | solvability-obstruction-o-nu | P | o_ν:H²₊→C³/A hom, im φ⁺=ker o_ν; nontrivial ⟹ torsor | 2026-09-29-solvability-obstruction-o-nu.tex |
| 42 | state-object-delta | P | ΔS=codiscrete cat; store/costate comonad via ⊗ | 2026-07-28-delta-state-object-and-workers.md |
| 43 | supply-chain-inventory-gerbe-h2 | P | inventory gerbe [𝔤]∈H²(N(C);Z(Aut F)); rectify ⟺ [𝔤]=0 | 2026-10-08-supply-chain-inventory-gerbe.md |
| 44 | t2-day-closedness-famcop | P | Dirichlet closedness over base = familial representability | 2026-08-26-t2-day-closedness-famcop.md |
| 45 | t4-left-closedness-lhd-famcop | P | ◁ left-closedness on Fam(C^op) | 2026-08-27-t4-left-closedness-lhd-famcop.md |
| 46 | tangent-container-derivative | P | ∂ = differential combinator of a CDC of poly functors | 2026-10-02-tangent-container-cdc.md |
| 47 | tangent-restricts-to-dcont | P | T(p)=p(y+εv) strict ◁-monoidal base change; laxator=chain rule | 2026-10-03-tangent-restricts-to-dcont.md |
| 48 | two-omega-sites | P | handoff [ω_h] and stabiliser [ω_st] sites irreducibly distinct | 2026-08-14-two-omega-sites-isotropy-restriction.md |
| 49 | vec-attention-composition | P | linear attention = composition in Mat(Vec) bicategory | 2026-08-22-linear-attention-odot-composition.md |
| 50 | virtual-container-cartan | P | ℕ→ℤ completion switches full Cartan calculus ON (SPoly_ℤ) | 2026-10-06-virtual-container-cartan.md |
| 51 | workers-retract-of-bhm-grading | P | Workers ⊗-grading is a retract (not fibre) of BHM ▷-grading | 2026-08-29-workers-retract-of-bhm-grading.md |
| 52 | workers-type-hierarchy | P | Workers_S type hierarchy across Cont's four structures | 2026-07-30-workers-type-hierarchy.md |
| 53 | holonomy-triviality (see #29) | — | — | — |

(Row 53 is a de-dup placeholder; 52 distinct roots + `clio-peer-claims` register = the 53 files.)

---

# Appendix B — Identified write gaps (for the drafting queue)

1. **Representation theorem has no registry node** (I.1) — the foundational "which functors are
   containers" is sourced only to `.tex`, ungraded. Open a proof file to ground it.
2. **Inventory `H¹` `[θ_R]` has no standalone node** (IV.1) — it lives inside
   `composition-nerve-level`. If the master document cites it as an independent degree-one result,
   it needs its own registry entry.
3. **Tax computation (SEED Path 5) has no write-up and no node** (IV.4) — model it or mark as
   explicit future work.
4. **GA empirical result is external** (IV.3) — Langer–Vega GECCO / ga-containers ACT are
   collaborator publications, not MacBeth nodes; cite as such.
5. **The nerve-note N2 correction (2026-10-09) must be propagated** — the demoted
   weld-`ω`-as-non-associativity gloss appears in the shipped degree-two-datum synthesis and the
   re-entrancy note; the master document must state `[ω]` as a splitting obstruction throughout
   (II.2, IV.2) and disambiguate "nerve level."
6. **Day-convolution treatment exists but is scattered** (I.3, per `OUTLINE.md` §3) — consolidation,
   not fresh proving.
7. **Effect "zoo" / update monad** (per `OUTLINE.md` §5) — the Ahman–Uustalu update monad has no
   MacBeth write-up of its own; the biggest *synthesis* gap, though the component results
   (`monad-comonad-entwining`, `state-object-delta`, `effect-coeffect-arrows`) are all `[proved]`.
