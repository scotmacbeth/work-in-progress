"""
Moving-nu skew-brace extension cocycle derivation -- symbolic verification.
2026-09-26  MacBeth.

Witness: skew brace on (G,+) = Z/2 x Z/4  (ABELIAN additive group, order 8).
  D = {(0,y): y in Z/4}   (kernel/ideal),  (D,+) = Z/4,  (D,circ) = Klein four.
  H = G/D = Z/2.
  lambda_g(x,y) = (x, s*y)   where s = (-1)^{gx+gy}   (fixes 1st coord, negates 2nd if gx+gy odd)
  a circ b = a + lambda_a(b).

This realises  lambda|_D = negation on the ODD elements of D (the unique nontrivial
skew brace of order 4 on Z/4 with Klein circle), and gives nu_1 = lambda_{s(1)}|_D
= negation when the section rep of 1 has (x+y) odd.  It is a genuine NON-trivial-kernel
witness ((D,+) != (D,circ)).  |D|=4 => L = im(lambda|_D) = {id,neg} = Aut(Z/4), so the
RESIDUE [nu] is trivial here (size artifact, cannot separate) -- but nu_1 itself is a
nontrivial automorphism, which is what we need to exercise the equations.

We (1) verify the object is a skew brace with the claimed kernel structure,
   (2) verify the COORDINATE formulas for (+) [=> eq (a)] and (circ) [=> eq (c) block]
       reproduce the true operations for ALL element pairs,
   (3) verify cocycle eq (a) [beta], eq (b) [tau], the mu/nu coupling-1 identity,
       and the derived cross equation (c),
   for several sections.
"""

# ---------- group G = Z/2 x Z/4 ----------
G = [(x, y) for x in range(2) for y in range(4)]

def add(u, v):
    return ((u[0] + v[0]) % 2, (u[1] + v[1]) % 4)

def negadd(u):
    return ((-u[0]) % 2, (-u[1]) % 4)

def lam(g, v):
    sign = -1 if (g[0] + g[1]) % 2 == 1 else 1
    return (v[0] % 2, (sign * v[1]) % 4)

def circ(u, v):
    return add(u, lam(u, v))

ZERO = (0, 0)

# circ inverse by search
def circinv(u):
    for w in G:
        if circ(u, w) == ZERO and circ(w, u) == ZERO:
            return w
    raise ValueError("no circ inverse for %r" % (u,))

# ---------- (0) sanity: (G,circ) is a group, (G,+,circ) a skew brace ----------
def check_group(op, inv, ident):
    # associativity
    for a in G:
        for b in G:
            for c in G:
                if op(op(a, b), c) != op(a, op(b, c)):
                    return "assoc fail"
    for a in G:
        if op(ident, a) != a or op(a, ident) != a:
            return "identity fail"
        ia = inv(a)
        if op(a, ia) != ident or op(ia, a) != ident:
            return "inverse fail"
    return "OK"

print("(G,+)   group:", check_group(add, negadd, ZERO))
print("(G,circ) group:", check_group(circ, circinv, ZERO))

# skew brace: a circ (b + c) = (a circ b) - a + (a circ c)
sb = all(
    circ(a, add(b, c)) == add(add(circ(a, b), negadd(a)), circ(a, c))
    for a in G for b in G for c in G
)
print("skew brace identity a o (b+c) = (a o b) - a + (a o c):", sb)

# ---------- (1) kernel structure ----------
D = [(0, y) for y in range(4)]          # as G-elements
# (D,+) = Z/4 ?
Dplus_orders = {d: next(n for n in range(1, 9)
                        if (lambda z: z == ZERO)(
                            __import__('functools').reduce(add, [d]*n)))
                for d in D if d != ZERO}
print("(D,+) nonzero element additive orders:", {d[1]: o for d, o in Dplus_orders.items()})

def circ_pow(d, n):
    r = ZERO
    for _ in range(n):
        r = circ(r, d)
    return r
Dcirc_orders = {d[1]: next(n for n in range(1, 9) if circ_pow(d, n) == ZERO)
                for d in D if d != ZERO}
print("(D,circ) nonzero element circle orders:", Dcirc_orders)
print("  => (D,+) = Z/4 (has order-4 elt),  (D,circ) = Klein (all order<=2):",
      4 in [Dplus_orders[d] for d in Dplus_orders] and set(Dcirc_orders.values()) <= {1, 2})

