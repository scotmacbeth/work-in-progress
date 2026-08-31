"""
Verify/refute MacBeth's (co)monoid classification table for monoidal
structures on Cont (finite containers).

Container: {'S': [shape labels], 'P': {shape: [position labels]}}
Morphism c->d: {'f': {s: shape_in_d}, 'b': {s: {pos in d[f(s)]: pos in c[s]}}}
  forward on shapes, BACKWARD on positions.
"""
import itertools

# ---------- core morphism machinery ----------

def idm(c):
    return {'f': {s: s for s in c['S']},
            'b': {s: {p: p for p in c['P'][s]} for s in c['S']}}

def compose(g, f, c, d, e):
    """f:c->d, g:d->e  =>  c->e."""
    F = {}
    B = {}
    for s in c['S']:
        ds = f['f'][s]
        es = g['f'][ds]
        F[s] = es
        b = {}
        for pe in e['P'][es]:
            pd = g['b'][ds][pe]      # in d[ds]
            pc = f['b'][s][pd]       # in c[s]
            b[pe] = pc
        B[s] = b
    return {'f': F, 'b': B}

def eq(m1, m2):
    return m1['f'] == m2['f'] and m1['b'] == m2['b']

def is_morphism(m, c, d):
    """sanity check well-formedness."""
    for s in c['S']:
        if s not in m['f']:
            return False
        ds = m['f'][s]
        if ds not in d['S']:
            return False
        b = m['b'][s]
        if set(b.keys()) != set(d['P'][ds]):
            return False
        for v in b.values():
            if v not in c['P'][s]:
                return False
    return True

def enum_morphisms(c, d):
    """all morphisms c->d."""
    Sc = c['S']
    out = []
    # shape choices: each s in Sc -> some shape in d['S']
    shape_opts = list(itertools.product(d['S'], repeat=len(Sc)))
    for shs in shape_opts:
        fmap = dict(zip(Sc, shs))
        # backward: for each s, function d[f(s)] -> c[s]
        per_s = []
        for s in Sc:
            ds = fmap[s]
            dom = d['P'][ds]
            cod = c['P'][s]
            if len(dom) == 0:
                per_s.append([{}])
            elif len(cod) == 0:
                per_s.append([])   # no function possible
            else:
                funcs = []
                for vals in itertools.product(cod, repeat=len(dom)):
                    funcs.append(dict(zip(dom, vals)))
                per_s.append(funcs)
        if any(len(x) == 0 for x in per_s):
            continue
        for combo in itertools.product(*per_s):
            bmap = {s: combo[i] for i, s in enumerate(Sc)}
            out.append({'f': fmap, 'b': bmap})
    return out

# ---------- monoidal structure base ----------
# each structure provides:
#   tensor_obj(a,b), tensor_mor(f,g,a,b,a2,b2), unit,
#   assoc(a,b,c): (a*b)*c -> a*(b*c),
#   lunit(c): I*c -> c,  runit(c): c*I -> c,
#   (for comonoid counit) counits enumerated as morphisms c->I
#   (for monoid unit) units enumerated as morphisms I->c

