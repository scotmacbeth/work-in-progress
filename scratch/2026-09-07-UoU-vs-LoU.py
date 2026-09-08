"""
Decisive test:  does  S(U o U) = S(L o U) = S_1 (finite intersections of single-U stabilizers)?
If yes at every n (and by the all-aleph0 lemma) then  U o U  ≅  L o U  ==> THM3 necessity FALSE for U.

We enumerate ACTUAL U o U structures (outer comm-unital-magma tree whose leaves are inner
comm-unital-magma elements, inner unit E' allowed as an outer leaf, outer unit absorbed),
with real content exactly [n] (each label once) and a bounded number of inner-unit pad leaves,
outer tree size bounded. Compute stabilizer in S_n by brute force. Collect the SET of conj classes.
Compare with S_1 (intersections of single-U-element stabilizers).
"""
import itertools
from itertools import permutations, combinations

# ---------- inner comm-binary trees over label set (each label once) ----------
def node(a,b): return ('N', tuple(sorted((a,b))))
def leaf(x):   return ('L', x)
UNIT = ('U',)   # inner unit E'

def gen_trees(labels):
    labels=tuple(labels); n=len(labels)
    if n==0: return []
    if n==1: return [leaf(labels[0])]
    res=set(); first=labels[0]; rest=labels[1:]
    for r in range(len(rest)+1):
        for combo in combinations(rest,r):
            left=(first,)+combo; right=tuple(x for x in rest if x not in combo)
            if not right: continue
            for lt in gen_trees(left):
                for rt in gen_trees(right):
                    res.add(node(lt,rt))
    return list(res)

def relabel_inner(t, m):
    if t==UNIT: return UNIT
    if t[0]=='L': return leaf(m[t[1]])
    a,b=t[1]; return node(relabel_inner(a,m), relabel_inner(b,m))

# ---------- outer comm-binary trees whose leaves are inner elements ----------
# outer structure: either OUTER_UNIT ('OU',) [only when no content] or comm-binary tree
# with leaves = inner elements (tuples). Represent outer leaf as ('OL', inner_elt).
def onode(a,b): return ('ON', tuple(sorted((a,b))))
def oleaf(inner): return ('OL', inner)

def gen_outer_trees(leaf_items):
    """comm binary trees with the given multiset of leaf_items (each used once as a distinct slot).
       leaf_items: list of inner elements (may repeat as equal tuples). We must treat equal items
       as indistinguishable for canonical form but they occupy distinct leaves. Enumerate by
       treating positions distinct then canonicalizing via sorted tuples."""
    items=list(leaf_items); k=len(items)
    # generate all comm binary trees over k distinguishable slots, then substitute items, canonicalize
    idx=list(range(k))
    def build(slots):
        if len(slots)==1: return [oleaf(items[slots[0]])]
        res=set(); first=slots[0]; rest=slots[1:]
        for r in range(len(rest)+1):
            for combo in combinations(rest,r):
                left=(first,)+combo; right=tuple(x for x in rest if x not in combo)
                if not right: continue
                for lt in build(left):
                    for rt in build(right):
                        res.add(onode(lt,rt))
        return list(res)
    if k==0: return [('OU',)]
    if k==1: return [oleaf(items[0])]
    return list(set(build(idx)))

def relabel_outer(o, m):
    if o==('OU',): return ('OU',)
    if o[0]=='OL': return oleaf(relabel_inner(o[1], m))
    a,b=o[1]; return onode(relabel_outer(a,m), relabel_outer(b,m))

def stab_of_outer(o, n):
    G=[]
    for p in permutations(range(n)):
        m=dict(zip(range(n),p))
        if relabel_outer(o,m)==o:
            G.append(p)
    return frozenset(G)

# ---------- enumerate U o U structures with content [n], up to pad & size ----------
def set_partitions(elts):
    elts=list(elts)
    if not elts:
        yield []; return
    first=elts[0]; rest=elts[1:]
    for smaller in set_partitions(rest):
        # add first to an existing block
        for i in range(len(smaller)):
            yield smaller[:i]+[smaller[i]+[first]]+smaller[i+1:]
        # or new block
        yield smaller+[[first]]

