"""
Deep-work 2026-09-17: test the H2-cluster "product decomposition" claim.

Claim under test (PROVE.md MAIN):  for the ZS extension 1 -> D -> K -> Gamma -> 1
   H^2_cat(BK; M)  ~=  H^2(pi; M)  (+)  H^2_base(Sk_C; M)
with pi = D (fibre/vertex), Sk_C = B(Gamma) (base), [omega] in H^2(Gamma;D).

Honest rival: the abutment is the LHS spectral sequence
   E_2^{p,q} = H^p(Gamma; H^q(D;M))  ==>  H^{p+q}(K;M),
and [omega]!=0 drives the transgression d_2, so the clean (+) FAILS when [omega]!=0.

We compute over F_2 (trivial coefficients M=F_2) by the bar resolution and
compare:
   dim H^2(K;F_2)                              (true abutment)
   dim E_2^{2,0}+dim E_2^{1,1}+dim E_2^{0,2}   (naive graded / Kunneth sum)
Difference (>0) == spectral-sequence differentials are nonzero == no clean (+).
"""

import itertools
import numpy as np

def F2_rank(M):
    """rank over F_2 of a 0/1 matrix."""
    if M.size == 0:
        return 0
    A = (M % 2).astype(np.int8).copy()
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c]:
                piv = i; break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] = (A[i] + A[r]) % 2
        r += 1
        if r == rows:
            break
    return r

class Group:
    def __init__(self, elements, mul, ident):
        self.el = list(elements)
        self.idx = {g: i for i, g in enumerate(self.el)}
        self.mul = mul          # mul(a,b) -> element
        self.e = ident
        self.n = len(self.el)

def cyclic(n):
    return Group(range(n), lambda a, b: (a + b) % n, 0)

def direct(G, H):
    el = [(g, h) for g in G.el for h in H.el]
    mul = lambda a, b: (G.mul(a[0], b[0]), H.mul(a[1], b[1]))
    return Group(el, mul, (G.e, H.e))

def Q8():
    # quaternion group; elements as strings, table
    names = ['1','-1','i','-i','j','-j','k','-k']
    # represent by (sign, letter): use quaternion multiplication
    # map to matrices via {1,i,j,k} sign
    q = {'1':(1,0,0,0),'-1':(-1,0,0,0),'i':(0,1,0,0),'-i':(0,-1,0,0),
         'j':(0,0,1,0),'-j':(0,0,-1,0),'k':(0,0,1*0,1),'-k':(0,0,0,-1)}
    # fix k
    q['k']=(0,0,0,1)
    def qmul(x,y):
        a0,a1,a2,a3=x; b0,b1,b2,b3=y
        # Hamilton product
        c0=a0*b0-a1*b1-a2*b2-a3*b3
        c1=a0*b1+a1*b0+a2*b3-a3*b2
        c2=a0*b2-a1*b3+a2*b0+a3*b1
        c3=a0*b3+a1*b2-a2*b1+a3*b0
        return (c0,c1,c2,c3)
    inv={v:k for k,v in q.items()}
    mul=lambda a,b: inv[qmul(q[a],q[b])]
    return Group(names, mul, '1')

def bar_cohomology_dim(G, n):
    """dim_F2 H^n(G; F_2) trivial coefficients, via bar complex.
    C^k = functions G^k -> F_2 ; d^k: C^k -> C^{k+1}.
    (d f)(g_1..g_{k+1}) = f(g_2..g_{k+1}) + sum (-1)^i f(..g_i g_{i+1}..) + (-1)^{k+1} f(g_1..g_k)
    over F_2 signs vanish.
    """
    el = G.el
    def Ck(k):
        return list(itertools.product(range(G.n), repeat=k))  # tuples of indices
    # differential matrix from C^k to C^{k+1}
    def diff_matrix(k):
        dom = Ck(k)      # basis of C^k
        cod = Ck(k+1)
        dom_idx = {t: i for i, t in enumerate(dom)}
        M = np.zeros((len(cod), len(dom)), dtype=np.int64)
        for row, tup in enumerate(cod):  # tup length k+1
            gs = [el[i] for i in tup]
            # term 0: f(g_2..g_{k+1})
            t0 = tup[1:]
            M[row, dom_idx[t0]] += 1
            # middle terms
            for i in range(1, k+1):
                # combine g_i and g_{i+1} (1-indexed) -> indices i-1, i
                prod = G.mul(gs[i-1], gs[i])
                newt = tup[:i-1] + (G.idx[prod],) + tup[i+1:]
                M[row, dom_idx[newt]] += 1
            # last term f(g_1..g_k)
            tl = tup[:k]
            M[row, dom_idx[tl]] += 1
        return M % 2
    # H^n = ker d^n / im d^{n-1}
    dim_Cn = G.n**n
    if n == 0:
        # H^0 = F_2 (constants); ker d^0
        d0 = diff_matrix(0)  # C^0 (dim1) -> C^1
        return 1  # trivial coeff connected -> 1
    dn = diff_matrix(n)          # C^n -> C^{n+1}
    dnm1 = diff_matrix(n-1)      # C^{n-1} -> C^n
    rank_dn = F2_rank(dn)
    rank_dnm1 = F2_rank(dnm1)
    dim_ker = dim_Cn - rank_dn
    dim_im = rank_dnm1
    return dim_ker - dim_im

