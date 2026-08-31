import lean_assoc, honest
from itertools import product
SS=honest.SS; thread=honest.thread
def make_SxM(mul,e,elems):
    d=len(elems); A={t:[(d,0),(0,d)] for t in SS}
    eps={0:elems.index(e),1:elems.index(e)}; delta={}
    for T in SS:
      for tvec in product(SS,repeat=2):
        sigma=thread(T,tvec); route={}
        for j,obj in enumerate(A[sigma]):
          s=0 if obj[0]>0 else 1
          route[j]=(j,{a:(0 if T[s]==0 else 1) for a in range(d)},
                    {(a,b):elems.index(mul(elems[a],elems[b])) for a in range(d) for b in range(d)})
        delta[(T,tvec)]=route
    return A,eps,delta
C=(['a'], {'a':('a0','a1')})
for name,(mul,e,el) in [
    ('S x 1   ', (lambda x,y:0,0,[0])),
    ('S x Z/2 ', (lambda x,y:(x+y)%2,0,[0,1])),
    ('S x Z/3 ', (lambda x,y:(x+y)%3,0,[0,1,2])),
    ('S x AND ', (lambda x,y:x*y,1,[0,1])),
    ('S x nonassoc-ctrl',(lambda x,y:[[0,0],[0,0]][x][y] if False else (1 if (x==1 or y==1) else 0),0,[0,1])),
  ]:
    A,eps,delta=make_SxM(mul,e,el)
    print(name,'->', lean_assoc.assoc_sample(A,eps,delta,C,nsamp=200,seed=1), flush=True)
# genuine non-associative control: define a magma that's non-assoc
def nonassoc(x,y):  # table on {0,1,2}: pick a known non-associative magma with left unit 0
    T={(0,0):0,(0,1):1,(0,2):2,(1,0):1,(1,1):2,(1,2):0,(2,0):2,(2,1):0,(2,2):1}  # this is Z/3 actually (assoc)
    return T[(x,y)]
# truly non-assoc: (1*1)*1 vs 1*(1*1)
def na(x,y):
    T={(0,0):0,(0,1):1,(0,2):2,(1,0):1,(1,1):2,(1,2):1,(2,0):2,(2,1):1,(2,2):1}
    return T[(x,y)]
A,eps,delta=make_SxM(na,0,[0,1,2])
print('S x NONASSOC ->', lean_assoc.assoc_sample(A,eps,delta,C,nsamp=400,seed=3), flush=True)
