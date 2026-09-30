#!/usr/bin/env python3
"""
TEST 2 (punchline): abstract  ker o_nu  ==  genuine  im phi^+ .

For a fixed good triplet (nu, mu=triv, sigma) on a trivial-brace kernel D and base
brace H, the theorem asserts

   { [beta] in H^2_+ : o_nu([beta]) = 0 }  =  { [beta] realised by a genuine skew
                                               brace with this triplet }.

We compute BOTH sides independently and compare, per triplet, for H=Z/2 and H=Z/3.

Abstract side:
  - build additive complex (op=+, action mu=triv) -> Z^2_+, B^2_+, H^2_+
  - build multiplicative complex (op=o on H, action sigma) -> Z^2_o
  - P(Z^2_o) subgroup of C^3;  o_nu([beta]) = [Q beta] mod P(Z^2_o)
Genuine side:
  - enumerate skew braces on each additive group E of order |D||H|; keep those with
    D a trivial-brace ideal; compute the induced triplet (nu,sigma) and class [beta];
    collect realised [beta] per triplet.
"""
import itertools
from collections import defaultdict

# ---------- reused Ab / Holomorph ----------
class Ab:
    def __init__(self,mods,name):
        self.mods=tuple(mods); self.name=name
        self.elems=[tuple(e) for e in itertools.product(*[range(m) for m in mods])]
        self.zero=tuple(0 for _ in mods); self.n=len(self.elems)
    def add(self,a,b): return tuple((x+y)%m for x,y,m in zip(a,b,self.mods))
    def neg(self,a):   return tuple((-x)%m for x,m in zip(a,self.mods))
    def smul(self,k,a):return tuple((k*x)%m for x,m in zip(a,self.mods))
    def autos(self):
        cand=[[v for v in self.elems if self.smul(m,v)==self.zero] for m in self.mods]
        res=[]
        for imgs in itertools.product(*cand):
            mp={}
            for a in self.elems:
                val=self.zero
                for ai,vi in zip(a,imgs): val=self.add(val,self.smul(ai,vi))
                mp[a]=val
            if len(set(mp.values()))==self.n: res.append(mp)
        return res

class Holomorph:
    def __init__(self,A):
        self.A=A; self.autos=A.autos()
        self.key2idx={tuple(m[a] for a in A.elems):i for i,m in enumerate(self.autos)}
        self.naut=len(self.autos); self.id_idx=self.key2idx[tuple(A.elems)]
        self.comp=[[self.key2idx[tuple(self.autos[i][self.autos[j][a]] for a in A.elems)]
                    for j in range(self.naut)] for i in range(self.naut)]
        self.inv=[next(j for j in range(self.naut) if self.comp[i][j]==self.id_idx)
                  for i in range(self.naut)]
    def mult(self,x,y):
        a,i=x;b,j=y; return (self.A.add(a,self.autos[i][b]),self.comp[i][j])
    def identity(self): return (self.A.zero,self.id_idx)
    def elements(self): return [(a,i) for a in self.A.elems for i in range(self.naut)]
    def reg_closure(self,gens):
        ident=self.identity(); tp={ident[0]:ident}; S={ident}
        for g in gens:
            a=g[0]
            if a in tp:
                if tp[a]!=g: return None
            else: tp[a]=g; S.add(g)
        changed=True
        while changed:
            changed=False
            for x in list(S):
                for y in list(S):
                    z=self.mult(x,y)
                    if z not in S:
                        a=z[0]
                        if a in tp:
                            if tp[a]!=z: return None
                        else: tp[a]=z;S.add(z);changed=True
        return frozenset(S)
    def regular_subgroups(self):
        nA=self.A.n; start=frozenset([self.identity()])
        found={start};work=[start];regs=set();hol=self.elements()
        while work:
            S=work.pop()
            if len(S)==nA: regs.add(S);continue
            used={s[0] for s in S}
            for g in hol:
                if g[0] in used: continue
                newS=self.reg_closure(list(S)+[g])
                if newS is None: continue
                if newS not in found: found.add(newS);work.append(newS)
        return list(regs)

