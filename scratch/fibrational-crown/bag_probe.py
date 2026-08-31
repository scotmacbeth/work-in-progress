"""
Adversarial probe: does the free-COMMUTATIVE-monoid monad Bag (multisets)
separate 'leaf-cartesian' (cartFun & leaf-cartMu) from 'cartesian monad'
(preserves connected limits)?  If Bag were Pi-Mendler this would REFUTE
Theorem 1's step (1)=>(2). We test the leaf conditions and a connected pullback.
"""
from collections import Counter
from itertools import combinations_with_replacement, product

# multiset over a set, fixed size n, as a sorted tuple (canonical rep)
def bag_n(elems, n):
    return sorted(set(combinations_with_replacement(sorted(elems), n)))

def bag_map(u, m):            # Bag(u): apply u elementwise, KEEP multiplicity
    return tuple(sorted(u[x] for x in m))

# ---- cartFun: u_* : leaves(m) -> leaves(Bag(u) m) bijective? ----
# leaves of a size-n multiset = n positions (with multiplicity). Bag(u) keeps n.
def cartFun_bag(maxn=3, dom=('a','b','c')):
    ok = True
    for n in range(0, maxn+1):
        for m in bag_n(dom, n):
            for cod in [('x',),('x','y')]:
                # all functions dom->cod
                for vals in product(cod, repeat=len(dom)):
                    u = dict(zip(dom, vals))
                    img = bag_map(u, m)
                    # leaves preserved iff |m| == |img| (multiplicity kept -> always n)
                    if len(m) != len(img):
                        ok = False
    return ok

# ---- leaf-cartMu: mu = multiset union (flatten) never merges leaves ----
# an element of Bag(Bag X): a multiset of multisets. flatten keeps total multiplicity.
def leaf_cartMu_bag(maxn=3, dom=('a','b')):
    # combined inner leaves count == leaves of flattened multiset ?
    inner = [m for n in range(0,maxn+1) for m in bag_n(dom,n)]
    ok = True
    for outer_size in range(0,3):
        for mm in combinations_with_replacement(inner, outer_size):
            flat = tuple(sorted(x for m in mm for x in m))
            combined = sum(len(m) for m in mm)
            if combined != len(flat):     # flatten keeps multiplicity -> no merge/creation
                ok = False
    return ok

# ---- connected-limit test: the {a,a'}->z0<-{b,b'} pullback ----
# X={a,ap}->z0, Y={b,bp}->z0 (both to same point of Z={z0,z1}); P = X x_Z Y
def preserves_this_pullback():
    # sizes at n=2
    X=['a','ap']; Y=['b','bp']
    P=[(x,y) for x in X for y in Y]      # all 4 (both legs land on z0)
    fX={'a':'z0','ap':'z0'}; gY={'b':'z0','bp':'z0'}
    # Bag(P) size 2:
    BagP2 = bag_n(P, 2)
    # pullback of Bag: (m in Bag(X)_2, n in Bag(Y)_2) with Bag(f)m == Bag(g)n in Bag(Z)_2
    BagX2 = bag_n(X,2); BagY2 = bag_n(Y,2)
    pb=[]
    for m in BagX2:
        for nn in BagY2:
            if bag_map(fX,m)==bag_map(gY,nn):
                pb.append((m,nn))
    # comparison Bag(P)-> pullback : multiset over P -> (project1, project2)
    comp = {}
    for M in BagP2:
        m1 = tuple(sorted(p[0] for p in M))
        m2 = tuple(sorted(p[1] for p in M))
        comp[M]=(m1,m2)
    injective = len(set(comp.values()))==len(BagP2)
    surjective = set(comp.values())==set(pb)
    return len(BagP2), len(pb), injective, surjective

print("Bag cartFun (leaf-bijective fmap):      ", cartFun_bag())
print("Bag leaf-cartMu (flatten no merge):     ", leaf_cartMu_bag())
nP,npb,inj,surj = preserves_this_pullback()
print(f"Connected pullback {{a,ap}}->z0<-{{b,bp}} at size 2:")
print(f"   |Bag(P)|={nP}   |Bag(X) x_Bag(Z) Bag(Y)|={npb}   comparison inj={inj} surj={surj}")
print("   => Bag preserves this connected limit:", inj and surj and nP==npb)
