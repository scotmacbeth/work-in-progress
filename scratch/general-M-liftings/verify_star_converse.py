from itertools import product
import honest, product_SxC as P, copy
SS=honest.SS; ID=honest.ID; S=[0,1]; thread=honest.thread
from verify_star import check_star
A,eps,delta0=P.build_SxC({0:P.mkcat_disc(3),1:P.mkcat_disc(3)})  # 3 objects/source, degree 1
def corrupt(delta, key,j,newout):
    d=copy.deepcopy(delta); out_j,inner,beta=d[key][j]; d[key][j]=(newout,inner,beta); return d
def src(obj): return 0 if obj[0]>0 else 1
tested=0; disagree=0; bb=0; bh=0
for T in SS:
  for tvec in product(SS,repeat=2):
    sig=thread(T,tvec)
    for j in range(len(A[sig])):
        s=src(A[sig][j]); cur=delta0[(T,tvec)][j][0]
        alts=[k for k in range(len(A[T])) if src(A[T][k])==s and k!=cur]
        for newout in alts:
            d=corrupt(delta0,(T,tvec),j,newout)
            a=honest.check_assoc_fast(A,eps,d); st,_=check_star(A,eps,d)
            tested+=1
            if a!=st: disagree+=1
            elif not a: bb+=1
            else: bh+=1
print(f"[disc3] corruptions={tested} disagree(assoc!=star)={disagree} both_break={bb} both_hold={bh}")
print("=> (star) tracks associativity across corruptions" if disagree==0 else "=> MISMATCH, investigate")
