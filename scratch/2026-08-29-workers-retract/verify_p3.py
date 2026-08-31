"""P3: oplax coherence of sigma, comonad-collapse r∘δ=Δ(d), and lax coherence of r.

Poly object P: dict-like with .sh (list of shapes), .pos (shape-> list of positions).
Poly morphism m: (fwd: dict sh_p->sh_q, bwd: dict sh_p-> dict(pos_q[fwd s]-> pos_p[s])).
"""
from itertools import product

class Poly:
    def __init__(self, sh, pos):
        self.sh=list(sh); self.pos={s:list(pos[s]) for s in sh}

def DeltaS(S):
    S=list(S)
    return Poly(S, {s:list(S) for s in S})

def DeltaSet(U):
    # Δ of a set U (=U·y^U)
    U=list(U)
    return Poly(U, {u:list(U) for u in U})

def tri(P,Q):
    # P ▷ Q
    sh=[]; pos={}
    for s in P.sh:
        Ps=P.pos[s]
        for h in product(Q.sh, repeat=len(Ps)):  # h: P[s]->S_Q, indexed by position in Ps
            hh=dict(zip(Ps,h))
            shape=(s, tuple(sorted(hh.items())))
            sh.append(shape)
            pos[shape]=[(a,b) for a in Ps for b in Q.pos[hh[a]]]
    return Poly(sh,pos), None

def as_h(shape, P):
    s, items = shape
    return s, dict(items)

def compose(f,g,dom):
    # f: p->q, g:q->r ; returns g∘f : p->r ; dom = list of shapes of p with pos
    ffwd,fbwd=f; gfwd,gbwd=g
    hfwd={}; hbwd={}
    for s in ffwd:
        qs=ffwd[s]; rs=gfwd[qs]
        hfwd[s]=rs
        hbwd[s]={c: fbwd[s][ gbwd[qs][c] ] for c in gbwd[qs]}
    return hfwd,hbwd

def tri_mor(f,fP,fQ, g,gP,gQ):
    # f:p->p' (fP=p,fQ=p'), g:q->q' (gP=q,gQ=q'); returns f▷g : p▷q -> p'▷q'
    ffwd,fbwd=f; gfwd,gbwd=g
    P,Pp=fP,fQ; Q,Qp=gP,gQ
    PtriQ,_=tri(P,Q)
    hfwd={}; hbwd={}
    for shape in PtriQ.sh:
        s,hh=as_h(shape,P)
        fs=ffwd[s]
        # h'(a') = g_1(h(f♯_s a'))
        Ppos=Pp.pos[fs]
        hp={}
        for ap in Ppos:
            a=fbwd[s][ap]
            hp[ap]=gfwd[hh[a]]
        tgt=(fs, tuple(sorted(hp.items())))
        hfwd[shape]=tgt
        # bwd: (a',b') -> (f♯ a', g♯_{h(a)} b')
        bwd={}
        for ap in Ppos:
            a=fbwd[s][ap]
            for bp in Qp.pos[hp[ap]]:
                b=gbwd[hh[a]][bp]
                bwd[(ap,bp)]=(a,b)
        hbwd[shape]=bwd
    return (hfwd,hbwd), PtriQ

def id_mor(P):
    return ({s:s for s in P.sh}, {s:{c:c for c in P.pos[s]} for s in P.sh})

def sigma(S,T):
    # Δ(S×T) -> ΔS▷ΔT
    S=list(S);T=list(T)
    A=DeltaSet(list(product(S,T)))
    DS=DeltaS(S); DT=DeltaS(T); B,_=tri(DS,DT)
    def const_g(t):
        hh={i:t for i in S}
        return (tuple(sorted(hh.items())))
    fwd={}; bwd={}
    for (s,t) in A.sh:
        tgt=(s, const_g(t))
        fwd[(s,t)]=tgt
        # B.pos[tgt] = [(i,j)] ; A.pos[(s,t)]=S×T ; id
        bwd[(s,t)]={(i,j):(i,j) for (i,j) in B.pos[tgt]}
    return (fwd,bwd), A, B, DS, DT

def r_mor(S,T):
    S=list(S);T=list(T)
    A=DeltaSet(list(product(S,T)))
    DS=DeltaS(S); DT=DeltaS(T); B,_=tri(DS,DT)
    fwd={}; bwd={}
    for shape in B.sh:
        s,hh=as_h(shape,DS)
        t=hh[s]  # g(s)
        fwd[shape]=(s,t)
        bwd[shape]={(i,j):(i,j) for (i,j) in A.pos[(s,t)]}
    return (fwd,bwd), A, B, DS, DT

