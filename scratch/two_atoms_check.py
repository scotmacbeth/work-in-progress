"""
two_atoms_check.py
==================
Test the "two-atoms / Zappa-Szép decomposition" conjecture for small categories
(equivalently, directed containers).

CONJECTURE
----------
Every small category C is a Zappa-Szép product of
  (P) its skeleton / reachability poset (objects + chosen transversal arrows, no
      nontrivial loops), and
  (M) the endomorphism monoids End(a) = Hom(a,a) at each object (the "loops"),
with composition as the mutual two-sided action.

Concrete unique-factorization (UF) claim, SOURCE version:
  every f: a->b factors uniquely as f = s' . e  with e in End(a) and s' a
  "skeleton" (transversal) morphism a->b.
TARGET version (dual):
  every f: a->b factors uniquely as f = e' . s  with e' in End(b), s transversal.

We test BOTH the "does a transversal exist making this work" question and the
"is the factorization unique" question, and characterize failures.

A small category is encoded explicitly:
  obj            : list of objects
  hom[(a,b)]     : list of morphism-ids (arbitrary hashable tokens), the arrows a->b
  comp[(g,f)]    : g . f   (apply f then g; f: a->b, g: b->c gives g.f : a->c)
  ident[a]       : identity morphism at a
Each morphism id is globally unique; src/dst recovered from a registry.
"""

from itertools import product as iproduct


class Cat:
    def __init__(self, name, objs, arrows, src, dst, comp, ident):
        self.name = name
        self.objs = list(objs)
        self.arrows = list(arrows)
        self.src = dict(src)      # arrow -> object
        self.dst = dict(dst)      # arrow -> object
        self.comp = dict(comp)    # (g,f) -> gf  (f then g), only where composable
        self.ident = dict(ident)  # object -> identity arrow
        self.check_axioms()

    def hom(self, a, b):
        return [m for m in self.arrows if self.src[m] == a and self.dst[m] == b]

    def end(self, a):
        return self.hom(a, a)

    def compose(self, g, f):
        # g after f
        assert self.dst[f] == self.src[g], f"not composable: {f}:{self.src[f]}->{self.dst[f]}, {g}:{self.src[g]}->{self.dst[g]}"
        return self.comp[(g, f)]

    def check_axioms(self):
        # identities
        for a in self.objs:
            assert a in self.ident, f"no identity at {a}"
            i = self.ident[a]
            assert self.src[i] == a and self.dst[i] == a
        # closure + unit + assoc
        for f in self.arrows:
            a, b = self.src[f], self.dst[f]
            assert self.compose(self.ident[b], f) == f, f"left unit fails on {f}"
            assert self.compose(f, self.ident[a]) == f, f"right unit fails on {f}"
        for f in self.arrows:
            for g in self.arrows:
                if self.dst[f] != self.src[g]:
                    continue
                gf = self.compose(g, f)
                assert self.src[gf] == self.src[f] and self.dst[gf] == self.dst[g]
                for h in self.arrows:
                    if self.dst[g] != self.src[h]:
                        continue
                    # h(gf) == (hg)f
                    lhs = self.compose(h, gf)
                    rhs = self.compose(self.compose(h, g), f)
                    assert lhs == rhs, f"assoc fails: {h},{g},{f}"


# ----------------------------------------------------------------------------
# The core test: Zappa-Szép unique factorization w.r.t. a chosen transversal.
# ----------------------------------------------------------------------------

