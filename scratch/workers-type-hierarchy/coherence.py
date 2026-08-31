"""
Coherence tests for the oplax comparison maps n^*_S.
Decisive test: counit coherence
    (ε_p ⋆ ε_q) ∘ n^*_{p,q}  ==  ε_{p⋆q}   as morphisms W(p⋆q) -> p⋆q.
Also associativity coherence.
ε_p : ΔS⊗p -> p   store counit: fwd (s,a)|->a ; bwd b|->(s,b).
"""
from containers import *
from test_maps import test_coprod, test_prod, test_tensor, test_lhd, small_conts

def eps(S,p):
    W = tensor(deltaS(S),p)
    fwd={}; bwd={}
    for sh in W.shapes:
        s,a = sh
        fwd[sh]=a
        bwd[sh]={}
        for b in p.fib[a]:
            bwd[sh][b]=(s,b)   # current-state s
    return Mor(W,p,fwd,bwd)

# functoriality of each ⋆ on morphisms: given f:p->p', g:q->q' build f⋆g
def coprod_mor(f,g):
    L=coprod(f.src,g.src); R=coprod(f.tgt,g.tgt)
    fwd={}; bwd={}
    for sh in L.shapes:
        side,x=sh
        if side=='l':
            fwd[sh]=('l',f.fwd[x]); bwd[sh]={d:f.bwd[x][d] for d in f.tgt.fib[f.fwd[x]]}
        else:
            fwd[sh]=('r',g.fwd[x]); bwd[sh]={d:g.bwd[x][d] for d in g.tgt.fib[g.fwd[x]]}
    return Mor(L,R,fwd,bwd)

def prod_mor(f,g):
    L=prod(f.src,g.src); R=prod(f.tgt,g.tgt)
    fwd={}; bwd={}
    for (a,c) in L.shapes:
        fa,gc=f.fwd[a],g.fwd[c]; fwd[(a,c)]=(fa,gc)
        d={}
        for pos in R.fib[(fa,gc)]:
            side,x=pos
            if side=='l': d[pos]=('l',f.bwd[a][x])
            else: d[pos]=('r',g.bwd[c][x])
        bwd[(a,c)]=d
    return Mor(L,R,fwd,bwd)

def tensor_mor(f,g):
    L=tensor(f.src,g.src); R=tensor(f.tgt,g.tgt)
    fwd={}; bwd={}
    for (a,c) in L.shapes:
        fa,gc=f.fwd[a],g.fwd[c]; fwd[(a,c)]=(fa,gc)
        d={}
        for (bd) in R.fib[(fa,gc)]:
            b2,d2=bd
            d[bd]=(f.bwd[a][b2], g.bwd[c][d2])
        bwd[(a,c)]=d
    return Mor(L,R,fwd,bwd)

def lhd_mor(f,g):
    # f:p->p', g:q->q'  ==> p◁q -> p'◁q'
    L=lhd(f.src,g.src); R=lhd(f.tgt,g.tgt)
    fwd={}; bwd={}
    for sh in L.shapes:
        a,gamma=sh
        Ba=f.src.fib[a]
        fa=f.fwd[a]
        Bfa=f.tgt.fib[fa]
        # new gamma': for each position of Bfa (index j), the src position is f.bwd[a] at it
        # gamma' (j) = g.fwd[ gamma[ index of f.bwd[a][pos_j] in Ba ] ]
        newgamma=[]
        for posj in Bfa:
            b = f.bwd[a][posj]       # a position in Ba
            i = Ba.index(b)
            c = gamma[i]
            newgamma.append(g.fwd[c])
        newgamma=tuple(newgamma)
        tgt=(fa,newgamma)
        fwd[sh]=tgt
        d={}
        for pos in R.fib[tgt]:   # pos=(posj, dd) with posj in Bfa, dd in D'(newgamma at j)
            posj,dd=pos
            j=Bfa.index(posj)
            b=f.bwd[a][posj]; i=Ba.index(b)
            c=gamma[i]
            db=g.bwd[c][dd]      # position in D(c)
            d[pos]=(b,db)
        bwd[sh]=d
    return Mor(L,R,fwd,bwd)

def check_counit(S, star_name):
    conts=small_conts()
    allok=True
    for p in conts:
        for q in conts:
            if star_name=='+':
                n=test_coprod(S,p,q); sm=coprod_mor(eps(S,p),eps(S,q)); pq=coprod(p,q)
            elif star_name=='x':
                n=test_prod(S,p,q); sm=prod_mor(eps(S,p),eps(S,q)); pq=prod(p,q)
            elif star_name=='t':
                n=test_tensor(S,p,q,'left'); sm=tensor_mor(eps(S,p),eps(S,q)); pq=tensor(p,q)
            elif star_name=='l':
                n=test_lhd(S,p,q);
                if isinstance(n,tuple):
                    allok=False; print("   lhd missing shape"); continue
                sm=lhd_mor(eps(S,p),eps(S,q)); pq=lhd(p,q)
            lhs=compose(n, sm)          # W(p⋆q) --n--> Wp⋆Wq --ε⋆ε--> p⋆q
            rhs=eps(S,pq)               # W(p⋆q) --ε--> p⋆q
            ov,_=lhs.validate(); ov2,_=rhs.validate()
            if not (ov and ov2):
                allok=False; print("   INVALID compose"); continue
            if not eq_mor(lhs,rhs):
                allok=False
                # print a witness
                print(f"   COUNIT FAILS at p={p.shapes},q={q.shapes}")
    return allok

if __name__=='__main__':
    S=['s0','s1']
    for name,label in [('+','coproduct +'),('x','product ×'),('t','Dirichlet ⊗ (merge=left)'),('l','substitution ◁')]:
        ok=check_counit(S,name)
        print(f"COUNIT COHERENCE  {label}:  {'HOLDS' if ok else 'FAILS'}")
