"""
TASK 2.  Is (v_S, empty) a monoidal structure on Set?
         A v_S B  :=  A + (A x S x B) + B.
Everything ELEMENTWISE: unitors, associator, naturality, pentagon, triangle.
"""
from core import *
from itertools import product as iproduct

FAILS = []
SIZES = [0, 1, 2]
BIG   = [3]          # a few size-3 spot checks


def sets_of(n, tag):
    return mkset(n, tag)


def apply(d, x):
    if x not in d:
        raise KeyError(f"map undefined at {x}")
    return d[x]


def compose_maps(g, f):
    """g o f  as dicts."""
    return {x: g[f[x]] for x in f}


def idmap(A):
    return {a: a for a in A}


# ===================================================================== (a) unitors
print("=" * 78)
print("TASK 2a  UNITORS   lambda : empty v_S B -> B    rho : A v_S empty -> A")
ok = True
detail = []
for n in SIZES + BIG:
    for s in SIZES + BIG:
        B, S = sets_of(n, 'b'), sets_of(s, 'k')
        Lset = vee(EMPTY, B, S)
        lm = lam(B, S)
        b1, why1 = is_bijection(lm, Lset, B)
        A = sets_of(n, 'a')
        Rset = vee(A, EMPTY, S)
        rh = rho(A, S)
        b2, why2 = is_bijection(rh, Rset, A)
        if not (b1 and b2):
            ok = False
            detail.append((n, s, why1, why2))
print(f"  lambda, rho bijections for |A|,|B|,|S| in {SIZES+BIG}: "
      f"{'PASS' if ok else 'FAIL ' + str(detail)}")
if not ok: FAILS.append("2a unitors")

# explicit witness
B, S = mkset(2, 'b'), mkset(2, 'k')
print(f"  witness |B|=2,|S|=2:  empty v_S B = {sorted(vee(EMPTY,B,S), key=repr)}")
print(f"                        lambda      = {dict(sorted(lam(B,S).items(), key=repr))}")
A = mkset(2, 'a')
print(f"  witness |A|=2,|S|=2:  A v_S empty = {sorted(vee(A,EMPTY,S), key=repr)}")
print(f"                        rho         = {dict(sorted(rho(A,S).items(), key=repr))}")
print("  (the A x S x empty middle piece is empty, so no elements are dropped)")

# NATURALITY of the unitors
print()
print("  naturality of lambda, rho (over all functions f : B -> B'):")
nat_ok = True
for nb in [0, 1, 2]:
    for nb2 in [0, 1, 2]:
        for s in [0, 1, 2]:
            B, B2, S = sets_of(nb, 'b'), sets_of(nb2, 'c'), sets_of(s, 'k')
            for f in funcs(B, B2):
                # lambda_B' o (id_empty v f) == f o lambda_B
                vf = vee_map({}, f, S)
                for x in vee(EMPTY, B, S):
                    if lam(B2, S)[vf(x)] != f[lam(B, S)[x]]:
                        nat_ok = False
                # rho
                vg = vee_map(f, {}, S)
                for x in vee(B, EMPTY, S):
                    if rho(B2, S)[vg(x)] != f[rho(B, S)[x]]:
                        nat_ok = False
print(f"    {'PASS' if nat_ok else 'FAIL'}")
if not nat_ok: FAILS.append("2a unitor naturality")


# ================================================================== (b) associator
print()
print("=" * 78)
print("TASK 2b  ASSOCIATOR  alpha : (A v B) v C -> A v (B v C)")
print("""  definition (on tagged elements):
    ('l',('l',a))              |-> ('l',a)
    ('l',('m',(a,s,b)))        |-> ('m',(a,s,('l',b)))
    ('l',('r',b))              |-> ('r',('l',b))
    ('m',(('l',a),s,c))        |-> ('m',(a,s,('r',c)))
    ('m',(('m',(a,s1,b)),s2,c))|-> ('m',(a,s1,('m',(b,s2,c))))
    ('m',(('r',b),s,c))        |-> ('r',('m',(b,s,c)))
    ('r',c)                    |-> ('r',('r',c))
  (normal form: a nonempty sublist of [A,B,C], with an S-label between each
   pair of CONSECUTIVE chosen entries; alpha preserves the normal form.)""")

