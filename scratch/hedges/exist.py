from itertools import product as iproduct
def tensor(p,q): return tuple(a*b for a in p for b in q)
def prod(p,q):   return tuple(a+b for a in p for b in q)
def coprod(p,q): return tuple(p)+tuple(q)
def comp(p,q):
    Sq=len(q); out=[]
    for a in p:
        for f in iproduct(range(Sq),repeat=a):
            out.append(sum(q[f[i]] for i in range(a)))
    return tuple(out)
OPS={'ox':tensor,'x':prod,'+':coprod,';':comp}; NM={'ox':'⊗','x':'×','+':'+',';':'◁'}
def has_empty(c): return any(x==0 for x in c)
def morph_exists(X,Y):        # ∃ container morphism X->Y ?
    return (not has_empty(X)) or has_empty(Y)
# 4-ary duoidal interchanger, R outer / C inner: src=(aCb)R(cCd) -> tgt=(aRc)C(bRd)
def src4(R,C,a,b,cc,d): return OPS[R](OPS[C](a,b),OPS[C](cc,d))
def tgt4(R,C,a,b,cc,d): return OPS[C](OPS[R](a,cc),OPS[R](b,d))
# candidate small containers (lists of position-cardinalities), keep tiny for ◁
CANDS=[(0,),(1,),(2,),(0,1),(1,1),(2,0),(1,0)]
def analyze(R,C):
    noexist=None; iso_all=True; seen=0
    for a in CANDS:
     for b in CANDS:
      for cc in CANDS:
       for d in CANDS:
        try:
            S=src4(R,C,a,b,cc,d); T=tgt4(R,C,a,b,cc,d)
        except Exception: continue
        seen+=1
        if sorted(S)!=sorted(T): iso_all=False
        if not morph_exists(S,T) and noexist is None:
            noexist=(a,b,cc,d,S,T)
    return noexist, iso_all
print("4-ary interchanger  R outer / C inner  (C = the tensor column):")
print(f"{'R\\C':>4}", *[f"{NM[C]:>26}" for C in OPS])
for R in OPS:
    cells=[]
    for C in OPS:
        ne,iso=analyze(R,C)
        if ne: v=f"NO-MAP@{ne[0]}{ne[1]}{ne[2]}{ne[3]}"
        elif iso: v="D(iso)?"
        else: v="map-ok,lax?"
        cells.append(v)
    print(f"{NM[R]:>4}", *[f"{x:>26}" for x in cells])
