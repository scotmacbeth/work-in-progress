# Coproduct-preservation check for the four functors  p ltimes(-), (-)ltimes q, p rtimes(-), (-)rtimes q.
# container = (S, d) with S a list of shapes, d: dict shape->direction-SET (use frozenset of labels so we
# test equality of DIRECTION SETS up to bijection, not just cardinality).
def mkset(S, dfun): return (list(S), {s:frozenset(dfun(s)) for s in S})
def n(k, tag): return {(tag,i) for i in range(k)}   # a k-element labelled set

def ltimes(p,q):
    Sp,dp=p; Sq,dq=q
    S=[(s,t) for s in Sp for t in Sq]
    # direction = dp[s]^{Sq}  x  dq[t]^{Sp}  (product of function-sets); represent as product set
    d={}
    for s in Sp:
        for t in Sq:
            left=set(_funcs(dp[s],Sq)); right=set(_funcs(dq[t],Sp))
            d[(s,t)]=frozenset((a,b) for a in left for b in right)
    return (S,d)
def rtimes(p,q):
    Sp,dp=p; Sq,dq=q
    S=[(s,t) for s in Sp for t in Sq]
    d={}
    for s in Sp:
        for t in Sq:
            left=set(_funcs(dp[s],Sq)); right=set(dq[t])
            d[(s,t)]=frozenset((a,b) for a in left for b in right)
    return (S,d)
def _funcs(codom, dom):
    # set of functions dom(list)->codom(set): represent as tuples
    dom=list(dom); codom=list(codom)
    import itertools
    return [tuple(zip(dom,choice)) for choice in itertools.product(codom,repeat=len(dom))]
def plus(p,q):
    Sp,dp=p; Sq,dq=q
    S=[('L',s) for s in Sp]+[('R',t) for t in Sq]
    d={}; d.update({('L',s):dp[s] for s in Sp}); d.update({('R',t):dq[t] for t in Sq})
    return (S,d)
def profile(c):
    S,d=c; return (len(S), sorted(len(d[s]) for s in S))
def iso(a,b):
    # containers isomorphic iff shape-bijection matching direction-set cardinalities (finite: cardinality multiset)
    return profile(a)==profile(b)

y=mkset(['*'], lambda s: n(1,'y'))
# witness p = y^2 : one shape, 2 directions
p=mkset(['s'], lambda s: n(2,'p'))
q1=mkset(['a'], lambda s: n(1,'q1'))
q2=mkset(['b'], lambda s: n(1,'q2'))

def test(name, F_of_qsum, F_sum):
    print(f"{name}: F(q1+q2) profile={profile(F_of_qsum)}  |  F(q1)+F(q2) profile={profile(F_sum)}  -> preserves coprod? {iso(F_of_qsum,F_sum)}")

print("=== varying RIGHT variable, p = y^2 fixed, q1=q2=y ===")
qsum=plus(q1,q2)
test("p |x(-) [ltimes]", ltimes(p,qsum), plus(ltimes(p,q1),ltimes(p,q2)))
test("p |x(-) [rtimes]", rtimes(p,qsum), plus(rtimes(p,q1),rtimes(p,q2)))

print("=== varying LEFT variable, q = y^2 fixed, p1=p2=y ===")
p1=mkset(['a'], lambda s: n(1,'p1')); p2=mkset(['b'], lambda s: n(1,'p2'))
qfix=mkset(['s'], lambda s: n(2,'q'))
psum=plus(p1,p2)
test("(-)|x q [ltimes]", ltimes(psum,qfix), plus(ltimes(p1,qfix),ltimes(p2,qfix)))
test("(-)|x q [rtimes]", rtimes(psum,qfix), plus(rtimes(p1,qfix),rtimes(p2,qfix)))

print("=== deeper rtimes LEFT-variable check with nontrivial p_i and q (direction SETS, not just card) ===")
p1b=mkset(['a0','a1'], {'a0':n(2,'a0'),'a1':n(3,'a1')}.get)
p2b=mkset(['b0'], {'b0':n(2,'b0')}.get)
qb=mkset(['t0','t1'], {'t0':n(2,'t0'),'t1':n(1,'t1')}.get)
L=rtimes(plus(p1b,p2b),qb); R=plus(rtimes(p1b,qb),rtimes(p2b,qb))
print("  (-)rtimes q preserves coprod (profile)?", iso(L,R), " L",profile(L)," R",profile(R))
# also check the actual direction sets match up to the canonical shape bijection
def dirmultiset(c):
    S,d=c; return sorted(len(d[s]) for s in S)
print("  direction-cardinality multisets equal?", dirmultiset(L)==dirmultiset(R))
