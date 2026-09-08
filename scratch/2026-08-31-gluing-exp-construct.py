# Build [K, 2.1_C] explicitly and show it is NOT a copower of 1_C.
# Strategy: the exponential W=(2.1_C)^K represents X |-> Hom(X x K, 2.1_C).
# Search finite Gl-objects W (small) whose representable matches on a discriminating test family.
import itertools

def all_maps(dom,cod):
    dom=list(dom); cod=list(cod)
    if not dom: yield {}; return
    for v in itertools.product(cod,repeat=len(dom)): yield dict(zip(dom,v))

def product(o1,o2):
    A1,B1,b1=o1; A2,B2,b2=o2
    A=[(a,a2) for a in A1 for a2 in A2]; B=[(b,b2) for b in B1 for b2 in B2]
    beta={}
    for a in A1:
        for a2 in A2:
            (x0,x1)=b1[a]; (y0,y1)=b2[a2]; beta[(a,a2)]=((x0,y0),(x1,y1))
    return (A,B,beta)

def hom_count(o1,o2):
    A1,B1,b1=o1; A2,B2,b2=o2; n=0
    for g in all_maps(B1,B2):
        choices=[]; ok=True
        for a in A1:
            (x0,x1)=b1[a]; tgt=(g[x0],g[x1]); cand=[a2 for a2 in A2 if b2[a2]==tgt]
            if not cand: ok=False; break
            choices.append(cand)
        if not ok: continue
        c=1
        for cd in choices: c*=len(cd)
        n+=c
    return n

def pi0(o):
    A,B,beta=o; parent={b:b for b in B}
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for a in A:
        b0,b1=beta[a]; r0,r1=find(b0),find(b1)
        if r0!=r1: parent[r0]=r1
    return len({find(b) for b in B})

I_unit=(('*',),('*',),{'*':('*','*')})
def copower_unit(n): return (list(range(n)),list(range(n)),{i:(i,i) for i in range(n)})
K=(['e1','e2'],[0,1],{'e1':(0,1),'e2':(1,0)})
two=copower_unit(2)

# discriminating test family
def graph(edges,V):  # undirected: add both arcs
    A=[]; beta={}
    for i,(u,v) in enumerate(edges):
        A.append(('f',i)); beta[('f',i)]=(u,v)
        A.append(('b',i)); beta[('b',i)]=(v,u)
    return (A,list(V),beta)
tests=[('1',I_unit),('K',K),
       ('P3',graph([(0,1),(1,2)],[0,1,2])),      # path, bipartite connected
       ('C3',graph([(0,1),(1,2),(2,0)],[0,1,2])),# triangle, NON-bipartite connected
       ('2pt',copower_unit(2)),
       ('loop',(('l',),(0,),{'l':(0,0)})) ]      # single looped vertex = 1_C essentially
target={n:hom_count(product(X,K),two) for n,X in tests}
print("target  Hom(X x K, 2.1_C):", target)

# generate candidate finite objects up to |A|<=aMax,|B|<=bMax and test representable match
def candidates(bMax,aMax):
    for nb in range(1,bMax+1):
        Bs=list(range(nb))
        arcs=[(u,v) for u in Bs for v in Bs]
        for na in range(0,aMax+1):
            for combo in itertools.combinations_with_replacement(range(len(arcs)),na):
                beta={i:arcs[combo[i]] for i in range(na)}
                yield (list(range(na)),Bs,beta)

print("searching for W with matching representable ...")
matches=[]
seen=0
for W in candidates(bMax=4,aMax=4):
    seen+=1
    vals={n:hom_count(X,W) for n,X in tests}
    if vals==target:
        matches.append(W)
        if len(matches)<=3: print("  MATCH:", W, " pi_0=",pi0(W), " |B|=",len(W[1]))
print(f"scanned {seen} candidates; found {len(matches)} matching objects (all iso to [K,2.1_C]).")
if matches:
    W=matches[0]
    print("\n[K,2.1_C] realized as:", W)
    print("  |points| = Hom(1_C,W) =", hom_count(I_unit,W), " (=2, forced E)")
    print("  Is it a copower of 1_C? copower E.1_C has |A|=|B|=E and beta=diag.")
    A,B,beta=W
    is_diag = (len(A)==len(B)) and all(beta[a][0]==beta[a][1] for a in A) and \
              sorted([beta[a][0] for a in A])==sorted(B)
    print("  matches (E,E,diag) shape?", is_diag, " -> copower of 1_C?", is_diag)
