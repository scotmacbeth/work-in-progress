#!/usr/bin/env python3
"""
2026-09-08  C_3 diagonal witness: does MacBeth's unit-peg / diagonal-stabilizer
mechanism generalize from the binary-commutative case (C_2) to a cyclic-ternary
operad (C_3)?

MECHANISM UNDER TEST
--------------------
For the free commutative UNITAL non-associative magma monad U (binary mu, H_mu=S_2,
plus nullary unit c with absorption mu(t,c)=t), U o U has a 4-label element whose
label-automorphism group is exactly the correlated diagonal C_2 = <(0 1)(2 3)>:
a lone fixed-point-free correlated swap of two rigid size-2 blocks. NO polynomial
outer functor [r] o U can realize this, because polynomial-outer stabilizers are
"block-fixing products" prod G_beta (a position/leaf is fixed iff fixed pointwise),
and a lone diagonal swap is not such a product. The unit c is the weapon: an inner
unit ELEMENT survives as a non-absorbing OUTER leaf (a rigid, label-free peg) that
rigidifies each block, so only the correlated block-swap survives.

MODEL
-----
Two-level free-algebra terms (elements of M o M over a finite label set):

  inner terms  (elements of M(X), X = labels + inner unit):
     ('IL', k)             leaf carrying label k (an actual label from [n])
     ('IU',)               the nullary inner unit c  (a distinguished ELEMENT of M(X))
     ('IO', op, (kids...)) inner operation node
  outer terms  (elements of M(M(X))):
     ('OL', inner)         outer leaf carrying an inner-element as its value
     ('OU',)               the nullary OUTER unit (a SEPARATE constant)
     ('OO', op, (kids...)) outer operation node

Key point that makes the mechanism work: ('OL', ('IU',)) -- an outer leaf whose value
is the INNER unit -- is NOT the outer unit, so it does NOT absorb under an outer
operation. It is a rigid, label-free peg.

Operation specs (name -> arity, symmetry group acting on argument order, unit law):
  'mu'    : binary, S2 (commutative),   absorbs unit          [the U monad]
  'omega' : ternary, C3 (cyclic <(123)>), NO unit absorption  [the test operad]
  'cat'   : binary, trivial (ordered),  absorbs unit          [flat neg. control]

Unit law modeling note (stated honestly): for the binary unital magma the unit law is
the standard absorption mu(x,c)=x. For the ternary operad there is no binary op, so the
nullary c has no absorption law inside omega -- it functions purely as a rigid nullary
peg (a distinguished generator). This is the faithful reading of "unit as a peg": the
property the mechanism actually exploits is that the peg is a rigid, label-free element
that survives (does not collapse) at the level where it breaks symmetry.

Aut(w) is computed by BRUTE FORCE over all of S_n: sigma in Aut iff relabeling the
labels of w by sigma and fully renormalizing (unit laws + symmetry canonicalization at
BOTH levels) gives back the normal form of w.
"""

import itertools

# ---------------------------------------------------------------- operation table
OPS = {
    'mu':    {'arity': 2, 'sym': 'S2', 'absorb': True},   # commutative unital binary (U)
    'omega': {'arity': 3, 'sym': 'C3', 'absorb': False},  # cyclic ternary + peg
    'cat':   {'arity': 2, 'sym': 'ID', 'absorb': True},   # non-commutative unital binary (flat)
}

# ---------------------------------------------------------------- raw constructors
def IL(k):            return ('IL', k)
IU = ('IU',)
def IO(name, *kids):  return ('IO', name, tuple(kids))
def OL(inner):        return ('OL', inner)
OU = ('OU',)
def OO(name, *kids):  return ('OO', name, tuple(kids))

# ---------------------------------------------------------------- canonicalization
def canon_children(sym, ck):
    ck = tuple(ck)
    if sym == 'S2':
        return tuple(sorted(ck))
    if sym == 'S3':
        return tuple(sorted(ck))
    if sym == 'C3':
        rots = [ck[i:] + ck[:i] for i in range(len(ck))]
        return min(rots)
    if sym == 'ID':
        return ck
    raise ValueError(sym)

