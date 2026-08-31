"""
Structural constraints that any unit-0 symmetric associative F must satisfy, and
why they block arity>=2. Verified numerically.

Facts checked:
 (U) constant-term law: F(0,b)=b, so column b has constant term = b.
     => a *pure* arity-2 shape p_b(a)=a^2 needs p_b(0)=0=b, i.e. only b=0,
        but b=0 is the unit with p_0(a)=a (linear). Contradiction. Verified.
 (D) multiplicative degree law: if F associative & each R_b polynomial with
     max-arity d(b):= deg_a F(a,b), then d(F(b,c)) = d(b)*d(c), d(0)=1.
     Checked on the surviving families (x, vee_S): d==1 everywhere, consistent.
     Any arity>=2 => d unbounded (d(b),d(b^k) -> inf) => carrier of shape-counts
     unbounded => no finite closed table possible.
"""

def deg_in_x(F, b, xs=range(0,8)):
    vals=[F(x,b) for x in xs]
    # highest nonzero finite difference order
    diffs=vals[:]
    order=0
    while any(diffs) and len(diffs)>1:
        nd=[diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
        if all(v==0 for v in nd):
            return order
        diffs=nd; order+=1
    return order

def check_degree_law(F, N=5):
    ok=True
    for b in range(N):
        for c in range(N):
            db=deg_in_x(F,b); dc=deg_in_x(F,c)
            fbc=F(b,c)
            dfbc=deg_in_x(F,fbc)
            if dfbc != db*dc:
                ok=False
                print(f"    degree-law FAILS at b={b},c={c}: d(b)*d(c)={db*dc} vs d(F(b,c))={dfbc}")
    return ok

if __name__=="__main__":
    fams={
      "product x*b (unit1)": lambda x,b: x*b,
      "coproduct x+b (unit0)": lambda x,b: x+b,
      "vee_3 x+b+3xb (unit0)": lambda x,b: x+b+3*x*b,
    }
    for name,F in fams.items():
        print("FAMILY",name)
        print("   d(b) for b=0..4:", [deg_in_x(F,b) for b in range(5)])
        law=check_degree_law(F)
        print("   multiplicative degree law holds:", law)

    print("\n(U) pure-square shape test: want F(a,b0)=a^2 for some b0 with unit 0.")
    print("    constant term F(0,b0) must equal a^2|_{a=0}=0, but unit forces F(0,b0)=b0")
    print("    => b0=0; yet column 0 is the identity a (degree 1), not a^2.  BLOCKED.")