def test_UF_source(C, transversal):
    """
    SOURCE version. transversal[(a,b)] = a chosen set of 'skeleton' arrows a->b.
    Test: the map  End(a) x T(a,b) -> Hom(a,b),  (e, s') -> s' . e   is a bijection.
    (right action of End(a) on the transversal-generated arrows)
    Returns (ok_exist, ok_unique, details).
    """
    ok = True
    details = []
    for a in C.objs:
        for b in C.objs:
            H = set(C.hom(a, b))
            T = transversal.get((a, b), [])
            E = C.end(a)
            produced = {}
            collision = False
            for s in T:
                for e in E:
                    f = C.compose(s, e)   # s' . e
                    if f in produced:
                        collision = True
                    produced[f] = (s, e)
            covered = set(produced.keys())
            exists = covered == H
            unique = (len(produced) == len(T) * len(E)) and not collision
            # unique means |T|*|E| distinct outputs hitting exactly H
            if not (exists and unique and len(T) * len(E) == len(H)):
                ok = False
            details.append((a, b, len(H), len(T), len(E), exists, unique,
                            len(T) * len(E) == len(H)))
    return ok, details


def find_transversal_source(C):
    """
    Try to find a transversal making SOURCE-UF hold.
    Necessary condition object-wise: for each (a,b), Hom(a,b) must split into
    free right-End(a)-orbits, i.e. End(a) acts freely on Hom(a,b) and the number
    of orbits is |Hom(a,b)| / |End(a)|. Pick one rep per orbit.
    Returns transversal dict or None if no transversal can work.
    """
    transversal = {}
    for a in C.objs:
        E = C.end(a)
        for b in C.objs:
            H = C.hom(a, b)
            if not H:
                transversal[(a, b)] = []
                continue
            # right action: f * e = f . e  (e in End(a), f: a->b)
            # orbits under this action
            seen = set()
            reps = []
            free = True
            for f in H:
                if f in seen:
                    continue
                orbit = set()
                for e in E:
                    orbit.add(C.compose(f, e))
                if len(orbit) != len(E):
                    free = False   # action not free on this orbit
                reps.append(f)
                seen |= orbit
            if not free or len(seen) != len(H):
                return None  # cannot partition into free orbits
            transversal[(a, b)] = reps
    return transversal


def is_skeleton_poset(C, transversal):
    """
    Does the transversal form a *poset skeleton*: composition of transversal
    arrows is again (uniquely) a transversal arrow, transversals contain identities,
    and at most one transversal arrow between any pair (antisymmetry-ish)?
    i.e. is the transversal a subcategory that is a poset (thin)?
    """
    Tset = set()
    for (a, b), ts in transversal.items():
        for t in ts:
            Tset.add(t)
    # identities transversal?
    for a in C.objs:
        if C.ident[a] not in Tset:
            return False, "identity not transversal"
    # thin: at most one transversal arrow per (a,b)
    for (a, b), ts in transversal.items():
        if len(ts) > 1:
            return False, f"thick: {len(ts)} transversal arrows {a}->{b}"
    # closed under composition
    for s in Tset:
        for t in Tset:
            if C.dst[t] != C.src[s]:
                continue
            if C.compose(s, t) not in Tset:
                return False, "transversal not closed under composition"
    return True, "transversal is a thin subcategory (poset skeleton)"


def run(C, verbose=True):
    if verbose:
        print("=" * 70)
        print(f"CATEGORY: {C.name}")
        print(f"  objects: {C.objs}")
        for a in C.objs:
            for b in C.objs:
                h = C.hom(a, b)
                if h:
                    print(f"  Hom({a},{b}) = {h}   |End| at {a} = {len(C.end(a))}")
    tv = find_transversal_source(C)
    if tv is None:
        if verbose:
            print("  >> NO transversal exists: End(a) does not act freely with")
            print("     full coverage on some Hom(a,b). UF (source) FAILS.")
        return {"name": C.name, "uf_source": False, "transversal": None,
                "skeleton_poset": None, "reason": "no free transversal"}
    ok, details = test_UF_source(C, tv)
    skp, skreason = is_skeleton_poset(C, tv)
    if verbose:
        print(f"  transversal found: "
              + ", ".join(f"T({a},{b})={ts}" for (a, b), ts in tv.items() if ts))
        print(f"  >> SOURCE-UF (f = s'.e, e in End(src)) : {'PASS' if ok else 'FAIL'}")
        print(f"  >> transversal is a poset skeleton?     : {skp}  ({skreason})")
    return {"name": C.name, "uf_source": ok, "transversal": tv,
            "skeleton_poset": skp, "reason": skreason}


