from itertools import product, islice
from verify import *

def enum_functions(dom, cod):
    dom=list(dom); cod=list(cod)
    for vals in product(cod, repeat=len(dom)):
        yield dict(zip(dom, vals))

def enum_workers(S, p, q):
    dom_shapes=[(s,a) for s in S for a in p['A']]
    for f in enum_functions(dom_shapes, q['A']):
        spaces=[]; keys=[]
        for (s,a) in dom_shapes:
            c=f[(s,a)]
            spaces.append(list(product(enum_functions(q['B'][c],S), enum_functions(q['B'][c],p['B'][a]))))
            keys.append((s,a))
        for combo in product(*spaces):
            f1={}; f2={}
            for k,(o1,o2) in zip(keys,combo): f1[k]=o1; f2[k]=o2
            yield {'S':list(S),'p':p,'q':q,'f':dict(f),'f1':f1,'f2':f2}

# multi-shape p,q; keep fibres small so enumeration is finite-ish
p = make_container(['a0','a1'], {'a0':['p0'],'a1':['p0','p1']})
q = make_container(['c0','c1'], {'c0':['q0'],'c1':['q0']})   # single positions -> smaller
r = make_container(['e0'], {'e0':['r0','r1']})
S=['s0','s1']; T=['t0','t1']; U=['u0']
z=make_container(['g0'],{'g0':['z0']})

w1s=list(islice(enum_workers(S,p,q),400))
w2s=list(islice(enum_workers(T,q,r),400))
w3s=list(islice(enum_workers(U,r,z),400))
print(f"|w1|<={len(w1s)} |w2|<={len(w2s)} |w3|<={len(w3s)}")
allvalid=True
for w in w1s:
    for wp in w2s:
        dom,cod,f,fsh=worker_as_contmap(compose_workers(w,wp))
        if not is_valid_contmap(dom,cod,f,fsh): allvalid=False; break
    if not allvalid: break
print("multi-shape composites valid:", allvalid)

assoc=True; n=0
for w1 in w1s[::11]:
    for w2 in w2s[::7]:
        for w3 in w3s[::3]:
            L=compose_workers(compose_workers(w1,w2),w3)
            R=compose_workers(w1,compose_workers(w2,w3))
            bij={(u,(t,s)):((u,t),s) for u in U for t in T for s in S}
            if not workers_equal_upto_state_bij(L,R,bij): assoc=False; break
            n+=1
        if not assoc: break
    if not assoc: break
print(f"multi-shape associativity ({n} triples):", assoc)
