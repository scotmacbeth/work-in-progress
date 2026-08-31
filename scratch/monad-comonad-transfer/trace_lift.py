"""
Trace the biKleisli triple composite to design the CLEANEST witness and expose the
structural chain for the rigorous lift proof.  M = Pf, all objects = A1.

We (1) search for clean witnesses (f,h = J-image 'pure' arrows if possible, or minimal
support), and (2) print each stage's backward action at the witness point (shape b, pos (1,0)).
"""
from entwine import (Cont, Mor, ident, compose, eq, Pf,
                     G_obj, T_obj, G_mor, T_mor,
                     eps_G, delta_G, eta_T, mu_T)
from bikleisli import lax_Pf, kappa, bik_id, bik_comp, enum_mors, welltyped
from itertools import product as iproduct

M = Pf(); lax = lax_Pf
A1 = Cont(['a','b'], {'a':[0,1], 'b':[0]})
OBJ = A1   # p=q=r=z=A1

# J-image ("pure") arrow of a container endomorphism phi: A1 -> A1 :  eta_T . phi . eps
def J(phi):
    return compose(eta_T(M, phi.tgt), compose(phi, eps_G(M, phi.src)))

# enumerate container endomorphisms A1->A1
def endos(A):
    return enum_mors(A, A)

Fpool = enum_mors(G_obj(M,OBJ), T_obj(M,OBJ))
print(f"total arrows A1~>A1: {len(Fpool)}")
Jset = { }
for phi in endos(A1):
    Jphi = J(phi)
    Jset[(tuple(sorted(Jphi.fwd.items())),
          tuple(sorted((s, tuple(sorted(Jphi.bwd[s].items()))) for s in Jphi.bwd)))] = Jphi
print(f"distinct J-image (pure) arrows: {len(Jset)}")
Jarrows = list(Jset.values())

def triple_diff(f,g,h):
    O=OBJ
    gf = bik_comp(M,lax,f,g,O,O,O)
    hg = bik_comp(M,lax,g,h,O,O,O)
    left  = bik_comp(M,lax,gf,h,O,O,O)   # (h.g).f
    right = bik_comp(M,lax,f,hg,O,O,O)   # h.(g.f)
    return left,right, not eq(left,right)

# Search: f,h pure ; g generic
best=None
for f in Jarrows:
    for h in Jarrows:
        for g in Fpool:
            l,r,bad = triple_diff(f,g,h)
            if bad:
                best=(f,g,h,l,r); break
        if best: break
    if best: break
print("\nf,h pure & g generic non-assoc found:", best is not None)

# Search: only g non-pure minimal; f=h=some fixed pure. Also try f=g=h search for symmetry.
sym=None
for g in Fpool:
    l,r,bad=triple_diff(g,g,g)
    if bad:
        sym=(g,l,r); break
print("symmetric f=g=h non-assoc found:", sym is not None)

def show(mor,label):
    print(f"  {label}: fwd={mor.fwd}")
    for s in mor.bwd:
        print(f"      bwd[{s}] = {mor.bwd[s]}")

if best:
    f,g,h,l,r = best
    print("\n=== CLEAN WITNESS (f,h pure, g generic) ===")
    show(f,"f"); show(g,"g"); show(h,"h")
    # locate the differing entry
    for s in l.fwd:
        for c in l.tgt.P[l.fwd[s]]:
            if l.bwd[s].get(c)!=r.bwd[s].get(c):
                print(f"  DIFF @ shape {s}, pos {c}: (h.g).f={l.bwd[s].get(c)}  h.(g.f)={r.bwd[s].get(c)}")

if sym:
    g,l,r=sym
    print("\n=== SYMMETRIC WITNESS f=g=h ===")
    show(g,"g=f=h")
    for s in l.fwd:
        for c in l.tgt.P[l.fwd[s]]:
            if l.bwd[s].get(c)!=r.bwd[s].get(c):
                print(f"  DIFF @ shape {s}, pos {c}: (h.g).f={l.bwd[s].get(c)}  h.(g.f)={r.bwd[s].get(c)}")
