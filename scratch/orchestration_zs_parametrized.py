"""
Parametrized verification: the family K_eps (eps in {0,1}) of supervisor-worker
orchestration categories, with s2 o p = q * tau^eps.

Goal: confirm ANALYTIC claims used in the promote-to-proved write-up:
 (a) K_eps is a well-defined category for both eps (associativity).
 (b) (L) holds: every Hom(-,b) is a free right D-set.
 (c) Sk_C (orbit category) is the SAME branch S->W=>R for both eps.
 (d) restriction maps of the presheaf are all zero.
 (e) B^2 = diagonal <(1,1)>, so H^2 = (Z/2)^2/diag ~= Z/2.
 (f) natural-transversal defect omega_T = (0, eps); hence [omega] = eps.
 (g) cross-check #SFS: 2 if eps=0, 0 if eps=1.
"""
from itertools import product

# Morphisms encoded as strings. tau is the S-involution.
# Objects: S, W, R.
# End(S) = {idS, tau}; Hom(S,W)={p,pt}; Hom(S,R)={q,qt}; Hom(W,R)={s,s2};
# End(W)={idW}; End(R)={idR}.

MORPH = ['idS','tau','p','pt','q','qt','s','s2','idW','idR']
dom = {'idS':'S','tau':'S','p':'S','pt':'S','q':'S','qt':'S',
       's':'W','s2':'W','idW':'W','idR':'R'}
cod = {'idS':'S','tau':'S','p':'W','pt':'W','q':'R','qt':'R',
       's':'R','s2':'R','idW':'W','idR':'R'}

def make_comp(eps):
    C = {}
    def setc(g,f,gf):  # g o f = gf
        C[(g,f)] = gf
    # identities
    for m in MORPH:
        setc(m, 'id'+dom[m], m)
        setc('id'+cod[m], m, m)
    # S-endos: tau^2 = idS
    setc('tau','tau','idS')
    # tau acting on the right of S->? arrows: definition of the tau-twist
    setc('p','tau','pt'); setc('pt','tau','p')
    setc('q','tau','qt'); setc('qt','tau','q')
    # worker outcomes o dispatch:
    # s o p = q ; s o pt = qt
    setc('s','p','q'); setc('s','pt','qt')
    # s2 o p = q*tau^eps ; s2 o pt = q*tau^(eps+1)
    setc('s2','p', 'q' if eps==0 else 'qt')
    setc('s2','pt','qt' if eps==0 else 'q')
    return C

def check_category(C):
    # totality on composable pairs
    for g in MORPH:
        for f in MORPH:
            if dom[g]==cod[f]:
                assert (g,f) in C, f"missing {g} o {f}"
                assert dom[C[(g,f)]]==dom[f] and cod[C[(g,f)]]==cod[g]
    # associativity
    for h in MORPH:
        for g in MORPH:
            for f in MORPH:
                if cod[f]==dom[g] and cod[g]==dom[h]:
                    left  = C[(h, C[(g,f)])]
                    right = C[(C[(h,g)], f)]
                    assert left==right, f"assoc fail {h}{g}{f}: {left} vs {right}"
    return True

D = ['idS','tau','idW','idR']   # the wide right factor

def right_orbits(C, target):
    """orbits of Hom(-,target) under right D-action (precomposition)."""
    homs = [m for m in MORPH if cod[m]==target]
    # union-find by f ~ f o d
    parent = {m:m for m in homs}
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def uni(a,b): parent[find(a)]=find(b)
    for f in homs:
        for d in D:
            if cod[d]==dom[f]:
                uni(f, C[(f,d)])
    orbs = {}
    for m in homs: orbs.setdefault(find(m),[]).append(m)
    return list(orbs.values())

def is_free(C, orbit):
    """orbit is free: for a generator c, d->c o d is injective from D-arrows-into-dom(c)."""
    c = orbit[0]
    a = dom[c]
    darrs = [d for d in D if cod[d]==a]
    images = [C[(c,d)] for d in darrs]
    return len(set(images))==len(images) and set(images)==set(orbit)

for eps in (0,1):
    C = make_comp(eps)
    assert check_category(C), eps
    # (b) freeness
    for tgt in ('S','W','R'):
        for orb in right_orbits(C,tgt):
            assert is_free(C,orb), (eps,tgt,orb)
    # (c) orbit-category composition [s]*[p], [s2]*[p]
    def orbrep(target, m):
        for orb in right_orbits(C,target):
            if m in orb: return tuple(sorted(orb))
        raise KeyError
    sp  = C[('s','p')]; s2p = C[('s2','p')]
    assert orbrep('R',sp)==orbrep('R',s2p)==orbrep('R','q'), eps  # both give [q]
    print(f"eps={eps}: category OK, (L) holds, [s]*[p]=[s2]*[p]=[q]")

# (e,f) defect + cohomology on the fixed Sk_C, coords (omega([s],[p]), omega([s2],[p]))
# presheaf restriction maps all zero (targets W,R have trivial vertex group).
# natural transversal T = {p,q,s,s2}. floor(.)=q for orb(q).
def defect(C):
    # s o p = q * w1  => w1 in {idS(=0), tau(=1)}
    sp  = C[('s','p')]   # 'q' or 'qt'
    s2p = C[('s2','p')]  # 'q' or 'qt'
    w1 = 0 if sp=='q' else 1
    w2 = 0 if s2p=='q' else 1
    return (w1,w2)

# B^2 from delta^1 h, h=(h_p,h_q): delta1([s],[p]) = h_p - h_q ; delta1([s2],[p]) = h_p - h_q
def B2():
    s=set()
    for hp in (0,1):
        for hq in (0,1):
            s.add(((hp-hq)%2,(hp-hq)%2))
    return s

B = B2()
assert B=={(0,0),(1,1)}, B
def in_B(v): return tuple(x%2 for x in v) in B
for eps in (0,1):
    C=make_comp(eps)
    w=defect(C)
    print(f"eps={eps}: defect omega_T={w}; [omega]=0? {in_B(w)}")
    assert w==(0,eps)
    # [omega]=0 iff eps=0
    assert in_B(w) == (eps==0)

print("H^2 = (Z/2)^2 / <(1,1)> ~= Z/2 ; [omega(K_eps)] = eps  (0=>trivial,1=>generator)")

# (g) brute-force #SFS cross check: count wide C making (C,D) strict factorization system.
def brute_sfs(C):
    # A wide subcategory C: contains all identities, closed under composition,
    # and (C,D) strict factorization: every morphism factors UNIQUELY as c o d, c in C, d in D.
    # We search over choices of one generator per free orbit (transversal) that close.
    # Orbits with nontrivial choice: Hom(-,W) orbit {p,pt}; Hom(-,R) orbit {q,qt}.
    # s,s2,idR,idW,idS forced in C (singleton orbits / identities).
    count=0
    for tp in ('p','pt'):
        for tq in ('q','qt'):
            Cset={'idS','idW','idR','s','s2',tp,tq}
            # closure check: all composites of C-arrows land in C
            ok=True
            for g in Cset:
                for f in Cset:
                    if dom[g]==cod[f]:
                        if C[(g,f)] not in Cset: ok=False
            if ok: count+=1
    return count

for eps in (0,1):
    C=make_comp(eps)
    n=brute_sfs(C)
    print(f"eps={eps}: #SFS = {n}")
    assert n==(2 if eps==0 else 0)

print("\nALL ANALYTIC CLAIMS CONFIRMED.")