def inner_canon(t):
    tag = t[0]
    if tag == 'IL':
        return t
    if tag == 'IU':
        return t
    if tag == 'IO':
        name = t[1]
        kids = [inner_canon(k) for k in t[2]]
        spec = OPS[name]
        if spec['absorb']:
            kids = [k for k in kids if k != ('IU',)]
            if len(kids) == 0:
                return ('IU',)
            if len(kids) == 1:
                return kids[0]
        return ('IO', name, canon_children(spec['sym'], kids))
    raise ValueError(t)

def outer_canon(t):
    tag = t[0]
    if tag == 'OL':
        return ('OL', inner_canon(t[1]))
    if tag == 'OU':
        return t
    if tag == 'OO':
        name = t[1]
        kids = [outer_canon(k) for k in t[2]]
        spec = OPS[name]
        if spec['absorb']:
            kids = [k for k in kids if k != ('OU',)]   # only the true OUTER unit absorbs
            if len(kids) == 0:
                return ('OU',)
            if len(kids) == 1:
                return kids[0]
        return ('OO', name, canon_children(spec['sym'], kids))
    raise ValueError(t)

# ---------------------------------------------------------------- relabeling
def relabel(t, perm):
    tag = t[0]
    if tag == 'IL':
        return ('IL', perm[t[1]])
    if tag in ('IU', 'OU'):
        return t
    if tag in ('IO', 'OO'):
        return (tag, t[1], tuple(relabel(k, perm) for k in t[2]))
    if tag == 'OL':
        return ('OL', relabel(t[1], perm))
    raise ValueError(t)

# ---------------------------------------------------------------- Aut by brute force
def aut(w, n):
    base = outer_canon(w)
    G = []
    for p in itertools.permutations(range(n)):
        perm = list(p)
        if outer_canon(relabel(w, perm)) == base:
            G.append(tuple(perm))
    return G

# ---------------------------------------------------------------- permutation utils
def to_cycles(perm):
    n = len(perm)
    seen = [False] * n
    cycles = []
    for i in range(n):
        if seen[i] or perm[i] == i:
            seen[i] = True
            continue
        cyc = []
        j = i
        while not seen[j]:
            seen[j] = True
            cyc.append(j)
            j = perm[j]
        if len(cyc) > 1:
            cycles.append(tuple(cyc))
    if not cycles:
        return "id"
    return "".join("(" + " ".join(map(str, c)) + ")" for c in cycles)

def group_from_gens_check(G):
    """Return generators (a small spanning subset) by greedy closure check."""
    Gset = set(G)
    n = len(next(iter(Gset)))
    ident = tuple(range(n))
    def compose(a, b):  # a after b
        return tuple(a[b[i]] for i in range(n))
    gens = []
    closure = {ident}
    for g in sorted(Gset):
        if g in closure:
            continue
        gens.append(g)
        # recompute closure
        frontier = list(closure) + [g]
        closure = set(closure)
        closure.add(g)
        changed = True
        while changed:
            changed = False
            cur = list(closure)
            for a in cur:
                for b in cur:
                    c = compose(a, b)
                    if c not in closure:
                        closure.add(c)
                        changed = True
    return gens, (closure == Gset)

# ---------------------------------------------------------------- decomposability
def set_partitions(collection):
    collection = list(collection)
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in set_partitions(collection[1:]):
        for i, subset in enumerate(smaller):
            yield smaller[:i] + [[first] + subset] + smaller[i+1:]
        yield [[first]] + smaller

def is_block_fixing_product(G, support):
    """
    G: list of perms (tuples on {0..n-1}). support: the moved points.
    Returns (decomposable?, witness_partition_or_None).
    G is a block-fixing product iff there is a partition of `support` into >=2
    G-invariant parts such that |G| == product over parts of |G restricted to part|
    (i.e. the restriction map G -> prod G|_part is onto the full direct product).
    """
    support = sorted(support)
    order = len(G)
    for part in set_partitions(support):
        if len(part) < 2:
            continue
        parts = [set(p) for p in part]
        # every part must be setwise G-invariant
        invariant = True
        for g in G:
            for P in parts:
                if {g[x] for x in P} != P:
                    invariant = False
                    break
            if not invariant:
                break
        if not invariant:
            continue
        # restriction orders
        prod = 1
        for P in parts:
            restrs = set()
            for g in G:
                restrs.add(tuple(sorted((x, g[x]) for x in P)))
            prod *= len(restrs)
        if prod == order:
            return True, [sorted(p) for p in parts]
    return False, None

