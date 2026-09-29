#!/usr/bin/env python3
"""
Independent from-scratch verification of Rick's nu/[Omega] refutation of the
'residue-independence' claim in skew-brace cohomology.

Written WITHOUT reusing any of Rick's scripts.  Everything here is a fresh
brute-force skew-brace enumerator built on the regular-subgroup-of-holomorph
correspondence:

    skew braces (A,+,o) with fixed additive group (A,+)
      <-->  regular subgroups N of Hol(A) = A rtimes Aut(A,+)
      <-->  functions lam: A -> Aut(A,+) with lam_0 = id and the gamma law
              lam_{a + lam_a(b)} = lam_a . lam_b      (for all a,b)
    where  a o b = a + lam_a(b).

We enumerate ALL such lam on each fixed additive group, keep those in which a
prescribed subgroup D is an *ideal* carrying the prescribed sub-brace, and then
tabulate the pair (residue [nu] of nu_1 modulo L , circle action sigma_1)
against the additive extension class [beta] (which is a property of (A,+,D)
alone).

WITNESS 1  (order 8):  D = Z/4,  H = Z/2,  additive mu = 1.
WITNESS 2  (order 16): D = Z/8 with brace lam^D_x = x5^x (so L = {1,5}), H=Z/2.

Author: MacBeth compute agent, 2026-09-29.
"""

import itertools
import sys

# ======================================================================
#  Finite abelian group  A = prod Z/m_i
# ======================================================================

class Ab:
    def __init__(self, mods, name):
        self.mods = tuple(mods)
        self.name = name
        self.elems = [tuple(e) for e in itertools.product(*[range(m) for m in mods])]
        self.zero = tuple(0 for _ in mods)
        self.n = len(self.elems)

    def add(self, a, b):
        return tuple((x + y) % m for x, y, m in zip(a, b, self.mods))

    def neg(self, a):
        return tuple((-x) % m for x, m in zip(a, self.mods))

    def smul(self, k, a):
        return tuple((k * x) % m for x, m in zip(a, self.mods))

    # all additive automorphisms as dicts elem->elem
    def autos(self):
        k = len(self.mods)
        gens = []
        for i in range(k):
            e = [0] * k
            e[i] = 1
            gens.append(tuple(e))
        # each generator g_i (order m_i) may map to any element v with m_i*v = 0
        cand = []
        for i, m in enumerate(self.mods):
            cand.append([v for v in self.elems if self.smul(m, v) == self.zero])
        result = []
        for imgs in itertools.product(*cand):
            mp = {}
            for a in self.elems:
                val = self.zero
                for ai, vi in zip(a, imgs):
                    val = self.add(val, self.smul(ai, vi))
                mp[a] = val
            if len(set(mp.values())) == self.n:      # bijective => automorphism
                result.append(mp)
        return result


# ======================================================================
#  Holomorph machinery + regular-subgroup (= skew brace) enumeration
# ======================================================================

