"""
General exact F2 homological-algebra engine for G = (Z/2)^r.

Group algebra kG = F2[(Z/2)^r], k = F2.
Basis of kG indexed by 0..2^r-1; group element i has exponent vector = bits of i.
Group multiplication = XOR of integers (= addition of exponent vectors in (Z/2)^r).

A module M is a dict: {'d': F2-dim, 'act': list of N_ALG (d x d) uint8 matrices},
where act[i] is the action of the i-th group BASIS element on M (over F2).

Everything mod 2 (numpy uint8). Adapted from the V4 engine in rick-v4-ext2/.
"""
import numpy as np
import itertools

# ============================================================
#  Exact F2 linear algebra (group-independent; copied from f2lib)
# ============================================================
def mod2(M):
    return np.asarray(M, dtype=np.uint8) & 1

def rref(M):
    M = mod2(M).copy()
    rows, cols = M.shape
    pivots = []
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]:
                M[i] ^= M[r]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return M, pivots

def rank(M):
    if M.size == 0:
        return 0
    _, p = rref(M)
    return len(p)

def kernel(M):
    """Basis (as columns) of right null space {x : M x = 0} over F2."""
    M = mod2(M)
    rows, cols = M.shape
    R, pivots = rref(M)
    pivset = set(pivots)
    free = [c for c in range(cols) if c not in pivset]
    basis = []
    piv_row = {pivots[i]: i for i in range(len(pivots))}
    for f in free:
        x = np.zeros(cols, dtype=np.uint8)
        x[f] = 1
        for pc in pivots:
            if R[piv_row[pc], f]:
                x[pc] ^= 1
        basis.append(x)
    if not basis:
        return np.zeros((cols, 0), dtype=np.uint8)
    return np.array(basis, dtype=np.uint8).T

def solve(A, B):
    """One particular solution X of A X = B over F2; raises if inconsistent."""
    A = mod2(A); B = mod2(B)
    m, n = A.shape
    k = B.shape[1]
    aug = np.concatenate([A, B], axis=1)
    R, piv = rref(aug)
    for p in piv:
        if p >= n:
            raise ValueError("inconsistent system")
    X = np.zeros((n, k), dtype=np.uint8)
    piv_row = {piv[i]: i for i in range(len(piv))}
    for pc in piv:
        if pc < n:
            X[pc] = R[piv_row[pc], n:n+k]
    return X

# ============================================================
#  Group  (Z/2)^r
# ============================================================
class Group:
    def __init__(self, r):
        self.r = r
        self.N = 1 << r          # |G| = algebra dimension
    def mul(self, i, j):
        return i ^ j
    def gens(self):
        """indices of the r standard generators x_0..x_{r-1}."""
        return [1 << k for k in range(self.r)]
    def left_mult(self, i):
        N = self.N
        M = np.zeros((N, N), dtype=np.uint8)
        for j in range(N):
            M[i ^ j, j] = 1
        return M
    def regular_module(self):
        return {'d': self.N, 'act': [self.left_mult(i) for i in range(self.N)]}

# ============================================================
#  Permutation module k[G/H] for a subgroup H
# ============================================================
def subgroup(G, gens_idx):
    """Generate the subgroup of (Z/2)^r spanned by given generator indices."""
    elems = {0}
    frontier = list(elems)
    changed = True
    gens_idx = list(gens_idx)
    while changed:
        changed = False
        for e in list(elems):
            for g in gens_idx:
                p = e ^ g
                if p not in elems:
                    elems.add(p); changed = True
    return sorted(elems)

