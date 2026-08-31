"""
Generic Kock double-strength commutativity checker for FINITE Set-monads,
plus affineness (|M1|) and the E+A×(-) criterion sweep.  PROVE 2026-07-31.

A monad is given as (obj, fmap, eta, mu):
  obj(X)     : list of elements of M X, for a finite list X
  fmap(f)(m) : functorial action, f a python function on elements
  eta(x)     : x -> M X
  mu(mm)     : M(M X) -> M X   (mm an element of M(M X); elements of M X are hashable)

Strength / costrength are the CANONICAL Set strengths:
  st (m,y) = fmap(lambda x:(x,y))(m)          : M X x Y   -> M(X x Y)
  st'(x,n) = fmap(lambda y:(x,y))(n)          : X x M Y   -> M(X x Y)
Commutative iff  Psi = Phi  where
  Psi(m,n) = mu( fmap(st')( st (m, n) ) )      note st here treats the 2nd slot as MY
  Phi(m,n) = mu( fmap(st )( st'(m, n) ) )
Careful bookkeeping below.
"""
from fractions import Fraction
from itertools import product as iproduct

def is_commutative(obj, fmap, eta, mu, X, Y, verbose=False):
    """Check Psi==Phi on all m in M X, n in M Y. Returns (bool, witness_or_None)."""
    MX = obj(X)
    MY = obj(Y)
    for m in MX:
        for n in MY:
            # Psi = mu . M(st') . st       with st: MX x MY -> M(X x MY)
            # st(m, n): freeze 2nd coord = the WHOLE n (an element of MY)
            st_mn = fmap(lambda x, n=n: (x, n))(m)          # in M(X x MY)
            # M(st'): apply st' to each position (x, n') where n' in MY
            def st_prime_pair(p):
                x, npr = p                                   # npr in MY
                return fmap(lambda y, x=x: (x, y))(npr)       # in M(X x Y)
            MMxy = fmap(st_prime_pair)(st_mn)                # in M(M(X x Y))
            Psi = mu(MMxy)

            # Phi = mu . M(st) . st'       with st': MX x MY -> M(MX x Y)
            st_prime_mn = fmap(lambda y, m=m: (m, y))(n)      # in M(MX x Y)
            def st_pair(p):
                mpr, y = p                                    # mpr in MX
                return fmap(lambda x, y=y: (x, y))(mpr)        # in M(X x Y)
            MMxy2 = fmap(st_pair)(st_prime_mn)                # in M(M(X x Y))
            Phi = mu(MMxy2)

            if Psi != Phi:
                if verbose:
                    print(f"    NON-COMM witness: m={m}, n={n}\n      Psi={Psi}\n      Phi={Phi}")
                return False, (m, n, Psi, Phi)
    return True, None

def affine_size(obj):
    """|M 1|  where 1 = ['*']."""
    return len(obj(['*']))

# ----------------------------------------------------------------------------
# Concrete finite monads
# ----------------------------------------------------------------------------

def identity_monad():
    obj = lambda X: list(X)
    fmap = lambda f: (lambda m: f(m))
    eta = lambda x: x
    mu = lambda mm: mm
    return obj, fmap, eta, mu

def writer_monad(A_elems, mul, unit):
    """M X = A x X. mul(a,a')-> a''; unit in A."""
    obj = lambda X: [(a, x) for a in A_elems for x in X]
    fmap = lambda f: (lambda m: (m[0], f(m[1])))
    eta = lambda x: (unit, x)
    # mm = (a, (a', x))
    mu = lambda mm: (mul(mm[0], mm[1][0]), mm[1][1])
    return obj, fmap, eta, mu

def exc_writer_monad(E_elems, A_elems, mul, unit, act):
    """M X = E + A x X.  inl e = ('e',e); inr(a,x)=('a',a,x).
       act(a,e)-> e' (left A-action on E). writer-with-absorbing-exceptions."""
    def obj(X):
        return [('e', e) for e in E_elems] + [('a', a, x) for a in A_elems for x in X]
    def fmap(f):
        def go(m):
            if m[0] == 'e': return m
            return ('a', m[1], f(m[2]))
        return go
    def eta(x): return ('a', unit, x)
    def mu(mm):
        if mm[0] == 'e': return mm                       # inl e
        a, z = mm[1], mm[2]                              # inr(a, z), z in M X
        if z[0] == 'e': return ('e', act(a, z[1]))       # inr(a, inl e) -> inl(a o e)
        return ('a', mul(a, z[1]), z[2])                 # inr(a, inr(a',x)) -> inr(a.a', x)
    return obj, fmap, eta, mu

