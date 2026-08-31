"""
cohomology_holonomy.py
======================
Is the (G) closure obstruction a COHOMOLOGICAL class?

Given (L) [each Hom_K(-,b) free over wide D], a transversal T (one generator per
orbit, the C-candidate) has a DEFECT 2-cochain:
    c2 . c1 = floor(c2 c1) . omega(c2,c1),   floor(...) in T,  omega in D.
Closure (G)  <=>  omega == identity everywhere.

This script:
  (1) builds the rigid twist (3 obj) and the 4-object pairwise example;
  (2) computes orbits / generators / all valid transversals / defect omega;
  (3) for the rigid twist, builds the ABELIAN BAR COMPLEX over F2 explicitly
      (C^1 -d1-> C^2 -d2-> C^3), checks d2.d1 = 0, computes H^2, and locates [omega];
  (4) tests the 2-cocycle identity on a category WITH a genuine composable
      transversal triple (so the cocycle condition is non-vacuous).
"""

import sys, itertools
sys.path.insert(0, "/home/agent/projects/scratch")
from two_atoms_check import Cat


# ===========================================================================
# Category builders
# ===========================================================================

def rigid_twist():
    """3 objects a,x,y. End(a)=Z/2={id_a,g}. p,pg:a->x; q,qg:a->y; s,s2:x->y.
    s p = q, s2 p = qg (rigid twist). D = End (vertex groups)."""
    objs = ["a", "x", "y"]
    ida, g = "id_a", "g"
    idx, idy = "id_x", "id_y"
    p, pg, q, qg, s, s2 = "p", "pg", "q", "qg", "s", "s2"
    arrows = [ida, g, idx, idy, p, pg, q, qg, s, s2]
    src = {ida:"a",g:"a",idx:"x",idy:"y",p:"a",pg:"a",q:"a",qg:"a",s:"x",s2:"x"}
    dst = {ida:"a",g:"a",idx:"x",idy:"y",p:"x",pg:"x",q:"y",qg:"y",s:"y",s2:"y"}
    ident = {"a":ida,"x":idx,"y":idy}
    comp = {}
    def setc(gg,ff,res): comp[(gg,ff)] = res
    # identities
    for m in arrows:
        setc(ident[dst[m]], m, m); setc(m, ident[src[m]], m)
    # End(a): g^2 = id
    setc(g,g,ida)
    # a->x : p, pg=p o g
    setc(p,g,pg); setc(pg,g,p)
    # a->y : q, qg=q o g
    setc(q,g,qg); setc(qg,g,q)
    # x->y composites
    setc(s,p,q); setc(s2,p,qg); setc(s,pg,qg); setc(s2,pg,q)
    D = {ida,g,idx,idy}   # endomorphism subcategory = vertex groups
    return Cat("rigid twist (3 obj)", objs, arrows, src, dst, comp, ident), D


def pairwise_4obj():
    """4 objects w,a,x,y. As in the pairwise note. D has cross arrows d,gd: w->a."""
    objs = ["w","a","x","y"]
    ms = ["id_w","id_a","id_x","id_y","g",
          "p","pg","q","qg","s","s2",
          "d","gd","pd","pgd","qd","qgd"]
    src = {"id_w":"w","id_a":"a","id_x":"x","id_y":"y","g":"a",
           "p":"a","pg":"a","q":"a","qg":"a","s":"x","s2":"x",
           "d":"w","gd":"w","pd":"w","pgd":"w","qd":"w","qgd":"w"}
    dst = {"id_w":"w","id_a":"a","id_x":"x","id_y":"y","g":"a",
           "p":"x","pg":"x","q":"y","qg":"y","s":"y","s2":"y",
           "d":"a","gd":"a","pd":"x","pgd":"x","qd":"y","qgd":"y"}
    ident = {"w":"id_w","a":"id_a","x":"id_x","y":"id_y"}
    comp = {}
    def setc(gg,ff,res): comp[(gg,ff)] = res
    for m in ms:
        setc(ident[dst[m]], m, m); setc(m, ident[src[m]], m)
    setc("g","g","id_a")
    setc("p","g","pg"); setc("pg","g","p")
    setc("q","g","qg"); setc("qg","g","q")
    setc("s","p","q"); setc("s2","p","qg"); setc("s","pg","qg"); setc("s2","pg","q")
    # cross arrows
    setc("g","d","gd"); setc("g","gd","d")
    setc("p","d","pd"); setc("p","gd","pgd")
    setc("pg","d","pgd"); setc("pg","gd","pd")
    setc("q","d","qd"); setc("q","gd","qgd")
    setc("qg","d","qgd"); setc("qg","gd","qd")
    setc("s","pd","qd"); setc("s2","pd","qgd"); setc("s","pgd","qgd"); setc("s2","pgd","qd")
    D = {"id_w","id_a","id_x","id_y","g","d","gd"}
    return Cat("pairwise 4 obj", objs, ms, src, dst, comp, ident), D


