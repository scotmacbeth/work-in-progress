#!/usr/bin/env python3
"""
Brute-force verification of a theorem about triangle(<) -comonoids in Fam(Vec_fd^op)
over the field k = F_2.

Claim:  #( <-comonoids on C=(S,(P_s)) ) = prod_s A(n_s)
        where A(n) = number of unital associative F_2-algebra structures on F_2^n;
        moreover every surviving delta_shape is the DIAGONAL s |-> (s,s),
        and every surviving delta_sharp[s] is a unital associative multiplication
        (with unit = eps_sharp[s]).

All arithmetic is mod 2.  Only numpy / itertools / stdlib used.
"""

import itertools
import numpy as np


# ---------------------------------------------------------------------------
# F_2 matrix helpers
# ---------------------------------------------------------------------------
def mm(a, b):
    """matrix product mod 2"""
    return (a @ b) % 2


def kron(a, b):
    return np.kron(a, b) % 2


def eye(n):
    return np.eye(n, dtype=np.int64) % 2


# ---------------------------------------------------------------------------
# Containers and morphisms in Fam(Vec_fd^op)
#
# Container C : dict shape -> dim (n_{P_s})
# Morphism  : {'f': dict shape_dom -> shape_cod,
#              'sh': dict shape_dom -> matrix (n_{P_s} x n_{Q_{f(s)}})}
#   FORWARD on shapes, BACKWARD (contravariant) on positions.
# ---------------------------------------------------------------------------
def idmor(C):
    return {'f': {s: s for s in C},
            'sh': {s: eye(C[s]) for s in C}}


def compose(m1, m2):
    """m1 : A->B, m2 : B->C  =>  A->C.
    shape: forward comp.  position (contravariant): m1.sh[s] @ m2.sh[m1.f[s]]."""
    f = {}
    sh = {}
    for s in m1['f']:
        t = m1['f'][s]
        f[s] = m2['f'][t]
        sh[s] = mm(m1['sh'][s], m2['sh'][t])
    return {'f': f, 'sh': sh}


def box(u, w):
    """ u : C1->C1', w : C2->C2'   =>   u <  w : C1<C2 -> C1'<C2'.
    shape (a,b)->(u.f a, w.f b);  position kron(u.sh a, w.sh b)."""
    f = {}
    sh = {}
    for a in u['f']:
        for b in w['f']:
            f[(a, b)] = (u['f'][a], w['f'][b])
            sh[(a, b)] = kron(u['sh'][a], w['sh'][b])
    return {'f': f, 'sh': sh}


# Unitors / associator : all position components identity (see header assumption).
def lam(C):
    """ I < C -> C.  domain shape ('*', b), dim 1*C[b]. """
    return {'f': {('*', b): b for b in C},
            'sh': {('*', b): eye(C[b]) for b in C}}


def rho(C):
    """ C < I -> C.  domain shape (a, '*'). """
    return {'f': {(a, '*'): a for a in C},
            'sh': {(a, '*'): eye(C[a]) for a in C}}


def alpha(C):
    """ C<(C<C) -> (C<C)<C.  domain shape (a,(c,d)) -> ((a,c),d), position identity."""
    f = {}
    sh = {}
    for a in C:
        for c in C:
            for d in C:
                f[(a, (c, d))] = ((a, c), d)
                sh[(a, (c, d))] = eye(C[a] * C[c] * C[d])
    return {'f': f, 'sh': sh}


def eps_mor(C, eps_sharp):
    """ epsilon : C -> I ; sh[s] is (C[s] x 1) column."""
    return {'f': {s: '*' for s in C},
            'sh': {s: eps_sharp[s] for s in C}}


def delta_mor(C, delta_shape, delta_sharp):
    """ delta : C -> C<C ; sh[s] is (C[s] x (C[l]*C[r])) with (l,r)=delta_shape[s]."""
    return {'f': dict(delta_shape),
            'sh': dict(delta_sharp)}


# ---------------------------------------------------------------------------
# sanity check on the associator assumption (np.kron associativity)
# ---------------------------------------------------------------------------
def check_kron_associative():
    rng = np.random.default_rng(0)
    for _ in range(50):
        A = rng.integers(0, 2, size=(2, 3))
        B = rng.integers(0, 2, size=(2, 2))
        Cc = rng.integers(0, 2, size=(3, 1))
        left = kron(kron(A, B), Cc)
        right = kron(A, kron(B, Cc))
        assert np.array_equal(left, right), "np.kron not associative -- alpha not identity!"
    return True


# ---------------------------------------------------------------------------
# comonoid laws
# ---------------------------------------------------------------------------
def is_comonoid(C, delta_shape, delta_sharp, eps_sharp):
    d = delta_mor(C, delta_shape, delta_sharp)
    e = eps_mor(C, eps_sharp)
    i = idmor(C)

    # Law 1: lam . (eps < id) . delta = id
    c1 = compose(compose(d, box(e, i)), lam(C))
    for s in C:
        if c1['f'][s] != s or not np.array_equal(c1['sh'][s], eye(C[s])):
            return False

    # Law 2: rho . (id < eps) . delta = id
    c2 = compose(compose(d, box(i, e)), rho(C))
    for s in C:
        if c2['f'][s] != s or not np.array_equal(c2['sh'][s], eye(C[s])):
            return False

    # Law 3: alpha . (id < delta) . delta = (delta < id) . delta
    lhs = compose(compose(d, box(i, d)), alpha(C))
    rhs = compose(d, box(d, i))
    for s in C:
        if lhs['f'][s] != rhs['f'][s]:
            return False
        if not np.array_equal(lhs['sh'][s], rhs['sh'][s]):
            return False
    return True


