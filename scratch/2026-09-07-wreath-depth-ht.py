"""
Verify the imprimitivity-depth invariant h_t for Theorem S'.

h_t(T) for a permutation group T on Omega (support = Omega):
  = max length of a strictly-refining chain of T-invariant partitions
    from {Omega} (top) down to {singletons} (bottom).
For a general group K (possibly intransitive), define
  h(K) = max over orbits O of K of h_t( K restricted to O ).

Claims to check:
 (A) h_t(S_2)=1, h_t(S_3)=1, h_t(S_4)=1 (primitive => 1),
     h_t(S_2 wr S_2 = D_4)=2, h_t(S_2 wr S_2 wr S_2)=3,
     h_t(S_a wr S_b)=2  (partition stabilizer, e.g. wr on 2x3),
     wreath additivity h_t(T1 wr T2) = h_t(T1)+h_t(T2).
 (B) bound: for a block-fixing (intransitive direct) product on disjoint
     supports, h = max of the factors' h.
 (C) MM-separation: 1M has constituents S_n (h=1); 1M o 1M realizes S_2 wr S_2 (h=2).
"""
from itertools import permutations, product
from functools import reduce

# ---- permutations as tuples (images of 0..n-1) ----
def compose(p, q):  # (p after q)
    return tuple(p[q[i]] for i in range(len(q)))
def group_closure(gens, n):
    ident = tuple(range(n))
    G = {ident}
    frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for s in gens:
                h = compose(s, g)
                if h not in G:
                    G.add(h); new.append(h)
        frontier = new
    return G

# ---- partitions of a set of points, as frozenset of frozensets ----
def apply_perm_to_partition(g, P):
    return frozenset(frozenset(g[x] for x in block) for block in P)
def invariant_partitions(G, points):
    pts = list(points)
    n_universe = (max(points)+1) if points else 0
    # enumerate all partitions of pts (Bell number) -- ok for |pts|<=8
    def all_partitions(lst):
        if not lst:
            yield []
            return
        first, rest = lst[0], lst[1:]
        for smaller in all_partitions(rest):
            for i in range(len(smaller)):
                yield smaller[:i] + [[first]+smaller[i]] + smaller[i+1:]
            yield [[first]] + smaller
    res = []
    for part in all_partitions(pts):
        P = frozenset(frozenset(b) for b in part)
        if all(apply_perm_to_partition(g, P) == P for g in G):
            res.append(P)
    return res

def refines(P, Q):
    # P finer than Q: every block of P is subset of some block of Q
    for b in P:
        if not any(b <= c for c in Q):
            return False
    return True

def longest_chain_length(parts):
    # longest strictly-decreasing (by refinement) chain from top {all} to bottom {singletons}
    # count = number of STEPS (edges). Build DAG P->Q if P strictly refines Q (immediate not required),
    # longest path in terms of edges.
    # memoized longest chain DOWNWARD from each partition to the singleton partition.
    parts = list(parts)
    # identify singleton partition
    from functools import lru_cache
    idx = {P:i for i,P in enumerate(parts)}
    # edges: Q (coarser) -> P (finer), P strictly refines Q
    import sys
    sys.setrecursionlimit(10000)
    memo = {}
    def down(Q):
        # longest number of steps from Q down to fully-singleton, moving to strictly finer invariant parts
        if Q in memo: return memo[Q]
        best = 0
        for P in parts:
            if P != Q and refines(P, Q):
                best = max(best, 1 + down(P))
        memo[Q] = best
        return best
    top = max(parts, key=lambda P: max(len(b) for b in P))  # {all}
    # top is the one-block partition
    for P in parts:
        if len(P) == 1:
            top = P
    return down(top)

def h_t_transitive(gens, n):
    G = group_closure(gens, n)
    points = frozenset(range(n))
    parts = invariant_partitions(G, points)
    return longest_chain_length(parts)

# ---------- wreath product construction ----------
def wreath(gensT1, n1, gensT2, n2):
    # T1 bottom (on n1), T2 top (on n2); product action on n1*n2 points
    # point (i in n2 block, j in n1 pos) -> index i*n1 + j
    n = n1*n2
    gens = []
    # bottom copies: T1 acting in block b (b in 0..n2-1)
    for b in range(n2):
        for t in gensT1:
            g = list(range(n))
            for j in range(n1):
                g[b*n1 + j] = b*n1 + t[j]
            gens.append(tuple(g))
    # top: T2 permuting blocks
    for t in gensT2:
        g = list(range(n))
        for b in range(n2):
            for j in range(n1):
                g[b*n1 + j] = t[b]*n1 + j
        gens.append(tuple(g))
    return gens, n

