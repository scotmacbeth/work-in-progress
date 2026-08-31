"""
zs_cocycle_check.py
===================
Two jobs:

(A) VERIFY the explicit Zappa-Szep cocycle extraction and that the matched-pair
    axioms ZS1-ZS4 (+ units) hold, on concrete categories that DO admit a closed
    transversal subcategory T (source orientation, E = endomorphisms). Sanity
    check for the by-hand derivation: ZS axioms <=> associativity.

(B) SETTLE the closure question. Theorem main (proven) says: at each (a,b),
    unique factorization f=t.e exists  <=>  Hom(a,b) free as right End(a)-set.
    But the global ZS PRODUCT needs T to be a *closed wide subcategory*. Question:
    does freeness of every hom guarantee a closed transversal can be CHOSEN?
    We brute-force search small categories: all-homs-free but NO closed transversal
    would prove closure is genuinely extra (two-level theorem).

Reuses the Cat machinery from two_atoms_check.py.
"""

import sys, itertools
sys.path.insert(0, "/home/agent/projects/scratch")
from two_atoms_check import (Cat, two_object_general, TRIV, Z2mon, Z3mon, IDEM,
                             monoid_cat, chain, comm_square, Zn)


# ---------------------------------------------------------------------------
# Orbits / freeness utilities (source orientation: right End(src)-action)
# ---------------------------------------------------------------------------

def right_orbits(C, a, b):
    """End(a)-orbits of Hom(a,b) under f -> f.e = f o e. Returns list of frozensets."""
    E = C.end(a)
    H = C.hom(a, b)
    seen = set(); orbits = []
    for f in H:
        if f in seen:
            continue
        orb = frozenset(C.compose(f, e) for e in E)
        orbits.append(orb)
        seen |= orb
    return orbits

def is_free_right(C, a, b):
    """Is Hom(a,b) free as a right End(a)-set? (each orbit has size |End(a)|,
    and the action map orbit is free i.e. f.e=f.e' => e=e')."""
    E = C.end(a)
    H = C.hom(a, b)
    if not H:
        return True
    for f in H:
        images = [C.compose(f, e) for e in E]
        if len(set(images)) != len(E):   # stabiliser nontrivial -> not free
            return False
    # partition into orbits each size |E| (automatic if all stabilisers trivial
    # AND orbits disjoint, which they are for a right action)
    return True

def all_homs_free(C):
    return all(is_free_right(C, a, b) for a in C.objs for b in C.objs)


# ---------------------------------------------------------------------------
# (B) Closed-transversal existence search
# ---------------------------------------------------------------------------

def closed_transversal_exists(C, return_one=False):
    """Search over all choices of one representative per End(a)-orbit of each
    Hom(a,b) for a family T that forms a WIDE SUBCATEGORY:
      - id_a in T(a,a) for all a,
      - t2 in T(b,c), t1 in T(a,b)  =>  t2 o t1 in T(a,c).
    Returns True/False (or a witnessing T if return_one)."""
    if not all_homs_free(C):
        return (False, None) if return_one else False
    objs = C.objs
    # orbit lists per (a,b)
    orbits = {}
    for a in objs:
        for b in objs:
            orbits[(a, b)] = right_orbits(C, a, b)
    # identity must be the chosen rep at (a,a) in its own orbit; fix it.
    # choice variables: for each (a,b) and each orbit, pick an element.
    keys = []
    for a in objs:
        for b in objs:
            for oi, orb in enumerate(orbits[(a, b)]):
                # if this is the orbit containing id_a (a==b), force id_a
                if a == b and C.ident[a] in orb:
                    continue  # forced, not a free variable
                keys.append((a, b, oi))
    # forced choices dict
    def base_choice():
        ch = {}
        for a in objs:
            for b in objs:
                for oi, orb in enumerate(orbits[(a, b)]):
                    if a == b and C.ident[a] in orb:
                        ch[(a, b, oi)] = C.ident[a]
        return ch
    domains = []
    for (a, b, oi) in keys:
        domains.append(list(orbits[(a, b)][oi]))
    # brute force product (small)
    for combo in itertools.product(*domains):
        ch = base_choice()
        for k, val in zip(keys, combo):
            ch[k] = val
        # assemble T set and per-hom transversal
        Tset = set(ch.values())
        # closure check
        ok = True
        # composition closure
        for s in list(Tset):
            for t in list(Tset):
                if C.dst[t] != C.src[s]:
                    continue
                if C.compose(s, t) not in Tset:
                    ok = False; break
            if not ok:
                break
        if not ok:
            continue
        # also verify it's a genuine transversal: |T(a,b)| = #orbits, action map bij
        # (already guaranteed: one rep per orbit, free). Good.
        if return_one:
            return True, ch
        return True
    return (False, None) if return_one else False


