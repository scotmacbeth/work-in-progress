"""
Verify the comonad laws (cofree comonad C^infty) and monad laws (free monad C*)
of a container C=(S,P), implementing the structure maps via the CONTAINER formulas
(root/subtree/path-concat for cofree; leaf/graft for free), on enumerated small trees.

Two test containers:
  Maybe : S={'nil':[], 'cons':['*']}             Ext = 1 + X
  Bin   : S={'leaf':[], 'node':['L','R']}        Ext = 1 + X^2

Trees are immutable (tuples) so we can use them as dict labels / compare equality.
"""
from itertools import product

# ----- container spec: dict shape -> list of positions -----
Maybe = {'nil': [], 'cons': ['*']}
Bin   = {'leaf': [], 'node': ['L', 'R']}

# =====================================================================
# COFREE COMONAD  C^infty : T(A) = nu X. A x Sigma_s (P s -> X)
# tree = ('C', shape, label, (child_for_p, ...))   children indexed by P(shape) order
# =====================================================================

def cof_trees(C, A, depth):
    """All cofree C-trees of height <= depth with labels in A (depth>=1)."""
    out = []
    for s, ps in C.items():
        if depth == 1:
            if len(ps) == 0:          # leaf shape: can stop
                for a in A:
                    out.append(('C', s, a, ()))
        else:
            child_choices = product(*[cof_trees(C, A, depth-1) for _ in ps]) if ps else [()]
            for a in A:
                for kids in child_choices:
                    out.append(('C', s, a, tuple(kids)))
    return out

def cof_label(t):                 # epsilon : root label
    return t[2]

def cof_subtree(t, path):         # t / n  : follow path (tuple of positions)
    if not path:
        return t
    _, s, a, kids = t
    ps = list(SPEC[s])
    i = ps.index(path[0])
    return cof_subtree(kids[i], path[1:])

def cof_delta(t):
    """delta(w): same skeleton, label each node n by subtree w/n. Recursive form:
       delta(w)=('C',shape, w, (delta(child),...))."""
    _, s, a, kids = t
    return ('C', s, t, tuple(cof_delta(k) for k in kids))

def cof_fmap(g, t):               # T(g): relabel every node's label by g
    _, s, a, kids = t
    return ('C', s, g(a), tuple(cof_fmap(g, k) for k in kids))

def check_comonad(C, A, depth, name):
    global SPEC; SPEC = C
    trees = cof_trees(C, A, depth)
    n_counitL = n_counitR = n_coassoc = 0
    for w in trees:
        # (eps T) . delta = id   : root label of delta(w) is w
        assert cof_label(cof_delta(w)) == w
        n_counitR += 1
        # (T eps) . delta = id   : fmap eps over delta(w)
        assert cof_fmap(cof_label, cof_delta(w)) == w
        n_counitL += 1
        # coassoc: (T delta).delta == (delta T).delta
        lhs = cof_fmap(cof_delta, cof_delta(w))   # (T delta).delta
        rhs = cof_delta(cof_delta(w))             # (delta T).delta
        assert lhs == rhs
        n_coassoc += 1
    print(f"[COFREE {name}] depth<= {depth}: {len(trees)} trees | "
          f"counitL {n_counitL}, counitR {n_counitR}, coassoc {n_coassoc}  ALL PASS")

# =====================================================================
# FREE MONAD  C* : T(A) = mu X. A + Sigma_s (P s -> X)
# tree = ('V', a)                         variable leaf carrying a in A
#      | ('N', shape, (child_for_p,...))  internal node
# =====================================================================

def free_trees(C, A, size):
    """All free C-trees with <= `size` internal nodes, variables in A."""
    out = []
    if size >= 0:
        for a in A:
            out.append(('V', a))
    if size >= 1:
        for s, ps in C.items():
            if not ps:
                out.append(('N', s, ()))                       # uses 1 node
            else:
                # distribute size-1 nodes among children (each child a full subtree)
                for kids in product(*[free_trees(C, A, size-1) for _ in ps]):
                    out.append(('N', s, tuple(kids)))
    # dedup
    seen=set(); uniq=[]
    for t in out:
        if t not in seen: seen.add(t); uniq.append(t)
    return uniq

def free_eta(a):                  # eta : a -> variable leaf
    return ('V', a)

def free_graft(t, g):
    """mu-core: replace each variable leaf ('V',a) by g(a) (a free tree)."""
    if t[0] == 'V':
        return g(t[1])
    _, s, kids = t
    return ('N', s, tuple(free_graft(k, g) for k in kids))

def free_mu(tt):
    """mu : T(TA)->TA. Here a T(TA) element is a free tree whose VARIABLES carry
       free trees (TA elements). Graft each such tree in place."""
    return free_graft(tt, lambda subtree: subtree)

def free_fmap(g, t):              # T(g): relabel variables
    if t[0] == 'V':
        return ('V', g(t[1]))
    _, s, kids = t
    return ('N', s, tuple(free_fmap(g, k) for k in kids))

def check_monad(C, A, size, name):
    trees = free_trees(C, A, size)
    nL=nR=nAssoc=0
    for w in trees:
        # mu . eta_T = id : eta at TA level wraps w as a variable, mu unwraps
        assert free_mu(('V', w)) == w; nR+=1
        # mu . T eta = id : fmap eta makes each var a one-leaf tree, graft restores
        assert free_mu(free_fmap(free_eta, w)) == w; nL+=1
    # associativity needs T(T(TA)). Test on triple-nested built from small pieces.
    small = free_trees(C, A, 1)
    cnt=0
    for w in free_trees(C, A, size):
        # build a TTT element by relabelling variables of w with TT-elements
        # (cycle through small trees-of-trees). Keep it finite/representative.
        for base in small[:3]:
            ttt = free_fmap(lambda a, b=base: free_fmap(lambda c: ('V',('V',c)), b), w)
            # (mu . T mu) vs (mu . mu T)
            lhs = free_mu(free_fmap(free_mu, ttt))
            rhs = free_mu(free_mu(ttt))
            assert lhs == rhs; cnt+=1; nAssoc+=1
    print(f"[FREE   {name}] size<= {size}: {len(trees)} trees | "
          f"unitL {nL}, unitR {nR}, assoc {nAssoc}  ALL PASS")

# =====================================================================
SPEC = Maybe
if __name__ == '__main__':
    A2 = ['a','b']; A3=['a','b','c']
    check_comonad(Maybe, A2, 3, 'Maybe')
    check_comonad(Maybe, A2, 4, 'Maybe')
    check_comonad(Bin,   A2, 3, 'Bin')
    check_monad(Maybe, A2, 3, 'Maybe')
    check_monad(Maybe, A3, 3, 'Maybe')
    check_monad(Bin,   A2, 2, 'Bin')
    check_monad(Bin,   A2, 3, 'Bin')
    print("\nAll comonad & monad laws verified on enumerated small trees.")
