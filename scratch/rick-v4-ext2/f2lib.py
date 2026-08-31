"""
Exact F2 linear algebra + F2[V4]-module homological algebra.

Group G = V4 = Z/2 x Z/2, basis of kG = F2[V4] indexed by exponent vectors:
  idx 0 = e = (0,0)
  idx 1 = a = (1,0)
  idx 2 = b = (0,1)
  idx 3 = ab= (1,1)
Group mult = XOR of the 2-bit exponent tuples.

A "module" is represented as:
  dict with 'd' = F2-dimension, and 'act' = list of 4 (d x d) uint8 matrices,
  act[i] = action of the i-th group-algebra BASIS element (e,a,b,ab) on the module.
Everything over F2 (numpy uint8, arithmetic mod 2).
"""

import numpy as np
import itertools

# ---------- group ----------
# exponent tuple for each basis index
EXP = [(0, 0), (1, 0), (0, 1), (1, 1)]           # e,a,b,ab
IDX = {e: i for i, e in enumerate(EXP)}

def gmul(i, j):
    """index of product of group elements i,j (XOR of exponents)."""
    ei, ej = EXP[i], EXP[j]
    return IDX[(ei[0] ^ ej[0], ei[1] ^ ej[1])]

# ---------- F2 linear algebra ----------
def mod2(M):
    return np.asarray(M, dtype=np.uint8) & 1

def rref(M):
    """Return (R, pivots) reduced row echelon form over F2."""
    M = mod2(M).copy()
    rows, cols = M.shape
    pivots = []
    r = 0
    for c in range(cols):
        # find pivot in column c at row >= r
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

def colspace_dim(M):
    """dim of column space = rank."""
    if M.size == 0:
        return 0
    return rank(M)

def kernel(M):
    """Basis (as columns) of right null space {x : M x = 0} over F2.
    M is (rows x cols); returns (cols x k) matrix whose columns span kernel."""
    M = mod2(M)
    rows, cols = M.shape
    R, pivots = rref(M)
    pivset = set(pivots)
    free = [c for c in range(cols) if c not in pivset]
    basis = []
    # map pivot column -> its row
    piv_row = {pivots[i]: i for i in range(len(pivots))}
    for f in free:
        x = np.zeros(cols, dtype=np.uint8)
        x[f] = 1
        for pc in pivots:
            # R[piv_row[pc], f] contributes
            if R[piv_row[pc], f]:
                x[pc] ^= 1
        basis.append(x)
    if not basis:
        return np.zeros((cols, 0), dtype=np.uint8)
    return np.array(basis, dtype=np.uint8).T

def col_reduce(M):
    """Return a matrix whose columns form a basis of the column space of M."""
    M = mod2(M)
    if M.size == 0 or M.shape[1] == 0:
        return np.zeros((M.shape[0], 0), dtype=np.uint8)
    # column space basis = transpose, row-reduce, pick independent rows
    Rt, piv = rref(M.T)
    cols = [M[:, 0:0]]  # placeholder
    # independent original columns: greedily
    basis = []
    cur = np.zeros((M.shape[0], 0), dtype=np.uint8)
    for c in range(M.shape[1]):
        cand = np.concatenate([cur, M[:, c:c+1]], axis=1)
        if rank(cand) > cur.shape[1]:
            cur = cand
    return cur

def solve(A, B):
    """Solve A X = B over F2 for X (columns), assuming a solution exists.
    A: (m x n), B: (m x k). Returns X (n x k) one particular solution.
    Raises if inconsistent."""
    A = mod2(A); B = mod2(B)
    m, n = A.shape
    k = B.shape[1]
    aug = np.concatenate([A, B], axis=1)
    R, piv = rref(aug)
    # check consistency: any pivot in the B-columns region
    for p in piv:
        if p >= n:
            raise ValueError("inconsistent system")
    X = np.zeros((n, k), dtype=np.uint8)
    piv_row = {piv[i]: i for i in range(len(piv))}
    for pc in piv:
        if pc < n:
            X[pc] = R[piv_row[pc], n:n+k]
    return X

def in_colspace(M, v):
    """Is vector v in column space of M?"""
    M = mod2(M); v = mod2(v).reshape(-1, 1)
    if M.shape[1] == 0:
        return not v.any()
    return rank(np.concatenate([M, v], axis=1)) == rank(M)
