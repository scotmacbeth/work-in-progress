"""
End-to-end test of the pairwise (L wedge G) criterion.

Given a finite category K and a designated WIDE subcategory D (a set of arrow
names closed under comp + containing all identities), decide whether there is a
wide subcategory C making (C,D) a strict factorization system:
    every f in K factors UNIQUELY as f = c o d, c in C, d in D.

Verify:  (SFS-C exists)  <=>  (L) every right D-module Hom_K(-,b) is FREE  AND
         (G) free bases can be chosen forming a wide subcategory C.

Free D-module: M = Hom_K(-,b): D^op -> Set, with x in M(a), d:a'->a in D acting
by x.d = x o d in M(a').  M is free with basis B (B_m subset M(m)) iff every
x in M(a) is UNIQUELY  c o d  with c in B_m (c:m->b) and d in D(a,m).
"""
from itertools import combinations, product as iproduct
from pairwise_zs_check import FinCat


def wide_subcats(K):
    """All wide subcategories of K (as frozensets of arrow names)."""
    ids = set(K.ident[o] for o in K.objects)
    nonid = [a for a in K.arrows if a not in ids]
    res = []
    for r in range(len(nonid) + 1):
        for sub in combinations(nonid, r):
            S = set(ids) | set(sub)
            # closed under composition?
            ok = True
            for g in S:
                for f in S:
                    if K.cod(f) == K.dom(g):
                        if K.compose(g, f) not in S:
                            ok = False; break
                if not ok: break
            if ok:
                res.append(frozenset(S))
    return res


def is_sfs(K, Cset, Dset):
    """Is every f in K uniquely c o d, c in C, d in D?"""
    for f in K.arrows:
        cnt = 0
        for c in Cset:
            for d in Dset:
                if K.cod(d) != K.dom(c): continue
                if K.dom(d) != K.dom(f) or K.cod(c) != K.cod(f): continue
                if K.compose(c, d) == f:
                    cnt += 1
        if cnt != 1:
            return False
    return True


def Dmodule_is_free(K, Dset, b):
    """Return list of all bases B (as frozensets of K-arrows with target b) s.t.
       every f:a->b factors uniquely as c o d, c in B, d in D.  Empty list => not free."""
    elems = [f for f in K.arrows if K.cod(f) == b]   # underlying set of M = Hom_K(-,b)
    bases = []
    # candidate basis = subset of elems; test unique factorization through it.
    for r in range(len(elems) + 1):
        for B in combinations(elems, r):
            Bset = set(B)
            ok = True
            for f in elems:
                a = K.dom(f)
                cnt = 0
                for c in Bset:
                    m = K.dom(c)            # c: m->b
                    for d in Dset:
                        if K.dom(d) != a or K.cod(d) != m: continue
                        if K.compose(c, d) == f:
                            cnt += 1
                if cnt != 1:
                    ok = False; break
            if ok:
                bases.append(frozenset(Bset))
    return bases


def criterion(K, Dset, verbose=False):
    # (L): each Hom_K(-,b) free
    L = True
    basis_choices = {}
    for b in K.objects:
        bs = Dmodule_is_free(K, Dset, b)
        basis_choices[b] = bs
        if not bs:
            L = False
    if not L:
        if verbose: print("   (L) FAILS")
        return False, L, None
    # (G): choose one basis per b s.t. union is a wide subcategory
    ids = set(K.ident[o] for o in K.objects)
    for combo in iproduct(*[basis_choices[b] for b in K.objects]):
        C = set().union(*combo)
        if not ids <= C:        # must contain identities
            continue
        # closed under composition?
        closed = True
        for g in C:
            for f in C:
                if K.cod(f) == K.dom(g) and K.compose(g, f) not in C:
                    closed = False; break
            if not closed: break
        if closed:
            if verbose: print("   (L) holds, (G) holds, C =", sorted(C))
            return True, L, C
    if verbose: print("   (L) holds but (G) FAILS")
    return False, L, None


def full_check(K, Dset, label):
    assert K.check_category(verbose=True), f"{label}: K not a category"
    # ground truth: does ANY wide C give an SFS with D?
    truth = any(is_sfs(K, C, Dset) for C in wide_subcats(K))
    crit, L, C = criterion(K, Dset, verbose=False)
    status = "OK" if crit == truth else "*** MISMATCH ***"
    print(f"[{label}] SFS-exists(bruteforce)={truth}  criterion(L&G)={crit}  "
          f"(L)={L}  {status}")
    return crit == truth


