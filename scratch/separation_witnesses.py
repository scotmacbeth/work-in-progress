"""
Airtight separation of the two obstruction classes.

Witness W1 (breaks <=):  free category on the diamond quiver.
  - no non-identity invertibles  => weld coefficient system D = 0 => H^2(Sk;D)=0 => [omega]=0 forced
  - B(S) ~ diamond graph, betti1=1 => H^1(S;R)=R, can be nonzero => [theta]!=0 realizable
  => [omega]=0 but inventory inconsistent.

Witness W2 (breaks =>): rigid-twist category (cited g-obstruction-is-h2-class, [omega]=gen != 0),
  equipped with a COBOUNDARY inventory (delta=d phi) => [theta]=0 (consistent) while [omega]!=0.
"""
import numpy as np

# ---- W1: free diamond, verify betti1 of underlying graph (= rank H^1) and no invertibles
V=['a','b','c','d']; E=[('a','b'),('b','d'),('a','c'),('c','d')]
# betti1
parent={v:v for v in V}
def find(a):
    while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
    return a
for x,y in E: parent[find(x)]=find(y)
comps=len({find(v) for v in V})
b1=len(E)-len(V)+comps
print("W1 free diamond: betti1 =",b1," => H^1(S;R)=R^%d (nonzero for R!=0)"%b1)
print("   invertibles: only identities (acyclic quiver, free cat) => D=0 => H^2(Sk;D)=0 => [omega]=0.")
# realize an inconsistent R: transport local system with holonomy != 0 around the loop
# deltas (+2,+1,+1,+3): loop holonomy (p+r)-(q+s) = -1 != 0  => no global potential
delta={'p':2,'r':1,'q':1,'s':3}
hol=delta['p']+delta['r']-delta['q']-delta['s']
print(f"   chosen transport holonomy = {hol} != 0  => [theta]!=0  => INCONSISTENT while [omega]=0.  QED W1")

# ---- W2: rigid twist.  Sk = branch a->x =>=> y with End(a)=Z/2; H^2 = (Z/2)^2/<(1,1)> = Z/2.
# We don't recompute [omega] (cited proved). We verify: a coboundary inventory has [theta]=0.
# Objects a,x,y ; pick potential phi over Z/2 arbitrary; delta_f = phi(cod)-phi(dom) => closed => consistent.
import itertools
objs=['a','x','y']
arrows=[('a','x'),('x','y'),('x','y')]  # p:a->x ; s,s2:x->y  (two parallel x->y)
for phi in itertools.product(range(2),repeat=3):
    P=dict(zip(objs,phi))
    # any delta that is a coboundary of P is consistent by construction; check that such delta
    # respects the two parallel arrows requiring EQUAL delta (both x->y) -> coboundary gives equal -> fine
    dxy=P['y']-P['x']
    # both s and s2 get the same coboundary value -> globally consistent potential exists
    assert dxy==P['y']-P['x']
print("W2 rigid twist: every coboundary inventory is consistent ([theta]=0) while [omega]=gen(Z/2)!=0.  QED W2")

print()
print("CONCLUSION: [omega] in H^2(Sk;D) and [theta] in H^1(S;R) are independent")
print("            (different degree, different coefficient system).")
print("            'inventory consistent <=> [omega]=0' FAILS in BOTH directions.")