def eq_mor(m1,m2,dom):
    f1,b1=m1; f2,b2=m2
    for s in dom.sh:
        if f1[s]!=f2[s]: return False,f"fwd@{s}"
        if b1[s]!=b2[s]: return False,f"bwd@{s}"
    return True,"eq"

# ---------- Check 1: retract r∘σ=id (recheck in this lib) ----------
def check_retract(nS,nT):
    S=range(nS);T=range(nT)
    sig,A,B,DS,DT=sigma(S,T)
    rr,_,_,_,_=r_mor(S,T)
    comp=compose(sig,rr,A)
    ok,_=eq_mor(comp,id_mor(A),A)
    return ok

# ---------- Check 2: comonad collapse r∘δ = Δ(d) with π2 ----------
def delta_store(S):
    # δ: ΔS -> ΔS▷ΔS ; δ_1(s)=(s,id_S), δ♯_s(i,j)=j
    S=list(S)
    DS=DeltaS(S); B,_=tri(DS,DS)
    fwd={}; bwd={}
    for s in S:
        idg=tuple(sorted({i:i for i in S}.items()))
        tgt=(s,idg)
        fwd[s]=tgt
        bwd[s]={(i,j):j for (i,j) in B.pos[tgt]}
    return (fwd,bwd), DS, B

def Delta_diag(S, which='pi2'):
    # Δ(d): ΔS -> Δ(S×S), s↦(s,s), backward (i,j)↦ j (pi2) or i (pi1)
    S=list(S)
    DS=DeltaS(S); A=DeltaSet(list(product(S,S)))
    fwd={}; bwd={}
    for s in S:
        fwd[s]=(s,s)
        if which=='pi2':
            bwd[s]={(i,j):j for (i,j) in A.pos[(s,s)]}
        else:
            bwd[s]={(i,j):i for (i,j) in A.pos[(s,s)]}
    return (fwd,bwd), DS, A

def check_collapse(nS):
    S=range(nS)
    dl,DS,B=delta_store(S)
    rr,A,B2,_,_=r_mor(S,S)
    comp=compose(dl,rr,DS)  # ΔS -> Δ(S×S)
    dd2,_,_=Delta_diag(S,'pi2')
    ok2,_=eq_mor(comp,dd2,DS)
    dd1,_,_=Delta_diag(S,'pi1')
    ok1,_=eq_mor(comp,dd1,DS)
    # also σ∘Δ(d): compare to δ
    sig,Asig,Bsig,_,_=sigma(S,S)
    sig_dd = compose(dd2, sig, DS)  # ΔS->Δ(S×S)->ΔS▷ΔS
    ok_sig_eq_delta,_=eq_mor(sig_dd, dl, DS)
    return ok2, ok1, ok_sig_eq_delta

# ---------- Check 3: oplax associativity hexagon for σ ----------
def Delta_bij(f, S, Sp):
    # f: S->Sp bijection (dict). Δf: ΔS->ΔSp, s↦f[s], backward f^{-1}
    S=list(S); Sp=list(Sp)
    DS=DeltaS(S); DSp=DeltaS(Sp)
    finv={f[s]:s for s in S}
    fwd={s:f[s] for s in S}
    bwd={s:{a:finv[a] for a in DSp.pos[f[s]]} for s in S}
    return (fwd,bwd), DS, DSp

