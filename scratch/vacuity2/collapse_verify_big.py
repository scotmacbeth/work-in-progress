import itertools
from collapse_verify import (star, Fmap2, all_maps, compose, S, assoc, tens)
from engine import generators, all_morphisms

# objects up to size 4
OBJS=[S(n) for n in range(5)]

# PENTAGON: objects only (no morphisms), sizes up to 4
def pentagon():
    for A in OBJS:
     for B in OBJS:
      for C in OBJS:
       for D in OBJS:
        p1=compose(assoc(A,B,star(C,D)), assoc(star(A,B),C,D))
        idD={x:x for x in D}; idA={x:x for x in A}
        aABC=assoc(A,B,C)
        left=tens(aABC, star(star(A,B),C), star(A,star(B,C)), idD, D, D)
        aBCD=assoc(B,C,D)
        right=tens(idA, A,A, aBCD, star(star(B,C),D), star(B,star(C,D)))
        mid=assoc(A,star(B,C),D)
        p2=compose(right, compose(mid, left))
        if p1!=p2: return False,(A,B,C,D)
    return True,None

# NATURALITY on ALL morphisms among sizes up to 4 (objects 0..4)
def naturality():
    sizes=range(5)
    def maps(a,b):
        A=S(a); B=S(b); return [(A,B,m) for m in all_maps(A,B)]
    for a in sizes:
     for ap in sizes:
      for b in sizes:
       for bp in sizes:
        for c in sizes:
         for cp in sizes:
          A,Ap,B,Bp,C,Cp=map(S,(a,ap,b,bp,c,cp))
          for f in all_maps(A,Ap):
           for g in all_maps(B,Bp):
            for h in all_maps(C,Cp):
                fg=tens(f,A,Ap,g,B,Bp)
                left=tens(fg,star(A,B),star(Ap,Bp),h,C,Cp)
                gh=tens(g,B,Bp,h,C,Cp)
                right=tens(f,A,Ap,gh,star(B,C),star(Bp,Cp))
                lhs=compose(assoc(Ap,Bp,Cp), left)
                rhs=compose(right, assoc(A,B,C))
                if lhs!=rhs: return False,(a,ap,b,bp,c,cp,f,g,h)
    return True,None

print("pentagon up to size 4 (objects):", pentagon())
# naturality full up to size 4 may be big; cap combos by pruning trivial (empty) fast
print("naturality full up to size 3:", end=" ", flush=True)
# reduce to size 3 for full-map naturality to keep runtime sane
def naturality3():
    for a in range(4):
     for ap in range(4):
      for b in range(4):
       for bp in range(4):
        for c in range(4):
         for cp in range(4):
          A,Ap,B,Bp,C,Cp=map(S,(a,ap,b,bp,c,cp))
          for f in all_maps(A,Ap):
           for g in all_maps(B,Bp):
            for h in all_maps(C,Cp):
                fg=tens(f,A,Ap,g,B,Bp)
                left=tens(fg,star(A,B),star(Ap,Bp),h,C,Cp)
                gh=tens(g,B,Bp,h,C,Cp)
                right=tens(f,A,Ap,gh,star(B,C),star(Bp,Cp))
                if compose(assoc(Ap,Bp,Cp),left)!=compose(right,assoc(A,B,C)):
                    return False,(a,ap,b,bp,c,cp)
    return True,None
print(naturality3())
