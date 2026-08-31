"""Verification for 2026-08-30 PROVE: fibredness vs left-closure of (-)<|q.
Containers over Set: p = (S, P) with S = list of shape labels, P = list of position-SIZES.
Containers over Vec_fd(F_2): same but P = list of DIMENSIONS.
"""
import itertools, random, math
from functools import reduce

# ---------- Set side ----------
def hom_set(p, r):
    """|Cont((S,P),(R,M))| = prod_s sum_rho |P_s|^{|M_rho|}."""
    P, M = p, r
    tot = 1
    for ps in P:
        s = 0
        for mr in M:
            s += ps**mr if not (ps==0 and mr==0) else 1
        tot *= s
    return tot

def lhd_set(P, Q):
    """p<|q shapes/positions. P,Q lists of sizes. Returns list of position-sizes."""
    out = []
    T = len(Q)
    for ps in P:
        for tau in itertools.product(range(T), repeat=ps):
            out.append(sum(Q[t] for t in tau))
    return out

def otimes_set(P, Q):
    return [a*b for a in P for b in Q]

# 1. shape set of p<|q depends on POSITIONS of p
print("== 1. shapes of p<|q read p's positions ==")
for Q in ([1,1],[0,0],[2,1]):
    for P in ([0],[1],[2]):
        print(f"  P={P} Q(sizes)={Q}: #shapes(p<|q) = {len(lhd_set(P,Q))}")

# 2. monomial q: adjunction Poly(p<|q, r) = Poly(p, H), H = (Sum_rho Q^{M_rho}, M_rho)
print("== 2. monomial q=(1,Q): right adjoint H = (Sigma_rho Q^{M_rho}, M_rho) ==")
random.seed(0); bad=0; n=0
for trial in range(3000):
    Q  = random.randint(0,3)
    P  = [random.randint(0,3) for _ in range(random.randint(1,3))]
    M  = [random.randint(0,3) for _ in range(random.randint(1,3))]
    lhs = hom_set(lhd_set(P,[Q]), M)
    HN = []
    for mr in M:
        mult = Q**mr if not (Q==0 and mr==0) else 1
        HN += [mr]*mult
    rhs = hom_set(P, HN)
    n+=1
    if lhs!=rhs: bad+=1; print("   MISMATCH",Q,P,M,lhs,rhs)
print(f"  checked {n}, mismatches {bad}")

# 2b. and p<|y^Q == p (x) y^Q
print("  collapse check p<|y^Q == p(x)y^Q:",
      all(sorted(lhd_set(P,[Q]))==sorted(otimes_set(P,[Q]))
          for P in [[0],[1],[2],[0,3],[1,2,2]] for Q in range(4)))

# 3. G_r(Z) for r = 2 = (2, [0,0]): should be 2^{T^Z}; test non-polynomiality
print("== 3. G_2(Z) = |Cont(y^Z <| q, 2)| = 2^{T^Z}, T=2 ==")
Q=[1,1]  # T=2
vals=[]
for Z in range(0,5):
    G = hom_set(lhd_set([Z],Q), [0,0])
    vals.append(G)
    print(f"  Z={Z}: G={G}   2^(2^{Z})={2**(2**Z)}")
# search for a polynomial functor fit: G(n) = sum_u n^{k_u}, u finite, k_u finite
def poly_fit(vals, maxexp=6):
    """G(0)=#{k_u=0}, G(1)=|U|. try all multisets of exponents of size G(1)."""
    U = vals[1]; z = vals[0]
    if U < z: return None  # #{k_u=0} cannot exceed |U|
    if U > 8: return "too many summands to brute force (|U|=%d)"%U
    for rest in itertools.combinations_with_replacement(range(1,maxexp+1), U-z):
        exps = [0]*z + list(rest)
        ok = all(sum((0**e if n==0 else n**e) for e in exps)==vals[n] for n in range(len(vals)))
        if ok: return exps
    return None
print("  polynomial-functor fit for (G(0..4)):", poly_fit(vals))

