"""
INDEPENDENT concrete verification of the 'collapse tensor' on FinSet:
    A*B = B        if A = empty      (unit on the left)
        = A        if B = empty      (unit on the right)
        = {PT}     if A,B both nonempty      (collapse to a fixed point)
Unit I = empty set.
Claim under test: is this a genuine (non-symmetric ok) monoidal category, i.e.
does a natural associator satisfying pentagon+triangle exist?  If yes, R_2 is a
NON-polynomial functor and we have a real counterexample.

Sets are python frozensets of labels.  Morphisms are dicts {x:y}.  We verify by
brute force over all morphisms among small finite sets.
"""
import itertools

PT = ('*',)                     # the collapse point

def star(A,B):
    A=frozenset(A); B=frozenset(B)
    if not A: return B
    if not B: return A
    return frozenset({PT})

def Fmap(f,g,A,B):
    """action of (f:A->A', g:B->B') on A*B -> A'*B'. f,g dicts."""
    A=frozenset(A); B=frozenset(B)
    Ap=frozenset(f.values()) if A else frozenset()   # careful: codomain not fully known from values
    # We must pass codomains explicitly; do it via closure over provided cod.
    raise RuntimeError("use Fmap2")

def Fmap2(f,A,Ap,g,B,Bp):
    """(f:A->Ap, g:B->Bp) acting on star(A,B) -> star(Ap,Bp). Returns dict."""
    A,Ap,B,Bp=map(frozenset,(A,Ap,B,Bp))
    dom=star(A,B); cod=star(Ap,Bp)
    res={}
    if not Ap and not Bp:
        # both codomain empty => A,B empty => dom empty
        return {}
    if not Ap:                  # Ap empty => A empty => dom = B, and cod = star(empty,Bp)=Bp
        # map is g
        for x in dom: res[x]=g[x]
        return res
    if not Bp:                  # Bp empty => B empty => dom = A, cod = Ap
        for x in dom: res[x]=f[x]
        return res
    # Ap,Bp both nonempty => cod = {PT}
    for x in dom: res[x]=PT
    return res

def all_maps(A,B):
    A=list(A); B=list(B)
    if not A: return [dict()]
    if not B: return []
    out=[]
    for vals in itertools.product(B,repeat=len(A)):
        out.append({A[i]:vals[i] for i in range(len(A))})
    return out

def compose(g,f):   # g after f
    return {x:g[f[x]] for x in f}

def S(n):  # standard set of size n
    return frozenset(range(n)) if n>0 else frozenset()

OBJS=[S(n) for n in range(3)]     # empty,1,2  (bump range for larger checks)

# ---- associator: star(star(A,B),C) -> star(A,star(B,C)) ----
# Build the CANONICAL associator: both sides are (as sets) determined; define the
# unique 'obvious' bijection. We derive it structurally:
def assoc(A,B,C):
    A,B,C=map(frozenset,(A,B,C))
    L=star(star(A,B),C); R=star(A,star(B,C))
    # Case analysis mirrors the definition.
    # If A empty: L=star(B,C), R=star(B,C) -> identity
    if not A: return {x:x for x in L}
    # A nonempty. If B empty: star(A,B)=A ; L=star(A,C). R=star(A,star(empty,C))=star(A,C). id
    if not B: return {x:x for x in L}
    # A,B nonempty: star(A,B)={PT}. If C empty: L=star({PT},empty)={PT}; R=star(A,star(B,empty))=star(A,B)={PT}. id on PT.
    if not C:
        # L={PT}, R={PT}
        return {x:x for x in L}
    # A,B,C all nonempty: L=star({PT},C)={PT}; R=star(A,{PT})={PT}. bijection PT->PT
    return {x:x for x in L}     # both {PT}

# sanity: assoc is a bijection L->R
def check_assoc_bijections():
    for A in OBJS:
        for B in OBJS:
            for C in OBJS:
                al=assoc(A,B,C)
                L=star(star(A,B),C); R=star(A,star(B,C))
                assert set(al.keys())==set(L), (A,B,C,'dom')
                assert set(al.values())==set(R), (A,B,C,'cod',al,R)
                assert len(set(al.values()))==len(al), (A,B,C,'not inj')
    return True

