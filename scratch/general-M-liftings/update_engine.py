"""
UPDATE-MONAD lifting engine.  Fork of honest.py / lean_assoc.py, generalised from the
STATE monad to the SIMPLY-TYPED UPDATE MONAD  <<M>> X = S -> P x X  of Ahman-Uustalu,
parametrised by (monoid P, right action  down: S x P -> S).

  Reader  = update monad for P = 1 (trivial monoid), down trivial.  orbits(down) = |S|.
  State   = update monad for P = free monoid on overwrite semigroup, down = overwrite.
            orbits(down) = 1  (overwrite is transitive).

M as a polynomial functor:  <<M>> X = Sigma_{f: S->P}  X^S.
  shape  f in P^S ;  positions = S  (CONSTANT, = |S|).   [the "grade" is the update f]
  unit   eta x = lam s. (o, x)                 -> shape OSHAPE=(o,...,o), value const.
  mult   mu F  = lam s. let (p,g)=F s; (p',x)=g (s down p) in (p (+) p', x)
     shape thread:  f'(s) = f(s) (+) g_s( s down f(s) )
     value thread:  z(s)  = x_s( s down f(s) )     [inner read at endpoint s' = s down f(s)]

Aggregator lifting (grade-independent by prior proof): A_f = A (same list of objects for
every shape f). Object (s,c): reads exactly position s (degree-1 = discrete opfibration).
A degree-1 transport is fixed by OUT,INN:  composite object (s,c)@f' routes to
  outer (s, OUT)@f  reading position s,   inner (s down f(s), INN)@g_s reading endpoint.
This is the update-monad analogue of free_transport.py; the STATE case (down=eval) is honest.py.
"""
from itertools import product

S = [0, 1]

# ---------------- monoid + action parametrisation ----------------
class Act:
    def __init__(self, elems, o, oplus, down, name=""):
        self.elems = list(elems)      # monoid carrier
        self.o = o                    # identity
        self.oplus = oplus            # oplus(a,b) = a (+) b
        self.down = down              # down(s,p) = s down p
        self.name = name
        self.SHAPES = [tuple(f) for f in product(self.elems, repeat=len(S))]
        self.OSHAPE = tuple(o for _ in S)
        self._check_monoid_action()

    def _check_monoid_action(self):
        E, o, op, dn = self.elems, self.o, self.oplus, self.down
        for a in E:
            assert op(o, a) == a and op(a, o) == a, "unit"
        for a in E:
            for b in E:
                for c in E:
                    assert op(op(a, b), c) == op(a, op(b, c)), "assoc"
        for s in S:
            assert dn(s, o) == s, "action unit"
            for p in E:
                for q in E:
                    assert dn(s, op(p, q)) == dn(dn(s, p), q), "action mult"

    def orbits(self):
        # connected components of S under s ~ s down p
        parent = {s: s for s in S}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def uni(a, b):
            parent[find(a)] = find(b)
        for s in S:
            for p in self.elems:
                uni(s, self.down(s, p))
        return len({find(s) for s in S})

    def thread(self, f, gvec):
        # composite outer shape f'(s) = f(s) (+) g_s(s down f(s))
        return tuple(self.oplus(f[s], gvec[s][self.down(s, f[s])]) for s in S)

# ---------------- aggregator plumbing (identical to honest.py) ----------------
def slots(obj):
    n0, n1 = obj
    return [(0, i) for i in range(n0)] + [(1, i) for i in range(n1)]

def Apos(A, f, Q):
    out = []
    for j, obj in enumerate(A[f]):
        sl = slots(obj); pools = [Q[s] for (s, i) in sl]
        for ch in product(*pools):
            out.append((j, ch))
    return out

def M_shapes(act, S0):
    return [(f, x) for f in act.SHAPES for x in product(S0, repeat=len(S))]

def T_container(act, A, C):
    S0, P = C
    sh = M_shapes(act, S0); Pd = {}
    for (f, x) in sh:
        Q = (P[x[0]], P[x[1]]); Pd[(f, x)] = tuple(Apos(A, f, Q))
    return (sh, Pd)

# ---------------- eta : Id => T ----------------
def eta_morph(act, A, eps, C):
    S0, P = C; TC = T_container(act, A, C)
    fwd = {s0: (act.OSHAPE, (s0, s0)) for s0 in S0}
    bwd = {}
    for s0 in S0:
        Q = (P[s0], P[s0]); m = {}
        for (j, ch) in Apos(A, act.OSHAPE, Q):
            m[(j, ch)] = ch[eps[j]]
        bwd[s0] = m
    return (C, TC, fwd, bwd)

# ---------------- mu backward at one <<M>>^2 shape ----------------
def mu_bwd_at(act, A, delta, P, w):
    (f, y) = w                                  # y[s] = (g_s, x_s)
    gvec = tuple(y[s][0] for s in S)
    xvec = tuple(y[s][1] for s in S)
    fprime = act.thread(f, gvec)
    z = tuple(xvec[s][act.down(s, f[s])] for s in S)
    img = (fprime, z)
    Q = (P[z[0]], P[z[1]]); route = delta[(f, gvec)]; m = {}
    for (j, ch) in Apos(A, fprime, Q):
        out_j, inner, beta = route[j]
        out_slots = slots(A[f][out_j]); outer = []
        for ai, a in enumerate(out_slots):
            (sa, ia) = a; k = inner[ai]; kobj = A[gvec[sa]][k]; ic = []
            for bi, b in enumerate(slots(kobj)):
                ic.append(ch[beta[(ai, bi)]])
            outer.append((k, tuple(ic)))
        m[(j, ch)] = (out_j, tuple(outer))
    return img, m

