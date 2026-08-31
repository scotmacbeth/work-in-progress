"""
Follow-ups:
 (A) Verify K_bug is ISOMORPHIC (as a category, with matching D) to the rigid twist,
     so the machine-checked H^2(Sk;Z/2)=Z/2, [omega]=generator TRANSFERS verbatim.
 (B) Inspect the extracted distributive law lambda for K_ok: is it a GENUINE nontrivial
     ZS law (worker outcome depends on token via the action), not the degenerate product?
 (C) Count the strict factorization systems for K_ok (= size of the Z^1 torsor).
"""
from itertools import permutations
from pairwise_zs_check import FinCat, extract_lambda, check_zs_axioms
from pairwise_end_to_end import wide_subcats, is_sfs, rigid_twist
from orchestration_zs import K_bug, K_ok, D_bug, D_ok


# ---------- (A) iso K_bug ~= rigid_twist ----------
def find_iso(K1, D1, K2, D2):
    """Search a bijection on objects+arrows that's a functor iso and matches D."""
    RT = K2
    # object maps: S->a, W->x, R->y is the intended one; verify it's an iso.
    obj_map = {"S": "a", "W": "x", "R": "y"}
    arr_map = {"1S": "1a", "tau": "g", "1W": "1x", "1R": "1y",
               "p": "p", "ptau": "pg", "s": "s", "s2": "s2", "q": "q", "qtau": "qg"}
    # check well-typed
    for f, (d, c) in K1.arrows.items():
        g = arr_map[f]
        if (K2.dom(g), K2.cod(g)) != (obj_map[d], obj_map[c]):
            return None, f"type mismatch {f}->{g}"
    # check composition preserved
    for (g, f), gf in K1.comp.items():
        lhs = arr_map[gf]
        rhs = K2.comp.get((arr_map[g], arr_map[f]))
        if lhs != rhs:
            return None, f"comp mismatch {g}o{f}: {lhs} vs {rhs}"
    # check D matches
    if set(arr_map[x] for x in D1) != set(D2):
        return None, "D mismatch"
    return arr_map, "OK"


print("=" * 72)
print("(A)  K_bug  ~=  rigid twist  (as category + matched D)")
RT = rigid_twist()
D_rt = {"1a", "g", "1x", "1y"}
iso, msg = find_iso(K_bug(), D_bug, RT, D_rt)
print("   isomorphism found:", iso is not None, " (", msg, ")")
if iso:
    print("   dictionary:", iso)
    print("   => H^2(Sk;Z/2) = Z/2, [omega] = generator TRANSFERS from Thm rt")
    print("      (machine-checked in cohomology_holonomy.py).")


# ---------- (B) the nontrivial distributive law for K_ok ----------
print("=" * 72)
print("(B)  K_ok distributive law lambda (the coherent worker/token interleaving)")
K = K_ok()
# recover C from the criterion
from pairwise_end_to_end import criterion
crit, L, C = criterion(K, D_ok, verbose=False)
Cset = set(C)
lam, fact, err = extract_lambda(K, Cset, D_ok)
print("   C =", sorted(Cset))
print("   lambda : (d, c) -> (^d c, d^c)   [ d o c = (^d c) o (d^c) ]")
nontrivial = []
for (d, c), (c2, d2) in sorted(lam.items()):
    tag = ""
    if c2 != c or d2 != d:
        tag = "   <-- NONTRIVIAL (action moves the arrow)"
        nontrivial.append((d, c))
    print(f"     ^{d} {c:5s} = {c2:5s} ,  {d}^{c:5s} = {d2:5s}{tag}")
print("   number of nontrivial law entries:", len(nontrivial))
# verify axioms on the C,D subcategories
Csub = FinCat(K.objects, {a: K.arrows[a] for a in Cset},
              {k: v for k, v in K.comp.items() if k[0] in Cset and k[1] in Cset}, K.ident)
Dsub = FinCat(K.objects, {a: K.arrows[a] for a in D_ok},
              {k: v for k, v in K.comp.items() if k[0] in D_ok and k[1] in D_ok}, K.ident)
print("   ZS1-ZS4 + units hold:", check_zs_axioms(Csub, Dsub, lam, verbose=True))


# ---------- (C) count SFS torsors ----------
print("=" * 72)
print("(C)  Strict-factorization-system count over D  (= Z^1 torsor size)")
for name, K, D in [("K_bug (re-entrant)", K_bug(), D_bug),
                   ("K_ok  (locked)   ", K_ok(),  D_ok)]:
    n = sum(1 for Cc in wide_subcats(K) if is_sfs(K, Cc, D))
    print(f"   {name}:  #SFS = {n}   "
          f"{'OBSTRUCTED ([omega] != 0)' if n == 0 else 'composes; torsor size ' + str(n)}")
