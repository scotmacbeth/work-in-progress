#!/usr/bin/env python3
"""
Computational verification of the universal property of the free monad on a
container, using the EXACT coordinate conventions supplied in the task.

Conventions (verbatim):
  container morphism phi:(A,PA)=>(B,PB) = (phi1:A->B, phisharp_a: PB(phi1 a)->PA(a)) [BACKWARD on positions]
  (phi;psi)1 = psi1 . phi1 ; (phi;psi)sharp_a = phisharp_a . psisharp_{phi1 a}
  (G<F).Shape = (t,f), f:Q(t)->S ; Pos(t,f)=(q,p) q:Q(t), p:P(f q)
  tensor (phi<psi):(A<C)=>(B<D):
     1(a,g)=(phi1 a, j:PB(phi1 a) -> psi1(g(phisharp_a j)))
     sharp_{(a,g)}(j,k)=(phisharp_a j, psisharp_{g(phisharp_a j)} k)
  I=({*},{*:{*}}); leftUnitor I<F=>F; rightUnitor F<I=>F; associator (H<G)<F=>H<(G<F).

We build all four operations generically, verify the monoid laws for m_X and for
each test monoid M, then check A/B/C/D.
"""
import sys
from itertools import product

CAP = 20000          # safety cap for shape enumeration of composite containers
FAILURES = []        # (label, message) verbatim
PAIRS_CHECKED = 0    # count of (t,u) pairs checked in check C

# ---------------------------------------------------------------------------
# Trees over a container X = {'shapes':[...], 'pos': s->list}
# tree = ('lf',)  or  ('nd', s, ((p0,sub0),(p1,sub1),...)) sorted by position.
# ---------------------------------------------------------------------------
LF = ('lf',)

def nd(s, kappa_dict):
    items = tuple(sorted(kappa_dict.items(), key=lambda kv: kv[0]))
    return ('nd', s, items)

def kappa_of(t):
    return dict(t[2])

def leaves(t):
    if t == LF:
        return [()]
    kap = kappa_of(t)
    res = []
    for p in sorted(kap):            # P(s) order == sorted positions (== keys)
        for w in leaves(kap[p]):
            res.append((p,) + w)
    return res

def graft(t, u):
    # u : dict  leaf-path(of t) -> tree
    if t == LF:
        return u[()]
    s = t[1]; kap = kappa_of(t); newk = {}
    for p in sorted(kap):
        u_p = {r: u[(p,) + r] for r in leaves(kap[p])}
        newk[p] = graft(kap[p], u_p)
    return nd(s, newk)

def split(t, u, z):
    # z : leaf-path of graft(t,u) ; returns (leaf of t, leaf of u[that leaf])
    if t == LF:
        return ((), z)
    p = z[0]; z2 = z[1:]
    kap = kappa_of(t)
    u_p = {r: u[(p,) + r] for r in leaves(kap[p])}
    l2, w2 = split(kap[p], u_p, z2)
    return ((p,) + l2, w2)

def count_nodes(t):
    if t == LF:
        return 0
    return 1 + sum(count_nodes(sub) for _, sub in t[2])

def gen_trees_nodes(X, max_nodes):
    """All closed X-trees with <= max_nodes internal nodes."""
    memo = {}
    def gen(budget):
        if budget in memo:
            return memo[budget]
        res = [LF]
        if budget >= 1:
            for s in X['shapes']:
                ps = X['pos'](s)
                def rec(i, remaining):
                    if i == len(ps):
                        yield {}
                        return
                    for sub in gen(remaining):
                        n = count_nodes(sub)
                        if n > remaining:
                            continue
                        for rest in rec(i + 1, remaining - n):
                            d = dict(rest); d[ps[i]] = sub
                            yield d
                for kap in rec(0, budget - 1):
                    res.append(nd(s, kap))
        res = list(dict.fromkeys(res))
        memo[budget] = res
        return res
    return gen(max_nodes)

