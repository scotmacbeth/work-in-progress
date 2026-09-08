"""
General free-symmetric-operad machinery for the stabilizer-flatness search.

A symmetric operad is given by a SIGNATURE: a list of operations, each an
(arity, symmetry_group) pair, where symmetry_group is a list of permutations of
range(arity) (as tuples g with new_children[j] = children[g[j]]).  Arity-0
operations are CONSTANTS (a_0 = number of arity-0 ops, counted with the trivial
group).  The associated analytic monad M = free operad on the signature; its
algebras are Sigma-algebras; M(X) = Sigma-trees with leaves in X (plus constants
as content-free nullary nodes).  NO extra relations (unlike the unital magma U,
whose unit is absorptive; here a "constant" is a plain nullary op, the clean
free-operad a_0>0 analogue of U).

TREE REPRESENTATION (all canonical unless noted):
  label leaf : ('lf', x)          x a label
  op node    : ('op', i, kids)    i op-index, kids = tuple of child trees, len=arity
               a constant is ('op', i, ())

M non-flat  <=>  some op has a nontrivial symmetry group (=> species not free).
"""
from itertools import combinations, permutations, product
from functools import lru_cache

# ---------------------------------------------------------------------------
# Signature object
# ---------------------------------------------------------------------------
class Sig:
    def __init__(self, name, ops):
        # ops: list of (arity, symgroup) ; symgroup list of tuples perm of range(arity)
        self.name = name
        self.ops = ops
        self.a0 = sum(1 for (ar, g) in ops if ar == 0)
        # non-flat iff some op has |symgroup|>1
        self.nonflat = any(len(g) > 1 for (ar, g) in ops)

    def arity(self, i): return self.ops[i][0]
    def sym(self, i):   return self.ops[i][1]

# ---------------------------------------------------------------------------
# Canonicalisation under node symmetry groups
# ---------------------------------------------------------------------------
def canon(sig, t):
    """Canonical form of an (already structurally built) tree under node symmetries."""
    if t[0] == 'lf':
        return t
    i, kids = t[1], t[2]
    ck = tuple(canon(sig, c) for c in kids)
    g = sig.sym(i)
    if len(ck) <= 1 or len(g) == 1:
        return ('op', i, ck)
    best = min(tuple(ck[gg[j]] for j in range(len(ck))) for gg in g)
    return ('op', i, best)

def relabel(sig, t, m):
    if t[0] == 'lf':
        return ('lf', m[t[1]])
    i, kids = t[1], t[2]
    return canon(sig, ('op', i, tuple(relabel(sig, c, m) for c in kids)))

def content(t):
    """multiset (as sorted list) of labels appearing at leaves."""
    if t[0] == 'lf':
        return [t[1]]
    out = []
    for c in t[2]:
        out += content(c)
    return out

# ---------------------------------------------------------------------------
# Enumeration of single-M trees with a given label set + up to `pad` constants
# ---------------------------------------------------------------------------
def gen_trees(sig, labels, pad, max_nodes):
    """All canonical Sigma-trees with content == set(labels) (each once) using
       between 0 and `pad` extra constant-leaves, and at most max_nodes internal
       op-nodes total.  Returns a set."""
    labels = tuple(sorted(labels))
    memo = {}
    const_ops = [i for i in range(len(sig.ops)) if sig.arity(i) == 0]

    def build(lbls, nc, nodes_left):
        """trees with exactly label-set lbls, exactly nc constant leaves, <=nodes_left op-nodes."""
        key = (lbls, nc, nodes_left)
        if key in memo:
            return memo[key]
        res = set()
        # base: single label leaf
        if len(lbls) == 1 and nc == 0:
            res.add(('lf', lbls[0]))
        # base: a single constant  (uses one op-node)
        if len(lbls) == 0 and nc == 1 and nodes_left >= 1:
            for ci in const_ops:
                res.add(('op', ci, ()))
        # recursive: an op-node of arity k>=1
        if nodes_left >= 1 and (len(lbls) + nc) >= 1:
            for oi, (ar, g) in enumerate(sig.ops):
                if ar < 1:
                    continue
                # distribute lbls (as a set) and nc constants among ar children
                for lab_assign in _set_functions(lbls, ar):
                    for con_assign in _compositions(nc, ar):
                        # each child gets lab_assign[j] labels, con_assign[j] consts
                        child_opts = []
                        ok = True
                        for j in range(ar):
                            cj_lbls = lab_assign[j]
                            cj_nc = con_assign[j]
                            if len(cj_lbls) == 0 and cj_nc == 0:
                                ok = False
                                break
                            opts = build(cj_lbls, cj_nc, nodes_left - 1)
                            if not opts:
                                ok = False
                                break
                            child_opts.append(list(opts))
                        if not ok:
                            continue
                        for combo in product(*child_opts):
                            # node uses 1 op-node; children used up to nodes_left-1 already;
                            # enforce total node budget: sum of nodes in combo + 1 <= nodes_left
                            if _count_nodes(('op', oi, combo)) <= nodes_left:
                                res.add(canon(sig, ('op', oi, combo)))
        memo[key] = res
        return res

    out = set()
    for p in range(pad + 1):
        out |= build(labels, p, max_nodes)
    return out