# also T=3
Q3=[1,1,1]; vals3=[hom_set(lhd_set([Z],Q3),[0,0]) for Z in range(0,4)]
print("  T=3 values:", vals3, "fit:", poly_fit(vals3))
# and |T|=0
Q0=[]; vals0=[hom_set(lhd_set([Z],Q0),[0,0]) for Z in range(0,4)]
print("  T=0 (q=0) values:", vals0, "fit:", poly_fit(vals0))
# and |T|=1 (should fit)
Q1=[1]; vals1=[hom_set(lhd_set([Z],Q1),[0,0]) for Z in range(0,5)]
print("  T=1 values:", vals1, "fit:", poly_fit(vals1))

# ---------- Vec_fd(F_2) side ----------
print("== 4. Fam(Vec_fd(F_2)^op) ==")
def hom_vec(P, M, qcard=2):
    """|Fam((S,P),(R,M))| = prod_s sum_rho |Hom(M_rho,P_s)| = prod_s sum_rho q^{m*p}."""
    tot=1
    for ps in P:
        tot *= sum(qcard**(mr*ps) for mr in M)
    return tot
def lhd_vec(P,Q):   # collapse: dims multiply, shapes = S x T
    return [a*b for a in P for b in Q]
# closure: H = (R^T, N_rho = sum_t dim M_{rho t} * dim Q_t)
def closure_vec(Q, M):
    U=[]
    for rho in itertools.product(range(len(M)), repeat=len(Q)):
        U.append(sum(M[rho[t]]*Q[t] for t in range(len(Q))))
    return U
random.seed(1); bad=0;n=0
for trial in range(4000):
    Q=[random.randint(0,2) for _ in range(random.randint(0,3))]
    P=[random.randint(0,2) for _ in range(random.randint(1,3))]
    M=[random.randint(0,2) for _ in range(random.randint(1,2))]
    lhs=hom_vec(lhd_vec(P,Q), M)
    rhs=hom_vec(P, closure_vec(Q,M))
    n+=1
    if lhs!=rhs: bad+=1; print("   MISMATCH",Q,P,M,lhs,rhs)
print(f"  closure adjunction over Vec_fd: checked {n}, mismatches {bad}")
print("  dim N_rho for Q=[1]*T, M=[1]:", [max(closure_vec([1]*T,[1])) for T in range(1,8)],
      "-> grows with T, leaves Vec_fd as T->oo")

# ---------- 5. explicit morphisms: functoriality of (-)<|q and cartesian preservation ----------
print("== 5. explicit container morphisms: (-)<|q functorial + preserves cartesian ==")
# container p = (S, P) with S=range(len(P)), P[s] = position set size
# morphism p->p' = (f: list len S -> S', sharp: list of dicts, sharp[s]: P'[f[s]] -> P[s])
def lhd_shapes(P,Q):
    """list of (s,tau) with tau a tuple of length P[s] valued in range(len(Q))"""
    return [(s,tau) for s in range(len(P)) for tau in itertools.product(range(len(Q)),repeat=P[s])]
def lhd_pos(P,Q,sh):
    s,tau = sh
    return [(d,e) for d in range(P[s]) for e in range(Q[tau[d]])]
def lhd_mor(P,Pp,f,sharp,Q):
    """returns (F, SHARP) for phi<|q ; F maps shape-index of p<|q to that of p'<|q"""
    shP, shPp = lhd_shapes(P,Q), lhd_shapes(Pp,Q)
    idx = {sh:i for i,sh in enumerate(shPp)}
    F=[];SHARP=[]
    for (s,tau) in shP:
        # tau' = tau . sharp[s] : P'[f[s]] -> T
        taup = tuple(tau[sharp[s][dp]] for dp in range(Pp[f[s]]))
        F.append(idx[(f[s],taup)])
        # backward: positions of target shape -> positions of source shape
        srcpos = lhd_pos(P,Q,(s,tau)); tgtpos = lhd_pos(Pp,Q,(f[s],taup))
        si = {x:i for i,x in enumerate(srcpos)}
        SHARP.append({j:si[(sharp[s][dp], e)] for j,(dp,e) in enumerate(tgtpos)})
    return F,SHARP
