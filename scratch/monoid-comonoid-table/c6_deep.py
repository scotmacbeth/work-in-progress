from table import *

print("C6 deep dive: structure of (x)-monoids  mu:c(x)c->c, eta:y->c")
print("mu at (s,s'): shape m(s,s') in S; backward phi_{s,s'}: P[m(s,s')] -> P[s] x P[s']")
print()

def deep(cont_obj, label):
    c = cont_obj
    S = c['S']
    res, nm, ne = count_monoids(Dir, c)
    print(f"=== {label}: #monoids={len(res)} (of {nm} mu x {ne} eta) ===")
    for mu, eta in res:
        m = {(s, t): mu['f'][(s, t)] for s in S for t in S}
        e = eta['f']['*']
        # backward: for the diagonal-ish, show phi_{s,s'}
        back = {}
        for s in S:
            for t in S:
                back[(s, t)] = dict(mu['b'][(s, t)])
        # eta backward: P[e] -> P_y[*]={0}, forced
        print(f"  shape-monoid m={m}, unit e={e}")
        for (s, t), phi in back.items():
            print(f"     phi_({s},{t}): {phi}")
    print()

deep(cont([1, 1]), "S=2 each P=1")
deep(cont([2]),    "S=1 P=2")
deep(cont([2, 1]), "S=2 P=[2,1]")

# Does the backward phi_{s,s'} make P into a lax structure over the monoid S?
# Check: is phi always a SECTION-like / does associativity of mu force a
# coherence among the phi's beyond what we already verified via law-check?
# We already verified full monoid laws hold for every counted solution.
# Here: for S=1 (trivial shape monoid) case with P=n, characterise phi:P->PxP.
print("Single-shape P=n: (x)-monoids and the induced phi: P -> P x P")
for n in [1, 2, 3]:
    c = cont([n])
    res, nm, ne = count_monoids(Dir, c)
    phis = []
    for mu, eta in res:
        phi = dict(mu['b'][(0, 0)])   # P -> P x P
        base = eta['b']['*'][0] if 0 in eta['b']['*'] else None
        phis.append((phi, base))
    print(f"  n={n}: #monoids={len(res)}")
    for phi, base in phis:
        print(f"     eta-base={base}  phi(P->PxP)={phi}")
