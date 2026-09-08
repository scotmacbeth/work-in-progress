"""Finite presheaves on a finite category D.  Brute-force but exact.
Presheaf X: dict obj -> tuple of elements; act[(arrow)] : X(cod) -> X(dom)  (contravariant)
"""
from itertools import product as iproduct

class Cat:
    def __init__(self, objs, arrows, comp):
        # arrows: name -> (dom, cod);  comp: (g,f) -> gf   for f:a->b, g:b->c
        self.objs = list(objs); self.arrows = dict(arrows); self.comp = dict(comp)
    def hom(self, a, b):
        return [n for n,(d,c) in self.arrows.items() if d==a and c==b]
    def cmp(self, g, f):
        return self.comp[(g,f)]

class PSh:
    """X.sets[obj] = tuple of elements ; X.act[arr] = dict elem_of_X(cod) -> elem_of_X(dom)"""
    def __init__(self, cat, sets, act):
        self.cat=cat; self.sets={o:tuple(s) for o,s in sets.items()}; self.act=act
    def check(self):
        C=self.cat
        for n,(d,c) in C.arrows.items():
            f=self.act[n]
            assert set(f.keys())==set(self.sets[c]), (n,'dom mismatch')
            for x in self.sets[c]: assert f[x] in self.sets[d], (n,x)
        for (g,f),gf in C.comp.items():
            # f:a->b, g:b->c  => X(gf) = X(f) o X(g) : X(c)->X(a)
            a=C.arrows[f][0]; c=C.arrows[g][1]
            for x in self.sets[c]:
                assert self.act[gf][x]==self.act[f][self.act[g][x]], ((g,f),x)
        return True
    def card(self): return {o:len(s) for o,s in self.sets.items()}

def yoneda(C,d):
    sets={c:tuple(C.hom(c,d)) for c in C.objs}
    act={}
    for n,(a,b) in C.arrows.items():
        # n: a->b ; y(d)(b)=hom(b,d) -> y(d)(a)=hom(a,d),  f |-> f o n
        act[n]={f:C.cmp(f,n) for f in sets[b]}
    return PSh(C,sets,act)

def terminal(C):
    sets={c:('*',) for c in C.objs}
    act={n:{'*':'*'} for n in C.arrows}
    return PSh(C,sets,act)

def const(C,T):
    T=tuple(T); sets={c:T for c in C.objs}; act={n:{t:t for t in T} for n in C.arrows}
    return PSh(C,sets,act)

def initial(C):
    return PSh(C,{c:() for c in C.objs},{n:{} for n in C.arrows})

def prod(X,Y):
    C=X.cat
    sets={c:tuple((x,y) for x in X.sets[c] for y in Y.sets[c]) for c in C.objs}
    act={}
    for n,(a,b) in C.arrows.items():
        act[n]={(x,y):(X.act[n][x],Y.act[n][y]) for (x,y) in sets[b]}
    return PSh(C,sets,act)

def coprod(X,Y):
    C=X.cat
    sets={c:tuple(('L',x) for x in X.sets[c])+tuple(('R',y) for y in Y.sets[c]) for c in C.objs}
    act={}
    for n,(a,b) in C.arrows.items():
        d={}
        for (tag,z) in sets[b]:
            d[(tag,z)]=(tag, X.act[n][z] if tag=='L' else Y.act[n][z])
        act[n]=d
    return PSh(C,sets,act)

def coprod_many(C, Xs):
    sets={c:tuple((i,x) for i,X in enumerate(Xs) for x in X.sets[c]) for c in C.objs}
    act={}
    for n,(a,b) in C.arrows.items():
        act[n]={(i,x):(i,Xs[i].act[n][x]) for (i,x) in sets[b]}
    return PSh(C,sets,act)

def nat(X,Y):
    """all natural transformations X->Y, as tuples of dicts keyed by object."""
    C=X.cat
    choices=[]
    objs=C.objs
    for c in objs:
        dom=X.sets[c]; cod=Y.sets[c]
        choices.append([dict(zip(dom,f)) for f in iproduct(cod,repeat=len(dom))])
    out=[]
    for combo in iproduct(*choices):
        alpha=dict(zip(objs,combo))
        ok=True
        for n,(a,b) in C.arrows.items():
            for x in X.sets[b]:
                if alpha[a][X.act[n][x]] != Y.act[n][alpha[b][x]]: ok=False;break
            if not ok: break
        if ok: out.append(tuple(sorted((c,tuple(sorted(alpha[c].items(),key=repr))) for c in objs)))
    return out

def exp(P,Q):
    """[P,Q](d) = Nat(y(d) x P, Q); restriction along n:a->b is precomposition with y(n)xP."""
    C=P.cat
    sets={}; reps={}
    for d in C.objs:
        yd=yoneda(C,d); X=prod(yd,P)
        ns=nat(X,Q)
        sets[d]=tuple(range(len(ns)))
        reps[d]=(X,ns)
    act={}
    for n,(a,b) in C.arrows.items():
        # y(n): y(a) -> y(b)  (postcompose with n).  gives map y(a)xP -> y(b)xP
        Xa,na=reps[a]; Xb,nb=reps[b]
        # component of y(n) x P at object c : (f: c->a, p) |-> (n o f, p)
        idx={al:i for i,al in enumerate(nb)}
        m={}
        for i,al in enumerate(nb):
            ald={c:dict(v) for c,v in al}
            # pull back along y(n)xP
            newal={}
            for c in C.objs:
                dd={}
                for (f,p) in Xa.sets[c]:
                    dd[(f,p)]=ald[c][(C.cmp(n,f),p)]
                newal[c]=dd
            key=tuple(sorted((c,tuple(sorted(newal[c].items(),key=repr))) for c in C.objs))
            m[i]=na.index(key)
        act[n]=m
    return PSh(C,sets,act)

def iso(X,Y):
    """brute force: is X ~= Y ?  (small only)"""
    C=X.cat
    if X.card()!=Y.card(): return False
    for al in nat(X,Y):
        ald={c:dict(v) for c,v in al}
        if all(len(set(ald[c].values()))==len(X.sets[c]) and len(X.sets[c])==len(Y.sets[c]) for c in C.objs):
            return True
    return False
