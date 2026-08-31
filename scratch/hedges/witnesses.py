from itertools import product as iproduct
def tensor(p,q): return tuple(a*b for a in p for b in q)
def prod(p,q):   return tuple(a+b for a in p for b in q)
def coprod(p,q): return tuple(p)+tuple(q)
def comp(p,q):
    Sq=len(q); out=[]
    for a in p:
        for f in iproduct(range(Sq),repeat=a):
            out.append(sum(q[f[i]] for i in range(a)))
    return tuple(out)
def it(c): return tuple(sorted(c))
def show(c): 
    from collections import Counter
    return "+".join(f"{n}·y^{k}" for k,n in sorted(Counter(c).items()))
y=(1,); y2=(2,); one=(0,); # 1 = y^∅
twoY=(1,1)  # 2y

print("=== ;/+ : ◁ over + — LEFT is iso, RIGHT fails (Niu-Spivak Ex 6.56 shape) ===")
a,b,c = (1,0),(1,),(1,)   # a=y+1, etc
print(" LEFT  (a+b)◁c vs (a◁c)+(b◁c):", it(comp(coprod(a,b),c)), "vs", it(coprod(comp(a,c),comp(b,c))), "->", it(comp(coprod(a,b),c))==it(coprod(comp(a,c),comp(b,c))))
# right-failure explicit (Ex 6.56): (y+1)◁(1+0)
p=(1,0); q1=(0,); q0=()  # 1=y^∅ has shape w/0 pos ; 0 = empty container
# use q = 1 + 0 : that's coprod((0,),()) = (0,)  (0 has no shapes)
qA=(0,); qB=()  
lhs=comp(p, coprod(qA,qB)); rhs=coprod(comp(p,qA),comp(p,qB))
print(" RIGHT (y+1)◁(1+0):  p◁(qA+qB)=",show(lhs)," vs (p◁qA)+(p◁qB)=",show(rhs)," iso?",it(lhs)==it(rhs))

print("\n=== ;/× : ◁ over × — LEFT iso, RIGHT fails (2y² vs 4y²) ===")
a,b,c=twoY,twoY,y
print(" LEFT  (a×b)◁c:", show(comp(prod(a,b),c)), " vs (a◁c)×(b◁c):", show(prod(comp(a,c),comp(b,c))), "iso?", it(comp(prod(a,b),c))==it(prod(comp(a,c),comp(b,c))))
p,q1,q2=twoY,y,y
print(" RIGHT p◁(q×q'):", show(comp(p,prod(q1,q2))), " vs (p◁q)×(p◁q'):", show(prod(comp(p,q1),comp(p,q2))), "iso?", it(comp(p,prod(q1,q2)))==it(prod(comp(p,q1),comp(p,q2))))

print("\n=== ⊗/+ and ×/+ : two-sided D (both variables iso) — spot check ===")
a,b,c=twoY,(2,1),(1,2)
for nm,R in [("⊗",tensor),("×",prod)]:
    L= it(R(coprod(a,b),c))==it(coprod(R(a,c),R(b,c)))
    Rr=it(R(a,coprod(b,c)))==it(coprod(R(a,b),R(a,c)))
    print(f" {nm}/+  left={L}  right={Rr}")

print("\n=== ×/⊗ non-existence witness (1,y,y,1): interchanger would be a morphism 1 -> y ===")
a,b,c,d=one,y,y,one
src=prod(tensor(a,b),tensor(c,d)); tgt=tensor(prod(a,c),prod(b,d))
print(" src (a⊗b)×(c⊗d) =",show(src)," (has empty shape:", any(x==0 for x in src),")")
print(" tgt (a×c)⊗(b×d) =",show(tgt)," (has empty shape:", any(x==0 for x in tgt),")")
print(" => no container morphism src->tgt  (empty-shape source, non-empty-shape target).")

print("\n=== ⊗/× formal interchanger EXISTS (pair-into-product) but is LAX not iso ===")
a,b,c,d=twoY,y,y,twoY
src=tensor(prod(a,b),prod(c,d)); tgt=prod(tensor(a,c),tensor(b,d))
print(" src (a×b)⊗(c×d)=",show(src)," tgt (a⊗c)×(b⊗d)=",show(tgt)," iso?",it(src)==it(tgt), " morphism exists?", (not any(x==0 for x in src)) or any(x==0 for x in tgt))

print("\n=== reconstructed table vs Hedges (compare each cell's verdict driver) ===")
