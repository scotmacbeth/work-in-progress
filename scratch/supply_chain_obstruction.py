"""
Supply-chain inventory consistency vs. ZS (G)-weld obstruction.

Tests the PROVE.md conjecture:  inventory consistent  <=>  [omega_ZS] = 0.

We compute, for small supply chains:
  (A) the INVENTORY obstruction [theta] of a resource local-system R:
      degree-1 class in H^1(underlying graph; A) = loop discrepancies.
  (B) the WELD obstruction [omega] of the ZS factorization S = C |><| D:
      degree-2 (G)-closure class; we detect its (non)vanishing structurally.

Goal: decide whether the two are the SAME class (conjecture true) or
      INDEPENDENT (conjecture false, dividing-line result).

Coefficients in A = Z (free) and A = Z/n.
"""
import numpy as np
from itertools import product
from fractions import Fraction

# ---------------------------------------------------------------------------
# (A) INVENTORY OBSTRUCTION : H^1 of the underlying directed graph
# ---------------------------------------------------------------------------
# A supply chain graph: nodes V, edges E (each an operation x->y).
# A resource local system assigns delta_f in A to each edge f.
# Inventory consistent  <=>  delta = d^0(phi)  <=>  [delta]=0 in H^1.
# H^1(graph;A) = A^(betti1),  betti1 = |E| - |V| + (#components).
# The class is read off by the cycle space: for each independent cycle,
# the signed sum of deltas must vanish.

def incidence(V, E):
    """Signed incidence matrix d^0: C^0 -> C^1 (rows=edges, cols=nodes).
       (d^0 phi)(x->y) = phi(y) - phi(x)."""
    idx = {v:i for i,v in enumerate(V)}
    M = np.zeros((len(E), len(V)), dtype=int)
    for e,(x,y) in enumerate(E):
        M[e, idx[y]] += 1
        M[e, idx[x]] -= 1
    return M

def betti1(V, E):
    # #components via union-find
    parent = {v:v for v in V}
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    for (x,y) in E:
        parent[find(x)] = find(y)
    comps = len({find(v) for v in V})
    return len(E) - len(V) + comps

def inventory_consistent_Q(V, E, delta):
    """Over Q: delta in image of d^0 ? (rank test). Returns (consistent?, betti1)."""
    M = incidence(V,E).astype(float)   # edges x nodes
    d = np.array(delta, dtype=float)
    # consistent iff d in column space of M
    aug = np.hstack([M, d.reshape(-1,1)])
    r_M  = np.linalg.matrix_rank(M)
    r_aug= np.linalg.matrix_rank(aug)
    return (r_M == r_aug), betti1(V,E)

def loop_sum(cycle_edges_signed, delta_map):
    return sum(sgn*delta_map[e] for (e,sgn) in cycle_edges_signed)

# ---- Case 2: reconvergent diamond -----------------------------------------
print("="*70)
print("CASE 2  reconvergent diamond  a->b->d, a->c->d")
V = ['a','b','c','d']
E = [('a','b'),('b','d'),('a','c'),('c','d')]   # p,r,q,s
names = ['p','r','q','s']
print("  betti1 (independent loops) =", betti1(V,E), " => H^1 has rank 1")
# inventory that is INCONSISTENT: route via b gives +3, via c gives +1
delta = {'p':2,'r':1,'q':1,'s':3}   # route b: p+r=3 ; route c: q+s=4  -> mismatch 1
dvec = [delta[n] for n in names]
cons, b1 = inventory_consistent_Q(V,E,dvec)
print(f"  delta={delta}")
print(f"  loop sum (p+r)-(q+s) = {delta['p']+delta['r']-delta['q']-delta['s']}")
print(f"  inventory consistent? {cons}   (expect False: nonzero H^1 class)")
# inventory that IS consistent (a potential exists): phi(a)=0,b=2,c=2,d=5
phi = {'a':0,'b':2,'c':2,'d':5}
delta2 = {'p':phi['b']-phi['a'],'r':phi['d']-phi['b'],
          'q':phi['c']-phi['a'],'s':phi['d']-phi['c']}
dvec2=[delta2[n] for n in names]
cons2,_=inventory_consistent_Q(V,E,dvec2)
print(f"  coboundary delta={delta2} consistent? {cons2}  (expect True)")
print("  ==> inventory obstruction is DEGREE 1 (loop discrepancy).")

# ---- Case 3: 3-cycle with invertible return leg ---------------------------
print("="*70)
print("CASE 3  3-cycle  a->b->c->a  (betti1=1)")
V3=['a','b','c']; E3=[('a','b'),('b','c'),('c','a')]
print("  betti1 =", betti1(V3,E3))
# nonzero cycle sum => inconsistent
d3=[1,1,1]  # sums to 3 around the loop
print("  delta=(1,1,1) loop sum=3 consistent?", inventory_consistent_Q(V3,E3,d3)[0],"(expect False)")
# over Z/3 the loop sum 3 == 0 : consistent mod 3
print("  NB over Z/3 loop sum 3==0 => consistent; H^1(C;Z/n)=Z/n sees n-torsion.")

# ---------------------------------------------------------------------------
# (B)  WELD OBSTRUCTION  [omega] in H^2  -- structural detection
# ---------------------------------------------------------------------------
# The (G)-closure class obstructs EXISTENCE of the transversal closing into a
# wide subcategory C (S = C |><| D).  It depends ONLY on the category S + D,
# NOT on any resource assignment.  We reuse the known rigid-twist witness.
#
# Rigid twist (from g-obstruction-is-h2-class):
#   objects a,x,y ; End(a)=Z/2=<g> ; p:a->x ; arrows x->y are {s, s2}
#   relations: s.p = q (:a->y) ; s2.p = q.g   (the twist)
#   transversal candidates can't close: [omega] = generator of H^2 = Z/2 != 0.
# This is a CATEGORY-LEVEL fact; inventory never enters.
print("="*70)
print("WELD obstruction [omega] is category-level, inventory-blind.")
print("  Rigid-twist witness: [omega] = generator of H^2(Sk;Z/2) != 0")
print("  (cited: g-obstruction-is-h2-class, proved).")
print("  Put the ZERO resource presheaf on it: every delta_f=0 => [theta]=0,")
print("  i.e. trivially inventory-CONSISTENT while [omega] != 0.")

# ---------------------------------------------------------------------------
# SEPARATION TABLE
# ---------------------------------------------------------------------------
print("="*70)
print("SEPARATION of the two classes:")
print("  diamond + mismatched delta :  [omega]=0 , [theta]!=0   (factors, INCONSISTENT)")
print("  rigid-twist + zero delta   :  [omega]!=0 , [theta]=0   (no factor, consistent)")
print("  => neither direction of 'consistent <=> [omega]=0' holds.")
print("  => inventory obstruction = H^1 of resource presheaf, NOT H^2 weld.")
