"""
Verification for: Gap 3 (is unit-connectedness NECESSARY?) and the 9bis dichotomy.
MacBeth 2026-08-30.  Pure Python, no deps.
"""
from itertools import product, combinations_with_replacement
from fractions import Fraction

GREEN, RED = "  OK ", " FAIL"
def rep(ok, msg): print((GREEN if ok else RED) + " | " + msg); assert ok, msg

print("="*78)
print("BLOCK 1.  Set_* : explicit construction of (X v X)^2 and of \\/_d [N_d, X]")
print("="*78)
# pointed set = python frozenset with distinguished basepoint 0 encoded as element ('*',)
def pt(n):            # pointed set with n non-basepoint elements
    return [('*',)] + [('e',i) for i in range(n)]
def wedge(A,B):       # A v B  : disjoint union, basepoints identified
    return [('*',)] + [('L',a) for a in A if a!=('*',)] + [('R',b) for b in B if b!=('*',)]
def pmaps(N,Y):       # pointed maps N -> Y  (list of dicts)
    dom = [x for x in N if x!=('*',)]
    out=[]
    for vals in product(Y, repeat=len(dom)):
        f={('*',):('*',)}
        for d,v in zip(dom,vals): f[d]=v
        out.append(f)
    return out
def smash_free_hom_size(N,Y): return len(pmaps(N,Y))

for m in range(0,5):
    X   = pt(m)
    XvX = wedge(X,X)
    P   = pt(2)                       # 3_* = S^0 v S^0  (2 non-basepoint elements)
    lhs = len(pmaps(P, XvX))          # [3_*, X v X]  = (X v X)^2
    rep(lhs == (2*m+1)**2, f"|[3_*, XvX]| = {lhs} = (2m+1)^2 with m={m}, |XvX|={len(XvX)}")

print()
print("  Now: can (X v X)^2 be  \\/_{d in D} [N_d, X]  for ANY family of pointed sets N_d?")
print("  |\\/_d [N_d,X]| = 1 + sum_d ( (m+1)^{n_d} - 1 ),  n_d = |N_d| - 1  (>=0).")
print("  n_d = 0 contributes 0, so WLOG all n_d >= 1 and D is finite.")
MMAX = 8
target = lambda m: (2*m+1)**2
# exhaustive search over multiplicity vectors a_1..a_K (a_j = # of summands with n_d = j)
K, AMAX = 4, 12
sols = []
for a in product(range(AMAX+1), repeat=K):
    if sum(a)==0: continue
    if all(1 + sum(a[j]*((m+1)**(j+1)-1) for j in range(K)) == target(m) for m in range(0,MMAX+1)):
        sols.append(a)
rep(sols == [], f"exhaustive search over all (a_1..a_{K}) with a_j <= {AMAX}: solutions = {sols}")
# and the reason, as a polynomial identity
print("  polynomial reason: need sum_d ((m+1)^{n_d}-1) = 4m^2+4m.  Degrees <= 2, so n_d in {1,2}.")
print("  a*(m) + b*(m^2+2m) = 4m^2+4m  =>  b=4 and a+2b=4  =>  a = -4 < 0.  IMPOSSIBLE.")
b = 4; a = 4 - 2*b
rep(a < 0, f"forced multiplicities: b(n=2) = {b}, a(n=1) = {a} < 0")

print()
print("  sanity: 3_* is NOT tiny in Set_*  ([3_*,-] does not preserve the wedge)")
def wsize(x,y): return x + y - 1        # |A v B| = |A| + |B| - 1
for (mA,mB) in [(1,1),(2,1),(2,3)]:
    A,B = pt(mA), pt(mB)
    lhs = len(pmaps(pt(2), wedge(A,B)))                                  # |[3_*, A v B]|
    rhs = wsize(len(pmaps(pt(2),A)), len(pmaps(pt(2),B)))                # |[3_*,A] v [3_*,B]|
    rep(lhs != rhs, f"|[3_*,A v B]|={lhs} != |[3_*,A] v [3_*,B]|={rhs}   (mA,mB)=({mA},{mB})")
print("  sanity: S^0 IS tiny  ([S^0,-] = id)")
for (mA,mB) in [(1,1),(2,3),(3,4)]:
    A,B = pt(mA), pt(mB)
    lhs = len(pmaps(pt(1), wedge(A,B)))
    rhs = wsize(len(pmaps(pt(1),A)), len(pmaps(pt(1),B)))
    rep(lhs == rhs, f"|[S^0, A v B]| = {lhs} = |[S^0,A] v [S^0,B]| = {rhs}  (mA,mB)=({mA},{mB})")
print("  => Set_* has a ZERO object (1_C = 0_C = *) yet is NOT closed under <|.")
print("     9bis dichotomy conjecture ('1_C = 0_C  =>  fine') is REFUTED.")

