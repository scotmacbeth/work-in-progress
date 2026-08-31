"""Finite containers as lists of position-set CARDINALITIES (one per shape).
A container up to iso = sorted multiset of |p[s]|.  All four monoidal ops
are computable from cardinalities alone (for the outer op) plus, for the
right argument of the substitution, the full cardinality list of q."""
from itertools import product as iproduct
from collections import Counter

# container = tuple of ints (position-set sizes, one per shape)
def isotype(c):  # canonical iso-type
    return tuple(sorted(c))

def tensor(p,q):            # Dirichlet  ⊗ : shapes SpxSq, positions |p[s]|*|q[t]|
    return tuple(a*b for a in p for b in q)
def prod(p,q):             # product  × : shapes SpxSq, positions |p[s]|+|q[t]|
    return tuple(a+b for a in p for b in q)
def coprod(p,q):           # coproduct + : shapes disjoint union, positions inherited
    return tuple(p)+tuple(q)
def comp(p,q):             # substitution ◁ : p◁q ; shapes Σ_s (p[s]->Sq); positions Σ_i |q[f i]|
    Sq=len(q); out=[]
    for a in p:            # shape s of p with a positions
        for f in iproduct(range(Sq),repeat=a):   # f:[a]->Sq
            out.append(sum(q[f[i]] for i in range(a)))
    return tuple(out)

OPS={'ox':tensor,'x':prod,'+':coprod,';':comp}   # ox=⊗, x=×, +=+, ;=◁
NAME={'ox':'⊗','x':'×','+':'+',';':'◁'}

def eq(c,d): return isotype(c)==isotype(d)

# random small containers
import random
def rand_cont(maxshapes=2,maxpos=2):
    n=random.randint(1,maxshapes)
    return tuple(random.randint(0,maxpos) for _ in range(n))

def test_3ary(R,C,trials=1500):
    """R distributes over C, 3-ary. LEFT: (aCb)Rc vs (aRc)C(bRc).
       RIGHT: aR(bCc) vs (aRb)C(aRc).  Return (left_iso_frac,right_iso_frac)."""
    r,c=OPS[R],OPS[C]; L=Rr=0
    for _ in range(trials):
        a,b,cc=rand_cont(),rand_cont(),rand_cont()
        if eq(r(c(a,b),cc), c(r(a,cc),r(b,cc))): L+=1
        if eq(r(a,c(b,cc)), c(r(a,b),r(a,cc))): Rr+=1
    return L/trials, Rr/trials

def test_4ary_iso(R,C,trials=1500):
    """duoidal interchanger R outer,C inner: src=(aCb)R(cCd), tgt=(aRc)C(bRd).
       fraction where src ≅ tgt (necessary for D)."""
    r,c=OPS[R],OPS[C]; k=0
    for _ in range(trials):
        a,b,d,e=rand_cont(),rand_cont(),rand_cont(),rand_cont()
        if eq(r(c(a,b),c(d,e)), c(r(a,d),r(b,e))): k+=1
    return k/trials

print("=== 3-ary distributivity  R over C : (left iso frac, right iso frac) ===")
print(f"{'R\\C':>4}", *[f"{NAME[C]:>12}" for C in OPS])
for R in OPS:
    row=[]
    for C in OPS:
        l,r=test_3ary(R,C)
        row.append(f"L{l:.2f}/R{r:.2f}")
    print(f"{NAME[R]:>4}", *[f"{x:>12}" for x in row])

print("\n=== 4-ary duoidal interchanger  R outer / C inner : src≅tgt fraction ===")
print(f"{'R\\C':>4}", *[f"{NAME[C]:>10}" for C in OPS])
for R in OPS:
    row=[]
    for C in OPS:
        row.append(f"{test_4ary_iso(R,C):.3f}")
    print(f"{NAME[R]:>4}", *[f"{x:>10}" for x in row])
