"""
Verify Neil Ghani's Ch4 conjecture:
  A monad M on Set lifts to a comonad G on Cont via G(S,P)=(S, M o P),
  the position-contravariance turning M's 3 monad laws into G's 3 comonad laws.
  Dually, a comonad W on Set lifts to a monad H on Cont.

Conventions (per task):
  Container (S,P): S finite set of shapes, P: s -> finite set of positions.
  Morphism (S,P)->(T,Q): forward u:S->T, and for each s a BACKWARD map Q(u s)->P(s).
  Composition composes forwards, composes backwards in opposite order.
"""

# ---------- Containers and morphisms ----------

class Cont:
    def __init__(self, S, P):
        self.S = list(S)            # shapes
        self.P = {s: list(P[s]) for s in S}   # positions per shape

class Mor:
    """morphism src -> tgt. fwd: dict s->t. bwd: dict s -> dict{ tgt_pos : src_pos }."""
    def __init__(self, src, tgt, fwd, bwd):
        self.src, self.tgt, self.fwd, self.bwd = src, tgt, fwd, bwd

def ident(A):
    return Mor(A, A, {s: s for s in A.S},
               {s: {p: p for p in A.P[s]} for s in A.S})

def compose(psi, phi):
    """phi: A->B, psi: B->C. returns A->C."""
    # structural compatibility (objects are rebuilt fresh, so compare shapes/positions)
    assert phi.tgt.S == psi.src.S and phi.tgt.P == psi.src.P
    A, C = phi.src, psi.tgt
    fwd = {s: psi.fwd[phi.fwd[s]] for s in A.S}
    bwd = {}
    for s in A.S:
        t = phi.fwd[s]          # in B
        g = psi.bwd[t]          # C.P[fwd_C(t)] -> B.P[t]
        f = phi.bwd[s]          # B.P[t] -> A.P[s]
        bwd[s] = {c: f[g[c]] for c in C.P[fwd[s]]}
    return Mor(A, C, fwd, bwd)

def eq(m1, m2):
    if m1.fwd != m2.fwd:
        return False
    # compare backward maps (as dicts) over identical domains
    if set(m1.bwd) != set(m2.bwd):
        return False
    for s in m1.bwd:
        if m1.bwd[s] != m2.bwd[s]:
            return False
    return True

# ---------- Endofunctor data on finite Set ----------
# An "F" supplies: obj(list)->list of elements of F(X); fmap(callable)->callable on F-elements.
# A Monad adds eta(elem)->F elem and mu(F(F) elem)->F elem.
# A Comonad adds eps(F elem)->elem and delta(F elem)->F(F) elem.

class Functor:
    def __init__(self, obj, fmap):
        self.obj, self.fmap = obj, fmap

# --- Maybe monad: M X = X + {bot} ---
def maybe():
    def obj(X):
        return [('inl', x) for x in X] + [('bot',)]
    def fmap(f):
        return lambda e: ('inl', f(e[1])) if e[0]=='inl' else ('bot',)
    def eta(x):
        return ('inl', x)
    def mu(e):                      # e in M(M X): ('inl', m) or ('bot',)
        return e[1] if e[0]=='inl' else ('bot',)
    F = Functor(obj, fmap); F.eta, F.mu = eta, mu; F.name='Maybe'
    return F

# --- Writer over Z/2: M X = X x Z/2 ---
def writer(mu_op=lambda a,b:(a+b)%2, eta_tag=0):
    def obj(X):
        return [('w', x, a) for x in X for a in (0,1)]
    def fmap(f):
        return lambda e: ('w', f(e[1]), e[2])
    def eta(x):
        return ('w', x, eta_tag)
    def mu(e):                      # e = ('w', ('w', x, a), b)
        inner = e[1]; b = e[2]
        return ('w', inner[1], mu_op(inner[2], b))
    F = Functor(obj, fmap); F.eta, F.mu = eta, mu; F.name='Writer/Z2'
    return F

# --- Product comonad: W X = X x E, basepoint e0 ---
def product_comonad(E=(0,1), e0=0):
    def obj(X):
        return [('p', x, e) for x in X for e in E]
    def fmap(f):
        return lambda e: ('p', f(e[1]), e[2])
    def eps(e):                     # ('p', x, e') -> x
        return e[1]
    def delta(e):                   # ('p', x, e') -> ('p', ('p', x, e'), e')
        return ('p', e, e[2])
    F = Functor(obj, fmap); F.eps, F.delta = eps, delta; F.name='Product(comonad)'
    return F

# ---------- Lifting a monad M to comonad G on Cont ----------

def Gobj(M, A):
    return Cont(A.S, {s: M.obj(A.P[s]) for s in A.S})

