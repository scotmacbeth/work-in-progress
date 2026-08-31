"""
Core representations for the Day-convolution / Spivak-family verification.

Finite sets  : python frozensets of hashable tags.
Functions    : python dicts (domain element -> codomain element), we also use
               frozenset-of-pairs form when we need hashability.
Container    : Cont(S, P) where S is a frozenset of shapes and P is a dict
               shape -> frozenset of positions.
Morphism     : Mor(u, f) where u : S -> S' (dict) and f[s] : P'(u s) -> P(s)
               (dict), i.e. CONTRAVARIANT on positions (standard container
               morphism, so that it induces a natural transformation of
               extensions).
"""
from itertools import product as iproduct
from dataclasses import dataclass
from typing import Dict, FrozenSet, Any


# ---------------------------------------------------------------- finite sets
def inl(x):  return ('inl', x)
def inr(x):  return ('inr', x)


def dunion(A, B):
    """Tagged disjoint union A + B."""
    return frozenset([inl(a) for a in A] + [inr(b) for b in B])


def cprod(A, B):
    """Cartesian product A x B."""
    return frozenset((a, b) for a in A for b in B)


EMPTY = frozenset()


def funcs(dom, cod):
    """All functions dom -> cod, as dicts.  |funcs(D,C)| = |C|^|D| (1 if D empty)."""
    dom = sorted(dom, key=repr)
    for vals in iproduct(*[sorted(cod, key=repr) for _ in dom]):
        yield dict(zip(dom, vals))


def hfun(d):
    """Hashable form of a function-dict: frozenset of (in, out) pairs."""
    return frozenset(d.items())


# ----------------------------------------------------------------- containers
@dataclass(frozen=True)
class Cont:
    S: FrozenSet[Any]                 # shapes
    P: Any                            # dict: shape -> frozenset of positions

    def pos(self, s):
        return self.P[s]

    def __repr__(self):
        items = sorted(((repr(s), sorted(map(repr, self.P[s]))) for s in self.S))
        return "Cont{" + ", ".join(f"{s}:{len(p)}pos" for s, p in items) + "}"

    def signature(self):
        """Multiset of position-counts, a readable invariant."""
        return sorted(len(self.P[s]) for s in self.S)


def extension(C, X):
    """[[C]](X) = { (s, f) : s in S, f : P(s) -> X }, f in hashable form.
    Materialises the whole set -- only use when it is small."""
    out = set()
    for s in C.S:
        for f in funcs(C.P[s], X):
            out.add((s, hfun(f)))
    return frozenset(out)


def count_extension(C, X):
    """|[[C]](X)|, counted by STREAMING the same elementwise enumeration used by
    extension() -- no set is materialised, so it does not blow up memory.

    This is only faithful if funcs() enumerates each function exactly once.
    That is cross-validated against extension() in validate_counting() below."""
    total = 0
    for s in C.S:
        for _ in funcs(C.P[s], X):
            total += 1
    return total


def validate_counting(containers, Xsizes=(0, 1, 2, 3)):
    """Cross-check: streaming count == size of the materialised set of elements.
    Guards against funcs() emitting duplicates (which would make counts a lie)."""
    bad = []
    for C in containers:
        for n in Xsizes:
            X = frozenset(f"x{i}" for i in range(n))
            if count_extension(C, X) != len(extension(C, X)):
                bad.append((C, n, count_extension(C, X), len(extension(C, X))))
    return bad


# --------------------------------------------------- the four (five) structures
def conv(C, D, star):
    """Convolution tensor: shapes S x T, positions (s,t) |-> star(P(s), Q(t))."""
    S = cprod(C.S, D.S)
    P = {(s, t): star(C.P[s], D.P[t]) for s in C.S for t in D.S}
    return Cont(S, P)


def prod(C, D):
    return conv(C, D, dunion)          # positions P(s) + Q(t)


def dirichlet(C, D):
    return conv(C, D, cprod)           # positions P(s) x Q(t)


def coprod(C, D):
    S = dunion(C.S, D.S)
    P = {}
    for s in C.S:
        P[inl(s)] = frozenset(inl(p) for p in C.P[s])
    for t in D.S:
        P[inr(t)] = frozenset(inr(q) for q in D.P[t])
    return Cont(S, P)


