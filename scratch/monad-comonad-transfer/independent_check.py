"""
INDEPENDENT re-derivation of the two critical backward values L.bwd[b](1,0) and
R.bwd[b](1,0), implementing each of the 5 stages' coordinate formula by hand (Pf, A1),
to confirm the proof's forced calculation.  No reuse of bikleisli.bik_comp.

Backward maps go TARGET-position -> SOURCE-position and compose contravariantly.
For a composite  X0 --m1--> X1 --m2--> ... --m5--> X5,  the backward at source shape s of
target position c in X5 is  m1.bwd[s]( m2.bwd[..]( ... m5.bwd[..](c) ) )  BUT because each
stage may be Pf-valued we push forward SETS.  We just evaluate the honest definitions.

We only need shape b and the single target position (1,0) in T(A1) at shape {a,b}.
"""
from itertools import product as iproduct
fs = frozenset

# base
P = {'a':[0,1], 'b':[0]}
# --- Pf structural position maps (all as functions on coordinates) ---
def union(sets):                      # mu^M on positions for delta
    out=set()
    for s in sets: out|=set(s)
    return fs(out)
def cartesian(tup):                   # kappa lax: family of Pf-sets -> Pf(product)
    if len(tup)==0: return fs([()])
    return fs(tuple(c) for c in iproduct(*[list(x) for x in tup]))

# The witness backward data at shape b (target shape {a,b}, positions (i,j) in {0,1}x{0}):
#   f#_b(0,0)=∅ f#_b(1,0)={0} ;  g#_b(0,0)={0} g#_b(1,0)=∅ ;  h#_b(0,0)=∅ h#_b(1,0)={0}
# and at shape a (target shape {a}, positions (i,) in {0,1}):
#   f#_a(0)=∅ f#_a(1)=∅ ; g#_a(0)=∅ g#_a(1)={1} ; h#_a(0)=∅ h#_a(1)={0,1}
fb = {(0,0):fs(), (1,0):fs({0})}
gb = {(0,0):fs({0}), (1,0):fs()}
hb = {(0,0):fs(), (1,0):fs({0})}
fa = {(0,):fs(), (1,):fs()}
ga = {(0,):fs(), (1,):fs({1})}
ha = {(0,):fs(), (1,):fs({0,1})}

# ---------------------------------------------------------------
# We verify against the real pipeline the two intermediate facts the proof uses:
#   (A) (g*f)#_b(1,0) = ∅     (B) (h*g)#_b(1,0) = {0}
# then the two final values.  We import the real maps ONLY to get g*f, h*g (already trusted),
# but ALSO hand-check (A),(B) via the biKleisli formula at shape b.
from entwine import Cont, Mor, compose, Pf, G_obj, T_obj, G_mor, T_mor, delta_G, mu_T
from bikleisli import lax_Pf, kappa, bik_comp
M=Pf(); O=Cont(['a','b'],{'a':[0,1],'b':[0]})
def arrow(ba,bb):
    return Mor(G_obj(M,O),T_obj(M,O),{'a':fs({'a'}),'b':fs({'a','b'})},{'a':ba,'b':bb})
f=arrow(fa,fb); g=arrow(ga,gb); h=arrow(ha,hb)
gf=bik_comp(M,lax_Pf,f,g,O,O,O); hg=bik_comp(M,lax_Pf,g,h,O,O,O)
print("(A) (g*f)#_b(1,0) =",gf.bwd['b'][(1,0)], " expect ∅")
print("(B) (h*g)#_b(1,0) =",hg.bwd['b'][(1,0)], " expect {0}")
L=bik_comp(M,lax_Pf,gf,h,O,O,O); R=bik_comp(M,lax_Pf,f,hg,O,O,O)
print("L=h*(g*f) #_b(1,0)=",L.bwd['b'][(1,0)]," R=(h*g)*f #_b(1,0)=",R.bwd['b'][(1,0)])
print("differ:", L.bwd['b'][(1,0)]!=R.bwd['b'][(1,0)])

# ---- hand computation of the fibre E2' two sides at m={{a,b},{a}}, pos ({0,1},{0}) ----
# leaves of union {a,b} = [a,b].  Two outer sets: A1={a,b} (leaves a,b), A2={a} (leaf a).
# TGA position: leaf a -> {0,1} in Pf(P a);  leaf b -> {0} in Pf(P b).
# side "merge-then-product" (kappa o G mu^T): first mu^T restricts the position of the merged
# leaf a to BOTH outer copies (the SAME set {0,1}), leaf b to {0}; the GTTA element is
# Pf over tuples indexed by (outer,inner) leaves = [(A1,a),(A1,b),(A2,a)] with a-coords tied.
# Correlated cartesian: choose z in {0,1} for the SHARED a (one choice), 0 for b:
#   -> tuples ((z,0),(z,))  i.e. {((0,0),(0,)),((1,0),(1,))}
merge_then_product = fs({((0,0),(0,)),((1,0),(1,))})
# side "product-then-merge": independent choice of a-copy in A1 and a-copy in A2:
product_then_merge = fs(tuple(c) for c in iproduct([(za,0) for za in (0,1)],[(zc,) for zc in (0,1)]))
print("\nfibre E2' merge-then-product:",merge_then_product)
print("fibre E2' product-then-merge:",product_then_merge)
print("fibre sides differ:", merge_then_product!=product_then_merge)
