"""
Framework A for ◁:  Phi^◁ : Δ(S×T) ⊗ (p◁q) -> (ΔS⊗p) ◁ (ΔT⊗q).
Outer container gets grade S, inner gets grade T; the base Δ(S×T) supplies both,
so NO state-merge is needed.  Test existence + iso.
"""
from containers import *
from test_maps import small_conts

def SxT(S,T): return [(s,t) for s in S for t in T]

def phi_lhd(S,T,p,q):
    ST=SxT(S,T)
    L=tensor(deltaS(ST), lhd(p,q))               # shape ((s,t),(a,gamma)); fib ST × Σ_b D(gamma b)
    R=lhd(tensor(deltaS(S),p), tensor(deltaS(T),q))
    # R: outer=ΔS⊗p=(S×A,(s,a)->S×Ba); inner=ΔT⊗q=(T×C,(t,c)->T×Dc)
    # R shape = ((s,a), Γ: S×Ba -> T×C).  position ((sp,b),(tq,d)).
    fwd={}; bwd={}
    for sh in L.shapes:
        (s,t),(a,gamma)=sh
        Ba=p.fib[a]
        outer=tensor(deltaS(S),p)                 # (S×A, ...)
        src_positions=outer.fib[(s,a)]            # list of (sp,b), sp in S, b in Ba
        # Γ(sp,b) = (t, gamma(b))  -- inner state taken from base t
        Gamma=[]
        for (sp,b) in src_positions:
            i=Ba.index(b); c=gamma[i]
            Gamma.append((t,c))
        Gamma=tuple(Gamma)
        tgt=((s,a),Gamma)
        if tgt not in R.shapes:
            return ('MISSING',tgt)
        fwd[sh]=tgt
        d={}
        for pos in R.fib[tgt]:      # ((sp,b),(tq,dd))
            (sp,b),(tq,dd)=pos
            # LHS position: ((s',t'),(b,dd)) in ST × Σ_b D(gamma b).
            #   take s'=sp (outer state), t'=tq (inner state) -> NO merge!
            d[pos]=((sp,tq),(b,dd))
        bwd[sh]=d
    return Mor(L,R,fwd,bwd)

if __name__=='__main__':
    S=['s0','s1']; T=['t0','t1']
    allvalid=True; alliso=True; details=[]
    for p in small_conts():
        for q in small_conts():
            m=phi_lhd(S,T,p,q)
            if isinstance(m,tuple):
                allvalid=False; details.append(('MISSING',m[1])); continue
            ok,msg=m.validate()
            if not ok: allvalid=False; details.append(('INVALID',msg))
            else:
                iso=m.is_iso()
                if not iso: alliso=False
                details.append(('ok','iso' if iso else 'non-iso'))
    print(f"Framework A  Phi^◁ : {'all valid' if allvalid else 'PROBLEM'}, "
          f"{'ISO (strong)' if alliso else 'non-iso'}")
    for d in details: print("   ",d)
