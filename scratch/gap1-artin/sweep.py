import random
from presheaf import *
from psh2 import *
from cats import *
from refl import RGRAPH

IDEM=Cat(['*'],{'id_*':('*','*'),'e':('*','*')},
         {('id_*','id_*'):'id_*',('id_*','e'):'e',('e','id_*'):'e',('e','e'):'e'})

def rand_psh(C,maxn=3,rng=random):
    while True:
        sets={c:tuple(range(rng.randint(0,maxn))) for c in C.objs}
        act={}
        gens=[n for n in C.arrows if not n.startswith('id_')]
        # build by choosing images for generators then check functoriality; retry on failure
        for n in C.arrows:
            d,c=C.arrows[n]
            if n.startswith('id_'): act[n]={x:x for x in sets[c]}
            else:
                if len(sets[d])==0 and len(sets[c])>0: break
                act[n]={x:rng.choice(sets[d]) for x in sets[c]} if sets[c] else {}
        else:
            X=PSh(C,sets,act)
            try:
                X.check(); return X
            except AssertionError: pass

def lemmaS(X,T=2):
    C=X.cat
    E=exp2(X,const(C,range(T)))
    card=list(E.card().values())
    if len(set(card))!=1: return False,E.card()
    return iso_bt(E,const(C,range(card[0]))), E.card()

random.seed(7)
for nm,C in [('Sierpinski',SIERP),('Idem-Set',IDEM),('RGraph',RGRAPH),('Graph',GRAPH),('Z/2-Set',Z2)]:
    ok=bad=0; ex=None
    for _ in range(30):
        X=rand_psh(C,2)
        try: r,card=lemmaS(X,2)
        except Exception as e: continue
        if r: ok+=1
        else:
            bad+=1
            if ex is None: ex=(X.card(),card)
    print(f'{nm:12s}  LemmaS holds {ok}/{ok+bad}   first failure (|P|,|[P,2.1]|) = {ex}')
