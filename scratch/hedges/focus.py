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
OPS={'ox':tensor,'x':prod,'+':coprod,';':comp}
def has_empty(c): return any(x==0 for x in c)
def morph_exists(X,Y): return (not has_empty(X)) or has_empty(Y)
def src4(R,C,a,b,cc,d): return OPS[R](OPS[C](a,b),OPS[C](cc,d))
def tgt4(R,C,a,b,cc,d): return OPS[C](OPS[R](a,cc),OPS[R](b,d))
CAND=[(0,),(1,),(2,),(0,0),(0,1),(1,0),(1,1),(2,1),(0,2),(1,2)]
def find_noexist(R,C):
    for a in CAND:
     for b in CAND:
      for cc in CAND:
       for d in CAND:
        try: S=src4(R,C,a,b,cc,d); T=tgt4(R,C,a,b,cc,d)
        except: continue
        if not morph_exists(S,T):
            return (a,b,cc,d,S,T)
    return None
for (R,C,label) in [(';','ox','◁ outer / ⊗ inner  (;/⊗)'),
                    ('ox',';','⊗ outer / ◁ inner  (⊗/;)'),
                    ('ox','x','⊗ outer / × inner  (⊗/×)'),
                    ('x','ox','× outer / ⊗ inner  (×/⊗)'),
                    ('+','ox','+ outer / ⊗ inner  (+/⊗)'),
                    ('+',';','+ outer / ◁ inner  (+/;)')]:
    r=find_noexist(R,C)
    if r: print(f"{label:38s}  NO natural map — witness a,b,c,d={r[0]},{r[1]},{r[2]},{r[3]}  src={r[4]} tgt={r[5]}")
    else: print(f"{label:38s}  (pointwise morphism exists at all tested pts — map may exist; naturality TBD)")
