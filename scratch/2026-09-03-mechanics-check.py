"""
2026-09-03 mechanics check.

Sanity-check the MECHANICS of natural-transformation identities on FINITE
truncations of F(X) = prod_{n<N} (oplus_{m<M} X), X = Q^d.

An element of F(Q^d) is an N x M x d tensor (N rows, M columns, d-dim vectors).
Everything is over the rationals (we test numerically with random rationals /
floats; exact zero-tolerance comparisons use a tiny epsilon).

This checks INDEXING/MECHANICS ONLY. Nothing here says anything about the
infinite / homological (lim^1) question.
"""

import numpy as np
from fractions import Fraction

np.random.seed(0)
TOL = 1e-9

def rint(*shape):
    """random small integer array (exact-ish rationals)."""
    return np.random.randint(-5, 6, size=shape).astype(float)

def approx_eq(a, b):
    return np.max(np.abs(np.asarray(a) - np.asarray(b))) < TOL if np.size(a) else True

results = []
def record(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


def run_all(N, M, d):
    print(f"\n===== N={N}, M={M}, d={d} =====")

    # ---- 1. ROW inclusion / projection ----
    def in_n(n, A):            # A is M x d  ->  N x M x d
        out = np.zeros((N, M, d))
        out[n] = A
        return out
    def pr_n(n, xi):           # xi is N x M x d -> M x d
        return xi[n].copy()

    ok = True
    detail_bits = []
    for n in range(N):
        for np_ in range(N):
            A = rint(M, d)
            comp = pr_n(n, in_n(np_, A))
            expect = A if n == np_ else np.zeros((M, d))
            good = approx_eq(comp, expect)
            ok = ok and good
    record(f"1 ROW pr_n o in_n' = delta_nn' id (N={N},M={M},d={d})", ok,
           "all n,n' pairs checked")

    # ---- 2. TELESCOPE d_map ----
    # (d.a)_n = a_n - a_{n+1}, a_N := 0.
    def d_map(a):              # a: N x M x d -> N x M x d
        out = np.empty_like(a)
        for n in range(N):
            nxt = a[n+1] if n+1 < N else np.zeros((M, d))
            out[n] = a[n] - nxt
        return out
    # build matrix on flattened space
    dim = N * M * d
    Mat = np.zeros((dim, dim))
    basis = np.eye(dim).reshape(dim, N, M, d)
    for j in range(dim):
        Mat[:, j] = d_map(basis[j]).reshape(-1)
    rank = np.linalg.matrix_rank(Mat, tol=TOL)
    full = (rank == dim)
    kernel_dim = dim - rank
    record(f"2 TELESCOPE d_map iso (rank {rank}/{dim}, ker {kernel_dim})", full,
           "ISO on finite truncation" if full else "NOT full rank")

    # ---- 3. h_E retract (column-0 split) ----
    # h_E modeled as N x d arrays.
    def s(g):                  # g: N x d -> N x M x d
        out = np.zeros((N, M, d))
        out[:, 0, :] = g
        return out
    def r(xi):                 # xi: N x M x d -> N x d
        return xi[:, 0, :].copy()

    g = rint(N, d)
    ok_rs = approx_eq(r(s(g)), g)
    record("3a h_E retract r o s = id", ok_rs)

    xi = rint(N, M, d)
    proj = s(r(xi))
    # expected: zero everywhere except column 0 which equals xi column 0
    exp = np.zeros((N, M, d)); exp[:, 0, :] = xi[:, 0, :]
    ok_sr = approx_eq(proj, exp)
    ok_idem = approx_eq(s(r(s(r(xi)))), proj)   # idempotent
    record("3b h_E s o r = column-0 projection (idempotent)", ok_sr and ok_idem,
           f"proj ok={ok_sr}, idempotent ok={ok_idem}")

    # ---- 4. D3 spread mechanics ----
    def make_alpha(S, gammas):
        # gammas: dict n -> vector in Q^M
        def alpha(xi):         # xi: N x M x d -> d
            acc = np.zeros(d)
            for n in S:
                acc += np.tensordot(gammas[n], xi[n], axes=([0], [0]))  # sum_m gamma_m * xi[n,m,:]
            return acc
        return alpha

    for trial, S in enumerate([[0, 2], list(range(N)), [N-1]]):
        S = [n for n in S if 0 <= n < N]
        gammas = {n: rint(M) for n in S}
        alpha = make_alpha(S, gammas)
        # alpha o in_n' = gamma^{n'} (acting on M x d) if n' in S else 0
        ok = True
        for np_ in range(N):
            A = rint(M, d)
            lhs = alpha(in_n(np_, A))
            if np_ in S:
                rhs = np.tensordot(gammas[np_], A, axes=([0], [0]))
            else:
                rhs = np.zeros(d)
            ok = ok and approx_eq(lhs, rhs)
        record(f"4a D3 alpha o in_n' = gamma^n' [1_S]  (S={S})", ok)

    # naturality: phi: Q^d -> Q^{d'}, F(phi) applies phi entrywise.
    dp = 3
    S = [0, 2, N-1]; S = [n for n in S if 0 <= n < N]
    gammas = {n: rint(M) for n in S}
    alpha = make_alpha(S, gammas)
    phi = rint(dp, d)          # dp x d
    def Fphi(xi):              # apply phi to each vector: N x M x d -> N x M x d'
        return np.einsum('pd,nmd->nmp', phi, xi)
    def alpha_dp(xi):          # alpha in codomain d' : need gammas same, xi has d' vectors
        acc = np.zeros(dp)
        for n in S:
            acc += np.tensordot(gammas[n], xi[n], axes=([0], [0]))
        return acc
    xi = rint(N, M, d)
    lhs = phi @ alpha(xi)          # phi o alpha
    rhs = alpha_dp(Fphi(xi))       # alpha o F(phi)
    ok_nat = approx_eq(lhs, rhs)
    record("4b D3 naturality  phi o alpha = alpha o F(phi)  (d=2 -> d'=3)", ok_nat)


for (N, M, d) in [(4, 4, 2), (5, 3, 2)]:
    run_all(N, M, d)

print("\n===== SUMMARY =====")
allok = True
for name, ok, detail in results:
    allok = allok and ok
    print(f"{'PASS' if ok else 'FAIL':4}  {name}")
print("\nOVERALL:", "ALL PASS" if allok else "SOME FAIL")
