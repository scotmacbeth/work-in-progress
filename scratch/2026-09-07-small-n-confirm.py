# Per-species-component comparison for small n: S(UoU)[n] (content=[n], cut-stabs+units) vs 𝒫(n).
import importlib.util, itertools
from itertools import permutations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
gen_trees=mm.gen_trees; relabel_inner=mm.relabel_inner; leaf=mm.leaf
canon=mm.canon_conj; setpart=mm.set_partitions
def aut_block(t,block,n):
    block=sorted(block); sub=[]
    for p in permutations(block):
        mp=dict(zip(block,p))
        if relabel_inner(t,mp)==t:
            sub.append(tuple((mp[x] if x in mp else x) for x in range(n)))
    return sub
def prod(subs,n):
    res={tuple(range(n))}
    for s in subs:
        nr=set()
        for x in res:
            for y in s: nr.add(tuple(x[y[i]] for i in range(n)))
        res=nr
    return frozenset(res)
def P_classes(n):
    cl=set()
    for part in setpart(range(n)):
        blocks=list(part); ch=[gen_trees(b) for b in blocks]
        for c in itertools.product(*ch):
            cl.add(canon(prod([aut_block(c[i],blocks[i],n) for i in range(len(blocks))],n),n))
    return cl
for n in [4,5]:
    P=P_classes(n)
    suu=mm.S_UoU(n,pad_max=2)
    print(f"n={n}: |𝒫(n)|={len(P)}  |S(UoU)[n]|={len(suu)}  S(UoU)⊆𝒫? {suu<=P}  separators={len(suu-P)}")
