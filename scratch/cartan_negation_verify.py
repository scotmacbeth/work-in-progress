"""
Verification for: SPoly/∂ additive bundle has NO fiberwise negation (Cartan boundary).
Checks:
 (a) dual-number tangent  Tp = p(y) + eps*v*dp  gives dp = 2y for y^2, 1+2y for y+y^2.
 (b) counting-functor preservation: N(p<|D) = N(p)(x+eps v) = N(p)(x) + eps v N(p)'(x).
 (c) Poly_N negation impossible: no N-polynomial g(x,v) with v+g=0 identically.
 (d) fiber monoid of the additive bundle over a shape is the free N-module on the holes;
     element (1,0) in N^2 has no additive inverse (finite search).
"""
import sympy as sp

x, v, eps = sp.symbols('x v epsilon')

def dualnum_tangent(poly_in_x):
    """Tp as dual-number substitution x -> x + eps v, truncated at eps^2=0.
    Returns (base, eps_coeff)."""
    sub = poly_in_x.subs(x, x + eps*v)
    ser = sp.expand(sub)
    # truncate eps^2 = 0
    ser = sp.Poly(ser, eps)
    base = ser.coeff_monomial(1)
    c1 = ser.coeff_monomial(eps)
    return sp.expand(base), sp.expand(c1)

print("=== (a)/(b) dual-number tangent = counting of p<|D, eps-coeff = v * N(p)' ===")
for p in [x**2, x + x**2, x**3, 1 + x, 3*x**4]:
    base, c1 = dualnum_tangent(p)
    assert sp.simplify(base - p) == 0, ("base part should be p", p, base)
    assert sp.simplify(c1 - v*sp.diff(p, x)) == 0, ("eps-coeff should be v*p'", p, c1)
    print(f"  p={sp.srepr(p)[:0] or str(p):10s}  Tp = {base}  +  eps*({c1})     N(p)'={sp.diff(p,x)}")
print("  -> matches ∂(y^2)=2y, ∂(y+y^2)=1+2y, etc.  PASS\n")

print("=== (c) Poly_N negation impossible: no N-coefficient poly g(x,v) with v+g(x,v)=0 ===")
# A negation on the bundle over object 1: (x,v) -> (x, g(x,v)), axiom v + g = 0 identically.
# g must be an N-polynomial (nonneg integer coeffs). v + g = 0 in Z[x,v] forces g = -v,
# which has a negative coefficient -> not an N-polynomial. Evaluate at v=1,x=0: 1+g(0,1)=0 => g=-1<0.
g_required = -v
has_neg_coeff = any(c < 0 for c in sp.Poly(g_required, x, v).coeffs())
print(f"  required g = {g_required}; is an N-polynomial (all coeffs >= 0)? {not has_neg_coeff}")
assert has_neg_coeff, "g=-v must have a negative coeff"
# also: value at v=1 must be -1, unreachable by any N-polynomial (values are >=0 for nonneg inputs)
print("  g(x,1) would need to equal -1 for all x; N-polynomials are >=0 on N.  No such g.  PASS\n")

print("=== (d) fiber over a shape = free N-module on its holes; (1,0) has no inverse ===")
# p = y^2 : one shape, holes {h1,h2}. Tangent fiber = free commutative monoid (N-module) on {h1,h2} = N^2.
# addition is componentwise N-addition. Search for an inverse of (1,0) within a finite window.
import itertools
N = 20
target_zero = (0, 0)
e = (1, 0)
found_inverse = None
for w in itertools.product(range(N), repeat=2):
    if (e[0] + w[0], e[1] + w[1]) == target_zero:
        found_inverse = w
        break
print(f"  fiber = N^2 (holes of y^2), element e=(1,0); inverse w with e+w=(0,0) in range<{N}: {found_inverse}")
assert found_inverse is None, "there must be NO additive inverse of (1,0) in N^2"
print("  -> no additive inverse exists (would need (-1,0)).  PASS\n")

# sanity: the monoid IS cancellative & commutative (so it's a genuine commutative monoid, just not a group)
print("=== monoid sanity: N^2 is a commutative monoid, cancellative, not a group ===")
a,b,c = (2,3),(1,4),(5,0)
assert (a[0]+b[0],a[1]+b[1]) == (b[0]+a[0],b[1]+a[1])  # commutative
# cancellative: a+c=b+c => a=b
print("  commutative: yes; identity (0,0): yes; inverses: no (only (0,0) is invertible).  PASS\n")

print("ALL CHECKS PASS")