# ---------- Example builders ----------

def walking_retract():
    """K: split idempotent. Hom(0,0)={id0,e}, Hom(1,1)={id1}, d:0->1, c:1->0,
       e=c o d, d o c=id1, e o e=e."""
    objs = [0, 1]
    arrows = {"id0": (0, 0), "e": (0, 0), "id1": (1, 1), "d": (0, 1), "c": (1, 0)}
    comp = {}
    comp[("id0", "id0")] = "id0"; comp[("id0", "e")] = "e"
    comp[("e", "id0")] = "e"; comp[("e", "e")] = "e"
    comp[("id1", "id1")] = "id1"
    comp[("d", "id0")] = "d"; comp[("id1", "d")] = "d"
    comp[("c", "id1")] = "c"; comp[("id0", "c")] = "c"
    comp[("d", "c")] = "id1"      # d o c = id1
    comp[("c", "d")] = "e"        # c o d = e
    # e = c o d, so d o e = d o c o d = id1 o d = d ; e o c = c o d o c = c o id1 = c
    comp[("d", "e")] = "d"; comp[("e", "c")] = "c"
    ident = {0: "id0", 1: "id1"}
    return FinCat(objs, arrows, comp, ident)


def rigid_twist():
    """The 10-morphism rigid twist (single-category counterexample).
       End(a)={1a,g}, g^2=1a. Hom(a,x)={p,pg}, Hom(x,y)={s,s2}, Hom(a,y)={q,qg}.
       s o p=q, s2 o p=qg ; s o pg=qg, s2 o pg=q ; pg=p o g, qg=q o g."""
    objs = ["a", "x", "y"]
    arrows = {"1a": ("a", "a"), "g": ("a", "a"), "1x": ("x", "x"), "1y": ("y", "y"),
              "p": ("a", "x"), "pg": ("a", "x"), "s": ("x", "y"), "s2": ("x", "y"),
              "q": ("a", "y"), "qg": ("a", "y")}
    comp = {}
    # End(a)=Z2
    comp[("1a", "1a")] = "1a"; comp[("1a", "g")] = "g"; comp[("g", "1a")] = "g"; comp[("g", "g")] = "1a"
    comp[("1x", "1x")] = "1x"; comp[("1y", "1y")] = "1y"
    # identities on the cross arrows
    for f, (d, c) in list(arrows.items()):
        comp[(arrows_id := f, None)] = None  # placeholder removed below
    comp.pop((list(arrows)[0], None), None)
    # do identities properly
    idof = {"a": "1a", "x": "1x", "y": "1y"}
    for f, (d, c) in arrows.items():
        comp[(f, idof[d])] = f
        comp[(idof[c], f)] = f
    # right End(a) action
    comp[("p", "g")] = "pg"; comp[("pg", "g")] = "p"
    comp[("q", "g")] = "qg"; comp[("qg", "g")] = "q"
    # cross composites x->y after a->x
    comp[("s", "p")] = "q"; comp[("s2", "p")] = "qg"
    comp[("s", "pg")] = "qg"; comp[("s2", "pg")] = "q"
    ident = {"a": "1a", "x": "1x", "y": "1y"}
    return FinCat(objs, arrows, comp, ident)


if __name__ == "__main__":
    ok = True

    # 1. walking retract: D = walking arrow {ids, d}. Expect SFS with C={ids,c}.
    K = walking_retract()
    ok &= full_check(K, {"id0", "id1", "d"}, "retract, D={ids,d:0->1}")
    # also D = endomorphisms E = {id0,id1,e}? e is endo at 0. Is that wide+closed? e o e=e yes.
    ok &= full_check(K, {"id0", "id1", "e"}, "retract, D=E endos {ids,e}")

    # 2. rigid twist with D = E (endomorphism subcategory) -> (L) holds, (G) fails.
    K = rigid_twist()
    ok &= full_check(K, {"1a", "g", "1x", "1y"}, "rigidtwist, D=E={1a,g,1x,1y}")

    print("\nALL CONSISTENT:", ok)
