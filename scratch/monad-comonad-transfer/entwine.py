"""
ENTWINING of the two container liftings of a Set-monad M (PROVE 2026-07-27).

  T_M : Cont -> Cont   (Ahman-Bauer Thm 6.3, monad)   T_M(S,P) = (M S, P*)
        with the PI-cointerpretation weak Mendler algebra
        P*(m) = prod_{b in leaves(m)} P(label b).
  G_M : Cont -> Cont   (transfer, comonad)             G_M(S,P) = (S, M o P).

Question: distributive law lambda between T_M (monad) and G_M (comonad).

Claim to test:
  * The canonical  str_Z : M(prod_b Z_b) -> prod_b M(Z_b)  (M applied to projections)
    assembles into a MIXED DISTRIBUTIVE LAW  lambda : T_M G_M => G_M T_M  (TG => GT),
    for EVERY monad M.  Verify the 4 entwining axioms.
  * The reverse GT => TG needs the LAX map prod_b M Z_b -> M(prod_b Z_b), which exists
    (coherently) iff M is a COMMUTATIVE monad.  Test on commutative vs non-commutative M.

A monad M here is a POLYNOMIAL (container) monad exposed by its LEAF structure:
   leaves(m) = list of (leaf_id, label)   with label in the carrier set;
   an element of M X is (shape, labelling).  We give obj/fmap/eta/mu + leaves.
"""
from itertools import product as iproduct

# ---------------- containers & morphisms (as in check.py) ----------------
class Cont:
    def __init__(self, S, P):
        self.S = list(S)
        self.P = {s: list(P[s]) for s in S}

class Mor:
    def __init__(self, src, tgt, fwd, bwd):
        self.src, self.tgt, self.fwd, self.bwd = src, tgt, fwd, bwd

def ident(A):
    return Mor(A, A, {s: s for s in A.S},
               {s: {p: p for p in A.P[s]} for s in A.S})

def compose(psi, phi):
    """phi:A->B, psi:B->C  ==> A->C. backward composes in opposite order."""
    A, C = phi.src, psi.tgt
    fwd = {s: psi.fwd[phi.fwd[s]] for s in A.S}
    bwd = {}
    for s in A.S:
        t = phi.fwd[s]
        g = psi.bwd[t]      # C.P[fwd_C t] -> B.P[t]
        f = phi.bwd[s]      # B.P[t] -> A.P[s]
        bwd[s] = {c: f[g[c]] for c in C.P[fwd[s]]}
    return Mor(A, C, fwd, bwd)

def eq(m1, m2):
    if m1.fwd != m2.fwd: return False
    if set(m1.bwd) != set(m2.bwd): return False
    for s in m1.bwd:
        if m1.bwd[s] != m2.bwd[s]: return False
    return True

# ---------------- polynomial monads via leaf structure -------------------
# Represent an element of M X canonically as a hashable tuple.  We provide:
#   obj(X)   : list of elements of M X
#   fmap(f)  : function on M-elements
#   eta(x)   : X-elt -> M X
#   mu(mm)   : M(M X) elt -> M X
#   leaves(m): ordered list of labels (the multiset of X-elements at the leaves)
# leaves order is CANONICAL (fixed by the shape) so P*(m) tuples are well-defined.

class Monad:
    def __init__(self, obj, fmap, eta, mu, leaves, name):
        self.obj, self.fmap, self.eta, self.mu = obj, fmap, eta, mu
        self.leaves, self.name = leaves, name

# --- Maybe = exception A+1: leaves(inl a)=[a], leaves(inr)=[] ---
def Maybe():
    obj = lambda X: [('inl', x) for x in X] + [('bot',)]
    fmap = lambda f: (lambda e: ('inl', f(e[1])) if e[0]=='inl' else ('bot',))
    eta  = lambda x: ('inl', x)
    mu   = lambda e: e[1] if e[0]=='inl' else ('bot',)
    leaves = lambda m: [m[1]] if m[0]=='inl' else []
    return Monad(obj, fmap, eta, mu, leaves, 'Maybe')

