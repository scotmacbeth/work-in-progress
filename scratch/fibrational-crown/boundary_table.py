"""
BOUNDARY TABLE for the "crown equivalence" TFAE (PROVE 2026-08-05).

For each Set-monad M we probe the five would-be-equivalent conditions and
report whether they COINCIDE or SPLIT.  The key risk flagged by the spec:
does "cartesian monad" (2) actually equal "non-branching / arity<=1" (5)?
List and Reader are the suspected splitters.

Conditions probed (per monad):
  arity      : the SET of leaf-counts |lv(m)| that occur           -> (5) non-branching = arity subset {0,1}
  cart_fun   : does fmap(u) preserve leaf-count for a NON-INJECTIVE u?
               (fmap merges leaves  <=>  M not a polynomial functor, e.g. Pf)   -> half of (1)/(2)
  cart_mu    : does mu preserve total leaf-count (no merging in multiplication)? -> half of (1)/(2), cartesian monad
  Tcart      : does T_M preserve a CARTESIAN container morphism (u,f) with u non-injective, f iso?
               (this is condition (1) literally)                                 -> (1)
  str_empty  : is str iso at a NULLARY shape, i.e. |M(1)| == 1?  (M preserves terminal)
  str_binary : is str iso at a BINARY shape, i.e. M(Z1 x Z2) ~= M Z1 x M Z2 ?    (M preserves the 2-fold product)
               str_empty AND str_binary(for all occurring arities) = (3) lambda invertible
  revE2      : does the reverse kappa (lax comparison) satisfy the E2' assoc axiom? = (4) (already proved <=> (5))

We use small finite test data.  List/State are exercised on bounded data
(length<=2 lists; that is enough to WITNESS branching and product-non-preservation).
"""
from itertools import product as iproduct, combinations

# ----------------------------------------------------------------------
# A monad is given by obj/fmap/eta/mu/leaves over finite sets.
# leaves(m) : ordered list of the X-labels sitting at the leaves of m.
#             |leaves(m)| = the arity of the shape of m.
# ----------------------------------------------------------------------
class Monad:
    def __init__(self, obj, fmap, eta, mu, leaves, name, polynomial=True):
        self.obj, self.fmap, self.eta, self.mu = obj, fmap, eta, mu
        self.leaves, self.name = leaves, name
        self.polynomial = polynomial

def Id():
    return Monad(lambda X:list(X), lambda f:(lambda x:f(x)),
                 lambda x:x, lambda mm:mm, lambda m:[m], 'Id')

def Maybe():
    obj = lambda X: [('inl',x) for x in X]+[('bot',)]
    fmap= lambda f:(lambda e:('inl',f(e[1])) if e[0]=='inl' else ('bot',))
    return Monad(obj, fmap, lambda x:('inl',x),
                 lambda e: e[1] if e[0]=='inl' else ('bot',),
                 lambda m:[m[1]] if m[0]=='inl' else [], 'Maybe(X+1)')

def Exc(E=('e0','e1')):           # exception monad E + X, |E| exceptions
    E=tuple(E)
    obj = lambda X: [('inl',x) for x in X]+[('exc',e) for e in E]
    fmap= lambda f:(lambda e:('inl',f(e[1])) if e[0]=='inl' else e)
    return Monad(obj, fmap, lambda x:('inl',x),
                 lambda e: e[1] if e[0]=='inl' else e,
                 lambda m:[m[1]] if m[0]=='inl' else [], f'Exc({len(E)}+X)')

def Writer(elems, op, unit, name='Writer'):
    obj = lambda X: [('w',x,n) for x in X for n in elems]
    return Monad(obj, lambda f:(lambda e:('w',f(e[1]),e[2])),
                 lambda x:('w',x,unit),
                 lambda e:('w',e[1][1],op(e[1][2],e[2])),
                 lambda m:[m[1]], name)

def Pf():                         # finite powerset: NOT polynomial (fmap/mu merge)
    def obj(X):
        X=list(X); res=[]
        for r in range(len(X)+1):
            for c in combinations(X,r): res.append(frozenset(c))
        return res
    return Monad(obj, lambda f:(lambda s:frozenset(f(x) for x in s)),
                 lambda x:frozenset([x]),
                 lambda ss:frozenset().union(*ss) if ss else frozenset(),
                 lambda m:sorted(m,key=str), 'Pf', polynomial=False)

def Reader(K=(0,1)):              # A^K  (representable) - NOT in Pi-Mendler class
    K=tuple(K)
    obj = lambda X:[tuple(t) for t in iproduct(X,repeat=len(K))]
    return Monad(obj, lambda f:(lambda e:tuple(f(v) for v in e)),
                 lambda x:tuple(x for _ in K),
                 lambda mm:tuple(mm[i][i] for i in range(len(K))),
                 lambda m:list(m), f'Reader(A^{len(K)})')

