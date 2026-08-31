"""
Sigma-container lifting monad-law check for Reader / State base monads.

A container C = (S,P): shapes S, positions P(s).  A morphism (S,P)->(S',P') is
  fwd : S -> S'   (forward on shapes)
  bwd : for each s, P'(fwd s) -> P(s)   (BACKWARD on positions).

Sigma-lifting endofunctor on Cont:
  T C = (M S, P^Sigma),   P^Sigma(m) = COPRODUCT_{b in lv(m)} P(x_b)
  positions of TC at m = { (b,p) : b leaf of m, p in P(label(m,b)) }.

  Unit  eta^Sigma_C : C -> TC
     fwd  s |-> eta_S(s)   (pure element, all leaves labelled s)
     bwd  P^Sigma(eta s) -> P(s):  (b,p) |-> p      [CODIAGONAL / fold: no choice]

  Mult  mu^Sigma_C : TTC -> TC
     fwd  mm |-> mu(mm)
     bwd  P^Sigma(mu mm) -> (P^Sigma)^Sigma(mm):  (L,p) |-> (sigma(mm,L), p)
          where sigma : lv(mu mm) -> I(mm) is the reverse-total section
          (Reader: L=e |-> diagonal token (e,e); State: L=s0 |-> threaded (s0,h(s0))).
          [CHOICE: picks one inner token per surviving leaf, label-matched.]

We test LEFT UNIT, RIGHT UNIT, ASSOCIATIVITY of (T, eta^Sigma, mu^Sigma) as
container morphisms.  fwd equality = base-monad law; bwd equality = the content.
"""
from itertools import product
import random


# ---------------------------------------------------------------------------
# Containers as (pos function, optional shape list)
# ---------------------------------------------------------------------------
class Container:
    def __init__(self, pos_fn, shapes=None):
        self._pos = pos_fn
        self.shapes = shapes            # list, or None if not enumerated

    def pos(self, s):
        return self._pos(s)


def T_container(M, C):
    # shapes kept LAZY (None): enumerating M.elements twice-nested blows up.
    def pos_fn(m):
        return [(b, p) for b in M.leaves(m) for p in C.pos(M.label(m, b))]
    return Container(pos_fn, shapes=None)


# ---------------------------------------------------------------------------
# Morphisms as objects with lazy fwd / bwd (bwd(s) returns dict {codpos:dompos})
# ---------------------------------------------------------------------------
class Mor:
    def __init__(self, dom, cod, fwd, bwd):
        self.dom = dom
        self.cod = cod
        self.fwd = fwd
        self.bwd = bwd


def eta(M, C):
    TC = T_container(M, C)
    def fwd(s):
        return M.unit(s)
    def bwd(s):
        u = M.unit(s)
        # all leaves of u labelled s, so P^Sigma(u) = coproduct of copies of P(s)
        return {(b, p): p for b in M.leaves(u) for p in C.pos(s)}
    return Mor(C, TC, fwd, bwd)


def mu(M, C):
    TC = T_container(M, C)
    TTC = T_container(M, TC)
    def fwd(mm):
        return M.mult(mm)
    def bwd(mm):
        mmm = M.mult(mm)
        d = {}
        for L in M.leaves(mmm):
            b, c = M.sigma(mm, L)
            for p in C.pos(M.label(mmm, L)):
                d[(L, p)] = (b, (c, p))
        return d
    return Mor(TTC, TC, fwd, bwd)


def T_mor(M, mor):
    TC = T_container(M, mor.dom)
    TD = T_container(M, mor.cod)
    D = mor.cod
    def fwd(m):
        return M.mmap(mor.fwd, m)
    def bwd(m):
        d = {}
        for b in M.leaves(m):
            lab = M.label(m, b)
            inner = mor.bwd(lab)               # dict {D-pos : dom-pos}
            for q in D.pos(mor.fwd(lab)):
                d[(b, q)] = (b, inner[q])
        return d
    return Mor(TC, TD, fwd, bwd)


def compose(g, f):
    """first f then g;  f:A->B, g:B->C  =>  g o f : A->C."""
    def fwd(a):
        return g.fwd(f.fwd(a))
    def bwd(a):
        fa = f.fwd(a)
        gb = g.bwd(fa)                          # {C-pos : B-pos}
        fb = f.bwd(a)                           # {B-pos : A-pos}
        target_shape = g.fwd(fa)
        return {cpos: fb[gb[cpos]] for cpos in g.cod.pos(target_shape)}
    return Mor(f.dom, g.cod, fwd, bwd)


def identity(C):
    return Mor(C, C, lambda s: s, lambda s: {p: p for p in C.pos(s)})


def mor_eq_on(m1, m2, shapes):
    """Check two morphisms agree (fwd and bwd) on the given list of dom shapes."""
    for s in shapes:
        if m1.fwd(s) != m2.fwd(s):
            return ("fwd", s, m1.fwd(s), m2.fwd(s))
        if m1.bwd(s) != m2.bwd(s):
            return ("bwd", s, m1.bwd(s), m2.bwd(s))
    return None


