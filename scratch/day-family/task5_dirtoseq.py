"""
TASK 5.  dirToSeq : C (x)_Dir D  ->  C <| D

  shapes    : (s,t) |-> (s, const_t)   where const_t : P(s) -> T is constant at t
  positions : (contravariantly, as a container morphism)
                 positions of (C <| D) at (s, const_t)
               =  { (p,q) : p in P(s), q in Q(const_t p) = Q(t) }
               =  P(s) x Q(t)
               =  positions of (C (x)_Dir D) at (s,t)
              -- the IDENTITY map.  Well-typed precisely because const_t is constant.

TASK 6 is at the bottom of this file.
"""
from core import *
from itertools import product as iproduct

FAILS = []


def all_small_containers(max_shapes=2, max_pos=2, tag='s'):
    out = []
    for n in range(max_shapes + 1):
        shapes = [f"{tag}{i}" for i in range(n)]
        for counts in iproduct(range(max_pos + 1), repeat=n):
            P = {shapes[i]: frozenset((shapes[i], j) for j in range(counts[i]))
                 for i in range(n)}
            out.append(Cont(frozenset(shapes), P))
    return out


def dirToSeq(C, D):
    src = dirichlet(C, D)
    tgt = compose(C, D)
    u, fmaps = {}, {}
    for s in C.S:
        for t in D.S:
            const_t = {p: t for p in C.P[s]}          # const_t : P(s) -> T
            tgt_shape = (s, hfun(const_t))
            u[(s, t)] = tgt_shape
            # position map: tgt.P[tgt_shape] -> src.P[(s,t)], the identity (p,q)|->(p,q)
            fmaps[(s, t)] = {x: x for x in tgt.P[tgt_shape]}
    return Mor(src, tgt, u, fmaps)


print("=" * 78)
print("TASK 5  dirToSeq is a well-typed container morphism?")
Cs = all_small_containers(2, 2, 's')
Ds = all_small_containers(2, 2, 't')

bad_type = []
for C in Cs:
    for D in Ds:
        m = dirToSeq(C, D)
        errs = check_mor_types(m)
        if errs:
            bad_type.append((C, D, errs[:2]))
print(f"  {len(Cs)*len(Ds)} container pairs; type errors: {len(bad_type)}")
print(f"  dirToSeq is a well-typed container morphism : "
      f"{'PASS' if not bad_type else 'FAIL'}")
for b in bad_type[:5]: print("    FAIL:", b)
if bad_type: FAILS.append("5 typing")

# the position component is ALWAYS a bijection -- the whole obstruction is on shapes
posbij = True
for C in Cs:
    for D in Ds:
        m = dirToSeq(C, D)
        for s in m.src.S:
            ok, _ = is_bijection(m.f[s], m.tgt.P[m.u[s]], m.src.P[s])
            if not ok: posbij = False
print(f"  every position component is a bijection     : {'PASS' if posbij else 'FAIL'}")
if not posbij: FAILS.append("5 position components")


# ---------------------------------------------------------------- (a) not injective
print()
print("TASK 5a  a C,D where the SHAPE map is NOT injective")
C = Cont(frozenset({'s0'}), {'s0': frozenset()})              # one shape, ZERO positions
D = Cont(frozenset({'t0', 't1'}), {'t0': frozenset(), 't1': frozenset()})   # two shapes
m = dirToSeq(C, D)
print(f"  C = one shape s0 with 0 positions;  D = two shapes t0,t1")
print(f"  shapes of C (x)_Dir D : {sorted(m.src.S, key=repr)}   (2 shapes)")
print(f"  shapes of C <| D      : {sorted(m.tgt.S, key=repr)}   "
      f"({len(m.tgt.S)} shape: only the empty function P(s0)=0 -> T)")
for x in sorted(m.src.S, key=repr):
    print(f"    u({x!r}) = {m.u[x]!r}")
inj = len(set(m.u.values())) == len(m.src.S)
print(f"  shape map injective? {inj}   -> NOT injective: "
      f"{'PASS (counterexample confirmed)' if not inj else 'FAIL'}")
if inj: FAILS.append("5a")
print("  reason: with P(s0) = empty there is exactly ONE function P(s0) -> T (the")
print("          empty one), so const_{t0} = const_{t1}; the choice of t is forgotten.")


# --------------------------------------------------------------- (b) not surjective
print()
print("TASK 5b  a C,D where the SHAPE map is NOT surjective")
C = Cont(frozenset({'s0'}), {'s0': frozenset({'p0', 'p1'})})   # one shape, TWO positions
D = Cont(frozenset({'t0', 't1'}), {'t0': frozenset(), 't1': frozenset()})
m = dirToSeq(C, D)
print(f"  C = one shape s0 with 2 positions p0,p1;  D = two shapes t0,t1")
print(f"  shapes of C (x)_Dir D : {len(m.src.S)}   (= |S|*|T| = 1*2)")
print(f"  shapes of C <| D      : {len(m.tgt.S)}   (= sum_s |T|^|P(s)| = 2^2)")
img = set(m.u.values())
print("  image of the shape map (the CONSTANT functions):")
for x in sorted(img, key=repr):
    s, f = x
    print(f"    (s0, {dict(sorted(f))})")
missed = sorted(set(m.tgt.S) - img, key=repr)
print("  shapes MISSED (the NON-constant functions p0,p1 -> T):")
for x in missed:
    s, f = x
    print(f"    (s0, {dict(sorted(f))})   <-- not in the image")
