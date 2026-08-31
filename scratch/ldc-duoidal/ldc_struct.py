"""Structural morphisms for the (⋉,⋊) duoidal/LDC structure, built on ldc_verify.py."""
from itertools import product
from ldc_verify import (C, Y, ltimes, rtimes, Mor, idmor, compose, eq_mor,
                        ltimes_mor, rtimes_mor, ev, all_mors, sample_containers)

def SB(x):  # shape list
    return x['S']

# ---------------- interchange  ζ : (A⋊B)⋉(C⋊D) -> (A⋉C)⋊(B⋉D) ----------------
def zeta(A, B, C_, D):
    P = rtimes(A, B); Q = rtimes(C_, D)          # src = P ⋉ Q
    U = ltimes(A, C_); V = ltimes(B, D)          # tgt = U ⋊ V
    src = ltimes(P, Q); tgt = rtimes(U, V)
    fwd = {((a, b), (c, d)): ((a, c), (b, d))
           for a in A['S'] for b in B['S'] for c in C_['S'] for d in D['S']}

    def make_bwd(a, b, c, d):
        def bwd(e):  # e = (H, w),  H: S_V->U[(a,c)],  w=(fB,fD) in V[(b,d)]
            H, w = e
            fB, fD = w
            # unpack
            def aval(bb, dd, cc):
                U_elt = ev(H, V['S'], (bb, dd))     # (fA_part, fC_part)
                fA_part, fC_part = U_elt
                return ev(fA_part, C_['S'], cc)
            def cval(bb, dd, aa):
                U_elt = ev(H, V['S'], (bb, dd))
                fA_part, fC_part = U_elt
                return ev(fC_part, A['S'], aa)
            def bval(dd):
                return ev(fB, D['S'], dd)
            def dval(bb):
                return ev(fD, B['S'], bb)
            # repack into src = P ⋉ Q element (F, G)
            # F: S_Q -> P[(a,b)] = (fA:S_B->A[a], yB in B[b])
            F = tuple(
                (tuple(aval(bb, dd, cc) for bb in B['S']), bval(dd))
                for (cc, dd) in Q['S']
            )
            # G: S_P -> Q[(c,d)] = (fC:S_D->C[c], yD in D[d])
            G = tuple(
                (tuple(cval(bb, dd, aa) for dd in D['S']), dval(bb))
                for (aa, bb) in P['S']
            )
            return (F, G)
        return bwd

    bwd = {((a, b), (c, d)): make_bwd(a, b, c, d)
           for a in A['S'] for b in B['S'] for c in C_['S'] for d in D['S']}
    return Mor(src, tgt, fwd, bwd)

# ---------------- distributor δ : A⋉(B⋊C) -> (A⋉B)⋊C ----------------
def delta(A, B, C_):
    src = ltimes(A, rtimes(B, C_))     # A ⋉ (B ⋊ C)
    tgt = rtimes(ltimes(A, B), C_)     # (A ⋉ B) ⋊ C
    fwd = {(a, (b, c)): ((a, b), c)
           for a in A['S'] for b in B['S'] for c in C_['S']}
    # src dir at (a,(b,c)) = A[a]^{S_{B⋊C}} × (B⋊C)[(b,c)]^{S_A}
    #   (B⋊C)[(b,c)] = B[b]^{S_C} × C[c]
    # tgt dir at ((a,b),c) = (A⋉B)[(a,b)]^{S_C} × C[c]
    #   (A⋉B)[(a,b)] = A[a]^{S_B} × B[b]^{S_A}
    BrC = rtimes(B, C_); AlB = ltimes(A, B)

    def make_bwd(a, b, c):
        def bwd(e):  # e = (K, y) ; K: S_C -> (A⋉B)[(a,b)] = (fA:S_B->A[a], gB:S_A->B[b]);  y in C[c]
            K, y = e
            # unpack
            def aval(cc, bb):  # A[a] indexed by (S_C, S_B)
                fA, gB = ev(K, C_['S'], cc)
                return ev(fA, B['S'], bb)
            def bval(cc, aa):  # B[b] indexed by (S_C, S_A)
                fA, gB = ev(K, C_['S'], cc)
                return ev(gB, A['S'], aa)
            cval = y            # C[c], NO exponent on tgt side
            # repack src = A ⋉ (B⋊C):  (Fa, Gbc)
            #   Fa: S_{B⋊C} -> A[a]
            Fa = tuple(aval(cc, bb) for (bb, cc) in BrC['S'])
            #   Gbc: S_A -> (B⋊C)[(b,c)] = (fB:S_C->B[b], zC in C[c])
            Gbc = tuple(
                (tuple(bval(cc, aa) for cc in C_['S']), cval)   # zC = const c-value (const in S_A)
                for aa in A['S']
            )
            return (Fa, Gbc)
        return bwd

    bwd = {(a, (b, c)): make_bwd(a, b, c)
           for a in A['S'] for b in B['S'] for c in C_['S']}
    return Mor(src, tgt, fwd, bwd)

