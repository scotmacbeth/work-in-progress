"""
Framework-B unit-law test for ◁ (substitution), and confirmation that ⊗ needs
a genuine monoid on S (projection fails the counit/unit law; a real monoid passes).

Oplax monoidal functor (W=ΔS⊗(−), n, n_0) w.r.t (◁, y).
LEFT unit law:  Wp --W(l^{-1})--> W(y◁p) --n--> Wy ◁ Wp --n_0◁id--> y◁Wp --l--> Wp   == id.
RIGHT unit law: Wp --W(r^{-1})--> W(p◁y) --n--> Wp ◁ Wy --id◁n_0--> Wp◁y --r--> Wp   == id.
We test the p-side candidate n^◁ and see if either unit law fails.

For ◁: y = ([*],{*:['0']}); y◁p = p up to iso; p◁y = p up to iso.
n_0 : Wy = ΔS -> y  (fwd s->*, bwd '0'-> e_s), parametrised by basepoint e.
"""
from containers import *
from test_maps import test_lhd, small_conts

def n0_map(S, e):     # ΔS -> y ; e: dict s-> chosen element of S
    W=deltaS(S); Y=Cont(['*'],{'*':['0']})
    fwd={s:'*' for s in S}
    bwd={s:{'0': e[s]} for s in S}
    return Mor(W,Y,fwd,bwd)

def lhd_mor_general(f,g):
    from coherence import lhd_mor
    return lhd_mor(f,g)

def id_mor(p):
    return Mor(p,p,{a:a for a in p.shapes},{a:{d:d for d in p.fib[a]} for a in p.shapes})

def test_left_unit_lhd(S, p, e):
    # y◁p == p  (strict? build iso). In our lhd(y,p): shapes (*, gamma) gamma:['0']->p.shapes
    # gamma is a 1-tuple (c,) ; position ('0',d) d in p.fib[c].  So lhd(y,p) ≅ p via (*, (c,))<->c.
    Y=Cont(['*'],{'*':['0']})
    ylp=lhd(Y,p)
    # iso l: ylp -> p
    l_fwd={}; l_bwd={}
    for sh in ylp.shapes:
        star,gamma=sh; c=gamma[0]
        l_fwd[sh]=c; l_bwd[sh]={d:('0',d) for d in p.fib[c]}
    l=Mor(ylp,p,l_fwd,l_bwd)
    # We test:  W(l) then invert? Simpler: check that composite equals ε-free identity on Wp.
    # Build the whole composite as morphisms Wp -> Wp and compare to id.
    Wp=tensor(deltaS(S),p)
    # W(l^{-1}) : Wp -> W(ylp).  l^{-1}: p->ylp
    linv=Mor(p,ylp,{c: (('*',(c,))) for c in p.shapes} , None)
    # build linv properly
    linv_fwd={c:('*',(c,)) for c in p.shapes}
    linv_bwd={}
    for c in p.shapes:
        tsh=('*',(c,))
        linv_bwd[c]={pos: pos[1] for pos in ylp.fib[tsh]}  # ('0',d)->d
    linv=Mor(p,ylp,linv_fwd,linv_bwd)
    # W(linv): Wp -> W(ylp)
    from coherence import tensor_mor
    Wlinv=tensor_mor(id_mor(deltaS(S)), linv)   # ΔS⊗p -> ΔS⊗(ylp)
    # n_{y,p}: W(ylp)=ΔS⊗(y◁p) -> Wy ◁ Wp
    n=test_lhd(S,Y,p)
    if isinstance(n,tuple):
        return ('missing',n)
    # n_0 ◁ id : (ΔS◁?)... Wy◁Wp = (ΔS)◁(ΔS⊗p); apply n_0 on outer: -> y◁Wp
    n0=n0_map(S,e)
    n0_lhd_id = lhd_mor_general(n0, id_mor(tensor(deltaS(S),p)))  # ΔS◁Wp -> y◁Wp
    # l' : y◁Wp -> Wp   (left unitor at Wp)
    Y2=Cont(['*'],{'*':['0']}); ylWp=lhd(Y2, Wp)
    lWp_fwd={}; lWp_bwd={}
    for sh in ylWp.shapes:
        star,gamma=sh; c=gamma[0]
        lWp_fwd[sh]=c; lWp_bwd[sh]={d:('0',d) for d in Wp.fib[c]}
    lWp=Mor(ylWp,Wp,lWp_fwd,lWp_bwd)
    # compose everything: Wp -Wlinv-> W(ylp) -n-> ΔS◁Wp -n0◁id-> y◁Wp -lWp-> Wp
    comp = compose(compose(compose(Wlinv,n), n0_lhd_id), lWp)
    ok,msg=comp.validate()
    if not ok: return ('invalid',msg)
    return ('eq' if eq_mor(comp, id_mor(Wp)) else 'NEQ', None)

if __name__=='__main__':
    S=['s0','s1']
    # basepoint choices to try for e_s
    e_id = {s:s for s in S}           # e_s = s
    e_const = {s:S[0] for s in S}     # e_s = s0
    for p in small_conts():
        r1=test_left_unit_lhd(S,p,e_id)
        r2=test_left_unit_lhd(S,p,e_const)
        print(f"p={p.shapes}: LEFT-unit ◁  e=id ->{r1}   e=const ->{r2}")