# ---------- abstract cochain machinery over abelian D ----------
class Coh:
    """Normalised inhomogeneous cochains for a finite group (Helems, op) acting on
       abelian D via right action act: label -> (D-auto as dict)."""
    def __init__(self, D, Helems, op, act, zeroH):
        self.D=D; self.H=Helems; self.op=op; self.act=act; self.zeroH=zeroH
        self.nz=[h for h in Helems if h!=zeroH]
    # cochain = dict on tuples of non-zero H-labels -> D elem (normalised: 0 else)
    def eval2(self,f,h1,h2):
        if h1==self.zeroH or h2==self.zeroH: return self.D.zero
        return f[(h1,h2)]
    def d1(self,theta):
        # theta: dict nz->D ; returns 2-cochain
        f={}
        for h1 in self.nz:
            for h2 in self.nz:
                t1=self.act[h2][theta.get(h1,self.D.zero)]
                t2=theta.get(self.op(h1,h2),self.D.zero)
                t3=theta.get(h2,self.D.zero)
                f[(h1,h2)]=self.D.add(self.D.add(t1,self.D.neg(t2)),t3)
        return f
    def d2(self,f):
        # f 2-cochain -> 3-cochain.  Right-module convention consistent with d1:
        #   (d2 f)(h1,h2,h3)= act_{h3}(f(h1,h2)) + f(h1 op h2,h3) - f(h1,h2 op h3) - f(h2,h3)
        # (signs derived by forcing d2 o d1 = 0; act is the RIGHT action
        #  act_{h3}act_{h2}=act_{h2 op h3}, i.e. sigma an anti-hom.)
        g={}
        for h1 in self.nz:
            for h2 in self.nz:
                for h3 in self.nz:
                    a=self.act[h3][self.eval2(f,h1,h2)]
                    b=self.eval2(f,self.op(h1,h2),h3)
                    c=self.eval2(f,h1,self.op(h2,h3))
                    e=self.eval2(f,h2,h3)
                    g[(h1,h2,h3)]=self.D.add(self.D.add(self.D.add(a,b),self.D.neg(c)),self.D.neg(e))
        return g
    def all_2cochains(self):
        keys=[(h1,h2) for h1 in self.nz for h2 in self.nz]
        for vals in itertools.product(self.D.elems,repeat=len(keys)):
            yield dict(zip(keys,vals))
    def all_1cochains(self):
        keys=list(self.nz)
        for vals in itertools.product(self.D.elems,repeat=len(keys)):
            yield dict(zip(keys,vals))
    def zero3(self):
        return {(h1,h2,h3):self.D.zero for h1 in self.nz for h2 in self.nz for h3 in self.nz}
    def is_zero3(self,g): return all(v==self.D.zero for v in g.values())

def add2(D,f1,f2): return {k:D.add(f1[k],f2[k]) for k in f1}
def neg2(D,f):     return {k:D.neg(v) for k,v in f.items()}

# ---------- the theorem's operators P,Q (mu trivial) ----------
def make_PQ(D, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam, nu):
    nz=[h for h in Helems if h!=zeroH]
    def ev(f,a,b):
        if a==zeroH or b==zeroH: return D.zero
        return f[(a,b)]
    def P(tau):
        g={}
        for h1 in nz:
            for h2 in nz:
                for h3 in nz:
                    t1=ev(tau,h1,h2)                 # mu trivial
                    t2=ev(tau,h1,Hplus(h2,h3))
                    t3=ev(tau,h1,h3)
                    g[(h1,h2,h3)]=D.add(D.add(t1,D.neg(t2)),t3)
        return g
    def Q(beta):
        g={}
        for h1 in nz:
            for h2 in nz:
                for h3 in nz:
                    nb=nu[h1][ev(beta,h2,h3)]
                    t2=ev(beta,h1,Hneg(h1))          # mu trivial
                    t3=ev(beta,Hneg(h1),Hcirc(h1,h3))
                    t4=ev(beta,Hcirc(h1,h2),Hlam(h1,h3))
                    g[(h1,h2,h3)]=D.add(D.add(D.add(nb,t2),D.neg(t3)),D.neg(t4))
        return g
    return P,Q

