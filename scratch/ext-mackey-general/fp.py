"""Exact linear algebra over F_p (p prime). Vectors/matrices are lists of ints mod p."""

def inv_mod(a, p):
    a %= p
    # Fermat
    return pow(a, p - 2, p)

def rref(rows, p):
    """Return (R, pivots) reduced row echelon form of matrix `rows` (list of list int) over F_p."""
    R = [[x % p for x in r] for r in rows]
    m = len(R)
    n = len(R[0]) if m else 0
    pivots = []
    pr = 0
    for c in range(n):
        # find pivot in column c at row >= pr
        piv = None
        for r in range(pr, m):
            if R[r][c] % p != 0:
                piv = r
                break
        if piv is None:
            continue
        R[pr], R[piv] = R[piv], R[pr]
        inv = inv_mod(R[pr][c], p)
        R[pr] = [(x * inv) % p for x in R[pr]]
        for r in range(m):
            if r != pr and R[r][c] % p != 0:
                f = R[r][c] % p
                R[r] = [(R[r][k] - f * R[pr][k]) % p for k in range(n)]
        pivots.append(c)
        pr += 1
        if pr == m:
            break
    return R, pivots

def rank(rows, p):
    if not rows:
        return 0
    _, piv = rref(rows, p)
    return len(piv)

def nullspace(rows, p):
    """Basis of {x : rows·x = 0}, rows is m x n. Returns list of n-vectors."""
    if not rows:
        return []
    R, piv = rref(rows, p)
    m = len(R)
    n = len(R[0])
    pivset = set(piv)
    free = [c for c in range(n) if c not in pivset]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, c in enumerate(piv):
            # row i has pivot at column c: sum_j R[i][j] x_j = 0 -> x_c = -sum_{j!=c} R[i][j] x_j
            v[c] = (-R[i][f]) % p
        basis.append(v)
    return basis

def col_space_rank(cols, p):
    """rank of matrix given by list of column vectors."""
    if not cols:
        return 0
    # transpose to rows
    n = len(cols[0])
    rows = [[cols[j][i] for j in range(len(cols))] for i in range(n)]
    return rank(rows, p)

def in_span(vecs, target, p):
    """Is target in F_p-span of vecs? vecs list of vectors."""
    if not vecs:
        return all(x % p == 0 for x in target)
    rows = [list(v) for v in vecs]
    r0 = rank(rows, p)
    r1 = rank(rows + [list(target)], p)
    return r0 == r1

def mat_vec(M, v, p):
    """M: list of rows (each len = len(v)). return M·v."""
    return [sum(M[i][j] * v[j] for j in range(len(v))) % p for i in range(len(M))]

def mat_mat(A, B, p):
    """A m x k, B k x n."""
    k = len(B)
    n = len(B[0]) if k else 0
    m = len(A)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) % p for j in range(n)] for i in range(m)]
