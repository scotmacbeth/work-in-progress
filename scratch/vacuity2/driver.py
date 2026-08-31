"""
Driver: sweep all size tables on skeleton {0..N}, enumerate genuine bifunctors
(strict unit), test polynomiality of R_B.  Report non-polynomial survivors; for
those, search for a natural associator (pentagon+triangle) to certify monoidal.
"""
import itertools, sys, time
from engine import all_morphisms, ident, comp, generators
from search import enumerate_actions, bifunctors, poly_test, fcompose

def size_tables(N):
    """all monoid size tables on {0..N} with a strict identity u in 0..N."""
    vals=list(range(N+1))
    out=[]
    for u in vals:
        others=[x for x in vals if x!=u]
        cells=[(a,b) for a in others for b in others]
        for assign in itertools.product(vals,repeat=len(cells)):
            s={a:{b:None for b in vals} for a in vals}
            for x in vals:
                s[u][x]=x; s[x][u]=x
            for (a,b),v in zip(cells,assign):
                s[a][b]=v
            # associativity
            ok=all(s[s[a][b]][c]==s[a][s[b][c]] for a in vals for b in vals for c in vals)
            if ok:
                out.append((u,s))
    return out

def assoc_exists(sizes,Lact,Ract,u,N):
    """search a natural associator with pentagon+triangle (strict unit)."""
    objs=list(range(N+1))
    mors=all_morphisms(N)
    # size of (a*b)*c and a*(b*c) equal by monoid assoc
    def L3(a,b,c): return sizes[sizes[a][b]][c]
    triples=[(a,b,c) for a in objs for b in objs for c in objs]
    # candidate bijections per triple; forced identity if any coord==u (strict unit)
    cand={}
    for (a,b,c) in triples:
        n=L3(a,b,c)
        if a==u or b==u or c==u:
            cand[(a,b,c)]=[tuple(range(n))]
        else:
            cand[(a,b,c)]=[p for p in itertools.permutations(range(n))]
    # naturality: for morphism triple (f:a->a',g:b->b',h:c->c'),
    #   alpha_{a',b',c'} o ((f*g)*h) == (f*(g*h)) o alpha_{a,b,c}
    # We build the functor actions on objects from Lact/Ract:
    #   (X*Y) as bifunctor:  morphism (p:X->X', q:Y->Y') acts by
    #       Lact[Y'][p] o Ract[X][q]
    def bimap(p,q):
        X,Xp,_=p; Y,Yp,_=q
        return fcompose(Lact[Yp][p], Ract[X][q])
    # ((f*g)*h): apply inner (f*g) then outer with h
    def outer_left(f,g,h):
        fg=comp_bi(f,g)                 # morphism (a*b)->(a'*b') as a FinSet map
        return bimap(fg,h)
    def outer_right(f,g,h):
        gh=comp_bi(g,h)
        return bimap(f,gh)
    def comp_bi(p,q):
        """the FinSet morphism p*q : (X*Y)->(X'*Y') realized by bimap, as a (dom,cod,tuple)."""
        X,Xp,_=p; Y,Yp,_=q
        t=bimap(p,q)
        return (sizes[X][Y], sizes[Xp][Yp], t)
    # backtracking assignment over triples with naturality pruning
    order=[t for t in triples if not (t[0]==u or t[1]==u or t[2]==u)]
    assign={t:cand[t][0] for t in triples if (t[0]==u or t[1]==u or t[2]==u)}
    def nat_ok(t):
        a,b,c=t
        al=assign[t]
        # for all morphisms out of (a,b,c)
        for f in mors:
            if f[0]!=a: continue
            for g in mors:
                if g[0]!=b: continue
                for h in mors:
                    if h[0]!=c: continue
                    tp=(f[1],g[1],h[1])
                    if tp not in assign: continue
                    ar=assign[tp]
                    # left: ar o ((f*g)*h)
                    L=fcompose(ar, outer_left(f,g,h))
                    R=fcompose(outer_right(f,g,h), al)
                    if L!=R: return False
        # also morphisms INTO (a,b,c)
        for f in mors:
            if f[1]!=a: continue
            for g in mors:
                if g[1]!=b: continue
                for h in mors:
                    if h[1]!=c: continue
                    tp=(f[0],g[0],h[0])
                    if tp not in assign: continue
                    ar=assign[tp]
                    L=fcompose(al, outer_left(f,g,h))
                    R=fcompose(outer_right(f,g,h), ar)
                    if L!=R: return False
        return True
    def pentagon_ok():
        # ((ab)c)d :  alpha_{ab,c,d} then alpha_{a,b,cd} == (a x alpha_{b,c,d}); alpha_{a,bc,d}; (alpha_{a,b,c} x d)
        for a in objs:
          for b in objs:
            for c in objs:
              for d in objs:
                # sizes
                n=sizes[sizes[sizes[a][b]][c]][d]
                # path1: alpha_{(a*b),c,d} then alpha_{a,b,(c*d)}
                A1=assign[(sizes[a][b],c,d)]
                A2=assign[(a,b,sizes[c][d])]
                p1=fcompose(A2,A1)
                # path2: (a x alpha_{b,c,d}) ; alpha_{a,(b*c),d} ; (alpha_{a,b,c} x d)
                # (alpha_{a,b,c} x d): bimap of (morphism alpha as map (ab)c->a(bc)) tensor id_d
                al_abc=assign[(a,b,c)]
                map_abc=(sizes[sizes[a][b]][c], sizes[a][sizes[b][c]], al_abc)
                idd=ident(d)
                q1=bimap(map_abc, idd)
                A3=assign[(a,sizes[b][c],d)]
                al_bcd=assign[(b,c,d)]
                map_bcd=(sizes[sizes[b][c]][d], sizes[b][sizes[c][d]], al_bcd)
                ida=ident(a)
                q3=bimap(ida, map_bcd)
                p2=fcompose(q3, fcompose(A3, q1))
                if p1!=p2: return False
        return True
    def rec(i):
        if i==len(order):
            return pentagon_ok()
        t=order[i]
        for p in cand[t]:
            assign[t]=p
            if nat_ok(t):
                if rec(i+1): return True
            del assign[t]
        return False
    return rec(0)