# ----------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------

def monoid_cat(name, elems, mul, unit):
    """One-object category from a monoid (elems, mul, unit)."""
    obj = "*"
    arrows = list(elems)
    src = {m: obj for m in arrows}
    dst = {m: obj for m in arrows}
    comp = {}
    for g in arrows:
        for f in arrows:
            comp[(g, f)] = mul(g, f)   # g.f  (we treat mul(g,f)=g*f as g after f)
    ident = {obj: unit}
    return Cat(name, [obj], arrows, src, dst, comp, ident)


def Zn(n):
    elems = list(range(n))
    return monoid_cat(f"Z/{n} (one-object)", elems, lambda a, b: (a + b) % n, 0)


def idempotent2():
    # {1, e}, e*e=e  -> the 2-element monoid with absorbing-ish idempotent
    # mul: 1 is unit, e*e=e
    def mul(a, b):
        if a == "1": return b
        if b == "1": return a
        return "e"
    return monoid_cat("M2 idempotent {1,e:e^2=e}", ["1", "e"], mul, "1")


def two_object_general(name, La, Lb, sset, left_action, right_action):
    """
    Build the 2-object category on objects a,b.
      La = (elemsA, mulA, unitA)   loops at a
      Lb = (elemsB, mulB, unitB)   loops at b
      sset = list of arrow tokens a->b   (Hom(a,b)); Hom(b,a) empty
      left_action(l_b, s) = l_b . s   in Hom(a,b)   (l_b in Lb)
      right_action(s, l_a) = s . l_a  in Hom(a,b)   (l_a in La)
    Composition built from monoid muls + actions; must satisfy assoc &
    action-compatibility for Cat() to accept it.
    """
    (eA, mA, uA) = La
    (eB, mB, uB) = Lb
    # tag arrows uniquely
    Aend = [("a", x) for x in eA]
    Bend = [("b", y) for y in eB]
    AB = [("s", t) for t in sset]
    arrows = Aend + Bend + AB
    src = {}
    dst = {}
    for x in eA:
        src[("a", x)] = "a"; dst[("a", x)] = "a"
    for y in eB:
        src[("b", y)] = "b"; dst[("b", y)] = "b"
    for t in sset:
        src[("s", t)] = "a"; dst[("s", t)] = "b"
    comp = {}
    # End(a) o End(a)
    for x in eA:
        for x2 in eA:
            comp[(("a", x), ("a", x2))] = ("a", mA(x, x2))
    # End(b) o End(b)
    for y in eB:
        for y2 in eB:
            comp[(("b", y), ("b", y2))] = ("b", mB(y, y2))
    # (a->b) o End(a):  s . l_a  = right_action
    for t in sset:
        for x in eA:
            comp[(("s", t), ("a", x))] = ("s", right_action(t, x))
    # End(b) o (a->b): l_b . s = left_action
    for y in eB:
        for t in sset:
            comp[(("b", y), ("s", t))] = ("s", left_action(y, t))
    ident = {"a": ("a", uA), "b": ("b", uB)}
    return Cat(name, ["a", "b"], arrows, src, dst, comp, ident)


# ----------------------------------------------------------------------------
# Specific small categories
# ----------------------------------------------------------------------------

def walking_arrow():
    # objects a,b; one arrow a->b; trivial loops
    return two_object_general(
        "Walking arrow (a->b, trivial loops)",
        (["*"], lambda x, y: "*", "*"),
        (["*"], lambda x, y: "*", "*"),
        ["s"],
        left_action=lambda lb, s: s,
        right_action=lambda s, la: s,
    )


def two_obj_loops(La_name, La, Lb_name, Lb, sset, la_act=None, lb_act=None):
    """Convenience with default trivial actions (s fixed by all loops)."""
    if la_act is None:
        la_act = lambda s, la: s
    if lb_act is None:
        lb_act = lambda lb, s: s
    return two_object_general(
        f"2-obj: La={La_name}, Lb={Lb_name}, |Hom(a,b)|={len(sset)}",
        La, Lb, sset, lb_act, la_act)


