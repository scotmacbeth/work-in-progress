"""
Does INN (the inner-object part of delta) ever genuinely depend on the inner grade vector tvec
(beyond the outer grade T)? If NO law-satisfying lifting has tvec-dependent INN, the ansatz
INN=tau^T used in the deepest-object fit is WLOG.

Test 1: perturb the trivial 𝕊×disc2 lifting so INN depends on tvec -> must break laws.
Test 2: randomized search over FULL (T,tvec)-dependent INN (OUT=id), O_s=2, and check every
        law-satisfier has INN independent of tvec (given source-preservation/grade-indep).
"""
from itertools import product
import random, honest
from free_transport import build, laws_ok
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM
O={0:['a','b'],1:['a','b']}
KEYS=[(T,tvec,s,x) for T in SS for tvec in product(SS,repeat=2) for s in S for x in O[s]]

def build_full(OUT,INN): return build(O,OUT,INN)

# Test 1: trivial transport (INN=x, i.e. tau=id) but make ONE factorization's INN depend on tvec
OUT0={k:k[3] for k in KEYS}
INN0={k:k[3] for k in KEYS}            # trivial (identity transport) -> 𝕊×disc2, laws hold
print("trivial 𝕊×disc2 laws:", laws_ok(*build_full(OUT0,INN0)))
# perturb: at T=id, make INN swap a<->b when tvec[s]==sw (depends on tvec, not just T)
INN1=dict(INN0)
for k in KEYS:
    T,tvec,s,x=k
    if T==ID and tvec[s]==(1,0):
        INN1[k]={'a':'b','b':'a'}[x]
print("tvec-dependent perturbation laws (expect False):", laws_ok(*build_full(OUT0,INN1)))

# Test 2: randomized search over full (T,tvec)-dependent INN (OUT=id). Check survivors' INN
#         factor through (T,s,x) after pushing via grade-independence. Here grade-indep is trivial
#         (object sets literally equal), so 'tvec-independent' = INN[(T,tvec,s,x)] same for all tvec.
def inn_tvec_dep(INN):
    seen={}
    for k in KEYS:
        T,tvec,s,x=k; key=(T,s,x)
        if key in seen and seen[key]!=INN[k]: return True
        seen.setdefault(key,INN[k])
    return False

rng=random.Random(7); found=0; tvecdep=0
for _ in range(400000):
    OUT={k:k[3] for k in KEYS}          # OUT=id (forced by RU1); focus on INN
    INN={k: rng.choice(O[k[0][k[2]]]) for k in KEYS}   # random object at state T[s]
    if laws_ok(*build_full(OUT,INN)):
        found+=1
        if inn_tvec_dep(INN): tvecdep+=1
print(f"Test2 (OUT=id, random INN full tvec-dep): survivors={found}, of which tvec-DEPENDENT={tvecdep}")