def sweep(N, report_all_monoidal=False, time_budget=1e9):
    t0=time.time()
    tables=size_tables(N)
    n_tables=len(tables)
    n_bifun=0; n_monoidal=0; nonpoly=[]; unit_cards=set()
    covered=0
    for (u,s) in tables:
        if time.time()-t0>time_budget:
            break
        covered+=1
        for Lact,Ract in bifunctors(s,u,N):
            n_bifun+=1
            pt=poly_test(s,Lact,Ract,N)
            allpoly=all(v[0] for v in pt.values())
            if not allpoly:
                # candidate non-poly bifunctor; check monoidal (associator)
                if assoc_exists(s,Lact,Ract,u,N):
                    n_monoidal+=1
                    unit_cards.add(u)
                    nonpoly.append((u,s,Lact,Ract,pt))
                # even if not monoidal, note it
            else:
                # polynomial bifunctor; count monoidal ones for unit-card evidence
                if report_all_monoidal:
                    if assoc_exists(s,Lact,Ract,u,N):
                        n_monoidal+=1; unit_cards.add(u)
    return dict(N=N, n_tables=n_tables, covered=covered, n_bifun=n_bifun,
                n_monoidal=n_monoidal, nonpoly=nonpoly, unit_cards=sorted(unit_cards),
                elapsed=time.time()-t0)

if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 2
    budget=float(sys.argv[2]) if len(sys.argv)>2 else 1e9
    ra = (len(sys.argv)>3)
    r=sweep(N, report_all_monoidal=ra, time_budget=budget)
    print(f"N={r['N']}: size tables={r['n_tables']} covered={r['covered']} "
          f"valid bifunctors={r['n_bifun']} monoidal(with assoc)~{r['n_monoidal']} "
          f"elapsed={r['elapsed']:.1f}s")
    print(f"  unit cardinalities among monoidal found: {r['unit_cards']}")
    print(f"  NON-POLYNOMIAL monoidal survivors: {len(r['nonpoly'])}")
    for (u,s,L,R,pt) in r['nonpoly'][:20]:
        print(f"   unit={u} sizes={[[s[a][b] for b in range(N+1)] for a in range(N+1)]}")
        for b,(ok,ex,bal,ind) in pt.items():
            if not ok: print(f"      B={b}: balanced={bal} independent={ind} EXTRA={ex}")