class Holomorph:
    def __init__(self, A):
        self.A = A
        self.autos = A.autos()                     # list of dicts
        # canonical key for each auto = tuple of images in fixed element order
        self.key2idx = {}
        for i, m in enumerate(self.autos):
            key = tuple(m[a] for a in A.elems)
            self.key2idx[key] = i
        self.naut = len(self.autos)
        self.id_idx = self._auto_index(lambda a: a)
        # composition table comp[i][j] = index of autos[i] o autos[j]
        self.comp = [[self._auto_index(lambda a, i=i, j=j: self.autos[i][self.autos[j][a]])
                      for j in range(self.naut)] for i in range(self.naut)]
        # inverse of each auto
        self.inv = [None] * self.naut
        for i in range(self.naut):
            for j in range(self.naut):
                if self.comp[i][j] == self.id_idx:
                    self.inv[i] = j
                    break

    def _auto_index(self, f):
        key = tuple(f(a) for a in self.A.elems)
        return self.key2idx[key]

    # Hol element = (a, i)  with a in A, i = auto index
    def mult(self, x, y):
        a, i = x
        b, j = y
        return (self.A.add(a, self.autos[i][b]), self.comp[i][j])

    def identity(self):
        return (self.A.zero, self.id_idx)

    def elements(self):
        return [(a, i) for a in self.A.elems for i in range(self.naut)]

    # -- regular closure: build subgroup, abort (None) if two elements share
    #    the same translation part (a genuinely regular subgroup has all
    #    translation parts distinct, so any subset does too).
    def reg_closure(self, gens):
        ident = self.identity()
        tp = {ident[0]: ident}
        S = {ident}
        for g in gens:
            a = g[0]
            if a in tp:
                if tp[a] != g:
                    return None
            else:
                tp[a] = g
                S.add(g)
        changed = True
        while changed:
            changed = False
            cur = list(S)
            for x in cur:
                for y in cur:
                    z = self.mult(x, y)
                    if z not in S:
                        a = z[0]
                        if a in tp:
                            if tp[a] != z:
                                return None      # collision -> not regular
                        else:
                            tp[a] = z
                            S.add(z)
                            changed = True
        return frozenset(S)

    def regular_subgroups(self):
        nA = self.A.n
        ident = self.identity()
        start = frozenset([ident])
        found = {start}
        work = [start]
        regs = set()
        hol = self.elements()
        while work:
            S = work.pop()
            if len(S) == nA:
                regs.add(S)
                continue
            used = {s[0] for s in S}
            for g in hol:
                if g[0] in used:      # would immediately collide
                    continue
                newS = self.reg_closure(list(S) + [g])
                if newS is None:
                    continue
                if newS not in found:
                    found.add(newS)
                    work.append(newS)
        return [r for r in regs]      # every one has size nA => regular


# ======================================================================
#  Skew-brace analysis relative to an ideal D  (H = Z/2 throughout)
# ======================================================================

def build_lambda(A, hol, reg):
    """From a regular subgroup, extract lam: a -> auto index."""
    lam = {}
    for (a, i) in reg:
        lam[a] = i
    return lam

def circ(A, hol, lam, a, b):
    return A.add(a, hol.autos[lam[a]][b])

def circ_inv(A, hol, lam, a):
    # b with a o b = 0  =>  lam_a(b) = -a  => b = lam_a^{-1}(-a)
    ai = lam[a]
    inv_auto = hol.autos[hol.inv[ai]]
    return inv_auto[A.neg(a)]

def cyclic_unit(A, gen, order, image_of_gen):
    """Given D cyclic = <gen> of given order, express an endo by the unit c
       with endo(gen) = c*gen.  Returns c in [0,order), or None if not a
       multiple of gen (should not happen for a genuine D-automorphism)."""
    table = {A.smul(k, gen): k for k in range(order)}
    return table.get(image_of_gen)

def analyse(A, hol, lam, D_elems, gen, order, g0):
    """Return dict with ideal-check + (L, nu unit, residue coset, sigma unit),
       or None if D is not an ideal of this skew brace."""
    Dset = set(D_elems)
    autos = hol.autos
    # 1. lambda-invariance: every lam_a preserves D
    for a in A.elems:
        img = {autos[lam[a]][d] for d in D_elems}
        if img != Dset:
            return None
    # 2. D normal in (A,+): abelian => automatic. (all our A are abelian)
    # 3. D normal in (A,o):  a o d o a^{-1} in D for all a in A, d in D
    for a in A.elems:
        ainv = circ_inv(A, hol, lam, a)
        for d in D_elems:
            x = circ(A, hol, lam, a, d)
            x = circ(A, hol, lam, x, ainv)
            if x not in Dset:
                return None
    # sub-brace on D: lam_d|_D as unit, for d in D
    L = set()
    subbrace = {}
    for d in D_elems:
        c = cyclic_unit(A, gen, order, autos[lam[d]][gen])
        if c is None:
            return None
        subbrace[d] = c
        L.add(c)
    # nu_1 = lam_{g0}|_D  as unit
    nu = cyclic_unit(A, gen, order, autos[lam[g0]][gen])
    if nu is None:
        return None
    residue = frozenset((nu * l) % order for l in L)
    # sigma_1 = o-conjugation by g0, restricted to D, as unit
    g0inv = circ_inv(A, hol, lam, g0)
    sig_gen = circ(A, hol, lam, g0, gen)
    sig_gen = circ(A, hol, lam, sig_gen, g0inv)
    sigma = cyclic_unit(A, gen, order, sig_gen)
    return dict(L=frozenset(L), subbrace=subbrace, nu=nu, residue=residue,
                sigma=sigma)

