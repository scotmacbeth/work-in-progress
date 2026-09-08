# Confirm the DECISIVE per-species-component facts:
#  (1) w in (U o U)[8] uses each label a..h exactly once  (so its stab G is an orbit-type of component [8])
#  (2) the 5 trees whose intersection gives G SHARE labels (=> live in higher components, irrelevant)
#  (3) restate: on component [m], poly∘U stabilizers = block-fixing products 𝒫(m); G∉𝒫(8) (already proved)
import importlib.util
from itertools import permutations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
leaf=mm.leaf; N=mm.node; oleaf=mm.oleaf; onode=mm.onode; relabel_outer=mm.relabel_outer
a,b,c,d,e,f,g,h=range(8)
V_ab=oleaf(N(leaf(a),leaf(b))); V_c=oleaf(leaf(c)); V_d=oleaf(leaf(d))
V_ef=oleaf(N(leaf(e),leaf(f))); V_g=oleaf(leaf(g)); V_h=oleaf(leaf(h))
w=onode(onode(V_ab,onode(V_c,V_d)), onode(V_ef,onode(V_g,V_h)))
# content of w: collect leaf labels
def content(o):
    if o==('OU',): return []
    if o[0]=='OL':
        t=o[1]
        def lv(t):
            if t==mm.UNIT: return []
            if t[0]=='L': return [t[1]]
            return lv(t[1][0])+lv(t[1][1])
        return lv(t)
    return content(o[1][0])+content(o[1][1])
cont=sorted(content(w))
print("content(w) =", cont, " each-once?", cont==list(range(8)))

# (2) reconstruct the 5 G-invariant trees from Hstar computation and show they share labels
import importlib.util as iu
spec2=iu.spec_from_file_location('hs','scratch/2026-09-07-Hstar.py')
# just re-derive quickly here: G-invariant trees on supports O1={a,b,e,f}, O2={c,d,g,h}, and [8]
relabel_inner=mm.relabel_inner; gen_trees=mm.gen_trees
def perm_from_cycles(cycles,n=8):
    p=list(range(n))
    for cyc in cycles:
        for i in range(len(cyc)): p[cyc[i]]=cyc[(i+1)%len(cyc)]
    return tuple(p)
G_gens=[perm_from_cycles([(a,b)]),perm_from_cycles([(c,d)]),perm_from_cycles([(e,f)]),
        perm_from_cycles([(g,h)]),perm_from_cycles([(a,e),(b,f),(c,g),(d,h)])]
def clo(gens,n=8):
    S={tuple(range(n))}; fr=list(S)
    while fr:
        x=fr.pop()
        for gg in gens:
            y=tuple(x[gg[i]] for i in range(n))
            if y not in S: S.add(y); fr.append(y)
    return S
G=clo(G_gens)
O1={a,b,e,f}; O2={c,d,g,h}
def ginv_trees(S):
    out=[]
    for t in gen_trees(sorted(S)):
        ok=True
        for gp in G:
            if any(gp[x] not in S for x in S): ok=False;break
            mm2={x:gp[x] for x in S}
            if relabel_inner(t,mm2)!=t: ok=False;break
        if ok: out.append((S,t))
    return out
inv=ginv_trees(frozenset(O1))+ginv_trees(frozenset(O2))+ginv_trees(frozenset(range(8)))
def treesupp(t):
    if t==mm.UNIT: return set()
    if t[0]=='L': return {t[1]}
    return treesupp(t[1][0])|treesupp(t[1][1])
print("\n#G-invariant single-U trees:", len(inv))
supps=[sorted(treesupp(t)) for (S,t) in inv]
for s in supps: print("   tree support:", s)
# do their supports overlap? (i.e. some label in >=2 of them)
from collections import Counter
cnt=Counter()
for s in supps:
    for x in s: cnt[x]+=1
reused=[x for x,k in cnt.items() if k>=2]
print("labels appearing in >=2 of the intersecting trees:", sorted(reused))
print("=> realizing (r∘U)-element REUSES those labels => lives in a HIGHER species component, not [8].")
print("=> On component [8], poly∘U gives only block-fixing products 𝒫(8); G∉𝒫(8). Separator stands.")
