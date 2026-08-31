# Probe star-prime (cartesianness of theta = !*(-) : 0*(-) => 1*(-)) and whether it
# needs associativity. Test unital bifunctors incl NON-associative and try to BREAK star'.
import itertools, random
random.seed(0)

# Represent a set as a python frozenset of hashable tags. A unital bifunctor on the
# skeleton {0-elt, 1-elt, 2-elt,...} given by explicit A*B element-sets and functorial action.

# We test the "support" tensor and a family of hand-built unital bifunctors, plus try random.

def S(n): return tuple(range(n))  # the n-element set as (0,..,n-1)

# ---- Coproduct ----
class Coprod:
    unit=0
    def star(self,A,B): return [('l',a) for a in A]+[('r',b) for b in B]
    def smap(self,f,g,A,B):
        d={}
        for x in self.star(A,B):
            d[x]=('l',f[x[1]]) if x[0]=='l' else ('r',g[x[1]])
        return d
# ---- Join A+B+AxB ----
class Join:
    unit=0
    def star(self,A,B):
        return [('l',a) for a in A]+[('r',b) for b in B]+[('m',a,b) for a in A for b in B]
    def smap(self,f,g,A,B):
        d={}
        for x in self.star(A,B):
            if x[0]=='l': d[x]=('l',f[x[1]])
            elif x[0]=='r': d[x]=('r',g[x[1]])
            else: d[x]=('m',f[x[1]],g[x[2]])
        return d
# ---- Support A+B+{*}[both nonempty] ----
class Support:
    unit=0
    def star(self,A,B):
        e=[('l',a) for a in A]+[('r',b) for b in B]
        if A and B: e.append(('m',))
        return e
    def smap(self,f,g,A,B):
        d={}
        for x in self.star(A,B):
            if x[0]=='l': d[x]=('l',f[x[1]])
            elif x[0]=='r': d[x]=('r',g[x[1]])
            else: d[x]=('m',)
        return d

def funcs(A,B):
    A=list(A); B=list(B)
    if not A: return [dict()]
    return [dict(zip(A,vals)) for vals in itertools.product(B,repeat=len(A))]

def star_prime_holds(T, maxC=3, verbose=False):
    # theta_C : 0*C -> 1*C  is  !*C  (! : 0 -> 1). Under unit, 0*C = C.
    one=S(1); zero=S(0)
    bang = {}  # ! : 0->1 empty map
    for nC in range(0,maxC+1):
        C=S(nC)
        starOC=T.star(zero,C)      # 0*C  (should biject with C via left unitor)
        star1C=T.star(one,C)       # 1*C
        star11=T.star(one,one)     # 1*1
        star01=T.star(zero,one)    # 0*1 (~1)
        # eta_C = !*C : 0*C -> 1*C ; map id_0->1 in slot1 (the only map 0->1), id_C slot2
        idC={c:c for c in C}
        eta = T.smap(bang, idC, zero, C)         # 0*C -> 1*C
        # p_L : image of 0*1 -> 1*1 under !*1
        id1={0:0}
        pL_map = T.smap(bang, id1, zero, one)    # 0*1 -> 1*1
        pL_vals=set(pL_map.values())             # should be a single point
        # 1*!_C : 1*C -> 1*1 (slot2 map !_C : C->1)
        bangC={c:0 for c in C}
        id1b={0:0}
        collapse = T.smap(id1b, bangC, one, C)   # 1*C -> 1*1
        # fibre over p_L
        assert len(pL_vals)==1, ("0*1->1*1 not a point",pL_vals)
        pL=next(iter(pL_vals))
        fibre=[z for z in star1C if collapse[z]==pL]
        im_eta=set(eta.values())
        # eta injective?
        inj = (len(set(eta.values()))==len(starOC))
        ok = inj and (im_eta==set(fibre))
        if verbose or not ok:
            print(f"  C={nC}: eta_inj={inj} |im_eta|={len(im_eta)} |fibre|={len(fibre)} star'={ok}")
        if not ok: return False
    return True

for name,T in [("Coprod",Coprod()),("Join",Join()),("Support",Support())]:
    print(name, "star' holds:", star_prime_holds(T))

# --- Adversarial: bi-unital bifunctors that are NON-polynomial in A ---
# A*B = A  +  B  +  supp(A)*B   where supp(A)=[A!=empty]  (bi-unital, non-poly in A)
class SuppTimesB:
    unit=0
    def star(self,A,B):
        e=[('l',a) for a in A]+[('r',b) for b in B]
        if A:  # supp(A) x B  (token 'x' present iff A nonempty)
            e+=[('x',b) for b in B]
        return e
    def smap(self,f,g,A,B):
        d={}
        for x in self.star(A,B):
            if x[0]=='l': d[x]=('l',f[x[1]])
            elif x[0]=='r': d[x]=('r',g[x[1]])
            else: d[x]=('x',g[x[1]])  # token survives since A nonempty => A' nonempty
        return d

# A*B = A + B + supp(A)*supp(B)   (a single glue point iff both nonempty = SUPPORT already)
# A*B = A + B + supp(A)   (a token iff A nonempty; bi-unital? at A=0: B ok; at B=0: A + supp(A)!=A) NO

# A*B = A + B + A*supp(B)  (mirror)
class ATimesSupp:
    unit=0
    def star(self,A,B):
        e=[('l',a) for a in A]+[('r',b) for b in B]
        if B:
            e+=[('x',a) for a in A]
        return e
    def smap(self,f,g,A,B):
        d={}
        for x in self.star(A,B):
            if x[0]=='l': d[x]=('l',f[x[1]])
            elif x[0]=='r': d[x]=('r',g[x[1]])
            else: d[x]=('x',f[x[1]])
        return d

# A*B = A + B + supp(A)*B + A*supp(B) + supp(A)*supp(B) ... build a messy bi-unital one
class Messy:
    unit=0
    def star(self,A,B):
        e=[('l',a) for a in A]+[('r',b) for b in B]
        if A: e+=[('xb',b) for b in B]
        if B: e+=[('xa',a) for a in A]
        if A and B: e.append(('g',))
        return e
    def smap(self,f,g,A,B):
        d={}
        for x in self.star(A,B):
            t=x[0]
            if t=='l': d[x]=('l',f[x[1]])
            elif t=='r': d[x]=('r',g[x[1]])
            elif t=='xb': d[x]=('xb',g[x[1]])
            elif t=='xa': d[x]=('xa',f[x[1]])
            else: d[x]=('g',)
        return d

for name,T in [("SuppTimesB",SuppTimesB()),("ATimesSupp",ATimesSupp()),("Messy",Messy())]:
    print(f"--- {name} (non-poly, bi-unital) ---")
    print(name,"star' holds:", star_prime_holds(T, verbose=True))