def check_hexagon(nS,nT,nU):
    S=list(range(nS));T=list(range(nT));U=list(range(nU))
    # Objects
    STU_L = list(product(product(S,T),U))     # (S×T)×U
    STU_R = list(product(S,product(T,U)))      # S×(T×U)
    A_L = DeltaSet(STU_L)
    # associator α: (S×T)×U -> S×(T×U) bijection
    alpha={((s,t),u):(s,(t,u)) for s in S for t in T for u in U}
    Dalpha, DA_L, DA_R = Delta_bij(alpha, STU_L, STU_R)
    # LHS: σ_{S×T,U} then (σ_{S,T} ▷ ΔU)
    ST=list(product(S,T))
    sig_STU_L, A1,B1,DST,DU = sigma(ST,U)   # Δ((S×T)×U) -> Δ(S×T)▷ΔU
    sig_ST, Asig, Bsig, DS,DT = sigma(S,T)  # Δ(S×T) -> ΔS▷ΔT
    idU = id_mor(DeltaS(U))
    # (σ_{S,T} ▷ ΔU) : Δ(S×T)▷ΔU -> (ΔS▷ΔT)▷ΔU
    stU_mor, dom_stU = tri_mor(sig_ST, DeltaSet(ST), tri(DS,DT)[0], idU, DeltaS(U), DeltaS(U))
    LHS = compose(sig_STU_L, stU_mor, A_L)
    # RHS: Δα ; σ_{S,T×U} ; (ΔS ▷ σ_{T,U})
    TU=list(product(T,U))
    sig_S_TU, A2, B2, DS2, DTU = sigma(S,TU)  # Δ(S×(T×U)) -> ΔS ▷ Δ(T×U)
    sig_TU, AtU, BtU, DT2, DU2 = sigma(T,U)   # Δ(T×U) -> ΔT▷ΔU
    idS=id_mor(DeltaS(S))
    S_sigTU_mor, dom2 = tri_mor(idS, DeltaS(S), DeltaS(S), sig_TU, DeltaSet(TU), tri(DeltaS(T),DeltaS(U))[0])
    # compose: A_L -Δα-> A_R -σ_{S,T×U}-> ΔS▷Δ(T×U) -(ΔS▷σ_{T,U})-> ΔS▷(ΔT▷ΔU)
    step1=compose(Dalpha, sig_S_TU, A_L)     # A_L -> ΔS▷Δ(T×U)
    RHS=compose(step1, S_sigTU_mor, A_L)     # A_L -> ΔS▷(ΔT▷ΔU)
    # ▷ strictly associative so (ΔS▷ΔT)▷ΔU == ΔS▷(ΔT▷ΔU) as Poly? shapes differ in nesting; compare via canonical reassoc.
    # We compare fwd/bwd after normalizing shape/pos nesting.
    return LHS, RHS, A_L

def flat_shape_L(shape):
    # O_L=(ΔS▷ΔT)▷ΔU : shape=((s,g_items), k_items) with k:(i,j)->U
    inner,k_items=shape
    s,g_items=inner
    g=dict(g_items); k=dict(k_items)
    return (s, tuple(sorted(g.items())), tuple(sorted(k.items())))

def flat_pos_L(c):
    # ((i,j),u)->(i,j,u)
    ij,u=c; i,j=ij; return (i,j,u)

def flat_shape_R(shape):
    # O_R=ΔS▷(ΔT▷ΔU): shape=(s, p_items) p:i->(t,m_items)
    s,p_items=shape
    p=dict(p_items)
    g={}; k={}
    for i,tm in p.items():
        t,m_items=tm; m=dict(m_items)
        g[i]=t
        for j,u in m.items():
            k[(i,j)]=u
    return (s, tuple(sorted(g.items())), tuple(sorted(k.items())))

def flat_pos_R(c):
    # (i,(j,u))->(i,j,u)
    i,ju=c; j,u=ju; return (i,j,u)

def normalize_target(mor, kind):
    fwd,bwd=mor
    fs = flat_shape_L if kind=='L' else flat_shape_R
    fp = flat_pos_L if kind=='L' else flat_pos_R
    nf={}; nb={}
    for s in fwd:
        nf[s]=fs(fwd[s])
        nb[s]={ fp(c):v for c,v in bwd[s].items() }
    return nf,nb