def H_dims(G, upto):
    return [bar_cohomology_dim(G, k) for k in range(upto+1)]

# ---- witnesses ----
Z2 = cyclic(2); Z3=cyclic(3); Z4=cyclic(4); Z6=cyclic(6)
V4 = direct(Z2, Z2)
Q = Q8()

print("H^*(G;F2) dims (k=0..3):")
for name, G in [("Z2",Z2),("Z3",Z3),("Z4",Z4),("Z6",Z6),("Z2xZ2",V4),("Q8",Q)]:
    print(f"  {name:8s}: {H_dims(G,3)}")

print()
print("=== LHS test in degree 2, trivial F2 action ===")
# For central extension w/ trivial action, E_2^{p,q}=H^p(Gamma)⊗H^q(D) so dims multiply.
def naive_deg2(Gamma, D):
    hG = H_dims(Gamma, 2)
    hD = H_dims(D, 2)
    e20 = hG[2]*hD[0]
    e11 = hG[1]*hD[1]
    e02 = hG[0]*hD[2]
    return e20, e11, e02, e20+e11+e02

cases = [
    ("Z4 = Z2.Z2 (nonsplit, [w]!=0)", Z4, Z2, Z2),
    ("Z2xZ2 = Z2.Z2 (split, [w]=0)",  V4, Z2, Z2),
    ("Q8 = (Z2)^2.Z2 (nonsplit)",     Q,  V4, Z2),
    ("Z6 = Z2.Z3 (coprime split)",    Z6, Z3, Z2),
]
for name, K, Gamma, D in cases:
    true_h2 = bar_cohomology_dim(K, 2)
    e20,e11,e02,tot = naive_deg2(Gamma, D)
    verdict = "CLEAN SUM OK" if tot==true_h2 else f"MISMATCH: SS differentials rank {tot-true_h2}"
    print(f"\n{name}")
    print(f"   dim H^2(K;F2) [true abutment] = {true_h2}")
    print(f"   E2 edges: E^2,0={e20} (base [w]) , E^1,1={e11} (cross), E^0,2={e02} (fibre pi)")
    print(f"   naive graded sum = {tot}   -->  {verdict}")

print()
print("=== Five-term exact sequence: 0->H1(G;M^D)->H1(K)->H1(D)^G --d2--> H2(G;M^D)->H2(K) ===")
print("    (trivial F2 coeffs; M^D=F2, H1(D)^G=H1(D), H2(G;M^D)=H2(G))")
print("    d2 = transgression = f |-> f_*[omega];  rank(d2) diagnoses [omega]")
for name, K, Gamma, D in cases:
    h1G = bar_cohomology_dim(Gamma,1)   # H1(Gamma;M^D)
    h1K = bar_cohomology_dim(K,1)       # H1(K)
    h1D = bar_cohomology_dim(D,1)       # H1(D)^Gamma (trivial action)
    h2G = bar_cohomology_dim(Gamma,2)   # H2(Gamma;M^D)  = base edge
    # exactness of 0->h1G->h1K->h1D--d2-->h2G->...
    # inflation H1(G)->H1(K) injective => rank = h1G
    # restriction H1(K)->H1(D)^G has image dim = h1K - h1G
    # ker(d2) = image(restriction) => rank(d2) = h1D - (h1K - h1G)
    rank_d2 = h1D - (h1K - h1G)
    surviving_base = h2G - rank_d2      # E_inf^{2,0}
    print(f"  {name}")
    print(f"     dims  H1(G)={h1G} H1(K)={h1K} H1(D)={h1D} H2(G)={h2G}")
    print(f"     rank(d2 transgression) = {rank_d2}   (0 <=> split/[w]=0 ; >0 <=> [w]!=0)")
    print(f"     E_inf^(2,0) surviving base edge = {surviving_base}")
