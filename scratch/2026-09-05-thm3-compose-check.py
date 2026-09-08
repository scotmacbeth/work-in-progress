# THM 3: do M-containers compose?
# Structural fact: [[p]]_M o [[q]]_M (X) = [[p]](M([[q]](MX))) = G(MX)
#   where G = [[p]] o M o [[q]]  (a functor Set->Set).
# Composite is an M-container extension [[r]]_M = [[r]] o M  iff G is a POLYNOMIAL functor.
# For ALL p,q  <=>  M itself is a polynomial functor (poly closed under composition).
#
# TEST (finite counting): take p = q = squaring container, [[q]](Y)=Y^2.
#   composite(X) = ( M( (MX)^2 ) )^2 .  With |X|=n, u=mc(n)=|M(n-set)|:
#   composite_n = mc(u^2)^2 .
#   Candidate [[r]]_M(X) = [[r]](MX) = sum_j a_j * u^j  (a_j = # shapes of r with j positions).
#   So M-containers compose (for this p,q) iff  n |-> mc(mc(n)^2)^2  fits  P(mc(n))
#   for a FIXED nonneg-integer-coeff polynomial P.

from fractions import Fraction

def mc_table(mc, ns):
    return [mc(n) for n in ns]

def composite_vals(mc, ns):
    out=[]
    for n in ns:
        u = mc(n)
        out.append(mc(u*u)**2)
    return out

def interp_poly(xs, ys):
    # Lagrange interpolation, return coeffs (as Fractions) of unique deg<=len-1 poly
    # then we check integrality / nonneg / that a lower-degree fit works.
    m=len(xs)
    # Build Vandermonde solve
    # coeffs c[0..m-1] with sum c_j x^j = y
    # Gaussian elimination over Fractions
    A=[[Fraction(xs[i])**j for j in range(m)]+[Fraction(ys[i])] for i in range(m)]
    for col in range(m):
        piv=None
        for r in range(col,m):
            if A[r][col]!=0: piv=r;break
        if piv is None: continue
        A[col],A[piv]=A[piv],A[col]
        pv=A[col][col]
        A[col]=[x/pv for x in A[col]]
        for r in range(m):
            if r!=col and A[r][col]!=0:
                f=A[r][col]
                A[r]=[a-f*b for a,b in zip(A[r],A[col])]
    return [A[i][m] for i in range(m)]

def fits_fixed_poly(mc, name, maxn=12):
    ns=list(range(0,maxn))
    us=[mc(n) for n in ns]
    comps=composite_vals(mc, ns)
    # Use the first k points to fit a polynomial in u, then test remaining points.
    # If M polynomial of "degree" d in mc, composite is poly in u of some fixed degree;
    # try increasing fit-degree; require it to PREDICT all further points AND have
    # nonneg integer coeffs (container structure).
    print(f"--- {name} ---")
    print("  n :", ns)
    print("  u=mc(n):", us)
    print("  composite = mc(u^2)^2:", comps)
    # try fit using first f points, predict the rest, for f=2..len
    good=None
    for f in range(2, len(ns)+1):
        xs=us[:f]; ys=comps[:f]
        if len(set(xs))<len(xs):
            continue
        coeffs=interp_poly(xs,ys)
        # evaluate on all points
        def ev(x):
            s=Fraction(0)
            for j,c in enumerate(coeffs):
                s+=c*Fraction(x)**j
            return s
        ok=all(ev(us[i])==comps[i] for i in range(len(ns)))
        integer_nonneg=all((c.denominator==1 and c>=0) for c in coeffs)
        if ok and integer_nonneg:
            good=(f,coeffs); break
    if good:
        f,coeffs=good
        cc=[int(c) for c in coeffs]
        # trim trailing zeros
        while cc and cc[-1]==0: cc.pop()
        print(f"  => FITS fixed polynomial P (from {f} pts), coeffs a_j = {cc}  => COMPOSES")
        print(f"     r has shapes: " + ", ".join(f"{a}x(pos={j})" for j,a in enumerate(cc) if a))
    else:
        print("  => NO fixed nonneg-int polynomial fits => DOES NOT COMPOSE")
    return good is not None

monads = {
    "Id (poly)":            lambda k: k,
    "Maybe X+1 (poly,nonaffine)": lambda k: k+1,
    "Exception X+2 (poly)": lambda k: k+2,
    "Writer 2*X (poly)":    lambda k: 2*k,
    "Reader X^2 (poly,affine,comm)": lambda k: k*k,
    "P+ nonempty powerset (affine,comm,NONpoly)": lambda k: 2**k - 1,
    "P full powerset (nonaffine,comm,NONpoly)":   lambda k: 2**k,
}
results={}
for name,mc in monads.items():
    results[name]=fits_fixed_poly(mc,name)
print("\n==== SUMMARY ====")
for name,r in results.items():
    print(f"  {'COMPOSES' if r else 'FAILS   '}  {name}")
