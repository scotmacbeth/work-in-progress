"""
qskb_converse_test.py

Test the CONVERSE of MacBeth's Lemma B:  SUB  ==>  (9)  ?
Lemma B itself is (9) ==> SUB.  For the two-object Z/2 family it was verified
(9) <=> SUB <=> completely-prunable.  Here we extend the enumeration to:
  Family A2: 2 objects, Q = Z/2   (reproduce baseline: expect 48 valid)
  Family A3: 2 objects, Q = Z/3
  Family A4: 2 objects, Q = Z/4   (|St|=8; abelian star types Z8, Z4xZ2, Z2^3)
  Family B2: 3 objects, coarse groupoid {0,1,2}, Q = Z/2  (|St|=6)

DEFINITION NOTE (Ferri): the star (St(lambda),+_lambda) is an ABELIAN group.
So we enumerate only COMMUTATIVE group operations on the star set.  (For the
Z/2 baseline all order-4 groups are abelian, so the "48" count is unchanged.)

We reuse qskb_task2.Zn only.  build_model/compat/check-invariance are
reimplemented here with an OBJ parameter so 3 objects work, but the arrow /
compose / star / loop / compat-(5) definitions are IDENTICAL to qskb_task2.
Group-structure enumeration is reimplemented locally so we can (a) add order-8
abelian groups and (b) filter to abelian only.
"""
import time, itertools, random
from itertools import permutations, product
from qskb_task2 import Zn

# ---------------- abstract abelian groups (Cayley mult on 0..n-1, identity 0) ----------------
def abstract_abelian_groups(order):
    """Return list of (name, mult_fn) for the ABELIAN iso types of `order`,
    elements 0..order-1, identity 0."""
    res=[]
    if order==2:
        res.append(("Z2", lambda a,b:(a+b)%2))
    elif order==3:
        res.append(("Z3", lambda a,b:(a+b)%3))
    elif order==4:
        res.append(("Z4", lambda a,b:(a+b)%4))
        dec={0:(0,0),1:(1,0),2:(0,1),3:(1,1)}; enc={v:k for k,v in dec.items()}
        res.append(("V4", lambda a,b: enc[((dec[a][0]+dec[b][0])%2,(dec[a][1]+dec[b][1])%2)]))
    elif order==6:
        res.append(("Z6", lambda a,b:(a+b)%6))   # S3 excluded (non-abelian)
    elif order==8:
        res.append(("Z8", lambda a,b:(a+b)%8))
        # Z4 x Z2 : element k -> (k%4, k//4), k in 0..7
        def z4z2(a,b):
            xa,ya=a%4,a//4; xb,yb=b%4,b//4
            return ((xa+xb)%4) + 4*((ya+yb)%2)
        res.append(("Z4xZ2", z4z2))
        # Z2^3 : bits
        def z2cube(a,b): return a^b
        res.append(("Z2^3", z2cube))
    else:
        raise ValueError("no abelian groups tabulated for order %d"%order)
    return res

def is_commutative(add, S):
    return all(add[(x,y)]==add[(y,x)] for x in S for y in S)

def group_structures_abelian(S, e):
    """Enumerate ABELIAN group operations on set S with identity e.
    Yields (name, add_dict, neg_dict). Every abstract type here is abelian, and
    relabeling preserves commutativity, so no extra filtering needed."""
    n=len(S)
    others=[x for x in S if x!=e]
    for (gname, mult) in abstract_abelian_groups(n):
        for perm in permutations(others):
            phi={0:e}
            for k in range(1,n): phi[k]=perm[k-1]
            inv_phi={v:k for k,v in phi.items()}
            add={}
            for x in S:
                for y in S:
                    add[(x,y)]=phi[mult(inv_phi[x],inv_phi[y])]
            neg={}
            for x in S:
                for y in S:
                    if add[(x,y)]==e and add[(y,x)]==e:
                        neg[x]=y; break
            yield (gname, add, neg)

# ---------------- generalized model (OBJ parametrized) ----------------
def build_model_obj(Q, OBJ):
    qname, qels, qmult, qe, qinv = Q
    ARROWS=[(i,j,q) for i in OBJ for j in OBJ for q in qels]
    def s(x): return x[0]
    def t(x): return x[1]
    def compose(x,y):
        assert t(x)==s(y)
        return (s(x), t(y), qmult(x[2], y[2]))
    def ident(i): return (i,i,qe)
    def star(i): return [(i,j,q) for j in OBJ for q in qels]
    def loops(): return [(i,i,q) for i in OBJ for q in qels]
    return dict(ARROWS=ARROWS, s=s, t=t, compose=compose, ident=ident,
                star=star, loops=loops, qels=qels, OBJ=OBJ, Q=Q)

def compat_holds_obj(M, add, neg):
    s=M['s']; t=M['t']; compose=M['compose']
    for a in M['ARROWS']:
        ta=t(a); sa=s(a)
        addta=add[ta]; addsa=add[sa]; nega=neg[sa][a]
        for b in M['star'](ta):
            ab=compose(a,b)
            for c in M['star'](ta):
                lhs=compose(a, addta[(b,c)])
                ac=compose(a,c)
                rhs=addsa[(addsa[(ab, nega)], ac)]
                if lhs!=rhs:
                    return False
    return True

def left_action_obj(M, add, neg, a, b):
    sa=M['s'](a); ab=M['compose'](a,b); nega=neg[sa][a]
    return add[sa][(nega, ab)]

def is_loop(x): return x[0]==x[1]

def check_invariance_obj(M, add, neg):
    viol=[]
    for a in M['ARROWS']:
        ta=M['t'](a)
        for n in M['loops']():
            if n[0]==ta:
                r=left_action_obj(M, add, neg, a, n)
                if not is_loop(r):
                    viol.append((a,n,r))
    return (len(viol)==0, viol)