S2 = [(1,0)]
S3 = [(1,0,2),(0,2,1)]
S4 = [(1,0,2,3),(0,2,1,3),(0,1,3,2)]

print("h_t(S2 on 2)      =", h_t_transitive(S2,2), " expect 1")
print("h_t(S3 on 3)      =", h_t_transitive(S3,3), " expect 1 (primitive)")
print("h_t(S4 on 4)      =", h_t_transitive(S4,4), " expect 1 (primitive)")

D4gens, D4n = wreath(S2,2,S2,2)
print("h_t(S2 wr S2 =D4) =", h_t_transitive(D4gens,D4n), " expect 2")

# triple wreath S2 wr S2 wr S2 on 8
w2gens,w2n = wreath(D4gens,D4n,S2,2)   # (S2 wr S2) wr S2
print("h_t((S2wrS2)wrS2) =", h_t_transitive(w2gens,w2n), " expect 3")

# S2 wr S3 on 6  (bottom S2, top S3): partition stabilizer of 3 blocks of 2
w3gens,w3n = wreath(S2,2,S3,3)
print("h_t(S2 wr S3)     =", h_t_transitive(w3gens,w3n), " expect 2")

# S3 wr S2 on 6
w4gens,w4n = wreath(S3,3,S2,2)
print("h_t(S3 wr S2)     =", h_t_transitive(w4gens,w4n), " expect 2")


print("\n--- general h(K) = max over orbits of h_t(restriction) ---")
def orbits(G, n):
    seen=set(); orbs=[]
    for x in range(n):
        if x in seen: continue
        orb=set()
        stack=[x]
        while stack:
            y=stack.pop()
            if y in orb: continue
            orb.add(y)
            for g in G: stack.append(g[y])
        seen|=orb
        orbs.append(sorted(orb))
    return orbs
def restrict_gens(gens, orb):
    idx={p:i for i,p in enumerate(orb)}
    out=[]
    for g in gens:
        out.append(tuple(idx[g[p]] for p in orb))
    return out, len(orb)
def h_general(gens, n):
    G=group_closure(gens,n)
    best=0
    for orb in orbits(G,n):
        if len(orb)<=1: continue
        rg,rn=restrict_gens(gens,orb)   # generators restricted (image on the orbit)
        best=max(best, h_t_transitive(rg,rn))
    return best

# Block-fixing product S2({0,1}) x S2({2,3}) on 4 points  -> expect h=1
prod_gens=[(1,0,2,3),(0,1,3,2)]
print("h(S2 x S2 block-fixing) =", h_general(prod_gens,4), " expect 1 (< D4's 2)")

# Block-fixing product (S2 wr S2)({0..3}) x S3({4,5,6}) -> expect max(2,1)=2
bf_gens = []
for g in D4gens: bf_gens.append(g+(4,5,6))          # D4 on 0..3, fix 4,5,6
for g in [(1,0,2),(0,2,1)]:                          # S3 on 4,5,6
    bf_gens.append((0,1,2,3)+tuple(4+x for x in g))
print("h(D4 x S3 block-fixing) =", h_general(bf_gens,7), " expect 2")

# additivity spot check: h_t(T1 wr T2) == h_t(T1)+h_t(T2)
def ht(gens,n): return h_t_transitive(gens,n)
for (name,g1,n1,g2,n2) in [
    ("S2 wr (S2wrS2)", S2,2, D4gens,D4n),
    ("(S2wrS2) wr S3", D4gens,D4n, S3,3),
]:
    wg,wn = wreath(g1,n1,g2,n2)
    print(f"h_t({name}) = {ht(wg,wn)}  expect {ht(g1,n1)+ht(g2,n2)} (=h_t(bottom)+h_t(top))")

# WITNESS check for a bounded-wreath-depth monad with W=2:
# Suppose A has a constituent b with H_b = D4 (h_t=2, the max W=2) and a non-flat
# constituent c with H_c = S2 (h=1). Then A o A realizes H_b wr H_c = D4 wr S2 (depth 3 > W=2).
wg,wn = wreath(D4gens,D4n, S2,2)   # D4 wr S2 : inner D4 (depth 2), outer S2 (depth1)
print("witness  h_t(D4 wr S2) =", ht(wg,wn), " expect W+1 = 3  (>W=2)")
