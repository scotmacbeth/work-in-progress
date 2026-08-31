"""
GRADED biKleisli test (PROVE 2026-07-31, Atkey index-degree).

Hypothesis: for BRANCHING M, restricting the effect-coeffect arrows to
UNIFORM-leaf-count arrows (grade = #leaves of f0(s), constant in s) RESTORES
associativity of >>>. If so, Arr_M is a (N,x)-GRADED Freyd category for all M;
the Boolean non-associativity is the shadow of mixing grades.

grade(f) = k  iff  len(M.leaves(f.fwd[s])) == k  for every source shape s.
Composition should multiply grades: grade(g.f) = grade(f)*grade(g).
"""
from entwine import (Cont, Mor, ident, compose, eq, Maybe, Pf, Writer,
                     G_obj, T_obj)
from bikleisli import (bik_id, bik_comp, enum_mors, welltyped, LAX, lax_Pf)
from itertools import product as iproduct

def grade(M, f):
    """Return k if f is uniform-k (len leaves constant over source shapes), else None."""
    ks = set(len(M.leaves(f.fwd[s])) for s in f.src.S)
    return next(iter(ks)) if len(ks) == 1 else None

def enum_uniform(M, p, q):
    """arrows Gp->Tq grouped by grade; only uniform ones kept."""
    Gp, Tq = G_obj(M, p), T_obj(M, q)
    byk = {}
    for m in enum_mors(Gp, Tq):
        k = grade(M, m)
        if k is not None:
            byk.setdefault(k, []).append(m)
    return byk

def test_uniform_assoc(M, objs, cap=None, verbose=True):
    lax = LAX[M.name]
    p, q, r, z = objs
    Fk = enum_uniform(M, p, q)
    Gk = enum_uniform(M, q, r)
    Hk = enum_uniform(M, r, z)
    if verbose:
        print(f"  grades p~>q: {[(k,len(v)) for k,v in sorted(Fk.items())]}")
        print(f"  grades q~>r: {[(k,len(v)) for k,v in sorted(Gk.items())]}")
        print(f"  grades r~>z: {[(k,len(v)) for k,v in sorted(Hk.items())]}")
    viol = 0; tested = 0; gradebad = 0; first = None
    Fs = [f for v in Fk.values() for f in (v[:cap] if cap else v)]
    Gs = [g for v in Gk.values() for g in (v[:cap] if cap else v)]
    Hs = [h for v in Hk.values() for h in (v[:cap] if cap else v)]
    for f in Fs:
        gf_grade = grade(M, f)
        for g in Gs:
            gf = bik_comp(M, lax, f, g, p, q, r)     # G p -> T r
            # grade multiplicativity check
            ggf = grade(M, gf); expect = gf_grade*grade(M,g)
            if ggf != expect: gradebad += 1
            for h in Hs:
                hg = bik_comp(M, lax, g, h, q, r, z)  # G q -> T z
                left  = bik_comp(M, lax, gf, h, p, r, z)  # (h.g).f
                right = bik_comp(M, lax, f, hg, p, q, z)  # h.(g.f)
                tested += 1
                if not eq(left, right):
                    viol += 1
                    if first is None: first = (f,g,h,left,right)
    if verbose:
        print(f"  UNIFORM triples tested: {tested}, associativity violations: {viol}")
        print(f"  grade-multiplicativity violations (grade(g.f)!=grade(f)*grade(g)): {gradebad}")
        if first:
            f,g,h,left,right = first
            print("  FIRST UNIFORM VIOLATION:")
            print(f"    f fwd={f.fwd} (grade {grade(M,f)})")
            print(f"    g fwd={g.fwd} (grade {grade(M,g)})")
            print(f"    h fwd={h.fwd} (grade {grade(M,h)})")
    return viol, tested, gradebad

# containers
U  = Cont(['0'], {'0': ['0']})
A1 = Cont(['a', 'b'], {'a': [0, 1], 'b': [0]})
A3 = Cont(['a', 'b'], {'a': [0, 1], 'b': [0, 1]})

if __name__ == "__main__":
    print("="*70); print("GRADED (uniform-leaf) associativity test")
    print("="*70)
    for name, M in [("Pf", Pf())]:
        print(f"\n### M = {name}, objects all A1")
        test_uniform_assoc(M, (A1, A1, A1, A1))
        print(f"\n### M = {name}, objects all A3 (both shapes branch)")
        test_uniform_assoc(M, (A3, A3, A3, A3))
        print(f"\n### M = {name}, objects p=r=U,q=z=A1 (matches bikleisli.py report)")
        test_uniform_assoc(M, (U, A1, U, A1))
