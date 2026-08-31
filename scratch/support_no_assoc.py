# Prove: NO natural associator exists for A*B = A⊔B⊔[both≠∅] on objects {∅,1}.
# Search ALL families of bijections α_{A,B,C}:(A*B)*C -> A*(B*C) and check naturality
# w.r.t. every morphism (only maps among {∅,1}: id_∅, the fill !:∅→1, id_1).
import itertools
def star(A,B):
    e=[('l',a) for a in A]+[('r',b) for b in B]
    if A and B: e.append('m')
    return tuple(e)
def smap(f,g,A,B):
    d={}
    for x in star(A,B):
        if x=='m': d[x]='m'
        elif x[0]=='l': d[x]=('l',f[x[1]])
        else: d[x]=('r',g[x[1]])
    return d
O={'0':(), '1':(0,)}
# morphisms between named objects: (name_src,name_tgt)->dict
def homs(a,b):
    A=O[a];B=O[b]; res=[]
    if not A: res.append({})
    else:
        for v in itertools.product(B,repeat=len(A)): res.append({A[i]:v[i] for i in range(len(A))})
    return res

names=['0','1']
def LHS(a,b,c): return star(star(O[a],O[b]),O[c])
def RHS(a,b,c): return star(O[a],star(O[b],O[c]))

# forced part of any associator: non-'m' elements are canonical (a,b,c leaves).
def forced_and_amb(a,b,c):
    A,B,C=O[a],O[b],O[c]; L=LHS(a,b,c); R=RHS(a,b,c)
    d={}; amb_src=[]
    for x in L:
        if x=='m': amb_src.append(x)
        elif x[0]=='l':
            p=x[1]
            if p=='m': amb_src.append(x)
            elif p[0]=='l': d[x]=('l',p[1])
            else: d[x]=('r',('l',p[1]))
        else: d[x]=('r',('r',x[1]))
    used=set(d.values()); amb_tgt=[r for r in R if r not in used]
    return d,amb_src,amb_tgt,L,R

# enumerate all associators (choice of bijection on ambiguous pts per triple)
triples=list(itertools.product(names,repeat=3))
choices=[]
for t in triples:
    d,asrc,atgt,L,R=forced_and_amb(*t)
    perms=list(itertools.permutations(atgt))
    opts=[]
    for perm in perms:
        dd=dict(d); dd.update({asrc[i]:perm[i] for i in range(len(asrc))})
        # must be bijection
        if set(dd.values())==set(R) and len(set(dd.values()))==len(R): opts.append(dd)
    choices.append(opts)

# naturality: for f:a->a',g:b->b',h:c->c', α_{a'b'c'}∘((f*g)*h) = (f*(g*h))∘α_{abc}
def natural(assoc):
    A=dict(zip(triples,assoc))
    for t in triples:
        a,b,c=t
        for ap in names:
         for bp in names:
          for cp in names:
           for f in homs(a,ap):
            for g in homs(b,bp):
             for h in homs(c,cp):
               al=A[t]; ar=A[(ap,bp,cp)]
               fg=smap(f,g,O[a],O[b]); left={x:ar[smap(fg,h,star(O[a],O[b]),O[c])[x]] for x in LHS(a,b,c)}
               gh=smap(g,h,O[b],O[c]); right={x:smap(f,gh,O[a],star(O[b],O[c]))[al[x]] for x in LHS(a,b,c)}
               if left!=right: return False
    return True

count=0; found=None
for combo in itertools.product(*choices):
    count+=1
    if natural(combo): found=combo; break
print("total associator families searched:", count)
print("a NATURAL associator exists on {∅,1}?", found is not None)
if found is None:
    print(">>> NO natural associator => support tensor is NOT a monoidal structure.")
