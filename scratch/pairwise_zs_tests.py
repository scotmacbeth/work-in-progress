"""Driver tests for pairwise ZS claims, using pairwise_zs_check.py."""
from itertools import product as iproduct
from pairwise_zs_check import FinCat, build_zs_product, check_zs_axioms, extract_lambda


def cyclic_monoid(n, obj=0, prefix=""):
    """Z/n as a one-object category on object `obj`. arrows prefix+'k', k=0..n-1.
       id = prefix+'0'. comp: a o b = a+b mod n."""
    objs = [obj]
    names = [f"{prefix}{k}" for k in range(n)]
    arrows = {nm: (obj, obj) for nm in names}
    comp = {}
    for i in range(n):
        for j in range(n):
            comp[(f"{prefix}{i}", f"{prefix}{j}")] = f"{prefix}{(i+j) % n}"
    ident = {obj: f"{prefix}0"}
    return FinCat(objs, arrows, comp, ident)


def all_type_correct_lambdas(C, D):
    """Yield every lambda: (d,c)->(c2,d2) with correct typing AND units forced.
       Units are forced; remaining 'free' pairs range over all type-correct (c2,d2)."""
    # composable pairs (d,c): dom(d)==cod(c)
    pairs = [(d, c) for d in D.arrows for c in C.arrows if D.dom(d) == C.cod(c)]
    # forced by units:
    forced = {}
    free = []
    for (d, c) in pairs:
        is_d_id = (d == D.ident[D.dom(d)])
        is_c_id = (c == C.ident[C.dom(c)])
        if is_d_id:
            forced[(d, c)] = (c, D.ident[C.dom(c)])          # ^id c = c, id^c=id
        elif is_c_id:
            forced[(d, c)] = (C.ident[D.cod(d)], d)          # ^d id = id, d^id=d
        else:
            free.append((d, c))
    # for each free pair, candidate (c2,d2): c2 in C, d2 in D with
    #   C.cod(c2)=D.cod(d), D.dom(d2)=C.dom(c), C.dom(c2)=D.cod(d2)
    cand = {}
    for (d, c) in free:
        lst = []
        for c2 in C.arrows:
            if C.cod(c2) != D.cod(d): continue
            for d2 in D.arrows:
                if D.dom(d2) != C.dom(c): continue
                if C.dom(c2) != D.cod(d2): continue
                lst.append((c2, d2))
        cand[(d, c)] = lst
    keys = free
    spaces = [cand[k] for k in keys]
    total = 1
    for s in spaces: total *= max(1, len(s))
    for combo in iproduct(*spaces):
        lam = dict(forced)
        for k, v in zip(keys, combo):
            lam[k] = v
        yield lam
    return


def equivalence_test(C, D, label):
    n_ax = n_assoc = n_disagree = n_total = 0
    disagreements = []
    for lam in all_type_correct_lambdas(C, D):
        n_total += 1
        ax = check_zs_axioms(C, D, lam)
        K = build_zs_product(C, D, lam)
        assoc = K.check_category()
        if ax: n_ax += 1
        if assoc: n_assoc += 1
        if ax != assoc:
            n_disagree += 1
            if len(disagreements) < 3:
                disagreements.append((dict(lam), ax, assoc))
    print(f"[{label}] total_lambda={n_total}  axioms_hold={n_ax}  "
          f"associative={n_assoc}  DISAGREE={n_disagree}")
    if disagreements:
        for lam, ax, assoc in disagreements:
            print("   DISAGREEMENT axioms=%s assoc=%s  lam=%s" % (ax, assoc, lam))
    return n_disagree == 0


# ---- Test 1: monoid x monoid, classical ZS, exhaustive ----
print("=== Test 1: monoid x monoid (exhaustive over all lambda) ===")
ok = True
ok &= equivalence_test(cyclic_monoid(2, prefix="a"), cyclic_monoid(2, prefix="b"),
                       "Z2 x Z2")
ok &= equivalence_test(cyclic_monoid(3, prefix="a"), cyclic_monoid(2, prefix="b"),
                       "Z3 x Z2")
ok &= equivalence_test(cyclic_monoid(2, prefix="a"), cyclic_monoid(3, prefix="b"),
                       "Z2 x Z3")

# ---- Test 2: a genuine two-object factor.  C and D share objects {0,1}.
# C = walking arrow c:0->1 plus a loop g (Z/2) at 1.   Actually keep small:
# C: objects {0,1}; arrows id0,id1, c:0->1.   (thin walking arrow)
# D: objects {0,1}; arrows id0,id1, d:1->0.   (thin walking arrow, other way)
def walking_arrow(src, dst, arrow_name, label0=0, label1=1):
    objs = [label0, label1]
    arrows = {f"id{label0}": (label0, label0), f"id{label1}": (label1, label1),
              arrow_name: (src, dst)}
    comp = {}
    for o in objs:
        comp[(f"id{o}", f"id{o}")] = f"id{o}"
    # arrow composed with identities
    comp[(arrow_name, f"id{src}")] = arrow_name
    comp[(f"id{dst}", arrow_name)] = arrow_name
    ident = {label0: f"id{label0}", label1: f"id{label1}"}
    return FinCat(objs, arrows, comp, ident)

print()
print("=== Test 2: two-object thin factors, C up (0->1), D down (1->0) ===")
C2 = walking_arrow(0, 1, "c")       # c: 0->1
D2 = walking_arrow(1, 0, "d")       # d: 1->0
equivalence_test(C2, D2, "Cup x Ddown")

# ---- Test 3: C = walking arrow c:1->0, D = walking arrow d:0->1  (gives retract) ----
print()
print("=== Test 3: C down (1->0), D up (0->1)  [walking retract] ===")
C3 = walking_arrow(1, 0, "c")       # c: 1->0
D3 = walking_arrow(0, 1, "d")       # d: 0->1
equivalence_test(C3, D3, "Cdown x Dup")
# show the resulting K for the (unique nontrivial) law
for lam in all_type_correct_lambdas(C3, D3):
    if check_zs_axioms(C3, D3, lam):
        K = build_zs_product(C3, D3, lam)
        print("   law", {k: v for k, v in lam.items()},
              "-> assoc category:", K.check_category(),
              " |arrows|:", len(K.arrows))
        # identify hom-sets
        homs = {}
        for f, (a, b) in K.arrows.items():
            homs.setdefault((a, b), []).append(f)
        for k in sorted(homs, key=str):
            print("     Hom%s = %s" % (k, homs[k]))
