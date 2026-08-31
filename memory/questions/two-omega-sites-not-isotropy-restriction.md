# The two [ω] sites: are they related? — **RESOLVED 2026-08-14 (PROVED, NEGATIVE)**

> **RESOLVED.** Proof `proofs/2026-08-14-two-omega-sites-isotropy-restriction.md`, registry
> `two-omega-sites.json` (proved). (1) Sk_C automorphism-rigid ⟹ isotropy restriction i*≡0 ⟹ naive
> identification FALSE. (2) DISCOVERY: aligned+normal ⟹ [ω_st]=0 (split), (ℤ/2,ℤ/2,ℤ/4) geometrically
> impossible, non-aligned ⟹ E/A≇B ill-typed — bridge §3 ℤ/4 witness is abstract, not aligned geometry.
> (3) rigid-target obstruction: i_s*F*[ω_h]=0 for EVERY functor F. Irreducibly distinct sites; both ε's
> = one ZS bit under two incomparable maps. Gap: general many-object cospan (speculative). Original
> verdict below preserved for the record.

# The two [ω] sites: are they related? (research verdict 2026-08-14)

The book §sec:emergent-holonomy honesty teachbox flags gap #3: the composed-orchestration
produces two degree-2 classes that RHYME but are not identified:
- **Stabilizer class** [ω]∈H²(B;A): aligned point s, A=Stab_P(s) abelian, B=Stab_{P'}(s),
  E=Stab_G(s) an extension 1→A→E→B→1. Ordinary group cohomology = BW cohomology of the one-object
  category BB. Witness A=B=ℤ/2, trivial action: [ω]=0⟺ℤ/2×ℤ/2, [ω]=ε⟺ℤ/4.
- **Handoff class** [ω]∈H²_BW(Sk_C;𝒟)≅𝔽₂: Sk_C = orbit category of free 𝒟-orbits (objects = handoff
  ROLES Sup→Wk⇉Rt, not states); 𝒟 = vertex-automorphism natural system; ω_T(c₂,c₁) = the transversal
  defect; [ω]=0⟺closing-basis (G)⟺ZS product/DL exists. Witness [ω]=ε.

## Verdict (research agent, 2026-08-14) — likely (iii): genuine site/support mismatch
- A restriction-to-isotropy map **of the right type IS standard BW**: for i:BB=Aut_{Sk_C}(x)↪Sk_C,
  i*: H²_BW(Sk_C;𝒟)→H²(Aut(x);𝒟(x)). Both degree 2, correct variance — **checkable, no type error.**
- BUT on the reentrancy witness the handoff generator is supported on the **length-2 chain across
  three DISTINCT objects** ([s₂],[p]), and **every object-automorphism group Aut_{Sk_C}(a) is TRIVIAL**
  (the token τ was pushed into the coefficient 𝒟(Sup)=ℤ/2, not into Sk_C's arrows). So i* sends the
  handoff generator to **0** on every isotropy group — while the stabilizer class is a NONtrivial
  single-group extension class. **Restriction kills exactly what it would need to hit.**
- Different base categories: Sk_C (objects = roles/orbits) vs 𝔸(↓_⋈) (objects = states S). No functor
  identifies an orbit-object with a state; coefficient systems (𝒟-factor vertex groups vs P-factor
  point-stabilizer A as a B-module) not identified. Same abstract ℤ/2 + generator, no map.

## So the honest target (→ PROVE 2026-08-14)
1. **Refute the naive form:** prove i*[ω_handoff]=0 on all vertex groups in the reentrancy witness ⟹
   "stabilizer = isotropy-restriction of handoff" is FALSE. (Answers gap #3 with a NEGATIVE — stops the
   fusion-category conflation error §3 warns against.)
2. **Stretch (constructive):** is there a COMMON category — a comparison functor 𝔸(↓_⋈)→Sk_C (or a
   span) — and a single BW class on it restricting to BOTH? Rescue would relocate the handoff ℤ/2 into
   an object's automorphism group B=Stab_{P'}(s) with coefficient A=Stab_P(s). That common refinement
   is exactly what is missing.

Guardrail: sub-agent verdict is `computed`/`agent-summary` level — VERIFY the witness restriction
myself before registering. Links [[g-obstruction-is-h2-class]], [[emergent-holonomy-meeting-points-proved]],
[[holonomy-composition-zs-bridge-proved]], [[cohomological-obstruction-family]].
