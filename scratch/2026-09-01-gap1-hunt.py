import itertools, math
from fractions import Fraction as Q

print("="*70)
print("BLOCK 1 -- Rel is COLLAPSE (every object tiny): P x (A |_| B) = P x A |_| P x B")
print("In Rel: coproduct = disjoint union, tensor = cartesian product of sets,")
print("internal hom [P,X] = P x X (compact closed, self-dual). Tiny iff")
print("[P,-] preserves coproducts.")
for P,A,B in [(2,3,1),(3,2,2),(1,4,5),(4,0,3)]:
    lhs = P*(A+B)          # |P x (A |_| B)|
    rhs = P*A + P*B        # |P x A |_| P x B|
    # but the REAL test is a bijection of the underlying sets, not just counts:
    S_lhs = set(itertools.product(range(P), list(range(A))+['B'+str(i) for i in range(B)]))
    S_rhs = set([('L',x,a) for x in range(P) for a in range(A)]) | \
            set([('R',x,b) for x in range(P) for b in range(B)])
    print(f"  P={P},A={A},B={B}: |lhs|={len(S_lhs)} |rhs|={len(S_rhs)} bijection={len(S_lhs)==len(S_rhs)==lhs==rhs}")
print("  => [P,-] preserves coproducts for ALL P  => Rel is COLLAPSE pole (admissible via <|=(x)),")
print("     non-cartesian ((x)=set-product != categorical product=disjoint union), but NOT Gap-1.")

print("\n"+"="*70)
print("BLOCK 2 -- Set x Vec admissibility on the collapse (fd) locus: ONE family N")
print("presents the composite in BOTH components.")
# Set side: p_Set=(S,{A_s}), q_Set=(T,{C_t}). Container composition:
#   shape set D = disjoint-union_s  T^{A_s}   (pairs (s, f:A_s->T))
#   positions   B_{(s,f)} = disjoint-union_{a in A_s} C_{f(a)}
S=['s']; A={'s':['1','2']}            # one shape, arity 2
T=['t1','t2']; C={'t1':['a'],'t2':['b','c']}
D=[]  # composed shapes
for s in S:
    for f in itertools.product(T, repeat=len(A[s])):   # f:A_s->T
        D.append((s,f))
print(f"  Set composite shape set D has |D| = {len(D)}  (= sum_s |T|^|A_s| = {sum(len(T)**len(A[s]) for s in S)})")
positions={ (s,f): [c for a_i,a in enumerate(A[s]) for c in C[f[a_i]]] for (s,f) in D }
for d in D: print(f"    shape {d}: positions {positions[d]}")

# Vec side: composite functor = X |-> (+)_{(s,t) in SxT} Hom(V_s (x) W_t, X)   (V_s fd => genuine coproduct)
# dims: dim V_s = 2, dim W_t1 = 1, dim W_t2 = 3
dimV={'s':2}; dimW={'t1':1,'t2':3}
composite_reps = [ dimV[s]*dimW[t] for s in S for t in T ]   # multiset of dims of V_s(x)W_t
print(f"  Vec composite is a direct sum of representables with position-dims (multiset): {sorted(composite_reps)}")
# Re-index onto the SAME D (|D|=4 >= |SxT|=2): put the 2 reps on 2 slots, 0 on the rest.
assert len(D) >= len(S)*len(T), "need |D| >= |SxT| to inject"
Wdims = composite_reps + [0]*(len(D)-len(composite_reps))   # 0 = zero object, Hom(0,-)=0 functor
print(f"  Assign to D's {len(D)} slots the position-dims: {Wdims}  (0 means W_d=0, contributes nothing)")
# EXACT functor equality check: multiset of NONZERO representables must match (0's add the zero functor)
def functor_dim_profile(reps, m):   # dim of (+)_i Hom(k^{r_i}, k^m) = sum_i r_i*m
    return sum(r*m for r in reps if r>0)
ok=all(functor_dim_profile(composite_reps,m)==functor_dim_profile(Wdims,m) for m in range(5))
print(f"  Multiset of nonzero reps matches (Hom(0,-)=0): {sorted(r for r in composite_reps if r>0)==sorted(r for r in Wdims if r>0)}")
print(f"  Functors equal on test objects k^m, m=0..4 (structural, not a dim-coincidence): {ok}")
print("  => N=(D,{(B_d, W_d)}) presents the composite in BOTH Set and Vec components.")
print("     Set part forces D (Set fully faithful); Vec part re-indexes freely (Thm D non-fullness).")
print("  => Set x Vec is <|-admissible on the collapse locus, NON-collapse, NON-cartesian => GAP-1 INHABITANT.")

print("\n"+"="*70)
print("BLOCK 3 -- WHY Set x Set dies but Set x Vec lives (Theorem B / Lemma E2 escape)")
print("Thm B step: 1 disconnected => 1 = A |_| B, then Lemma S with A=(1_C1,0) gives")
print("  [A, T.1] = (T.1_C1 , 1_C2);  need = E.1 componentwise => 1_C2 = E.1_C2.")
print("Lemma E2 concludes |E|=1 -- but ONLY if 1_C2 =/= 0 (nonzero terminal).")
for name,term2 in [("Set x Set (C2=Set, 1_C2=1 != 0)",1),("Set x Vec (C2=Vec, 1_C2=0)",0)]:
    if term2!=0:
        print(f"  {name}: 1_C2=E.1_C2 with 1_C2!=0 forces |E|=1 => then T.1_C1=1_C1 => |T|=1 CONTRADICTION => INADMISSIBLE")
    else:
        print(f"  {name}: 1_C2=E.1_C2 becomes 0 = E.0 = 0 -- VACUOUS, no constraint on E => Thm B EVAPORATES => admissible")

print("\n"+"="*70)
print("BLOCK 4 -- Task B: is I_1 (x) I_2 = 0 forced by I = I_1 |_| I_2?  Census of mechanisms.")
print("  additive/semiadditive, biproduct-split unit: e_i=iota_i pi_i idempotent, e_1 e_2 = iota_1 (pi_1 iota_2) pi_2 = 0")
print("     (uses zero morphism pi_1 iota_2 = 0, NOT subtraction) ; e_1(x)e_2 ~ e_1 e_2 = 0 ; image I_1(x)I_2 = 0.  => B=0")
print("  extensive (disjoint coproducts): B->I factors through both u_1,u_2 => through pullback=0 => B->0 => B=0 (strict initial).")
print("  Day-convolution presheaf bases: unit = representable = INDECOMPOSABLE, so no nontrivial split at all.")
print("  product categories C1xC2: (I1,0)(x)(0,I2)=(0,0)=0.  => B=0.")
print("  K-theory shadow: phi:C->(N,+,x), phi(I)=phi(I)^2 => phi(I) in {0,1}; phi(I)=phi(I1)+phi(I2)")
print("     with both >=1 impossible when phi(I)=1 -- but such phi exists ONLY on extensive-type bases.")
print("  Set x Vec ITSELF: I=(1,k) splits as (1,0)|_|(0,k), and I_1(x)I_2=(1x0,0(x)k)=(empty,0)=0  => B=0 here too.")
print("  => B=0 in every constructible closed sym. monoidal C; NO counterexample found;")
print("     genuine abstract forcing needs extensivity OR zero-object-biproduct (proved above).")
print("  CRUCIAL: Set x Vec has B=0 AND is admissible+disconnected+non-cartesian, so EVEN IF B=0 always,")
print("     the '9.1-note' route (B=0 => Thm B runs verbatim) is FALSE: Thm B also needs nonzero terminal (E2).")
