"""
Count labeled small categories with a prescribed object set and out-degrees,
to verify the bijection  #(monad liftings of Reader with underlying poly L)
                        = #(small categories realizing L's pure leaf-graph).

For a PURE polynomial L (every shape reads exactly one leaf v with arity d),
objects = shapes, each object s has leaf lambda(s) and out-degree d_s.
Leaves are independent (disjoint union), so total = product over leaves of
#categories on that leaf's objects with those out-degrees.
"""
from itertools import product

def count_categories(outdeg):
    """outdeg: list of out-degrees d_i (>=1) for objects 0..n-1 (single leaf).
       Count labeled category structures: arrows out of i are labeled 0..d_i-1,
       identity is one chosen label, each non-id arrow has a target, composition
       table satisfies unit + associativity."""
    n=len(outdeg)
    objs=range(n)
    # arrows out of i: labels 0..d_i-1
    Aidx={i:list(range(outdeg[i])) for i in objs}
    total=0
    # choose identity label per object
    for idchoice in product(*[range(outdeg[i]) for i in objs]):
        idlab={i:idchoice[i] for i in objs}
        # choose targets for each arrow; id_i has target i
        # non-id arrows: assign target in objs
        nonid=[(i,a) for i in objs for a in Aidx[i] if a!=idlab[i]]
        for tgtchoice in product(*[objs for _ in nonid]):
            tgt={}
            for i in objs:
                tgt[(i,idlab[i])]=i
            for k,(i,a) in enumerate(nonid):
                tgt[(i,a)]=tgtchoice[k]
            # now enumerate composition tables g(a,b): a:i->j (a in A_i, tgt=j), b in A_j (b:j->k)
            #   result in A_i with tgt=k. Unit constraints fix some entries.
            # Build list of (a,b) pairs needing definition (composable), with allowed results.
            pairs=[]   # (i,a,j,b,k)
            for i in objs:
                for a in Aidx[i]:
                    j=tgt[(i,a)]
                    for b in Aidx[j]:
                        k=tgt[(j,b)]
                        pairs.append((i,a,j,b,k))
            # allowed result for (i,a,j,b,k): arrows in A_i with target k
            def results(i,k):
                return [c for c in Aidx[i] if tgt[(i,c)]==k]
            # unit-forced: b∘id_i = b (i==j, a=id_i): result b (but b in A_i? b in A_i since j=i)
            #             id_j∘a = a (b=id_j): result a
            forced={}
            ok=True
            for (i,a,j,b,k) in pairs:
                if a==idlab[i]:      # id_i ; b∘id_i = b, need i==... a=id_i:i->i so j=i
                    forced[(i,a,j,b)]=b
                if b==idlab[j]:      # id_j ; id_j∘a = a
                    if (i,a,j,b) in forced and forced[(i,a,j,b)]!=a:
                        ok=False;break
                    forced[(i,a,j,b)]=a
            if not ok: continue
            # free pairs
            free=[(i,a,j,b,k) for (i,a,j,b,k) in pairs if (i,a,j,b) not in forced]
            # enumerate results for free pairs
            choice_lists=[]
            for (i,a,j,b,k) in free:
                r=results(i,k)
                if not r: choice_lists=None;break
                choice_lists.append(r)
            if choice_lists is None: continue
            for combo in (product(*choice_lists) if choice_lists else [()]):
                comp={}
                for (i,a,j,b) ,val in forced.items():
                    comp[(i,a,b)]=val
                for idx,(i,a,j,b,k) in enumerate(free):
                    comp[(i,a,b)]=combo[idx]
                # check associativity: (c∘b)∘a = c∘(b∘a) for composable a:i->j,b:j->k,c:k->l
                good=True
                for i in objs:
                    for a in Aidx[i]:
                        j=tgt[(i,a)]
                        for b in Aidx[j]:
                            k=tgt[(j,b)]
                            for c in Aidx[k]:
                                # b∘a
                                ba=comp[(i,a,b)]         # in A_i, target k
                                # c∘(b∘a)
                                lhs=comp[(i,ba,c)]
                                # c∘b
                                cb=comp[(j,b,c)]         # in A_j, target l
                                rhs=comp[(i,a,cb)]
                                if lhs!=rhs: good=False;break
                            if not good:break
                        if not good:break
                    if not good:break
                if good: total+=1
    return total

if __name__=="__main__":
    # single-leaf checks against enum monad-counts
    print("outdeg [2]     (B0^2)      -> #cats =", count_categories([2]), " (enum: 4)")
    print("outdeg [1,1]   (B0+B0)     -> #cats =", count_categories([1,1])," (enum: 1)")
    print("outdeg [2,1]   (B0^2+B0)   -> #cats =", count_categories([2,1])," (enum: 6)")
    print("outdeg [3]     (B0^3)      -> #cats =", count_categories([3]), " (=#monoids on 3 elts)")
    print("outdeg [1]     (B0)        -> #cats =", count_categories([1]), " (=1)")
    print("outdeg [2,2]   (B0^2+B0^2) -> #cats =", count_categories([2,2]))
