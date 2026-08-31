"""
Task 2 + minimal arity-2 witness: test explicit candidate cardinality-operations
F(x,b)=|X star B| for unit law (F(e,b)=b), symmetry, and associativity
F(F(a,b),c)=F(a,F(b,c)). Report first failing triple. Also report the
per-variable 'arity' (degree of F in x, i.e. does R_b grow like x^2?).
"""

def first_assoc_fail(F, grid=range(0,7)):
    for a in grid:
        for b in grid:
            fab=F(a,b)
            for c in grid:
                lhs=F(fab,c); rhs=F(a,F(b,c))
                if lhs!=rhs:
                    return (a,b,c,lhs,rhs)
    return None

def unit_check(F, e, grid=range(0,7)):
    bad=[b for b in grid if F(e,b)!=b or F(b,e)!=b]
    return bad

def sym_check(F, grid=range(0,7)):
    bad=[(a,b) for a in grid for b in grid if F(a,b)!=F(b,a)]
    return bad

def arity_of_Rb(F, b, xs=range(0,6)):
    # fit growth in x: second finite difference > 0 => degree>=2
    vals=[F(x,b) for x in xs]
    d2=[vals[i+2]-2*vals[i+1]+vals[i] for i in range(len(vals)-2)]
    return vals, d2, any(v!=0 for v in d2)

CANDS = {
  # minimal symmetric arity-2 (unit 0): x+b+x^2 b + x b^2
  "min_arity2  x+b+x^2 b+x b^2": (lambda x,b: x+b+x*x*b+x*b*b, 0),
  # x + b + x^2 b^2 (symmetric, arity 2, unit 0)
  "x+b+x^2 b^2": (lambda x,b: x+b+x*x*b*b, 0),
  # unit-1 attempt with square: x*b + (x*b)^2 ? unit1 needs F(1,b)=b -> b + b^2 !=b fails; skip
  # X x List(B): x*(1+b+b^2+...) truncated is infinite; test finite geom won't be exact.
  # coproduct baseline (arity<=1): x+b unit0
  "coproduct x+b": (lambda x,b: x+b, 0),
  # product baseline (arity<=1): x*b unit1
  "product x*b": (lambda x,b: x*b, 1),
  # vee_S with S=2: x+b+2xb unit0
  "vee_2 x+b+2xb": (lambda x,b: x+b+2*x*b, 0),
  # 'both squared and linear' x+b+xb+x^2 b^2
  "x+b+xb+x^2b^2": (lambda x,b: x+b+x*b+x*x*b*b, 0),
  # additive with square only on diagonal-ish: x+b+ (xb)^2
  "x+b+(xb)^2": (lambda x,b: x+b+(x*b)**2, 0),
}

if __name__=="__main__":
    for name,(F,e) in CANDS.items():
        print("="*60)
        print("CANDIDATE:", name, " unit e=",e)
        bad_e=unit_check(F,e)
        bad_s=sym_check(F)
        print("  unit fails at b=", bad_e if bad_e else "OK")
        print("  symmetry fails at", bad_s[:3] if bad_s else "OK")
        # arity: does R_2 grow quadratically?
        for b in (1,2,3):
            vals,d2,q=arity_of_Rb(F,b)
            print(f"  R_{b}(x) for x=0..5: {vals}  2nd-diff:{d2}  arity>=2:{q}")
        af=first_assoc_fail(F)
        if af is None:
            print("  ASSOCIATIVITY: holds on grid 0..6  <<< SURVIVES")
        else:
            a,b,c,l,r=af
            print(f"  ASSOC FAILS first at (a,b,c)=({a},{b},{c}): (a*b)*c={l} vs a*(b*c)={r}")
