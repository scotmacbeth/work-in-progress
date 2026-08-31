# Connection: EXTENSIVITY is the boundary of the container program

**Crown claim.** The single categorical hypothesis that carries all of Set container theory —
representation theorem, `DCont≅Cat`, polynomial-functors-over-a-base — is **extensivity**
(coproducts are disjoint and universal, so `S=π₀` is an invariant of the extension functor).
Three independent literatures pivot on it, and my own 08-18 two-part Vec theorem is the same
pivot seen twice. **Base-change Set↝Vec breaks container theory at exactly one point: `∐ ⊊ ⊕`.**

## The one event, two faces (my PROVE 08-18, `proofs/2026-08-18-linear-containers-vec.md`)

- **Object-collapse.** Vec's terminal `= 0` ⟹ `⟦S,P⟧(0)=0` ⟹ Set slogan `F(1)=S` dies; finite
  ⟹ `⊕=Π` biproduct ⟹ `⟦S,P⟧≅Id^N`; shape partition invisible, shapes = indecomposable summands.
- **Morphism-collapse.** `Nat = ∏_s ⊕_t Vec(Q_t,P_s)`, container-hom `= ∏_s ∐_t Vec(Q_t,P_s)`;
  `⟦−⟧` faithful but not full because `∐_t ↪ ⊕_t` strictly.
- **Comonoid-collapse (PROVED 08-19, the THIRD face).** The Set `◁`-composition carries shapes
  `Σ_s S^{P_s}` — a *dependent sum* whose dependency is exactly the composable-arrow data of
  `DCont≅Cat`. Over Vec (Prop 4.1, `2026-08-19-vec-comonoids-algebras.md`) it flattens to the plain
  product `S×S`; the counit then forces `δ_shape=diagonal`, δ never reaches an off-diagonal block
  `P_a⊗P_b` (a≠b), and the `◁`-comonoid collapses to a *family* of one-object k-algebras —
  **no multi-object algebroid**. Deepest reading of the failure: not just shapes invisible / hom not
  full but *the composition data itself destroyed*. `Comon_◁(Fam(Vec_fd^op))≅Fam(Alg_k^op)`.
- **These are the SAME phenomenon:** the coproduct in the hom-formula IS the shape-disjoint-union
  in Set (extensive) and IS the biproduct in Vec (non-extensive). One inclusion `∐⊊⊕` governs
  the object non-recovery, the fullness failure, AND the dependent-sum flattening `Σ_s S^{P_s}↝S×S`
  that kills the algebroid. Three faces, one root.

## The three literatures that pivot on the same hypothesis (browse 08-18)

1. **Diers familial representability** (Diers 1977; nLab *multirepresentable functor*;
   Carboni–Johnstone 1995; Freyd 1966; Adámek–Rosický 1994). `F:A→Set` is a coproduct of
   representables ⟺ each component of `el(F)` has an initial object; then `S=π₀(el F)` and the
   positions (generic objects) are **recovered canonically** — *because Set is extensive*. Over
   Vec, `⊕` is a biproduct, `π₀` is not an invariant, and `(S,(P_s))↦⊕_s Vec(P_s,−)` is not
   faithful on objects. **This is the precise statement that the Set representation theorem
   degenerates.** (source `agent-summary`; nLab/definition level.)
2. **Gambino–Kock polynomial functors** (`arXiv:0906.4931`). Define poly functors over a
   **locally cartesian closed** base; get the free-monad-is-polynomial theorem. LCC ⟹ extensive
   enough; Vec is neither LCC nor extensive ⟹ machinery does not transfer. Their LCC assumption
   IS Diers' extensivity IS my `∐=⊕`. (`agent-summary`.)
3. **My `∐ ⊊ ⊕`** (PROVE 08-18, proved). The concrete failure at the additive base.

So: **Diers-extensivity = Gambino–Kock-LCC = my morphism-collapse.** Three names, one hypothesis;
its failure is the whole content of the Vec front.

## Why this is load-bearing (grant + program)

- It reframes the SEED's spine `Containers≃DCont≃PolyComonoid≃Cat` as a theorem *about extensive
  bases*. The equivalence chain is not base-neutral; it is a shadow of extensivity. That is a
  sharper, more honest statement of what the container program IS.
- It tells you exactly what a Vec (or any non-extensive-base) theory must replace: not `(S,P)`
  data but a **coordinate-free invariant** — a single position object with a comonoid /
  decomposition structure. This is the crown target
  ([[../topics/containers-over-vec]]: poly-`◁`-comonoid = algebroid).
- Cross-domain: the same "extensivity is what makes the disjoint-union bookkeeping work" appears
  wherever a classification is indexed by `π₀` — including the Set-side full-faithfulness of `⟦−⟧`
  (Abbott–Altenkirch–Ghani) that every container paper opens with. Nobody states that theorem as
  "…and this uses extensivity"; the Vec front makes the hidden hypothesis visible.

## The two valuations of `∐⊊⊕` — collapse is a LIABILITY globally, an ASSET locally (08-24, Neil's steer)

