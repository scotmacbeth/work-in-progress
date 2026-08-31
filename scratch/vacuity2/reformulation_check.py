# TASK (3): verify the pullback-of-points reformulation on four tensors.
#
# For a tensor ⋆ and a set B, R_B(X)=X⋆B.  R_B preserves the pullback of the
# two points i0,i1:1->2 iff the comparison
#     R_B(∅)=∅⋆B  -->  balanced(B) := { u ∈ 1⋆B : (i0⋆B)(u)=(i1⋆B)(u) in 2⋆B }
# induced by (∅->1)⋆B is a bijection.  The image of (∅->1)⋆B is the
# "independent" set.  balanced ⊋ independent  =>  non-polynomial witness.
#
# Conventions match pullback_lens.py: sets are lists of elements; a tensor is a
# pair (obj(A,B), mapA(f,A,B)) where mapA is the action on f:A->A' (B fixed).

def analyse(name, obj, mapA, Bsets):
    print("="*72)
    print(f"TENSOR: {name}")
    A0=[]; A1=[0]; A2=[0,1]
    i0={0:0}; i1={0:1}                # the two points 1->2
    bang={}                           # unique ∅->1  (empty function)
    for B in Bsets:
        T0=obj(A0,B)                  # ∅⋆B
        T1=obj(A1,B)                  # 1⋆B
        m0=mapA(i0,A1,B); m1=mapA(i1,A1,B)     # 1⋆B -> 2⋆B
        balanced=[u for u in T1 if m0[u]==m1[u]]
        emb=mapA(bang,A0,B)           # ∅⋆B -> 1⋆B  (dict on elements of T0)
        independent=[emb[x] for x in T0]      # image
        extra=[u for u in balanced if u not in independent]
        poly_nec = (len(balanced)==len(independent)) and \
                   all(u in balanced for u in independent)
        print(f"  |B|={len(B)}: |∅⋆B|={len(T0)}  balanced={balanced}")
        print(f"          independent(image ∅⋆B)={independent}")
        print(f"          balanced==independent ? {poly_nec}"
              f"   extra(balanced not independent)={extra}")
    print()

# ---------------- × (unit 1) ----------------
def times_obj(A,B): return [(a,b) for a in A for b in B]
def times_mapA(f,A,B): return {(a,b):(f[a],b) for a in A for b in B}

# ---------------- + (unit ∅) ----------------
def plus_obj(A,B): return [('l',a) for a in A]+[('r',b) for b in B]
def plus_mapA(f,A,B):
    d={}
    for x in plus_obj(A,B):
        d[x]=('l',f[x[1]]) if x[0]=='l' else x
    return d

# ---------------- join A+B+A×B (unit ∅) ----------------
def join_obj(A,B):
    return ([('l',a) for a in A]+[('r',b) for b in B]
            +[('m',a,b) for a in A for b in B])
def join_mapA(f,A,B):
    d={}
    for x in join_obj(A,B):
        if x[0]=='l': d[x]=('l',f[x[1]])
        elif x[0]=='r': d[x]=x
        else: d[x]=('m',f[x[1]],x[2])
    return d

# ---------------- support A⊔B⊔{•}[A,B≠∅] (unit ∅, NON-associative) ----------
def sup_obj(A,B):
    e=[('l',a) for a in A]+[('r',b) for b in B]
    if A and B: e.append('m')
    return e
def sup_mapA(f,A,B):
    d={}
    for x in sup_obj(A,B):
        if x=='m': d[x]='m'
        elif x[0]=='l': d[x]=('l',f[x[1]])
        else: d[x]=x
    return d

Bsets=[[0],[0,1]]
analyse("× product (unit 1)", times_obj, times_mapA, Bsets)
analyse("+ coproduct (unit ∅)", plus_obj, plus_mapA, Bsets)
analyse("join A+B+A×B (unit ∅)", join_obj, join_mapA, Bsets)
analyse("support A⊔B⊔{•} (unit ∅, non-assoc)", sup_obj, sup_mapA, Bsets)

# ---- phantom family claim for support: over nonempty X, c_X = • of X⋆B,
#      with c_1 = • ; naturality across nonempty maps; fails to extend to ∅. ----
print("="*72)
print("SUPPORT phantom family check (B fixed nonempty, X ranges over nonempty sets):")
def sup_map_full(f,A,B):   # action of f:A->A' on X⋆B, general
    return sup_mapA(f,A,B)
B=[0,1]
# c_X := '•' whenever X,B nonempty.  Check naturality: for f:X->X' (both nonempty)
# does (f⋆B)(c_X)=c_{X'} ?  i.e. sup_mapA sends 'm'->'m'.
import itertools
ok=True
for nX in [1,2,3]:
  for nY in [1,2,3]:
    X=list(range(nX)); Y=list(range(nY))
    for fv in itertools.product(range(nY),repeat=nX):
        f={i:fv[i] for i in range(nX)}
        img=sup_map_full(f,X,B)['m']
        if img!='m': ok=False
print(f"  c_X='•' is natural across ALL maps between nonempty sets: {ok}")
print("  c_1 = '•' ∈ 1⋆B is exactly the balanced-not-independent element above.")
print("  Extending to X=∅: ∅⋆B has NO '•' (rule needs A≠∅), so the family")
print("  cannot be extended to ∅ => genuine phantom, witnessing non-polynomiality.")
