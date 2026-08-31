"""
Test NON-polynomial (analytic) aggregators L : Set^E -> Set for a monad lifting.
Focus on the UNIT obstruction: a natural eps : L(<A>) -> A must pick, naturally
in A, an element of A from each x in L(<A>). We brute-force search for ANY natural
eps over small A, and report whether one exists.  (No natural eps => no lifting.)
"""
from itertools import product, permutations

def natural_eps_exists(barL_eval, barL_act, sizes=(1,2,3)):
    """barL_eval(k)->list of elements of barL([k]); barL_act(elt, f)->elt for f:[k]->[k'].
       Search for eps: for each k a function elt->range(k), natural under all f.
       We check existence via: eps must be equivariant; use the orbit/naturality constraints.
       Practical check: eps_A(x) must be fixed under all bijections of A fixing x, and
       natural under all maps. We test: for A=range(n), for each x, the set of 'forced'
       values = intersection over all endomaps f of preimages... we just test naturality
       of a candidate built from A=large distinct, pulled back."""
    # Strategy: build eps on the 'generic' element via naturality from a large set,
    # then verify. A natural transf barL=>Id is determined by its value on each element
    # of barL(N) for N large with distinct labels, and must be natural. Equivalent:
    # for the terminal-ish, eps_N(x) in N; naturality under f:N->M forces eps_M(barL f x)=f(eps_N x).
    # We test consistency: for N=range(n), define orbits under Sym(N); eps must be Sym(N)-equivariant
    # AND natural under all N->N maps. We search by trying to assign eps_N and checking.
    n=3
    elts=barL_eval(n)
    # candidate assignment must satisfy: for every map f:[n]->[n], eps(barL f x)=f(eps x)
    maps=list(product(range(n),repeat=n))
    # set up variables eps[x] in range(n); constraint propagation
    # Try all assignments? too many. Use naturality under CONSTANT maps first:
    # f=const_j : barL f x = barL(const_j)(x); eps(that)=j for ALL x. So eps(const-image)=j.
    # const image element c_j := barL(const_j)(x0) is same for all x (functor of constant).
    # gives eps(c_j)=j. Then naturality under injections etc.
    # We'll just brute force assignments consistent with all maps, for n=3 (|elts| small if L small).
    import itertools
    idx={x:i for i,x in enumerate(elts)}
    # precompute action of each map on each element
    act={}
    for f in maps:
        for x in elts:
            act[(f,x)]=barL_act(x, list(f))
    # backtracking over eps values
    assign={}
    def consistent(x,val):
        for f in maps:
            fx=act[(f,x)]
            if fx in assign_full:
                if assign_full[fx]!=f[val]:
                    return False
        return True
    # simpler: solve as constraints eps(act[f,x]) == f[eps[x]] ; use fixpoint over full assignment guesses
    # brute force: for each element independent value in range(n), filter by all constraints
    from itertools import product as prod
    keys=list(elts)
    for guess in prod(range(n),repeat=len(keys)):
        assign_full={keys[i]:guess[i] for i in range(len(keys))}
        ok=True
        for f in maps:
            for x in elts:
                if assign_full[act[(f,x)]]!=f[assign_full[x]]:
                    ok=False;break
            if not ok:break
        if ok:
            return True, assign_full
    return False, None

if __name__=="__main__":
    e=2
    # ---- analytic: symmetric square of leaf 0 : L(B)=Sym^2(B_0) ----
    def sym2_eval(k):
        return [frozenset([a]) if a==b else frozenset([a,b]) for a in range(k) for b in range(k) if a<=b]
    def sym2_act(elt, f):
        return frozenset(f[a] for a in elt)
    ok,asg=natural_eps_exists(sym2_eval, sym2_act)
    print(f"Sym^2(B_0): natural eps exists? {ok}")

    # ---- analytic: Bag (finite multiset) of leaf 0, size exactly 2 : unordered-with-mult ----
    from collections import Counter
    def bag2_eval(k):
        res=[]
        for a in range(k):
            for b in range(k):
                if a<=b:
                    res.append(tuple(sorted((a,b))))
        return res
    def bag2_act(elt,f):
        return tuple(sorted((f[elt[0]],f[elt[1]])))
    ok,asg=natural_eps_exists(bag2_eval, bag2_act)
    print(f"Bag_2(B_0) (unordered pair w/mult): natural eps exists? {ok}")

    # ---- sanity: polynomial B_0^2 (ordered) SHOULD have eps ----
    def ord2_eval(k):
        return [(a,b) for a in range(k) for b in range(k)]
    def ord2_act(elt,f):
        return (f[elt[0]],f[elt[1]])
    ok,asg=natural_eps_exists(ord2_eval, ord2_act)
    print(f"B_0^2 (ordered, polynomial): natural eps exists? {ok}  (expect True)")
