# Correct functorial action for the collapse tensor and a HOSTILE monoidality check.
# A*B: elements  ('R',b) [b in B] if A empty ; ('L',a) [a in A] if B empty ; PT if both nonempty.
import itertools
PT=('pt',)
def star(A,B):
    A=tuple(A);B=tuple(B)
    if len(A)==0 and len(B)==0: return ()
    if len(A)==0: return tuple(('R',b) for b in B)
    if len(B)==0: return tuple(('L',a) for a in A)
    return (PT,)
def smap(f,g,A,B,A2,B2):
    # f:A->A2, g:B->B2 (dicts). Returns dict star(A,B)->star(A2,B2). Target FORM depends on A2,B2.
    A=tuple(A);B=tuple(B)
    d={}
    for x in star(A,B):
        if x==PT:
            # A,B nonempty => A2,B2 nonempty => PT
            d[x]=PT
        elif x[0]=='R':      # A empty, element is b in B
            b2=g[x[1]]
            if len(A2)==0: d[x]=('R',b2)      # A2 empty: copy of B2
            else: d[x]=PT                      # A2 nonempty, B2 nonempty(b2 exists) => PT
        else:                # x[0]=='L', B empty, element a in A
            a2=f[x[1]]
            if len(B2)==0: d[x]=('L',a2)
            else: d[x]=PT
    return d
def elems(n): return tuple(range(n))
def homs(A,B):
    A=tuple(A);B=tuple(B)
    if len(A)==0: return [dict()]
    return [dict(zip(A,v)) for v in itertools.product(B,repeat=len(A))]

def check_bifunctor(maxn=3):
    # identity
    for na in range(maxn+1):
     for nb in range(maxn+1):
       A,B=elems(na),elems(nb)
       idA={a:a for a in A}; idB={b:b for b in B}
       m=smap(idA,idB,A,B,A,B)
       assert all(m[x]==x for x in star(A,B)),("id",na,nb,m)
    # composition (bounded)
    R=range(maxn+1)
    for na in R:
     for nb in R:
      A,B=elems(na),elems(nb)
      for na2 in R:
       for nb2 in R:
        A2,B2=elems(na2),elems(nb2)
        for f in homs(A,A2):
         for g in homs(B,B2):
          for na3 in R:
           for nb3 in R:
            A3,B3=elems(na3),elems(nb3)
            for f2 in homs(A2,A3):
             for g2 in homs(B2,B3):
               fc={a:f2[f[a]] for a in A}; gc={b:g2[g[b]] for b in B}
               direct=smap(fc,gc,A,B,A3,B3)
               m1=smap(f,g,A,B,A2,B2); m2=smap(f2,g2,A2,B2,A3,B3)
               comp={x:m2[m1[x]] for x in star(A,B)}
               assert direct==comp,("COMP FAIL",(na,nb,na2,nb2,na3,nb3),f,g,f2,g2,direct,comp)
    return True

def LHS(A,B,C): return star(star(A,B),C)
def RHS(A,B,C): return star(A,star(B,C))
def alpha(A,B,C):
    A,B,C=tuple(A),tuple(B),tuple(C)
    L=LHS(A,B,C);R=RHS(A,B,C)
    ne=(len(A)>0)+(len(B)>0)+(len(C)>0)
    if ne==0: return {}
    if ne>=2:
        assert len(L)==1 and len(R)==1,("card",A,B,C,L,R)
        return {L[0]:R[0]}
    # exactly one nonempty: both sides are a tagged copy of that factor; match base index
    def base(el):
        cur=el
        while isinstance(cur,tuple) and cur and cur[0] in ('L','R'): cur=cur[1]
        return cur
    Rby={base(r):r for r in R}
    return {l:Rby[base(l)] for l in L}

def check_alpha(maxn=3):
    for na in range(maxn+1):
     for nb in range(maxn+1):
      for nc in range(maxn+1):
       A,B,C=elems(na),elems(nb),elems(nc)
       a=alpha(A,B,C)
       assert set(a)==set(LHS(A,B,C)) and set(a.values())==set(RHS(A,B,C)) and len(set(a.values()))==len(a),("alpha",na,nb,nc)
    return True

def smapT(f,g,A,B,A2,B2): return smap(f,g,A,B,A2,B2)
def check_nat(maxn=2):
    R=range(maxn+1)
    for na in R:
     for nb in R:
      for nc in R:
       A,B,C=elems(na),elems(nb),elems(nc)
       for na2 in R:
        for nb2 in R:
         for nc2 in R:
          A2,B2,C2=elems(na2),elems(nb2),elems(nc2)
          for f in homs(A,A2):
           for g in homs(B,B2):
            for h in homs(C,C2):
              # (f*g)*h : (A*B)*C -> (A2*B2)*C2
              fg=smap(f,g,A,B,A2,B2)
              left=smap(fg,h,star(A,B),C, star(A2,B2),C2)
              a2=alpha(A2,B2,C2)
              p1={x:a2[left[x]] for x in LHS(A,B,C)}
              gh=smap(g,h,B,C,B2,C2)
              right=smap(f,gh,A,star(B,C), A2,star(B2,C2))
              a1=alpha(A,B,C)
              p2={x:right[a1[x]] for x in LHS(A,B,C)}
              if p1!=p2: return (False,(na,nb,nc,na2,nb2,nc2,f,g,h))
    return (True,None)

