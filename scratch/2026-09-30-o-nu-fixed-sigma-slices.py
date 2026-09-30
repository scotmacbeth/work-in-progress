#!/usr/bin/env python3
"""
FIXED-sigma SLICES of the residue-dependent solvability obstruction o_nu.

This is a PRESENTATION (verification) of the already-PROVED result
    o_nu : H^2_+ -> C^3 / A(Z^2_o(sigma)),   o_nu([beta]) = [Q beta],
    im phi^+ = ker o_nu
(proofs/2026-09-29-solvability-obstruction-o-nu.tex, Theorem 1), sliced by the
circle action sigma.  For Rick's two read-points:

  (a) ADDITIVITY of o_nu|_sigma and that it KILLS B^2_+ (coboundaries), per slice.
  (b) the TORSOR statement: nontrivial kernel => o_nu affine => im phi^+ a torsor,
      no basepoint when nu*sigma !≡ 1 (mod 4).

For the TRIVIAL-brace kernels (|G|=8: H=Z/2,D=Z/4 ; |G|=9: H=Z/3,D=Z/3) we compute
o_nu|_sigma abstractly (RY regime) and verify additivity + B^2-killing + ker/basepoint.
For the NON-trivial-brace kernel (|G|=16: D=Z/8, L={1,5}, H=Z/2) the RY complex does
not directly apply; we slice the GENUINE order-16 enumeration by sigma and read off the
affine three-way lock 4b ≡ 2(nu*sigma-1) (mod 8) and the basepoint dichotomy.

Reuses machinery from the four 09-29 scripts.
Grade: tables = COMPUTED (verification); underlying theorem = PROVED.
"""
import itertools
from collections import defaultdict

# ---- import shared machinery (Ab, Holomorph, Brace, is_ideal, etc.) ----------
exec(open("scratch/2026-09-29-o-nu-operator-check.py").read().split("if __name__")[0])
# ---- import abstract cochain machinery (Coh, make_PQ, add2, neg2, key3) -------
_kvi = open("scratch/2026-09-29-o-nu-kernel-vs-image.py").read().split("# ======")[0]
# strip the duplicate Ab/Holomorph/Brace definitions already provided above:
# we only need Coh, make_PQ, add2, neg2, key3 from it.  Executing the whole prefix
# is harmless (it just redefines identical classes), so exec it in this namespace.
exec(_kvi)

# ------------------------------------------------------------------------------
def autodict_mul(D, k):
    """the automorphism  x |-> k*x  of a cyclic D, as a dict on D.elems."""
    return {a: D.smul(k, a) for a in D.elems}

def unit_of_auto_on_cyclic(D, autod):
    """for cyclic D=Z/n, recover the unit k with autod = (x|->k x)."""
    gen = D.elems[1]                    # generator (1,)
    img = autod[gen]
    return img[0] % D.mods[0]

