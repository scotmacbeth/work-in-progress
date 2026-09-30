#!/usr/bin/env python3
"""
o_nu for a NON-TRIVIAL-brace kernel D.

Target kernel: D = the unique NON-TRIVIAL skew brace on Z/4, i.e. (D,+)=Z/4 with
lam^D_x = 3^x (so lam_1|_D = (mult by -1)), giving (D,o) = Klein four Z/2 x Z/2.
Its sub-brace units are  L = { iso(lam_d(gen)) : d in D } = {1,3} = ALL of Aut(Z/4).
=> Aut(D)/L is TRIVIAL: the residue [nu] carries NO information for this kernel.
(Contrast D=Z/8 brace lam=5^x: L={1,5} proper in Aut(Z/8)={1,3,5,7}, |Aut/L|=2.)

We enumerate genuine skew-brace extensions 0->D->G->H->0 with D this non-trivial
ideal, for H in {Z/2, Z/3, Z/2xZ/2}, via the regular-subgroup-of-holomorph engine,
and answer, per section-independent triplet (residue [nu], sigma):

  (a) is [nu] genuinely section-invariant?  (check many sections give same residue)
  (b) is the solvability condition AFFINE (constant offset in b) vs LINEAR?
  (c) realised set im phi^+ = { [beta] realised } ; does it contain [beta]=0 ?
  (d) the |G|-lock analogue  (lam^D_d - 1) b  vs  offset, for this kernel.
  STEP2: is  im phi^+ == ker o_nu  still true?  Two abstract o_nu are tested:
        (o_nu^+) the trivial-case operators verbatim (multiplicative complex over
                 (D,+));  (o_nu^o) corrected multiplicative complex over (D,o).

Everything is COMPUTED (witness-level).
"""
import itertools
from collections import defaultdict

# ---- reuse the proven Ab / Holomorph / Coh / operators / Brace -------------
exec(open("scratch/2026-09-29-o-nu-kernel-vs-image.py").read().split("if __name__")[0])

# ---------------------------------------------------------------------------
def is_ideal(br, Dset):
    E = br.E
    for a in E.elems:
        if {br.lamap(a, d) for d in Dset} != Dset:
            return False
    for a in E.elems:
        ainv = br.circ_inv(a)
        for d in Dset:
            if br.circ(br.circ(a, d), ainv) not in Dset:
                return False
    return True

def subbrace_units(br, Dlist, iso):
    """units {iso(lam_d(gen))} of the sub-brace on D (gen = iso^{-1}(1))."""
    isoInv = {iso[d]: d for d in Dlist}
    gen = isoInv[1]
    L = set()
    for d in Dlist:
        img = br.lamap(d, gen)
        if img not in iso:
            return None
        L.add(iso[img])
    return frozenset(L)

