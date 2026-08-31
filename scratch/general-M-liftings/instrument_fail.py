"""
Instrument the ASSOC failure of the representable copresheaf S(0,-) transport.
Dump, at the failing TTT-shape, the LHS (mu.Tmu) and RHS (mu.muTC) backward maps and DIFF them,
decoding towers as (grade, object) to read the exact obstruction equation the transport must satisfy.
"""
from itertools import product
import honest, lean_assoc, copresheaf
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM

# build representable S(0,-) transport
F1={0:[u for u in SS if u[0]==0], 1:[u for u in SS if u[0]==1]}
def comp(g,x): return tuple(g[x[k]] for k in S)
Fact1={g:{(s,x):comp(g,x) for s in S for x in F1[s]} for g in SS}
A,eps,delta=copresheaf.build_from_copresheaf(F1,Fact1)

# the base container C = single shape 'a', tokens a0,a1 (degree 2) so tokens distinguish slots
C=(['a'],{'a':('a0','a1')})
S0,P=C

# find a failing TTT-shape by scanning
def Mshapes(S0): return [(t,x) for t in SS for x in product(S0,repeat=2)]
TC=lean_assoc.build_container(A,C); Ptc=TC[1]; S0tc=TC[0]
S0ttc=Mshapes(S0tc); ttt=Mshapes(S0ttc)

def objname(A, grade, jidx):
    # decode object index jidx in A[grade] to (source-state, element) via copresheaf ordering
    # copresheaf orders objects as [(s,x) for s in S for x in F[s]]
    objs=[(s,x) for s in S for x in F1[s]]
    return objs[jidx]

def lhs_rhs_at(w3):
    (t3,X3)=w3
    muC_fwd={}; muC_bwd={}
    for s in S:
        img,m=lean_assoc.mu_bwd_at(A,delta,P,X3[s]); muC_fwd[s]=img; muC_bwd[s]=m
    X2=tuple(muC_fwd[s] for s in S); w2_lhs=(t3,X2)
    img1,muAtw2=lean_assoc.mu_bwd_at(A,delta,P,w2_lhs)
    Q_TT=(Ptc[X2[0]],Ptc[X2[1]])
    Tmu_bwd={}
    for (j,choiced) in lean_assoc.posA(A,t3,Q_TT):
        sl=honest.slots(A[t3][j]); nc=tuple(muC_bwd[s][tok] for (tok,(s,i)) in zip(choiced,sl))
        Tmu_bwd[(j,choiced)]=(j,nc)
    lhs={p: Tmu_bwd[muAtw2[p]] for p in muAtw2}
    img_rhs2, muTC_bwd = lean_assoc.mu_bwd_at(A,delta,Ptc,w3)
    img_rhs1, muC2 = lean_assoc.mu_bwd_at(A,delta,P,img_rhs2)
    rhs={p: muTC_bwd[muC2[p]] for p in muC2}
    return img1,img_rhs1,lhs,rhs

for w3 in ttt:
    img1,img_rhs1,lhs,rhs=lhs_rhs_at(w3)
    if img1==img_rhs1 and lhs!=rhs:
        (t3,X3)=w3
        print("FAILING TTT-shape:")
        print("  outer grade T =",NM[t3])
        for s in S:
            (ts,xs)=X3[s]
            print(f"   state {s}: middle grade t_{s}={NM[ts]}, inner=",
                  [(NM[xs[r][0]], xs[r][1]) for r in S])
        print("  collapsed T-shape:",img1)
        # diff
        for p in lhs:
            if lhs[p]!=rhs[p]:
                # p is a T-position (jidx,choice); decode object
                jidx,choice=p
                print("  DIFF at T-pos object", objname(A,img1[0],jidx), "choice",choice)
                print("     LHS tower:", decode:=lhs[p])
                print("     RHS tower:", rhs[p])
        break
