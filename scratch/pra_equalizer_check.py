"""Structural check: does (-)<|q preserve equalizers in Cont(Set)?
Equalizers in Fam(Set^op) = equalizer of SHAPES + COEQUALIZER of position sets."""
from itertools import product as iproduct

class UF:
    def __init__(s, xs): s.par={x:x for x in xs}
    def find(s,x):
        while s.par[x]!=x: s.par[x]=s.par[s.par[x]]; x=s.par[x]
        return x
    def union(s,a,b): s.par[s.find(a)]=s.find(b)

def coeq(dom, u, v):
    """coequalizer of u,v : dom -> cod (dicts). returns map cod -> representative"""
    cod = set(u.values())|set(v.values())
    return None

def equalizer(p, pp, m1, m2):
    """p=(S,P), pp=(S',P') dicts; m=(f,phi) with phi[s]: dict pos'->pos"""
    S,P = p; Sp,Pp = pp
    f,phi = m1; g,psi = m2
    E = [s for s in S if f[s]==g[s]]
    Z = {}
    for s in E:
        uf = UF(P[s])
        for b in Pp[f[s]]:
            uf.union(phi[s][b], psi[s][b])
        Z[s] = frozenset(uf.find(a) for a in P[s])
    return (E, Z)

def Lq(p, q):
    """p<|q; returns container plus the shape-decoding so we can push morphisms"""
    S,P = p; T,Q = q
    shapes=[]; pos={}
    for s in S:
        Pl = sorted(P[s])
        for cv in iproduct(T, repeat=len(Pl)):
            c = dict(zip(Pl, cv))
            sh = (s, tuple(sorted(c.items())))
            shapes.append(sh)
            pos[sh] = frozenset((a,x) for a in Pl for x in Q[c[a]])
    return (shapes,pos)

def Lq_mor(p, pp, m, q):
    """image of m : p -> pp under (-)<|q"""
    S,P=p; Sp,Pp=pp; f,phi=m; T,Q=q
    F={}; PHI={}
    Lp = Lq(p,q); Lpp = Lq(pp,q)
    for sh in Lp[0]:
        s, cit = sh; c=dict(cit)
        cc = {b: c[phi[s][b]] for b in Pp[f[s]]}
        tgt = (f[s], tuple(sorted(cc.items())))
        F[sh]=tgt
        PHI[sh]={(b,x):(phi[s][b],x) for b in Pp[f[s]] for x in Q[cc[b]]}
    return (F,PHI), Lp, Lpp

def profile(cont):
    S,P=cont
    return sorted(len(P[s]) for s in S)

# ---- example: p = (1, {a1,a2}), p' = (1,{b}), phi(b)=a1, psi(b)=a2
p  = (['s'], {'s': frozenset({'a1','a2'})})
pp = (['t'], {'t': frozenset({'b'})})
m1 = ({'s':'t'}, {'s':{'b':'a1'}})
m2 = ({'s':'t'}, {'s':{'b':'a2'}})

def run(q, p, pp, m1, m2, label):
    E = equalizer(p,pp,m1,m2)
    LE = Lq(E,q)
    M1,Lp,Lpp = Lq_mor(p,pp,m1,q)
    M2,_,_    = Lq_mor(p,pp,m2,q)
    EL = equalizer(Lp,Lpp,M1,M2)
    print(f"{label}: q={profile(q_as_cont(q))}  L(Eq)={profile(LE)}   Eq(L)={profile(EL)}   equal={profile(LE)==profile(EL)}")
    return profile(LE)==profile(EL)

def q_as_cont(q):
    T,Q=q; return (T,Q)

qs = [
  (['t0'],{'t0':frozenset()}),                                   # q = 1
  (['t0'],{'t0':frozenset({0})}),                                # q = y
  (['t0','t1'],{'t0':frozenset(),'t1':frozenset({0})}),          # q = 1+y
  (['t0','t1'],{'t0':frozenset({0,1}),'t1':frozenset({0})}),     # q = y^2+y
  (['t0','t1','t2'],{'t0':frozenset(),'t1':frozenset({0}),'t2':frozenset({0,1})}),
  ([],{}),                                                       # q = 0
]
ok=True
for i,q in enumerate(qs):
    ok &= run(q,p,pp,m1,m2,f"ex1 q#{i}")

# ---- example 2: p = (2 shapes), p' = (2 shapes), a non-injective / merging case
p2  = (['s1','s2'], {'s1':frozenset({'a','b','c'}), 's2':frozenset({'d'})})
pp2 = (['t1'], {'t1':frozenset({'x','y'})})
m1b = ({'s1':'t1','s2':'t1'}, {'s1':{'x':'a','y':'b'}, 's2':{'x':'d','y':'d'}})
m2b = ({'s1':'t1','s2':'t1'}, {'s1':{'x':'b','y':'c'}, 's2':{'x':'d','y':'d'}})
for i,q in enumerate(qs):
    ok &= run(q,p2,pp2,m1b,m2b,f"ex2 q#{i}")

# ---- example 3: shapes NOT all equalized
p3  = (['s1','s2'], {'s1':frozenset({'a','b'}), 's2':frozenset({'c'})})
pp3 = (['t1','t2'], {'t1':frozenset({'x'}), 't2':frozenset({'z'})})
m1c = ({'s1':'t1','s2':'t1'}, {'s1':{'x':'a'}, 's2':{'x':'c'}})
m2c = ({'s1':'t1','s2':'t2'}, {'s1':{'x':'b'}, 's2':{'z':'c'}})
for i,q in enumerate(qs):
    ok &= run(q,p3,pp3,m1c,m2c,f"ex3 q#{i}")
print("ALL EQUALIZERS PRESERVED:", ok)