def triple_chain_twist():
    """A category designed to have a composable transversal TRIPLE a->x->y->z,
    with a Z/2 loop at the source a, so the 2-cocycle identity is NON-vacuous.
    Objects a,x,y,z. End(a)=Z/2={id,g}. Single transversal arrow a->x (p), x->y (u),
    y->z (v); all hom-sets into x,y,z from a are free Z/2-orbits; everything strictly
    commutes (no twist) so closure HOLDS -> omega == 0 -> tests cocycle=0 case + d2.d1=0.
    Then we also flip one composite to create a twist and re-test."""
    objs = ["a","x","y","z"]
    # arrows: id's, g; p,pg: a->x ; u: x->y ; v: y->z ;
    #   a->y = u p, with pg-> u pg ; a->z = v u p ...
    # Make x,y,z have trivial End, single transversal each step, free Z/2 orbit from a.
    ms = ["id_a","g","id_x","id_y","id_z",
          "p","pg","u","v",
          "up","upg","vp","vpg",          # a->y : up=u p, upg ; a->z via y: vp = v u p
          ]
    # define a->y = {up,upg}, a->z = {vp,vpg}
    src = {"id_a":"a","g":"a","id_x":"x","id_y":"y","id_z":"z",
           "p":"a","pg":"a","u":"x","v":"y","up":"a","upg":"a","vp":"a","vpg":"a"}
    dst = {"id_a":"a","g":"a","id_x":"x","id_y":"y","id_z":"z",
           "p":"x","pg":"x","u":"y","v":"z","up":"y","upg":"y","vp":"z","vpg":"z"}
    ident = {"a":"id_a","x":"id_x","y":"id_y","z":"id_z"}
    comp = {}
    def setc(gg,ff,res): comp[(gg,ff)] = res
    for m in ms:
        setc(ident[dst[m]], m, m); setc(m, ident[src[m]], m)
    setc("g","g","id_a")
    setc("p","g","pg"); setc("pg","g","p")
    setc("u","p","up"); setc("u","pg","upg")
    setc("up","g","upg"); setc("upg","g","up")
    setc("v","up","vp"); setc("v","upg","vpg")
    setc("vp","g","vpg"); setc("vpg","g","vp")
    # v o u : y->z o x->y need? u:x->y, v:y->z, v u : x->z. Introduce? a->z only via composites.
    # v o (u o p) = (v o u) o p. We must define v o u as x->z arrow. Add vu, vug? Hom(x,z).
    # To keep minimal & strictly-commutative, add vu: x->z with vu o p = vp, vu o pg = vpg,
    # and v o u = vu.
    src["vu"]="x"; dst["vu"]="z"; ms.append("vu")
    setc("id_z","vu","vu"); setc("vu","id_x","vu")
    setc("v","u","vu")
    setc("vu","p","vp"); setc("vu","pg","vpg")
    D = {"id_a","g","id_x","id_y","id_z"}
    return Cat("triple chain (no twist)", objs, ms, src, dst, comp, ident), D


