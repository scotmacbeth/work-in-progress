"""
Independent brute-force verification of monoids & comonoids internal to Cont
for the four canonical monoidal structures: +, x, (x)Dirichlet, and (for sanity) checks.
Author: MacBeth, 2026-07-19.

A container c = (S, P) with S a list of shapes, P a dict shape -> list of position labels.
A Poly morphism f: A -> B is (phi, psi):
   phi: dict  a_shape -> b_shape        (FORWARD on shapes)
   psi: dict  a_shape -> (dict  b_position_at_phi(a) -> a_position_at_a)   (BACKWARD on positions)
Composition of A--f-->B--g-->C: (gf).phi[a]=g.phi[f.phi[a]];
   (gf).psi[a] = { c_pos : f.psi[a][ g.psi[f.phi[a]][c_pos] ] }   (backward maps compose contravariantly)
"""
from itertools import product

class Mor:
    def __init__(self, src, tgt, phi, psi):
        self.src=src; self.tgt=tgt; self.phi=phi; self.psi=psi
    def __eq__(self, o):
        return self.phi==o.phi and self.psi==o.psi
    def __hash__(self):
        return hash((tuple(sorted(self.phi.items())),))

def compose(g, f):
    # f: A->B, g: B->C  => g o f : A->C
    A, C = f.src, g.tgt
    phi={}; psi={}
    for a in A['S']:
        b=f.phi[a]; c=g.phi[b]
        phi[a]=c
        psi[a]={cp: f.psi[a][g.psi[b][cp]] for cp in C['P'][c]}
    return Mor(A,C,phi,psi)

def ident(A):
    return Mor(A,A,{a:a for a in A['S']},{a:{p:p for p in A['P'][a]} for a in A['S']})

def enum_mors(A,B):
    """all morphisms A->B"""
    shapes=A['S']
    # for each a: choose b in B.S and function B.P[b]->A.P[a]
    per_shape=[]
    for a in shapes:
        opts=[]
        for b in B['S']:
            dom=B['P'][b]; cod=A['P'][a]
            if len(cod)==0 and len(dom)>0:
                continue  # no function into empty set
            for vals in product(cod, repeat=len(dom)):
                psi={dom[i]:vals[i] for i in range(len(dom))}
                opts.append((b,psi))
        per_shape.append(opts)
    for combo in product(*per_shape):
        phi={shapes[i]:combo[i][0] for i in range(len(shapes))}
        psi={shapes[i]:combo[i][1] for i in range(len(shapes))}
        yield Mor(A,B,phi,psi)

# ---------------- tensor structures ----------------
# each provides: unit(), tens(c,d), tmor(f,g), assoc(c,d,e), lunit(c), runit(c)

class Coproduct:
    name='+'
    def unit(self): return {'S':[], 'P':{}}
    def tens(self,c,d):
        S=[('L',s) for s in c['S']]+[('R',t) for t in d['S']]
        P={}
        for s in c['S']: P[('L',s)]=[('l',p) for p in c['P'][s]]
        for t in d['S']: P[('R',t)]=[('r',q) for q in d['P'][t]]
        return {'S':S,'P':P}
    def tmor(self,f,g):
        C=self.tens(f.src,g.src); D=self.tens(f.tgt,g.tgt)
        phi={};psi={}
        for s in f.src['S']:
            phi[('L',s)]=('L',f.phi[s]); psi[('L',s)]={('l',p):('l',f.psi[s][p]) for p in f.tgt['P'][f.phi[s]]}
        for t in g.src['S']:
            phi[('R',t)]=('R',g.phi[t]); psi[('R',t)]={('r',q):('r',g.psi[t][q]) for q in g.tgt['P'][g.phi[t]]}
        return Mor(C,D,phi,psi)
    def assoc(self,c,d,e):
        L=self.tens(self.tens(c,d),e); R=self.tens(c,self.tens(d,e))
        phi={};psi={}
        def emb_pos(p):  # position labels get re-tagged; build by matching structure
            return p
        for s in c['S']:
            a=('L',('L',s)); b=('L',s)
            phi[a]=b; psi[a]={('l',p):('l',('l',p)) for p in c['P'][s]}
            # careful: positions of R at ('L',s) are ('l',<c pos>); positions of L at a are ('l',('l',p))
            psi[a]={('l',p):('l',('l',p)) for p in c['P'][s]}
        for t in d['S']:
            a=('L',('R',t)); b=('R',('L',t))
            phi[a]=b; psi[a]={('r',('l',q)):('l',('r',q)) for q in d['P'][t]}
        for u in e['S']:
            a=('R',u); b=('R',('R',u))
            phi[a]=b; psi[a]={('r',('r',w)):('r',w) for w in e['P'][u]}
        return Mor(L,R,phi,psi)
    def lunit(self,c):
        # 0 + c -> c   ; shapes ('R',s)->s
        L=self.tens(self.unit(),c)
        phi={('R',s):s for s in c['S']}
        psi={('R',s):{p:('r',p) for p in c['P'][s]} for s in c['S']}
        return Mor(L,c,phi,psi)
    def runit(self,c):
        L=self.tens(c,self.unit())
        phi={('L',s):s for s in c['S']}
        psi={('L',s):{p:('l',p) for p in c['P'][s]} for s in c['S']}
        return Mor(L,c,phi,psi)