bij_ok = True
bad = []
grid = [(a, b, c, s) for a in SIZES for b in SIZES for c in SIZES for s in SIZES]
grid += [(3, 1, 2, 1), (2, 3, 1, 2), (1, 2, 3, 2), (3, 3, 3, 3), (2, 2, 2, 3), (3, 0, 2, 3)]
for (na, nb, nc, ns) in grid:
    A, B, C, S = sets_of(na, 'a'), sets_of(nb, 'b'), sets_of(nc, 'c'), sets_of(ns, 'k')
    dom = vee(vee(A, B, S), C, S)
    cod = vee(A, vee(B, C, S), S)
    al = alpha(A, B, C, S)
    ok, why = is_bijection(al, dom, cod)
    if not ok:
        bij_ok = False
        bad.append((na, nb, nc, ns, why, len(dom), len(cod)))
print(f"  alpha is a bijection on all {len(grid)} size-tuples "
      f"(|A|,|B|,|C|,|S| in {{0,1,2}} plus size-3 spot checks): "
      f"{'PASS' if bij_ok else 'FAIL'}")
for b in bad[:8]: print("    FAIL at", b)
if not bij_ok: FAILS.append("2b associator bijection")

# explicit worked instance
A, B, C, S = mkset(1, 'a'), mkset(1, 'b'), mkset(1, 'c'), mkset(1, 'k')
print(f"  worked instance |A|=|B|=|C|=|S|=1  ({len(vee(vee(A,B,S),C,S))} elements each side):")
for x, y in sorted(alpha(A, B, C, S).items(), key=repr):
    print(f"    {x!r:42s} |-> {y!r}")

# NATURALITY of alpha
print()
print("  naturality of alpha in all three arguments (all f:A->A', g:B->B', h:C->C'")
print("  with |A|,|A'|,|B|,|B'|,|C|,|C'| <= 2, |S| <= 2):")
nat_ok = True
cnt = 0
for na, na2, nb, nb2, nc, nc2, ns in iproduct([0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2]):
    if not nat_ok: break
    A, A2 = sets_of(na,'a'), sets_of(na2,'A')
    B, B2 = sets_of(nb,'b'), sets_of(nb2,'B')
    C, C2 = sets_of(nc,'c'), sets_of(nc2,'C')
    S = sets_of(ns,'k')
    # one representative function each (all of them would be huge); sweep all
    # functions only when domains are small
    for f in funcs(A, A2):
        for g in funcs(B, B2):
            for h in funcs(C, C2):
                cnt += 1
                # alpha_{A'B'C'} o ((f v g) v h)  ==  (f v (g v h)) o alpha_{ABC}
                fg   = vee_map(f, g, S)
                fgh_l = vee_map({x: fg(x) for x in vee(A,B,S)}, h, S)
                gh   = vee_map(g, h, S)
                fgh_r = vee_map(f, {x: gh(x) for x in vee(B,C,S)}, S)
                al, al2 = alpha(A, B, C, S), alpha(A2, B2, C2, S)
                for x in vee(vee(A, B, S), C, S):
                    if al2[fgh_l(x)] != fgh_r(al[x]):
                        nat_ok = False
                        print("    FAIL naturality at", x, (na,na2,nb,nb2,nc,nc2,ns))
                        break
print(f"    checked {cnt} function-triples: {'PASS' if nat_ok else 'FAIL'}")
if not nat_ok: FAILS.append("2b associator naturality")


# ==================================================================== (c) PENTAGON
print()
print("=" * 78)
print("TASK 2c  PENTAGON")
print("""  path 1:  ((AvB)vC)vD --alpha_{AvB,C,D}--> (AvB)v(CvD) --alpha_{A,B,CvD}--> Av(Bv(CvD))
  path 2:  ((AvB)vC)vD --alpha_{A,B,C} v D--> (Av(BvC))vD --alpha_{A,BvC,D}--> Av((BvC)vD)
                       --A v alpha_{B,C,D}--> Av(Bv(CvD))""")
pent_ok = True
pbad = []
tested = 0
for na, nb, nc, nd, ns in iproduct(SIZES, SIZES, SIZES, SIZES, SIZES):
    A, B, C, D = sets_of(na,'a'), sets_of(nb,'b'), sets_of(nc,'c'), sets_of(nd,'d')
    S = sets_of(ns,'k')
    dom = vee(vee(vee(A, B, S), C, S), D, S)
    cod = vee(A, vee(B, vee(C, D, S), S), S)

    AB, BC, CD = vee(A,B,S), vee(B,C,S), vee(C,D,S)
    BCD = vee(B, CD, S)

    # path 1
    a1 = alpha(AB, C, D, S)              # ((AvB)vC)vD -> (AvB)v(CvD)
    a2 = alpha(A, B, CD, S)              # (AvB)v(CvD) -> Av(Bv(CvD))
    p1 = {x: a2[a1[x]] for x in dom}

    # path 2
    a3 = alpha(A, B, C, S)               # (AvB)vC -> Av(BvC)
    a3vD = vee_map(a3, idmap(D), S)      # ((AvB)vC)vD -> (Av(BvC))vD
    a4 = alpha(A, BC, D, S)              # (Av(BvC))vD -> Av((BvC)vD)
    a5 = alpha(B, C, D, S)               # (BvC)vD -> Bv(CvD)
    Ava5 = vee_map(idmap(A), a5, S)      # Av((BvC)vD) -> Av(Bv(CvD))
    p2 = {x: Ava5(a4[a3vD(x)]) for x in dom}

    tested += 1
    # both land in cod
    for x in dom:
        assert p1[x] in cod and p2[x] in cod, "pentagon path escapes codomain!"
    if p1 != p2:
        pent_ok = False
        diffs = [(x, p1[x], p2[x]) for x in dom if p1[x] != p2[x]]
        pbad.append((na, nb, nc, nd, ns, len(dom), len(diffs), diffs[:2]))

