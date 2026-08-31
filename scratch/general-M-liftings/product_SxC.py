"""
Forward construction from D = S x C  (C a small category), projection to S is Conduche.
Objects over state s = Ob C. aggregator object at (grade sigma, source s, c) has positions =
out-morphisms of c in C (degree |out(c)|). delta: S-source-routing (trivial action) x C-composition.
Test global categories C (should lift) vs per-state-different (should fail: S connected).
"""
from itertools import product
import honest, lean_assoc
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread
C0=(['a'], {'a':('a0','a1')})

class Cat:
    def __init__(self, obs, homs, comp, ident):
        self.obs=obs; self.homs=homs; self.comp=comp; self.ident=ident
        # homs: dict (c,c')->list of morphism ids ; out(c)=all morphisms with source c
    def out(self,c):
        r=[]
        for (a,b),ms in self.homs.items():
            if a==c:
                for m in ms: r.append((m,b))   # (morphism, target)
        return r

def build_SxC(Cs_per_source):
    """Cs_per_source: dict s-> Cat.  (For a global product pass same Cat for both.)"""
    # objects at source s: Ob of Cs_per_source[s]; but composition across states needs a shared law.
    # For a genuine product S x C we pass the SAME Cat for both sources and use its composition.
    # For per-state-different we pass different Cats (expected to fail).
    def A_of():
        # A is grade-independent: same for all sigma
        lst=[]; idx={}
        for s in S:
            Cc=Cs_per_source[s]
            for c in Cc.obs:
                d=len(Cc.out(c))
                idx[(s,c)]=len(lst)
                lst.append((d,0) if s==0 else (0,d))
        return lst, idx
    lst,idx=A_of()
    A={sigma:list(lst) for sigma in SS}
    IDX={sigma:dict(idx) for sigma in SS}
    # eps on A_id: object (s,c) marked position = index of identity morphism in out(c)
    eps={}
    for (s,c),i in idx.items():
        Cc=Cs_per_source[s]; outc=Cc.out(c)
        e=Cc.ident[c]
        eps[i]=[m for (m,b) in outc].index(e)
    # delta: composite object j=(s,c) in A_sigma. out=(s,c) in A_T ; for each out-position p=(f:c->c1)
    #   inner object = (T(s), c1) in A_{tvec[s]} ; beta((p, q:c1->c2)) = position of (g = q o f : c->c2) in out(c).
    delta={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            sigma=thread(T,tvec); route={}
            for (s,c),j in IDX[sigma].items():
                Cs=Cs_per_source[s]; Ct=Cs_per_source[T[s]]
                outc=Cs.out(c); out_j=IDX[T][(s,c)]
                inner={};
                # out-object (s,c) in A_T has positions = out(c) (its degree). enumerate its slots.
                # slots of out-obj = range(len(outc)) at state s
                for ai,(f,c1) in enumerate(outc):
                    # inner object over T(s): must be (T(s), c1). But c1 in Cs.obs; inner cat is Ct.
                    if (T[s],c1) not in IDX[tvec[s]]:
                        route=None; break
                    inner[ai]=IDX[tvec[s]][(T[s],c1)]
                if route is None: break
                beta={}
                for ai,(f,c1) in enumerate(outc):
                    Ct2=Cs_per_source[T[s]]; out_c1=Ct2.out(c1)
                    for bi,(q,c2) in enumerate(out_c1):
                        if (q,f) not in Cs.comp:
                            route=None; break
                        g=Cs.comp[(q,f)]   # q o f : c->c2
                        beta[(ai,bi)]=[m for (m,b) in outc].index(g)
                    if route is None: break
                if route is None: break
                route[j]=(out_j, inner, beta)
            if route is None:
                delta=None; break
            delta[(T,tvec)]=route
        if delta is None: break
    return A,eps,delta

def mkcat_BM(mul,e,elems):
    # one object '*', morphisms=elems, comp = mul, ident=e
    homs={('*','*'):list(elems)}
    comp={(y,x):mul(y,x) for x in elems for y in elems}   # comp[(y,x)] = y o x
    return Cat(['*'], homs, comp, {'*':e})

def mkcat_arrow():
    # 2 objects 0,1; morphisms id0,id1, u:0->1. out(0)={id0,u}, out(1)={id1}
    homs={(0,0):['i0'],(0,1):['u'],(1,1):['i1']}
    comp={('i0','i0'):'i0', ('u','i0'):'u', ('i1','u'):'u', ('i1','i1'):'i1'}
    return Cat([0,1], homs, comp, {0:'i0',1:'i1'})

def mkcat_disc(n):
    homs={(i,i):['i%d'%i] for i in range(n)}
    comp={('i%d'%i,'i%d'%i):'i%d'%i for i in range(n)}
    return Cat(list(range(n)), homs, comp, {i:'i%d'%i for i in range(n)})

def test(name,cats):
    A,eps,delta=build_SxC(cats)
    if delta is None:
        print(f'{name}: delta UNDEFINED (cannot route across states)'); return
    u=honest.check_units_fast(A,eps,delta)
    a=lean_assoc.assoc_sample(A,eps,delta,C0,nsamp=400,seed=7)
    print(f'{name}: units={u}  assoc={a}',flush=True)

Z2=mkcat_BM(lambda y,x:(y+x)%2,0,[0,1])
Z3=mkcat_BM(lambda y,x:(y+x)%3,0,[0,1,2])
test('SxC  C=Z/2 (global)', {0:Z2,1:Z2})
test('SxC  C=arrow(0->1)  ', {0:mkcat_arrow(),1:mkcat_arrow()})
test('SxC  C=disc3        ', {0:mkcat_disc(3),1:mkcat_disc(3)})
test('per-state Z2 vs Z3  ', {0:Z2,1:Z3})       # different monoids per state -> expect fail/undef
test('per-state disc2 vs disc3', {0:mkcat_disc(2),1:mkcat_disc(3)})
