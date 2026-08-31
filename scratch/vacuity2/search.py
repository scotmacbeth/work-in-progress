"""
Enumerate genuine monoidal structures on skeleton {0..N} for a given size table,
then test polynomiality of R_B via the pullback-of-points comparison.
"""
import itertools, sys
from engine import comp, ident, all_morphisms, generators

def fcompose(actg, actf):
    """compose stored function-tuples: (g o f)[i] = actg[actf[i]]."""
    return tuple(actg[actf[i]] for i in range(len(actf)))

def enumerate_actions(sizes, fixed, side, N):
    """
    Enumerate functorial one-variable actions.
    side='L': left action with fixed RIGHT object b=fixed; morphism m:a->a' acts on
              dom size sizes[a][fixed] -> sizes[a'][fixed].
    side='R': right action with fixed LEFT object a=fixed; morphism m:b->b' acts on
              sizes[fixed][b] -> sizes[fixed][b'].
    Returns list of dicts: morphism -> function-tuple.
    """
    gens=generators(N)
    def domcod(m):
        x,y,t=m
        if side=='L': return sizes[x][fixed], sizes[y][fixed]
        else:         return sizes[fixed][x], sizes[fixed][y]
    # choice lists
    choice=[]
    for m in gens:
        d,c=domcod(m)
        if d==0:
            fns=[()]
        elif c==0:
            fns=[]     # no function from nonempty to empty -> action impossible
        else:
            fns=[tuple(t) for t in itertools.product(range(c),repeat=d)]
        if not fns:
            return []   # cannot realize
        choice.append((m,fns))
    results=[]
    base={}
    for n in range(N+1):
        d,_=domcod((n,n,tuple(range(n))))
        base[ident(n)]=tuple(range(d))
    allm=all_morphisms(N)
    for combo in itertools.product(*[c[1] for c in choice]):
        act=dict(base)
        ok=True
        for (m,_),fn in zip(choice,combo):
            if m in act and act[m]!=fn: ok=False;break
            act[m]=fn
        if not ok: continue
        # BFS close under composition
        conflict=False
        changed=True
        while changed and not conflict:
            changed=False
            cur=list(act.items())
            for f,af in cur:
                for g,ag in cur:
                    if f[1]==g[0]:
                        cm=comp(g,f)
                        cf=fcompose(ag,af)
                        if cm in act:
                            if act[cm]!=cf: conflict=True;break
                        else:
                            act[cm]=cf; changed=True
                if conflict: break
        if conflict: continue
        if all(m in act for m in allm):
            results.append(act)
    # dedupe
    uniq=[]; seen=set()
    for act in results:
        key=tuple(sorted((m,act[m]) for m in allm))
        if key not in seen: seen.add(key); uniq.append(act)
    return uniq

def bifunctors(sizes, u, N):
    """Yield (Lact, Ract) valid bifunctors with STRICT unit u."""
    objs=range(N+1)
    # forced strict-unit actions:
    # Lact[u][m]=m (fixed right object u; s[a][u]=a). Ract[u][m]=m.
    Lopts={}; Ropts={}
    for b in objs:
        opts=enumerate_actions(sizes,b,'L',N)
        if b==u:
            opts=[a for a in opts if all(a[m]==m[2] for m in all_morphisms(N))]
        Lopts[b]=opts
        if not opts: return
    for a in objs:
        opts=enumerate_actions(sizes,a,'R',N)
        if a==u:
            opts=[o for o in opts if all(o[m]==m[2] for m in all_morphisms(N))]
        Ropts[a]=opts
        if not opts: return
    mors=all_morphisms(N)
    # interchange: Lact[b'][f] o Ract[a][g] == Ract[a'][g] o Lact[b][f]
    # as functions range(s[a][b]) -> range(s[a'][b'])
    # backtrack over choice of Lact[b] and Ract[a]
    Lkeys=list(objs); Rkeys=list(objs)
    for Lcombo in itertools.product(*[Lopts[b] for b in Lkeys]):
        Lact={b:Lcombo[i] for i,b in enumerate(Lkeys)}
        for Rcombo in itertools.product(*[Ropts[a] for a in Rkeys]):
            Ract={a:Rcombo[i] for i,a in enumerate(Rkeys)}
            ok=True
            for f in mors:
                a,ap,tf=f
                for g in mors:
                    b,bp,tg=g
                    # domain range(s[a][b])
                    # left path: Ract[a][g]: s[a][b]->s[a][bp]; then Lact[bp][f]: s[a][bp]->s[ap][bp]
                    lhs=fcompose(Lact[bp][f], Ract[a][g])
                    rhs=fcompose(Ract[ap][g], Lact[b][f])
                    if lhs!=rhs: ok=False;break
                if not ok: break
            if ok:
                yield Lact,Ract

def poly_test(sizes, Lact, Ract, N, Bset=(1,2)):
    """R_B pullback-of-points test for each B; return dict B-> (ok, extra_count)."""
    out={}
    if N<2: return out          # pullback-of-points test needs object 2
    i0=(1,2,(0,)); i1=(1,2,(1,)); bang=(0,1,())
    for b in Bset:
        if b>N: continue
        T0=sizes[0][b]; T1=sizes[1][b]
        m0=Lact[b][i0]; m1=Lact[b][i1]        # 1*b -> 2*b
        balanced=[u for u in range(T1) if m0[u]==m1[u]]
        emb=Lact[b][bang]                       # 0*b -> 1*b
        independent=list(dict.fromkeys(emb[x] for x in range(T0)))
        extra=[u for u in balanced if u not in independent]
        # polynomial-necessary: comparison ∅*b -> balanced is a bijection
        ok=(len(balanced)==len(set(emb[x] for x in range(T0)))
            and all(u in balanced for u in (emb[x] for x in range(T0)))
            and len(set(emb[x] for x in range(T0)))==T0)
        out[b]=(ok, len(extra), balanced, independent)
    return out
