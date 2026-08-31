"""
Find the MINIMAL-support non-associative biKleisli triple for M=Pf on A1, and produce a
full stage-by-stage trace of both bracketings' backward map at shape b.

Minimal = fewest total non-empty backward entries across f,g,h.  We fix forward maps to
the idempotent u = {a:{a}, b:{a,b}} (the overlap-creating one) since that is what the diff
requires, but we let the search confirm minimality over ALL forwards too (small pools).
"""
from entwine import (Cont, Mor, ident, compose, eq, Pf,
                     G_obj, T_obj, G_mor, T_mor,
                     eps_G, delta_G, eta_T, mu_T)
from bikleisli import lax_Pf, kappa, bik_comp, enum_mors
from itertools import product as iproduct

M = Pf(); lax = lax_Pf
A1 = Cont(['a','b'], {'a':[0,1], 'b':[0]}); O=A1

def brackets(f,g,h):
    gf = bik_comp(M,lax,f,g,O,O,O); hg = bik_comp(M,lax,g,h,O,O,O)
    L = bik_comp(M,lax,gf,h,O,O,O); R = bik_comp(M,lax,f,hg,O,O,O)
    return L,R

def support(m):   # count non-empty backward images
    return sum(1 for s in m.bwd for c in m.bwd[s] if m.bwd[s][c])

Fpool = enum_mors(G_obj(M,O), T_obj(M,O))
# restrict to arrows whose forward is the idempotent overlap map (big speedup + relevance)
def fwd_is(m, u): return m.fwd == u
U = {'a': frozenset({'a'}), 'b': frozenset({'a','b'})}
pool = [m for m in Fpool if fwd_is(m,U)]
print(f"arrows with forward u={{'a':{{a}},'b':{{a,b}}}}: {len(pool)}")

best=None; bestscore=10**9
for f in pool:
    for g in pool:
        for h in pool:
            L,R = brackets(f,g,h)
            if not eq(L,R):
                sc = support(f)+support(g)+support(h)
                if sc < bestscore:
                    bestscore=sc; best=(f,g,h,L,R)
print("minimal support total:", bestscore)
f,g,h,L,R = best
def show(m,lab):
    print(f"  {lab}: fwd={dict(m.fwd)}")
    for s in sorted(m.bwd):
        print(f"      bwd[{s}]={m.bwd[s]}")
print("\n=== MINIMAL WITNESS ==="); show(f,"f"); show(g,"g"); show(h,"h")
print("\n(h.g).f backward[b]:", L.bwd['b'])
print("h.(g.f) backward[b]:", R.bwd['b'])
for c in L.tgt.P[L.fwd['b']]:
    if L.bwd['b'].get(c)!=R.bwd['b'].get(c):
        print(f"  DIFF @ shape b, pos {c}:  (h.g).f={L.bwd['b'][c]}   h.(g.f)={R.bwd['b'].get(c)}")

# ---- full stage trace of both bracketings ----
def stages_gf(f,g):
    s1=delta_G(M,O); s2=G_mor(M,f); s3=kappa(M,lax,O); s4=T_mor(M,g); s5=mu_T(M,O)
    return [("delta",s1),("Gf",s2),("kappa",s3),("Tg",s4),("muT",s5)]

print("\n=== STAGE TRACE: g*f  (backward at shape b) ===")
# g*f = muT . Tg . kappa . Gf . delta   ; trace how target pos flows back
gf = bik_comp(M,lax,f,g,O,O,O)
print("  g*f fwd[b]=",gf.fwd['b']," bwd[b]=",gf.bwd['b'])
# Build the outer composite (h.g).f = ( (g*f) then h )  and h.(g.f)=( f then (h*g) )
print("\n  g*f as morphism: shapes/positions")
print("   target shape at b:",gf.fwd['b']," positions there:",gf.tgt.P[gf.fwd['b']])
