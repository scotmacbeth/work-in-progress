"""
zs_closure_counterexample.py
============================
Candidate: a 3-object category C (a -> x -> y) where EVERY Hom(a,b) is free as a
right End(a)-set (so the objectwise factorization f=t.e exists at every pair),
but NO global choice of transversals forms a closed wide subcategory T.
=> the Zappa-Szep PRODUCT needs strictly more than objectwise freeness; closure
   (vanishing of a holonomy/cocycle obstruction) is genuinely extra.

Design (the "rigid twist"):
  End(a) = {1,g}, g^2=1.   End(x) = {1,k}, k^2=1.   End(y) = {1}.
  Hom(a,x) = {p, pg=p.g}            free right End(a); End(x) acts trivially: k.p=p
  Hom(x,y) = {s, sk=s.k, s2, s2k}   free right End(x), TWO orbits
  Hom(a,y) = {q, qg=q.g}            free right End(a), ONE orbit
  Cross composites:  s.p=q,  s2.p=qg   <-- the rigid twist (differ by g, NO slack)
"""

import sys
sys.path.insert(0, "/home/agent/projects/scratch")
from two_atoms_check import Cat
from zs_cocycle_check import (is_free_right, all_homs_free,
                              closed_transversal_exists, right_orbits)


def build_counterexample():
    """MINIMAL rigid-twist. Only End(a)=Z/2 is nontrivial; End(x)=End(y)=triv.
    10 morphisms. Hom(x,y)={s,s2} has TWO singleton orbits (End(x) trivial) so the
    transversal T(x,y)={s,s2} is FORCED -- no slack there -- and the twist
    s.p=q, s2.p=qg makes closure impossible for either choice of T(a,x),T(a,y)."""
    objs = ["a", "x", "y"]
    ida, g   = ("a", 0), ("a", 1)        # End(a) = {1, g}, g^2 = 1
    idx      = ("x", 0)                   # End(x) = {1}
    idy      = ("y", 0)                   # End(y) = {1}
    p, pg    = ("p", 0), ("p", 1)        # Hom(a,x) = {p, pg=p.g}     (1 orbit)
    s, s2    = ("s", 0), ("s2", 0)       # Hom(x,y) = {s, s2}         (2 orbits)
    q, qg    = ("q", 0), ("q", 1)        # Hom(a,y) = {q, qg=q.g}     (1 orbit)

    arrows = [ida, g, idx, idy, p, pg, s, s2, q, qg]
    src = {}; dst = {}
    for m in [ida, g]: src[m]="a"; dst[m]="a"
    src[idx]="x"; dst[idx]="x"
    src[idy]="y"; dst[idy]="y"
    for m in [p, pg]:  src[m]="a"; dst[m]="x"
    for m in [s, s2]:  src[m]="x"; dst[m]="y"
    for m in [q, qg]:  src[m]="a"; dst[m]="y"

    comp = {}
    def setc(gg, ff, val): comp[(gg, ff)] = val

    setc(ida,ida,ida); setc(ida,g,g); setc(g,ida,g); setc(g,g,ida)   # End(a)=Z/2
    setc(idx,idx,idx); setc(idy,idy,idy)                             # trivial endos
    # a->x : right End(a) free, left End(x) trivial
    setc(p,ida,p); setc(pg,ida,pg); setc(idx,p,p); setc(idx,pg,pg)
    setc(p,g,pg); setc(pg,g,p)
    # x->y : units only (End(x),End(y) trivial)
    setc(s,idx,s); setc(s2,idx,s2); setc(idy,s,s); setc(idy,s2,s2)
    # a->y : right End(a) free
    setc(q,ida,q); setc(qg,ida,qg); setc(idy,q,q); setc(idy,qg,qg)
    setc(q,g,qg); setc(qg,g,q)
    # CROSS: the rigid twist.  s.p=q, s2.p=qg ; rest forced by right g-action
    setc(s, p, q);   setc(s, pg, qg)     # s.pg=(s.p).g=qg
    setc(s2, p, qg); setc(s2, pg, q)     # s2.pg=(s2.p).g=q

    ident = {"a": ida, "x": idx, "y": idy}
    return Cat("RIGID-TWIST a->x->y (MINIMAL closure obstruction, 10 morphisms)",
               objs, arrows, src, dst, comp, ident)


if __name__ == "__main__":
    print("Building candidate category and checking the category axioms...")
    C = build_counterexample()   # Cat() raises if not associative/unital
    print("  -> It IS a valid small category (associativity + units verified).")
    print()
    print("Freeness of every hom over its SOURCE endomorphism monoid:")
    for a in C.objs:
        for b in C.objs:
            h = C.hom(a, b)
            if h:
                print(f"   Hom({a},{b}) size {len(h):>2}  |End({a})|={len(C.end(a))}"
                      f"  free? {is_free_right(C,a,b)}  "
                      f"#orbits={len(right_orbits(C,a,b))}")
    print("  ALL homs free over source-End:", all_homs_free(C))
    print()
    exists = closed_transversal_exists(C)
    print("CLOSED transversal subcategory exists:", exists)
    if not exists:
        print()
        print("  *** CONFIRMED: every hom is FREE, yet NO closed transversal. ***")
        print("  *** Closure is genuinely EXTRA beyond objectwise freeness.   ***")
        print("  *** => the single-category ZS criterion is TWO-LEVEL.        ***")
        # show explicitly the conflict: enumerate the (few) transversal choices
        print()
        print("  Enumerating all transversal choices and why each fails closure:")
        import itertools
        orbits = {(a,b): right_orbits(C,a,b) for a in C.objs for b in C.objs}
        # free vars: T(a,x) 1 orbit -> 2 choices; T(x,y) 2 orbits -> 2x2; T(a,y) 1 orbit -> 2
        Tax = orbits[("a","x")][0]
        Txy0, Txy1 = orbits[("x","y")]
        Tay = orbits[("a","y")][0]
        for cax in Tax:
            for c0 in Txy0:
                for c1 in Txy1:
                    for cay in Tay:
                        # check s.p-type closure: cxy o cax in T(a,y)?
                        bad = []
                        for cxy in (c0, c1):
                            comp = C.compose(cxy, cax)
                            if comp != cay:
                                bad.append((cxy, cax, comp))
                        status = "CLOSED" if not bad else f"fails: {bad}"
                        print(f"    T(a,x)={cax} T(x,y)={{{c0},{c1}}} T(a,y)={cay}: {status}")
    else:
        print("  (candidate closed after all - design needs revisiting)")
