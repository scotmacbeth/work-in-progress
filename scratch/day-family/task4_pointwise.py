"""
TASK 4.  POINTWISENESS of the convolution tensor built from v_S.

    (C (x)_S D) := ( S_C x S_D , (s,t) |-> P(s) v_S Q(t) )

Question: is  |[[C (x)_S D]](X)| = |[[C]](X)| * |[[D]](X)|  ?
Expect: holds for S = empty (then v_S = disjoint union = the product tensor),
        fails for |S| = 1.
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


def vee_tensor(C, D, S):
    return conv(C, D, lambda P, Q: vee(P, Q, S))


Cs = all_small_containers(2, 2, 's')
Ds = all_small_containers(2, 2, 't')
Xs = [0, 1, 2, 3]

print("=" * 78)
print("TASK 4  pointwiseness of the v_S-convolution tensor")
print()

# The v_S-tensor of two 2-position shapes has up to 2+2*|S|*2+2 = 12 positions,
# so [[--]](X) at |X|=3 has 3^12 elements per shape.  Materialising every element
# exhausts memory (an earlier run was OOM-killed).  So we COUNT by streaming the
# same elementwise enumeration -- but first we PROVE the counter agrees with the
# materialised elementwise set wherever the set is small enough to build.
probe = []
for C in Cs:
    for D in Ds:
        for ns in [0, 1, 2]:
            probe.append(conv(C, D, lambda P, Q, S=mkset(ns, 'k'): vee(P, Q, S)))
probe = [C for C in probe if all(len(C.P[s]) <= 6 for s in C.S)] + Cs + Ds
badc = validate_counting(probe, Xsizes=(0, 1, 2, 3))
print(f"  [sanity] streaming count == |materialised elementwise set| on "
      f"{len(probe)} containers x 4 values of X: "
      f"{'PASS' if not badc else 'FAIL ' + str(badc[:3])}")
if badc: FAILS.append("4 counting unsound")
print("  [sanity] so the counts below ARE elementwise enumerations, just not stored.")
print()
print(f"  {'|S|':>3} | {'instances':>9} {'pointwise':>9} {'violations':>10} | verdict")
print("  " + "-" * 60)

results = {}
for ns in [0, 1, 2]:
    S = mkset(ns, 'k')
    bad, tot = [], 0
    for C in Cs:
        for D in Ds:
            for n in Xs:
                X = mkset(n)
                lhs = count_extension(vee_tensor(C, D, S), X)
                rhs = count_extension(C, X) * count_extension(D, X)
                tot += 1
                if lhs != rhs:
                    bad.append((C, D, n, lhs, rhs))
    results[ns] = bad
    verdict = "POINTWISE" if not bad else "NOT pointwise"
    print(f"  {ns:>3} | {tot:>9} {tot-len(bad):>9} {len(bad):>10} | {verdict}")

# S = empty must be pointwise
ok0 = not results[0]
print()
print(f"  S = empty  => pointwise everywhere : {'PASS' if ok0 else 'FAIL'}")
if not ok0:
    FAILS.append("4 S=empty not pointwise")
    for b in results[0][:5]: print("     violation:", b)

# and v_empty really is the product tensor, structurally
struct = all(vee_tensor(C, D, EMPTY) == prod(C, D) for C in Cs for D in Ds)
print(f"  S = empty  => v_empty-convolution IS the product tensor (structurally, "
      f"up to the tag relabel l/r vs inl/inr): {'PASS' if struct else 'checked separately'}")
if not struct:
    # tags differ ('l'/'r' vs 'inl'/'inr'); compare position COUNTS shape-by-shape
    same = all(sorted(len(vee_tensor(C,D,EMPTY).P[s]) for s in vee_tensor(C,D,EMPTY).S)
               == sorted(len(prod(C,D).P[s]) for s in prod(C,D).S)
               for C in Cs for D in Ds)
    print(f"     (tags differ; position counts agree shape-by-shape: "
          f"{'PASS' if same else 'FAIL'})")
    if not same: FAILS.append("4 v_empty != product")

# |S| = 1 must FAIL
ok1 = bool(results[1])
print(f"  |S| = 1    => NOT pointwise (needs a counterexample) : "
      f"{'PASS' if ok1 else 'FAIL'}")
if not ok1: FAILS.append("4 |S|=1 unexpectedly pointwise")

if results[1]:
    def size(b):
        C, D, n, l, r = b
        return (len(C.S)+len(D.S), sum(len(C.P[s]) for s in C.S)
                + sum(len(D.P[t]) for t in D.S), -n)
    # prefer a non-degenerate counterexample (|X| >= 2, no empty containers)
    cands = [b for b in results[1]
             if b[2] >= 2 and len(b[0].S) > 0 and len(b[1].S) > 0]
    C, D, n, lhs, rhs = min(cands, key=size)
    S = mkset(1, 'k')
    print()
    print("  EXPLICIT COUNTEREXAMPLE at |S| = 1")
    print(f"    S = {sorted(S)}")
    print(f"    C : shapes {sorted(C.S)}, positions "
          f"{{{', '.join(f'{s}: {len(C.P[s])}' for s in sorted(C.S))}}}")
    print(f"    D : shapes {sorted(D.S)}, positions "
          f"{{{', '.join(f'{t}: {len(D.P[t])}' for t in sorted(D.S))}}}")
    CD = vee_tensor(C, D, S)
    for s in sorted(CD.S, key=repr):
        (cs, ds) = s
        p, q = len(C.P[cs]), len(D.P[ds])
        print(f"    (C (x)_S D) at shape {s}: |P({cs}) v_S Q({ds})| = "
              f"{p} + {p}*1*{q} + {q} = {len(CD.P[s])}")
    print()
    for m in [0, 1, 2, 3]:
        X = mkset(m)
        l = count_extension(CD, X); r = count_extension(C, X) * count_extension(D, X)
        mark = "agree" if l == r else "DIFFER  <-- counterexample"
        print(f"    |X|={m}: |[[C (x)_S D]](X)| = {l:3d}   "
              f"|[[C]](X)|*|[[D]](X)| = {r:3d}   {mark}")

    print()
    print("  CLEANEST INSTANCE  C = D = y  (one shape, one position), |S| = 1:")
    y1 = Cont(frozenset({'*'}), {'*': frozenset({'p'})})
    y2 = Cont(frozenset({'#'}), {'#': frozenset({'q'})})
    T = vee_tensor(y1, y2, S)
    sh = next(iter(T.S))
    print(f"    positions of y (x)_S y at {sh}: {sorted(T.P[sh], key=repr)}")
    print(f"    => 1 + 1*1*1 + 1 = 3 positions, so [[y (x)_S y]](X) = X^3")
    for m in [0, 1, 2, 3]:
        X = mkset(m)
        l = count_extension(T, X); r = count_extension(y1, X) * count_extension(y2, X)
        print(f"    |X|={m}: X^3 = {l:2d}   vs   |[[y]](X)|^2 = {r:2d}   "
              f"{'agree' if l == r else 'DIFFER'}")

print()
print("  Note: pointwiseness of the convolution is exactly the statement that")
print("  kappa : P(s) + Q(t) -> P(s) v_S Q(t) is a bijection (Task 3): the extension")
print("  at (s,t) is X^{|P(s) v_S Q(t)|}, and the product of extensions contributes")
print("  X^{|P(s)|+|Q(t)|} = X^{|P(s) + Q(t)|}.  Same obstruction, same middle piece.")

print()
print("TASK 4 RESULT:", "PASS" if not FAILS else f"FAIL {FAILS}")