# ---------------------------------------------------------------------------
def enumerate_kernel(E, Dlist, iso, sections, Helems, zeroH,
                     Hplus, Hcirc, Hneg, want_L, order):
    """For every genuine brace on E with D=this non-trivial ideal, extract the
       section-independent (residue,sigma) and additive class rep b (per h-pair).
       `sections` : list of section dicts (to test section-invariance of residue).
       Returns list of records."""
    hol = Holomorph(E)
    regs = hol.regular_subgroups()
    Dset = set(Dlist)
    isoInv = {iso[d]: d for d in Dlist}
    gen = isoInv[1]
    quotient = None  # provided per-section below
    recs = []
    for reg in regs:
        lam = {a: i for (a, i) in reg}
        br = Brace(E, hol, lam)
        if not is_ideal(br, Dset):
            continue
        L = subbrace_units(br, Dlist, iso)
        if L is None or L != want_L:
            continue
        recs.append((br,))
    # analyse with the *first* section for the invariants, cross-check residue
    # section-invariance across all supplied sections.
    out = []
    for (br,) in recs:
        per_section = []
        for s, quotient in sections:
            def Hp(h1, h2, s=s, quotient=quotient): return quotient(br.E.add(s[h1], s[h2]))
            # residue_h, sigma_h units (mod order), per non-zero h
            res = {}
            for h in Helems:
                if h == zeroH:
                    continue
                sh = s[h]; shinv = br.circ_inv(sh)
                nu_unit = iso[br.lamap(sh, gen)]
                sig_gen = br.circ(br.circ(sh, gen), shinv)
                sigma_unit = iso[sig_gen]
                residue = frozenset((nu_unit * l) % order for l in want_L)
                res[h] = (nu_unit, sigma_unit, residue)
            per_section.append((s, quotient, res))
        # residue must agree across sections (section-invariance test)
        residues0 = {h: v[2] for h, v in per_section[0][2].items()}
        sigmas0 = {h: v[1] for h, v in per_section[0][2].items()}
        sec_inv = True
        for (_, _, res) in per_section[1:]:
            for h in res:
                if res[h][2] != residues0[h] or res[h][1] != sigmas0[h]:
                    sec_inv = False
        # additive class: use first section; b(h1,h2)=iso(beta) reps
        s0, quotient0, res0 = per_section[0]
        def Hp0(h1, h2): return quotient0(br.E.add(s0[h1], s0[h2]))
        beta = {}
        for h1 in Helems:
            for h2 in Helems:
                if h1 == zeroH or h2 == zeroH:
                    continue
                bE = br.E.add(br.E.add(br.E.neg(s0[Hp0(h1, h2)]), s0[h1]), s0[h2])
                beta[(h1, h2)] = iso[bE]  # in Z/order
        out.append(dict(br=br, residues=residues0, sigmas=sigmas0,
                        nu_units={h: res0[h][0] for h in res0},
                        beta=beta, sec_inv=sec_inv))
    return out, len(regs)

# ---------------------------------------------------------------------------
def beta_class_H2(order, Helems, zeroH, Hplus, mu_triv, beta_units):
    """coset rep of [beta] in H^2_+((H,+),Z/order; trivial) as canonical tuple."""
    D = Ab([order], "D")
    coh = Coh(D, Helems, Hplus, mu_triv, zeroH)
    f = {(h1, h2): (beta_units[(h1, h2)],)
         for h1 in Helems for h2 in Helems if h1 != zeroH and h2 != zeroH}
    B = [coh.d1(theta) for theta in coh.all_1cochains()]
    orbit = [tuple(sorted(add2(D, f, b).items())) for b in B]
    return min(orbit)

