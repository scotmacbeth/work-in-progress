"""
Full enumeration of the TRANSPORT ANSATZ at |S|=2, O_s = 2 objects each:
  OUT = identity (outer object = input);  INN(T,tvec,s,x) = tau_T(s,x)  (indep of tvec).
tau is a function: for each T in SS, s in S, x in O[s]:  tau_T(s,x) in O[T(s)].
Keys: 4 (T) x [ (0,a),(0,b),(1,a),(1,b) ] = 4x4 = 16 assignments, each 2 choices => 2^16.
Enumerate, keep law-satisfiers, classify (endpoint-local? trivial product? functorial action?).
"""
from itertools import product
import honest
from free_transport import build, laws_ok
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM
O={0:['a','b'],1:['a','b']}
OBJS=[(s,x) for s in S for x in O[s]]
TAU_KEYS=[(T,s,x) for T in SS for s in S for x in O[s]]   # 16 keys

def mk_delta_data(tau):
    OUT={}; INN={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            for s in S:
                for x in O[s]:
                    OUT[(T,tvec,s,x)]=x
                    INN[(T,tvec,s,x)]=tau[(T,s,x)]
    return OUT,INN

def all_taus():
    choicelists=[O[T[s]] for (T,s,x) in TAU_KEYS]
    for combo in product(*choicelists):
        yield {TAU_KEYS[i]:combo[i] for i in range(len(TAU_KEYS))}

def endpoint_local(tau):
    seen={}
    for (T,s,x),v in tau.items():
        key=(T[s],s,x)
        if key in seen and seen[key]!=v: return False
        seen[key]=v
    return True

def is_identity_transport(tau):
    # trivial product SxC with C=disc2 identified a<->a,b<->b: tau_T(s,x)=x
    return all(v==x for (T,s,x),v in tau.items())

def functorial_action(tau):
    # does tau define a functor S->Set (copresheaf) on objects, i.e. tau_T(s,x) depends only on
    # (T restricted as arrow s->T(s)) and composes: tau_{U o T}(s,x) = tau_U(T(s), tau_T(s,x))?
    if not endpoint_local(tau): return False
    # build action phi[(s,s')](x) when exists arrow; then check composition over all triples
    # endpoint-local => tau depends on (T(s),s,x); define phi_{s->s'}(x)=tau_T(s,x) any T with T(s)=s'
    phi={}
    for (T,s,x),v in tau.items():
        phi[(s,T[s],x)]=v
    for U in SS:
        for T in SS:
            for s in S:
                for x in O[s]:
                    lhs=tau[(honest.comp(U,T),s,x)]
                    rhs=tau[(U,T[s],tau[(T,s,x)])]
                    if lhs!=rhs: return False
    return True

if __name__=="__main__":
    survivors=[]
    for tau in all_taus():
        OUT,INN=mk_delta_data(tau)
        A,eps,delta=build(O,OUT,INN)
        if laws_ok(A,eps,delta):
            survivors.append(dict(tau))
    print(f"ANSATZ survivors (laws hold): {len(survivors)} / {2**16}")
    el=sum(1 for t in survivors if endpoint_local(t))
    idt=sum(1 for t in survivors if is_identity_transport(t))
    fun=sum(1 for t in survivors if functorial_action(t))
    print(f"  endpoint-local: {el}/{len(survivors)}")
    print(f"  identity transport (tau_T(s,x)=x): {idt}/{len(survivors)}")
    print(f"  functorial action (copresheaf): {fun}/{len(survivors)}")
    # show the non-identity survivors
    for t in survivors:
        if not is_identity_transport(t):
            # print compactly
            print("   NONID:", {(NM[k[0]],k[1],k[2]):v for k,v in t.items() if v!=k[2]})
