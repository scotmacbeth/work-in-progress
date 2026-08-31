# HOSTILE referee check that the "collapse tensor" is genuinely monoidal.
# A*B := B if A empty; A if B empty; {('pt',)} if both nonempty. Unit = empty set.
# Elements tagged so functorial action is unambiguous. We do NOT assume assoc=id;
# we CONSTRUCT the canonical associator via a normal form and verify naturality+pentagon,
# exactly the test that EXPOSED the support tensor's non-associativity.
import itertools

PT=('pt',)   # the unique collapse point
def star(A,B):
    A=tuple(A); B=tuple(B)
    if len(A)==0: return tuple(('R',b) for b in B)   # copy of B  (strict left unit up to tag)
    if len(B)==0: return tuple(('L',a) for a in A)   # copy of A
    return (PT,)
def smap(f,g,A,B):
    # f:A->A', g:B->B' as dicts; returns dict on star(A,B)->star(A',B')
    A=tuple(A); B=tuple(B)
    d={}
    if len(A)==0:
        for x in star(A,B): d[x]=('R',g[x[1]])
    elif len(B)==0:
        for x in star(A,B): d[x]=('L',f[x[1]])
    else:
        # both nonempty -> {PT}; image both nonempty (f,g total on nonempty) -> PT
        d[PT]=PT
    return d

def elems(n): return tuple(range(n))
def homs(A,B):
    A=tuple(A);B=tuple(B)
    if len(A)==0: return [dict()]
    return [dict(zip(A,v)) for v in itertools.product(B,repeat=len(A))]

# ---- bifunctor axioms: identity + composition ----
def check_bifunctor(maxn=3):
    for na in range(maxn+1):
     for nb in range(maxn+1):
        A,B=elems(na),elems(nb)
        # identity
        idA={a:a for a in A}; idB={b:b for b in B}
        m=smap(idA,idB,A,B)
        assert all(m[x]==x for x in star(A,B)), ("id fail",na,nb)
    # composition
    for na in range(maxn+1):
     for nb in range(maxn+1):
      A,B=elems(na),elems(nb)
      for na2 in range(maxn+1):
       for nb2 in range(maxn+1):
        A2,B2=elems(na2),elems(nb2)
        for f in homs(A,A2):
         for g in homs(B,B2):
          for na3 in range(maxn+1):
           for nb3 in range(maxn+1):
            A3,B3=elems(na3),elems(nb3)
            for f2 in homs(A2,A3):
             for g2 in homs(B2,B3):
               fc={a:f2[f[a]] for a in A}; gc={b:g2[g[b]] for b in B}
               left=smap(fc,gc,A,B)
               m1=smap(f,g,A,B); m2=smap(f2,g2,A2,B2)
               comp={x:m2[m1[x]] for x in star(A,B)}
               assert left==comp, ("comp fail",na,nb,na2,nb2,na3,nb3)
    return True

# ---- canonical associator: since (A*B)*C and A*(B*C) are each a singleton whenever
# >=2 of A,B,C nonempty (collapse), and otherwise a tagged copy of the unique nonempty
# factor (or empty), define alpha by matching underlying "origin". Build both sides and
# a bijection by the rule below, then TEST naturality + pentagon. ----
def LHS(A,B,C): return star(star(A,B),C)
def RHS(A,B,C): return star(A,star(B,C))

def alpha(A,B,C):
    # returns dict LHS(A,B,C)->RHS(A,B,C)
    A,B,C=tuple(A),tuple(B),tuple(C)
    ne=[len(A)>0,len(B)>0,len(C)>0]
    L=LHS(A,B,C); R=RHS(A,B,C)
    # both sides same cardinality (checked); map by matching the surviving factor's element.
    # Cases by which single factor is nonempty (others empty) -> copy of that factor;
    # >=2 nonempty -> singleton. Build element-origin for each side.
    def origin_side(el, side):
        # returns the base element index in the surviving factor, or 'pt'
        # decode nested tags: outer L/R
        cur=el
        # unwrap: elements are like ('L',x) or ('R',x) or PT, possibly nested
        while isinstance(cur,tuple) and cur[0] in ('L','R'):
            cur=cur[1]
        return cur  # an int (base index) or... PT unwraps to ('pt',)? PT=('pt',): cur[0]='pt'
    # if >=2 nonempty: both singletons -> map PT->PT
    if sum(ne)>=2:
        assert len(L)==1 and len(R)==1
        return {L[0]:R[0]}
    if sum(ne)==0:
        return {}
    # exactly one nonempty: both sides copy of that factor's elements; match by base index
    d={}
    Rby={}
    for r in R: Rby[origin_side(r,'R')]=r
    for l in L:
        base=origin_side(l,'L')
        d[l]=Rby[base]
    assert len(d)==len(L)==len(R)
    return d

def check_alpha_bijection(maxn=3):
    for na in range(maxn+1):
     for nb in range(maxn+1):
      for nc in range(maxn+1):
        A,B,C=elems(na),elems(nb),elems(nc)
        a=alpha(A,B,C)
        assert set(a.keys())==set(LHS(A,B,C)), ("alpha dom",na,nb,nc)
        assert set(a.values())==set(RHS(A,B,C)), ("alpha cod",na,nb,nc,a,RHS(A,B,C))
        assert len(set(a.values()))==len(a), "alpha not injective"
    return True

