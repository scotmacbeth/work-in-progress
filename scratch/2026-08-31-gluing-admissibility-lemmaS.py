# Gl(T), T = (-)^2 : Set -> Set.  Comma category (Id_Set / T).
# Objects: (A, B, beta: A -> B x B).   Think: B = vertices, A = (directed) edges, beta = endpoints.
# Morphisms (A,B,beta) -> (A',B',beta') : pairs (f:A->A', g:B->B') with beta'(f(a)) = (g x g)(beta(a)).
#   i.e.  for all a:  beta'(f(a)) = (g(beta(a)_0), g(beta(a)_1)).
# Terminal / unit  1_C = I = ({*},{*}, *->(*,*)).
# Copower  T . 1_C  =  (T, T, diag).   ["kappa copies of I"]
#
# GOAL: test Lemma S at P=K (a symmetric edge), T={0,1}:
#   Lemma S (necessary for ◁-admissibility): [P, T.1_C] is a copower of 1_C, i.e. ≅ E.1_C.
# We compute Hom-sets by brute force and show [K, 2.1_C] is NOT any E.1_C.

import itertools

# ---------- basic combinatorics ----------
def all_maps(dom, cod):
    dom=list(dom); cod=list(cod)
    if len(dom)==0:
        yield {}; return
    for vals in itertools.product(cod, repeat=len(dom)):
        yield dict(zip(dom, vals))

# ---------- Gl(T) objects ----------
# object = (A, B, beta) with beta: dict a -> (b0,b1)
I_unit = (('*',), ('*',), {'*':('*','*')})   # 1_C

def copower_unit(T):
    T=list(T)
    return (T, T, {t:(t,t) for t in T})       # T . 1_C = (T,T,diag)

def product(o1,o2):
    # X x P in Gl(T): componentwise; T lex so (B x B')^... ; beta_{X x P}(a,a') = ((b0,b0'),(b1,b1'))
    A1,B1,b1=o1; A2,B2,b2=o2
    A=[(a,a2) for a in A1 for a2 in A2]
    B=[(b,b2) for b in B1 for b2 in B2]
    beta={}
    for a in A1:
        for a2 in A2:
            (x0,x1)=b1[a]; (y0,y1)=b2[a2]
            beta[(a,a2)] = ((x0,y0),(x1,y1))
    return (A,B,beta)

def coproduct(o1,o2):
    A1,B1,b1=o1; A2,B2,b2=o2
    A=[('L',a) for a in A1]+[('R',a) for a in A2]
    B=[('L',b) for b in B1]+[('R',b) for b in B2]
    beta={}
    for a in A1: x,y=b1[a]; beta[('L',a)]=(('L',x),('L',y))
    for a in A2: x,y=b2[a]; beta[('R',a)]=(('R',x),('R',y))
    return (A,B,beta)

# ---------- Hom-sets ----------
def hom(o1,o2):
    A1,B1,b1=o1; A2,B2,b2=o2
    homs=[]
    for g in all_maps(B1,B2):
        # given g, f must satisfy beta2(f(a)) = (g(b0), g(b1)); f(a) can be ANY a' with beta2(a')=that pair
        ok=True
        choices=[]
        for a in A1:
            (x0,x1)=b1[a]
            target=(g[x0], g[x1])
            cand=[a2 for a2 in A2 if b2[a2]==target]
            if not cand: ok=False; break
            choices.append((a,cand))
        if not ok: continue
        for combo in itertools.product(*[c for (_,c) in choices]):
            f={a:combo[i] for i,(a,_) in enumerate(choices)}
            homs.append((f,g))
    return homs

def hom_count(o1,o2): return len(hom(o1,o2))

# ---------- pi_0 : connected components of the graph (B, edges from beta) ----------
def pi0(o):
    A,B,beta=o
    parent={b:b for b in B}
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(x,y):
        rx,ry=find(x),find(y)
        if rx!=ry: parent[rx]=ry
    for a in A:
        b0,b1=beta[a]; union(b0,b1)
    return len({find(b) for b in B})

# ---------- test objects ----------
# K = symmetric edge: vertices {0,1}, edges e1:(0,1), e2:(1,0).  pi_0 = 1.
K = (['e1','e2'], [0,1], {'e1':(0,1),'e2':(1,0)})
# directed single-arc edge (alternative witness)
Karc = (['e'], [0,1], {'e':(0,1)})

print("=== sanity: pi_0 ===")
print("pi_0(K)      =", pi0(K), " (expect 1)")
print("pi_0(1_C)    =", pi0(I_unit), " (expect 1)")
KK = product(K,K)
print("pi_0(K x K)  =", pi0(KK), " (expect 2 by Weichsel: two bipartite conn graphs)")
print("pi_0(K)*pi_0(K) =", pi0(K)*pi0(K), " -> pi_0 does NOT preserve products iff differs")

print("\n=== check Hom(X, T.1_C) = |T|^{pi_0(X)} ===")
two = copower_unit(['a','b'])   # 2 . 1_C
for name,X in [('1_C',I_unit),('K',K),('Karc',Karc),('KxK',KK),('K+K',coproduct(K,K))]:
    hc=hom_count(X,two); pred=2**pi0(X)
    print(f"  Hom({name}, 2.1_C) = {hc:4d}   2^pi_0 = {pred:4d}   OK={hc==pred}")

print("\n=== LEMMA S TEST at P=K, T={0,1}:  is [K, 2.1_C] a copower of 1_C? ===")
# [K,2.1_C] represents  X |-> Hom(X x K, 2.1_C).
# If [K,2.1_C] ≅ E.1_C then Hom(X, E.1_C)=Hom(XxK,2.1_C) for all X.
# points force E = Hom(1_C x K, 2.1_C) = Hom(K,2.1_C):
E_forced = hom_count(product(I_unit,K), two)
print("  E forced (= |pts of [K,2.1_C]|) = Hom(K,2.1_C) =", E_forced, " (= 2^{pi_0 K} = 2)")
# now test iso at X=K:
lhs = hom_count(product(K,K), two)   # Hom(KxK, 2.1_C)
Ecop = copower_unit(list(range(E_forced)))
rhs = hom_count(K, Ecop)             # Hom(K, E.1_C)
print(f"  Hom(K x K, 2.1_C)      = {lhs}")
print(f"  Hom(K, {E_forced}.1_C)          = {rhs}")
print(f"  EQUAL? {lhs==rhs}   -> Lemma S {'HOLDS' if lhs==rhs else 'FAILS => Gl inadmissible'}")

print("\n=== stronger: no E at all works (scan E) ===")
# For [K,2.1_C] ≅ E.1_C we'd need Hom(X,E.1_C)=Hom(XxK,2.1_C) for X in a test family.
testX = [('1_C',I_unit),('K',K),('Karc',Karc),('KK',KK)]
target = {n: hom_count(product(X,K),two) for n,X in testX}
print("  target functor values Hom(X x K, 2.1_C):", target)
found=None
for E in range(0,10):
    Ec=copower_unit(list(range(E)))
    vals={n:hom_count(X,Ec) for n,X in testX}
    if vals==target: found=E; break
print("  E making E.1_C match on test family:", found, "(None => not a copower of 1_C)")
