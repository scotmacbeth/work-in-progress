"""
TASK 3.  The canonical map  kappa : A + B -> A * B  for a monoidal (*, I) with I = empty.

    A  ~= A * I  --(A * !)-->  A * B      (! : empty -> B)
    B  ~= I * B  --(! * B)-->  A * B

For * = v_S:
    rho^{-1} : A -> A v_S empty  is  a |-> ('l', a)   (the middle piece is empty)
    (id_A v !) : A v_S empty -> A v_S B  sends ('l',a) |-> ('l',a)
      => kappa(inl a) = ('l', a)
    lam^{-1} : B -> empty v_S B  is  b |-> ('r', b)
    (! v id_B) : empty v_S B -> A v_S B  sends ('r',b) |-> ('r',b)
      => kappa(inr b) = ('r', b)

So kappa is exactly the inclusion of the two OUTER summands; its image misses the
middle piece A x S x B entirely.
"""
from core import *
from itertools import product as iproduct

FAILS = []


def kappa(A, B, S):
    """Built by literally composing unitor-inverse with the functorial action."""
    bang_to_B = {}                    # ! : empty -> B  (the empty function)
    bang_to_A = {}                    # ! : empty -> A
    rho_inv = {a: L(a) for a in A}    # inverse of rho : A v_S empty -> A
    lam_inv = {b: R(b) for b in B}    # inverse of lam : empty v_S B -> B
    Avbang = vee_map({a: a for a in A}, bang_to_B, S)   # A v empty -> A v B
    bangvB = vee_map(bang_to_A, {b: b for b in B}, S)   # empty v B -> A v B
    k = {}
    for a in A:
        k[inl(a)] = Avbang(rho_inv[a])
    for b in B:
        k[inr(b)] = bangvB(lam_inv[b])
    return k


print("=" * 78)
print("TASK 3  kappa : A + B -> A v_S B")
print()
print(f"  {'|S|':>3} {'|A|':>3} {'|B|':>3} | {'|A+B|':>5} {'|AvB|':>5} | inj?  surj? | bijection?")
print("  " + "-" * 62)

rows = []
for ns in [0, 1, 2]:
    for na in [0, 1, 2]:
        for nb in [0, 1, 2]:
            A, B, S = mkset(na, 'a'), mkset(nb, 'b'), mkset(ns, 'k')
            dom, cod = dunion(A, B), vee(A, B, S)
            k = kappa(A, B, S)
            # sanity: well-defined into the codomain, total on the domain
            assert frozenset(k.keys()) == dom, "kappa not total"
            assert set(k.values()) <= set(cod), "kappa escapes codomain"
            injective = len(set(k.values())) == len(dom)
            surjective = set(k.values()) == set(cod)
            bij, _ = is_bijection(k, dom, cod)
            rows.append((ns, na, nb, bij))
            print(f"  {ns:>3} {na:>3} {nb:>3} | {len(dom):>5} {len(cod):>5} | "
                  f"{str(injective):5s} {str(surjective):5s} | "
                  f"{'YES' if bij else 'no  (misses A x S x B)'}")

print()
print("  ANALYSIS")
# kappa is always injective; it is surjective iff the middle piece is empty,
# i.e. iff |A|*|S|*|B| = 0.
always_inj = True
for ns, na, nb, bij in rows:
    A, B, S = mkset(na,'a'), mkset(nb,'b'), mkset(ns,'k')
    k = kappa(A, B, S)
    if len(set(k.values())) != len(dunion(A, B)):
        always_inj = False
print(f"    kappa_{{A,B}} is injective in every instance tested : "
      f"{'PASS' if always_inj else 'FAIL'}")
if not always_inj: FAILS.append("3 injectivity")

pred_ok = all(bij == (ns * na * nb == 0) for ns, na, nb, bij in rows)
print(f"    kappa_{{A,B}} is a BIJECTION exactly when |A|*|S|*|B| = 0 : "
      f"{'PASS' if pred_ok else 'FAIL'}")
if not pred_ok: FAILS.append("3 bijection criterion")

# the headline statement: bijective for ALL A,B  <=>  S empty
per_S = {}
for ns in [0, 1, 2]:
    per_S[ns] = all(bij for (s, a, b, bij) in rows if s == ns)
print()
print(f"    {'|S|':>3} | kappa_{{A,B}} a bijection for ALL |A|,|B| in {{0,1,2}}?")
for ns in [0, 1, 2]:
    print(f"    {ns:>3} | {'YES' if per_S[ns] else 'NO'}")
head_ok = per_S[0] and not per_S[1] and not per_S[2]
print(f"    => kappa is a natural ISOMORPHISM  iff  S = empty : "
      f"{'PASS' if head_ok else 'FAIL'}")
if not head_ok: FAILS.append("3 headline")

print()
print("  EXPLICIT WITNESS |A|=|B|=|S|=1  (kappa is NOT surjective):")
A, B, S = mkset(1,'a'), mkset(1,'b'), mkset(1,'k')
k = kappa(A, B, S)
for x in sorted(dunion(A, B), key=repr):
    print(f"    kappa({x!r}) = {k[x]!r}")
missing = sorted(set(vee(A,B,S)) - set(k.values()), key=repr)
print(f"    A v_S B = {sorted(vee(A,B,S), key=repr)}")
print(f"    NOT IN THE IMAGE: {missing}   <-- the middle piece A x S x B")

print()
print("  CAVEAT (honest reporting): for a FIXED pair (A,B) with A or B empty,")
print("  kappa_{A,B} is a bijection for every S (the middle piece A x S x B is")
print("  empty for trivial reasons).  The clean statement is therefore:")
print("    kappa_{A,B} bijective  <=>  |A|*|S|*|B| = 0;")
print("    kappa bijective for ALL A,B (i.e. a natural iso)  <=>  S = empty.")

print()
print("TASK 3 RESULT:", "PASS" if not FAILS else f"FAIL {FAILS}")
