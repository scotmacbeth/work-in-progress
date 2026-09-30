#!/usr/bin/env python3
"""
Does the CORRECTED AFFINE obstruction reproduce genuine im phi^+ for H=Z/2?

Affine lock (candidate corrected o_nu, H=Z/2):
    [beta] (rep b in Z/order) is realisable with residue nu, circle sigma  iff
        (lam^D_1 - 1) * b  ==  2 * (nu*sigma - 1)   (mod order)
        has a solution b in the additive class [beta] (= b mod 2Z/order).
The kernel of this AFFINE map is a COSET of ker(x |-> (lam^D_1-1)x) in H^2_+,
which need NOT contain [beta]=0 (torsor, no basepoint) when the RHS is odd*2.

We compare, per genuine (nu,sigma), the affine-predicted realisable class against
the genuine im phi^+ from enumeration, for D=Z/4 (lam^D_1=3) and D=Z/8 (lam^D_1=5).
"""
import itertools
from collections import defaultdict
exec(open("scratch/2026-09-29-o-nu-kernel-vs-image.py").read().split("if __name__")[0])

def is_ideal(br, Dset):
    E = br.E
    if any(br.lamap(a, d) not in Dset for a in E.elems for d in Dset): return False
    for a in E.elems:
        ainv = br.circ_inv(a)
        for d in Dset:
            if br.circ(br.circ(a, d), ainv) not in Dset: return False
    return True

def run(order, lamD1, groups, label):
    print("=" * 74); print(label); print("=" * 74)
    genuine = defaultdict(set)      # (nu,sigma) -> set of [beta] (parity 0/1)
    for (E, Dlist, iso, s) in groups:
        Dset = set(Dlist); isoInv = {iso[d]: d for d in Dlist}; gen = isoInv[1]
        hol = Holomorph(E); regs = hol.regular_subgroups()
        for reg in regs:
            lam = {a: i for a, i in reg}; br = Brace(E, hol, lam)
            if not is_ideal(br, Dset): continue
            L = {iso[br.lamap(d, gen)] for d in Dlist}
            if L == {1}: continue                 # want NON-trivial kernel
            s1 = s[1]; s1inv = br.circ_inv(s1)
            nu = iso[br.lamap(s1, gen)]
            sigma = iso[br.circ(br.circ(s1, gen), s1inv)]
            bE = br.E.add(br.E.add(br.E.neg(s[0]), s1), s1)   # beta(1,1)=-s(0)+s1+s1
            b = iso[bE]
            genuine[(nu, sigma)].add(b % 2)       # [beta]=parity
    # affine predictor
    n_match = 0; n_tot = 0
    print(f"  {'(nu,sigma)':<14}{'genuine im[beta]':<20}{'affine-pred im[beta]':<22}match")
    for (nu, sigma) in sorted(genuine):
        n_tot += 1
        rhs = (2 * (nu * sigma - 1)) % order
        pred = set()
        for b in range(order):
            if ((lamD1 - 1) * b) % order == rhs:
                pred.add(b % 2)
        g = genuine[(nu, sigma)]
        m = (pred == g)
        n_match += int(m)
        print(f"  {str((nu,sigma)):<14}{str(sorted(g)):<20}{str(sorted(pred)):<22}"
              f"{'MATCH' if m else 'MISMATCH'}")
    print(f"  => affine predictor reproduces genuine im phi^+ on {n_match}/{n_tot} "
          f"(nu,sigma) triplets")
    return n_match == n_tot

if __name__ == "__main__":
    # D=Z/4 nontrivial (lam^D_1 = 3): additive groups Z/8 (no nontriv kernel) + Z/4xZ/2
    Z8 = Ab([8], "Z/8"); D8 = [(0,), (2,), (4,), (6,)]; iso8 = {(2 * k,): k for k in range(4)}
    s8 = {0: (0,), 1: (1,)}
    Z4Z2 = Ab([4, 2], "Z/4xZ/2"); D42 = [(k, 0) for k in range(4)]; iso42 = {(k, 0): k for k in range(4)}
    s42 = {0: (0, 0), 1: (0, 1)}
    run(4, 3, [(Z8, D8, iso8, s8), (Z4Z2, D42, iso42, s42)], "D=Z/4 nontrivial, H=Z/2  (offset always 0)")

    # D=Z/8 nontrivial (lam^D_1 = 5): additive groups Z/16 + Z/2xZ/8
    Z16 = Ab([16], "Z/16"); D16 = [(2 * k,) for k in range(8)]; iso16 = {(2 * k,): k for k in range(8)}
    s16 = {0: (0,), 1: (1,)}
    Z2Z8 = Ab([2, 8], "Z/2xZ/8"); D28 = [(0, y) for y in range(8)]; iso28 = {(0, y): y for y in range(8)}
    s28 = {0: (0, 0), 1: (1, 0)}
    run(8, 5, [(Z16, D16, iso16, s16), (Z2Z8, D28, iso28, s28)], "D=Z/8 nontrivial, H=Z/2  (offset gives TORSOR)")
