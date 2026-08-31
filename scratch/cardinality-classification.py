"""
Classify COMMUTATIVE, ASSOCIATIVE, UNITAL polynomial binary operations
f: N x N -> N with nonneg integer coefficients, up to total degree D.

f(x,y) = sum_{i+j<=D} c_{ij} x^i y^j, with c_{ij} = c_{ji}.

Constraints:
  1. commutative: built in via c_{ij}=c_{ji}
  2. associative: f(f(x,y),z) = f(x,f(y,z)) identically
  3. unital: exists e in {0,1,2,3} with f(x,e) = x identically

Symbolic solve + brute-force cross-check.
"""

import sympy as sp
from sympy import symbols, Poly, expand, solve, groebner, Rational
import itertools

x, y, z = symbols('x y z')


def make_coeffs(D):
    """Symmetric coefficient symbols c_{ij}=c_{ji}, i+j<=D. Returns dict and list."""
    coeffs = {}
    syms = []
    for i in range(D + 1):
        for j in range(i, D + 1):
            if i + j <= D:
                s = symbols(f'c_{i}_{j}')
                coeffs[(i, j)] = s
                coeffs[(j, i)] = s
                syms.append(s)
    return coeffs, syms


def build_f(coeffs, D):
    def f(a, b):
        e = 0
        for i in range(D + 1):
            for j in range(D + 1):
                if i + j <= D and (i, j) in coeffs:
                    e += coeffs[(i, j)] * a**i * b**j
        return e
    return f


def symbolic_classify(D):
    print("=" * 70)
    print(f"SYMBOLIC CLASSIFICATION, total degree D = {D}")
    print("=" * 70)
    coeffs, syms = make_coeffs(D)
    f = build_f(coeffs, D)

    for e in range(4):
        # unit constraint: f(x,e) - x == 0 identically in x
        unit_expr = expand(f(x, e) - x)
        unit_poly = Poly(unit_expr, x)
        unit_eqs = unit_poly.all_coeffs()

        # associativity
        assoc_expr = expand(f(f(x, y), z) - f(x, f(y, z)))
        assoc_poly = Poly(assoc_expr, x, y, z)
        assoc_eqs = list(assoc_poly.as_dict().values())

        eqs = [sp.Eq(v, 0) for v in unit_eqs + assoc_eqs if v != 0]

        try:
            sol = solve(eqs, syms, dict=True)
        except Exception as ex:
            sol = f"solve-error: {ex}"

        print(f"\n--- unit e = {e} ---")
        print(f"  #equations: {len(eqs)}")
        print(f"  solutions (over Q): {sol}")

        # Interpret: for each solution dict, express f
        if isinstance(sol, list):
            for s in sol:
                fexpr = expand(f(x, y).subs(s))
                free = sorted({str(v) for term in s.values()
                               for v in term.free_symbols} |
                              {str(sm) for sm in syms if sm not in s})
                print(f"    -> f(x,y) = {fexpr}   free params: {free}")


def brute_force(Dmax=3, crange=(0, 1, 2, 3), test_range=range(0, 7)):
    print("\n" + "=" * 70)
    print(f"BRUTE FORCE cross-check: c_ij in {crange}, i+j<={Dmax}, "
          f"eval on {{0..6}}^3")
    print("=" * 70)
    # symmetric index positions i<=j, i+j<=Dmax
    positions = [(i, j) for i in range(Dmax + 1) for j in range(i, Dmax + 1)
                 if i + j <= Dmax]
    print(f"free coeff positions (i<=j): {positions}  "
          f"({len(positions)} coeffs, {len(crange)**len(positions)} combos)")

    def evalf(cdict, a, b):
        tot = 0
        for (i, j), c in cdict.items():
            if c == 0:
                continue
            tot += c * a**i * b**j
            if i != j:
                tot += c * a**j * b**i
        return tot

    passing = []
    for combo in itertools.product(crange, repeat=len(positions)):
        cdict = {pos: v for pos, v in zip(positions, combo)}
        # find units e in 0..3 with f(x,e)=x on test range
        for e in range(4):
            if all(evalf(cdict, xv, e) == xv for xv in test_range):
                # check associativity on cube
                ok = True
                for a in test_range:
                    for b in test_range:
                        for cc in test_range:
                            if evalf(cdict, evalf(cdict, a, b), cc) != \
                               evalf(cdict, a, evalf(cdict, b, cc)):
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break
                if ok:
                    passing.append((tuple(sorted(cdict.items())), e))

    # group by unit
    from collections import defaultdict
    by_unit = defaultdict(list)
    for cd, e in passing:
        by_unit[e].append(cd)

    for e in sorted(by_unit):
        print(f"\n  unit e={e}:  {len(by_unit[e])} passing operations")
        for cd in by_unit[e]:
            nz = {pos: v for pos, v in cd if v != 0}
            print(f"    nonzero coeffs {nz}")


if __name__ == '__main__':
    for D in (2, 3, 4):
        symbolic_classify(D)
    brute_force(Dmax=3)