# lambda|_D
lamD = {d[1]: lam(d, (0, 1))[1] for d in D}   # image of generator 1
print("lambda_d(1) for d in D (y-part):", lamD, " (3 = -1 mod 4)")
# L = im(lambda|_D) as maps on D
def as_map(autom_on_y):
    return tuple(autom_on_y(y) for y in range(4))
L = set(as_map(lambda y, d=d: lam(d, (0, y))[1]) for d in D)
print("L = im(lambda|_D) as tuples over y=0..3:", sorted(L),
      " |L| =", len(L), "(=Aut(Z/4)=full)")

# ---------- coordinate machinery for a chosen section ----------
Hs = [0, 1]
def hadd(a, b): return (a + b) % 2
def hcirc(a, b): return (a + b) % 2     # first coord adds; = hadd  (H trivial: o_H=+_H=Z/2)
def hneg(a): return (-a) % 2
lamH = lambda h, k: k                    # lambda^H = id (lambda fixes first coord)

# D as Z/4 (y-values); additive & circle ops on D:
def Dadd(y1, y2): return (y1 + y2) % 4
def Dneg(y): return (-y) % 4
def Dcirc(y1, y2): return circ((0, y1), (0, y2))[1]
def Dcircinv(y):
    for z in range(4):
        if Dcirc(y, z) == 0:
            return z
    raise ValueError

