"""Faster: natural transformations by backtracking; isomorphism by refinement+backtracking."""
from presheaf import *
import sys
sys.setrecursionlimit(10000)

def nat_bt(X,Y,limit=None):
    """List of natural transformations X->Y as dict obj->dict."""
    C=X.cat
    items=[(c,x) for c in C.objs for x in X.sets[c]]
    # constraints: for arrow n:a->b and x in X(b): al[a][X(n)x] = Y(n)[al[b][x]]
    cons=[]
    for n,(a,b) in C.arrows.items():
        if n.startswith('id_'): continue
        for x in X.sets[b]:
            cons.append(((a,X.act[n][x]),(b,x),n))
    by_item={}
    for (tgt,src,n) in cons:
        by_item.setdefault(src,[]).append((tgt,n)); by_item.setdefault(tgt,[]).append((src,n))
    out=[]
    assign={}
    def ok(item):
        c,x=item
        for (tgt,src,n) in cons:
            if src in assign and tgt in assign:
                a=tgt[0]; 
                if assign[tgt]!=Y.act[n][assign[src]]: return False
        return True
    def rec(i):
        if limit and len(out)>=limit: return
        if i==len(items):
            out.append({c:{x:assign[(c,x)] for x in X.sets[c]} for c in C.objs}); return
        c,x=items[i]
        for v in Y.sets[c]:
            assign[(c,x)]=v
            good=True
            for (tgt,src,n) in cons:
                if src in assign and tgt in assign:
                    if assign[tgt]!=Y.act[n][assign[src]]: good=False;break
            if good: rec(i+1)
            del assign[(c,x)]
    rec(0)
    return out

def _refine(X):
    """color refinement signature per element"""
    C=X.cat
    col={(c,x):c for c in C.objs for x in X.sets[c]}
    for _ in range(len(C.objs)*4+4):
        new={}
        for c in C.objs:
            for x in X.sets[c]:
                sig=[col[(c,x)]]
                for n,(a,b) in sorted(C.arrows.items()):
                    if b==c: sig.append((n,col[(a,X.act[n][x])]))
                # incoming
                inc=[]
                for n,(a,b) in sorted(C.arrows.items()):
                    if a==c:
                        inc.append((n,tuple(sorted(str(col[(b,y)]) for y in X.sets[b] if X.act[n][y]==x))))
                new[(c,x)]=hash((tuple(sig),tuple(inc)))
        col=new
    return col

def iso_bt(X,Y):
    C=X.cat
    if X.card()!=Y.card(): return False
    cx=_refine(X); cy=_refine(Y)
    from collections import Counter
    if Counter(cx.values())!=Counter(cy.values()): return False
    items=[(c,x) for c in C.objs for x in X.sets[c]]
    assign={}; used={c:set() for c in C.objs}
    def rec(i):
        if i==len(items): return True
        c,x=items[i]
        for v in Y.sets[c]:
            if v in used[c] or cy[(c,v)]!=cx[(c,x)]: continue
            assign[(c,x)]=v; used[c].add(v)
            good=True
            for n,(a,b) in C.arrows.items():
                if b==c:
                    k=(a,X.act[n][x])
                    if k in assign and assign[k]!=Y.act[n][v]: good=False;break
                if a==c:
                    for y in X.sets[b]:
                        if X.act[n][y]==x:
                            k=(b,y)
                            if k in assign and Y.act[n][assign[k]]!=v: good=False;break
                    if not good: break
            if good and rec(i+1): return True
            del assign[(c,x)]; used[c].discard(v)
        return False
    return rec(0)

def exp2(P,Q):
    C=P.cat; sets={}; reps={}
    for d in C.objs:
        yd=yoneda(C,d); X=prod(yd,P)
        ns=nat_bt(X,Q)
        keys=[tuple(sorted((c,tuple(sorted(al[c].items(),key=repr))) for c in C.objs)) for al in ns]
        sets[d]=tuple(range(len(ns))); reps[d]=(X,ns,{k:i for i,k in enumerate(keys)})
    act={}
    for n,(a,b) in C.arrows.items():
        Xa,na,ka=reps[a]; Xb,nb,kb=reps[b]
        m={}
        for i,al in enumerate(nb):
            newal={}
            for c in C.objs:
                newal[c]={(f,p):al[c][(C.cmp(n,f),p)] for (f,p) in Xa.sets[c]}
            key=tuple(sorted((c,tuple(sorted(newal[c].items(),key=repr))) for c in C.objs))
            m[i]=ka[key]
        act[n]=m
    R=PSh(C,sets,act); R.check(); return R
