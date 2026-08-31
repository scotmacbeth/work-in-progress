"""
Enumerate THIN liftings: at most one object per (grade t, source s) slot, each degree 1.
Object at slot (t,s) is pure at state s => arity (1,0) if s==0 else (0,1).
delta is FORCED (all degree 1): composite j=(sigma,s) routes to out=(T,s), inner=(t_s,T(s)).
Enumerate subsets P of the 8 slots; build A, eps, delta; check monad laws via honest oracle.
Then interpret which P survive (structure over the action category S).
"""
from itertools import product
import honest
S=[0,1]; SS=honest.SS; ID=honest.ID; NM=honest.NM
thread=honest.thread
SLOTS=[(t,s) for t in SS for s in S]   # 8 slots

def arity(s): return (1,0) if s==0 else (0,1)

def build(P):
    """P: frozenset of populated slots (t,s). Return (A,eps,delta) or None if delta impossible."""
    # objects: at grade t, list objects for populated (t,s). record index per slot.
    A={t:[] for t in SS}
    slot_idx={}   # (t,s)-> object index within A[t]
    for (t,s) in sorted(P):
        slot_idx[(t,s)]=len(A[t])
        A[t].append(arity(s))
    # eps: grade-id objects -> marked slot (their unique position, index 0)
    eps={}
    for (t,s) in P:
        if t==ID:
            eps[slot_idx[(t,s)]]=0
    # delta: for each (T,tvec) and each populated composite (sigma,s), route.
    delta={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            sigma=thread(T,tvec)
            route={}
            for s in S:
                if (sigma,s) not in P: continue
                j=slot_idx[(sigma,s)]
                out_slot=(T,s); inner_slot=(tvec[s], T[s])
                if out_slot not in P or inner_slot not in P:
                    return None   # cannot route -> no lifting
                out_j=slot_idx[out_slot]
                # out object arity(s): its slots = [ (s,0) ] single slot index 0
                # inner: slot 0 of out-obj -> inner object index
                inner={0: slot_idx[inner_slot]}
                # beta: composite RHS slot (a=0,b=0) -> slot 0 of j
                beta={(0,0):0}
                route[j]=(out_j, inner, beta)
            delta[(T,tvec)]=route
    return A,eps,delta

from itertools import combinations
if __name__=="__main__":
    import sys
    closure=0; units=0; good=[]
    for r in range(0,9):
        for combo in combinations(SLOTS, r):
            P=frozenset(combo)
            b=build(P)
            if b is None: continue
            closure+=1
            A,eps,delta=b
            if not honest.check_units_fast(A,eps,delta): continue
            units+=1
            if honest.check_assoc_fast(A,eps,delta):
                good.append(P)
    print("closure-ok:",closure," units-ok:",units," full-liftings:",len(good), flush=True)
    # describe each by (grade->sources populated)
    def desc(P):
        d={}
        for (t,s) in P: d.setdefault(NM[t],[]).append(s)
        return {k:sorted(v) for k,v in sorted(d.items())}
    for P in good:
        print("  ", desc(P))
