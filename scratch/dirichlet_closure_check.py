"""
Independent check of MacBeth's claim that (Cont, ⊗, y) is closed with

    S_{[q,r]}     = Cont(q,r) = Σ_{u:S_q→S_r} ∏_{t:S_q} (r[u t] → q[t])
    [q,r][(u,φ)]  = Σ_{t:S_q} r[u t]

METHOD (anti-mirror):
  * A container is (S, pos) with S = range(n), pos[s] = |p[s]|.
  * `hom_enum(a,b)` enumerates Cont(a,b) DIRECTLY from the raw definition
    (u : S_a → S_b together with φ_s : b[u s] → a[s]).  It is a single generic
    routine that knows NOTHING about ⊗ or [-,-].
  * `tensor(p,q)` and `ihom(q,r)` build containers from their raw definitions.
  * We then compare  |hom(tensor(p,q), r)|  vs  |hom(p, ihom(q,r))| .
    Neither side is defined in terms of the other; the only shared code is the
    generic hom enumerator, which is the definition itself.
  * NEGATIVE CONTROLS: deliberately wrong internal homs must make the test FAIL.

Positions of size 0 and shape-sets of size 0 are included; 0**0 = 1 in Python,
which is the correct count of maps ∅ → ∅ (and ∅ → X in general: exactly one).
"""
import itertools, random, sys
from functools import lru_cache

# ---------------------------------------------------------------- containers
# container = tuple of position-set SIZES, one per shape.  So
#   p = (2,0,3)  means S_p = {0,1,2}, |p[0]|=2, |p[1]|=0, |p[2]|=3.
#   ()           means S_p = ∅  (the initial container, extension = constant ∅).

def nshapes(p):
    return len(p)

# ------------------------------------------------- raw hom-set (enumeration)
def hom_enum(a, b):
    """Enumerate Cont(a,b) from the definition:
       (u : S_a → S_b,  φ_s : b[u s] → a[s] for each s).
       Returned as a list of (u, phi) with u a tuple of length |S_a| and
       phi a tuple of |S_a| tuples, phi[s] of length b[u[s]] with entries < a[s].
    """
    out = []
    for u in itertools.product(range(nshapes(b)), repeat=nshapes(a)):
        # for each shape s of a, all functions b[u s] -> a[s]
        per_shape = []
        for s in range(nshapes(a)):
            dom = b[u[s]]          # |b[u s]|
            cod = a[s]             # |a[s]|
            per_shape.append(list(itertools.product(range(cod), repeat=dom)))
        for phi in itertools.product(*per_shape):
            out.append((u, phi))
    return out

def hom_size(a, b):
    """|Cont(a,b)| = ∏_{s∈S_a} Σ_{v∈S_b} |a[s]|^{|b[v]|}, straight from the
       definition (choose u s and then a map b[u s] → a[s], independently per s).
       Used only for the large sweep; cross-checked against hom_enum below."""
    total = 1
    for s in range(nshapes(a)):
        total *= sum(a[s] ** b[v] for v in range(nshapes(b)))
    return total

# ---------------------------------------------------------------- ⊗ and [-,-]
def tensor(p, q):
    """p ⊗ q = (S_p × S_q, (s,t) ↦ p[s] × q[t]).  Shape order: lexicographic."""
    return tuple(p[s] * q[t] for s in range(nshapes(p)) for t in range(nshapes(q)))

def ihom(q, r):
    """MacBeth: shapes = Cont(q,r); positions at (u,φ) = Σ_{t:S_q} r[u t]."""
    return tuple(sum(r[u[t]] for t in range(nshapes(q)))
                 for (u, phi) in hom_enum(q, r))

# ---- negative controls (deliberately WRONG internal homs) -------------------
def ihom_wrong_positions_q(q, r):
    """WRONG: positions Σ_{t} q[t]  (target's positions replaced by source's)."""
    sq = sum(q)
    return tuple(sq for _ in hom_enum(q, r))

def ihom_wrong_shapes_only_u(q, r):
    """WRONG: shapes = only the shape maps S_q → S_r (forget φ)."""
    return tuple(sum(r[u[t]] for t in range(nshapes(q)))
                 for u in itertools.product(range(nshapes(r)), repeat=nshapes(q)))

def ihom_wrong_positions_product(q, r):
    """WRONG: positions ∏_{t} r[u t] instead of Σ_{t} r[u t]."""
    out = []
    for (u, phi) in hom_enum(q, r):
        prod = 1
        for t in range(nshapes(q)):
            prod *= r[u[t]]
        out.append(prod)
    return tuple(out)

