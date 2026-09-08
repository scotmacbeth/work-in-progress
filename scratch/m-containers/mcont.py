from itertools import product
from math import prod

# A polynomial monad M given as container (I, B) with M(X)=sum_{i in I} X^{B_i}.
# Represent I as list of ints = |B_i| (arity of shape i).
# Examples:
Maybe   = [1,0]          # X^1 + X^0 = X+1
Excep2  = [1,0,0]        # X + 2  (exception with E=2)
Writer2 = [1,1]          # X + X = 2*X
Reader2 = [2]            # X^2   (reader over R=2)
Id      = [1]            # X
Const1  = [0]            # 1  (not a monad-extension of interest but test)

def MA(arities, a):
    # |M(A)| for |A|=a
    return sum(a**k for k in arities)

def Phi(arities, a):
    # Nat((M-)^A, M) = prod_{phi:A->I} sum_{i in I} (sum_{x in A} B_{phi(x)})^{B_i}
    I = len(arities)
    total = 1
    for phi in product(range(I), repeat=a):      # phi: A->I, A={0..a-1}
        posA = sum(arities[phi[x]] for x in range(a))   # |positions of shape phi| = sum_a B_{phi a}
        s = sum(posA**arities[i] for i in range(I))      # sum_i |Set(B_i, posA)|
        total *= s
    return total

names = {"Id":Id,"Maybe":Maybe,"Excep2":Excep2,"Writer2":Writer2,"Reader2":Reader2}
print("Comparing MA vs Phi(A)=Nat((M-)^A,M).  Full-on-homs needs MA==Phi(A) for all A.")
for nm,ar in names.items():
    row=[]
    for a in range(0,4):
        row.append((a, MA(ar,a), Phi(ar,a), MA(ar,a)==Phi(ar,a)))
    print(f"{nm:8s}", row)
