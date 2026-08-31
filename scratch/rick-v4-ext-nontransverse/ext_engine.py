r"""
Non-transverse Ext tower engine for G = V4 = Z/2 x Z/2 over k = F2.

Computes  Ext^n_{kG}(k[G/A], k[G/B])  for n = 0..6, as F2-dimensions, via a
minimal free resolution of k[G/A] over kG, then Hom_{kG}(-, k[G/B]), then
cohomology (dim ker - dim im) in each degree, ALL over F2.

Reuses the verified V4 homological-algebra machinery from
  /home/agent/projects/scratch/rick-v4-ext2/  (f2lib.py, modules.py)
which was validated on H*(V4;F2) = [1,2,3,4,5,6,7] and the transverse case.

Cross-checked against the Mackey/Shapiro formula
  Ext^n_{kG}(k[G/A], k[G/B]) = (+)_{g in A\G/B}  H^n(A ^ gBg^{-1}; k),
and (since G is abelian, gBg^{-1}=B) against the closed form
  #(A\G/B) copies of  H^n(A^B; k).

Also computes the RANK VARIETY of each k[G/A] (support/Quillen question, Q2).

Run:  python3 ext_engine.py
"""
import sys, os
import numpy as np

# --- reuse the verified rick-v4-ext2 engine ---
sys.path.insert(0, "/home/agent/projects/scratch/rick-v4-ext2")
from f2lib import mod2, rank, EXP, IDX, gmul          # noqa: E402
from modules import module_from_ab, ext_tower         # noqa: E402

DEG = 6   # compute Ext^0..Ext^6

# ------------------------------------------------------------------
# group-theoretic bookkeeping for V4 (elements: 0=e,1=a,2=b,3=ab)
# ------------------------------------------------------------------
SUBGROUPS = {
    "e":   [0],            # trivial subgroup {e}
    "<a>": [0, 1],
    "<b>": [0, 2],
    "<ab>":[0, 3],
    "G":   [0, 1, 2, 3],
}

def intersect(H, K):
    s = set(H) & set(K)
    return sorted(s)

def double_cosets(A, B):
    """List of double cosets A g B in G=V4 (as frozensets of element indices)."""
    seen = set()
    cosets = []
    for g in range(4):
        dc = frozenset(gmul(gmul(a, g), b) for a in A for b in B)
        if dc not in seen:
            seen.add(dc)
            cosets.append(dc)
    return cosets

def order(H):
    return len(H)

# ------------------------------------------------------------------
# permutation module k[G/H] as an F2[V4]-module (action of a and b)
# ------------------------------------------------------------------
def perm_module(H):
    """Build k[G/H]: basis = left cosets gH; group elt acts by left mult.
    Returns module dict via module_from_ab (needs action of a and b)."""
    # left cosets
    cosets = []
    seen = set()
    for g in range(4):
        c = frozenset(gmul(g, h) for h in H)
        if c not in seen:
            seen.add(c); cosets.append(c)
    d = len(cosets)
    cidx = {}
    for pos, c in enumerate(cosets):
        for x in c:
            cidx[x] = pos
    def act_of(gen):
        M = np.zeros((d, d), dtype=np.uint8)
        for pos, c in enumerate(cosets):
            rep = min(c)
            img = gmul(gen, rep)
            M[cidx[img], pos] = 1
        return M
    if d == 1:
        # trivial module k[G/G]
        one = np.array([[1]], dtype=np.uint8)
        return {'d': 1, 'act': [one, one, one, one]}
    return module_from_ab(mat_a=act_of(1), mat_b=act_of(2))

# ------------------------------------------------------------------
# Mackey/Shapiro closed-form prediction
# ------------------------------------------------------------------
def Hn_cyclic2(deg):
    """H^n(Z/2; F2) = F2 for all n>=0  -> dims [1,1,...,1]."""
    return [1] * (deg + 1)

def Hn_trivialgrp(deg):
    """H^n({e}; F2) = F2 for n=0, 0 else."""
    return [1] + [0] * deg

def Hn_V4(deg):
    """H^n(V4; F2): Poincare series 1/(1-t)^2 -> dim = n+1."""
    return [n + 1 for n in range(deg + 1)]

def group_cohomology_dims(H, deg):
    """H^n(H; F2) dims for H one of our V4 subgroups (abelian)."""
    o = order(H)
    if o == 1:
        return Hn_trivialgrp(deg)
    if o == 2:
        return Hn_cyclic2(deg)
    if o == 4:
        return Hn_V4(deg)
    raise ValueError

def mackey_prediction(A, B, deg):
    r"""(+)_{g in A\G/B} H^n(A ^ gBg^{-1}; k). G abelian => gBg^{-1}=B.
    Returns (tower, ncosets, AcapB)."""
    cosets = double_cosets(A, B)
    ncos = len(cosets)
    AcapB = intersect(A, B)          # A ^ B (=A^gBg^{-1} for all g, G abelian)
    base = group_cohomology_dims(AcapB, deg)
    tower = [ncos * base[n] for n in range(deg + 1)]
    # sanity: #cosets = |G||A^B|/(|A||B|)
    formula = (4 * order(AcapB)) // (order(A) * order(B))
    assert ncos == formula, (ncos, formula)
    return tower, ncos, AcapB

# ------------------------------------------------------------------
# rank variety of an F2[V4]-module  (Q2)
# ------------------------------------------------------------------
def action_of_algebra_elt(mod, coeffs_in_e_a_b_ab):
    """action matrix of sum coeffs[i]*basis_i on module."""
    d = mod['d']
    M = np.zeros((d, d), dtype=np.uint8)
    for i in range(4):
        if coeffs_in_e_a_b_ab[i]:
            M = (M + mod['act'][i]) & 1
    return M

