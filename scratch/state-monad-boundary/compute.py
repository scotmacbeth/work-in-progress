"""
State/Reader boundary: Q1 counting, Q2 cartesian pullback test, Q3 pi-Mendler.
All finite, explicit. Elements represented as tuples/ints.
"""
from itertools import product

# ---------------------------------------------------------------------------
# Q1 : POLYNOMIAL FORM (counting the iso in (b))
# ---------------------------------------------------------------------------
def q1():
    print("="*70)
    print("Q1  Polynomial form / counting")
    print("="*70)
    print("(a) Reader_E(X)=X^E : container = (1 shape, E positions).")
    print("    |Reader_E(X)| = |X|^|E|.  For E size 2:")
    for nx in (0,1,2,3):
        print(f"      |X|={nx}: |Reader(X)|={nx**2}  (=|X|^2)")
    print()
    print("(b) State_S(X)=(S x X)^S  vs  Sum_{h in S^S} |X|^|S|")
    for sS in (2,3):
        print(f"  |S|={sS}:")
        for nx in (0,1,2,3):
            lhs = (sS*nx)**sS                     # |(SxX)^S|
            rhs = (sS**sS) * (nx**sS)             # sum over h:S->S of |X|^|S|
            print(f"    |X|={nx}: |(SxX)^S|={lhs:6d}   Sum_h |X|^|S|={rhs:6d}   match={lhs==rhs}")
    print("  => State_S container = (shapes = S^S, each shape has |S| positions).")

# ---------------------------------------------------------------------------
# Generic finite pullback / cartesian test for a monad's mu.
#   square:   MMX --muX--> MX
#             MMf|          |Mf
#             MMY --muY--> MY
#   cartesian at f  <=>  canonical  MMX -> MX x_{MY} MMY  is a bijection.
# ---------------------------------------------------------------------------
def cartesian_test(name, MX, MMX, Mf, MMf, muX, muY, X, Y):
    # build pullback set P = {(a,c) in MX x MMY : Mf(a)==muY(c)}
    MY  = MX(Y)
    MMY = MMX(Y)
    mxX, mmxX = MX(X), MMX(X)
    # pullback set P = {(a,c) in MX(X) x MMY : Mf(a)==muY(c)}
    P = []
    for a in mxX:
        fa = Mf(a, X, Y)
        for c in MMY:
            if muY(c, Y) == fa:
                P.append((a, c))
    Pset = set(P)
    # phi
    images = []
    ok_land = True
    for G in mmxX:
        img = (muX(G, X), MMf(G, X, Y))
        images.append(img)
        if img not in Pset:
            ok_land = False
    inj = len(set(images)) == len(images)
    surj = set(images) == Pset
    print(f"[{name}] f:{X}->{Y}  |MMX|={len(mmxX)} |P|={len(Pset)}  "
          f"lands_in_P={ok_land}  phi_injective={inj}  phi_surjective={surj}  "
          f"=> CARTESIAN={inj and surj}")
    return inj and surj

# ---------------------------------------------------------------------------
# READER monad,  E = {0,1}
# ---------------------------------------------------------------------------
E = (0,1)
def R_MX(X):
    # functions E->X  as tuples length |E|
    return list(product(X, repeat=len(E)))
def R_MMX(X):
    mx = R_MX(X)
    # functions E->MX  as tuples length |E| of MX-elements
    return list(product(mx, repeat=len(E)))
def R_Mf(a, X, Y, f=None):
    f = f or (lambda x: 0)  # default collapse; overridden via closure
    return tuple(_f[x] for x in a)
# We need f as data. Use module-level dict.
_f = {}
def R_Mf(a, X, Y):
    return tuple(_f[x] for x in a)
def R_MMf(G, X, Y):
    return tuple(R_Mf(g, X, Y) for g in G)
def R_muX(G, X):
    # mu(G)(e) = G(e)(e)
    return tuple(G[e][e] for e in range(len(E)))