# --- Reader A^K : element = tuple (a_k)_{k in K}; leaves = the K labels ---
def Reader(K=(0,1)):
    K = tuple(K)
    obj = lambda X: [tuple(t) for t in iproduct(X, repeat=len(K))]
    fmap = lambda f: (lambda e: tuple(f(v) for v in e))
    eta  = lambda x: tuple(x for _ in K)
    # mu : (X^K)^K -> X^K   diagonal: (mm)[i] is an X^K; result_i = mm[i][i]
    mu   = lambda mm: tuple(mm[i][i] for i in range(len(K)))
    leaves = lambda m: list(m)                 # K leaves, labels m[0..|K|-1]
    return Monad(obj, fmap, eta, mu, leaves, f'Reader^{len(K)}')

# --- Finite powerset Pf : element = frozenset; leaves = sorted elements ---
def Pf():
    def obj(X):
        X=list(X)
        from itertools import combinations
        res=[]
        for r in range(len(X)+1):
            for c in combinations(X, r):
                res.append(frozenset(c))
        return res
    fmap = lambda f: (lambda s: frozenset(f(x) for x in s))
    eta  = lambda x: frozenset([x])
    mu   = lambda ss: frozenset().union(*ss) if ss else frozenset()
    def leaves(m):
        return sorted(m, key=str)
    return Monad(obj, fmap, eta, mu, leaves, 'Pf')

# --- Writer over a monoid N (may be NON-commutative): A x N ---
def Writer(elems, op, unit, name='Writer'):
    obj = lambda X: [('w', x, n) for x in X for n in elems]
    fmap = lambda f: (lambda e: ('w', f(e[1]), e[2]))
    eta  = lambda x: ('w', x, unit)
    mu   = lambda e: ('w', e[1][1], op(e[1][2], e[2]))   # ('w',('w',x,n1),n2)->('w',x, n1*n2)
    leaves = lambda m: [m[1]]                             # single leaf label
    return Monad(obj, fmap, eta, mu, leaves, name)

# --- List truncated? Lists are infinite; we test List obstruction separately/symbolically.

# ---------------- P* : the PI-cointerpretation weak Mendler algebra ------
# P is a dict label -> list of positions.  An element of P*(m) is a tuple choosing,
# for each leaf b of m (in canonical order), a position in P(label_b).
def Pstar_set(M, P, m):
    labs = M.leaves(m)
    if not labs:
        return [()]                      # empty product = singleton
    return [tuple(t) for t in iproduct(*[P[lab] for lab in labs])]

# ---------------- G_M and T_M as endofunctors on Cont --------------------
def G_obj(M, A):
    return Cont(A.S, {s: M.obj(A.P[s]) for s in A.S})

def T_obj(M, A):
    S2 = M.obj(A.S)                                  # shapes = M S
    P2 = {m: Pstar_set(M, A.P, m) for m in S2}
    return Cont(S2, P2)

# --------- helper: does the composite of shapes/positions match? ----------
def same_cont(A, B):
    return A.S == B.S and all(sorted(map(str,A.P[s]))==sorted(map(str,B.P[s])) for s in A.S)

# ---------------- the entwining lambda : T G X -> G T X ------------------
# forward: identity on shapes M S. backward: str  [G T pos] -> [T G pos].
# We BUILD it as a Cont morphism  src = T_M G_M X ,  tgt = G_M T_M X.
#   src positions at m=(shape over S with labels in S): (M P)*(m) = prod_b M(P(x b))
#   tgt positions at m:                                 M(P*(m)) = M(prod_b P(x b))
# backward map bwd[m]: tgt-pos -> src-pos  == str : M(prod_b Z_b) -> prod_b M Z_b.
def lambda_entwine(M, A):
    TG = T_obj(M, G_obj(M, A))        # T_M(G_M A):  shapes M S, positions (M P)*
    GT = G_obj(M, T_obj(M, A))        # G_M(T_M A):  shapes M S, positions M(P*)
    fwd = {m: m for m in TG.S}
    bwd = {}
    for m in TG.S:                    # m in M S
        labs = M.leaves(m)            # the S-labels x(b)
        # str : M(prod_b P(lab_b)) -> prod_b M(P(lab_b))
        # an element w in M(prod_b P(lab_b)) is an M-structure over tuples t=(p_b)_b.
        # str(w)[b] = M(pi_b)(w) = fmap(t |-> t[b])(w).   Together a tuple over b.
        bwd[m] = {}
        for w in GT.P[m]:             # w in M(P*(m)) = M(prod_b P(lab_b))
            tup = tuple(M.fmap((lambda t, b=b: t[b]))(w) for b in range(len(labs)))
            bwd[m][w] = tup           # element of prod_b M(P(lab_b)) = TG.P[m]
    return Mor(TG, GT, fwd, bwd)      # T_M G_M A -> G_M T_M A

