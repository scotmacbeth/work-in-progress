from presheaf import *
from cats import *

def lemmaS_report(C,name,Ps,Ts=(2,)):
    print('='*60); print('BASE',name)
    for pn,P in Ps:
        for k in Ts:
            E=exp(P,const(C,range(k)))
            card=E.card()
            # copower of 1 <=> constant presheaf with identity transitions
            vals=set(card.values())
            isconst = len(vals)==1 and all(
                all(E.act[n][x]==x for x in E.sets[C.arrows[n][1]]) for n in C.arrows)
            # weaker: iso to const(E0)
            n0=list(card.values())[0]
            isoconst = iso(E,const(C,range(n0))) if len(vals)==1 else False
            print(f'  P={pn:12s} T={k}  [P,T.1] cards={card}  copower-of-1? {isoconst}')

print('SET'); lemmaS_report(SET,'Set',[('y(*)',yoneda(SET,'*')),('1',terminal(SET)),
        ('2.1',coprod(terminal(SET),terminal(SET)))])
lemmaS_report(SIERP,'Sierpinski Set^->',[('y(0)',yoneda(SIERP,'0')),('y(1)=1',yoneda(SIERP,'1')),
        ('y0+y1',coprod(yoneda(SIERP,'0'),yoneda(SIERP,'1')))])
lemmaS_report(GRAPH,'Graph = Gl((-)^2)',[('y(V)=vertex',yoneda(GRAPH,'V')),
        ('y(E)=edge',yoneda(GRAPH,'E')),('1=loop',terminal(GRAPH))])
lemmaS_report(Z2,'Z/2-Set',[('y(*)=Z2',yoneda(Z2,'*')),('1',terminal(Z2))])
