"""
ATTEMPT 3: Take the rigid_twist (group g at source a, D=E gives (L) true,
(G) false) and ADD a new object w with a D cross arrow into the picture,
arranged so it does NOT disturb the existing holonomy obstruction but DOES
put a genuine cross arrow into D.

Rigid twist: a,x,y; End(a)=Z/2={1a,g}; p,pg:a->x; s,s2:x->y; q,qg:a->y.
D=E={1a,g,1x,1y}.  (L) true, (G) false.

Add object w and arrow d:w->a in D, plus the g-orbit dg? We need D closed:
if d:w->a and g:a->a in D then g o d in D too.  Set End(w)=trivial.
Hom(w,a) = {d, gd}.  This adds a cross arrow d to D while keeping End(a)=Z/2.

But adding d:w->a means new arrows w->x, w->y appear (p o d etc). Must keep
the category consistent and check (L)/(G) still behave.  Crucially Hom(-,b) for
b in {x,y} now also has elements from w; freeness must still hold and (G) fail.
"""
from pairwise_zs_check import FinCat
from pairwise_end_to_end import wide_subcats, is_sfs, Dmodule_is_free, criterion
from pairwise_counterexample_search import validate

def attempt3():
    objs=["w","a","x","y"]
    arrows={
        "1w":("w","w"),"1a":("a","a"),"g":("a","a"),"1x":("x","x"),"1y":("y","y"),
        "p":("a","x"),"pg":("a","x"),
        "s":("x","y"),"s2":("x","y"),
        "q":("a","y"),"qg":("a","y"),
        # new D cross arrow w->a and its g-twist
        "d":("w","a"),"gd":("w","a"),
        # induced arrows w->x, w->y (composites with p,s,q)
        "pd":("w","x"),"pgd":("w","x"),
        "qd":("w","y"),"qgd":("w","y"),
    }
    comp={}
    idof={"w":"1w","a":"1a","x":"1x","y":"1y"}
    for f,(dm,cd) in arrows.items():
        comp[(f,idof[dm])]=f
        comp[(idof[cd],f)]=f
    # End(a)=Z2
    comp[("1a","1a")]="1a"; comp[("1a","g")]="g"; comp[("g","1a")]="g"; comp[("g","g")]="1a"
    comp[("1x","1x")]="1x"; comp[("1y","1y")]="1y"; comp[("1w","1w")]="1w"
    # right End(a) action on a->x, a->y (rigid twist):
    comp[("p","g")]="pg"; comp[("pg","g")]="p"
    comp[("q","g")]="qg"; comp[("qg","g")]="q"
    # cross composites x->y after a->x:
    comp[("s","p")]="q"; comp[("s2","p")]="qg"
    comp[("s","pg")]="qg"; comp[("s2","pg")]="q"
    # ---- new arrow d:w->a, g o d = gd
    comp[("g","d")]="gd"; comp[("g","gd")]="d"
    # p o d = pd, p o gd = (p o g) o d = pg o d ; define consistently:
    #   pd := p o d, pgd := pg o d.  Then p o gd = (p o g) o d = pg o d = pgd.
    #   pg o gd = (pg o g) o d = p o d = pd.
    comp[("p","d")]="pd"; comp[("pg","d")]="pgd"
    comp[("p","gd")]="pgd"; comp[("pg","gd")]="pd"
    # q o d = qd, q o gd = qg o d = qgd, etc
    comp[("q","d")]="qd"; comp[("qg","d")]="qgd"
    comp[("q","gd")]="qgd"; comp[("qg","gd")]="qd"
    # s o pd = s o (p o d) = (s o p) o d = q o d = qd
    comp[("s","pd")]="qd"; comp[("s2","pd")]="qgd"
    # s o pgd = (s o pg) o d = qg o d = qgd ; s2 o pgd = (s2 o pg) o d = q o d = qd
    comp[("s","pgd")]="qgd"; comp[("s2","pgd")]="qd"
    ident=idof
    return FinCat(objs,arrows,comp,ident)

if __name__=="__main__":
    K=attempt3()
    # D = E plus the cross arrows d, gd
    validate(K, {"1w","1a","g","1x","1y","d","gd"}, "attempt3: D=E+{d,gd:w->a}")
