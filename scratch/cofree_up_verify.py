#!/usr/bin/env python3
"""
Computational verification of the cofree-comonoid universal-property proof
for the induced morphism ghat : D => C(p) of a directed container into the
cofree comonoid on a base container p.

All coordinate conventions follow the task spec EXACTLY:
  - container morphism phi:(A,PA)=>(B,PB): phi1:A->B, phisharp_a:PB(phi1 a)->PA(a)
  - composition (phi;psi)1 = psi1 . phi1 ; (phi;psi)sharp_a = phisharp_a . psisharp_{phi1 a}
  - directed container D=(T,Q) with o,sub,shift and laws D1..D5
  - cofree carrier = trees over p; positions = rooted paths (vertices)

Exit 0 iff all positive checks PASS and all negative controls fire (>0 mismatches).
"""

import sys
import itertools

# ----------------------------------------------------------------------------
# BASE CONTAINER p
# ----------------------------------------------------------------------------
S = ['a', 'b']
P = {'a': [0, 1], 'b': [0]}   # positions are index lists

# ----------------------------------------------------------------------------
# DIRECTED CONTAINER D  (the small category X --f--> Y, plus identities)
# ----------------------------------------------------------------------------
T = ['X', 'Y']
Q = {'X': ['idX', 'f'], 'Y': ['idY']}

def o(tau):
    return {'X': 'idX', 'Y': 'idY'}[tau]

def sub(tau, q):
    tbl = {
        ('X', 'idX'): 'X',
        ('X', 'f'):   'Y',
        ('Y', 'idY'): 'Y',
    }
    return tbl[(tau, q)]

def shift(tau, q, qp):
    # q : out of tau ; qp : out of sub(tau,q) ; result = qp . q  (composition)
    if (tau, q) == ('X', 'idX'):
        return qp                     # idX absorbed
    if (tau, q) == ('X', 'f'):
        # qp must be idY
        assert qp == 'idY', qp
        return 'f'
    if (tau, q) == ('Y', 'idY'):
        return qp
    raise KeyError((tau, q, qp))

# ----------------------------------------------------------------------------
# MORPHISM  g : U(D) => p
# ----------------------------------------------------------------------------
def g1(tau):
    return {'X': 'a', 'Y': 'b'}[tau]

# gsharp_tau : P(g1 tau) -> Q(tau)
_GSHARP = {
    'X': {0: 'idX', 1: 'f'},
    'Y': {0: 'idY'},
}
def gsharp(tau, i):
    return _GSHARP[tau][i]

# ----------------------------------------------------------------------------
# COFREE CARRIER : trees over p, to finite depth d=5
# tree = ('node', s, (child_0, child_1, ...))  or  ('trunc',)
# ----------------------------------------------------------------------------
TRUNC = ('trunc',)
DEPTH = 5     # d
L = 4         # max vertex path length

def is_node(t):
    return t[0] == 'node'

def root(t):
    assert is_node(t)
    return t[1]

def child(t, i):
    if not is_node(t):
        return TRUNC
    return t[2][i]

def tree_eq(t1, t2, depth):
    """Structural equality up to `depth` levels of nodes; truncation matches anything."""
    if depth <= 0:
        return True
    if t1 == TRUNC or t2 == TRUNC:
        return True
    if not (is_node(t1) and is_node(t2)):
        return t1 == t2
    if t1[1] != t2[1]:
        return False
    if len(t1[2]) != len(t2[2]):
        return False
    return all(tree_eq(a, b, depth - 1) for a, b in zip(t1[2], t2[2]))

def enum_vertices(t, maxlen):
    """All rooted paths (tuples) landing on a real node, up to length maxlen."""
    out = []
    def rec(node, path):
        if node == TRUNC:
            return
        out.append(path)
        if len(path) >= maxlen:
            return
        if is_node(node):
            for i in range(len(node[2])):
                rec(node[2][i], path + (i,))
    rec(t, ())
    return out

# cofree structural operations on trees
def o_cofree(t):
    return ()

def sub_cofree(t, v):
    if v == ():
        return t
    i, w = v[0], v[1:]
    if t == TRUNC:
        return TRUNC
    return sub_cofree(child(t, i), w)

