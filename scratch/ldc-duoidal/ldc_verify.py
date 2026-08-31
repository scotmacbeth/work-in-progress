"""
Verifier for the (⋉, ⋊) duoidal / LDC structure on Poly (containers).

Polynomial p: shape set S_p (ordered list), directions p[s] (ordered list of tokens).
Morphism phi: p->q : fwd (dict s->q-shape), bwd (dict s-> function q[fwd s]->p[s]).

Tensors build direction ELEMENTS as concrete tuples so exponentials are function-tuples.
An exponent p[s]^{X} element = tuple over sorted(X) of values in p[s].
Product elements = ('L', f, g) style tagged tuples. We keep them fully concrete so that
two parallel morphisms can be compared by evaluating bwd on every direction element.
"""
from itertools import product

# ---------- containers ----------
def C(S, d):
    # S: list of shapes; d: dict shape-> list of direction tokens
    return {'S': list(S), 'd': {s: list(d[s]) for s in S}}

def Y():  # unit y
    return C(['*'], {'*': ['·']})

def order(X):  # canonical order of a shape set (list)
    return list(X)

# function p[s]^X represented as tuple aligned to order(X)
# product represented as a tuple of the factor-elements

# ---------- tensor on OBJECTS ----------
def ltimes(p, q):
    Sp, Sq = p['S'], q['S']
    S = [(s, t) for s in Sp for t in Sq]
    d = {}
    for s in Sp:
        for t in Sq:
            # p[s]^{Sq}  ×  q[t]^{Sp}
            fs = list(product(p['d'][s], repeat=len(Sq)))   # tuples over order(Sq)
            gs = list(product(q['d'][t], repeat=len(Sp)))    # tuples over order(Sp)
            d[(s, t)] = [(f, g) for f in fs for g in gs]
    return {'S': S, 'd': d, 'Sp': Sp, 'Sq': Sq}

def rtimes(p, q):
    Sp, Sq = p['S'], q['S']
    S = [(s, t) for s in Sp for t in Sq]
    d = {}
    for s in Sp:
        for t in Sq:
            # p[s]^{Sq}  ×  q[t]
            fs = list(product(p['d'][s], repeat=len(Sq)))
            ys = list(q['d'][t])
            d[(s, t)] = [(f, y) for f in fs for y in ys]
    return {'S': S, 'd': d, 'Sp': Sp, 'Sq': Sq}

# helpers to read/write exponent tuples
def idx(X, x):  # position of x in ordered set X
    return list(X).index(x)

def ev(f, X, x):  # evaluate function-tuple f: X-> at point x
    return f[idx(X, x)]

def mkfun(X, vals):  # build tuple from dict x->value
    return tuple(vals[x] for x in X)

# ---------- morphisms ----------
class Mor:
    def __init__(self, src, tgt, fwd, bwd):
        self.src = src; self.tgt = tgt
        self.fwd = fwd            # dict s -> tgt shape
        self.bwd = bwd            # dict s -> (callable: tgt-dir-elt -> src-dir-elt)
    def apply_bwd(self, s, e):
        return self.bwd[s](e)

def idmor(p):
    return Mor(p, p, {s: s for s in p['S']}, {s: (lambda e: e) for s in p['S']})

def compose(psi, phi):  # psi∘phi : phi.src -> psi.tgt
    assert phi.tgt is psi.src or phi.tgt == psi.src
    fwd = {s: psi.fwd[phi.fwd[s]] for s in phi.src['S']}
    def make_bwd(s):
        t = phi.fwd[s]
        return lambda e: phi.bwd[s](psi.bwd[t](e))
    bwd = {s: make_bwd(s) for s in phi.src['S']}
    return Mor(phi.src, psi.tgt, fwd, bwd)

def eq_mor(phi, psi):
    # parallel morphisms equal?  same fwd, same bwd on every target-dir element
    if phi.src['S'] != psi.src['S']:
        return False
    for s in phi.src['S']:
        if phi.fwd[s] != psi.fwd[s]:
            print("   fwd differ at", s, phi.fwd[s], psi.fwd[s]); return False
        tsh = phi.fwd[s]
        for e in phi.tgt['d'][tsh]:
            if phi.bwd[s](e) != psi.bwd[s](e):
                print("   bwd differ at shape", s, "elt", e, "->", phi.bwd[s](e), "vs", psi.bwd[s](e))
                return False
    return True

