import importlib.util, itertools
from itertools import permutations, combinations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
gen_trees=m.gen_trees; relabel_inner=m.relabel_inner; leaf=m.leaf
canon_conj=m.canon_conj; set_partitions=m.set_partitions

def aut_tree_on_block(t, block, n):
    # Aut(t) as subgroup of S_n fixing everything outside block
    block=sorted(block); sub=[]
    for p in permutations(block):
        mp=dict(zip(block,p))
        if relabel_inner(t,mp)==t:
            full=tuple((mp[x] if x in mp else x) for x in range(n))
            sub.append(full)
    return sub  # list of perms (as tuples) fixing complement

def prod_group(list_of_subs, n):
    # direct product of subgroups each fixing others' support -> combine
    import itertools as it
    groups=[set(s) for s in list_of_subs]
    result={tuple(range(n))}
    for g in groups:
        newr=set()
        for a in result:
            for b in g:
                # compose: both fix disjoint supports so just take componentwise nontrivial
                comp=tuple(a[b[i]] for i in range(n)) # a∘b
                newr.add(comp)
        result=newr
    return frozenset(result)

def S_BoU(n):
    classes=set()
    for part in set_partitions(range(n)):
        blocks=[b for b in part]
        choices=[gen_trees(b) for b in blocks]
        for choice in itertools.product(*choices):
            subs=[aut_tree_on_block(choice[i], blocks[i], n) for i in range(len(blocks))]
            H=prod_group(subs,n)
            classes.add(canon_conj(H,n))
    return classes

def S_UoU(n, pad_max=3):
    return m.S_UoU(n, pad_max=pad_max)

for n in [3,4,5,6]:
    sbou=S_BoU(n)
    # test padding sufficiency: compare pad_max 2 vs 3
    suu2=m.S_UoU(n,pad_max=2); suu3=m.S_UoU(n,pad_max=3)
    stab_ok = (suu2==suu3)
    suu=suu3
    print(f"n={n}: |S(BoU) block-fixing products|={len(sbou)}, |S(UoU)|={len(suu)} (pad stable={stab_ok})")
    sep = suu - sbou
    print(f"   S(UoU) subset of S(BoU)? {suu<=sbou}   #separators(UoU not a block-fixing product)={len(sep)}")
    if sep:
        for c in list(sep)[:4]:
            print(f"      SEPARATOR group order={len(c)}  perms(sample)={sorted(c)[:6]}")
