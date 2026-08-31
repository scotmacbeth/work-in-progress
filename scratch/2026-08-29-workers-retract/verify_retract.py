"""Verify the Workers-retract-of-BHM claim as GENUINE Poly morphisms.

Poly object: (shapes:list, pos: dict shape->list of positions)
Poly morphism f: p->q: (fwd: dict shape_p -> shape_q, bwd: dict shape_p -> (dict pos_q[f(s)] -> pos_p[s]))
Composition (g∘f)(p->q->wait): if f:p->q, g:q->r then g∘f: p->r,
   fwd: s -> g.fwd[f.fwd[s]]
   bwd: s -> for pos c in r[gf(s)]:  f.bwd[s][ g.bwd[f.fwd[s]][c] ]
"""
from itertools import product

def sets(n): return list(range(n))

def DeltaS(S):
    # ΔS = S·y^S : shapes S, positions S
    shapes = list(S)
    pos = {s: list(S) for s in S}
    return shapes, pos

def Dirichlet_Delta(S,T):
    # Δ(S×T): shapes S×T, positions S×T
    shapes = list(product(S,T))
    pos = {st: list(product(S,T)) for st in shapes}
    return shapes, pos

def Triangle(S,T):
    # ΔS ▷ ΔT: shapes (s, g) g:S->T ; positions (i,j) i∈S, j∈T
    gs = list(product(T, repeat=len(S)))  # g as tuple indexed by S
    shapes = [(s, g) for s in S for g in gs]
    pos = {(s,g): list(product(S,T)) for (s,g) in shapes}
    return shapes, pos

def apply_g(g, i, S):
    # g is a tuple indexed by position of i in S
    return g[list(S).index(i)]

def compose(f, g):
    # f: p->q  (f=(ffwd,fbwd)), g: q->r (g=(gfwd,gbwd)); returns g∘f : p->r
    ffwd, fbwd = f
    gfwd, gbwd = g
    hfwd = {}
    hbwd = {}
    for s in ffwd:
        qs = ffwd[s]
        rs = gfwd[qs]
        hfwd[s] = rs
        # bwd: for each pos c in r[rs], map to p[s] via fbwd[s][ gbwd[qs][c] ]
        hbwd[s] = {c: fbwd[s][ gbwd[qs][c] ] for c in gbwd[qs]}
    return hfwd, hbwd

def is_identity(morph, shapes, pos):
    fwd, bwd = morph
    for s in shapes:
        if fwd[s] != s: return False, f"fwd not id at {s}: {fwd[s]}"
        for c in pos[s]:
            if bwd[s][c] != c: return False, f"bwd not id at {s},{c}: {bwd[s][c]}"
    return True, "ok"

def check(nS, nT):
    S, T = sets(nS), sets(nT)
    A_sh, A_pos = Dirichlet_Delta(S,T)
    B_sh, B_pos = Triangle(S,T)
    # sigma: A->B
    def const_g(t): return tuple(t for _ in S)
    sig_fwd = {(s,t): (s, const_g(t)) for (s,t) in A_sh}
    sig_bwd = {(s,t): {c:c for c in B_pos[(s, const_g(t))]} for (s,t) in A_sh}
    sigma = (sig_fwd, sig_bwd)
    # r: B->A
    r_fwd = {(s,g): (s, apply_g(g,s,S)) for (s,g) in B_sh}
    r_bwd = {(s,g): {c:c for c in A_pos[(s, apply_g(g,s,S))]} for (s,g) in B_sh}
    r = (r_fwd, r_bwd)
    # r∘σ : A->A
    comp = compose(sigma, r)
    ok, msg = is_identity(comp, A_sh, A_pos)
    # also check well-typed: sigma bwd domain matches B_pos[sig_fwd], r bwd domain matches A_pos[r_fwd]
    typed = True
    for (s,t) in A_sh:
        if set(sig_bwd[(s,t)].keys()) != set(B_pos[sig_fwd[(s,t)]]): typed=False
        for c,v in sig_bwd[(s,t)].items():
            if v not in A_pos[(s,t)]: typed=False
    for (s,g) in B_sh:
        if set(r_bwd[(s,g)].keys()) != set(A_pos[r_fwd[(s,g)]]): typed=False
        for c,v in r_bwd[(s,g)].items():
            if v not in B_pos[(s,g)]: typed=False
    # is sigma∘r = id_B ?
    comp2 = compose(r, sigma)
    ok2, _ = is_identity(comp2, B_sh, B_pos)
    print(f"|S|={nS},|T|={nT}: |A_sh|={len(A_sh)} |B_sh|={len(B_sh)} | r∘σ=id_A: {ok} ({msg}) | well-typed: {typed} | σ∘r=id_B: {ok2}")

for (a,b) in [(1,1),(2,2),(3,2),(2,3),(3,3)]:
    check(a,b)