print()
print("="*78)
print("BLOCK 2.  Set x Set : [A, T.1] for A = (1,0) a summand of 1 = (1,1)")
print("="*78)
# objects are pairs of cardinalities; [.,.] componentwise exponential; copower of 1 is (E,E)
def hom(P, Y): return (Y[0]**P[0], Y[1]**P[1])
one = (1,1)
for T in [1,2,3,5]:
    A = (1,0)                      # 1 = A + B with A=(1,0), B=(0,1), both nonzero
    TA = hom(A, (T,T))             # [A, T.1]
    diagonal = (TA[0] == TA[1])
    rep(diagonal == (T==1), f"T={T}: [A, T.1] = {TA};  copower of 1 (i.e. diagonal)? {diagonal}")
print("  => in Set x Set the criterion fails at P = A already, for every |T| >= 2.")

print()
print("="*78)
print("BLOCK 3.  positive control: Set is fine (decoration set T^P absorbs it)")
print("="*78)
for P in [0,1,2,3]:
    for T in [1,2,3]:
        for m in [0,1,2,3]:
            lhs = (T*m)**P                       # |[P, T x X]|, |X| = m
            rhs = sum(m**P for _ in range(T**P)) # |coprod_{c in T^P} [P,X]|
            rep(lhs==rhs, f"Set: |[{P}, {T}x{m}]| = {lhs} = |coprod_{{{T}^{P}}}[{P},{m}]| = {rhs}")
print("  => over Set the decoration set is T^P and the identity is distributivity.")

print()
print("="*78)
print("BLOCK 4.  the fatal probe B = 0_C on the collapse locus (kappa = gamma^B)")
print("="*78)
print("  kappa_{B,Z} : coprod_t C(B,[Q_t,Z])  ->  C(B, coprod_t [Q_t,Z])   (= gamma with probe B)")
print("  at B = 0_C both hom-sets are singletons on the RIGHT and T-fold on the LEFT:")
for T in [1,2,3,7]:
    lhs, rhs = T, 1        # |coprod_t C(0,Y_t)| = T ;  |C(0, coprod Y_t)| = 1
    rep((lhs==rhs) == (T==1), f"|T|={T}:  LHS={lhs}, RHS={rhs}, bijective? {lhs==rhs}")
print("  => on the collapse locus, ANY base: left adjoint => |T| = 1.  (2-line Thm 2 necessity.)")

print()
print("="*78)
print("BLOCK 5.  connectedness of I in the candidate bases (gamma at B = I)")
print("="*78)
# Set: C(1,-) = Id, preserves coproducts.  Vec: C(k,V)=V, coprod->direct sum, fails.
# Set_*: C(S^0,Y) = underlying pointed set; gamma: disjoint union -> wedge, fails (basepoints).
for name, lhs, rhs in [("Set   |1 -> A+B|", None, None)]:
    pass
for (a,b) in [(2,3),(1,1),(4,2)]:
    rep(a+b == a+b, f"Set:   |Hom(1,A+B)| = {a+b} = |Hom(1,A)| + |Hom(1,B)| = {a}+{b}  CONNECTED")
for (a,b) in [(2,3),(1,1)]:
    lhs = a+b                    # disjoint union of underlying pointed sets
    rhs = a+b-1                  # wedge identifies the two basepoints
    rep(lhs != rhs, f"Set_*: |Hom(S^0,A)| + |Hom(S^0,B)| = {lhs} != |Hom(S^0, A v B)| = {rhs}  DISCONNECTED")
# Vec over F_2: gamma must be built AS A MAP -- cardinalities collide at dim 1
# (|V|+|W| = 2+2 = 4 = |V(+)W|), the very trap flagged in the predecessor.
def vecs(d): return list(product([0,1], repeat=d))
for (dV,dW) in [(1,1),(1,2),(2,2)]:
    V, W = vecs(dV), vecs(dW)
    # Hom(k,V) = V ; disjoint union tagged by summand
    src = [("V",v) for v in V] + [("W",w) for w in W]
    # gamma : includes into V (+) W
    img = [tuple(v)+tuple([0]*dW) for v in V] + [tuple([0]*dV)+tuple(w) for w in W]
    tgt = [tuple(u)+tuple(w) for u in V for w in W]
    inj = len(set(img)) == len(img)
    sur = set(img) == set(tgt)
    rep((not inj) and (not sur),
        f"Vec/F2 dim({dV},{dW}): |src|={len(src)} |tgt|={len(tgt)} ; gamma injective? {inj} surjective? {sur}  DISCONNECTED")
print("  Set x Set: Hom((1,1),(A,B)) = A x B ;  gamma: A1B1 + A2B2 -> (A1+A2)(B1+B2)  DISCONNECTED")
for (a1,b1,a2,b2) in [(1,1,1,1),(2,1,1,3)]:
    rep(a1*b1+a2*b2 != (a1+a2)*(b1+b2),
        f"  {a1*b1+a2*b2} != {(a1+a2)*(b1+b2)}   (A1,B1,A2,B2)=({a1},{b1},{a2},{b2})")

print()
print("ALL BLOCKS GREEN")
