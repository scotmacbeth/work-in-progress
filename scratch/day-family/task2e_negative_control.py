"""
NEGATIVE CONTROL for TASK 2.

A pentagon checker that says PASS on everything is worthless.  There is a second,
equally "obvious" candidate associator: the one that SWAPS the two S-labels in
the five-fold middle term

    ('m',(('m',(a,s1,b)),s2,c))  |-->  ('m',(a, s2, ('m',(b, s1, c))))

It is still a natural bijection (same cardinalities, same naturality squares).
If the pentagon check is real, it must REJECT this one.
"""
from core import *
from itertools import product as iproduct


def alpha_swap(A, B, C, S):
    d = {}
    AB = vee(A, B, S)
    for x in vee(AB, C, S):
        tag, val = x
        if tag == 'l':
            it, iv = val
            if it == 'l':   d[x] = L(iv)
            elif it == 'r': d[x] = R(L(iv))
            else:
                a, s, b = iv
                d[x] = M(a, s, L(b))
        elif tag == 'r':
            d[x] = R(R(val))
        else:
            blk, s2, c = val
            bt, bv = blk
            if bt == 'l':   d[x] = M(bv, s2, R(c))
            elif bt == 'r': d[x] = R(M(bv, s2, c))
            else:
                a, s1, b = bv
                d[x] = M(a, s2, M(b, s1, c))    # <-- LABELS SWAPPED
    return d


def idmap(A): return {a: a for a in A}

print("=" * 78)
print("NEGATIVE CONTROL: the label-swapping associator alpha'")

# it IS still a natural bijection
bij = True
for na, nb, nc, ns in iproduct([0,1,2],[0,1,2],[0,1,2],[0,1,2]):
    A,B,C,S = mkset(na,'a'), mkset(nb,'b'), mkset(nc,'c'), mkset(ns,'k')
    ok, _ = is_bijection(alpha_swap(A,B,C,S), vee(vee(A,B,S),C,S), vee(A,vee(B,C,S),S))
    bij &= ok
print(f"  alpha' is a bijection everywhere            : {'yes' if bij else 'no'}")

nat = True
for na,na2,nb,nb2,nc,nc2,ns in iproduct([0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2]):
    A,A2 = mkset(na,'a'), mkset(na2,'A')
    B,B2 = mkset(nb,'b'), mkset(nb2,'B')
    C,C2 = mkset(nc,'c'), mkset(nc2,'C')
    S = mkset(ns,'k')
    for f in funcs(A,A2):
        for g in funcs(B,B2):
            for h in funcs(C,C2):
                fg = vee_map(f,g,S)
                lft = vee_map({x: fg(x) for x in vee(A,B,S)}, h, S)
                gh = vee_map(g,h,S)
                rgt = vee_map(f, {x: gh(x) for x in vee(B,C,S)}, S)
                a, a2 = alpha_swap(A,B,C,S), alpha_swap(A2,B2,C2,S)
                for x in vee(vee(A,B,S),C,S):
                    if a2[lft(x)] != rgt(a[x]): nat = False
print(f"  alpha' is natural in A,B,C                  : {'yes' if nat else 'no'}")

# but does it satisfy the pentagon?
viol = []
for na, nb, nc, nd, ns in iproduct([0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2]):
    A,B,C,D = mkset(na,'a'), mkset(nb,'b'), mkset(nc,'c'), mkset(nd,'d')
    S = mkset(ns,'k')
    dom = vee(vee(vee(A,B,S),C,S),D,S)
    AB, BC, CD = vee(A,B,S), vee(B,C,S), vee(C,D,S)
    a1, a2 = alpha_swap(AB,C,D,S), alpha_swap(A,B,CD,S)
    p1 = {x: a2[a1[x]] for x in dom}
    a3vD = vee_map(alpha_swap(A,B,C,S), idmap(D), S)
    a4 = alpha_swap(A,BC,D,S)
    Ava5 = vee_map(idmap(A), alpha_swap(B,C,D,S), S)
    p2 = {x: Ava5(a4[a3vD(x)]) for x in dom}
    if p1 != p2:
        viol.append((na,nb,nc,nd,ns,
                     [(x,p1[x],p2[x]) for x in dom if p1[x]!=p2[x]][:1]))

print(f"  alpha' satisfies the PENTAGON               : "
      f"{'yes -- CHECKER IS BROKEN' if not viol else 'NO (as it must not)'}")
print(f"  pentagon violations found for alpha'        : {len(viol)} / 243 size-tuples")
if viol:
    na,nb,nc,nd,ns,ex = viol[0]
    print(f"  first violating instance |A|,|B|,|C|,|D|,|S| = {(na,nb,nc,nd,ns)}")
    for x,y1,y2 in ex:
        print(f"    x        = {x!r}")
        print(f"    path 1   = {y1!r}")
        print(f"    path 2   = {y2!r}    <-- differ")
print()
print("NEGATIVE CONTROL RESULT:",
      "PASS - the pentagon test discriminates (accepts alpha, rejects alpha')"
      if viol else "FAIL - the pentagon test accepts everything, it is vacuous")
