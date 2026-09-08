from presheaf import *
from psh2 import *
from cats import *

def pi0(X):
    """colim_{D^op} X : quotient of disjoint union of X(c) by x ~ X(n)(x)."""
    C=X.cat
    par={(c,x):(c,x) for c in C.objs for x in X.sets[c]}
    def find(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    def uni(a,b):
        a,b=find(a),find(b)
        if a!=b: par[a]=b
    for n,(a,b) in C.arrows.items():
        for x in X.sets[b]: uni((a,X.act[n][x]),(b,x))
    return sorted({find(k) for k in par},key=repr), find

def pi0_preserves_products(C,name,objs):
    print('  BASE',name)
    bad=0
    for na,A in objs:
        for nb,B in objs:
            pa,_=pi0(A); pb,_=pi0(B); pab,_=pi0(prod(A,B))
            flag='' if len(pab)==len(pa)*len(pb) else '   <-- FAILS'
            if flag: bad+=1
            print(f'    |pi0({na} x {nb})|={len(pab)} vs |pi0|*|pi0|={len(pa)*len(pb)}{flag}')
    return bad

# monoid with absorbing idempotent: M={1,e}, e*e=e
IDEM=Cat(['*'],{'id_*':('*','*'),'e':('*','*')},
         {('id_*','id_*'):'id_*',('id_*','e'):'e',('e','id_*'):'e',('e','e'):'e'})

for nm,C in [('Set',SET),('Sierpinski',SIERP),('Graph',GRAPH),('Z/2-Set',Z2),('Idem-Set',IDEM)]:
    objs=[('y(%s)'%d,yoneda(C,d)) for d in C.objs]+[('1',terminal(C))]
    pi0_preserves_products(C,nm,objs)

print()
print('Lemma S / distributivity for Idem-Set:')
def maps_to_copower(P,k): return nat_bt(P,const(P.cat,range(k)))
def restrict(P,d,i):
    C=P.cat
    sets={c:tuple(x for x in P.sets[c] if d[c][x]==i) for c in C.objs}
    act={n:{x:P.act[n][x] for x in sets[C.arrows[n][1]]} for n in C.arrows}
    return PSh(C,sets,act)
def prod_many(C,Xs):
    R=terminal(C)
    for X in Xs: R=prod(R,X)
    return R
for pn,P in [('y(*)',yoneda(IDEM,'*')),('1',terminal(IDEM)),('y+y',coprod(yoneda(IDEM,'*'),yoneda(IDEM,'*')))]:
    E=exp2(P,const(IDEM,range(2))); n0=list(E.card().values())[0]
    print(f'  [P={pn},2.1] card={E.card()} copower? {iso_bt(E,const(IDEM,range(n0)))}')
    Ys=[terminal(IDEM)]*2
    LHS=exp2(P,coprod_many(IDEM,Ys))
    RHS=coprod_many(IDEM,[prod_many(IDEM,[exp2(restrict(P,d,i),Ys[i]) for i in range(2)]) for d in maps_to_copower(P,2)])
    print(f'    distributivity: LHS={LHS.card()} RHS={RHS.card()} ISO={iso_bt(LHS,RHS)}')