# ------------------------------------------------------------------------------
def slice_abstract(Dmods, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam, sigma_units,
                   nu_units, label):
    """Trivial-kernel abstract slice.
       For each sigma unit (fixed-sigma slice) and each nu unit, build o_nu and:
        (i)  ADDITIVITY: o_nu(b1+b2) == o_nu(b1)+o_nu(b2)  mod A, over all pairs in Z^2_+
        (ii) B^2-KILLING: o_nu(d_+ theta) == 0, over all additive coboundaries
        (iii) ker o_nu, basepoint present (0-class in ker?), and the closed-form
              |G|=8 condition (1+nu) b in 2 D^sigma  (checked when H=Z/2).
    """
    print("="*74)
    print("SLICE FAMILY:", label)
    print("="*74)
    D = Ab(Dmods, "D")
    mu_triv = {h: {d: d for d in D.elems} for h in Helems}
    add_coh = Coh(D, Helems, Hplus, mu_triv, zeroH)     # additive complex (mu triv)

    # additive 2-cocycles and coboundaries (sigma-independent domain)
    Z2p = [f for f in add_coh.all_2cochains() if add_coh.is_zero3(add_coh.d2(f))]
    B2p_keys = set()
    thetas = list(add_coh.all_1cochains())
    for th in thetas:
        B2p_keys.add(tuple(sorted(add_coh.d1(th).items())))
    # H^2_+ cosets
    def bkey(f): return tuple(sorted(f.items()))
    cosets = {}
    for f in Z2p:
        orbit = [bkey(add2(D, f, dict(bk))) for bk in B2p_keys]
        cosets.setdefault(min(orbit), []).append(f)
    zero_rep = min(bkey(add2(D, {k: D.zero for k in Z2p[0]}, dict(bk))) for bk in B2p_keys)
    print(f"  |Z^2_+|={len(Z2p)}  |B^2_+|={len(B2p_keys)}  |H^2_+|={len(cosets)} "
          f"(sigma-independent domain; mu trivial)")

    for su in sigma_units:
        sigma = {h: autodict_mul(D, su if h != zeroH else 1) for h in Helems}
        # multiplicative complex with this sigma; A(Z^2_o(sigma)) as C^3-subgroup
        mul_coh = Coh(D, Helems, Hcirc, sigma, zeroH)
        Z2o = [f for f in mul_coh.all_2cochains() if mul_coh.is_zero3(mul_coh.d2(f))]
        print(f"\n  --- fixed sigma = x{su}  (|Z^2_o(sigma)|={len(Z2o)}) ---")
        for nuu in nu_units:
            nu = {h: autodict_mul(D, nuu if h != zeroH else 1) for h in Helems}
            P, Q = make_PQ(D, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam, nu)
            def T(taubar):
                return {(h1, h2): nu[Hcirc(h1, h2)][taubar[(h1, h2)]] for (h1, h2) in taubar}
            A = set(key3(P(T(f))) for f in Z2o)      # A(Z^2_o(sigma)) <= C^3

            # (i) ADDITIVITY over all pairs in Z^2_+ (mod A)
            add_pass = add_tot = 0
            for b1 in Z2p:
                for b2 in Z2p:
                    add_tot += 1
                    lhs = Q(add2(D, b1, b2))
                    rhs = add2(D, Q(b1), Q(b2))
                    # equal mod A  <=>  lhs - rhs in A
                    diff = add2(D, lhs, neg2(D, rhs))
                    if key3(diff) in A:
                        add_pass += 1

            # (ii) B^2-KILLING over all coboundaries d_+ theta
            b2_pass = b2_tot = 0
            for th in thetas:
                b2_tot += 1
                if key3(Q(add_coh.d1(th))) in A:
                    b2_pass += 1

            # (iii) kernel + basepoint
            ker = set()
            for rep, fs in cosets.items():
                if key3(Q(fs[0])) in A:
                    ker.add(rep)
            basepoint = zero_rep in ker

            # closed-form |G|=8 condition (1+nu) b in 2 D^sigma  (H=Z/2 only)
            cf = ""
            if len(Helems) == 2:
                Dsig = [d for d in D.elems if sigma[1][d] == d]
                twoDsig = set(D.smul(2, d) for d in Dsig)
                # ker via closed form
                cf_ker = set()
                for rep, fs in cosets.items():
                    b = fs[0][(1, 1)]
                    if D.add(b, D.smul(nuu, b)) in twoDsig:   # (1+nu) b
                        cf_ker.add(rep)
                cf = "  closed-form (1+nu)b∈2D^σ ker " + ("MATCHES" if cf_ker == ker else "*** MISMATCH ***")

            print(f"    nu=x{nuu}: additivity {add_pass}/{add_tot} | "
                  f"B^2-killing {b2_pass}/{b2_tot} | |ker|={len(ker)}/{len(cosets)} | "
                  f"basepoint {'PRESENT' if basepoint else 'ABSENT'}{cf}")

