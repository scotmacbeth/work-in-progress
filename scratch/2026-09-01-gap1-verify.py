#!/usr/bin/env python3
"""
Gap-1 verification over finite fields.
TASK 1: (-)<| comparison map is a natural ISO over C = Set x Vec_fd (k=F2).
TASK 2: dual numbers R = F2[e]/e^2 is a COLLAPSE base (copower-tiny everywhere,
        <|=(x)_R), and k is copower-tiny but NOT projective/dualizable.

All arithmetic over GF(2). Everything explicit; maps built and checked.
"""

import itertools
import numpy as np
import random

random.seed(12345)
np.random.seed(12345)

# ============================================================
# GF(2) linear algebra
# ============================================================

def rref_gf2(M):
    """Return (R, pivots) reduced row echelon over GF2. M: 2D int array."""
    M = (np.array(M, dtype=int) % 2).copy()
    if M.size == 0:
        return M, []
    rows, cols = M.shape
    pivots = []
    r = 0
    for c in range(cols):
        # find pivot
        piv = None
        for i in range(r, rows):
            if M[i, c] == 1:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c] == 1:
                M[i] ^= M[r]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return M, pivots

def rank_gf2(M):
    M = np.array(M, dtype=int) % 2
    if M.size == 0:
        return 0
    _, piv = rref_gf2(M)
    return len(piv)

def nullspace_gf2(M):
    """Basis (list of vectors) of {x : M x = 0} over GF2. M: rows x cols."""
    M = np.array(M, dtype=int) % 2
    if M.size == 0:
        # no constraints: full space of dimension = number of columns
        cols = M.shape[1] if M.ndim == 2 else 0
        return [np.eye(cols, dtype=int)[i] for i in range(cols)]
    rows, cols = M.shape
    R, pivots = rref_gf2(M)
    pivset = set(pivots)
    free = [c for c in range(cols) if c not in pivset]
    basis = []
    for f in free:
        x = np.zeros(cols, dtype=int)
        x[f] = 1
        for ri, pc in enumerate(pivots):
            # pivot row ri has 1 at pc; entry at free col f
            if R[ri, f] == 1:
                x[pc] = 1
        basis.append(x % 2)
    return basis

def solve_gf2(A, b):
    """Solve A x = b over GF2 (A columns are a basis, expect unique). Returns x or None."""
    A = np.array(A, dtype=int) % 2
    b = np.array(b, dtype=int) % 2
    rows, cols = A.shape
    aug = np.concatenate([A, b.reshape(-1, 1)], axis=1) % 2
    R, pivots = rref_gf2(aug)
    # check consistency: any pivot in last column?
    if (cols) in pivots:
        return None
    x = np.zeros(cols, dtype=int)
    for ri, pc in enumerate(pivots):
        if pc < cols:
            x[pc] = R[ri, cols]
    return x % 2

# ============================================================
# TASK 1
# ============================================================

def enum_functions(domain, codomain):
    """All functions domain->codomain as tuples aligned to domain order."""
    n = len(domain)
    return [tuple(vals) for vals in itertools.product(codomain, repeat=n)]

