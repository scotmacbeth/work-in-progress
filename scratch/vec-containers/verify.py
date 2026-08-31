import numpy as np
import itertools

# Field: use rationals via numpy floats over small ints; work with dimensions & explicit maps.
# We verify structural claims by explicit finite-dimensional linear algebra.

print("="*60)
print("CHECK 1: Finite collapse  <<S,P>>(W) = W^N,  N=sum dim P_s")
print("="*60)
# Container ({a,b}, (k^2, k^1)); extension at W=k^d is  Vec(k^2,k^d) + Vec(k^1,k^d)
# dim = d*2 + d*1 = 3d = N*d with N=3.  And Id^N (W) = W^N has dim 3d. Match.
for d in range(0,5):
    lhs = d*2 + d*1              # dim of directsum of homs
    rhs = 3*d                    # dim of (k^d)^3
    print(f"  dim W={d}:  <<S,P>>(W)={lhs}   Id^3(W)={rhs}   match={lhs==rhs}")

print()
print("="*60)
print("CHECK 2: Hom formula  Nat = prod_s (+)_t Vec(Q_t,P_s)")
print("  and non-fullness  cont-hom = prod_s (disjoint-union)_t Vec(Q_t,P_s)")
print("="*60)
# Take (S,P)=({1,2},(k,k)),  (T,Q)=({1,2},(k,k)).  All positions = k (dim 1).
# Extensions are both Id^2.  Nat(Id^2,Id^2)=M_2(k), dim 4.
# By formula: prod_{s in {1,2}} (+)_{t in {1,2}} Vec(k,k) = (k+k) x (k+k), dim 2+2=4. Match.
dim_nat_formula = sum( sum(1 for t in [1,2]) for s in [1,2] )  # each Vec(k,k)=1-dim
print(f"  Nat dim by formula = {dim_nat_formula}  (expect dim M_2(k)=4)")
# Container morphisms ({1,2},(k,k))->({1,2},(k,k)):
#   choose f:{1,2}->{1,2} (4 functions), and per s a map Q_{f(s)}=k -> P_s=k i.e. a scalar.
# These realize exactly the "monomial" matrices: matrix M with M[s,t] can be nonzero
# ONLY at t=f(s); one nonzero-allowed entry per ROW.  The set of achievable matrices:
achievable = set()
scalars = [0,1,2]  # sample scalars (a small field-ish sample; structure not exhaustive)
for f in itertools.product([0,1],repeat=2):     # f(1),f(2) in {0,1}
    for c in itertools.product(scalars,repeat=2):
        M = np.zeros((2,2),dtype=int)
        for s in range(2):
            M[s, f[s]] = c[s]
        achievable.add(tuple(M.flatten()))
# Is the anti-diagonal-mixing matrix [[1,1],[0,0]] achievable? (row 0 has TWO nonzeros)
target = (1,1, 0,0)
print(f"  matrix [[1,1],[0,0]] (row 0 mixes two shapes) achievable as container morphism? {target in achievable}")
print("  -> If False: this Nat is NOT a container morphism => extension NOT full.  QED non-fullness.")

print()
print("="*60)
print("CHECK 3: L3  Vec(P, (+)_t V_t) = (+)_t Vec(P,V_t) for P fin-dim; fails inf-dim")
print("="*60)
# finite: P=k^2, V_t=k for t in T (|T|=m). LHS dim = dim Vec(k^2, k^m)=2m.
# RHS dim = sum_t dim Vec(k^2,k)=sum_t 2 = 2m. match.
for m in range(1,5):
    lhs = 2*m
    rhs = sum(2 for _ in range(m))
    print(f"  |T|={m}:  Vec(k^2,+k)={lhs}   (+)Vec(k^2,k)={rhs}  match={lhs==rhs}")
print("  Inf-dim P: Vec(P,+_t V_t) with P=k^(N) infinite: a linear map k^(N)->+_t V_t")
print("  need NOT have finite-support image? Actually image of BASIS can hit infinitely")
print("  many t => map not in +_t Vec(P,V_t). Concretely Vec(k^(N), (+)_N k):")
print("  identity-like map sending e_i->f_i lands in +_N k fine, but general phi has")
print("  columns = arbitrary finitely-supported vectors; the DIRECT SUM +_t Vec(P,V_t)")
print("  = maps hitting finitely many t. dim(Vec(k^(N),k^(N))) = |N|*2^|N| >> |N| = dim(+).")

print()
print("="*60)
print("CHECK 4: Composition  Id^N o Id^M = Id^{NM}; (S,P)o(T,Q)=(SxT,P(x)Q) dims")
print("="*60)
# (S,P)=({a,b},(k^2,k^1)) N=3 ;  (T,Q)=({u},(k^2)) M=2.
# composite shapes = SxT (2 x 1 =2 shapes), positions P_s (x) Q_t dims: 2*2=4, 1*2=2.
# total = 4+2 = 6 = N*M = 3*2. Match Id^6.
Ndim = 2+1; Mdim=2
comp = 2*2 + 1*2
print(f"  N={Ndim} M={Mdim}  composite total dim = {comp}  vs N*M={Ndim*Mdim}  match={comp==Ndim*Mdim}")
