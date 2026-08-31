"""
groupoid_zs.py
==============
GROUPOID-base instance of the Zappa-Szep merge obstruction [omega] in H^2(Sk_C; D).

Question (PROVE 2026-07-24): when the base category presented by the directed
container is a GROUPOID (every morphism invertible), is the merge obstruction
forced to vanish?  The seed conjecture said "connected groupoid => Sk_C
contractible => [omega]=0 automatically".

This script REFUTES the strong conjecture and pins the correct dividing line.

A connected groupoid is NOT contractible: it is a K(Gamma,1) for its vertex group
Gamma, so H^2(Sk_C; D) = H^2(Gamma; M) is GROUP COHOMOLOGY of the vertex group,
generally nonzero.

We realise the ZS setup with a ONE-OBJECT groupoid base = a group.  Take a finite
group K, a normal abelian subgroup D (the "internal relabelings", the right factor).
Then:
  * orbits of the right D-action on K = left cosets kD ;
  * Sk_C = K/D  (a one-object connected groupoid = the quotient group Gamma) ;
  * the vertex-group presheaf 𝒟 = D as a Gamma-module (conjugation action) ;
  * the ZS defect 2-cochain omega_T = the Schreier factor set of the extension
        1 -> D -> K -> Gamma -> 1 ;
  * a transversal "closes" (G holds)  <=>  its reps form a subgroup = a COMPLEMENT
        of D  <=>  the extension splits  <=>  [omega]=0 in H^2(Gamma; D).

So:  #(closing transversals) = #(complements of D in K).

Examples:
  (A) codiscrete groupoid on 2 objects, D=identities:   contractible, merges.
  (B) K = Z/4,  D = <2> = Z/2:      Sk_C = Z/2 groupoid, NONSPLIT -> [omega] != 0.  ** REFUTES **
  (C) K = Z/2 x Z/2, D = <(1,0)>:   Sk_C = Z/2 groupoid, SPLIT   -> [omega] = 0.   (merges)
  (D) K = Q8, D = center <-1>:      Sk_C = (Z/2)^2 groupoid, NONSPLIT -> [omega]!=0.
  (E) K = Z/6, D = Z/3:             Sk_C = Z/2 groupoid, coprime -> SPLIT (Schur-Zassenhaus).

We machine-check (via the model-independent #complements count AND, for the
Z/2-coefficient cases, an explicit F2 bar complex with the CORRECT restriction
maps phi) that groupoid bases CAN obstruct.
"""

import sys, itertools
sys.path.insert(0, "/home/agent/projects/scratch")
from two_atoms_check import Cat
from cohomology_holonomy import (orbits_into, orbit_of, generators_of, is_generator,
                                 L_holds, all_transversals, defect, closes,
                                 trivial_left_action, abelian_vertex_groups, okey,
                                 orbit_lookup, f2_rank)

# ---------------------------------------------------------------------------
# group -> one-object category
# ---------------------------------------------------------------------------

def group_cat(name, elems, mul, e):
    """One-object category (object '*') from a finite group (elems, mul, identity e).
    mul(g,h) = g*h.  Category composition comp[(g,h)] = g . h = g*h (g after h)."""
    objs = ["*"]
    arrows = list(elems)
    src = {g: "*" for g in elems}
    dst = {g: "*" for g in elems}
    ident = {"*": e}
    comp = {}
    for g in elems:
        for h in elems:
            comp[(g, h)] = mul(g, h)
    return Cat(name, objs, arrows, src, dst, comp, ident)

def Zn(n):
    elems = list(range(n))
    return group_cat(f"Z/{n}", elems, lambda a, b: (a + b) % n, 0)

def ZmxZn(m, n):
    elems = [(a, b) for a in range(m) for b in range(n)]
    return group_cat(f"Z/{m} x Z/{n}", elems,
                     lambda x, y: ((x[0] + y[0]) % m, (x[1] + y[1]) % n), (0, 0))

