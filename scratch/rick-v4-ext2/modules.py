"""
F2[V4]-module homological algebra: minimal free resolutions and Ext.
Uses f2lib for exact F2 linear algebra.
"""
import numpy as np
import itertools
from f2lib import mod2, rank, kernel, solve, EXP, IDX, gmul

I4 = np.eye(4, dtype=np.uint8)

# ---------- kG regular module (R as a left module over itself) ----------
def left_mult_matrix(i):
    """4x4 matrix of left multiplication by basis element i on kG (basis e,a,b,ab)."""
    M = np.zeros((4, 4), dtype=np.uint8)
    for j in range(4):
        M[gmul(i, j), j] = 1
    return M

def regular_module():
    return {'d': 4, 'act': [left_mult_matrix(i) for i in range(4)]}

# ---------- building modules from generator actions ----------
def module_from_ab(mat_a, mat_b):
    """Build module dict given action matrices of a and b (e=I, ab=a@b)."""
    mat_a = mod2(mat_a); mat_b = mod2(mat_b)
    d = mat_a.shape[0]
    I = np.eye(d, dtype=np.uint8)
    act = [I, mat_a, mat_b, mod2(mat_a @ mat_b)]
    return {'d': d, 'act': act}

def act_elt(mod, rvec):
    """Action of algebra element rvec (length-4 F2 vector) on module mod: returns d x d matrix."""
    rvec = mod2(rvec)
    d = mod['d']
    M = np.zeros((d, d), dtype=np.uint8)
    for i in range(4):
        if rvec[i]:
            M = (M + mod['act'][i]) & 1
    return M

# ---------- radical ----------
# J = augmentation ideal = span{a+e, b+e, ab+e} as a subspace of kG.
J_BASIS = []
for g in (1, 2, 3):  # a,b,ab
    v = np.zeros(4, dtype=np.uint8); v[g] = 1; v[0] ^= 1  # g + e
    J_BASIS.append(v)
J_BASIS = np.array(J_BASIS, dtype=np.uint8).T   # 4 x 3

def JM_subspace(mod):
    """Return matrix whose columns span J*M inside M (dim d)."""
    d = mod['d']
    cols = []
    # J spanned by (a+e),(b+e),(ab+e); act on each basis vector of M
    for k in range(J_BASIS.shape[1]):
        Aj = act_elt(mod, J_BASIS[:, k])   # d x d
        for c in range(d):
            cols.append(Aj[:, c])
    if not cols:
        return np.zeros((d, 0), dtype=np.uint8)
    return np.array(cols, dtype=np.uint8).T

def min_generators(mod):
    """Return list of column vectors in M that lift a basis of M/JM (minimal generators)."""
    d = mod['d']
    JM = JM_subspace(mod)
    # extend JM basis to a basis of F2^d; the added vectors are lifts of M/JM basis
    from f2lib import rank as f2rank
    cur = JM.copy() if JM.shape[1] else np.zeros((d, 0), dtype=np.uint8)
    gens = []
    base_rank = f2rank(cur) if cur.shape[1] else 0
    r = base_rank
    for c in range(d):
        e = np.zeros((d, 1), dtype=np.uint8); e[c, 0] = 1
        cand = np.concatenate([cur, e], axis=1)
        if f2rank(cand) > r:
            cur = cand
            r += 1
            gens.append(e[:, 0].copy())
    return gens  # length = d - dim(JM)

# ---------- free modules R^m and homs ----------
def free_act_elt(m, rvec):
    """Action of algebra elt rvec on free module R^m (dim 4m), block form."""
    blk = act_elt_regular(rvec)  # 4x4
    d = 4 * m
    M = np.zeros((d, d), dtype=np.uint8)
    for t in range(m):
        M[4*t:4*t+4, 4*t:4*t+4] = blk
    return M

def act_elt_regular(rvec):
    rvec = mod2(rvec)
    M = np.zeros((4, 4), dtype=np.uint8)
    for i in range(4):
        if rvec[i]:
            M = (M + left_mult_matrix(i)) & 1
    return M

def phi_matrix(gens, mod):
    """Map phi: R^m -> mod sending basis-generator t (times algebra basis u)
    to act(u) @ gens[t].  R^m has ordered basis: (u in 0..3) fastest within block t.
    Column ordering: block t (t=0..m-1), within block u=0..3.
    Returns matrix (mod['d'] x 4m)."""
    d = mod['d']
    m = len(gens)
    cols = []
    for t in range(m):
        for u in range(4):
            au = mod['act'][u]
            cols.append((au @ gens[t]) & 1)
    if not cols:
        return np.zeros((d, 0), dtype=np.uint8)
    return np.array(cols, dtype=np.uint8).T

def submodule_as_module(K):
    """Given K = (4m x r) columns spanning an R-submodule of R^m (m = K.shape[0]//4),
    return (module_dict for K in its own basis, and the inclusion columns K).
    Action of basis elt u on K expressed in the chosen column basis of K."""
    dim_amb = K.shape[0]
    m = dim_amb // 4
    r = K.shape[1]
    act = []
    for u in range(4):
        Au = free_act_elt(m, unit_vec(u))  # dim_amb x dim_amb
        # image of each K column under Au, expressed in K basis
        img = (Au @ K) & 1                 # dim_amb x r
        # solve K X = img  => X is r x r
        X = solve(K, img)
        act.append(X & 1)
    return {'d': r, 'act': act}, K

