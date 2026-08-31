"""
ATTEMPT 2: Put the Z/2 loop DOWNSTREAM, give D a cross arrow that is an
ISO-like map so it doesn't create covering ambiguity.

Key realization from attempt1: a D cross arrow d:a->x makes Hom(a,y) factor
through Hom(x,y).  For freeness, # D-orbits in Hom(a,y) must equal # basis
arrows reachable.  Balance them: make d:a->x in D a *bijection-on-homs* so that
Hom(a,-) and Hom(x,-) are in D-equivariant bijection, and put the Z/2 holonomy
as End in D at x (the target of d).

Construction: objects a, x, y.
  D-part:  d: a->x  (cross), and Z/2 loop g: x->x  (g^2=1x).  identities.
           closure: g o d = d' (another a->x).  So Hom(a,x) cap D = {d, gd}.
  C-part:  arrows x->y: {c, c2}; arrows a->y: {e, ee}.
  Twist so no C-transversal closes.
This makes D = {1a,1x,1y, g, d, gd}.  g is the holonomy loop (now at x, in D),
d is the cross arrow.  Branch is a->x=>y but the group g sits at x in D acting
on the LEFT-composition with c.
"""
from pairwise_zs_check import FinCat
from pairwise_end_to_end import wide_subcats, is_sfs, Dmodule_is_free, criterion
from pairwise_counterexample_search import validate

def attempt2():
    objs=["a","x","y"]
    arrows={
        "1a":("a","a"),"1x":("x","x"),"1y":("y","y"),
        "g":("x","x"),                # Z/2 loop at x, in D
        "d":("a","x"),"gd":("a","x"), # gd = g o d ; both in D
        "c":("x","y"),"c2":("x","y"), # C arrows x->y
        "e":("a","y"),"ee":("a","y"), # a->y
    }
    comp={}
    idof={"a":"1a","x":"1x","y":"1y"}
    # identities
    for f,(dm,cd) in arrows.items():
        comp[(f,idof[dm])]=f
        comp[(idof[cd],f)]=f
    # Z/2 at x
    comp[("g","g")]="1x"
    # g o d = gd, g o gd = d
    comp[("g","d")]="gd"; comp[("g","gd")]="d"
    # C arrows composed with g on the right: c o g = ?, c2 o g = ?
    # We want C closed-candidate selection; define c o g and c2 o g so that
    # cross composites have a twist.  Let c o g = c2, c2 o g = c  (g swaps them).
    comp[("c","g")]="c2"; comp[("c2","g")]="c"
    # composites x->y after a->x:
    #   c o d = e.  Then c o gd = (c o g) o d = c2 o d.  And we set c2 o d = ee.
    #   So define on the four:
    comp[("c","d")]="e"
    comp[("c2","d")]="ee"
    # c o gd: c o (g o d) = (c o g) o d = c2 o d = ee
    comp[("c","gd")]="ee"
    # c2 o gd = (c2 o g) o d = c o d = e
    comp[("c2","gd")]="e"
    # e o (D-endos at a): only 1a.  But also need composites with g acting...
    # a has no nontrivial endo; fine.
    ident=idof
    return FinCat(objs,arrows,comp,ident)

if __name__=="__main__":
    K=attempt2()
    validate(K, {"1a","1x","1y","g","d","gd"}, "attempt2: D={1a,1x,1y,g,d,gd}")
