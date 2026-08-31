"""
Forward construction from a COPRESHEAF F: S -> Set  (an S-set / discrete opfibration over the
action category S).  Category of elements el(F): objects (s,x) x in F(s); morphism (s,x)->(s',x')
over g:s->s' (g in S^S with g(s)=s') iff F(g)(x)=x'.  Discrete opfibration -> unique lifts -> degree 1.

Lifting:  A_sigma(Q) = coprod_{s} coprod_{x in F(s)} Q_s^{ |{ phi out of (s,x) over arrow sigma:s->sigma(s) }| }.
For a discrete opfib this multiplicity is 1 (unique lift), object (s,x) contributes Q_s once to every A_sigma.
delta = composition in el(F) along S-factorizations.
Verify units + (lean) associativity for several copresheaves.
"""
from itertools import product
import honest, lean_assoc
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM

def build_from_copresheaf(F, Fact):
    """F: dict s-> list of elements.  Fact: dict (g in S^S)-> dict mapping (s,x)->(g(s), F(g)(x)).
       Provide Fact[g][(s,x)] = the target element x' in F(g(s)). Must be functorial."""
    # objects grouped by source state
    objs={s:list(F[s]) for s in S}
    # A_sigma: order objects as [source0 objs ..., source1 objs ...], each degree 1 at its source
    def A_of(sigma):
        lst=[]; idxmap={}
        for s in S:
            for x in objs[s]:
                idxmap[(s,x)]=len(lst)
                lst.append((1,0) if s==0 else (0,1))
        return lst, idxmap
    A={}; IDX={}
    for sigma in SS:
        A[sigma],IDX[sigma]=A_of(sigma)
    # eps on A_id: object (s,x) marked position 0 (its unique out-morphism over id_s = identity)
    eps={}
    for (s,x),i in IDX[ID].items(): eps[i]=0
    # delta: for (T,tvec), composite object j=(s,x) in A_sigma (sigma=thread).
    #   arrow sigma from s = the endofunction sigma (as morphism s->sigma(s)).
    #   factor: u = T (arrow s->T(s)); v = tvec[s] (arrow T(s)->sigma(s)); check v(T(s))==sigma(s).
    #   out object = (s,x) in A_T ; its unique out-pos -> inner object = target of x under u = (T(s), F(u)(x)) in A_{tvec[s]}.
    delta={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            sigma=thread(T,tvec); route={}
            for (s,x),j in IDX[sigma].items():
                # out-object (s,x) in A_T
                out_j=IDX[T][(s,x)]
                # single out-position (a=0) -> inner object = (T(s), F(T)(x)) in A_{tvec[s]}
                xp=Fact[T][(s,x)]              # target element in F(T(s))
                mid=T[s]
                inner_obj=IDX[tvec[s]][(mid,xp)]
                inner={0:inner_obj}
                beta={(0,0):0}
                route[j]=(out_j,inner,beta)
            delta[(T,tvec)]=route
    return A,eps,delta

def check(name,F,Fact):
    A,eps,delta=build_from_copresheaf(F,Fact)
    u=honest.check_units_fast(A,eps,delta)
    C=(['a'], {'a':('a0','a1')})
    a=lean_assoc.assoc_sample(A,eps,delta,C,nsamp=400,seed=2)
    print(f'{name}: units={u}  assoc={a}',flush=True)

# --- copresheaf 1: representable S(0,-):  F(s)=Hom(0,s)  ---
F1={0:[u for u in SS if u[0]==0], 1:[u for u in SS if u[0]==1]}   # elements are the endofunctions x with x(0)=s
# F1(g)(x) = g o x  (post-compose)   ; x in Hom(0,s), g:s->s' => g o x in Hom(0,s')
def comp(g,x): return tuple(g[x[k]] for k in S)
Fact1={g:{(s,x):comp(g,x) for s in S for x in F1[s]} for g in SS}
check('rep S(0,-)', F1, Fact1)

# --- copresheaf 2: representable S(1,-) ---
F2={0:[u for u in SS if u[0]==0], 1:[u for u in SS if u[0]==1]}   # wait need Hom(1,s)
F2={0:[u for u in SS if u[1]==0], 1:[u for u in SS if u[1]==1]}   # elements x with x(1)=s
Fact2={g:{(s,x):comp(g,x) for s in S for x in F2[s]} for g in SS}
check('rep S(1,-)', F2, Fact2)

# --- copresheaf 3: constant F(s)={*}  (= Sigma) ---
F3={0:['*'],1:['*']}
Fact3={g:{(s,'*'):'*' for s in S} for g in SS}
check('constant-1 (=Sigma)', F3, Fact3)

# --- copresheaf 4: the terminal S-set representable-sum / F=Hom(-, ?)... use coproduct rep0+rep1 ---
# F4 = S(0,-) + S(1,-)  (disjoint)
F4={s:[('a',x) for x in F1[s]]+[('b',x) for x in F2[s]] for s in S}
def comp2(g,ex): tag,x=ex; return (tag, comp(g,x))
Fact4={g:{(s,ex):comp2(g,ex) for s in S for ex in F4[s]} for g in SS}
check('S(0,-)+S(1,-)', F4, Fact4)

# --- NON-functorial control: break F(g) to violate functoriality -> should fail assoc ---
import copy
Fbad=copy.deepcopy(Fact1)
# corrupt one action value
k=list(Fbad[SS[2]].keys())[0]
vals=[v for v in F1[SS[2][ list(F1.keys())[0] ] ]] if False else None
# just point it wrongly to some element in the right fibre-ish (force non-functorial)
g=SS[2]  # sw
some_s, some_x = list(Fbad[g].keys())[0]
# set target to a WRONG element of F(g(some_s))
tgt_state=g[some_s]
wrong=[x for x in F1[tgt_state]]
Fbad[g][(some_s,some_x)] = wrong[-1] if wrong[-1]!=comp(g,some_x) else (wrong[0] if len(wrong)>1 else wrong[0])
check('NON-functorial ctrl', F1, Fbad)