def shift_cofree(t, v, wp):
    if v == ():
        return wp
    i, w = v[0], v[1:]
    return (i,) + shift_cofree(child(t, i), w, wp)

# counit eps_p : C(p) => p
def eps1(t):
    return root(t)

def eps_sharp(t, i):
    return (i,)

# ----------------------------------------------------------------------------
# INDUCED MORPHISM  ghat : D => C(p)
# ----------------------------------------------------------------------------
def make_ghat1(shift_fn, corecursion_child='correct'):
    memo = {}
    def ghat1(tau, d):
        key = (tau, d)
        if key in memo:
            return memo[key]
        if d <= 0:
            memo[key] = TRUNC
            return TRUNC
        s = g1(tau)
        kids = []
        for i in P[s]:
            if corecursion_child == 'correct':
                tau_i = sub(tau, gsharp(tau, i))
            else:  # N3 corruption: child i = ghat1(tau) instead of ghat1(tau_i)
                tau_i = tau
            kids.append(ghat1(tau_i, d - 1))
        node = ('node', s, tuple(kids))
        memo[key] = node
        return node
    return ghat1

def make_ghat_sharp(shift_fn):
    def ghat_sharp(tau, v):
        if v == ():
            return o(tau)
        i, w = v[0], v[1:]
        tau_i = sub(tau, gsharp(tau, i))
        return shift_fn(tau, gsharp(tau, i), ghat_sharp(tau_i, w))
    return ghat_sharp

ghat1 = make_ghat1(shift)
ghat_sharp = make_ghat_sharp(shift)

def GHAT1(tau):
    return ghat1(tau, DEPTH)

# ----------------------------------------------------------------------------
# Generic morphism combinators for the box (<|) composition check
# A morphism is an object with .fwd(shape) and .sharp(shape, target_pos)
# ----------------------------------------------------------------------------
class Mor:
    def __init__(self, fwd, sharp):
        self.fwd = fwd
        self.sharp = sharp

def compose(phi, psi):
    # phi ; psi  : (phi;psi)1 = psi1 . phi1 ; sharp_a = phisharp_a . psisharp_{phi1 a}
    def fwd(a):
        return psi.fwd(phi.fwd(a))
    def sharp(a, pos):
        return phi.sharp(a, psi.sharp(phi.fwd(a), pos))
    return Mor(fwd, sharp)

def box(phi, psi):
    # phi <| psi : r<|s => r'<|s'
    # shape of r<|s = (a, k) with k : P_r(a) -> S_s
    def fwd(sh):
        a, k = sh
        a2 = phi.fwd(a)
        def k2(i2):
            return psi.fwd(k(phi.sharp(a, i2)))
        return (a2, k2)
    def sharp(sh, pos):
        a, k = sh
        i2, j2 = pos
        i = phi.sharp(a, i2)
        j = psi.sharp(k(i), j2)
        return (i, j)
    return Mor(fwd, sharp)

# delta_D : D => D<|D    shape (tau, q->sub(tau,q)), pos (q,q') -> shift(tau,q,q')
delta_D = Mor(
    fwd=lambda tau: (tau, (lambda q: sub(tau, q))),
    sharp=lambda tau, pos: shift(tau, pos[0], pos[1]),
)

# delta_cofree : C(p) => C(p)<|C(p)
delta_cofree = Mor(
    fwd=lambda t: (t, (lambda v: sub_cofree(t, v))),
    sharp=lambda t, pos: shift_cofree(t, pos[0], pos[1]),
)

ghat_mor = Mor(fwd=GHAT1, sharp=ghat_sharp)

# ============================================================================
# CHECKS
# ============================================================================
results = []   # (name, ncases, passed_bool)
neg_results = []  # (name, nmismatch)

def record(name, ncases, ok):
    results.append((name, ncases, ok))

