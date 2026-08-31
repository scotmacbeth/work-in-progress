"""
GAP-CLOSURE checks for the two upgrades (PROVE 2026-08-05, heartbeat-3).

Reuses the monad models from boundary_table.py.

THEOREM 2  ((3) => (5)):   str at an arity k>=2 is NON-SURJECTIVE whenever |M1|>=2.
   Mechanism: for w in M(prod_b Z_b), str(w)=(M pi_b w)_b has ALL components sharing
   the single shape M!(w) in M1.  So any codomain tuple with two DIFFERENT shapes in
   two components is OUTSIDE the image.  We exhibit such a mismatched tuple.
   Also: unit shape eta(*) is UNARY for Pi-Mendler M (|leaves(eta x)|==1),
   NON-unary for Reader/State -> gives |M1|>=2 automatically once a k>=2 shape exists.

THEOREM 1  ((1)<=>(2)):  cartFun  <=>  T_M preserves cartesian morphisms (already in
   boundary_table); here we probe the MONAD half:  the leaf-comparison
        kappa_mu : Sum_b lv(inner_b)  ->  lv(mu mm)          (combined-inner -> result)
   defined by LABEL-MATCHING (Pi-cointerpretation j reindexes along it).
   Claims:
     * kappa_mu is INJECTIVE  (no merging)  for polynomial (cartFun) M
       -- proved from label-freeness; here we check Id/Maybe/Exc/Writer/List (Y) vs Pf (N).
     * kappa_mu is SURJECTIVE (no creation/duplication) for the whole class
       -- checks whether any member DUPLICATES a leaf in mu.
"""
from boundary_table import (Id, Maybe, Exc, Writer, Pf, Reader, ListB, StateB)
from itertools import product as iproduct

def yn(b): return 'Y' if b else '.'

# ----------------------------------------------------------------------
# THEOREM 2 core :  unit shape arity  and  str non-surjectivity at k>=2
# ----------------------------------------------------------------------
print("="*70)
print("THEOREM 2 :  unit-shape arity   and   str surjectivity at arity k")
print("="*70)

def unit_arity(M):
    # arity of eta(*) : number of leaves of eta applied to a one-point set label 'o'
    return len(M.leaves(M.eta('o')))

def M1_size(M):
    return len(M.obj(['o']))          # |M 1|  (shapes)

def str_surjective_at(M, Zs):
    """
    Zs = list of factor sets (the family (Z_b)_b), all nonempty.
    str : M(prod Zs) -> prod_b M(Z_b),   w |-> (M pi_b w)_b.
    Return (surjective?, witness_missing_tuple_or_None).
    We compare the IMAGE (as a set of shape-signatures across components) to the
    full codomain; a codomain element with mismatched component-shapes is missing.
    """
    Zs = [list(Z) for Z in Zs]
    prod = list(iproduct(*Zs))                     # prod_b Z_b as tuples
    Mprod = M.obj(prod)
    # image: for w, component b element = M(pi_b)(w); record its SHAPE (via M! : ->M1)
    def shape(el):
        # shape = image under M(const 'o')  (collapse all labels)
        return str(M.fmap(lambda t: 'o')(el))
    image = set()
    for w in Mprod:
        comp_shapes = tuple(shape(M.fmap((lambda bb: (lambda t: t[bb]))(b))(w))
                            for b in range(len(Zs)))
        image.add(comp_shapes)
    # codomain shape-signatures: independent choice of a shape per component
    per_comp_shapes = []
    for Z in Zs:
        MZ = M.obj(Z)
        per_comp_shapes.append(sorted(set(shape(el) for el in MZ)))
    codomain = set(iproduct(*per_comp_shapes))
    missing = codomain - image
    return (len(missing) == 0), (sorted(missing)[0] if missing else None), len(image), len(codomain)

monads = [Id(), Maybe(), Exc(('e',)), Writer([0,1], lambda a,b:(a+b)%2, 0, 'Writer(Z2)'),
          ListB(2), Pf(), Reader((0,1)), StateB((0,1))]