def ListB(maxlen=2):             # free monoid, BOUNDED length for finiteness
    def obj(X):
        X=list(X); res=[()]
        for L in range(1,maxlen+1):
            for t in iproduct(X,repeat=L): res.append(t)
        return res
    # mu = concatenation (flatten); may exceed maxlen but we only feed small data
    return Monad(obj, lambda f:(lambda t:tuple(f(x) for x in t)),
                 lambda x:(x,),
                 lambda tt:tuple(x for sub in tt for x in sub),
                 lambda m:list(m), f'List(len<={maxlen})')

def StateB(S=(0,1)):             # State X = (S x X)^S, bounded/representable-like
    S=tuple(S)
    # element = function S -> (S,X) ; represent as tuple over S of (s',x)
    def obj(X):
        X=list(X)
        codomain=[(s2,x) for s2 in S for x in X]
        return [tuple(t) for t in iproduct(codomain,repeat=len(S))]
    def fmap(f):
        return lambda e: tuple((sx[0],f(sx[1])) for sx in e)
    def eta(x): return tuple((s,x) for s in S)     # s |-> (s,x)
    def mu(mm):
        # mm : S -> (S, State X);  result s = run inner at the returned state
        res=[]
        for i,s in enumerate(S):
            s2, innerfn = mm[i]        # innerfn is a State X element (tuple over S)
            j=S.index(s2)
            res.append(innerfn[j])     # (s3, x)
        return tuple(res)
    leaves = lambda m:[sx[1] for sx in m]          # the X-labels, one per s in S
    return Monad(obj, fmap, eta, mu, leaves, f'State(S={len(S)})', polynomial=False)

# ----------------------------------------------------------------------
# PROBES
# ----------------------------------------------------------------------
def arity_profile(M, X=('p','q')):
    return sorted(set(len(M.leaves(m)) for m in M.obj(list(X))))

def cart_functor(M, Xsize=2):
    """fmap(u) with u NON-injective: does leaf-count ever drop? (merge => not polynomial)"""
    X=list(range(Xsize)); u=lambda z:0            # collapse everything to 0
    merged=False; worst=None
    for m in M.obj(X):
        n0=len(M.leaves(m)); n1=len(M.leaves(M.fmap(u)(m)))
        if n1<n0:
            merged=True; worst=(m, n0, n1); break
    return (not merged), worst

def cart_mu(M, Xsize=2):
    """does mu preserve total leaf-count? (merge in multiplication => non-cartesian monad)"""
    X=list(range(Xsize)); merged=False; worst=None
    MMX = M.obj(M.obj(X))
    for mm in MMX:
        inner = sum(len(M.leaves(lb)) for lb in M.leaves(mm))
        got   = len(M.leaves(M.mu(mm)))
        if got<inner:
            merged=True; worst=(mm, inner, got); break
    return (not merged), worst

def T_preserves_cartesian(M):
    """
    Condition (1) LITERALLY.  Take a cartesian container morphism (u,f):(S,P)->(T,Q):
    u:S->T arbitrary, f_s: Q(u s) -> P(s) a BIJECTION (so P ~= u^*Q).
    T_M(u,f) has backward at m in MS:  Q*(M u m) -> P*(m).
    Cartesian-preserved <=> that backward map is a bijection for all m.
    We pick a NON-INJECTIVE u to stress leaf-merging, f = identity bijection.
    """
    S=['a','b']; T=['t']; u={'a':'t','b':'t'}
    P={'a':[0,1],'b':[0,1]}; Q={'t':[0,1]}
    f={'a':{0:0,1:1},'b':{0:0,1:1}}               # Q(u s)=Q(t)={0,1} -> P(s) bijection
    # P* over S-fibres ; Q* over T-fibres
    def leaves_labels(m): return M.leaves(m)      # labels are elements of the SHAPE set
    ok=True; worst=None
    for m in M.obj(S):                            # m in M S
        mt = M.fmap(lambda s:u[s])(m)             # in M T
        labsS=M.leaves(m); labsT=M.leaves(mt)
        # P*(m) = prod_{b in labsS} P(label_b) ; Q*(mt)=prod_{c in labsT} Q(label_c)
        Pstar = list(iproduct(*[P[l] for l in labsS])) if labsS else [()]
        Qstar = list(iproduct(*[Q[l] for l in labsT])) if labsT else [()]
        # backward map: for a Q*-tuple q (one pos per target leaf c), produce a P*-tuple
        # (one pos per source leaf b) by: source leaf b has label x_b, target leaf u(x_b);
        # if fmap merged, several source leaves share ONE target leaf -> map is not injective
        # We just compare CARDINALITIES: cartesian-preserved needs |Qstar|==|Pstar|.
        if len(Qstar)!=len(Pstar):
            ok=False; worst=(m,len(Pstar),len(Qstar)); break
    return ok, worst

def str_empty(M):
    """str iso at nullary shape  <=>  M(1) ~= 1."""
    return len(M.obj([0]))==1