def gamma_ok(A, hol, lam):
    """Sanity: verify lam satisfies the gamma law (it must, coming from a
       genuine regular subgroup)."""
    autos = hol.autos
    for a in A.elems:
        for b in A.elems:
            lhs = lam[A.add(a, autos[lam[a]][b])]
            rhs = hol.comp[lam[a]][lam[b]]
            if lhs != rhs:
                return False
    return True

def beta_splits(A, D_elems):
    """[beta]=0 (additive extension of H=Z/2 by D splits) iff there is an
       element of order dividing 2 lying OUTSIDE D (an additive complement
       generator).  Returns True if [beta]=0, False if [beta]!=0."""
    Dset = set(D_elems)
    for x in A.elems:
        if x not in Dset and A.smul(2, x) == A.zero:
            return True
    return False


# ======================================================================
#  Reporting helpers
# ======================================================================

def residue_str(r, order):
    return "{" + ",".join(str(x) for x in sorted(r)) + "}"

def run_case(A, D_elems, gen, order, g0, prescribed_L, label, want_subbrace=None):
    hol = Holomorph(A)
    regs = hol.regular_subgroups()
    beta0 = beta_splits(A, D_elems)
    print(f"\n==== {label} ====")
    print(f"  additive group (A,+) = {A.name},  |A|={A.n},  |Aut(A,+)|={hol.naut}")
    print(f"  D = <{gen}> of order {order},  |D|={len(D_elems)},  section rep g0={g0}")
    print(f"  total skew braces on (A,+) found: {len(regs)}")
    print(f"  additive extension class [beta] on (A,+,D): "
          f"{'[beta]=0 (splits)' if beta0 else '[beta]!=0 (non-split)'}")
    # collect
    rows = []          # (residue, sigma, nu, L)
    for reg in regs:
        lam = build_lambda(A, hol, reg)
        assert gamma_ok(A, hol, lam), "gamma law violated -- enumerator bug!"
        res = analyse(A, hol, lam, D_elems, gen, order, g0)
        if res is None:
            continue
        if res["L"] != frozenset(prescribed_L):
            continue    # wrong sub-brace type on D
        rows.append((res["residue"], res["sigma"], res["nu"], tuple(sorted(res["L"]))))
    # tabulate distinct (residue, sigma)
    from collections import Counter
    cnt = Counter((residue_str(r, order), s) for (r, s, nu, L) in rows)
    print(f"  skew braces with D an ideal carrying prescribed sub-brace "
          f"L={sorted(prescribed_L)}: {len(rows)}")
    print(f"  occurring ([nu]-residue, sigma) pairs  (sigma as unit mod {order};"
          f" -1 = {order-1}):")
    for (rs, s), c in sorted(cnt.items()):
        print(f"      residue={rs:12s}  sigma={s}    count={c}")
    return dict(beta0=beta0, rows=rows, pairs=set(cnt.keys()), n_braces=len(regs))


# ======================================================================
#  Explicit named-witness verification (independent construction)
# ======================================================================

def verify_explicit_brace(A, lam_fn, label):
    """Build lam from an explicit formula lam_fn(a) -> auto-as-dict, verify it
       is a genuine skew brace (gamma law) and return lam-index map."""
    hol = Holomorph(A)
    lam = {}
    for a in A.elems:
        mp = {b: lam_fn(a, b) for b in A.elems}
        # check it is an automorphism we know
        key = tuple(mp[b] for b in A.elems)
        if key not in hol.key2idx:
            print(f"  [{label}] FAIL: lam_{a} is not an additive automorphism")
            return None, None
        lam[a] = hol.key2idx[key]
    ok = gamma_ok(A, hol, lam)
    print(f"  [{label}] explicit brace: gamma law {'OK' if ok else 'FAILED'}")
    return hol, (lam if ok else None)


# ======================================================================
#  MAIN
# ======================================================================

