r"""
L3 verification: the emergent-holonomy invariant is GEOMETRIC.

Setup: G = P.P' exact factorization (Zappa-Szep), G acts on S (left, g.s = g[s]),
s in S. U = Stab_G(s), A = U cap P = Stab_P(s), B = U cap P' = Stab_{P'}(s).
Every g in U factors uniquely g = p p' (p in P, p' in P').

Define the INTERMEDIATE POINT of the dispatch-return loop:
    int(g) = p' . s        (g = p p')
Then g.s = p.(p'.s) = p.int(g) = s, so int(g) in M := (P.s) cap (P'.s).

CLAIMS to verify over the sweep (0 mismatches required):
 (C1) int is constant on double cosets A g B, and induces a bijection
          Abar : A\U/B  ->  M = (P.s) cap (P'.s).
      i.e.  #(A\U/B) == |M|,  and Abar injective+surjective.
 (C2) alignment  U = A.B  <=>  |A\U/B| = 1  <=>  M = {s}.
 (C3) the biconditional (L2):  (U == A.B as sets) <=> (U == (U cap P)(U cap P')).
      [definitional -- must be identically true]
 (C4) the naive ratio |U|/(|A||B|) equals |M| ONLY when every double coset AgB
      has size |A||B| (i.e. A cap g B g^{-1} = 1). Find a case where the ratio
      is NOT an integer / differs from |M|  -> shows |M| is the correct invariant.
"""
from itertools import combinations

def comp(a, b): return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    r=[0]*len(a)
    for i,x in enumerate(a): r[x]=i
    return tuple(r)
def idperm(n): return tuple(range(n))
def closure(gens,n):
    if not gens: return {idperm(n)}
    G={idperm(n)}; fr=list(G)
    while fr:
        nf=[]
        for g in fr:
            for h in gens:
                x=comp(g,h)
                if x not in G: G.add(x); nf.append(x)
        fr=nf
    return G
def stab(H,s): return {h for h in H if h[s]==s}
def orbit(H,s): return {h[s] for h in H}
def prod_set(Aset,Bset): return {comp(a,b) for a in Aset for b in Bset}

def is_exact(G,P,Pp):
    prods={}
    for p in P:
        for q in Pp:
            g=comp(p,q)
            if g in prods: return None
            prods[g]=(p,q)
    if set(prods)!=set(G): return None
    if len(P&Pp)!=1: return None
    return prods   # g -> (p,p')

def all_subgroups(G,n):
    G=list(G); subs={frozenset([idperm(n)])}
    for k in (1,2):
        for gens in combinations(G,k):
            subs.add(frozenset(closure(list(gens),n)))
    return [set(s) for s in subs]

def double_cosets(A,U,B):
    # partition U into A g B double cosets
    remaining=set(U); dcs=[]
    while remaining:
        g=next(iter(remaining))
        dc=prod_set(prod_set(A,{g}),B)
        dcs.append(dc)
        remaining-=dc
    return dcs

def check(name,gens,n):
    G=closure(gens,n)
    subs=all_subgroups(G,n)
    nfac=0; nchk=0
    bad=[]
    ratio_noninteger_example=None
    aligned_examples=0; proper_examples=0
    for P in subs:
        for Pp in subs:
            if len(P)*len(Pp)!=len(G): continue
            if len(P&Pp)!=1: continue
            fac=is_exact(G,P,Pp)
            if fac is None: continue
            nfac+=1
            for s in range(n):
                nchk+=1
                U=stab(G,s); A=U&P; B=U&Pp
                # int map
                intmap={}
                for g in U:
                    p,pp=fac[g]
                    intmap[g]=pp[s]        # p'.s
                image=set(intmap.values())
                Ps=orbit(P,s); Pps=orbit(Pp,s)
                M=Ps & Pps
                dcs=double_cosets(A,U,B)
                # (C1) bijection A\U/B <-> M
                # constant on double cosets:
                const_ok=all(len({intmap[g] for g in dc})==1 for dc in dcs)
                # image == M:
                img_ok=(image==M)
                # #double cosets == |M| (injective, given surjective+const):
                count_ok=(len(dcs)==len(M))
                if not(const_ok and img_ok and count_ok):
                    bad.append((name,s,'C1',const_ok,img_ok,count_ok,len(dcs),len(M)))
                # (C2) alignment
                AB=prod_set(A,B)
                aligned = (AB==U)
                c2 = (aligned == (len(M)==1)) and (aligned == (M=={s}))
                if not c2: bad.append((name,s,'C2',aligned,len(M),M=={s}))
                if aligned: aligned_examples+=1
                else: proper_examples+=1
                # (C3) L2 definitional
                c3 = ((AB==U)==(prod_set(U&P,U&Pp)==U))
                if not c3: bad.append((name,s,'C3'))
                # (C4) ratio vs |M|
                num=len(U); den=len(A)*len(B)
                ratio_int = (num%den==0)
                ratio=num//den if ratio_int else None
                if ratio_int and ratio!=len(M) and ratio_noninteger_example is None:
                    ratio_noninteger_example=(name,s,'ratio!=|M| but integer',ratio,len(M))
                if (not ratio_int) and ratio_noninteger_example is None:
                    ratio_noninteger_example=(name,s,'ratio NON-INTEGER',num,den,'|M|=',len(M),
                                              'dc sizes',sorted(len(dc) for dc in dcs))
    print("%-10s |G|=%2d  facts=%2d checks=%3d  aligned=%3d proper=%3d  mismatches=%d"
          %(name,len(G),nfac,nchk,aligned_examples,proper_examples,len(bad)))
    for b in bad[:6]: print("   MISMATCH",b)
    if ratio_noninteger_example: print("   ratio-note:",ratio_noninteger_example)
    return len(bad)

if __name__=="__main__":
    tests=[("S3",[(1,2,0),(1,0,2)],3),
           ("S4",[(1,2,3,0),(1,0,2,3)],4),
           ("A4",[(1,2,0,3),(0,2,3,1)],4),
           ("D4",[(1,2,3,0),(3,2,1,0)],4),
           ("Z2xZ2",[(1,0,2,3),(0,1,3,2)],4),
           ("S3x..",[(1,2,0,3,4),(1,0,2,3,4)],5),   # S3 on 3 pts + 2 fixed
           ("S4b",[(1,2,3,0),(1,0,2,3)],4),
           ("D6",[(1,2,3,4,5,0),(5,4,3,2,1,0)],6),
           ("S5part",[(1,2,3,4,0),(1,0,2,3,4)],5),
           ]
    total=0
    for nm,g,n in tests:
        total+=check(nm,g,n)
    print("\nTOTAL MISMATCHES:",total)
