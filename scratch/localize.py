"""Localize the obstruction: run the bifunctor search on various object subsets
to see the minimal set of objects/morphisms where 'max' bifunctor fails."""
import itertools
from collections import defaultdict

def build(objsizes):
    morphs = []
    for dom in objsizes:
        for cod in objsizes:
            for tab in itertools.product(range(cod), repeat=dom):
                morphs.append((dom, cod, tab))
    return morphs

def ident(a): return (a,a,tuple(range(a)))
def comp(g,f):
    assert f[1]==g[0]
    return (f[0],g[1],tuple(g[2][f[2][x]] for x in range(f[0])))

def search(objsizes, objmap, limit=1):
    morphs = build(objsizes)
    byhom = defaultdict(list)
    for m in morphs: byhom[(m[0],m[1])].append(m)
    pairs = [(m1,m2) for m1 in morphs for m2 in morphs]
    def cand(m1,m2):
        return byhom[(objmap(m1[0],m2[0]), objmap(m1[1],m2[1]))]
    def cpair(q,p):
        (a1,a2)=p;(b1,b2)=q
        if a1[1]!=b1[0] or a2[1]!=b2[0]: return None
        return (comp(b1,a1),comp(b2,a2))
    def propagate(assign,newly):
        queue=list(newly)
        while queue:
            p=queue.pop(); fp=assign[p]
            for q in list(assign.keys()):
                fq=assign[q]
                for (r,val) in ((cpair(q,p), None),(cpair(p,q),None)):
                    pass
                r=cpair(q,p)
                if r is not None:
                    val=comp(fq,fp)
                    if r in assign:
                        if assign[r]!=val: return None
                    else: assign[r]=val; queue.append(r)
                r2=cpair(p,q)
                if r2 is not None:
                    val2=comp(fp,fq)
                    if r2 in assign:
                        if assign[r2]!=val2: return None
                    else: assign[r2]=val2; queue.append(r2)
        return True
    results=[]
    assign={}
    for a in objsizes:
        for b in objsizes:
            assign[(ident(a),ident(b))]=ident(objmap(a,b))
    if propagate(assign,list(assign.keys())) is None: return results
    def pick(assign):
        best=None;bn=999
        for p in pairs:
            if p not in assign:
                n=len(cand(*p))
                if n<bn: bn=n;best=p
                if n==1: break
        return best
    def bt(assign):
        if len(results)>=limit: return
        v=pick(assign)
        if v is None: results.append(dict(assign)); return
        for val in cand(*v):
            a2=dict(assign); a2[v]=val
            if propagate(a2,[v]) is not None:
                bt(a2)
                if len(results)>=limit: return
    bt(assign)
    return results

mx=lambda a,b:max(a,b)
for objs in [(1,2),(0,1,2),(0,2),(0,1),(1,),(2,),(0,1,2)]:
    r=search(objs, mx, limit=1)
    print(f"objects {objs}: max-bifunctor exists? {len(r)>0}")
