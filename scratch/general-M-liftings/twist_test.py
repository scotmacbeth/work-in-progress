"""
MORPHISM-level holonomy test. Build 𝕊×C but TWIST the transport by a category automorphism
alpha_g of C, depending on the 𝕊-arrow g (i.e. on g as endofunction). If alpha is a nontrivial
functor S^S -> Aut(C) (holonomy on morphisms), does it lift?
Predicted: fails unless alpha trivial (endpoint-locality + unit => alpha_{g}=alpha depends only on
endpoints and alpha_{s->s}=id => trivial).

C = Z/n as one-object category (morphisms = Z/n, composition = +). Aut(Z/n as monoid-category) =
group automorphisms of Z/n = units mod n. Twist alpha_g = multiplication by a unit depending on g.
The delta: composite object (s,*) over sigma, factor (T,tvec):
  outer (s,*)@T; per out-morphism f in Z/n: inner (T(s),*)@tvec[s];
  beta((f, q)) = alpha_T(f) 'composed' with q ... we twist the C-composition transport by alpha_T.
We implement: beta[(ai=f, bi=q)] = index of ( q + alpha_T(f) )  [twisted grafting].
Trivial alpha (identity) recovers the product (should pass). Nontrivial alpha should FAIL.
"""
from itertools import product
import honest, lean_assoc
S=[0,1]; SS=honest.SS; ID=honest.ID; thread=honest.thread; NM=honest.NM

def build_twisted_Zn(n, alpha):
    """alpha: dict g(in SS) -> unit in Z/n (a group automorphism m|->alpha[g]*m mod n).
       one object '*' at each state; out-degree n (morphisms of Z/n)."""
    # objects: (s,'*') for s in S ; index
    lst=[]; idx={}
    for s in S:
        idx[(s,'*')]=len(lst); lst.append((n,0) if s==0 else (0,n))
    A={sig:list(lst) for sig in SS}; IDX={sig:dict(idx) for sig in SS}
    # eps on A_id: marked position = identity morphism 0
    eps={idx[(s,'*')]:0 for s in S}          # slot 0 = morphism 0 (identity of Z/n)
    delta={}
    for T in SS:
        for tvec in product(SS,repeat=2):
            sig=thread(T,tvec); route={}
            for s in S:
                j=IDX[sig][(s,'*')]; out_j=IDX[T][(s,'*')]
                inner={}; beta={}
                a=alpha[T]                    # twist by outer grade T
                for f in range(n):            # out-position f (a morphism c->c) at outer obj, slot f
                    inner[f]=IDX[tvec[s]][(T[s],'*')]
                    for q in range(n):        # out-position of inner obj
                        # twisted composite: g = q + a*f  mod n   (a=1 => plain grafting = product)
                        g=(q + a*f) % n
                        beta[(f,q)]=g
                route[j]=(out_j, inner, beta)
            delta[(T,tvec)]=route
    return A,eps,delta

def test(name,n,alpha):
    A,eps,delta=build_twisted_Zn(n,alpha)
    u=honest.check_units_fast(A,eps,delta)
    a=lean_assoc.assoc_sample(A,eps,delta,(['a'],{'a':('a0','a1')}),nsamp=400,seed=3)
    print(f"{name}: units={u} assoc={a}")

# trivial twist alpha=1 everywhere (=product 𝕊×Z/3) -> should PASS
test("Z/3 trivial twist (alpha=1)", 3, {g:1 for g in SS})
# nontrivial twist: alpha_g = 2 (inversion, unit mod 3) for g=sw, else 1 -> holonomy -> should FAIL
test("Z/3 twist alpha_sw=2 (inversion holonomy)", 3, {g:(2 if g==(1,0) else 1) for g in SS})
# twist by 2 for ALL g (constant nontrivial): alpha_{s->s}=2 too => violates unit-triviality? test
test("Z/3 twist alpha=2 everywhere", 3, {g:2 for g in SS})
# twist depending on g only via endpoint but nontrivial on a loop: alpha_id=1 but alpha_{c0}=2 (c0:0->0 loop, 1->0)
test("Z/3 twist alpha_c0=2 (loop at 0 nontrivial)", 3, {g:(2 if g==(0,0) else 1) for g in SS})
