# Is Gl(T), T=(-)^2, EXTENSIVE?  (copowers-file 4v labelled it "non-extensive" -- test that.)
# Artin gluing theorem: F:E->S lex between toposes => (S/F) is a topos => extensive.
# (-)^2 is right adjoint to 2x(-), hence preserves ALL limits => lex. So Gl((-)^2) should be a topos.
# We CHECK: (i) coproduct injections disjoint (pullback = initial 0_C=(∅,∅,∅));
#           (ii) universality: for random h:Z->X⊔Y, Z ≅ (h*X) ⊔ (h*Y).
# Limits in (Id/T) with T lex are componentwise (T preserves them). Implement pullback componentwise.

import itertools, random
random.seed(7)

def all_maps(dom,cod):
    dom=list(dom); cod=list(cod)
    if not dom: yield {}; return
    for v in itertools.product(cod,repeat=len(dom)): yield dict(zip(dom,v))

def coproduct(o1,o2):
    A1,B1,b1=o1; A2,B2,b2=o2
    A=[('L',a) for a in A1]+[('R',a) for a in A2]
    B=[('L',b) for b in B1]+[('R',b) for b in B2]
    beta={}
    for a in A1: x,y=b1[a]; beta[('L',a)]=(('L',x),('L',y))
    for a in A2: x,y=b2[a]; beta[('R',a)]=(('R',x),('R',y))
    return (A,B,beta)

def injL(o1,o2):
    A1,B1,_=o1
    return ({a:('L',a) for a in A1},{b:('L',b) for b in B1})
def injR(o1,o2):
    A2,B2,_=o2
    return ({a:('R',a) for a in A2},{b:('R',b) for b in B2})

# pullback of  (fA,fB):X->Z  and  (gA,gB):Y->Z  in Gl(T), componentwise:
#   A-part: {(x,y): fA(x)=gA(y)};  B-part: {(x,y): fB(x)=gB(y)};  beta induced.
def pullback(X,mX,Y,mY):
    AX,BX,bX=X; AY,BY,bY=Y; (fA,fB)=mX; (gA,gB)=mY
    A=[(x,y) for x in AX for y in AY if fA[x]==gA[y]]
    B=[(x,y) for x in BX for y in BY if fB[x]==gB[y]]
    beta={}
    for (x,y) in A:
        (x0,x1)=bX[x]; (y0,y1)=bY[y]
        # need (x0,y0),(x1,y1) to be in B (they are, since fB(x0)=... consistency from morphism laws)
        beta[(x,y)]=((x0,y0),(x1,y1))
    return (A,B,beta)

def is_initial(o):
    A,B,_=o; return len(A)==0 and len(B)==0

def iso_count_invariant(o):
    # cheap iso-invariant multiset for sanity comparison: (|A|,|B|, sorted degree structure)
    A,B,beta=o
    return (len(A),len(B))

def rand_obj(nA,nB):
    A=list(range(nA)); B=list(range(nB))
    beta={a:(random.randrange(nB),random.randrange(nB)) for a in A}
    return (A,B,beta)

# compose morphisms in Gl (component-wise dict compose)
def comp(m2,m1):
    (f2A,f2B)=m2; (f1A,f1B)=m1
    return ({a:f2A[f1A[a]] for a in f1A},{b:f2B[f1B[b]] for b in f1B})

print("=== (i) disjointness: pullback of coproduct injections = initial? (200 trials) ===")
bad=0
for _ in range(200):
    X=rand_obj(random.randint(0,3),random.randint(1,3))
    Y=rand_obj(random.randint(0,3),random.randint(1,3))
    S=coproduct(X,Y)
    iL=injL(X,Y); iR=injR(X,Y)
    pb=pullback(X,iL,Y,iR)
    if not is_initial(pb): bad+=1
print("  non-disjoint cases (should be 0):", bad)

print("\n=== (ii) universality: for random h:Z->X⊔Y,  Z ≅ h*X ⊔ h*Y  (100 trials) ===")
# build random Z and random morphism h:Z->X⊔Y, then check Z's (|A|,|B|) == coproduct of pullbacks'.
def rand_morphism(Z,W):
    # random morphism Z->W in Gl: choose gB:BZ->BW then fA consistent (if none, retry)
    AZ,BZ,bZ=Z; AW,BW,bW=W
    for _try in range(200):
        gB={b:random.choice(BW) for b in BZ}
        fA={}; ok=True
        for a in AZ:
            (x0,x1)=bZ[a]; tgt=(gB[x0],gB[x1])
            cand=[a2 for a2 in AW if bW[a2]==tgt]
            if not cand: ok=False; break
            fA[a]=random.choice(cand)
        if ok: return (fA,gB)
    return None

bad2=0; tested=0
for _ in range(400):
    X=rand_obj(random.randint(1,3),random.randint(1,3))
    Y=rand_obj(random.randint(1,3),random.randint(1,3))
    S=coproduct(X,Y)
    Z=rand_obj(random.randint(1,3),random.randint(1,4))
    h=rand_morphism(Z,S)
    if h is None: continue
    tested+=1
    iL=injL(X,Y); iR=injR(X,Y)
    ZX=pullback(Z,h,X,iL)   # pullback of h and injL
    ZY=pullback(Z,h,Y,iR)
    recomb=coproduct(ZX,ZY)
    if iso_count_invariant(Z)!=iso_count_invariant(recomb): bad2+=1
print(f"  tested={tested}, universality-count-mismatches (should be 0):", bad2)
print("  (count-invariant check; matches => consistent with extensivity/topos)")
