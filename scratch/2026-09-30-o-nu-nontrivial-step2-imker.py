#!/usr/bin/env python3
"""
STEP 2: is  im phi^+ == ker o_nu  still TRUE for a NON-TRIVIAL kernel?

We reuse the trivial-case abstract machinery (abstract_kernel) VERBATIM -- i.e.
the operators P,Q and the multiplicative complex Z^2_o taken over (D,+) -- and
compare, per genuine good triplet (nu,sigma), the abstractly computed ker o_nu
against the genuine im phi^+ (regular-subgroup enumeration).  The ONLY change from
2026-09-29-o-nu-kernel-vs-image.py is the kernel filter: keep braces whose
sub-brace on D is NON-TRIVIAL (instead of trivial).

Kernel: D = Z/4 nontrivial (L={1,3}).  This directly tests whether the theorem
'im phi^+ = ker o_nu' survives the non-triviality of D with the *unchanged*
operators, and -- since (D,o) != (D,+) -- whether using + for the multiplicative
complex (the point where the proof used triviality) still gives the right answer.
"""
import itertools
from collections import defaultdict
exec(open("scratch/2026-09-29-o-nu-kernel-vs-image.py").read().split("if __name__")[0])

def genuine_realised_nt(Dabs, Helems, zeroH, additive_groups, bkey_of):
    """Same as genuine_realised but keeps NON-trivial-brace kernels."""
    out = defaultdict(set)
    for (E, Dset_list, s, quotient, isoD) in additive_groups:
        Dset = set(Dset_list)
        isoInv = {isoD[d]: d for d in Dset_list}
        hol = Holomorph(E); regs = hol.regular_subgroups()
        for reg in regs:
            lam = {a: i for (a, i) in reg}; br = Brace(E, hol, lam)
            if any(br.lamap(a, d) not in Dset for a in E.elems for d in Dset):
                continue
            ok = True
            for a in E.elems:
                ainv = br.circ_inv(a)
                for d in Dset:
                    if br.circ(br.circ(a, d), ainv) not in Dset:
                        ok = False; break
                if not ok: break
            if not ok: continue
            # KEEP only NON-trivial sub-brace on D
            if all(br.lamap(d, e) == e for d in Dset for e in Dset):
                continue
            nu0 = {}; sigma0 = {}
            for h in Helems:
                sh = s[h]; shinv = br.circ_inv(sh)
                nu0[h] = {dp: isoD[br.lamap(sh, isoInv[dp])] for dp in Dabs.elems}
                sigma0[h] = {dp: isoD[br.circ(br.circ(sh, isoInv[dp]), shinv)] for dp in Dabs.elems}
            def Hplus(h1, h2): return quotient(E.add(s[h1], s[h2]))
            beta0 = {}
            for h1 in Helems:
                for h2 in Helems:
                    if h1 == zeroH or h2 == zeroH: continue
                    bE = E.add(E.add(E.neg(s[Hplus(h1, h2)]), s[h1]), s[h2])
                    beta0[(h1, h2)] = isoD[bE]
            for phi in Dabs.autos():
                phinv = {v: k for k, v in phi.items()}
                nu = {}; sigma = {}
                for h in Helems:
                    nu[h] = tuple(sorted({dp: phi[nu0[h][phinv[dp]]] for dp in Dabs.elems}.items()))
                    sigma[h] = tuple(sorted({dp: phi[sigma0[h][phinv[dp]]] for dp in Dabs.elems}.items()))
                beta = {k: phi[v] for k, v in beta0.items()}
                tkey = (tuple(sorted(nu.items())), tuple(sorted(sigma.items())))
                out[tkey].add(bkey_of(beta))
    return out

