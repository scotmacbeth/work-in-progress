import importlib.util, itertools
from itertools import permutations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
gen_trees=mm.gen_trees; relabel_inner=mm.relabel_inner; leaf=mm.leaf
canon=mm.canon_conj; setpart=mm.set_partitions
n=4
def aut_block(t,block):
    block=sorted(block); sub=[]
    for p in permutations(block):
        mp=dict(zip(block,p))
        if relabel_inner(t,mp)==t: sub.append(tuple((mp[x] if x in mp else x) for x in range(n)))
    return sub
def prod(subs):
    res={tuple(range(n))}
    for s in subs:
        nr=set()
        for x in res:
            for y in s: nr.add(tuple(x[y[i]] for i in range(n)))
        res=nr
    return frozenset(res)
P={}
for part in setpart(range(n)):
    blocks=list(part); ch=[gen_trees(b) for b in blocks]
    for c in itertools.product(*ch):
        H=prod([aut_block(c[i],blocks[i]) for i in range(len(blocks))])
        P[canon(H,n)]=(part,c,len(H))
Pset=set(P)
# reconstruct S_UoU groups with their representative structures
ground=list(range(n)); 
suu_detail=[]
for part in mm.set_partitions(ground):
    bt=[gen_trees(b) for b in part]
    for choice in itertools.product(*bt):
        real=list(choice)
        for pad in range(3):
            items=real+[mm.UNIT]*pad
            for o in mm.gen_outer_trees(items):
                st=mm.stab_of_outer(o,n)
                suu_detail.append((canon(st,n),o,st))
suu={c for (c,o,st) in suu_detail}
print("𝒫(4) classes (order):", sorted(len(P[k]==P[k] and canon and 0 or 0 for k in [])) if False else [P[k][2] for k in Pset])
print("separator classes:", )
for c in (suu-Pset):
    # find a witness structure and its perms
    for (cc,o,st) in suu_detail:
        if cc==c:
            print("  SEPARATOR order",len(st),"perms",sorted(st))
            print("   witness outer structure:",o)
            break
