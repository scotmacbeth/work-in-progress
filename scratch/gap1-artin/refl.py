from presheaf import *
from psh2 import *
from cats import *

# Delta_{<=1}: objects V=[0], E=[1]; s,t:V->E (faces), r:E->V (degeneracy), rs=rt=id_V
arrows={'id_V':('V','V'),'id_E':('E','E'),'s':('V','E'),'t':('V','E'),'r':('E','V'),
        'sr':('E','E'),'tr':('E','E')}
comp={}
def setc(g,f,gf): comp[(g,f)]=gf
for n,(d,c) in arrows.items(): setc('id_'+c,n,n); setc(n,'id_'+d,n)
setc('r','s','id_V'); setc('r','t','id_V')
setc('s','r','sr');   setc('t','r','tr')
setc('sr','sr','sr'); setc('sr','tr','sr'); setc('tr','sr','tr'); setc('tr','tr','tr')
setc('sr','s','s');   setc('sr','t','s');   setc('tr','s','t');   setc('tr','t','t')
setc('r','sr','r');   setc('r','tr','r')
RGRAPH=Cat(['V','E'],arrows,comp)

def pi0(X):
    C=X.cat
    par={(c,x):(c,x) for c in C.objs for x in X.sets[c]}
    def find(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    for n,(a,b) in C.arrows.items():
        for x in X.sets[b]:
            u,v=find((a,X.act[n][x])),find((b,x))
            if u!=v: par[u]=v
    return len({find(k) for k in par})

print('REFLEXIVE GRAPHS  D = Delta_{<=1}')
objs=[('y(V)',yoneda(RGRAPH,'V')),('y(E)',yoneda(RGRAPH,'E')),('1',terminal(RGRAPH))]
for na,A in objs:
    for nb,B in objs:
        a,b,ab=pi0(A),pi0(B),pi0(prod(A,B))
        print(f'  |pi0({na} x {nb})|={ab}  vs {a}*{b}={a*b}  {"OK" if ab==a*b else "FAILS"}')
for na,P in objs:
    E=exp2(P,const(RGRAPH,range(2))); n0=list(E.card().values())[0]
    same=len(set(E.card().values()))==1
    print(f'  [P={na}, 2.1] = {E.card()}  copower-of-1? {same and iso_bt(E,const(RGRAPH,range(n0)))}')
