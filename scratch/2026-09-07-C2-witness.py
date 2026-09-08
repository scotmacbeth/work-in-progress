import importlib.util
from itertools import permutations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
leaf=mm.leaf; UNIT=mm.UNIT; oleaf=mm.oleaf; onode=mm.onode; relabel_outer=mm.relabel_outer
gen_trees=mm.gen_trees; relabel_inner=mm.relabel_inner
n=4
# rigid 2-label block via unit: b(i,j) = inner tree mu(i, mu(j, E'))?  Actually inner unit absorbs at inner level!
# Careful: at INNER level, mu(j,E') would use inner unit -> ABSORBED = j. So build rigidity at OUTER level:
# outer part W = mu(V_i, mu(V_j, E'_outerleaf)) where V_i,V_j inner leaves and E' is inner-unit AS OUTER LEAF.
V0=oleaf(leaf(0)); V1=oleaf(leaf(1)); V2=oleaf(leaf(2)); V3=oleaf(leaf(3)); Eu=oleaf(UNIT)
WL=onode(V0, onode(V2, Eu))   # outer: mu(0, mu(2, E'))
WR=onode(V1, onode(V3, Eu))   # outer: mu(1, mu(3, E'))
w=onode(WL,WR)
G=[p for p in permutations(range(4)) if relabel_outer(w,dict(zip(range(4),p)))==w]
print("witness w = mu( mu(0,mu(2,E')), mu(1,mu(3,E')) )")
print("Stab(w) =", G, " order", len(G))
print("is it <(01)(23)> ?", set(G)=={(0,1,2,3),(1,0,3,2)})
# content each-once?
def content(o):
    if o==('OU',): return []
    if o[0]=='OL':
        def lv(t):
            if t==UNIT: return []
            if t[0]=='L': return [t[1]]
            return lv(t[1][0])+lv(t[1][1])
        return lv(o[1])
    return content(o[1][0])+content(o[1][1])
print("content:", sorted(content(w)), "each-once?", sorted(content(w))==[0,1,2,3])
# Now: is <(01)(23)> a product of tree groups 𝒫(4)? Show NO by the order argument, and brute check.
target={(0,1,2,3),(1,0,3,2)}
import itertools
def aut_block(t,block):
    block=sorted(block); sub=[]
    for p in permutations(block):
        mp=dict(zip(block,p))
        if relabel_inner(t,mp)==t: sub.append(tuple((mp[x] if x in mp else x) for x in range(4)))
    return sub
def prod(subs):
    res={(0,1,2,3)}
    for s in subs:
        nr=set()
        for x in res:
            for y in s: nr.add(tuple(x[y[i]] for i in range(4)))
        res=nr
    return frozenset(res)
def setpart(elts):
    elts=list(elts)
    if not elts: yield []; return
    fst,rest=elts[0],elts[1:]
    for sm in setpart(rest):
        for i in range(len(sm)): yield sm[:i]+[sm[i]+[fst]]+sm[i+1:]
        yield sm+[[fst]]
found=False
allP=set()
for part in setpart(range(4)):
    blocks=list(part); ch=[gen_trees(b) for b in blocks]
    for c in itertools.product(*ch):
        H=prod([aut_block(c[i],blocks[i]) for i in range(len(blocks))])
        allP.add(H)
# is target conjugate to any H in allP?
def conj(H,g):
    gm=dict(zip(range(4),g)); gi=[0]*4
    for i,x in enumerate(g): gi[x]=i
    return frozenset(tuple(gm[hh[gi[j]]] for j in range(4)) for hh in H)
tg=frozenset(target)
inP=any(conj(H,g)==tg for H in allP for g in permutations(range(4)))
print("Is <(01)(23)> conjugate to a product of tree groups (in 𝒫(4))?", inP)
print(">>> Stab(w)=<(01)(23)> is an orbit-type of (U∘U)[4] but NOT of any (poly∘U)[4]  => U∘U ≇ poly∘U")
