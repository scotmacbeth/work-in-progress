"""
Pairwise Zappa-Szep checks.

Goal: support the pairwise (L wedge G) criterion. Two new facts to confirm on
GENUINE two-category examples (D is a wide subcategory with cross-object arrows,
NOT just the endomorphisms):

  (A) Distributive law lambda: D.C => C.D given by rewriting d o c = (^d c) o (d^c)
      satisfies the matched-pair axioms ZS1-ZS4 + units  IFF  the product C |><| D
      is a category (associative + unital).

  (B) Free right D-module Hom_K(-,b)  IFF  unique factorization f = c o d exists
      with c in a chosen basis (per target b).

Representation of a finite category:
  objects: list of hashable labels
  arrows : dict  name -> (dom, cod)
  comp   : dict  (g, f) -> gf   defined when cod(f)==dom(g)   [g o f]
  ident  : dict  obj -> name of identity arrow
"""

from itertools import product


class FinCat:
    def __init__(self, objects, arrows, comp, ident):
        self.objects = list(objects)
        self.arrows = dict(arrows)        # name -> (dom,cod)
        self.comp = dict(comp)            # (g,f) -> gf  (g after f)
        self.ident = dict(ident)          # obj -> id name

    def dom(self, f): return self.arrows[f][0]
    def cod(self, f): return self.arrows[f][1]

    def compose(self, g, f):
        assert self.cod(f) == self.dom(g), f"not composable {g} o {f}"
        return self.comp[(g, f)]

    def hom(self, a, b):
        return [f for f, (d, c) in self.arrows.items() if d == a and c == b]

    def check_category(self, verbose=False):
        # identities
        for o in self.objects:
            i = self.ident[o]
            assert self.dom(i) == o and self.cod(i) == o
            for f in self.arrows:
                if self.cod(f) == o:
                    if self.compose(i, f) != f:
                        if verbose: print("left id fail", i, f);
                        return False
                if self.dom(f) == o:
                    if self.compose(f, i) != f:
                        if verbose: print("right id fail", f, i)
                        return False
        # associativity
        for h in self.arrows:
            for g in self.arrows:
                if self.cod(g) != self.dom(h): continue
                for f in self.arrows:
                    if self.cod(f) != self.dom(g): continue
                    if self.compose(self.compose(h, g), f) != \
                       self.compose(h, self.compose(g, f)):
                        if verbose: print("assoc fail", h, g, f)
                        return False
        return True


# ---------------------------------------------------------------------------
# Build the Zappa-Szep product C |><| D from a distributive law lambda.
#
# C, D are FinCat on the SAME object set O.  A morphism a->b of C|><|D is a pair
# (c, d) with d: a->m in D, c: m->b in C.   [ f = c o d, d first ]
# lambda is a dict: (d, c) -> (c2, d2)  for d in D, c in C with dom(d)==cod(c),
#   meaning  d o c = c2 o d2   with  c2 in C, d2 in D,  written ^d c = c2, d^c = d2.
# Composition:  (c2,d2) o (c1,d1) = ( c2 o ^{d2} c1 ,  (d2)^{c1} . d1 ).
# ---------------------------------------------------------------------------

def build_zs_product(C, D, lam):
    assert set(C.objects) == set(D.objects)
    O = list(C.objects)
    # morphisms = composable pairs (c,d): d:a->m in D, c:m->b in C
    arrows = {}
    names = {}     # (c,d) -> name
    for d in D.arrows:
        a, m = D.dom(d), D.cod(d)
        for c in C.arrows:
            if C.dom(c) != m: continue
            b = C.cod(c)
            nm = (c, d)
            arrows[nm] = (a, b)
            names[nm] = nm
    ident = {o: (C.ident[o], D.ident[o]) for o in O}

    def lact(d, c):  # ^d c  (the C part of d o c)
        return lam[(d, c)][0]
    def ract(d, c):  # d^c  (the D part of d o c)
        return lam[(d, c)][1]

    comp = {}
    for n2 in arrows:        # second/outer: (c2,d2): b->cc
        c2, d2 = n2
        for n1 in arrows:    # first/inner:  (c1,d1): a->b
            c1, d1 = n1
            if arrows[n1][1] != arrows[n2][0]:
                continue
            # need d2 o c1 :  d2: b->m2 in D, c1: m1->b in C  -> composable since cod(c1)=b=dom(d2)
            if D.dom(d2) != C.cod(c1):
                # shouldn't happen given object matching, but guard
                continue
            lc = lact(d2, c1)   # in C: k->m2
            rd = ract(d2, c1)   # in D: m1->k
            # new c = c2 o lc  (C),  new d = rd . d1 (D, = rd o d1)
            newc = C.compose(c2, lc)
            newd = D.compose(rd, d1)
            comp[(n2, n1)] = (newc, newd)
    return FinCat(O, arrows, comp, ident)


