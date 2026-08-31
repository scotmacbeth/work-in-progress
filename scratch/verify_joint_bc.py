"""
JOINT (shape x position) Beck-Chevalley & Frobenius for Cont(cod) = Fam(cod^op).

Closes the gap in 2026-08-28-cont-cod-fibration.md (node shape-level-hyperdoctrine):
  - shape-level quantifiers exist (Fam-Kan along u:S->S'):
        exists_j = Lan_u = fibrewise COPRODUCT in (Set/P)^op = PRODUCT in Set/P
        forall_j = Ran_u = fibrewise PRODUCT   in (Set/P)^op = COPRODUCT in Set/P
    (consistent with Thm 5.2: container-exists uses Set product, container-forall uses Set sum)
  - shape quantifier adjunctions   exists_j -| j^* -| forall_j    (hom-count check)
  - the exchange square (shape-pure j vs position-pure r) IS a pullback in Cont(Set)=Poly
  - JOINT Beck-Chevalley over it:  forall-side HOLDS, exists-side FAILS (sum-of-products gap)
  - same-type shape BC over a shape-pullback square (Fam BC): HOLDS for both
  - Frobenius for the shape existential.

A predicate over a container (S,{P_s}) is an object of prod_s (Set/P_s)^op:
  a family  Phi = { Phi[s] : E_s -> P_s }  of witness bundles (SliceObj per shape).
"""
from itertools import product
from collections import Counter

# ---------- Set/B primitives ----------
class SliceObj:
    def __init__(self,A,f): self.A=tuple(A); self.f=dict(f)
    def __repr__(self): return f"({list(self.A)}->{[self.f[a] for a in self.A]})"

def profile(o,B):                      # fibre sizes over base B
    c=Counter(o.f[a] for a in o.A)
    return tuple(c.get(b,0) for b in B)

def Sigma(f,obj):                      # Sigma_f post-compose ; obj over X, f:X->Y -> over Y
    return SliceObj(obj.A, {a: f[obj.f[a]] for a in obj.A})

def slice_iso(o1,o2,B):                # iso in Set/B  <=>  equal fibre-size profile
    return profile(o1,B)==profile(o2,B)

def slice_prod_list(objs,B):           # product in Set/B (iterated fibre product); [] -> terminal id_B
    tot=[]; m={}
    for combo in product(*[o.A for o in objs]):
        bs={objs[i].f[combo[i]] for i in range(len(objs))}
        if len(bs)<=1:
            b = combo and objs[0].f[combo[0]]
            if not objs:
                continue
            if len(bs)==1:
                e=combo; tot.append(e); m[e]=next(iter(bs))
    if not objs:                       # terminal object of Set/B : one witness per base pt
        return SliceObj(list(B), {b:b for b in B})
    return SliceObj(tot,m)

def slice_coprod_list(objs,B):         # coproduct in Set/B (disjoint union); [] -> initial 0->B
    tot=[]; m={}
    for i,o in enumerate(objs):
        for a in o.A:
            e=(i,a); tot.append(e); m[e]=o.f[a]
    return SliceObj(tot,m)

def hom_count_slice(a,b,B):            # |Hom_{Set/B}(a,b)| = prod_p (n^b_p)^(n^a_p)
    na=profile(a,B); nb=profile(b,B)
    r=1
    for i in range(len(B)):
        r*= nb[i]**na[i]
    return r

# ---------- container-level ----------
# container: (S tuple, P dict s->tuple positions)
# predicate: dict s -> SliceObj over P[s]

def jstar(u, Phi_tgt):
    # j=(u,{id}): (S,{P'[u s]}) -> (S',P').  j^*: fibre(tgt)->fibre(src)
    return {s: Phi_tgt[u[s]] for s in u}

def exists_j(u, S, Sp, Pp, Phi_src):
    # (S,{Pp[u s]}) --> (S',Pp).  (exists_j Phi)[s'] = product in Set/Pp[s'] over fibre u^{-1}(s')
    out={}
    for sp in Sp:
        objs=[Phi_src[s] for s in S if u[s]==sp]
        out[sp]=slice_prod_list(objs, Pp[sp])
    return out

def forall_j(u, S, Sp, Pp, Phi_src):
    out={}
    for sp in Sp:
        objs=[Phi_src[s] for s in S if u[s]==sp]
        out[sp]=slice_coprod_list(objs, Pp[sp])
    return out