# ---- CHECK 1 : D-laws D1..D5 ----------------------------------------------
def check_D_laws(shift_fn):
    n = 0
    mism = 0
    for tau in T:
        # D1
        n += 1
        if sub(tau, o(tau)) != tau:
            mism += 1
        # D2 : shift(tau, o(tau), q) = q  for q in Q(sub(tau,o tau)) = Q(tau)
        for q in Q[sub(tau, o(tau))]:
            n += 1
            if shift_fn(tau, o(tau), q) != q:
                mism += 1
        # D3 : shift(tau, q, o(sub(tau,q))) = q  for q in Q(tau)
        for q in Q[tau]:
            n += 1
            if shift_fn(tau, q, o(sub(tau, q))) != q:
                mism += 1
        # D4 : sub(tau, shift(tau,q,q')) = sub(sub(tau,q), q')
        for q in Q[tau]:
            for qp in Q[sub(tau, q)]:
                n += 1
                if sub(tau, shift_fn(tau, q, qp)) != sub(sub(tau, q), qp):
                    mism += 1
        # D5 : shift(tau, shift(tau,q,q'), q'') = shift(tau, q, shift(sub(tau,q),q',q''))
        for q in Q[tau]:
            for qp in Q[sub(tau, q)]:
                for qpp in Q[sub(sub(tau, q), qp)]:
                    n += 1
                    lhs = shift_fn(tau, shift_fn(tau, q, qp), qpp)
                    rhs = shift_fn(tau, q, shift_fn(sub(tau, q), qp, qpp))
                    if lhs != rhs:
                        mism += 1
    return n, mism

n, m = check_D_laws(shift)
record("1  D-laws D1..D5 (sanity)", n, m == 0)

# ---- CHECK 2 : corecursion equations for ghat1 -----------------------------
def check_corecursion(g1fn):
    n = 0
    mism = 0
    for tau in T:
        t = g1fn(tau, DEPTH)
        # root(ghat1 tau) = g1 tau
        n += 1
        try:
            if root(t) != g1(tau):
                mism += 1
        except Exception:
            mism += 1
        # child(ghat1 tau, i) = ghat1(tau_i)
        for i in P[g1(tau)]:
            n += 1
            try:
                tau_i = sub(tau, gsharp(tau, i))
                if not tree_eq(child(t, i), g1fn(tau_i, DEPTH - 1), DEPTH - 1):
                    mism += 1
            except Exception:
                mism += 1
    return n, mism

n, m = check_corecursion(ghat1)
record("2  corecursion of ghat1", n, m == 0)

# ---- CHECK 3 : triangle (forward + backward) -------------------------------
def check_triangle(eps_sharp_fn):
    n = 0
    mism = 0
    for tau in T:
        t = GHAT1(tau)
        # forward: eps1(ghat1 tau) = g1 tau
        n += 1
        if eps1(t) != g1(tau):
            mism += 1
        # backward: ghat_sharp_tau( eps_sharp_{ghat1 tau}(i) ) = gsharp_tau(i)
        for i in P[g1(tau)]:
            n += 1
            try:
                v = eps_sharp_fn(t, i)
                if ghat_sharp(tau, v) != gsharp(tau, i):
                    mism += 1
            except Exception:
                mism += 1
    return n, mism

n, m = check_triangle(eps_sharp)
record("3  triangle fwd+bwd", n, m == 0)

# ---- CHECK 4 : Lemma U (comult forward) ------------------------------------
def check_lemmaU(g1fn):
    n = 0
    mism = 0
    for tau in T:
        t = g1fn(tau, DEPTH)
        for v in enum_vertices(t, L):
            n += 1
            try:
                lhs = sub_cofree(t, v)
                tau_v = sub(tau, ghat_sharp(tau, v))
                rhs = g1fn(tau_v, DEPTH)
                if not tree_eq(lhs, rhs, DEPTH - len(v)):
                    mism += 1
            except Exception:
                mism += 1
    return n, mism

n, m = check_lemmaU(ghat1)
record("4  Lemma U (comult fwd)", n, m == 0)

# ---- CHECK 5 : Lemma S (comult backward) -----------------------------------
def check_lemmaS(shift_fn, gsharp_fn):
    n = 0
    mism = 0
    for tau in T:
        t = GHAT1(tau)
        for v in enum_vertices(t, L):
            sub_t = sub_cofree(t, v)
            for w in enum_vertices(sub_t, L - len(v)):
                n += 1
                try:
                    lhs = gsharp_fn(tau, shift_cofree(t, v, w))
                    mid = gsharp_fn(tau, v)
                    rhs = shift_fn(tau, mid, gsharp_fn(sub(tau, mid), w))
                    if lhs != rhs:
                        mism += 1
                except Exception:
                    mism += 1
    return n, mism

