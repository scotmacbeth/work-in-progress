"""
Tiny check: the action category S x| P (a.k.a. transport/transformation category,
category of elements of the action) for an update monad's act (S, P, |).

We take:
  S = Z/2 as a SET       = {0, 1}
  P = Z/2 as a MONOID    = ({0,1}, +, 0)   (group, but a monoid is all we need)
  action  s | p = s + p  (mod 2)           (right action: s|0 = s, s|(p+q) = (s|p)|q)

Action category A = S x| P:
  objects     = S
  hom(s,s')   = { p in P : s | p = s' }
  id_s        = 0 (the monoid unit)
  composition = + in P  (p : s->s', q : s'->s''  =>  p+q : s->s'')

We verify the category laws, list the morphisms, and then ask:
does A admit a NONTRIVIAL strict (orthogonal) factorization system / Zappa-Szep
factorization of A into two wide subcategories (L, R) such that every morphism
factors UNIQUELY as l;r with l in L, r in R?
"""

from itertools import product

S = [0, 1]
Padd = lambda p, q: (p + q) % 2
Pe = 0
act = lambda s, p: (s + p) % 2

# Build hom-sets
hom = {}
for s in S:
    for sp in S:
        hom[(s, sp)] = [p for p in [0, 1] if act(s, p) == sp]

print("Action category S x| P  with S=Z/2 (set), P=Z/2 (monoid, +):")
for s in S:
    for sp in S:
        print(f"  hom({s},{sp}) = {{ p : {s}|p = {sp} }} = {hom[(s,sp)]}")

# Check right-action laws
assert all(act(s, Pe) == s for s in S), "unit law of action"
assert all(act(s, Padd(p, q)) == act(act(s, p), q) for s in S for p in [0,1] for q in [0,1]), "compatibility"

# Category laws: identities and associativity (P is a group so trivially holds, but check)
# A morphism is a triple (s, p, s') with act(s,p)=s'.
morphs = [(s, p, act(s, p)) for s in S for p in [0, 1]]
print("\nMorphisms (source, label p, target):")
for m in morphs:
    print("  ", m)

def comp(m1, m2):
    # m1: s->s', m2: s'->s'' ; result s->s'' with label p1+p2
    (s, p1, sp) = m1
    (t, p2, tpp) = m2
    assert sp == t, "not composable"
    return (s, Padd(p1, p2), tpp)

# identity at s is (s, 0, s)
for m in morphs:
    s, p, sp = m
    assert comp((s, 0, s), m) == m, "left identity"
    assert comp(m, (sp, 0, sp)) == m, "right identity"
print("\nIdentity + associativity laws hold (P a group => associative).")

# This category is the 'codiscrete'/'chaotic' category on 2 objects:
# exactly ONE morphism between every ordered pair of objects.
counts = {(s, sp): len(hom[(s, sp)]) for s in S for sp in S}
print("\nHom-set sizes:", counts)
print("=> exactly one morphism between any two objects: this is the CONTRACTIBLE")
print("   (codiscrete / cofree) category on the 2-element set S.")
print("   This matches Ahman-Uustalu's 'array comonad' example (cofree cat on S).")

# ---- Strict factorization / Zappa-Szep question ----
# A strict factorization system (L,R) on a category A: L,R wide subcategories,
# every morphism factors UNIQUELY as l;r, l in L, r in R.
#
# Enumerate all wide subcategories (containing all 4 identities, closed under comp).
# Objects: {0,1}. The 4 morphisms are id0=(0,0,0), id1=(1,0,1),
#   a=(0,1,1) [0->1], b=(1,1,0) [1->0]. Note a;b=id0, b;a=id1, so {id0,id1,a,b}
#   is the whole (groupoid) category; a,b are mutually inverse.
ID = {(0,0,0), (1,0,1)}
A = set(morphs)

def is_wide_subcat(subset):
    if not ID <= subset:
        return False
    for m1 in subset:
        for m2 in subset:
            if m1[2] == m2[0]:  # composable
                if comp(m1, m2) not in subset:
                    return False
    return True

# all subsets containing the identities
others = [m for m in A if m not in ID]
subcats = []
for r in range(len(others)+1):
    for combo in product([0,1], repeat=len(others)):
        subset = ID | {others[i] for i in range(len(others)) if combo[i]}
        if is_wide_subcat(subset):
            subcats.append(frozenset(subset))
subcats = sorted(set(subcats), key=lambda x: len(x))
print("\nWide subcategories (by morphism set):")
for sc in subcats:
    print("   ", sorted(sc))

def factorizations(L, R):
    """For each morphism m, count factorizations m = l;r, l in L, r in R."""
    result = {}
    for m in A:
        facs = []
        for l in L:
            for r in R:
                if l[2] == r[0] and l[0] == m[0] and r[2] == m[2] and comp(l, r) == m:
                    facs.append((l, r))
        result[m] = facs
    return result

print("\nSearching for NONTRIVIAL strict factorization (L,R), unique l;r for every m:")
found_nontrivial = False
for L in subcats:
    for R in subcats:
        fac = factorizations(L, R)
        if all(len(v) == 1 for v in fac.values()):
            trivialL = (L == ID)   # L only identities  -> R = A
            trivialR = (R == ID)   # R only identities  -> L = A
            tag = "TRIVIAL" if (trivialL or trivialR) else "*** NONTRIVIAL ***"
            print(f"  factorization found: |L|={len(L)} |R|={len(R)}  [{tag}]")
            if not (trivialL or trivialR):
                found_nontrivial = True
print("\nNontrivial strict factorization exists?", found_nontrivial)
