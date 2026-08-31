"""
Verify the two emergent-holonomy witnesses by explicit permutation computation.
Group elements are permutations of a finite set, represented as tuples where
perm[i] = image of point i (0-indexed).
"""
from itertools import product

def compose(p, q):
    # (p*q)(i) = p(q(i))  -- apply q then p
    return tuple(p[q[i]] for i in range(len(p)))

def identity(n):
    return tuple(range(n))

def inverse(p):
    inv = [0]*len(p)
    for i, pi in enumerate(p):
        inv[pi] = i
    return tuple(inv)

def closure(gens, n):
    e = identity(n)
    elems = {e}
    frontier = [e]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = compose(g, x)
            if y not in elems:
                elems.add(y)
                frontier.append(y)
    return elems

def stab(group, s):
    return {g for g in group if g[s] == s}

def is_exact_factorization(P, Pprime, G):
    inter = P & Pprime
    products = {compose(p, q) for p in P for q in Pprime}
    return (inter == {tuple(range(len(next(iter(G)))))},
            len(P)*len(Pprime) == len(G),
            products == G)

def double_cosets(U, A, B):
    """Number and list of (A,B)-double cosets A\\U/B inside U."""
    remaining = set(U)
    cosets = []
    while remaining:
        u = next(iter(remaining))
        dc = {compose(compose(a, u), b) for a in A for b in B}
        cosets.append(dc)
        remaining -= dc
    return cosets

def analyze(name, Pgens, Ppgens, n, s):
    print(f"===== {name} witness =====")
    P = closure(Pgens, n)
    Pp = closure(Ppgens, n)
    G = closure(Pgens + Ppgens, n)
    print(f"|P|={len(P)}, |P'|={len(Pp)}, |G|={len(G)}")
    disj, sizes, cover = is_exact_factorization(P, Pp, G)
    print(f"Exact factorization: P∩P'={{e}}? {disj}; |P||P'|=|G|? {sizes}; P·P'=G? {cover}")
    A = stab(P, s)
    B = stab(Pp, s)
    U = stab(G, s)
    print(f"A=Stab_P({s+1})  size {len(A)}")
    print(f"B=Stab_P'({s+1}) size {len(B)}")
    print(f"U=Stab_G({s+1})  size {len(U)}")
    dcs = double_cosets(U, A, B)
    h = len(dcs)
    print(f"h(s)=|A\\U/B| = {h}")
    print(f"Expected h=|U|={len(U)} since A=B={{e}}? {h==len(U) and len(A)==1 and len(B)==1}")
    print()
    return dict(P=P, Pp=Pp, G=G, A=A, B=B, U=U, h=h)

if __name__ == "__main__":
    # S3 on {1,2,3} -> 0-indexed {0,1,2}, s=1 -> index 0
    c3   = (1,2,0)   # (123)
    t12  = (1,0,2)   # (12)
    s3 = analyze("S3", [c3], [t12], 3, 0)

    # A4 on {1,2,3,4} -> {0,1,2,3}, s=1 -> index 0
    # V4 gens: (12)(34), (13)(24)
    v_a = (1,0,3,2)  # (12)(34)
    v_b = (2,3,0,1)  # (13)(24)
    c123 = (1,2,0,3) # (123)
    a4 = analyze("A4", [v_a, v_b], [c123], 4, 0)
