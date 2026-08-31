"""
grade_independence.py  (MacBeth compute agent, 2026-08-10)

CRUX sub-lemma test for the State-liftings completeness conjecture (holonomy-free).

A polynomial fibred lifting of State (|S|=2) is, post-purity, a family of aggregators
A_sigma : Set^S -> Set, sigma in S^S (4 grades: id,sw,c0,c1), each a coproduct of PURE
objects.  A pure object = (source state s in {0,1}, out-degree d>=0).  We test:

  (i)  GRADE-INDEPENDENCE: is the per-grade PROFILE (multiset of (source,degree) objects)
       forced to be the SAME across all 4 grades?
  (ii) Or is there a GRADE-DEPENDENT-PROFILE SURVIVOR (a valid lifting whose profile
       genuinely differs between grades)?  -> would make the answer finer than Cat.

We reuse honest.py's genuine finite-Cont-morphism monad-law engine (all 3 laws as
container-morphism identities).  We do EXHAUSTIVE free-delta sweeps over bounded families:

  FAMILY M (multiplicity, degree 1): objects all degree 1, n(g,s) in {0,1,2} objects at
      (grade g, source s).  out_j & inner are genuine choices; beta trivial.
  FAMILY D (single object per (g,s), degree in {1,2}): out_j & inner forced; beta free
      (backward reindex).  Reproduces Reader's degree-2 mechanism.

For each candidate profile we enumerate ALL delta (bounded product) + all counits eps and
run honest.check_laws.  We report which profiles admit a lifting and whether any valid
lifting is grade-dependent.
"""
from itertools import product
import honest

S=[0,1]; SS=honest.SS; ID=honest.ID; NM=honest.NM; thread=honest.thread
GN={v:k for k,v in NM.items()}  # name->grade

# ---------------------------------------------------------------------------
# FAMILY M : multiplicity of degree-1 pure objects.  n[(g,s)] in {0,1,2}.
# object = pure degree-1 at source s -> arity (1,0) if s==0 else (0,1).
# ---------------------------------------------------------------------------
def build_M(n):
    """n: dict (grade,source)->count.  Return (A, obj_at) where obj_at[(g,s)] = list of
       object indices within A[g] that are the degree-1 objects at source s."""
    A={g:[] for g in SS}
    obj_at={}
    for g in SS:
        for s in S:
            obj_at[(g,s)]=[]
            for _ in range(n[(g,s)]):
                obj_at[(g,s)].append(len(A[g]))
                A[g].append((1,0) if s==0 else (0,1))
    return A, obj_at

def source_of(obj):
    return 0 if obj[0]>0 else 1

def enum_delta_M(A,obj_at):
    """Yield delta dicts.  For each (T,tvec) and object j in A[sigma] (source s):
         choose out_j among obj_at[(T,s)]  and inner0 among obj_at[(tvec[s],T[s])].
       beta trivial {(0,0):0}.  If any required target slot empty -> no delta (skip via None)."""
    # collect the choice list per context
    contexts=[]  # each: (key=(T,tvec), j, s, out_options, inner_options)
    for T in SS:
        for tvec in product(SS,repeat=2):
            sigma=thread(T,tvec)
            for j,obj in enumerate(A[sigma]):
                s=source_of(obj)
                outs=obj_at[(T,s)]
                inns=obj_at[(tvec[s],T[s])]
                if not outs or not inns:
                    return  # dead profile: routing impossible -> no delta at all
                contexts.append(((T,tvec),j,outs,inns))
    # cartesian product over (out choice, inner choice) per context
    choicelists=[list(product(c[2],c[3])) for c in contexts]
    total=1
    for cl in choicelists: total*=len(cl)
    if total>args_cap:
        yield ('TOOBIG',total); return
    for combo in product(*choicelists):
        delta={}
        for (ctx,(out_j,inn)) in zip(contexts,combo):
            (T,tvec),j,outs,inns=ctx
            key=(T,tvec)
            delta.setdefault(key,{})
            delta[key][j]=(out_j,{0:inn},{(0,0):0})
        yield delta

def enum_eps_M(A,obj_at):
    """counit marks a slot for each A_id object; degree 1 -> slot 0 forced."""
    yield {j:0 for j in range(len(A[ID]))}

args_cap=200000  # per-profile delta product cap for exhaustive sweep

# ---------------------------------------------------------------------------
# FAMILY D : exactly one object per (g,s) [full support], degree d[(g,s)] in {1,2}.
# out_j, inner forced (unique object).  beta free: backward map
#   {(a,b): a in range(m=deg out_j), b in range(din=deg inner)} -> range(D_j=deg j).
# ---------------------------------------------------------------------------
def build_D(d):
    A={g:[] for g in SS}
    idx={}
    for g in SS:
        for s in S:
            idx[(g,s)]=len(A[g])
            A[g].append((d[(g,s)],0) if s==0 else (0,d[(g,s)]))
    return A, idx

