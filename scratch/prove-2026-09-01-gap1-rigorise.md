# PROVE scratch — Rigorise Set×Vec_fd ∈ Gap 1, hunt irreducible inhabitant

Date: 2026-09-01. Goal (1): promote Set×Vec_fd admissibility from `computed`→`proved`
(full ◁ construction + naturality + locus + coherence discussion). Goal (2): irreducible
non-product Gap-1 inhabitant — test k[ε]/ε² first.

## Setup / conventions

C = Set × Vec_fd. Objects X = (X_s, X_v), X_s a set, X_v a fd k-vector space.
- ⊗ = (×_Set, ⊗_k), unit I = (1, k).
- [X,Y] = (Y_s^{X_s}, Hom_k(X_v, Y_v)).
- coproduct ∐ = (⊔_Set, ⊕_k). (Vec coproduct = biproduct.)

Fam(C^op): p = (S, (P_s)_{s∈S}), P_s = (A_s, V_s), A_s a set, V_s fd.
Extension: ⟦p⟧(X) = ∐_{s∈S}[P_s,X] = ( ∐_{s} X_s^{A_s},  ⊕_{s} Hom_k(V_s, X_v) ).

**LOCUS (the summability boundary, stated up front):** for ⟦p⟧ to be an endofunctor of
Set×Vec_fd we need ⊕_s Hom_k(V_s,X_v) fd, i.e. **finite vec-support**: {s : V_s ≠ 0} finite.
S itself and each A_s may be arbitrary (infinite). Call 𝒫 ⊆ Fam(C^op) the full subcat of
objects with finite vec-support (V_s fd, cofinitely many V_s = 0).

## Computational Evidence (scratch/2026-09-01-gap1-verify.py — ALL PASS)

- **Target (1)** built the map on 3 cases /𝔽_2 (2 asymmetric, 1 zero-position): Θ_set a BIJECTION
  with inverse round-trip both ways (exhaustive); Θ_vec an INVERTIBLE coordinate permutation
  (s,t,i,j,k)↔(s,t,k,j,i), full rank; naturality squares (both components) commute for nontrivial φ.
  |D| and dims all match. Case (a) |D|=4, 16/16, 4/4; (b) |D|=6, 42/42, 6/6; (c) |D|=6, 42/42, 2/2.
  **A built map, not a 4=4 collision.** Θ is a natural iso.
- **Dual numbers** /R=𝔽_2[ε]/ε²: (2a) dim Hom_R(P,⊕M)=Σ dim Hom_R(P,M) on 50 random + {k,R,R⊕k},
  0 mismatches (every fg module copower-tiny). (2b) collapse ◁=⊗_R identity, 50 random, 0 mismatches.
  (2c) k copower-tiny YES, k projective NO (no R-linear section of R↠k). ⟹ fd-R-Mod = COLLAPSE base.

## OUTCOME: both targets discharged. Verify phase — all steps GREEN (hostile re-read done).
Proof file: proofs/2026-09-01-gap1-setxvec-proved.md (proved). Registry promoted. Collaborator note
+ memory + SUMMARY + PROGRESSIVE_DISCLOSURE updated.

## Precise Statement — Target (1)

**Theorem (Set×Vec_fd admissible).** On the locus 𝒫 (finite vec-support), for all p,q ∈ 𝒫
there is r = p◁q ∈ 𝒫 with a NATURAL iso ⟦p◁q⟧ ≅ ⟦p⟧∘⟦q⟧ of endofunctors of Set×Vec_fd.
Hence 𝒫 is ◁-admissible (Def 1.1). Moreover C = Set×Vec_fd is:
- non-collapse: (A,V) copower-tiny ⟺ |A|≤1; objects with |A|≥2 not tiny.
- non-cartesian: ⊗ ≠ × since ⊗_k ≠ ⊕_k.
- disconnected unit: C(I,−) = (X_s × |X_v|) does not preserve coproducts (Vec factor).
⟹ Theorem B (extensive+ccc+admissible ⟹ connected) is NOT SHARP: "admissible ⟹ connected"
fails in general; the extensivity+cartesian hypotheses are essential.

### The construction of r = p◁q  (p=(S,(A_s,V_s)), q=(T,(B_t,W_t)))
- Shape set D = ∐_{s∈S} T^{A_s} = {(s,f) : s∈S, f:A_s→T}.  [FORCED by Set factor]
- Set-position C_{(s,f)} = ∐_{a∈A_s} B_{f(a)}.  [FORCED]
- Vec-positions: pick (if the vec-sum is nonempty) a slot d_0∈D; set
  U_{d_0} = ⊕_{s,t} V_s⊗W_t (finite ⟹ fd), U_d = 0 otherwise.  [a CHOICE — see coherence]
  (If ⊕_{s,t}V_s⊗W_t = 0, all U_d = 0.)

