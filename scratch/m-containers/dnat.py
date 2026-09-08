import numpy as np
rng=np.random.default_rng(1)
def Df(f,nY,u):
    out=np.zeros(nY)
    for x,w in enumerate(u): out[f[x]]+=w
    return out

# TEST the base lemma: natural transformations D => D_{<=1} (sub-prob valued) that are the
# "Z-marginal" pieces must be scalar multiples sigma -> lambda*sigma.
# Concretely: verify sigma -> lambda*sigma is natural for any lambda, and that NO natural
# transformation D=>D can be non-constant-scalar by testing a candidate "square" map fails.

# 1) scalar multiples are natural (as sub-distributions): trivially yes (Df linear). Confirm:
ok=True
for _ in range(500):
    lam=rng.random(); nX=rng.integers(1,5);nY=rng.integers(1,5)
    f=[int(rng.integers(0,nY)) for _ in range(nX)]
    u=rng.random(nX);u/=u.sum()
    if not np.allclose(Df(f,nY,lam*u), lam*Df(f,nY,u)): ok=False;break
print("scalar multiples sigma->lambda*sigma are natural:",ok)

# 2) A tempting non-scalar natural op? "entropy-reweighting" sigma_i -> sigma_i^2/Z : NOT natural
def sq(u):
    w=u**2; return w/w.sum()
bad=False
for _ in range(500):
    nX=3;nY=2; f=[int(rng.integers(0,nY)) for _ in range(nX)]
    u=rng.random(nX);u/=u.sum()
    if not np.allclose(Df(f,nY,sq(u)), sq(Df(f,nY,u))): bad=True;break
print("nonlinear reweighting sigma->sigma^2/Z breaks naturality (as expected):",bad)

# 3) Connectedness mechanism: AFFINE monad (M1=1) => (M-)^A connected.
#    Demonstrate the forcing: any nat transf (M-)^A => G1 + G2 factors through one summand
#    because (M1)^A = 1 picks a summand and every X->1 drags all of (MX)^A into it.
#    (structural, checked in reasoning; numeric sanity for D at A=1 target D+D:)
#    a nat transf D => D⊔D : value at the point of D1=1 lands in summand L or R; naturality
#    via X->1 forces global L or R. We just assert the structural proof; sanity: D1 has 1 elt.
print("D1 cardinality =", 1, " (affine => single global point forces connectedness)")
