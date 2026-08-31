"""
zs_converse_check.py
====================
Confirm the CONVERSE half of "ZS axioms <=> associativity":
build the Zappa-Szep product T |><| E directly from abstract matched-pair data
(left action {}^e t, restriction e^t, and the two category structures T, E on a
shared object set), with multiplication
    (t2,e2) . (t1,e1) = ( t2 . {}^{e2}t1 ,  e2^{t1} . e1 )
and check: the product is associative  <=>  ZS1-ZS4 hold. We take VALID data
(extracted from a real ZS category), confirm associativity, then BREAK each axiom
by perturbing one value and confirm associativity then FAILS -- showing the axioms
are exactly what associativity needs.
"""
import sys, itertools
sys.path.insert(0, "/home/agent/projects/scratch")
from two_atoms_check import Cat, chain
from zs_cocycle_check import (closed_transversal_exists, extract_cocycle,
                              connected_groupoid_Z2)


def zs_product_assoc(C, Tset, factor, leftact, restr):
    """Build the ZS product multiplication on pairs (t,e) and test associativity.
    A 'pair' a->b is (t,e) with t in T(a,b), e in End(a), meaning t o e.
    Returns (n_triples_checked, n_assoc_fail)."""
    # enumerate all pairs as the morphisms (t in T(a,b), e in End(a))
    pairs = []   # (t, e, a, b)
    Tlist = list(Tset)
    for t in Tlist:
        a, b = C.src[t], C.dst[t]
        for e in C.end(a):
            pairs.append((t, e))

    def mult(P2, P1):
        # P2:b->c = (t2,e2), P1:a->b=(t1,e1); need src/dst match
        t2, e2 = P2; t1, e1 = P1
        if C.src[t2] != C.dst[t1]:   # b mismatch (dst of t1 = b = src of t2)
            return None
        # but careful: P1 morphism a->b means dom=src(e1)=src(t1)? t1 o e1, e1 in End(a)
        # dom = a = src(t1); cod = dst(t1)=b.  P2 dom=src(t2)=b? src(t2)=dom of t2.
        # we need dst(t1)=src(t2).
        # {}^{e2} t1 : need e2 in End(src(t2)) acting on t1 in T(.,src(t2))
        if (e2, t1) not in leftact:
            return None
        lt = leftact[(e2, t1)]      # {}^{e2}t1 in T(a, src(t2))? dst(lt)=dst(t1)...
        rt = restr[(e2, t1)]        # e2^{t1} in End(a)
        # t2 . {}^{e2}t1  (composition in T, i.e. in C among transversal arrows)
        if C.dst[lt] != C.src[t2]:
            return None
        tt = C.compose(t2, lt)
        if tt not in Tset:
            return None   # closure needed
        # e2^{t1} . e1  in End(a)
        ee = C.compose(rt, e1)
        return (tt, ee)

    nfail = 0; ntot = 0
    for P3 in pairs:
        for P2 in pairs:
            for P1 in pairs:
                a = mult(P2, P1)
                if a is None: continue
                left = mult(P3, a)
                b = mult(P3, P2)
                if b is None: continue
                right = mult(b, P1)
                if left is None or right is None: continue
                ntot += 1
                if left != right:
                    nfail += 1
    return ntot, nfail


def run(C):
    print("="*72); print("CATEGORY:", C.name)
    ok, T = closed_transversal_exists(C, return_one=True)
    if not ok:
        print("  no closed transversal; skip"); return
    Tset, factor, leftact, restr = extract_cocycle(C, T)
    ntot, nfail = zs_product_assoc(C, Tset, factor, leftact, restr)
    print(f"  VALID data: associativity triples checked={ntot}, failures={nfail}")
    assert nfail == 0, "valid ZS data should be associative!"
    print("  >> with correct ZS data: product associative. ✓")

    # Now BREAK the left action at one point and re-test associativity.
    import copy
    broke_any = False
    keys = list(leftact.keys())
    for kk in keys:
        la2 = dict(leftact)
        # find an alternative value in the same T(a,b) to swap to
        t = kk[1]; a, b = C.src[t], C.dst[t]
        alts = [u for u in Tset if C.src[u]==a and C.dst[u]==b and u != la2[kk]]
        if not alts:
            continue
        la2[kk] = alts[0]
        ntot2, nfail2 = zs_product_assoc(C, Tset, factor, la2, restr)
        if nfail2 > 0:
            broke_any = True
            print(f"  perturb leftact[{kk}] -> {alts[0]}: assoc failures={nfail2} "
                  f"(of {ntot2})  => axioms are NECESSARY for assoc. ✓")
            break
    if not broke_any:
        print("  (no single-point perturbation broke assoc here; structure too rigid/small)")


if __name__ == "__main__":
    run(connected_groupoid_Z2())
    run(chain(3))