def perm_module_GmodH(G, H_elems):
    """Build k[G/H] as a kG-module with full act array for all N group elements.
    Basis = left cosets gH. Action of group elt i sends coset rep c -> i^c."""
    Hset = set(H_elems)
    # partition G into cosets
    seen = set()
    reps = []
    coset_of = {}     # element -> coset index
    for c in range(G.N):
        if c in seen:
            continue
        idx = len(reps)
        reps.append(c)
        for h in H_elems:
            e = c ^ h
            coset_of[e] = idx
            seen.add(e)
    d = len(reps)     # = |G|/|H|
    act = []
    for i in range(G.N):
        Mi = np.zeros((d, d), dtype=np.uint8)
        for j in range(d):
            # coset j (rep reps[j]) maps to coset containing i ^ reps[j]
            Mi[coset_of[i ^ reps[j]], j] = 1
        act.append(Mi)
    return {'d': d, 'act': act, 'reps': reps, 'coset_of': coset_of}

# ============================================================
#  Module algebra helpers
# ============================================================
def act_elt(G, mod, rvec):
    """Action of algebra element rvec (length-N F2 vector) on mod: d x d matrix."""
    rvec = mod2(rvec)
    d = mod['d']
    M = np.zeros((d, d), dtype=np.uint8)
    for i in range(G.N):
        if rvec[i]:
            M = (M + mod['act'][i]) & 1
    return M

# --- radical: JM = sum_k (x_k - 1) M  (augmentation ideal times M) ---
def JM_subspace(G, mod):
    d = mod['d']
    I = np.eye(d, dtype=np.uint8)
    cols = []
    for g in G.gens():
        Xg = (mod['act'][g] + I) & 1     # (x_k - 1) acting on M
        for c in range(d):
            cols.append(Xg[:, c])
    if not cols:
        return np.zeros((d, 0), dtype=np.uint8)
    return np.array(cols, dtype=np.uint8).T

def min_generators(G, mod):
    """Column vectors lifting a basis of M/JM (minimal generators)."""
    d = mod['d']
    JM = JM_subspace(G, mod)
    cur = JM.copy() if JM.shape[1] else np.zeros((d, 0), dtype=np.uint8)
    gens = []
    r = rank(cur) if cur.shape[1] else 0
    for c in range(d):
        e = np.zeros((d, 1), dtype=np.uint8); e[c, 0] = 1
        cand = np.concatenate([cur, e], axis=1)
        if rank(cand) > r:
            cur = cand; r += 1
            gens.append(e[:, 0].copy())
    return gens

# ============================================================
#  Free modules R^m, homs, minimal free resolution
# ============================================================
def free_act_elt(G, m, rvec):
    """Action of algebra elt rvec on free module R^m (dim N*m), block diagonal."""
    blk = act_elt(G, G.regular_module(), rvec)  # N x N
    N = G.N
    d = N * m
    M = np.zeros((d, d), dtype=np.uint8)
    for t in range(m):
        M[N*t:N*t+N, N*t:N*t+N] = blk
    return M

def unit_vec(G, u):
    v = np.zeros(G.N, dtype=np.uint8); v[u] = 1
    return v

def phi_matrix(G, gens, mod):
    """Map phi: R^m -> mod, generator t times algebra basis u |-> act(u) @ gens[t].
    Column order: block t (0..m-1), within block u=0..N-1. Returns (mod['d'] x N*m)."""
    N = G.N
    cols = []
    for t in range(len(gens)):
        for u in range(N):
            cols.append((mod['act'][u] @ gens[t]) & 1)
    if not cols:
        return np.zeros((mod['d'], 0), dtype=np.uint8)
    return np.array(cols, dtype=np.uint8).T

def submodule_as_module(G, K):
    """K = (N*m x r) columns spanning an R-submodule of R^m. Return its module dict
    (action of each group basis elt in K's column basis) and inclusion K."""
    N = G.N
    m = K.shape[0] // N
    act = []
    for u in range(N):
        Au = free_act_elt(G, m, unit_vec(G, u))
        img = (Au @ K) & 1
        X = solve(K, img)
        act.append(X & 1)
    return {'d': K.shape[1], 'act': act}, K