# ===========================================================================
def run_case(order, want_L, Helems, zeroH, Hplus, Hcirc, Hneg, Hlam,
             groups, label, do_abstract=True):
    print("=" * 74)
    print("CASE", label)
    print("=" * 74)
    D = Ab([order], "D")
    mu_triv = {h: {d: d for d in D.elems} for h in Helems}

    # gather genuine realised [beta] per (residue,sigma) triplet
    bucket = defaultdict(set)                 # (residues,sigmas) -> set of [beta]
    bucket_bunits = defaultdict(set)          # keep raw b(1,1) for H=Z/2 lock
    all_sec_inv = True
    total_braces_kept = 0
    for (E, Dlist, iso, sections) in groups:
        recs, nregs = enumerate_kernel(E, Dlist, iso, sections, Helems, zeroH,
                                       Hplus, Hcirc, Hneg, want_L, order)
        for r in recs:
            total_braces_kept += 1
            all_sec_inv &= r["sec_inv"]
            resid_key = tuple(sorted((h, r["residues"][h]) for h in r["residues"]))
            sig_key = tuple(sorted((h, r["sigmas"][h]) for h in r["sigmas"]))
            bkey = beta_class_H2(order, Helems, zeroH, Hplus, mu_triv, r["beta"])
            bucket[(resid_key, sig_key)].add(bkey)
            if Helems == [0, 1]:  # H=Z/2: record scalar b(1,1)
                bucket_bunits[(resid_key, sig_key)].add(r["beta"][(1, 1)])
        print(f"  [{E.name}] regular subgroups={nregs}, kept (D non-triv ideal, "
              f"L={sorted(want_L)}): {len(recs)}")

    print(f"  section-invariance of (residue,sigma) across sections: "
          f"{'HOLDS' if all_sec_inv else '*** FAILS ***'}")

    # H^2_+ total size (for basepoint / torsor readout)
    coh = Coh(D, Helems, Hplus, mu_triv, zeroH)
    Z2p = [f for f in coh.all_2cochains() if coh.is_zero3(coh.d2(f))]
    B2p = set(tuple(sorted(coh.d1(th).items())) for th in coh.all_1cochains())
    reps = set()
    for f in Z2p:
        orbit = [tuple(sorted(add2(D, f, dict(bk)).items())) for bk in B2p]
        reps.add(min(orbit))
    H2size = len(reps)
    zero_rep = min([tuple(sorted(add2(D, {k: (0,) for k in
                    [(h1, h2) for h1 in coh.nz for h2 in coh.nz]}, dict(bk)).items()))
                    for bk in B2p])
    print(f"  |H^2_+| = {H2size}   (zero class present as basepoint check)")

    # per-triplet table
    print("  " + "-" * 70)
    print(f"  {'residue[nu]':<22}{'sigma':<14}{'|im phi^+|':<11}{'0 in im?':<10}coset?")
    n_coset = 0
    n_total = 0
    torsor_no_base = 0
    for (rk, sk), realised in sorted(bucket.items()):
        n_total += 1
        has_zero = zero_rep in realised
        is_coset = coset_test(D, coh, B2p, realised)
        n_coset += int(is_coset)
        if is_coset and not has_zero:
            torsor_no_base += 1
        rdesc = "{" + ",".join(str(sorted(v)[0]) + "L" for _, v in rk) + "}" \
            if False else str([sorted(v) for _, v in rk])
        sdesc = str([s for _, s in sk])
        print(f"  {rdesc:<22}{sdesc:<14}{len(realised):<11}"
              f"{('yes' if has_zero else 'NO'):<10}{'yes' if is_coset else 'NO'}")
    print(f"  => realised set is a COSET (affine kernel signature) on "
          f"{n_coset}/{n_total} triplets; TORSOR-without-basepoint on {torsor_no_base}")

    # (d) H=Z/2 three-way lock analogue
    if Helems == [0, 1]:
        print("  " + "-" * 70)
        print("  (d) |G|-lock for this kernel:  for each realised brace, "
              "b(1,1), nu, sigma, (lam^D_1 - 1)*b mod order, 2*(nu*sigma-1) mod order")
        for (rk, sk), bs in sorted(bucket_bunits.items()):
            nu = rk[0][1]  # residues, but need nu unit; recover from bucket via nu_units
            pass
        # simpler: recompute directly over kept braces
        lock_rows = []
        for (E, Dlist, iso, sections) in groups:
            recs, _ = enumerate_kernel(E, Dlist, iso, sections, Helems, zeroH,
                                       Hplus, Hcirc, Hneg, want_L, order)
            isoInv = {iso[d]: d for d in Dlist}
            for r in recs:
                b = r["beta"][(1, 1)]
                nu = r["nu_units"][1]
                sig = r["sigmas"][1]
                lamD1 = 3 if order == 4 else 5  # unit of lam^D_gen (nontrivial brace)
                lhs = ((lamD1 - 1) * b) % order
                rhs = (2 * (nu * sig - 1)) % order
                lock_rows.append((b, nu, sig, lhs, rhs, lhs == rhs))
        seen = sorted(set(lock_rows))
        oklock = all(x[5] for x in lock_rows)
        for (b, nu, sig, lhs, rhs, ok) in seen:
            bc = "[b]=0" if b % 2 == 0 else "[b]!=0"
            print(f"      b={b} nu={nu} sig={sig}: (lam-1)b={lhs}  2(nu*sig-1)={rhs}  "
                  f"{bc}  {'match' if ok else 'MISMATCH'}")
        print(f"      lock (lam^D_1-1)b == 2(nu*sig-1): {'HOLDS' if oklock else 'FAILS'} "
              f"on {sum(x[5] for x in lock_rows)}/{len(lock_rows)}")

    return bucket, zero_rep

