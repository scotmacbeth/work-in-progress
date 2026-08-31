"""
Test the framework-B oplax comonoidal comparison maps
    n^*_S : ΔS ⊗ (p ⋆ q)  ->  (ΔS ⊗ p) ⋆ (ΔS ⊗ q)
for ⋆ in {+, ×, ⊗, ◁}, over small S, p, q.
Report: is the natural candidate a valid container morphism? is it iso?
Also test the reverse (lax) direction where relevant.
"""
from containers import *

def small_conts():
    # a few tiny containers p=(A,B)
    p1 = Cont(['a'], {'a':['b0']})               # y-like but fibre size1
    p2 = Cont(['a'], {'a':['b0','b1']})          # one shape, 2 positions
    p3 = Cont(['a0','a1'], {'a0':['b'], 'a1':[]})# two shapes incl empty fibre
    return [p1,p2,p3]

def test_coprod(S,p,q):
    L = tensor(deltaS(S), coprod(p,q))
    R = coprod(tensor(deltaS(S),p), tensor(deltaS(S),q))
    fwd={}; bwd={}
    for sh in L.shapes:
        s, cs = sh              # cs = ('l',a) or ('r',c)
        side, x = cs
        tgt = (side,(s,x))
        fwd[sh]=tgt
        bwd[sh]={}
        for pos in R.fib[tgt]:  # pos=(sp,b)
            bwd[sh][pos]=pos
    m=Mor(L,R,fwd,bwd)
    return m

def test_prod(S,p,q):
    L = tensor(deltaS(S), prod(p,q))
    R = prod(tensor(deltaS(S),p), tensor(deltaS(S),q))
    fwd={}; bwd={}
    for sh in L.shapes:
        s,(a,c)=sh
        tgt=((s,a),(s,c))       # diagonal
        fwd[sh]=tgt
        bwd[sh]={}
        for pos in R.fib[tgt]:  # ('l',(sp,b)) or ('r',(sp,d))
            side,(sp,x)=pos
            bwd[sh][pos]=(sp,(side,x))
    return Mor(L,R,fwd,bwd)

def test_tensor(S,p,q, merge='left'):
    L = tensor(deltaS(S), tensor(p,q))
    R = tensor(tensor(deltaS(S),p), tensor(deltaS(S),q))
    fwd={}; bwd={}
    for sh in L.shapes:
        s,(a,c)=sh
        tgt=((s,a),(s,c))       # diagonal on shapes
        fwd[sh]=tgt
        bwd[sh]={}
        for pos in R.fib[tgt]:  # ((sp1,b),(sp2,d))
            (sp1,b),(sp2,d)=pos
            sp = sp1 if merge=='left' else sp2
            bwd[sh][pos]=(sp,(b,d))
    return Mor(L,R,fwd,bwd)

def test_lhd(S,p,q, statepol='copy'):
    L = tensor(deltaS(S), lhd(p,q))
    R = lhd(tensor(deltaS(S),p), tensor(deltaS(S),q))
    fwd={}; bwd={}
    for sh in L.shapes:
        s,(a,gamma)=sh          # gamma tuple over p.fib[a]
        Ba = p.fib[a]
        # Build Gamma: (S×Ba) -> (S×C).  index positions of tensor(deltaS,p) at (s,a) = S×Ba
        # Gamma(sp,b) = (sp, gamma_at_b)   [state = sp, C-shape from gamma]
        # need Gamma expressed as a tuple over positions of (ΔS⊗p).fib[(s,a)]
        src_positions = tensor(deltaS(S),p).fib[(s,a)]  # list of (sp,b)
        # map each (sp,b) to a target C-shape of (ΔS⊗q) = (S×C) shape (sq,c)
        Gamma=[]
        for (sp,b) in src_positions:
            i = Ba.index(b)
            c = gamma[i]
            Gamma.append((sp, c))   # (state=sp, C-shape=c)
        Gamma=tuple(Gamma)
        tgt = ((s,a), Gamma)
        if tgt not in R.shapes:
            return ('MISSING_SHAPE', tgt)
        fwd[sh]=tgt
        bwd[sh]={}
        for pos in R.fib[tgt]:
            # pos = ((sp,b),(sq,d))
            (sp,b),(sq,d)=pos
            # LHS position: (state, (b,d)) with state in S
            st = sp    # policy: take the p-side state
            bwd[sh][pos]=(st,(b,d))
    return Mor(L,R,fwd,bwd)

if __name__=='__main__':
    S=['s0','s1']
    conts=small_conts()
    print("=== ⋆ = +  (coproduct) ===")
    for p in conts:
        for q in conts:
            m=test_coprod(S,p,q); ok,msg=m.validate()
            print(f"  valid={ok} iso={m.is_iso() if ok else '-'}  {msg if not ok else ''}")
    print("=== ⋆ = ×  (product) ===")
    for p in conts:
        for q in conts:
            m=test_prod(S,p,q); ok,msg=m.validate()
            print(f"  valid={ok} iso={m.is_iso() if ok else '-'}  {msg if not ok else ''}")
    print("=== ⋆ = ⊗  (Dirichlet), merge=left (NO monoid) ===")
    for p in conts:
        for q in conts:
            m=test_tensor(S,p,q,'left'); ok,msg=m.validate()
            print(f"  valid={ok} iso={m.is_iso() if ok else '-'}  {msg if not ok else ''}")
    print("=== ⋆ = ◁  (substitution), state policy = p-side ===")
    for p in conts:
        for q in conts:
            r=test_lhd(S,p,q)
            if isinstance(r,tuple):
                print(f"  {r[0]}: {r[1]}"); continue
            ok,msg=r.validate()
            print(f"  valid={ok} iso={r.is_iso() if ok else '-'}  {msg if not ok else ''}")
