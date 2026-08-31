"""On a known 𝕊×C lifting, extract sh_t = delta_out of LU-factorization (id,(t)),
and pr_t = delta_out of a chosen (t,(t'_s)) with sigma=id, and check they are inverse
bijections J_t^s <-> J_id^s.  Confirms the intended grade-independence witnesses."""
from itertools import product
import honest, product_SxC as P
SS=honest.SS; ID=honest.ID; NM=honest.NM; S=[0,1]; thread=honest.thread
def objs_at(IDX, g, s):  # object indices in A[g] with source s
    return [j for (ss,c),j in IDX[g].items() if ss==s]
def run(name, cats):
    A,eps,delta=P.build_SxC(cats)
    IDX={g:{} for g in SS}
    # rebuild IDX (build_SxC doesn't return it) : replicate its object order
    lst=[]; idx={}
    for s in S:
        Cc=cats[s]
        for c in Cc.obs:
            idx[(s,c)]=len(lst); lst.append((len(Cc.out(c)),0) if s==0 else (0,len(Cc.out(c))))
    IDX={g:dict(idx) for g in SS}
    ok=True
    for t in SS:
        for s in S:
            # sh_t : LU factorization (T=id, t_r=t all r), sigma=t. delta[(id,(t,t))][j].out
            key_lu=(ID,(t,t))
            # pr_t : pick (T=t, t'_r) with t'_r(t(r))=r  => sigma=id
            tvec=tuple( next(u for u in SS if u[t[r]]==r) for r in S )
            key_pr=(t,tvec)
            assert thread(t,tvec)==ID, (t,tvec,thread(t,tvec))
            sh={}; pr={}
            for j in objs_at(IDX,t,s):   # domain grade sigma=t
                sh[j]=delta[key_lu][j][0]
            for i in objs_at(IDX,ID,s):  # domain grade sigma=id
                pr[i]=delta[key_pr][i][0]
            # check bijection & inverse
            Jt=set(objs_at(IDX,t,s)); Jid=set(objs_at(IDX,ID,s))
            bij = (set(sh.values())==Jid and set(pr.values())==Jt
                   and all(pr[sh[j]]==j for j in Jt) and all(sh[pr[i]]==i for i in Jid))
            if not bij:
                ok=False; print(f"   {name} t={NM[t]} s={s}: sh/pr NOT inverse bij  sh={sh} pr={pr}")
    print(f"{name}: sh_t,pr_t inverse bijections J_t^s<->J_id^s for all t,s: {ok}")
run("C=Z/2", {0:P.Z2,1:P.Z2})
run("C=arrow", {0:P.mkcat_arrow(),1:P.mkcat_arrow()})
run("C=disc3", {0:P.mkcat_disc(3),1:P.mkcat_disc(3)})
run("C=Z/3", {0:P.Z3,1:P.Z3})