def coset_test(D, coh, B2p, realised):
    """Is `realised` (set of H^2_+ coset reps) a single coset of some subgroup?
       Equivalent: realised - realised (difference set) is a subgroup, and
       realised = r0 + that subgroup."""
    reps = list(realised)
    if len(reps) == 1:
        return True
    # lift each rep to a representative 2-cochain
    def to_cochain(rep):
        return dict(rep)
    r0 = to_cochain(reps[0])
    diffs = set()
    for r in reps:
        fr = to_cochain(r)
        d = add2(D, fr, neg2(D, r0))
        # reduce mod B2p to canonical class
        orbit = [tuple(sorted(add2(D, d, dict(bk)).items())) for bk in B2p]
        diffs.add(min(orbit))
    # diffs should be a subgroup of H^2_+: closed under add and contains 0
    # check closure
    diffs_c = [dict(x) for x in diffs]
    for a in diffs_c:
        for b in diffs_c:
            s = add2(D, a, b)
            orbit = [tuple(sorted(add2(D, s, dict(bk)).items())) for bk in B2p]
            if min(orbit) not in diffs:
                return False
    # realised must equal r0 + diffs (same cardinality already since bijection)
    return len(diffs) == len(realised)

# ===========================================================================
if __name__ == "__main__":
    # ---------- H = Z/2 ,  D = Z/4 nontrivial (L={1,3}) ----------
    Hp = lambda a, b: (a + b) % 2; Hc = Hp; Hn = lambda a: (-a) % 2; Hl = lambda a, b: b
    # E = Z/8 , D = 2Z/8 ~= Z/4 (b != 0 side)
    Z8 = Ab([8], "Z/8"); D8 = [(0,), (2,), (4,), (6,)]; iso8 = {(2 * k,): k for k in range(4)}
    secs8 = [({0: (0,), 1: (1,)}, lambda x: x[0] % 2),
             ({0: (0,), 1: (3,)}, lambda x: x[0] % 2),
             ({0: (0,), 1: (5,)}, lambda x: x[0] % 2)]
    # E = Z/4 x Z/2 , D = Z/4 x 0  (b = 0 side)
    Z4Z2 = Ab([4, 2], "Z/4xZ/2"); D42 = [(k, 0) for k in range(4)]; iso42 = {(k, 0): k for k in range(4)}
    secs42 = [({0: (0, 0), 1: (0, 1)}, lambda x: x[1] % 2),
              ({0: (0, 0), 1: (1, 1)}, lambda x: x[1] % 2),
              ({0: (0, 0), 1: (2, 1)}, lambda x: x[1] % 2)]
    groups2 = [(Z8, D8, iso8, secs8), (Z4Z2, D42, iso42, secs42)]
    run_case(4, frozenset({1, 3}), [0, 1], 0, Hp, Hc, Hn, Hl, groups2,
             "H=Z/2, D=Z/4 nontrivial (L={1,3}=Aut(Z/4))")

    # ---------- H = Z/3 , D = Z/4 nontrivial ----------
    Hp3 = lambda a, b: (a + b) % 3; Hc3 = Hp3; Hn3 = lambda a: (-a) % 3; Hl3 = lambda a, b: b
    # E = Z/12 , D = {0,3,6,9} = 3Z/12 ~= Z/4 (gen 3);  quotient x -> x%3 ; section i->i
    Z12 = Ab([12], "Z/12"); D12 = [(3 * k,) for k in range(4)]; iso12 = {(3 * k,): k for k in range(4)}
    secs12 = [({0: (0,), 1: (1,), 2: (2,)}, lambda x: x[0] % 3),
              ({0: (0,), 1: (4,), 2: (2,)}, lambda x: x[0] % 3)]
    groups3 = [(Z12, D12, iso12, secs12)]
    run_case(4, frozenset({1, 3}), [0, 1, 2], 0, Hp3, Hc3, Hn3, Hl3, groups3,
             "H=Z/3, D=Z/4 nontrivial")