n, m = check_lemmaS(shift, ghat_sharp)
record("5  Lemma S (comult bwd)", n, m == 0)

# ---- CHECK 6 : comonoid-morphism comult law via <|-formulas ----------------
# LHS = delta_D ; (ghat <| ghat)    RHS = ghat ; delta_cofree   (both D => C<|C)
def check_comonoid_law():
    LHS = compose(delta_D, box(ghat_mor, ghat_mor))
    RHS = compose(ghat_mor, delta_cofree)
    nf = 0; mf = 0   # forward
    nb = 0; mb = 0   # backward
    for tau in T:
        aL, kL = LHS.fwd(tau)
        aR, kR = RHS.fwd(tau)
        # forward: outer tree
        nf += 1
        if not tree_eq(aL, aR, DEPTH):
            mf += 1
        for v in enum_vertices(aL, L):
            # forward: inner tree families
            nf += 1
            if not tree_eq(kL(v), kR(v), DEPTH - len(v)):
                mf += 1
            # backward over positions (v, v')
            inner = kR(v)
            for vp in enum_vertices(inner, L - len(v)):
                nb += 1
                if LHS.sharp(tau, (v, vp)) != RHS.sharp(tau, (v, vp)):
                    mb += 1
    return (nf, mf), (nb, mb)

(fw, mfw), (bw, mbw) = check_comonoid_law()
record("6a comonoid law fwd (trees)", fw, mfw == 0)
record("6b comonoid law bwd (positions)", bw, mbw == 0)

# ---- CHECK 7 : counit compatibility ghat_sharp_tau(()) = o(tau) ------------
def check_counit_compat():
    n = 0; mism = 0
    for tau in T:
        n += 1
        if ghat_sharp(tau, ()) != o(tau):
            mism += 1
    return n, mism

n, m = check_counit_compat()
record("7  counit compat ()->o(tau)", n, m == 0)

# ---- CHECK 8 : UNIQUENESS (backward, determinacy) --------------------------
# Constraints on any h with the same shape map:
#   (c0) hsharp_tau(())          = o(tau)
#   (c1) hsharp_tau((i,))        = gsharp_tau(i)              [triangle backward]
#   (cS) hsharp_tau((i,)+w)      = shift(tau, hsharp_tau((i,)),
#                                        hsharp_{sub(tau,hsharp_tau((i,)))}(w))
#        (the v'=(i,) instance of Lemma S ; shift_cofree(t,(i,),w) = (i,)+w)
# We process vertices in increasing length across all base objects, and at
# each vertex brute-force over ALL candidate values in Q(tau), asserting that
# EXACTLY ONE is consistent with the constraints given the already-forced
# shorter values -- and that it equals ghat_sharp.
def check_uniqueness():
    fixed = {tau: {} for tau in T}
    # collect all (tau, vertex) pairs with len<=L, grouped by length
    all_pairs = []
    for tau in T:
        for v in enum_vertices(GHAT1(tau), L):
            all_pairs.append((tau, v))
    all_pairs.sort(key=lambda p: len(p[1]))

    n = 0
    mism = 0
    for tau, v in all_pairs:
        candidates = []
        for c in Q[tau]:
            ok = True
            if len(v) == 0:
                ok = (c == o(tau))
            elif len(v) == 1:
                i = v[0]
                ok = (c == gsharp(tau, i))
            else:
                i, w = v[0], v[1:]
                base_pos = fixed[tau][(i,)]              # already forced, len 1
                tau_i = sub(tau, base_pos)
                inner = fixed[tau_i][w]                  # already forced, len<len(v)
                required = shift(tau, base_pos, inner)
                ok = (c == required)
            if ok:
                candidates.append(c)
        n += 1
        # uniqueness: exactly one consistent candidate, and it is ghat_sharp
        forced = ghat_sharp(tau, v)
        if len(candidates) != 1 or candidates[0] != forced:
            mism += 1
        fixed[tau][v] = forced
    return n, mism

