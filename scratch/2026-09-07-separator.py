import importlib.util, itertools
from itertools import permutations, combinations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
leaf=mm.leaf; UNIT=mm.UNIT; oleaf=mm.oleaf; onode=mm.onode; N=mm.node
relabel_outer=mm.relabel_outer; gen_trees=mm.gen_trees; relabel_inner=mm.relabel_inner

# labels a..h = 0..7
a,b,c,d,e,f,g,h=range(8)
# inner trees
V_ab = oleaf(N(leaf(a),leaf(b)))
V_c=oleaf(leaf(c)); V_d=oleaf(leaf(d))
V_ef = oleaf(N(leaf(e),leaf(f)))
V_g=oleaf(leaf(g)); V_h=oleaf(leaf(h))
W_A = onode(V_ab, onode(V_c,V_d))
W_B = onode(V_ef, onode(V_g,V_h))
w = onode(W_A, W_B)

# stabilizer in S_8
def stab(o,n=8):
    G=[]
    for p in permutations(range(n)):
        mp=dict(zip(range(n),p))
        if relabel_outer(o,mp)==o: G.append(p)
    return G
G=stab(w)
print("U o U structure w stabilizer order =", len(G))

# identify G structure: orbits
def orbits(G,n=8):
    seen=set(); orbs=[]
    for x in range(n):
        if x in seen: continue
        orb=set(p[x] for p in G); orbs.append(sorted(orb)); seen|=orb
    return orbs
print("orbits:", orbits(G))

Gset=set(G)
# Check: is G a product of tree groups on some partition? i.e. is G in 𝒫(8)?
# 𝒫 generator: partition -> per-block tree -> Aut fixing complement -> product.
def set_partitions(elts):
    elts=list(elts)
    if not elts: yield []; return
    fst=elts[0]; rest=elts[1:]
    for sm in set_partitions(rest):
        for i in range(len(sm)):
            yield sm[:i]+[sm[i]+[fst]]+sm[i+1:]
        yield sm+[[fst]]

def aut_on_block(t, block, n=8):
    block=sorted(block); sub=[]
    for p in permutations(block):
        mp=dict(zip(block,p))
        if relabel_inner(t,mp)==t:
            sub.append(tuple((mp[x] if x in mp else x) for x in range(n)))
    return sub

def prod_group(subs,n=8):
    res={tuple(range(n))}
    for s in subs:
        nr=set()
        for x in res:
            for y in s:
                nr.add(tuple(x[y[i]] for i in range(n)))
        res=nr
    return frozenset(res)

def conj_classes_equal(H1,H2,n=8):
    # is H1 conjugate to H2 ?
    if len(H1)!=len(H2): return False
    H2=set(H2)
    H1l=list(H1)
    for gp in permutations(range(n)):
        gm=dict(zip(range(n),gp)); gi=[0]*n
        for i,x in enumerate(gp): gi[x]=i
        conj=set(tuple(gm[hh[gi[j]]] for j in range(n)) for hh in H1l)
        if conj==H2: return True
    return False

# Search: is Gset conjugate to any product-of-tree-groups? (only need to test products with same order 32 and same orbit shape)
found=False
target_order=len(Gset)
count_checked=0
import sys
for part in set_partitions(range(8)):
    blocks=[bl for bl in part]
    # quick order bound: product of |Aut(tree)| must equal 32
    choices=[gen_trees(bl) for bl in blocks]
    for choice in itertools.product(*choices):
        subs=[aut_on_block(choice[i],blocks[i]) for i in range(len(blocks))]
        order=1
        for s in subs: order*=len(s)
        if order!=target_order: continue
        H=prod_group(subs)
        count_checked+=1
        if conj_classes_equal(Gset,H):
            found=True
            print("  G IS a product of tree groups on partition", [sorted(bl) for bl in blocks], "trees", choice)
            break
    if found: break
print("checked", count_checked, "order-32 product candidates")
print("G is a product-of-tree-groups (in 𝒫)?", found)
print(">>> If False: G is a SEPARATOR: U o U stabilizer NOT realizable by any flat B∘U  => converse HOLDS for U")
