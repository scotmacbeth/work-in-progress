"""
MORPHISM-level free-transport enumeration. One object '*' per state, out-degree 2 (positions {0,1}),
so the fibre 'category' C̃_s is a monoid on {0,1} (P1). Transport along grade g = a permutation
perm_g of the 2 out-positions (free), applied in the beta grafting. Enumerate (monoid, perm-family)
and keep law-satisfiers; classify perm-family (trivial? endpoint-local? functorial?).

delta at (T,tvec), object (s,*)@sigma:
  outer (s,*)@T ; per out-pos f in {0,1}: inner (T(s),*)@tvec[s];
  beta[(f,q)] = mul( q , perm_T(f) )   -- twisted grafting: transport f by perm_T then compose with q
  (perm_T = identity recovers plain monoid grafting = product 𝕊×BM).
eps marks the monoid identity e.
"""
from itertools import product, permutations
import honest, lean_assoc
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM
POS=[0,1]; PERMS=[dict(zip(POS,p)) for p in permutations(POS)]  # 2 perms: id and swap

def monoids_on_2():
    # binary op mul[(y,x)] with identity, associative; enumerate all, return (mul,e)
    res=[]
    for e in POS:
        for vals in product(POS,repeat=4):
            mul={}
            it=iter(vals)
            for y in POS:
                for x in POS:
                    mul[(y,x)]=next(it)
            # identity
            if any(mul[(e,x)]!=x or mul[(x,e)]!=x for x in POS): continue
            # assoc
            if any(mul[(mul[(z,y)],x)]!=mul[(z,mul[(y,x)])] for x in POS for y in POS for z in POS): continue
            res.append((mul,e))
    return res

def build_hom(mul,e,perm):
    """perm: dict g(in SS)->perm(dict). objects (s,*) deg 2."""
    lst=[]; idx={}
    for s in S:
        idx[(s,'*')]=len(lst); lst.append((2,0) if s==0 else (0,2))
    A={sig:list(lst) for sig in SS}; IDX={sig:dict(idx) for sig in SS}
    eps={idx[(s,'*')]:e for s in S}
    delta={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            sig=thread(T,tvec); route={}
            for s in S:
                j=IDX[sig][(s,'*')]; out_j=IDX[T][(s,'*')]; inner={}; beta={}
                pT=perm[T]
                for f in POS:
                    inner[f]=IDX[tvec[s]][(T[s],'*')]
                    for q in POS:
                        beta[(f,q)]=mul[(q, pT[f])]
                route[j]=(out_j,inner,beta)
            delta[(T,tvec)]=route
    return A,eps,delta

def laws(A,eps,delta):
    if not honest.check_units_fast(A,eps,delta): return False
    r=lean_assoc.assoc_sample(A,eps,delta,(['a'],{'a':('a0','a1')}),nsamp=1500,seed=5)
    return r[0]=='ok'

def perm_families():
    keys=SS
    for combo in product(PERMS,repeat=len(keys)):
        yield {keys[i]:combo[i] for i in range(len(keys))}

def is_trivial(perm): return all(all(p[x]==x for x in POS) for p in perm.values())
def endpoint_local(perm):
    # perm_g depends on g only via ... but perm acts on morphisms transported along arrow s->g(s).
    # For source s, endpoint g(s). endpoint-local: perm_g restricted to source-s use depends only on g(s).
    # Here perm_g is used at both sources; test: for g,g' with g(s)=g'(s) do the s-uses agree? The build
    # uses pT=perm[T] uniformly (not per-source). We just report functorial-triviality: perm_id must be id.
    return True
def perm_id_trivial(perm): return all(perm[ID][x]==x for x in POS)

if __name__=="__main__":
    Ms=monoids_on_2()
    print(f"monoids on 2 elements: {len(Ms)}")
    total=0; survivors=[]
    for (mul,e) in Ms:
        for perm in perm_families():
            if laws(*build_hom(mul,e,perm)):
                survivors.append((mul,e,perm)); total+=1
    print(f"law-satisfying (monoid,perm) pairs: {total}")
    triv=sum(1 for (mul,e,perm) in survivors if is_trivial(perm))
    permidtriv=sum(1 for (mul,e,perm) in survivors if perm_id_trivial(perm))
    print(f"  with TRIVIAL perm-family (=product 𝕊×BM): {triv}/{total}")
    print(f"  with perm_id = identity: {permidtriv}/{total}")
    # show any NON-trivial perm survivor
    for (mul,e,perm) in survivors:
        if not is_trivial(perm):
            print("  NONTRIVIAL perm survivor: e=",e," perm=",{NM[g]:[perm[g][0],perm[g][1]] for g in SS})
    # count distinct monoids that appear
    monset=set()
    for (mul,e,perm) in survivors:
        monset.add((tuple(sorted(mul.items())),e))
    print(f"  distinct monoids among survivors: {len(monset)} (expect 4 = #monoids on 2 elts? note some coincide)")