def enum_delta_D(d):
    A,idx=build_D(d)
    contexts=[]
    for T in SS:
        for tvec in product(SS,repeat=2):
            sigma=thread(T,tvec)
            for s in S:
                j=idx[(sigma,s)]
                out_j=idx[(T,s)]; m=d[(T,s)]
                inner_obj=idx[(tvec[s],T[s])]; din=d[(tvec[s],T[s])]
                Dj=d[(sigma,s)]
                pairs=[(a,b) for a in range(m) for b in range(din)]
                contexts.append(((T,tvec),j,out_j,m,inner_obj,din,Dj,pairs))
    # beta options per context = Dj ** len(pairs)
    total=1
    for c in contexts: total*= c[6]**len(c[7])
    if total>args_cap:
        yield ('TOOBIG',total); return
    betalists=[list(product(range(c[6]),repeat=len(c[7]))) for c in contexts]
    for combo in product(*betalists):
        delta={}
        for c,betavals in zip(contexts,combo):
            (T,tvec),j,out_j,m,inner_obj,din,Dj,pairs=c
            key=(T,tvec)
            delta.setdefault(key,{})
            inner={a:inner_obj for a in range(m)}
            beta={pairs[k]:betavals[k] for k in range(len(pairs))}
            delta[key][j]=(out_j,inner,beta)
        yield delta

def enum_eps_D(d):
    A,idx=build_D(d)
    # A_id objects: (id,0) degree d0, (id,1) degree d1.  eps marks a slot each.
    d0=d[(ID,0)]; d1=d[(ID,1)]
    for e0 in range(d0):
        for e1 in range(d1):
            yield {idx[(ID,0)]:e0, idx[(ID,1)]:e1}

# ---------------------------------------------------------------------------
# profile signatures & grade-dependence test
# ---------------------------------------------------------------------------
def profile_sig_M(n):
    return tuple((NM[g], n[(g,0)], n[(g,1)]) for g in SS)

def grade_dependent_M(n):
    for s in S:
        vals={n[(g,s)] for g in SS if True}
        if len(vals)>1: return True
    return False

def grade_dependent_D(d):
    for s in S:
        if len({d[(g,s)] for g in SS})>1: return True
    return False

# ---------------------------------------------------------------------------
# DRIVERS
# ---------------------------------------------------------------------------
def sweep_M(max_total=4, use_full=False):
    """Exhaustive sweep of FAMILY M over all profiles n:(8 slots)->{0,1,2} with
       total objects <= max_total.  Returns (valid, dead, toobig, witnesses)."""
    checker = honest.check_laws if use_full else honest.check_laws_fast
    slots=[(g,s) for g in SS for s in S]
    valid=[]; dead=0; toobig=0; witnesses=[]
    for vals in product(range(3),repeat=8):
        n={slots[i]:vals[i] for i in range(8)}
        if sum(vals)==0 or sum(vals)>max_total: continue
        # A_id must be nonempty for the counit/unit to make sense
        if n[(ID,0)]+n[(ID,1)]==0: continue
        A,obj_at=build_M(n)
        found_any=False; is_toobig=False
        for delta in enum_delta_M(A,obj_at):
            if delta is None: continue
            if isinstance(delta,tuple) and delta[0]=='TOOBIG':
                is_toobig=True; break
            for eps in enum_eps_M(A,obj_at):
                if checker(A,eps,delta):
                    found_any=True
                    break
            if found_any: break
        if is_toobig:
            toobig+=1; continue
        if found_any:
            valid.append(n)
            if grade_dependent_M(n): witnesses.append(('M',n))
        else:
            # distinguish dead (no delta) vs delta-exists-but-no-law
            dead+=1
    return valid,dead,toobig,witnesses

def sweep_D(use_full=False):
    """Exhaustive sweep of FAMILY D: one object per (g,s), degree d in {1,2}, full support.
       256 profiles.  Free beta.  Skips TOOBIG (records)."""
    checker = honest.check_laws if use_full else honest.check_laws_fast
    slots=[(g,s) for g in SS for s in S]
    valid=[]; toobig=0
    for vals in product([1,2],repeat=8):
        d={slots[i]:vals[i] for i in range(8)}
        found=False; is_toobig=False
        for delta in enum_delta_D(d):
            if isinstance(delta,tuple) and delta[0]=='TOOBIG':
                is_toobig=True; break
            for eps in enum_eps_D(d):
                if checker(A_D(d),eps,delta):
                    found=True; break
            if found: break
        if is_toobig: toobig+=1; continue
        if found:
            valid.append(d)
    return valid,toobig

def A_D(d):
    A,_=build_D(d); return A

if __name__=="__main__":
    import sys
    which=sys.argv[1] if len(sys.argv)>1 else 'M'
    if which=='M':
        mt=int(sys.argv[2]) if len(sys.argv)>2 else 3
        full = (len(sys.argv)>3 and sys.argv[3]=='full')
        valid,dead,toobig,wit=sweep_M(max_total=mt,use_full=full)
        print(f"[FAMILY M] max_total={mt} full={full}: valid={len(valid)} dead={dead} toobig={toobig}")
        gd=[n for n in valid if grade_dependent_M(n)]
        print(f"   grade-DEPENDENT valid profiles: {len(gd)}")
        for n in valid:
            tag=" <== GRADE-DEPENDENT" if grade_dependent_M(n) else ""
            print("   ", profile_sig_M(n), tag)
    elif which=='D':
        full = (len(sys.argv)>2 and sys.argv[2]=='full')
        valid,toobig=sweep_D(use_full=full)
        print(f"[FAMILY D] full={full}: valid={len(valid)} toobig(skipped)={toobig}")
        gd=[d for d in valid if grade_dependent_D(d)]
        print(f"   grade-DEPENDENT valid profiles: {len(gd)}")
        for d in valid:
            sig=tuple((NM[g],d[(g,0)],d[(g,1)]) for g in SS)
            tag=" <== GRADE-DEPENDENT" if grade_dependent_D(d) else ""
            print("   ", sig, tag)
