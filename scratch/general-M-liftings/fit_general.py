"""
Fit LHS/RHS deepest-object formulas for a GENERIC (random, not law-abiding) degree-1 transport,
so tau^{id} != id and we see the true general formula. The backward maps are defined for ANY delta.
Object set: O_s = 3 labels per state. tau^g(s,x) = random object at state g[s].
"""
from itertools import product
import random, honest, lean_assoc
from free_transport import build
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM; comp=honest.comp

O={0:['p','q','r'],1:['u','v','w']}
rng=random.Random(42)
# random tau: for each (g,s,x) -> element of O[g[s]]
TAU={}
for g in SS:
    for s in S:
        for x in O[s]:
            TAU[(g,s,x)]=rng.choice(O[g[s]])
def tau(g,s,x): return TAU[(g,s,x)]

OUT={}; INN={}
for T in SS:
    for tvec in product(SS,repeat=2):
        for s in S:
            for x in O[s]:
                OUT[(T,tvec,s,x)]=x                 # ansatz OUT=id
                INN[(T,tvec,s,x)]=tau(T,s,x)        # transport uses outer grade T
A,eps,delta=build(O,OUT,INN)
OBJS=[(s,x) for s in S for x in O[s]]
def objof(i): return OBJS[i]

C=(['a'],{'a':('a0','a1')}); S0,P=C
def Mshapes(S0): return [(t,x) for t in SS for x in product(S0,repeat=2)]
TC=lean_assoc.build_container(A,C); Ptc=TC[1]; S0tc=TC[0]; S0ttc=Mshapes(S0tc); TTT=Mshapes(S0ttc)

def deepest(tower):
    idx=tower[0]; rest=tower[1]
    while isinstance(rest,tuple) and len(rest)>=1 and isinstance(rest[0],tuple):
        inner=rest[0]; idx=inner[0]; rest=inner[1]
    return idx

def sides_at(w3):
    (t3,X3)=w3
    muC_fwd={}; muC_bwd={}
    for s in S:
        img,m=lean_assoc.mu_bwd_at(A,delta,P,X3[s]); muC_fwd[s]=img; muC_bwd[s]=m
    X2=tuple(muC_fwd[s] for s in S); w2_lhs=(t3,X2)
    img1,muAtw2=lean_assoc.mu_bwd_at(A,delta,P,w2_lhs)
    Q_TT=(Ptc[X2[0]],Ptc[X2[1]]); Tmu_bwd={}
    for (j,choiced) in lean_assoc.posA(A,t3,Q_TT):
        sl=honest.slots(A[t3][j]); nc=tuple(muC_bwd[s][tok] for (tok,(s,i)) in zip(choiced,sl))
        Tmu_bwd[(j,choiced)]=(j,nc)
    lhs={p: Tmu_bwd[muAtw2[p]] for p in muAtw2}
    img_rhs2, muTC_bwd = lean_assoc.mu_bwd_at(A,delta,Ptc,w3)
    img_rhs1, muC2 = lean_assoc.mu_bwd_at(A,delta,P,img_rhs2)
    rhs={p: muTC_bwd[muC2[p]] for p in muC2}
    return img1,img_rhs1,lhs,rhs

recs=[]
for w3 in TTT:
    (t3,X3)=w3
    tvec=tuple(X3[s][0] for s in S)
    rho={}
    for s in S:
        (ts,xs)=X3[s]
        for r in S: rho[(s,r)]=xs[r][0]
    img1,img1b,lhs,rhs=sides_at(w3)
    for p in lhs:
        jidx,choice=p; (s,x)=objof(jidx)
        recs.append(dict(t3=t3,tvec=tvec,rho=rho,s=s,x=x,
                         L=objof(deepest(lhs[p])),R=objof(deepest(rhs[p]))))
print("records:",len(recs))
def sp(t3,tvec): return tuple(tvec[s][t3[s]] for s in S)
# LHS check
badL=sum(1 for r in recs if (r['tvec'][r['s']][r['t3'][r['s']]], tau(r['tvec'][r['s']], r['t3'][r['s']], tau(r['t3'],r['s'],r['x'])))!=r['L'])
print("LHS = tau^{t_s}(t3(s),tau^{t3}(s,x)) mismatches:",badL)
# RHS search: tau^{g2}(g1(s), tau^{g1}(s,x))
def vocab(r):
    s=r['s']; t3=r['t3']; tvec=r['tvec']; rho=r['rho']; spv=sp(t3,tvec)
    return {'t3':t3,'t_s':tvec[s],'sigmap':spv,'rho_sTs':rho[(s,t3[s])],'rho_ss':rho[(s,s)],'id':ID}
def gen(r,g1n,g2n):
    s=r['s']; x=r['x']; v=vocab(r); g1=v[g1n]; g2=v[g2n]
    return (g2[g1[s]], tau(g2,g1[s], tau(g1,s,x)))
for g1 in ['t3','t_s','sigmap','rho_sTs','rho_ss','id']:
    for g2 in ['t3','t_s','sigmap','rho_sTs','rho_ss','id']:
        if sum(1 for r in recs if gen(r,g1,g2)!=r['R'])==0:
            print(f"  RHS = tau^{{{g2}}}(g1(s), tau^{{{g1}}}(s,x)) with g1={g1},g2={g2} : MATCH")