def gen_trees_depth(X, d):
    """All closed X-trees with depth <= d."""
    if d < 0:
        return []
    res = [LF]
    if d >= 1:
        sub = gen_trees_depth(X, d - 1)
        for s in X['shapes']:
            ps = X['pos'](s)
            for kap in product(sub, repeat=len(ps)):
                res.append(nd(s, dict(zip(ps, kap))))
    return list(dict.fromkeys(res))

# ---------------------------------------------------------------------------
# Generic containers & morphisms
# ---------------------------------------------------------------------------
class Cont:
    def __init__(self, name, pos_fn, enum_fn):
        self.name = name
        self._pos = pos_fn
        self._enum = enum_fn
    def pos(self, s):
        return self._pos(s)
    def enum_shapes(self):
        return self._enum()

class Mor:
    def __init__(self, name, dom, cod, f1, fsharp):
        self.name = name; self.dom = dom; self.cod = cod
        self.f1 = f1; self.fsharp = fsharp

# Unit container I
I = Cont('I', lambda s: ['*'], lambda: ['*'])

def cprod(G, F):
    def pos(shp):
        t, fvals = shp
        gp = G.pos(t)
        out = []
        for i, q in enumerate(gp):
            for p in F.pos(fvals[i]):
                out.append((q, p))
        return out
    def enum():
        out = []
        Fs = list(F.enum_shapes())
        for t in G.enum_shapes():
            gp = G.pos(t)
            for combo in product(Fs, repeat=len(gp)):
                out.append((t, combo))
                if len(out) > CAP:
                    return out
        return out
    return Cont('(%s<%s)' % (G.name, F.name), pos, enum)

def id_mor(C):
    return Mor('id_%s' % C.name, C, C, lambda s: s, lambda s, r: r)

def comp_mor(phi, psi):
    # phi:A=>B , psi:B=>C  ; (phi;psi):A=>C
    assert phi.cod is psi.dom or phi.cod.name == psi.dom.name
    def f1(s):
        return psi.f1(phi.f1(s))
    def fsharp(s, j):
        return phi.fsharp(s, psi.fsharp(phi.f1(s), j))
    return Mor('(%s;%s)' % (phi.name, psi.name), phi.dom, psi.cod, f1, fsharp)

def tensor_mor(phi, psi):
    # phi:A=>B , psi:C=>D  ; (phi<psi):(A<C)=>(B<D)
    A, B, C, D = phi.dom, phi.cod, psi.dom, psi.cod
    dom = cprod(A, C); cod = cprod(B, D)
    def f1(shp):
        a, gvals = shp
        b = phi.f1(a)
        Apos = A.pos(a); Bpos = B.pos(b)
        hvals = []
        for j in Bpos:
            qA = phi.fsharp(a, j)
            src_c = gvals[Apos.index(qA)]
            hvals.append(psi.f1(src_c))
        return (b, tuple(hvals))
    def fsharp(shp, r):
        a, gvals = shp
        j, k = r
        Apos = A.pos(a)
        qA = phi.fsharp(a, j)
        src_c = gvals[Apos.index(qA)]
        return (qA, psi.fsharp(src_c, k))
    return Mor('(%s<%s)' % (phi.name, psi.name), dom, cod, f1, fsharp)

def left_unitor(F):
    dom = cprod(I, F); cod = F
    def f1(shp):
        star, gvals = shp
        return gvals[0]          # g(*)
    def fsharp(shp, p):
        return ('*', p)
    return Mor('lam_%s' % F.name, dom, cod, f1, fsharp)

def right_unitor(F):
    dom = cprod(F, I); cod = F
    def f1(shp):
        s, gvals = shp
        return s
    def fsharp(shp, p):
        return (p, '*')
    return Mor('rho_%s' % F.name, dom, cod, f1, fsharp)

def associator(H, G, F):
    HG = cprod(H, G)
    dom = cprod(HG, F); cod = cprod(H, cprod(G, F))
    def f1(shp):
        hg, kvals = shp
        h, gvals = hg
        Hpos = H.pos(h)
        HGpos = HG.pos(hg)
        mvals = []
        for u in Hpos:
            gu = gvals[Hpos.index(u)]
            Gpos = G.pos(gu)
            innervals = []
            for v in Gpos:
                innervals.append(kvals[HGpos.index((u, v))])
            mvals.append((gu, tuple(innervals)))
        return (h, tuple(mvals))
    def fsharp(shp, r):
        u, vp = r
        v, p = vp
        return ((u, v), p)
    return Mor('assoc', dom, cod, f1, fsharp)