n, m = check_uniqueness()
record("8  uniqueness (determinacy)", n, m == 0)

# ============================================================================
# NEGATIVE CONTROLS  (must produce >0 mismatches)
# ============================================================================
# N1 : corrupt shift of D -- swap the two output values in one case
def shift_bad(tau, q, qp):
    if (tau, q) == ('X', 'idX'):
        # correct returns qp ; corruption swaps idX <-> f
        return {'idX': 'f', 'f': 'idX'}[qp]
    return shift(tau, q, qp)

# rebuild ghat_sharp with corrupted shift (ghat1 shape map unaffected)
ghat_sharp_bad = make_ghat_sharp(shift_bad)
# Lemma S with corrupted shift + corrupted ghat_sharp
_, mS_n1 = check_lemmaS(shift_bad, ghat_sharp_bad)
# comonoid backward law with corrupted shift : rebuild the morphisms
def check_comonoid_bwd_corrupt():
    delta_D_bad = Mor(
        fwd=lambda tau: (tau, (lambda q: sub(tau, q))),
        sharp=lambda tau, pos: shift_bad(tau, pos[0], pos[1]),
    )
    ghat_mor_bad = Mor(fwd=GHAT1, sharp=ghat_sharp_bad)
    LHS = compose(delta_D_bad, box(ghat_mor_bad, ghat_mor_bad))
    RHS = compose(ghat_mor_bad, delta_cofree)
    mism = 0
    for tau in T:
        aL, kL = LHS.fwd(tau)
        for v in enum_vertices(aL, L):
            inner = kL(v)
            for vp in enum_vertices(inner, L - len(v)):
                try:
                    if LHS.sharp(tau, (v, vp)) != RHS.sharp(tau, (v, vp)):
                        mism += 1
                except Exception:
                    mism += 1
    return mism
m6_n1 = check_comonoid_bwd_corrupt()
neg_results.append(("N1 corrupt shift -> LemmaS mismatches", mS_n1))
neg_results.append(("N1 corrupt shift -> comonoid-bwd mismatches", m6_n1))

# N2 : corrupt eps_sharp -- use () instead of (i,)
def eps_sharp_bad(t, i):
    return ()
_, mtri_n2 = check_triangle(eps_sharp_bad)
neg_results.append(("N2 corrupt eps_sharp -> triangle-bwd mismatches", mtri_n2))

# N3 : corrupt ghat1 corecursion -- child i = ghat1(tau) not ghat1(tau_i)
ghat1_bad = make_ghat1(shift, corecursion_child='corrupt')
_, mcor_n3 = check_corecursion(ghat1_bad)
_, mU_n3 = check_lemmaU(ghat1_bad)
neg_results.append(("N3 corrupt corecursion -> check2 mismatches", mcor_n3))
neg_results.append(("N3 corrupt corecursion -> LemmaU mismatches", mU_n3))

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("=" * 68)
print("COFREE UNIVERSAL PROPERTY : COMPUTATIONAL VERIFICATION")
print("  base p: S={a,b}, P(a)=[0,1], P(b)=[0]")
print("  D: category X--f-->Y ; depth d=%d, vertex length L=%d" % (DEPTH, L))
print("=" * 68)
print("POSITIVE CHECKS")
all_pos_ok = True
for name, nc, ok in results:
    status = "PASS" if ok else "FAIL"
    if not ok:
        all_pos_ok = False
    print("  [%s] %-34s  cases=%-5d" % (status, name, nc))
print("-" * 68)
print("NEGATIVE CONTROLS (mismatches must be > 0)")
all_neg_ok = True
for name, mm in neg_results:
    fired = mm > 0
    if not fired:
        all_neg_ok = False
    status = "FIRED" if fired else "SILENT!"
    print("  [%s] %-46s mismatches=%d" % (status, name, mm))
print("=" * 68)
overall = all_pos_ok and all_neg_ok
print("OVERALL: %s" % ("ALL PASS + ALL CONTROLS FIRED" if overall else "FAILURE"))
print("=" * 68)

sys.exit(0 if overall else 1)