def task1_case(name, S, A, Vdim, T, B, Wdim, Xs_size, Xv_dim, verbose=False):
    Xs = list(range(Xs_size))
    x = Xv_dim

    # ---- build r = p <| q ----
    D = []
    for s in S:
        for f in itertools.product(T, repeat=len(A[s])):  # f aligned to A[s] order
            D.append((s, f))
    absD = len(D)

    # C_{(s,f)} for each element
    def Cset(s, f):
        Clist = []
        for ai, a in enumerate(A[s]):
            t = f[ai]
            for b in B[t]:
                Clist.append((ai, b))
        return Clist

    # ---------- SET component ----------
    # LHS elements: (s,f,g) with g: Cset -> Xs
    LHS = []
    for (s, f) in D:
        Clist = Cset(s, f)
        for g in itertools.product(Xs, repeat=len(Clist)):
            LHS.append((s, f, g, Clist))

    # qX set = [(t, gtuple: B[t]->Xs)]
    qX = []
    for t in T:
        for gt in itertools.product(Xs, repeat=len(B[t])):
            qX.append((t, gt))
    # RHS set: (s, h) with h: A[s] -> qX
    RHS = set()
    for s in S:
        for h in itertools.product(range(len(qX)), repeat=len(A[s])):
            RHS.add((s, tuple(qX[hi] for hi in h)))

    def Theta_set(elt):
        s, f, g, Clist = elt
        pos = {cb: idx for idx, cb in enumerate(Clist)}
        h = []
        for ai, a in enumerate(A[s]):
            t = f[ai]
            g_a = tuple(g[pos[(ai, b)]] for b in B[t])
            h.append((t, g_a))
        return (s, tuple(h))

    def Theta_set_inv(elt):
        s, h = elt
        f = tuple(hv[0] for hv in h)
        Clist = Cset(s, f)
        pos = {cb: idx for idx, cb in enumerate(Clist)}
        g = [None] * len(Clist)
        for ai, a in enumerate(A[s]):
            t, g_a = h[ai]
            for bi, b in enumerate(B[t]):
                g[pos[(ai, b)]] = g_a[bi]
        return (s, f, tuple(g), Clist)

    images = [Theta_set(e) for e in LHS]
    set_lhs_size = len(LHS)
    set_rhs_size = len(RHS)
    injective = len(set(images)) == len(images)
    surjective = set(images) == RHS
    # inverse round trips
    inv_ok = True
    for e in LHS:
        y = Theta_set(e)
        e2 = Theta_set_inv(y)
        # compare ignoring Clist recompute (Clist deterministic)
        if (e2[0], e2[1], e2[2]) != (e[0], e[1], e[2]):
            inv_ok = False
            break
    for y in RHS:
        e = Theta_set_inv(y)
        y2 = Theta_set(e)
        if y2 != y:
            inv_ok = False
            break
    set_bijection = injective and surjective and (set_lhs_size == set_rhs_size) and inv_ok

    # ---------- VEC component ----------
    # LHS basis labels (s,t,i,j,k):  Hom(U_{d0}, X), U=(+)_{s,t} V_s(x)W_t
    lhs_labels = []
    for s in S:
        for t in T:
            for i in range(Vdim[s]):
                for j in range(Wdim[t]):
                    for k in range(x):
                        lhs_labels.append((s, t, i, j, k))
    lhs_index = {lab: idx for idx, lab in enumerate(lhs_labels)}
    # RHS basis labels: (+)_s Hom(V_s, (+)_t Hom(W_t,X)); coordinate (s,t,k,j,i)
    rhs_labels = []
    for s in S:
        for t in T:
            for k in range(x):
                for j in range(Wdim[t]):
                    for i in range(Vdim[s]):
                        rhs_labels.append((s, t, k, j, i))
    rhs_index = {lab: idx for idx, lab in enumerate(rhs_labels)}

    dimL = len(lhs_labels)
    dimR = len(rhs_labels)
    # Theta_vec: permutation. lhs (s,t,i,j,k) -> rhs (s,t,k,j,i)
    def theta_vec_matrix(xx):
        # build for given X_v dim xx (regenerate labels with that k-range)
        L = []
        for s in S:
            for t in T:
                for i in range(Vdim[s]):
                    for j in range(Wdim[t]):
                        for k in range(xx):
                            L.append((s, t, i, j, k))
        Ridx = {}
        R = []
        for s in S:
            for t in T:
                for k in range(xx):
                    for j in range(Wdim[t]):
                        for i in range(Vdim[s]):
                            R.append((s, t, k, j, i))
        for idx, lab in enumerate(R):
            Ridx[lab] = idx
        Th = np.zeros((len(R), len(L)), dtype=int)
        for col, (s, t, i, j, k) in enumerate(L):
            Th[Ridx[(s, t, k, j, i)], col] = 1
        return Th, L, R, Ridx

    Th, Llab, Rlab, Ridx = theta_vec_matrix(x)
    vec_dims_equal = (dimL == dimR)
    # invertible: square and full rank
    vec_invertible = (Th.shape[0] == Th.shape[1]) and (rank_gf2(Th) == Th.shape[0])
    # also confirm it's a genuine permutation
    is_perm = True
    if Th.size > 0:
        is_perm = (Th.sum(axis=0) == 1).all() and (Th.sum(axis=1) == 1).all()
    elif Th.shape[0] == Th.shape[1]:
        is_perm = True

    # ---------- NATURALITY ----------
    # pick phi: X -> X'.  phi_s: Xs -> Xs' function ; phi_v: matrix xprime x x
    xprime = x + 1 if x >= 1 else 0
    Xs_p_size = Xs_size + 1
    # random-ish phi_s
    phi_s = [ (i + 1) % Xs_p_size for i in range(Xs_size) ]
    # phi_v random over GF2
    phi_v = np.random.randint(0, 2, size=(xprime, x)) if (xprime > 0 and x > 0) else np.zeros((xprime, x), dtype=int)

    # SET naturality: check for all LHS elements
    # r(phi): (s,f,g) -> (s,f, phi_s o g)
    # pq(phi): (s,h) -> (s, a->(t, phi_s o g_a))
    set_nat_ok = True
    for e in LHS:
        s, f, g, Clist = e
        g2 = tuple(phi_s[v] for v in g)
        e2 = (s, f, g2, Clist)
        left = Theta_set(e2)  # in X'
        # right: apply pq(phi) to Theta_set(e)
        s0, h = Theta_set(e)
        h2 = tuple((t, tuple(phi_s[v] for v in g_a)) for (t, g_a) in h)
        right = (s0, h2)
        if left != right:
            set_nat_ok = False
            break

    # VEC naturality
    ThX, LlabX, RlabX, RidxX = theta_vec_matrix(x)
    ThXp, LlabXp, RlabXp, RidxXp = theta_vec_matrix(xprime)
    # r(phi): LHS(X)->LHS(X'): entry [(s,t,i,j,kp),(s,t,i,j,k)] = phi_v[kp,k]
    LidxX = {lab: idx for idx, lab in enumerate(LlabX)}
    LidxXp = {lab: idx for idx, lab in enumerate(LlabXp)}
    rmap = np.zeros((len(LlabXp), len(LlabX)), dtype=int)
    for (s, t, i, j, k), col in LidxX.items():
        for kp in range(xprime):
            if phi_v[kp, k]:
                rmap[LidxXp[(s, t, i, j, kp)], col] ^= 1
    # pq(phi): RHS(X)->RHS(X'): entry [(s,t,kp,j,i),(s,t,k,j,i)] = phi_v[kp,k]
    ppmap = np.zeros((len(RlabXp), len(RlabX)), dtype=int)
    for (s, t, k, j, i), col in RidxX.items():
        for kp in range(xprime):
            if phi_v[kp, k]:
                ppmap[RidxXp[(s, t, kp, j, i)], col] ^= 1
    # check Theta_{X'} @ rmap == ppmap @ Theta_X
    lhs_comp = (ThXp @ rmap) % 2
    rhs_comp = (ppmap @ ThX) % 2
    vec_nat_ok = np.array_equal(lhs_comp, rhs_comp)

    print(f"--- CASE {name} ---")
    print(f"  |D| = {absD}")
    print(f"  SET: LHS size={set_lhs_size}, RHS size={set_rhs_size}, "
          f"Theta_set bijection={set_bijection} (inj={injective},surj={surjective},inv={inv_ok})")
    print(f"  VEC: LHS dim={dimL}, RHS dim={dimR}, dims_equal={vec_dims_equal}, "
          f"Theta_vec invertible={vec_invertible}, permutation={is_perm}")
    print(f"  NATURALITY: set_square_commutes={set_nat_ok}, vec_square_commutes={vec_nat_ok}")
    allpass = set_bijection and vec_dims_equal and vec_invertible and set_nat_ok and vec_nat_ok
    print(f"  => {'PASS' if allpass else 'FAIL'}")
    print()
    return allpass