class Product:
    name='x'
    def unit(self): return {'S':['*'], 'P':{'*':[]}}
    def tens(self,c,d):
        S=[(s,t) for s in c['S'] for t in d['S']]
        P={(s,t):[('l',p) for p in c['P'][s]]+[('r',q) for q in d['P'][t]] for s in c['S'] for t in d['S']}
        return {'S':S,'P':P}
    def tmor(self,f,g):
        C=self.tens(f.src,g.src); D=self.tens(f.tgt,g.tgt)
        phi={};psi={}
        for s in f.src['S']:
            for t in g.src['S']:
                a=(s,t); b=(f.phi[s],g.phi[t]); phi[a]=b
                d={}
                for p in f.tgt['P'][f.phi[s]]: d[('l',p)]=('l',f.psi[s][p])
                for q in g.tgt['P'][g.phi[t]]: d[('r',q)]=('r',g.psi[t][q])
                psi[a]=d
        return Mor(C,D,phi,psi)
    def assoc(self,c,d,e):
        L=self.tens(self.tens(c,d),e); R=self.tens(c,self.tens(d,e))
        phi={};psi={}
        for s in c['S']:
            for t in d['S']:
                for u in e['S']:
                    a=((s,t),u); b=(s,(t,u)); phi[a]=b
                    dd={}
                    for p in c['P'][s]: dd[('l',p)]=('l',('l',p))
                    for q in d['P'][t]: dd[('r',('l',q))]=('l',('r',q))
                    for w in e['P'][u]: dd[('r',('r',w))]=('r',w)
                    psi[a]=dd
        return Mor(L,R,phi,psi)
    def lunit(self,c):
        L=self.tens(self.unit(),c)
        phi={('*',s):s for s in c['S']}
        psi={('*',s):{p:('r',p) for p in c['P'][s]} for s in c['S']}
        return Mor(L,c,phi,psi)
    def runit(self,c):
        L=self.tens(c,self.unit())
        phi={(s,'*'):s for s in c['S']}
        psi={(s,'*'):{p:('l',p) for p in c['P'][s]} for s in c['S']}
        return Mor(L,c,phi,psi)

class Dirichlet:
    name='(x)'
    def unit(self): return {'S':['*'], 'P':{'*':['.']}}
    def tens(self,c,d):
        S=[(s,t) for s in c['S'] for t in d['S']]
        P={(s,t):[(p,q) for p in c['P'][s] for q in d['P'][t]] for s in c['S'] for t in d['S']}
        return {'S':S,'P':P}
    def tmor(self,f,g):
        C=self.tens(f.src,g.src); D=self.tens(f.tgt,g.tgt)
        phi={};psi={}
        for s in f.src['S']:
            for t in g.src['S']:
                a=(s,t); b=(f.phi[s],g.phi[t]); phi[a]=b
                d={(p,q):(f.psi[s][p],g.psi[t][q]) for p in f.tgt['P'][f.phi[s]] for q in g.tgt['P'][g.phi[t]]}
                psi[a]=d
        return Mor(C,D,phi,psi)
    def assoc(self,c,d,e):
        L=self.tens(self.tens(c,d),e); R=self.tens(c,self.tens(d,e))
        phi={};psi={}
        for s in c['S']:
            for t in d['S']:
                for u in e['S']:
                    a=((s,t),u); b=(s,(t,u)); phi[a]=b
                    dd={(p,(q,w)):((p,q),w) for p in c['P'][s] for q in d['P'][t] for w in e['P'][u]}
                    psi[a]=dd
        return Mor(L,R,phi,psi)
    def lunit(self,c):
        L=self.tens(self.unit(),c)
        phi={('*',s):s for s in c['S']}
        psi={('*',s):{p:('.',p) for p in c['P'][s]} for s in c['S']}
        return Mor(L,c,phi,psi)
    def runit(self,c):
        L=self.tens(c,self.unit())
        phi={(s,'*'):s for s in c['S']}
        psi={(s,'*'):{p:(p,'.') for p in c['P'][s]} for s in c['S']}
        return Mor(L,c,phi,psi)