# ---------------------------------------------------------------------------
# Morphism equality checker
# ---------------------------------------------------------------------------
def check_mor_eq(label, phi, psi, shapes):
    """Return True if phi==psi on given shapes (fwd + bwd on all target pos)."""
    for shp in shapes:
        a = phi.f1(shp); b = psi.f1(shp)
        if a != b:
            FAILURES.append((label, 'FWD shape=%r : %r != %r' % (shp, a, b)))
            return False
        for r in phi.cod.pos(a):
            x = phi.fsharp(shp, r); y = psi.fsharp(shp, r)
            if x != y:
                FAILURES.append((label,
                    'BWD shape=%r pos=%r : %r != %r' % (shp, r, x, y)))
                return False
    return True

# ---------------------------------------------------------------------------
# Free monad on X: container m_X, monoid morphisms e_m, mu_m, insertion alpha
# ---------------------------------------------------------------------------
def build_free(X, name='m', enum_nodes=1):
    cont = Cont(name,
                lambda t: leaves(t),
                lambda: gen_trees_nodes(X, enum_nodes))
    # e_m : I => m_X
    def e1(star):
        return LF
    def esharp(star, z):    # z leaf of LF -> pos_I(*) = '*'
        return '*'
    e_m = Mor('e_%s' % name, I, cont, e1, esharp)
    # mu_m : m_X < m_X => m_X
    dom = cprod(cont, cont)
    def mu1(shp):
        t, uvals = shp
        u = dict(zip(leaves(t), uvals))
        return graft(t, u)
    def musharp(shp, z):
        t, uvals = shp
        u = dict(zip(leaves(t), uvals))
        return split(t, u, z)
    mu_m = Mor('mu_%s' % name, dom, cont, mu1, musharp)
    # alpha : X => m_X
    def a1(s):
        return nd(s, {p: LF for p in X['pos'](s)})
    def asharp(s, leaf):    # leaf = (p,)
        return leaf[0]
    Xc = Cont('X', lambda s: X['pos'](s), lambda: list(X['shapes']))
    alpha = Mor('alpha', Xc, cont, a1, asharp)
    return cont, e_m, mu_m, alpha, Xc

# ---------------------------------------------------------------------------
# Induced morphism ghat : m_X => M  for monoid M and g:X=>M
#   M is a dict: cont, eps, muM1(a,bdict)->T, muMsharp(a,bdict,r)->(q,rho),
#                eM_mor, muM_mor, finite(bool)
# ---------------------------------------------------------------------------
def build_ghat(mcont, X, M, g1, gsharp):
    eps = M['eps']
    Mc = M['cont']
    def ghat1(t):
        if t == LF:
            return eps
        s = t[1]; kap = kappa_of(t)
        a = g1(s)
        b = {q: ghat1(kap[gsharp(s, q)]) for q in Mc.pos(a)}
        return M['muM1'](a, b)
    def ghatsharp(t, r):
        if t == LF:
            return ()
        s = t[1]; kap = kappa_of(t)
        a = g1(s)
        b0 = {q: ghat1(kap[gsharp(s, q)]) for q in Mc.pos(a)}
        q, rho = M['muMsharp'](a, b0, r)
        p = gsharp(s, q)
        return (p,) + ghatsharp(kap[p], rho)
    ghat = Mor('ghat', mcont, Mc, ghat1, ghatsharp)
    return ghat, ghat1