# ---------------- naturality tester ----------------
def check_nat_zeta(quads, cap=3):
    """quads: list of (A,B,C,D) with attached morphism lists to keep it tiny."""
    n = 0
    for (A, B, Cc, D) in quads:
        z1 = zeta(A, B, Cc, D)
        mA = all_mors(A, A, cap=cap); mB = all_mors(B, B, cap=cap)
        mC = all_mors(Cc, Cc, cap=cap); mD = all_mors(D, D, cap=cap)
        for phi in mA:
            for psi in mB:
                for chi in mC:
                    for om in mD:
                        left = compose(zeta(phi.tgt, psi.tgt, chi.tgt, om.tgt),
                                       ltimes_mor(rtimes_mor(phi, psi), rtimes_mor(chi, om)))
                        right = compose(rtimes_mor(ltimes_mor(phi, chi), ltimes_mor(psi, om)),
                                        z1)
                        n += 1
                        if not eq_mor(left, right):
                            print("ZETA NATURALITY FAIL", A['S'], B['S'], Cc['S'], D['S'])
                            return False
    print(f"ζ naturality: checked {n} squares, all commute.")
    return True

def check_nat_delta(objs, cap=8):
    n = 0
    for A in objs:
        for B in objs:
            for Cc in objs:
                for phi in all_mors(A, A, cap=cap):
                    for psi in all_mors(B, B, cap=cap):
                        for chi in all_mors(Cc, Cc, cap=cap):
                            left = compose(delta(phi.tgt, psi.tgt, chi.tgt),
                                           ltimes_mor(phi, rtimes_mor(psi, chi)))
                            right = compose(rtimes_mor(ltimes_mor(phi, psi), chi),
                                            delta(A, B, Cc))
                            n += 1
                            if not eq_mor(left, right):
                                print("DELTA NATURALITY FAIL", A['S'], B['S'], Cc['S'])
                                return False
    print(f"δ naturality: checked {n} squares, all commute.")
    return True

# ---------------- well-definedness: bwd lands in the right set ----------------
def check_welldef(mor, name):
    for s in mor.src['S']:
        t = mor.fwd[s]
        srcset = set(map(repr, mor.src['d'][s]))
        for e in mor.tgt['d'][t]:
            img = mor.bwd[s](e)
            if repr(img) not in srcset:
                print(f"{name}: bwd image not in src dir set at shape {s}: {img}")
                return False
    print(f"{name}: well-defined (all bwd images land in src directions).")
    return True

if __name__ == '__main__':
    # tiny objects: keep EITHER shapes OR dirs at 1 to avoid exponential blowup
    yy = Y()
    two = C(['0', '1'], {'0': ['*'], '1': ['*']})      # 2 shapes, 1 dir  (constant 2)
    sq = C(['0'], {'0': ['u', 'v']})                    # 1 shape, 2 dirs  (y^2)
    small = [yy, two, sq]
    # well-definedness
    check_welldef(zeta(two, sq, two, sq), "ζ (two,sq,two,sq)")
    check_welldef(zeta(two, two, two, two), "ζ (all two)")
    check_welldef(delta(sq, two, sq), "δ (sq,two,sq)")
    check_welldef(delta(two, two, two), "δ (all two)")
    print("---- δ naturality ----")
    check_nat_delta(small, cap=6)
    print("---- ζ naturality ----")
    quads = [(two, sq, two, sq), (two, two, two, two), (sq, two, sq, two),
             (two, sq, sq, two), (yy, two, sq, two), (two, yy, two, sq)]
    check_nat_zeta(quads, cap=3)
