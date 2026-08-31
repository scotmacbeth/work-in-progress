"""
Verification harness for ΔS / reader-store / category of Workers.
Everything is finite and exhaustive. No randomness (per Δ-law harness convention).

Container: p = (A, B) where A is a list of shapes, B: dict shape -> list of positions.
Morphism p->q: (f, fsharp) where f: dict a->c ; fsharp: dict a -> (dict d(in D(f a)) -> b in B a).
We represent positions/shapes as python objects; functions as dicts.
"""
from itertools import product

# ---------- container helpers ----------
def make_container(A, B):
    return {"A": list(A), "B": {a: list(B[a]) for a in A}}

def extension(p, X):
    """⟦p⟧X as a set of (shape, tuple-of-values indexed by positions order)."""
    out = []
    for a in p["A"]:
        poss = p["B"][a]
        for vals in product(X, repeat=len(poss)):
            out.append((a, dict(zip(poss, vals))))
    return out

# ---------- Δ ----------
def Delta(S):
    """ΔS = (S, s->S). Positions of every shape are the whole S (tag them to keep them distinct as a set)."""
    A = list(S)
    B = {s: list(S) for s in S}
    return make_container(A, B)

# ---------- Dirichlet tensor ----------
def tensor(p, q):
    A = [(a, c) for a in p["A"] for c in q["A"]]
    B = {}
    for (a, c) in A:
        # positions = product B[a] x D[c]; tag as pairs
        B[(a, c)] = [(bp, dp) for bp in p["B"][a] for dp in q["B"][c]]
    return make_container(A, B)

def containers_equal(p, q):
    if set(map(str, p["A"])) != set(map(str, q["A"])):
        return False
    for a in p["A"]:
        if sorted(map(str, p["B"][a])) != sorted(map(str, q["B"][a])):
            return False
    return True

# ============================================================
# T1: D1-D5 for ΔS with o_s=s, s|p=p, p+p'=p'
# ============================================================
def check_directed_laws(S):
    """Directed container on ΔS: P(s)=S, o_s=s, s↓p=p, p⊕p'=p'."""
    o = {s: s for s in S}          # o_s = s
    down = lambda s, p: p          # s ↓ p = p
    oplus = lambda p, pp: pp       # p ⊕ p' = p'  (2nd projection)
    ok = True
    for s in S:
        # D1: s ↓ o_s = s
        if down(s, o[s]) != s: ok=False; print("D1 fail", s)
        for p in S:  # p ∈ P(s)=S
            # D3 (right unit): p ⊕ o_{s↓p} = p
            if oplus(p, o[down(s,p)]) != p: ok=False; print("D3 fail", s,p)
            # D4 (left unit): o_s ⊕ p = p
            if oplus(o[s], p) != p: ok=False; print("D4 fail", s,p)
            for pp in S:  # p' ∈ P(s↓p)=S
                # D2: s ↓ (p⊕p') = (s↓p) ↓ p'
                if down(s, oplus(p,pp)) != down(down(s,p), pp): ok=False; print("D2 fail",s,p,pp)
                for ppp in S:  # p'' ∈ P(s↓p↓p')
                    # D5: (p⊕p')⊕p'' = p⊕(p'⊕p'')
                    if oplus(oplus(p,pp),ppp) != oplus(p, oplus(pp,ppp)): ok=False; print("D5 fail")
    return ok

# ============================================================
# T1: induced comonad = store comonad; check comonad laws on finite X
# ============================================================
def store_counit(S, elt):
    (s, v) = elt   # v: dict S->X
    return v[s]                     # extract at focus  == v(o_s), o_s=s
def store_comult(S, elt):
    (s, v) = elt
    # δ(s,v) = (s, λp.(p, v))   (using s↓p=p, p⊕p'=p')
    inner = {p: (p, v) for p in S}
    return (s, inner)

def check_comonad_laws(S, X):
    ok = True
    for s in S:
        for vvals in product(X, repeat=len(S)):
            v = dict(zip(S, vvals))
            elt = (s, v)
            # left counit: extract outer of δ = id.  ⟦ε⟧ on outer layer
            (s2, inner) = store_comult(S, elt)
            # counit on the OUTER store: apply ε to (s2, p->inner[p]) gives inner[s2] = (s2, v) ... should be elt
            left = inner[s2]
            if left != elt: ok=False; print("left counit fail", elt, left)
            # right counit: map ε over inner values then it's identity
            right = (s2, {p: store_counit(S, inner[p]) for p in S})
            # store_counit(inner[p]) = store_counit((p,v)) = v[p]
            right = (s2, {p: v[p] for p in S})
            if right != elt: ok=False; print("right counit fail", elt, right)
            # coassociativity: (δ then δ on outer) vs (δ then map δ on inner)
            # outer-δ: δ(s,v)=(s, p->(p,v)); apply δ again to the whole -> (s, p->(p, p->(p,v)))?? do both routes
            # Route A: δ;δ_outer :  take (s2,inner); apply δ to get (s2, q->(q, inner))
            A_ = (s2, {q: (q, inner) for q in S})
            # Route B: δ; (id * δ over inner): (s2, p-> δ(inner[p]))
            B_ = (s2, {p: store_comult(S, inner[p]) for p in S})
            # compare as nested structures
            if str(A_) != str(B_): ok=False; print("coassoc fail", elt)
    return ok