# ---------- functorial action of tensors on morphisms ----------
def ltimes_mor(phi, psi):  # phi:A->A', psi:B->B'  =>  A⋉B -> A'⋉B'
    A, Ap = phi.src, phi.tgt; B, Bp = psi.src, psi.tgt
    src = ltimes(A, B); tgt = ltimes(Ap, Bp)
    fwd = {(a, b): (phi.fwd[a], psi.fwd[b]) for a in A['S'] for b in B['S']}
    def make_bwd(a, b):
        def bwd(e):  # e = (f', g') in A'[φa]^{S_B'} × B'[ψb]^{S_A'}
            fp, gp = e
            SB, SBp = B['S'], Bp['S']
            SA, SAp = A['S'], Ap['S']
            # f: S_B -> A[a]:  f(x)=φ.bwd_a( f'(ψ.fwd x) )
            f = tuple(phi.bwd[a](ev(fp, SBp, psi.fwd[x])) for x in SB)
            # g: S_A -> B[b]:  g(x)=ψ.bwd_b( g'(φ.fwd x) )
            g = tuple(psi.bwd[b](ev(gp, SAp, phi.fwd[x])) for x in SA)
            return (f, g)
        return bwd
    bwd = {(a, b): make_bwd(a, b) for a in A['S'] for b in B['S']}
    return Mor(src, tgt, fwd, bwd)

def rtimes_mor(phi, psi):  # phi:A->A', psi:B->B'  =>  A⋊B -> A'⋊B'
    A, Ap = phi.src, phi.tgt; B, Bp = psi.src, psi.tgt
    src = rtimes(A, B); tgt = rtimes(Ap, Bp)
    fwd = {(a, b): (phi.fwd[a], psi.fwd[b]) for a in A['S'] for b in B['S']}
    def make_bwd(a, b):
        def bwd(e):  # e = (f', y') in A'[φa]^{S_B'} × B'[ψb]
            fp, yp = e
            SB, SBp = B['S'], Bp['S']
            f = tuple(phi.bwd[a](ev(fp, SBp, psi.fwd[x])) for x in SB)
            y = psi.bwd[b](yp)
            return (f, y)
        return bwd
    bwd = {(a, b): make_bwd(a, b) for a in A['S'] for b in B['S']}
    return Mor(src, tgt, fwd, bwd)

# ---------- random small containers & morphisms (deterministic, no RNG) ----------
def sample_containers():
    y = Y()
    p = C(['p0', 'p1'], {'p0': ['a0', 'a1'], 'p1': ['b0']})
    q = C(['q0'], {'q0': ['c0', 'c1']})
    r = C(['r0', 'r1'], {'r0': ['d0'], 'r1': ['e0', 'e1']})
    return y, p, q, r

def all_mors(src, tgt, cap=64):
    """enumerate morphisms src->tgt (fwd any shape map; bwd any dir map). capped."""
    Ssrc = src['S']; Stgt = tgt['S']
    out = []
    for fchoice in product(Stgt, repeat=len(Ssrc)):
        fwd = {s: fchoice[i] for i, s in enumerate(Ssrc)}
        # for each s, choose a function tgt[fwd s] -> src[s]
        perslot = []
        for s in Ssrc:
            tds = tgt['d'][fwd[s]]; sds = src['d'][s]
            perslot.append(list(product(sds, repeat=len(tds))))  # each = tuple over tds
        for combo in product(*perslot):
            bwd = {}
            for i, s in enumerate(Ssrc):
                tds = tgt['d'][fwd[s]]; tbl = combo[i]
                bwd[s] = (lambda tds, tbl: (lambda e: tbl[tds.index(e)]))(tds, tbl)
            out.append(Mor(src, tgt, fwd, bwd))
            if len(out) >= cap:
                return out
    return out

if __name__ == '__main__':
    y, p, q, r = sample_containers()
    print("sanity: |ltimes(p,q).S| =", len(ltimes(p, q)['S']),
          " dir profile:", sorted(len(v) for v in ltimes(p, q)['d'].values()))
    print("sanity: |rtimes(p,q).S| =", len(rtimes(p, q)['S']),
          " dir profile:", sorted(len(v) for v in rtimes(p, q)['d'].values()))
    # id functoriality
    print("ltimes(id,id)==id ?", eq_mor(ltimes_mor(idmor(p), idmor(q)), idmor(ltimes(p, q))))
    print("rtimes(id,id)==id ?", eq_mor(rtimes_mor(idmor(p), idmor(q)), idmor(rtimes(p, q))))