print(f"  tested {tested} size-tuples (|A|,|B|,|C|,|D|,|S| in {{0,1,2}}), "
      f"comparing the two composites ELEMENTWISE")
print(f"  PENTAGON: {'PASS - the two paths are equal as functions' if pent_ok else 'FAIL'}")
for b in pbad[:5]: print("    FAIL:", b)
if not pent_ok: FAILS.append("2c pentagon")

# largest instance size, as evidence of non-triviality
A,B,C,D,S = mkset(2,'a'),mkset(2,'b'),mkset(2,'c'),mkset(2,'d'),mkset(2,'k')
print(f"  (largest instance: |((AvB)vC)vD| = "
      f"{len(vee(vee(vee(A,B,S),C,S),D,S))} elements, all matched)")

# a size-3 spot check
for tup in [(3,1,1,1,1),(1,3,1,2,1),(2,1,3,1,2),(1,1,1,1,3),(2,2,2,2,3)]:
    na,nb,nc,nd,ns = tup
    A,B,C,D = sets_of(na,'a'),sets_of(nb,'b'),sets_of(nc,'c'),sets_of(nd,'d')
    S = sets_of(ns,'k')
    dom = vee(vee(vee(A,B,S),C,S),D,S)
    AB, BC, CD = vee(A,B,S), vee(B,C,S), vee(C,D,S)
    a1, a2 = alpha(AB,C,D,S), alpha(A,B,CD,S)
    p1 = {x: a2[a1[x]] for x in dom}
    a3vD = vee_map(alpha(A,B,C,S), idmap(D), S)
    a4 = alpha(A,BC,D,S)
    Ava5 = vee_map(idmap(A), alpha(B,C,D,S), S)
    p2 = {x: Ava5(a4[a3vD(x)]) for x in dom}
    r = "equal" if p1 == p2 else "DIFFER"
    print(f"  size-3 spot check {tup}: |dom|={len(dom):4d}  paths {r}")
    if p1 != p2: FAILS.append(f"2c pentagon size-3 {tup}")


# ==================================================================== (d) TRIANGLE
print()
print("=" * 78)
print("TASK 2d  TRIANGLE:  (A v I) v B --alpha--> A v (I v B) --A v lambda--> A v B")
print("                    equals        rho v B : (A v I) v B --> A v B      (I = empty)")
tri_ok = True
tbad = []
for na, nb, ns in iproduct(SIZES + BIG, SIZES + BIG, SIZES + BIG):
    A, B, S = sets_of(na,'a'), sets_of(nb,'b'), sets_of(ns,'k')
    I = EMPTY
    dom = vee(vee(A, I, S), B, S)
    cod = vee(A, B, S)
    al = alpha(A, I, B, S)                       # (AvI)vB -> Av(IvB)
    Avlam = vee_map(idmap(A), lam(B, S), S)      # Av(IvB) -> AvB
    left = {x: Avlam(al[x]) for x in dom}
    rhovB = vee_map(rho(A, S), idmap(B), S)      # (AvI)vB -> AvB
    right = {x: rhovB(x) for x in dom}
    for x in dom:
        assert left[x] in cod and right[x] in cod, "triangle escapes codomain!"
    if left != right:
        tri_ok = False
        tbad.append((na, nb, ns, [(x, left[x], right[x]) for x in dom if left[x] != right[x]][:2]))
print(f"  TRIANGLE: {'PASS - the two composites are equal as functions' if tri_ok else 'FAIL'}")
for b in tbad[:5]: print("    FAIL:", b)
if not tri_ok: FAILS.append("2d triangle")

print()
print("TASK 2 RESULT:", "PASS - (v_S, empty) is a genuine monoidal structure on Set"
      if not FAILS else f"FAIL {FAILS}")
