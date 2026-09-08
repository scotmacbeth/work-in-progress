#!/usr/bin/env python3
"""
Verify: PLETHYSM RIGHT-CANCELLATION in the power-sum ring, truncated at degree N.

Ring R = Q[[p_1,p_2,...]], deg(p_k)=k.  Element = dict {partition(tuple, weakly decreasing): Fraction}.
partition () = the constant 1 (degree 0).

Plethysm F o H (F,H in R):
  - algebra homomorphism in F determined by  p_k o H = H[p_j -> p_{jk}]
  - so for a monomial p_mu = prod p_{mu_i},  p_mu o H = prod_i (p_{mu_i} o H)
  - p_k o H = replace every part j of every partition in H by j*k, keeping coeff.

Claim (theorem to test): if H has ZERO constant term and NONZERO p_1 coefficient,
then F -> F o H is injective (mod degree N): distinct F,G give distinct FoH.

We test injectivity by verifying that the images of the monomial basis {p_mu : |mu|<=N}
under (-)oH are linearly independent (as vectors of coefficients truncated at degree N).
"""
from fractions import Fraction
from itertools import product
import sys

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, mx), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest

def all_parts_upto(N):
    out = []
    for n in range(0, N+1):
        for mu in partitions(n):
            out.append(mu)
    return out

def padd(a, b):
    r = dict(a)
    for k,v in b.items():
        r[k] = r.get(k, Fraction(0)) + v
        if r[k] == 0: del r[k]
    return r

def pscale(a, c):
    return {k: v*c for k,v in a.items() if v*c != 0}

def merge_part(mu, nu):
    return tuple(sorted(mu+nu, reverse=True))

def pmul(a, b, N):
    r = {}
    for mu, cu in a.items():
        du = sum(mu)
        for nu, cv in b.items():
            if du + sum(nu) > N:
                continue
            key = merge_part(mu, nu)
            r[key] = r.get(key, Fraction(0)) + cu*cv
            if r[key] == 0: del r[key]
    return r

def scale_partition(mu, k):
    return tuple(sorted((j*k for j in mu), reverse=True))

def p_k_pleth_H(k, H, N):
    """ p_k o H : replace part j -> j*k in every partition of H; drop terms of degree>N """
    r = {}
    for mu, c in H.items():
        smu = scale_partition(mu, k)
        if sum(smu) > N: continue
        r[smu] = r.get(smu, Fraction(0)) + c
        if r[smu] == 0: del r[smu]
    return r

def pmonomial_pleth_H(mu, H, N):
    """ p_mu o H = prod_i (p_{mu_i} o H) """
    res = {(): Fraction(1)}  # the constant 1
    for part in mu:
        res = pmul(res, p_k_pleth_H(part, H, N), N)
    return res

def pleth(F, H, N):
    """ F o H truncated at degree N """
    r = {}
    for mu, c in F.items():
        term = pscale(pmonomial_pleth_H(mu, H, N), c)
        r = padd(r, term)
    return r

# ------- Test 1: injectivity of (-)oH via rank of image matrix -------
def test_injectivity(H, N, label):
    basis = all_parts_upto(N)          # domain basis {p_mu}
    idx = {mu:i for i,mu in enumerate(basis)}
    # image vectors
    rows = []
    for mu in basis:
        img = pmonomial_pleth_H(mu, H, N)
        vec = [Fraction(0)]*len(basis)
        for nu, c in img.items():
            vec[idx[nu]] = c
        rows.append(vec)
    # rank over Q of the len(basis) x len(basis) matrix (rows = images)
    import copy
    M = [row[:] for row in rows]
    n = len(M)
    rank = 0
    col = 0
    r = 0
    while r < n and col < n:
        piv = None
        for i in range(r, n):
            if M[i][col] != 0:
                piv = i; break
        if piv is None:
            col += 1; continue
        M[r], M[piv] = M[piv], M[r]
        inv = Fraction(1)/M[r][col]
        M[r] = [x*inv for x in M[r]]
        for i in range(n):
            if i!=r and M[i][col]!=0:
                f = M[i][col]
                M[i] = [a-f*b for a,b in zip(M[i], M[r])]
        r += 1; col += 1
    rank = r
    inj = (rank == n)
    print(f"[{label}] N={N}: |basis|={n}, rank(image)={rank}, injective={inj}")
    return inj