class Prod:  # categorical product x
    name = 'x (product)'
    unit = {'S': ['*'], 'P': {'*': []}}   # terminal

    @staticmethod
    def tensor_obj(a, b):
        S = [(s, t) for s in a['S'] for t in b['S']]
        P = {}
        for s in a['S']:
            for t in b['S']:
                P[(s, t)] = [('l', p) for p in a['P'][s]] + [('r', q) for q in b['P'][t]]
        return {'S': S, 'P': P}

    @staticmethod
    def tensor_mor(f, g, a, b, a2, b2):
        F = {}
        B = {}
        for s in a['S']:
            for t in b['S']:
                fs, gt = f['f'][s], g['f'][t]
                F[(s, t)] = (fs, gt)
                bb = {}
                for p in a2['P'][fs]:
                    bb[('l', p)] = ('l', f['b'][s][p])
                for q in b2['P'][gt]:
                    bb[('r', q)] = ('r', g['b'][t][q])
                B[(s, t)] = bb
        return {'f': F, 'b': B}

    @staticmethod
    def assoc(a, b, c):  # (a x b) x c -> a x (b x c)
        AB = Prod.tensor_obj(a, b)
        ABc = Prod.tensor_obj(AB, c)
        BC = Prod.tensor_obj(b, c)
        aBC = Prod.tensor_obj(a, BC)
        F = {}
        B = {}
        for s in a['S']:
            for t in b['S']:
                for u in c['S']:
                    src = ((s, t), u)
                    tgt = (s, (t, u))
                    F[src] = tgt
                    bb = {}
                    # target positions of aBC at (s,(t,u)):
                    #   ('l',p) p in a[s]; ('r',('l',q)) q in b[t]; ('r',('r',w)) w in c[u]
                    for p in a['P'][s]:
                        bb[('l', p)] = ('l', ('l', p))
                    for q in b['P'][t]:
                        bb[('r', ('l', q))] = ('l', ('r', q))
                    for w in c['P'][u]:
                        bb[('r', ('r', w))] = ('r', w)
                    B[src] = bb
        return {'f': F, 'b': B}, ABc, aBC

    @staticmethod
    def lunit(c):  # I x c -> c
        Ic = Prod.tensor_obj(Prod.unit, c)
        F = {}
        B = {}
        for s in c['S']:
            F[('*', s)] = s
            bb = {}
            for p in c['P'][s]:
                bb[p] = ('r', p)   # positions of I x c at (*,s) are ('r',p)
            B[('*', s)] = bb
        return {'f': F, 'b': B}, Ic

    @staticmethod
    def runit(c):  # c x I -> c
        cI = Prod.tensor_obj(c, Prod.unit)
        F = {}
        B = {}
        for s in c['S']:
            F[(s, '*')] = s
            bb = {}
            for p in c['P'][s]:
                bb[p] = ('l', p)
            B[(s, '*')] = bb
        return {'f': F, 'b': B}, cI


class Coprod:  # categorical coproduct +
    name = '+ (coproduct)'
    unit = {'S': [], 'P': {}}   # initial

    @staticmethod
    def tensor_obj(a, b):
        S = [('L', s) for s in a['S']] + [('R', t) for t in b['S']]
        P = {}
        for s in a['S']:
            P[('L', s)] = list(a['P'][s])
        for t in b['S']:
            P[('R', t)] = list(b['P'][t])
        return {'S': S, 'P': P}

    @staticmethod
    def tensor_mor(f, g, a, b, a2, b2):
        F = {}
        B = {}
        for s in a['S']:
            F[('L', s)] = ('L', f['f'][s])
            B[('L', s)] = dict(f['b'][s])
        for t in b['S']:
            F[('R', t)] = ('R', g['f'][t])
            B[('R', t)] = dict(g['b'][t])
        return {'f': F, 'b': B}

    @staticmethod
    def assoc(a, b, c):  # (a+b)+c -> a+(b+c)
        AB = Coprod.tensor_obj(a, b)
        ABc = Coprod.tensor_obj(AB, c)
        BC = Coprod.tensor_obj(b, c)
        aBC = Coprod.tensor_obj(a, BC)
        F = {}
        B = {}
        # source shapes: ('L',('L',s)) ('L',('R',t)) ('R',u)
        for s in a['S']:
            src = ('L', ('L', s)); tgt = ('L', s)
            F[src] = tgt
            B[src] = {p: p for p in a['P'][s]}
        for t in b['S']:
            src = ('L', ('R', t)); tgt = ('R', ('L', t))
            F[src] = tgt
            B[src] = {p: p for p in b['P'][t]}
        for u in c['S']:
            src = ('R', u); tgt = ('R', ('R', u))
            F[src] = tgt
            B[src] = {p: p for p in c['P'][u]}
        return {'f': F, 'b': B}, ABc, aBC

    @staticmethod
    def lunit(c):  # 0 + c -> c
        Ic = Coprod.tensor_obj(Coprod.unit, c)
        F = {}; B = {}
        for s in c['S']:
            F[('R', s)] = s
            B[('R', s)] = {p: p for p in c['P'][s]}
        return {'f': F, 'b': B}, Ic

    @staticmethod
    def runit(c):  # c + 0 -> c
        cI = Coprod.tensor_obj(c, Coprod.unit)
        F = {}; B = {}
        for s in c['S']:
            F[('L', s)] = s
            B[('L', s)] = {p: p for p in c['P'][s]}
        return {'f': F, 'b': B}, cI


