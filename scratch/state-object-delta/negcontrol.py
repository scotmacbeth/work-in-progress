from verify import make_container, Delta, tensor
def product(p,q):  # Day of +
    A=[(a,c) for a in p['A'] for c in q['A']]
    B={(a,c): [('L',x) for x in p['B'][a]]+[('R',y) for y in q['B'][c]] for (a,c) in A}
    return make_container(A,B)
S=['a','b']; T=['0','1','2']
dt=tensor(Delta(S),Delta(T)); dp=product(Delta(S),Delta(T))
prof=lambda c:(len(c['A']),sorted(len(c['B'][a]) for a in c['A']))
print("ΔS⊗ΔT fibres (Dirichlet):", prof(dt), " -> Δ(S×T) has |S×T|=",len(S)*len(T))
print("ΔS×ΔT fibres (product):  ", prof(dp), " (=|S|+|T|=",len(S)+len(T),") NOT Δ(S×T)")
