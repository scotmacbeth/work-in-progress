"""
HONEST engine: build T, eta^T, mu^T as genuine finite-CONTAINER morphisms from
aggregator-family + counit + comultiplication-routing data, and check the three
monad laws directly as equalities of container morphisms.  |S|=2.

A container (S0,P): S0=list of shape-ids; P: dict shape-> tuple of position tokens.
A container morphism f: (S0,P)->(S0',P'):  fwd: dict shape->shape' ; bwd: dict shape-> (dict pos'-> pos).

State container M=(SS, S): shapes SS=S^S, positions S (both source states).
Lifting <-> family A=(A_t)_{t in SS};  A_t is a polynomial Set^S->Set given by a
list of OBJECTS, each object = (n0,n1) = #slots reading state 0, state 1.
Slots of object j: ordered [(0,0),..,(0,n0-1),(1,0),..,(1,n1-1)].
"""
from itertools import product

S=[0,1]
SS=list(product(S,repeat=2))                 # endofunctions (t0,t1)
NM={(0,0):'c0',(0,1):'id',(1,0):'sw',(1,1):'c1'}
ID=(0,1)
def comp(v,u): return tuple(v[u[s]] for s in S)   # v after u

def slots(obj):
    n0,n1=obj
    return [(0,i) for i in range(n0)]+[(1,i) for i in range(n1)]

# ---------- the lifting T on containers ----------
def M_shapes(S0):
    """<<M>> S0 = { (t, x) : t in SS, x: S->S0 }.  x as tuple length 2."""
    return [(t,x) for t in SS for x in product(S0,repeat=2)]

def Apos(A, t, Q):
    """elements of A_t(Q):  Q=(Q0,Q1) tuples of tokens. returns list of (j, choice)."""
    out=[]
    for j,obj in enumerate(A[t]):
        sl=slots(obj)
        pools=[Q[s] for (s,i) in sl]
        for choice in product(*pools):
            out.append((j,choice))
    return out

def T_container(A, C):
    S0,P=C
    S0T=M_shapes(S0)
    PT={}
    for (t,x) in S0T:
        Q=(P[x[0]], P[x[1]])
        PT[(t,x)]=tuple(Apos(A,t,Q))
    return (S0T,PT)

# ---------- eta^T : Id => T ----------
def eta_morph(A, eps, C):
    """eps: dict (grade-id object index)-> marked slot index (into slots of that obj)."""
    S0,P=C
    TC=T_container(A,C)
    fwd={s0:(ID, (s0,s0)) for s0 in S0}
    bwd={}
    for s0 in S0:
        tsh=fwd[s0]                     # (id,(s0,s0))
        # positions of T at tsh = A_id( <P[s0]> )
        m={}
        Q=(P[s0],P[s0])
        for (j,choice) in Apos(A, ID, Q):
            e=eps[j]                     # marked slot index
            m[(j,choice)]=choice[e]      # a token in P[s0]
        bwd[s0]=m
    return (C,TC,fwd,bwd)

# ---------- mu^T : TT => T ----------
def thread(T,tvec):
    """outer next-state T, inner tvec=(t_0,t_1). composite sigma(s)=t_s(T(s))."""
    return tuple(tvec[s][T[s]] for s in S)

