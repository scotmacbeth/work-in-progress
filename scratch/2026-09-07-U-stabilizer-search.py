"""
Search for a separating group H in  S(U o U) \ S(B o U over flat B).

U = free commutative unital magma monad.
Single-U-element stabilizer on [n]:  Aut(tree t on support S)  x  Sym([n]\S).
S(BoU) = all FINITE INTERSECTIONS of single-U-element stabilizers.
S(UoU) = { Aut(F) ∩ Aut(P) : F a comm. binary tree on [n], P a tree-realizable cut-partition }
         (times Sym(complement) if support < [n]; we work with full support = [n]).

If some H in S(UoU) is NOT the intersection of all single-U generators containing it,
then H in S(UoU) \ S(BoU): a separator => converse holds for U (U o U not ≅ poly o U).
"""
import itertools
from itertools import permutations, combinations
from functools import lru_cache

# ---- commutative binary trees over a set of labels ----
# tree = ('L', label)  or  ('N', frozenset-like sorted tuple of two child-trees)
# canonical form: children sorted.

def leaf(x): return ('L', x)
def node(a, b):
    return ('N', tuple(sorted((a, b))))

def support(t):
    if t[0] == 'L': return frozenset([t[1]])
    a,b = t[1]; return support(a) | support(b)

def relabel(t, perm):  # perm: dict label->label
    if t[0]=='L': return leaf(perm[t[1]])
    a,b = t[1]; return node(relabel(a,perm), relabel(b,perm))

# enumerate all comm binary trees whose leaves are exactly the labels in `labels` (a tuple), each once
def gen_trees(labels):
    labels = tuple(labels)
    n = len(labels)
    if n==1:
        return [leaf(labels[0])]
    res = set()
    # split labels into two nonempty subsets (unordered), each side gets a subtree
    lab = list(labels)
    first = lab[0]
    rest = lab[1:]
    # to avoid double counting the unordered split, fix `first` in the left part
    for r in range(0, len(rest)+1):
        for combo in combinations(rest, r):
            left = (first,) + combo
            right = tuple(x for x in rest if x not in combo)
            if len(right)==0: continue
            for lt in gen_trees(left):
                for rt in gen_trees(right):
                    res.add(node(lt, rt))
    return list(res)

def aut(t):
    n = len(support(t))
    S = sorted(support(t))
    G = []
    for p in permutations(S):
        perm = dict(zip(S, p))
        if relabel(t, perm) == t:
            G.append(tuple(perm[x] for x in S))  # image tuple in order of S
    return S, G   # G = list of permutations as tuples aligned to sorted support S

# nodes of a tree = list of supports (frozensets) of every node (leaf + internal)
def node_supports(t):
    if t[0]=='L': return [support(t)]
    a,b = t[1]
    return [support(t)] + node_supports(a) + node_supports(b)

# all cut-partitions of a tree: recursively cut-here or recurse
def cuts(t):
    # returns list of partitions; each partition = frozenset of frozenset(blocks)
    if t[0]=='L':
        return [frozenset([support(t)])]
    a,b = t[1]
    res = []
    # cut here: whole t is one block
    res.append(frozenset([support(t)]))
    # recurse both children independently
    for ca in cuts(a):
        for cb in cuts(b):
            res.append(ca | cb)
    return res

# ---- permutation groups as sets of tuples over sorted domain S = [0..n-1] ----
def perm_apply_partition(perm_tuple, S, P):
    # perm_tuple aligned to sorted S (list). map label->image
    m = dict(zip(S, perm_tuple))
    newP = frozenset(frozenset(m[x] for x in block) for block in P)
    return newP

def group_from_aut_and_partition(t):
    """S(UoU) generators: for tree t (full support [n]) and each cut P,
       H = { sigma in Aut(t) : sigma preserves P }.  Return set of these H (as frozenset of perm tuples)."""
    S, G = aut(t)
    out = {}
    for P in set(cuts(t)):
        H = frozenset(g for g in G if perm_apply_partition(g, S, P) == P)
        out[P] = H
    return S, out

# ---- single-U-element stabilizer on full ground [n]: Aut(tree u on subset) x Sym(complement) ----
def single_U_stabilizers(n):
    """Return list of subgroups of S_n (as frozenset of perm tuples over 0..n-1)."""
    ground = list(range(n))
    gens = set()
    for r in range(1, n+1):
        for S in combinations(ground, r):
            comp = [x for x in ground if x not in S]
            Slist = list(S)
            for t in gen_trees(Slist):
                _, autG = aut(t)   # perms aligned to sorted support = sorted(S)
                sortedS = sorted(S)
                # build full-S_n group: on S act by autG, on comp act by ANY permutation
                subgroup = set()
                for a in autG:
                    amap = dict(zip(sortedS, a))
                    for cp in permutations(comp):
                        cmap = dict(zip(comp, cp))
                        full = tuple((amap[x] if x in amap else cmap[x]) for x in ground)
                        subgroup.add(full)
                gens.add(frozenset(subgroup))
    # also the empty-intersection = whole S_n handled in closure test as universe
    return list(gens)

def intersect(gsets):
    if not gsets:
        return None
    r = gsets[0]
    for g in gsets[1:]:
        r = r & g
    return r

def run(n, verbose=True):
    ground = list(range(n))
    universe = frozenset(permutations(ground))
    # generators for S(BoU)
    gens = single_U_stabilizers(n)
    if verbose: print(f"n={n}: #single-U generators = {len(gens)}, |S_n|={len(universe)}")
    # S(UoU) groups
    trees = gen_trees(ground)
    seen_H = set()
    separators = []
    for t in trees:
        S, hmap = group_from_aut_and_partition(t)
        for P, H in hmap.items():
            key = H
            if key in seen_H:
                continue
            seen_H.add(key)
            # closure test: intersection of all generators (and universe) containing H
            containing = [universe]  # empty intersection = whole group is allowed (B_i empty)
            for g in gens:
                if H <= g:
                    containing.append(g)
            clo = intersect(containing)
            if clo != H:
                separators.append((t, P, H, clo))
    if verbose:
        print(f"  #distinct S(UoU) groups tested = {len(seen_H)}")
        print(f"  #separators (H not an intersection of single-U stabs) = {len(separators)}")
    return separators

if __name__ == "__main__":
    for n in [4,5,6]:
        seps = run(n)
        for (t,P,H,clo) in seps[:3]:
            print("   SEPARATOR tree=",t)
            print("     cut P=", sorted([tuple(sorted(b)) for b in P]))
            print("     |H|=",len(H)," |closure|=",len(clo))
