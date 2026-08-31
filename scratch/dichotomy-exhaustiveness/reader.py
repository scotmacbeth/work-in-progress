"""
Reader-lifting monad-law checker.  Given aggregator L (Poly over E vars),
candidate unit eps (per L-shape: a chosen slot (v,j)) and candidate mult del
(a nat transf A2 => B2), build the lifting T as an endofunctor on containers
with unit/mult, and check the three monad laws on small test containers by
comparing backward maps element-by-element.

Containers here: (S = list of shape names, P = dict shape->size).
"""
from itertools import product
from poly import Poly, subst, mono, make_A2_B2, enum_nats, nat_act

# ---- converters between L-native and A2/B2 encodings ----
def native_to_A2(e, elt):
    # native (s,(f_b)_b) -> A2 elt (s, combo over E^2) with combo[b*e+b]=f_b
    s, fbs = elt
    n2 = e*e
    combo = [() for _ in range(n2)]
    for b in range(e):
        combo[b*e+b] = tuple(fbs[b])
    return (s, tuple(combo))

def B2_to_nested(e, L, B2elt):
    # B2 elt (s', combo over E^2) -> nested (s', (F_b)) where
    # F_b is list over [a_{s'}(b)] of (s'', (g_c)).  We must UNfold subst.
    # We reconstruct by re-deriving the subst structure. Simpler: we recompute
    # B2's shape decomposition. To avoid fragility we instead build B2 elements
    # by construction and keep a parallel "nested" builder.  (Handled in eval_B2.)
    raise NotImplementedError

# Because unfolding subst is fragile, we instead evaluate the nested functor
# directly and enumerate del as a nat transf between the DIRECTLY-evaluated
# functors, using a canonical element listing.  See NestedFunctors below.

class Nested:
    """Directly evaluate the two functors of D:E^2->Set that del connects:
       Dom(D) = L(b |-> D(b,b))
       Cod(D) = L(b |-> L(c |-> D(b,c)))
       Elements listed canonically so a nat transf = index map on a universal D.
    """
    def __init__(self, L, e):
        self.L = L; self.e = e
    def dom_eval(self, D):   # D: dict (b,c)->size
        L,e = self.L,self.e
        sizes = tuple(D[(b,b)] for b in range(e))
        return L.eval(sizes)   # (s,(f_b)) with f_b:[a_s(b)]->range(D[b,b])
    def cod_eval(self, D):
        L,e = self.L,self.e
        # inner sets: for each b, innerset_b = L.eval(sizes c->D[b,c]) as a list
        inner = []
        for b in range(e):
            inner.append(L.eval(tuple(D[(b,c)] for c in range(e))))
        sizes = tuple(len(inner[b]) for b in range(e))
        outer = L.eval(sizes)   # (s',(F_b)) F_b:[a_{s'}(b)]->range(len inner_b)
        # decode into nested actual elements
        res = []
        for (sp, Fbs) in outer:
            decoded = tuple(tuple(inner[b][Fbs[b][k]] for k in range(len(Fbs[b])))
                            for b in range(e))
            res.append(((sp, Fbs), decoded, inner))
        return res, inner

# universal family D0: give each (b,c) a distinct large-enough size and distinct labels
# We represent naturality-respecting nat transfs by their action, enumerated as
# container morphisms between Dom and Cod viewed as polynomials over E^2.
# For that we still need Dom,Cod as Poly over E^2 -> reuse make_A2_B2.

def enum_eps(L):
    # per shape choose a slot (v,j) with j in range(arity_v); require total arity>=1
    per = []
    for ar in L.shapes:
        slots = [(v,j) for v in range(L.n) for j in range(ar[v])]
        if not slots:
            return   # no unit possible
        per.append(slots)
    for choice in product(*per):
        yield list(choice)

def eps_apply(L, eps, elt):
    # elt in L(<A>) native (here A native = L.eval(sizes all equal)); (s,combo) combo[v]:tuple
    s, combo = elt
    v,j = eps[s]
    return combo[v][j]

# ---------- build T as endofunctor on containers ----------
def T_pos(L, e, P, m):
    # m: tuple length e of shapes; returns list of positions (L-native)
    sizes = tuple(P[m[v]] for v in range(e))
    return L.eval(sizes)

def check_laws(L, e, eps, A2, B2, delta, tests):
    """delta: nat transf A2=>B2. Check monad laws on given test containers.
       Returns True iff all laws hold on all tests. Uses container-morphism defs."""
    # index lookups
    for (S,P) in tests:
        # --- objects ---
        Sh = list(product(S, repeat=e))              # Reader shapes S^E as tuples
        # positions of T(S,P): dict m -> list
        Tp = {m: T_pos(L,e,P,m) for m in Sh}
        Tp_idx = {m: {el:i for i,el in enumerate(Tp[m])} for m in Sh}
        # --- unit backward at shape s (in S): eps at family <P[s]> ---
        # eta fwd: s -> const_s ; check right/left unit & assoc via mu,Teta,etamu
        # Build mu^T backward using delta.
        # For a double shape mm in S^{E^2} (tuple length e*e, index b*e+c):
        Sh2 = list(product(S, repeat=e*e))
        def mu_fwd(mm):
            return tuple(mm[b*e+b] for b in range(e))
        # TT positions at mm : L over family b-> Tp[m_b], m_b=(mm[b*e+c])_c
        def m_b(mm,b): return tuple(mm[b*e+c] for c in range(e))
        def TTpos(mm):
            inner = [Tp[m_b(mm,b)] for b in range(e)]
            sizes = tuple(len(inner[b]) for b in range(e))
            outer = L.eval(sizes)
            return outer, inner
        # mu backward: from Tp[mu mm] -> TTpos(mm), via delta (A2=>B2) at D=(b,c)->P[mm[b,c]]
        def mu_bwd_fn(mm):
            D = {(b,c): P[mm[b*e+c]] for b in range(e) for c in range(e)}
            # domain elements as A2.eval(D as sizes over E^2)
            sizesE2 = tuple(D[(b//e, b%e)] for b in range(e*e))
            domA2 = A2.eval(sizesE2)
            codB2 = B2.eval(sizesE2)
            # map A2/B2 elements to native T/TT elements
            outer, inner = TTpos(mm)
            inner_idx = [{el:i for i,el in enumerate(inner[b])} for b in range(e)]
            outer_idx = {el:i for i,el in enumerate(outer)}
            # A2 native: (s, combo over E^2), only (b,b) nonzero. -> Tp[mu mm] native (s,(f_b))
            mm_mu = mu_fwd(mm)
            Tp_mu = Tp[mm_mu]
            Tpmu_idx = {el:i for i,el in enumerate(Tp_mu)}
            def A2_to_T(a2):
                s, combo = a2
                fbs = tuple(combo[b*e+b] for b in range(e))
                return Tpmu_idx[(s, fbs)]
            def B2_to_TT(b2):
                sp, combo = b2
                # B2 = subst(L, b-> subst(L,c->y_{(b,c)})). Need to decode combo (over E^2)
                # into nested. We recompute via matching against outer/inner by re-evaluation.
                # Instead: build the SAME B2 element from scratch is hard; use a bijection
                # constructed by enumerating B2.eval and TT in the SAME order.
                raise NotImplementedError
            # fallback handled below
            return None
        # The B2->TT decoding is the crux; handled by aligned enumeration (see check2).
        return None
    return None
