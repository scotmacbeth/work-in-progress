"""
Test the INTERCHANGE law for ⊗_W in framework A (grade-multiplying), all four ⋆.
   (w1'∘w1) ⊗ (w2'∘w2)  ==  (w1'⊗w2') ∘ (w1⊗w2)   up to grade bijection.
Also test that ⊗_W of identities behaves.  Enumerate all small workers.
"""
from containers import *
from worker_harness import Worker, compose, tensorW, eq_upto_grade, STARS
from itertools import product as iproduct

def all_workers(G, p, q, limit=None):
    """all container morphisms ΔG⊗p -> q."""
    src=tensor(deltaS(G), p)
    ws=[]
    # forward: each src shape -> a q shape ; backward: each target position -> src position
    shapes=src.shapes
    fwd_choices=list(iproduct(q.shapes, repeat=len(shapes)))
    for fwd_t in fwd_choices:
        fwd=dict(zip(shapes,fwd_t))
        # backward: for each shape, for each target position choose a src position
        per_shape=[]
        ok=True
        for sh in shapes:
            c=fwd[sh]; targ=q.fib[c]; srcpos=src.fib[sh]
            if len(srcpos)==0 and len(targ)>0: ok=False; break
            per_shape.append((sh, targ, srcpos))
        if not ok: continue
        # enumerate backward
        choice_spaces=[list(iproduct(sp, repeat=len(targ))) if len(targ)>0 else [()] for (_,targ,sp) in per_shape]
        for combo in iproduct(*choice_spaces):
            bwd={}
            for (sh,targ,sp),vals in zip(per_shape,combo):
                bwd[sh]={d:v for d,v in zip(targ,vals)}
            m=Mor(src,q,fwd,bwd)
            okv,_=m.validate()
            if okv:
                ws.append(Worker(G,p,q,m))
                if limit and len(ws)>=limit: return ws
    return ws

def run(star):
    # richer objects: multi-shape and multi-position to exercise state duplication
    p =Cont(['a0','a1'],{'a0':['b0','b1'],'a1':['b2']})
    q =Cont(['c0','c1'],{'c0':['d0'],'c1':['d1','d2']})
    r =Cont(['e'],{'e':['g0','g1']})
    p2=Cont(['A'],{'A':['B0','B1']})
    q2=Cont(['C'],{'C':['D0','D1']})
    r2=Cont(['E0','E1'],{'E0':['G'],'E1':['H']})
    S=['s'];  Sp=['x','y']   # w1 grade S, w1' grade Sp
    T=['u','v']; Tp=['m']
    W1 =all_workers(S,p,q, limit=40)
    W1p=all_workers(Sp,q,r, limit=40)
    W2 =all_workers(T,p2,q2, limit=40)
    W2p=all_workers(Tp,q2,r2, limit=40)
    tested=0; fails=0
    for w1 in W1[:4]:
        for w1p in W1p[:4]:
            for w2 in W2[:4]:
                for w2p in W2p[:4]:
                    # LHS: (w1'∘w1) ⊗ (w2'∘w2)
                    c1=compose(w1,w1p)   # p->r grade S×Sp
                    c2=compose(w2,w2p)   # p2->r2 grade T×Tp
                    lhs=tensorW(c1,c2,star)
                    # RHS: (w1'⊗w2') ∘ (w1⊗w2)
                    t_low =tensorW(w1,w2,star)     # p⋆p2 -> q⋆q2 grade S×T
                    t_high=tensorW(w1p,w2p,star)   # q⋆q2 -> r⋆r2 grade Sp×Tp
                    rhs=compose(t_low,t_high)      # p⋆p2 -> r⋆r2 grade (S×T)×(Sp×Tp)
                    tested+=1
                    if not eq_upto_grade(lhs,rhs):
                        fails+=1
                        if fails<=2:
                            print(f"   [{star}] interchange FAIL example (grades {lhs.G} vs {rhs.G})")
    return tested,fails

if __name__=='__main__':
    for star in ['⊗','×','+','◁']:
        t,f=run(star)
        print(f"⋆={star}:  interchange tested={t}  fails={f}  ==> {'HOLDS' if f==0 else 'FAILS'}")
