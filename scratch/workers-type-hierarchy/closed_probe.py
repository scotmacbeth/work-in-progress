"""
Closed-structure probes.
(1) ⊗-closed sanity: ΔS⊗(r⊗p) == (ΔS⊗r)⊗p  (strict assoc)  -> currying out p is clean.
(2) ×-closed obstruction: compare counts
       N1 = |Cont( ΔS⊗(r×p), q)|             (the actual Workers hom  r×p ->_S q)
       N2 = |Cont( (ΔS⊗r)×p, q)|             (what 'same exponential q^p' would give)
    If N1 != N2 for some r, the naive ×-closure (with Cont's CCC exponential) fails:
    the state ΔS entangles with p, so it cannot be curried out.
"""
from containers import *
from itertools import product as iproduct

def count_morphisms(src, tgt):
    n=0
    shapes=src.shapes
    for fwd_t in iproduct(tgt.shapes, repeat=len(shapes)):
        fwd=dict(zip(shapes,fwd_t))
        ways=1; ok=True
        for sh in shapes:
            c=fwd[sh]; t=len(tgt.fib[c]); s=len(src.fib[sh])
            if t>0 and s==0: ok=False; break
            ways*= (s**t)
        if ok: n+=ways
    return n

def strict_eq(c1,c2):
    if sorted(map(str,c1.shapes))!=sorted(map(str,c2.shapes)): return False
    f1={str(a):sorted(map(str,c1.fib[a])) for a in c1.shapes}
    f2={str(a):sorted(map(str,c2.fib[a])) for a in c2.shapes}
    return f1==f2

if __name__=='__main__':
    S=['s0','s1']
    p=Cont(['a'],{'a':['b0','b1']})
    q=Cont(['c'],{'c':['d0','d1']})
    rs=[Cont(['r0'],{'r0':['x']}),
        Cont(['r0','r1'],{'r0':['x'],'r1':['y','z']}),
        Cont(['r0'],{'r0':[]})]
    print("(1) ⊗-assoc  ΔS⊗(r⊗p) == (ΔS⊗r)⊗p :")
    for r in rs:
        L=tensor(deltaS(S),tensor(r,p)); R=tensor(tensor(deltaS(S),r),p)
        print(f"    r={r.shapes}:  {strict_eq(L,R)}")
    print("(2) ×-closed naive-currying obstruction:")
    for r in rs:
        A=tensor(deltaS(S),prod(r,p))       # ΔS⊗(r×p)
        B=prod(tensor(deltaS(S),r),p)       # (ΔS⊗r)×p
        N1=count_morphisms(A,q); N2=count_morphisms(B,q)
        print(f"    r={r.shapes}:  |Work(r×p,q)|={N1}   |Cont((ΔS⊗r)×p,q)|={N2}   {'MATCH' if N1==N2 else 'DIFFER -> not ×-closed with q^p'}")
