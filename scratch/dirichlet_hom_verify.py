import random
from itertools import product

# Container = list of position-set sizes, one per shape.

def shapeA_positions(q, r):
    """Construction A (morphism form). Return list of position-sizes, one per shape (morphism)."""
    Sq = len(q); Sr = len(r)
    pos = []
    # enumerate all shape-maps sigma: S_q -> S_r, and all backward maps.
    for sigma in product(range(Sr), repeat=Sq):
        # backward maps: for each t, a function r[sigma(t)] -> q[t].
        # number = prod_t |q[t]|^{|r[sigma(t)]|}; each such is one morphism (shape).
        backdomsizes = [q[t] for t in range(Sq)]  # codomain sizes
        backranges = [r[sigma[t]] for t in range(Sq)]  # domain sizes |r[sigma(t)]|
        # position at this morphism = sum_t |r[sigma(t)]|
        p = sum(backranges)
        # count of morphisms with this sigma = prod_t q[t]^{r[sigma(t)]}
        cnt = 1
        for t in range(Sq):
            cnt *= backdomsizes[t] ** backranges[t]
        pos.extend([p] * cnt)
    return pos

def comp_container(r, c):
    """r <| c : container composition. r,c as position-size lists. Return list of position-sizes."""
    Sr = len(r); Sc = len(c)
    pos = []
    for s in range(Sr):
        # g : r[s] -> S_c , enumerate all functions
        for g in product(range(Sc), repeat=r[s]):
            p = sum(c[g[b]] for b in range(r[s]))
            pos.append(p)
    return pos

def product_container(factors):
    """Container product. factors = list of position-size lists. shapes=tuples, pos=sum."""
    result = [0]  # single empty tuple, pos 0
    for f in factors:
        newres = []
        for base in result:
            for p in f:
                newres.append(base + p)
        result = newres
    return result

def shapeB_positions(q, r):
    factors = []
    for i in range(len(q)):
        qi = q[i]
        c = [1] * qi  # q[i]*y : qi shapes, each position size 1
        F_i = comp_container(r, c)
        factors.append(F_i)
    return product_container(factors)

def run_case(q, r):
    A = shapeA_positions(q, r)
    B = shapeB_positions(q, r)
    return len(A), len(B), sorted(A) == sorted(B)

cases = [([2], [1,2])]
random.seed(7)
for _ in range(8):
    nq = random.randint(1,3); nr = random.randint(1,3)
    q = [random.randint(1,3) for _ in range(nq)]
    r = [random.randint(1,3) for _ in range(nr)]
    cases.append((q, r))

print(f"{'q':<12}{'r':<12}{'|ShapeA|':<10}{'|ShapeB|':<10}{'multiset==':<10}")
allmatch = True
for q, r in cases:
    sa, sb, eq = run_case(q, r)
    if not eq or sa != sb:
        allmatch = False
    print(f"{str(q):<12}{str(r):<12}{sa:<10}{sb:<10}{str(eq):<10}")
print()
print("ALL CASES MATCHED" if allmatch else "MISMATCH DETECTED")