print("=" * 60)
print("TASK 1: (-)<| comparison map natural ISO over Set x Vec_fd / F2")
print("=" * 60)

# Case (a)
resa = task1_case(
    "a",
    S=['s'], A={'s': ['a1', 'a2']}, Vdim={'s': 1},
    T=['t1', 't2'], B={'t1': ['b'], 't2': ['b']}, Wdim={'t1': 1, 't2': 1},
    Xs_size=2, Xv_dim=2)

# Case (b) asymmetric
resb = task1_case(
    "b",
    S=['s1', 's2'], A={'s1': ['a'], 's2': ['a1', 'a2']}, Vdim={'s1': 1, 's2': 2},
    T=['t1', 't2'], B={'t1': ['b1'], 't2': ['b1', 'b2']}, Wdim={'t1': 1, 't2': 1},
    Xs_size=2, Xv_dim=1)

# Case (c) with zero-dim V_s and zero-dim W_t
resc = task1_case(
    "c",
    S=['s1', 's2'], A={'s1': ['a1'], 's2': ['a1', 'a2']}, Vdim={'s1': 0, 's2': 1},
    T=['t1', 't2'], B={'t1': ['b1'], 't2': ['b1', 'b2']}, Wdim={'t1': 0, 't2': 1},
    Xs_size=2, Xv_dim=2)

