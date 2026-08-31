"""
Genuine monoidal-structure search engine on a finite skeleton of FinSet.

Objects = {0,1,...,N} realized as sets range(n).  A tensor is:
  - size table  s[a][b] = |a * b|   (must be a monoid; enforced separately)
  - left action  Lact[b][m] : range(s[a][b]) -> range(s[a'][b])   for m:a->a'
  - right action Ract[a][m] : range(s[a][b]) -> range(s[a][b'])   for m:b->b'
subject to: each Lact[b], Ract[a] is a FUNCTOR; interchange; strict unit.

We enumerate actions by assigning values on a GENERATING set of FinSet-morphisms
and closing under composition (BFS), rejecting on any functoriality conflict.

Functions are tuples f with f[i] in range(cod), len(f)=dom.
Morphisms are (dom,cod,tuple).
"""
import itertools

def comp(g, f):                    # (g o f): dom f -> cod g ; f:(a,b,tf) g:(b,c,tg)
    a,b,tf=f; b2,c,tg=g
    assert b==b2
    return (a,c,tuple(tg[tf[i]] for i in range(a)))

def ident(n): return (n,n,tuple(range(n)))

def all_morphisms(N):
    """all FinSet morphisms among objects 0..N."""
    M=[]
    for a in range(N+1):
        for b in range(N+1):
            if a==0:
                M.append((0,b,()))
            elif b==0:
                pass
            else:
                for t in itertools.product(range(b),repeat=a):
                    M.append((a,b,tuple(t)))
    return M

def generators(N):
    """A generating set of FinSet|{0..N} under composition.
    For N<=3 this set generates every morphism (verified by close())."""
    G=[]
    # empty maps 0->n handled as generators 0->1 then inclusion; include 0->1:
    if N>=1: G.append((0,1,()))
    # injections k->k+1 (all strictly-increasing? we need ALL injections; use
    # coface maps + transpositions).  Simpler: include ALL injections and ALL
    # surjections between adjacent sizes, plus transpositions.
    def injs(a,b):
        res=[]
        for t in itertools.product(range(b),repeat=a):
            if len(set(t))==a: res.append((a,b,tuple(t)))
        return res
    def surjs(a,b):
        res=[]
        for t in itertools.product(range(b),repeat=a):
            if set(t)==set(range(b)): res.append((a,b,tuple(t)))
        return res
    for k in range(1,N+1):
        G+=injs(k-1,k) if k-1>=1 else []
        G+=surjs(k,k-1) if k-1>=1 else []
    # transpositions on each size
    for n in range(2,N+1):
        for i in range(n):
            for j in range(i+1,n):
                t=list(range(n)); t[i],t[j]=t[j],t[i]
                G.append((n,n,tuple(t)))
    # dedupe
    return list(dict.fromkeys(G))

def close_check_generates(N):
    """verify generators+ids close to ALL morphisms."""
    G=generators(N); allm=set(all_morphisms(N))
    have={ident(n) for n in range(N+1)} | set(G)
    changed=True
    while changed:
        changed=False
        cur=list(have)
        for f in cur:
            for g in cur:
                if f[1]==g[0]:
                    c=comp(g,f)
                    if c not in have:
                        have.add(c); changed=True
    return have>=allm, allm-have