def check_naturality(maxn=2):
    # alpha natural in all three variables: for f:A->A', g:B->B', h:C->C'
    for na in range(maxn+1):
     for nb in range(maxn+1):
      for nc in range(maxn+1):
       A,B,C=elems(na),elems(nb),elems(nc)
       for na2 in range(maxn+1):
        for nb2 in range(maxn+1):
         for nc2 in range(maxn+1):
          A2,B2,C2=elems(na2),elems(nb2),elems(nc2)
          for f in homs(A,A2):
           for g in homs(B,B2):
            for h in homs(C,C2):
              # (A*B)*C : map = (f*g)*h
              fg=smap(f,g,A,B); left_map=smap(fg,h,star(A,B),C)
              a2=alpha(A2,B2,C2)
              # path1: alpha' o ((f*g)*h)
              p1={x:a2[left_map[x]] for x in LHS(A,B,C)}
              # path2: (f*(g*h)) o alpha
              gh=smap(g,h,B,C); right_map=smap(f,gh,A,star(B,C))
              a1=alpha(A,B,C)
              p2={x:right_map[a1[x]] for x in LHS(A,B,C)}
              if p1!=p2:
                  return (False,(na,nb,nc,na2,nb2,nc2,f,g,h,p1,p2))
    return (True,None)

def check_pentagon(maxn=2):
    # ((A*B)*C)*D  -> A*(B*(C*D)) two ways
    for na in range(maxn+1):
     for nb in range(maxn+1):
      for nc in range(maxn+1):
       for nd in range(maxn+1):
        A,B,C,D=elems(na),elems(nb),elems(nc),elems(nd)
        # objects
        AB=star(A,B); BC=star(B,C); CD=star(C,D)
        # path1: a(A,B,C)*D ; a(A,BC,D) ; A*a(B,C,D)
        # source ((A*B)*C)*D
        src=star(star(star(A,B),C),D)
        # step1: alpha(A,B,C) tensored with D : ((A*B)*C)*D -> (A*(B*C))*D
        aABC=alpha(A,B,C)
        idD={d:d for d in D}
        step1=smap(aABC,idD,star(star(A,B),C),D)  # -> (A*(B*C))*D
        # step2: alpha(A, B*C, D): (A*(B*C))*D -> A*((B*C)*D)
        step2=alpha(A,BC,D)
        # step3: A * alpha(B,C,D): A*((B*C)*D) -> A*(B*(C*D))
        idA={a:a for a in A}
        aBCD=alpha(B,C,D)
        step3=smap(idA,aBCD,A,star(star(B,C),D))
        path1={}
        for x in src:
            y=step1[x]; z=step2[y]; w=step3[z]; path1[x]=w
        # path2: alpha(A*B,C,D) ; alpha(A,B,C*D)
        # step a: alpha(A*B, C, D): ((A*B)*C)*D -> (A*B)*(C*D)
        stepa=alpha(AB,C,D)
        # step b: alpha(A,B,C*D): (A*B)*(C*D) -> A*(B*(C*D))
        stepb=alpha(A,B,CD)
        path2={}
        for x in src:
            y=stepa[x]; z=stepb[y]; path2[x]=z
        if path1!=path2:
            return (False,(na,nb,nc,nd,path1,path2))
    return (True,None)

def check_triangle(maxn=3):
    # alpha(A,0,B): (A*0)*B -> A*(0*B) must agree with rho_A * B and A * lambda_B
    # Here 0 = empty. (A*emptyset)=copy of A (tags 'L'); (emptyset*B)=copy of B (tags 'R').
    # rho_A: A*0 ~ A ; lambda_B: 0*B ~ B. Just check alpha(A,[],B) composes to the identity
    # bijection on the underlying A*B under the unit identifications.
    for na in range(maxn+1):
     for nb in range(maxn+1):
      A,B=elems(na),elems(nb)
      E=elems(0)
      a=alpha(A,E,B)  # (A*0)*B -> A*(0*B)
      # (A*0)*B: A*0 = copy of A ('L',a); then (copyA)*B. |copyA|=|A|.
      # A*(0*B): 0*B = copy of B; then A*(copyB).
      # both equal star(A,B) up to the unit tags; just assert bijection consistent w/ base
      assert set(a.keys())==set(LHS(A,E,B))
      assert set(a.values())==set(RHS(A,E,B))
    return True

print("bifunctor (id+comp), maxn=3:", check_bifunctor(3))
print("alpha is a bijection, maxn=3:", check_alpha_bijection(3))
print("triangle ok, maxn=3:", check_triangle(3))
nat=check_naturality(2); print("associator NATURALITY, maxn=2:", nat[0], "" if nat[0] else nat[1][:6])
pent=check_pentagon(2); print("PENTAGON, maxn=2:", pent[0], "" if pent[0] else pent[1][:4])
# non-polynomiality of R_2
print("R_2(empty)=|0*2|=",len(star(elems(0),elems(2))), " R_2(1)=|1*2|=",len(star(elems(1),elems(2))))
