#!/usr/bin/env python3
"""
Decisive test of the o_nu machinery.

The theorem defines two linear operators on skew-brace 2-cochains (RY eq 3.10):

  (P tau)(h1,h2,h3) = mu_{lam_{h1}(h3)}(tau(h1,h2)) - tau(h1,h2+h3) + tau(h1,h3)
  (Q beta)(h1,h2,h3)= nu_{h1}(beta(h2,h3)) + mu_{h1 o h3}(beta(h1,-h1))
                        - beta(-h1, h1 o h3) - beta(h1 o h2, lam_{h1}(h3))

and the coupling (RY 3.10) is  P tau = Q beta.

TEST 1 (operator correctness): take a GENUINE skew brace G with a trivial-brace
ideal D, choose a section s:H->G, extract the honest cochains

  beta(h1,h2) = -s(h1+h2) + s(h1) + s(h2)                              in D
  tau (h1,h2) = -s(h1 o h2) + (s(h1) o s(h2))                          in D

and check  P tau == Q beta  identically.  If my P,Q transcribe (3.10) correctly,
this holds for EVERY genuine brace, for EVERY H.  We test H=Z/2 (orders 8,16) and
H=Z/3, H=Z/4 (trivial-brace kernels).

Since every additive group here is abelian, mu is trivial (mu_h = id).  We keep
mu in the formulas for fidelity but it evaluates to id.
"""

import itertools

# ----------------------------------------------------------------------
class Ab:
    def __init__(self, mods, name):
        self.mods = tuple(mods); self.name = name
        self.elems = [tuple(e) for e in itertools.product(*[range(m) for m in mods])]
        self.zero = tuple(0 for _ in mods); self.n = len(self.elems)
    def add(self,a,b): return tuple((x+y)%m for x,y,m in zip(a,b,self.mods))
    def neg(self,a):   return tuple((-x)%m for x,m in zip(a,self.mods))
    def smul(self,k,a):return tuple((k*x)%m for x,m in zip(a,self.mods))
    def autos(self):
        k=len(self.mods)
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
        self.naut=len(self.autos)
        self.id_idx=self.key2idx[tuple(A.elems)]
        self.comp=[[self.key2idx[tuple(self.autos[i][self.autos[j][a]] for a in A.elems)]
                    for j in range(self.naut)] for i in range(self.naut)]
        self.inv=[next(j for j in range(self.naut) if self.comp[i][j]==self.id_idx)
                  for i in range(self.naut)]
    def mult(self,x,y):
        a,i=x; b,j=y; return (self.A.add(a,self.autos[i][b]), self.comp[i][j])
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
                        else: tp[a]=z; S.add(z); changed=True
        return frozenset(S)
    def regular_subgroups(self):
        nA=self.A.n; ident=self.identity(); start=frozenset([ident])
        found={start}; work=[start]; regs=set(); hol=self.elements()
        while work:
            S=work.pop()
            if len(S)==nA: regs.add(S); continue
            used={s[0] for s in S}
            for g in hol:
                if g[0] in used: continue
                newS=self.reg_closure(list(S)+[g])
                if newS is None: continue
                if newS not in found: found.add(newS); work.append(newS)
        return list(regs)

# ----------------------------------------------------------------------
# Brace on additive group E given by lam: E -> auto-index (a o b = a + lam_a(b))
class Brace:
    def __init__(self, E, hol, lam):
        self.E=E; self.hol=hol; self.lam=lam
    def circ(self,a,b): return self.E.add(a, self.hol.autos[self.lam[a]][b])
    def lamap(self,a,b): return self.hol.autos[self.lam[a]][b]     # lambda_a(b)
    def circ_inv(self,a):
        ai=self.lam[a]; return self.hol.autos[self.hol.inv[ai]][self.E.neg(a)]

def is_ideal(br, Dset):
    E=br.E
    # lam_a preserves D, D normal in (E,o); (E,+) abelian so +-normal auto
    for a in E.elems:
        if {br.lamap(a,d) for d in Dset}!=Dset: return False
    for a in E.elems:
        ainv=br.circ_inv(a)
        for d in Dset:
            if br.circ(br.circ(a,d),ainv) not in Dset: return False
    return True

def kernel_trivial_brace(br, Dset):
    # D is a trivial brace iff a o b = a+b for a,b in D, i.e. lam_d|_D = id
    for d in Dset:
        for e in Dset:
            if br.lamap(d,e)!=e: return False
    return True

