"""
◁-closedness of Workers.

Reduction (same template as ×):
  Workers_S(a◁p, q) = Cont(ΔS⊗(a◁p), q)
                    ≅ Cont(a◁p, R)          [⊗-closure, R=[ΔS,q]_⊗]
  Using Cont(c,R)=∏_{s_c}⟦R⟧(P_c(s_c)) and shapes of a◁p = (s_a,γ:P_a(s_a)→S_p),
  positions Σ_{i∈P_a s_a}P_p(γ i):
  Cont(a◁p,R) = ∏_{s_a} T(P_a(s_a)),   where
     T(A) := ∏_{γ:A→S_p} ⟦R⟧( Σ_{i∈A} P_p(γ i) ).
  So a↦Cont(a◁p,R) is representable in Cont  IFF  T is a polynomial functor
  (then H = the container with ⟦H⟧=T, and Workers ◁-closed iff H∈image[ΔS,-]).

  FIRST GATE: is T polynomial?  Polynomial functors = preserve wide pullbacks
  (Gambino–Kock). We test pullback preservation: |T(P)| vs |T(B)×_{T(D)}T(C)|.
  If unequal, T not polynomial ⟹ Cont itself is not ◁-closed at R ⟹ Workers not ◁-closed.
"""
from containers import *
from itertools import product as iproduct

# ---- a functor value ⟦R⟧(Z): list of (s_R, tuple over P_R(s_R) of elements of Z) ----
def ext_elems(R, Z):
    # Z: list of labels
    elems = []
    for sR in R.shapes:
        pos = R.fib[sR]
        for assign in iproduct(Z, repeat=len(pos)):
            elems.append((sR, dict(zip(pos, assign))))
    return elems

# ---- T(A): A a list. element = dict γ(as tuple over A of S_p-shapes) -> ⟦R⟧(TotalPos(γ)) elem ----
def totalpos(p, A, gamma):
    # gamma: dict i-> s_p ; returns list of (i, x) with x in P_p(gamma[i])
    return [ (i, x) for i in A for x in p.fib[gamma[i]] ]

def T_elems(p, R, A):
    A = list(A)
    gammas = [ dict(zip(A, g)) for g in iproduct(p.shapes, repeat=len(A)) ]
    # for each gamma, the set ⟦R⟧(totalpos)
    per = []
    for gamma in gammas:
        tp = totalpos(p, A, gamma)
        per.append(ext_elems(R, tp))
    # element of T(A) = choice of one elem per gamma
    return gammas, per

def T_card(p, R, A):
    A=list(A)
    card=1
    for g in iproduct(p.shapes, repeat=len(A)):
        gamma=dict(zip(A,g))
        tp=totalpos(p,A,gamma)
        card *= len(ext_elems(R,tp))
    return card

# ---- T on a morphism h:A->A' ----
# element e: gamma'(:A'->S_p) |-> ⟦R⟧(TotalPos_{A'}(gamma')) elem.
# (T h e)(gamma') = ⟦R⟧(sigma_h)( e(gamma'∘h) ),
#   sigma_h : TotalPos_A(gamma'∘h) -> TotalPos_{A'}(gamma'),  (i,x) |-> (h i, x).
def T_map(p, R, A, Ap, h):
    A=list(A); Ap=list(Ap)
    gammasA, perA = T_elems(p,R,A)     # domain indexing
    gammasAp, perAp = T_elems(p,R,Ap)  # not needed directly
    def apply(e):
        # e: frozen element = tuple of (gamma-key, (sR, assign-tuple)); rebuild lookup
        ed = { k:(v[0], dict(v[1])) for k,v in e }
        out = {}
        for gp in iproduct(p.shapes, repeat=len(Ap)):
            gammap = dict(zip(Ap, gp))
            gcomp = { i: gammap[h[i]] for i in A }     # gamma'∘h : A->S_p
            e_val = ed[_key(gcomp)]                      # ⟦R⟧(TotalPos_A(gcomp)) elem = (sR, assign dict)
            sR, assign = e_val
            # sigma_h: (i,x) in TotalPos_A(gcomp) -> (h i, x) in TotalPos_Ap(gammap)
            # ⟦R⟧(sigma_h): (sR, assign) -> (sR, assign' ) with assign'[posR] = sigma_h(assign[posR])
            newassign = { pr: (h[assign[pr][0]], assign[pr][1]) for pr in assign }
            out[_key(gammap)] = (sR, newassign)
        return _freeze_elem(out)
    return apply

def _key(gamma_dict):
    return tuple(sorted(gamma_dict.items()))
def _freeze_elem(d):
    # d: gamma-key -> (sR, assign dict). make hashable
    return tuple(sorted( (k,(v[0], tuple(sorted(v[1].items())))) for k,v in d.items() ))

def T_object_elements(p,R,A):
    A=list(A)
    gammas = [ dict(zip(A,g)) for g in iproduct(p.shapes, repeat=len(A)) ]
    perlists=[]
    for gamma in gammas:
        tp=totalpos(p,A,gamma)
        perlists.append([ (sR, assign) for (sR,assign) in ext_elems(R,tp) ])
    elems=[]
    for combo in iproduct(*perlists):
        d = { _key(gammas[i]): combo[i] for i in range(len(gammas)) }
        elems.append(_freeze_elem(d))
    return elems

# ============ pullback preservation test ============
def pullback_test(p, R, B, C, D, f, g):
    # cospan f:B->D, g:C->D ; P = {(b,c): f b = g c}
    P = [ (b,c) for b in B for c in C if f[b]==g[c] ]
    # projections
    pi1 = { (b,c): b for (b,c) in P }
    pi2 = { (b,c): c for (b,c) in P }
    # T on P, B, C, D
    TP = set(T_object_elements(p,R,P))
    TB = T_object_elements(p,R,B)
    TC = T_object_elements(p,R,C)
    Tf = T_map(p,R,B,D,f)
    Tg = T_map(p,R,C,D,g)
    # pullback set {(u,v): Tf u = Tg v}
    Tf_img = { id(u): Tf(u) for u in TB }
    # compute cardinalities
    fB = [ Tf(u) for u in TB ]
    gC = [ Tg(v) for v in TC ]
    from collections import Counter
    # pullback = sum over d in TD of (#preimage in TB)*(#preimage in TC)
    cB=Counter(fB); cC=Counter(gC)
    keys=set(cB)|set(cC)
    pb = sum(cB[k]*cC[k] for k in keys)
    return len(TP), pb, len(TB), len(TC)

if __name__=='__main__':
    # p = 2 shapes, 1 position each  (the interesting multi-shape case)
    p = Cont(['p0','p1'], {'p0':['x'], 'p1':['y']})
    # try several R
    Rs = {
      'y (Id)'      : Cont(['r'], {'r':['0']}),
    }
    # a genuine pullback: B=3,C=2,D=2 ; f:0->0,1->1,2->1 ; g=id
    B=['b0','b1','b2']; C=['c0','c1']; D=['d0','d1']
    f={'b0':'d0','b1':'d1','b2':'d1'}; g={'c0':'d0','c1':'d1'}
    for name,R in Rs.items():
        tp,pb,tb,tc = pullback_test(p,R,B,C,D,f,g)
        print(f"R={name:14s}: |T(P)|={tp:6d}  |T(B)x_T(D)T(C)|={pb:6d}  {'POLY-ok' if tp==pb else 'NOT POLYNOMIAL -> Cont not ◁-closed here'}")
