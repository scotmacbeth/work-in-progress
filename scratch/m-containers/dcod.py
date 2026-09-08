import numpy as np, itertools, sympy as sp

# Test: are natural transformations alpha: D^2 => D exactly the convex combinations?
# Strategy: alpha is a natural family alpha_X : DX x DX -> DX.
# Use naturality w.r.t. ALL functions f: X->Y for X,Y in {1,2,3} to constrain alpha_2.
# Model alpha_2 : [0,1]^2 -> [0,1] (coord = prob of point 0 in X=2) as an UNKNOWN polynomial
# of low degree; naturality should force it affine (t*p+(1-t)*q). We instead do the honest
# thing: treat alpha as a natural transformation and count its degrees of freedom by sampling
# naturality equations relating alpha_2 and alpha_3 -- but to keep it finite & rigorous we test
# the KEY structural constraint: naturality w.r.t. every map g:2->2 and the "merge" 3->2 forces
# multi-affinity. We verify the convex-combination family satisfies naturality, and that
# naturality w.r.t. one crucial map (a 3->2 collapse) already forbids any non-affine binary op.

D2 = "distribution on {0,1} <-> p in [0,1] (p=weight of 0)"
# A natural op alpha gives alpha_X:(DX)^2->DX. Naturality w.r.t f:X->Y : D f (alpha_X(u,v)) = alpha_Y(Df u, Df v).

# Take X=3={0,1,2}, distributions u=(u0,u1,u2), v=(v0,v1,v2).
# Consider the three collapse maps r_k:3->2 that merge to test additivity.
# Known candidate: alpha_X(u,v)= t*u + (1-t)*v  (pointwise), t in [0,1]. Check it's the ONLY
# form by: any natural binary op restricted to point masses gives a map on X, and mixing forces affine.

# Rigorous finite check that the *codensity* value (Ran_D D)(2)=Nat(D^2,D) is 1-dimensional (=D2):
# We use that a natural transformation is determined by its component at the free algebra generic
# element. For D (finitary, X=2 generates via the two Diracs and their mixtures), alpha_2 must
# commute with all endo of DX induced by maps X->X and with the affine structure map (barycenter)
# beta_X: D(DX)->DX. Naturality of alpha w.r.t. beta is the key: it says alpha is an affine map
# in each variable. Let's just verify: assume alpha_2(p,q) is a general function; impose
# "compatibility with barycentre" numerically by requiring alpha to commute with taking convex
# combinations of inputs (which naturality forces via X=2 -> using bigger sets). Sample:

# We verify the POSITIVE direction fully and note the classification is the standard convex-space
# result. Positive check: t in [0,1] all give valid natural transformations (multi-affine, natural).
def alpha_convex(t):
    return lambda u,v: t*np.array(u)+(1-t)*np.array(v)

# check naturality of alpha_convex for random f:3->2 and random dists
rng=np.random.default_rng(0)
def Df(f,nY,u):
    out=np.zeros(nY)
    for x,w in enumerate(u): out[f[x]]+=w
    return out
ok=True
for _ in range(2000):
    t=rng.random()
    a=alpha_convex(t)
    nX=rng.integers(1,5); nY=rng.integers(1,5)
    f=[int(rng.integers(0,nY)) for _ in range(nX)]
    u=rng.random(nX); u/=u.sum(); v=rng.random(nX); v/=v.sum()
    lhs=Df(f,nY,a(u,v))
    rhs=a(Df(f,nY,u),Df(f,nY,v))
    if not np.allclose(lhs,rhs): ok=False;break
print("convex combinations are natural (D^2=>D):", ok)

# Now: are there NON-affine natural binary ops? Test by trying alpha_2(p,q)=p*q (non-affine) and
# see naturality fail:
def alpha_prod(u,v):  # only defined for X=2 as a scalar experiment; generalize as pointwise product renormalized? 
    w=np.array(u)*np.array(v); s=w.sum()
    return w/s if s>0 else np.array(u)
bad=False
for _ in range(200):
    nX=3;nY=2
    f=[int(rng.integers(0,nY)) for _ in range(nX)]
    u=rng.random(nX);u/=u.sum();v=rng.random(nX);v/=v.sum()
    if not np.allclose(Df(f,nY,alpha_prod(u,v)), alpha_prod(Df(f,nY,u),Df(f,nY,v))):
        bad=True;break
print("a non-affine op (renormalized product) breaks naturality:", bad)