def Q8():
    # quaternion group {1,-1,i,-i,j,-j,k,-k} as strings; multiplication table
    e = "1"
    elems = ["1", "-1", "i", "-i", "j", "-j", "k", "-k"]
    neg = {"1": "-1", "-1": "1", "i": "-i", "-i": "i", "j": "-j", "-j": "j", "k": "-k", "-k": "k"}
    base = {("i", "i"): "-1", ("j", "j"): "-1", ("k", "k"): "-1",
            ("i", "j"): "k", ("j", "k"): "i", ("k", "i"): "j",
            ("j", "i"): "-k", ("k", "j"): "-i", ("i", "k"): "-j"}
    def sign(x):
        return -1 if x.startswith("-") else 1
    def core(x):
        return x[1:] if x.startswith("-") else x
    def mul(x, y):
        s = sign(x) * sign(y)
        cx, cy = core(x), core(y)
        if cx == "1":
            r = cy
        elif cy == "1":
            r = cx
        else:
            r = base[(cx, cy)]
        # apply overall sign s to r
        rs = sign(r) * s
        cr = core(r)
        return cr if rs == 1 else ("-" + cr if cr != "1" else "-1")
    return group_cat("Q8", elems, mul, e)

def subgroup_D(K, gens_and_elems):
    """D = a given wide subcategory = subset of arrows (must contain identity, closed)."""
    return set(gens_and_elems)

# ---------------------------------------------------------------------------
# structural report (model-independent)
# ---------------------------------------------------------------------------

def report(K, D, expect=None):
    print("=" * 74)
    print("K =", K.name, "  |K| =", len(K.arrows), "  D =", sorted(map(str, D)), " |D| =", len(D))
    # D a subgroup / wide subcat?  (identity + closure)
    idg = K.ident["*"]
    closedD = all(K.compose(g, h) in D for g in D for h in D) and idg in D
    print("  D wide subcat (contains id, closed):", closedD)
    # abelian vertex groups (H)(i)
    print("  (H)(i) abelian vertex groups:", abelian_vertex_groups(K, D))
    print("  (L) each Hom(-,b) free over D:", L_holds(K, D))
    Ts = list(all_transversals(K, D))
    # (H)(ii) trivial left action on the natural transversal
    hii, fails = trivial_left_action(K, D, Ts[0])
    print("  (H)(ii) trivial left action:", hii, ("" if hii else f"(fails: {fails[:3]})"))
    # Sk_C = orbit category: objects, and #morphisms = #orbits
    orbs = orbits_into(K, D, "*")
    print(f"  Sk_C = K/D : one object, {len(orbs)} morphisms (= |K/D| = {len(K.arrows)//len(D)})")
    # #closing transversals = #complements = split iff > 0
    nclose = sum(1 for T in Ts if closes(K, D, T))
    print(f"  #transversals = {len(Ts)},  #CLOSING (= #complements of D) = {nclose}")
    verdict = "MERGES  ([omega]=0, extension splits)" if nclose > 0 else "OBSTRUCTED  ([omega]!=0, nonsplit)"
    print("  VERDICT:", verdict)
    if expect is not None:
        assert (nclose > 0) == expect, f"EXPECTED merges={expect}, got nclose={nclose}"
        print("  [expectation matched]")
    return Ts, nclose

# ---------------------------------------------------------------------------
# CORRECTED F2 bar complex WITH restriction maps phi (for Z/2 vertex groups)
# ---------------------------------------------------------------------------

def phi_F2(K, D, rep):
    """Restriction map phi_c : G_* -> G_* along generator c=rep, defined by
    psi o c = c o phi_c(psi), i.e. phi_c(psi) = c^{-1} psi c (conjugation).
    Vertex group G_* = D here has order 2 -> return the F2 scalar (0 or 1) of
    the induced map on the nontrivial element.  For abelian K this is always 1 (id)."""
    G = [m for m in D if K.src[m] == "*" and K.dst[m] == "*"]
    nontriv = [g for g in G if g != K.ident["*"]]
    if not nontriv:
        return 0
    g = nontriv[0]
    # need c^{-1}: find inverse of rep in K
    inv = None
    for x in K.arrows:
        if K.compose(rep, x) == K.ident["*"] and K.compose(x, rep) == K.ident["*"]:
            inv = x; break
    conj = K.compose(K.compose(inv, g), rep)   # c^{-1} g c
    return 1 if conj == g else 0   # (=1 if phi=id, i.e. fixes the nontrivial elt)

