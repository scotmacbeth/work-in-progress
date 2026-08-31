"""
Memory-lean, per-shape backward-map computation for eta^T, mu^T, T(f), and a SAMPLING
associativity check.  Avoids materializing <<M>>^k containers.  |S|=2.
A position of A_t(P o x) is (j, choice) with choice a tuple over slots(A[t][j]) of tokens.
"""
from itertools import product
import honest, random
S=[0,1]; SS=honest.SS; ID=honest.ID; slots=honest.slots; thread=honest.thread

# ---- lean position enumeration for one shape ----
def posA(A,t,Q):
    out=[]
    for j,obj in enumerate(A[t]):
        sl=slots(obj); pools=[Q[s] for (s,i) in sl]
        for ch in product(*pools): out.append((j,ch))
    return out

# ---- mu backward at a single TT-shape w=(T,y), y[s]=(t_s,x_s), over base container (S0,P) ----
def mu_bwd_at(A,delta,P,w):
    (T,y)=w
    tvec=tuple(y[s][0] for s in S); xvec=tuple(y[s][1] for s in S)
    sigma=thread(T,tvec); z=tuple(xvec[s][T[s]] for s in S)
    img=(sigma,z)
    Qsig=(P[z[0]],P[z[1]]); route=delta[(T,tvec)]; m={}
    for (j,choice) in posA(A,sigma,Qsig):
        out_j,inner,beta=route[j]; out_slots=slots(A[T][out_j]); outer=[]
        for ai,a in enumerate(out_slots):
            (sa,ia)=a; k=inner[ai]; kobj=A[tvec[sa]][k]; ic=[]
            for bi,b in enumerate(slots(kobj)):
                ic.append(choice[beta[(ai,bi)]])
            outer.append((k,tuple(ic)))
        m[(j,choice)]=(out_j,tuple(outer))
    return img,m

# ---- eta backward at base shape s0 ----
def eta_bwd_at(A,eps,P,s0):
    img=(ID,(s0,s0)); Q=(P[s0],P[s0]); m={}
    for (j,choice) in posA(A,ID,Q): m[(j,choice)]=choice[eps[j]]
    return img,m

# ---- T(f) backward at a T-shape (t,x); f:(S0,P)->(S0',P') morphism (ff,fb) ----
def Tf_bwd_at(A,ff,fb,P,Pd,shape):
    (t,x)=shape; xd=tuple(ff[x[s]] for s in S); img=(t,xd)
    Qd=(Pd[xd[0]],Pd[xd[1]]); m={}
    for (j,choiced) in posA(A,t,Qd):
        sl=slots(A[t][j]); nc=tuple(fb[x[s]][tok] for (tok,(s,i)) in zip(choiced,sl))
        m[(j,choiced)]=(j,nc)
    return img,m

# We check assoc:  mu . T(mu) == mu . mu_{TC}   as maps TTT(C) -> T(C).
# domain shape w3 in <<M>>^3(S0).  Both sides: w3 |-> image T-shape, and backward T-pos->TTT-pos.
# We compare the backward maps (dicts) per sampled w3.  (Forward shapes coincide = monad on shapes.)

def Mshapes(S0): return [(t,x) for t in SS for x in product(S0,repeat=2)]

def build_container(A,C):
    S0,P=C; sh=Mshapes(S0); Pd={}
    for (t,x) in sh:
        Q=(P[x[0]],P[x[1]]); Pd[(t,x)]=tuple(posA(A,t,Q))
    return (sh,Pd)

def assoc_sample(A,eps,delta,C,nsamp=40,seed=0):
    random.seed(seed)
    S0,P=C
    TC=build_container(A,C)                 # T(C): shapes + positions (small; degree over |P|)
    Ptc=TC[1]; S0tc=TC[0]
    S0ttc=Mshapes(S0tc)                     # TT(C) SHAPES only (no positions -> low memory)
    # mu at C : TT->T  (fwd on TT-shapes)
    # mu at TC: TTT->TT
    # T(mu)   : TTT->TT  (T applied to mu:TT->T)
    # enumerate TTT shapes = Mshapes(S0ttc)
    ttt=Mshapes(S0ttc)
    if len(ttt)>nsamp: ttt=random.sample(ttt,nsamp)
    # fwd/bwd of mu at C, as callables via mu_bwd_at(A,delta,P,·)
    # LHS = mu_C . T(mu_C):  w3 --T(mu)--> w2' in TT --mu_C--> w1 in T
    # RHS = mu_C . mu_TC :   w3 --mu_TC--> w2'' in TT --mu_C--> w1 in T
    # mu_C fwd: we get from mu_bwd_at(...,P,·).  T(mu): use Tf with f=mu_C.
    # Precompute mu_C as morphism dicts on TT (needed as f for T(mu)) -- but that's big.
    # Instead compute per-shape:
    # need mu_C backward available for arbitrary TT-shape: mu_bwd_at(A,delta,P, w2)
    # T(mu_C) backward at TTT-shape w3=(t,X) where X:S->S0tt: image (t, mu_C.fwd∘X); backward via mu_C.bwd
    for w3 in ttt:
        (t3,X3)=w3   # X3: S->S0ttc (TT-shapes)
        # ---- LHS: T(mu_C) then mu_C ----
        # T(mu_C) at w3: image shape (t3, X2) with X2[s]=mu_C.fwd(X3[s]); backward mu_C.bwd at X3[s]
        muC_fwd={}; muC_bwd={}
        for s in S:
            img,m=mu_bwd_at(A,delta,P,X3[s]); muC_fwd[s]=img; muC_bwd[s]=m
        X2=tuple(muC_fwd[s] for s in S); w2_lhs=(t3,X2)   # in TT(C) shapes
        # backward of T(mu_C) at w3: A_{t3}(P_TC o X2) -> A_{t3}(P_TT o X3)
        # then mu_C at w2_lhs: T pos -> TT pos(w2_lhs). Compose.
        # mu_C : TT(C)->T(C) at TT-shape w2_lhs=(t3,X2); base container C (P). X2 are T(C)-shapes.
        img1,muAtw2=mu_bwd_at(A,delta,P,w2_lhs)
        # T(mu_C) backward at w3 maps TT(C)-pos at w2_lhs -> TTT(C)-pos at w3
        Q_TT=(Ptc[X2[0]],Ptc[X2[1]])
        Tmu_bwd={}
        for (j,choiced) in posA(A,t3,Q_TT):
            sl=slots(A[t3][j])
            nc=tuple(muC_bwd[s][tok] for (tok,(s,i)) in zip(choiced,sl))
            Tmu_bwd[(j,choiced)]=(j,nc)
        # LHS backward: T(C)-pos at img1 -> via muAtw2 -> TT(C)-pos at w2_lhs -> via Tmu_bwd -> TTT-pos
        lhs={p: Tmu_bwd[muAtw2[p]] for p in muAtw2}
        # ---- RHS: mu_TC then mu_C ----
        # mu_TC: TTT->TT at shape w3, base container TC (P=Ptc)
        img_rhs2, muTC_bwd = mu_bwd_at(A,delta,Ptc,w3)   # gives TT(C)-shape img_rhs2 and bwd TT-pos->TTT-pos
        # then mu_C at img_rhs2
        img_rhs1, muC2 = mu_bwd_at(A,delta,P,img_rhs2)
        rhs={p: muTC_bwd[muC2[p]] for p in muC2}
        if img1!=img_rhs1:
            return ('FWD-MISMATCH',w3)
        if lhs!=rhs:
            return ('ASSOC-FAIL',w3)
    return ('ok',len(ttt))