# sanity: bwd lands in the right set
def lambda_welltyped(M, A):
    lam = lambda_entwine(M, A)
    TG, GT = lam.src, lam.tgt
    for m in GT.S:
        srcset = set(map(str, TG.P[m]))
        for w in GT.P[m]:
            if str(lam.bwd[m][w]) not in srcset:
                return False, (m, w, lam.bwd[m][w])
    return True, None

# ---------------- functor actions G(phi), T(phi) for naturality ----------
def G_mor(M, phi):
    GA, GB = G_obj(M, phi.src), G_obj(M, phi.tgt)
    fwd = dict(phi.fwd); bwd = {}
    for s in GA.S:
        t = phi.fwd[s]
        Mf = M.fmap((lambda p, s=s: phi.bwd[s][p]))
        bwd[s] = {m: Mf(m) for m in GB.P[t]}
    return Mor(GA, GB, fwd, bwd)

def T_mor(M, phi):
    # T(phi):(M S,P*)->(M T,Q*), forward M(u) on shapes; backward on positions.
    TA, TB = T_obj(M, phi.src), T_obj(M, phi.tgt)
    u = phi.fwd
    fwd = {m: M.fmap(lambda s: u[s])(m) for m in TA.S}
    bwd = {}
    for m in TA.S:                       # m in M S; leaves labels x(b) in S
        labsS = M.leaves(m)              # labels x(b) in S (source leaves)
        mt = fwd[m]                      # in M T; leaves labels u(x(b))
        labsT = M.leaves(mt)             # target leaf labels (may be FEWER: fmap can merge)
        tpos = {str(lab): j for j, lab in enumerate(labsT)}   # label -> target leaf index
        bwd[m] = {}
        for q in TB.P[mt]:               # q : one position per target leaf
            # source leaf b (label x_b): target leaf = u(x_b); pull q there, then f_{x_b}
            tup = tuple(phi.bwd[labsS[b]][q[tpos[str(u[labsS[b]])]]] for b in range(len(labsS)))
            bwd[m][q] = tup
    return Mor(TA, TB, fwd, bwd)

# ---------------- (co)unit / (co)mult of T and G ------------------------
def eps_G(M, A):                          # G A -> A, backward eta
    GA = G_obj(M, A)
    return Mor(GA, A, {s:s for s in A.S},
               {s:{p:M.eta(p) for p in A.P[s]} for s in A.S})
def delta_G(M, A):                        # G A -> G G A, backward mu
    GA=G_obj(M,A); GGA=G_obj(M,GA)
    return Mor(GA, GGA, {s:s for s in A.S},
               {s:{mm:M.mu(mm) for mm in GGA.P[s]} for s in A.S})

def eta_T(M, A):                          # A -> T A, forward eta on shapes; backward i_P
    TA = T_obj(M, A)
    fwd = {s: M.eta(s) for s in A.S}
    bwd = {}
    for s in A.S:
        m = fwd[s]                        # eta(s) in M S, leaves = [s] (single leaf labelled s)
        # T A positions at m: P*(m)=prod_{single leaf} P(s) ; i_P: that -> P(s)
        bwd[s] = {tup: tup[0] for tup in TA.P[m]}
    return Mor(A, TA, fwd, bwd)

