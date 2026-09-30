#!/usr/bin/env python3
"""
LINCHPIN CHECK for the descent of o_nu.

Claim (Fact ii, the coupling part of B^2 subset Z^2): for ARBITRARY theta:H->D with
theta(0)=0, the diagonal coboundary
    beta  = d_+ theta                 (mu-twisted additive coboundary)
    taubar= d_o theta1,  theta1(h)=nu_h^{-1}(theta(h))   (sigma-twisted mult. coboundary)
    tau   = T(taubar),   tau(h1,h2)=nu_{h1 o h2}(taubar(h1,h2))
satisfies the coupling  P tau == Q beta  IDENTICALLY.

If so, o_nu(d_+ theta)=[Q(d_+theta)]=[P(tau)] in P(T Z^2_o) is ZERO, so o_nu descends
to H^2_+ WITHOUT presupposing existence of any brace with a prescribed residue.  We
supply valid good-triplets (nu,mu,sigma) from genuine braces but run over ARBITRARY
theta (independent of the brace's section) to isolate the formal identity.
"""
import itertools
exec(open("scratch/2026-09-29-o-nu-operator-check.py").read().split("if __name__")[0])

def harvest_triplet(br, E, Dset_list, s, Hlabels, quotient, isoD):
    """Return nu,mu,sigma as dicts label-> (Dabs-auto dict) plus H ops, on abstract D."""
    Dset=set(Dset_list); isoInv={isoD[d]:d for d in Dset_list}
    Dabs_elems=[isoD[d] for d in Dset_list]
    def Hplus(a,b): return quotient(E.add(s[a],s[b]))
    def Hcirc(a,b): return quotient(br.circ(s[a],s[b]))
    def Hneg(a):    return quotient(E.neg(s[a]))
    def Hlam(a,b):  return quotient(br.lamap(s[a],s[b]))
    nu={};mu={};sigma={}
    for h in Hlabels:
        sh=s[h]; shinv=br.circ_inv(sh)
        nu[h]={isoD[d]: isoD[br.lamap(sh,d)] for d in Dset_list}
        mu[h]={isoD[d]: isoD[E.add(E.add(E.neg(sh),d),sh)] for d in Dset_list}  # =id, E abelian
        sigma[h]={isoD[d]: isoD[br.circ(br.circ(sh,d),shinv)] for d in Dset_list}
    return nu,mu,sigma,Hplus,Hcirc,Hneg,Hlam,Dabs_elems

def auto_inv(auto, elems):
    return {v:k for k,v in auto.items()}

def check_identity(Dadd, Hlabels, zeroH, nu,mu,sigma, Hplus,Hcirc,Hneg,Hlam, ntheta=200):
    """Dadd: Ab on abstract D. Run random thetas, check P(T d_o theta1)=Q(d_+ theta)."""
    nz=[h for h in Hlabels if h!=zeroH]
    zero=Dadd.zero
    def ev2(f,a,b):
        if a==zeroH or b==zeroH: return zero
        return f[(a,b)]
    # operators
    def dplus(theta):   # (d_+theta)(h1,h2)=mu_{h2}(theta(h1))-theta(h1+h2)+theta(h2)
        f={}
        for h1 in nz:
            for h2 in nz:
                t1=mu[h2][theta.get(h1,zero)]
                t2=theta.get(Hplus(h1,h2),zero)
                t3=theta.get(h2,zero)
                f[(h1,h2)]=Dadd.add(Dadd.add(t1,Dadd.neg(t2)),t3)
        return f
    def dcirc(theta1): # (d_o theta1)(h1,h2)=sigma_{h2}(theta1(h1))-theta1(h1 o h2)+theta1(h2)
        f={}
        for h1 in nz:
            for h2 in nz:
                t1=sigma[h2][theta1.get(h1,zero)]
                t2=theta1.get(Hcirc(h1,h2),zero)
                t3=theta1.get(h2,zero)
                f[(h1,h2)]=Dadd.add(Dadd.add(t1,Dadd.neg(t2)),t3)
        return f
    nuinv={h:auto_inv(nu[h],Dadd.elems) for h in Hlabels}
    def T(taubar):
        return {(h1,h2): nu[Hcirc(h1,h2)][taubar[(h1,h2)]] for (h1,h2) in taubar}
    def P(tau):
        g={}
        for h1 in nz:
            for h2 in nz:
                for h3 in nz:
                    t1=mu[Hlam(h1,h3)][ev2(tau,h1,h2)]
                    t2=ev2(tau,h1,Hplus(h2,h3))
                    t3=ev2(tau,h1,h3)
                    g[(h1,h2,h3)]=Dadd.add(Dadd.add(t1,Dadd.neg(t2)),t3)
        return g
    def Q(beta):
        g={}
        for h1 in nz:
            for h2 in nz:
                for h3 in nz:
                    nb=nu[h1][ev2(beta,h2,h3)]
                    t2=mu[Hcirc(h1,h3)][ev2(beta,h1,Hneg(h1))]
                    t3=ev2(beta,Hneg(h1),Hcirc(h1,h3))
                    t4=ev2(beta,Hcirc(h1,h2),Hlam(h1,h3))
                    g[(h1,h2,h3)]=Dadd.add(Dadd.add(Dadd.add(nb,t2),Dadd.neg(t3)),Dadd.neg(t4))
        return g
    # exhaustive if small, else random-ish (deterministic scan)
    thetas=[]
    allmaps=list(itertools.product(Dadd.elems,repeat=len(nz)))
    for vals in allmaps:
        thetas.append({h:v for h,v in zip(nz,vals)})
    nfail=0
    for theta in thetas:
        theta1={h: nuinv[h][theta[h]] for h in nz}
        beta=dplus(theta); taubar=dcirc(theta1); tau=T(taubar)
        if P(tau)!=Q(beta): nfail+=1
    return len(thetas),nfail