def compose(f1,sh1,f2,sh2):
    """p--phi1-->p'--phi2-->p''  ; sh_i are lists of dicts (target pos -> source pos)"""
    f = [f2[f1[s]] for s in range(len(f1))]
    sh = [{d:sh1[s][sh2[f1[s]][d]] for d in sh2[f1[s]]} for s in range(len(f1))]
    return f,sh
random.seed(7); nfun=0; ncart=0; badf=0; badc=0
for _ in range(400):
    Q=[random.randint(0,2) for _ in range(random.randint(1,3))]
    P  =[random.randint(0,2) for _ in range(random.randint(1,2))]
    Pp =[random.randint(0,2) for _ in range(random.randint(1,2))]
    Ppp=[random.randint(0,2) for _ in range(random.randint(1,2))]
    f1=[random.randrange(len(Pp)) for _ in range(len(P))]
    f2=[random.randrange(len(Ppp)) for _ in range(len(Pp))]
    try:
        sh1=[{d:random.randrange(P[s]) for d in range(Pp[f1[s]])} for s in range(len(P))]
        sh2=[{d:random.randrange(Pp[s]) for d in range(Ppp[f2[s]])} for s in range(len(Pp))]
    except ValueError:
        continue   # P[s]==0 but Pp[f1[s]]>0 : no morphism
    # functoriality: (phi2 . phi1)<|q == (phi2<|q) . (phi1<|q)
    fc,shc = compose(f1,sh1,f2,sh2)
    A = lhd_mor(P,Ppp,fc,shc,Q)
    B1= lhd_mor(P,Pp ,f1,sh1,Q); B2= lhd_mor(Pp,Ppp,f2,sh2,Q)
    B = compose(B1[0],B1[1],B2[0],B2[1])
    nfun+=1
    if A[0]!=B[0] or A[1]!=B[1]: badf+=1
    # cartesian: sharp[s] a bijection  =>  image under <|q also bijective on each fibre
    if len(P)==len(Pp) and sorted(f1)==list(range(len(P))) and all(P[f1.index(s)]==Pp[s] for s in range(len(Pp))):
        pass
for _ in range(400):   # cartesian test: build genuinely cartesian phi (f arbitrary, sharp = identity)
    Q=[random.randint(0,2) for _ in range(random.randint(1,3))]
    Pp=[random.randint(0,2) for _ in range(random.randint(1,3))]
    f =[random.randrange(len(Pp)) for _ in range(random.randint(1,3))]
    P =[Pp[f[s]] for s in range(len(f))]                 # cartesian lift  (S, P'.f)
    sh=[{d:d for d in range(Pp[f[s]])} for s in range(len(f))]
    F,SHARP = lhd_mor(P,Pp,f,sh,Q)
    ncart+=1
    ok = all(len(set(SHARP[i].values()))==len(SHARP[i])
             and len(SHARP[i])==len(lhd_pos(P,Q,lhd_shapes(P,Q)[i])) for i in range(len(F)))
    if not ok: badc+=1
print(f"  functoriality of (-)<|q: {nfun} checked, {badf} failures")
print(f"  cartesian preservation:  {ncart} checked, {badc} failures")

# ---------- 6. G_2 functorial action is preimage along restriction ----------
print("== 6. G_2(Z)=2^{T^Z}, action = preimage along res; invariant-subset image test ==")
T=2
for Zn in (1,2,3):
    TZ=list(itertools.product(range(T),repeat=Zn))
    for n in range(Zn):
        A=[m for m in range(Zn) if m!=n]
        res={tau:tuple(tau[m] for m in A) for tau in TZ}
        TA=sorted(set(res.values()))
        img=set()
        for W in itertools.chain.from_iterable(itertools.combinations(TA,k) for k in range(len(TA)+1)):
            img.add(frozenset(t for t in TZ if res[t] in set(W)))
        # image = subsets invariant under changing coordinate n
        inv=set()
        for k in range(len(TZ)+1):
            for S_ in itertools.combinations(TZ,k):
                S_=set(S_)
                if all(tuple(v if m!=n else b for m,v in enumerate(t)) in S_ for t in S_ for b in range(T)):
                    inv.add(frozenset(S_))
        assert img==inv, (Zn,n)
print("  image of G_2(A_n) = {subsets invariant under changing coordinate n}: CONFIRMED for |Z|<=3")
