"""
Left adjoint to (-)<|q over Fam(Vec_fd^op).  MacBeth 2026-08-30 successor PROVE.

Encoding.  An object of Fam(Vec_fd^op) is a finite list of dimensions [d_s]_{s in S}
(a family of f.d. k-vector spaces).  Over k = F_q,
    |C(Y,X)| = q^(dim Y * dim X)
    |Fam((A,X),(B,Y))| = prod_{a in A} sum_{b in B} q^(dim Y_b * dim X_a)
(morphism = forward on shapes, BACKWARD on positions).
Day/Dirichlet tensor = substitution on the tiny locus (T4 Prop 2.1):
    p (x) q = (S x T, P_s (x) Q_t)   -> dims [ds*dt for ds in P for dt in Q]
"""
from itertools import product as iproduct
from fractions import Fraction

def hom(A, B, q):
    """|Fam((A,X),(B,Y))| with A,B lists of dims."""
    tot = 1
    for da in A:
        tot *= sum(q**(db*da) for db in B)
    return tot

def tens(P, Q):
    return [a*b for a in P for b in Q]

def prod_fam(P, Q):
    """binary product in Fam(C^op): (S x S', P_s (+) P'_s')  -> dims add"""
    return [a+b for a in P for b in Q]

# ---------------------------------------------------------------- 1. THE FALSIFIER
# Brief: C=Vec_fd, T=N, all Q_t=k, compare both sides of (dagger) at dim P = 1 and 2.
# Linear analogue of (dagger):
#     LHS  =  coprod_{t in T} C(P (x) Q_t, Z)          [ = Fam(<Z>, <P> <| q) ]
#     RHS  =  C(P, (+)_{t in T} [Q_t, Z])              [ = Fam(<Z>, F_q<P>) with naive F_q ]
# canonical map (t, f) |-> iota_t o f.
print("=== 1. THE CHEAPEST FALSIFIER (brief's RUN FIRST) ===")
print("C=Vec_fd, Q_t = k for all t, Z = k, k = F_2.  |LHS| vs |RHS| and injectivity/surjectivity")
k = 2
for T in (1,2,3,5):
    for dP in (1,2,3):
        lhs = T * k**(dP*1)                      # coprod_t C(k^dP (x) k, k) = T copies of dual
        rhs = k**(dP*T)                          # C(k^dP, k^T)
        # image of the canonical map: maps k^dP -> k^T landing in a single coordinate axis
        img = 1 + T*(k**dP - 1)                  # zero map counted once, plus nonzero ones per axis
        print(f"  |T|={T:2d} dim P={dP}:  |LHS|={lhs:5d}  |RHS|={rhs:5d}  |image|={img:5d}"
              f"   injective={lhs==img}  surjective={img==rhs}")
print("  --> fails already at dim P = 1 whenever |T|>=2; FINITENESS OF T IS IRRELEVANT.")

# ---------------------------------------------------------------- 2. NECESSITY: terminal object
print()
print("=== 2. L_q does not preserve the TERMINAL object unless |T|=1 ===")
# terminal of Fam(Vec^op) = <0> = [0]; L_q(1) = [0*dt for dt in Q] = [0]*|T|
for T in (1,2,3):
    one = [0]
    Lone = tens(one, [1]*T)
    # iso in Fam(D) <=> bijection of shape sets + isos of positions
    print(f"  |T|={T}: 1 = {one},  1<|q = {Lone},  iso? {len(one)==len(Lone)}")
    # confirm non-iso by hom-counts as a double check
    print(f"      |Fam(1<|q, 1)|={hom(Lone,one,2)}  |Fam(1, 1<|q)|={hom(one,Lone,2)}")

# ---------------------------------------------------------------- 3. NECESSITY: binary products
print()
print("=== 3. L_q does not preserve BINARY PRODUCTS unless |T|=1 (no zero objects used) ===")
for T in (1,2,3):
    Q = [1]*T
    p, pp = [1], [1]        # <k> and <k>
    a = tens(prod_fam(p,pp), Q)          # (p x p') (x) q
    b = prod_fam(tens(p,Q), tens(pp,Q))  # (p (x) q) x (p' (x) q)
    print(f"  |T|={T}: (pxp')<|q = {a}   (p<|q)x(p'<|q) = {b}   iso? {sorted(a)==sorted(b)}")

# ---------------------------------------------------------------- 4. CONTRAST: Set preserves them
print()
print("=== 4. CONTRAST over Set: (-)<|q preserves terminal and binary products ===")
def set_lhd(p, q_T, ):
    """p = list of position-set SIZES; q_T = |T|. shapes of p<|q = sum_s T^{P_s}."""
    return sum(q_T**ps for ps in p)
