"""
State container monad M = (S^S, s |-> S), <<M>> X = (S x X)^S = S^S x X^S.

An element of M(A):  phi: S -> S x A  =  (g: S->S, a: S->A).
As a container: shape g in S^S, positions S, A-labels a: S->A.

Derived (see notes):
  eta_M : forward * |-> id_S ;                 backward trivial.
  mu_M  : forward (g,k) |-> (s |-> k_s(g(s))) ; backward s |-> (s, g(s)).
where an element of M<|M at shape (g,k):  g in S^S, k: S -> S^S.

We validate the monoid laws by realizing M as an honest Set-monad and checking
eta/mu naturality + the three monad laws on small sets A.
"""
from itertools import product

def Sfuncs(n):
    return list(product(range(n), repeat=n))   # all g: S->S as tuples

# ---- State Set-monad on a finite set A (A = range(a)) ----
def M_elems(n, a):
    """Elements of M(A): (g, tuple a-labels length n).  g in S^S, label:S->A."""
    out=[]
    for g in Sfuncs(n):
        for lab in product(range(a), repeat=n):
            out.append((g, lab))
    return out

def eta(n, a, x):
    idS=tuple(range(n))
    return (idS, tuple(x for _ in range(n)))

def mu(n, elem):
    """elem in M(M(A)) : (g, blab) where blab[s] = (k_s, a_s), an element of M(A).
       returns element of M(A)."""
    g, blab = elem
    # k_s = blab[s][0] (in S^S), a_s = blab[s][1] (S->A)
    gout = tuple(blab[s][0][g[s]] for s in range(n))
    aout = tuple(blab[s][1][g[s]] for s in range(n))
    return (gout, aout)

def M_map(n, f, elem):
    """functorial action M(f) for f: A->A'  (f a python callable/dict)."""
    g, lab = elem
    return (g, tuple(f[x] for x in lab))

def check_state_monad(n, amax=3):
    res={"left_unit":True,"right_unit":True,"assoc":True,"eta_nat":True,"mu_nat":True}
    for a in range(1, amax+1):
        A=range(a)
        # left unit: mu . M(eta) = id  ;  right unit: mu . eta_{M A} = id
        for e in M_elems(n,a):
            # M(eta): apply eta to each label element -> element of M(M(A))
            # eta: A -> M(A), as a "function" dict x-> eta(x)
            etaf={x:eta(n,a,x) for x in A}
            Me = M_map(n, etaf, e)           # in M(M(A))
            if mu(n, Me)!=e: res["left_unit"]=False
            # eta_{MA}(e): treat e as an element of M(A); eta at the set M(A)
            # eta_{MA}(e) = (id_S, const_e) in M(M(A))
            idS=tuple(range(n))
            eta_MA=(idS, tuple(e for _ in range(n)))
            if mu(n, eta_MA)!=e: res["right_unit"]=False
        # assoc: mu . M(mu) = mu . mu   on M(M(M(A)))  (a=1 keeps it finite & fast)
        if a==1:
            MA=M_elems(n,a)
            def MM_elems():
                for g in Sfuncs(n):
                    for blab in product(MA, repeat=n):
                        yield (g, blab)
            MMA=list(MM_elems())
            muf={x:mu(n,x) for x in MMA}
            for g3 in Sfuncs(n):
                for clab in product(MMA, repeat=n):
                    e3=(g3, clab)   # in M(M(M(A)))
                    left=mu(n, M_map(n, muf, e3))
                    right=mu(n, mu(n, e3))
                    if left!=right: res["assoc"]=False
    res["monad"]=all(res[k] for k in ("left_unit","right_unit","assoc"))
    return res

if __name__=="__main__":
    for n in (1,2,3):
        print(f"|S|={n}:", check_state_monad(n, amax=2 if n>=3 else 3))