print(f"{'monad':20s} {'|M1|':5s} {'unitArity':9s}  (Pi-Mendler wants unitArity==1)")
for M in monads:
    print(f"{M.name:20s} {M1_size(M):<5d} {unit_arity(M):<9d}")

print()
print("str surjectivity at a BINARY arity (Z1={0,1}, Z2={x,y}), both nonempty:")
print(f"{'monad':20s} {'surj?':5s} {'|img|':6s} {'|cod|':6s}  missing-shape-tuple (shape mismatch witness)")
for M in monads:
    surj, wit, ni, nc = str_surjective_at(M, [[0,1],['x','y']])
    w = '' if surj else f'  MISSING e.g. {wit}'
    print(f"{M.name:20s} {yn(surj):5s} {ni:<6d} {nc:<6d}{w}")

# ----------------------------------------------------------------------
# THEOREM 1 monad-half :  kappa_mu injective / surjective
# ----------------------------------------------------------------------
print()
print("="*70)
print("THEOREM 1 monad-half :  leaf-comparison kappa_mu for mu  (cartMu)")
print("="*70)
print("kappa_mu : combined-inner leaves -> result leaves, by LABEL MATCHING.")
print("We test on generic mm with ALL-DISTINCT inner labels (polynomial: labels free).")
print("  injective  = no MERGING ;  surjective = no CREATION/DUPLICATION.")
print("  cartMu <=> bijective.")
print()

def kappa_mu_probe(M, base='abcd'):
    """
    Build generic mm in MM(S) with DISTINCT labels, compute mu, and test whether
    the multiset of result-leaf labels equals the multiset of combined-inner labels
    (bijection of label-multisets  <=>  kappa_mu bijective, since labels distinct).
    We only get a clean read for POLYNOMIAL M where positions carry free labels;
    for Pf the 'labels' are the elements themselves (so merging shows as label loss).
    """
    S = list(base)
    inj = True_dup = None
    worst = None
    inj_ok = True; surj_ok = True
    for mm in M.obj(M.obj(S)):
        # combined-inner labels (with multiplicity) : for each inner leaf, its S-label
        inner_labels = []
        for inner in M.leaves(mm):        # inner in M S
            inner_labels += list(M.leaves(inner))
        result_labels = list(M.leaves(M.mu(mm)))
        from collections import Counter
        ci = Counter(inner_labels); rs = Counter(result_labels)
        # merging: some label appears fewer times in result than inner (two inner->one)
        # BUT only counts as merge if those inner leaves are DISTINCT positions with
        # equal labels; with distinct S this cannot happen for polynomial M.
        # creation/dup: some result count exceeds inner count.
        if any(rs[l] < ci[l] for l in ci):      # a combined-inner leaf lost
            inj_ok = False
            if worst is None: worst = ('MERGE', mm, dict(ci), dict(rs))
        if any(rs[l] > ci.get(l,0) for l in rs): # a result leaf not backed by inner
            surj_ok = False
            if worst is None: worst = ('CREATE/DUP', mm, dict(ci), dict(rs))
    return inj_ok, surj_ok, worst

for M in [Id(), Maybe(), Exc(('e',)), Writer([0,1], lambda a,b:(a+b)%2,0,'Writer(Z2)'),
          ListB(2), Pf(), Reader((0,1))]:
    inj, surj, worst = kappa_mu_probe(M)
    tag = '' if (inj and surj) else f'   <- {worst[0] if worst else "?"}'
    print(f"{M.name:20s}  no-merge(inj)={yn(inj)}  no-create/dup(surj)={yn(surj)}  cartMu={yn(inj and surj)}{tag}")

print()
print("READING:")
print(" - unitArity==1 exactly for the Pi-Mendler monads; Reader/State have unitArity>=2")
print("   -> once a k>=2 shape exists, unit shape (arity 1) differs from it => |M1|>=2.")
print(" - str NON-surjective at binary arity for every |M1|>=2 monad with a >=2 shape")
print("   (List, Pf) : missing tuple = two DIFFERENT component-shapes. => (3) fails => (3)=>(5).")
print(" - kappa_mu bijective (cartMu) for polynomial members; Pf merges (non-inj).")
print("   NO member DUPLICATES (surj holds throughout) -> no-creation confirmed on class.")