# ---------------------------------------------------------------------------
# Monoid-law checker for a monoid (C, e, mu)  over shapes-sample of C
# ---------------------------------------------------------------------------
def check_monoid_laws(label, C, e_mor, mu_mor):
    ok = True
    # left_unit: (e < id_C); mu = lambda_C     over I<C
    lhs = comp_mor(tensor_mor(e_mor, id_mor(C)), mu_mor)
    rhs = left_unitor(C)
    ok &= check_mor_eq(label + ':left_unit', lhs, rhs, lhs.dom.enum_shapes())
    # right_unit: (id_C < e); mu = rho_C       over C<I
    lhs = comp_mor(tensor_mor(id_mor(C), e_mor), mu_mor)
    rhs = right_unitor(C)
    ok &= check_mor_eq(label + ':right_unit', lhs, rhs, lhs.dom.enum_shapes())
    # assoc: (mu < id_C); mu = a; (id_C < mu); mu   over (C<C)<C
    lhs = comp_mor(tensor_mor(mu_mor, id_mor(C)), mu_mor)
    rhs = comp_mor(comp_mor(associator(C, C, C),
                            tensor_mor(id_mor(C), mu_mor)), mu_mor)
    ok &= check_mor_eq(label + ':assoc', lhs, rhs, lhs.dom.enum_shapes())
    return ok

# ---------------------------------------------------------------------------
# Build the three test monoids
# ---------------------------------------------------------------------------
def make_writer():
    Wc = Cont('W', lambda n: ['*'], lambda: [0, 1, 2])
    eps = 0
    def muM1(a, b):
        return (a + b['*']) % 3
    def muMsharp(a, b, r):        # r = '*'
        return ('*', '*')
    # eM : I => W
    eM = Mor('eW', I, Wc, lambda s: 0, lambda s, q: '*')
    # muM : W<W => W
    dom = cprod(Wc, Wc)
    def mu1(shp):
        a, bvals = shp
        b = dict(zip(Wc.pos(a), bvals))
        return muM1(a, b)
    def musharp(shp, r):
        a, bvals = shp
        b = dict(zip(Wc.pos(a), bvals))
        return muMsharp(a, b, r)
    muM = Mor('muW', dom, Wc, mu1, musharp)
    return {'name': 'Writer(Z/3)', 'cont': Wc, 'eps': eps, 'muM1': muM1,
            'muMsharp': muMsharp, 'eM_mor': eM, 'muM_mor': muM, 'finite': True}

def make_reader():
    E = [0, 1]
    Rc = Cont('R', lambda s: list(E), lambda: ['*'])
    eps = '*'
    def muM1(a, b):
        return '*'
    def muMsharp(a, b, r):        # r in E ; diagonal
        return (r, r)
    eM = Mor('eR', I, Rc, lambda s: '*', lambda s, q: '*')
    dom = cprod(Rc, Rc)
    def mu1(shp):
        a, bvals = shp
        b = dict(zip(Rc.pos(a), bvals))
        return muM1(a, b)
    def musharp(shp, r):
        a, bvals = shp
        b = dict(zip(Rc.pos(a), bvals))
        return muMsharp(a, b, r)
    muM = Mor('muR', dom, Rc, mu1, musharp)
    return {'name': 'Reader(E={0,1})', 'cont': Rc, 'eps': eps, 'muM1': muM1,
            'muMsharp': muMsharp, 'eM_mor': eM, 'muM_mor': muM, 'finite': True}

def make_free_target(Y):
    Fc = Cont('mY', lambda t: leaves(t), lambda: gen_trees_nodes(Y, 1))
    eps = LF
    def muM1(a, b):              # b : dict leaves(a)->tree
        return graft(a, b)
    def muMsharp(a, b, r):
        return split(a, b, r)
    eM = Mor('emY', I, Fc, lambda s: LF, lambda s, z: '*')
    dom = cprod(Fc, Fc)
    def mu1(shp):
        a, bvals = shp
        b = dict(zip(Fc.pos(a), bvals))
        return graft(a, b)
    def musharp(shp, r):
        a, bvals = shp
        b = dict(zip(Fc.pos(a), bvals))
        return split(a, b, r)
    muM = Mor('mumY', dom, Fc, mu1, musharp)
    return {'name': 'Free(m_Y binary)', 'cont': Fc, 'eps': eps, 'muM1': muM1,
            'muMsharp': muMsharp, 'eM_mor': eM, 'muM_mor': muM, 'finite': False}