def mu_morph(A, delta, C):
    """delta: dict key (T,tvec) -> dict j(object idx in A_sigma) -> (out_j, inner, beta)
        out_j: object idx in A_T
        inner: dict slot_a(index into slots of out obj) -> object idx in A_{t_{s(a)}} (pure at T(s(a)))
        beta : dict (slot_a, slot_b)-> slot_c  (slot_b index into inner-obj slots; slot_c into A_sigma obj j slots)
    """
    S0,P=C
    TC=T_container(A,C)
    TTC=T_container(A,TC)               # TT
    # forward mu_M : <<M>>^2 S0 -> <<M>> S0
    S0T=TC[0]                            # <<M>>S0 (shapes of TC)
    fwd={}; bwd={}
    for (T,y) in TTC[0]:                 # y: S-> S0T ; y[s]=(t_s, x_s)
        tvec=tuple(y[s][0] for s in S)
        xvec=tuple(y[s][1] for s in S)  # x_s: S->S0
        sigma=thread(T,tvec)
        z=tuple(xvec[s][T[s]] for s in S)  # z(s)=x_s(T(s))
        fwd[(T,y)]=(sigma, z)
        # positions of T at (sigma,z) = A_sigma(P o z)  ; map back to positions of TT at (T,y)
        Qsig=(P[z[0]],P[z[1]])
        route=delta[(T,tvec)]
        m={}
        for (j,choice) in Apos(A, sigma, Qsig):
            out_j, inner, beta = route[j]
            out_obj=A[T][out_j]
            out_slots=slots(out_obj)
            # build the TT-position: element of A_T( s-> A_{t_s}(P o x_s) )
            # outer choice: for each slot a=(s,i) of out_obj, an element of A_{t_s}(P o x_s)
            outer_choice=[]
            for ai,a in enumerate(out_slots):
                (sa,ia)=a
                k=inner[ai]                    # inner object idx in A_{t_sa}, pure at T(sa)
                kobj=A[tvec[sa]][k]
                kslots=slots(kobj)
                # inner choice: each slot b of kobj (at state T(sa)) -> token in (P o x_sa)(state_b)
                inner_choice=[]
                for bi,b in enumerate(kslots):
                    (sb,ib)=b
                    # by purity sb should = T[sa]; token read = (P o x_sa)(sb)=P[x_sa[sb]]
                    slot_c=beta[(ai,bi)]        # slot index into j's slots
                    tok=choice[slot_c]          # token in (P o z)(state of slot_c) = P[z[state]]
                    inner_choice.append(tok)
                outer_choice.append((k, tuple(inner_choice)))
            m[(j,choice)]=(out_j, tuple(outer_choice))
        bwd[(T,y)]=m
    return (TTC,TC,fwd,bwd)

# ---------- generic container-morphism plumbing ----------
def compose(g, f):
    """g after f. f:C->D, g:D->E. returns C->E."""
    Cf,Df,ff,fb=f
    Dg,Eg,gf,gb=g
    fwd={s: gf[ff[s]] for s in ff}
    bwd={}
    for s in ff:
        ds=ff[s]; es=gf[ds]
        # E-pos at es -> D-pos at ds -> C-pos at s
        bwd[s]={ep: fb[s][gb[ds][ep]] for ep in gb[ds]}
    return (Cf,Eg,fwd,bwd)

def ident(C):
    S0,P=C
    return (C,C,{s:s for s in S0},{s:{p:p for p in P[s]} for s in S0})

def eq_morph(f,g):
    return f[2]==g[2] and f[3]==g[3]

# ---------- T on a morphism f: C->D ----------
def T_on(A, f):
    C,D,ff,fb=f
    TC=T_container(A,C); TD=T_container(A,D)
    S0,P=C; S0d,Pd=D
    fwd={}; bwd={}
    for (t,x) in TC[0]:
        xd=tuple(ff[x[s]] for s in S)     # u o x
        fwd[(t,x)]=(t,xd)
        # backward: A_t(Pd o u o x) -> A_t(P o x) via fb reindexed
        Q =(P[x[0]],P[x[1]])
        Qd=(Pd[xd[0]],Pd[xd[1]])
        m={}
        for (j,choiced) in Apos(A,t,Qd):
            sl=slots(A[t][j])
            newchoice=tuple(fb[x[s]][tok] for (tok,(s,i)) in zip(choiced,sl))
            m[(j,choiced)]=(j,newchoice)
        bwd[(t,x)]=m
    return (TC,TD,fwd,bwd)

# ---------- test containers ----------
def test_containers():
    Cs=[]
    # a few small containers with distinct tokens
    Cs.append((['a'], {'a':('a0','a1')}))
    Cs.append((['a','b'], {'a':('a0',),'b':('b0','b1')}))
    Cs.append((['a'], {'a':('a0','a1','a2')}))
    Cs.append((['p','q'], {'p':('p0','p1'),'q':('q0',)}))
    return Cs

FAST_CS=[(['a'], {'a':('a0','a1')}),
         (['a','b'], {'a':('a0',),'b':('b0','b1')})]