The whole note above reads `∐⊊⊕` as an *obstruction*: it breaks the rep theorem, kills full-faithfulness,
destroys the algebroid. Neil's 2026-08-24 Vec reply flips the sign on the *same equation* in the
application layer, and the flip is the cleanest ML-facing hook the Vec front has produced.

- **Neil's question:** prompt A with reply-space `A`, prompt B with reply-space `B` — what vector space
  handles *either* prompt? **Answer: the coproduct of the two one-shape linear containers `({*},A)⊔({*},B)`,
  whose extension is `h_A⊕h_B ≅ h_{A⊕B}`** (WRITE 08-24, `expository/containers-over-vec.tex` Prop 9.2;
  proof = only the existing additivity lemma, no new math, no new citations).
- **The reading (`A⊕B` is the biproduct):** coproduct = *either*, product = *both*; in Vec they coincide.
  So **"answer either prompt" and "be ready for both prompts" are the SAME object.** Over Set they split
  (`A⊔B ≠ A×B`) — the biproduct is exactly what makes either = both. Neil's own intuition ("coproducts
  survive but *also* carry the product's universal property, so no loss of coproducts") **is** the
  biproduct; the collapse Set↝Vec is not a degeneracy but the *precise content* of either=both.
- **One equation, opposite valuations.** `h_A⊕h_B ≅ h_{A⊕B}` global = `⟦S,P⟧≅Id^N`, the shape-erasure
  that made a rep theorem impossible (liability). The *same* additivity of `h`, read locally on a two-shape
  coproduct, is self-duality of either/both (asset). The Vec front's obstruction and its application hook
  are literally the same lemma at two scales.
- **The `⊕` does double duty.** The biproduct that gives either=both is the *same* `⊕_b` powering across-
  prompt composition in the matrix `◁` (`(P◁Q)_{ac}=⊕_b P_{ab}⊗Q_{bc}`, [[vec-lax-matrix-crown-resolved]]).
  Vec having biproducts underwrites both either=both AND composable-responses — one structural fact, the
  extensivity failure, is what the application *needs*, not what defeats it.
- **Grant-Impact framing (Path 5).** This is the container reading of "an LLM prompt is a request-type with
  a response-space, and handling a menu of prompts = the biproduct of their response-spaces." "Responses =
  uncertainty = basis of learning" (Neil). Ties the Vec front directly to agent-orchestration applications.

## The biproduct collapse is UNIVERSAL — Hedges' additive lenses are the same lemma (browse 08-25)

The either=both reading above is not a Vec artifact; it recurs wherever a linear/additive structure sits
under a container-like formalism. **Jules Hedges, "Autodiff through function types"** (julesh.com,
2026-02-20) proves the category of **additive lenses is cartesian closed because commutative monoids have
biproducts** (products = coproducts) — the *identical* `∐=⊕` phenomenon as my proved
[[vec-biproduct-collapse-proved]], under autodiff/gradient types instead of Vec containers. His punchline is
a *cautionary* companion for the "uses" note: using function types as a learning parameter space just
re-derives ordinary deep learning with overhead. **Grant-universality payoff:** "biproduct ⟹ either=both"
is a structural cross-domain pattern (Vec containers, additive lenses, and — via the matrix `◁` — composable
responses), exactly the kind of one-theorem-many-domains claim the SEED's universality value wants. Strong
citation candidate. Source `reading/2026-08-25.md` (blog, direct-read-quality summary).

**Two precedents for the Vec "uses" front (Neil's #1 priority), neither framed as "container":**
Vertechi's "NN layers as parametric spans" (`y[t(p)] += x[s(p)]·w[π(p)]` = container/poly shape with a
Vec-valued action on positions) and Bradley's `[0,1]`-enriched LLM-semantics category. Neither cites
Abbott/Ahman/Ghani ⟹ the container framing is a genuine contribution *only if it unifies/sharpens* these,
not just restates them. Do a comparison pass before finalizing the VCont note. (agent-summary, 08-25.)

## Caveats / provenance

- **Primary citable anchor now secured (browse 08-19):** nLab *extensive category* states
  "**Vect is not even finitely extensive**" verbatim (Carboni–Lack–Walters 1993) — the crux of
  Face 2 no longer rests on my own derivation. nLab *multirepresentable functor* (indexed 08-19)
  pins Diers' criterion (Prop 2.1.2). Both now in `sources.json`.
- Diers / Gambino–Kock / Adámek–Rosický entries remain `agent-summary` (abstract/definition level,
  not deep-read) — deep-read Diers + Carboni–Johnstone 1995 before load-bearing in a paper.
- The char-p subtlety (David Speyer trap, [[../topics/containers-over-vec]]) sits underneath:
  even value-wise equality of functors is weaker than functor-equality, so "shapes invisible"
  is about the *evaluation*, not a genuine collapse of distinct functors.

## Links

[[../topics/containers-over-vec]] · [[vec-biproduct-collapse-proved]] · [[vec-containers-new-front]]
· contrast with Set-side [[dcont-cat-is-the-convergence-hub]] (the extensive-base equivalence hub).
