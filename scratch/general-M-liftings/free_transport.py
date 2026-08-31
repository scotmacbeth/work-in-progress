"""
FREE-TRANSPORT PROBE.  |S|=2.  Discrete-opfibration-type liftings (each object degree 1),
objects O_s per source state, grade-INDEPENDENT object sets (grade-independence PROVED).
We parametrize the transport FREELY (NOT assumed functorial) and let the monad laws decide.

Object set: O_s = list of objects at source state s. Total objects across a grade: same for all grades.
A_sigma(Q) = coprod_s coprod_{x in O_s} Q_s^1   (degree 1 each).  [aggregator, grade-independent]

Data to fix a lifting (degree-1):
 - eps: for each x in O_id-fibre... but grade-indep so just: for object (s,x), a marked position.
   Degree 1 => marked position is the unique one. counit forces target of identity = itself? see below.
 - delta at (T,tvec): object (s,x) in A_sigma  ->  outer (s, OUT(T,tvec,s,x)) in A_T,
     inner (T(s), INN(T,tvec,s,x)) in A_{tvec[s]}, beta trivial (degree1).
   We parametrize OUT, INN as FREE functions and enumerate; keep those satisfying all 3 laws.

We WANT to discover: (a) OUT(...)=x always (outer=identity), (b) INN depends only on T(s) (endpoint),
(c) the induced transport is a trivial iso-system => product.  If instead exotic survivors appear,
the conjecture is FALSE (finer than Cat).
"""
from itertools import product
import honest
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM

def build(O, OUT, INN):
    """O: dict s->list objects. OUT,INN: dict key (T,tvec,s,x)->object-at-appropriate-state.
       Returns honest-engine (A,eps,delta) with degree-1 objects, or None if ill-typed."""
    # global object list & index per grade (grade-independent)
    lst=[]; idx={}
    for s in S:
        for x in O[s]:
            idx[(s,x)]=len(lst)
            lst.append((1,0) if s==0 else (0,1))
    A={sig:list(lst) for sig in SS}
    IDX={sig:dict(idx) for sig in SS}
    # eps on A_id: degree-1, unique marked position 0
    eps={i:0 for i in range(len(lst))}
    delta={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            sig=thread(T,tvec); route={}
            for (s,x) in [(s,x) for s in S for x in O[s]]:
                j=IDX[sig][(s,x)]
                outx=OUT[(T,tvec,s,x)]           # object at state s
                out_j=IDX[T][(s,outx)]
                innx=INN[(T,tvec,s,x)]           # object at state T[s]
                inner={0: IDX[tvec[s]][(T[s],innx)]}
                beta={(0,0):0}
                route[j]=(out_j, inner, beta)
            delta[(T,tvec)]=route
    return A,eps,delta

def laws_ok(A,eps,delta):
    return honest.check_units_fast(A,eps,delta) and honest.check_assoc_fast(A,eps,delta)

# ---- enumerate free transports for a given O, with OUT,INN ranging over all typed choices ----
def enumerate_liftings(O, restrict_out_identity=False, verbose=False):
    keys=[(T,tvec,s,x) for T in SS for tvec in product(SS,repeat=2) for s in S for x in O[s]]
    # choices: for each key, OUT in O[s], INN in O[T[s]]
    out_choices={k:(list(O[k[2]]) if not restrict_out_identity else [k[3]]) for k in keys}
    inn_choices={k:list(O[k[0][k[2]]]) for k in keys}  # O[T[s]]
    # too big to full-enumerate; we instead SOLVE law-by-law is hard. Do randomized+structured search.
    return keys,out_choices,inn_choices

if __name__=="__main__":
    # sanity: reproduce Sigma (O_s single object) trivial transport
    O={0:['*'],1:['*']}
    OUT={(T,tvec,s,x):'*' for T in SS for tvec in product(SS,repeat=2) for s in S for x in O[s]}
    INN={(T,tvec,s,x):'*' for T in SS for tvec in product(SS,repeat=2) for s in S for x in O[s]}
    A,eps,delta=build(O,OUT,INN)
    print("Sigma via free-transport builder, laws:", laws_ok(A,eps,delta))