def rstar(tau, Phi_tgt):
    # r=(id,{tau[s']:P'[s']->R[s']}): (S',R)->(S',P').  r^*=(Sigma_tau)^op pointwise
    return {sp: Sigma(tau[sp], Phi_tgt[sp]) for sp in Phi_tgt}

# ================= tests =================
def gen_bundles(P, maxA=2):
    pool=('e','f','g','h')
    out=[]
    for n in range(0,maxA+1):
        A=pool[:n]
        for vals in product(P, repeat=n):
            out.append(SliceObj(A,{a:v for a,v in zip(A,vals)}))
    return out

def gen_preds(S,P,maxA=2):
    perS={s:gen_bundles(P[s],maxA) for s in S}
    keys=list(S)
    for combo in product(*[perS[s] for s in keys]):
        yield {s:combo[i] for i,s in enumerate(keys)}

def test_shape_adjunction():
    # u: S={a,b,c}->S'={x,y}
    S=('a','b','c'); Sp=('x','y')
    u={'a':'x','b':'x','c':'y'}
    Pp={'x':(0,1),'y':(0,)}
    # source container positions: P_src[s]=Pp[u[s]]
    Psrc={s:Pp[u[s]] for s in S}
    okL=okR=True
    src_preds=list(gen_preds(S,Psrc,maxA=2))
    tgt_preds=list(gen_preds(Sp,Pp,maxA=2))
    # exists_j -| j^* :  Hom_src(Phi, j^*Psi) = Hom_tgt(exists_j Phi, Psi)
    import random
    random.seed(1)
    sample_src=random.sample(src_preds, min(len(src_preds),40))
    sample_tgt=random.sample(tgt_preds, min(len(tgt_preds),40))
    for Phi in sample_src:
        Ej=exists_j(u,S,Sp,Pp,Phi)
        Fj=forall_j(u,S,Sp,Pp,Phi)
        for Psi in sample_tgt:
            jPsi=jstar(u,Psi)
            # Hom over source container = prod_s Hom_{(Set/Psrc[s])^op}(Phi[s],jPsi[s])
            #   = prod_s Hom_{Set/Psrc[s]}(jPsi[s], Phi[s])
            lhsL=1
            for s in S: lhsL*=hom_count_slice(jPsi[s], Phi[s], Psrc[s])
            rhsL=1
            for sp in Sp: rhsL*=hom_count_slice(Psi[sp], Ej[sp], Pp[sp])
            if lhsL!=rhsL: okL=False
            # j^* -| forall_j : Hom_src(j^*Psi, Phi) = Hom_tgt(Psi, forall_j Phi)
            #   src: prod_s Hom_{(Set/-)^op}(jPsi[s],Phi[s]) = prod_s Hom_{Set/-}(Phi[s], jPsi[s])
            lhsR=1
            for s in S: lhsR*=hom_count_slice(Phi[s], jPsi[s], Psrc[s])
            rhsR=1
            for sp in Sp: rhsR*=hom_count_slice(Fj[sp], Psi[sp], Pp[sp])
            if lhsR!=rhsR: okR=False
    print(f"[{'OK' if okL else 'FAIL'}] shape adjunction  exists_j -| j^*")
    print(f"[{'OK' if okR else 'FAIL'}] shape adjunction  j^* -| forall_j")
    return okL and okR

# ---- Poly (Cont(Set)) morphisms & exchange-square pullback UP ----
def poly_compose(m2,m1):
    # m1=(u,rho):(S,P)->(S',P'), m2=(v,sig):(S',P')->(S'',P'')  ; returns (v u, {rho[s] o sig[u s]})
    (u,rho)=m1; (v,sig)=m2
    w={s:v[u[s]] for s in u}
    pos={}
    for s in u:
        r=rho[s]; sg=sig[u[s]]          # sg: P''[v u s]->P'[u s], r: P'[u s]->P[s]
        pos[s]={p:r[sg[p]] for p in sg}
    return (w,pos)

def poly_eq(m1,m2):
    (u1,r1)=m1;(u2,r2)=m2
    if u1!=u2: return False
    for s in u1:
        if r1[s]!=r2[s]: return False
    return True