# ---- functoriality of the bifunctor ----
def check_functor():
    for A in OBJS:
     for Ap in OBJS:
      for App in OBJS:
       for B in OBJS:
        for Bp in OBJS:
         for Bpp in OBJS:
          for f in all_maps(A,Ap):
           for f2 in all_maps(Ap,App):
            for g in all_maps(B,Bp):
             for g2 in all_maps(Bp,Bpp):
                lhs=Fmap2(compose(f2,f),A,App,compose(g2,g),B,Bpp)
                rhs=compose(Fmap2(f2,Ap,App,g2,Bp,Bpp), Fmap2(f,A,Ap,g,B,Bp))
                if lhs!=rhs:
                    return False,(A,Ap,App,B,Bp,Bpp,f,f2,g,g2,lhs,rhs)
    # identity
    for A in OBJS:
     for B in OBJS:
        idA={x:x for x in A}; idB={x:x for x in B}
        m=Fmap2(idA,A,A,idB,B,B)
        if m!={x:x for x in star(A,B)}: return False,('id',A,B,m)
    return True,None

# ---- tensor of two morphisms as a single morphism between star-objects ----
def tens(f,A,Ap,g,B,Bp):
    return Fmap2(f,A,Ap,g,B,Bp)   # dict star(A,B)->star(Ap,Bp)

# ---- naturality of associator ----
def check_nat():
    for A in OBJS:
     for Ap in OBJS:
      for B in OBJS:
       for Bp in OBJS:
        for C in OBJS:
         for Cp in OBJS:
          for f in all_maps(A,Ap):
           for g in all_maps(B,Bp):
            for h in all_maps(C,Cp):
                # (f*g)*h : star(star(A,B),C) -> star(star(Ap,Bp),Cp)
                fg=tens(f,A,Ap,g,B,Bp)           # star(A,B)->star(Ap,Bp)
                left_mor=tens(fg,star(A,B),star(Ap,Bp),h,C,Cp)
                # f*(g*h)
                gh=tens(g,B,Bp,h,C,Cp)
                right_mor=tens(f,A,Ap,gh,star(B,C),star(Bp,Cp))
                lhs=compose(assoc(Ap,Bp,Cp), left_mor)
                rhs=compose(right_mor, assoc(A,B,C))
                if lhs!=rhs:
                    return False,(A,Ap,B,Bp,C,Cp,f,g,h,lhs,rhs)
    return True,None

# ---- pentagon ----
def check_pentagon():
    for A in OBJS:
     for B in OBJS:
      for C in OBJS:
       for D in OBJS:
        # ((AB)C)D
        # path1: a_{AB,C,D} ; a_{A,B,CD}
        p1=compose(assoc(A,B,star(C,D)), assoc(star(A,B),C,D))
        # path2: (a_{A,B,C} * id_D) ; a_{A,BC,D} ; (id_A * a_{B,C,D})
        idD={x:x for x in D}; idA={x:x for x in A}
        aABC=assoc(A,B,C)                       # star(star(A,B),C)->star(A,star(B,C))
        left=tens(aABC, star(star(A,B),C), star(A,star(B,C)), idD, D, D)
        aBCD=assoc(B,C,D)
        right=tens(idA, A,A, aBCD, star(star(B,C),D), star(B,star(C,D)))
        mid=assoc(A,star(B,C),D)
        p2=compose(right, compose(mid, left))
        if p1!=p2:
            return False,(A,B,C,D,p1,p2)
    return True,None

# ---- triangle (strict unit I=empty): a_{A,I,B} should be identity, and unitors id ----
def check_triangle():
    I=S(0)
    for A in OBJS:
     for B in OBJS:
        a=assoc(A,I,B)
        # star(star(A,I),B)=star(A,B); star(A,star(I,B))=star(A,B); expect identity
        if a!={x:x for x in star(A,B)}:
            return False,(A,B,a)
    return True,None

# ---- unit: I=empty is strict two-sided unit at object AND morphism level ----
def check_unit():
    I=S(0)
    for A in OBJS:
     for Ap in OBJS:
      for f in all_maps(A,Ap):
        idI={}
        # I*A = A ; I*f = f
        if tens(idI,I,I,f,A,Ap)!=f: return False,('left',A,Ap,f)
        if tens(f,A,Ap,idI,I,I)!=f: return False,('right',A,Ap,f)
    return True,None

if __name__=="__main__":
    print("assoc bijections:", check_assoc_bijections())
    fo=check_functor();   print("bifunctoriality:", fo[0], "" if fo[0] else fo[1])
    un=check_unit();      print("strict unit    :", un[0], "" if un[0] else un[1])
    tr=check_triangle();  print("triangle       :", tr[0], "" if tr[0] else tr[1])
    na=check_nat();       print("assoc natural  :", na[0], "" if na[0] else na[1])
    pe=check_pentagon();  print("pentagon       :", pe[0], "" if pe[0] else pe[1])
