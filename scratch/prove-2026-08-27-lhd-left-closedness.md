# PROVE scratch — ◁ left-closedness on Fam(C^op) (T4-left)

Started 2026-08-27. Target from state/PROVE.md.

## 0. The objects, base-general

`C` closed symmetric monoidal, complete+cocomplete, small (co)products. Internal hom `[-,-]`.
`Fam(C^op)`: objects `(S,(P_s)_{s∈S})`, S a set, P_s ∈ C. Morphisms
  Fam((A,X),(B,Y)) = ∏_{a} ∐_{b} C(Y_b, X_a).
Free coproduct completion of C^op; generators `⟨Z⟩ := ({*}, Z)`, embedding C^op ↪ Fam(C^op).

**Extension as endofunctor** (uses closedness+cocompleteness):
  ⟦S,P⟧ : C → C,   ⟦S,P⟧ X = ∐_{s∈S} [P_s, X].
Over C=Set: [P_s,X]=X^{P_s}, ∐=Σ, so ⟦S,P⟧X = Σ_s X^{P_s} = Poly. ✓

Substitution product ◁ is functor composition of extensions WHEN the composite lands back in
this class:  ⟦(S,P)◁(T,Q)⟧ = ⟦S,P⟧ ∘ ⟦T,Q⟧.  Explicitly
  ⟦(S,P)◁(T,Q)⟧X = ∐_s [P_s, ∐_t [Q_t, X]].            (COMP)
This lands back in Poly_C = {∐_u[N_u,-]} iff  [P_s, ∐_t B_t]  is again a coproduct of
closed-representables. THAT distributivity is the whole game (see §2).

## 1. DISAMBIGUATION — which adjoint is "left internal hom"? (do first)

⟦p◁q⟧ = ⟦p⟧∘⟦q⟧, p OUTER, q INNER.

Two one-sided operations, each a possible internal hom:
 (I)  L_q := (−)◁q : p ↦ p◁q.  On extensions = PREcompose by ⟦q⟧: F ↦ F∘⟦q⟧.
      • RIGHT adjoint to L_q  = Ran_{⟦q⟧}(−).   [the "◁-CLOSURE"]
      • LEFT adjoint to L_q   = Lan_{⟦q⟧}(−).
 (II) R_p := p◁(−) : q ↦ p◁q.  On extensions = POSTcompose by ⟦p⟧: F ↦ ⟦p⟧∘F.
      • RIGHT adjoint to R_p exists iff ⟦p⟧ has a right adjoint (rare for poly).
      • LEFT adjoint  to R_p exists iff ⟦p⟧ has a left adjoint.

Known facts (my corpus):
 - ◁-COCLOSURE exists in Cont (= directed containers, Niu–Spivak Prop 6.57;
   my position-op note: G=Lan_{(S,P)}M is the ◁-left-coclosure). It is a LEFT adjoint / Lan.
 - ◁-CLOSURE (right adjoint to −◁p) does NOT exist in Cont (workers Thm 2:
   Ran_{⟦p⟧}F is non-polynomial, double-exp shape growth).

So the honest reading of PROVE.md "left internal hom [Q◁−], curry the LEFT argument,
OBSTRUCTED over Cont" = **RIGHT adjoint to L_q = (−)◁q = Ran_{⟦q⟧}**. This is the
◁-closure. TARGET: does a richer base C repair Ran_{⟦q⟧} landing back in Poly_C?

Neil's hint says LEFT Kan preserves representability. Ran is RIGHT Kan. Tension noted:
either (a) Neil means the coclosure (Lan, already known — then the task is generalize it to
Fam(C^op) and name the survival hypothesis), or (b) the mechanism for the closure is
secretly a Lan after a dualization (over rigid C, Ran_{⟦q⟧}=Lan_{⟦q^*⟧}-ish). Resolve in §2–3.

## 2. The Set obstruction, re-derived structurally (what exactly fails)

Right adjoint to L_q=(−)◁q. Since L_q preserves shape-coproducts in its LEFT arg
(⟦(∐_i p_i)◁q⟧=∐_i⟦p_i⟧∘⟦q⟧), by the universal property of the free coproduct completion
the right adjoint exists iff the functor
  G(Z) := Fam( ⟨Z⟩◁q, (R,M) ) : C^op → Set     (⟨Z⟩=({*},Z))
is familially representable, for every target (R,M). Then [q◁−](R,M)=(U,(N_u)) with
G ≅ ∐_u C(N_u,−).