# ===========================================================================
# Orbits, generators, transversals, defect cochain  (general wide D)
# ===========================================================================

def arrows_into(C, b):
    return [m for m in C.arrows if C.dst[m] == b]

def Dcomposable_into(C, D, a):
    """D-arrows with codomain a (so f:a->b can be precomposed: f o d, d:a'->a)."""
    return [d for d in D if C.dst[d] == a]

def orbit_of(C, D, f):
    """Orbit of f:a->b under right D-action f -> f o d (d in D, d: a'->a).
    Equivalence generated by f ~ f o d. Returns frozenset."""
    b = C.dst[f]
    seen = set([f]); frontier = [f]
    while frontier:
        h = frontier.pop()
        a = C.src[h]
        for d in Dcomposable_into(C, D, a):
            hd = C.compose(h, d)
            if hd not in seen:
                seen.add(hd); frontier.append(hd)
    return frozenset(seen)

def orbits_into(C, D, b):
    seen = set(); orbs = []
    for f in arrows_into(C, b):
        if f in seen: continue
        o = orbit_of(C, D, f); orbs.append(o); seen |= o
    return orbs

def is_generator(C, D, c, orbit):
    """c generates orbit  <=>  d -> c o d  (d in D, d: src(c)->* wait codomain=src c)
    is a bijection D_into(src c) -> orbit."""
    a = C.src[c]
    Ds = Dcomposable_into(C, D, a)
    imgs = [C.compose(c, d) for d in Ds]
    if set(imgs) != set(orbit): return False
    if len(set(imgs)) != len(Ds): return False   # free (injective)
    return True

def generators_of(C, D, orbit):
    return [c for c in orbit if is_generator(C, D, c, orbit)]

def is_free_orbit(C, D, orbit):
    return len(generators_of(C, D, orbit)) > 0

def L_holds(C, D):
    for b in C.objs:
        for o in orbits_into(C, D, b):
            if not is_free_orbit(C, D, o):
                return False
    return True

def all_transversals(C, D):
    """All choices of one generator per orbit (over all targets), with the unit
    orbit forced to id. Yields dict orbit(frozenset)->generator and the T-set."""
    orbit_list = []
    for b in C.objs:
        for o in orbits_into(C, D, b):
            orbit_list.append(o)
    choice_sets = []
    forced = {}
    free_orbits = []
    for o in orbit_list:
        gens = generators_of(C, D, o)
        # force the unit orbit (the one containing some id) to the identity
        idb = None
        for m in o:
            if m in C.ident.values() and C.src[m]==C.dst[m]:
                idb = m
        if idb is not None and idb in gens:
            forced[o] = idb
        else:
            free_orbits.append(o); choice_sets.append(gens)
    for combo in itertools.product(*choice_sets):
        T = dict(forced)
        for o, c in zip(free_orbits, combo):
            T[o] = c
        yield T

def orbit_lookup(C, D, f):
    """Return the orbit (frozenset) containing f."""
    return orbit_of(C, D, f)

def defect(C, D, T):
    """For composable generators c2,c1 in T: c2 o c1 = floor . omega.
    Returns dict (c2,c1)->omega (a D-arrow), and the floor map.
    omega lives in D (specifically D-arrows into the apex of orbit(c2 c1))."""
    gens = set(T.values())
    # map: orbit -> chosen generator
    chosen = {}
    for o, c in T.items():
        chosen[o] = c
    om = {}; flr = {}
    for c1 in gens:
        for c2 in gens:
            if C.dst[c1] != C.src[c2]: continue
            comp = C.compose(c2, c1)         # c2 o c1
            o = orbit_lookup(C, D, comp)
            c3 = chosen[o]                   # floor(c2 c1)
            # comp = c3 o omega, omega in D unique
            a = C.src[comp]
            found = None
            for d in Dcomposable_into(C, D, C.src[c3]):
                # need omega: a -> src(c3), c3 o omega = comp
                if C.src[d]==a and C.compose(c3, d)==comp:
                    found = d; break
            assert found is not None, f"no omega for {c2}o{c1}"
            om[(c2,c1)] = found; flr[(c2,c1)] = c3
    return om, flr

