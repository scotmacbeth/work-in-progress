"""
Trace the KNOWN non-associative witness triple (from the bikleisli hunt) stage by stage.
M = Pf, all objects A1.  Verify non-assoc and dump the structural chain at shape b.
"""
from entwine import (Cont, Mor, compose, eq, Pf,
                     G_obj, T_obj, G_mor, T_mor, eps_G, delta_G, eta_T, mu_T)
from bikleisli import lax_Pf, kappa, bik_comp

M = Pf(); lax = lax_Pf
A1 = Cont(['a','b'], {'a':[0,1], 'b':[0]}); O=A1
fs = frozenset
Gp, Tq = G_obj(M,O), T_obj(M,O)

def arrow(bwd):
    fwd = {'a': fs({'a'}), 'b': fs({'a','b'})}
    return Mor(Gp, Tq, fwd, bwd)

# positions:  Tq at shape {a}   = P*({a}) = P(a) = {0,1}, encoded as tuples (0,),(1,)
#             Tq at shape {a,b} = P(a)xP(b) = {(0,0),(1,0)}
# source Gp positions at a = Pf(P a)=Pf{0,1}: 0-> subsets;  at b = Pf(P b)=Pf{0}
f = arrow({'a': {(0,): fs(), (1,): fs()},
           'b': {(0,0): fs(), (1,0): fs({0})}})
g = arrow({'a': {(0,): fs(), (1,): fs({1})},
           'b': {(0,0): fs({0}), (1,0): fs()}})
h = arrow({'a': {(0,): fs(), (1,): fs({0,1})},
           'b': {(0,0): fs(), (1,0): fs({0})}})

gf = bik_comp(M,lax,f,g,O,O,O)
hg = bik_comp(M,lax,g,h,O,O,O)
L  = bik_comp(M,lax,gf,h,O,O,O)   # (h*g)*f
R  = bik_comp(M,lax,f,hg,O,O,O)   # h*(g*f)
print("non-associative:", not eq(L,R))
print("L=(h*g)*f fwd:",dict(L.fwd)); print("R=h*(g*f) fwd:",dict(R.fwd))
print("L.bwd['b']:", L.bwd['b'])
print("R.bwd['b']:", R.bwd['b'])
for c in L.tgt.P[L.fwd['b']]:
    if L.bwd['b'].get(c)!=R.bwd['b'].get(c):
        print(f"  DIFF @ shape b pos {c}:  L={L.bwd['b'][c]}  R={R.bwd['b'].get(c)}")

print("\n--- intermediate composites ---")
print("g*f  fwd:",dict(gf.fwd)); print("g*f  bwd[b]:",gf.bwd['b'])
print("h*g  fwd:",dict(hg.fwd)); print("h*g  bwd[b]:",hg.bwd['b'])

# Now decompose the OUTER composition (h*g)*f = muT.T(h).kappa.G(gf... no:
# (h*g)*f uses the arrow (h*g):q~>z composed after f? No: bik associativity is
#   left  = ((g*f) then h)  wait: our brackets: L = bik_comp(gf,h) = h*(g*f)?? recheck labels
# bik_comp(M,lax,X,Y) computes Y*X (X:p~>q, Y:q~>r) => X then Y.  So:
#   gf = bik_comp(f,g) = g*f  (f then g)
#   L  = bik_comp(gf,h) = h*(g*f)      <-- RIGHT assoc actually
#   R  = bik_comp(f,hg) = (h*g)*f      <-- LEFT assoc
# (naming doesn't matter; they differ). Trace L's outer stages:
print("\n--- outer stage trace for L = bik_comp(gf,h) : the 5 stages ---")
X, Y = gf, h            # X: p~>r (=g*f), Y: r~>z (=h)
d  = delta_G(M,O)       # Gp -> GGp
Gx = G_mor(M,X)         # GGp -> G T r
k  = kappa(M,lax,O)     # G T r -> T G r
Ty = T_mor(M,Y)         # T G r -> T T z
m  = mu_T(M,O)          # T T z -> T z
for nm,st in [("delta",d),("G(g*f)",Gx),("kappa",k),("T(h)",Ty),("muT",m)]:
    print(f"  {nm}: fwd[b or img]... bwd at b-relevant shape")
# compose step by step and show backward[b]
c1 = d
c2 = compose(Gx,d)
c3 = compose(k,c2)
c4 = compose(Ty,c3)
c5 = compose(m,c4)
for nm,c in [("delta",c1),("G(g*f).delta",c2),("kappa..",c3),("T(h)..",c4),("muT.. =L",c5)]:
    print(f"  after {nm}: fwd[b]={c.fwd['b']}  bwd[b]={c.bwd['b']}")

print("\n--- outer stage trace for R = bik_comp(f,hg) : the 5 stages ---")
X2, Y2 = f, hg          # X2: p~>q (=f), Y2: q~>z (=h*g)
d2  = delta_G(M,O)
Gx2 = G_mor(M,X2)       # GGp -> G T q
k2  = kappa(M,lax,O)
Ty2 = T_mor(M,Y2)
m2  = mu_T(M,O)
r1=d2; r2=compose(Gx2,d2); r3=compose(k2,r2); r4=compose(Ty2,r3); r5=compose(m2,r4)
for nm,c in [("delta",r1),("G(f).delta",r2),("kappa..",r3),("T(h*g)..",r4),("muT.. =R",r5)]:
    print(f"  after {nm}: fwd[b]={c.fwd['b']}  bwd[b]={c.bwd['b']}")

# Pinpoint the E2' element: after G(.).delta at shape b the target shape is {a,b};
# T(.) turns it into the overlap {{a},{a,b}}.  Show the pre-muT position tuple at (1,0)-relevant.
print("\n--- E2' element identification ---")
print("L: shape after G(g*f).delta at b -> Pf-shape:", c2.fwd['b'], " ; after T(h): ", c4.tgt.S and 'see fwd', L.fwd['b'])
print("L T(h)-image shape of {a,b}:", frozenset(h.fwd[x] for x in c2.fwd['b']))
print("R T(h*g)-image shape of {a,b}:", frozenset(hg.fwd[x] for x in r2.fwd['b']))