Need ⟨Z⟩◁q. ⟦⟨Z⟩⟧X=[Z,X], so ⟦⟨Z⟩◁q⟧X=[Z, ∐_t[Q_t,X]].  Over Set: =(∐_t X^{Q_t})^Z
= ∐_{τ:Z→T} ∏_{d∈Z}X^{Q_{τ d}} = ∐_{τ:Z→T} X^{Σ_d Q_{τ d}}. Container: shapes T^Z,
positions Σ_{d∈Z}Q_{τ d}. Then (L2 of workers)
  G(Z)=Fam(⟨Z⟩◁q,(R,M)) = ∏_{τ:Z→T} ⟦R,M⟧-hom... = ∏_{τ:Z→T} ∐_{r} C(M_r, Σ_{d∈Z}Q_{τ d}).
Over Set with C(M_r, N)=N^{... } wait C=Set so C(M_r,K)=K^{M_r}? No: Fam(Set^op) hom uses
C(Y_b,X_a); target positions M_r map INTO source positions. Let me just take R=y (M_r single,
=1... ) — cleanest witness. Redo carefully in code / below.

KEY STRUCTURE: the shape set of ⟨Z⟩◁q is `T^Z` = C-exponential-of-a-set-object... over Set the
shapes grow like |T|^{|Z|}; the outer product ∏_{τ:Z→T} then has |T|^{|Z|}-many factors ⟹
representing object would need |shapes| ~ (something)^{|T|^{|Z|}} — double exponential ⟹ not
polynomial. **The blow-up source: `[Z, ∐_t B_t]` turns an exponent-object Z into a PRODUCT over
the |Z| "elements", and product-over-elements distributed against ∐_t creates T^Z branches.**

Over Set the exponent Z is a SET so `[Z,−]=∏_{elts of Z}`. **The double-exp is powered by Z
having elements.** A richer base repairs this iff its `[Z,−]` does NOT explode against ∐ —
i.e. iff `[Z,−]` preserves coproducts (Z "tiny"/atomic). THAT is the hypothesis to name.

## 3. Conjecture (to test then prove)

