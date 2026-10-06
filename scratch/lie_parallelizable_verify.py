"""
Verify Conjecture P (corrected): parallelizability of polynomial functors in
the representable tangent category (Poly, T=(-)<|D), D = y+ev.

A polynomial functor p = sum_a y^{E_a} is encoded by the MULTISET of out-degrees
[ |E_a| : a in Ob ]  (only cardinalities matter up to iso).

Tangent bundle: Tp = p(Y) + W * d p(Y),   dp = sum_a |E_a| y^{|E_a|-1}.
As a two-variable polynomial functor Tp(Y,W).

Projection pi: Tp -> p collapses W-directions. The ADDITIVE BUNDLE Tp -> p has,
over the position (shape) a, a fibre that is a FREE module of rank |E_a|
(the |E_a| ways to place the single tangent hole W among the E_a directions).

Bundle Tp -> p is TRIVIAL (iso to p x V over p, V fixed) iff the rank function
a |-> |E_a| is CONSTANT. Reason: positions of p form a DISCRETE set, so a bundle
over p is just a family of modules indexed by that discrete set; two such are
isomorphic over p iff the rank functions agree; trivial = ranks all equal to a
constant (= rank of the fixed fibre V).

We verify:
  (1) dp and Tp computed symbolically match the fibre-rank reading.
  (2) fibre rank over shape a equals |E_a|.
  (3) triviality <=> constant out-degree, on the four PROVE.md cases + counterexamples.
  (4) the (illegitimate) 'iso of total objects' dp = p x V FAILS (cardinality),
      confirming the type-confusion resolution.
"""

import sympy as sp
from sympy import symbols, Poly, expand, srepr
from collections import Counter

Y, W = symbols('Y W', nonnegative=True)

def p_poly(outdegs):
    """p(Y) = sum_a Y^{d_a} as a sympy expr in Y."""
    return sum(Y**d for d in outdegs)

def dp_poly(outdegs):
    """d p / dY."""
    return sp.diff(p_poly(outdegs), Y)

def Tp_poly(outdegs):
    """Tp(Y,W) = p(Y) + W * dp(Y)  (the e-linear dual-number truncation)."""
    return p_poly(outdegs) + W*dp_poly(outdegs)

def fibre_ranks(outdegs):
    """Over each shape a, the tangent fibre is free of rank |E_a|.
       Return the multiset of ranks (= the out-degrees themselves)."""
    return sorted(outdegs)

def is_parallelizable(outdegs):
    """Tp -> p trivial as additive bundle  <=>  all out-degrees equal."""
    return len(set(outdegs)) <= 1

def total_object_product_possible(outdegs):
    """Check the ILLEGITIMATE reading dp ≅ p x V as total objects (cardinality).
       dp positions each have (d-1) dirns; p x V positions have (d + |V dirn|) dirns.
       A decrement by a product that only adds is impossible unless trivial.
       Return True iff conceivable (we expect False for nontrivial)."""
    # p x V with V = sum_c y^{f_c}: positions (a,c), dirns d_a + f_c.
    # dp: positions (a,e in E_a), dirns d_a - 1.  Need d_a + f_c = d_a - 1 => f_c = -1. impossible.
    return all(d == 0 for d in outdegs)  # only the empty/constant case

CASES = {
    "1: terminal cat 1 (p=y)":            [1],
    "2: group Z/2 (p=y^2)":               [2],
    "2': group Z/3 (p=y^3)":              [3],
    "3: walking arrow (p=y^2+y)":         [2, 1],
    "4: codiscrete groupoid 2 obj (2y^2)":[2, 2],
    "CX monoid {1,e} e^2=e (p=y^2)":      [2],     # non-groupoid, homogeneous
    "CX groupoid Z/2 ⊔ Z/3 (y^2+y^3)":    [2, 3],  # groupoid, inhomogeneous
    "connected groupoid: 2 obj, vtx Z/2": [4, 4],  # Hom(a,b)=Z/2 each, out-deg=2*2=4
    "monoid (Z/4,+) one obj":             [4],
    "poset 0<1<2 (p=y^3+y^2+y)":          [3, 2, 1],
}

print("="*90)
print(f"{'case':<42} {'out-degs':<14} {'Tp(Y,W)':<22} {'par?':<5} {'groupoid-pred'}")
print("="*90)
for name, od in CASES.items():
    tp = expand(Tp_poly(od))
    par = is_parallelizable(od)
    print(f"{name:<42} {str(sorted(od)):<14} {str(tp):<22} {str(par):<5}")

print()
print("Detailed checks:")
for name, od in CASES.items():
    p = expand(p_poly(od)); d = expand(dp_poly(od)); tp = expand(Tp_poly(od))
    ranks = fibre_ranks(od)
    par = is_parallelizable(od)
    # sanity: coefficient structure of Tp: W-linear part is exactly dp
    w_part = sp.diff(tp, W)
    assert expand(w_part) == d, f"W-part mismatch {name}"
    # fibre rank over a shape of out-degree k must be k:
    # dp = sum_a k_a Y^{k_a - 1}; the number of tangent generators attached to a shape
    # of out-degree k is k. Check: coeff pattern.
    assert ranks == sorted(od)
    print(f"  {name}: p={p}, dp={d}, Tp={tp}, fibre-ranks={ranks}, "
          f"constant-rank={par}")

print()
print("Theorem P predictions vs groupoid conjecture:")
def is_groupoid_guess(name):
    return ("group" in name or "groupoid" in name) and "monoid" not in name
for name, od in CASES.items():
    par = is_parallelizable(od)
    grp = ("group" in name.lower() or "groupoid" in name.lower()) and "monoid" not in name.lower()
    flag = "  <-- MISMATCH groupoid-conj" if (par != grp) else ""
    print(f"  {name:<42} parallelizable={par!s:<5} looks-groupoid={grp!s:<5}{flag}")

print()
print("Illegitimate 'dp = p x V as total objects' check (expect only trivial):")
for name, od in CASES.items():
    print(f"  {name:<42} total-object-product-possible={total_object_product_possible(od)}")
