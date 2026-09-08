#!/usr/bin/env python3
"""
Verify the SUPPORT-INDECOMPOSABLE decomposition machinery used in Theorem S.

For K <= Sym(Omega), a *support-splitting* is a partition supp(K)=|_|C_t with
K = prod_t K_t,  K_t = {k in K : supp(k) subset C_t}.  The finest one exists
(common refinement of two splittings is a splitting -- Lemma), giving canonical
support-indecomposable direct factors.  Their multiset of degrees |C_t| is a
CONJUGACY INVARIANT.

We check:
  (1) For Young product S2 x S2 <= S4  -> two factors, degrees {2,2}.
  (2) For diagonal <(12)(34)> <= S4    -> ONE factor, degree 4 (indecomposable).
  (3) For wreath D4 = S2 wr S2 <= S4   -> ONE factor, degree 4 (indecomposable);
      order 8, NOT a Young product (Young orders in S4: {1,2,4,6,24}).
  (4) The witness bound: for K=(Hc)^d ⋊ H (H nontrivial on d blocks of size e),
      SOME support-indecomposable factor has degree >= 2e.   (block-linking)
  (5) Conjugacy invariance of the degree-multiset (random conjugation).
"""
from itertools import permutations, product
import random

def compose(p,q):  # (p after q)
    return tuple(p[q[i]] for i in range(len(q)))
def support(p):
    return set(i for i in range(len(p)) if p[i]!=i)

def group_from_gens(gens, n):
    ident = tuple(range(n))
    G = {ident}
    frontier = [ident]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = compose(g,x)
            if y not in G:
                G.add(y); frontier.append(y)
    return G

def finest_support_splitting(G, n):
    """Return list of parts (frozensets) of the finest support-splitting on supp(G)."""
    supp = set()
    for g in G: supp |= support(g)
    # Start with the discrete partition on supp; a splitting must keep supp(g) inside one part.
    # Finest splitting = finest partition P of supp s.t. every g in G has supp(g) within a block,
    # AND K = prod of K_t (automatic once support-contained: each g decomposes as product of its
    # restrictions to blocks, and each restriction is in G? NO - need restrictions in G).
    # Correct construction: the finest splitting is the finest partition such that
    #   (a) each g's support lies in a single block  -> merge blocks that some g's support spans
    # is NECESSARY but we must ALSO ensure the block-restrictions lie in G.
    # We compute the finest partition satisfying BOTH by iterative coarsening:
    #   parts = singletons of supp; repeat: for each g, the blocks meeting supp(g) that are
    #   "linked" -- we merge blocks b,b' if there is g in G whose restriction to b∪(rest) is NOT
    #   realizable, i.e. we cannot split g. Practically: two points x,y must be together iff there
    #   is NO way to write every group element as a product respecting a separation.
    # Simplest correct method for small groups: try ALL partitions refining the "support-contained"
    # constraint and pick the finest that is a genuine splitting (restrictions land in G).
    supp = sorted(supp)
    m = len(supp)
    if m==0: return []
    idx = {x:i for i,x in enumerate(supp)}
    # candidate: a partition is valid splitting iff for every g in G and every block C,
    #   the restriction g|C (identity off C) is in G, and product of restrictions = g.
    def restriction(g, C):
        r = list(range(n))
        for x in C:
            r[x]=g[x]
        return tuple(r)
    def is_splitting(parts):
        for g in G:
            prod_check = list(range(n))
            for C in parts:
                rg = restriction(g,C)
                if rg not in G:
                    return False
        return True
    # enumerate set partitions of supp (Bell number; fine for m<=6)
    def set_partitions(elts):
        if not elts:
            yield []
            return
        first = elts[0]
        for rest in set_partitions(elts[1:]):
            # add first to each existing block, or as new block
            for i in range(len(rest)):
                yield rest[:i]+[rest[i]+[first]]+rest[i+1:]
            yield rest+[[first]]
    best = None
    for parts in set_partitions(supp):
        parts_fs = [frozenset(b) for b in parts]
        if is_splitting(parts_fs):
            # finest = maximize number of parts
            if best is None or len(parts_fs) > len(best):
                best = parts_fs
    return best

def degree_multiset(G,n):
    parts = finest_support_splitting(G,n)
    return sorted(len(p) for p in parts)

def conjugate(G, s, n):
    sinv = [0]*n
    for i in range(n): sinv[s[i]]=i
    sinv = tuple(sinv)
    return set(compose(s, compose(g, sinv)) for g in G)

# ---- Cases ----
n=4
# (1) Young S2 x S2 = <(0 1),(2 3)>
Y = group_from_gens([(1,0,2,3),(0,1,3,2)], n)
print("S2xS2 order", len(Y), "degree-multiset", degree_multiset(Y,n), "(expect [2,2])")
# (2) diagonal <(01)(23)>
Dg = group_from_gens([(1,0,3,2)], n)
print("<(01)(23)> order", len(Dg), "degree-multiset", degree_multiset(Dg,n), "(expect [4])")
# (3) D4 = S2 wr S2 : gens (01),(23) within blocks and (02)(13) swap blocks {0,1},{2,3}
D4 = group_from_gens([(1,0,2,3),(0,1,3,2),(2,3,0,1)], n)
print("D4=S2wrS2 order", len(D4), "degree-multiset", degree_multiset(D4,n), "(expect [4]; order 8)")
young_orders = set()
# Young orders in S4: products of factorials over compositions of 4
from math import factorial
def comps(n):
    if n==0:
        yield ()
        return
    for first in range(1,n+1):
        for rest in comps(n-first):
            yield (first,)+rest
for c in comps(4):
    young_orders.add(int(1))  # placeholder
young_orders = set()
for c in comps(4):
    o=1
    for part in c: o*=factorial(part)
    young_orders.add(o)
print("Young subgroup orders in S4:", sorted(young_orders), "-> D4 order 8 in it?", 8 in young_orders)

# (5) conjugacy invariance
random.seed(1)
for name,G in [("S2xS2",Y),("diag",Dg),("D4",D4)]:
    s = list(range(n)); random.shuffle(s); s=tuple(s)
    Gc = conjugate(G,s,n)
    assert degree_multiset(G,n)==degree_multiset(Gc,n), name
print("conjugacy-invariance of degree-multiset: OK")

# (4) witness bound with e=2, d=2, Hc=1, H=S2 (so K = 1^2 ⋊ S2 acting on 2 blocks of size 2 = D... )
# blocks {0,1},{2,3}; H swaps blocks rigidly: (0 2)(1 3). Hc trivial.
n=4
Kw = group_from_gens([(2,3,0,1)], n)   # single block-swap, e=2,d=2
print("witness (Hc=1,e=2,d=2): order",len(Kw),"degree-multiset",degree_multiset(Kw,n),
      "-> has factor degree >= 2e=4 ?", max(degree_multiset(Kw,n))>=4)
# witness with Hc=S2,e=2,d=2 : = D4 (already), factor degree 4 >= 2e=4
print("witness (Hc=S2,e=2,d=2): =D4 factor",max(degree_multiset(D4,n)),">=4")