def check_lax_hexagon(nS,nT,nU):
    S=list(range(nS));T=list(range(nT));U=list(range(nU))
    ST=list(product(S,T)); TU=list(product(T,U))
    DS=DeltaS(S); DT=DeltaS(T); DU=DeltaS(U)
    DST=DeltaSet(ST); DTU=DeltaSet(TU)
    B_ST,_=tri(DS,DT)           # ΔS▷ΔT
    B_TU,_=tri(DT,DU)           # ΔT▷ΔU
    O_L,_=tri(B_ST,DU)          # (ΔS▷ΔT)▷ΔU
    O_R,_=tri(DS,B_TU)          # ΔS▷(ΔT▷ΔU)
    # r morphisms
    r_ST,_,_,_,_=r_mor(S,T)     # ΔS▷ΔT -> Δ(S×T)
    r_TU,_,_,_,_=r_mor(T,U)     # ΔT▷ΔU -> Δ(T×U)
    r_STU,_,_,_,_=r_mor(ST,U)   # Δ(S×T)▷ΔU -> Δ((S×T)×U)
    r_S_TU,_,_,_,_=r_mor(S,TU)  # ΔS▷Δ(T×U) -> Δ(S×(T×U))
    idU=id_mor(DU); idS=id_mor(DS)
    # LHS: O_L -(r_ST▷idU)-> Δ(S×T)▷ΔU -(r_{S×T,U})-> Δ((S×T)×U) -Δα-> Δ(S×(T×U))
    rU_mor,_=tri_mor(r_ST, B_ST, DST, idU, DU, DU)     # O_L -> Δ(S×T)▷ΔU
    step=compose(rU_mor, r_STU, O_L)                    # O_L -> Δ((S×T)×U)
    alpha={((s,t),u):(s,(t,u)) for s in S for t in T for u in U}
    Dalpha,_,_=Delta_bij(alpha, list(product(ST,U)), list(product(S,TU)))
    LHS=compose(step, Dalpha, O_L)                      # O_L -> Δ(S×(T×U))
    # RHS: O_R -(idS▷r_TU)-> ΔS▷Δ(T×U) -(r_{S,T×U})-> Δ(S×(T×U))
    Sr_mor,_=tri_mor(idS, DS, DS, r_TU, B_TU, DTU)      # O_R -> ΔS▷Δ(T×U)
    RHS=compose(Sr_mor, r_S_TU, O_R)                    # O_R -> Δ(S×(T×U))
    # compare via canonical ternary flatten of the SOURCE (domain O_L vs O_R)
    Lmap={};
    for s in O_L.sh:
        cs=flat_shape_L(s); Lmap[cs]=(LHS[0][s], {c:flat_pos_L(v) for c,v in LHS[1][s].items()})
    Rmap={}
    for s in O_R.sh:
        cs=flat_shape_R(s); Rmap[cs]=(RHS[0][s], {c:flat_pos_R(v) for c,v in RHS[1][s].items()})
    okf=all(Lmap[cs][0]==Rmap[cs][0] for cs in Lmap)
    okb=all(Lmap[cs][1]==Rmap[cs][1] for cs in Lmap)
    return okf,okb

def check_sigma_unit(nS):
    # σ_{S,1}: Δ(S×1) -> ΔS▷Δ1 = ΔS▷y ≅ ΔS should be the right unitor (iso, essentially id)
    S=list(range(nS)); One=[0]
    sig,A,B,DS,D1=sigma(S,One)  # Δ(S×1)->ΔS▷Δ1
    # ΔS▷Δ1: Δ1=y (1 shape, 1 pos). check B ≅ ΔS and σ is that iso on shapes/pos
    # shapes of Δ(S×1) = (s,0); shapes of B=(s, g:S->{0}) unique g. fwd (s,0)->(s,unique)
    okf = all(sig[0][(s,0)][0]==s for s in S)
    return okf, len(B.sh)==nS

if __name__=="__main__":
    print("Check1 retract:", [ (n, check_retract(n,n)) for n in [1,2,3] ])
    print("Check2 collapse (r∘δ=Δd_pi2, =Δd_pi1, σ∘Δd==δ?):", [ (n, check_collapse(n)) for n in [1,2,3] ])
    # P3a: sigma oplax associativity hexagon
    for (a,b,c) in [(1,1,1),(2,1,1),(1,2,1),(1,1,2),(2,2,2),(2,3,2)]:
        L,R,dom=check_hexagon(a,b,c)
        Ln=normalize_target(L,'L'); Rn=normalize_target(R,'R')
        okf = all(Ln[0][s]==Rn[0][s] for s in dom.sh)
        okb = all(Ln[1][s]==Rn[1][s] for s in dom.sh)
        print(f"P3a sigma oplax-hexagon |S|={a}|T|={b}|U|={c}: fwd_eq={okf} bwd_eq={okb}")
    # P3b: r lax associativity hexagon
    for (a,b,c) in [(1,1,1),(2,1,1),(1,2,1),(1,1,2),(2,2,2),(2,3,2)]:
        print(f"P3b r lax-hexagon |S|={a}|T|={b}|U|={c}: {check_lax_hexagon(a,b,c)}")
    # sigma unit coherence
    print("sigma unit:", [(n, check_sigma_unit(n)) for n in [1,2,3]])
