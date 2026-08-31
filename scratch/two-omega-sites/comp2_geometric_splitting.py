"""
Comp 2 (Part 1.5): geometric-splitting sweep.

For internal exact factorizations G = P.P' acting (faithfully, naturally) on points,
and each point stabilizer E = Stab_G(s), set A = E cap P, B = E cap P'.
Test the structural claims:
  (i)   A cap B = 1  ALWAYS  (since A cap B <= P cap P' = {e}).
  (ii)  aligned (|A||B|=|E| and A.B=E)  =>  B is a complement to A in E,
        so if A is normal the extension 1->A->E->B->1 SPLITS ([omega_st]=0).
  (iii) the abstract witness (A,B,E) ~ (C2,C2,C4) is NEVER realized:
        A cap B=1 with |A|=|B|=2 forces two DISTINCT order-2 subgroups => Klein four, not C4.
  Also: does any exact factorization ever yield a NON-split point-stabilizer extension
        over its P-part with quotient iso to its P'-part? (predict: no, in aligned case).
"""
import sys
sys.path.insert(0, "/home/agent/projects/scratch/general-M-liftings")
from zs_holonomy import (comp, inv, idperm, closure, subgroup,
                         is_exact_factorization, stab, factor_product, all_subgroups)
from itertools import combinations

def order_of(g, e):
    x = g; k = 1
    while x != e:
        x = comp(x, g); k += 1
    return k

def fingerprint(H, n):
    """iso fingerprint of a subgroup H (set of perms): (|H|, abelian?, sorted element-order multiset)."""
    e = idperm(n)
    H = list(H)
    abelian = all(comp(a,b)==comp(b,a) for a in H for b in H)
    orders = tuple(sorted(order_of(g,e) for g in H))
    return (len(H), abelian, orders)

def name_group(fp):
    order, ab, orders = fp
    if order==1: return "1"
    if order==2: return "C2"
    if order==3: return "C3"
    if order==4:
        return "C4" if 4 in orders else "V4"
    if order==6:
        return "C6" if 6 in orders else "S3"
    if order==8:
        if 8 in orders: return "C8"
        if ab: return "C4xC2" if 4 in orders else "C2^3"
        return "D4" if orders.count(4)==2 else "Q8"
    return f"grp{order}{'ab' if ab else 'nonab'}{orders}"

def is_normal(A, E, n):
    return all(comp(comp(g,a),inv(g)) in A for g in E for a in A)

def has_complement(A, E, n):
    """does E split over normal A? i.e. exists subgroup C<=E with A cap C=1 and A.C=E."""
    e = idperm(n)
    subs = all_subgroups(E, n)
    target = len(E)//len(A)
    for C in subs:
        if len(C)!=target: continue
        if len(A & C)!=1: continue
        if factor_product(A,C)==E:
            return True
    return False

def sweep(name, gens, n):
    G = closure(gens, n)
    subs = all_subgroups(G, n)
    triples = []
    for P in subs:
        for Pp in subs:
            if len(P)*len(Pp)!=len(G): continue
            if len(P & Pp)!=1: continue
            if not is_exact_factorization(G,P,Pp): continue
            for s in range(n):
                SG = stab(G,s); A = SG & P; B = SG & Pp
                assert len(A & B)==1, "A cap B != 1  (IMPOSSIBLE)"      # claim (i)
                aligned = (factor_product(A,B)==SG)
                fpE, fpA, fpB = fingerprint(SG,n), fingerprint(A,n), fingerprint(B,n)
                Anorm = is_normal(A,SG,n)
                split = has_complement(A,SG,n) if Anorm else None
                triples.append((name_group(fpA),name_group(fpB),name_group(fpE),
                                aligned, Anorm, split))
    return triples

CASES = [
    ("S3",    [(1,2,0),(1,0,2)], 3),
    ("S4",    [(1,2,3,0),(1,0,2,3)], 4),
    ("A4",    [(1,2,0,3),(0,2,3,1)], 4),
    ("D4",    [(1,2,3,0),(3,2,1,0)], 4),
    ("V4",    [(1,0,2,3),(0,1,3,2)], 4),
    ("S4b",   [(1,2,3,0),(1,0,2,3)], 4),
    ("D6/S3x?",[(1,2,3,4,5,0),(5,4,3,2,1,0)], 6),   # dihedral order 12 on 6 pts
    ("A5",    [(1,2,3,4,0),(1,0,2,3,4)], 5),
]

from collections import Counter
allc = Counter()
saw_C4_from_C2C2 = False
nonsplit_aligned = []
for name,gens,n in CASES:
    tr = sweep(name,gens,n)
    for (a,b,ee,aligned,anorm,split) in tr:
        allc[(a,b,ee,aligned,anorm,split)] += 1
        if a=="C2" and b=="C2" and ee=="C4":
            saw_C4_from_C2C2 = True
        if aligned and anorm and split is False:
            nonsplit_aligned.append((name,a,b,ee))

print("=== (A,B,E, aligned, A-normal, split) multiset over all exact factorizations ===")
for key,ct in sorted(allc.items(), key=lambda kv:(-kv[1],str(kv[0]))):
    a,b,ee,al,an,sp = key
    print(f"  A={a:6} B={b:6} E={ee:8} aligned={al!s:5} Anorm={an!s:5} split={sp!s:5}   x{ct}")

print()
print("CLAIM (i)  A cap B = 1 always:                    HELD (no assertion fired)")
print("CLAIM (iii) (A,B,E)=(C2,C2,C4) ever realized?     ", saw_C4_from_C2C2, " (expect False)")
print("Any ALIGNED + A-normal + NON-split extension?     ", nonsplit_aligned if nonsplit_aligned else "NONE (expect none)")