# ---------------------------------------------------------------------------
# (A) Cocycle extraction + ZS axiom verification on a closed transversal
# ---------------------------------------------------------------------------

def extract_cocycle(C, Tchoice):
    """Given a closed transversal (dict orbit-key -> rep, OR just a set), build:
      - Tset, and per-hom transversal membership
      - factor(f) = (t, e) with t in T(src,dst), e in End(src), f = t o e (unique)
      - leftact[(e_b, t)] = {}^{e_b} t  in T          (e_b in End(dst t))
      - restr[(e_b, t)]   = e_b^{t}     in End(src t)
    from the defining relation  e_b o t = ({}^{e_b}t) o (e_b^{t}).
    """
    if isinstance(Tchoice, dict):
        Tset = set(Tchoice.values())
    else:
        Tset = set(Tchoice)

    # factorization: for f:a->b, find unique t in T(a,b), e in End(a) with t o e = f
    def factor(f):
        a, b = C.src[f], C.dst[f]
        E = C.end(a)
        cands = []
        for t in Tset:
            if C.src[t] != a or C.dst[t] != b:
                continue
            for e in E:
                if C.compose(t, e) == f:
                    cands.append((t, e))
        assert len(cands) == 1, f"factorization not unique for {f}: {cands}"
        return cands[0]

    leftact = {}; restr = {}
    for t in Tset:
        a, b = C.src[t], C.dst[t]
        for eb in C.end(b):           # endo at target of t
            f = C.compose(eb, t)      # eb o t : a -> b
            tt, ee = factor(f)        # = ({}^{eb}t) o (eb^t)
            leftact[(eb, t)] = tt
            restr[(eb, t)] = ee
    return Tset, factor, leftact, restr


