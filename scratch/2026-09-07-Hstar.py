import importlib.util, itertools
from itertools import permutations, combinations
spec=importlib.util.spec_from_file_location('m','scratch/2026-09-07-UoU-vs-LoU.py')
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
leaf=mm.leaf; N=mm.node; relabel_inner=mm.relabel_inner; gen_trees=mm.gen_trees

n=8
a,b,c,d,e,f,g,h=range(8)
# G generators
def perm_from_cycles(cycles):
    p=list(range(n))
    for cyc in cycles:
        for i in range(len(cyc)):
            p[cyc[i]]=cyc[(i+1)%len(cyc)]
    return tuple(p)
gens=[perm_from_cycles([(a,b)]),perm_from_cycles([(c,d)]),perm_from_cycles([(e,f)]),
      perm_from_cycles([(g,h)]),perm_from_cycles([(a,e),(b,f),(c,g),(d,h)])]
def closure(gens):
    G={tuple(range(n))}; frontier=list(G)
    while frontier:
        x=frontier.pop()
        for gg in gens:
            y=tuple(x[gg[i]] for i in range(n))
            if y not in G: G.add(y); frontier.append(y)
    return G
G=closure(gens)
print("|G| =", len(G))

Gset=G
def is_invariant_tree(t, S):
    # does every g in G, restricted, fix tree t on support S (with S a G-invariant set)?
    Ssort=sorted(S)
    for gp in G:
        # g must map S to S
        if any(gp[x] not in S for x in S): return False
        m={x:gp[x] for x in S}
        if relabel_inner(t,m)!=t: return False
    return True
def stab_of_tree(t,S):
    # Aut(t) x Sym(complement) as subgroup of S_n
    Ssort=sorted(S); comp=[x for x in range(n) if x not in S]
    aut=[]
    for p in permutations(Ssort):
        m=dict(zip(Ssort,p))
        if relabel_inner(t,m)==t: aut.append(p)
    sub=set()
    for al in aut:
        am=dict(zip(Ssort,al))
        for cp in permutations(comp):
            cm=dict(zip(comp,cp))
            sub.add(tuple((am[x] if x in am else cm[x]) for x in range(n)))
    return frozenset(sub)

# G-invariant supports = unions of G-orbits. orbits:
orbs=[]; seen=set()
for x in range(n):
    if x in seen: continue
    o=sorted(set(p[x] for p in G)); orbs.append(o); seen|=set(o)
print("orbits:", orbs)
# candidate supports: nonempty unions of orbits
supports=[]
for r in range(1,len(orbs)+1):
    for combo in combinations(range(len(orbs)),r):
        S=set()
        for i in combo: S|=set(orbs[i])
        supports.append(frozenset(S))
print("G-invariant supports sizes:", [len(S) for S in supports])

# collect all single-U stabilizers that CONTAIN G (i.e. G-invariant trees)
Hstar=frozenset(permutations(range(n)))  # start with everything
gen_stabs=[]
for S in supports:
    for t in gen_trees(sorted(S)):
        if is_invariant_tree(t,S):
            st=stab_of_tree(t,S)
            if Gset<=st:
                gen_stabs.append((S,t,st))
print("#single-U stabilizers containing G:", len(gen_stabs))
for (S,t,st) in gen_stabs:
    Hstar=Hstar & st
print("|H*| (intersection of all single-U-stabs containing G) =", len(Hstar))
print("H* == G ?", Hstar==Gset)
if Hstar==Gset:
    print(">>> G IS a finite intersection of single-U stabilizers (G in S_1). ARGUMENT FAILS: poly∘U can realize G.")
else:
    print(">>> H* strictly bigger than G => G NOT in S_1 => G is a genuine separator. Extra elements:", len(Hstar)-len(Gset))
