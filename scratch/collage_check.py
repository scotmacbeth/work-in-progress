"""
Sanity check for the collage reconstruction theorem
(2026-06-10-collage-reconstruction.tex).

We take a small category C given by an explicit composition table, build:
  - the hom-sets Hom(a,b)
  - the endomorphism monoids End(x) = Hom(x,x)
  - the (End(b),End(a))-biset structure (pre/post composition)
  - the tensor product Hom(b,c) (x)_{End(b)} Hom(a,b) as the COEQUALIZER
    of the two action maps (= quotient by the generated equivalence relation)
  - the balanced map mu : tensor -> Hom(a,c), mu(g (x) f) = g . f
and verify:
  (i)   balance: (g.e).f == g.(e.f)
  (ii)  mu is well defined on the tensor (constant on each equivalence class)
  (iii) the reconstructed composition g o^flat f := mu([g (x) f]) equals the
        original composition table (isomorphism = identity on objects/morphisms).

A "small category" here is a dict-based presentation.
"""

from itertools import product


class Category:
    def __init__(self, objects, morphisms, dom, cod, ident, comp):
        # morphisms: set of morphism labels
        # dom,cod: dict morphism -> object
        # ident: dict object -> identity morphism
        # comp: dict (g,f) -> g o f   (defined when dom(g)==cod(f))
        self.objects = list(objects)
        self.morphisms = set(morphisms)
        self.dom = dom
        self.cod = cod
        self.ident = ident
        self.comp = comp

    def hom(self, a, b):
        return [m for m in self.morphisms if self.dom[m] == a and self.cod[m] == b]

    def end(self, x):
        return self.hom(x, x)

    def o(self, g, f):
        assert self.dom[g] == self.cod[f], f"not composable: {g} o {f}"
        return self.comp[(g, f)]


# ---------- the tensor as a coequalizer (quotient by generated relation) ----------

def tensor_classes(C, a, b, c):
    """
    Hom(b,c) (x)_{End(b)} Hom(a,b).
    Coequalizer of lambda,rho : Hom(b,c) x End(b) x Hom(a,b) => Hom(b,c) x Hom(a,b)
      lambda(g,e,f) = (g.e, f) = (g o e, f)      [right End(b)-action on Hom(b,c)]
      rho(g,e,f)    = (g, e.f) = (g, e o f)       [left End(b)-action on Hom(a,b)]
    Return: dict pair -> class-representative (union-find), and list of classes.
    """
    Hbc = C.hom(b, c)
    Hab = C.hom(a, b)
    Eb = C.end(b)
    pairs = list(product(Hbc, Hab))

    parent = {p: p for p in pairs}

    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(p, q):
        rp, rq = find(p), find(q)
        if rp != rq:
            parent[rp] = rq

    # generators of ~ : (g o e, f) ~ (g, e o f)
    for g in Hbc:
        for e in Eb:
            for f in Hab:
                left = (C.o(g, e), f)
                right = (g, C.o(e, f))
                union(left, right)

    classes = {}
    for p in pairs:
        classes.setdefault(find(p), []).append(p)
    return find, list(classes.values()), pairs


def check_category(C, name):
    print(f"=== {name} ===")
    ok = True

    # (i) balance + (ii) mu well defined, for every composable triple of objects
    for a, b, c in product(C.objects, repeat=3):
        # balance check elementwise
        for g in C.hom(b, c):
            for e in C.end(b):
                for f in C.hom(a, b):
                    lhs = C.o(C.o(g, e), f)   # (g.e).f
                    rhs = C.o(g, C.o(e, f))   # g.(e.f)
                    if lhs != rhs:
                        print(f"  BALANCE FAIL ({a},{b},{c}): {lhs} != {rhs}")
                        ok = False

        find, classes, pairs = tensor_classes(C, a, b, c)

        # mu must be constant on each equivalence class
        for cls in classes:
            vals = {C.o(g, f) for (g, f) in cls}
            if len(vals) != 1:
                print(f"  MU ILL-DEFINED ({a},{b},{c}): class {cls} -> {vals}")
                ok = False

        # (iii) reconstructed composition equals original
        for (g, f) in pairs:
            rep_class = [cls for cls in classes if (g, f) in cls][0]
            mu_val = C.o(rep_class[0][0], rep_class[0][1])  # mu([g (x) f])
            if mu_val != C.o(g, f):
                print(f"  RECON FAIL: mu([{g}(x){f}]) = {mu_val} != {C.o(g,f)}")
                ok = False

    # unit laws (identities are the monoid units 1_x)
    for f in C.morphisms:
        a, b = C.dom[f], C.cod[f]
        if C.o(C.ident[b], f) != f or C.o(f, C.ident[a]) != f:
            print(f"  UNIT FAIL on {f}")
            ok = False

    print("  RESULT:", "C^flat reconstructs C exactly (isomorphic)" if ok else "MISMATCH")
    print()
    return ok


