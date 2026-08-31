"""
State monad container form and the general-M reduction, |S|=2.
State X = (S x X)^S.  As container:  M(X)= coprod_{t in S^S}  X^S   (shape t=next-state fn, positions S).
mu(mm)(s) = inner_s(T(s)) with mm(s)=(T(s), inner_s).  Check: is there a monad morphism State=>Id?
Confirm ev_{s0} is NOT one (state threading), so the auxiliary-monoid-Pi transfer needs care;
Sigma (=M<|-) DOES lift since State is a container (triangle-)monoid.
Verify the SHAPE-threading formula sigma_mu(s)= t_s(T(s)) that couples the aggregator family (A_t)_t.
"""
import itertools
S=[0,1]
SS=list(itertools.product(S,repeat=len(S)))  # functions S->S as tuples (f(0),f(1))
def comp(f,g):  # f after g : s-> f(g(s))
    return tuple(f[g[s]] for s in S)
idf=tuple(S)  # (0,1)

# check monad-morphism candidate ev_{s0}: m=(t,x) |-> x(s0)  fails
def state_mu_shape(T, ts):
    # T in SS (outer next-state), ts: dict s-> inner next-state (in SS). returns threaded next-state
    return tuple(ts[s][T[s]] for s in S)

# demonstrate threading couples shapes: mu-shape depends on BOTH outer T and inner t_s at T(s)
import random
random.seed(1)
examples=[]
for _ in range(6):
    T=random.choice(SS); ts={s:random.choice(SS) for s in S}
    examples.append((T,{k:v for k,v in ts.items()}, state_mu_shape(T,ts)))
for T,ts,sig in examples:
    print(f"T={T} t0={ts[0]} t1={ts[1]}  ->  mu-shape sigma={sig}")

# Sanity: eta shape is id (t=id). Only A_{id} is touched by the unit.
print("\neta shape = id =", idf, " => unit only constrains A_id ; A_t for t!=id unconstrained by unit")
print("S^S shapes:", SS)