def str_binary(M):
    """str iso at a binary shape <=> M(Z1 x Z2) -> M Z1 x M Z2 is a bijection (M preserves 2-fold product)."""
    Z1=[0,1]; Z2=['x','y']
    prod=[(a,b) for a in Z1 for b in Z2]
    lhs=M.obj(prod)                               # M(Z1 x Z2)
    # str(w) = (M pi1 w, M pi2 w)
    img=set()
    for w in lhs:
        a=M.fmap(lambda t:t[0])(w); b=M.fmap(lambda t:t[1])(w)
        img.add((str(a),str(b)))
    rhs_card=len(M.obj(Z1))*len(M.obj(Z2))
    # iso iff str injective (|img|==|lhs|) AND surjective (|img|==rhs_card)
    return (len(img)==len(lhs)) and (len(img)==rhs_card)

# reverse-kappa E2' : reuse the entwine machinery result.  Non-branching => holds.
# We give the KNOWN verdict (proved in affine-classification / entwine.py):
#   Maybe/Exc/Writer/Id : E2' holds ;  Pf/List/State/Reader(branching) : E2' fails.
def revE2_known(M):
    prof=arity_profile(M)
    return all(k<=1 for k in prof)                # E2' <=> non-branching (Thm A, proved)

# ----------------------------------------------------------------------
# RUN
# ----------------------------------------------------------------------
Z2add=lambda a,b:(a+b)%2
T2=[(0,0),(0,1),(1,0),(1,1)]
t2op=lambda g,f:(g[f[0]],g[f[1]]); T2u=(0,1)

monads=[Id(), Maybe(), Exc(('e',)), Writer([0,1],Z2add,0,'Writer(Z2)'),
        Writer(T2,t2op,T2u,'Writer(T2,noncomm)'),
        ListB(2), Pf(), Reader((0,1)), StateB((0,1))]

hdr=f"{'monad':22s} {'arity':10s} {'nonbr(5)':8s} {'cartFun':7s} {'cartMu':6s} {'Tcart(1)':8s} {'strEmp':6s} {'strBin':6s} {'lamInv(3)':9s} {'revE2(4)':8s}"
print(hdr); print('-'*len(hdr))
rows=[]
for M in monads:
    prof=arity_profile(M)
    nonbr=all(k<=1 for k in prof)
    cf,_=cart_functor(M); cm,_=cart_mu(M)
    tc,_=T_preserves_cartesian(M)
    se=str_empty(M); sb=str_binary(M)
    # lambda invertible (3): str iso at EVERY occurring arity.
    #   arity 0 present -> need str_empty ; arity>=2 present -> need str_binary(& higher)
    laminv = True
    if 0 in prof: laminv = laminv and se
    if any(k>=2 for k in prof): laminv = laminv and sb
    # arity exactly {1}: str trivially iso (id) -> laminv True
    re2=revE2_known(M)
    cartmonad = cf and cm
    def yn(b): return ' Y' if b else ' .'
    print(f"{M.name:22s} {str(prof):10s} {yn(nonbr):8s} {yn(cf):7s} {yn(cm):6s} {yn(tc):8s} {yn(se):6s} {yn(sb):6s} {yn(laminv):9s} {yn(re2):8s}")
    rows.append((M.name,prof,nonbr,cf,cm,tc,se,sb,laminv,re2,cartmonad))

print()
print("LEGEND: nonbr(5)=arity<=1 ; cartFun=fmap preserves leaves ; cartMu=mu preserves leaves ;")
print("        cartMonad=(cartFun & cartMu)=(1)/(2) ; Tcart(1)=T_M preserves cartesian morphisms ;")
print("        strEmp=M1~1 ; strBin=M preserves 2-prod ; lamInv(3)=str iso at all occurring arities ;")
print("        revE2(4)=reverse kappa E2' holds (<=>non-branching, proved).")
print()
print("SPLIT ANALYSIS")
print("-"*40)
cartset=set(r[0] for r in rows if r[10])
nonbrset=set(r[0] for r in rows if r[2])
laminvset=set(r[0] for r in rows if r[8])
print(f"  cartesian-monad  (1)/(2): {sorted(cartset)}")
print(f"  non-branching    (4)/(5): {sorted(nonbrset)}")
print(f"  lambda-invertible   (3) : {sorted(laminvset)}")
print()
print(f"  cartesian \\ non-branching (SPLITTERS of (2)<->(5)): {sorted(cartset-nonbrset)}")
print(f"  non-branching \\ lambda-inv (SPLITTERS of (5)<->(3)): {sorted(nonbrset-laminvset)}")
print(f"  lambda-inv \\ non-branching (Reader-type, needs Pi-Mendler restriction): {sorted(laminvset-nonbrset)}")
print()
# consistency check: (1) Tcart == cartesian-monad ?
print("  (1) Tcart  vs  (2) cartesian-monad agreement:")
for r in rows:
    tag='' if r[5]==r[10] else '   <-- MISMATCH'
    print(f"     {r[0]:22s} Tcart={r[5]}  cartMonad={r[10]}{tag}")