def compose(C, D):
    """C <| D : shapes (s, f) with f : P(s) -> T ; positions (p,q), q in Q(f p)."""
    S = set()
    P = {}
    for s in C.S:
        for f in funcs(C.P[s], D.S):
            sh = (s, hfun(f))
            S.add(sh)
            P[sh] = frozenset((p, q) for p in C.P[s] for q in D.P[f[p]])
    return Cont(frozenset(S), P)


# ---------------------------------------------------------------- morphisms
@dataclass(frozen=True)
class Mor:
    src: Cont
    tgt: Cont
    u: Any            # dict  S -> S'
    f: Any            # dict  s -> (dict  P'(u s) -> P(s))


def check_mor_types(m):
    """The morphism is well-typed: u lands in tgt.S, f[s] : P'(u s) -> P(s) total."""
    errs = []
    for s in m.src.S:
        if s not in m.u:
            errs.append(f"u undefined at {s}");  continue
        us = m.u[s]
        if us not in m.tgt.S:
            errs.append(f"u({s})={us} not a target shape");  continue
        dom_expected = m.tgt.P[us]
        g = m.f[s]
        if frozenset(g.keys()) != frozenset(dom_expected):
            errs.append(f"f[{s}] domain {set(g.keys())} != P'(u s) {set(dom_expected)}")
            continue
        for x, y in g.items():
            if y not in m.src.P[s]:
                errs.append(f"f[{s}]({x})={y} not in P({s})")
    return errs


def is_bijection(g, dom, cod):
    if frozenset(g.keys()) != frozenset(dom):
        return False, "domain mismatch"
    img = set(g.values())
    if not img <= set(cod):
        return False, "image escapes codomain"
    if len(img) != len(dom):
        return False, "not injective"
    if img != set(cod):
        return False, "not surjective"
    return True, "bijection"


def is_iso(m):
    """A container morphism is an iso iff u is a bijection of shapes and each
    position map f[s] is a bijection."""
    ok_u, why_u = is_bijection(m.u, m.src.S, m.tgt.S)
    if not ok_u:
        return False, f"shape map: {why_u}"
    for s in m.src.S:
        ok, why = is_bijection(m.f[s], m.tgt.P[m.u[s]], m.src.P[s])
        if not ok:
            return False, f"position map at {s}: {why}"
    return True, "iso"


# ---------------------------------------------- Spivak's family  A v_S B
def L(a):        return ('l', a)
def M(a, s, b):  return ('m', (a, s, b))
def R(b):        return ('r', b)


def vee(A, B, S):
    """A v_S B  =  A  +  A x S x B  +  B   (three tagged pieces)."""
    out = [L(a) for a in A] + [M(a, s, b) for a in A for s in S for b in B] \
        + [R(b) for b in B]
    return frozenset(out)


def vee_map(fA, fB, S):
    """Functorial action: (fA v fB) on elements of A v_S B."""
    def go(x):
        tag, val = x
        if tag == 'l':  return L(fA[val])
        if tag == 'r':  return R(fB[val])
        a, s, b = val
        return M(fA[a], s, fB[b])
    return go


def lam(B, S):
    """left unitor  lambda : empty v_S B  ->  B."""
    return {R(b): b for b in B}          # the only elements present


def rho(A, S):
    """right unitor  rho : A v_S empty  ->  A."""
    return {L(a): a for a in A}


def alpha(A, B, C, S):
    """associator  (A v B) v C  ->  A v (B v C)   as a dict on tagged elements."""
    d = {}
    AB = vee(A, B, S)
    for x in vee(AB, C, S):
        tag, val = x
        if tag == 'l':
            it, iv = val                      # val in A v B
            if it == 'l':      d[x] = L(iv)                       # a
            elif it == 'r':    d[x] = R(L(iv))                    # b
            else:
                a, s, b = iv
                d[x] = M(a, s, L(b))                             # a-s-b
        elif tag == 'r':
            d[x] = R(R(val))                                     # c
        else:
            blk, s2, c = val                  # blk in A v B
            bt, bv = blk
            if bt == 'l':      d[x] = M(bv, s2, R(c))            # a-s2-c
            elif bt == 'r':    d[x] = R(M(bv, s2, c))            # b-s2-c
            else:
                a, s1, b = bv
                d[x] = M(a, s1, M(b, s2, c))                     # a-s1-b-s2-c
    return d


def alpha_inv(A, B, C, S):
    d = alpha(A, B, C, S)
    inv = {v: k for k, v in d.items()}
    assert len(inv) == len(d)
    return inv


# ------------------------------------------------------------ small test data
def mkset(n, tag='x'):
    return frozenset(f"{tag}{i}" for i in range(n))
