from itertools import product
import honest, product_SxC as P, copy
SS=honest.SS; S=[0,1]; thread=honest.thread
A,eps,delta0=P.build_SxC({0:P.mkcat_disc(2),1:P.mkcat_disc(2)})
def dout(d): return {(k,j):r[0] for k,route in d.items() for j,r in route.items()}
def star_ok(delta):
    d=dout(delta)
    for T in SS:
      for tvec in product(SS,repeat=2):
        sigp=thread(T,tvec)
        for rho in product(SS,repeat=4):
            R={(s,r):rho[2*s+r] for s in S for r in S}
            tau=(tuple(R[(0,r)][tvec[0][r]] for r in S),tuple(R[(1,r)][tvec[1][r]] for r in S))
            sig=thread(T,tau); ro=(R[(0,T[0])],R[(1,T[1])])
            for j in range(len(A[sig])):
                if d[((T,tau),j)]!=d[((T,tvec),d[((sigp,ro),j)])]: return False
    return True
def src(o): return 0 if o[0]>0 else 1
res=[]; cnt=0
for T in SS:
 for tvec in product(SS,repeat=2):
  sig=thread(T,tvec)
  for j in range(len(A[sig])):
    s=src(A[sig][j]); cur=delta0[(T,tvec)][j][0]
    for nk in [k for k in range(len(A[T])) if src(A[T][k])==s and k!=cur]:
        d=copy.deepcopy(delta0); o,i,b=d[(T,tvec)][j]; d[(T,tvec)][j]=(nk,i,b)
        a=honest.check_assoc_fast(A,eps,d); st=star_ok(d)
        res.append((a,st)); cnt+=1
        if cnt>=16: break
    if cnt>=16: break
  if cnt>=16: break
 if cnt>=16: break
dis=sum(1 for a,st in res if a!=st); bb=sum(1 for a,st in res if not a and not st); bh=sum(1 for a,st in res if a and st)
print(f"[conv4] {len(res)} corruptions: disagree={dis} both_break={bb} both_hold={bh}")
