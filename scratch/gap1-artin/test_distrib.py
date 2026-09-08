from presheaf import *
from psh2 import *
from cats import *

def maps_to_copower(P,k):
    return nat_bt(P,const(P.cat,range(k)))

def restrict(P,d,i):
    C=P.cat
    sets={c:tuple(x for x in P.sets[c] if d[c][x]==i) for c in C.objs}
    act={n:{x:P.act[n][x] for x in sets[C.arrows[n][1]]} for n in C.arrows}
    Q=PSh(C,sets,act); Q.check(); return Q

def prod_many(C,Xs):
    R=terminal(C)
    for X in Xs: R=prod(R,X)
    return R

def distrib_test(C,name,P,Ys):
    k=len(Ys)
    LHS=exp2(P,coprod_many(C,Ys))
    parts=[prod_many(C,[exp2(restrict(P,d,i),Ys[i]) for i in range(k)])
           for d in maps_to_copower(P,k)]
    RHS=coprod_many(C,parts)
    ok=iso_bt(LHS,RHS)
    print(f'  {name}: |Hom(P,{k}.1)|={len(parts)}  LHS={LHS.card()}  RHS={RHS.card()}  ISO={ok}')
    return ok

print('--- SET ---')
one=terminal(SET); two=coprod(one,one)
distrib_test(SET,'P=2 Y=(1,1)',two,[one,one])
distrib_test(SET,'P=2 Y=(2,1)',two,[two,one])

print('--- SIERPINSKI (Lemma S HOLDS) ---')
y0,y1=yoneda(SIERP,'0'),yoneda(SIERP,'1')
for pn,P in [('y0',y0),('y1=1',y1),('y0+y1',coprod(y0,y1)),('y0+y0',coprod(y0,y0))]:
    for yn,Ys in [('(1,1)',[terminal(SIERP)]*2),('(y0,y1)',[y0,y1]),('(y0,y0)',[y0,y0])]:
        distrib_test(SIERP,f'P={pn} Y={yn}',P,Ys)

print('--- GRAPH (Lemma S FAILS) ---')
for pn,P in [('y(V)',yoneda(GRAPH,'V')),('y(E)',yoneda(GRAPH,'E')),('1',terminal(GRAPH))]:
    distrib_test(GRAPH,f'P={pn} Y=(1,1)',P,[terminal(GRAPH)]*2)

print('--- Z/2-Set (Lemma S FAILS) ---')
for pn,P in [('y(*)',yoneda(Z2,'*')),('1',terminal(Z2))]:
    distrib_test(Z2,f'P={pn} Y=(1,1)',P,[terminal(Z2)]*2)