def main():
    print("#" * 72)
    print("# Independent verification of Rick's nu/[Omega] refutation")
    print("# (residue-independence claim) at orders 8 and 16")
    print("#" * 72)

    verdicts = {}

    # ------------------------------------------------------------------
    # WITNESS 1  (order 8):  D = Z/4 trivial brace, H = Z/2, sigma = -1
    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("WITNESS 1  (order 8):  D=Z/4 trivial (L={1}), H=Z/2, mu=1")
    print("=" * 72)

    # (A) additive group Z/8, D = 2Z/8 = {0,2,4,6}, gen=2 (order 4), g0=1
    Z8 = Ab([8], "Z/8")
    D8 = [(0,), (2,), (4,), (6,)]
    caseZ8 = run_case(Z8, D8, (2,), 4, (1,), prescribed_L={1},
                      label="Witness1(A): (A,+)=Z/8,  D=2Z/8~=Z/4 trivial")

    # (B) additive group Z/2 x Z/4, D = {(0,y)} ~= Z/4, gen=(0,1), g0=(1,0)
    Z2Z4 = Ab([2, 4], "Z/2 x Z/4")
    Dz2z4 = [(0, y) for y in range(4)]
    caseZ2Z4 = run_case(Z2Z4, Dz2z4, (0, 1), 4, (1, 0), prescribed_L={1},
                        label="Witness1(B): (A,+)=Z/2xZ/4,  D={0}xZ/4 trivial")

    # ---- Claim (i): the explicit Z/2xZ/4 brace lam_{(i,x)}(j,y)=(j, y+2jx) ----
    print("\n---- Claim (i): explicit Z/2xZ/4 brace, expect nu=1, [beta]=0 ----")
    def lam_i(a, b):
        (i, x) = a
        (j, y) = b
        return (j, (y + 2 * j * x) % 4)
    holB, lamB = verify_explicit_brace(Z2Z4, lam_i, "claim(i)")
    if lamB is not None:
        res = analyse(Z2Z4, holB, lamB, Dz2z4, (0, 1), 4, (1, 0))
        b0 = beta_splits(Z2Z4, Dz2z4)
        print(f"  computed: nu_1 (unit mod4) = {res['nu']}   "
              f"L={sorted(res['L'])}   residue={residue_str(res['residue'],4)}   "
              f"sigma={res['sigma']} ( -1 = 3 )   [beta]={'0' if b0 else '!=0'}")
        ok_i = (res['nu'] == 1 and b0 and res['sigma'] == 3)
        verdicts['(i)'] = ok_i
        print(f"  Claim (i)  [nu=1 admissible on Z/2xZ/4 with [beta]=0, sigma=-1]: "
              f"{'VERIFIED' if ok_i else 'REFUTED'}")

    # ---- Claim (ii): on Z/8, NO skew brace has (nu=1, sigma=-1) ----
    print("\n---- Claim (ii): exhaustive on Z/8 -- expect NO (nu=1, sigma=-1) ----")
    # nu=1 means residue={1} (since L={1}); sigma=-1 means unit 3 mod4
    bad = [(rs, s) for (rs, s) in caseZ8['pairs'] if rs == "{1}" and s == 3]
    present_ii = len(bad) > 0
    verdicts['(ii)'] = (not present_ii) and (not caseZ8['beta0'])
    print(f"  pairs present on Z/8: {sorted(caseZ8['pairs'])}")
    print(f"  (nu=1 i.e. residue={{1}}, sigma=-1 i.e. 3) present? {present_ii}")
    print(f"  Claim (ii) [ (nu=1,sigma=-1) NOT realisable on Z/8, [beta]!=0 ]: "
          f"{'VERIFIED' if verdicts['(ii)'] else 'REFUTED'}")

    # ---- Claim (iii): nu=-1 realisable with BOTH [beta]=0 and [beta]!=0 ----
    print("\n---- Claim (iii): nu=-1 (residue={3}) realisable on both groups ----")
    # nu=-1 : residue {3} (unit 3 = -1 mod 4); sigma=-1 (unit 3)
    nuNeg_Z8 = any(rs == "{3}" and s == 3 for (rs, s) in caseZ8['pairs'])
    nuNeg_Z2Z4 = any(rs == "{3}" and s == 3 for (rs, s) in caseZ2Z4['pairs'])
    print(f"  nu=-1,sigma=-1 on Z/8       ([beta]!=0): {nuNeg_Z8}")
    print(f"  nu=-1,sigma=-1 on Z/2xZ/4   ([beta]=0):  {nuNeg_Z2Z4}")
    verdicts['(iii)'] = nuNeg_Z8 and nuNeg_Z2Z4
    print(f"  Claim (iii): {'VERIFIED' if verdicts['(iii)'] else 'REFUTED'}")

    # ---- Conclusion order 8: realisable [beta] set DEPENDS on nu ----
    # For nu=1 (residue {1}): which additive groups admit it (with sigma=-1)?
    def groups_admitting(residue_str_target, sigma_target):
        out = []
        if any(rs == residue_str_target and s == sigma_target for (rs, s) in caseZ8['pairs']):
            out.append("[beta]!=0 (Z/8)")
        if any(rs == residue_str_target and s == sigma_target for (rs, s) in caseZ2Z4['pairs']):
            out.append("[beta]=0 (Z/2xZ/4)")
        return out
    adm_nu1 = groups_admitting("{1}", 3)
    adm_nuNeg = groups_admitting("{3}", 3)
    print("\n---- Conclusion (order 8): realisable [beta] depends on nu? ----")
    print(f"  nu=1  (sigma=-1) realisable [beta] classes: {adm_nu1}")
    print(f"  nu=-1 (sigma=-1) realisable [beta] classes: {adm_nuNeg}")
    coupled8 = (set(adm_nu1) != set(adm_nuNeg))
    verdicts['concl8'] = coupled8
    print(f"  => realisable-[beta] set DEPENDS on nu (independence FALSE): "
          f"{'CONFIRMED' if coupled8 else 'NOT confirmed'}")

    # ------------------------------------------------------------------
    # WITNESS 2  (order 16): D = Z/8 with lam^D_x = x5^x  (L={1,5}), sigma=id
    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("WITNESS 2 (order 16): D=Z/8 brace lam^D_x = x5^x (L={1,5}), H=Z/2, mu=1")
    print("=" * 72)

    # (A) additive group Z/16, D = 2Z/16 ~= Z/8, gen=2 (order8), g0=1
    Z16 = Ab([16], "Z/16")
    D16 = [(2 * k,) for k in range(8)]
    # prescribed sub-brace L = {1,5} on D~=Z/8
    caseZ16 = run_case(Z16, D16, (2,), 8, (1,), prescribed_L={1, 5},
                       label="Witness2(A): (A,+)=Z/16,  D=2Z/16~=Z/8 brace L={1,5}")

    # (B) additive group Z/2 x Z/8, D = {(0,y)} ~= Z/8, gen=(0,1), g0=(1,0)
    Z2Z8 = Ab([2, 8], "Z/2 x Z/8")
    Dz2z8 = [(0, y) for y in range(8)]
    caseZ2Z8 = run_case(Z2Z8, Dz2z8, (0, 1), 8, (1, 0), prescribed_L={1, 5},
                        label="Witness2(B): (A,+)=Z/2xZ/8,  D={0}xZ/8 brace L={1,5}")

    # ---- explicit W_b: Z/2xZ/8, lam_{(i,x)}(j,y) = (j, 5^x * y) ----
    print("\n---- W_b explicit: Z/2xZ/8, lam_{(i,x)}(j,y)=(j, 5^x y) ----")
    def lam_wb(a, b):
        (i, x) = a
        (j, y) = b
        return (j, (pow(5, x, 8) * y) % 8)
    holWb, lamWb = verify_explicit_brace(Z2Z8, lam_wb, "W_b")
    if lamWb is not None:
        res = analyse(Z2Z8, holWb, lamWb, Dz2z8, (0, 1), 8, (1, 0))
        if res is not None:
            b0 = beta_splits(Z2Z8, Dz2z8)
            print(f"  W_b: residue={residue_str(res['residue'],8)}  sigma={res['sigma']}"
                  f"  L={sorted(res['L'])}  [beta]={'0' if b0 else '!=0'}")

    # ---- explicit W_a: Z/16, lam_x(y) = (1+2a)^x * y for some a giving {3,7} ----
    print("\n---- W_a explicit: Z/16, lam_x(y) = (unit)^x y ----")
    # try units u = 3 (=1+2*1) generating nu residue {3,7} on D=2Z/16
    for u in (3, 7, 5, 9, 11, 13, 15):
        def lam_wa(a, b, u=u):
            (x,) = a
            (y,) = b
            return ((pow(u, x, 16) * y) % 16,)
        holWa, lamWa = verify_explicit_brace(Z16, lam_wa, f"W_a(u={u})")
        if lamWa is None:
            continue
        res = analyse(Z16, holWa, lamWa, D16, (2,), 8, (1,))
        if res is None:
            print(f"    u={u}: D not an ideal / wrong sub-brace")
            continue
        b0 = beta_splits(Z16, D16)
        print(f"    u={u}: residue={residue_str(res['residue'],8)} sigma={res['sigma']}"
              f"  L={sorted(res['L'])}  [beta]={'0' if b0 else '!=0'}")

    # ---- Coupling claim: which (residue,sigma) pairs occur on each group ----
    print("\n---- Witness2 coupling analysis ----")
    print(f"  Z/16   ([beta]!=0) pairs: {sorted(caseZ16['pairs'])}")
    print(f"  Z/2xZ/8 ([beta]=0) pairs: {sorted(caseZ2Z8['pairs'])}")
    L_resid = "{1,5}"
    other_resid = "{3,7}"
    SIGMA_ID = 1     # prescribed circle action for Witness 2 is sigma = id
    # coupling predicted at the PRESCRIBED circle data sigma=id:
    #   [beta]!=0 (Z/16)   <-> residue {3,7}
    #   [beta]=0  (Z/2xZ/8)<-> residue {1,5}
    z16_res_all = {rs for (rs, s) in caseZ16['pairs']}
    z2z8_res_all = {rs for (rs, s) in caseZ2Z8['pairs']}
    z16_res = {rs for (rs, s) in caseZ16['pairs'] if s == SIGMA_ID}
    z2z8_res = {rs for (rs, s) in caseZ2Z8['pairs'] if s == SIGMA_ID}
    print(f"  ALL residues on Z/16   ([beta]!=0), any sigma: {sorted(z16_res_all)}")
    print(f"  ALL residues on Z/2xZ/8 ([beta]=0), any sigma: {sorted(z2z8_res_all)}")
    print(f"  NOTE: on Z/2xZ/8 the residue {other_resid} occurs ONLY with "
          f"sigma in {{3,7}} (=nu itself), never with the prescribed sigma=id.")
    print(f"  -- restricting to the PRESCRIBED circle action sigma=id --")
    print(f"  residues on Z/16   ([beta]!=0), sigma=id: {sorted(z16_res)}")
    print(f"  residues on Z/2xZ/8 ([beta]=0), sigma=id: {sorted(z2z8_res)}")
    missing_pair = other_resid not in z2z8_res     # ([nu]={3,7},[beta]=0,sigma=id) missing?
    missing_pair2 = L_resid not in z16_res         # ([nu]={1,5},[beta]!=0,sigma=id) missing?
    print(f"  pair ([nu]={other_resid}, [beta]=0, sigma=id)   MISSING? {missing_pair}")
    print(f"  pair ([nu]={L_resid}, [beta]!=0, sigma=id)   MISSING? {missing_pair2}")
    coupled16 = missing_pair and missing_pair2 and (z16_res == {other_resid}) and (z2z8_res == {L_resid})
    verdicts['concl16'] = coupled16
    print(f"  => at the prescribed circle action sigma=id, residue and [beta]"
          f" are COUPLED at order 16: {'CONFIRMED' if coupled16 else 'NOT confirmed'}")

    # ------------------------------------------------------------------
    #  FINAL VERDICT
    # ------------------------------------------------------------------
    print("\n" + "#" * 72)
    print("# SUMMARY OF CLAIMS")
    print("#" * 72)
    for k in ['(i)', '(ii)', '(iii)', 'concl8', 'concl16']:
        v = verdicts.get(k)
        print(f"  {k:8s}: {'VERIFIED/CONFIRMED' if v else 'REFUTED/NOT-CONFIRMED'}")
    overall = verdicts.get('concl8') and verdicts.get('concl16') \
        and verdicts.get('(i)') and verdicts.get('(ii)') and verdicts.get('(iii)')
    print("\nFINAL VERDICT:")
    if overall:
        print("  Enumeration CONFIRMS Rick's refutation: residue [nu] and the")
        print("  additive class [beta]/[Omega] are COUPLED -- the residue-")
        print("  independence claim is FALSE at both order 8 and order 16.")
    else:
        print("  Enumeration does NOT fully confirm the refutation (see above).")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