def closes(C, D, T):
    om, _ = defect(C, D, T)
    return all(C.src[d]==C.dst[d] and d in C.ident.values() for d in om.values())

def trivial_left_action(C, D, T):
    """Hypothesis (H-left): for every transversal generator c1:a->b and every
    psi in G_b=Aut_D(b), psi o c1 lies in orbit(c1) (i.e. psi o c1 = c1 o rho,
    rho in D). This is EXACTLY what makes orbit-composition (Sk_C) well-defined
    and the gauge action of omega a coboundary in an ABELIAN complex.
    Returns (holds, witnesses_of_failure)."""
    gens=list(T.values()); fails=[]
    for c1 in gens:
        b=C.dst[c1]
        Gb=[m for m in D if C.src[m]==b and C.dst[m]==b]  # vertex group at b
        orb=orbit_lookup(C,D,c1)
        for psi in Gb:
            pc=C.compose(psi,c1)        # psi o c1
            if pc not in orb:
                fails.append((psi,c1,pc))
    return (len(fails)==0, fails)

def abelian_vertex_groups(C, D):
    """Are all vertex groups G_a=Aut_D(a) abelian?"""
    for a in C.objs:
        G=[m for m in D if C.src[m]==a and C.dst[m]==a]
        for u in G:
            for v in G:
                if C.compose(u,v)!=C.compose(v,u): return False
    return True


# ===========================================================================
# (1)-(2) Survey rigid twist & 4-obj: transversals, defects, closure
# ===========================================================================

def survey(C, D):
    print("="*72); print("CATEGORY:", C.name, "   |D| =", len(D))
    print("  (L) holds:", L_holds(C, D))
    Ts = list(all_transversals(C, D))
    print(f"  #valid transversals: {len(Ts)}")
    any_close = False
    defect_summary = []
    for i,T in enumerate(Ts):
        om,_ = defect(C, D, T)
        nontriv = {k:v for k,v in om.items() if not (v in C.ident.values())}
        cl = (len(nontriv)==0)
        any_close = any_close or cl
        defect_summary.append((i, sorted((f"{k[0]}o{k[1]}",v) for k,v in nontriv.items())))
    print(f"  some transversal closes (G holds): {any_close}")
    print("  defect (nontrivial omega) per transversal:")
    for i,ds in defect_summary:
        print(f"    T{i}: {ds}")
    return Ts


# ===========================================================================
# (3) Abelian bar complex over F2 for the rigid twist; compute H^2, locate [omega]
# ===========================================================================

def f2_rank(rows):
    """rank over F2 of list of 0/1 tuples."""
    rows = [list(r) for r in rows]
    rank = 0; ncol = len(rows[0]) if rows else 0
    r = 0
    for col in range(ncol):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][col]==1: piv=i; break
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        for i in range(len(rows)):
            if i!=r and rows[i][col]==1:
                rows[i]=[(a^b) for a,b in zip(rows[i],rows[r])]
        r+=1; rank+=1
    return rank

def okey(orbit):
    """Canonical hashable key for an orbit (frozenset of arrows)."""
    return min(sorted(orbit, key=str))

