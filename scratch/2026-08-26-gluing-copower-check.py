# Gl(T) for T = (-)^2 : Set -> Set  (comma category Id_Set / T)
# Objects: (A, B, beta: A -> B^2).  We test finite objects.
# Point functor C(I,-) with I = (1,1, *->(*,*)):
#   Hom(I,(A,B,beta)) = { a in A : beta(a) in Diagonal(B) }
# Coproduct: (A,B,beta) + (A',B',beta') = (A+A', B+B', delta)
#   delta(a) = (inj_B(b1), inj_B(b2)) where beta(a)=(b1,b2); similarly a'.
# We verify: (A) copowers of I: C(I, kappa*I) has exactly kappa points.
#            (C) test: for random objects X,Y, C(I,X+Y) == C(I,X) + C(I,Y)  (localizes)

import itertools, random
random.seed(1)

def points(A, B, beta):
    # beta: dict a-> (b1,b2). points = a with b1==b2
    return [a for a in A if beta[a][0]==beta[a][1]]

def copower_I(kappa):
    # kappa copies of I=(1,1). B-part=range(kappa), A-part=range(kappa), beta(j)=(j,j)
    A=list(range(kappa)); B=list(range(kappa))
    beta={j:(j,j) for j in range(kappa)}
    return A,B,beta

def coproduct(o1,o2):
    A1,B1,b1=o1; A2,B2,b2=o2
    A=[('L',a) for a in A1]+[('R',a) for a in A2]
    B=[('L',b) for b in B1]+[('R',b) for b in B2]
    beta={}
    for a in A1: x,y=b1[a]; beta[('L',a)]=(('L',x),('L',y))
    for a in A2: x,y=b2[a]; beta[('R',a)]=(('R',x),('R',y))
    return A,B,beta

# (A): copowers of I
print("=== (A) copowers of unit ===")
for k in range(1,6):
    A,B,beta=copower_I(k)
    p=points(A,B,beta)
    print(f"kappa={k}: |C(I,kappa*I)|={len(p)}  expected kappa*|M|={k}*1={k}  OK={len(p)==k}")

# random finite object generator
def rand_obj(nA,nB):
    A=list(range(nA)); B=list(range(nB))
    beta={a:(random.randrange(nB),random.randrange(nB)) for a in A}
    return A,B,beta

# (C) test: does C(I,-) preserve binary coproducts?
print("=== (C) preservation of binary coproducts (100 random pairs) ===")
bad=0
for _ in range(100):
    X=rand_obj(random.randint(1,4),random.randint(1,4))
    Y=rand_obj(random.randint(1,4),random.randint(1,4))
    lhs=len(points(*coproduct(X,Y)))
    rhs=len(points(*X))+len(points(*Y))
    if lhs!=rhs: bad+=1
print("mismatches (C fails if >0):", bad)
