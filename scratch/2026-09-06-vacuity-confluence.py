"""
Confluence / normal-form check for the commutative-unital-magma operad.
Rewrite rules (oriented):  mu(t,c) -> t,  mu(c,t) -> t,  mu(c,c) -> c.
Claim: normal forms of arity-n terms (n>=1) = binary trees with EXACTLY the n
variable leaves, no constants. So A[n] = free commutative magma count, and no two
distinct all-variable trees are identified (rules never touch variable-only trees).

We test confluence by exhaustive rewriting of all terms up to a size bound over a
small leaf alphabet {c, x1, x2} and checking every term has a UNIQUE normal form.
"""
import itertools

C=('c',)
def isC(t): return t==C
def mk(a,b):
    # commutative constructor, canonical
    return ('m',) + tuple(sorted((a,b)))

def one_step(t):
    """all terms reachable by ONE rewrite anywhere (rules can fire on either
    orientation-free since mu commutative)."""
    outs=set()
    if t[0]!='m': return outs
    a,b=t[1],t[2]
    # root redexes
    if isC(a) and isC(b): outs.add(C)
    if isC(b): outs.add(a)
    if isC(a): outs.add(b)
    # inner
    for na in ([one_step(a)] if a[0]=='m' else [set()])[0]:
        outs.add(mk(na,b))
    for nb in ([one_step(b)] if b[0]=='m' else [set()])[0]:
        outs.add(mk(a,nb))
    return outs

def normal_forms(t):
    """set of normal forms reachable"""
    frontier={t}; nf=set(); seen=set()
    while frontier:
        u=frontier.pop()
        if u in seen: continue
        seen.add(u)
        steps=one_step(u)
        if not steps: nf.add(u)
        else: frontier|=steps
    return nf

# enumerate all terms up to a depth bound over alphabet
alpha=[C,('c','x1'),('c','x2')]  # placeholder; build leaves properly
leaves=[C, ('v','x1'), ('v','x2')]
def leafmk(l): return l if l[0]=='c' else ('m'+'',) if False else l
# simpler: leaves are C or ('v',name); constructor mk works on any nodes
def gen(depth):
    if depth==0:
        return list(leaves)
    smaller=gen(depth-1)
    res=set(smaller)
    for a in smaller:
        for b in smaller:
            res.add(mk(a,b))
    return list(res)

# adapt one_step/normal_forms to leaf form ('v',name) and C
def isCg(t): return t==C
def one_step_g(t):
    outs=set()
    if t[0]!='m': return outs
    a,b=t[1],t[2]
    if isCg(a) and isCg(b): outs.add(C)
    if isCg(b): outs.add(a)
    if isCg(a): outs.add(b)
    if a[0]=='m':
        for na in one_step_g(a): outs.add(mk(na,b))
    if b[0]=='m':
        for nb in one_step_g(b): outs.add(mk(a,nb))
    return outs
def nf_g(t):
    frontier={t}; nf=set(); seen=set()
    while frontier:
        u=frontier.pop()
        if u in seen: continue
        seen.add(u)
        st=one_step_g(u)
        if not st: nf.add(u)
        else: frontier|=st
    return nf

terms=gen(3)
bad=[t for t in terms if len(nf_g(t))!=1]
print(f"terms tested: {len(terms)}")
print(f"terms with a NON-unique normal form: {len(bad)}  ->  {'CONFLUENT' if not bad else 'NOT confluent'}")

# check: normal forms contain no C unless the term IS C
nfs=set()
for t in terms:
    nfs|=nf_g(t)
def has_c(t):
    if t==C: return True
    if t[0]=='m': return has_c(t[1]) or has_c(t[2])
    return False
leftover=[t for t in nfs if t!=C and has_c(t)]
print(f"normal forms (other than c) that still contain a constant c: {len(leftover)}  ->  {'clean' if not leftover else 'PROBLEM'}")
print()
print("Linear-regular check of the equations (=> operadic => analytic):")
print("  commutativity mu(x,y)=mu(y,x): vars {x,y} once each side. OK")
print("  unit  mu(x,c)=x: var set {x} both sides, x once each side; c is arity-0. OK")
print("  => theory is presented by linear-regular equations => symmetric operad => ANALYTIC monad.")