### The comparison map Θ_X = (Θ^set_X, Θ^vec_X), explicit
**Set part** Θ^set_X : ∐_{(s,f)} X_s^{C_{(s,f)}} → ∐_s (∐_t X_s^{B_t})^{A_s}.
LHS elt = (s, f:A_s→T, g:∐_a B_{f(a)}→X_s). RHS elt = (s, h:A_s→∐_t X_s^{B_t}).
Map: (s,f,g) ↦ (s, h) with h(a) = (f(a), g|_{B_{f(a)}}). Inverse: h(a)=(t_a,k_a) ↦ f(a)=t_a,
g|_{a-th summand}=k_a. This is the classical Set-container composition bijection, natural in X_s.

**Vec part** Θ^vec_X : [U_{d_0}, X_v] = [⊕_{s,t}V_s⊗W_t, X_v] → ⊕_s[V_s, ⊕_t[W_t,X_v]].
Composite of natural isos:
 [⊕_{s,t}V_s⊗W_t, X_v] ≅ ∏_{s,t}[V_s⊗W_t,X_v]   (hom out of ⊕ = ∏; univ. prop.)
   = ⊕_{s,t}[V_s⊗W_t,X_v]                          (finite support ⟹ ∏=⊕)
   ≅ ⊕_{s,t}[V_s,[W_t,X_v]]                         (tensor-hom adjunction)
   ≅ ⊕_s[V_s, ⊕_t[W_t,X_v]]                         (V_s fd ⟹ [V_s,−] preserves finite ⊕)
All four steps natural in X_v ⟹ Θ^vec natural. Both components isos ⟹ Θ iso. ∎

### Locus closure
r ∈ 𝒫: vec-support of r = {d_0} (or ∅), trivially finite. U_{d_0}=⊕_{s,t}V_s⊗W_t fd since
{(s,t):V_s⊗W_t≠0} = {s:V_s≠0}×{t:W_t≠0} finite (both factors finite by locus) and each fd. ✓
**Outside the locus:** infinite vec-support ⟹ ⊕_s[V_s,−] leaves Vec_fd (extension not even an
endofunctor). Over FULL Vec (drop fd): non-fd positions V_s not copower-tiny, [V_s,−] fails to
preserve ⊕_t, absorption breaks — predecessor Gap 1, OPEN.

### Coherence / associativity (the bonus, honest)
◁ is NOT strictly associative as an op on 𝒫: the slot choice makes (p◁q)◁r and p◁(q◁r)
generally non-isomorphic objects (Vec-data redistributed among fixed Set-slots — Theorem D's
non-faithfulness on the Vec factor). BUT ⟦(p◁q)◁r⟧ = ⟦p⟧⟦q⟧⟦r⟧ = ⟦p◁(q◁r)⟧ as endofunctors
(functor composition strictly associative; each ⟦p◁q⟧≅⟦p⟧⟦q⟧ naturally). Unit y=({*},(1,k)),
⟦y⟧=Id. So the monoidal structure lives in the IMAGE ⟦𝒫⟧ ⊆ [C,C] (a strict monoid under ∘),
not on 𝒫 itself. Admissibility (Def 1.1) is exactly the right level. Obstruction to strict
monoidality = non-injectivity of ⟦−⟧ on the Vec factor = Theorem D.

## Target (2) — irreducible inhabitant hunt

### KEY CORRECTION to the brief's probe (dual numbers)
The brief conjectured R=k[ε]/ε² gives an "internal rigid/flexible mix" (dualizable free modules
vs non-dualizable k). BUT the programme's axis is **copower-tiny** ([P,−] preserves coproducts),
NOT dualizable. Over R:
- Hom_R(k,−) = ker(ε:−→−) preserves ALL direct sums (kernels commute with ⊕). So **k IS
  copower-tiny** despite being non-projective/non-dualizable.
- Every fg R-module ≅ R^a⊕k^b; R and k both copower-tiny; ⊕ of copower-tiny is copower-tiny.
- More generally: P finitely generated ⟹ Hom_R(P,−) preserves ⊕ (image of fg lands in finite
  subsum). So over the Artinian ring R, EVERY fg module is copower-tiny.
⟹ **fd-R-Mod (= fg-R-Mod) is a COLLAPSE base** (all objects tiny), ◁ = ⊗_R, admissible,
disconnected unit — sits with Vec_fd on the collapse pole. **NOT Gap 1** (Gap 1 = non-collapse).
The dual-numbers probe is REFUTED. The projective/dualizable-vs-not distinction is NOT the
rigid/flexible axis; copower-tiny = finitely generated is.

### Consequence — sharpened structural picture
- rigid (non-copower-tiny) ⟺ non-fg (in module/additive world) OR extensive |A|≥2 (Set world).
- In an ADDITIVE base with fg=fd (Artinian ring, Vec_fd, gr-Vec_fd, …) EVERY object is
  copower-tiny ⟹ collapse pole ⟹ never Gap 1.
- To be non-collapse & additive you need genuinely non-fg objects ⟹ infinite ⊕ in the
  absorption ⟹ ties irreducibility to the OPEN predecessor Gap 1 (full-Vec admissibility).
