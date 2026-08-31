import itertools
def star(A,B):
    e=[('l',a) for a in A]+[('r',b) for b in B]
    if A and B: e.append('m')
    return tuple(e)
def smap(f,g,A,B):
    d={}
    for x in star(A,B):
        if x=='m': d[x]='m'
        elif x[0]=='l': d[x]=('l',f[x[1]])
        else: d[x]=('r',g[x[1]])
    return d
def idm(A): return {a:a for a in A}

# compositional normal-form maps (canonical => natural)
def build2(bracket,Xs):
    if isinstance(bracket,int):
        i=bracket; S=tuple(Xs[i]); can={x:('leaf',i,x) for x in S}
        return S,can,([i] if Xs[i] else [])
    bl,br=bracket
    Sl,canl,NEl=build2(bl,Xs); Sr,canr,NEr=build2(br,Xs)
    S=star(Sl,Sr); can={}
    for x in S:
        if x=='m': can[x]=('sep',(NEl[-1],NEr[0]))
        elif x[0]=='l': can[x]=canl[x[1]]
        else: can[x]=canr[x[1]]
    return S,can,NEl+NEr
def canon(bracket,Xs):
    S,can,_=build2(bracket,Xs); return S,can
def assoc(A,B,C):
    Xs=[A,B,C]
    L,cL=canon(((0,1),2),Xs); R,cR=canon((0,(1,2)),Xs)
    invR={v:k for k,v in cR.items()}
    assert len(invR)==len(R)
    return {x:invR[cL[x]] for x in L},L,R
def bij(d,L,R): return set(d)==set(L) and set(d.values())==set(R) and len(set(d.values()))==len(R)
def rho(A): return {('l',a):a for a in A}
def lam(B): return {('r',b):b for b in B}
def compose(d2,d1): return {x:d2[d1[x]] for x in d1}

sets=[(),(0,),(0,1),(0,1,2)]
def allmaps(A,B):
    A=list(A)
    if not A: yield {}; return
    for v in itertools.product(B,repeat=len(A)): yield {A[i]:v[i] for i in range(len(A))}

def check_assoc_nat():
    for A in sets:
     for B in sets:
      for C in sets:
       d,L,R=assoc(A,B,C)
       if not bij(d,L,R): return ("not bijection",A,B,C)
    for A in sets[:3]:
     for B in sets[:3]:
      for C in sets[:3]:
       for Ap in sets[:3]:
        for Bp in sets[:3]:
         for Cp in sets[:3]:
          for f in allmaps(A,Ap):
           for g in allmaps(B,Bp):
            for h in allmaps(C,Cp):
             dA,L,_=assoc(A,B,C); dAp,_,_=assoc(Ap,Bp,Cp)
             fg=smap(f,g,A,B); lhs={x:dAp[smap(fg,h,star(A,B),C)[x]] for x in L}
             gh=smap(g,h,B,C); rhs={x:smap(f,gh,A,star(B,C))[dA[x]] for x in L}
             if lhs!=rhs: return ("naturality fail",A,B,C,Ap,Bp,Cp)
    return "OK"
print("associator natural iso:", check_assoc_nat())

def check_pentagon():
    S=[(),(0,),(0,1)]
    for A in S:
     for B in S:
      for C in S:
       for D in S:
        aL1,_,_=assoc(star(A,B),C,D); aL2,_,_=assoc(A,B,star(C,D))
        p1=compose(aL2,aL1)
        aABC,_,_=assoc(A,B,C); m1=smap(aABC,idm(D),star(star(A,B),C),D)
        aA_BC_D,_,_=assoc(A,star(B,C),D); aBCD,_,_=assoc(B,C,D)
        m3=smap(idm(A),aBCD,A,star(star(B,C),D))
        p2=compose(m3,compose(aA_BC_D,m1))
        if p1!=p2: return ("PENTAGON FAIL",A,B,C,D)
    return "OK"
print("pentagon:", check_pentagon())

def check_triangle():
    for A in sets:
     for B in sets:
      a,L,R=assoc(A,(),B)
      left=smap(rho(A),idm(B),star(A,()),B)
      right=compose(smap(idm(A),lam(B),A,star((),B)), a)
      if left!=right: return ("TRIANGLE FAIL",A,B)
    return "OK"
print("triangle:", check_triangle())

# unit coherence: left/right unitor natural isos, and λ_∅=ρ_∅
print("rho natural bijection A*∅≅A:", all(set(rho(A))==set(star(A,())) and set(rho(A).values())==set(A) for A in sets))
print("lam natural bijection ∅*B≅B:", all(set(lam(B))==set(star((),B)) and set(lam(B).values())==set(B) for B in sets))

prof=[len(star(tuple(range(m)),(0,1))) for m in range(4)]
print("|A*B|, |B|=2, |A|=0..3:", prof)