def mu_morph(act, A, delta, C):
    S0, P = C
    TC = T_container(act, A, C); TTC = T_container(act, A, TC)
    fwd = {}; bwd = {}
    for w in TTC[0]:
        img, m = mu_bwd_at(act, A, delta, P, w)
        fwd[w] = img; bwd[w] = m
    return (TTC, TC, fwd, bwd)

# ---------------- T on a morphism f: C->D (shape untouched) ----------------
def T_on(act, A, f):
    C, D, ff, fb = f
    TC = T_container(act, A, C); TD = T_container(act, A, D)
    S0, P = C; S0d, Pd = D; fwd = {}; bwd = {}
    for (t, x) in TC[0]:
        xd = tuple(ff[x[s]] for s in S); fwd[(t, x)] = (t, xd)
        Qd = (Pd[xd[0]], Pd[xd[1]]); m = {}
        for (j, chd) in Apos(A, t, Qd):
            sl = slots(A[t][j])
            nc = tuple(fb[x[s]][tok] for (tok, (s, i)) in zip(chd, sl))
            m[(j, chd)] = (j, nc)
        bwd[(t, x)] = m
    return (TC, TD, fwd, bwd)

# ---------------- generic morphism plumbing ----------------
def compose(g, f):
    Cf, Df, ff, fb = f; Dg, Eg, gf, gb = g
    fwd = {s: gf[ff[s]] for s in ff}; bwd = {}
    for s in ff:
        ds = ff[s]; bwd[s] = {ep: fb[s][gb[ds][ep]] for ep in gb[ds]}
    return (Cf, Eg, fwd, bwd)

def ident(C):
    S0, P = C
    return (C, C, {s: s for s in S0}, {s: {p: p for p in P[s]} for s in S0})

def eq_morph(a, b):
    return a[2] == b[2] and a[3] == b[3]

# ---------------- law checks (lean, sampled assoc) ----------------
TINY = (['a'], {'a': ('a0', 'a1')})

def check_units(act, A, eps, delta, C=TINY):
    TC = T_container(act, A, C)
    eta = eta_morph(act, A, eps, C); mu = mu_morph(act, A, delta, C)
    if not eq_morph(compose(mu, T_on(act, A, eta)), ident(TC)):
        return False
    etaT = eta_morph(act, A, eps, TC)
    if not eq_morph(compose(mu, etaT), ident(TC)):
        return False
    return True

def assoc_sample(act, A, eps, delta, C=TINY, nsamp=400, seed=0):
    import random
    random.seed(seed)
    S0, P = C
    TC = T_container(act, A, C); Ptc = TC[1]; S0tc = TC[0]
    S0ttc = M_shapes(act, S0tc)
    ttt = M_shapes(act, S0ttc)
    if len(ttt) > nsamp:
        ttt = random.sample(ttt, nsamp)
    for w3 in ttt:
        (t3, X3) = w3
        muC_fwd = {}; muC_bwd = {}
        for s in S:
            img, m = mu_bwd_at(act, A, delta, P, X3[s]); muC_fwd[s] = img; muC_bwd[s] = m
        X2 = tuple(muC_fwd[s] for s in S); w2 = (t3, X2)
        img1, muAtw2 = mu_bwd_at(act, A, delta, P, w2)
        Q_TT = (Ptc[X2[0]], Ptc[X2[1]]); Tmu_bwd = {}
        for (j, chd) in Apos(A, t3, Q_TT):
            sl = slots(A[t3][j])
            nc = tuple(muC_bwd[s][tok] for (tok, (s, i)) in zip(chd, sl))
            Tmu_bwd[(j, chd)] = (j, nc)
        lhs = {p: Tmu_bwd[muAtw2[p]] for p in muAtw2}
        img_r2, muTC_bwd = mu_bwd_at(act, A, delta, Ptc, w3)
        img_r1, muC2 = mu_bwd_at(act, A, delta, P, img_r2)
        rhs = {p: muTC_bwd[muC2[p]] for p in muC2}
        if img1 != img_r1:
            return ('FWD-MISMATCH', w3)
        if lhs != rhs:
            return ('ASSOC-FAIL', w3)
    return ('ok', len(ttt))

def laws_ok(act, A, eps, delta, nsamp=400):
    if not check_units(act, A, eps, delta):
        return False
    return assoc_sample(act, A, eps, delta, nsamp=nsamp)[0] == 'ok'

# ---------------- degree-1 transport builder (fork of free_transport) ----------------
def build_deg1(act, O, OUT, INN):
    """O: dict s->list objs.  OUT[(f,gvec,s,c)]=obj at pos s.  INN[(f,gvec,s,c)]=obj at pos down(s,f[s])."""
    lst = []; idx = {}
    for s in S:
        for c in O[s]:
            idx[(s, c)] = len(lst); lst.append((1, 0) if s == 0 else (0, 1))
    A = {f: list(lst) for f in act.SHAPES}
    IDX = {f: dict(idx) for f in act.SHAPES}
    eps = {i: 0 for i in range(len(lst))}
    delta = {}
    for f in act.SHAPES:
        for gvec in product(act.SHAPES, repeat=len(S)):
            fp = act.thread(f, gvec); route = {}
            for s in S:
                for c in O[s]:
                    j = IDX[fp][(s, c)]
                    outc = OUT[(f, gvec, s, c)]; out_j = IDX[f][(s, outc)]
                    m = act.down(s, f[s])                    # endpoint position
                    innc = INN[(f, gvec, s, c)]
                    inner = {0: IDX[gvec[s]][(m, innc)]}
                    route[j] = (out_j, inner, {(0, 0): 0})
            delta[(f, gvec)] = route
    return A, eps, delta