def loops_at(M, lam):
    return [x for x in M['star'](lam) if x[0]==lam and x[1]==lam]

def SUB_bool(M, add, neg, lam):
    L=loops_at(M,lam); Lset=set(L)
    closed=all(add[lam][(x,y)] in Lset for x in L for y in L)
    invc=all(neg[lam][x] in Lset for x in L)
    return closed and invc

def cond9(M, add, neg):
    allinv,_=check_invariance_obj(M, add, neg); return allinv

def fmt(x): return f"({x[0]},{x[1]},{x[2]})"

# ---------------- run a family ----------------
def run_family(Q, OBJ, label, cap=None, seed=12345):
    t0=time.time()
    M=build_model_obj(Q, OBJ)
    structs_by_obj={}
    for lam in OBJ:
        S=M['star'](lam); e=M['ident'](lam)
        structs_by_obj[lam]=list(group_structures_abelian(S,e))
    per_obj=len(structs_by_obj[OBJ[0]])
    total_combos=per_obj**len(OBJ)
    print(f"\n{'#'*70}")
    print(f"FAMILY {label}: objects={OBJ}, Q={Q[0]}, |St|={len(M['star'](OBJ[0]))}")
    print(f"  abelian group-structs per object = {per_obj}; combos = {per_obj}^{len(OBJ)} = {total_combos}")

    capped=False
    if cap is not None and total_combos>cap:
        capped=True
        print(f"  *** CAP {cap} < {total_combos}: RANDOM-SAMPLING {cap} combos (NOT exhaustive). ***")
        rng=random.Random(seed)
        def combo_gen():
            for _ in range(cap):
                yield tuple(rng.choice(structs_by_obj[lam]) for lam in OBJ)
        combos_iter=combo_gen()
    else:
        combos_iter=product(*[structs_by_obj[lam] for lam in OBJ])

    valid=0; nsub=0; n9=0; sub_not9=[]; nine_not_sub=[]; tested=0
    for combo in combos_iter:
        tested+=1
        add={}; neg={}
        for idx,lam in enumerate(OBJ):
            gname,a,n=combo[idx]; add[lam]=a; neg[lam]=n
        if not compat_holds_obj(M, add, neg): continue
        valid+=1
        sub=all(SUB_bool(M,add,neg,lam) for lam in OBJ)
        c9=cond9(M,add,neg)
        if sub: nsub+=1
        if c9: n9+=1
        if sub and not c9: sub_not9.append((combo, add, neg))
        if c9 and not sub: nine_not_sub.append((combo, add, neg))
    dt=time.time()-t0
    print(f"  tested combos: {tested}{' (SAMPLED)' if capped else ''}")
    print(f"  VALID QSKBs   : {valid}")
    print(f"  with SUB      : {nsub}")
    print(f"  with (9)      : {n9}")
    print(f"  SUB & NOT (9) : {len(sub_not9)}   <-- refutes SUB=>(9) if > 0")
    print(f"  (9) & NOT SUB : {len(nine_not_sub)}  (would refute Lemma B (9)=>SUB if > 0)")
    print(f"  elapsed: {dt:.1f}s")
    if sub_not9:
        print(f"  !!!! COUNTEREXAMPLE(S) to SUB=>(9) in family {label} !!!!")
        for (combo, add, neg) in sub_not9[:2]:
            print_witness(M, combo, add, neg)
    if nine_not_sub:
        print(f"  (informational) witness (9)&NOT-SUB:")
        for (combo, add, neg) in nine_not_sub[:1]:
            print_witness(M, combo, add, neg)
    return dict(label=label, valid=valid, nsub=nsub, n9=n9,
                sub_not9=len(sub_not9), nine_not_sub=len(nine_not_sub),
                capped=capped, converse_ok=(len(sub_not9)==0))

def print_witness(M, combo, add, neg):
    OBJ=M['OBJ']
    print("    ---- QSKB witness ----")
    for idx,lam in enumerate(OBJ):
        gname=combo[idx][0]
        S=M['star'](lam)
        print(f"    object {lam}: +_{lam} abstract type = {gname}; St = {[fmt(x) for x in S]}")
        for x in S:
            row=[fmt(add[lam][(x,y)]) for y in S]
            print(f"        {fmt(x)} + : {row}")
    allinv,viol=check_invariance_obj(M, add, neg)
    print(f"    (9) violations (a, loop n at t(a), a>n):")
    for (a,n,r) in viol[:6]:
        print(f"      a={fmt(a)}  n={fmt(n)}  a>n={fmt(r)}")

if __name__=="__main__":
    results=[]
    results.append(run_family(Zn(2), [0,1], "A2 (2obj,Z/2)"))
    results.append(run_family(Zn(3), [0,1], "A3 (2obj,Z/3)"))
    results.append(run_family(Zn(4), [0,1], "A4 (2obj,Z/4)", cap=2_000_000))
    results.append(run_family(Zn(2), [0,1,2], "B2 (3obj,Z/2)", cap=2_000_000))

    print(f"\n{'='*70}\nSUMMARY TABLE")
    print(f"{'family':<18}{'valid':>7}{'SUB':>6}{'(9)':>6}{'SUB&¬(9)':>10}{'(9)&¬SUB':>10}{'conv?':>7}")
    for r in results:
        print(f"{r['label']:<18}{r['valid']:>7}{r['nsub']:>6}{r['n9']:>6}"
              f"{r['sub_not9']:>10}{r['nine_not_sub']:>10}{str(r['converse_ok']):>7}"
              + ("  [SAMPLED]" if r['capped'] else ""))
    allok=all(r['converse_ok'] for r in results)
    print(f"\nVERDICT: SUB=>(9) holds in ALL tested families: {allok}")