# ---------------- monoid / comonoid law checkers ----------------
def is_monoid(T, c, mu, eta):
    idc=ident(c)
    # associativity: mu o (mu (x) id) == mu o (id (x) mu) o assoc
    lhs=compose(mu, T.tmor(mu, idc))
    rhs=compose(mu, compose(T.tmor(idc, mu), T.assoc(c,c,c)))
    if not lhs==rhs: return False
    # left unit: mu o (eta (x) id) == lunit
    if not compose(mu, T.tmor(eta, idc))==T.lunit(c): return False
    # right unit
    if not compose(mu, T.tmor(idc, eta))==T.runit(c): return False
    return True

def is_comonoid(T, c, delta, eps):
    idc=ident(c)
    # coassociativity: (id (x) delta) o delta == assoc o (delta (x) id) o delta  : c -> c(x)(c(x)c)
    lhs=compose(T.tmor(idc, delta), delta)
    rhs=compose(T.assoc(c,c,c), compose(T.tmor(delta, idc), delta))
    if not lhs==rhs: return False
    # counit: lunit o (eps (x) id) o delta == id ; runit o (id (x) eps) o delta == id
    if not compose(T.lunit(c), compose(T.tmor(eps, idc), delta))==idc: return False
    if not compose(T.runit(c), compose(T.tmor(idc, eps), delta))==idc: return False
    return True

def count_monoids(T, c, verbose=False):
    I=T.unit(); cc=T.tens(c,c)
    mus=list(enum_mors(cc,c)); etas=list(enum_mors(I,c))
    sols=[]
    for mu in mus:
        for eta in etas:
            if is_monoid(T,c,mu,eta): sols.append((mu,eta))
    return sols, len(mus), len(etas)

def count_comonoids(T, c):
    I=T.unit(); cc=T.tens(c,c)
    deltas=list(enum_mors(c,cc)); epss=list(enum_mors(c,I))
    sols=[]
    for delta in deltas:
        for eps in epss:
            if is_comonoid(T,c,delta,eps): sols.append((delta,eps))
    return sols, len(deltas), len(epss)

# ---------------- test containers ----------------
def cont(sizes):
    """container with shapes 0..n-1 and P[i] = list of ints of length sizes[i]"""
    S=list(range(len(sizes)))
    P={i:list(range(sizes[i])) for i in range(len(sizes))}
    return {'S':S,'P':P}

if __name__=='__main__':
    tests=[('y=[1]',cont([1])),('[2]',cont([2])),('[0]',cont([0])),
           ('[1,1]',cont([1,1])),('[0,1]',cont([0,1])),('[2,0]',cont([2,0])),
           ('[1,2]',cont([1,2]))]

    print("###### DIRICHLET (x) ######")
    for lbl,c in tests:
        s,_,_=count_comonoids(Dirichlet(),c); m,_,_=count_monoids(Dirichlet(),c)
        print(f"  {lbl:8}: comonoids={len(s):3}  monoids={len(m):3}")

    print("###### PRODUCT x ######")
    for lbl,c in tests:
        s,_,_=count_comonoids(Product(),c); m,_,_=count_monoids(Product(),c)
        print(f"  {lbl:8}: comonoids={len(s):3}  monoids={len(m):3}")

    print("###### COPRODUCT + ######")
    for lbl,c in tests:
        s,_,_=count_comonoids(Coproduct(),c); m,_,_=count_monoids(Coproduct(),c)
        print(f"  {lbl:8}: comonoids={len(s):3}  monoids={len(m):3}")
