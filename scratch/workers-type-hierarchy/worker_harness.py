"""
Ground-truth harness: build the graded/Para tensor of Workers and test the
INTERCHANGE law (functoriality of ⊗_W) and UNIT, for each object-tensor ⋆.

Worker w : p ->_G q  is a container morphism  mor : ΔG ⊗ p -> q.
We store (G, p, q, mor) with G a list (the grade set).

Composition  (w1: p->_S q) then (w2: q->_T r)  = p ->_{S×T} r :
    ΔS⊗p --w1--> q,  ΔT⊗q --w2--> r.
    build on ΔT⊗(ΔS⊗p) : (ΔT⊗w1) then w2 ; relabel to Δ(S×T)⊗p.
Grade convention: result grade set = [(s,t) ...] (we relabel T×S inner split to S×T).

Tensor  (w1: p->_S q) ⊗ (w2: p'->_T q') = p⋆p' ->_{S×T} q⋆q' :
    Δ(S×T)⊗(p⋆p') --Φ^⋆--> (ΔS⊗p)⋆(ΔT⊗q') ... --w1⋆w2--> q⋆q'.
"""
from containers import *
from coherence import tensor_mor, prod_mor, coprod_mor, lhd_mor, eps
from frameworkA import phi_tensor, phi_prod, phi_coprod
from frameworkA_lhd import phi_lhd

def idmor(p): return Mor(p,p,{a:a for a in p.shapes},{a:{d:d for d in p.fib[a]} for a in p.shapes})

# relabel a container's shapes/positions by bijections (returns a new Cont + iso both ways)
def relabel_grade_tensor_source(Ginner_list, Gouter_list, p, order):
    """Return iso between tensor(deltaS(prod_list), p) and
       tensor(deltaS(Gouter), tensor(deltaS(Ginner), p)) as dict maps.
       order: how prod grade (g,) corresponds to (outer,inner)."""
    pass

class Worker:
    def __init__(self, G, p, q, mor):
        self.G=G; self.p=p; self.q=q; self.mor=mor  # mor: tensor(deltaS(G),p)->q
    def check(self):
        src=tensor(deltaS(self.G), self.p)
        assert self.mor.src.shapes==src.shapes, "src mismatch"
        ok,msg=self.mor.validate(); return ok,msg

def prod_list(A,B): return [(a,b) for a in A for b in B]

def compose(w1, w2):
    # w1: p->_S q ; w2: q->_T r ; result p ->_{S×T} r
    S,T=w1.G,w2.G
    p,q,r=w1.p,w1.q,w2.q
    # ΔT⊗(ΔS⊗p) --ΔT⊗w1--> ΔT⊗q --w2--> r
    dTw1 = tensor_mor(idmor(deltaS(T)), w1.mor)       # ΔT⊗(ΔS⊗p) -> ΔT⊗q
    inner = compose_mor(dTw1, w2.mor)                 # ΔT⊗(ΔS⊗p) -> r  (shapes (t,(s,a)))
    # relabel source ΔT⊗(ΔS⊗p) [shapes (t,(s,a)), fib T×(S×Ba)] to Δ(S×T)⊗p [shapes ((s,t),a), fib (S×T)×Ba]
    G=prod_list(S,T)
    src=tensor(deltaS(G), p)   # shapes ((s,t),a), fib [((s2,t2),b)]
    fwd={}; bwd={}
    for sh in src.shapes:
        (s,t),a=sh
        tsh=(t,(s,a))          # corresponding shape in inner.src
        fwd[sh]=inner.fwd[tsh] # forward to r (same target)
        # position relabel: inner.src fib at tsh = T×(S×Ba) elements (t2,(s2,b));
        # src fib at sh = (S×T)×Ba elements ((s2,t2),b). bwd of result at target-pos d:
        e=inner.fwd[tsh]
        bwd[sh]={}
        for d in r.fib[e]:
            val=inner.bwd[tsh][d]  # (t2,(s2,b))
            t2,(s2,b)=val
            bwd[sh][d]=((s2,t2),b)
    mor=Mor(src,r,fwd,bwd)
    return Worker(G,p,r,mor)

def compose_mor(m1,m2):
    from containers import compose as cc
    return cc(m1,m2)

STARS={
 '⊗': (tensor, tensor_mor, phi_tensor),
 '×': (prod,   prod_mor,   phi_prod),
 '+': (coprod, coprod_mor, phi_coprod),
 '◁': (lhd,    lhd_mor,    phi_lhd),
}

def tensorW(w1, w2, star):
    star_obj, star_mor, phi = STARS[star]
    S,T=w1.G,w2.G
    G=prod_list(S,T)
    p,q,p2,q2=w1.p,w1.q,w2.p,w2.q
    Phi=phi(S,T,p,p2)                          # Δ(S×T)⊗(p⋆p2) -> (ΔS⊗p)⋆(ΔT⊗p2)
    if isinstance(Phi,tuple): raise RuntimeError("phi missing")
    fg = star_mor(w1.mor, w2.mor)              # (ΔS⊗p)⋆(ΔT⊗p2) -> q⋆q2
    mor = compose_mor(Phi, fg)                 # Δ(S×T)⊗(p⋆p2) -> q⋆q2
    return Worker(G, star_obj(p,p2), star_obj(q,q2), mor)

def eq_upto_grade(wa, wb):
    """Compare two workers p->r with grades that are products in possibly different
       association/order. Compare underlying morphisms up to a grade bijection on the
       ΔG factor. We test: exists bijection beta: Ga->Gb with mor equal."""
    if wa.p.shapes!=wb.p.shapes or wa.q.shapes!=wb.q.shapes: return False
    Ga, Gb = wa.G, wb.G
    if len(Ga)!=len(Gb): return False
    from itertools import permutations
    # try all bijections Ga->Gb (small)
    for perm in permutations(Gb):
        beta=dict(zip(Ga,perm))
        if _mor_eq_under_beta(wa.mor, wb.mor, beta, wa.p):
            return True
    return False

def _mor_eq_under_beta(ma, mb, beta, p):
    # ma,mb: ΔGa⊗p -> q  and ΔGb⊗p -> q. shape (g,a) -> (beta g, a). positions (g2,b)->(beta g2,b)
    for (g,a) in ma.src.shapes:
        sh_a=(g,a); sh_b=(beta[g],a)
        if str(ma.fwd[sh_a])!=str(mb.fwd[sh_b]): return False
        e=ma.fwd[sh_a]
        for d in ma.tgt.fib[e]:
            va=ma.bwd[sh_a][d]      # (g2,b)
            vb=mb.bwd[sh_b][d]      # (g2',b)
            g2,b=va; g2b,bb=vb
            if not (beta[g2]==g2b and str(b)==str(bb)): return False
    return True