# ------------------------------------------------------------------------------
def slice_G16():
    """Non-trivial-brace kernel D=Z/8 (L={1,5}), H=Z/2, |G|=16.
       Slice the GENUINE enumeration by sigma; report per (sigma,nu): realizable b,
       [beta], affine RHS c=2(nu*sigma-1) mod 8, basepoint present iff b=0 realizable
       iff nu*sigma ≡ 1 (mod 4).  o_nu is AFFINE, not linear.
    """
    print("="*74)
    print("SLICE FAMILY: |G|=16  D=Z/8 (L={1,5}) nontrivial kernel, H=Z/2  (AFFINE)")
    print("="*74)

    def enum(E, Dset_list, s, iso_to_Z8):
        hol = Holomorph(E); regs = hol.regular_subgroups()
        Dset = set(Dset_list); isoInv = {iso_to_Z8[d]: d for d in Dset_list}
        rows = []
        for reg in regs:
            lam = {a: i for (a, i) in reg}; br = Brace(E, hol, lam)
            if not is_ideal(br, Dset): continue
            gen = isoInv[1]
            Lset = set()
            for d in Dset_list:
                Lset.add(iso_to_Z8[br.lamap(d, gen)] % 8)
            if Lset != {1, 5}: continue
            s1, s0 = s[1], s[0]
            nu = iso_to_Z8[br.lamap(s1, gen)]
            s1inv = br.circ_inv(s1)
            sigma = iso_to_Z8[br.circ(br.circ(s1, gen), s1inv)]
            bE = E.add(E.add(E.neg(s0), s1), s1)
            b = iso_to_Z8[bE]
            rows.append((b, nu, sigma))
        return rows

    Z16 = Ab([16], "Z/16"); D16 = [(2*k,) for k in range(8)]
    s16 = {0: (0,), 1: (1,)}; iso16 = {(2*k,): k for k in range(8)}
    Z2Z8 = Ab([2, 8], "Z/2xZ/8"); D28 = [(0, y) for y in range(8)]
    s28 = {0: (0, 0), 1: (1, 0)}; iso28 = {(0, y): y for y in range(8)}

    rows = enum(Z16, D16, s16, iso16) + enum(Z2Z8, D28, s28, iso28)
    # group by sigma
    by_sigma = defaultdict(list)
    for (b, nu, sigma) in rows:
        by_sigma[sigma].append((nu, b))

    print("  Genuine order-16 braces with this kernel:", len(rows))
    all_ok = True
    for sigma in sorted(by_sigma):
        print(f"\n  --- fixed sigma = x{sigma} ---")
        # collect per nu
        seen = defaultdict(set)
        for (nu, b) in by_sigma[sigma]:
            seen[nu].add(b)
        for nu in sorted(seen):
            bs = sorted(seen[nu])
            c = (2*((nu*sigma) - 1)) % 8                 # affine offset
            # verify affine lock 4b ≡ c for every realized b
            lock_ok = all((4*b) % 8 == c for b in bs)
            basepoint = 0 in bs                          # split additive class realizable?
            predicted = (nu*sigma) % 4 == 1              # nu*sigma ≡ 1 (mod 4)
            dichotomy_ok = (basepoint == predicted)
            all_ok &= lock_ok and dichotomy_ok
            beta_kind = "[β]=0" if all(b % 2 == 0 for b in bs) else "[β]≠0"
            print(f"    nu=x{nu}: realizable b={bs} {beta_kind} | "
                  f"affine c=2(νσ-1)={c}  4b≡c {'OK' if lock_ok else 'FAIL'} | "
                  f"νσ mod4={(nu*sigma)%4} | basepoint {'PRESENT' if basepoint else 'ABSENT'} "
                  f"(pred {'PRESENT' if predicted else 'ABSENT'}) "
                  f"{'✓' if dichotomy_ok else '*** MISMATCH ***'}")
    print(f"\n  |G|=16 affine-lock + basepoint-dichotomy across all sigma:",
          "PASS" if all_ok else "FAIL")
    return all_ok

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # H=Z/2 base brace is trivial (Hcirc=Hplus, Hlam trivial)
    Hp = lambda a, b: (a+b) % 2; Hc = Hp; Hn = lambda a: (-a) % 2; Hl = lambda a, b: b
    # D=Z/4: Aut={1,3}; involutions (sigma anti-hom, nu hom, order-2 H): {1,3}
    slice_abstract([4], [0, 1], 0, Hp, Hc, Hn, Hl,
                   sigma_units=[1, 3], nu_units=[1, 3],
                   label="|G|=8: H=Z/2, D=Z/4 (trivial kernel, RY)")

    # H=Z/3 base brace trivial
    Hp3 = lambda a, b: (a+b) % 3; Hc3 = Hp3; Hn3 = lambda a: (-a) % 3; Hl3 = lambda a, b: b
    # D=Z/3: Aut={1,2}; for H=Z/3, sigma anti-hom needs sigma_1^3=id -> any unit (order|2)
    #        nu hom needs nu_1^3=id -> unit of mult-order dividing 3 in (Z/3)^*={1,2}: only 1.
    # We slice over all sigma in {1,2} and nu in {1} (the honest admissible set).
    slice_abstract([3], [0, 1, 2], 0, Hp3, Hc3, Hn3, Hl3,
                   sigma_units=[1, 2], nu_units=[1],
                   label="|G|=9: H=Z/3, D=Z/3 (trivial kernel, RY)")

    # |G|=16 non-trivial kernel
    slice_G16()
