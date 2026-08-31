"""
Enumerate law-satisfying degree-1 liftings with 2 objects per state, to test:
 (Q1) is OUT forced = identity (outer object = input object) ?
 (Q2) does INN depend on tvec, or only on T (endpoint) ?
 (Q3) are all survivors trivial products SxC (C discrete-2 or its relabelings)?

Strategy: use RU/LU to pin, then enumerate residual against ASSOC.
We do a STRUCTURED enumeration: parametrize OUT, INN fully but prune with unit laws first via
a per-factorization local check is hard; instead we (a) randomized-search full space for survivors,
(b) fully enumerate the 'transport ansatz' (OUT=id, INN=tau_T indep of tvec) and classify.
"""
from itertools import product
import random, honest
from free_transport import build, laws_ok
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM

O={0:['a','b'],1:['a','b']}
FACT=[(T,tvec) for T in SS for tvec in product(SS,repeat=2)]
KEYS=[(T,tvec,s,x) for (T,tvec) in FACT for s in S for x in O[s]]

def rand_full(rng):
    OUT={k: rng.choice(O[k[2]]) for k in KEYS}
    INN={k: rng.choice(O[k[0][k[2]]]) for k in KEYS}   # object at state T[s]=k[0][k[2]]
    return OUT,INN

def randomized_search(N=200000, seed=0):
    rng=random.Random(seed); survivors=[]
    for _ in range(N):
        OUT,INN=rand_full(rng)
        A,eps,delta=build(O,OUT,INN)
        if laws_ok(A,eps,delta):
            survivors.append((dict(OUT),dict(INN)))
    return survivors

def is_out_identity(OUT):
    return all(OUT[k]==k[3] for k in KEYS)

def inn_depends_on_tvec(INN):
    # check if INN(T,tvec,s,x) varies with tvec at fixed (T,s,x)
    bad=[]
    seen={}
    for k in KEYS:
        T,tvec,s,x=k
        key=(T,s,x)
        if key in seen and seen[key]!=INN[k]: bad.append((key,seen[key],INN[k]))
        seen.setdefault(key,INN[k])
    return bad

def inn_depends_only_on_endpoint(INN):
    # endpoint of arrow from s under T is T(s). Does INN(T,.,s,x) depend on T only via T(s)?
    seen={}; bad=[]
    for k in KEYS:
        T,tvec,s,x=k
        key=(T[s],s,x)   # endpoint T(s), source s, object x
        if key in seen and seen[key]!=INN[k]: bad.append((key,seen[key],INN[k]))
        seen.setdefault(key,INN[k])
    return bad

if __name__=="__main__":
    surv=randomized_search(N=300000,seed=1)
    print(f"randomized full-space survivors found: {len(surv)}")
    # classify
    out_id=sum(1 for OUT,INN in surv if is_out_identity(OUT))
    print(f"  of these, OUT=identity: {out_id}/{len(surv)}")
    tvec_indep=sum(1 for OUT,INN in surv if not inn_depends_on_tvec(INN))
    print(f"  INN independent of tvec: {tvec_indep}/{len(surv)}")
    endpt=sum(1 for OUT,INN in surv if not inn_depends_only_on_endpoint(INN))
    print(f"  INN endpoint-local (depends on T only via T(s)): {sum(1 for OUT,INN in surv if not inn_depends_only_on_endpoint(INN))}/{len(surv)}")
    # dedupe distinct (OUT,INN)
    uniq=set()
    for OUT,INN in surv:
        uniq.add((tuple(sorted(OUT.items())),tuple(sorted(INN.items()))))
    print(f"  distinct survivors: {len(uniq)}")