def key3(g): return tuple(sorted(g.items()))

# ---------- abstract predictor ----------
def abstract_kernel(D, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam, mu, sigma, nu):
    add_coh=Coh(D,Helems,Hplus, mu, zeroH)
    mul_coh=Coh(D,Helems,Hcirc,sigma,zeroH)
    # sanity d2 o d1 = 0
    for theta in itertools.islice(add_coh.all_1cochains(),5):
        assert add_coh.is_zero3(add_coh.d2(add_coh.d1(theta))), "additive d2d1!=0"
    for theta in itertools.islice(mul_coh.all_1cochains(),5):
        assert mul_coh.is_zero3(mul_coh.d2(mul_coh.d1(theta))), "mult d2d1!=0"
    # Z^2_+ , B^2_+
    Z2p=[f for f in add_coh.all_2cochains() if add_coh.is_zero3(add_coh.d2(f))]
    B2p=set()
    for theta in add_coh.all_1cochains():
        f=add_coh.d1(theta); B2p.add(tuple(sorted(f.items())))
    # H^2_+ as cosets
    def bkey(f): return tuple(sorted(f.items()))
    cosets={}
    for f in Z2p:
        # coset rep: canonical min over f+B2p
        orbit=[]
        for bk in B2p:
            b=dict(bk); orbit.append(bkey(add2(D,f,b)))
        rep=min(orbit)
        cosets.setdefault(rep,[]).append(f)
    # Z^2_o = { taubar : d_o taubar = 0 } (RY multiplicative cocycle, sigma-twisted).
    # The variable in P is tau = nu_o(taubar):  tau(h1,h2)=nu_{h1 o h2}(taubar(h1,h2)).
    Z2o=[f for f in mul_coh.all_2cochains() if mul_coh.is_zero3(mul_coh.d2(f))]
    P,Q=make_PQ(D,Helems,zeroH,Hplus,Hcirc,Hneg,Hlam,nu)
    def T(taubar):
        return {(h1,h2): nu[Hcirc(h1,h2)][taubar[(h1,h2)]]
                for (h1,h2) in taubar}
    PZ=set()
    for f in Z2o: PZ.add(key3(P(T(f))))
    # close under subgroup ops (it should already be a subgroup, but ensure)
    # (P is linear and Z2o a group, so image is a subgroup; just collect)
    # kernel of o_nu: cosets [beta] with Q(beta) in PZ
    ker=set()
    for rep,fs in cosets.items():
        beta=fs[0]
        if key3(Q(beta)) in PZ:
            ker.add(rep)
    return cosets, ker, bkey

# ---------- genuine side ----------
class Brace:
    def __init__(self,E,hol,lam): self.E=E;self.hol=hol;self.lam=lam
    def circ(self,a,b): return self.E.add(a,self.hol.autos[self.lam[a]][b])
    def lamap(self,a,b): return self.hol.autos[self.lam[a]][b]
    def circ_inv(self,a): return self.hol.autos[self.hol.inv[self.lam[a]]][self.E.neg(a)]

