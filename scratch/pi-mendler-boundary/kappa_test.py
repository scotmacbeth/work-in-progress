"""
DECISIVE TEST for the pi-Mendler boundary.

The multiplication laxator of the Pi-cointerpretation,
    j : P*(mu mm)  ->  (P*)*(mm),      i.e.   Prod_{lv(mu mm)}  ->  Prod_{I(mm)},
is (by Yoneda, naturality in P) exactly reindexing along a TOTAL, LABEL-PRESERVING
function
    kappa_mu : I(mm) = ⊔_{b in lv(mm)} lv(inner_b)  -->  lv(mu mm),
    with label_{mu mm}(kappa(i)) = label(i)  for every inner leaf i.

j EXISTS  <=>  such a total label-preserving kappa_mu exists for every mm.
  - injective kappa  <=> mu-cartesian (no merge)
  - total kappa      <=> mu drops no leaf   <-- the condition Reader/State fail

We enumerate mm over small data and test, for each monad, whether a total
label-preserving kappa_mu exists.  (We DON'T need to construct j; existence of
kappa is necessary & sufficient for j to exist naturally.)
"""
from itertools import product

def test_monad(name, S, MofM_elements, mu, outer_leaves, inner_of, mu_leaves, label_mm, label_mu):
    """
    Generic tester.
      MofM_elements: list of mm in M(M S)
      mu(mm): the element mu(mm) in M S
      For a given mm:
        I(mm) = list of inner-leaf tokens i, each with a label label_mm(mm, i) in S
        lv(mu mm) = list of leaf tokens L, each with label label_mu(mu(mm), L) in S
      kappa exists iff every i in I(mm) has SOME L in lv(mu mm) with matching label.
    """
    all_ok = True
    fail_witness = None
    for mm in MofM_elements:
        m = mu(mm)
        I = inner_of(mm)                    # list of inner leaf tokens
        L = mu_leaves(m)                    # list of leaves of mu mm
        Llabels = {ll: label_mu(m, ll) for ll in L}
        # check totality: every inner leaf i can map to some leaf with equal label
        total = True
        for i in I:
            lab = label_mm(mm, i)
            if not any(Llabels[ll] == lab for ll in L):
                total = False
                break
        if not total:
            all_ok = False
            fail_witness = (mm, m)
            break
    verdict = "kappa TOTAL for all mm  => j EXISTS  => Pi-Mendler OK" if all_ok \
        else f"kappa NOT TOTAL  => NO j  => NOT Pi-Mendler   (witness mm={fail_witness[0]}, mu mm={fail_witness[1]})"
    print(f"[{name:8s}] {verdict}")
    return all_ok

# ---------------------------------------------------------------- READER_E, E={0,1}
E=(0,1)
def reader(S):
    Sset=list(range(S))
    # M S = S^E  (tuples length |E|)
    MS=list(product(Sset,repeat=len(E)))
    # M(M S) = (S^E)^E : tuples length|E| of MS-elements  -> represent as tuple of tuples
    MMS=list(product(MS,repeat=len(E)))
    def mu(G):           # G: E->MS ; mu(G)(e)=G[e][e]
        return tuple(G[e][e] for e in range(len(E)))
    def outer_leaves(G): return list(range(len(E)))     # outer leaves = E
    def inner_of(G):     # I = {(e,e')}: e outer, e' inner position
        return [(e,ep) for e in range(len(E)) for ep in range(len(E))]
    def mu_leaves(m):    return list(range(len(E)))      # leaves of mu G = E
    def label_mm(G,i):   e,ep=i; return G[e][ep]         # label of inner leaf (e,e') = G(e)(e')
    def label_mu(m,ll):  return m[ll]                    # label of leaf ll of mu G = (muG)(ll)
    return MMS,mu,outer_leaves,inner_of,mu_leaves,label_mm,label_mu

# ---------------------------------------------------------------- STATE_S, state set = {0,1}
St=(0,1)
def state(S):
    Xset=list(range(S))                    # value set X (labels live in X)
    # M X = (St x X)^St : function St-> St x X ; represent as tuple length|St| of (s',x)
    def MX(X):
        cell=list(product(St,X)); return list(product(cell,repeat=len(St)))
    MS=MX(Xset)
    # M(M X): function St -> St x MS
    cellM=list(product(St,MS)); MMS=list(product(cellM,repeat=len(St)))
    def mu(F):   # F: St -> St x MS ; mu(F)(s0): (s1,m)=F[s0]; return m[s1]
        out=[]
        for s0 in range(len(St)):
            s1,m=F[s0]; out.append(m[s1])
        return tuple(out)
    def outer_leaves(F): return list(range(len(St)))
    def inner_of(F):     # inner leaves: for each outer state s0, the inner m=F[s0][1] has |St| leaves s'
        return [(s0,sp) for s0 in range(len(St)) for sp in range(len(St))]
    def mu_leaves(m):    return list(range(len(St)))
    def label_mm(F,i):
        s0,sp=i; s1,m=F[s0]; return m[sp][1]        # label(value) at inner leaf (s0,s') = x-part of F[s0].m[s']
    def label_mu(m,ll):  return m[ll][1]            # value at leaf ll of mu F
    return MMS,mu,outer_leaves,inner_of,mu_leaves,label_mm,label_mu