def bar_complex_F2(C, D, Tref):
    """Build C^1 -d1-> C^2 -d2-> C^3 for the ORBIT category Sk_C with coefficient
    presheaf 𝒟(a)=vertex group G_a (assumed <= Z/2 here, F2 coords), in the clean
    abelian/trivial-left-action case.

    Cochains are indexed by ORBITS (arrows of Sk_C), NOT by a particular
    transversal's generators -- this is the whole point: Sk_C's morphisms are the
    free D-orbits.  A transversal is a *section* (choice of representative); the
    cochain coordinates are rep-independent.

    Differential (presheaf cohomology over F2; restriction maps phi vanish here):
       (d1 h)(o2,o1) = phi_{o1}(h(o2)) - h(o2*o1) + h(o1)
       (d2 w)(o3,o2,o1)= phi_{o1}(w(o3,o2)) - w(o3*o2,o1) + w(o3,o2*o1) - w(o2,o1)
    where o2*o1 := orbit(c2 o c1) for any reps (well-defined: trivial left action).
    """
    objs = C.objs
    def grp_dim(o_obj):
        E = [m for m in D if C.src[m]==o_obj and C.dst[m]==o_obj]
        return 0 if len(E)<=1 else 1   # 1 F2-coordinate if |G|=2

    # orbit bookkeeping: all orbits, their source object, a chosen rep from Tref
    all_orbs = {}            # okey -> orbit frozenset
    orb_src = {}             # okey -> source object (apex)
    orb_isunit = {}          # okey -> True if it is a unit orbit (contains an id)
    for b in objs:
        for o in orbits_into(C, D, b):
            k = okey(o); all_orbs[k]=o
            rep = Tref[o]
            orb_src[k] = C.src[rep]
            orb_isunit[k] = any(m in C.ident.values() and C.src[m]==C.dst[m] for m in o)

    def orb_of(f):  return okey(orbit_lookup(C,D,f))
    def star(o2k,o1k):
        """orbit product: orbit(rep(o2) o rep(o1))."""
        c1 = Tref[all_orbs[o1k]]; c2 = Tref[all_orbs[o2k]]
        return orb_of(C.compose(c2,c1))
    def composable(o2k,o1k):
        c1 = Tref[all_orbs[o1k]]; c2 = Tref[all_orbs[o2k]]
        return C.dst[c1]==C.src[c2]

    nd_orbs = [k for k in all_orbs if not orb_isunit[k] and grp_dim(orb_src[k])==1]
    # 2-cochains: composable orbit pairs (o2,o1), both nonunit, grp_dim(src o1)=1
    C2k=[]; C3k=[]
    nonunit = [k for k in all_orbs if not orb_isunit[k]]
    for o1 in nonunit:
        for o2 in nonunit:
            if composable(o2,o1) and grp_dim(orb_src[o1])==1:
                C2k.append((o2,o1))
    for o1 in nonunit:
        for o2 in nonunit:
            for o3 in nonunit:
                if composable(o2,o1) and composable(o3,o2) and grp_dim(orb_src[o1])==1:
                    C3k.append((o3,o2,o1))

    C1 = nd_orbs; C2 = C2k; C3 = C3k
    idx1 = {c:i for i,c in enumerate(C1)}
    idx2 = {p:i for i,p in enumerate(C2)}

    d1=[]
    for (o2,o1) in C2:
        row=[0]*len(C1)
        if o1 in idx1: row[idx1[o1]]^=1
        s=star(o2,o1)
        if s in idx1: row[idx1[s]]^=1
        # phi term vanishes (dst(o1) trivial group here)
        d1.append(row)
    d2=[]
    for (o3,o2,o1) in C3:
        row=[0]*len(C2)
        s32=star(o3,o2); s21=star(o2,o1)
        if (s32,o1) in idx2: row[idx2[(s32,o1)]]^=1
        if (o3,s21) in idx2: row[idx2[(o3,s21)]]^=1
        if (o2,o1) in idx2: row[idx2[(o2,o1)]]^=1
        d2.append(row)

    # Z^2 = ker d2 ; B^2 = im d1 ; H^2 = Z^2/B^2
    nC2 = len(C2)
    # ker d2 dimension = nC2 - rank(d2)
    rank_d2 = f2_rank(d2) if d2 else 0
    dim_Z2 = nC2 - rank_d2
    rank_d1 = f2_rank(d1) if d1 else 0
    dim_B2 = rank_d1
    dim_H2 = dim_Z2 - dim_B2

    return dict(C1=C1,C2=C2,C3=C3,d1=d1,d2=d2,
                dim_Z2=dim_Z2,dim_B2=dim_B2,dim_H2=dim_H2,
                idx2=idx2, all_orbs=all_orbs)


