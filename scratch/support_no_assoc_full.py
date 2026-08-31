# FULLY GENERAL: allow ANY bijection (A*B)*C -> A*(B*C) (no canonical-leaf assumption),
# search for a family natural w.r.t. all morphisms among {∅,1}. If none, support tensor
# is definitively NOT a monoidal structure.
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
names=['0','1']
def homs(a,b):
    A=O[a];B=O[b]
    if not A: return [{}]
    return [{A[i]:v[i] for i in range(len(A))} for v in itertools.product(B,repeat=len(A))]
def L(a,b,c): return star(star(O[a],O[b]),O[c])
def R(a,b,c): return star(O[a],star(O[b],O[c]))

triples=list(itertools.product(names,repeat=3))
# all bijections L->R per triple
allbij={}
for t in triples:
    Lt=L(*t); Rt=R(*t)
    assert len(Lt)==len(Rt)
    allbij[t]=[dict(zip(Lt,perm)) for perm in itertools.permutations(Rt)]
print("bijection counts per triple:", {t:len(allbij[t]) for t in triples})

def nat_ok_pair(A_map, t, tp, morphs):
    # check naturality square for a single (t -> tp) given chosen assoc dicts A_map[t],A_map[tp]
    a,b,c=t; ap,bp,cp=tp
    al=A_map[t]; ar=A_map[tp]
    for f in morphs[0]:
     for g in morphs[1]:
      for h in morphs[2]:
        fg=smap(f,g,O[a],O[b]); left={x:ar[smap(fg,h,star(O[a],O[b]),O[c])[x]] for x in L(*t)}
        gh=smap(g,h,O[b],O[c]); right={x:smap(f,gh,O[a],star(O[b],O[c]))[al[x]] for x in L(*t)}
        if left!=right: return False
    return True

# Backtracking search over choice of bijection per triple, pruning with naturality
# among already-assigned triples.
def morphs_between(t,tp):
    a,b,c=t; ap,bp,cp=tp
    return (homs(a,ap),homs(b,bp),homs(c,cp))

order=triples
def search():
    assign={}
    def rec(i):
        if i==len(order): return dict(assign)
        t=order[i]
        for cand in allbij[t]:
            assign[t]=cand
            ok=True
            for tp in order[:i+1]:
                # naturality for every morphism t->tp and tp->t among assigned
                for (s,d) in [(t,tp),(tp,t)]:
                    if d in assign:
                        if not nat_ok_pair(assign,s,d,morphs_between(s,d)): ok=False;break
                if not ok: break
            if ok:
                r=rec(i+1)
                if r is not None: return r
            del assign[t]
        return None
    return rec(0)

res=search()
print("A fully-general natural associator exists on {∅,1}?", res is not None)
if res is None:
    print(">>> RIGOROUS: support tensor admits NO natural associator => NOT monoidal.")
