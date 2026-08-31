"""
Decisive test: does a COMMUTATIVE BRANCHING monad of FIXED arity 2 (Reader^2 = X^2)
fail the reverse-kappa axiom E2' ?  And does it give a full-morphism non-associative
biKleisli triple?   Compare with Pf (union, merging).

We need a LAX comparison  rho : prod_b M(Z_b) -> M(prod_b Z_b)  for Reader.
Reader is commutative; its monoidal 'zip' is:
   M Z0 x M Z1 -> M(Z0 x Z1),  ((a0,a1),(b0,b1)) |-> ((a0,b0),(a1,b1)).
Generalize to n leaves: given (w_b)_b with w_b = (w_b[0], w_b[1]) in Z_b^2,
   rho((w_b)_b) = ( (w_b[0])_b , (w_b[1])_b )  in (prod_b Z_b)^2.
i.e. rho[i] = tuple over b of w_b[i].  (transpose)
"""
from entwine import (Cont, Mor, ident, compose, eq,
                     Maybe, Pf, Reader, Writer,
                     G_obj, T_obj, G_mor, T_mor,
                     eps_G, delta_G, eta_T, mu_T,
                     lambda_rev, check_axioms_rev)
from itertools import product as iproduct

def lax_reader(M, P, labs, t):
    # t = (w_b)_b, each w_b in Reader-elt over P(lab_b) = a tuple of length |K|.
    # rho[i] = tuple_b (w_b[i]);   result is a Reader-elt over prod_b P(lab_b),
    # i.e. a tuple of length |K|, each entry a tuple over b.
    K = len(t[0]) if t else 0    # arity of Reader (env size)
    if len(labs) == 0:
        # empty product: element of prod = (); Reader-elt = tuple of () of length K
        return tuple(() for _ in range(K))
    return tuple(tuple(t[b][i] for b in range(len(labs))) for i in range(K))

# Reader^2 monad
R2 = Reader((0,1))
print("Reader^2 leaves of a sample:", R2.leaves(R2.eta('z')), "eta:", R2.eta('z'))
print("Reader^2 mu of ((p,q),(r,s)):", R2.mu((('p','q'),('r','s'))))

A1 = Cont(['a','b'], {'a':[0,1], 'b':[0]})
A2 = Cont(['a'],     {'a':[0,1,2]})
A3 = Cont(['a','b'], {'a':[0,1], 'b':[0,1]})

print("\n=== Reverse kappa axioms E1'-E4' for Reader^2 ===")
for name, C in [('A1',A1),('A2',A2),('A3',A3)]:
    try:
        ax = check_axioms_rev(R2, lax_reader, C)
        print(f"  {name}: " + "  ".join(f"{k.split()[0]}={('P' if v else 'FAIL')}" for k,v in ax.items()))
    except Exception as e:
        print(f"  {name}: ERROR {type(e).__name__}: {e}")

# Locate the E2' failure element for Reader^2 on A1 if any
print("\n=== locate Reader^2 E2' discrepancy on A1 ===")
M = R2
lam = lambda_rev(M, lax_reader, A1); GA = G_obj(M, A1)
lhs = compose(lam, G_mor(M, mu_T(M, A1)))
lamTA = lambda_rev(M, lax_reader, T_obj(M, A1))
rhs = compose(mu_T(M, GA), compose(T_mor(M, lam), lamTA))
diffs = 0
for s in lhs.bwd:
    for k in lhs.bwd[s]:
        if lhs.bwd[s].get(k) != rhs.bwd[s].get(k):
            if diffs < 5:
                print(f"  shape {s}\n    pos {k}\n      lhs={lhs.bwd[s][k]}\n      rhs={rhs.bwd[s].get(k)}")
            diffs += 1
print(f"  total differing entries: {diffs}")