def min_resolution(G, mod, length):
    """Minimal free resolution of mod up to homological degree `length`.
    Returns betti = [m0..m_length] and boundaries[k] = d_{k+1}: P_{k+1}->P_k
    (columns are elements of R^{m_k} = F2^{N*m_k})."""
    N = G.N
    betti = []
    boundaries = []
    gens = min_generators(G, mod)
    betti.append(len(gens))
    cur_mod = mod
    phi = phi_matrix(G, gens, cur_mod)
    for n in range(1, length + 1):
        K = kernel(phi)
        if K.shape[1] == 0:
            betti.append(0)
            boundaries.append(np.zeros((phi.shape[1], 0), dtype=np.uint8))
            for _ in range(n + 1, length + 1):
                betti.append(0)
                boundaries.append(np.zeros((0, 0), dtype=np.uint8))
            break
        Kmod, Kincl = submodule_as_module(G, K)
        kgens_local = min_generators(G, Kmod)
        betti.append(len(kgens_local))
        dn_cols = [(Kincl @ g) & 1 for g in kgens_local]
        dn = (np.array(dn_cols, dtype=np.uint8).T if dn_cols
              else np.zeros((K.shape[0], 0), dtype=np.uint8))
        boundaries.append(dn)
        phi = phi_matrix(G, kgens_local, Kmod)
        cur_mod = Kmod
    return betti, boundaries

# ============================================================
#  Ext^n(mod, Nmod) via Hom(P_*, Nmod)
# ============================================================
def hom_differential(G, dn, Nmod):
    """Induced map Hom(R^{m_{n-1}},N) -> Hom(R^{m_n},N) from boundary d_n.
    Hom(R^m,N)=N^m. (f d_n)(gen_t)=f(d_n gen_t); d_n gen_t=(w^0..w^{m'-1}), w^i in R;
    f(w)=sum_i act_N(w^i) f_i. Returns (dN*m_n x dN*m_{n-1})."""
    Nalg = G.N
    dN = Nmod['d']
    m_prev = dn.shape[0] // Nalg if dn.shape[0] else 0
    m_n = dn.shape[1]
    out = np.zeros((dN * m_n, dN * m_prev), dtype=np.uint8)
    for t in range(m_n):
        col = dn[:, t]
        for i in range(m_prev):
            w = col[Nalg*i:Nalg*i+Nalg]
            Aw = act_elt(G, Nmod, w)
            out[dN*t:dN*t+dN, dN*i:dN*i+dN] = Aw
    return out

def ext_tower(G, mod, Nmod, length):
    """dim Ext^n_{kG}(mod, Nmod) for n=0..length. Returns (ext_dims, betti)."""
    betti, boundaries = min_resolution(G, mod, length + 1)
    dN = Nmod['d']
    dims = [dN * b for b in betti]
    diffs = []
    for n in range(length + 1):
        if n < len(boundaries):
            D = hom_differential(G, boundaries[n], Nmod)
        else:
            D = np.zeros((dims[n+1] if n+1 < len(dims) else 0, dims[n]), dtype=np.uint8)
        diffs.append(D)
    ext = []
    for n in range(length + 1):
        Cn = dims[n]
        dn = diffs[n] if n < len(diffs) else np.zeros((0, Cn), dtype=np.uint8)
        if dn.shape[1] != Cn:
            dn = np.zeros((dn.shape[0], Cn), dtype=np.uint8)
        ker_dim = Cn - rank(dn)
        im_dim = 0 if n == 0 else rank(diffs[n-1])
        ext.append(ker_dim - im_dim)
    return ext, betti

# ============================================================
#  Group cohomology H^n(H; F2) dimension, via H = (Z/2)^s
# ============================================================
def H_trivial_dims(s, length):
    """dim H^n((Z/2)^s; F2) = number of degree-n monomials in s variables
    = C(n+s-1, s-1). (Poincare series 1/(1-t)^s.)"""
    from math import comb
    if s == 0:
        return [1] + [0]*length     # trivial group: H^0=F2, else 0
    return [comb(n + s - 1, s - 1) for n in range(length + 1)]