def omega_vector_F2(C, D, T, bc):
    """omega of transversal T as an F2 vector in C^2 = orbit-pair coordinates."""
    om,_ = defect(C,D,T)
    vec=[0]*len(bc["C2"])
    for (c2,c1),val in om.items():
        o2 = okey(orbit_lookup(C,D,c2)); o1 = okey(orbit_lookup(C,D,c1))
        if (o2,o1) in bc["idx2"]:
            v = 0 if val in C.ident.values() else 1   # id_a->0, g->1
            vec[bc["idx2"][(o2,o1)]] = v
    return vec

def in_span_F2(vec, basis_rows):
    """is vec in F2-span of basis_rows (the rows of d1 = B^2 generators)?"""
    test = basis_rows + [vec]
    return f2_rank(basis_rows)==f2_rank(test) if basis_rows else (sum(vec)==0)


# ===========================================================================
# (4) 2-cocycle identity test (general, valued in D, non-abelian-safe)
# ===========================================================================

def test_cocycle_identity(C, D, T):
    """Check the derived identity on every composable transversal TRIPLE:
       omega(c3, floor(c2 c1)) . omega(c2,c1)  ==  omega(floor(c3 c2), c1) . (c1-action on omega(c3,c2))
    where (c1-action) is: precomposition realizing left-action triviality, i.e. we
    test the *associativity-derived* equality of D-parts. We test it as an EQUALITY
    of the two factorizations of c3 c2 c1 directly (model-independent)."""
    gens = list(T.values())
    om, flr = defect(C, D, T)
    ok = True; tested = 0
    for c1 in gens:
        for c2 in gens:
            for c3 in gens:
                if C.dst[c1]!=C.src[c2] or C.dst[c2]!=C.src[c3]: continue
                if any(c in C.ident.values() for c in (c1,c2,c3)): continue
                tested += 1
                # both bracketings of c3 c2 c1 factor as floor(c3 c2 c1) . (D-part)
                full = C.compose(c3, C.compose(c2,c1))
                # already guaranteed associative in C; the D-parts from the two
                # nested factorizations must agree -> that's the cocycle identity.
                # left:  c3 . (c2 c1) = c3 . (floor(c2c1) . om(c2,c1))
                #       = (floor(c3,floor(c2c1)) . om(c3,floor c2c1)) . om(c2,c1)
                f21 = flr[(c2,c1)]
                left_floor = flr[(c3, f21)]
                # right: (c3 c2) c1 = (floor(c3c2) . om(c3,c2)) . c1
                f32 = flr[(c3,c2)]
                right_floor = flr[(f32, c1)]
                if left_floor != right_floor:
                    ok = False
    return ok, tested