surj = img == set(m.tgt.S)
print(f"  shape map surjective? {surj}   -> NOT surjective: "
      f"{'PASS (counterexample confirmed)' if not surj else 'FAIL'}")
if surj: FAILS.append("5b")


# ------------------------------------------------------------------ (c) conjecture
print()
print("TASK 5c  CONJECTURE:  dirToSeq_{C,D} is an ISO  <=>  for every shape s of C,")
print("         the constant-map injection  const : T -> T^{P(s)}  is a BIJECTION.")

def const_map_is_bijection(T, Pset):
    """const : T -> T^{Pset},  t |-> const_t.   Bijection?"""
    cod = [hfun(f) for f in funcs(Pset, T)]
    d = {t: hfun({p: t for p in Pset}) for t in T}
    ok, _ = is_bijection(d, T, frozenset(cod))
    return ok

Cs = all_small_containers(2, 2, 's')
Ds = all_small_containers(2, 2, 't')
counterexamples = []
tested = 0
agree = 0
truth_table = {}
for C in Cs:
    for D in Ds:
        m = dirToSeq(C, D)
        iso, why = is_iso(m)
        rhs = all(const_map_is_bijection(D.S, C.P[s]) for s in C.S)
        tested += 1
        if iso == rhs:
            agree += 1
        else:
            counterexamples.append((C, D, iso, rhs, why))
        truth_table[(tuple(sorted(len(C.P[s]) for s in C.S)), len(D.S))] = (iso, rhs)

print(f"  exhaustive over {len(Cs)} x {len(Ds)} = {tested} pairs "
      f"(<=2 shapes, <=2 positions per shape, both sides)")
print(f"  conjecture holds on {agree}/{tested} pairs; counterexamples: "
      f"{len(counterexamples)}")
print(f"  CONJECTURE: {'PASS - no counterexample' if not counterexamples else 'FAIL'}")
for ce in counterexamples[:10]:
    print("    COUNTEREXAMPLE:", ce)
if counterexamples: FAILS.append("5c conjecture")

print()
print("  summary by (position-counts of C, |T|)  ->  (iso?, const bijective for all s?)")
print(f"    {'pos-counts of C':>18} {'|T|':>4} | {'iso?':>5} {'const-bij?':>10}")
for k in sorted(truth_table, key=repr):
    iso, rhs = truth_table[k]
    print(f"    {str(k[0]):>18} {k[1]:>4} | {str(iso):>5} {str(rhs):>10}")

print()
print("  reading of the criterion: const : T -> T^{P(s)} is a bijection iff")
print("    |P(s)| = 1   (then T^{P(s)} = T),  or  |T| <= 1  (then both sides are")
print("    singletons, or both empty when |T|=0 and |P(s)|>=1).")
print("  |P(s)| = 0 with |T| >= 2 kills INJECTIVITY  (Task 5a).")
print("  |P(s)| >= 2 with |T| >= 2 kills SURJECTIVITY (Task 5b).")


# ============================================================== TASK 6
print()
print("=" * 78)
print("TASK 6  C (x)_Dir y^B  =  C <| y^B    (right argument has exactly ONE shape)")

def yB(n):
    """y^B : one shape, B positions."""
    return Cont(frozenset({'*'}), {'*': frozenset(f"b{i}" for i in range(n))})

Cs6 = all_small_containers(2, 3, 's') + all_small_containers(3, 2, 's')
ok6, bad6 = True, []
tested6 = 0
for C in Cs6:
    for n in range(0, 4):
        D = yB(n)
        m = dirToSeq(C, D)
        errs = check_mor_types(m)
        iso, why = is_iso(m)
        tested6 += 1
        if errs or not iso:
            ok6 = False
            bad6.append((C, n, errs[:1], why))
        # extensions must agree in cardinality too
        for k in range(0, 4):
            X = mkset(k)
            if len(extension(dirichlet(C, D), X)) != len(extension(compose(C, D), X)):
                ok6 = False
                bad6.append((C, n, "extension count mismatch", k))
print(f"  tested {tested6} (C, |B|) pairs: C with <=2 shapes/<=3 pos and "
      f"<=3 shapes/<=2 pos; |B| in 0..3")
print(f"  dirToSeq_{{C, y^B}} is an ISOMORPHISM in every case : "
      f"{'PASS' if ok6 else 'FAIL'}")
for b in bad6[:5]: print("    FAIL:", b)
if not ok6: FAILS.append("6")

C = Cont(frozenset({'s0', 's1'}), {'s0': frozenset({'p0', 'p1'}), 's1': frozenset({'q0'})})
D = yB(2)
m = dirToSeq(C, D)
print(f"  worked instance: C = 2 shapes (2 pos, 1 pos), B = 2")
print(f"    shapes of C (x)_Dir y^B : {len(m.src.S)}")
print(f"    shapes of C <| y^B      : {len(m.tgt.S)}   "
      f"(sum_s |T|^|P(s)| = 1^2 + 1^1 = 2)")
for x in sorted(m.src.S, key=repr):
    print(f"    u({x!r}) -> shape with {len(m.tgt.P[m.u[x]])} positions; "
          f"source shape has {len(m.src.P[x])} positions")
print("  reason: |T| = 1, so T^{P(s)} is a singleton for every s -- the const map")
print("  T -> T^{P(s)} is a bijection for EVERY s, and Task 5c's criterion is met.")

print()
print("TASKS 5-6 RESULT:", "PASS" if not FAILS else f"FAIL {FAILS}")