def S_UoU(n, pad_max=2, verbose=False):
    ground=list(range(n))
    stabs=set()
    count=0
    for part in set_partitions(ground):
        # each block -> an inner tree over that block; choose trees
        block_tree_choices=[gen_trees(b) for b in part]
        for choice in itertools.product(*block_tree_choices):
            real_inner=list(choice)              # inner trees carrying labels
            for pad in range(pad_max+1):
                leaf_items = real_inner + [UNIT]*pad
                for o in gen_outer_trees(leaf_items):
                    st=stab_of_outer(o,n)
                    # canonical conj class rep: sort by ... use frozenset of sorted images; conj by normalizing
                    stabs.add(canon_conj(st,n))
                    count+=1
    if verbose: print(f"  U o U: {count} structures, {len(stabs)} conj-classes of stabilizers")
    return stabs

# ---------- S_1 : intersections of single-U-element stabilizers ----------
def single_U_gens(n):
    ground=list(range(n)); gens=set()
    for r in range(1,n+1):
        for S in combinations(ground,r):
            Slist=list(S); comp=[x for x in ground if x not in S]
            for t in gen_trees(Slist):
                # stab = {sigma: sigma|S in Aut(t), sigma|comp arbitrary}
                # compute Aut(t) as perms of S
                aut=[]
                for p in permutations(Slist):
                    m=dict(zip(Slist,p))
                    if relabel_inner(t,m)==t: aut.append(p)
                sub=set()
                for a in aut:
                    am=dict(zip(Slist,a))
                    for cp in permutations(comp):
                        cm=dict(zip(comp,cp))
                        full=tuple((am[x] if x in am else cm[x]) for x in ground)
                        sub.add(full)
                gens.add(frozenset(sub))
    return list(gens)

def canon_conj(H,n):
    # canonical rep of conjugacy class of subgroup H<=S_n: min over conjugates of sorted tuple
    best=None
    for g in permutations(range(n)):
        gm=dict(zip(range(n),g)); gi=[0]*n
        for i,x in enumerate(g): gi[x]=i
        conj=frozenset(tuple(gm[x] for x in [ (h[gi[j]]) for j in range(n)]) for h in H)
        # careful conj: (g h g^-1)(j) = g(h(g^-1(j)))
        conj=frozenset(tuple(gm[h[gi[j]]] for j in range(n)) for h in H)
        key=tuple(sorted(conj))
        if best is None or key<best: best=key
    return best

def S1_classes(n):
    gens=single_U_gens(n)
    universe=frozenset(permutations(range(n)))
    # closure under intersection
    closed=set(gens); closed.add(universe)
    frontier=list(closed)
    allset=set(closed)
    changed=True
    while changed:
        changed=False
        cur=list(allset); new=set()
        for i in range(len(cur)):
            for j in range(i,len(cur)):
                inter=cur[i]&cur[j]
                if inter not in allset and inter not in new:
                    new.add(inter)
        if new:
            allset|=new; changed=True
    return set(canon_conj(H,n) for H in allset)

if __name__=="__main__":
    for n in [3,4]:
        print(f"=== n={n} ===")
        s1=S1_classes(n)
        print(f"  |S_1 (intersections)| = {len(s1)} conj classes")
        suu=S_UoU(n, pad_max=2, verbose=True)
        print(f"  S(UoU) subset of S_1 ? {suu<=s1}")
        print(f"  S_1 subset of S(UoU) ? {s1<=suu}")
        print(f"  EQUAL ? {suu==s1}")
        if not suu<=s1:
            print("  !! U o U has EXTRA stabilizer types (separator vs L o U) -> converse HOLDS for U")
        if not s1<=suu:
            print("  L o U has types U o U lacks:", len(s1-suu))