class Dir:  # Dirichlet (x) tensor
    name = '(x) Dirichlet'
    unit = {'S': ['*'], 'P': {'*': [0]}}   # y

    @staticmethod
    def tensor_obj(a, b):
        S = [(s, t) for s in a['S'] for t in b['S']]
        P = {}
        for s in a['S']:
            for t in b['S']:
                P[(s, t)] = [(p, q) for p in a['P'][s] for q in b['P'][t]]
        return {'S': S, 'P': P}

    @staticmethod
    def tensor_mor(f, g, a, b, a2, b2):
        F = {}; B = {}
        for s in a['S']:
            for t in b['S']:
                fs, gt = f['f'][s], g['f'][t]
                F[(s, t)] = (fs, gt)
                bb = {}
                for p in a2['P'][fs]:
                    for q in b2['P'][gt]:
                        bb[(p, q)] = (f['b'][s][p], g['b'][t][q])
                B[(s, t)] = bb
        return {'f': F, 'b': B}

    @staticmethod
    def assoc(a, b, c):
        AB = Dir.tensor_obj(a, b)
        ABc = Dir.tensor_obj(AB, c)
        BC = Dir.tensor_obj(b, c)
        aBC = Dir.tensor_obj(a, BC)
        F = {}; B = {}
        for s in a['S']:
            for t in b['S']:
                for u in c['S']:
                    src = ((s, t), u); tgt = (s, (t, u))
                    F[src] = tgt
                    bb = {}
                    # target pos (p,(q,w)) -> source pos ((p,q),w)
                    for p in a['P'][s]:
                        for q in b['P'][t]:
                            for w in c['P'][u]:
                                bb[(p, (q, w))] = ((p, q), w)
                    B[src] = bb
        return {'f': F, 'b': B}, ABc, aBC

    @staticmethod
    def lunit(c):  # y (x) c -> c
        Ic = Dir.tensor_obj(Dir.unit, c)
        F = {}; B = {}
        for s in c['S']:
            F[('*', s)] = s
            B[('*', s)] = {p: (0, p) for p in c['P'][s]}
        return {'f': F, 'b': B}, Ic

    @staticmethod
    def runit(c):  # c (x) y -> c
        cI = Dir.tensor_obj(c, Dir.unit)
        F = {}; B = {}
        for s in c['S']:
            F[(s, '*')] = s
            B[(s, '*')] = {p: (p, 0) for p in c['P'][s]}
        return {'f': F, 'b': B}, cI


# ---------- comonoid / monoid checkers ----------

def comonoid_laws(M, c, delta, eps):
    """delta: c->c*c, eps: c->I. Return (counitL, counitR, coassoc) bools."""
    cc = M.tensor_obj(c, c)
    I = M.unit
    # left counit: lunit_c o (eps * id_c) o delta = id_c
    epsid = M.tensor_mor(eps, idm(c), c, c, I, c)   # c*c -> I*c
    Ic_obj = M.tensor_obj(I, c)
    lam, Ic2 = M.lunit(c)
    # compose: c --delta--> c*c --epsid--> I*c --lam--> c
    t1 = compose(epsid, delta, c, cc, Ic_obj)
    left = compose(lam, t1, c, Ic_obj, c)
    cL = eq(left, idm(c))
    # right counit
    ideps = M.tensor_mor(idm(c), eps, c, c, c, I)   # c*c -> c*I
    cI_obj = M.tensor_obj(c, I)
    rho, cI2 = M.runit(c)
    t2 = compose(ideps, delta, c, cc, cI_obj)
    right = compose(rho, t2, c, cI_obj, c)
    cR = eq(right, idm(c))
    # coassoc: alpha o (delta * id) o delta = (id * delta) o delta
    deltaid = M.tensor_mor(delta, idm(c), c, c, cc, c)   # c*c -> (c*c)*c
    ccc_L = M.tensor_obj(cc, c)
    iddelta = M.tensor_mor(idm(c), delta, c, c, c, cc)   # c*c -> c*(c*c)
    ccc_R = M.tensor_obj(c, cc)
    alpha, ABc, aBC = M.assoc(c, c, c)  # (c*c)*c -> c*(c*c)
    lhs0 = compose(deltaid, delta, c, cc, ccc_L)         # c -> (c*c)*c
    lhs = compose(alpha, lhs0, c, ccc_L, ccc_R)          # c -> c*(c*c)
    rhs = compose(iddelta, delta, c, cc, ccc_R)          # c -> c*(c*c)
    coa = eq(lhs, rhs)
    return cL, cR, coa

