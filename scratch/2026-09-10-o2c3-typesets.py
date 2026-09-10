#!/usr/bin/env python3
"""
Part 4: molecule TYPE-SET comparison  T_{MoM}  vs  T_{LoM}  at arity m (m<=4)
for O_{2,C3}.

T_{MoM} = { S_m-conj class of Stab(w) : w a two-level O_{2,C3} tree on [m] }.
T_{LoM} = Young products (block-diagonal, distinguishable blocks, NO inter-block swaps)
          of single-O_{2,C3}-tree Auts over set partitions of [m]  (L = list container, polynomial).

Escape iff  T_{MoM}  contains a type ABSENT from T_{LoM}.
For pure C_3 they coincided (no escape).  For S_3 the escape Delta_{C2} appeared at m=4.
Question: which happens for the hybrid O_{2,C3}?
"""
import itertools, os, sys, importlib.util
from collections import Counter
d=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,d)
spec=importlib.util.spec_from_file_location("o2c3model",os.path.join(d,"2026-09-10-o2c3-model.py"))
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
canon,aut,ocanon,oaut,show,conj_key=mod.canon,mod.aut,mod.ocanon,mod.oaut,mod.show,mod.conj_key
L,U,P,Mu,Om=mod.L,mod.U,mod.P,mod.Mu,mod.Om
OL,OU,OMu,OOm=mod.OL,mod.OU,mod.OMu,mod.OOm

# ---- single inner O-trees on EXACTLY label-set S (leaves+units+mu/omega nodes) ----
_memo={}
def inner_trees(S, depth):
    S=frozenset(S); key=(S,depth)
    if key in _memo: return _memo[key]
    res=set()
    if len(S)==1:
        (a,)=tuple(S); res.add(L(a))
    if depth>0 and len(S)>=1:
        items=sorted(S)
        for arity,Node in ((2,Mu),(3,Om)):
            for assign in itertools.product(range(arity),repeat=len(items)):
                slots=[[] for _ in range(arity)]
                for it,sl in zip(items,assign): slots[sl].append(it)
                choice=[]; ok=True
                for sl in slots:
                    if not sl: choice.append([U])
                    else:
                        sub=inner_trees(frozenset(sl),depth-1)
                        if not sub: ok=False;break
                        choice.append(list(sub))
                if not ok: continue
                for combo in itertools.product(*choice):
                    res.add(canon(Node(*combo)))
    _memo[key]=res
    return res

# ---- two-level outer trees on EXACTLY [m], bounded outer depth & pegs ----
def set_partitions(s):
    s=list(s)
    if not s: yield []; return
    first=s[0]
    for rest in set_partitions(s[1:]):
        for i in range(len(rest)):
            yield rest[:i]+[[first]+rest[i]]+rest[i+1:]
        yield [[first]]+rest

def outer_trees(m, outer_depth, inner_depth, max_pegs):
    labels=list(range(m))
    subtrees={}
    for r in range(1,m+1):
        for sub in itertools.combinations(labels,r):
            subtrees[frozenset(sub)]=list(inner_trees(frozenset(sub),inner_depth))
    peg=OL(U)
    def build_outer(leaves, depth):
        res=set(); n=len(leaves)
        if n==1:
            res.add(ocanon(leaves[0])); return res
        if depth<=0: return res
        for arity,Node in ((2,OMu),(3,OOm)):
            for assign in itertools.product(range(arity),repeat=n):
                groups=[[] for _ in range(arity)]
                for i,a in enumerate(assign): groups[a].append(leaves[i])
                choice=[]; ok=True
                for g in groups:
                    if not g: choice.append([OU])
                    elif len(g)==1: choice.append([ocanon(g[0])])
                    else:
                        sub=build_outer(g,depth-1)
                        if not sub: ok=False;break
                        choice.append(list(sub))
                if not ok: continue
                for combo in itertools.product(*choice):
                    res.add(ocanon(Node(*combo)))
        return res
    results=set()
    for part in set_partitions(labels):
        block_choices=[[OL(t) for t in subtrees[frozenset(b)]] for b in part]
        for npg in range(0,max_pegs+1):
            for leaves in itertools.product(*block_choices):
                lm=list(leaves)+[peg]*npg
                if not lm: continue
                for ot in build_outer(lm, outer_depth):
                    results.add(ot)
    return results

# ---- L o M : Young products of single-tree Auts over set partitions ----
def young_products(m, depth):
    labels=list(range(m))
    auts_on={}
    for r in range(1,m+1):
        for sub in itertools.combinations(labels,r):
            sub=frozenset(sub); sl=sorted(sub); idx={b:i for i,b in enumerate(sl)}
            groups=[]
            for t in inner_trees(sub,depth):
                def rel(tt):
                    tag=tt[0]
                    if tag=='L': return ('L',idx[tt[1]])
                    if tag in ('U','P'): return tt
                    return (tag,tuple(rel(k) for k in tt[1]))
                G=aut(rel(t),r); groups.append((sl,G))
            auts_on[sub]=groups
    types=set()
    for part in set_partitions(labels):
        blocks=[frozenset(b) for b in part]
        for combo in itertools.product(*[auts_on[b] for b in blocks]):
            factorsets=[]
            for (sl,G) in combo:
                fs=[]
                for g in G:
                    p=list(range(m))
                    for i,b in enumerate(sl): p[b]=sl[g[i]]
                    fs.append(tuple(p))
                factorsets.append(fs)
            prod=set()
            for elt in itertools.product(*factorsets):
                p=list(range(m))
                for q in elt: p=[q[p[i]] for i in range(m)]
                prod.add(tuple(p))
            types.add(conj_key(prod,m))
    return types

if __name__=='__main__':
    for m in [2,3,4]:
        od = 3 if m<=3 else 2
        idp= 3 if m<=3 else 2
        mp = 3 if m<=3 else 2
        outers=outer_trees(m, outer_depth=od, inner_depth=idp, max_pegs=mp)
        T_A={}
        for t in outers:
            G=oaut(t,m); T_A.setdefault(conj_key(G,m),t)
        T_L=young_products(m, depth=(3 if m<=3 else 2))
        A=set(T_A)
        onlyA=A-T_L; onlyL=T_L-A
        print(f"\nm={m}: |outers|={len(outers)}  |T_A(MoM)|={len(A)}  |T_L(LoM)|={len(T_L)}")
        print(f"  ESCAPES (in MoM, NOT in LoM  => necessity HOLDS): {len(onlyA)}")
        for k in sorted(onlyA):
            print(f"     order={k[0]}  cyc={k[1]}")
            print(f"       witness Stab = {show(oaut(T_A[k],m))}")
        print(f"  in LoM but not enumerated in MoM (peg/depth truncation): {len(onlyL)}")
        for k in sorted(onlyL)[:6]:
            print(f"     order={k[0]}  cyc={k[1]}")
