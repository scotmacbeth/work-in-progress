"""
Literal request: brute-force CLOSED multiplication tables m[a][b] on X={0,1,2,3}
(values in X), symmetric, with a two-sided unit e, and associative
m[m[a][b]][c]=m[a][m[b][c]]. For each solution report the 'arity signature':
for each column b, does m[.,b] fit a polynomial (nonneg int coeffs) of degree>=2?
(detected via 2nd finite difference on 0,1,2,3).

Point: a genuine arity-2 column grows like x^2 and cannot stay inside {0,1,2,3},
so a closed finite table cannot witness arity>=2. We confirm by exhaustion.
"""
import itertools

N=4  # X={0,1,2,3}
X=range(N)

def is_unit(m,e):
    return all(m[e][b]==b and m[b][e]==b for b in X)

def assoc(m):
    for a in X:
        for b in X:
            ab=m[a][b]
            for c in X:
                if m[ab][c]!=m[a][m[b][c]]:
                    return False
    return True

def col_arity_ge2(m,b):
    v=[m[a][b] for a in X]  # x=0,1,2,3
    d2=[v[i+2]-2*v[i+1]+v[i] for i in range(2)]
    return any(d>0 for d in d2), v

def gen_symmetric():
    # upper triangle entries a<=b, each in X
    pairs=[(a,b) for a in X for b in range(a,N)]
    for vals in itertools.product(X, repeat=len(pairs)):
        m=[[0]*N for _ in range(N)]
        for (k,(a,b)) in enumerate(pairs):
            m[a][b]=vals[k]; m[b][a]=vals[k]
        yield m

if __name__=="__main__":
    total=0; withunit=0; sols=[]
    for m in gen_symmetric():
        # need some unit
        es=[e for e in X if is_unit(m,e)]
        if not es: continue
        withunit+=1
        if not assoc(m): continue
        sols.append((m,es[0]))
    print(f"symmetric+unit+associative closed tables on |X|=4: {len(sols)}")
    anyar2=False
    arity_hist={}
    for m,e in sols:
        maxd2=0
        for b in X:
            ge2,v=col_arity_ge2(m,b)
            if ge2: anyar2=True
        # classify by formula type: check if m[a][b]==a*b (mod stays in range) etc
    print("ANY closed table with an arity>=2 column:", anyar2)
    # show a few example tables + identify product/coproduct/vee among them
    def classify(m,e):
        if all(m[a][b]==(a*b if a*b<N else None) for a in X for b in X):
            pass
        # test formulas
        forms={
          'product a*b': lambda a,b:a*b,
          'coproduct a+b': lambda a,b:a+b,
        }
        for s in range(0,4):
            forms[f'vee_{s} a+b+{s}ab']=(lambda a,b,s=s:a+b+s*a*b)
        hits=[name for name,f in forms.items() if all(m[a][b]==f(a,b) for a in X for b in X if f(a,b)<N) and all(f(a,b)<N or True for a in X for b in X)]
        # only exact if fully matches within range
        exact=[name for name,f in forms.items() if all(m[a][b]==f(a,b) for a in X for b in X if 0<=f(a,b)<N) ]
        return exact
    seenforms={}
    for m,e in sols:
        c=tuple(tuple(r) for r in m)
        cl=classify(m,e)
        key=cl[0] if cl else "other"
        seenforms[key]=seenforms.get(key,0)+1
    print("rough classification (within-range formula match):", seenforms)
