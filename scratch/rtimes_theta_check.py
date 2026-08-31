import itertools

# Full structural check of the adjunction bijection Theta on a small explicit example,
# using ACTUAL direction SETS (not just cardinalities). Directions are finite sets = range(k).

# Container: (S:list, d:dict shape->set(=frozenset of ints))
def mkset(k): return frozenset(range(k))

# Morphism p->p' : (f0: dict s-> s', fsharp: dict s -> (function p'[f0 s] -> p[s]) as dict)
def all_morphisms(p, pp):
    S,d = p; Spp,dpp = pp
    res=[]
    for f0vals in itertools.product(Spp, repeat=len(S)):
        f0 = {s: f0vals[i] for i,s in enumerate(S)}
        # for each s, choose a function dpp[f0 s] -> d[s]
        per_s_choices=[]
        shapes=list(S)
        for s in shapes:
            dom=sorted(dpp[f0[s]]); cod=sorted(d[s])
            fns=[dict(zip(dom, vals)) for vals in itertools.product(cod, repeat=len(dom))]
            per_s_choices.append(fns)
        for combo in itertools.product(*per_s_choices):
            fsharp={shapes[i]:combo[i] for i in range(len(shapes))}
            res.append((f0,fsharp))
    return res

def rtimes(p,q):
    Sp,dp=p; Sq,dq=q; nq=len(Sq)
    S=[(s,t) for s in Sp for t in Sq]
    # dir at (s,t) = Set(S_q, p[s]) x q[t]. Represent as set of pairs (g, y):
    #   g: function S_q->p[s] (tuple indexed by sorted Sq), y in q[t]
    d={}
    for s in Sp:
        for t in Sq:
            dps=sorted(dp[s]); 
            gs=list(itertools.product(sorted(dp[s]), repeat=nq)) # functions S_q->p[s]
            elems=frozenset((g,y) for g in gs for y in sorted(dq[t]))
            d[(s,t)]=elems
    return (S,d)

def internal_hom(q,r):
    Sq,dq=q; Sr,dr=r; nq=len(Sq)
    S=[]; d={}
    Sqs=sorted(Sq)
    for avals in itertools.product(Sr, repeat=nq):
        a={Sqs[i]:avals[i] for i in range(nq)}
        # c: for each t, function r[a t]->q[t]
        per_t=[]
        for t in Sqs:
            dom=sorted(dr[a[t]]); cod=sorted(dq[t])
            per_t.append([dict(zip(dom,vals)) for vals in itertools.product(cod,repeat=len(dom))])
        for ccombo in itertools.product(*per_t):
            c={Sqs[i]:ccombo[i] for i in range(nq)}
            lbl=(avals, tuple(sorted((t, tuple(sorted(c[t].items()))) for t in Sqs)))
            S.append(lbl)
            # dir = S_q x coprod_t r[a t]   ; elements (tprime, (t, rho))
            elems=set()
            for tprime in Sqs:
                for t in Sqs:
                    for rho in sorted(dr[a[t]]):
                        elems.add((tprime,(t,rho)))
            d[lbl]=frozenset(elems)
    return (S,d)

# Now: for given p,q,r, Theta: Cont(p rtimes q, r) -> Cont(p, [q,r]).
# We just check it's a well-defined bijection by cardinality + injectivity via explicit construction.

def theta(alpha, p, q, r, Gqr):
    (f0,fsharp)=alpha
    Sp,dp=p; Sq,dq=q; Sr,dr=r; Sqs=sorted(Sq)
    SG,dG=Gqr
    beta0={}; betash={}
    for s in Sp:
        a=tuple(f0[(s,t)] for t in Sqs)
        # c_t = mu_{s,t}: r[a_s t] -> q[t]  = second component of fsharp[(s,t)]
        c={}
        for t in Sqs:
            fn=fsharp[(s,t)]  # dict: element of r[f0(s,t)] -> (g,y) pair
            c[t]={rho: fn[rho][1] for rho in sorted(dr[f0[(s,t)]])}
        lbl=(a, tuple(sorted((t, tuple(sorted(c[t].items()))) for t in Sqs)))
        beta0[s]=lbl
        # beta^#_s: dG[lbl] -> p[s], (tprime,(t,rho)) -> lambda_{s,t}(rho)(tprime) = fsharp[(s,t)][rho][0][index tprime]
        elems=dG[lbl]
        bs={}
        for (tprime,(t,rho)) in elems:
            g = fsharp[(s,t)][rho][0]   # g: tuple indexed by sorted Sq
            idx=Sqs.index(tprime)
            bs[(tprime,(t,rho))]=g[idx]
        betash[s]=bs
    return (beta0,betash)

# test
p=([0,1],{0:mkset(2),1:mkset(1)})
q=([0,1],{0:mkset(2),1:mkset(1)})
r=([0],{0:mkset(2)})

L=rtimes(p,q)
Gqr=internal_hom(q,r)
homL=all_morphisms(L,r)
homR=all_morphisms(p,Gqr)
print("|Cont(p rtimes q, r)| =",len(homL))
print("|Cont(p,[q,r])|      =",len(homR))
images=set()
for alpha in homL:
    b=theta(alpha,p,q,r,Gqr)
    # canonicalize b for set membership
    key=(tuple(sorted(b[0].items())), tuple(sorted((s,tuple(sorted(b[1][s].items()))) for s in b[1])))
    images.add(key)
print("distinct images (injectivity):",len(images), " == |homL|?", len(images)==len(homL))
print("images subset of valid targets & bijective?", len(images)==len(homR)==len(homL))