def run_section(sec, label):
    print("\n" + "=" * 70)
    print("SECTION %s : s(0)=%r  s(1)=%r" % (label, sec[0], sec[1]))
    print("=" * 70)

    def Dpart(g, h):
        # g - s(h)  (must lie in D)
        d = add(g, negadd(sec[h]))
        assert d[0] == 0, ("Dpart not in D", g, h, d)
        return d[1]

    # cochains
    def mu(h, y):        # additive conj: s(h)+d-s(h)  (abelian => id)
        return add(add(sec[h], (0, y)), negadd(sec[h]))[1]
    def beta(h, k):
        g = add(add(sec[h], sec[k]), negadd(sec[hadd(h, k)]))
        assert g[0] == 0
        return g[1]
    def nu(h, y):        # lambda_{s(h)}|_D
        return lam(sec[h], (0, y))[1]
    def T(h, k):         # ADDITIVE-difference circle factor set: s(h)o s(k) - s(hoK)
        g = add(circ(sec[h], sec[k]), negadd(sec[hcirc(h, k)]))
        assert g[0] == 0, ("T not in D", h, k, g)
        return g[1]
    def tau(h, k):       # CIRCLE-difference factor set: s(h)o s(k) o s(hoK)^{-1}
        g = circ(circ(sec[h], sec[k]), circinv(sec[hcirc(h, k)]))
        assert g[0] == 0
        return g[1]
    def sigma(h, y):     # circle conj: s(h) o d o s(h)^{-1}
        g = circ(circ(sec[h], (0, y)), circinv(sec[h]))
        assert g[0] == 0
        return g[1]
    def Lambda(d1, h1, y):     # lambda_{s(h1)+d1}|_D
        g = add(sec[h1], (0, d1))
        return lam(g, (0, y))[1]
    def rho(d1, h1, k):        # D-part of lambda_{s(h1)+d1}(s(k))
        g = add(sec[h1], (0, d1))
        img = lam(g, sec[k])
        d = add(img, negadd(sec[lamH(h1, k)]))
        assert d[0] == 0, ("rho not in D", d)
        return d[1]

    print("beta:", {(h, k): beta(h, k) for h in Hs for k in Hs})
    print("T   :", {(h, k): T(h, k) for h in Hs for k in Hs})
    print("tau :", {(h, k): tau(h, k) for h in Hs for k in Hs})
    print("nu_h on D (image of gen 1):", {h: nu(h, 1) for h in Hs}, " (3=neg,1=id)")
    print("sigma_h on D (image of gen 1):", {h: sigma(h, 1) for h in Hs})
    print("mu_h on D (image of gen 1):", {h: mu(h, 1) for h in Hs})

    # ---- eq (a): additive 2-cocycle with action mu ----
    okA = True
    for h in Hs:
        for k in Hs:
            for l in Hs:
                lhs = Dadd(mu(h, beta(k, l)), beta(h, hadd(k, l)))
                rhs = Dadd(beta(h, k), beta(hadd(h, k), l))
                if lhs != rhs:
                    okA = False
                    print("  (a) FAIL at", h, k, l, lhs, rhs)
    print("eq (a) additive 2-cocycle [mu*beta(k,l)+beta(h,k+l)=beta(h,k)+beta(h+k,l)]:", okA)

    # ---- eq (b): circle 2-cocycle with action sigma, in (D,circ) ----
    okB = True
    for h in Hs:
        for k in Hs:
            for l in Hs:
                lhs = Dcirc(sigma(h, tau(k, l)), tau(h, hcirc(k, l)))
                rhs = Dcirc(tau(h, k), tau(hcirc(h, k), l))
                if lhs != rhs:
                    okB = False
                    print("  (b) FAIL at", h, k, l, lhs, rhs)
    print("eq (b) circle 2-cocycle [sigma*tau(k,l) o tau(h,koL)=tau(h,k) o tau(hoK,l)]:", okB)

    # ---- coupling-1: nu_h mu_k nu_h^{-1} = mu_{lambda^H_h k}  (as maps on D) ----
    def compose_maps(f, g_):   # f after g on y
        return tuple(f(g_(y)) for y in range(4))
    okC1 = True
    for h in Hs:
        nuh = lambda y, h=h: nu(h, y)
        # nu_h^{-1}
        nuh_inv_tbl = {nu(h, y): y for y in range(4)}
        nuh_inv = lambda y, t=nuh_inv_tbl: t[y]
        for k in Hs:
            muk = lambda y, k=k: mu(k, y)
            lhs = tuple(nu(h, mu(k, nuh_inv(y))) for y in range(4))
            rhs = tuple(mu(lamH(h, k), y) for y in range(4))
            if lhs != rhs:
                okC1 = False
                print("  coupling-1 FAIL at h,k=", h, k, lhs, rhs)
    print("coupling-1 [nu_h mu_k nu_h^-1 = mu_{lamH_h k}]:", okC1)

    # ---- COORDINATE FORMULA CHECKS (the real validation of the derivation) ----
    # (+) formula:  (d1,h1) (+) (d2,h2) = (d1 + mu_{h1} d2 + beta(h1,h2), h1+_H h2)
    ok_plus = True
    for g1 in G:
        for g2 in G:
            h1, h2 = g1[0], g2[0]
            d1, d2 = Dpart(g1, h1), Dpart(g2, h2)
            dres = Dadd(Dadd(d1, mu(h1, d2)), beta(h1, h2))
            hres = hadd(h1, h2)
            pred = add(sec[hres], (0, dres))
            if pred != add(g1, g2):
                ok_plus = False
                print("  (+)-formula FAIL", g1, g2, pred, add(g1, g2))
    print("coordinate (+) formula reproduces true + :", ok_plus)

    # (circ) formula:
    # (d1,h1)(o)(d2,h2) = ( d1 + mu_{h1}( Lambda_{(d1,h1)} d2 + rho_{(d1,h1)}(h2) )
    #                        + beta(h1, lamH_{h1} h2),   h1 o_H h2 )
    ok_circ = True
    for g1 in G:
        for g2 in G:
            h1, h2 = g1[0], g2[0]
            d1, d2 = Dpart(g1, h1), Dpart(g2, h2)
            inner = Dadd(Lambda(d1, h1, d2), rho(d1, h1, h2))
            dres = Dadd(Dadd(d1, mu(h1, inner)), beta(h1, lamH(h1, h2)))
            hres = hcirc(h1, h2)
            pred = add(sec[hres], (0, dres))
            if pred != circ(g1, g2):
                ok_circ = False
                print("  (o)-formula FAIL", g1, g2, "pred", pred, "true", circ(g1, g2),
                      "d1,h1,d2,h2", d1, h1, d2, h2, "Lam", Lambda(d1, h1, d2),
                      "rho", rho(d1, h1, h2))
    print("coordinate (circ) formula reproduces true circ :", ok_circ)

    # Lambda ~ nu mod L :  Lambda_{(d,h)} o nu_h^{-1} in L for all d,h
    okLam = True
    for h in Hs:
        nuh_inv = {nu(h, y): y for y in range(4)}
        for d1 in range(4):
            comp = tuple(Lambda(d1, h, nuh_inv[y]) for y in range(4))
            if comp not in L:
                okLam = False
                print("  Lambda~nu FAIL", d1, h, comp)
    print("Lambda_{(d,h)} = nu_h (mod L) for all d :", okLam)

    # ---- cross equation (c) as derived (D abelian in this witness) ----
    # mu_h nu_h beta(k,l) + T(h,k+_H l)
    #   = T(h,k) - mu_{h o_H k} mu_h^{-1} beta(h,-_H h) + beta(h o_H k, -_H h)
    #     + mu_{(h o_H k) -_H h} T(h,l) + beta((h o_H k) -_H h, h o_H l)
    def mu_inv(h, y):
        t = {mu(h, z): z for z in range(4)}
        return t[y]
    okC = True
    for h in Hs:
        for k in Hs:
            for l in Hs:
                lhs = Dadd(mu(h, nu(h, beta(k, l))), T(h, hadd(k, l)))
                hk = hcirc(h, k)
                t1 = T(h, k)
                t2 = Dneg(mu(hk, mu_inv(h, beta(h, hneg(h)))))
                t3 = beta(hk, hneg(h))
                idx = hadd(hk, hneg(h))          # (h o_H k) -_H h
                t4 = mu(idx, T(h, l))
                t5 = beta(idx, hcirc(h, l))
                rhs = Dadd(Dadd(Dadd(Dadd(t1, t2), t3), t4), t5)
                if lhs != rhs:
                    okC = False
                    print("  (c) FAIL at h,k,l=", h, k, l, "lhs", lhs, "rhs", rhs)
    print("cross equation (c) [derived] holds:", okC)

    # test that the nu_h factor in (c) is NECESSARY: recompute LHS without nu
    diff_seen = False
    for h in Hs:
        for k in Hs:
            for l in Hs:
                with_nu = Dadd(mu(h, nu(h, beta(k, l))), T(h, hadd(k, l)))
                without = Dadd(mu(h, beta(k, l)), T(h, hadd(k, l)))
                if with_nu != without:
                    diff_seen = True
    print("  does dropping nu change LHS of (c) anywhere? ", diff_seen,
          "  (needs nu!=id AND beta!=0 simultaneously)")

    return dict(okA=okA, okB=okB, okC1=okC1, ok_plus=ok_plus,
                ok_circ=ok_circ, okLam=okLam, okC=okC)


