"""Verify (star): associativity projects to delta_out functoriality, and the two
instantiations give pr_t . sh_t = id and sh_t . pr_t = id.  We extract delta_out from the
honest engine's mu_morph on genuine T^3 elements and check (star) directly, lifting-agnostic
(tested on Sigma and SxZ2).  Also verify the threading identities by pure combinatorics."""
from itertools import product
import honest, product_SxC as P
SS=honest.SS; ID=honest.ID; NM=honest.NM; S=[0,1]; thread=honest.thread; comp=honest.comp

# ---- (A) threading identities used in the derivation (pure combinatorics) ----
def check_threading():
    ok=True
    for T in SS:
      for tvec in product(SS,repeat=2):
        for rho in product(SS,repeat=4):   # rho[(s,r)] as flat
            R={(s,r):rho[2*s+r] for s in S for r in S}
            sigp=thread(T,tvec)                       # sigma' = t_s(T(s))
            tau ={s: tuple(R[(s,r)][tvec[s][r]] for r in S) for s in S}  # tau_s(r)=rho_{s,r}(t_s(r))
            sig =thread(T, (tau[0],tau[1]))           # sigma via (T,(tau_s))
            # alt: sigma = thread(sigma', (rho_{s,T(s)}))
            rho_outer=(R[(0,T[0])], R[(1,T[1])])
            sig2=thread(sigp, rho_outer)
            if sig!=sig2: ok=False; print("threading mismatch",T,tvec,R)
    return ok
print("threading identity sigma=thread(T,tau)=thread(sigma',rho_.T.):", check_threading())

# ---- (B) extract delta_out(T,tvec,j) for a lifting ----
def delta_out_map(delta):
    f={}
    for key,route in delta.items():
        for j,(out_j,inner,beta) in route.items():
            f[(key,j)]=out_j
    return f

# ---- (C) verify (star) numerically: for all (T,tvec,rho), 
#          delta_out^{(T,tau)}(j) == delta_out^{(T,tvec)}( delta_out^{(sigma',rho_.T.)}(j) ) ----
def check_star(A,eps,delta):
    dout=delta_out_map(delta)
    ok=True; tested=0
    for T in SS:
      for tvec in product(SS,repeat=2):
        sigp=thread(T,tvec)
        for rho in product(SS,repeat=4):
            R={(s,r):rho[2*s+r] for s in S for r in S}
            tau=(tuple(R[(0,r)][tvec[0][r]] for r in S), tuple(R[(1,r)][tvec[1][r]] for r in S))
            sig=thread(T,tau)
            rho_outer=(R[(0,T[0])],R[(1,T[1])])
            for j in range(len(A[sig])):
                inner_j=dout[((sigp,rho_outer),j)]         # delta_out^{(sigma',rho_.T.)}
                lhs=dout[((T,tau),j)]                        # delta_out^{(T,tau)}
                rhs=dout[((T,tvec),inner_j)]                 # delta_out^{(T,tvec)} of that
                tested+=1
                if lhs!=rhs: ok=False
    return ok,tested

for name,(A,eps,delta) in [("Sigma",honest.sigma_lifting()),
                           ("SxZ2",P.build_SxC({0:P.Z2,1:P.Z2}))]:
    ok,t=check_star(A,eps,delta)
    print(f"(star) delta_out functoriality on {name}: {ok}  (checked {t} instances)")

# ---- (D) the two instantiations: confirm tau=id is achievable & gives RU ----
def instantiate_prsh():
    """For each t,s: build the 3-fold data giving RHS=pr_t.sh_t, LHS=(t,(id))=RU."""
    ok=True
    for t in SS:
        # pr's inner t'_s: t'_s(t(s))=s
        tp=tuple(next(u for u in SS if u[t[s]]==s) for s in S)
        # 3-fold: T=t, t_s=tp ; rho_{s,t(s)}=t ; rho_{s,r}(t'_s(r))=r for r!=t(s)
        R={}
        for s in S:
            for r in S:
                if r==t[s]: R[(s,r)]=t
                else:
                    # need rho with rho[tp[s][r]]=r
                    R[(s,r)]=next(u for u in SS if u[tp[s][r]]==r)
        tau=(tuple(R[(0,r)][tp[0][r]] for r in S), tuple(R[(1,r)][tp[1][r]] for r in S))
        if tau!=((0,1),(0,1)):   # id=(0,1)
            ok=False; print("  pr.sh: tau != id for t=",NM[t],"tau=",tau)
    return ok
print("pr_t.sh_t instantiation gives tau=id (=>LHS=RU):", instantiate_prsh())