def Gmor(M, phi):
    """apply functor G to morphism phi: A->B, giving G A -> G B."""
    GA, GB = Gobj(M, phi.src), Gobj(M, phi.tgt)
    fwd = dict(phi.fwd)
    bwd = {}
    for s in GA.S:
        t = phi.fwd[s]
        fcall = lambda p, s=s: phi.bwd[s][p]        # B.P[t] -> A.P[s]
        Mf = M.fmap(fcall)
        bwd[s] = {m: Mf(m) for m in GB.P[t]}         # M(B.P[t]) -> M(A.P[s])
    return Mor(GA, GB, fwd, bwd)

def eps_G(M, A):
    """eps_A : G A -> A, backward = eta."""
    GA = Gobj(M, A)
    fwd = {s: s for s in A.S}
    bwd = {s: {p: M.eta(p) for p in A.P[s]} for s in A.S}   # A.P[s] -> M(A.P[s])
    return Mor(GA, A, fwd, bwd)

def delta_G(M, A):
    """delta_A : G A -> G G A, backward = mu."""
    GA = Gobj(M, A); GGA = Gobj(M, GA)
    fwd = {s: s for s in A.S}
    bwd = {s: {mm: M.mu(mm) for mm in GGA.P[s]} for s in A.S}  # M(M P) -> M P
    return Mor(GA, GGA, fwd, bwd)

def comonad_laws_G(M, A):
    GA = Gobj(M, A)
    d = delta_G(M, A)
    # law1 counit-left (eps G): eps_{GA} o delta_A = id_GA
    l1 = compose(eps_G(M, GA), d)
    # law2 counit-right (G eps): G(eps_A) o delta_A = id_GA
    l2 = compose(Gmor(M, eps_G(M, A)), d)
    # law3 coassoc: (G delta_A) o delta_A = (delta_{GA}) o delta_A
    lhs = compose(Gmor(M, d), d)
    rhs = compose(delta_G(M, GA), d)
    return {
        'counit-left  (eps G)': eq(l1, ident(GA)),
        'counit-right (G eps)': eq(l2, ident(GA)),
        'coassoc':              eq(lhs, rhs),
    }

# ---------- Lifting a comonad W to monad H on Cont ----------

def Hobj(W, A):
    return Cont(A.S, {s: W.obj(A.P[s]) for s in A.S})

def Hmor(W, phi):
    HA, HB = Hobj(W, phi.src), Hobj(W, phi.tgt)
    fwd = dict(phi.fwd); bwd = {}
    for s in HA.S:
        t = phi.fwd[s]
        fcall = lambda p, s=s: phi.bwd[s][p]
        Wf = W.fmap(fcall)
        bwd[s] = {m: Wf(m) for m in HB.P[t]}
    return Mor(HA, HB, fwd, bwd)

def eta_H(W, A):
    """eta_A : A -> H A, backward = W.eps."""
    HA = Hobj(W, A)
    fwd = {s: s for s in A.S}
    bwd = {s: {w: W.eps(w) for w in HA.P[s]} for s in A.S}   # W(P) -> P
    return Mor(A, HA, fwd, bwd)

def mu_H(W, A):
    """mu_A : H H A -> H A, backward = W.delta."""
    HA = Hobj(W, A); HHA = Hobj(W, HA)
    fwd = {s: s for s in A.S}
    bwd = {s: {w: W.delta(w) for w in HA.P[s]} for s in A.S}  # W(P) -> W(W(P))
    return Mor(HHA, HA, fwd, bwd)

def monad_laws_H(W, A):
    HA = Hobj(W, A)
    m = mu_H(W, A)
    # left unit: mu_A o H(eta_A) = id_HA
    lu = compose(m, Hmor(W, eta_H(W, A)))
    # right unit: mu_A o eta_{HA} = id_HA
    ru = compose(m, eta_H(W, HA))
    # assoc: mu_A o H(mu_A) = mu_A o mu_{HA}
    lhs = compose(m, Hmor(W, mu_H(W, A)))
    rhs = compose(m, mu_H(W, HA))
    return {
        'left-unit':  eq(lu, ident(HA)),
        'right-unit': eq(ru, ident(HA)),
        'assoc':      eq(lhs, rhs),
    }

# ---------- Test container ----------
A = Cont(['a', 'b'], {'a': [0, 1], 'b': [0]})

def show(title, d):
    print(title)
    for k, v in d.items():
        print(f"   {k:22s} : {'PASS' if v else 'FAIL'}")

print("="*60)
print("Monad -> Comonad on Cont   (positions become M o P)")
print("="*60)
for M in [maybe(), writer()]:
    show(f"M = {M.name}", comonad_laws_G(M, A))

print()
print("="*60)
print("Comonad -> Monad on Cont (dual)   (positions become W o P)")
print("="*60)
W = product_comonad()
show(f"W = {W.name}", monad_laws_H(W, A))