def check_laws_on(A, eps, delta, Cs, verbose=False):
    for C in Cs:
        TC=T_container(A,C)
        eta=eta_morph(A,eps,C)
        mu =mu_morph(A,delta,C)
        Teta=T_on(A, eta)
        if not eq_morph(compose(mu, Teta), ident(TC)):
            if verbose: print("RU fail",C);
            return False
        etaT=eta_morph(A,eps,TC)
        if not eq_morph(compose(mu, etaT), ident(TC)):
            if verbose: print("LU fail",C)
            return False
        Tmu=T_on(A, mu); muT=mu_morph(A,delta,TC)
        if not eq_morph(compose(mu, Tmu), compose(mu, muT)):
            if verbose: print("ASSOC fail",C)
            return False
    return True

TINY=[(['a'], {'a':('a0','a1')})]

def check_units_fast(A, eps, delta):
    for C in TINY:
        TC=T_container(A,C)
        eta=eta_morph(A,eps,C); mu=mu_morph(A,delta,C)
        if not eq_morph(compose(mu, T_on(A,eta)), ident(TC)): return False
        etaT=eta_morph(A,eps,TC)
        if not eq_morph(compose(mu, etaT), ident(TC)): return False
    return True

def check_assoc_fast(A, eps, delta):
    for C in TINY:
        mu=mu_morph(A,delta,C); TC=T_container(A,C)
        if not eq_morph(compose(mu, T_on(A,mu)), compose(mu, mu_morph(A,delta,TC))):
            return False
    return True

def check_laws_fast(A, eps, delta, verbose=False):
    return check_units_fast(A,eps,delta) and check_assoc_fast(A,eps,delta)

def check_laws(A, eps, delta, verbose=False):
    for C in test_containers():
        TC=T_container(A,C)
        eta=eta_morph(A,eps,C)
        mu =mu_morph(A,delta,C)
        # right unit: mu . T(eta) = id_T     [T(eta): T => TT]
        Teta=T_on(A, eta)
        ru=compose(mu, Teta)
        if not eq_morph(ru, ident(TC)):
            if verbose: print("RU fail on",C)
            return False
        # left unit: mu . eta_{TC} = id_T    [eta at container TC : TC=>T(TC)=TT]
        etaT=eta_morph(A,eps,TC)
        lu=compose(mu, etaT)
        if not eq_morph(lu, ident(TC)):
            if verbose: print("LU fail on",C)
            return False
        # assoc: mu . T(mu) = mu . mu_{TC}
        Tmu=T_on(A, mu)
        muT=mu_morph(A,delta,TC)
        lhs=compose(mu, Tmu)
        rhs=compose(mu, muT)
        if not eq_morph(lhs,rhs):
            if verbose: print("ASSOC fail on",C)
            return False
    return True

# ================= sanity: Sigma = State<|- lifting =================
def sigma_lifting():
    """A_t(Q)=Q0 + Q1 for ALL t. objects: obj0=(1,0) reads state0, obj1=(0,1) reads state1."""
    A={t:[(1,0),(0,1)] for t in SS}
    # counit on A_id: unit picks... eta shape id. eps must send each grade-id object to a slot.
    # For Sigma the counit A_id(<V>)=V+V -> V is fold: both objects map to their single slot.
    eps={0:0, 1:0}     # obj0 slot0, obj1 slot0 (each has 1 slot)
    # delta: for (T,tvec), object j in A_sigma. A_sigma objs: 0=(1,0)@state0, 1=(0,1)@state1.
    # composite obj j reads state s(j) (0 or 1). out object in A_T reading same state s(j).
    # inner: the single slot of out-obj (at state s(j)) -> inner obj in A_{t_{s(j)}} pure at T(s(j)).
    delta={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            sigma=thread(T,tvec)
            route={}
            for j,obj in enumerate([(1,0),(0,1)]):
                sj=0 if obj==(1,0) else 1     # state read by composite object j
                out_j=j                        # object in A_T reading state sj (same indexing)
                # out obj = [(1,0),(0,1)][j] reads state sj; its 1 slot at state sj
                # inner: A_{t_sj} object pure at T(sj): object reading state T(sj) = index (0 if T(sj)==0 else 1)
                k=0 if T[sj]==0 else 1
                inner={0:k}                    # slot 0 of out-obj -> inner k
                # beta: composite RHS slot (a=0, b=0) -> slot 0 of j
                beta={(0,0):0}
                route[j]=(out_j, inner, beta)
            delta[(T,tvec)]=route
    return A,eps,delta

if __name__=="__main__":
    A,eps,delta=sigma_lifting()
    print("Sigma lifting satisfies monad laws:", check_laws(A,eps,delta,verbose=True))
