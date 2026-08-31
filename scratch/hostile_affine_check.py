# Hostile referee check of §5.2 logic: "B+D_B×X affine in X  ⟹  D_X affine".
# The logical core: if F(X)=B+D_B*X is a coproduct  Id_summand ⊔ (D_B×X)_summand,
# and the TOTAL is affine (all arities <=1), then the (D_B×X) summand is affine.
# Test: take a NON-affine bifunctor and confirm it does NOT satisfy the unit ∅⋆B=B
#       and/or the symmetry identity — i.e. the hypotheses genuinely bite.
from itertools import product

# Candidate NON-affine "would-be tensor": X⋆B := B + X + X^2 * B  (a degree-2 extra, s'=1 on X^2)
# cardinality:
def bad(x,b): return b + x + x*x*b
# Is it associative? (necessary for monoidal) -- expect FAIL, matching Key Lemma.
assoc_ok = all(bad(bad(x,b),c)==bad(x,bad(b,c)) for x,b,c in product(range(5),repeat=3))
print("degree-2-in-X candidate  b+x+x^2 b :  associative? ", assoc_ok, " (expected False)")

# The affine family x+b+s x b IS associative (control):
def vee(s): return lambda x,b: x+b+s*x*b
for s in range(4):
    op=vee(s)
    ok=all(op(op(x,b),c)==op(x,op(b,c)) for x,b,c in product(range(6),repeat=3))
    print(f"  affine x+b+{s}xb associative? {ok} (expected True)")

# Also confirm: any x^2 coefficient breaks associativity's degree bookkeeping.
# |（X⋆B)⋆C| degree in |X|:  for bad, LHS = bad(bad(x,b),c). Leading term in x:
# bad(x,b) ~ x^2 b, then bad(_,c) ~ (x^2 b)^2 c = x^4 ... vs RHS bad(x, bad(b,c)) ~ x^2 (...).
# So degree 4 vs 2 in x -> can't be natural. Confirm numerically the growth:
import sympy as sp
x,b,c=sp.symbols('x b c')
L=sp.expand(bad(bad(x,b),c)); R=sp.expand(bad(x,bad(b,c)))
print("deg_x LHS(assoc) =", sp.degree(L,x), " deg_x RHS =", sp.degree(R,x), " (mismatch => no monoidal structure)")
