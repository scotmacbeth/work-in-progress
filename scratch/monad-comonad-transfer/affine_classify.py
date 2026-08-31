"""
T1 CLASSIFICATION of non-branching (arity<=1) polynomial monads  (PROVE 2026-07-30).

Functor:  M X = E + A x X    (E = nullary shapes, A = unary shapes).
Represent an element of M X as:
    ('e', e)        for e in E        (0 leaves)
    ('a', a, x)     for a in A, x in X (1 leaf, label x)

CLAIM (monad-structure pin).  A monad structure on the functor E + A x (-)
is THE SAME DATA as a monoid structure  (x)  on  N := E |_| A  with
  * unit  e_A in A,
  * every  e in E  a LEFT ZERO  ( e (x) n = e ),  and  N (x) E  subset E
    (i.e. E is a two-sided ideal consisting of left zeros).
The dictionary:
    eta_X(x) = ('a', e_A, x)                        (writer-style unit)
    mu :  outer 'e'  -> absorbs (left zero)         e (x) n = e
          'a' over 'e'  -> a (x) e   in E           (sigma : AxE -> E)
          'a' over 'a'  -> a (x) a'  in E |_| A      (gamma : AxA -> E|_|A)
So mu is read off from (x) with the variable x carried iff the whole spine
multiplies into A.

This script:
  (1) enumerates ALL candidate (e_A, sigma, gamma) for small |E|,|A|;
  (2) checks the MONAD laws (unit-left, unit-right, assoc) on a test set;
  (3) checks the MONOID laws for the induced (x) on N (assoc + two-sided unit);
  (4) confirms predicate (2) <=> predicate (3) on EVERY candidate  ==>  bijection.
"""
from itertools import product as iproduct

# ---- build eta, mu from (E, A, e_A, sigma, gamma) -------------------------
def make_monad(E, A, e_A, sigma, gamma):
    # sigma: dict (a,e)->e' in E ;  gamma: dict (a,a')-> ('e',e) or ('a',a'')
    def obj(X):
        return [('e', e) for e in E] + [('a', a, x) for a in A for x in X]
    def fmap(f):
        def go(m):
            if m[0] == 'e': return m
            return ('a', m[1], f(m[2]))
        return go
    def eta(x):
        return ('a', e_A, x)
    def mu(mm):
        # mm in M(M X):  ('e',e) | ('a', a, z) with z in M X
        if mm[0] == 'e':
            return ('e', mm[1])                 # outer exception: left zero
        a, z = mm[1], mm[2]
        if z[0] == 'e':
            return ('e', sigma[(a, z[1])])      # a (x) e  in E
        # z = ('a', a', x)
        ap, x = z[1], z[2]
        g = gamma[(a, ap)]
        if g[0] == 'e':
            return ('e', g[1])
        return ('a', g[1], x)
    return obj, fmap, eta, mu

# ---- monad laws on a concrete test object X -------------------------------
def monad_laws_hold(E, A, e_A, sigma, gamma, X=('x0', 'x1')):
    obj, fmap, eta, mu = make_monad(E, A, e_A, sigma, gamma)
    MX = obj(X)
    # left unit:  mu . M(eta) = id_{MX}
    Meta = fmap(eta)
    for m in MX:
        if mu(Meta(m)) != m:
            return False
    # right unit:  mu . eta_{MX} = id_{MX}
    for m in MX:
        if mu(eta(m)) != m:
            return False
    # assoc:  mu . M(mu) = mu . mu_{MX}   on M(M(M X))
    MMX = obj(MX)          # M(M X)
    MMMX = obj(MMX)        # M(M(M X))
    Mmu = fmap(mu)
    for mmm in MMMX:
        if mu(Mmu(mmm)) != mu(mu(mmm)):
            return False
    return True

# ---- induced binary op (x) on N = E |_| A, and monoid check --------------
def make_otimes(E, A, e_A, sigma, gamma):
    # N elements tagged: ('e',e) or ('a',a)
    N = [('e', e) for e in E] + [('a', a) for a in A]
    def otimes(n, np):
        if n[0] == 'e':
            return n                         # left zero
        a = n[1]
        if np[0] == 'e':
            return ('e', sigma[(a, np[1])])  # a (x) e
        return gamma[(a, np[1])]             # a (x) a'  (already tagged 'e'/'a')
    return N, otimes

def monoid_laws_hold(E, A, e_A, sigma, gamma):
    N, otimes = make_otimes(E, A, e_A, sigma, gamma)
    u = ('a', e_A)
    # two-sided unit
    for n in N:
        if otimes(u, n) != n or otimes(n, u) != n:
            return False
    # associativity
    for a in N:
        for b in N:
            for c in N:
                if otimes(otimes(a, b), c) != otimes(a, otimes(b, c)):
                    return False
    return True

# ---- enumerate all (e_A, sigma, gamma) for given E, A ---------------------
def enumerate_and_compare(nE, nA, verbose=False):
    E = [f'e{i}' for i in range(nE)]
    A = [f'a{i}' for i in range(nA)]      # a0 will often be the unit but we range e_A over N
    N_labels = [('e', e) for e in E] + [('a', a) for a in A]
    AE = [(a, e) for a in A for e in E]
    AA = [(a, ap) for a in A for ap in A]
    # gamma target = E|_|A tagged
    gamma_targets = [('e', e) for e in E] + [('a', a) for a in A]

    total = 0
    mono = 0
    monad = 0
    mismatch = 0
    # candidate unit ranges over N (elements of A give a real unit; E ones will fail)
    unit_candidates = A[:]   # unit must live in A for the functor form; include only A
    # (an E-unit can't be a two-sided unit unless |N|=1, and eta must be writer-style;
    #  restricting to A is WLOG for the functor E+AxX, matches eta_X(x)=('a',e_A,x))
    for e_A in unit_candidates:
        for sig_vals in iproduct(E, repeat=len(AE)):
            sigma = {AE[i]: sig_vals[i] for i in range(len(AE))}
            for gam_vals in iproduct(gamma_targets, repeat=len(AA)):
                gamma = {AA[i]: gam_vals[i] for i in range(len(AA))}
                total += 1
                md = monad_laws_hold(E, A, e_A, sigma, gamma)
                mo = monoid_laws_hold(E, A, e_A, sigma, gamma)
                mono += mo
                monad += md
                if md != mo:
                    mismatch += 1
                    if verbose and mismatch <= 3:
                        print("  MISMATCH e_A=%s sigma=%s gamma=%s monad=%s monoid=%s"
                              % (e_A, sigma, gamma, md, mo))
    return total, monad, mono, mismatch

if __name__ == "__main__":
    print("=" * 68)
    print("T1: monad-structure(E+AxX)  <=>  monoid(E|_|A, unit in A, E left-zero ideal)")
    print("=" * 68)
    for (nE, nA) in [(0, 1), (1, 1), (0, 2), (1, 2), (2, 1), (2, 2), (3, 2), (1, 3)]:
        total, monad, mono, mismatch = enumerate_and_compare(nE, nA, verbose=True)
        tag = "OK (bijection)" if mismatch == 0 else "!!! MISMATCH !!!"
        print(f"  |E|={nE} |A|={nA}:  candidates={total:6d}  "
              f"#monad-laws={monad:5d}  #monoid-laws={mono:5d}  mismatch={mismatch}   {tag}")