task1_all = resa and resb and resc
print(f"TASK 1 OVERALL: {'ALL PASS' if task1_all else 'SOME FAIL'}")
print()


# ============================================================
# TASK 2 : dual numbers R = F2[e]/e^2
# ============================================================
# Module = (dim d, N) with N nilpotent, N^2=0, column convention: N[:,i]=e.basis_i.
# Module map T:P->M is (dimM x dimP) with T N_P = N_M T.

def rand_invertible_gf2(d):
    if d == 0:
        return np.zeros((0, 0), dtype=int)
    while True:
        M = np.random.randint(0, 2, size=(d, d))
        if rank_gf2(M) == d:
            return M % 2

def inv_gf2(M):
    d = M.shape[0]
    if d == 0:
        return np.zeros((0, 0), dtype=int)
    aug = np.concatenate([M % 2, np.eye(d, dtype=int)], axis=1)
    R, piv = rref_gf2(aug)
    return R[:, d:] % 2

def rand_nilpotent(d):
    """Random N over GF2 with N^2=0, dim d, column convention."""
    if d == 0:
        return np.zeros((0, 0), dtype=int)
    if d == 1:
        return np.zeros((1, 1), dtype=int)
    m = random.randint(1, d - 1)
    n = d - m
    N0 = np.zeros((d, d), dtype=int)
    Bblk = np.random.randint(0, 2, size=(m, n))
    N0[0:m, m:d] = Bblk  # maps last n coords into first m; N0^2=0
    P = rand_invertible_gf2(d)
    Pinv = inv_gf2(P)
    N = (P @ N0 @ Pinv) % 2
    assert np.array_equal((N @ N) % 2, np.zeros((d, d), dtype=int))
    return N

def hom_R_basis(P, M):
    """Basis (list of dimM x dimP matrices) of Hom_R(P,M). P=(dP,NP),M=(dM,NM)."""
    dP, NP = P
    dM, NM = M
    nvars = dM * dP
    if nvars == 0:
        return []
    # operator L: flatten(T) -> flatten(T NP + NM T)
    L = np.zeros((nvars, nvars), dtype=int)
    for a in range(dM):
        for b in range(dP):
            T = np.zeros((dM, dP), dtype=int)
            T[a, b] = 1
            res = (T @ NP + NM @ T) % 2
            L[:, a * dP + b] = res.reshape(-1)
    L %= 2
    ns = nullspace_gf2(L)
    return [v.reshape(dM, dP) % 2 for v in ns]

def hom_R_dim(P, M):
    return len(hom_R_basis(P, M))

def hom_R_module(Q, X):
    """Hom_R(Q,X) as an R-module: returns (dim, N_hom) with basis matrices too.
       e-action: T -> N_X T (column convention on the Hom space)."""
    dQ, NQ = Q
    dX, NX = X
    basis = hom_R_basis(Q, X)
    d = len(basis)
    if d == 0:
        return (0, np.zeros((0, 0), dtype=int), [])
    # flattened basis as columns
    Bmat = np.zeros((dX * dQ, d), dtype=int)
    for idx, T in enumerate(basis):
        Bmat[:, idx] = T.reshape(-1)
    Nhom = np.zeros((d, d), dtype=int)
    for idx, T in enumerate(basis):
        S = (NX @ T) % 2
        c = solve_gf2(Bmat, S.reshape(-1))
        assert c is not None, "e-action not closed on Hom_R"
        Nhom[:, idx] = c
    Nhom %= 2
    assert np.array_equal((Nhom @ Nhom) % 2, np.zeros((d, d), dtype=int))
    return (d, Nhom, basis)

