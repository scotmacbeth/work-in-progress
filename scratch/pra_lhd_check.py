"""
Cont(Set) small-case verification for the PROVE session 2026-08-30 (pra-vs-probe-method).

A container is represented by the LIST of position-cardinalities, one entry per shape.
  p = [|P_s| : s in S].
Hom-sets in Cont(Set) depend only on cardinalities:
  |Cont((R,U),(S,P))| = prod_{rho in R} sum_{s in S} |U_rho|^{|P_s|}
(with the convention 0^0 = 1).
"""
from itertools import product as iproduct

def pw(base, exp):
    # set-theoretic |X|^n with 0^0 = 1
    return 1 if exp == 0 else base ** exp

def hom(r, p):
    """|Cont(r, p)| for containers given as position-cardinality lists."""
    tot = 1
    for u in r:
        tot *= sum(pw(u, a) for a in p)
    return tot

def compose(p, q):
    """p <| q as a position-cardinality list. Shapes: sum_s T^{P_s}; positions sum_{a in P_s} Q_{c(a)}."""
    T = len(q)
    out = []
    for a in p:                       # a = |P_s|
        for c in iproduct(range(T), repeat=a):   # c : P_s -> T
            out.append(sum(q[t] for t in c))
    return out

def ext(q, n):
    """|[[q]](n)| = sum_t n^{Q_t}."""
    return sum(pw(n, k) for k in q)

def F(r, q):
    """Candidate left adjoint: identity on shapes, apply [[q]] to each position set."""
    return [ext(q, u) for u in r]

def containers(max_shapes, max_pos):
    """all containers with <= max_shapes shapes, each position set of size <= max_pos"""
    out = []
    for n in range(0, max_shapes + 1):
        for tup in iproduct(range(max_pos + 1), repeat=n):
            out.append(list(tup))
    return out

if __name__ == "__main__":
    ps = containers(2, 2)
    qs = containers(2, 2)
    rs = containers(2, 2)
    bad = []
    n = 0
    for q in qs:
        for p in ps:
            pq = compose(p, q)
            for r in rs:
                n += 1
                lhs = hom(F(r, q), p)      # Cont(F r, p)
                rhs = hom(r, pq)           # Cont(r, p <| q)
                if lhs != rhs:
                    bad.append((q, p, r, lhs, rhs))
    print("triples checked:", n, " mismatches:", len(bad))
    for b in bad[:10]:
        print("  MISMATCH", b)

    # a few named sanity rows, printed with actual numbers
    print()
    print("q            p          r          |Cont(Fr,p)|  |Cont(r,p<|q)|   p<|q")
    rows = [
        ([0,1], [1],    [0]),    # q = 1+y  (Maybe),  p = y^1,  r = y^0
        ([0,1], [1],    [1]),
        ([0,1], [2],    [1]),
        ([2],   [2],    [1]),    # q = y^2,  p = y^2, r = y^1
        ([1,1], [2],    [2]),    # q = 2y
        ([0],   [1,2],  [1]),    # q = y^0 = 1
        ([],    [0,1],  [2]),    # q = 0
        ([0,2], [2],    [2]),
    ]
    for q,p,r in rows:
        print(f"{str(q):12} {str(p):10} {str(r):10} {hom(F(r,q),p):>12} {hom(r,compose(p,q)):>15}   {compose(p,q)}")
