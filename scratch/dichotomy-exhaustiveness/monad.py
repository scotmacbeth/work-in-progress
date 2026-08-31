"""
Honest Reader-lifting monad checker.

Container: (S, P) with S=list of shapes, P=dict shape->list of positions (hashable).
Morphism f: (S,P)->(S',P') : f.fwd = dict s->s' ; f.bwd = dict s-> (dict/func: pos'(fwd s)->pos(s))
  (backward on positions, target->source, as a python dict keyed by target-position).

A lifting is given by:
  L_eval(Bs)      : Bs list length e of position-lists -> list of L-positions
  L_act(elt,maps) : maps list length e of dict old->new -> elt (covariant functor action)
  eps(elt)        : L-position of L([A]*e) -> element of A   (unit backward; A implicit in elt)
  delta(mm,S,P,elt): elt in pos_T[diag(mm)] -> element of pos_TT[mm]  (mult backward)
where mm=(m0,...,m_{e-1}), each m^b a tuple length e of S-shapes ; diag=(b->m^b[b]).
"""
from itertools import product

class Cont:
    def __init__(self, S, P):
        self.S=list(S); self.P={s:list(P[s]) for s in S}

class Mor:
    def __init__(self, src, tgt, fwd, bwd):
        self.src=src; self.tgt=tgt; self.fwd=fwd; self.bwd=bwd

def compose(g, f):   # g o f
    fwd={s:g.fwd[f.fwd[s]] for s in f.src.S}
    bwd={}
    for s in f.src.S:
        gs=f.fwd[s]; gbwd=g.bwd[gs]; fbwd=f.bwd[s]
        # (g o f).bwd[s]: pos_{gtgt}(fwd s) -> pos_{src}(s) = fbwd o gbwd
        bwd[s]={q: fbwd[gbwd[q]] for q in gbwd}
    return Mor(f.src, g.tgt, fwd, bwd)

def ident(cont):
    fwd={s:s for s in cont.S}
    bwd={s:{q:q for q in cont.P[s]} for s in cont.S}
    return Mor(cont,cont,fwd,bwd)

def mor_eq(f,g):
    if f.fwd!=g.fwd: return False
    for s in f.src.S:
        if f.bwd[s]!=g.bwd[s]: return False
    return True

class Lifting:
    def __init__(self, e, L_eval, L_act, eps, delta):
        self.e=e; self.L_eval=L_eval; self.L_act=L_act; self.eps=eps; self.delta=delta
    # T on objects
    def obj(self, cont):
        e=self.e
        Sh=list(product(cont.S, repeat=e))
        P={m: self.L_eval([cont.P[m[v]] for v in range(e)]) for m in Sh}
        return Cont(Sh, P)
    # T on morphisms
    def mor(self, f):
        e=self.e
        Tsrc=self.obj(f.src); Ttgt=self.obj(f.tgt)
        fwd={m: tuple(f.fwd[m[v]] for v in range(e)) for m in Tsrc.S}
        bwd={}
        for m in Tsrc.S:
            maps=[f.bwd[m[v]] for v in range(e)]   # target->source per leaf
            tm=fwd[m]
            bwd[m]={q: self.L_act(q, maps) for q in Ttgt.P[tm]}
        return Mor(Tsrc,Ttgt,fwd,bwd)
    # unit eta: cont -> T cont
    def eta(self, cont):
        e=self.e; T=self.obj(cont)
        fwd={s: tuple(s for _ in range(e)) for s in cont.S}
        bwd={}
        for s in cont.S:
            cm=fwd[s]
            bwd[s]={q: self.eps(q) for q in T.P[cm]}
        return Mor(cont,T,fwd,bwd)
    # mult mu: TT cont -> T cont
    def mu(self, cont):
        e=self.e; T=self.obj(cont); TT=self.obj(T)
        # TT.S = tuples length e of T-shapes; a T-shape is a tuple length e of S-shapes
        fwd={}; bwd={}
        for mm in TT.S:     # mm=(m^0,...,m^{e-1}), m^b in S^E
            diag=tuple(mm[b][b] for b in range(e))    # T-shape
            fwd[mm]=diag
            bwd[mm]={q: self.delta(mm, cont.S, cont.P, q) for q in T.P[diag]}
        return Mor(TT,T,fwd,bwd)

def check_monad(lift, tests):
    res={"right_unit":True,"left_unit":True,"assoc":True}
    for cont in tests:
        T=lift.obj(cont)
        eta=lift.eta(cont)
        mu=lift.mu(cont)
        # right unit: mu o eta_T = id_T   (eta at T cont), i.e. mu o eta(Tcont)
        etaT=lift.eta(T)
        ru=compose(mu, etaT)
        if not mor_eq(ru, ident(T)): res["right_unit"]=False
        # left unit: mu o T(eta) = id_T
        Teta=lift.mor(eta)
        lu=compose(mu, Teta)
        if not mor_eq(lu, ident(T)): res["left_unit"]=False
        # assoc: mu o T(mu) = mu o mu_T
        Tmu=lift.mor(mu)                 # TTT->TT
        muT=lift.mu(T)                   # TT(T)->T(T) = mu at cont T
        left=compose(mu, Tmu)            # TTT->T
        right=compose(mu, muT)           # TTT->T
        if not mor_eq(left,right): res["assoc"]=False
    res["monad"]=all(res[k] for k in ("right_unit","left_unit","assoc"))
    return res
