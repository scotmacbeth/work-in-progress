"""
Resolve Workers ×-closedness.

Reduced test: Workers ×-closed  iff  R^p in image of [ΔS,-]_⊗,
where R=[ΔS,q]_⊗ and (-)^p is Cont's CCC exponential.

CLAIM (contradicts prior conjecture): YES, with internal hom
   E = ∏_{s_p} q ◁ (y ⊕ c_{S×P_p(s_p)}),  ⟦E⟧Y = ∏_{s_p}⟦q⟧(Y + S×P_p(s_p)).
i.e. R^p ≅ [ΔS,E]_⊗.

We verify:
 (L1) ⟦[ΔS,r]⟧X = (⟦r⟧(S×X))^|S|   (objectwise counts)
 (L2) ⟦q^p⟧X   = ∏_{s_p}⟦q⟧(X+P_p s_p)
 (MAIN) R^p ≅ [ΔS,E]  as containers  (same multiset of fibre sizes)
 (control) also confirm E ≠ q^p (naive) in general.
"""
from containers import *
from itertools import product as iproduct
from collections import Counter

# ---------- extension counting ----------
def ext_count(c, n):
    # |⟦c⟧(X)| for |X|=n  = Σ_shapes n^{|fib|}
    return sum(n**len(c.fib[a]) for a in c.shapes)

def fibre_multiset(c):
    return tuple(sorted(len(c.fib[a]) for a in c.shapes))

def iso(c1, c2):
    return fibre_multiset(c1) == fibre_multiset(c2)

# ---------- constant container c_K = (K, k->∅) ----------
def const(K):
    # K given as list of labels
    return Cont(list(K), {k: [] for k in K})

# y ⊕ c_K :  ⟦⟧X = X + K
def y_plus_const(K):
    return coprod(y(), const(K))

# ---------- Dirichlet hom [p,q]_⊗ ----------
# shapes = Cont(p,q) morphisms; pos at (u,bwd) = Σ_{s_p} P_q(u s_p).
def all_morphisms(p, q):
    mors = []
    for uvals in iproduct(q.shapes, repeat=len(p.shapes)):
        u = dict(zip(p.shapes, uvals))
        # backward: for each s_p, a map P_q(u s_p) -> P_p(s_p)
        choice_spaces = []
        keys = []
        for sp in p.shapes:
            tgtpos = q.fib[u[sp]]
            srcpos = p.fib[sp]
            keys.append(sp)
            # a backward map = assignment tgtpos -> srcpos (if srcpos empty and tgtpos nonempty: none)
            if len(tgtpos) > 0 and len(srcpos) == 0:
                choice_spaces = None
                break
            choice_spaces.append(list(iproduct(srcpos, repeat=len(tgtpos))))
        if choice_spaces is None:
            continue
        for combo in iproduct(*choice_spaces):
            bwd = {}
            for sp, assign in zip(keys, combo):
                bwd[sp] = dict(zip(q.fib[u[sp]], assign))
            mors.append((u, bwd))
    return mors

def dirichlet_hom(p, q):
    mors = all_morphisms(p, q)
    shapes = []
    fib = {}
    for idx, (u, bwd) in enumerate(mors):
        sh = ('m', idx)
        shapes.append(sh)
        pos = []
        for sp in p.shapes:
            for d in q.fib[u[sp]]:
                pos.append((sp, d))
        fib[sh] = pos
    return Cont(shapes, fib)

# ---------- CCC exponential r^p = ∏_{s_p} r ◁ (y⊕c_{P_p(s_p)}) ----------
def prod_list(cs):
    acc = Cont([()], {(): []})   # terminal-ish unit for product? unit of × is y? no.
    # unit for × (product) is the terminal container 1 = (1, *->∅): ⟦⟧X = 1.
    acc = Cont(['*'], {'*': []})
    for c in cs:
        acc = prod(acc, c)
    return acc

def ccc_exp(p, r):
    parts = []
    for sp in p.shapes:
        K = [ (sp,i) for i in range(len(p.fib[sp])) ]  # |K| = |P_p(sp)|
        parts.append(lhd(r, y_plus_const(K)))
    return prod_list(parts)

