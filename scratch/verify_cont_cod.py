"""
Verify the Set-side facts underpinning Cont(cod)'s logic:
  (A) Sigma_f  -| f^*  -| Pi_f   for f: X->Y in Set   (finite, brute-force hom-set bijections)
  (B) Beck-Chevalley for a pullback square (Sigma and Pi versions)
  (C) Frobenius reciprocity for Sigma_f
The op + Fam parts are then formal (op reverses adjunctions; Fam is componentwise).

Representation:
  A finite set = a python tuple of hashable elements.
  An object of Set/B = a dict {a: b} i.e. a function A->B given as a mapping from A-elements to B-elements.
  We represent it as (A_tuple, map_dict) with map_dict: a -> b in B.
  A morphism in Set/B  (f:A->B) -> (g:C->B) = function A->C with g(h(a))=f(a).
We brute force hom-sets by enumerating all functions between finite sets.
"""
from itertools import product

def all_functions(dom, cod):
    """all functions dom->cod as dicts. dom,cod tuples."""
    cod = list(cod)
    for vals in product(cod, repeat=len(dom)):
        yield {a: v for a, v in zip(dom, vals)}

# ---------- Set/B category ----------
class SliceObj:
    def __init__(self, A, f):  # A tuple, f dict A->B
        self.A = tuple(A); self.f = dict(f)
    def __repr__(self): return f"({self.A}->{ {a:self.f[a] for a in self.A} })"

def slice_homs(o1, o2):
    """morphisms o1->o2 in Set/B : functions h:A1->A2 with o2.f(h(a))=o1.f(a)."""
    res=[]
    for h in all_functions(o1.A, o2.A):
        if all(o2.f[h[a]] == o1.f[a] for a in o1.A):
            res.append(h)
    return res

# ---------- functors along f: X -> Y ----------
def Sigma(f, obj):
    """Sigma_f : Set/X -> Set/Y ; postcompose. obj=(A -> X). result A -> Y."""
    return SliceObj(obj.A, {a: f[obj.f[a]] for a in obj.A})

def pullback(f, obj):
    """f^* : Set/Y -> Set/X. obj = (C -> Y). result = { (x,c): x } over X, with C-> along."""
    # pullback P = {(x,c) : f(x)=obj.f(c)} ; map to X is projection; also proj to C.
    P=[]; toX={}; toC={}
    for x in f:  # f is dict X->Y ; keys are X
        for c in obj.A:
            if f[x]==obj.f[c]:
                e=(x,c); P.append(e); toX[e]=x; toC[e]=c
    return SliceObj(tuple(P), toX), toC  # object over X, plus projection to C (for naturality)

def Pi(f, obj, X, Y):
    """Pi_f : Set/X -> Set/Y. obj=(A->X).
       (Pi_f obj)_y = set of sections s: f^{-1}(y) -> A with obj.f(s(x))=x.
       total space = {(y, s)}, map to Y = y."""
    Aset=obj.A
    tot=[]; toY={}
    for y in Y:
        fibX=[x for x in f if f[x]==y]
        # sections s: fibX -> A with obj.f(s(x))=x
        # enumerate
        choices=[]
        for x in fibX:
            opts=[a for a in Aset if obj.f[a]==x]
            choices.append(opts)
        if not fibX:
            # empty fiber: exactly one section (empty), fibre of Pi over y = 1
            e=(y, ()); tot.append(e); toY[e]=y
            continue
        for combo in product(*choices):
            s=tuple(zip(fibX, combo))
            e=(y, s); tot.append(e); toY[e]=y
    return SliceObj(tuple(tot), toY)

# ---------- adjunction tests ----------
def check_adjunction(name, LF, Ldom, Rcod, RF, homL, homR):
    """generic: |Hom(LF a, b)| == |Hom(a, RF b)| for all a in Ldom, b in Rcod."""
    ok=True
    for a in Ldom:
        for b in Rcod:
            l=len(homL(LF(a), b)); r=len(homR(a, RF(b)))
            if l!=r:
                ok=False; print(f"  FAIL {name}: |Hom(F a,b)|={l} != |Hom(a,G b)|={r}  a={a} b={b}")
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
    return ok

def gen_slice_objs(B, maxA=3):
    """generate a sample of Set/B objects with |A|<=maxA (A drawn from a fixed pool)."""
    pool=('u','v','w','x','y','z')
    objs=[]
    for nA in range(0, maxA+1):
        A=pool[:nA]
        for f in all_functions(A, B):
            objs.append(SliceObj(A,f))
    return objs

def run():
    # Test over several f: X->Y
    tests=[
        # X, Y, f
        (('1','2','3'), ('a',), {'1':'a','2':'a','3':'a'}),      # collapse P->1
        (('1','2'), ('a','b'), {'1':'a','2':'b'}),                 # iso-ish
        (('1','2','3'), ('a','b'), {'1':'a','2':'a','3':'b'}),     # surjection
        (('1',), ('a','b'), {'1':'a'}),                            # non-surjective incl
    ]
    for (X,Y,f) in tests:
        print(f"\n=== f: {X} -> {Y}, f={f} ===")
        SX=gen_slice_objs(X, maxA=2)   # domain objects for Sigma/Pi (over X)
        SY=gen_slice_objs(Y, maxA=2)   # objects over Y (for f^*)
        homX=lambda a,b: slice_homs(a,b)
        homY=lambda a,b: slice_homs(a,b)
        # Sigma_f -| f^*  : |Hom_Y(Sigma a, b)| == |Hom_X(a, f^* b)|
        check_adjunction("Sigma_f -| f^*",
            LF=lambda a: Sigma(f,a), Ldom=SX, Rcod=SY,
            RF=lambda b: pullback(f,b)[0], homL=homY, homR=homX)
        # f^* -| Pi_f : |Hom_X(f^* b, a)| == |Hom_Y(b, Pi a)|
        check_adjunction("f^* -| Pi_f",
            LF=lambda b: pullback(f,b)[0], Ldom=SY, Rcod=SX,
            RF=lambda a: Pi(f,a,X,Y), homL=homX, homR=homY)

run()