print()
print("="*60)
print("NEGATIVE CONTROLS (must FAIL)")
print("="*60)
# (a) broken, non-associative mu (NAND on Z/2 tags) -> coassoc should FAIL
Mbad_mu = writer(mu_op=lambda a, b: 1 - (a * b))   # NAND, non-associative
show("M = Writer with NAND mu (broken assoc)", comonad_laws_G(Mbad_mu, A))
# (b) broken eta (wrong tag 1 instead of 0) -> a counit law should FAIL
Mbad_eta = writer(eta_tag=1)
show("M = Writer with eta_tag=1 (broken unit)", comonad_laws_G(Mbad_eta, A))

# ---------- Extra checks for the PROVE session (2026-07-25) ----------
# (i) G preserves binary coproducts of containers (needed for Lan_y characterisation).
# (ii) naturality of eps and delta on a nontrivial morphism.

def coprod(A, B):
    # disjoint union of shapes with tags; positions carried over
    S = [('L', s) for s in A.S] + [('R', s) for s in B.S]
    P = {}
    for s in A.S: P[('L', s)] = A.P[s]
    for s in B.S: P[('R', s)] = B.P[s]
    return Cont(S, P)

def test_G_preserves_coproduct(M, A, B):
    GA, GB = Gobj(M, A), Gobj(M, B)
    lhs = Gobj(M, coprod(A, B))       # G(A + B)
    rhs = coprod(GA, GB)              # G A + G B
    return lhs.S == rhs.S and lhs.P == rhs.P

# a nontrivial morphism phi: A -> Cbig  (A=({a,b},...) as in file)
Cbig = Cont(['x'], {'x': [10, 11, 12]})
phi = Mor(A, Cbig, {'a': 'x', 'b': 'x'},
          {'a': {10: 0, 11: 1, 12: 0}, 'b': {10: 0, 11: 0, 12: 0}})

def test_eps_natural(M, phi):
    # eps_tgt o G(phi) == phi o eps_src
    lhs = compose(eps_G(M, phi.tgt), Gmor(M, phi))
    rhs = compose(phi, eps_G(M, phi.src))
    return eq(lhs, rhs)

def test_delta_natural(M, phi):
    # delta_tgt o G(phi) == G^2(phi) o delta_src
    lhs = compose(delta_G(M, phi.tgt), Gmor(M, phi))
    rhs = compose(Gmor(M, Gmor(M, phi)), delta_G(M, phi.src))
    return eq(lhs, rhs)

Bc = Cont(['c'], {'c': [7]})
print("\n=== PROVE extras ===")
for M in (maybe(), writer()):
    print(f"M={M.name}: G preserves coproduct:", test_G_preserves_coproduct(M, A, Bc),
          "| eps natural:", test_eps_natural(M, phi),
          "| delta natural:", test_delta_natural(M, phi))

# ---------- Part (a): G(p) = {M/p}, the left coclosure of composition ----------
# Verify Poly({M/p}, r) ≅ Poly(p, r◁M) by COUNTING, with M=Maybe (=y+1, polynomial so r◁M is poly).
# Poly hom count: |Poly(sum_i y^{A_i}, sum_j y^{B_j})| = prod_i sum_j |A_i|^{|B_j|}.
from itertools import product as iproduct

def poly_hom_count(src_exps, tgt_exps):
    # src = list of exponent-set-sizes A_i ; tgt = list of B_j.  |Poly(src,tgt)| = prod_i sum_j A_i^{B_j}
    total = 1
    for a in src_exps:
        total *= sum(a**b for b in tgt_exps)
    return total

# M = Maybe: on a set of size n, |M(n)| = n+1.
def Msize(n): return n+1

# p = (S,P): exponents = [|Ps|]. Take p with position sizes [2,0,1].
p_exps = [2, 0, 1]
# {M/p} = G(p): exponents [ |M(Ps)| ] = [n+1]
Gp_exps = [Msize(n) for n in p_exps]     # [3,1,2]

# r ranges over several test polynomials (list of exponent sizes)
for r_exps in ([1], [0,2], [3,1], [2,2,0]):
    # r ◁ M : (r◁M)(X)=r(M X). r = sum_j y^{R_j}, so (r◁M)(X)= sum_j (M X)^{R_j} = sum_j |M X|^{R_j}.
    # As a polynomial in X this is NOT a single monomial, but for counting Poly(p, r◁M) we only need
    # (r◁M) evaluated at the sets p[i]=Ps: |Poly(p, r◁M)| = prod_i (r◁M)(Ps) = prod_i sum_j |M(Ps)|^{R_j}.
    lhs = poly_hom_count(Gp_exps, r_exps)                  # Poly({M/p}, r)
    rhs = 1
    for n in p_exps:                                        # Poly(p, r◁M) = prod_i sum_j |M(Ps)|^{R_j}
        rhs *= sum(Msize(n)**Rj for Rj in r_exps)
    print(f"r_exps={r_exps}:  Poly(G p, r)={lhs}  Poly(p, r◁M)={rhs}  MATCH={lhs==rhs}")