def all_poly_morphisms(SP_src, SP_tgt, maxpos=None):
    (S,P)=SP_src; (Sp,Pp)=SP_tgt
    # u:S->Sp ; rho[s]: Pp[u s]->P[s]
    for uvals in product(Sp, repeat=len(S)):
        u={s:uvals[i] for i,s in enumerate(S)}
        # for each s choose rho[s]:Pp[u s]->P[s]
        choice_space=[]
        for s in S:
            dom=Pp[u[s]]; cod=P[s]
            fs=[{d:v for d,v in zip(dom,vals)} for vals in product(cod,repeat=len(dom))]
            choice_space.append(fs)
        for combo in product(*choice_space):
            rho={s:combo[i] for i,s in enumerate(S)}
            yield (u,rho)

def test_exchange_is_pullback():
    """cospan  j:(S,{Pp[u s]})->(S',Pp)   r:(S',R)->(S',Pp)
       claim PB = (S,{R[u s]}) with r'=(id,{tau[u s]}), j'=(u,{id}).
       Verify universal property on small test cones T."""
    S=('a','b'); Sp=('x',); u={'a':'x','b':'x'}
    Pp={'x':(0,1)}; R={'x':(0,)}
    tau={'x':{0:0,1:0}}                      # tau[x]:Pp[x]->R[x]
    # containers
    Csrc_j=(S,{s:Pp[u[s]] for s in S})       # (S,{Pp[u s]})
    Ctgt =(Sp,Pp)                            # (S',Pp)
    Csrc_r=(Sp,R)                            # (S',R)
    PB=(S,{s:R[u[s]] for s in S})            # candidate pullback (S,{R[u s]})
    # cospan legs
    j=(u,{s:{p:p for p in Pp[u[s]]} for s in S})     # (u,{id}) : Csrc_j->Ctgt
    r=({sp:sp for sp in Sp}, {sp:tau[sp] for sp in Sp})  # (id,{tau}) : Csrc_r->Ctgt
    # candidate projections
    rp=({s:s for s in S}, {s:tau[u[s]] for s in S})  # r'=(id,{tau[u s]}): PB->Csrc_j
    jp=(u, {s:{p:p for p in R[u[s]]} for s in S})    # j'=(u,{id}): PB->Csrc_r
    # square commutes?
    if not poly_eq(poly_compose(j,rp), poly_compose(r,jp)):
        print("[FAIL] exchange square does not commute"); return False
    # UP over small test cones T
    testTs=[(('t',),{'t':(0,)}), (('t',),{'t':(0,1)}), (('t','u'),{'t':(0,),'u':(0,1)})]
    ok=True; checked=0
    for T in testTs:
        for a in all_poly_morphisms(T, Csrc_j):
            ja=poly_compose(j,a)
            for b in all_poly_morphisms(T, Csrc_r):
                if poly_eq(ja, poly_compose(r,b)):
                    # need unique m:T->PB with rp o m=a, jp o m=b
                    meds=[m for m in all_poly_morphisms(T, PB)
                          if poly_eq(poly_compose(rp,m),a) and poly_eq(poly_compose(jp,m),b)]
                    checked+=1
                    if len(meds)!=1: ok=False; print("  UP FAIL: #mediating=",len(meds))
    print(f"[{'OK' if ok else 'FAIL'}] exchange square is a pullback in Poly (UP, {checked} cones)")
    return ok