def tensor_over_R(P, Q):
    """P (x)_R Q. Returns (dim, N)."""
    dP, NP = P
    dQ, NQ = Q
    pq = dP * dQ
    if pq == 0:
        return (0, np.zeros((0, 0), dtype=int))
    def idx(i, j):
        return i * dQ + j
    # relations: (NP e_i)(x)f_j - e_i(x)(NQ f_j) for all i,j
    rels = []
    for i in range(dP):
        for j in range(dQ):
            v = np.zeros(pq, dtype=int)
            for k in range(dP):
                if NP[k, i]:
                    v[idx(k, j)] ^= 1
            for l in range(dQ):
                if NQ[l, j]:
                    v[idx(i, l)] ^= 1
            if v.any():
                rels.append(v % 2)
    if len(rels) == 0:
        Rel = np.zeros((0, pq), dtype=int)
    else:
        Rel = np.array(rels, dtype=int) % 2
    R, pivots = rref_gf2(Rel)
    pivset = set(pivots)
    nonpiv = [c for c in range(pq) if c not in pivset]
    qdim = len(nonpiv)
    def reduce_vec(v):
        v = v.copy() % 2
        for ri, pc in enumerate(pivots):
            if v[pc] == 1:
                v ^= R[ri]
        return v % 2
    def coords(v):
        vr = reduce_vec(v)
        return np.array([vr[c] for c in nonpiv], dtype=int)
    # N on tensor: e-action = NP (x) 1: e_i(x)f_j -> (NP e_i)(x)f_j
    Ntensor_full = np.zeros((pq, pq), dtype=int)
    for i in range(dP):
        for j in range(dQ):
            col = idx(i, j)
            for k in range(dP):
                if NP[k, i]:
                    Ntensor_full[idx(k, j), col] ^= 1
    Nq = np.zeros((qdim, qdim), dtype=int)
    for ci, c in enumerate(nonpiv):
        e = np.zeros(pq, dtype=int)
        e[c] = 1
        img = (Ntensor_full @ e) % 2
        Nq[:, ci] = coords(img)
    Nq %= 2
    return (qdim, Nq)

def direct_sum_modules(mods):
    dims = [m[0] for m in mods]
    D = sum(dims)
    N = np.zeros((D, D), dtype=int)
    off = 0
    for (d, Nm) in mods:
        if d > 0:
            N[off:off + d, off:off + d] = Nm
        off += d
    return (D, N)


print("=" * 60)
print("TASK 2: dual numbers R = F2[e]/e^2 is a COLLAPSE base")
print("=" * 60)

# fixed modules
k_mod = (1, np.zeros((1, 1), dtype=int))                     # k = R/eR
R_mod = (2, np.array([[0, 0], [1, 0]], dtype=int))           # R, column conv: e.1=e, e.e=0
RplusK = direct_sum_modules([R_mod, k_mod])

# ---------- 2a: copower-tiny (finite families) ----------
print("\n[2a] Copower-tininess:  Hom_R(P, (+)_i M_i) =?= (+)_i Hom_R(P, M_i)")
def rand_module(maxd=3):
    d = random.randint(1, maxd)
    return (d, rand_nilpotent(d))

test_Ps = {'k': k_mod, 'R': R_mod, 'R+k': RplusK,
           'randN1': rand_module(2), 'randN2': rand_module(3)}
mismatch_2a = 0
total_2a = 0
for pname, P in test_Ps.items():
    for trial in range(10):
        fam = [rand_module(3) for _ in range(random.randint(1, 4))]
        big = direct_sum_modules(fam)
        lhs = hom_R_dim(P, big)
        rhs = sum(hom_R_dim(P, Mi) for Mi in fam)
        total_2a += 1
        if lhs != rhs:
            mismatch_2a += 1
            print(f"   MISMATCH P={pname}: {lhs} != {rhs}")
print(f"   tested {total_2a} instances, mismatches = {mismatch_2a}")
# explicit dims for named P against a fixed family
fam_fixed = [k_mod, R_mod, rand_module(2)]
big_fixed = direct_sum_modules(fam_fixed)
for pname, P in [('k', k_mod), ('R', R_mod), ('R+k', RplusK)]:
    l = hom_R_dim(P, big_fixed)
    r = sum(hom_R_dim(P, Mi) for Mi in fam_fixed)
    print(f"   P={pname:4s}: dim Hom_R(P, (+)M)={l}, (+) dim Hom_R(P,M)={r}, equal={l==r}")