def bar_H2_F2(K, D, Tref):
    """H^2 of the one-object orbit category (= Gamma = K/D) with Z/2 coefficient
    presheaf, CORRECT phi.  Only valid when every vertex group has order <= 2."""
    orbs = list(orbits_into(K, D, "*"))
    def is_unit(o):
        return any(m == K.ident["*"] for m in o)
    def okeys():
        return [okey(o) for o in orbs]
    allk = {okey(o): o for o in orbs}
    unit = {k: is_unit(allk[k]) for k in allk}
    grp2 = len([m for m in D if K.src[m] == "*" and K.dst[m] == "*"]) == 2
    # phi is a single scalar (same map along every generator, conjugation); for
    # abelian K it is 1.  Compute along the natural rep of each orbit.
    def orb_of(f): return okey(orbit_lookup(K, D, f))
    def star(k2, k1):
        c1 = Tref[allk[k1]]; c2 = Tref[allk[k2]]
        return orb_of(K.compose(c2, c1))
    def phi_of(k1):
        return phi_F2(K, D, Tref[allk[k1]])
    nonunit = [k for k in allk if not unit[k]]
    C1 = nonunit[:]                       # source group = D (order 2) at the single object
    C2 = [(k2, k1) for k1 in nonunit for k2 in nonunit]
    C3 = [(k3, k2, k1) for k1 in nonunit for k2 in nonunit for k3 in nonunit]
    i1 = {k: i for i, k in enumerate(C1)}
    i2 = {p: i for i, p in enumerate(C2)}
    # d1: (d1 h)(o2,o1) = phi_{o1}(h(o2)) - h(o2*o1) + h(o1)
    d1 = []
    for (k2, k1) in C2:
        row = [0] * len(C1)
        if k2 in i1 and phi_of(k1): row[i1[k2]] ^= 1
        s = star(k2, k1)
        if s in i1: row[i1[s]] ^= 1
        if k1 in i1: row[i1[k1]] ^= 1
        d1.append(row)
    # d2: (d2 w)(o3,o2,o1)=phi_{o1}(w(o3,o2)) - w(o3*o2,o1)+ w(o3,o2*o1) - w(o2,o1)
    d2 = []
    for (k3, k2, k1) in C3:
        row = [0] * len(C2)
        if (k3, k2) in i2 and phi_of(k1): row[i2[(k3, k2)]] ^= 1
        s32 = star(k3, k2); s21 = star(k2, k1)
        if (s32, k1) in i2: row[i2[(s32, k1)]] ^= 1
        if (k3, s21) in i2: row[i2[(k3, s21)]] ^= 1
        if (k2, k1) in i2: row[i2[(k2, k1)]] ^= 1
        d2.append(row)
    rank_d2 = f2_rank(d2) if d2 else 0
    rank_d1 = f2_rank(d1) if d1 else 0
    dimZ2 = len(C2) - rank_d2
    dimB2 = rank_d1
    dimH2 = dimZ2 - dimB2
    # omega vector for Tref
    om, _ = defect(K, D, Tref)
    vec = [0] * len(C2)
    for (c2, c1), val in om.items():
        k2 = okey(orbit_lookup(K, D, c2)); k1 = okey(orbit_lookup(K, D, c1))
        if (k2, k1) in i2:
            vec[i2[(k2, k1)]] = 0 if val == K.ident["*"] else 1
    # in B^2 ?
    inB = (f2_rank(d1) == f2_rank(d1 + [vec])) if d1 else (sum(vec) == 0)
    # d2.d1==0 check
    import numpy as np
    ok_chain = True
    if d1 and d2:
        ok_chain = not ((np.array(d2) % 2).dot(np.array(d1) % 2) % 2).any()
    return dict(C1=C1, C2=C2, C3=C3, dimH2=dimH2, dimZ2=dimZ2, dimB2=dimB2,
                omega=vec, inB2=inB, phi=phi_of(C1[0]) if C1 else None, chain0=ok_chain)


def cohom_report(K, D, Tref):
    r = bar_H2_F2(K, D, Tref)
    print(f"  [F2 bar complex]  dim C1,C2,C3 = {len(r['C1'])},{len(r['C2'])},{len(r['C3'])}"
          f"   phi(scalar)={r['phi']}   d2.d1=0: {r['chain0']}")
    print(f"     dim Z^2={r['dimZ2']}  dim B^2={r['dimB2']}  dim H^2={r['dimH2']}  |H^2|={2**r['dimH2']}")
    print(f"     omega_T = {r['omega']}   in B^2? {r['inB2']}   => [omega]{'=0' if r['inB2'] else '!=0 (GENERATOR)'}")
    return r