# ---- multiset forms of the same internal homs (for big cases: same raw
#      definitions, but shapes recorded as (position-size, multiplicity) pairs so
#      we never have to materialise |Cont(q,r)| tuples).  Multiplicity of a shape
#      map u is  ∏_t |q[t]|^{|r[u t]|}  = the number of φ's over it. --------------
def ihom_ms(q, r):
    out = []
    for u in itertools.product(range(nshapes(r)), repeat=nshapes(q)):
        mult = 1
        for t in range(nshapes(q)):
            mult *= q[t] ** r[u[t]]
        if mult == 0:
            continue                                   # no φ over this u
        out.append((sum(r[u[t]] for t in range(nshapes(q))), mult))
    return out

def ihom_ms_wrong_positions_q(q, r):
    sq = sum(q)
    return [(sq, m) for (_, m) in ihom_ms(q, r)]

def ihom_ms_wrong_shapes_only_u(q, r):
    return [(sum(r[u[t]] for t in range(nshapes(q))), 1)
            for u in itertools.product(range(nshapes(r)), repeat=nshapes(q))]

def ihom_ms_wrong_positions_product(q, r):
    out = []
    for u in itertools.product(range(nshapes(r)), repeat=nshapes(q)):
        mult = 1
        prod = 1
        for t in range(nshapes(q)):
            mult *= q[t] ** r[u[t]]
            prod *= r[u[t]]
        if mult == 0:
            continue
        out.append((prod, mult))
    return out

def hom_size_ms(a, b_ms):
    total = 1
    for s in range(nshapes(a)):
        total *= sum(m * (a[s] ** sz) for (sz, m) in b_ms)
    return total

# ---------------------------------------------------------------- the test
def lhs(p, q, r):
    return hom_size(tensor(p, q), r)

def rhs(p, q, r, ih=ihom):
    return hom_size(p, ih(q, r))

def rhs_ms(p, q, r, ihm=ihom_ms):
    return hom_size_ms(p, ihm(q, r))

def run(triples, ih, label, verbose_fail=3, ms=False):
    fails = []
    for (p, q, r) in triples:
        L = lhs(p, q, r)
        R = rhs_ms(p, q, r, ih) if ms else rhs(p, q, r, ih)
        if L != R:
            fails.append((p, q, r, L, R))
    print(f"  {label:38s}  tested {len(triples):6d}  failures {len(fails):6d}")
    for f in fails[:verbose_fail]:
        print(f"      e.g. p={f[0]} q={f[1]} r={f[2]}  |Cont(p⊗q,r)|={f[3]}  |Cont(p,[q,r])|={f[4]}")
    return len(fails)

# ---------------------------------------------------------------- sanity: enum vs size
print("=== 0. sanity: hom_enum length == hom_size (raw enumeration vs count) ===")
bad = 0
small = [c for n in range(0, 3) for c in itertools.product(range(0, 3), repeat=n)]
for a in small:
    for b in small:
        if len(hom_enum(a, b)) != hom_size(a, b):
            bad += 1
            print("   MISMATCH", a, b, len(hom_enum(a, b)), hom_size(a, b))
print(f"   containers checked: {len(small)**2}, mismatches: {bad}")
assert bad == 0

# ---------------------------------------------------------------- 1. FULL enumeration test
# Compare hom-SETS by explicit enumeration (not just cardinality) on tiny cases,
# and also check the explicit transpose map is a bijection.
print("\n=== 1. explicit bijection check (transpose is well-defined & bijective) ===")

