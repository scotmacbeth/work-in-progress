# Polynomial functor <=> preserves connected limits. Simplest connected limit test:
# preservation of the pullback of the two points  1 -i0-> 2 <-i1- 1 , whose pullback is ∅.
# So (−)⋆B polynomial REQUIRES:  ∅⋆B  ≅  (1⋆B) ×_{2⋆B} (1⋆B)   via R_B(i0),R_B(i1).
# Check this necessary condition for ∨_S (should hold) and support tensor (should fail).

def pb(X, f, Y, g):   # {(x,y): f[x]==g[y]}
    return [(x,y) for x in X for y in Y if f[x]==g[y]]

# ---- ∨_S :  A ∨ B = A ⊔ (A×S×B) ⊔ B ----
def vee(A,B,S):
    return [('a',a) for a in A]+[('m',a,s,b) for a in A for s in S for b in B]+[('b',b) for b in B]
def vee_mapA(f,A,B,S):  # induced by f:A->A' on (−)∨B
    d={}
    for x in vee(A,B,S):
        if x[0]=='a': d[x]=('a',f[x[1]])
        elif x[0]=='m': d[x]=('m',f[x[1]],x[2],x[3])
        else: d[x]=x
    return d
def test(tensorA_map, tensorA_obj, name, S=None):
    A0=[]; A1=[0]; A2=[0,1]; B=[0,1]   # ∅,1,2 and B of size 2
    i0={0:0}; i1={0:1}   # 1->2
    T1=tensorA_obj(A1,B); T2=tensorA_obj(A2,B); T0=tensorA_obj(A0,B)
    m0=tensorA_map(i0,A1,B); m1=tensorA_map(i1,A1,B)   # 1⋆B -> 2⋆B
    P=pb(T1,m0,T1,m1)
    ok = len(P)==len(T0)
    print(f"{name}: |∅⋆B|={len(T0)}, |pullback (1⋆B)×_(2⋆B)(1⋆B)|={len(P)}  -> preserves pullback (polynomial-necessary): {ok}")

test(lambda f,A,B: vee_mapA(f,A,B,[0]), lambda A,B: vee(A,B,[0]), "∨_S (|S|=1)")

# ---- support tensor A*B = A ⊔ B ⊔ [both≠∅] ----
def sup_obj(A,B):
    e=[('l',a) for a in A]+[('r',b) for b in B]
    if A and B: e.append('m')
    return e
def sup_mapA(f,A,B):
    d={}
    for x in sup_obj(A,B):
        if x=='m': d[x]='m'
        elif x[0]=='l': d[x]=('l',f[x[1]])
        else: d[x]=('r',x[1])
    return d
test(sup_mapA, sup_obj, "support A⊔B⊔[both≠∅]")

# also cartesian × and coproduct + as sanity (both polynomial)
def times_obj(A,B): return [(a,b) for a in A for b in B]
def times_mapA(f,A,B): return {(a,b):(f[a],b) for a in A for b in B}
test(times_mapA, times_obj, "× (product)")
def plus_obj(A,B): return [('l',a) for a in A]+[('r',b) for b in B]
def plus_mapA(f,A,B):
    d={}
    for x in plus_obj(A,B): d[x]=('l',f[x[1]]) if x[0]=='l' else x
    return d
test(plus_mapA, plus_obj, "+ (coproduct)")