# ---------- E = ∏_{s_p} q ◁ (y ⊕ c_{S×P_p(s_p)}) ----------
def workers_x_hom(S, p, q):
    parts = []
    for sp in p.shapes:
        K = [ (s, i) for s in S for i in range(len(p.fib[sp])) ]  # |K|=|S|*|P_p(sp)|
        parts.append(lhd(q, y_plus_const(K)))
    return prod_list(parts)

# =========================================================
if __name__ == '__main__':
    S = ['s0', 's1']
    dS = deltaS(S)

    # TINY test objects (keep homs enumerable)
    p = Cont(['a0'], {'a0':['b']})            # 1 shape, 1 position
    q = Cont(['e0'], {'e0':['f']})            # 1 shape, 1 position

    print("=== L1: ⟦[ΔS,r]⟧X == (⟦r⟧(S×X))^|S| ===")
    for r in [p, q, Cont(['z'],{'z':[]}), Cont(['w'],{'w':['1','2','3']})]:
        H = dirichlet_hom(dS, r)
        ok = True
        for n in range(1,4):
            lhs = ext_count(H, n)
            # ⟦r⟧(S×X): |S×X| = |S|*n ; then ^|S|
            rhs = ext_count(r, len(S)*n) ** len(S)
            if lhs != rhs: ok = False
        print(f"  r shapes={r.shapes}: {'OK' if ok else 'FAIL'}  (n=2: {ext_count(H,2)} vs {ext_count(r,2*len(S))**len(S)})")

    print("\n=== L2: ⟦q^p⟧X == ∏_{s_p}⟦q⟧(X+P_p s_p) ===")
    E_ccc = ccc_exp(p, q)
    ok=True
    for n in range(1,4):
        lhs = ext_count(E_ccc, n)
        rhs = 1
        for sp in p.shapes:
            rhs *= ext_count(q, n + len(p.fib[sp]))
        if lhs!=rhs: ok=False
    print(f"  {'OK' if ok else 'FAIL'} (n=2: lhs={ext_count(E_ccc,2)})")

    print("\n=== MAIN: R^p ≅ [ΔS,E]_⊗ ? ===")
    R = dirichlet_hom(dS, q)            # R = [ΔS,q]_⊗
    Rp = ccc_exp(p, R)                  # R^p  (Cont CCC exponential)
    E  = workers_x_hom(S, p, q)         # candidate internal hom
    HE = dirichlet_hom(dS, E)           # [ΔS,E]_⊗
    print(f"  |shapes R^p|={len(Rp.shapes)}  |shapes [ΔS,E]|={len(HE.shapes)}")
    print(f"  fibre-multiset equal (⟹ iso)? {iso(Rp, HE)}")
    # also objectwise counts
    for n in range(1,4):
        print(f"    n={n}: |⟦R^p⟧|={ext_count(Rp,n)}   |⟦[ΔS,E]⟧|={ext_count(HE,n)}   {'==' if ext_count(Rp,n)==ext_count(HE,n) else '!!'}")

    print("\n=== control: naive candidate q^p is NOT the hom (E ≠ q^p in general) ===")
    naive = ccc_exp(p, q)
    print(f"  fibre-multiset E == q^p ? {iso(E, naive)}  (expect False when |S|>1)")

    print("\n=== ALSO: direct Workers hom-set counts  |Work(a×p,q)| == |Work(a,E)| ? ===")
    def count_mor(src,tgt):
        # number of container morphisms src->tgt
        return len(all_morphisms(src,tgt))
    test_as = [Cont(['t'],{'t':['u']}), p, q, Cont(['v0','v1'],{'v0':[],'v1':['w']})]
    allok=True
    for a in test_as:
        lhs = count_mor(tensor(dS, prod(a,p)), q)   # Workers_S(a×p,q)
        rhs = count_mor(tensor(dS, a), E)            # Workers_S(a,E)
        flag = (lhs==rhs)
        allok &= flag
        print(f"  a={a.shapes}: |Work(a×p,q)|={lhs}  |Work(a,E)|={rhs}  {'MATCH' if flag else 'DIFFER'}")
    print(f"  ALL MATCH: {allok}")