if __name__=="__main__":
    print("="*70)
    print("LINCHPIN: P(T d_o theta1) == Q(d_+ theta) for ALL theta (formal identity)")
    print("="*70)
    allok=True
    cases=[]
    # H=Z/2,D=Z/4  (E=Z/8 supplies triplets with nu=+-1,sigma=+-1)
    cases.append(("H=Z2,D=Z4", Ab([8],"Z/8"),[(0,),(2,),(4,),(6,)],{0:(0,),1:(1,)},
                  [0,1],0,lambda x:x[0]%2,{(2*k,):(k,) for k in range(4)}, Ab([4],"D")))
    # H=Z/2,D=(Z/2)^2 via Z/4xZ/2
    cases.append(("H=Z2,D=(Z2)^2", Ab([4,2],"Z/4xZ/2"),
                  [(0,0),(2,0),(0,1),(2,1)],{0:(0,0),1:(1,0)},[0,1],0,lambda x:x[0]%2,
                  {(0,0):(0,0),(2,0):(1,0),(0,1):(0,1),(2,1):(1,1)}, Ab([2,2],"D")))
    # H=Z/3,D=Z/3 via Z/9
    cases.append(("H=Z3,D=Z3", Ab([9],"Z/9"),[(0,),(3,),(6,)],{0:(0,),1:(1,),2:(2,)},
                  [0,1,2],0,lambda x:x[0]%3,{(3*k,):(k,) for k in range(3)}, Ab([3],"D")))
    # H=Z/4,D=Z/4 via Z/16
    cases.append(("H=Z4,D=Z4", Ab([16],"Z/16"),[(4*k,) for k in range(4)],
                  {0:(0,),1:(1,),2:(2,),3:(3,)},[0,1,2,3],0,lambda x:x[0]%4,
                  {(4*k,):(k,) for k in range(4)}, Ab([4],"D")))

    for (name,E,Dl,s,Hl,zh,q,iso,Dadd) in cases:
        hol=Holomorph(E); regs=hol.regular_subgroups()
        ntrip=0; tot=0; fails=0
        seen_trip=set()
        for reg in regs:
            lam={a:i for (a,i) in reg}; br=Brace(E,hol,lam)
            if not is_ideal(br,set(Dl)): continue
            if not kernel_trivial_brace(br,set(Dl)): continue
            nu,mu,sigma,Hp,Hc,Hn,Hla,Del=harvest_triplet(br,E,Dl,s,Hl,q,iso)
            tkey=(tuple(sorted((h,tuple(sorted(nu[h].items()))) for h in Hl)),
                  tuple(sorted((h,tuple(sorted(sigma[h].items()))) for h in Hl)))
            if tkey in seen_trip: continue
            seen_trip.add(tkey); ntrip+=1
            n,nf=check_identity(Dadd,Hl,zh,nu,mu,sigma,Hp,Hc,Hn,Hla)
            tot+=n; fails+=nf
        ok=(fails==0)
        allok&=ok
        print(f"[{name}] distinct triplets={ntrip}, thetas checked={tot}, "
              f"identity holds on {tot-fails}/{tot}  {'OK' if ok else '*** FAIL ***'}")
    print("\nLINCHPIN (coboundary satisfies coupling, formally):",
          "PASS" if allok else "FAIL")
