"""
2026-09-25  SOCLE verification for the W4 witness on (G,+)=Z/2 x Z/4.

W4 = skew brace on Z2xZ4 with distinguished ideal D={0}xZ/4 that is a
TRIVIAL brace (lam_a|_D = id for a in D) AND has split-triple
(mult, add, sb) = (Y, Y, N):  both the multiplicative and additive
extensions 1 -> D -> G -> G/D -> 1 SPLIT, but there is NO common
sub-skew-brace complement.

Definitions used:
  lam[a][b] = lambda_a(b)          (from characterize-decomp.py)
  a o b     = a + lam[a][b]         (multiplicative op)
  Soc(G)    = Ker(lam) cap Z(G,+)   = {a : lam_a = id} cap {a : a+b=b+a all b}
  Since (G,+)=Z2xZ4 is ABELIAN, Z(G,+)=G, so Soc(G)=Ker(lam).

For each skew brace matching the W4 criteria we report:
  Ker(lam), Fix(lam), Z(G,+), Soc(G), and the exact relationship to D.
"""
from itertools import product, combinations
import importlib.util

spec = importlib.util.spec_from_file_location(
    "ch", "/home/agent/projects/scratch/2026-09-24-characterize-decomp.py")
ch = importlib.util.module_from_spec(spec); spec.loader.exec_module(ch)

def prod_group(mods):
    E = list(product(*[range(m) for m in mods]))
    add = lambda a, b: tuple((a[i]+b[i]) % mods[i] for i in range(len(mods)))
    neg = lambda a: tuple((-a[i]) % mods[i] for i in range(len(mods)))
    return E, add, neg, tuple(0 for _ in mods)

A = prod_group([2, 4]); E, add, neg, zero = A; n = len(E)

def order(x):
    k = 1; c = x
    while c != zero:
        c = add(c, x); k += 1
    return k

def iso_type(D):
    orders = sorted(order(x) for x in D)
    if max(orders) == len(D):
        return f"Z/{len(D)}"
    return f"(orders {orders})"

D_target = frozenset([(0, 0), (0, 1), (0, 2), (0, 3)])   # {0} x Z/4

sbs = ch.skew_braces(A)
print(f"# skew braces on Z2xZ4 enumerated: {len(sbs)}")
print(f"# D_target = {{0}}xZ/4 = {sorted(D_target)}")
print("="*72)

def is_add_sub(D):
    return all(add(a, b) in D for a in D for b in D) and all(neg(a) in D for a in D)

matches = []
for si, lam in enumerate(sbs):
    def mul(a, b): return add(a, lam[a][b])
    inv = {a: next(b for b in E if mul(a, b) == zero) for a in E}

    def is_mnorm(D): return all(mul(mul(g, d), inv[g]) in D for g in E for d in D)
    def is_laminv(D): return all(lam[a][d] in D for a in E for d in D)

    # is D_target an ideal here?
    D = set(D_target)
    if not (is_add_sub(D) and is_mnorm(D) and is_laminv(D)):
        continue
    d = len(D)

    # split triple for D_target
    def is_msub(K): return all(mul(a, b) in K for a in K for b in K) and all(inv[a] in K for a in K)
    def has(pf):
        for r in range(1, n+1):
            for K in combinations(E, r):
                K = set(K)
                if zero in K and len(K)*d == n and (K & D) == {zero} and pf(K):
                    return True
        return False
    msplit = has(is_msub)
    asplit = has(is_add_sub)
    def is_sb(H): return is_add_sub(H) and all(mul(a, b) in H for a in H for b in H) and all(inv[a] in H for a in H)
    ssplit = has(is_sb)
    trip = (msplit, asplit, ssplit)
    if trip != (True, True, False):
        continue

    # trivial-brace kernel check on D
    triv_D = all(lam[a][b] == b for a in D for b in D)

    matches.append((si, lam, trip, triv_D))

print(f"# skew braces with D_target an ideal AND triple (T,T,F): {len(matches)}")
print("="*72)

for si, lam, trip, triv_D in matches:
    def mul(a, b): return add(a, lam[a][b])
    # Ker(lam): a with lam_a = identity map
    Ker = sorted(a for a in E if all(lam[a][b] == b for b in E))
    # Fix(lam): a fixed by every lam_c  (a with lam_c(a)=a for all c)
    Fix = sorted(a for a in E if all(lam[c][a] == a for c in E))
    # Z(G,+): additive centre  (abelian => all of G)
    Zadd = sorted(a for a in E if all(add(a, b) == add(b, a) for b in E))
    # Soc = Ker(lam) cap Z(G,+)
    Soc = sorted(a for a in E if a in set(Ker) and a in set(Zadd))

    D = D_target
    print(f"sb#{si}   triple(mult,add,sb)={trip}   D trivial-brace? {triv_D}")
    print(f"    lam|_D: " + ", ".join(f"lam_{a}={[lam[a][b] for b in sorted(D)]}" for a in sorted(D)))
    print(f"    D        = {sorted(D)}   iso(D,+)={iso_type(D)}")
    print(f"    Ker(lam) = {Ker}")
    print(f"    Fix(lam) = {Fix}")
    print(f"    Z(G,+)   = {Zadd}   (|Z|={len(Zadd)}, all of G? {len(Zadd)==n})")
    print(f"    Soc(G)   = Ker cap Z = {Soc}")
    # relationships
    setD, setSoc, setKer = set(D), set(Soc), set(Ker)
    print(f"    ---- relationship D vs Soc ----")
    print(f"    D == Soc ?   {setD == setSoc}")
    print(f"    D subset Soc ? {setD <= setSoc}")
    print(f"    Soc subset D ? {setSoc <= setD}")
    if setD < setSoc:
        print(f"    => D STRICTLY CONTAINED in Soc; extra in Soc\\D = {sorted(setSoc-setD)}")
    elif setSoc < setD:
        print(f"    => Soc STRICTLY CONTAINED in D; extra in D\\Soc = {sorted(setD-setSoc)}")
    elif setD == setSoc:
        print(f"    => D EQUALS Soc")
    else:
        print(f"    => INCOMPARABLE; D\\Soc={sorted(setD-setSoc)}  Soc\\D={sorted(setSoc-setD)}")
    # lam=id on all of D?
    print(f"    lam_a = id for ALL a in D ? {all(all(lam[a][b]==b for b in E) for a in D)}")
    print(f"    elements of Ker OUTSIDE D: {sorted(setKer - setD)}")
    print("-"*72)

if not matches:
    print("NO skew brace matched the W4 criteria (D_target ideal + triple (T,T,F)).")