# H1 = Z_A for A = X + E_2 :  Z_X = p_1 ; Z_{E_2} = (p_1^2 + p_2)/2
# a_0 = 0, a_1 = 1  -> theorem predicts injective
H1 = padd({(1,): Fraction(1)}, {(1,1): Fraction(1,2), (2,): Fraction(1,2)})
# H2 = Z_A for A = X + E_3 : Z_{E_3} = (p_1^3 + 3 p_1 p_2 + 2 p_3)/6
H2 = padd({(1,): Fraction(1)},
          {(1,1,1): Fraction(1,6), (2,1): Fraction(3,6), (3,): Fraction(2,6)})
# H3 : a_0 = 0 but a_1 = 0 (H = p_2 + ...) -> theorem does NOT apply, expect NON-injective
H3 = {(2,): Fraction(1), (1,1): Fraction(1,2)}   # no p_1 term
# H4 : monad-like unbounded truncated: A = X + E_2 + E_3
H4 = padd(H1, {(1,1,1): Fraction(1,6), (2,1): Fraction(3,6), (3,): Fraction(2,6)})

print("=== Test 1: injectivity of plethysm (-)oH ===")
for N in (4,5,6):
    test_injectivity(H1, N, "A=X+E2 (a1=1)")
for N in (5,6):
    test_injectivity(H2, N, "A=X+E3 (a1=1)")
for N in (4,5):
    test_injectivity(H4, N, "A=X+E2+E3 (a1=1)")
print("--- control: H with a_1=0 should FAIL injectivity ---")
for N in (4,5):
    test_injectivity(H3, N, "H=p2+... (a1=0)")

# ------- Test 2: the actual consequence.  A = X + E_2 (non-flat).
# Compute Z_A o Z_A. Show it has genuine p_2-type (non-p_1) content, and that the ONLY
# solution Z_B (flat: only p_1-powers) to Z_B o Z_A = Z_A o Z_A would need Z_B = Z_A (not flat).
print("\n=== Test 2: A = X + E_2, compute Z_A o Z_A and test flat-B solvability ===")
N = 6
ZA = H1
ZAZA = pleth(ZA, ZA, N)
def show(P):
    items = sorted(P.items(), key=lambda kv:(sum(kv[0]), kv[0]))
    return " + ".join(f"{v}*p{mu}" for mu,v in items if v!=0)
print("Z_A       =", show(ZA))
print("Z_A o Z_A =", show(ZAZA))

# flat B: Z_B = sum_n b_n p_1^n / (something) ; general flat species B has Z_B = sum_n c_n p_1^n
# where c_n = |B[n]|/n!  (>=0 rationals with n! c_n integer). Solve Z_B o Z_A = Z_A o Z_A.
# Z_B o Z_A = sum_n c_n (p_1 o Z_A)^n = sum_n c_n (Z_A)^n   since p_1 o Z_A = Z_A.
# So we need sum_n c_n (Z_A)^n = Z_A o Z_A. Solve for c_n by matching lowest degrees.
# Build powers (Z_A)^n:
powZA = { 0: {():Fraction(1)} }
cur = {():Fraction(1)}
for n in range(1, N+1):
    cur = pmul(cur, ZA, N)
    powZA[n] = cur
# ZA has bottom degree 1, so (ZA)^n has bottom degree n. Match degree by degree.
target = dict(ZAZA)
c = {}
ok = True
for n in range(0, N+1):
    # coefficient of the unique lowest new content: the p_1^n coefficient of target vs powers
    key = tuple([1]*n) if n>0 else ()
    # contribution to p_1^n from c_m (ZA)^m for m<=n: only m<=n; (ZA)^m has p_1^n coeff
    lhs = sum(c.get(m,Fraction(0))*powZA[m].get(key,Fraction(0)) for m in range(0,n))
    tcoef = target.get(key, Fraction(0))
    denom = powZA[n].get(key, Fraction(0))
    if denom == 0:
        # can't solve using p_1^n pivot; skip (shouldn't happen since (ZA)^n has p_1^n coeff = a_1^n =1)
        c[n] = Fraction(0)
    else:
        c[n] = (tcoef - lhs)/denom
# Now form Z_B o Z_A with these c_n and compare to target
ZB = {}
for n,cn in c.items():
    if n==0:
        ZB = padd(ZB, pscale({():Fraction(1)}, cn))
    else:
        ZB = padd(ZB, pscale({tuple([1]*n):Fraction(1)}, cn))
ZBZA = pleth(ZB, ZA, N)
match = (padd(ZBZA, pscale(target,Fraction(-1))) == {})
print("Solved flat Z_B (coeffs c_n):", {n:c[n] for n in sorted(c) if c[n]!=0})
print("Z_B (candidate flat) =", show(ZB))
print("Does flat Z_B reproduce Z_A o Z_A up to deg",N,"?", match)
print("Is candidate Z_B flat (only p_1 powers)?",
      all(set(mu)<= {1} for mu in ZB))