# ---------- Example 1: walking arrow with Z/2 endomorphism monoids ----------
# Objects: 0,1.  At each object a Z/2 monoid {id, s} with s o s = id.
# One "transversal" arrow t: 0->1.  Hom(0,1) = { t, t o s0 = s1 o t , ... }.
# To keep it a genuine category we build it as a quotient/product structure:
# morphisms 0->1 are pairs (Z/2 at 1) x t x (Z/2 at 0) but with the middle
# collapsing; simplest concrete model: the category with End(0)=End(1)=Z/2 and
# Hom(0,1) a free (Z/2,Z/2)-biset of rank 1, i.e. {t, s1.t}={t, t.s0} (size 2,
# with s1.t = t.s0). This is the category B(Z/2) "doubled" along an iso-like arrow.
#
# Concretely: take the GROUP Z/2 x {0,1} as objects? Simpler: the contractible
# groupoid on 2 objects times nothing... Let's just use the one-object cases
# below for rigor and use a clean 2-object example: the category from a group
# action. We use: two objects, End = Z/2, and t,t' : 0->1 with t' = s1 o t,
# composition forced by group laws (it is the "translation groupoid" of Z/2).

def connected_groupoid_Z2():
    """
    Two objects 0,1; the connected groupoid with vertex group Z/2.
    Every hom-set Hom(a,b) has size 2 and is a free (Z/2,Z/2)-biset of rank 1.
    A morphism a->b is labelled  "g:a->b" with g in Z/2 = {e,x}, representing
    g composed with the canonical iso a->b.  Composition multiplies group elts:
        (g:b->c) o (h:a->b) = (g*h : a->c).
    This is the cleanest 2-object example with NON-trivial endomorphism monoids,
    so the tensor over End(b)=Z/2 genuinely collapses |Hom(b,c)|*|Hom(a,b)|=4
    pairs down to 2 classes.
    """
    objs = [0, 1]
    grp = ['e', 'x']
    mul = {('e', 'e'): 'e', ('e', 'x'): 'x', ('x', 'e'): 'x', ('x', 'x'): 'e'}

    mor, dom, cod = [], {}, {}
    for a in objs:
        for b in objs:
            for g in grp:
                m = f"{g}:{a}->{b}"
                mor.append(m); dom[m] = a; cod[m] = b

    def parse(m):
        g, rest = m.split(':')
        a, b = rest.split('->')
        return g, int(a), int(b)

    ident = {a: f"e:{a}->{a}" for a in objs}

    comp = {}
    for gm in mor:
        for fm in mor:
            gg, gb, gc = parse(gm)
            fg, fa, fb = parse(fm)
            if fb == gb:  # composable: cod(f)=dom(g)
                comp[(gm, fm)] = f"{mul[(gg, fg)]}:{fa}->{gc}"
    return Category(objs, mor, dom, cod, ident, comp)


def Zn_one_object(n):
    """ Z/n as a one-object category (a monoid). Objects: ['*']. """
    objs = ['*']
    mor = [f"{k}" for k in range(n)]
    dom = {m: '*' for m in mor}
    cod = {m: '*' for m in mor}
    ident = {'*': '0'}
    comp = {}
    for g in range(n):
        for f in range(n):
            comp[(str(g), str(f))] = str((g + f) % n)
    return Category(objs, mor, dom, cod, ident, comp)


if __name__ == "__main__":
    ok1 = check_category(connected_groupoid_Z2(),
                         "Connected groupoid on 2 objects, vertex group Z/2")
    ok2 = check_category(Zn_one_object(3), "Z/3 as a one-object category")
    print("ALL CHECKS PASSED" if (ok1 and ok2) else "SOME CHECK FAILED")