# ---------------------------------------------------------------------------
# Base monads
# ---------------------------------------------------------------------------
class ReaderM:
    name = "Reader"
    def __init__(self, E):
        self.E = E
    def elements(self, labels):
        return list(product(labels, repeat=self.E))
    def leaves(self, m):
        return range(self.E)
    def label(self, m, b):
        return m[b]
    def mmap(self, f, m):
        return tuple(f(x) for x in m)
    def unit(self, s):
        return tuple(s for _ in range(self.E))
    def mult(self, mm):
        return tuple(mm[e][e] for e in range(self.E))
    def sigma(self, mm, L):
        return (L, L)                            # diagonal token
    def random_elt(self, depth, base_labels, rng):
        if depth == 0:
            return rng.choice(base_labels)
        return tuple(self.random_elt(depth - 1, base_labels, rng)
                     for _ in range(self.E))


class StateM:
    name = "State"
    def __init__(self, St):
        self.St = St
    def elements(self, labels):
        cells = list(product(range(self.St), labels))
        return list(product(cells, repeat=self.St))
    def leaves(self, m):
        return range(self.St)
    def label(self, m, b):
        return m[b][1]
    def mmap(self, f, m):
        return tuple((s1, f(lab)) for (s1, lab) in m)
    def unit(self, s):
        return tuple((s0, s) for s0 in range(self.St))
    def mult(self, mm):
        # mm[s0] = (s1, g); result[s0] = g[s1]  (a cell (s',label))
        return tuple(mm[s0][1][mm[s0][0]] for s0 in range(self.St))
    def sigma(self, mm, L):
        s1 = mm[L][0]                            # threaded state
        return (L, s1)
    def random_elt(self, depth, base_labels, rng):
        if depth == 0:
            return rng.choice(base_labels)
        return tuple((rng.randrange(self.St),
                      self.random_elt(depth - 1, base_labels, rng))
                     for _ in range(self.St))


# ---------------------------------------------------------------------------
# Test drivers
# ---------------------------------------------------------------------------
def base_containers():
    return [
        ("1shape/2pos",  Container(lambda s: list(range({0: 2}[s])), shapes=[0])),
        ("2shape/1,2",   Container(lambda s: list(range({0: 1, 1: 2}[s])), shapes=[0, 1])),
        ("2shape/2,3",   Container(lambda s: list(range({0: 2, 1: 3}[s])), shapes=[0, 1])),
    ]


def test_unit_laws(M):
    print(f"\n=== {M.name} : UNIT LAWS (full enumeration of TC) ===")
    for cname, C in base_containers():
        TC = T_container(M, C)
        etaC = eta(M, C)
        etaTC = eta(M, TC)
        muC = mu(M, C)
        T_etaC = T_mor(M, etaC)
        idTC = identity(TC)
        left = compose(muC, etaTC)     # mu . eta_T
        right = compose(muC, T_etaC)   # mu . T(eta)
        shapes = M.elements(C.shapes)  # TC shapes (one level, small)
        rL = mor_eq_on(left, idTC, shapes)
        rR = mor_eq_on(right, idTC, shapes)
        print(f"  [{cname}]  #TC-shapes={len(shapes)}")
        print(f"     LEFT  unit (mu.eta_T = id):  {'PASS' if rL is None else 'FAIL'}"
              + ("" if rL is None else f"  cex@{rL[0]} shape={rL[1]}"))
        print(f"     RIGHT unit (mu.T(eta)= id):  {'PASS' if rR is None else 'FAIL'}"
              + ("" if rR is None else f"  cex@{rR[0]} shape={rR[1]}"))
        if rL is not None:
            print(f"        left  side={rL[2]}\n        id    ={rL[3]}")
        if rR is not None:
            print(f"        right side={rR[2]}\n        id    ={rR[3]}")


def test_assoc(M, n_samples=3000, seed=0):
    print(f"\n=== {M.name} : ASSOCIATIVITY (mu.mu_T = mu.T(mu)) [random sample] ===")
    rng = random.Random(seed)
    for cname, C in base_containers():
        TC = T_container(M, C)
        muC = mu(M, C)
        muTC = mu(M, TC)
        T_muC = T_mor(M, muC)
        LHS = compose(muC, muTC)       # mu . mu_T
        RHS = compose(muC, T_muC)      # mu . T(mu)
        # sample TTTC shapes = depth-3 nested M-elements over base labels
        samples = [M.random_elt(3, C.shapes, rng) for _ in range(n_samples)]
        cex = mor_eq_on(LHS, RHS, samples)
        print(f"  [{cname}]  #samples={n_samples}: "
              f"{'PASS' if cex is None else 'FAIL'}"
              + ("" if cex is None else f"  cex@{cex[0]}"))
        if cex is not None:
            print(f"        shape mmm = {cex[1]}")
            print(f"        LHS = {cex[2]}")
            print(f"        RHS = {cex[3]}")


if __name__ == "__main__":
    for M in [ReaderM(2), StateM(2), ReaderM(3)]:
        print("#" * 70)
        print(f"# BASE MONAD: {M.name}  (param={getattr(M,'E',getattr(M,'St',None))})")
        print("#" * 70)
        test_unit_laws(M)
        test_assoc(M)