def run_nt(Dmods, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam, additive_groups, label):
    print("=" * 74); print("CASE", label); print("=" * 74)
    D = Ab(Dmods, "D")
    mu_triv = {h: {d: d for d in D.elems} for h in Helems}
    add_coh = Coh(D, Helems, Hplus, mu_triv, zeroH)
    def bkey_of(beta):
        f = {(h1, h2): beta[(h1, h2)] for h1 in Helems for h2 in Helems
             if h1 != zeroH and h2 != zeroH}
        B = [add_coh.d1(theta) for theta in add_coh.all_1cochains()]
        orbit = [tuple(sorted(add2(D, f, b).items())) for b in B]
        return min(orbit)
    genuine = genuine_realised_nt(D, Helems, zeroH, additive_groups, bkey_of)
    if not genuine:
        print("  (no genuine non-trivial-kernel braces found)"); return True
    n_match = 0; n_tot = 0
    for tkey, realset in sorted(genuine.items()):
        nu_items, sig_items = tkey
        nu = {}; sigma = {}
        for h, items in nu_items: nu[h] = {d: v for d, v in items}
        for h, items in sig_items: sigma[h] = {d: v for d, v in items}
        mu_triv2 = {h: {d: d for d in D.elems} for h in Helems}
        n_tot += 1
        gen0 = D.elems[1]
        try:
            cosets, ker, bk = abstract_kernel(D, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam,
                                              mu_triv2, sigma, nu)
        except AssertionError as e:
            print(f"  nu(gen)={{h:nu[h][gen0] for h in Helems if h!=zeroH}} "
                  f"sigma(gen)={ {h:sigma[h][gen0] for h in Helems if h!=zeroH} }: "
                  f"abstract o_nu^+ ILL-DEFINED over (D,+):  {e}   genuine|im|={len(realset)}")
            continue
        match = (ker == realset)
        n_match += int(match)
        gen = D.elems[1]
        nu_desc = {h: nu[h][gen] for h in Helems if h != zeroH}
        sig_desc = {h: sigma[h][gen] for h in Helems if h != zeroH}
        print(f"  nu(gen)={nu_desc} sigma(gen)={sig_desc}: "
              f"|H^2_+|={len(cosets)}  genuine|im|={len(realset)}  ker|o_nu^+|={len(ker)}  "
              f"{'MATCH' if match else '*** MISMATCH ***'}")
        if not match:
            print("     genuine im:", sorted(realset))
            print("     ker o_nu^+:", sorted(ker))
    print(f"  => o_nu^+ (verbatim trivial-case operators): {n_match}/{n_tot} triplets match")
    return n_match == n_tot

if __name__ == "__main__":
    # H=Z/2, D=Z/4 nontrivial
    Hp = lambda a, b: (a + b) % 2; Hc = Hp; Hn = lambda a: (-a) % 2; Hl = lambda a, b: b
    Z8 = Ab([8], "Z/8"); D8 = [(0,), (2,), (4,), (6,)]; s8 = {0: (0,), 1: (1,)}; q8 = lambda x: x[0] % 2
    iso8 = {(2 * k,): (k,) for k in range(4)}
    Z4Z2 = Ab([4, 2], "Z/4xZ/2"); D42 = [(k, 0) for k in range(4)]; s42 = {0: (0, 0), 1: (0, 1)}
    q42 = lambda x: x[1] % 2; iso42 = {(k, 0): (k,) for k in range(4)}
    ag2 = [(Z8, D8, s8, q8, iso8), (Z4Z2, D42, s42, q42, iso42)]
    run_nt([4], [0, 1], 0, Hp, Hc, Hn, Hl, ag2, "H=Z/2, D=Z/4 nontrivial (o_nu^+ verbatim)")

    # H=Z/3, D=Z/4 nontrivial
    Hp3 = lambda a, b: (a + b) % 3; Hc3 = Hp3; Hn3 = lambda a: (-a) % 3; Hl3 = lambda a, b: b
    Z12 = Ab([12], "Z/12"); D12 = [(3 * k,) for k in range(4)]; s12 = {0: (0,), 1: (1,), 2: (2,)}
    q12 = lambda x: x[0] % 3; iso12 = {(3 * k,): (k,) for k in range(4)}
    ag3 = [(Z12, D12, s12, q12, iso12)]
    run_nt([4], [0, 1, 2], 0, Hp3, Hc3, Hn3, Hl3, ag3, "H=Z/3, D=Z/4 nontrivial (o_nu^+ verbatim)")

# ---- appended: D = Z/8 nontrivial (L={1,5}), the torsor witness, same o_nu^+ ----
def run_z8():
    Hp = lambda a, b: (a + b) % 2; Hc = Hp; Hn = lambda a: (-a) % 2; Hl = lambda a, b: b
    Z16 = Ab([16], "Z/16"); D16 = [(2 * k,) for k in range(8)]; s16 = {0: (0,), 1: (1,)}
    q16 = lambda x: x[0] % 2; iso16 = {(2 * k,): (k,) for k in range(8)}
    Z2Z8 = Ab([2, 8], "Z/2xZ/8"); D28 = [(0, y) for y in range(8)]; s28 = {0: (0, 0), 1: (1, 0)}
    q28 = lambda x: x[0] % 2; iso28 = {(0, y): (y,) for y in range(8)}
    ag = [(Z16, D16, s16, q16, iso16), (Z2Z8, D28, s28, q28, iso28)]
    # restrict genuine filter further to L={1,5} by post-check inside run_nt? run_nt keeps
    # ALL nontrivial kernels; on Z/8 the only nontrivial sub-brace is L={1,5}, so fine.
    run_nt([8], [0, 1], 0, Hp, Hc, Hn, Hl, ag, "H=Z/2, D=Z/8 nontrivial L={1,5} (o_nu^+ verbatim, TORSOR witness)")

run_z8()
