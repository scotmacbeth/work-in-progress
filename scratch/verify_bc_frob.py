"""
Beck-Chevalley and Frobenius reciprocity in Set (codomain fibration).
Reuse the Set/B machinery.  Then the container-logic versions are the fibrewise op
(formal: op preserves iso, reverses adjunctions, swaps product<->coproduct).
"""
from itertools import product

def all_functions(dom, cod):
    cod=list(cod)
    for vals in product(cod, repeat=len(dom)):
        yield {a:v for a,v in zip(dom,vals)}

class SliceObj:
    def __init__(self,A,f): self.A=tuple(A); self.f=dict(f)
    def __repr__(self): return f"({list(self.A)}->{[self.f[a] for a in self.A]})"

def Sigma(f,obj):  # postcompose ; obj over X, f:X->Y  -> over Y
    return SliceObj(obj.A, {a: f[obj.f[a]] for a in obj.A})

def pull(f,obj):
    """f^*: obj over Y (obj.f:C->Y), f:X->Y -> object over X.
       P={(x,c): f(x)=obj.f(c)}, map->X = x. also return proj to C."""
    P=[]; toX={}; toC={}
    Xset=list(f.keys())
    for x in Xset:
        for c in obj.A:
            if f[x]==obj.f[c]:
                e=(x,c); P.append(e); toX[e]=x; toC[e]=c
    return SliceObj(P,toX), toC

def Pi(f,obj,Y):
    """Pi_f: obj over X -> over Y. fibre over y = sections of f^{-1}(y)->A."""
    tot=[]; toY={}
    for y in Y:
        fibX=[x for x in f if f[x]==y]
        if not fibX:
            e=(y,()); tot.append(e); toY[e]=y; continue
        choices=[[a for a in obj.A if obj.f[a]==x] for x in fibX]
        for combo in product(*choices):
            e=(y, tuple(zip(fibX,combo))); tot.append(e); toY[e]=y
    return SliceObj(tot,toY)

def slice_iso(o1,o2):
    """are o1,o2 isomorphic in Set/base? (bijection A1<->A2 commuting with maps to base)"""
    if len(o1.A)!=len(o2.A): return False
    # need bijection respecting fibres: for each base elt, fibre sizes equal
    from collections import Counter
    if Counter(o1.f[a] for a in o1.A)!=Counter(o2.f[a] for a in o2.A): return False
    return True  # for finite sets, equal fibre-size profile over base => iso in Set/base

def gen(B,maxA=2):
    pool=('p','q','r','s')
    out=[]
    for n in range(0,maxA+1):
        A=pool[:n]
        for f in all_functions(A,B): out.append(SliceObj(A,f))
    return out

# ---------------- Beck-Chevalley ----------------
# Pullback square:
#    P --k--> C
#    |        |
#   h|        |g
#    v        v
#    A --f--> B
# BC-Sigma:  f^* Sigma_g  ~=  Sigma_h k^*   : Set/C -> Set/A
# BC-Pi:     f^* Pi_g      ~=  Pi_h k^*
def build_pullback(f, g):
    """f:A->B, g:C->B dicts. Return P set, h:P->A, k:P->C."""
    A=list(f.keys()); C=list(g.keys())
    P=[]; h={}; k={}
    for a in A:
        for c in C:
            if f[a]==g[c]:
                e=(a,c); P.append(e); h[e]=a; k[e]=c
    return P,h,k

def test_BC():
    # choose f:A->B, g:C->B
    cases=[
        ({'a1':'b1','a2':'b2'}, {'c1':'b1','c2':'b1','c3':'b2'}, ('b1','b2')),
        ({'a1':'b1','a2':'b1','a3':'b2'}, {'c1':'b1','c2':'b2'}, ('b1','b2','b3')),  # non-surj into B
    ]
    allok=True
    for f,g,B in cases:
        A=tuple(f.keys()); C=tuple(g.keys())
        P,h,k=build_pullback(f,g)
        hmap=SliceObj(P,h)  # P->A  (as object over A? h:P->A)
        # We need functors:
        #   Sigma_g: Set/C->Set/B ;  f^*: Set/B->Set/A
        #   k^*: Set/C->Set/P ; Sigma_h: Set/P->Set/A ; Pi_h: Set/P->Set/A ; Pi_g: Set/C->Set/B
        okS=okP=True
        for obj in gen(C,maxA=2):           # object over C
            # LHS_Sigma = f^*(Sigma_g(obj))
            lhsS=pull(f, Sigma(g,obj))[0]
            # RHS_Sigma = Sigma_h(k^*(obj))
            kstar=pull({e:k[e] for e in P}, obj)[0]      # over P (k:P->C)
            rhsS=Sigma({e:h[e] for e in P}, kstar)        # Sigma_h : over P -> over A
            if not slice_iso(lhsS, rhsS): okS=False; print("  BC-Sigma FAIL", obj, lhsS, rhsS)
            # Pi version
            lhsP=pull(f, Pi(g,obj,B))[0]
            rhsP=Pi({e:h[e] for e in P}, kstar, A)
            if not slice_iso(lhsP, rhsP): okP=False; print("  BC-Pi FAIL", obj, lhsP, rhsP)
        print(f"[{'OK' if okS else 'FAIL'}] Beck-Chevalley (Sigma)   f={f} g={g}")
        print(f"[{'OK' if okP else 'FAIL'}] Beck-Chevalley (Pi)      f={f} g={g}")
        allok = allok and okS and okP
    return allok

# ---------------- Frobenius ----------------
# Sigma_f -| f^* , f:X->Y.  Frobenius:  Sigma_f(phi x_X f^* psi) ~= Sigma_f(phi) x_Y psi
# x_X = product in Set/X = fibre product over X.
def slice_prod(o1,o2):
    """product in Set/base of o1,o2 (both over same base): pullback over base."""
    P=[]; m={}
    for a in o1.A:
        for b in o2.A:
            if o1.f[a]==o2.f[b]:
                e=(a,b); P.append(e); m[e]=o1.f[a]
    return SliceObj(P,m)

def test_Frobenius():
    cases=[
        ({'x1':'y1','x2':'y1','x3':'y2'}, ('y1','y2')),
        ({'x1':'y1','x2':'y2','x3':'y3'}, ('y1','y2','y3')),
    ]
    allok=True
    for f,Y in cases:
        X=tuple(f.keys())
        ok=True
        for phi in gen(X,maxA=2):        # over X
            for psi in gen(Y,maxA=2):    # over Y
                fstar_psi=pull(f,psi)[0]                      # over X
                lhs=Sigma(f, slice_prod(phi, fstar_psi))     # over Y
                rhs=slice_prod(Sigma(f,phi), psi)            # over Y
                if not slice_iso(lhs,rhs):
                    ok=False; print("  Frob FAIL", phi, psi, lhs, rhs)
        print(f"[{'OK' if ok else 'FAIL'}] Frobenius (Sigma_f)   f={f}")
        allok=allok and ok
    return allok

if __name__=="__main__":
    print("--- Beck-Chevalley ---")
    bc=test_BC()
    print("--- Frobenius ---")
    fr=test_Frobenius()
    print("\nALL:", "OK" if (bc and fr) else "FAIL")