for T in (1,2,3):
    one = [0]   # y^0, positions empty
    print(f"  |T|={T}: shapes of 1<|q = {set_lhd(one,T)} (want 1)", end="  ")
    p, pp = [1],[2]
    # product in Fam(Set^op): positions are DISJOINT UNION
    pr = [a+b for a in p for b in pp]
    print(f"| shapes (pxp')<|q = {set_lhd(pr,T)}  vs  {set_lhd(p,T)*set_lhd(pp,T)}")

# ---------------------------------------------------------------- 5. SUFFICIENCY |T|=1
print()
print("=== 5. |T|=1: the monomial adjunction  Fam(F_Q r, p) = Fam(r, p (x) Q)  ===")
import random
random.seed(11)
bad = 0; n = 0
for _ in range(4000):
    kq = random.choice([2,3])
    R = [random.randint(0,3) for _ in range(random.randint(1,3))]   # r = (R,U)
    P = [random.randint(0,3) for _ in range(random.randint(1,3))]   # p = (S,P)
    dQ = random.randint(0,3)
    lhs = hom([u*dQ for u in R], P, kq)      # Fam(F_Q r, p),  F_Q(R,U)=(R, U (x) Q^*)
    rhs = hom(R, [ps*dQ for ps in P], kq)    # Fam(r, p (x) Q)
    n += 1
    if lhs != rhs: bad += 1
print(f"  {n-bad}/{n} agree, mismatches = {bad}")

# ---------------------------------------------------------------- 6. p.r.a. STILL HOLDS
print()
print("=== 6. p.r.a. over Vec: (L_q)_1 : Fam -> prod_T Fam  has left adjoint  coprod_t F_{Q_t} ===")
bad = 0; n = 0
for _ in range(3000):
    kq = random.choice([2,3])
    Q = [random.randint(0,3) for _ in range(random.randint(1,3))]     # q = (T,Q)
    P = [random.randint(0,3) for _ in range(random.randint(1,3))]     # p
    rs = [[random.randint(0,3) for _ in range(random.randint(1,2))] for _ in Q]  # (r_t)_t
    # LHS: hom in prod_T Fam  from (r_t) to ((L_q)_1 p)_t = (S, P_s (x) Q_t)
    lhs = 1
    for r_t, dQ in zip(rs, Q):
        lhs *= hom(r_t, [ps*dQ for ps in P], kq)
    # RHS: Fam( coprod_t F_{Q_t}(r_t), p )
    F = []
    for r_t, dQ in zip(rs, Q):
        F += [u*dQ for u in r_t]
    rhs = hom(F, P, kq)
    n += 1
    if lhs != rhs: bad += 1
print(f"  {n-bad}/{n} agree, mismatches = {bad}")

# ---------------------------------------------------------------- 7. no OTHER left adjoint
print()
print("=== 7. exhaustive: for |T|=2 is there ANY (U,N) with Fam((U,N),p) = Fam(<Z>, p(x)q) for all p? ===")
# G_Z(p) = |Fam(<Z>, p (x) q)| = sum_{s,t} k^{dP_s * dQ_t * dZ ... } careful: C(P_s (x) Q_t, Z)
def G(P, Q, dZ, kq):
    return sum(kq**(ps*qt*dZ) for ps in P for qt in Q)
def H(U, P, kq):   # |Fam((U,N),p)|, U = list of dims N_u
    return hom(U, P, kq)
kq = 2; Q = [1,1]; dZ = 1
testps = [[0],[1],[2],[0,0],[1,1],[0,1],[3],[1,2]]
found = []
for size in range(0,3):
    for U in iproduct(range(0,5), repeat=size):
        if all(G(P,Q,dZ,kq) == H(list(U),P,kq) for P in testps):
            found.append(U)
print(f"  candidates (U,N) with |U|<=2, dims<=4 matching on {len(testps)} test objects: {found}")
print("  (empty => no representing object; cf. the terminal-object argument)")

# ---------------------------------------------------------------- 8. Set x Set: <| DOES NOT EXIST
print()
print("=== 8. C = Set x Set: p <| q is not an object of Fam(C^op) ===")
# [[S,P]](X) = coprod_s [P_s, X], componentwise; the number of summands in each component
# of a family (E,N) is |E| -- the SAME for both components.  Evaluate at X = 1_C = (1,1).
# [[p<|q]](1,1) = [[p]]( (T,T) ) = (T^A, T^B).
for (A,B,T) in [(1,2,2),(1,2,3),(2,2,2),(0,1,2),(1,3,2)]:
    c1, c2 = T**A, T**B
    print(f"  p=<({A},{B})>, |T|={T}:  [[p<|q]](1,1) = ({c1},{c2})"
          f"   copower of (1,1)? {c1==c2}")
print("  --> for A != B and |T|>=2 the two components force |E|=T^A and |E|=T^B: no such family.")