def genuine_realised(Dabs, Helems, zeroH, additive_groups, bkey_of):
    """additive_groups: list of (E, Dset(list), section dict, quotient fn, isoD).
       isoD maps a kernel element of E (as it sits in E) to the abstract group Dabs.
       Returns dict: triplet-key -> set of [beta]-cosets realised.
       Triplet nu,sigma are expressed as autos of the ABSTRACT Dabs."""
    out=defaultdict(set)
    for (E,Dset_list,s,quotient,isoD) in additive_groups:
        Dset=set(Dset_list)
        isoInv={isoD[d]:d for d in Dset_list}    # abstract -> kernel-in-E
        hol=Holomorph(E); regs=hol.regular_subgroups()
        for reg in regs:
            lam={a:i for (a,i) in reg}; br=Brace(E,hol,lam)
            if any(br.lamap(a,d) not in Dset for a in E.elems for d in Dset): continue
            ok=True
            for a in E.elems:
                ainv=br.circ_inv(a)
                for d in Dset:
                    if br.circ(br.circ(a,d),ainv) not in Dset: ok=False;break
                if not ok: break
            if not ok: continue
            if any(br.lamap(d,e)!=e for d in Dset for e in Dset): continue  # trivial kernel
            # triplet nu,sigma : H -> Aut(Dabs), via isoD conjugation (raw, one iso)
            nu0={}; sigma0={}
            for h in Helems:
                sh=s[h]; shinv=br.circ_inv(sh)
                nu0[h]={dp: isoD[br.lamap(sh, isoInv[dp])] for dp in Dabs.elems}
                sigma0[h]={dp: isoD[br.circ(br.circ(sh, isoInv[dp]), shinv)] for dp in Dabs.elems}
            # beta cochain (in Dabs)
            def Hplus(h1,h2): return quotient(E.add(s[h1],s[h2]))
            beta0={}
            for h1 in Helems:
                for h2 in Helems:
                    if h1==zeroH or h2==zeroH: continue
                    bE=E.add(E.add(E.neg(s[Hplus(h1,h2)]),s[h1]),s[h2])
                    beta0[(h1,h2)]=isoD[bE]
            # Aut(Dabs)-saturate: the choice of iso D~=Dabs is free; relabelling by
            # phi in Aut(Dabs) conjugates the triplet and pushes beta by phi.
            for phi in Dabs.autos():
                phinv={v:k for k,v in phi.items()}
                nu={}; sigma={}
                for h in Helems:
                    nu[h]=tuple(sorted({dp:phi[nu0[h][phinv[dp]]] for dp in Dabs.elems}.items()))
                    sigma[h]=tuple(sorted({dp:phi[sigma0[h][phinv[dp]]] for dp in Dabs.elems}.items()))
                beta={k:phi[v] for k,v in beta0.items()}
                tkey=(tuple(sorted(nu.items())),tuple(sorted(sigma.items())))
                out[tkey].add(bkey_of(beta))
    return out

# ======================================================================
def canon_auto(D, autodict_on_D):
    # represent an auto of D by tuple of images over D.elems
    return tuple(autodict_on_D[d] for d in D.elems)

def run(Dmods, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam, additive_groups, label):
    print("="*70); print("CASE",label); print("="*70)
    D=Ab(Dmods,"D")
    Dautos=Ab(Dmods,"D").autos()
    # We'll compare per triplet. First get genuine realised sets, and infer which
    # (nu,sigma) triplets actually occur; for each, compute abstract kernel.
    # Build bkey via additive complex (mu trivial).
    mu_triv={h:{d:d for d in D.elems} for h in Helems}
    add_coh=Coh(D,Helems,Hplus,mu_triv,zeroH)
    def bkey_of(beta):
        f={(h1,h2):beta[(h1,h2)] for h1 in Helems for h2 in Helems if h1!=zeroH and h2!=zeroH}
        # reduce mod B^2_+ : canonical coset rep
        B=[]
        for theta in add_coh.all_1cochains():
            B.append(add_coh.d1(theta))
        orbit=[tuple(sorted(add2(D,f,b).items())) for b in B]
        return min(orbit)
    genuine=genuine_realised(D,Helems,zeroH,additive_groups,bkey_of)
    if not genuine:
        print("  (no genuine trivial-kernel braces found)"); return True

    # For each occurring triplet, build nu/sigma as label->autodict and compute kernel
    n_match=0; n_tot=0
    for tkey,realset in sorted(genuine.items()):
        nu_items,sig_items=tkey
        nu={}; sigma={}
        for h,items in nu_items:
            nu[h]={d:v for d,v in items}
        for h,items in sig_items:
            sigma[h]={d:v for d,v in items}
        # extend nu,sigma to full D-autos (they're defined on Dset only = all of D here)
        # need them as full maps D.elems->D.elems; Dset = D.elems (D is the kernel group)
        mu_triv2={h:{d:d for d in D.elems} for h in Helems}
        cosets,ker,bk=abstract_kernel(D,Helems,zeroH,Hplus,Hcirc,Hneg,Hlam,
                                      mu_triv2,sigma,nu)
        n_tot+=1
        match = (ker==realset)
        if match: n_match+=1
        # readable nu,sigma summary on a generator of D
        gen=D.elems[1]
        nu_desc={h:nu[h][gen] for h in Helems if h!=zeroH}
        sig_desc={h:sigma[h][gen] for h in Helems if h!=zeroH}
        print(f"  triplet nu(gen)={nu_desc} sigma(gen)={sig_desc}: "
              f"|H^2_+|={len(cosets)}  genuine|im|={len(realset)}  ker|o_nu|={len(ker)}  "
              f"{'MATCH' if match else '*** MISMATCH ***'}")
        if not match:
            print("     realised:",sorted(realset)[:3])
            print("     kernel  :",sorted(ker)[:3])
    print(f"  => {n_match}/{n_tot} triplets match")
    return n_match==n_tot

