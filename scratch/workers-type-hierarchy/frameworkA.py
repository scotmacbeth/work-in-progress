"""
Framework A (grade-tensoring / Para): the monoidal-actegory comparison
    Phi^*_{S,T}:  Δ(S×T) ⊗ (p ⋆ q)  ->  (ΔS ⊗ p) ⋆ (ΔT ⊗ q)
We need THIS direction to make Para/graded-Workers monoidal (to tensor two
workers of grades S and T into one of grade S×T).
Test existence of a natural candidate and whether it is iso; also the reverse.
"""
from containers import *
from test_maps import small_conts

def SxT(S,T): return [(s,t) for s in S for t in T]

# ---- ⋆ = ⊗ : Phi : Δ(S×T)⊗(p⊗q) -> (ΔS⊗p)⊗(ΔT⊗q) ----
def phi_tensor(S,T,p,q):
    ST=SxT(S,T)
    L=tensor(deltaS(ST), tensor(p,q))      # shape ((s,t),(a,c)); fib ST×(Ba×Dc)
    R=tensor(tensor(deltaS(S),p), tensor(deltaS(T),q)) # shape ((s,a),(t,c)); fib (S×Ba)×(T×Dc)
    fwd={}; bwd={}
    for sh in L.shapes:
        (s,t),(a,c)=sh
        tgt=((s,a),(t,c)); fwd[sh]=tgt
        d={}
        for pos in R.fib[tgt]:      # ((sp,b),(tq,dd))
            (sp,b),(tq,dd)=pos
            d[pos]=((sp,tq),(b,dd)) # send to ST×(Ba×Dc)
        bwd[sh]=d
    return Mor(L,R,fwd,bwd)

# ---- ⋆ = × : need Δ(S×T)⊗(p×q) -> (ΔS⊗p)×(ΔT⊗q). backward must fabricate a grade. ----
def phi_prod(S,T,p,q):
    ST=SxT(S,T)
    L=tensor(deltaS(ST), prod(p,q))        # fib ST×(Ba+Dc)
    R=prod(tensor(deltaS(S),p), tensor(deltaS(T),q)) # fib (S×Ba)+(T×Dc)
    fwd={}; bwd={}
    for sh in L.shapes:
        (s,t),(a,c)=sh
        tgt=((s,a),(t,c)); fwd[sh]=tgt
        d={}
        for pos in R.fib[tgt]:      # ('l',(sp,b)) or ('r',(tq,dd))
            side,(g,x)=pos
            # need element ((?,?),(side,x)) in ST×(Ba+Dc): must supply BOTH s- and t- comp
            if side=='l':
                # have sp (=g in S), need a t: FABRICATE -> use base t (the shape's t)
                d[pos]=((g,t),('l',x))
            else:
                d[pos]=((s,g),('r',x))   # g in T, fabricate s from base
        bwd[sh]=d
    return Mor(L,R,fwd,bwd)

# ---- ⋆ = + : Δ(S×T)⊗(p+q) -> (ΔS⊗p)+(ΔT⊗q) ----
def phi_coprod(S,T,p,q):
    ST=SxT(S,T)
    L=tensor(deltaS(ST), coprod(p,q))      # shape ((s,t),('l',a)); fib ST×Ba
    R=coprod(tensor(deltaS(S),p), tensor(deltaS(T),q))
    fwd={}; bwd={}
    for sh in L.shapes:
        (s,t),cs=sh; side,x=cs
        if side=='l': tgt=('l',(s,x))
        else:         tgt=('r',(t,x))
        fwd[sh]=tgt
        d={}
        for pos in R.fib[tgt]:   # (g,b) with g a single grade (S or T)
            g,b=pos
            if side=='l': d[pos]=((g,t),b)   # fabricate t from base
            else:         d[pos]=((s,g),b)   # fabricate s from base
        bwd[sh]=d
    return Mor(L,R,fwd,bwd)

if __name__=='__main__':
    S=['s0','s1']; T=['t0','t1','t2']
    conts=small_conts()
    for name,fn in [('⊗',phi_tensor),('×',phi_prod),('+',phi_coprod)]:
        allvalid=True; alliso=True
        for p in conts:
            for q in conts:
                m=fn(S,T,p,q); ok,msg=m.validate()
                if not ok: allvalid=False; print(f"  {name} INVALID: {msg}")
                else:
                    if not m.is_iso(): alliso=False
        print(f"Framework A  Phi^{name}: {'all valid' if allvalid else 'INVALID'}, "
              f"{'ISO (strong)' if alliso else 'non-iso (lax/oplax only)'}")