# ----------------------------------------------------------------------
# Given a genuine brace with trivial-brace ideal D and section s:H->E,
# extract beta,tau and the triplet nu,mu,sigma; then test P tau == Q beta.
def extract_and_check(br, D, Dset, H_elems, s, quotient):
    """H_elems: list of coset reps labels; s: dict label-> E-element (section);
       quotient: function E-elem -> H label."""
    E=br.E
    def Dsub(x): # x in D as tuple, return
        return x
    # triplet
    def nu(h):  # nu_h(x)=lam_{s(h)}(x)
        return lambda x,h=h: br.lamap(s[h], x)
    def mu(h):  # mu_h(x) = -s(h)+x+s(h) = x  (E abelian)
        return lambda x,h=h: x
    # group ops on H induced
    def Hplus(h1,h2): return quotient(E.add(s[h1],s[h2]))
    def Hcirc(h1,h2): return quotient(br.circ(s[h1],s[h2]))
    def Hneg(h1):     return quotient(E.neg(s[h1]))
    def Hlam(h1,h2):  return quotient(br.lamap(s[h1], s[h2]))
    # cochains beta,tau : H x H -> D  (as E-elements lying in D)
    def beta(h1,h2):
        return E.add(E.add(E.neg(s[Hplus(h1,h2)]), s[h1]), s[h2])
    def tau(h1,h2):
        return E.add(E.neg(s[Hcirc(h1,h2)]), br.circ(s[h1],s[h2]))
    # sanity: beta,tau land in D
    for h1 in H_elems:
        for h2 in H_elems:
            assert beta(h1,h2) in Dset, "beta not in D"
            assert tau(h1,h2)  in Dset, "tau not in D"
    # operators P,Q  (mu trivial)
    def P(h1,h2,h3):
        t1=tau(h1,h2); t2=tau(h1,Hplus(h2,h3)); t3=tau(h1,h3)
        return E.add(E.add(t1, E.neg(t2)), t3)
    def Q(h1,h2,h3):
        nb = nu(h1)(beta(h2,h3))
        t2 = beta(h1, Hneg(h1))                        # mu trivial
        t3 = beta(Hneg(h1), Hcirc(h1,h3))
        t4 = beta(Hcirc(h1,h2), Hlam(h1,h3))
        return E.add(E.add(E.add(nb, t2), E.neg(t3)), E.neg(t4))
    ok=True
    for h1 in H_elems:
        for h2 in H_elems:
            for h3 in H_elems:
                if P(h1,h2,h3)!=Q(h1,h2,h3):
                    ok=False
                    return False, (h1,h2,h3,P(h1,h2,h3),Q(h1,h2,h3))
    return True, None

# ----------------------------------------------------------------------
def run_family(E, Dset_list, gen_desc, s, H_elems, quotient, label):
    hol=Holomorph(E); regs=hol.regular_subgroups()
    Dset=set(Dset_list)
    n_checked=0; n_triv=0; n_fail=0; fails=[]
    for reg in regs:
        lam={a:i for (a,i) in reg}
        br=Brace(E,hol,lam)
        if not is_ideal(br,Dset): continue
        if not kernel_trivial_brace(br,Dset): continue
        n_triv+=1
        ok,info=extract_and_check(br,None,Dset,H_elems,s,quotient)
        n_checked+=1
        if not ok:
            n_fail+=1; fails.append(info)
    print(f"[{label}] additive={E.name} |E|={E.n}: braces={len(regs)}, "
          f"trivial-kernel D-ideal braces={n_triv}, P==Q holds on {n_checked-n_fail}/{n_checked}")
    if fails:
        print("   FAIL sample:", fails[0])
    return n_fail==0

# ----------------------------------------------------------------------
if __name__=="__main__":
    print("="*70)
    print("TEST 1: P tau == Q beta on all genuine trivial-brace-kernel braces")
    print("="*70)

    allok=True

    # ---- H = Z/2 ----
    # E=Z/8, D=2Z/8, s(0)=0,s(1)=1
    Z8=Ab([8],"Z/8"); D8=[(0,),(2,),(4,),(6,)]
    s8={0:(0,),1:(1,)}; q8=lambda x:(x[0]%2)
    allok &= run_family(Z8,D8,"D=2Z/8",s8,[0,1],q8,"H=Z2,E=Z8")
    # E=Z/2xZ/4, D={0}xZ/4
    Z2Z4=Ab([2,4],"Z/2xZ/4"); Dz=[(0,y) for y in range(4)]
    sz={0:(0,0),1:(1,0)}; qz=lambda x:(x[0]%2)
    allok &= run_family(Z2Z4,Dz,"D=0xZ4",sz,[0,1],qz,"H=Z2,E=Z2xZ4")

    # ---- H = Z/3 ----  D=Z/3, E=Z/9 (D=3Z/9) and E=Z/3xZ/3
    Z9=Ab([9],"Z/9"); D9=[(0,),(3,),(6,)]
    s9={0:(0,),1:(1,),2:(2,)}; q9=lambda x:(x[0]%3)
    allok &= run_family(Z9,D9,"D=3Z/9",s9,[0,1,2],q9,"H=Z3,E=Z9")
    Z3Z3=Ab([3,3],"Z/3xZ/3"); D33=[(0,y) for y in range(3)]
    s33={0:(0,0),1:(1,0),2:(2,0)}; q33=lambda x:(x[0]%3)
    allok &= run_family(Z3Z3,D33,"D=0xZ3",s33,[0,1,2],q33,"H=Z3,E=Z3xZ3")

    # ---- H = Z/4 ----  D=Z/4, E=Z/16 (D=4Z/16) and E=Z/4xZ/4
    Z16=Ab([16],"Z/16"); D16=[(4*k,) for k in range(4)]
    s16={0:(0,),1:(1,),2:(2,),3:(3,)}; q16=lambda x:(x[0]%4)
    allok &= run_family(Z16,D16,"D=4Z/16",s16,[0,1,2,3],q16,"H=Z4,E=Z16")

    print()
    print("OVERALL P==Q on all genuine trivial-kernel braces:",
          "PASS" if allok else "FAIL")