if __name__=="__main__":
    allok=True
    # ---------------- H = Z/2, D = Z/4 ----------------
    # H labels {0,1}; +,o both Z/2 (single group), lam trivial
    Hp=lambda a,b:(a+b)%2; Hc=Hp; Hn=lambda a:(-a)%2; Hl=lambda a,b:b
    Z8=Ab([8],"Z/8"); D8=[(0,),(2,),(4,),(6,)]; s8={0:(0,),1:(1,)}; q8=lambda x:x[0]%2
    iso8={(2*k,):(k,) for k in range(4)}                       # 2Z/8 -> Z/4
    Z2Z4=Ab([2,4],"Z2xZ4"); Dz=[(0,y) for y in range(4)]; sz={0:(0,0),1:(1,0)}; qz=lambda x:x[0]%2
    isoz={(0,y):(y,) for y in range(4)}                        # {0}xZ/4 -> Z/4
    ag2=[(Z8,D8,s8,q8,iso8),(Z2Z4,Dz,sz,qz,isoz)]
    allok &= run([4],[0,1],0,Hp,Hc,Hn,Hl,ag2,"H=Z/2, D=Z/4")

    # ---------------- H = Z/2, D = (Z/2)^2  (Aut(D)=S3, nontrivial nu,sigma) ------
    E8=Ab([2,2,2],"(Z/2)^3"); D8b=[(0,y,z) for y in range(2) for z in range(2)]
    s8b={0:(0,0,0),1:(1,0,0)}; q8b=lambda x:x[0]%2
    iso8b={(0,y,z):(y,z) for y in range(2) for z in range(2)}
    Z4Z2=Ab([4,2],"Z/4xZ/2")
    D4b=[(0,0),(2,0),(0,1),(2,1)]; s4b={0:(0,0),1:(1,0)}; q4b=lambda x:x[0]%2
    iso4b={(0,0):(0,0),(2,0):(1,0),(0,1):(0,1),(2,1):(1,1)}
    agV=[(E8,D8b,s8b,q8b,iso8b),(Z4Z2,D4b,s4b,q4b,iso4b)]
    allok &= run([2,2],[0,1],0,Hp,Hc,Hn,Hl,agV,"H=Z/2, D=(Z/2)^2")

    # ---------------- H = Z/3, D = Z/3 ----------------
    Hp3=lambda a,b:(a+b)%3; Hc3=Hp3; Hn3=lambda a:(-a)%3; Hl3=lambda a,b:b
    Z9=Ab([9],"Z/9"); D9=[(0,),(3,),(6,)]; s9={0:(0,),1:(1,),2:(2,)}; q9=lambda x:x[0]%3
    iso9={(3*k,):(k,) for k in range(3)}
    Z3Z3=Ab([3,3],"Z3xZ3"); D33=[(0,y) for y in range(3)]; s33={0:(0,0),1:(1,0),2:(2,0)}; q33=lambda x:x[0]%3
    iso33={(0,y):(y,) for y in range(3)}
    ag3=[(Z9,D9,s9,q9,iso9),(Z3Z3,D33,s33,q33,iso33)]
    allok &= run([3],[0,1,2],0,Hp3,Hc3,Hn3,Hl3,ag3,"H=Z/3, D=Z/3")

    print("\nOVERALL ker o_nu == im phi^+ :", "PASS" if allok else "FAIL")