def u_action(mod, alpha, beta):
    """action of u = alpha*x + beta*y  where x=a-1=a+e, y=b-1=b+e (char 2).
    In the (e,a,b,ab) basis: x = e+a -> coeffs[0]^=1,[1]^=1 ; y = e+b."""
    # coeffs for x and y as elements of kG
    x = [1, 1, 0, 0]   # e + a
    y = [1, 0, 1, 0]   # e + b
    coeffs = [(alpha * x[i] + beta * y[i]) & 1 for i in range(4)]
    return action_of_algebra_elt(mod, coeffs)

def rank_variety_F2points(mod):
    """For the three F2-rational projective points (1:0),(0:1),(1:1) of P^1,
    decide whether u=alpha*x+beta*y acts FREELY on mod (=> point NOT in V_r)
    or non-freely (=> point IN V_r).
    M free over F2[u]/(u^2) <=> rank(u-action) = d/2.
    Returns dict point-> (rank, is_free, in_variety)."""
    d = mod['d']
    res = {}
    for (alpha, beta) in [(1, 0), (0, 1), (1, 1)]:
        U = u_action(mod, alpha, beta)
        r = rank(U)
        # U^2 must be 0 (u^2=0 in kV4)
        assert not (U @ U % 2).any(), "u^2 != 0 !?"
        is_free = (d % 2 == 0) and (r == d // 2)
        res[(alpha, beta)] = dict(rank=int(r), is_free=bool(is_free),
                                  in_variety=not is_free)
    return res

# ------------------------------------------------------------------
# the five cases
# ------------------------------------------------------------------
CASES = [
    ("(i)   A=B=<a>",            "<a>", "<a>"),
    ("(ii)  A=<a>, B=G",         "<a>", "G"),
    ("(iii) A=G,   B=<a>",       "G",   "<a>"),
    ("(iv)  A=<a>, B=<b> [transverse control]", "<a>", "<b>"),
    ("(v)   A=B=G  (= H^*(V4))", "G",   "G"),
]

def run():
    print("=" * 70)
    print("Ext^n_{kV4}(k[G/A], k[G/B]),  n=0..%d,  char 2" % DEG)
    print("=" * 70)
    all_ok = True
    summary = []
    for label, Aname, Bname in CASES:
        A, B = SUBGROUPS[Aname], SUBGROUPS[Bname]
        MA = perm_module(A)     # k[G/A]  (the module being resolved)
        NB = perm_module(B)     # k[G/B]  (the Hom target)
        ext, betti = ext_tower(MA, NB, DEG)
        mack, ncos, AcapB = mackey_prediction(A, B, DEG)
        ok = (ext == mack)
        all_ok = all_ok and ok
        print("\n" + label)
        print("  dim k[G/A]=%d, dim k[G/B]=%d;  A^B=%s (order %d);  #(A\\G/B)=%d"
              % (MA['d'], NB['d'],
                 "{" + ",".join("e a b ab".split()[i] for i in AcapB) + "}",
                 order(AcapB), ncos))
        print("  Ext (resolution) : %s" % ext)
        print("  Ext (Mackey pred): %s" % mack)
        print("  betti(k[G/A])    : %s" % betti)
        print("  AGREE            : %s" % ok)
        summary.append((label, ext, mack, ok))
    print("\n" + "=" * 70)
    print("ALL CASES AGREE (resolution == Mackey): %s" % all_ok)
    print("=" * 70)

    # ---------------- rank varieties (Q2) ----------------
    print("\n" + "=" * 70)
    print("RANK VARIETIES  V_r(k[G/A])  in P^1  (Q2)")
    print("  x=a-1 (a-direction), y=b-1 (b-direction); point (alpha:beta)")
    print("=" * 70)
    for Hname in ["<a>", "<b>", "G", "e"]:
        M = perm_module(SUBGROUPS[Hname])
        rv = rank_variety_F2points(M)
        invar = [pt for pt, info in rv.items() if info['in_variety']]
        print("\n  k[G/%s]  (dim %d):" % (Hname, M['d']))
        for pt in [(1, 0), (0, 1), (1, 1)]:
            info = rv[pt]
            tag = "IN V_r" if info['in_variety'] else "free (not in V_r)"
            print("    u=%d*x+%d*y : rank=%d  %s" % (pt[0], pt[1], info['rank'], tag))
        print("    -> V_r among F2-points: %s"
              % (["(%d:%d)" % p for p in invar] or "empty (M projective)"))

    # ---------------- parametric (all-of-P^1) confirmation ----------------
    # x = a-1, y = b-1.  On k[G/<a>]: a acts trivially so x acts as the ZERO
    # matrix; u = alpha*x + beta*y = beta*(b-1).  rank(u) = rank(b-1)*[beta!=0].
    # Hence over ANY field, u acts freely (rank 1) iff beta != 0, and
    # non-freely iff beta = 0.  => V_r(k[G/<a>]) = {(alpha:beta): beta=0}
    #                                            = the single point (1:0).
    print("\n  PARAMETRIC confirmation (valid over all of P^1, any field):")
    Ma = perm_module(SUBGROUPS["<a>"])
    x_act = action_of_algebra_elt(Ma, [1, 1, 0, 0])   # a-1
    y_act = action_of_algebra_elt(Ma, [1, 0, 1, 0])   # b-1
    print("    k[G/<a>]: (a-1) acts as ZERO matrix? %s ;  rank(b-1)=%d"
          % (not x_act.any(), rank(y_act)))
    print("    => u=alpha x+beta y acts as beta*(b-1); non-free iff beta=0")
    print("    => V_r(k[G/<a>]) = single point (1:0)  [proper subvariety of P^1]")
    return all_ok, summary

if __name__ == "__main__":
    run()