def reader_q2():
    print("="*70)
    print("Q2  Reader cartesian test  (E={0,1})")
    print("="*70)
    # f: X->Y collapsing X={0,1} -> Y={0}
    global _f
    X=(0,1); Y=(0,)
    _f = {0:0,1:0}
    cartesian_test("Reader", R_MX, R_MMX, R_Mf, R_MMf, R_muX, R_muX, X, Y)
    # also identity-ish f: X={0,1}->Y={0,1}
    Y2=(0,1); _f={0:0,1:1}
    cartesian_test("Reader", R_MX, R_MMX, R_Mf, R_MMf, R_muX, R_muX, X, Y2)
    print("  backward position map of mu: E -> E x E, e|->(e,e)  (the DIAGONAL).")
    print("  diagonal is injective, NOT surjective (misses off-diagonal of ExE).")

# ---------------------------------------------------------------------------
# STATE monad,  S = {0,1}
# ---------------------------------------------------------------------------
S = (0,1)
def St_MX(X):
    # functions S -> S x X, as tuples length |S| of pairs (s',x)
    cell = list(product(S, X))            # S x X
    return list(product(cell, repeat=len(S)))
def St_MMX(X):
    mx = St_MX(X)
    cell = list(product(S, mx))           # S x MX
    return list(product(cell, repeat=len(S)))
def St_Mf(a, X, Y):
    return tuple((sp, _f[x]) for (sp,x) in a)
def St_MMf(F, X, Y):
    return tuple((sp, St_Mf(m, X, Y)) for (sp,m) in F)
def St_muX(F, X):
    # mu(F)(s0): (s1,m)=F[s0]; return m[s1]
    out=[]
    for s0 in range(len(S)):
        s1, m = F[s0]
        out.append(m[s1])
    return tuple(out)

def state_q2():
    print("="*70)
    print("Q2  State cartesian test  (S={0,1})")
    print("="*70)
    global _f
    X=(0,1); Y=(0,)
    _f={0:0,1:0}
    cartesian_test("State", St_MX, St_MMX, St_Mf, St_MMf, St_muX, St_muX, X, Y)
    Y2=(0,1); _f={0:0,1:1}
    cartesian_test("State", St_MX, St_MMX, St_Mf, St_MMf, St_muX, St_muX, X, Y2)
    print("  For fixed outer shape h:S->S, backward position map of mu:")
    print("     S -> S x S,  s0 |-> (s0, h(s0))   = graph-of-h embedding.")
    print("  injective (first coord s0), NOT surjective => state is threaded/reused.")

# ---------------------------------------------------------------------------
# Q3 : pi-Mendler diagnostic. Is mu a well-defined CONTAINER morphism
#      (single-valued backward leaf map, no quotient) ?
#      Test on single-shape container (1,A), |A|=2, i.e. the leaf-transport.
# ---------------------------------------------------------------------------
def q3():
    print("="*70)
    print("Q3  pi-Mendler: is mu's backward leaf-map a well-defined function?")
    print("="*70)
    A=(0,1)
    # Reader: backward map delta: A -> A x A (diagonal). Check single-valued & total.
    delta = {a:(a,a) for a in A}
    tot = all(a in delta for a in A)
    single = all(isinstance(delta[a],tuple) for a in A)
    inj = len(set(delta.values()))==len(A)
    surj = set(delta.values())==set(product(A,A))
    print(f"[Reader] backward E->ExE = diagonal: total={tot} single_valued={single} "
          f"injective={inj} surjective(=>cartesian)={surj}")
    print("   => well-defined function, NO quotient/merge => pi-Mendler YES; non-cart (not surj).")
    # State: for each shape h, backward s0->(s0,h(s0)); enumerate all h to confirm always a function
    allfun=True; anyquotient=False
    for h in product(S, repeat=len(S)):           # h: S->S
        bmap = {s0:(s0,h[s0]) for s0 in S}
        if not all(s0 in bmap for s0 in S): allfun=False
        # single-valued by construction; check no two outputs forced to merge inputs (injective on s0)
        if len(set(k for k in bmap))!=len(S): anyquotient=True
    print(f"[State ] backward s0->(s0,h(s0)) for ALL {len(list(product(S,repeat=len(S))))} shapes h: "
          f"always_total_function={allfun}  needs_quotient={anyquotient}")
    print("   => well-defined function for every shape, NO quotient/merge => pi-Mendler YES; non-cart.")
    print("   (Contrast Bag: mu must quotient by leaf-permutation symmetry -> backward map")
    print("    is only defined up to Sym(A), NOT a single-valued function => pi-Mendler NO / analytic.)")

if __name__=="__main__":
    q1(); print()
    reader_q2(); print()
    state_q2(); print()
    q3()