- To be non-collapse & extensive ⟹ Theorem B forces CONNECTED unit ⟹ not Gap 1.
- Gap 1 therefore lives at the SEAM of an extensive (rigid) and additive (flexible) mechanism.
  The cleanest realisation is a PRODUCT Set×Vec_fd. **Conjecture (decomposition):** every
  "nice" Gap-1 inhabitant decomposes as rigid-extensive × flexible-additive; irreducible
  inhabitants either don't exist (in nice bases) or require resolving predecessor Gap 1.

### GENERAL LEMMA (proved) — every fg-module base is COLLAPSE
**Lemma (fg ⟹ copower-tiny).** For any ring R and any finitely generated left R-module P,
Hom_R(P,−) preserves coproducts (P is copower-tiny).
*Proof.* Let p_1,…,p_n generate P. Any φ: P→⊕_{i∈I}M_i sends each p_j into a finite subsum
⊕_{i∈F_j}M_i (finite support of φ(p_j)). Put F=∪_j F_j (finite). The p_j generate P and φ is
R-linear, so φ(P)⊆⊕_{i∈F}M_i: φ factors through the finite subsum. Hence
Hom_R(P,⊕_I M_i)=colim_{F fin}Hom_R(P,⊕_{i∈F}M_i)=colim_F ∏_{i∈F}Hom_R(P,M_i)=⊕_{i∈I}Hom_R(P,M_i),
and the canonical map ⊕_iHom_R(P,M_i)→Hom_R(P,⊕_iM_i) is a bijection. ∎

**Corollary.** For R commutative Noetherian, the base fg-R-Mod (closed sym monoidal under ⊗_R,
[−,−]=Hom_R, unit R, disconnected) is a **collapse base**: every object copower-tiny, ◁=⊗_R
(finite-support proviso, as for Vec_fd=fg-k-Mod). Hence NO fg-module base inhabits Gap 1 —
including k[ε]/ε² (dual numbers), k[x], recollements/pullbacks of module cats, ℤ-modules, etc.
This kills the entire "modules over a mixed ring" candidate family for irreducible Gap-1 at once.
The dual-numbers "rigid/flexible mix" was projective-vs-nonprojective (dualizable), which is NOT
the programme's axis; copower-tiny = fg, and Artinian ⟹ all fg ⟹ all tiny ⟹ collapse.

### Coherence resolved (the obstruction characterised)
A CANONICAL monoidal structure on (𝒫,◁,y) does NOT exist: the concentration slot d_0∈D=∐_sT^{A_s}
needs AC and is not natural. But a NON-canonical one DOES: choose slots compatibly via the Set
associator (Set-container composition is canonically associative; concentrate the total vec-space
⊕V⊗W⊗Z at the Set-corresponding slot on each side). The obstruction to CANONICITY is exactly the
non-faithfulness of ⟦−⟧ on the Vec factor (Theorem D). The canonical monoid lives in ⟦𝒫⟧⊆[C,C]
(functor composition, strictly associative). Admissibility (Def 1.1) is the honest deliverable.

### Absorptive dichotomy (necessary condition, toward the characterisation)
Call P ∈ C **absorptive** if X ↦ [P, ⟦q⟧(X)] is an extension for every q ∈ Fam(C^op).

**Prop (localisation of admissibility).** Fam(C^op) is ◁-admissible ⟺ every object of C is
absorptive. *Proof.* (⟸) ⟦p⟧⟦q⟧(X)=∐_{s}[P_s,⟦q⟧(X)]; each summand an extension (P_s absorptive
at this q), and a coproduct of extensions is an extension (∐∘∐=∐). (⟹) take p=⟨P⟩. ∎
This is the cleanest form of Neil's #1 question: admissibility is a PER-OBJECT property.

Two sources of absorptivity:
- **copower-tiny** P: [P,⟦q⟧X]=[P,∐_t[Q_t,X]]=∐_t[P⊗Q_t,X] — extension (shape T, positions P⊗Q_t).
- **distributive/extensive** P: [P,∐_tY_t]=∐_{f:P→T}∏_a Y_{f(a)} and ∏_a[Q,X]=[∐Q,X] — extension.
CONJECTURE (absorptive dichotomy): over a closed cocomplete base every absorptive object is a
"product" of a copower-tiny part and a distributive part; hence admissibility ⟺ every object
splits tiny⊗distributive. Set×Vec_fd: (A,V)=(A,k-ish)⊗(1,V), distributive⊗tiny. fg-R-Mod: every
object tiny (distributive part trivial). Set/topos: every object distributive (tiny part trivial).
This conjecture, if true, IS the classifying axis (replaces cartesianness/idempotent-splitting).

## Strategy
Target (1): direct construction + explicit natural iso (done above, verify computationally).
Target (2): refute dual numbers (prove the copower-tiny=fg lemma), then state sharpened
conjecture + decomposition conjecture + absorptive framing as honest partial progress; leave
irreducibility precisely open (tied to predecessor Gap 1 / to the decomposition conjecture).

## Key Lemma (target 1 crux)
The Vec absorption: [⊕_{s,t}V_s⊗W_t, X_v] ≅ ⊕_s[V_s,⊕_t[W_t,X_v]] naturally, via the 4-step
chain. Load-bearing finiteness: {s:V_s≠0}, {t:W_t≠0} finite (locus).