# ================================================================ TASK 1: C_2 control
def task1():
    print("=" * 70)
    print("TASK 1  --  CONTROL: reproduce the U (binary commutative unital) C_2")
    print("=" * 70)
    n = 4
    peg = OL(IU)                       # rigid label-free peg = inner unit as outer leaf
    def lab(k): return OL(IL(k))       # outer leaf carrying singleton inner label k
    # two rigid blocks on INTERLEAVED supports {0,2} and {1,3}, iso via (0 1)(2 3);
    # outer mu is commutative so the correlated swap of the two blocks fixes w.
    P = OO('mu', OO('mu', lab(0), peg), lab(2))   # rigid pair on {0,2}
    Q = OO('mu', OO('mu', lab(1), peg), lab(3))   # rigid pair on {1,3}, iso to P via (0 1)(2 3)
    w = OO('mu', P, Q)

    # sanity: each block rigid?
    autP = [g for g in itertools.permutations(range(4))
            if outer_canon(relabel(P, list(g))) == outer_canon(P)]
    autP = [g for g in autP if all(g[x] == x for x in (1, 3))]  # perms of {0,2}
    print("  block P nontrivial self-symmetry among {0,2}? ",
          [to_cycles(list(g)) for g in autP if list(g) != list(range(4))] or "none (rigid)")

    G = aut(w, n)
    gens, ok = group_from_gens_check(G)
    print("  |Aut(w)| =", len(G))
    print("  elements:", [to_cycles(list(g)) for g in G])
    print("  generators:", [to_cycles(list(g)) for g in gens], " (span ok:", ok, ")")
    target = {tuple([0,1,2,3]), tuple([1,0,3,2])}   # id and (0 1)(2 3)
    got = set(G)
    print("  Aut == <(0 1)(2 3)> (C_2, order 2)? ", got == target)
    return got == target and len(G) == 2

# ================================================================ TASK 2: C_3 extend
def task2():
    print()
    print("=" * 70)
    print("TASK 2  --  EXTEND: cyclic-ternary operad omega (H_omega = C_3), unit peg")
    print("=" * 70)
    n = 6
    # inner rigid blocks b_i = omega(a,b,peg) as ELEMENTS of M(X); rigid via cyclic sym.
    b1 = IO('omega', IL(0), IL(1), IU)
    b2 = IO('omega', IL(2), IL(3), IU)
    b3 = IO('omega', IL(4), IL(5), IU)

    # rigidity check of an inner block over its own pair
    def inner_block_rigid(b, pair):
        for g in itertools.permutations(range(n)):
            if all(g[x] == x for x in range(n) if x not in pair):
                if inner_canon(relabel(b, list(g))) == inner_canon(b) and list(g) != list(range(n)):
                    return False
        return True
    print("  b1 rigid on {0,1}? ", inner_block_rigid(b1, {0, 1}))

    # outer omega (cyclic C_3) of the three isomorphic blocks; blocks {0,1},{2,3},{4,5}
    # are cycled by the diagonal (0 2 4)(1 3 5).
    w = OO('omega', OL(b1), OL(b2), OL(b3))

    G = aut(w, n)
    gens, ok = group_from_gens_check(G)
    print("  |Aut(w)| =", len(G))
    print("  elements:", [to_cycles(list(g)) for g in G])
    print("  generators:", [to_cycles(list(g)) for g in gens], " (span ok:", ok, ")")
    Delta = tuple([2,3,4,5,0,1])  # (0 2 4)(1 3 5): 0->2,2->4,4->0 ; 1->3,3->5,5->1
    target = {tuple(range(6)), Delta, tuple([4,5,0,1,2,3])}  # id, Delta, Delta^2
    got = set(G)
    print("  Delta = (0 2 4)(1 3 5) present? ", Delta in got)
    print("  Aut == <(0 2 4)(1 3 5)> (C_3, order 3)? ", got == target)
    return got, target