def mu_T(M, A):                           # T T A -> T A, forward mu; backward j (label-matching)
    # Valid for the PI-Mendler class (Pf, Maybe, Id): labels of leaves(mu mm) are DISTINCT,
    # so j = restriction: nested leaf (b,c') with label a maps to the unique leaf of mu(mm)
    # carrying label a.  (Pf: restriction h|_{S'};  arity<=1 monads: trivial.)
    TTA = T_obj(M, T_obj(M, A)); TA = T_obj(M, A)
    fwd = {mm: M.mu(mm) for mm in TTA.S}
    bwd = {}
    for mm in TTA.S:                      # mm in M(M S)
        m = fwd[mm]                       # mu(mm) in M S
        outer = M.leaves(mm)             # outer leaf labels: elements of M S
        inner = [M.leaves(lb) for lb in outer]   # inner leaf labels: elements of S
        lm = M.leaves(m)                 # leaves of mu(mm): labels in S, DISTINCT (Pf/Maybe/Id)
        assert len(lm) == len(set(map(str, lm))), (M.name, 'labels not distinct', lm)
        pos_of = {str(lab): i for i, lab in enumerate(lm)}   # label -> leaf index in mu(mm)
        bwd[mm] = {}
        for tup in TA.P[m]:              # tup: one position per leaf of mu(mm)
            res = []
            for b in range(len(outer)):
                res.append(tuple(tup[pos_of[str(inner[b][c])]] for c in range(len(inner[b]))))
            bwd[mm][tup] = tuple(res)
    return Mor(TTA, TA, fwd, bwd)

# ---------------- entwining axioms (lambda: T G => G T) -----------------
# Using T monad (eta_T,mu_T), G comonad (eps_G,delta_G). Standard mixed-DL axioms:
# (E1 unit-T)  lambda o (eta_T G) = G(eta_T)            : G => G T
# (E2 mult-T)  lambda o (mu_T G)  = G(mu_T) o (lambda T) o (T lambda) : T T G => G T
# (E3 counit-G) (eps_T? ) : (G eps? ) ... use  (eps_G T) o lambda = T(eps_G) : T G => T
# (E4 comult-G) (delta_G T) o lambda = (G lambda) o (lambda G) o (T delta_G) : T G => G G T
def check_axioms(M, A):
    lam = lambda_entwine(M, A)                       # T G A -> G T A
    GA = G_obj(M,A); TA = T_obj(M,A)
    out = {}

    # E1: lam o eta_T(GA) = G(eta_T A)      both  G A -> G T A
    lhs = compose(lam, eta_T(M, GA))
    rhs = G_mor(M, eta_T(M, A))
    out['E1 unit-T'] = eq(lhs, rhs)

    # E3: eps_G(TA) o lam = T(eps_G A)      both  T G A -> T A
    lhs = compose(eps_G(M, TA), lam)
    rhs = T_mor(M, eps_G(M, A))
    out['E3 counit-G'] = eq(lhs, rhs)

    # E4: delta_G(TA) o lam = G(lam) o lam(G A) o T(delta_G A)   T G A -> G G T A
    lhs = compose(delta_G(M, TA), lam)
    lamGA = lambda_entwine(M, GA)                    # T G (G A) -> G T (G A)
    rhs = compose(G_mor(M, lam), compose(lamGA, T_mor(M, delta_G(M, A))))
    out['E4 comult-G'] = eq(lhs, rhs)

    # E2: lam o mu_T(GA) = G(mu_T A) o lam(TA) o T(lam)          T T G A -> G T A
    lhs = compose(lam, mu_T(M, GA))
    lamTA = lambda_entwine(M, TA)                    # T G (T A) -> G T (T A)
    Tlam  = T_mor(M, lam)                            # T(T G A) -> T(G T A)
    rhs = compose(G_mor(M, mu_T(M, A)), compose(lamTA, Tlam))
    out['E2 mult-T'] = eq(lhs, rhs)
    return out

# ---------------- test containers ----------------
A1 = Cont(['a','b'], {'a':[0,1], 'b':[0]})
A2 = Cont(['a'],     {'a':[0,1,2]})

