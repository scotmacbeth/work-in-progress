"""
T2: E2' (associativity of the kappa-compositor) for the WHOLE non-branching class.

Build a genuine affine monad  M = E + A x (-)  from a monoid  N = E |_| A
(E a left-zero ideal), as an entwine.py Monad, then:
  (a) run entwine's reverse-kappa axiom checker (E1',E3',E4',E2') on it;
  (b) run bikleisli's associativity test (the ARROW category axioms) on it;
for several affine monads incl. |E|>=2, |A|>=2, and an ABORTING gamma
(A x A -> E possible) -- the case the Maybe/Writer tests never exercised.
"""
from entwine import (Cont, Mor, compose, eq, G_obj, T_obj, G_mor, T_mor,
                     eps_G, delta_G, eta_T, mu_T, Monad, lambda_rev, check_axioms_rev)
import bikleisli as BK
from itertools import product as iproduct

# ---- affine monad from (E, A, unit u, otimes table) ----------------------
# otimes: dict (n,n') -> n''  on N = tagged E|_|A.  n tagged ('e',e) or ('a',a).
def affine_monad(E, A, u, otimes, name):
    def obj(X):
        return [('e', e) for e in E] + [('a', a, x) for a in A for x in X]
    def fmap(f):
        return lambda m: m if m[0] == 'e' else ('a', m[1], f(m[2]))
    def eta(x):
        return ('a', u, x)
    def mu(mm):
        if mm[0] == 'e':
            return ('e', mm[1])
        a, z = mm[1], mm[2]
        if z[0] == 'e':
            r = otimes[(('a', a), ('e', z[1]))]
            return ('e', r[1])                       # a (x) e  lands in E
        ap, x = z[1], z[2]
        r = otimes[(('a', a), ('a', ap))]
        return ('e', r[1]) if r[0] == 'e' else ('a', r[1], x)
    def leaves(m):
        return [] if m[0] == 'e' else [m[2]]
    return Monad(obj, fmap, eta, mu, leaves, name)

# ---- lax map for kappa : GT => TG on an affine monad ----------------------
# labs has length 0 (nullary shape m in E) or 1 (unary).  t = (w_b)_b, w_b in M(P(lab_b)).
def lax_affine(M, P, labs, t):
    if len(labs) == 0:
        return M.eta(())                              # element of M(1), 1 = {()}
    (w,) = t
    return M.fmap(lambda z: (z,))(w)                  # rewrap single content into 1-tuple

# ---- monoid validity (assoc + two-sided unit + E left-zero ideal) --------
def valid_monoid(E, A, u, otimes):
    N = [('e', e) for e in E] + [('a', a) for a in A]
    U = ('a', u)
    for n in N:
        if otimes[(U, n)] != n or otimes[(n, U)] != n:
            return False, "unit"
    for a in N:
        for b in N:
            for c in N:
                if otimes[(otimes[(a, b)], c)] != otimes[(a, otimes[(b, c)])]:
                    return False, "assoc"
    for e in E:            # left zeros + ideal
        for n in N:
            if otimes[(('e', e), n)] != ('e', e):
                return False, "leftzero"
        for n in N:
            if otimes[(n, ('e', e))][0] != 'e':
                return False, "ideal"
    return True, "ok"

# ---- test containers (with branching-capable shapes for q) ---------------
U1 = Cont(['0'], {'0': ['0']})
A1 = Cont(['a', 'b'], {'a': [0, 1], 'b': [0]})
A3 = Cont(['a', 'b'], {'a': [0, 1], 'b': [0, 1]})

# ---- is mu^M cartesian? (no leaf created/destroyed)  <=> T_M well-defined --
def mu_cartesian(M, Sset=('s0', 's1')):
    """Check: for every mm in M(M Sset), #leaves(mu mm) == sum of inner leaf counts,
    and the inner leaves inject into leaves(mu mm).  Fails exactly when mu MERGES or
    DESTROYS leaves (aborting affine monads)."""
    MS = M.obj(list(Sset))
    MMS = M.obj(MS)
    for mm in MMS:
        outer = M.leaves(mm)                       # labels in MS
        inner_total = sum(len(M.leaves(lb)) for lb in outer)
        m = M.mu(mm)
        if len(M.leaves(m)) != inner_total:
            return False, mm
    return True, None

def run_e2prime(M, containers):
    print(f"\n  M = {M.name}")
    for cn, C in containers.items():
        ax = check_axioms_rev(M, lax_affine, C)
        allok = all(ax.values())
        line = "  ".join(f"{k.split()[0]}={'P' if v else 'FAIL'}" for k, v in ax.items())
        print(f"    {cn:14s}: {line}   {'ALL PASS' if allok else '<<< FAIL'}")

def run_bikleisli_assoc(M, p, q, r, z):
    """arrow category: (h.g).f == h.(g.f) exhaustively; identity laws too."""
    lax = lax_affine
    F  = BK.enum_arrows(M, p, q)
    Gs = BK.enum_arrows(M, q, r)
    H  = BK.enum_arrows(M, r, z)
    idp, idq = BK.bik_id(M, p), BK.bik_id(M, q)
    unit_ok = all(eq(BK.bik_comp(M, lax, f, idq, p, q, q), f) and
                  eq(BK.bik_comp(M, lax, idp, f, p, p, q), f) for f in F)
    viol = 0
    for f in F:
        for g in Gs:
            gf = BK.bik_comp(M, lax, f, g, p, q, r)
            for h in H:
                hg = BK.bik_comp(M, lax, g, h, q, r, z)
                left  = BK.bik_comp(M, lax, gf, h, p, r, z)
                right = BK.bik_comp(M, lax, f, hg, p, q, z)
                if not eq(left, right):
                    viol += 1
    print(f"    arrows p~>q={len(F)} q~>r={len(Gs)} r~>z={len(H)}: "
          f"unit_laws={unit_ok}  assoc_violations={viol}/{len(F)*len(Gs)*len(H)}")

