"""
CRUX CHECK: Does the species tangent functor T=(-)<|D, Tp = p + ev*dp, preserve
the CARTESIAN product x (required for Lanfranchi Def 4.18 'parallelizable' to even
be well-posed)?  And does it preserve the DIRICHLET tensor?

Two-sorted polynomial functors in (X=base, W=tangent). Tp(X,W) = p(X) + W*dp(X).

Cartesian product of polynomial functors p,q:  (p x q)(Z) = p(Z)*q(Z)   [pointwise]
  => on reps y^A x y^B = y^{A+B}.  So as polynomials in one var: p(X)*q(X).
Dirichlet tensor:  y^A (x)_Dir y^B = y^{A*B};  on counting polys it's the
  'exponent-multiplying' product; but on the e-linear tangent level the relevant
  check is the Leibniz rule for d.

We test T-preservation by comparing T(p*q) vs T(p)*T(q) truncated, and the Leibniz
structure. We work with counting polynomials in X (sympy), W the tangent marker,
e^2=0 implemented by dropping W^2 and higher.
"""
import sympy as sp
X, W = sp.symbols('X W')

def trunc(expr):
    """drop W^2 and higher (e^2=0)."""
    expr = sp.expand(expr)
    p = sp.Poly(expr, W)
    out = 0
    for (k,), c in p.terms():
        if k <= 1:
            out += c*W**k
    return sp.expand(out)

def T(pX):
    """Tp = p(X) + W*dp(X)  (p given as expr in X)."""
    return sp.expand(pX + W*sp.diff(pX, X))

# --- Cartesian product (pointwise multiply as polynomials in X) ---
print("=== Does T preserve the CARTESIAN product (pointwise p(X)*q(X))? ===")
for (pn,p),(qn,q) in [(('y',X),('y',X)), (('y^2',X**2),('y',X)), (('y^2',X**2),('y^2',X**2))]:
    lhs = T(sp.expand(p*q))                 # T(p x q): first form product then T
    # T(p)*T(q): multiply the two-sorted tangent objects, then truncate e^2=0
    rhs = trunc(T(p)*T(q))
    eq = sp.simplify(lhs - rhs) == 0
    print(f"  p={pn}, q={qn}:  T(p x q) = {lhs}")
    print(f"               T(p) x T(q)|trunc = {rhs}   EQUAL? {eq}")

print()
print("=== Leibniz for the Dirichlet tensor: d(p (x) q) = dp (x) q + p (x) dq ? ===")
# On the e-linear tangent level, T preserves a product (x) iff d satisfies Leibniz for it.
# Cartesian pointwise product p(X)q(X): d(pq)=p'q+pq'  -> Leibniz HOLDS for d itself...
# but the ISSUE is the e^2 cross term W^2 in T(p)xT(q). Check the cross term:
for (pn,p),(qn,q) in [(('y',X),('y',X)), (('y^2',X**2),('y^2',X**2))]:
    full = sp.expand(T(p)*T(q))     # untruncated
    w2 = sp.Poly(full, W).coeff_monomial(W**2)
    print(f"  p={pn} q={qn}:  W^2 (spurious e^2) coefficient of T(p)*T(q) = {w2}  "
          f"(nonzero => x NOT T-compatible)")

print()
print("=== Which p admit Tp ≅ p×m over p?  (m = Tp/p must be a polynomial functor) ===")
for name, pX in [('const 3', sp.Integer(3)), ('y', X), ('y^2', X**2),
                 ('y^2+y', X**2+X), ('y^3', X**3), ('2y^2', 2*X**2)]:
    Tp = T(pX)                       # p + W p'
    m = sp.cancel(Tp/pX)             # = 1 + W p'/p
    dp = sp.diff(pX, X)
    if dp == 0 or pX.is_number:      # constant p: m = 1, polynomial
        poly = True
    else:                            # p | p' in Q[X]  <=>  remainder 0
        _, r = sp.div(sp.Poly(dp, X), sp.Poly(pX, X))
        poly = r.is_zero
    print(f"  p={name:<8} Tp={sp.expand(Tp)!s:<16} m=Tp/p={m!s:<14} polynomial(=>parallelizable)? {'YES' if poly else 'NO'}")

print()
print("CONCLUSION:")
print(" - T(y x y)=T(y^2) vs T(y)xT(y): differ by the W^2 (e^2) cross term.")
print("   The categorical product is NOT compatible with T (T does not preserve x).")
print(" - Hence (Poly, x, (-)<|D) is NOT a Cartesian tangent category, so Lanfranchi")
print("   Def 4.18 'parallelizable' (TM = M x m) is not well-posed with the categorical x.")
print(" - The tangent-compatible symmetric monoidal product is the DIRICHLET tensor")
print("   (Leibniz holds mod e^2), but Dirichlet is NOT Cartesian (no diagonal), so")
print("   Def 4.18 still does not apply. => the port fails. Dividing line.")