def test_joint_BC():
    """joint BC over exchange square:
         r^* o exists_j   vs   exists_j' o r'^*
         r^* o forall_j   vs   forall_j' o r'^*   """
    S=('a','b','c'); Sp=('x','y'); u={'a':'x','b':'x','c':'y'}
    Pp={'x':(0,1),'y':(0,)}; R={'x':(0,),'y':(0,)}
    tau={'x':{0:0,1:0},'y':{0:0}}
    Psrc={s:Pp[u[s]] for s in S}
    okE=okA=True; ce=ca=0
    import random; random.seed(3)
    preds=list(gen_preds(S,Psrc,maxA=2))
    for Phi in random.sample(preds, min(len(preds),120)):
        # LHS exists: r^*(exists_j Phi)
        Ej=exists_j(u,S,Sp,Pp,Phi)
        L_E=rstar(tau, Ej)                                   # over (Sp,R)
        # RHS exists: exists_j'( r'^* Phi )  ; r'^* uses tau[u s] per shape
        rpPhi={s:Sigma(tau[u[s]], Phi[s]) for s in S}        # over (S,{R[u s]})
        Rr={s:R[u[s]] for s in S}
        R_E=exists_j(u,S,Sp,R,rpPhi)                         # over (Sp,R)
        for sp in Sp:
            ce+=1
            if not slice_iso(L_E[sp],R_E[sp],R[sp]): okE=False
        # forall
        Fj=forall_j(u,S,Sp,Pp,Phi)
        L_A=rstar(tau, Fj)
        R_A=forall_j(u,S,Sp,R,rpPhi)
        for sp in Sp:
            ca+=1
            if not slice_iso(L_A[sp],R_A[sp],R[sp]): okA=False
    print(f"[{'OK' if okE else 'FAIL (expected)'}] joint BC exists-side  r^* exists_j = exists_j' r'^*   ({ce} checks)")
    print(f"[{'OK' if okA else 'FAIL'}] joint BC forall-side  r^* forall_j = forall_j' r'^*   ({ca} checks)")
    return okA, okE   # return (forall-holds, exists-holds)

def test_same_type_shape_BC():
    """shape-pullback square:  u:S->S'', v:S'->S''  ;  PB=S x_{S''} S'.
       positions all pulled from a base family Q over S''.
       BC:  vhat^* exists_u  =  exists_uhat vbar^*  (and forall)."""
    S2=('m','n'); Q={'m':(0,1),'n':(0,)}
    S=('a','b','c'); u={'a':'m','b':'m','c':'n'}
    Sp=('p','q'); v={'p':'m','q':'n'}
    # containers with positions Q[shape's image]
    PS={s:Q[u[s]] for s in S}
    PSp={sp:Q[v[sp]] for sp in Sp}
    # pullback of shapes: PB={(s,sp): u[s]=v[sp]}
    PBsh=[(s,sp) for s in S for sp in Sp if u[s]==v[sp]]
    # maps out of PB: uhat:(s,sp)->sp (over v),  vbar:(s,sp)->s (over u)
    uhat={x:x[1] for x in PBsh}    # PB -> Sp   (shape map, image v)
    vbar={x:x[0] for x in PBsh}    # PB -> S
    PPB={x:Q[u[x[0]]] for x in PBsh}   # positions Q[common image]
    # We test BC for quantifying along u (S->S2) then restricting along v (Sp->S2):
    #   v^* (exists_u Phi)   vs   exists_uhat (vbar^* Phi)     both land over Sp
    okE=okA=True; ce=ca=0
    import random; random.seed(5)
    preds=list(gen_preds(S,PS,maxA=2))
    for Phi in random.sample(preds,min(len(preds),120)):
        # exists_u Phi over (S2,Q)
        Eu=exists_j(u,S,S2,Q,Phi)
        # v^* : restrict family along v  (shape-pure jstar with map v)
        L=jstar(v, Eu)                       # over Sp
        # vbar^* Phi : restrict Phi along vbar -> family over PB
        vbarPhi={x:Phi[vbar[x]] for x in PBsh}
        # exists_uhat over PB->Sp
        R=exists_j(uhat, PBsh, Sp, PSp, vbarPhi)
        for sp in Sp:
            ce+=1
            if not slice_iso(L[sp],R[sp],PSp[sp]): okE=False
        Fu=forall_j(u,S,S2,Q,Phi)
        La=jstar(v,Fu)
        Ra=forall_j(uhat, PBsh, Sp, PSp, vbarPhi)
        for sp in Sp:
            ca+=1
            if not slice_iso(La[sp],Ra[sp],PSp[sp]): okA=False
    print(f"[{'OK' if okE else 'FAIL'}] same-type shape BC (exists)   ({ce} checks)")
    print(f"[{'OK' if okA else 'FAIL'}] same-type shape BC (forall)   ({ca} checks)")
    return okE and okA