TRIV = (["*"], lambda x, y: "*", "*")
def Z2mon():
    return ([0, 1], lambda a, b: (a + b) % 2, 0)
def Z3mon():
    return ([0, 1, 2], lambda a, b: (a + b) % 3, 0)
def IDEM():
    def mul(a, b):
        if a == "1": return b
        if b == "1": return a
        return "e"
    return (["1", "e"], mul, "1")


def chain(n):
    """Linear poset 0<1<...<n-1: a thin category, one arrow i->j for i<=j."""
    objs = list(range(n))
    arrows = []
    src = {}; dst = {}; ident = {}
    for i in range(n):
        for j in range(i, n):
            t = (i, j)
            arrows.append(t); src[t] = i; dst[t] = j
        ident[i] = (i, i)
    comp = {}
    for (i, j) in arrows:
        for (k, l) in arrows:
            if dst[(k, l)] == src[(i, j)]:  # (i,j) after (k,l): k<=l=i? need l==i
                pass
    # composition: (j,k) after (i,j) = (i,k)
    for g in arrows:
        for f in arrows:
            if dst[f] == src[g]:
                comp[(g, f)] = (src[f], dst[g])
    return Cat(f"Chain 0<..<{n-1}", objs, arrows, src, dst, comp, ident)


def comm_square():
    """Commutative square 00->01->11, 00->10->11, with composite 00->11."""
    objs = ["00", "01", "10", "11"]
    # thin poset (product of two 2-chains)
    le = {("00","00"),("01","01"),("10","10"),("11","11"),
          ("00","01"),("00","10"),("00","11"),("01","11"),("10","11")}
    arrows = list(le)
    src = {p: p[0] for p in arrows}
    dst = {p: p[1] for p in arrows}
    ident = {o: (o, o) for o in objs}
    comp = {}
    for g in arrows:
        for f in arrows:
            if dst[f] == src[g]:
                comp[(g, f)] = (src[f], dst[g])
    return Cat("Commutative square", objs, arrows, src, dst, comp, ident)


def chain_with_loop_at_end(loopname, loop):
    """0 -> 1, with a loop monoid `loop` at object 1 (target). Loops at 0 trivial.
       Arrow s:0->1. Right action trivial; left action = loop acts by mult on Hom(0,1)
       but Hom(0,1) is a torsor copy of the loop monoid? We set Hom(0,1) = loop elems,
       l_b . s_x = (l_b * x). This makes Hom(0,1) a free left Lb-set of rank 1."""
    (eB, mB, uB) = loop
    sset = list(eB)  # one arrow per loop element: a free Lb-torsor
    return two_object_general(
        f"0->1 with loop {loopname} at TARGET (free Lb-set Hom)",
        TRIV, loop, sset,
        left_action=lambda lb, s: mB(lb, s),   # lb . s_x = s_{lb*x}
        right_action=lambda s, la: s,
    )


def chain_with_loop_at_src(loopname, loop):
    """0 -> 1, loop monoid at object 0 (source). Hom(0,1) a free RIGHT La-set."""
    (eA, mA, uA) = loop
    sset = list(eA)
    return two_object_general(
        f"0->1 with loop {loopname} at SOURCE (free La-set Hom)",
        loop, TRIV, sset,
        left_action=lambda lb, s: s,
        right_action=lambda s, la: mA(s, la),  # s_x . la = s_{x*la}
    )