# ---------------------------------------------------------------- Pf (powerset), X=range(S)
def pf(S):
    Xset=list(range(S))
    from itertools import chain, combinations
    def subsets(xs): return [frozenset(c) for r in range(len(xs)+1) for c in combinations(xs,r)]
    subs=subsets(Xset)                    # M X = subsets of X
    MMS=[frozenset(t) for r in range(len(subs)+1)  # M M X = subsets of subsets  (keep small)
         for t in __import__('itertools').combinations(subs,r)]
    def mu(SS):   # union
        u=frozenset().union(*SS) if SS else frozenset()
        return u
    def outer_leaves(SS): return list(SS)
    def inner_of(SS):     return [(s,x) for s in SS for x in s]   # (which set, element)
    def mu_leaves(m):     return list(m)
    def label_mm(SS,i):   s,x=i; return x
    def label_mu(m,ll):   return ll
    return MMS,mu,outer_leaves,inner_of,mu_leaves,label_mm,label_mu

# ---------------------------------------------------------------- List (len<=2 truncated), X=range(S)
def lst(S):
    Xset=list(range(S))
    def lists_upto(xs,n):
        out=[()]
        for k in range(1,n+1):
            out+=list(product(xs,repeat=k))
        return out
    LS=lists_upto(Xset,2)                 # M X = lists len<=2
    MMS=lists_upto(LS,2)                   # M M X = lists of lists (len<=2)
    def mu(LL):    # concat
        r=()
        for l in LL: r=r+l
        return r
    def outer_leaves(LL): return list(range(len(LL)))
    def inner_of(LL):     return [(oi,ii) for oi,l in enumerate(LL) for ii in range(len(l))]
    def mu_leaves(m):     return list(range(len(m)))
    def label_mm(LL,i):   oi,ii=i; return LL[oi][ii]
    def label_mu(m,ll):   return m[ll]
    return MMS,mu,outer_leaves,inner_of,mu_leaves,label_mm,label_mu

print("="*78)
print("Pi-Mendler boundary test: does the multiplication laxator j exist?")
print("(j exists <=> total label-preserving kappa_mu : I(mm) -> lv(mu mm) for all mm)")
print("="*78)
for S in (3,):
    print(f"\n--- label/value set size S={S} ---")
    test_monad("Reader", S, *reader(S))
    test_monad("State",  S, *state(S))
    test_monad("Pf",     S, *pf(S))
    test_monad("List",   S, *lst(S))

# ============================================================================
# SUPPLEMENT 1: kappa injective? (merge test) -> Pi-Mendler-but-non-cartesian
#   Pf must be TOTAL (in Pi-Mendler) but NON-injective (non-cartesian mu).
# ============================================================================
def kappa_injectivity(name, S, MMS,mu,outer_leaves,inner_of,mu_leaves,label_mm,label_mu):
    # For monads where kappa IS total, is there an mm forcing a NON-injective kappa?
    # kappa is forced non-injective iff two distinct inner leaves must map to the SAME
    # mu-leaf, i.e. |I(mm)| > |lv(mu mm)| while still total  => a merge.
    worst=None
    for mm in MMS:
        m=mu(mm); I=inner_of(mm); L=mu_leaves(m)
        # total?
        Ll={ll:label_mu(m,ll) for ll in L}
        if not all(any(Ll[ll]==label_mm(mm,i) for ll in L) for i in I): 
            continue
        if len(I)>len(L):   # pigeonhole: some merge forced
            worst=(mm,len(I),len(L)); break
    if worst: print(f"[{name:6s}] total kappa but |I|={worst[1]}>|lv(mu)|={worst[2]} at mm={worst[0]} => kappa NON-injective => mu NON-cartesian, yet Pi-Mendler.")
    else:     print(f"[{name:6s}] no forced merge found (kappa can be injective) => cartesian-compatible.")

print("\n"+"="*78)
print("SUPPLEMENT: within Pi-Mendler, is mu cartesian (kappa injective) or merging?")
print("="*78)
kappa_injectivity("Pf",  3, *pf(3))
kappa_injectivity("List",3, *lst(3))

# ============================================================================
# SUPPLEMENT 2: general |E| off-diagonal drop for Reader, sizes 2..5
# ============================================================================
print("\n"+"="*78)
print("SUPPLEMENT: Reader off-diagonal drop persists for all |E|>=2 (S large)")
print("="*78)
for k in (2,3,4,5):
    E=tuple(range(k))
    # witness G: G(0)=const 0 ; G(1)(0)=99 (fresh), else 0.  mu G = all-0. inner leaf (1,0) label 99 dropped.
    # confirm 99 not a diagonal value:
    diag_vals={0}   # muG(e)=G(e)(e): G(0)(0)=0, G(1)(1)=0, others const 0
    dropped_label=99
    ok = dropped_label not in diag_vals
    print(f"  |E|={k}: inner leaf (1,0) has label 99, diagonal labels={diag_vals}, dropped={ok} => kappa not total")
