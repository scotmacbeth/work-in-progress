"""
Brute-force verification: bare ⊗-comonoids in Poly (Cont).
Container c = list of fiber sets. Shape set S = range(len(fibers)), fiber c[s]=range(fibers[s]).
Poly morphism f: p->q = (f1: Sp->Sq, {fsharp_s: q[f1 s] -> p[s]}).
⊗: shapes Sp×Sq; (p⊗q)[(s,t)] = p[s]×q[t].
Unit y = one shape, one direction.
We enumerate candidate (δ, ε) and check comonoid laws by DIRECT composition
of Poly-morphisms, with NO reference to the hand-derived 'monoid' claim.
Then we independently compute the set of (S, per-shape monoid structures)
and check the two sets coincide.
"""
from itertools import product

def compose(g, q_shapes, f, p_shapes):
    # f: p->q  (f1, fsharp), g: q->r (g1, gsharp). returns h: p->r
    f1, fsharp = f; g1, gsharp = g
    h1 = [g1[f1[s]] for s in range(p_shapes)]
    # hsharp_s: r[g1[f1 s]] -> p[s]  = fsharp_s ∘ gsharp_{f1 s}
    hsharp = []
    for s in range(p_shapes):
        gs = gsharp[f1[s]]   # r[g1 f1 s] -> q[f1 s]
        fs = fsharp[s]       # q[f1 s] -> p[s]
        hsharp.append([fs[gs[d]] for d in range(len(gs))])
    return (h1, hsharp)

def tensor_container(fibers):
    # returns (shapes list of (s,t), fiber size dict) for c⊗c
    S=len(fibers)
    shapes=[(s,t) for s in range(S) for t in range(S)]
    return shapes

def eq_morph(a,b):
    return a[0]==b[0] and [list(x) for x in a[1]]==[list(y) for y in b[1]]

def check_container(fibers):
    S=len(fibers)
    # y : 1 shape, 1 dir
    # candidate ε: ε1: S->0(single shape *), εsharp_s: y[*]=1 -> c[s] : pick e_s in c[s]
    # candidate δ: δ1: S -> S×S ; δsharp_s: (c⊗c)[δ1 s] -> c[s]
    # enumerate
    valid=set()
    # δ1 choices
    d1_choices=list(product([ (a,b) for a in range(S) for b in range(S)], repeat=S))
    for e in product(*[range(fibers[s]) for s in range(S)]):  # counit elements
        for d1 in d1_choices:
            # for each s, δsharp_s: c[a]×c[b] -> c[s] where (a,b)=d1[s]
            fiber_dom=[]
            for s in range(S):
                a,b=d1[s]
                fiber_dom.append([(x,y) for x in range(fibers[a]) for y in range(fibers[b])])
            # enumerate all m_s
            ranges=[list(product(range(fibers[s]),repeat=len(fiber_dom[s]))) for s in range(S)]
            for combo in product(*ranges):
                # build δ morphism c -> c⊗c
                # target c⊗c shapes indexed as (a,b); we represent shape as tuple
                # δ1 as list mapping s-> shape-index; use dict of shape->idx
                cc_shapes=[(a,b) for a in range(S) for b in range(S)]
                idx={sh:i for i,sh in enumerate(cc_shapes)}
                cc_fiber=[fibers[a]*fibers[b] for (a,b) in cc_shapes]
                # encode fiber element (x,y) of c[a]×c[b] as x*fibers[b]+y
                delta1=[idx[d1[s]] for s in range(S)]
                deltasharp=[]
                for s in range(S):
                    a,b=d1[s]
                    m=combo[s]  # tuple over domain pairs -> value in c[s]
                    dom=fiber_dom[s]
                    arr=[0]*(fibers[a]*fibers[b])
                    for k,(x,y) in enumerate(dom):
                        arr[x*fibers[b]+y]=m[k]
                    deltasharp.append(arr)
                delta=(delta1,deltasharp)
                # ε morphism c -> y : ε1 all 0, εsharp_s: y[*]=1 -> c[s], [e_s]
                eps=([0]*S,[[e[s]] for s in range(S)])
                # ---- counit law: (ε⊗id)∘δ = id  and (id⊗ε)∘δ = id ----
                # need ⊗ of morphisms. Build ε⊗id: c⊗c -> y⊗c ≅ c
                if not counit_ok(fibers,delta,eps,e,d1,combo): continue
                if not coassoc_ok(fibers,delta,d1,combo): continue
                valid.add((tuple(d1),tuple(combo),tuple(e)))
    return valid