# ===========================================================================
# main
# ===========================================================================
if __name__ == "__main__":
    RT, Drt = rigid_twist()
    Ts_rt = survey(RT, Drt)

    print("\n" + "#"*72)
    print("# RIGID TWIST: explicit F2 bar complex, H^2, and [omega]")
    print("#"*72)
    Tref = Ts_rt[0]
    bc = bar_complex_F2(RT, Drt, Tref)
    print("  C^1 (nondeg gens, src-group Z/2):", bc["C1"])
    print("  C^2 (composable pairs):", bc["C2"])
    print("  C^3 (composable triples):", bc["C3"])
    print("  dim Z^2 =", bc["dim_Z2"], " dim B^2 =", bc["dim_B2"], " dim H^2 =", bc["dim_H2"])
    print("  |H^2| =", 2**bc["dim_H2"])
    # check d2.d1 = 0
    import numpy as np
    if bc["d1"] and bc["d2"]:
        D1=np.array(bc["d1"])%2; D2=np.array(bc["d2"])%2
        prod=(D2.dot(D1))%2
        print("  d2 . d1 == 0 :", not prod.any())
    # locate omega classes for ALL transversals
    print("  [omega] in B^2 (=> closes) per transversal:")
    for i,T in enumerate(Ts_rt):
        vec = omega_vector_F2(RT, Drt, T, bc)
        inB = in_span_F2(vec, bc["d1"])
        print(f"    T{i}: omega-vector={vec}  in B^2? {inB}  (closes={closes(RT,Drt,T)})")

    print("\n" + "#"*72)
    print("# PAIRWISE 4-OBJECT")
    print("#"*72)
    P4, Dp4 = pairwise_4obj()
    Ts_p4 = survey(P4, Dp4)

    print("\n  PAIRWISE: H^2 location per transversal (orbit-indexed):")
    bcp = bar_complex_F2(P4, Dp4, Ts_p4[0])
    print("   dim Z^2 =",bcp["dim_Z2"]," dim B^2 =",bcp["dim_B2"]," dim H^2 =",bcp["dim_H2"])
    for i,T in enumerate(Ts_p4):
        vec=omega_vector_F2(P4,Dp4,T,bcp); inB=in_span_F2(vec,bcp["d1"])
        print(f"    T{i}: omega={vec} in B^2? {inB} closes={closes(P4,Dp4,T)}")

    print("\n" + "#"*72)
    print("# TRIPLE CHAIN (non-vacuous cocycle identity + d2.d1=0 test)")
    print("#"*72)
    TC, Dtc = triple_chain_twist()
    Ts_tc = survey(TC, Dtc)
    for i,T in enumerate(Ts_tc):
        ok,n = test_cocycle_identity(TC, Dtc, T)
        print(f"    T{i}: floor-cocycle identity holds on {n} triples: {ok}")
    bctc = bar_complex_F2(TC, Dtc, Ts_tc[0])
    print("  C^1:",len(bctc["C1"]),"C^2:",len(bctc["C2"]),"C^3:",len(bctc["C3"]))
    print("  dim Z^2 =",bctc["dim_Z2"]," dim B^2 =",bctc["dim_B2"]," dim H^2 =",bctc["dim_H2"])
    if bctc["d1"] and bctc["d2"]:
        D1=np.array(bctc["d1"])%2; D2=np.array(bctc["d2"])%2
        print("  d2 . d1 == 0 :", not ((D2.dot(D1))%2).any(), " (C^3 nonempty:",len(bctc["C3"])>0,")")
    print("  [omega] location per transversal (expect closing T -> in B^2):")
    for i,T in enumerate(Ts_tc):
        vec=omega_vector_F2(TC,Dtc,T,bctc); inB=in_span_F2(vec,bctc["d1"])
        print(f"    T{i}: omega={vec} in B^2? {inB} closes={closes(TC,Dtc,T)}")

    # FULL additive Z/2 cocycle identity on triple chain (phi=0 here):
    print("  FULL additive 2-cocycle identity  w(o3,o2*o1)+w(o2,o1)=w(o3*o2,o1):")
    for i,T in enumerate(Ts_tc):
        om,flr=defect(TC,Dtc,T); gens=list(T.values()); ok=True; cnt=0
        def val(c2,c1):
            v=om.get((c2,c1)); return 0 if (v is None or v in TC.ident.values()) else 1
        for c1 in gens:
         for c2 in gens:
          for c3 in gens:
            if TC.dst[c1]!=TC.src[c2] or TC.dst[c2]!=TC.src[c3]: continue
            if any(c in TC.ident.values() for c in (c1,c2,c3)): continue
            cnt+=1
            f21=flr[(c2,c1)]; f32=flr[(c3,c2)]
            lhs=(val(c3,f21)+val(c2,c1))%2
            rhs=(val(f32,c1))%2   # phi(w(c3,c2))=0 (trivial left action, Z/2)
            if lhs!=rhs: ok=False
        print(f"    T{i}: identity holds on {cnt} triples: {ok}")
