import importlib.util, itertools
from itertools import permutations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
leaf=mm.leaf; oleaf=mm.oleaf; onode=mm.onode; N=mm.node
relabel_outer=mm.relabel_outer; gen_trees=mm.gen_trees; relabel_inner=mm.relabel_inner
a,b,c,d,e,f,g,h=range(8)
V_ab=oleaf(N(leaf(a),leaf(b))); V_c=oleaf(leaf(c)); V_d=oleaf(leaf(d))
V_ef=oleaf(N(leaf(e),leaf(f))); V_g=oleaf(leaf(g)); V_h=oleaf(leaf(h))
w=onode(onode(V_ab,onode(V_c,V_d)), onode(V_ef,onode(V_g,V_h)))
# stabilizer
G=[]
for p in permutations(range(8)):
    mp=dict(zip(range(8),p))
    if relabel_outer(w,mp)==w: G.append(p)
print("stab order =", len(G))
# orbits
seen=set(); orbs=[]
for x in range(8):
    if x in seen: continue
    orb=sorted(set(p[x] for p in G)); orbs.append(orb); seen|=set(orb)
print("orbits:", orbs)
# support-splitting: can support (all 8) be partitioned into C1,C2 with G = {g:supp in C1} x {g:supp in C2}?
def supp(p): return frozenset(i for i in range(8) if p[i]!=i)
Gset=set(G)
# G is support-decomposable iff exists nontrivial partition of support into unions s.t. every g factors.
# test: the subgroup of G-elements supported in a proper subset S generates G together with complement.
# Simplest: find finest splitting by union-find on "points linked if some g in G moves both with connected support"
# Two points linked if exists g in G with both in supp(g) and g support-"connected". Use: build graph, x~y if some g in G has x,y in supp(g). Then components = coarsest possible blocks; G decomposes over components iff each g supported within one component.
import collections
parent=list(range(8))
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
def uni(x,y): parent[find(x)]=find(y)
for p in G:
    s=sorted(supp(p))
    for i in range(1,len(s)): uni(s[0],s[i])
comps=collections.defaultdict(list)
for x in range(8): comps[find(x)].append(x)
comps=[sorted(v) for v in comps.values()]
print("support-connected components:", comps)
# G support-decomposable iff #components>1 AND every g supported within one comp (auto by construction of components? no)
decomp = len(comps)>1
print("support-INDECOMPOSABLE (single component)?", len(comps)==1)
# tree-group orders possible on 8 leaves of form mu(A,B): A,B 4-leaf. |Aut| in:
# A≇B: |Aut(A)|*|Aut(B)|, each in {2,8} (caterpillar/balanced) -> {4,16,64}
# A≅B: 2*|Aut(A)|^2, |Aut(A)| in {2,8} -> {8,128}
print("possible single-tree-group orders on 8 leaves:", sorted({4,16,64,8,128}))
print("G order 32 in that set?", 32 in {4,16,64,8,128})
print(">>> G support-indecomposable & order 32 not a tree-group order => G NOT a product of tree-groups => SEPARATOR")