def check_zs_axioms(C, D, lam, verbose=False):
    """Check units + ZS1-ZS4 for the distributive law lam.
       lact(d,c)=^d c in C ; ract(d,c)=d^c in D ; with d o c = (^d c) o (d^c)."""
    def lact(d, c): return lam[(d, c)][0]
    def ract(d, c): return lam[(d, c)][1]
    ok = True
    def fail(msg, *a):
        nonlocal ok
        ok = False
        if verbose: print("AXIOM FAIL", msg, a)

    # domain of definition: pairs (d,c) with dom(d)==cod(c)
    pairs = [(d, c) for d in D.arrows for c in C.arrows if D.dom(d) == C.cod(c)]

    # 0. the defining relation  d o c = (^d c) o (d^c) must hold *in some ambient*.
    #    We can't check it without K; instead we check internal consistency:
    #    typing.  ^d c in C with dom = cod(d^c), cod = cod(d); d^c in D with dom=dom(c).
    for (d, c) in pairs:
        lc, rd = lact(d, c), ract(d, c)
        if C.cod(lc) != D.cod(d): fail("type lc cod", d, c)
        if D.dom(rd) != C.dom(c): fail("type rd dom", d, c)
        if C.dom(lc) != D.cod(rd): fail("type middle", d, c)

    # Units (U-left): id_D acts trivially: ^{id} c = c, id^c = id_{dom c}
    for c in C.arrows:
        m = C.cod(c); a = C.dom(c)
        idm = D.ident[m]
        if lact(idm, c) != c: fail("Uleft lact", c)
        if ract(idm, c) != D.ident[a]: fail("Uleft ract", c)
    # Units (U-right): acting on identity C-arrow: ^d id = id_{cod d}, d^{id}=d
    for d in D.arrows:
        b = D.dom(d)
        idb = C.ident[b]
        if lact(d, idb) != C.ident[D.cod(d)]: fail("Uright lact", d)
        if ract(d, idb) != d: fail("Uright ract", d)

    # ZS2: D acts on C from the left:  ^{d' d} c = ^{d'}(^d c)
    #   d:b->? , d':?->? composable d' o d ; c: m->b in C
    for c in C.arrows:
        b = C.cod(c)
        for d in D.arrows:
            if D.dom(d) != b: continue
            for dp in D.arrows:
                if D.dom(dp) != D.cod(d): continue
                ddp = D.compose(dp, d)  # d' o d
                lhs = lact(ddp, c)
                rhs = lact(dp, lact(d, c))
                if lhs != rhs: fail("ZS2", dp, d, c, lhs, rhs)
    # ZS3 (cocycle for restriction wrt D-composition):
    #   (d' d)^c = (d')^{^d c} . d^c
    for c in C.arrows:
        b = C.cod(c)
        for d in D.arrows:
            if D.dom(d) != b: continue
            for dp in D.arrows:
                if D.dom(dp) != D.cod(d): continue
                ddp = D.compose(dp, d)
                lhs = ract(ddp, c)
                rhs = D.compose(ract(dp, lact(d, c)), ract(d, c))
                if lhs != rhs: fail("ZS3", dp, d, c, lhs, rhs)
    # ZS1: action distributes over C-composition:
    #   ^d (c2 o c1) = (^d c2) o (^{d^{c2}} c1)
    #   c1: a->m, c2: m->b in C ; d: b->? in D
    for c1 in C.arrows:
        for c2 in C.arrows:
            if C.cod(c1) != C.dom(c2): continue
            c21 = C.compose(c2, c1)
            for d in D.arrows:
                if D.dom(d) != C.cod(c2): continue
                lhs = lact(d, c21)
                rhs = C.compose(lact(d, c2), lact(ract(d, c2), c1))
                if lhs != rhs: fail("ZS1", d, c2, c1, lhs, rhs)
    # ZS4: restriction over C-composition:
    #   d^{c2 o c1} = (d^{c2})^{c1}
    for c1 in C.arrows:
        for c2 in C.arrows:
            if C.cod(c1) != C.dom(c2): continue
            c21 = C.compose(c2, c1)
            for d in D.arrows:
                if D.dom(d) != C.cod(c2): continue
                lhs = ract(d, c21)
                rhs = ract(ract(d, c2), c1)
                if lhs != rhs: fail("ZS4", d, c2, c1, lhs, rhs)
    return ok


# ---------------------------------------------------------------------------
# Extract a distributive law from an ambient K with wide subcats C, D forming SFS.
# ---------------------------------------------------------------------------

def extract_lambda(K, Cset, Dset):
    """Cset, Dset: sets of arrow-names of K that are the wide subcategories.
       Returns lam dict (d,c)->(c2,d2) by unique-factorizing d o c in K, or None
       if some d o c has no/non-unique C-then-D factorization."""
    # build factorization table: every K-arrow f -> unique (c,d), c in C, d in D, f=c o d
    fact = {}
    for f in K.arrows:
        cands = []
        for c in Cset:
            for d in Dset:
                if K.cod(d) != K.dom(c): continue
                if K.dom(d) != K.dom(f) or K.cod(c) != K.cod(f): continue
                if K.compose(c, d) == f:
                    cands.append((c, d))
        if len(cands) != 1:
            return None, f, cands
        fact[f] = cands[0]
    lam = {}
    for d in Dset:
        for c in Cset:
            if K.cod(c) != K.dom(d): continue
            f = K.compose(d, c)     # d o c in K
            lam[(d, c)] = fact[f]   # (c2,d2)
    return lam, fact, None