# ============================================================
# T3: Workers
# ============================================================
# A worker w: ΔS⊗p -> q  is stored as dict:
#   'S': list ; 'p':(A,B) ; 'q':(C,D)
#   'f': dict (s,a)->c
#   'f1': dict (s,a)-> (dict d in D[c] -> s')   [state writeback]
#   'f2': dict (s,a)-> (dict d in D[c] -> b in B[a])  [position back-map]

def worker_as_contmap(w):
    """Return (dom_container, cod_container, f, fsharp) with f:(s,a)->c, fsharp:(s,a)->(d-> (s',b))."""
    S=w['S']; p=w['p']; q=w['q']
    dom = tensor(Delta(S), p)   # shapes (s,a), positions (s'',bp)
    cod = q
    f = {(s,a): w['f'][(s,a)] for s in S for a in p['A']}
    fsharp = {}
    for s in S:
        for a in p['A']:
            c = f[(s,a)]
            fsharp[(s,a)] = {d: (w['f1'][(s,a)][d], w['f2'][(s,a)][d]) for d in q['B'][c]}
    return dom,cod,f,fsharp

def is_valid_contmap(dom,cod,f,fsharp):
    """Check f: shapes(dom)->shapes(cod) and fsharp[a]: D(f a) -> B_dom(a)."""
    for a in dom['A']:
        c = f[a]
        if c not in cod['A']: print("bad shape", a, c); return False
        for d in cod['B'][c]:
            b = fsharp[a][d]
            if b not in dom['B'][a]: print("bad backmap", a, d, b, "not in", dom['B'][a]); return False
    return True

def compose_workers(w, wp):
    """w: ΔS⊗p->q ; wp: ΔT⊗q->r.  Return worker w'': Δ(T×S)⊗p -> r with state T×S."""
    S=w['S']; T=wp['S']; p=w['p']; q=w['q']; r=wp['q']
    assert containers_equal(q, wp['p']), "middle container mismatch"
    ST = [(t,s) for t in T for s in S]      # state = T×S
    f2 = {}; f1={}; f2b={}
    F={}; F1={}; F2={}
    for (t,s) in ST:
        for a in p['A']:
            c = w['f'][(s,a)]
            e = wp['f'][(t,c)]
            F[((t,s),a)] = e
            F1[((t,s),a)] = {}
            F2[((t,s),a)] = {}
            for d2 in r['B'][e]:
                tprime = wp['f1'][(t,c)][d2]          # in T
                d1 = wp['f2'][(t,c)][d2]              # in D[c]
                sprime = w['f1'][(s,a)][d1]           # in S
                b = w['f2'][(s,a)][d1]                # in B[a]
                F1[((t,s),a)][d2] = (tprime, sprime) # state ∈ T×S
                F2[((t,s),a)][d2] = b
    return {'S':ST,'p':p,'q':r,'f':F,'f1':F1,'f2':F2}

def identity_worker(p):
    """id_p : Δ1⊗p -> p, state = {*}. Δ1⊗p ≅ p."""
    star='*'
    S=[star]
    f={}; f1={}; f2={}
    for a in p['A']:
        f[(star,a)] = a
        f1[(star,a)] = {d: star for d in p['B'][a]}   # only one state
        f2[(star,a)] = {d: d for d in p['B'][a]}      # identity backmap
    return {'S':S,'p':p,'q':p,'f':f,'f1':f1,'f2':f2}

# ---------- worker equality up to a state bijection ----------
def workers_equal_upto_state_bij(w1, w2, bij):
    """bij: dict state(w1)->state(w2). Check w1 == w2 after relabelling states by bij.
    Requires same p,q."""
    if not containers_equal(w1['p'],w2['p']) or not containers_equal(w1['q'],w2['q']): return False
    p=w1['p']
    for s1 in w1['S']:
        s2=bij[s1]
        for a in p['A']:
            if w1['f'][(s1,a)] != w2['f'][(s2,a)]: return False
            c=w1['f'][(s1,a)]
            for d in w1['q']['B'][c]:
                # state writeback compared under bij
                if bij[w1['f1'][(s1,a)][d]] != w2['f1'][(s2,a)][d]: return False
                if w1['f2'][(s1,a)][d] != w2['f2'][(s2,a)][d]: return False
    return True