def verify_ZS_axioms(C, Tset, leftact, restr):
    """Check ZS1-ZS4 + units on all applicable elements. Returns dict of pass/fail."""
    res = {"ZS1": True, "ZS2": True, "ZS3": True, "ZS4": True,
           "unitL": True, "unitR": True, "defrel": True}
    Ts = list(Tset)

    def la(e, t):  # {}^e t
        return leftact[(e, t)]
    def rs(e, t):  # e^t
        return restr[(e, t)]

    # defining relation: e o t == (la(e,t)) o (rs(e,t))
    for t in Ts:
        b = C.dst[t]
        for e in C.end(b):
            lhs = C.compose(e, t)
            rhs = C.compose(la(e, t), rs(e, t))
            if lhs != rhs:
                res["defrel"] = False

    # units: {}^id t = t,  id^t = id_src ;  {}^e id = id ,  e^id = e
    for t in Ts:
        a, b = C.src[t], C.dst[t]
        if la(C.ident[b], t) != t:        res["unitL"] = False
        if rs(C.ident[b], t) != C.ident[a]: res["unitL"] = False
    for a in C.objs:
        ida = C.ident[a]
        for e in C.end(a):
            # t = id_a is in T(a,a); {}^e id_a should be id_a, e^{id_a}=e
            if (e, ida) in leftact:
                if la(e, ida) != ida:  res["unitR"] = False
                if rs(e, ida) != e:    res["unitR"] = False

    # ZS1: {}^e (t2 o t1) = ({}^e t2) o ({}^{e^{t2}} t1)
    # ZS4: e^{t2 o t1} = (e^{t2})^{t1}
    for t1 in Ts:
        for t2 in Ts:
            if C.dst[t1] != C.src[t2]:
                continue
            t21 = C.compose(t2, t1)
            if t21 not in Tset:
                continue  # needs closure; skip if not (shouldn't happen for closed T)
            c = C.dst[t2]
            for e in C.end(c):
                # ZS1
                lhs1 = la(e, t21)
                et2 = rs(e, t2)
                rhs1 = C.compose(la(e, t2), la(et2, t1))
                if lhs1 != rhs1:
                    res["ZS1"] = False
                # ZS4
                lhs4 = rs(e, t21)
                rhs4 = rs(rs(e, t2), t1)
                if lhs4 != rhs4:
                    res["ZS4"] = False

    # ZS2: {}^{e2 o e1} t = {}^{e2}({}^{e1} t)
    # ZS3: (e2 o e1)^t = (e2^{ {}^{e1} t }) o (e1^t)
    for t in Ts:
        b = C.dst[t]
        E = C.end(b)
        for e1 in E:
            for e2 in E:
                e21 = C.compose(e2, e1)   # e2 o e1 in End(b)
                # ZS2
                lhs2 = la(e21, t)
                rhs2 = la(e2, la(e1, t))
                if lhs2 != rhs2:
                    res["ZS2"] = False
                # ZS3
                lhs3 = rs(e21, t)
                rhs3 = C.compose(rs(e2, la(e1, t)), rs(e1, t))
                if lhs3 != rhs3:
                    res["ZS3"] = False
    return res


# ---------------------------------------------------------------------------
# Builders for candidate categories (incl. cyclic-shape / groupoid cases)
# ---------------------------------------------------------------------------

def connected_groupoid_Z2():
    """2-object connected groupoid, vertex group Z/2. a≅b, Aut=Z/2.
    Morphisms x->y indexed by Z/2 (the 'translation' composed with a group elt).
    Compose: arrows are (y<-x, g) with g in Z/2; (z<-y,h)o(y<-x,g)=(z<-x, h+g)."""
    objs = ["a", "b"]
    Z2 = [0, 1]
    arrows = []
    src = {}; dst = {}
    for x in objs:
        for y in objs:
            for g in Z2:
                t = (y, x, g)  # arrow x -> y carrying group elt g
                arrows.append(t); src[t] = x; dst[t] = y
    comp = {}
    for g2 in arrows:
        for f in arrows:
            if dst[f] != src[g2]:
                continue
            # g2: y->z (z,y,h), f: x->y (y,x,g) => (z,x,h+g)
            (z, y2, h) = g2; (y1, x, g) = f
            comp[(g2, f)] = (z, x, (h + g) % 2)
    ident = {x: (x, x, 0) for x in objs}
    return Cat("Connected groupoid 2 obj, Aut=Z/2", objs, arrows, src, dst, comp, ident)