def check_pentagon(maxn=2):
    R=range(maxn+1)
    for na in R:
     for nb in R:
      for nc in R:
       for nd in R:
        A,B,C,D=elems(na),elems(nb),elems(nc),elems(nd)
        AB,BC,CD=star(A,B),star(B,C),star(C,D)
        src=star(star(AB,C),D)
        idA={a:a for a in A}; idD={d:d for d in D}
        s1=smap(alpha(A,B,C),idD, star(AB,C),D, star(A,BC),D)  # ((A(BC))D
        s2=alpha(A,BC,D)                                       # A((BC)D)
        s3=smap(idA,alpha(B,C,D), A,star(BC,D), A,star(B,CD))  # A(B(CD))
        path1={x:s3[s2[s1[x]]] for x in src}
        sa=alpha(AB,C,D)                                       # (AB)(CD)
        sb=alpha(A,B,CD)                                       # A(B(CD))
        path2={x:sb[sa[x]] for x in src}
        if path1!=path2: return (False,(na,nb,nc,nd,path1,path2))
    return (True,None)

print("bifunctor id+comp (maxn=3):", check_bifunctor(3))
print("alpha bijection (maxn=3):", check_alpha(3))
nat=check_nat(2); print("associator NATURALITY (maxn=2):", nat)
pen=check_pentagon(2); print("PENTAGON (maxn=2):", pen)
print("R_2(0)=",len(star((),elems(2)))," R_2(1)=",len(star(elems(1),elems(2))),
      " R_2 non-polynomial since",len(star((),elems(2))),">",len(star(elems(1),elems(2))))

print("\n=== extended / hostile round 2 ===")
nat3=check_nat(3); print("associator NATURALITY (maxn=3):", nat3[0])
pen3=check_pentagon(3); print("PENTAGON (maxn=3):", pen3[0])

# unitors: lambda_A: 0*A -> A, rho_A: A*0 -> A. Check they are natural isos & triangle.
def lam(A):  # 0*A = copy of A -> A
    A=tuple(A); return {('R',a):a for a in A}
def rho(A):  # A*0 = copy of A -> A
    A=tuple(A); return {('L',a):a for a in A}
def check_unitors(maxn=3):
    for n in range(maxn+1):
        A=elems(n)
        assert set(lam(A).values())==set(A) and len(set(lam(A).values()))==n
        assert set(rho(A).values())==set(A) and len(set(rho(A).values()))==n
    # naturality of lambda: for f:A->A2, lam(A2) o (id_0 * f) = f o lam(A)
    for n in range(maxn+1):
     for n2 in range(maxn+1):
      A,A2=elems(n),elems(n2)
      for f in homs(A,A2):
        m=smap({},f,(),A,(),A2)   # 0*A -> 0*A2
        left={x: lam(A2)[m[x]] for x in star((),A)}
        right={x: f[lam(A)[x]] for x in star((),A)}
        assert left==right,("lam nat",n,n2,f)
    return True
print("unitors natural isos (maxn=3):", check_unitors(3))

# triangle: alpha(A,0,B) then (rho_A * B) vs (A * lam_B)
def check_triangle(maxn=3):
    for na in range(maxn+1):
     for nb in range(maxn+1):
       A,B=elems(na),elems(nb); E=()
       a=alpha(A,E,B)   # (A*0)*B -> A*(0*B)
       # left path: (A*0)*B --alpha--> A*(0*B) --A*lam_B--> A*B
       Alam=smap({x:x for x in A}, lam(B), A, star(E,B), A, B)
       lp={x: Alam[a[x]] for x in LHS(A,E,B)}
       # right path: (A*0)*B --rho_A * B--> A*B
       rhoB=smap(rho(A), {x:x for x in B}, star(A,E),B, A,B)
       rp={x: rhoB[x] for x in LHS(A,E,B)}
       assert lp==rp,("triangle",na,nb,lp,rp)
    return True
print("TRIANGLE (maxn=3):", check_triangle(3))

# symmetry braiding beta_{A,B}: A*B -> B*A ; check natural + symmetric + hexagon-lite
def beta(A,B):
    A=tuple(A);B=tuple(B)
    L=star(A,B);R=star(B,A)
    if len(A)==0 and len(B)==0: return {}
    if len(A)==0:  # L: ('R',b); R = star(B,())=('L',b)
        return {('R',b):('L',b) for b in B}
    if len(B)==0:
        return {('L',a):('R',a) for a in A}
    return {PT:PT}
def check_sym(maxn=3):
    for na in range(maxn+1):
     for nb in range(maxn+1):
       A,B=elems(na),elems(nb)
       b1=beta(A,B); b2=beta(B,A)
       comp={x:b2[b1[x]] for x in star(A,B)}
       assert comp=={x:x for x in star(A,B)},("sym involutive",na,nb)
    return True
print("braiding involutive beta_{B,A}o beta_{A,B}=id (maxn=3):", check_sym(3))