def powerset_monad(nonempty=False):
    """M X = P X (finite subsets). elements are frozensets."""
    def obj(X):
        Xs = list(X)
        subs = []
        for r in range(len(Xs) + 1):
            for combo in iproduct([0, 1], repeat=len(Xs)):
                s = frozenset(Xs[i] for i in range(len(Xs)) if combo[i])
                subs.append(s)
        subs = list(set(subs))
        if nonempty:
            subs = [s for s in subs if len(s) > 0]
        return subs
    def fmap(f):
        return lambda s: frozenset(f(x) for x in s)
    def eta(x): return frozenset([x])
    def mu(ss):  # ss a frozenset of frozensets
        out = frozenset().union(*ss) if len(ss) else frozenset()
        return out
    return obj, fmap, eta, mu

def distribution_monad(denom=2):
    """M X = distributions with denominators dividing denom (finite grid), for testing.
       element = tuple(sorted (x, Fraction)) with weights summing to 1. This is a
       PARTIAL enumeration (grid) sufficient to TEST commutativity, not a full monad obj."""
    def grid_dists(Xs):
        # all weight vectors over Xs with entries k/denom summing to 1
        n = len(Xs)
        res = []
        def rec(i, rem, acc):
            if i == n - 1:
                acc2 = acc + [rem]
                res.append(tuple((Xs[j], Fraction(acc2[j], denom)) for j in range(n)))
                return
            for k in range(rem + 1):
                rec(i + 1, rem - k, acc + [k])
        if n == 0:
            return []
        rec(0, denom, [])
        # normalise representation: drop zero-weight, sort
        norm = []
        for d in res:
            dd = tuple(sorted((x, w) for (x, w) in d if w != 0))
            norm.append(dd)
        return list(set(norm))
    def obj(X):
        return grid_dists(list(X))
    def fmap(f):
        def go(d):
            acc = {}
            for (x, w) in d:
                acc[f(x)] = acc.get(f(x), Fraction(0)) + w
            return tuple(sorted(acc.items()))
        return go
    def eta(x): return ((x, Fraction(1)),)
    def mu(dd):  # dd a distribution over distributions
        acc = {}
        for (d, w) in dd:
            for (x, w2) in d:
                acc[x] = acc.get(x, Fraction(0)) + w * w2
        return tuple(sorted((x, w) for (x, w) in acc.items() if w != 0))
    return obj, fmap, eta, mu

# ----------------------------------------------------------------------------
# Monoids
# ----------------------------------------------------------------------------
def trivial_monoid():
    return ['*'], (lambda a, b: '*'), '*'

def Zn_monoid(n):
    return list(range(n)), (lambda a, b: (a + b) % n), 0

def noncomm3_monoid():
    """N = {1,a,b}, identity 1, a.x=a, b.x=b for x in {a,b} (left-zero band + identity)."""
    els = ['1', 'a', 'b']
    def mul(x, y):
        if x == '1': return y
        if y == '1': return x
        return x   # left-zero on {a,b}
    return els, mul, '1'

if __name__ == "__main__":
    X = ['x0', 'x1']; Y = ['y0', 'y1']
    print("=" * 70)
    print("COMMUTATIVITY (Kock double strength) + AFFINENESS |M1|")
    print("=" * 70)

    def report(name, monad, expect_comm, expect_M1):
        obj, fmap, eta, mu = monad
        comm, wit = is_commutative(obj, fmap, eta, mu, X, Y)
        M1 = affine_size(obj)
        ok = (comm == expect_comm) and (M1 == expect_M1)
        print(f"{name:34s} comm={str(comm):5s} (exp {expect_comm})  |M1|={M1} (exp {expect_M1})  {'OK' if ok else '!!!MISMATCH!!!'}")
        return comm, M1

    # Id
    report("Id", identity_monad(), True, 1)
    # Maybe = 1 + (-)  (E={e0}, A trivial)
    report("Maybe = 1+(-)", exc_writer_monad(['e0'], ['*'], (lambda a,b:'*'), '*', (lambda a,e:e)), True, 2)
    # exception 2 + (-)   (|E|=2, A trivial) -> NON-comm (left-vs-right exception)
    report("Exception 2+(-)", exc_writer_monad(['e0','e1'], ['*'], (lambda a,b:'*'), '*', (lambda a,e:e)), False, 2)
    # Writer over Z2 (commutative)
    e,m,u = Zn_monoid(2); report("Writer Z2  (A comm)", writer_monad(e,m,u), True, 2)
    # Writer over noncomm 3-elt monoid -> NON-comm (LOAD-BEARING)
    e,m,u = noncomm3_monoid(); report("Writer N3  (A NON-comm) [LOAD]", writer_monad(e,m,u), False, 3)
    # Powerset with empty
    report("Pf (powerset, with 0)", powerset_monad(nonempty=False), True, 2)
    # Non-empty powerset
    report("P+ (non-empty powerset)", powerset_monad(nonempty=True), True, 1)
    # Distribution (grid denom=2) -- test only
    report("D (distribution, grid d=2)", distribution_monad(2), True, 1)
