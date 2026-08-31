"""
Minimal witness that NO bifunctor F: C x C -> C with object map max exists,
already on the two objects S1 (size 1), S2 (size 2).

Morphisms used:
  i0 : S1 -> S2   (point 0),  tab (0,)
  t  : S2 -> S1   (the UNIQUE map S2->S1, collapse), tab (0,0)
  identities id1, id2.
Fact in C:  t o i0 = id_{S1}   (i0 is a section of t; t is a retraction).

Claim: interchange forces F(t,i0) : (S2*S1) -> (S1*S2)  [size2 -> size2]
to be simultaneously a constant map and a bijection.  Contradiction.
"""

def comp(g,f):
    assert f[1]==g[0]
    return (f[0],g[1],tuple(g[2][f[2][x]] for x in range(f[0])))
def ident(a): return (a,a,tuple(range(a)))

i0 = (1,2,(0,)); i1=(1,2,(1,)); t=(2,1,(0,0)); id1=ident(1); id2=ident(2)
# check t o i0 = id1
assert comp(t,i0)==id1
assert comp(t,i1)==id1
mx=lambda a,b:max(a,b)

# object map: sizes.  A*B has size max.
# F(f,g): (dom f * dom g) -> (cod f * cod g).

# ---- Forced deduction (holds for ANY bifunctor with object map max) ----
print("hom-set sizes relevant:")
# number of functions size m -> size n = n^m
def numfun(m,n): return n**m
print("  hom(S2,S1) = size2->size1 :", numfun(2,1), " (UNIQUE map => collapse to a point)")
print("  hom(S1,S2) = size1->size2 :", numfun(1,2), " (both are points, rank 1)")
print("  hom(S2,S2) = size2->size2 :", numfun(2,2))

# F(t,id1): lives in hom( S2*S1 , S1*S1 ) = hom(size2, size1) -> UNIQUE = collapse
dc = (mx(t[0],id1[0]), mx(t[1],id1[1]))   # (2,1)
print("\nF(t,id1) domain/cod sizes:", dc, "-> forced to the unique map (collapse):", (2,1,(0,0)))
F_t_id1 = (2,1,(0,0))

# F(id1,i0): hom( S1*S1 , S1*S2 ) = hom(size1,size2): a point (rank 1)
dc2 = (mx(id1[0],i0[0]), mx(id1[1],i0[1]))  # (1,2)
print("F(id1,i0) domain/cod sizes:", dc2, "-> some point p:S1->S2 (rank 1)")
# whichever point, say sends 0 -> p in {0,1}. P1 = F(id1,i0) o F(t,id1).
for p in [ (1,2,(0,)), (1,2,(1,)) ]:
    P1 = comp(p, F_t_id1)   # size2 -> size2
    print("  if F(id1,i0)=",p,"  P1 = F(id1,i0) o F(t,id1) =", P1,
          " image size =", len(set(P1[2])), "(constant)" if len(set(P1[2]))==1 else "")

# ---- P2 side: both factors invertible ----
# F(id2,i0) o F(id2,t)?  Use: F(id2,t) o F(id2,i0) = F(id2, t o i0)=F(id2,id1)=id_{S2}
#   => F(id2,i0) is invertible (a bijection S2->S2)
# F(t,id2) o F(i0,id2) = F(t o i0, id2) = F(id1,id2)=id_{S2}
#   => F(t,id2) invertible.
# P2 = F(t,id2) o F(id2,i0) = bijection o bijection = bijection (image size 2).
print("\nF(id2,i0): bijection S2->S2 because F(id2,t) o F(id2,i0)=F(id2,id1)=id")
print("F(t,id2):  bijection S2->S2 because F(t,id2) o F(i0,id2)=F(id1,id2)=id")
print("=> P2 = F(t,id2) o F(id2,i0) is a BIJECTION (image size 2)")

# ---- Interchange: P1 and P2 are two factorizations of the SAME morphism F(t,i0) ----
# P1 :  (t,i0) = (id1,i0) o (t,id1)
# P2 :  (t,i0) = (t,id2) o (id2,i0)
# verify these are equal decompositions in the product category:
def cpair(q,p):
    (a1,a2)=p;(b1,b2)=q
    assert a1[1]==b1[0] and a2[1]==b2[0]
    return (comp(b1,a1),comp(b2,a2))
assert cpair((id1,i0),(t,id1)) == (t,i0)
assert cpair((t,id2),(id2,i0)) == (t,i0)
print("\nInterchange: (id1,i0)o(t,id1) = (t,i0) = (t,id2)o(id2,i0)  [verified]")
print("=> F(t,i0) must equal P1 (constant, image size 1) AND P2 (bijection, image size 2).")
print("=> 1 = |image of a constant on a 2-elt set| = |image of a bijection| = 2.  CONTRADICTION.")
print("\nCONCLUSION: no bifunctor with object map max exists, already on {S1,S2}.")