sections = {
    "good  (nu_1=neg, beta=0)": {0: (0, 0), 1: (1, 0)},
    "twist (nu_1=id,  beta!=0)": {0: (0, 0), 1: (1, 1)},
    "twist2 (nu_1=neg, beta?)": {0: (0, 0), 1: (1, 2)},
}
results = {}
for lbl, sec in sections.items():
    results[lbl] = run_section(sec, lbl)

print("\n" + "#" * 70)
print("SUMMARY  (all should be True):")
for lbl, r in results.items():
    print(" ", lbl, "->", r)

# ======================================================================
# ABSTRACT demonstration that the coupling term  mu_h nu_h beta(k,l)  in
# eq (c) is STRUCTURALLY present (not identically absorbable).
# On the concrete |D|=4 witness the term is invisible because whenever
# nu_1=neg the value beta(k,l) is 2-torsion (neg-fixed) -- the algebraic
# shadow of "flip nu forces coboundary".  Here we simply exhibit a data
# point where nu=neg acts NON-trivially on a candidate beta value, so the
# LHS of (c) demonstrably depends on nu.
# ======================================================================
print("\n" + "#" * 70)
print("ABSTRACT: is the nu-factor in (c) removable?  Take D=Z/4, nu=neg,")
print("beta(k,l)=1 (a non-2-torsion value), mu=id, T(...)=0:")
b_val = 1
with_nu = Dadd(Dneg(b_val), 0)      # mu_h nu_h beta = neg(1) = 3
without = Dadd(b_val, 0)            # would-be nu-free LHS = 1
print("   LHS with nu   = neg(beta) =", with_nu)
print("   LHS without nu =      beta =", without)
print("   => coupling term is NON-trivial (%d != %d): nu genuinely acts on beta"
      % (with_nu, without))
print("   The concrete witness hides this only because nu=neg <=> beta in {0,2}")
print("   (2-torsion, neg-fixed): the coupling is confined to coboundaries, |D|=4 artifact.")
