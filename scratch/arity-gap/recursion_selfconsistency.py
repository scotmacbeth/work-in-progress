"""
Test: is the associativity arity-recursion self-consistent for an infinite seed arity?

Setup (case I=1): index set of R_B is 1*B = B; R_B(X) = sum_{b in B} X^{A_{B,b}},
all A_{B,b} nonempty; A_{1,*}=1. Associativity R_2 o R_2 ~= R_{2*2} forces the arity
recursion  A_{C*B,(b,phi)} = sum_{i in A_{B,b}} A_{C,phi(i)},  phi: A_{B,b} -> C=1*C.

We seed R_2 = y^{a0} + y^{a1} (index set 2={0,1}), and PROPAGATE to R_2^2, then read off
the multiset of arities of R_2^2. Compare growth for finite seed (a1=n>=2) vs infinite (a1=lambda).

We model cardinals as: finite ints, or the token 'INF' for a fixed infinite cardinal lambda,
with arithmetic  n + INF = INF, INF + INF = INF, k*INF = INF (k>=1), INF*INF = INF,
2^INF = INF (all collapse to the single infinite cardinal token; we only track finite-vs-infinite
and, for finite, the exact value, which is what the Key-Lemma growth argument needs).
"""

from collections import Counter
from itertools import product


def add(x, y):
    if x == 'INF' or y == 'INF':
        return 'INF'
    return x + y


def is_inf(x):
    return x == 'INF'


def two_pow(x):
    # |2^a| : 2^n finite for finite n; 2^INF = INF
    if x == 'INF':
        return 'INF'
    return 2 ** x


def propagate_R2_squared(a0, a1):
    """
    R_2 has index set {0,1} with arities (a0,a1).  1*2 = 2 (I=1), so phi maps into C=2,
    i.e. phi: A_{2,b} -> {0,1}.  Composite R_2 o R_2 = R_{2*2}. Enumerate its indices (b,phi)
    and their arities Sum_{i in A_{2,b}} A_{2,phi(i)}.  Return multiset (Counter) of arities.
    For finite arities we enumerate phi exactly; for INF arity we reason: phi: lambda->{0,1};
    the arity Sum_{i} A_{2,phi(i)} — each summand is a0 or a1(>=1), summed over lambda terms,
    hence = INF (lambda copies of >=1).  Number of such phi = 2^lambda = INF.
    """
    arities = Counter()
    arity_list_of = {0: a0, 1: a1}
    for b in (0, 1):
        Ab = arity_list_of[b]
        if Ab == 'INF':
            # every phi gives arity INF; there are 2^lambda = INF of them
            arities['INF (x INF-many phi)'] += 1  # symbolic bucket
        else:
            # phi ranges over functions Ab -> {0,1}, i.e. 2^Ab of them
            for phi in product((0, 1), repeat=Ab):
                s = 0
                for i in range(Ab):
                    s = add(s, arity_list_of[phi[i]])
                arities[s] += 1
    return arities


def index_count_2star2(a0, a1):
    # |2*2| = |R_2(2)| = 2^a0 + 2^a1
    return add(two_pow(a0), two_pow(a1))


print("=== R_2 = y^{a0} + y^{a1};  propagate to R_2 o R_2 = R_{2*2} ===\n")

for (a0, a1) in [(1, 1), (1, 2), (1, 3), (2, 2), (1, 'INF'), ('INF', 'INF')]:
    print(f"seed R_2: arities (a0,a1) = ({a0},{a1})")
    N = index_count_2star2(a0, a1)
    print(f"  |2*2| = index count of R_{{2*2}} = 2^{a0}+2^{a1} = {N}")
    ar = propagate_R2_squared(a0, a1)
    print(f"  arities appearing in R_2 o R_2 (value : #indices): {dict(ar)}")
    # max finite arity, to show growth
    finite_ar = [k for k in ar if isinstance(k, int)]
    maxa = max(finite_ar) if finite_ar else None
    seed_max = max([v for v in (a0, a1) if isinstance(v, int)] or [0])
    has_inf = any((k == 'INF' or 'INF' in str(k)) for k in ar)
    print(f"  max finite arity in composite: {maxa}  (seed max finite arity: {seed_max})"
          f"  infinite arity present: {has_inf}")
    if maxa is not None and maxa > seed_max:
        print(f"  >>> GROWTH: composite arity {maxa} > seed {seed_max}  "
              f"==> if global kappa finite, CONTRADICTION (Key Lemma).")
    if has_inf:
        print("  >>> STABLE: infinite arity reproduces infinite arity, NO cardinality "
              "contradiction (kappa^2 = kappa).")
    print()

print("Conclusion: finite seed arity >=2 forces strictly growing arities (unbounded, "
      "consistent with\nKey Lemma killing finite kappa); infinite seed arity is a fixed point "
      "of the recursion.\nEither way the recursion is cardinally SELF-CONSISTENT -- no counting "
      "obstruction to an\ninfinite-arity structure.")