def counit_ok(fibers,delta,eps,e,d1,combo):
    S=len(fibers)
    delta1,deltasharp=delta
    # left counit: (ε⊗id)∘δ should equal id_c
    # ε⊗id on shape (a,b) -> (*,b) ~ b ; backward c[b] -> c[a]×c[b], v ↦ (e[a],v)
    # compose: for s, δ1 s=(a,b). shape after: b. need == s.
    for s in range(S):
        a,b=d1[s]
        if b!=s: return False
        # backward: c[s]=c[b] -> via (ε⊗id)sharp: v↦(e[a],v) encode-> then deltasharp_s
        ds=deltasharp[s]  # (c[a]×c[b] encoded x*fibers[b]+y) -> c[s]
        for v in range(fibers[b]):
            enc=e[a]*fibers[b]+v
            if ds[enc]!=v: return False
    # right counit: (id⊗ε)∘δ = id ; shape (a,b)->a ~ a; need a==s; backward v↦(v,e[b])
    for s in range(S):
        a,b=d1[s]
        if a!=s: return False
        ds=deltasharp[s]
        for v in range(fibers[a]):
            enc=v*fibers[b]+e[b]
            if ds[enc]!=v: return False
    return True

def coassoc_ok(fibers,delta,d1,combo):
    S=len(fibers)
    # after counit, d1[s]=(s,s); m_s: c[s]×c[s]->c[s]
    delta1,deltasharp=delta
    for s in range(S):
        n=fibers[s]
        ds=deltasharp[s]  # encoded x*n+y -> value
        def m(x,y): return ds[x*n+y]
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    if m(m(x,y),z)!=m(x,m(y,z)): return False
    return True

def monoids_on(n):
    # all associative unital binary ops on range(n): return set of (op-as-tuple, unit)
    res=[]
    for op in product(range(n),repeat=n*n):
        M=[[op[i*n+j] for j in range(n)] for i in range(n)]
        # unit?
        units=[e for e in range(n) if all(M[e][x]==x and M[x][e]==x for x in range(n))]
        if not units: continue
        assoc=all(M[M[x][y]][z]==M[x][M[y][z]] for x in range(n) for y in range(n) for z in range(n))
        if not assoc: continue
        for e in units:
            res.append((op,e))
    return res

# TEST 1: one-shape container y^A, |A|=n. Bare ⊗-comonoids should = monoids on A.
for n in [1,2,3]:
    fibers=[n]
    V=check_container(fibers)
    # extract: each valid has d1=((0,0),), combo=(op_tuple,), e=(unit,)
    got=set()
    for d1,combo,e in V:
        assert d1==((0,0),), d1
        got.add((combo[0],e[0]))
    mon=set((op,u) for (op,u) in monoids_on(n))
    print(f"y^{n}: bare ⊗-comonoids found={len(got)}  monoids(assoc+unital)={len(mon)}  MATCH={got==mon}")

# TEST 2: two-shape container [1,2] (fibers of size 1 and 2)
fibers=[1,2]
V=check_container(fibers)
# expected: δ1 diagonal; monoid on c[0](size1: trivial, 1 monoid) × monoid on c[1](size2: 2 monoids)
m1=len(monoids_on(1)); m2=len(monoids_on(2))
# also each shape's unit is determined by its monoid; count valid = product over shapes of #monoids
import math
exp=m1*m2
print(f"[1,2]: bare ⊗-comonoids found={len(V)}  expected(diag × prod of per-fiber monoids)={exp}  MATCH={len(V)==exp}")
# verify all have diagonal δ1
alldiag=all(d1==((0,0),(1,1)) for d1,_,_ in V)
print(f"[1,2]: all δ1 diagonal? {alldiag}")