# non-commutative monoid: full transformation monoid T_2 on {0,1} (4 elts), as tuples (f0,f1)
T2 = [(0,0),(0,1),(1,0),(1,1)]      # (f(0),f(1))
def t2op(g,f):                       # composition g o f
    return (g[f[0]], g[f[1]])
T2_unit = (0,1)                      # identity
def is_comm(elems, op):
    return all(op(a,b)==op(b,a) for a in elems for b in elems)

print("="*68)
print("ENTWINING  lambda : T_M G_M => G_M T_M   (TG => GT, the str direction)")
print("="*68)
for M in [Maybe(), Pf(),
          Writer([0,1], lambda a,b:(a+b)%2, 0, 'Writer/Z2'),
          Writer(T2, t2op, T2_unit, 'Writer/T2(noncomm)')]:
    wt,_ = lambda_welltyped(M, A1)
    ax = check_axioms(M, A1)
    print(f"\nM = {M.name}   lambda well-typed: {wt}")
    for k,v in ax.items():
        print(f"    {k:14s}: {'PASS' if v else 'FAIL'}")

# ==================== naturality of lambda : T G => G T ====================
def lambda_natural(M, phi):
    # square: lam_Y o (T G)(phi) = (G T)(phi) o lam_X   for phi: X -> Y
    X, Y = phi.src, phi.tgt
    lamX = lambda_entwine(M, X)          # T G X -> G T X
    lamY = lambda_entwine(M, Y)          # T G Y -> G T Y
    TGphi = T_mor(M, G_mor(M, phi))      # T G X -> T G Y
    GTphi = G_mor(M, T_mor(M, phi))      # G T X -> G T Y
    lhs = compose(lamY, TGphi)           # T G X -> G T Y
    rhs = compose(GTphi, lamX)
    return eq(lhs, rhs)

phi_nt = Mor(A1, Cont(['x'], {'x':[10,11,12]}),
             {'a':'x','b':'x'},
             {'a':{10:0,11:1,12:0}, 'b':{10:0,11:0,12:0}})

print("\n" + "="*68)
print("NATURALITY of lambda : T G => G T  (on a nontrivial morphism)")
print("="*68)
for M in [Maybe(), Pf(), Writer([0,1], lambda a,b:(a+b)%2, 0, 'Writer/Z2')]:
    print(f"  M={M.name:10s}: lambda natural = {lambda_natural(M, phi_nt)}")

# ==================== reverse GT => TG via the LAX map ====================
# needs rho : prod_b M(Z_b) -> M(prod_b Z_b) (lax monoidal). Provide per commutative monad.
# For Pf: rho((S_b)_b) = cartesian product {(z_b): z_b in S_b} as a subset of prod_b Z_b.
def lambda_rev_Pf(A):
    M = Pf()
    GT = G_obj(M, T_obj(M, A))     # shapes M S, positions M(P*) = Pf(prod_b P)
    TG = T_obj(M, G_obj(M, A))     # shapes M S, positions (M P)* = prod_b Pf(P)
    fwd = {m:m for m in GT.S}
    bwd = {}
    for m in GT.S:                 # m in Pf S
        labs = M.leaves(m)
        bwd[m] = {}
        for t in TG.P[m]:          # t = (S_b)_b, S_b in Pf(P(lab_b))  (each t[b] a frozenset)
            # cartesian product -> a subset of prod_b P(lab_b)
            if len(labs)==0:
                cart = frozenset([()])
            else:
                cart = frozenset(tuple(c) for c in iproduct(*[list(t[b]) for b in range(len(labs))]))
            bwd[m][t] = cart       # in Pf(prod_b P) = GT.P[m]
    return Mor(GT, TG, fwd, bwd)   # G T A -> T G A