def _frob_generic(Q, S, Sp, u, Pp, Psrc, prodname):
    """Test Frobenius  Q_j( Phi (x) j^*Psi ) = Q_j Phi (x) Psi
       for quantifier Q in {exists_j,forall_j} and (x) a chosen fibre binary op."""
    if prodname=='wedge':   # container /\ = categorical product of fibre (Set/P)^op = COPRODUCT in Set/P
        binop=lambda o1,o2,B: slice_coprod_list([o1,o2],B)
    else:                   # container \/ = categorical coproduct of fibre = PRODUCT in Set/P
        binop=lambda o1,o2,B: slice_prod_list([o1,o2],B)
    ok=True;c=0
    import random; random.seed(7)
    sp_preds=list(gen_preds(S,Psrc,maxA=2)); tp_preds=list(gen_preds(Sp,Pp,maxA=2))
    for Phi in random.sample(sp_preds,min(len(sp_preds),40)):
        for Psi in random.sample(tp_preds,min(len(tp_preds),20)):
            jPsi=jstar(u,Psi)
            conj={s:binop(Phi[s], jPsi[s], Psrc[s]) for s in S}
            L=Q(u,S,Sp,Pp,conj)
            QPhi=Q(u,S,Sp,Pp,Phi)
            R={sp:binop(QPhi[sp],Psi[sp],Pp[sp]) for sp in Sp}
            for sp in Sp:
                c+=1
                if not slice_iso(L[sp],R[sp],Pp[sp]): ok=False
    return ok

def test_shape_frobenius():
    S=('a','b','c'); Sp=('x','y'); u={'a':'x','b':'x','c':'y'}
    Pp={'x':(0,1),'y':(0,)}; Psrc={s:Pp[u[s]] for s in S}
    results={}
    for Qname,Q in [('exists',exists_j),('forall',forall_j)]:
        for prodname in ['wedge','vee']:
            r=_frob_generic(Q,S,Sp,u,Pp,Psrc,prodname)
            results[(Qname,prodname)]=r
            print(f"    Frobenius {Qname}_j  with (x)={prodname:5s}: {'OK' if r else 'FAIL'}")
    # CONTROL: standard un-opped Set-family Frobenius  exists=coprod, /\=product
    #   over trivial positions (P=1 everywhere): exists_u{X_s}=sum, /\=product; Set distributive.
    Sc=('a','b','c'); Spc=('x','y'); uc={'a':'x','b':'x','c':'y'}
    Pc={'x':(0,),'y':(0,)}; Pscc={s:Pc[uc[s]] for s in Sc}
    def famExists(u,S,Sp,Pp,Phi):     # sum of profiles = coproduct in Set/P
        return forall_j(u,S,Sp,Pp,Phi)  # forall_j is coproduct-in-Set/P = the Set-family SUM
    # standard family: exists = SUM, conj = PRODUCT(fibre product)
    okctrl=True;cc=0
    import random; random.seed(11)
    sp=list(gen_preds(Sc,Pscc,maxA=3)); tp=list(gen_preds(Spc,Pc,maxA=3))
    for Phi in random.sample(sp,min(len(sp),30)):
        for Psi in random.sample(tp,min(len(tp),15)):
            jPsi=jstar(uc,Psi)
            conj={s:slice_prod_list([Phi[s],jPsi[s]],Pscc[s]) for s in Sc}   # x_Set/P
            L=famExists(uc,Sc,Spc,Pc,conj)
            E=famExists(uc,Sc,Spc,Pc,Phi)
            R={x:slice_prod_list([E[x],Psi[x]],Pc[x]) for x in Spc}
            for x in Spc:
                cc+=1
                if not slice_iso(L[x],R[x],Pc[x]): okctrl=False
    print(f"    CONTROL Set-family Frobenius (sum-exists, prod-conj): {'OK' if okctrl else 'FAIL'}  ({cc})")
    holds = any(results.values())
    return holds, results