# ---------------------------------------------------------------------------
# codiscrete groupoid on 2 objects (contractible), D = identities
# ---------------------------------------------------------------------------

def codiscrete2():
    """Objects 0,1; exactly one iso in each hom-set. Equivalent to terminal cat 1."""
    objs = ["0", "1"]
    a = "a"      # 0->1
    b = "b"      # 1->0  (= a^{-1})
    i0, i1 = "i0", "i1"
    arrows = [i0, i1, a, b]
    src = {i0: "0", i1: "1", a: "0", b: "1"}
    dst = {i0: "0", i1: "1", a: "1", b: "0"}
    ident = {"0": i0, "1": i1}
    comp = {}
    def setc(g, f, r): comp[(g, f)] = r
    for m in arrows: setc(ident[dst[m]], m, m); setc(m, ident[src[m]], m)
    setc(b, a, i0); setc(a, b, i1)   # a b = id, b a = id
    return Cat("codiscrete groupoid 2", objs, arrows, src, dst, comp, ident), {i0, i1}


# ===========================================================================
if __name__ == "__main__":
    print("#" * 74)
    print("# GROUPOID-BASE ZAPPA-SZEP MERGE OBSTRUCTION")
    print("#" * 74)

    # (A) codiscrete groupoid: contractible => merges
    CD, Dcd = codiscrete2()
    print("\n(A) CODISCRETE groupoid on 2 objects (contractible, Gamma=1), D=identities")
    Ts = list(all_transversals(CD, Dcd))
    ncl = sum(1 for T in Ts if closes(CD, Dcd, T))
    print(f"    (L): {L_holds(CD,Dcd)}   #transversals={len(Ts)}  #closing={ncl}  ->",
          "MERGES" if ncl > 0 else "OBSTRUCTED")

    # (B) Z/4 >= Z/2  : NONSPLIT -> obstructed  ** the refutation **
    K = Zn(4); D = subgroup_D(K, {0, 2})
    print("\n(B) K=Z/4, D=<2>=Z/2  (Sk_C = Z/2 groupoid)   ** REFUTATION **")
    Ts, ncl = report(K, D, expect=False)
    cohom_report(K, D, Ts[0])

    # (C) Z/2 x Z/2 >= Z/2 : SPLIT -> merges (SAME base groupoid Z/2)
    K = ZmxZn(2, 2); D = subgroup_D(K, {(0, 0), (1, 0)})
    print("\n(C) K=Z/2 x Z/2, D=<(1,0)>=Z/2  (Sk_C = Z/2 groupoid, but SPLIT)")
    Ts, ncl = report(K, D, expect=True)
    cohom_report(K, D, Ts[0])

    # (D) Q8 >= center Z/2 : NONSPLIT -> obstructed over a rank-2 groupoid base
    K = Q8(); D = subgroup_D(K, {"1", "-1"})
    print("\n(D) K=Q8, D=Z(Q8)=<-1>=Z/2  (Sk_C = (Z/2)^2 groupoid, NONSPLIT)")
    Ts, ncl = report(K, D, expect=False)
    cohom_report(K, D, Ts[0])

    # (E) Z/6 >= Z/3 : coprime => Schur-Zassenhaus split -> merges
    K = Zn(6); D = subgroup_D(K, {0, 2, 4})
    print("\n(E) K=Z/6, D=<2>=Z/3  (Sk_C = Z/2 groupoid, coprime orders => splits)")
    report(K, D, expect=True)   # (no F2 cohom: vertex group is Z/3)

    print("\n" + "#" * 74)
    print("# SUMMARY: groupoid base does NOT force [omega]=0.")
    print("#   Z/4>=Z/2 and Q8>=Z/2 are connected-groupoid bases with [omega]!=0.")
    print("#   The obstruction = the Schreier extension class of 1->D->K->Sk_C->1.")
    print("#   It vanishes for ALL D iff cd(Sk_C)<=1 (free groupoid); torsion can obstruct.")
    print("#" * 74)