def two_obj_two_way_idem():
    """a,b with p:a->b, q:b->a, qp=:e in End(a), pq=:e' in End(b), and we try to
    make e,e' nontrivial idempotents (non-iso 2-cycle)."""
    # End(a)={1,e}, End(b)={1,e'}, e=qp, e'=pq, idempotent: e^2=e.
    # Hom(a,b)={p, e'p=p e?}, ... we build via explicit table and let Cat verify.
    objs = ["a", "b"]
    # name morphisms
    ida, ea = ("a", 0), ("a", 1)   # End(a)={ida, ea=qp}, ea idempotent
    idb, eb = ("b", 0), ("b", 1)   # End(b)={idb, eb=pq}
    p = ("p",); q = ("q",)
    arrows = [ida, ea, idb, eb, p, q]
    src = {ida:"a",ea:"a",idb:"b",eb:"b",p:"a",q:"b"}
    dst = {ida:"a",ea:"a",idb:"b",eb:"b",p:"b",q:"a"}
    comp = {}
    # End(a): {ida,ea}, ea*ea=ea (idempotent), ida unit
    comp[(ida,ida)]=ida; comp[(ida,ea)]=ea; comp[(ea,ida)]=ea; comp[(ea,ea)]=ea
    comp[(idb,idb)]=idb; comp[(idb,eb)]=eb; comp[(eb,idb)]=eb; comp[(eb,eb)]=eb
    # p:a->b, q:b->a. qp=ea, pq=eb.
    comp[(q,p)]=ea   # q o p : a->a
    comp[(p,q)]=eb   # p o q : b->b
    # p o ida = p, idb o p = p, etc (units)
    comp[(p,ida)]=p; comp[(idb,p)]=p
    comp[(q,idb)]=q; comp[(ida,q)]=q
    # p o ea : a->b.  p o ea = p o (q o p) = (p o q) o p = eb o p.
    # need eb o p and p o ea defined. Let's set p o ea =: pea, eb o p =: ebp, equal.
    # Introduce as new arrow? That'd enlarge Hom(a,b). Try to keep Hom(a,b)={p}?
    # p o ea = p o q o p = eb o p. If we want Hom(a,b)={p} only, need p o ea = p
    # and eb o p = p. Then ea acts trivially on right of p, eb trivially on left.
    comp[(p,ea)]=p; comp[(eb,p)]=p
    comp[(q,eb)]=q; comp[(ea,q)]=q
    # check ea o ea = ea: (qp)(qp)=q(pq)p=q eb p = q (eb p)=q p = ea. consistent with eb p=p. ok
    ident = {"a":ida,"b":idb}
    try:
        return Cat("2-obj idempotent 2-cycle (qp=ea,pq=eb idemp, Hom={p})",
                   objs, arrows, src, dst, comp, ident)
    except AssertionError as ex:
        print("  [build failed]", ex); return None


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

def report(C):
    print("=" * 72)
    print("CATEGORY:", C.name)
    for a in C.objs:
        for b in C.objs:
            h = C.hom(a, b)
            if h:
                print(f"   Hom({a},{b})={h}  free/End({a})? {is_free_right(C,a,b)}")
    af = all_homs_free(C)
    print("   ALL homs free over source-End:", af)
    if not af:
        print("   -> Level-1 (factorization) already fails somewhere; skip closure.")
        return
    exists, T = closed_transversal_exists(C, return_one=True)
    print("   CLOSED transversal subcategory exists:", exists)
    if exists:
        Tset, factor, leftact, restr = extract_cocycle(C, T)
        res = verify_ZS_axioms(C, Tset, leftact, restr)
        print("   chosen T:", sorted(Tset, key=str))
        print("   ZS axiom verification:", res)
        if all(res.values()):
            print("   >> ALL matched-pair axioms hold (ZS1-ZS4+units+defrel). C = T ⋈ E. ✓")
        else:
            print("   >> SOME axiom FAILED — contradicts derivation, investigate!")
    else:
        print("   >> all homs FREE but NO closed transversal:")
        print("   >> CLOSURE IS GENUINELY EXTRA. Two-level theorem confirmed.")


if __name__ == "__main__":
    cats = []
    # Closed cases (should pass ZS axioms):
    cats.append(connected_groupoid_Z2())
    cats.append(chain(3))
    cats.append(comm_square())
    cats.append(Zn(2)); cats.append(Zn(3))
    cats.append(monoid_cat("S3? no - Z/4", *( [0,1,2,3], )) if False else Zn(4))
    # source-loop torsor (free) 2-object cases
    from two_atoms_check import chain_with_loop_at_src
    cats.append(chain_with_loop_at_src("Z/2", Z2mon()))
    cats.append(chain_with_loop_at_src("Z/3", Z3mon()))
    c = two_obj_two_way_idem()
    if c: cats.append(c)
    for C in cats:
        if C is not None:
            report(C)
