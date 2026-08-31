import sympy as sp
m,n,k,S = sp.symbols('m n k S', nonnegative=True)

# Growth/associativity obstruction for a "degree-2 extra" unit-initial candidate:
#   A * B := A + Sym2(A)*B + B ,  |Sym2(A)| = m(m+1)/2
def star_card(a,b):
    return a + sp.Rational(1,2)*a*(a+1)*b + b
lhs = star_card(star_card(m,n),k)   # (A*B)*C
rhs = star_card(m, star_card(n,k))  # A*(B*C)
print("degree-2 extra: (A*B)*C - A*(B*C) as poly in m:")
diff = sp.expand(lhs-rhs)
print("  leading m-degree LHS:", sp.degree(sp.Poly(sp.expand(lhs),m)))
print("  leading m-degree RHS:", sp.degree(sp.Poly(sp.expand(rhs),m)))
print("  difference not identically zero:", sp.simplify(diff)!=0)

# Contrast: affine ∨_S  A*B = A + m*S*n + B  => (1+S n) m + n
def vs_card(a,b): return a + a*S*b + b
lhs2 = vs_card(vs_card(m,n),k); rhs2 = vs_card(m, vs_card(n,k))
print("\n∨_S (affine) associativity holds at cardinality level:",
      sp.simplify(sp.expand(lhs2-rhs2))==0)

# max monoid: associative at cardinality level (sanity)
print("\nmax is an associative unital(0) monoid on N: max(max(m,n),k)=max(m,max(n,k)) trivially true.")
# 'max(n,c)' is NOT a N-combination of powers:
import itertools
def is_card_poly(vals):  # vals: list f(0),f(1),...,f(N); can it be sum of n^{k_i} with N-coeffs?
    # try small: coefficients c0..c3 (# of exponent-0,1,2,3 terms), nonneg ints
    N=len(vals)-1
    for c in itertools.product(range(6),repeat=4):
        ok=all(sum(c[e]*(x**e) for e in range(4))==vals[x] for x in range(N+1))
        if ok: return c
    return None
maxc2=[max(x,2) for x in range(4)]
print("max(n,2) for n=0..3:", maxc2, "-> N-combo of powers?", is_card_poly(maxc2))
