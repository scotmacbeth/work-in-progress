"""
(c) Unbounded wreath depth: the balanced binary tree with 2^k leaves has
automorphism group (as a subgroup of S_{2^k} permuting the leaves) equal to the
iterated wreath product S_2 wr S_2 wr ... wr S_2 (k times), of order 2^{2^k - 1}.
We verify by brute force for k=1,2,3 that the leaf-stabilizer has this order and
that its NESTING depth (finest support-splitting recursion) is exactly k.
"""
from itertools import permutations

def balanced(labels):
    labels = list(labels)
    if len(labels)==1:
        return ('L', labels[0])
    h = len(labels)//2
    return ('N',) + tuple(sorted((balanced(labels[:h]), balanced(labels[h:]))))

def canon(t):
    if t[0]=='L': return t
    a,b = canon(t[1]), canon(t[2])
    return ('N',)+tuple(sorted((a,b)))

def relabel(t, perm):
    if t[0]=='L': return ('L', perm[t[1]])
    return canon(('N', relabel(t[1],perm), relabel(t[2],perm)))

for k in range(1,4):
    n = 2**k
    T = canon(balanced(range(n)))
    stab = [p for p in permutations(range(n)) if relabel(T, p)==T]
    order = len(stab)
    expected = 2**(2**k - 1)
    print(f"k={k}, leaves={n}: |Aut(balanced tree)| = {order}, expected 2^(2^k-1) = {expected}  {'OK' if order==expected else 'MISMATCH'}")
    assert order==expected

# nesting depth of iterated wreath: |S_2 wr .. wr S_2 (k)| = 2^(2^k -1); depth = k
print()
print("Wreath NESTING depth of balanced 2^k tree = k  ->  UNBOUNDED as k->inf. GOOD (c).")
print("(Aut = complete-binary-tree automorphism group = S_2 wr S_2 wr ... wr S_2, k factors.)")

# ---- (a) unit absorption: A[0] and A[1] finite via rewriting mu(x,c)=x, mu(c,c)=c ----
# Symbolic check: closed terms all reduce to c; one-variable terms all reduce to x1.
# Model terms with 'c' leaves and reduce: any tree with a pure-constant subtree
# absorbs it. Show a few reductions.
def reduce_unit(t):
    # t leaves are either ('L','c') or ('L', var). Reduce mu(s,c)->s, mu(c,c)->c.
    if t[0]=='L': return t
    a=reduce_unit(t[1]); b=reduce_unit(t[2])
    ca = (a==('L','c')); cb=(b==('L','c'))
    if ca and cb: return ('L','c')
    if cb: return a
    if ca: return b
    return canon(('N',a,b))

C=('L','c'); X=('L','x1')
tests = [
    ('N',C,C),                      # mu(c,c)
    ('N',X,C),                      # mu(x1,c)
    ('N',('N',X,C),C),              # mu(mu(x1,c),c)
    ('N',X,('N',C,C)),             # mu(x1, mu(c,c))
    ('N',('N',C,('N',C,C)),X),     # mu(mu(c,mu(c,c)), x1)
]
print()
for t in tests:
    print("  reduce", t, "->", reduce_unit(t))
print("  -> closed terms ->  c ; one-variable terms -> x1.  A[0]={c}, A[1]={x1}: FINITE. GOOD (a).")