def collapsing_loop_at_src(loopname, loop):
    """0->1, loop at source, but Hom(0,1) has a SINGLE arrow that all source-loops
       fix (action collapses). e.g. Z/2 at 0 but s.g = s. Tests non-free action."""
    return two_object_general(
        f"0->1 with loop {loopname} at SOURCE, COLLAPSED (|Hom(a,b)|=1)",
        loop, TRIV, ["s"],
        left_action=lambda lb, s: s,
        right_action=lambda s, la: s,   # all source loops fix s -> not free
    )


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def build_all():
    cats = []
    # --- DECISIVE 2-OBJECT CASE: vary loop monoids, trivial action first ---
    print("### PART 1: decisive 2-object case (objects a,b; one skeleton s:a->b)")
    print("### Loop monoids at a and b varied; s fixed by loops (trivial action).\n")
    combos = [
        ("triv", TRIV, "triv", TRIV),
        ("Z/2", Z2mon(), "triv", TRIV),
        ("triv", TRIV, "Z/2", Z2mon()),
        ("Z/2", Z2mon(), "Z/2", Z2mon()),
        ("Z/3", Z3mon(), "triv", TRIV),
        ("idem", IDEM(), "triv", TRIV),
        ("triv", TRIV, "idem", IDEM()),
        ("idem", IDEM(), "idem", IDEM()),
    ]
    for (na, La, nb, Lb) in combos:
        cats.append(("P1", two_obj_loops(na, La, nb, Lb, ["s"])))

    # --- PART 1b: Hom(a,b) as a free torsor of a source/target loop ---
    print()
    for (n, m) in [("Z/2", Z2mon()), ("Z/3", Z3mon()), ("idem", IDEM())]:
        cats.append(("P1b", chain_with_loop_at_src(n, m)))
        cats.append(("P1b", chain_with_loop_at_end(n, m)))
    # collapsing (non-free) source action -- should expose failure of SOURCE-UF
    for (n, m) in [("Z/2", Z2mon()), ("Z/3", Z3mon()), ("idem", IDEM())]:
        cats.append(("P1b", collapsing_loop_at_src(n, m)))

    # --- PART 2: broader sample ---
    cats.append(("P2", walking_arrow()))
    cats.append(("P2", chain(2)))
    cats.append(("P2", chain(3)))
    cats.append(("P2", chain(4)))
    cats.append(("P2", comm_square()))
    cats.append(("P2", Zn(2)))
    cats.append(("P2", Zn(3)))
    cats.append(("P2", Zn(4)))
    cats.append(("P2", monoid_cat("M2 idempotent {1,e}", *(lambda m=IDEM(): (m[0], m[1], m[2]))())))
    return cats


if __name__ == "__main__":
    cats = build_all()
    results = []
    part = None
    for (p, C) in cats:
        if p != part:
            part = p
            print("\n" + "#" * 70)
            print(f"# {part}")
            print("#" * 70)
        results.append(run(C))
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    npass = 0
    for r in results:
        verdict = "PASS" if r["uf_source"] else "FAIL"
        skp = r["skeleton_poset"]
        skstr = "skeleton=poset" if skp else ("skeleton=THICK/none" if skp is not None else "n/a")
        if r["uf_source"]:
            npass += 1
        print(f"  [{verdict}] {r['name']:<55} {skstr}")
    print(f"\n  {npass}/{len(results)} categories satisfy SOURCE unique factorization.")


# ----------------------------------------------------------------------------
# TARGET-version test and diagnosis (added after PART-1 verdict)
# ----------------------------------------------------------------------------

def find_transversal_target(C):
    """TARGET version: f = e'.s, e' in End(b)=End(dst). Need End(b) to act FREELY
    on the LEFT of Hom(a,b) with full coverage."""
    transversal = {}
    for b in C.objs:
        E = C.end(b)
        for a in C.objs:
            H = C.hom(a, b)
            if not H:
                transversal[(a, b)] = []
                continue
            seen = set(); reps = []; free = True
            for f in H:
                if f in seen:
                    continue
                orbit = set()
                for e in E:
                    orbit.add(C.compose(e, f))   # e'.f  left action
                if len(orbit) != len(E):
                    free = False
                reps.append(f); seen |= orbit
            if not free or len(seen) != len(H):
                return None
            transversal[(a, b)] = reps
    return transversal


def diagnose(C):
    src_tv = find_transversal_source(C)
    tgt_tv = find_transversal_target(C)
    return (src_tv is not None, tgt_tv is not None)