**Conj T4-left.** On Fam(C^op), (−)◁q has a right adjoint landing in Fam(C^op) for all q
IFF every position object is **tiny** (=[Z,−] preserves small coproducts, i.e. ⟨Z⟩ is a
"linear/atomic" exponent). Equivalently ◁-closure exists ⟺ the exponents `[P_s,−]` are
coproduct-preserving. Name: **atomic-exponent / tininess** is the load-bearing conjunct.
- Over Set: tiny objects = ... only Z with [Z,−]=(−)^Z preserving ∐. (−)^Z preserves
  coproducts iff Z is ... connected? No: (−)^Z preserves ∐ iff Z is "connected and ..." —
  actually in Set, (−)^Z preserves coproducts iff |Z|≤1. (Z=∅:const 1, preserves; Z=1: identity,
  preserves; |Z|≥2: (A+B)^Z≠A^Z+B^Z.) ⟹ closure exists only when all positions are 0 or 1
  ⟹ linear polynomials. MATCHES: −◁p closure fails as soon as a shape has ≥2 positions
  (workers: "p with ≥2 shapes each ≥1 position"; sharpest witness p=2 shapes 1 position —
  recheck: is the obstruction ≥2 positions or ≥2 shapes? workers says T_R(A)=A^{S_p^A}, blows
  from |S_p|≥2, i.e. ≥2 SHAPES not positions. RE-EXAMINE.)

  ⟹ CAREFUL: the exponent creating the blow-up in G(Z)=∏_{τ:Z→T}(...) is the INNER shape set
  T of q, raised to the Z. So it's |T|≥2 (q has ≥2 shapes) that powers T^Z. And Z ranges over
  ALL objects (it's the variable of the representable). So even linear q with |T|≥2 kills it
  over Set. The "tiny positions" idea is about a DIFFERENT slot. Recheck in §4.

## 4. RESOLVED — the collapse mechanism (the crown)

**Variance settled.** "◁ left internal hom [Q◁−] / curry LEFT argument" = **right adjoint to
L_q=(−)◁q = the ◁-CLOSURE**. Over Cont (Set base) this is OBSTRUCTED (workers Thm 2:
Ran_{⟦q⟧}F non-polynomial, |T|^Z double-exp shape growth). Distinct from the ◁-COCLOSURE
(=DCont, right adjoint to p◁(−), a Lan, KNOWN, exists over Set). Not re-proving that.

**The obstruction's source, structural.** ⟦⟨Z⟩◁q⟧X = [Z, ∐_t[Q_t,X]]. Over Set,
[Z,−]=(−)^Z=∏_{d∈Z}, and ∏_Z distributes over ∐_t into T^Z branches (extensive/ccc
distributive law) ⟹ shape set of ⟨Z⟩◁q is T^Z ⟹ the ◁-closure would need a container
with |T|^{|Z|}-indexed data ⟹ super-polynomial ⟹ no closure. **The blow-up is powered by
[Z,−] NOT preserving the coproduct ∐_t.**

**The repair (my PROVED Prop 4.1, 2026-08-18/19).** Over Vec_fd, [Z,−]=Vec(Z,−) is LINEAR:
for Z finite-dimensional (= dualizable = TINY), [Z,∐_t B_t]=∐_t[Z,B_t] (internal hom
preserves coproducts). Hence
  ⟦⟨Z⟩◁q⟧X = [Z,⊕_t[Q_t,X]] = ⊕_t[Z,[Q_t,X]] = ⊕_t[Z⊗Q_t,X] = ⟦⟨Z⟩⊗q⟧X.
NO T^Z branching — shape set is just T. More: for ALL p,
  ⟦(S,P)◁(T,Q)⟧X = ∐_s[P_s,∐_t[Q_t,X]] = ∐_{s,t}[P_s⊗Q_t,X] = ⟦(S,P)⊗(T,Q)⟧X.
So **`◁ = ⊗` over Vec_fd** — EXACTLY my proved Prop 4.1: `(S,P)◁(T,Q)=(S×T,(P_s⊗Q_t))`,
the SAME formula as ⊗. The substitution product's dependent-sum shape set Σ_s Dec_T(P_s)
COLLAPSES to the plain product S×T; §6 of vec-comonoids-algebras is this collapse's comonoid
face (algebroid → family of algebras). The collapse is **tininess of positions**.

**Consequence chain.**
1. Over a base where positions are tiny (=dualizable), ◁ = ⊗ as bifunctors. ◁ becomes
   SYMMETRIC; left-◁-hom = right-◁-hom = ⊗-internal-hom. The whole "◁ non-symmetric, two
   homs, closure obstructed" phenomenon is a feature of NON-tiny (extensive) bases.
2. Therefore ◁-left-closedness over such a base is governed by T2's familial-representability
   criterion (Thm 1.1) VERBATIM (G(Z)=Fam(⟨Z⟩◁q,(R,M))=Fam(⟨Z⟩⊗q,(R,M))=Φ_{Q,M}(Z)).
   ⟹ ◁-closed on **Fam_fin(Vec_fd^op)** with hom [q◁−](R,M)=(R^T,(⊕_t M_{ρt}⊗Q_t^*)_ρ)
   (T2 Thm 2.3/3.2(1)); FAILS on Fam(Vec_fd^op) [∞ shapes, conjunct B] and Fam(Vec^op)
   [∞-dim positions break tininess = conjunct A = collapse itself fails].
3. **THE CROWN (opposite of T1/T2).** Non-extensivity of the linear base — the OBSTRUCTION
   to fullness (T1) and ⊗-closedness (T2) — is here the REPAIR: it collapses ◁ to the closed
   ⊗. Over extensive Set, ◁≠⊗, ◁ genuinely non-symmetric, ◁-closure FAILS while ⊗ closes.
   **Extensivity and ◁-closedness are in OPPOSITION.** Villain becomes hero.

**Neil's hint decoded.** "left Kan preserves representability, then coproducts": over rigid C,
C(M_r, Z⊗Q_t)=C(M_r⊗Q_t^*, Z) — the left adjoint (−)⊗Q_t^* preserves (co)representability —
then ∏_t of corepresentables = corepresentable at ∐_t (coproducts). Exactly T2's rigid regime,
now recognized as the ◁-closure via the collapse.

**Set nuance to include.** Over Set, ◁-closure exists iff the fixed factor q is a MONOMIAL
(single shape |T|=1): then no T^Z branching (workers "single-shape p escape"). Rigid base
lifts this to ALL q (finite corner). So rigidity trades "monomial-only" for "all q, finite S".

## 5. To verify computationally
(a) ◁ (endofunctor composition) = ⊗ over Vec_fd(F_2): dims of ⟦p◁q⟧ vs ⟦p⊗q⟧ agree.
(b) closure bijection Fam((A,X)◁q,(R,M)) ≅ Fam((A,X),(R^T,(⊕M⊗Q*))) over F_2, finite.
(c) Set: ◁≠⊗ shape counts; double-exp persists (already in workers lhd_cardinality.py).
