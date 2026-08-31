"""
ZS-holonomy composition: compute-first (guardrail 2) for the 08-12 bridge.

We realise the Zappa-Szep product INTERNALLY as an exact factorization G = P.P'
(every g = p p' uniquely, P cap P' = {e}) of a finite group G acting on a set S.
Then the composite update-monad action on S is s.(p,p') = s.(pp') = s.g, so the
composite isotropy at s is Stab_G(s), and the factor isotropies are Stab_G(s) cap P,
Stab_G(s) cap P'.

We test conjecture (b):   Stab_G(s) =? (Stab_G(s) cap P) . (Stab_G(s) cap P').
"""
from itertools import permutations, product

# ---- permutation-group toolkit (perms as tuples, S = 0..n-1) ----
def comp(a, b):            # (a after b)(i) = a[b[i]]
    return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    r = [0]*len(a)
    for i,x in enumerate(a): r[x] = i
    return tuple(r)
def idperm(n): return tuple(range(n))

def closure(gens, n):
    G = {idperm(n)}
    frontier = list(G)
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                x = comp(g, h)
                if x not in G:
                    G.add(x); nf.append(x)
        frontier = nf
    return G

def subgroup(gens, n):
    return closure(gens, n) if gens else {idperm(n)}

def is_exact_factorization(G, P, Pp):
    # every g in G = p p' uniquely, P cap P' = {e}
    n = None
    prods = {}
    for p in P:
        for q in Pp:
            g = comp(p, q)
            if g in prods:
                return False   # non-unique
            prods[g] = (p, q)
    if len(prods) != len(G): return False
    if set(prods) != set(G): return False
    e = next(iter(P));
    # identity check via intersection
    inter = P & Pp
    if len(inter) != 1: return False
    return prods    # dict g -> (p,p')

def stab(H, s):        # H a set of perms, point s
    return {h for h in H if h[s] == s}

def factor_product(A, B):     # set product A.B
    return {comp(a, b) for a in A for b in B}

# ---------------------------------------------------------------
# Test 1: S_3 on 3 points, G = A3 . <(12)>
# ---------------------------------------------------------------
def test_S3():
    n = 3
    a = (1,2,0)   # (0 1 2)
    t = (1,0,2)   # (0 1)   [call points 0,1,2 ~ 1,2,3]
    G = closure([a,t], n)
    P  = subgroup([a], n)         # A3 = <(012)>
    Pp = subgroup([t], n)         # <(01)>
    fac = is_exact_factorization(G, P, Pp)
    print("S3: |G|=%d |P|=%d |P'|=%d  exact-factorization=%s" %
          (len(G), len(P), len(Pp), bool(fac)))
    for s in range(n):
        SG  = stab(G, s)
        SP  = stab(G, s) & P        # Stab_G(s) cap P = Stab_P(s)
        SPp = stab(G, s) & Pp
        prod = factor_product(SP, SPp)
        eq = (prod == SG)
        print("  s=%d: |Stab_G|=%d |Stab_P|=%d |Stab_P'|=%d  |SP.SP'|=%d  EQUAL=%s"
              % (s, len(SG), len(SP), len(SPp), len(prod), eq))
    return G, P, Pp

# ---------------------------------------------------------------
# Test 2: sweep exact factorizations of small perm groups, check (b)
# ---------------------------------------------------------------
def all_subgroups(G, n):
    G = list(G)
    subs = set()
    # generate subgroups by closing all small gen-sets (cheap for small G)
    from itertools import combinations
    subs.add(frozenset([idperm(n)]))
    for k in (1,2):
        for gens in combinations(G, k):
            subs.add(frozenset(closure(list(gens), n)))
    return [set(s) for s in subs]

def sweep(name, gens, n):
    G = closure(gens, n)
    subs = all_subgroups(G, n)
    found = 0; proper = 0; total_checks = 0
    e = idperm(n)
    for P in subs:
        for Pp in subs:
            if len(P)*len(Pp) != len(G): continue
            if len(P & Pp) != 1: continue
            fac = is_exact_factorization(G, P, Pp)
            if not fac: continue
            found += 1
            for s in range(n):
                SG = stab(G, s)
                SP = SG & P; SPp = SG & Pp
                prod = factor_product(SP, SPp)
                total_checks += 1
                # containment must ALWAYS hold
                assert prod <= SG, "containment FAILED (impossible)"
                if prod != SG:
                    proper += 1
    print("%-14s |G|=%2d : exact-factorizations=%2d  point-checks=%3d  PROPER(b-fails)=%3d"
          % (name, len(G), found, total_checks, proper))

# ---------------------------------------------------------------
# Test 3: reentrancy witness  Z/2 |><| Z/2  as extension, [omega]=eps
#   E_eps = Z/2 x Z/2 (eps=0)  vs  Z/4 (eps=1); A=<a> normal, B=<b> quotient.
#   Check: eps=0 -> direct product (a,b commute); eps=1 -> non-split-as-direct (order 4 cyclic).
# ---------------------------------------------------------------
def test_reentrancy():
    # Represent E as permutations to test commuting / structure.
    # eps=0: Z/2 x Z/2 acting on 4 pts as (01)(23) and (02)(13)  [commute]
    a0 = (1,0,3,2); b0 = (2,3,0,1)
    E0 = closure([a0,b0],4)
    comm0 = comp(a0,b0)==comp(b0,a0)
    print("eps=0: |E|=%d  a,b commute=%s  (=> Z/2 x Z/2 direct)" % (len(E0), comm0))
    # eps=1: Z/4 = <c>, a=c^2 (the A=Z/2), b=c (maps onto B=Z/2). a normal, does not split as direct.
    c = (1,2,3,0)      # 4-cycle
    a1 = comp(c,c)     # c^2 = (02)(13), the order-2 normal subgroup
    E1 = closure([c],4)
    order4 = len(E1)
    # b lifts the generator of B; here b=c has order 4, so <a>,<b> do NOT give direct product
    splits_direct = any(x!=idperm(4) and comp(x,x)==idperm(4) and comp(x,a1)==comp(a1,x)
                        and x not in {idperm(4),a1} and closure([x],4) & {a1}=={idperm(4)}
                        for x in E1)
    print("eps=1: |E|=%d  cyclic order-4=%s  splits-as-direct-product=%s"
          % (len(E1), order4==4, splits_direct))
    print("  => [omega]=eps: eps=0 composite holonomy = commuting pair; eps=1 = entangled (Z/4).")

if __name__ == "__main__":
    print("=== Test 1: S3 counterexample to (b) ===")
    test_S3()
    print("\n=== Test 2: sweep small groups, count where (b) FAILS ===")
    sweep("S3",      [(1,2,0),(1,0,2)], 3)
    sweep("S4",      [(1,2,3,0),(1,0,2,3)], 4)
    sweep("A4",      [(1,2,0,3),(0,2,3,1)], 4)
    sweep("D4",      [(1,2,3,0),(3,2,1,0)], 4)
    sweep("Z2xZ2",   [(1,0,2,3),(0,1,3,2)], 4)
    print("\n=== Test 3: reentrancy Z/2|><|Z/2, [omega]=eps ===")
    test_reentrancy()
