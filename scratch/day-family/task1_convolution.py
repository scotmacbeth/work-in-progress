"""
TASK 1.  Convolution with * = disjoint union reproduces the PRODUCT;
         with * = cartesian product reproduces the DIRICHLET tensor.
         Pointwiseness test: |[[C (*) D]](X)| == |[[C]](X)| * |[[D]](X)| ?
"""
from core import *
from itertools import product as iproduct

FAILS = []


def all_small_containers(max_shapes=2, max_pos=2, tag='s'):
    """Every container with <= max_shapes shapes and <= max_pos positions each."""
    out = []
    for n in range(max_shapes + 1):
        shapes = [f"{tag}{i}" for i in range(n)]
        for counts in iproduct(range(max_pos + 1), repeat=n):
            P = {shapes[i]: frozenset((shapes[i], j) for j in range(counts[i]))
                 for i in range(n)}
            out.append(Cont(frozenset(shapes), P))
    return out


# --- 1a. structural identity: conv(dunion) == prod, conv(cprod) == dirichlet
print("=" * 78)
print("TASK 1a  convolution(disjoint union) == product   (structural, by construction)")
print("         convolution(cartesian prod) == Dirichlet (structural, by construction)")
Cs = all_small_containers(2, 2, 's')
Ds = all_small_containers(2, 2, 't')
same_prod = same_dir = True
for C in Cs:
    for D in Ds:
        A, B = conv(C, D, dunion), prod(C, D)
        if A != B: same_prod = False
        A, B = conv(C, D, cprod), dirichlet(C, D)
        if A != B: same_dir = False
print(f"  conv(+) == product     : {'PASS' if same_prod else 'FAIL'}  ({len(Cs)*len(Ds)} pairs)")
print(f"  conv(x) == Dirichlet   : {'PASS' if same_dir else 'FAIL'}  ({len(Cs)*len(Ds)} pairs)")
if not (same_prod and same_dir): FAILS.append("1a structural identity")


# --- 1b. pointwiseness of the extension
print()
print("TASK 1b  |[[C (*) D]](X)| == |[[C]](X)| * |[[D]](X)| ?   for |X| = 0,1,2,3")

def pointwise_report(name, tensor, Cs, Ds, Xsizes=(0, 1, 2, 3)):
    bad = []
    total = 0
    for C in Cs:
        for D in Ds:
            for n in Xsizes:
                X = mkset(n)
                lhs = len(extension(tensor(C, D), X))
                rhs = len(extension(C, X)) * len(extension(D, X))
                total += 1
                if lhs != rhs:
                    bad.append((C, D, n, lhs, rhs))
    print(f"  {name}: {total - len(bad)}/{total} instances pointwise; "
          f"{len(bad)} violations")
    return bad

bad_p = pointwise_report("product  ", prod, Cs, Ds)
bad_d = pointwise_report("Dirichlet", dirichlet, Cs, Ds)

print(f"  product   pointwise everywhere : {'PASS' if not bad_p else 'FAIL'}")
if bad_p:
    FAILS.append("1b product not pointwise")
    for b in bad_p[:5]: print("     violation:", b)
print(f"  Dirichlet NOT pointwise (needs >=1 counterexample): "
      f"{'PASS' if bad_d else 'FAIL'}")
if not bad_d: FAILS.append("1b Dirichlet unexpectedly pointwise")

# --- smallest explicit Dirichlet counterexample
if bad_d:
    def size(b):
        C, D, n, l, r = b
        return (len(C.S) + len(D.S), sum(len(C.P[s]) for s in C.S)
                + sum(len(D.P[t]) for t in D.S), n)
    C, D, n, lhs, rhs = min(bad_d, key=size)
    print()
    print("  SMALLEST DIRICHLET COUNTEREXAMPLE")
    print(f"    C = {C}  shapes={sorted(C.S)}  P={{{', '.join(f'{s}: {len(C.P[s])} pos' for s in sorted(C.S))}}}")
    print(f"    D = {D}  shapes={sorted(D.S)}  Q={{{', '.join(f'{t}: {len(D.P[t])} pos' for t in sorted(D.S))}}}")
    CD = dirichlet(C, D)
    print(f"    C (x)_Dir D : shapes={sorted(map(str,CD.S))}, "
          f"positions={[len(CD.P[s]) for s in sorted(CD.S, key=repr)]}")
    print(f"    |X| = {n}:  |[[C(x)D]](X)| = {lhs}   but   "
          f"|[[C]](X)|*|[[D]](X)| = {len(extension(C, mkset(n)))}*"
          f"{len(extension(D, mkset(n)))} = {rhs}")
    print(f"    => {lhs} != {rhs}.  Dirichlet is NOT pointwise.")

# spelled-out canonical counterexample: C = D = y (one shape, one position)
print()
print("  CANONICAL COUNTEREXAMPLE  C = D = y  (one shape, one position):")
y  = Cont(frozenset({'*'}), {'*': frozenset({'p'})})
y2 = Cont(frozenset({'#'}), {'#': frozenset({'q'})})
for n in (0, 1, 2, 3):
    X = mkset(n)
    l = len(extension(dirichlet(y, y2), X))
    r = len(extension(y, X)) * len(extension(y2, X))
    print(f"    |X|={n}: |[[y (x)_Dir y]](X)| = {l:2d}   |[[y]](X)|*|[[y]](X)| = {r:2d}"
          f"   {'agree' if l == r else 'DIFFER'}")
print("    ([[y (x)_Dir y]] = X^(1*1) = X   vs   [[y]]*[[y]] = X^2 )")

print()
print("TASK 1 RESULT:", "PASS" if not FAILS else f"FAIL {FAILS}")