def test_position_frobenius():
    """POSITION-level (along eta:(S,{1})->(S,{P_s})).  Audit of existing proof 6.2.
       Per shape independent; test one shape with P=P_s.
         A phi   = (Pi_!  phi)^op     : product over positions  -> profile-over-1 = prod_p n_p
         E phi   = (Sigma_! phi)^op   : total space             -> profile-over-1 = sum_p n_p
         Delta_c psi = (!^* psi)       : constant family P x psi -> profile all = |psi|
       Frobenius candidates (which quantifier Q, which fibre binop):
         Q( phi  (x)  Delta_c psi )  =?=  Q phi  (x)  psi        (RHS (x) over the 1-fibre)
       binop wedge = /\ = coprod in Set/P = SUM ;  vee = \/ = prod in Set/P = PRODUCT."""
    P=(0,1,2)
    def A_(phi):   # -> integer (size of set over 1)
        n=profile(phi,P); r=1
        for x in n: r*=x
        return r
    def E_(phi):
        return sum(profile(phi,P))
    def Deltac(k):     # constant family, |psi|=k -> bundle over P profile all k
        A=[(p,i) for p in P for i in range(k)]
        return SliceObj(A,{a:a[0] for a in A})
    def binop_fib(o1,o2,B,kind):
        return slice_coprod_list([o1,o2],B) if kind=='wedge' else slice_prod_list([o1,o2],B)
    def binop_1(a,b,kind):   # over terminal 1: sum or product of the two set-sizes
        return a+b if kind=='wedge' else a*b
    res={}
    for Qname,Q in [('A',A_),('E',E_)]:
        for kind in ['wedge','vee']:
            ok=True
            for phi in gen_bundles(P,maxA=3):
                for k in range(0,3):
                    dc=Deltac(k)
                    L=Q(binop_fib(phi,dc,P,kind))
                    R=binop_1(Q(phi), k, kind)
                    if L!=R: ok=False; break
                if not ok: break
            res[(Qname,kind)]=ok
            print(f"    position Frobenius  {Qname}(phi {kind} Delta_c psi)=Q phi {kind} psi : {'OK' if ok else 'FAIL'}")
    return res

def test_position_vs_shape_BC():
    """position quantifier (A along eta) commutes with shape substitution j^*=restriction.
       Trivial (shape subst just relabels fibres) but verify."""
    S=('a','b','c'); Sp=('x','y'); u={'a':'x','b':'x','c':'y'}   # shape subst along u
    Pp={'x':(0,1),'y':(0,)}
    # predicate over (Sp,Pp); A along eta gives predicate over (Sp,{1}); then j^*
    # vs j^* then A.  Should agree.
    def A_shapewise(Phi,Sset,Pdict):
        out={}
        for s in Sset:
            n=profile(Phi[s],Pdict[s]); r=1
            for x in n: r*=x
            out[s]=r   # size over 1
        return out
    ok=True;c=0
    import random; random.seed(9)
    preds=list(gen_preds(Sp,Pp,maxA=2))
    for Psi in random.sample(preds,min(len(preds),60)):
        # path1: A then j^* (restrict the size-family along u)
        Apsi=A_shapewise(Psi,Sp,Pp)
        L={s:Apsi[u[s]] for s in S}
        # path2: j^* then A
        jPsi=jstar(u,Psi); Psrc={s:Pp[u[s]] for s in S}
        R=A_shapewise(jPsi,S,Psrc)
        for s in S:
            c+=1
            if L[s]!=R[s]: ok=False
    print(f"    position-quantifier vs shape-substitution commute: {'OK' if ok else 'FAIL'} ({c})")
    return ok

if __name__=="__main__":
    print("=== shape quantifier adjunctions ===")
    a=test_shape_adjunction()
    print("=== exchange square is a pullback ===")
    b=test_exchange_is_pullback()
    print("=== joint (shape x position) BC over exchange square ===")
    fa,ex=test_joint_BC()
    print("=== same-type shape BC (Fam BC) ===")
    c=test_same_type_shape_BC()
    print("=== shape Frobenius (all combos + Set-family control) ===")
    d,dres=test_shape_frobenius()
    print("=== position Frobenius audit (A vs E) ===")
    pres=test_position_frobenius()
    print("=== position-quantifier vs shape-substitution ===")
    pv=test_position_vs_shape_BC()
    print("\nSUMMARY:")
    print("  shape adjunctions exists_j-|j^*-|forall_j :", "OK" if a else "FAIL")
    print("  exchange square is pullback              :", "OK" if b else "FAIL")
    print("  joint BC forall-side                     :", "OK" if fa else "FAIL")
    print("  joint BC exists-side                     :", "HOLDS" if ex else "FAILS (predicted: sum-of-products gap)")
    print("  same-type shape BC (both)                :", "OK" if c else "FAIL")
    print("  shape Frobenius (some combo holds)       :", "OK" if d else "FAILS for ALL combos")