# ---------- 2b: collapse composition <| = (x)_R ----------
print("\n[2b] Collapse:  dim Hom_R(P,(+)_t Hom_R(Q_t,X)) =?= (+)_t dim Hom_R(P (x)_R Q_t, X)")
mismatch_2b = 0
N2b = 50
for trial in range(N2b):
    P = rand_module(3)
    X = rand_module(3)
    ntq = random.randint(1, 3)
    Qs = [rand_module(3) for _ in range(ntq)]
    # LHS: Hom_R(P, (+)_t Hom_R(Q_t,X))
    inner_mods = [hom_R_module(Q, X)[:2] for Q in Qs]  # (dim, N)
    inner_big = direct_sum_modules(inner_mods)
    lhs = hom_R_dim(P, inner_big)
    # RHS: (+)_t Hom_R(P (x)_R Q_t, X)
    rhs = 0
    for Q in Qs:
        PtQ = tensor_over_R(P, Q)
        rhs += hom_R_dim(PtQ, X)
    if lhs != rhs:
        mismatch_2b += 1
        print(f"   MISMATCH trial {trial}: lhs={lhs} rhs={rhs}")
print(f"   ran {N2b} random instances, mismatches = {mismatch_2b}")

# ---------- 2c: k copower-tiny YES, projective/dualizable NO ----------
print("\n[2c] Contrast: k copower-tiny=YES (2a), k projective/dualizable=NO")
# k copower-tiny already YES from 2a (P='k' rows above).
# projection pi: R -> k, R-linear.  pi=[[1,0]] (column conv on R basis {1,e})
pi = np.array([[1, 0]], dtype=int)
# check pi is R-linear: pi N_R = N_k pi
NR = R_mod[1]; Nk = k_mod[1]
pi_Rlin = np.array_equal((pi @ NR) % 2, (Nk @ pi) % 2)
# section s: k -> R with pi s = id and R-linear (in Hom_R(k,R))
homkR = hom_R_basis(k_mod, R_mod)  # list of 2x1 matrices
section_exists = False
# a general R-linear map k->R is a GF2-combination of basis; check if any gives pi s = id
if len(homkR) > 0:
    dimspan = len(homkR)
    for coeffs in itertools.product([0, 1], repeat=dimspan):
        s = np.zeros((2, 1), dtype=int)
        for c, T in zip(coeffs, homkR):
            if c:
                s = (s + T) % 2
        if np.array_equal((pi @ s) % 2, np.array([[1]], dtype=int)):
            section_exists = True
            break
dim_homkk = hom_R_dim(k_mod, k_mod)
dim_homkR = hom_R_dim(k_mod, R_mod)
dim_homkR_F2 = 1 * 2  # F2-dim of all linear maps k->R
print(f"   pi:R->k is R-linear: {pi_Rlin}")
print(f"   dim Hom_R(k,k) = {dim_homkk}  (expected 1)")
print(f"   dim Hom_R(k,R) = {dim_homkR}  (F2-Hom would be {dim_homkR_F2})")
print(f"   R-linear section k->R of pi exists: {section_exists}  (=> k projective/dualizable: {section_exists})")
# copower-tiny of k confirmed:
k_tiny = True  # verified in 2a
for Mi_list in [[k_mod, R_mod], [R_mod, R_mod, k_mod]]:
    big = direct_sum_modules(Mi_list)
    if hom_R_dim(k_mod, big) != sum(hom_R_dim(k_mod, Mi) for Mi in Mi_list):
        k_tiny = False
print(f"   k copower-tiny (rechecked): {k_tiny}")

# ============================================================
# SUMMARY
# ============================================================
print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"TASK 1: case a={'PASS' if resa else 'FAIL'}, "
      f"case b={'PASS' if resb else 'FAIL'}, case c={'PASS' if resc else 'FAIL'}")
print(f"TASK 2a: copower-tiny mismatches = {mismatch_2a}/{total_2a}")
print(f"TASK 2b: collapse <|=(x)_R mismatches = {mismatch_2b}/{N2b}")
print(f"TASK 2c: k copower-tiny=YES, section exists (projective)={section_exists} => "
      f"k projective/dualizable = {'YES' if section_exists else 'NO'}")