def is_comonoid(M, c, delta, eps):
    a, b, d = comonoid_laws(M, c, delta, eps)
    return a and b and d

def count_comonoids(M, c):
    cc = M.tensor_obj(c, c)
    I = M.unit
    deltas = enum_morphisms(c, cc)
    epss = enum_morphisms(c, I)
    res = []
    for delta in deltas:
        for eps in epss:
            if is_comonoid(M, c, delta, eps):
                res.append((delta, eps))
    return res, len(deltas), len(epss)


def monoid_laws(M, c, mu, eta):
    """mu: c*c->c, eta: I->c."""
    cc = M.tensor_obj(c, c)
    I = M.unit
    # assoc: mu o (mu * id) = mu o (id * mu) o alpha   on (c*c)*c -> c
    muid = M.tensor_mor(mu, idm(c), cc, c, c, c)   # (c*c)*c -> c*c
    ccc_L = M.tensor_obj(cc, c)
    idmu = M.tensor_mor(idm(c), mu, c, cc, c, c)   # c*(c*c) -> c*c
    ccc_R = M.tensor_obj(c, cc)
    alpha, ABc, aBC = M.assoc(c, c, c)             # (c*c)*c -> c*(c*c)
    lhs = compose(mu, muid, ccc_L, cc, c)          # (c*c)*c -> c
    r0 = compose(idmu, alpha, ccc_L, ccc_R, cc)    # (c*c)*c -> c*c
    rhs = compose(mu, r0, ccc_L, cc, c)
    assoc = eq(lhs, rhs)
    # left unit: mu o (eta * id) = lunit_c   on I*c -> c
    etaid = M.tensor_mor(eta, idm(c), I, c, c, c)  # I*c -> c*c
    Ic = M.tensor_obj(I, c)
    lam, _ = M.lunit(c)
    lu = compose(mu, etaid, Ic, cc, c)
    ulL = eq(lu, lam)
    # right unit
    ideta = M.tensor_mor(idm(c), eta, c, I, c, c)  # c*I -> c*c
    cI = M.tensor_obj(c, I)
    rho, _ = M.runit(c)
    ru = compose(mu, ideta, cI, cc, c)
    ulR = eq(ru, rho)
    return assoc, ulL, ulR

def is_monoid(M, c, mu, eta):
    a, b, d = monoid_laws(M, c, mu, eta)
    return a and b and d

def count_monoids(M, c):
    cc = M.tensor_obj(c, c)
    I = M.unit
    mus = enum_morphisms(cc, c)
    etas = enum_morphisms(I, c)
    res = []
    for mu in mus:
        for eta in etas:
            if is_monoid(M, c, mu, eta):
                res.append((mu, eta))
    return res, len(mus), len(etas)


# ---------- sample containers ----------
def cont(P_cards, labels=None):
    """Build container from list of position cardinalities."""
    S = list(range(len(P_cards)))
    P = {i: list(range(P_cards[i])) for i in S}
    return {'S': S, 'P': P}

samples = {
    'y (1sh,1pos)': cont([1]),
    '1sh,0pos(=1)': cont([0]),
    '1sh,2pos': cont([2]),
    '1sh,3pos': cont([3]),
    '2sh,[1,1]': cont([1, 1]),
    '2sh,[2,1]': cont([2, 1]),
    '2sh,[0,1]': cont([0, 1]),
    '3sh,[1,1,1]': cont([1, 1, 1]),
}

if __name__ == '__main__':
    print("sanity: sample morphism counts")
    for M in (Prod, Coprod, Dir):
        c = samples['1sh,2pos']
        cc = M.tensor_obj(c, c)
        print(f"  {M.name}: c(x)c shapes={len(cc['S'])} pos={[len(cc['P'][s]) for s in cc['S']]}")
