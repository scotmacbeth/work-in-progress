import honest, time
from itertools import product
SS=honest.SS; ID=honest.ID; thread=honest.thread

def make_SxM(mul, e, elems):
    d=len(elems)
    A={t:[(d,0),(0,d)] for t in SS}
    eps={0: elems.index(e), 1: elems.index(e)}
    delta={}
    for T in SS:
      for tvec in product(SS,repeat=2):
        sigma=thread(T,tvec); route={}
        for j,obj in enumerate(A[sigma]):
          s = 0 if obj[0]>0 else 1
          out_j=j
          inner={a:(0 if T[s]==0 else 1) for a in range(d)}
          beta={(a,b): elems.index(mul(elems[a], elems[b])) for a in range(d) for b in range(d)}
          route[j]=(out_j, inner, beta)
        delta[(T,tvec)]=route
    return A,eps,delta

def rep(name,A,eps,delta):
    t0=time.time(); u=honest.check_units_fast(A,eps,delta)
    a=honest.check_assoc_fast(A,eps,delta) if u else None
    print(f'{name}: units={u} assoc={a}  ({round(time.time()-t0,2)}s)',flush=True)

rep('S x 1  (=Sigma)', *make_SxM(lambda x,y:0,0,[0]))
rep('S x Z/2', *make_SxM(lambda x,y:(x+y)%2,0,[0,1]))
# non-associative control
badmul=lambda x,y: {(0,0):0,(0,1):1,(1,0):1,(1,1):0}[(x,y)] if (x,y)!=(1,1) else 1
rep('S x nonunital-ctrl', *make_SxM(lambda x,y: 1, 0, [0,1]))  # mul const 1: non-unital
