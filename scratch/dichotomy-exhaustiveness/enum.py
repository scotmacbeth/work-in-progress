"""
Enumerate ALL monad liftings of Reader y^E for a given polynomial aggregator L,
built from the pure-inner-shape routing (which is forced for delta to exist).

L given as `shapes` = list of arity-tuples length e (a_s(v) >= 0).
"""
from itertools import product
from monad import Cont, Lifting, check_monad

def poly_L(shapes, e):
    def L_eval(Bs):
        elts=[]
        for si,ar in enumerate(shapes):
            per=[list(product(Bs[v],repeat=ar[v])) for v in range(e)]
            for combo in product(*per):
                elts.append((si,tuple(combo)))
        return elts
    def L_act(elt,maps):
        si,combo=elt
        return (si, tuple(tuple(maps[v][x] for x in combo[v]) for v in range(e)))
    return L_eval,L_act

def pure_shapes(shapes,e):
    # dict v-> list of shape indices reading only leaf v (arity 0 elsewhere; total>=1)
    d={v:[] for v in range(e)}
    for si,ar in enumerate(shapes):
        nz=[v for v in range(e) if ar[v]>0]
        if len(nz)==1:
            d[nz[0]].append(si)
    return d

def enum_eps(shapes,e):
    per=[]
    for ar in shapes:
        slots=[(v,j) for v in range(e) for j in range(ar[v])]
        if not slots: return   # zero-arity shape -> no unit
        per.append(slots)
    for ch in product(*per):
        yield list(ch)

def enum_delta_data(shapes,e):
    """Yield delta 'data': list over Dom-shapes s of (s_dagger, inner, bm).
       inner: dict (v,k)->pure-inner-shape-idx ; bm: dict v-> tuple(len total_v) in range(a_s(v))."""
    pures=pure_shapes(shapes,e)
    per_shape=[]
    for si,ar in enumerate(shapes):
        opts=[]
        for sdag in range(len(shapes)):
            adag=shapes[sdag]
            # for each (v,k) choose a v-pure inner shape
            copy_slots=[]
            copy_key=[]
            feasible=True
            for v in range(e):
                for k in range(adag[v]):
                    if not pures[v]:
                        feasible=False;break
                    copy_slots.append(pures[v]); copy_key.append((v,k))
                if not feasible:break
            if not feasible: continue
            for inner_choice in (product(*copy_slots) if copy_slots else [()]):
                inner={copy_key[i]:inner_choice[i] for i in range(len(copy_key))}
                # total diagonal slots per leaf v
                totals={}
                for v in range(e):
                    tv=0
                    for k in range(adag[v]):
                        tv+=shapes[inner[(v,k)]][v]
                    totals[v]=tv
                # backward map per leaf v: [totals[v]] -> range(a_s(v))
                bm_opts=[]
                bm_keys=[]
                ok=True
                for v in range(e):
                    if totals[v]>0 and ar[v]==0:
                        ok=False;break
                    bm_opts.append(list(product(range(ar[v]),repeat=totals[v])))
                    bm_keys.append(v)
                if not ok: continue
                for bmc in product(*bm_opts):
                    bm={bm_keys[i]:bmc_i for i,bmc_i in enumerate(bmc)}
                    opts.append((sdag,inner,bm))
        if not opts:
            return   # some Dom-shape has no delta target -> no lifting
        per_shape.append(opts)
    for choice in product(*per_shape):
        yield list(choice)

def make_delta(shapes,e,data):
    def delta(mm,S,P,elt):
        s,fvs=elt                     # f_v tuple in P[mm[v][v]]
        sdag,inner,bm=data[s]
        adag=shapes[sdag]
        Fbs=[]
        for b in range(e):
            Fb=[]
            offset=0
            for k in range(adag[b]):
                ish=inner[(b,k)]
                nb=shapes[ish][b]     # inner b-pure arity at b
                # g_c: empty for c!=b ; g_b length nb
                gb=tuple(fvs[b][bm[b][offset+j]] for j in range(nb))
                offset+=nb
                g=tuple(gb if c==b else () for c in range(e))
                Fb.append((ish,g))
            Fbs.append(tuple(Fb))
        return (sdag,tuple(Fbs))
    return delta

def enum_liftings(shapes,e,tests_scan,tests_verify,limit=None):
    L_eval,L_act=poly_L(shapes,e)
    monads=[]
    count=0
    epss=list(enum_eps(shapes,e))
    if not epss: return monads,0
    datas=list(enum_delta_data(shapes,e))
    for data in datas:
        delta=make_delta(shapes,e,data)
        for eps_choice in epss:
            def eps(elt,ec=eps_choice):
                s,combo=elt; v,j=ec[s]; return combo[v][j]
            lift=Lifting(e,L_eval,L_act,eps,delta)
            count+=1
            if check_monad(lift,tests_scan)["monad"]:
                if check_monad(lift,tests_verify)["monad"]:   # remove false positives
                    monads.append((eps_choice,data))
            if limit and count>=limit: return monads,count
    return monads,count

if __name__=="__main__":
    e=2
    tests_scan=[Cont(['a'],{'a':[0,1]}), Cont(['a'],{'a':[0,1,2]})]        # |S|=1 cheap
    tests_verify=[Cont(['a','b'],{'a':[0],'b':[0,1]}),                      # distinct leaves
                  Cont(['a','b'],{'a':[0,1],'b':[0,1,2]})]
    # scan a family of small L's (shapes = arity tuples over E=2)
    cand = {
      "Sigma_{0}":      [(1,0)],
      "Sigma_{01}":     [(1,0),(0,1)],
      "PI=B0B1":        [(1,1)],
      "PI+pures":       [(1,1),(1,0),(0,1)],
      "B0^2":           [(2,0)],
      "B0^2+B0":        [(2,0),(1,0)],
      "B0+B0(dup)":     [(1,0),(1,0)],
      "B0B1+B0+B1":     [(1,1),(1,0),(0,1)],  # same as PI+pures
      "B0^2*B1+pures":  [(2,1),(1,0),(0,1)],
    }
    for name,shapes in cand.items():
        monads,count=enum_liftings(shapes,e,tests_scan,tests_verify)
        print(f"{name:16s} shapes={shapes}: {len(monads)} monad(s) out of {count} (eps,delta) combos")