def transpose(p, q, r, m):
    """(U,Φ) : p⊗q → r   ↦   (Ū,Φ̄) : p → [q,r].
       Built from the derivation; used ONLY to confirm the counting bijection is
       realised by the expected map.  The pass/fail of tasks 3 is NOT based on this."""
    U, Phi = m
    sq, sr = nshapes(q), nshapes(r)
    ih_shapes = hom_enum(q, r)                 # the shape set of [q,r]
    index = {c: i for i, c in enumerate(ih_shapes)}
    Ubar, Phibar = [], []
    for s in range(nshapes(p)):
        # shape map of the transpose: the container morphism q → r
        u_s = tuple(U[s * sq + t] for t in range(sq))
        phi_s = []
        for t in range(sq):
            k = s * sq + t
            # Phi[k] : r[U(s,t)] → p[s] × q[t];  we encode p[s]×q[t] as x*q[t]+y
            qt = q[t]
            phi_s.append(tuple(Phi[k][x] % qt for x in range(r[U[k]])))   # 2nd component
        c = (u_s, tuple(phi_s))
        Ubar.append(index[c])
        # position map  Σ_t r[u_s t] → p[s]   (1st component of Phi), in the same
        # order that ihom's positions are counted: t ascending
        pm = []
        for t in range(sq):
            k = s * sq + t
            qt = q[t]
            for x in range(r[U[k]]):
                pm.append(Phi[k][x] // qt)                                 # 1st component
        Phibar.append(tuple(pm))
    return (tuple(Ubar), tuple(Phibar))

tiny = [c for n in range(0, 3) for c in itertools.product(range(0, 3), repeat=n)]
CAP = 30000          # skip triples whose hom-sets are too big to enumerate explicitly
nchk = 0
nskip = 0
for p in tiny:
    for q in tiny:
        for r in tiny:
            if hom_size(tensor(p, q), r) > CAP or hom_size(p, ihom(q, r)) > CAP:
                nskip += 1
                continue
            L = hom_enum(tensor(p, q), r)
            R = set(hom_enum(p, ihom(q, r)))
            img = set()
            for m in L:
                tm = transpose(p, q, r, m)
                assert tm in R, f"transpose lands outside Cont(p,[q,r]): {p} {q} {r} {m} -> {tm}"
                img.add(tm)
            assert len(img) == len(L), f"transpose not injective: {p} {q} {r}"
            assert img == R, f"transpose not surjective: {p} {q} {r} ({len(img)} vs {len(R)})"
            nchk += 1
print(f"   transpose is a bijection Cont(p⊗q,r) → Cont(p,[q,r]) on {nchk} triples "
      f"({nskip} skipped: hom-set > {CAP})")
print("   (shapes ≤ 2, positions ≤ 2, empty cases included)")

# ---------------------------------------------------------------- 2. exhaustive cardinality sweep
print("\n=== 2. exhaustive sweep, |S| ≤ 2, positions ≤ 2 (includes all empty cases) ===")
exh = [(p, q, r) for p in tiny for q in tiny for r in tiny]
f_ok = run(exh, ihom, "MacBeth [q,r]  (claim)")
f_c1 = run(exh, ihom_wrong_positions_q, "NEG CTRL: positions Σ_t q[t]")
f_c2 = run(exh, ihom_wrong_shapes_only_u, "NEG CTRL: shapes = shape maps only")
f_c3 = run(exh, ihom_wrong_positions_product, "NEG CTRL: positions ∏_t r[u t]")

# ---------------------------------------------------------------- 3. random sweep, sizes 0..3
print("\n=== 3. random sweep, |S| ∈ 0..3, positions ∈ 0..3 ===")
random.seed(20260714)
def rand_container():
    n = random.randint(0, 3)
    return tuple(random.randint(0, 3) for _ in range(n))
rnd = [(rand_container(), rand_container(), rand_container()) for _ in range(3000)]
# cross-check the multiset counter against the explicit one on the tiny cases first
for p in tiny:
    for q in tiny:
        for r in tiny:
            assert rhs(p, q, r, ihom) == rhs_ms(p, q, r, ihom_ms), (p, q, r)
print("   (multiset counter agrees with explicit [q,r] enumeration on all tiny triples)")
r_ok = run(rnd, ihom_ms, "MacBeth [q,r]  (claim)", ms=True)
r_c1 = run(rnd, ihom_ms_wrong_positions_q, "NEG CTRL: positions Σ_t q[t]", ms=True)
r_c2 = run(rnd, ihom_ms_wrong_shapes_only_u, "NEG CTRL: shapes = shape maps only", ms=True)
r_c3 = run(rnd, ihom_ms_wrong_positions_product, "NEG CTRL: positions ∏_t r[u t]", ms=True)

# ---------------------------------------------------------------- 4. edge cases spelled out
print("\n=== 4. named edge cases ===")
y = (1,)                       # the unit: one shape, one position?  NO -- see below
unit = (1,)                    # y = (1, * ↦ 1): one shape, ONE position
cases = {
    "S_q = ∅":            ((2,), (), (1, 2)),
    "S_r = ∅":            ((2,), (1,), ()),
    "S_p = ∅":            ((), (1,), (2,)),
    "all pos = 0":        ((0,), (0,), (0,)),
    "q = y (unit)":       ((2, 1), unit, (3, 0)),
    "r = y (unit)":       ((2, 0), (1, 3), unit),
    "p has empty pos":    ((0, 2), (1,), (2, 1)),
}
for name, (p, q, r) in cases.items():
    L, R = lhs(p, q, r), rhs(p, q, r)
    print(f"  {name:20s} p={str(p):10s} q={str(q):10s} r={str(r):10s}  L={L:6d} R={R:6d}  {'OK' if L==R else '*** FAIL ***'}")

# ---------------------------------------------------------------- 5. unit law y ⊗ p ≅ p
print("\n=== 5. unit: [y, r] ≅ r ? (should be, since y ⊗ q ≅ q) ===")
for r in tiny:
    ih = ihom(unit, r)
    print(f"   r={str(r):10s}  [y,r]={str(ih):20s}  {'≅ r' if sorted(ih)==sorted(r) else '*** NOT ≅ r ***'}")

# ---------------------------------------------------------------- 6. NATURALITY in p (explicit)
print("\n=== 6. naturality in p: transpose(m ∘ (g ⊗ id_q)) == transpose(m) ∘ g ? ===")
def comp(f, g_):
    """compose  a --f--> b --g_--> c   in Cont.   f=(u,φ):a→b, g_=(w,χ):b→c.
       result = (w∘u, s ↦ φ_s ∘ χ_{u s})."""
    u, phi = f
    w, chi = g_
    u2 = tuple(w[u[s]] for s in range(len(u)))
    phi2 = tuple(tuple(phi[s][chi[u[s]][x]] for x in range(len(chi[u[s]])))
                 for s in range(len(u)))
    return (u2, phi2)

def tensor_id(p2, p, q, g_):
    """g ⊗ id_q  :  p2 ⊗ q → p ⊗ q   for g = (v,ψ) : p2 → p."""
    v, psi = g_
    sq = nshapes(q)
    u = tuple(v[s2] * sq + t for s2 in range(nshapes(p2)) for t in range(sq))
    phi = []
    for s2 in range(nshapes(p2)):
        for t in range(sq):
            # (p⊗q)[(v s2, t)] = p[v s2] × q[t]  →  p2[s2] × q[t] ;  encode x*q[t]+y
            qt = q[t]
            dom = p[v[s2]] * qt
            phi.append(tuple((psi[s2][x // qt]) * qt + (x % qt) for x in range(dom)))
    return (u, tuple(phi))

nat_checked = 0
nat_fail = 0
nat_skip = 0
smalltiny = [c for n in range(0, 3) for c in itertools.product(range(0, 3), repeat=n)]
for p2 in smalltiny:
    for p in smalltiny:
        for q in smalltiny:
            for r in smalltiny:
                if hom_size(p2, p) * hom_size(tensor(p, q), r) > 4000:
                    nat_skip += 1
                    continue
                for g_ in hom_enum(p2, p):
                    for m in hom_enum(tensor(p, q), r):
                        left = transpose(p2, q, r, comp(tensor_id(p2, p, q, g_), m))
                        right = comp(g_, transpose(p, q, r, m))
                        nat_checked += 1
                        if left != right:
                            nat_fail += 1
                            if nat_fail <= 3:
                                print("   NAT FAIL", p2, p, q, r, g_, m, left, right)
print(f"   naturality squares checked: {nat_checked}, failures: {nat_fail} "
      f"({nat_skip} (p2,p,q,r) quadruples skipped as too large)")

# ---------------------------------------------------------------- summary
print("\n================ SUMMARY ================")
print(f" exhaustive triples : {len(exh)}   failures: {f_ok}")
print(f" random triples     : {len(rnd)}   failures: {r_ok}")
print(f" TOTAL triples      : {len(exh)+len(rnd)}   TOTAL failures: {f_ok + r_ok}")
print(f" negative control 1 (positions Σ_t q[t])      caught: {f_c1 + r_c1} failures  -> {'CAUGHT' if f_c1+r_c1 else '!!! NOT CAUGHT — TEST IS WORTHLESS !!!'}")
print(f" negative control 2 (shapes = shape maps)     caught: {f_c2 + r_c2} failures  -> {'CAUGHT' if f_c2+r_c2 else '!!! NOT CAUGHT — TEST IS WORTHLESS !!!'}")
print(f" negative control 3 (positions ∏_t r[u t])    caught: {f_c3 + r_c3} failures  -> {'CAUGHT' if f_c3+r_c3 else '!!! NOT CAUGHT — TEST IS WORTHLESS !!!'}")
print(f" naturality in p    : {nat_checked} squares, {nat_fail} failures")
