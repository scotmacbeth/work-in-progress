"""
Extract, for the copresheaf transport tau^g(s,x)=comp(g,x)=g o x, the deepest-object of both
associativity sides over ALL TTT-shapes & starting objects, and FIT symbolic formulas.
Candidate:  LHS_deep = tau^{t_s}( t3(s), tau^{t3}(s,x) ).
Then search for RHS formula among simple compositions of tau over {t3,t_s,rho_{s,T(s)},sigma',...}.
"""
from itertools import product
import honest, lean_assoc, copresheaf
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM; comp=honest.comp

F1={0:[u for u in SS if u[0]==0], 1:[u for u in SS if u[0]==1]}
def cmp(g,x): return tuple(g[x[k]] for k in S)   # g o x  (post-compose)
Fact1={g:{(s,x):cmp(g,x) for s in S for x in F1[s]} for g in SS}
A,eps,delta=copresheaf.build_from_copresheaf(F1,Fact1)
OBJS=[(s,x) for s in S for x in F1[s]]     # index order used by build_from_copresheaf
def objof(idx): return OBJS[idx]
def idxof(s,x): return OBJS.index((s,x))

tau=lambda g,s,x: cmp(g,x)   # transport: object x at state s, along grade g -> object at state g[s]

C=(['a'],{'a':('a0','a1')}); S0,P=C
def Mshapes(S0): return [(t,x) for t in SS for x in product(S0,repeat=2)]
TC=lean_assoc.build_container(A,C); Ptc=TC[1]; S0tc=TC[0]; S0ttc=Mshapes(S0tc)
TTT=Mshapes(S0ttc)

def deepest(tower):
    # tower = (objidx, ( (slotobj, subtower_or_tokens), ... ))  -> follow first slot to the leaf objidx
    idx=tower[0]; rest=tower[1]
    while isinstance(rest,tuple) and len(rest)>=1 and isinstance(rest[0],tuple):
        inner=rest[0]          # (objidx, sub)
        idx=inner[0]; rest=inner[1]
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
    return img1,lhs,rhs

# collect records
recs=[]
for w3 in TTT:
    (t3,X3)=w3
    tvec=tuple(X3[s][0] for s in S)         # middles t_s
    rho={}                                   # rho_{s,r}
    for s in S:
        (ts,xs)=X3[s]
        for r in S: rho[(s,r)]=xs[r][0]
    img1,lhs,rhs=sides_at(w3)
    sig=img1[0]
    for p in lhs:
        jidx,choice=p
        (s,x)=objof(jidx)
        Ld=objof(deepest(lhs[p])); Rd=objof(deepest(rhs[p]))
        recs.append(dict(t3=t3,tvec=tvec,rho=rho,s=s,x=x,sig=sig,L=Ld,R=Rd))

# verify LHS formula
def sigma_prime(t3,tvec): return tuple(tvec[s][t3[s]] for s in S)
def check_LHS():
    bad=0
    for r in recs:
        t3=r['t3']; tvec=r['tvec']; s=r['s']; x=r['x']
        pred_state=tvec[s][t3[s]]
        inner=tau(t3,s,x); pred=tau(tvec[s], t3[s], inner)   # tau^{t_s}(t3(s), tau^{t3}(s,x))
        if (pred_state,pred)!=r['L']: bad+=1
    return bad
print("LHS formula tau^{t_s}(t3(s),tau^{t3}(s,x)) mismatches:", check_LHS(), "/", len(recs))

# search RHS formula among candidate grade-sequences applied to x
def try_RHS(desc, fn):
    bad=0
    for r in recs:
        if fn(r)!=r['R']: bad+=1
    if bad==0: print("  RHS MATCH:", desc)
    return bad

cands={
 "tau^{rho_{s,T(s)}}(sig'(s), tau^{sig'}(s,x))": lambda r:(
     (lambda sp: (r['rho'][(r['s'], r['t3'][r['s']])][ sp[r['s']] ],
                  tau(r['rho'][(r['s'], r['t3'][r['s']])], sp[r['s']], tau(sp, r['s'], r['x']))))(sigma_prime(r['t3'],r['tvec'])) ),
 "tau^{rho_{s,T(s)}}(t_s(t3(s)), tau^{sig'}(s,x))": lambda r:(
     (lambda sp: (r['rho'][(r['s'], r['t3'][r['s']])][ sp[r['s']] ],
                  tau(r['rho'][(r['s'], r['t3'][r['s']])], sp[r['s']], tau(sp, r['s'], r['x']))))(sigma_prime(r['t3'],r['tvec'])) ),
}
for d,f in cands.items():
    try: b=try_RHS(d,f)
    except Exception as e: b=('err',e)
    print("  RHS cand", d, "mismatch", b)

# brute: RHS as tau^{g2}(., tau^{g1}(s,x)) for g1,g2 in a small vocab depending on r
def vocab(r):
    s=r['s']; t3=r['t3']; tvec=r['tvec']; rho=r['rho']; sp=sigma_prime(t3,tvec)
    return {
        't3':t3,'t_s':tvec[s],'sigmap':sp,
        'rho_sTs':rho[(s,t3[s])],'rho_ss':rho[(s,s)],
        'id':ID,
    }
def rhs_generic(r,g1name,g2name):
    s=r['s']; x=r['x']; v=vocab(r); g1=v[g1name]; g2=v[g2name]
    inner=tau(g1,s,x); st1=g1[s]
    return (g2[st1], tau(g2,st1,inner))
best=None
for g1 in ['t3','t_s','sigmap','rho_sTs','rho_ss','id']:
    for g2 in ['t3','t_s','sigmap','rho_sTs','rho_ss','id']:
        bad=sum(1 for r in recs if rhs_generic(r,g1,g2)!=r['R'])
        if bad==0: print(f"  RHS = tau^{{{g2}}}(., tau^{{{g1}}}(s,x)) : MATCH")