# axioms for lambda' : G T => T G (mirror set)
# E1' counit-G:  (eps_G' side)   T(eps_G) o lam' = eps_G(TA)  ... use dual squares:
# We check the 4 mixed-DL axioms for lam':GT=>TG:
#  (a) lam' o (G eta_T) = eta_T G          A? : G A -> T G A
#  (b) lam' o (G mu_T)  = mu_T G o (T lam') o (lam' T)
#  (c) (T eps_G) o lam' = eps_G T          G T A -> T A? -> ...
#  (d) (T delta_G) o lam' = (lam' G) o (G lam') o (delta_G T)
def check_axioms_rev_Pf(A):
    M = Pf()
    lam = lambda_rev_Pf(A)                       # G T A -> T G A
    GA = G_obj(M,A); TA = T_obj(M,A)
    out = {}
    # (a) lam o G(eta_T A) = eta_T(GA)     both  G A -> T G A
    lhs = compose(lam, G_mor(M, eta_T(M,A)))
    rhs = eta_T(M, GA)
    out["E1' unit-T"] = eq(lhs, rhs)
    # (c) T(eps_G A) o lam = eps_G(TA)     both  G T A -> T A
    lhs = compose(T_mor(M, eps_G(M,A)), lam)
    rhs = eps_G(M, TA)
    out["E3' counit-G"] = eq(lhs, rhs)
    # (d) T(delta_G A) o lam = lam(GA) o G(lam) o delta_G(TA)   G T A -> T G G A
    lhs = compose(T_mor(M, delta_G(M,A)), lam)
    lamGA = lambda_rev_Pf(GA)                     # G T (G A) -> T G (G A)
    rhs = compose(lamGA, compose(G_mor(M, lam), delta_G(M, TA)))
    out["E4' comult-G"] = eq(lhs, rhs)
    # (b) lam o G(mu_T A) = mu_T(GA) o T(lam) o lam(TA)   G T T A -> T G A
    lhs = compose(lam, G_mor(M, mu_T(M,A)))
    lamTA = lambda_rev_Pf(TA)                     # G T (T A) -> T G (T A)
    rhs = compose(mu_T(M, GA), compose(T_mor(M, lam), lamTA))
    out["E2' mult-T"] = eq(lhs, rhs)
    return out

print("\n" + "="*68)
print("REVERSE  lambda' : G T => T G  via LAX map (Pf, COMMUTATIVE)")
print("="*68)
for k,v in check_axioms_rev_Pf(A1).items():
    print(f"    {k:14s}: {'PASS' if v else 'FAIL'}")

# ---- generic reverse lambda' : G T => T G via a supplied LAX map --------
def lambda_rev(M, lax, A):
    # lax(labs, t) : t=(w_b)_b with w_b in M(P(lab_b))  ->  element of M(prod_b P(lab_b))
    GT = G_obj(M, T_obj(M, A)); TG = T_obj(M, G_obj(M, A))
    fwd = {m:m for m in GT.S}; bwd = {}
    for m in GT.S:
        labs = M.leaves(m)
        bwd[m] = {t: lax(M, A.P, labs, t) for t in TG.P[m]}
    return Mor(GT, TG, fwd, bwd)

def lax_Maybe(M, P, labs, t):
    # t = (w_b): if all inl -> inl of tuple of contents; if any bot -> bot
    if any(w[0]=='bot' for w in t):
        return ('bot',)
    return ('inl', tuple(w[1] for w in t))

def check_axioms_rev(M, lax, A):
    lam = lambda_rev(M, lax, A)
    GA = G_obj(M,A); TA = T_obj(M,A); out={}
    out["E1' unit-T"]   = eq(compose(lam, G_mor(M, eta_T(M,A))), eta_T(M, GA))
    out["E3' counit-G"] = eq(compose(T_mor(M, eps_G(M,A)), lam), eps_G(M, TA))
    lamGA = lambda_rev(M, lax, GA)
    out["E4' comult-G"] = eq(compose(T_mor(M, delta_G(M,A)), lam),
                             compose(lamGA, compose(G_mor(M, lam), delta_G(M, TA))))
    lamTA = lambda_rev(M, lax, TA)
    out["E2' mult-T"]   = eq(compose(lam, G_mor(M, mu_T(M,A))),
                             compose(mu_T(M, GA), compose(T_mor(M, lam), lamTA)))
    return out

