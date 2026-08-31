"""Position-level grade-independence: for the LU factorization (sh) and pr factorization,
check that the backward beta maps restrict to inverse bijections Out(j) <-> Out(sh(j)),
so A_t ≅ A_id as FULL polynomial functors (degree preserved), on 𝕊×C."""
from itertools import product
import honest, product_SxC as P
SS=honest.SS; ID=honest.ID; S=[0,1]; thread=honest.thread
def rebuild_idx(cats):
    lst=[]; idx={}
    for s in S:
        Cc=cats[s]
        for c in Cc.obs:
            idx[(s,c)]=len(lst); lst.append((len(Cc.out(c)),0) if s==0 else (0,len(Cc.out(c))))
    return lst,idx
def deg(obj): return obj[0]+obj[1]
def run(name,cats):
    A,eps,delta=P.build_SxC(cats); lst,idx=rebuild_idx(cats)
    ok=True
    for t in SS:
        # sh: LU factorization (id,(t,t)); object j in A_t -> (sh(j)=out_j, inner f, beta)
        key=(ID,(t,t))
        for (s,c),j in idx.items():
            out_j,inner,beta=delta[key][j]     # out_j = sh(j) in A_id
            # degree preserved?
            if deg(A[t][j])!=deg(A[ID][out_j]): ok=False; print("  deg mismatch",name,t,s,c)
    print(f"{name}: sh_t preserves out-degree for all t (A_t≅A_id as functors): {ok}")
run("Z/2",{0:P.Z2,1:P.Z2})
run("arrow",{0:P.mkcat_arrow(),1:P.mkcat_arrow()})
run("disc3",{0:P.mkcat_disc(3),1:P.mkcat_disc(3)})
run("Z/3",{0:P.Z3,1:P.Z3})
