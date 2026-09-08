from fractions import Fraction

# ---------- polynomial container arithmetic via generating functions ----------
# A container is given by a dict {num_positions: num_shapes_with_that_many_positions}
# Its extension cardinality function is P(y) = sum_j a_j y^j.
# Composition p<|q has extension P(Q(y)) (functor composition). We work with the
# cardinality FUNCTIONS (poly in y) which compose; this is exact for polynomial functors.

def poly_eval(coeffs, y):
    # coeffs: dict j->a_j ; evaluate at integer y
    return sum(a*(y**j) for j,a in coeffs.items())

def poly_compose_cardfun(P, Qval):
    # returns a function y-> P(Q(y)) given P dict and Qval a python function
    return lambda y: poly_eval(P, Qval(y))

# ---------- Part A sanity: M polynomial, r = p <| ceil(M) <| q reproduces composite ----------
# We verify at the level of cardinality FUNCTIONS that
#   comp(n) = |[[p]] o M o [[q]] o M (n)|  equals  |[[r]] o M (n)|
# where r's card-fun R(y) = P(Mgf(Q(y)))  (P,Q card funs of p,q; Mgf card fun of M).
# comp(n) = P( Mgf( Q( Mgf(n) ) ) ),  RHS = R(Mgf(n)) = P(Mgf(Q(Mgf(n)))).  Tautologically equal
# BUT the point is R has NONNEG INTEGER coeffs (r is a real container) exactly when M polynomial.

def card_funs():
    return {
        'Id':        lambda y: y,
        'Maybe':     lambda y: y+1,
        'Excep+2':   lambda y: y+2,
        'Writer2x':  lambda y: 2*y,
        'ReaderX^2': lambda y: y*y,
        'P+':        lambda y: 2**y - 1,
        'P':         lambda y: 2**y,
    }

# p = q = squaring: P(y)=Q(y)=y^2
def demo_partA():
    Mgf = lambda y: y+1  # Maybe
    P = {2:1}  # squaring: y^2
    Q = {2:1}
    Qval = lambda y: poly_eval(Q,y)
    Pval = lambda y: poly_eval(P,y)
    print("== Part A demo: M=Maybe, p=q=squaring ==")
    comps=[]
    for n in range(0,7):
        comp = Pval( Mgf( Qval( Mgf(n) ) ) )
        comps.append(comp)
    print("  comp(n), n=0..6:", comps)
    # r card fun: R(y) = P(Mgf(Q(y))) = ((y^2)+1)^2 = y^4+2y^2+1
    R = {4:1,2:2,0:1}
    rhs = [poly_eval(R, Mgf(n)) for n in range(0,7)]
    print("  R(Mgf(n)) with R=y^4+2y^2+1:", rhs)
    print("  match:", comps==rhs, " r-container shapes {pos:count}=",R)

demo_partA()

# ---------- Part B necessity: closure at p=q=Id  =>  m o m = R o m for a FIXED nonneg-int poly R ----------
# comp_Id(n) = |M(M(n))| = m(m(n)) ; must equal R(m(n)) for a fixed polynomial R.
# So on the set V=image(m), the function  v |-> m(v)  must agree with a fixed polynomial R.
def test_pqId(name, m, maxn=8):
    ns=list(range(0,maxn))
    ms=[m(n) for n in ns]
    mm=[m(m(n)) for n in ns]  # = comp at p=q=Id
    # Need a fixed poly R with R(m(n))=m(m(n)). Interpolate through (m(n),m(m(n))) using
    # first k DISTINCT m-values, then check it predicts the rest with nonneg int coeffs.
    pts=[]
    seen={}
    for n in ns:
        v=ms[n]; w=mm[n]
        if v in seen:
            if seen[v]!=w:
                return (name, False, "m(v) not even well-defined as function of v (m not injective inconsistent)")
        seen[v]=w
        pts.append((v,w))
    xs=sorted(seen); 
    # try increasing degree fits
    def interp(xsub,ysub):
        k=len(xsub)
        A=[[Fraction(xsub[i])**j for j in range(k)]+[Fraction(ysub[i])] for i in range(k)]
        for col in range(k):
            piv=next((r for r in range(col,k) if A[r][col]!=0),None)
            if piv is None: continue
            A[col],A[piv]=A[piv],A[col]; pv=A[col][col]
            A[col]=[x/pv for x in A[col]]
            for r in range(k):
                if r!=col and A[r][col]!=0:
                    f=A[r][col]; A[r]=[a-f*b for a,b in zip(A[r],A[col])]
        return [A[i][k] for i in range(k)]
    xl=sorted(seen)
    for f in range(2,len(xl)+1):
        xsub=xl[:f]; ysub=[seen[x] for x in xsub]
        if len(set(xsub))<len(xsub): continue
        c=interp(xsub,ysub)
        ev=lambda x,c=c: sum(cj*Fraction(x)**j for j,cj in enumerate(c))
        ok=all(ev(x)==seen[x] for x in xl)
        intnn=all(cj.denominator==1 and cj>=0 for cj in c)
        if ok and intnn:
            cc=[int(x) for x in c]
            while cc and cc[-1]==0: cc.pop()
            return (name, True, f"m|im(m) = fixed poly R coeffs {cc}")
    return (name, False, f"no fixed nonneg-int poly R fits m|im(m); m(n)={ms}, m(m(n))={mm}")

print("\n== Part B: necessity test at p=q=Id (m o m = R o m ?) ==")
for name,m in card_funs().items():
    r=test_pqId(name,m)
    print(f"  {'PASS' if r[1] else 'FAIL'}  {name:9s} : {r[2]}")

# Growth witness for P+: m(m(n)) doubly exponential vs R(m(n)) poly
print("\n== P+ growth witness (digit counts of m(m(n))) ==")
m=lambda y:2**y-1
for n in range(0,7):
    v=m(m(n))
    print(f"  n={n}: m(n)={m(n)}, m(m(n)) has {len(str(v))} digits")