def unit_vec(u):
    v = np.zeros(4, dtype=np.uint8); v[u] = 1
    return v

# ---------- minimal free resolution ----------
def min_resolution(mod, length):
    """Compute minimal free resolution of mod up to homological degree `length`.
    Returns:
      betti = [m0, m1, ..., m_length]  (ranks of free modules P_n = R^{m_n})
      boundaries = [d1, d2, ...] where d_n : R^{m_n} -> R^{m_{n-1}} given as a
                   list of m_n columns, each an element of R^{m_{n-1}} = F2^{4 m_{n-1}}.
    """
    betti = []
    boundaries = []
    # P_0 -> mod
    gens = min_generators(mod)
    betti.append(len(gens))
    cur_mod = mod
    cur_gens = gens
    # phi_0 : R^{m0} -> mod
    phi = phi_matrix(cur_gens, cur_mod)
    for n in range(1, length + 1):
        # kernel of phi : subspace of R^{m_{n-1}} (dim 4*m_{n-1})
        K = kernel(phi)             # (4 m_{n-1}) x r
        if K.shape[1] == 0:
            betti.append(0)
            boundaries.append(np.zeros((phi.shape[1], 0), dtype=np.uint8))
            # once zero, stays zero
            for _ in range(n+1, length+1):
                betti.append(0)
                boundaries.append(np.zeros((0, 0), dtype=np.uint8))
            break
        Kmod, Kincl = submodule_as_module(K)
        # minimal generators of the kernel submodule (in K's own basis)
        kgens_local = min_generators(Kmod)   # vectors in F2^r
        m_n = len(kgens_local)
        betti.append(m_n)
        # boundary d_n: R^{m_n} -> R^{m_{n-1}}: generator t -> Kincl @ kgens_local[t]
        dn_cols = []
        for g in kgens_local:
            col = (Kincl @ g) & 1     # element of R^{m_{n-1}}
            dn_cols.append(col)
        dn = np.array(dn_cols, dtype=np.uint8).T if dn_cols else np.zeros((K.shape[0], 0), dtype=np.uint8)
        boundaries.append(dn)
        # set up next phi: map R^{m_n} -> Kmod using kgens_local
        phi = phi_matrix(kgens_local, Kmod)
        cur_mod = Kmod
    return betti, boundaries

# ---------- Ext^n(mod, N) via Hom(P_*, N) ----------
def hom_differential(dn, N):
    """Given boundary d_n : R^{m_n} -> R^{m_{n-1}} (columns = elements of F2^{4 m_{n-1}}),
    return the induced map Hom(R^{m_{n-1}},N) -> Hom(R^{m_n},N).
    Hom(R^m,N) = N^m, coordinates: block t (0..m-1), within block N-coords.
    A hom f is data (f_0,...,f_{m-1}) in N. Precompose with d_n:
      (f d_n)(gen_t) = f( d_n(gen_t) ).  d_n(gen_t) in R^{m_{n-1}} = (w^0,...,w^{m_{n-1}-1}), w^i in R.
      f(w) = sum_i act_N(w^i) @ f_i.
    Returns matrix ( dN*m_n  x  dN*m_{n-1} )."""
    dN = N['d']
    m_prev = dn.shape[0] // 4 if dn.shape[0] else 0
    m_n = dn.shape[1]
    out = np.zeros((dN * m_n, dN * m_prev), dtype=np.uint8)
    for t in range(m_n):
        col = dn[:, t]  # F2^{4 m_prev}
        for i in range(m_prev):
            w = col[4*i:4*i+4]          # element of R
            Aw = act_elt(N, w)          # dN x dN
            out[dN*t:dN*t+dN, dN*i:dN*i+dN] = Aw
    return out

def ext_tower(mod, N, length):
    """Compute dim Ext^n(mod, N) for n=0..length. Returns list of dims and betti."""
    betti, boundaries = min_resolution(mod, length + 1)
    dN = N['d']
    # cochain complex C^n = Hom(R^{m_n}, N) = N^{m_n}, dim = dN*betti[n]
    # differentials d^n: C^n -> C^{n+1} induced by boundary_{n+1}: P_{n+1}->P_n
    dims = [dN * b for b in betti]
    diffs = []
    for n in range(length + 1):
        if n + 1 < len(boundaries) + 1 and n < len(boundaries):
            dn1 = boundaries[n]  # boundaries[0] = d_1 : P_1 -> P_0, induces C^0->C^1
        else:
            dn1 = None
        # boundaries index: boundaries[k] = d_{k+1}
        if n < len(boundaries):
            D = hom_differential(boundaries[n], N)
        else:
            D = np.zeros((dims[n+1] if n+1 < len(dims) else 0, dims[n]), dtype=np.uint8)
        diffs.append(D)
    # cohomology H^n = ker(d^n)/im(d^{n-1})
    ext = []
    for n in range(length + 1):
        Cn = dims[n]
        # d^n : C^n -> C^{n+1}
        dn = diffs[n] if n < len(diffs) else np.zeros((0, Cn), dtype=np.uint8)
        if dn.shape[1] != Cn:
            # reshape safety
            dn = np.zeros((dn.shape[0], Cn), dtype=np.uint8)
        ker_dim = Cn - rank(dn)
        # d^{n-1} : C^{n-1} -> C^n
        if n == 0:
            im_dim = 0
        else:
            dm = diffs[n-1]
            im_dim = rank(dm)
        ext.append(ker_dim - im_dim)
    return ext, betti