# ================= build several affine monads =============================
def build_examples():
    ex = []

    # (1) M = 2 + 3xX, A = Z/3 (NON-aborting), E = {e0,e1} absorbing-discarding.
    E = ['e0', 'e1']; A = ['u', 'a', 'b']; u = 'u'
    add = {'u': 0, 'a': 1, 'b': 2}; inv = {0: 'u', 1: 'a', 2: 'b'}
    ot = {}
    for x in E + A:
        for y in E + A:
            nx = ('e', x) if x in E else ('a', x)
            ny = ('e', y) if y in E else ('a', y)
            if x in E:
                ot[(nx, ny)] = ('e', x)                       # left zero
            elif y in E:
                ot[(nx, ny)] = ('e', y)                       # a (x) e = e (trivial action)
            else:
                ot[(nx, ny)] = ('a', inv[(add[x] + add[y]) % 3])   # Z/3
    ex.append(("2+3X, A=Z/3 (non-aborting)", E, A, u, ot))

    # (2) M = 1 + 2xX, nilpotent monoid {u,z,0}: z*z=0 in E  (ABORTING gamma).
    #     This is the multiplicative monoid {1, z, 0} with z^2 = 0.
    E = ['0']; A = ['u', 'z']; u = 'u'
    ot = {}
    def tag(w): return ('e', w) if w in E else ('a', w)
    table = {}
    for y in E + A: table[('u', y)] = y
    for x in E + A: table[(x, 'u')] = x
    table[('0', '0')] = '0'; table[('0', 'z')] = '0'; table[('z', '0')] = '0'
    table[('z', 'z')] = '0'                        # ABORT: z (x) z = 0 in E
    for x in E + A:
        for y in E + A:
            ot[(tag(x), tag(y))] = tag(table[(x, y)])
    ex.append(("1+2X nilpotent, z*z=0 (ABORTING)", E, A, u, ot))

    # (3) M = 1 + 2xX, A = Z/2 x ... actually A={u,a} Z/2, E={e0}, a(x)e=e.
    E = ['e0']; A = ['u', 'a']; u = 'u'
    ot = {}
    def tag2(w): return ('e', w) if w in E else ('a', w)
    tb = {}
    for y in E + A: tb[('u', y)] = y
    for x in E + A: tb[(x, 'u')] = x
    for e in E:
        for y in E + A: tb[(e, y)] = e
    tb[('a', 'e0')] = 'e0'; tb[('a', 'a')] = 'u'          # Z/2
    for x in E + A:
        for y in E + A:
            ot[(tag2(x), tag2(y))] = tag2(tb[(x, y)])
    ex.append(("1+2X, A=Z/2 (exception+writer)", E, A, u, ot))

    # (4) auto-search a VALID aborting monoid with |E|=2, |A|=2 (gamma hits E).
    E = ['e0', 'e1']; A = ['u', 'z']; u = 'u'
    Ntag = [('e', e) for e in E] + [('a', a) for a in A]
    found = None
    for sig in iproduct(E, repeat=2):                     # sigma(z,e0), sigma(z,e1) in E
        for gam in iproduct(['e0', 'e1', 'u', 'z'], repeat=1):   # gamma(z,z) in E|_|A
            gzz = gam[0]
            ot = {}
            # unit + left-zero skeleton
            for n in Ntag:
                ot[(('a', 'u'), n)] = n
                ot[(n, ('a', 'u'))] = n
            for e in E:
                for n in Ntag: ot[(('e', e), n)] = ('e', e)
            ot[(('a', 'z'), ('e', 'e0'))] = ('e', sig[0])
            ot[(('a', 'z'), ('e', 'e1'))] = ('e', sig[1])
            ot[(('a', 'z'), ('a', 'z'))] = ('e', gzz) if gzz in E else ('a', gzz)
            ok, _ = valid_monoid(E, A, u, ot)
            aborts = ot[(('a', 'z'), ('a', 'z'))][0] == 'e'
            if ok and aborts:
                found = ot; break
        if found: break
    if found:
        ex.append(("2+2X auto-found ABORTING (|E|=2)", E, A, u, found))
    return ex

if __name__ == "__main__":
    print("=" * 70)
    print("T2: E2' for the kappa-compositor on the WHOLE non-branching class")
    print("=" * 70)
    conts = {'U1': U1, 'A1({a:2,b:1})': A1, 'A3({a:2,b:2})': A3}
    for (name, E, A, u, ot) in build_examples():
        ok, why = valid_monoid(E, A, u, ot)
        print(f"\n### {name}   [monoid valid: {ok} ({why})]")
        assert ok, ("built an invalid monoid!", name, why)
        M = affine_monad(E, A, u, ot, name)
        cart, wit = mu_cartesian(M)
        print(f"  mu^M cartesian (T_M well-defined): {cart}"
              + ("" if cart else f"   [leaf destroyed at {wit}]"))
        if not cart:
            print("    -> ABORTING monad: outside the polynomial class; T_M's mu"
                  " has no canonical backward map. E2'/arrow story N/A.")
            continue
        run_e2prime(M, conts)
        print("  -- arrow-category associativity (biKleisli, tiny objects) --")
        run_bikleisli_assoc(M, U1, U1, U1, U1)