def _count_nodes(t):
    if t[0] == 'lf':
        return 0
    return 1 + sum(_count_nodes(c) for c in t[2])

def _set_functions(lbls, k):
    """all ways to split the set lbls into an ordered k-tuple of disjoint subsets covering lbls."""
    lbls = list(lbls)
    if k == 1:
        yield (tuple(lbls),)
        return
    n = len(lbls)
    # assign each label to one of k children
    for assign in product(range(k), repeat=n):
        parts = [tuple(lbls[i] for i in range(n) if assign[i] == j) for j in range(k)]
        yield tuple(parts)

def _compositions(nc, k):
    """all ordered k-tuples of nonneg ints summing to nc."""
    if k == 1:
        yield (nc,)
        return
    for first in range(nc + 1):
        for rest in _compositions(nc - first, k - 1):
            yield (first,) + rest

# ---------------------------------------------------------------------------
# Stabilizer of a tree (as a subgroup of Sym(ground)), and group utilities
# ---------------------------------------------------------------------------
def stab(sig, t, ground):
    G = []
    gl = list(ground)
    for p in permutations(gl):
        m = dict(zip(gl, p))
        if relabel(sig, t, m) == t:
            # represent as perm tuple on 0..n-1 with ground mapped to indices
            G.append(_as_perm(m, ground))
    return frozenset(G)

def _as_perm(m, ground):
    # m: dict on ground; return tuple over range(n) where index = position in sorted(ground) union...
    # We use ground = range(n) throughout the M o M search, so simplest: assume ground==range(n).
    n = len(ground)
    return tuple(m[i] for i in range(n))

def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(a):
    r = [0] * len(a)
    for i, x in enumerate(a):
        r[x] = i
    return tuple(r)

def conj_group(H, g):
    """g H g^{-1}"""
    gi = inv(g)
    return frozenset(tuple(g[h[gi[j]]] for j in range(len(g))) for h in H)

def canon_conj(H, n):
    best = None
    for g in permutations(range(n)):
        c = conj_group(H, g)
        key = tuple(sorted(c))
        if best is None or key < best:
            best = key
    return best

# ---------------------------------------------------------------------------
# Support-indecomposable factorisation of a permutation group
# ---------------------------------------------------------------------------
def supp(p):
    return frozenset(i for i in range(len(p)) if p[i] != i)

def support_components(H, n):
    """finest partition of the moved points s.t. every element of H is supported
       within one block (union-find linking points co-moved by some element)."""
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def uni(x, y):
        parent[find(x)] = find(y)
    for p in H:
        s = sorted(supp(p))
        for i in range(1, len(s)):
            uni(s[0], s[i])
    from collections import defaultdict
    comps = defaultdict(list)
    moved = set()
    for p in H:
        moved |= supp(p)
    for x in moved:
        comps[find(x)].append(x)
    return [sorted(v) for v in comps.values()]

def factor_on(H, block):
    """restrict H to permutations of `block` (elements of H supported within block),
       returned as a permutation group on 0..len(block)-1."""
    bset = set(block)
    idx = {b: i for i, b in enumerate(sorted(block))}
    fac = set()
    fac.add(tuple(range(len(block))))
    for p in H:
        if supp(p) <= bset:
            fac.add(tuple(idx[p[b]] for b in sorted(block)))
    return frozenset(fac)

def indecomposable_factors(H, n):
    """list of (degree, canonical-conjugacy-key) for each support-indecomposable factor."""
    comps = support_components(H, n)
    facs = []
    for blk in comps:
        F = factor_on(H, blk)
        d = len(blk)
        facs.append((d, canon_conj(F, d)))
    return facs
