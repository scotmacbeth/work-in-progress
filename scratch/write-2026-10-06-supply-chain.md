# WRITE scratch — supply-chain inventory = degree-1 class (2026-10-06)

## Trigger status
WRITE.md is STALE: it targets the Lanfranchi parallelizability note, which is ALREADY
SHIPPED (papers/parallelizability-does-not-port.tex, 8pp, commit e154282, SHIPPED memory
node 10-06). Per feedback `check_memory_and_registry_before_dispatching_trigger`, do not
redo. Fell through to "most significant unwritten recent proof" =
proofs/2026-10-06-supply-chain-inventory-consistency.md (proved; registry supply-chain-zs
updated 10-06 with dividing-line correction; NO draft in papers/). Grant Applications pillar.
→ Note this stale trigger in the Robin handoff.

## Phase 1 — the one sentence (seed)
Supply-chain inventory consistency is the vanishing of a DEGREE-1 class [θ_R]∈H¹(𝒮;R) on the
resource presheaf (the route-reconvergence discrepancy), and is LOGICALLY INDEPENDENT of the
degree-2 Zappa–Szép weld obstruction [ω]∈H²(Sk_𝒮;𝒟) governing whether the chain factors at
all — so the cohomological DEGREE of a compositional failure records WHERE the conserved
quantity lives (nodes H¹ vs weld H²).

## Audience
Categories + cohomology literate (BW cohomology, Mayer–Vietoris, presheaves/local systems).
NOT assumed: the container dictionary. Define on first use: directed container ≅ small cat,
ZS product ⋈, weld obstruction [ω], resource presheaf R, [θ_R].

## Skeleton
1. Intro — compositional correctness has economic consequences; "two routes to a delivered
   good"; conjecture (C): inventory inconsistent ⟺ [ω]≠0 (false-generalisation of blockchain
   re-entrancy [ω]=ε). Gap: nobody wrote the resource presheaf explicitly & compared classes.
   Result: (C) false both ways; inventory consistency = [θ_R]=0 in H¹, independent of [ω].
   Method: Lemma A (λ invisible) + Mayer–Vietoris + 2 witnesses. Consequence: degree table.
2. Preliminaries — (2.1) directed container = small cat; (2.2) ZS product & weld [ω]∈H²(Sk;𝒟);
   (2.3) resource presheaf / local system R, inventory global section; the modelling choice
   (free cat on operation quiver, NOT thin poset — distinct routes = distinct morphisms).
3. Lemma A — matched-pair law invisible to inventory (generators argument; brute-checked flip
   ZS pair ℤ/3). Consequence: inventory cut out by 𝒞- and 𝒟-constraints only.
4. Theorem 1 — inventory consistency ⟺ [θ_R]=0 ∈ H¹(𝒮;R) (unconditional via Lemma A);
   closed form via Mayer–Vietoris of cover {𝒞,𝒟}, discrete overlap O, acyclic factors ⇒
   H¹ ≅ coker[H⁰(𝒞)⊕H⁰(𝒟)→H⁰(O)] = reconvergence discrepancy. Diamond example (deltas 2,1,1,3
   → holonomy −1; over ℤ/n gcd engine).
5. Theorem 2 — independence. W1: free diamond, no invertibles ⇒ 𝒟=0 ⇒ [ω]=0 forced, but
   betti₁=1 ⇒ [θ_R]≠0. W2: rigid-twist a→x⇉y, End=ℤ/2, [ω]=gen≠0, coboundary inventory ⇒
   [θ_R]=0. Different degree AND coefficients (R vs 𝒟) ⇒ no natural comparison map.
6. Why (C) looked right — re-entrancy is where inventory IS the weld-state (no separate
   presheaf); Prop 3 (no rescue regime: Bℤ degree mismatch H¹=A,H²=0). Reconcile W_{n,ε}:
   it computed the WELD/PROVENANCE class via PARALLEL arrows (vertex-group loop), correct but
   of the OTHER class; relabel provenance-consistency. Dividing line = WHERE the loop lives
   (parallel arrows/vertex group → H²; distinct-node reconvergence/nerve → H¹).
7. Conclusion — degree table (nodes H¹ route / weld H² handoff / factorization H² closure);
   economic reading; honest open: torsor/gerbe inventory → genuine H² (still ≠ [ω]); non-acyclic
   factors (equivalence survives, closed form changes); Prop 3 general connecting map sketched;
   object-level fidelity (SEED Q4) OPEN — abstraction not fidelity claim.

## Honesty ledger (diff every sentence vs PROOF FILE §9)
- Lemma A: inventory in a sheaf of GROUPS. Torsor-valued ⇒ gerbe ⇒ H² (OPEN). State clearly.
- Thm 1 EQUIVALENCE (consistent⟺[θ_R]=0) is UNCONDITIONAL (Lemma A); only the CLOSED FORM
  needs acyclic 𝒞,𝒟. Do not overstate the closed form as unconditional.
- Prop 3: state at the level the witnesses + Bℤ degree-mismatch support (no NATURAL iso in
  general). The general spectral-sequence connecting map is SKETCHED, not developed → OPEN.
- Modelling fidelity: "a real supply chain IS this category" = SEED Q4, OPEN. Faithful
  abstraction, not fidelity claim. Say so.
- W_{n,ε} node is NOT wrong — correct computation of the WELD class, mislabelled. Be fair.
- Be scrupulously fair: (C) is a *reasonable* conjecture (re-entrancy template), not a blunder.

## Citations (all deep-read or classical-load-bearing across shipped corpus)
- au-dccat Ahman–Uustalu 2016 (deep-read 1604.01187) — DCont = small cat
- au-distlaw Ahman–Uustalu 2013 — ZS from distributive laws of directed containers
- bw Baues–Wirsching 1985 — cohomology of small categories (classical)
- rw Rosebrugh–Wood 2002 — distributive laws & factorization (classical)
- weibel Weibel 1994 — homological algebra (Mayer–Vietoris / group cohomology, classical)
- Internal (proved shared stubs): pairwise-zs, g-obstruction(=H²), orchestration/re-entrancy
  (lean-verified [ω]=ε), supply-chain-zs (computed, now relabelled), logic-of-containers
  (Cont(cod)=Fam(cod^op) fibration, proved).

## Output
papers/supply-chain-inventory-degree-one.tex ; compile pdflatex; push + Robin note.
