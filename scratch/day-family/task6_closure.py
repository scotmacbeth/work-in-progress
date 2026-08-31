"""
task6 — verify the uniform closure formula for Day tensors.

Claim (left-closed form):   Cont(y^R  ⊙_⋆  p ,  q)  ≅  Π_{i∈S_p} ⟦q⟧(R ⋆ p[i]).
Consequence (necessity witness):  ⟦[y^B, y]_⋆⟧(R) = R ⋆ B.

We check CARDINALITIES elementwise (small sets), for ⋆ ∈ {+, ×, ∨_S}.
"""
from itertools import product as iproduct
from core import (Cont, conv, dunion, cprod, vee, funcs, mkset,
                  count_extension, extension)

def yR(R):
    """representable container y^R : one shape, position set R."""
    return Cont(frozenset({'*'}), {'*': R})

def count_hom(a, b):
    """|Cont(a,b)| = Π_{s∈S_a} ⟦b⟧(a[s]),  computed elementwise (no counting shortcut
       beyond count_extension, itself cross-validated in core.validate_counting)."""
    total = 1
    for s in a.S:
        total *= count_extension(b, a.P[s])   # |⟦b⟧(a[s])|
    return total

def star_plus(A, B):  return dunion(A, B)
def star_times(A, B): return cprod(A, B)
def mk_vee(S):
    def st(A, B): return vee(A, B, S)
    return st

STARS = {
    '+': star_plus,
    '×': star_times,
    '∨_S(|S|=1)': mk_vee(mkset(1, 's')),
    '∨_S(|S|=2)': mk_vee(mkset(2, 's')),
}

def small_containers(max_shapes=2, max_pos=2, tag='p'):
    """enumerate small containers: up to max_shapes shapes, each with 0..max_pos positions."""
    outs = []
    for nsh in range(0, max_shapes + 1):
        shapes = [f"{tag}s{i}" for i in range(nsh)]
        for poscounts in iproduct(range(0, max_pos + 1), repeat=nsh):
            P = {shapes[i]: mkset(poscounts[i], f"{tag}{i}_") for i in range(nsh)}
            outs.append(Cont(frozenset(shapes), P))
    return outs

def main():
    Rsizes = [0, 1, 2, 3]
    ps = small_containers(max_shapes=2, max_pos=2, tag='p')
    qs = small_containers(max_shapes=2, max_pos=2, tag='q')

    total = 0
    fails = 0
    for name, star in STARS.items():
        for R in [mkset(n, 'r') for n in Rsizes]:
            yr = yR(R)
            for p in ps:
                # LHS: |Cont(y^R ⊙_⋆ p, q)|
                tensor = conv(yr, p, star)   # y^R ⊙_⋆ p
                for q in qs:
                    lhs = count_hom(tensor, q)
                    # RHS: Π_{i∈S_p} |⟦q⟧(R ⋆ p[i])|
                    rhs = 1
                    for i in p.S:
                        rhs *= count_extension(q, star(R, p.P[i]))
                    total += 1
                    if lhs != rhs:
                        fails += 1
                        if fails <= 8:
                            print(f"FAIL [{name}] |R|={len(R)} p={p} q={q}: lhs={lhs} rhs={rhs}")
    print(f"\nCLOSURE FORMULA: {total-fails}/{total} pass ({fails} fail)")

    # ---- necessity witness: ⟦[y^B,y]⟧R = R ⋆ B, i.e. |Cont(y^R ⊙_⋆ y^B, y)| = |R ⋆ B|
    yconst = yR(frozenset({'•'}))   # y = y^1
    tot2 = 0; fail2 = 0
    for name, star in STARS.items():
        for R in [mkset(n, 'r') for n in Rsizes]:
            for B in [mkset(n, 'b') for n in Rsizes]:
                lhs = count_hom(conv(yR(R), yR(B), star), yconst)
                rhs = len(star(R, B))
                tot2 += 1
                if lhs != rhs:
                    fail2 += 1
                    if fail2 <= 8:
                        print(f"NEC FAIL [{name}] |R|={len(R)} |B|={len(B)}: {lhs} vs {rhs}")
    print(f"NECESSITY WITNESS ⟦[y^B,y]⟧R = R⋆B: {tot2-fail2}/{tot2} pass ({fail2} fail)")

if __name__ == '__main__':
    main()
