"""
Targeted confirmations of the degree-1 transport theory:
  T1. tau^{id}=id is FORCED by units (a functorial+endpoint-local transport with tau^{id}!=id fails units).
  T2. deepest-object constraint <=> full associativity (degree-1): endpoint-local+functorial+unital
      transports PASS full honest laws; violating endpoint-locality FAILS.
  T3. There is NO nontrivial survivor: every law-satisfying degree-1 transport on O_s is
      a trivial coherent iso-system (=> 𝕊 x disc(D)).
Build transports directly as psi_{s->m}: O_s->O_m (endpoint-local by construction) and as full
tau^g (possibly not endpoint-local) and run the honest engine.
"""
from itertools import product, permutations
import honest
from free_transport import build, laws_ok
S=[0,1]; SS=honest.SS; ID=honest.ID; comp=honest.comp; NM=honest.NM

def tau_from_psi(O, psi):
    # psi: dict (s,m)->(dict x-> object in O[m]); endpoint-local tau^g(s,x)=psi[(s,g[s])][x]
    OUT={}; INN={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            for s in S:
                for x in O[s]:
                    OUT[(T,tvec,s,x)]=x
                    INN[(T,tvec,s,x)]=psi[(s,T[s])][x]
    return build(O,OUT,INN)

def tau_from_fn(O, tau):
    OUT={}; INN={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            for s in S:
                for x in O[s]:
                    OUT[(T,tvec,s,x)]=x
                    INN[(T,tvec,s,x)]=tau(T,s,x)
    return build(O,OUT,INN)

O={0:['a','b'],1:['a','b']}

# ---- T1: endpoint-local + functorial but tau^{id} = swap (not id) ----
# psi_{s->m} = swap for ALL (s,m). Then functorial? psi_{m->n} o psi_{s->m}=swap o swap=id != swap=psi_{s->n}. Not functorial.
# Use psi_{s->m}=id for s!=m and psi_{s->s}=swap: check units.
psi_T1={(s,m): {x: ({'a':'b','b':'a'}[x] if s==m else x) for x in O[s]} for s in S for m in S}
A,eps,delta=tau_from_psi(O,psi_T1)
print("T1  psi_{s->s}=swap (tau^{id}!=id): units=",honest.check_units_fast(A,eps,delta),
      " assoc=",honest.check_assoc_fast(A,eps,delta))

# ---- T2a: trivial coherent iso-system psi=id everywhere (= 𝕊 x disc2) ----
psi_id={(s,m):{x:x for x in O[s]} for s in S for m in S}
A,eps,delta=tau_from_psi(O,psi_id)
print("T2a trivial psi=id (𝕊xdisc2): laws=",laws_ok(A,eps,delta))

# ---- T2b: coherent iso-system with a global relabel: psi_{s->m}(a)=b,(b)=a for ALL s,m incl s=m ----
# This is functorial? psi o psi = id != psi. NOT functorial => should fail. (swap is an involution)
psi_swap={(s,m):{'a':'b','b':'a'} for s in S for m in S}
A,eps,delta=tau_from_psi(O,psi_swap)
print("T2b psi=swap everywhere (non-functorial): laws=",laws_ok(A,eps,delta),
      " (expect False: swap not idempotent => not functorial)")

# ---- T2c: relabel by a FIXED bijection consistently: identify O_0,O_1 via a<->a,b<->b but 'rename'
# equivalently psi=id => already T2a. A genuine 'twist' would need psi_{0->1}!=psi_{1->0}^{-1}... explore:
# psi_{0->1}=swap, psi_{1->0}=swap, psi_{s->s}=id. functorial: psi_{1->0}o psi_{0->1}=id=psi_{0->0} ✓;
#   psi_{0->1}o psi_{1->0}=id=psi_{1->1} ✓. This is a coherent iso-system (relabel O_1 by swap). Should PASS.
psi_relabel={(0,0):{x:x for x in O[0]},(1,1):{x:x for x in O[1]},
             (0,1):{'a':'b','b':'a'},(1,0):{'a':'b','b':'a'}}
A,eps,delta=tau_from_psi(O,psi_relabel)
print("T2c coherent relabel (psi_{0<->1}=swap, psi_{s->s}=id): laws=",laws_ok(A,eps,delta),
      " (expect True: = 𝕊xdisc2 up to relabel)")

# ---- T3: NON endpoint-local functorial (copresheaf-like on 2 objects): tau^g depends on full g ----
# emulate: objects=S-set {a,b}=copy of S; tau^g(s,x)= g(x_as_state)? Build the S(0,-)-style on 2 obj.
# tau^g(s,a)=a if g fixes.., let's do tau^g(s,x)= 'a' if g[ (0 if x=='a' else 1) ]==0 else 'b'  (post-comp-ish)
def tau_np(g,s,x):
    st=0 if x=='a' else 1
    return 'a' if g[st]==0 else 'b'
A,eps,delta=tau_from_fn(O,tau_np)
# endpoint-local? tau_np depends on g via g[st], st depends on x not s => NOT endpoint-local in s.
print("T3  non-endpoint-local functorial: units=",honest.check_units_fast(A,eps,delta),
      " assoc=",honest.check_assoc_fast(A,eps,delta)," (expect assoc False)")