# ---------------------------------------------------------------------------
# Checks A, B, C, D for a given (M, g, X)
# ---------------------------------------------------------------------------
def run_checks(Mlabel, M, X, g1, gsharp):
    global PAIRS_CHECKED
    results = {}
    Mc = M['cont']
    mcont, e_m, mu_m, alpha, Xc = build_free(X, name='m', enum_nodes=1)
    ghat, ghat1 = build_ghat(mcont, X, M, g1, gsharp)
    # g as a morphism X => M
    g_mor = Mor('g', Xc, Mc, g1, gsharp)

    # (A) Triangle: (alpha ; ghat) == g
    comp = comp_mor(alpha, ghat)
    okA = True
    for s in X['shapes']:
        lhs1 = comp.f1(s); rhs1 = g1(s)
        if lhs1 != rhs1:
            okA = False
            FAILURES.append((Mlabel + ':A',
                'FWD s=%r : ghat1(alpha s)=%r != g1(s)=%r' % (s, lhs1, rhs1)))
            break
        for q in Mc.pos(rhs1):
            lb = comp.fsharp(s, q); rb = gsharp(s, q)
            if lb != rb:
                okA = False
                FAILURES.append((Mlabel + ':A',
                    'BWD s=%r q=%r : (alpha;ghat)sharp=%r != gsharp=%r'
                    % (s, q, lb, rb)))
                break
        if not okA:
            break
    results['A'] = okA

    # (B) Unit law: (e_m ; ghat) == eM
    comp = comp_mor(e_m, ghat)
    okB = check_mor_eq(Mlabel + ':B', comp, M['eM_mor'], ['*'])
    results['B'] = okB

    # (C) Mult law: (mu_m ; ghat) == (ghat<ghat); muM  over (m_X<m_X)
    morphism1 = comp_mor(mu_m, ghat)
    morphism2 = comp_mor(tensor_mor(ghat, ghat), M['muM_mor'])
    dom = cprod(mcont, mcont)
    okC = True
    ts = gen_trees_nodes(X, 3)                 # t : up to 3 internal nodes
    depth1 = gen_trees_nodes(X, 1)             # u values : depth<=1 trees
    for t in ts:
        lvs = leaves(t)
        for combo in product(depth1, repeat=len(lvs)):
            shp = (t, combo)
            PAIRS_CHECKED += 1
            a = morphism1.f1(shp); b = morphism2.f1(shp)
            if a != b:
                okC = False
                FAILURES.append((Mlabel + ':C',
                    'FWD shp=%r : (mu;ghat)1=%r != ((ghat<ghat);muM)1=%r'
                    % (shp, a, b)))
                break
            for r in Mc.pos(a):
                x = morphism1.fsharp(shp, r); y = morphism2.fsharp(shp, r)
                if x != y:
                    okC = False
                    FAILURES.append((Mlabel + ':C',
                        'BWD shp=%r pos=%r : (mu;ghat)sharp=%r != ((ghat<ghat);muM)sharp=%r'
                        % (shp, r, x, y)))
                    break
            if not okC:
                break
        if not okC:
            break
    results['C'] = okC

    # (D) Uniqueness (finite M only)
    if M['finite']:
        trees = gen_trees_depth(X, 2)
        T = list(Mc.enum_shapes())
        idx = {t: i for i, t in enumerate(trees)}
        node_trees = [t for t in trees if t != LF]
        solutions = []
        for assign in product(T, repeat=len(trees)):
            f = dict(zip(trees, assign))
            if f[LF] != M['eps']:
                continue
            good = True
            for t in node_trees:
                s = t[1]; kap = kappa_of(t)
                a = g1(s)
                bd = {q: f[kap[gsharp(s, q)]] for q in Mc.pos(a)}
                if f[t] != M['muM1'](a, bd):
                    good = False
                    break
            if good:
                solutions.append(f)
        # expected: exactly one, equal to ghat1 restricted
        ghat_restr = {t: ghat1(t) for t in trees}
        okD = (len(solutions) == 1 and solutions[0] == ghat_restr)
        if not okD:
            FAILURES.append((Mlabel + ':D',
                '#solutions=%d ; matches ghat1=%s'
                % (len(solutions),
                   (len(solutions) == 1 and solutions[0] == ghat_restr))))
        results['D'] = okD
    else:
        results['D'] = None    # N/A (infinite M)
    return results

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("Universal property of the free monad on a container -- verification")
    print("=" * 72)

    X = {'shapes': ['x'], 'pos': lambda s: [0, 1]}   # binary source

    # ---- sanity: monoid laws for m_X ------------------------------------
    print("\n[Sanity] Monoid laws for the free monad m_X (a few small X):")
    for Xtest, xname in [({'shapes': ['x'], 'pos': lambda s: [0, 1]}, 'binary'),
                         ({'shapes': ['c'], 'pos': lambda s: [0]}, 'list')]:
        mcont, e_m, mu_m, alpha, Xc = build_free(Xtest, name='m', enum_nodes=1)
        ok = check_monoid_laws('m_X(%s)' % xname, mcont, e_m, mu_m)
        print("   m_X (%-6s): %s" % (xname, 'PASS' if ok else 'FAIL'))

    # ---- test monoids ----------------------------------------------------
    Y = {'shapes': ['y'], 'pos': lambda s: [0, 1]}
    writer = make_writer()
    reader = make_reader()
    freeM = make_free_target(Y)

    print("\n[Sanity] Monoid laws for the three test monoids M:")
    for M in (writer, reader, freeM):
        ok = check_monoid_laws(M['name'], M['cont'], M['eM_mor'], M['muM_mor'])
        print("   %-18s: %s" % (M['name'], 'PASS' if ok else 'FAIL'))

    # g's (explicit) -------------------------------------------------------
    # Writer: g1(x)=1 ; gsharp trivial (Q singleton) -> 0
    gW1 = lambda s: 1
    gWsharp = lambda s, q: 0
    # Reader: g1(x)=* ; gsharp nontrivial swap on E
    gR1 = lambda s: '*'
    gRsharp = lambda s, q: {0: 1, 1: 0}[q]
    # Free: g1(x)= nd(y,{0:lf,1:lf}) ; gsharp swap on its two leaves
    gF_tree = nd('y', {0: LF, 1: LF})
    gF1 = lambda s: gF_tree
    gFsharp = lambda s, q: {(0,): 1, (1,): 0}[q]

    print("\n[Main] Universal-property checks per (M, g):")
    all_results = []
    configs = [('Writer(Z/3)', writer, gW1, gWsharp),
               ('Reader(E)',    reader, gR1, gRsharp),
               ('Free(m_Y)',    freeM,  gF1, gFsharp)]
    for label, M, g1, gsharp in configs:
        res = run_checks(label, M, X, g1, gsharp)
        all_results.append((label, res))

    # ---- summary table ---------------------------------------------------
    def cell(v):
        if v is None:
            return ' n/a '
        return 'PASS' if v else 'FAIL'
    print("\n" + "=" * 72)
    print("SUMMARY TABLE")
    print("=" * 72)
    print("%-14s | %-6s | %-6s | %-6s | %-6s" %
          ('(M,g)', 'A tri', 'B unit', 'C mult', 'D uniq'))
    print("-" * 72)
    any_fail = False
    for label, res in all_results:
        row = [cell(res['A']), cell(res['B']), cell(res['C']), cell(res['D'])]
        if any(c == 'FAIL' for c in row):
            any_fail = True
        print("%-14s | %-6s | %-6s | %-6s | %-6s" %
              (label, row[0], row[1], row[2], row[3]))
    print("-" * 72)
    print("Total (t,u) pairs checked in (C): %d" % PAIRS_CHECKED)

    if FAILURES:
        any_fail = True
        print("\nFAILURES (verbatim):")
        for lab, msg in FAILURES:
            print("  [%s] %s" % (lab, msg))
    else:
        print("\nNo failures recorded.")

    print("\nOVERALL:", "FAIL" if any_fail else "PASS")
    sys.exit(1 if any_fail else 0)

if __name__ == '__main__':
    main()