# ================================================================ TASK 3: escape check
def task3(Gset):
    print()
    print("=" * 70)
    print("TASK 3  --  ESCAPE CHECK: is Delta a block-fixing product in F(6)?")
    print("=" * 70)
    G = list(Gset)
    support = set(range(6))  # Delta moves all 6 points
    # orbits
    def orbits(G, n):
        seen = set(); orbs = []
        for i in range(n):
            if i in seen: continue
            orb = set()
            frontier = [i]
            while frontier:
                x = frontier.pop()
                if x in orb: continue
                orb.add(x)
                for g in G:
                    frontier.append(g[x])
            seen |= orb
            orbs.append(sorted(orb))
        return orbs
    orbs = orbits(G, 6)
    print("  orbits of Delta:", orbs)
    dec, wit = is_block_fixing_product(G, support)
    print("  |Delta| =", len(G))
    # show the orbit-partition restriction orders to make the failure explicit
    print("  restriction to {0,2,4}:",
          sorted({to_cycles([g[x] if x in (0,2,4) else x for x in range(6)]) for g in G}))
    print("  restriction to {1,3,5}:",
          sorted({to_cycles([g[x] if x in (1,3,5) else x for x in range(6)]) for g in G}))
    print("  product of restriction orders over orbit partition = 3 * 3 = 9  != |Delta| = 3")
    print("  Delta a block-fixing product over SOME invariant partition? ", dec,
          "" if wit is None else ("witness " + str(wit)))
    fires = not dec
    print("  => support-indecomposable (correlated diagonal)? ", fires)
    print("  => composition test FIRES (Aut(w) not in F(6)  =>  M o M  !~=  [r] o M)? ", fires)
    return fires

# ================================================================ TASK 4: flat control
def task4():
    print()
    print("=" * 70)
    print("TASK 4  --  NEGATIVE CONTROL: free unital NON-commutative binary magma (FLAT)")
    print("=" * 70)
    n = 4
    peg = OL(IU)
    def lab(k): return OL(IL(k))
    # SAME peg construction, but operation 'cat' is ordered (H = trivial), i.e. flat/polynomial
    P = OO('cat', OO('cat', lab(0), peg), lab(2))
    Q = OO('cat', OO('cat', lab(1), peg), lab(3))
    w = OO('cat', P, Q)
    G = aut(w, n)
    gens, ok = group_from_gens_check(G)
    print("  |Aut(w)| =", len(G))
    print("  elements:", [to_cycles(list(g)) for g in G])
    dec, wit = is_block_fixing_product(G, set(range(4))) if len(G) > 1 else (True, "trivial group")
    print("  diagonal (0 1)(2 3) an automorphism? ", tuple([1,0,3,2]) in set(G))
    print("  Aut is trivial or a block-fixing product (NO diagonal escape)? ",
          (len(G) == 1) or dec)
    return (len(G) == 1) or dec, tuple([1,0,3,2]) not in set(G)

# ================================================================ MAIN
if __name__ == "__main__":
    t1 = task1()
    got2, target2 = task2()
    t2 = (got2 == target2)
    t3 = task3(got2)
    t4_noescape, t4_nodiag = task4()

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("  Task 1  reproduced C_2 = <(0 1)(2 3)> (order 2):        ", t1)
    print("  Task 2  Aut(w) = C_3 = <(0 2 4)(1 3 5)> (order 3):      ", t2)
    print("  Task 3  Delta support-indecomposable, test fires:       ", t3)
    print("  Task 4  flat control shows NO diagonal escape:          ", t4_noescape,
          "(diagonal not an aut:", t4_nodiag, ")")
    verdict = t1 and t2 and t3 and t4_noescape and t4_nodiag
    print()
    print("  OVERALL: peg-diagonal mechanism GENERALIZES to cyclic-ternary? ", verdict)