print("\n" + "="*68)
print("REVERSE  lambda' : G T => T G  via LAX  (triangulation)")
print("="*68)
for k,v in check_axioms_rev(Maybe(), lax_Maybe, A1).items():
    print(f"  Maybe  {k:14s}: {'PASS' if v else 'FAIL'}")

# locate the E2' failure for Pf explicitly
print("\n-- locating Pf E2' failure --")
M = Pf(); A = A1
lam = lambda_rev_Pf(A); GA=G_obj(M,A)
lhs = compose(lam, G_mor(M, mu_T(M,A)))
lamTA = lambda_rev_Pf(T_obj(M,A))
rhs = compose(mu_T(M, GA), compose(T_mor(M, lam), lamTA))
diffs=0
for s in lhs.bwd:
    for k in lhs.bwd[s]:
        if lhs.bwd[s].get(k)!=rhs.bwd[s].get(k):
            if diffs<3:
                print(f"  shape {s} pos {k}:  lhs={lhs.bwd[s][k]}  rhs={rhs.bwd[s].get(k)}")
            diffs+=1
print(f"  total differing entries: {diffs}")

print("\n" + "="*68)
print("str non-triviality + extra coverage")
print("="*68)
# Is str : M(prod Z) -> prod M Z ever non-iso?  (else forward E2 would be vacuous)
for M in [Pf(), Maybe()]:
    lam = lambda_entwine(M, A1)
    noniso = False
    for m in lam.tgt.S:
        dom = len(lam.tgt.P[m]); cod = len(lam.src.P[m])   # |M(prod)| vs |prod M|
        if dom != cod: noniso = True
    print(f"  M={M.name:6s}: str non-iso somewhere = {noniso}")

# forward axioms on a second container A2 = ({a}, {a:[0,1,2]}) and Pf on 3-elt positions
A2 = Cont(['a'], {'a':[0,1,2]})
print("  forward entwining on A2:")
for M in [Pf(), Maybe(), Writer(T2, t2op, T2_unit,'Writer/T2')]:
    ax = check_axioms(M, A2)
    print(f"    M={M.name:12s}: {'ALL PASS' if all(ax.values()) else ax}")

# asked-direction GT=>TG on A2 (should fail E2' for Pf; pass for Maybe)
print("  asked GT=>TG (lax) on A2:")
axm = check_axioms_rev(Maybe(), lax_Maybe, A2)
print(f"    Maybe: {'ALL PASS' if all(axm.values()) else axm}")
axp = check_axioms_rev_Pf(A2)
print(f"    Pf   : {axp}")

# ============ FINAL forward-entwining sweep: all monads x all containers ============
print("\n" + "="*68)
print("FINAL forward lambda:TG=>GT sweep (all 4 axioms must PASS)")
print("="*68)
conts = {'A1({a:2,b:1})': A1, 'A2({a:3})': A2,
         'A3({a:2,b:2})': Cont(['a','b'],{'a':[0,1],'b':[0,1]})}
monads = [Maybe(), Pf(),
          Writer([0,1], lambda a,b:(a+b)%2,0,'Writer/Z2'),
          Writer(T2,t2op,T2_unit,'Writer/T2nc')]
allpass=True
for cn,C in conts.items():
    for M in monads:
        ax=check_axioms(M,C); ok=all(ax.values()); allpass&=ok
        if not ok: print(f"  FAIL {M.name} on {cn}: {ax}")
print(f"  forward entwining: ALL PASS across {len(conts)}x{len(monads)} cases = {allpass}")

# asked GT=>TG: show it fails on branching containers but passes on A2 for Pf
print("\n asked GT=>TG (lax) branching-obstruction map:")
KEY='E2\' mult-T'
for cn,C in conts.items():
    axp=check_axioms_rev_Pf(C)
    others=all(v for k,v in axp.items() if k!=KEY)
    print(f"   Pf on {cn:16s}: E2(mult)={axp[KEY]}   others_all_pass={others}")