# ---------------------------------------------------------------------------
# brute-force enumeration of all candidate comonoid structures on C
# ---------------------------------------------------------------------------
def all_matrices(r, c):
    if r * c == 0:
        yield np.zeros((r, c), dtype=np.int64)
        return
    for bits in itertools.product((0, 1), repeat=r * c):
        yield np.array(bits, dtype=np.int64).reshape(r, c)


def enumerate_comonoids(C):
    shapes = list(C)
    pairs = [(a, b) for a in shapes for b in shapes]   # S x S
    survivors = []

    # all eps_sharp : per shape a column in F_2^{n_s}
    eps_choices = {s: list(all_matrices(C[s], 1)) for s in shapes}

    # all delta_shape : function S -> S x S
    for shape_assign in itertools.product(pairs, repeat=len(shapes)):
        delta_shape = {shapes[k]: shape_assign[k] for k in range(len(shapes))}

        # per-shape delta_sharp choices, size depends on delta_shape[s]
        dsharp_choices = {}
        for s in shapes:
            l, r = delta_shape[s]
            dsharp_choices[s] = list(all_matrices(C[s], C[l] * C[r]))

        for eps_combo in itertools.product(*[eps_choices[s] for s in shapes]):
            eps_sharp = {shapes[k]: eps_combo[k] for k in range(len(shapes))}
            for dsh_combo in itertools.product(*[dsharp_choices[s] for s in shapes]):
                delta_sharp = {shapes[k]: dsh_combo[k] for k in range(len(shapes))}
                if is_comonoid(C, delta_shape, delta_sharp, eps_sharp):
                    survivors.append((delta_shape,
                                      {s: delta_sharp[s].copy() for s in shapes},
                                      {s: eps_sharp[s].copy() for s in shapes}))
    return survivors


# ---------------------------------------------------------------------------
# independent count: unital associative F_2-algebras on F_2^n
# ---------------------------------------------------------------------------
def prod_alg(M, x, y, n):
    """ multiplication using tensor-basis matrix M (n x n^2), kron column order i*n+j."""
    return mm(M, kron(x, y))


def enumerate_algebras(n):
    """Return list of (M, eta) unital associative F_2-algebra structures on F_2^n."""
    basis = [np.array([[1 if k == i else 0] for k in range(n)], dtype=np.int64)
             for i in range(n)]
    algs = []
    for M in all_matrices(n, n * n):
        for eta in all_matrices(n, 1):
            # unit law on basis
            ok = True
            for e in basis:
                if not np.array_equal(prod_alg(M, eta, e, n), e):
                    ok = False
                    break
                if not np.array_equal(prod_alg(M, e, eta, n), e):
                    ok = False
                    break
            if not ok:
                continue
            # associativity on basis triples
            for ei in basis:
                for ej in basis:
                    for ek in basis:
                        left = prod_alg(M, ei, prod_alg(M, ej, ek, n), n)
                        right = prod_alg(M, prod_alg(M, ei, ej, n), ek, n)
                        if not np.array_equal(left, right):
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break
            if ok:
                algs.append((M.copy(), eta.copy()))
    return algs


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------
def run():
    assert check_kron_associative()
    print("np.kron associativity check passed -> associator alpha = identity. OK\n")

    # algebra counts we need
    alg_cache = {}
    for n in (1, 2):
        algs = enumerate_algebras(n)
        alg_cache[n] = algs
        print(f"A({n}) = {len(algs)}  (unital associative F_2-algebra structures on F_2^{n})")
    print()

    def alg_set(n):
        return {(M.tobytes(), eta.tobytes()) for (M, eta) in alg_cache[n]}

    cases = [
        ("case1: S={0}, dims=(1)",        {0: 1}),
        ("case2: S={0}, dims=(2)",        {0: 2}),
        ("case3: S={0,1}, dims=(1,1)",    {0: 1, 1: 1}),
        ("case4: S={0,1}, dims=(1,2)",    {0: 1, 1: 2}),
    ]

    header = f"{'case':<28}{'#comon':>8}{'prod A':>8}{'diag?':>7}{'algebra-match?':>16}{'MATCH':>8}"
    print(header)
    print("-" * len(header))

    all_ok = True
    for name, C in cases:
        survivors = enumerate_comonoids(C)
        n_comon = len(survivors)
        predicted = 1
        for s in C:
            predicted *= len(alg_cache[C[s]])

        # all delta_shape diagonal?
        diag = all(all(surv[0][s] == (s, s) for s in C) for surv in survivors)

        # every per-shape delta_sharp = a unital-assoc mult with unit = eps_sharp?
        alg_match = True
        for delta_shape, dsharp, esharp in survivors:
            for s in C:
                if delta_shape[s] != (s, s):
                    alg_match = False
                    continue
                key = (dsharp[s].tobytes(), esharp[s].tobytes())
                if key not in alg_set(C[s]):
                    alg_match = False
        match = (n_comon == predicted) and diag and alg_match
        all_ok = all_ok and match
        print(f"{name:<28}{n_comon:>8}{predicted:>8}{str(diag):>7}"
              f"{str(alg_match):>16}{('OK' if match else 'FAIL'):>8}")

    print()
    print("A(1) =", len(alg_cache[1]), " A(2) =", len(alg_cache[2]))
    print("ALL CASES MATCHED" if all_ok else "SOME CASE FAILED -- investigate")


if __name__ == "__main__":
    run()
