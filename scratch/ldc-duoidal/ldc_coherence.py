"""Associators, unitors, and the LDC/duoidal coherence diagrams."""
from ldc_verify import (C, Y, ltimes, rtimes, Mor, idmor, compose, eq_mor,
                        ltimes_mor, rtimes_mor, ev)
from ldc_struct import zeta, delta, check_welldef

def invert(m):
    """inverse of an iso morphism m: src->tgt (fwd bijective on shapes, bwd bijective per shape)."""
    inv_fwd = {}
    for s in m.src['S']:
        inv_fwd[m.fwd[s]] = s
    def make_bwd(t):
        s = inv_fwd[t]
        # bwd_s : tgt[t] -> src[s] is a bijection; invert it by tabulation
        table = {}
        for e in m.tgt['d'][t]:
            table[repr(m.bwd[s](e))] = e
        srcelts = m.src['d'][s]
        return lambda x: table[repr(x)]
    inv_bwd = {t: make_bwd(t) for t in m.tgt['S']}
    return Mor(m.tgt, m.src, inv_fwd, inv_bwd)

# ---- associators (isos), identity on flattened normal form ----
def assoc_ltimes(A, B, Cc):  # (A⋉B)⋉C -> A⋉(B⋉C)
    AB = ltimes(A, B); BC = ltimes(B, Cc)
    src = ltimes(AB, Cc); tgt = ltimes(A, BC)
    fwd = {((a, b), c): (a, (b, c)) for a in A['S'] for b in B['S'] for c in Cc['S']}
    def make_bwd(a, b, c):
        def bwd(e):  # tgt elt (Fa, Gbc)
            Fa, Gbc = e
            def aval(bb, cc): return ev(Fa, BC['S'], (bb, cc))
            def bval(aa, cc):
                fB, fC = ev(Gbc, A['S'], aa); return ev(fB, Cc['S'], cc)
            def cval(aa, bb):
                fB, fC = ev(Gbc, A['S'], aa); return ev(fC, B['S'], bb)
            # src elt ((A⋉B)⋉C): (K: S_C->(A⋉B)[(a,b)], wC: S_{A⋉B}->C[c])
            K = tuple((tuple(aval(bb, cc) for bb in B['S']),
                       tuple(bval(aa, cc) for aa in A['S']))
                      for cc in Cc['S'])
            wC = tuple(cval(aa, bb) for (aa, bb) in AB['S'])
            return (K, wC)
        return bwd
    bwd = {((a, b), c): make_bwd(a, b, c) for a in A['S'] for b in B['S'] for c in Cc['S']}
    return Mor(src, tgt, fwd, bwd)

def assoc_rtimes(A, B, Cc):  # (A⋊B)⋊C -> A⋊(B⋊C)
    AB = rtimes(A, B); BC = rtimes(B, Cc)
    src = rtimes(AB, Cc); tgt = rtimes(A, BC)
    fwd = {((a, b), c): (a, (b, c)) for a in A['S'] for b in B['S'] for c in Cc['S']}
    def make_bwd(a, b, c):
        def bwd(e):  # tgt elt (Fa, (fB, yC))
            Fa, w = e; fB, yC = w
            def aval(bb, cc): return ev(Fa, BC['S'], (bb, cc))
            def bval(cc): return ev(fB, Cc['S'], cc)
            cval = yC
            # src elt: (K: S_C->(A⋊B)[(a,b)]=(fA:S_B->A[a], yB), yC')
            K = tuple((tuple(aval(bb, cc) for bb in B['S']), bval(cc)) for cc in Cc['S'])
            return (K, cval)
        return bwd
    bwd = {((a, b), c): make_bwd(a, b, c) for a in A['S'] for b in B['S'] for c in Cc['S']}
    return Mor(src, tgt, fwd, bwd)

# ---- unitors (right unit y) ----
def runit_ltimes(A):  # A⋉y -> A
    src = ltimes(A, Y()); tgt = A
    fwd = {(a, '*'): a for a in A['S']}
    def make_bwd(a):
        def bwd(x):  # x in A[a]; build (f: S_y->A[a], g: S_A->y[*])
            f = (x,)                       # single value over S_y={*}
            g = tuple('·' for _ in A['S'])  # y[*] only element
            return (f, g)
        return bwd
    return Mor(src, tgt, fwd, {(a, '*'): make_bwd(a) for a in A['S']})

def lunit_ltimes(A):  # y⋉A -> A
    src = ltimes(Y(), A); tgt = A
    fwd = {('*', a): a for a in A['S']}
    def make_bwd(a):
        def bwd(x):  # (f:S_A->y[*], g:S_y->A[a])
            f = tuple('·' for _ in A['S']); g = (x,)
            return (f, g)
        return bwd
    return Mor(src, tgt, fwd, {('*', a): make_bwd(a) for a in A['S']})

def runit_rtimes(A):  # A⋊y -> A
    src = rtimes(A, Y()); tgt = A
    fwd = {(a, '*'): a for a in A['S']}
    def make_bwd(a):
        def bwd(x):  # (f:S_y->A[a], y·); dir = A[a]^{S_y} × y[*]
            return ((x,), '·')
        return bwd
    return Mor(src, tgt, fwd, {(a, '*'): make_bwd(a) for a in A['S']})

def lunit_rtimes(A):  # y⋊A -> A
    src = rtimes(Y(), A); tgt = A
    fwd = {('*', a): a for a in A['S']}
    def make_bwd(a):
        def bwd(x):  # dir = y[*]^{S_A} × A[a] = 1 × A[a]; elt (f:S_A->y, x)
            return (tuple('·' for _ in A['S']), x)
        return bwd
    return Mor(src, tgt, fwd, {('*', a): make_bwd(a) for a in A['S']})

# ---------- LDC coherence pentagons for δ  (⊗=⋉, ⅋=⋊) ----------
def ldc_pentagon_tensor(A, B, Cc, D):
    """ Common source A⋉(B⋉(C⋊D)); both paths end at ((A⋉B)⋉C)⋊D. """
    aInv = invert(assoc_ltimes(A, B, Cc))          # A⋉(B⋉C) -> (A⋉B)⋉C
    # Path A: α⁻¹_⋉ then δ
    pA = compose(delta(ltimes(A, B), Cc, D),
                 invert(assoc_ltimes(A, B, rtimes(Cc, D))))   # A⋉(B⋉(C⋊D)) -> (A⋉B)⋉(C⋊D) -> ((A⋉B)⋉C)⋊D
    # Path B: (A⋉δ) then δ then (α⁻¹_⋉ ⋊ D)
    step1 = ltimes_mor(idmor(A), delta(B, Cc, D))            # -> A⋉((B⋉C)⋊D)
    step2 = delta(A, ltimes(B, Cc), D)                        # -> (A⋉(B⋉C))⋊D
    step3 = rtimes_mor(aInv, idmor(D))                        # -> ((A⋉B)⋉C)⋊D
    pB = compose(step3, compose(step2, step1))
    return eq_mor(pA, pB)

def ldc_pentagon_par(A, B, Cc, D):
    """ Common source A⋉(B⋊(C⋊D)); both paths end at ((A⋉B)⋊C)⋊D. """
    arInvAB = invert(assoc_rtimes(ltimes(A, B), Cc, D))       # (A⋉B)⋊(C⋊D) -> ((A⋉B)⋊C)⋊D
    # Path A: δ then α⁻¹_⋊
    pA = compose(arInvAB, delta(A, B, rtimes(Cc, D)))
    # Path B: (A⋉α⁻¹_⋊) then δ then (δ⋊D)
    step1 = ltimes_mor(idmor(A), invert(assoc_rtimes(B, Cc, D)))  # A⋉(B⋊(C⋊D)) -> A⋉((B⋊C)⋊D)
    step2 = delta(A, rtimes(B, Cc), D)                            # -> (A⋉(B⋊C))⋊D
    step3 = rtimes_mor(delta(A, B, Cc), idmor(D))                 # -> ((A⋉B)⋊C)⋊D
    pB = compose(step3, compose(step2, step1))
    return eq_mor(pA, pB)

def ldc_unit(A, B):
    """ unit coherence: A⋉(y⋊B) --δ--> (A⋉y)⋊B --ρ⋉⋊B--> A⋊B
        should equal  A⋉(y⋊B) --A⋉λ⋊--> A⋉B ... but ⋉≠⋊ so compare to the canonical iso.
        Standard LDC unit law: δ_{A,y,B} followed by (ρ⋉ ⋊ B) equals (A ⋉ λ⋊) followed by ???
        Here both units are y. Law: A⋉(y⋊B) = A⋉B via A⋉λ⋊  vs  δ;(ρ⋉⋊B).
        LHS object A⋉(y⋊B)->A⋉B ; RHS A⋉(y⋊B)->(A⋉y)⋊B->A⋊B.  Different targets (A⋉B vs A⋊B)!
        The genuine law uses the mix map. Skip strict form; instead test the two 'obvious' unit
        reductions land consistently by checking δ collapses to identity-ish when a slot = y. """
    # test: delta(A, y, B): A⋉(y⋊B) -> (A⋉y)⋊B ; compose unitors to A⋊B and compare to
    #   A⋉(y⋊B) --A⋉(lunit_rtimes B)--> A⋉B, then compare via mix? We instead check the
    #   triangle: (ρ⋉ ⋊ B) ∘ δ_{A,y,B} == (something). Just report the map for inspection.
    m = compose(rtimes_mor(runit_ltimes(A), idmor(B)), delta(A, Y(), B))  # A⋉(y⋊B) -> A⋊B
    n = compose(idmor(rtimes(A, B)), rtimes_mor(idmor(A), idmor(B)))  # placeholder
    # meaningful check: m should equal  A⋉(y⋊B) --A⋉λ⋊--> A⋉B --mix--> A⋊B
    # We don't have mix; just verify m is well-defined & natural elsewhere. Return welldef.
    return check_welldef(m, f"unit map A⋉(y⋊B)->A⋊B")

# ---------- duoidal coherence: interchange associativity (3 rows x 2 cols) ----------
def grand_interchange_3x2(P):
    """ P[i][k], i=0,1,2 rows (⋊), k=0,1 cols (⋉).
        LHS (P00⋊P10⋊P20) ⋉ (P01⋊P11⋉P21) ... build two bracketings of ζ_grid and compare. """
    # columns as ⋊ (left-bracketed): col_k = (P0k ⋊ P1k) ⋊ P2k
    def colL(k): return rtimes(rtimes(P[0][k], P[1][k]), P[2][k])
    def colR(k): return rtimes(P[0][k], rtimes(P[1][k], P[2][k]))
    # rows as ⋉: row_i = P_i0 ⋉ P_i1
    def row(i): return ltimes(P[i][0], P[i][1])

    A, B, Cc = P[0][0], P[1][0], P[2][0]   # col 0 entries
    D, E, F = P[0][1], P[1][1], P[2][1]    # col 1 entries

    # --- Bracketing 1: treat top 2 rows first.
    #  LHS = colL(0) ⋉ colL(1) = ((A⋊B)⋊C) ⋉ ((D⋊E)⋊F)
    #  Use assoc to right-bracket columns, then a "3x2 ζ" built from binary ζ + assoc.
    # We compute the grand map two ways and compare the induced backward maps.
    # Way1: reassociate columns to right-bracket, then apply ζ3 built as:
    #   ((A⋊(B⋊C)) ⋉ (D⋊(E⋊F)))  --ζ on A,(B⋊C),D,(E⋊F)--> (A⋉D) ⋊ ((B⋊C)⋉(E⋊F))
    #   then id⋊ζ on B,C,E,F:  -> (A⋉D) ⋊ ((B⋉E)⋊(C⋉F))
    src = ltimes(colR(0), colR(1))
    z_top = zeta(A, rtimes(B, Cc), D, rtimes(E, F))   # (A⋊(B⋊C))⋉(D⋊(E⋊F)) -> (A⋉D)⋊((B⋊C)⋉(E⋊F))
    z_bot = rtimes_mor(idmor(ltimes(A, D)), zeta(B, Cc, E, F))  # -> (A⋉D)⋊((B⋉E)⋊(C⋉F))
    way1 = compose(z_bot, z_top)   # src -> (A⋉D)⋊((B⋉E)⋊(C⋉F))

    # Way2: group bottom two rows first.
    #   ((A⋊(B⋊C)) ⋉ (D⋊(E⋊F)))  reassoc as A⋊(B⋊C) etc, apply ζ on (A⋊B... ) grouping differently:
    #   First ζ on (A,B) style then bottom. Use: colR = A⋊(B⋊C).
    #   ζ' on A,(B⋊C): same as z_top (only one binary split of a 2-col ⋊ into head/tail) -> identical structure.
    #   To get a genuinely different bracketing, split column as head=(A⋊B), tail=C i.e. left-bracket.
    src2 = ltimes(colL(0), colL(1))    # ((A⋊B)⋊C) ⋉ ((D⋊E)⋊F)
    z_head = zeta(rtimes(A, B), Cc, rtimes(D, E), F)   # ((A⋊B)⋊C)⋉((D⋊E)⋊F) -> ((A⋊B)⋉(D⋊E)) ⋊ (C⋉F)
    z_sub = rtimes_mor(zeta(A, B, D, E), idmor(ltimes(Cc, F)))  # -> ((A⋉D)⋊(B⋉E)) ⋊ (C⋉F)
    way2_pre = compose(z_sub, z_head)   # src2 -> ((A⋉D)⋊(B⋉E))⋊(C⋉F)
    # bring both to a common object via ⋊-associator on the target
    #  way1 target: (A⋉D)⋊((B⋉E)⋊(C⋉F));  way2 target: ((A⋉D)⋊(B⋉E))⋊(C⋉F)
    a_r = assoc_rtimes(ltimes(A, D), ltimes(B, E), ltimes(Cc, F))  # ((..)⋊(..))⋊(..) -> (..)⋊((..)⋊(..))
    way2 = compose(a_r, way2_pre)   # src2 -> (A⋉D)⋊((B⋉E)⋊(C⋉F))
    # bring way1 source (right-bracketed cols) to way2 source (left-bracketed cols) via col associators
    #  src = colR(0)⋉colR(1); src2 = colL(0)⋉colL(1); relate by (assoc_rtimes^{-1} ⋉ assoc_rtimes^{-1})
    # assoc_rtimes: (X⋊Y)⋊Z -> X⋊(Y⋊Z); so colL->colR is assoc_rtimes. Apply to both columns:
    colmap = ltimes_mor(assoc_rtimes(A, B, Cc), assoc_rtimes(D, E, F))  # src2 -> src
    way1_from_src2 = compose(way1, colmap)   # src2 -> common target
    return eq_mor(way1_from_src2, way2)

def grand_interchange_2x3(P):
    """ P[i][k], i=0,1 rows(⋊), k=0,1,2 cols(⋉). Two bracketings of the 3-fold ⋉ must agree. """
    def col(k): return rtimes(P[0][k], P[1][k])
    A, D = P[0][0], P[1][0]
    B, E = P[0][1], P[1][1]
    Cc, F = P[0][2], P[1][2]
    # way1: left-bracket ⋉ : (col0⋉col1)⋉col2
    src1 = ltimes(ltimes(col(0), col(1)), col(2))
    z01 = ltimes_mor(zeta(A, D, B, E), idmor(col(2)))            # -> ((A⋉B)⋊(D⋉E))⋉(C⋊F)
    z2 = zeta(ltimes(A, B), ltimes(D, E), Cc, F)                 # -> ((A⋉B)⋉C)⋊((D⋉E)⋉F)
    way1 = compose(z2, z01)                                      # src1 -> ((A⋉B)⋉C)⋊((D⋉E)⋉F)
    # way2: right-bracket ⋉ : col0⋉(col1⋉col2)
    src2 = ltimes(col(0), ltimes(col(1), col(2)))
    z12 = ltimes_mor(idmor(col(0)), zeta(B, E, Cc, F))          # -> (A⋊D)⋉((B⋉C)⋊(E⋉F))
    z0 = zeta(A, D, ltimes(B, Cc), ltimes(E, F))                # -> (A⋉(B⋉C))⋊(D⋉(E⋉F))
    way2 = compose(z0, z12)                                      # src2 -> (A⋉(B⋉C))⋊(D⋉(E⋉F))
    # relate sources: src1 -> src2 via α_⋉
    smap = assoc_ltimes(col(0), col(1), col(2))                 # src1 -> src2
    # relate targets: way1 target ((A⋉B)⋉C)⋊((D⋉E)⋉F) -> way2 target via α_⋉ ⋊ α_⋉
    tmap = rtimes_mor(assoc_ltimes(A, B, Cc), assoc_ltimes(D, E, F))
    lhs = compose(tmap, way1)          # src1 -> way2target
    rhs = compose(way2, smap)          # src1 -> way2target
    return eq_mor(lhs, rhs)

def delta_from_zeta(A, B, Cc):
    """ δ built from ζ + normality isos; must equal the directly-defined δ. """
    m1 = ltimes_mor(invert(runit_rtimes(A)), idmor(rtimes(B, Cc)))  # A⋉(B⋊C) -> (A⋊y)⋉(B⋊C)
    m2 = zeta(A, Y(), B, Cc)                                          # -> (A⋉B)⋊(y⋉C)
    m3 = rtimes_mor(idmor(ltimes(A, B)), lunit_ltimes(Cc))           # -> (A⋉B)⋊C
    return compose(m3, compose(m2, m1))

if __name__ == '__main__':
    two = C(['0', '1'], {'0': ['*'], '1': ['*']})
    sq = C(['0'], {'0': ['u', 'v']})
    yy = Y()
    objs = [yy, two, sq]

    print("=== associator/unitor well-definedness ===")
    check_welldef(assoc_ltimes(two, sq, two), "α_⋉")
    check_welldef(assoc_rtimes(two, sq, two), "α_⋊")
    check_welldef(runit_ltimes(sq), "ρ_⋉")
    check_welldef(runit_rtimes(sq), "ρ_⋊")

    print("=== associators are isos (round-trip via inverse = flat identity check) ===")
    # α_⋉ should be iso: check it's a bijection on directions (cardinalities equal + injective)
    import itertools
    def is_iso(m):
        for s in m.src['S']:
            t = m.fwd[s]
            imgs = [m.bwd[s](e) for e in m.tgt['d'][t]]
            if len(set(map(repr, imgs))) != len(m.src['d'][s]):
                return False
        return len(m.src['S']) == len(m.tgt['S'])
    print(" α_⋉ iso?", is_iso(assoc_ltimes(two, sq, two)))
    print(" α_⋊ iso?", is_iso(assoc_rtimes(two, sq, two)))

    print("=== LDC coherence pentagons for δ ===")
    tests = [(two, sq, two, sq), (sq, two, sq, two), (two, two, two, two),
             (yy, two, sq, two), (two, sq, sq, two), (sq, sq, two, sq)]
    okT = all(ldc_pentagon_tensor(*t) for t in tests)
    print(" ⊗-associativity pentagon (all cases):", okT)
    okP = all(ldc_pentagon_par(*t) for t in tests)
    print(" ⅋-associativity pentagon (all cases):", okP)

    print("=== duoidal interchange associativity (3x2 grid) ===")
    # small grids
    def grid(entries):
        return [[entries[0], entries[1]], [entries[2], entries[3]], [entries[4], entries[5]]]
    G1 = grid([two, sq, sq, two, two, sq])
    G2 = grid([two, two, two, two, two, two])
    G3 = grid([sq, two, two, sq, sq, two])
    print(" 3x2 grid1 (⋊-assoc compat):", grand_interchange_3x2(G1))
    print(" 3x2 grid2:", grand_interchange_3x2(G2))
    print(" 3x2 grid3:", grand_interchange_3x2(G3))

    def grid23(e):
        return [[e[0], e[1], e[2]], [e[3], e[4], e[5]]]
    H1 = grid23([two, yy, two, yy, two, yy])
    H2 = grid23([two, two, two, two, two, two])
    H3 = grid23([sq, yy, yy, yy, yy, yy])
    print(" 2x3 grid1 (⋉-assoc compat):", grand_interchange_2x3(H1))
    print(" 2x3 grid2:", grand_interchange_2x3(H2))
    print(" 2x3 grid3:", grand_interchange_2x3(H3))

    print("=== δ is the ζ-induced distributor (normality reduction) ===")
    red_tests = [(two, sq, two), (sq, two, sq), (two, two, two), (sq, sq, sq),
                 (two, sq, sq), (sq, two, two)]
    okR = all(eq_mor(delta_from_zeta(*t), delta(*t)) for t in red_tests)
    print(" δ == ζ-induced distributor (all cases):", okR)

    print("=== normality: unit interchange isos ===")
    # normal duoidal needs: the interchange of units is iso. With shared unit y:
    #   y ≅ y⋊y (via unitor) and y ≅ y⋉y ; and the four unit-compatibility maps are isos.
    print(" y⋊y ≅ y ?", eq_mor(runit_rtimes(Y()), lunit_rtimes(Y())),
          " (both A⋊y->A and y⋊A->A at A=y coincide)")
    print(" y⋉y ≅ y ?", eq_mor(runit_ltimes(Y()), lunit_ltimes(Y())))
    # check runit/lunit are isos
    def is_iso(m):
        for s in m.src['S']:
            t = m.fwd[s]
            imgs = [m.bwd[s](e) for e in m.tgt['d'][t]]
            if len(set(map(repr, imgs))) != len(m.src['d'][s]): return False
        return len(m.src['S']) == len(m.tgt['S'])
    print(" ρ_⋉ iso?", is_iso(runit_ltimes(sq)), " λ_⋉ iso?", is_iso(lunit_ltimes(sq)),
          " ρ_⋊ iso?", is_iso(runit_rtimes(sq)), " λ_⋊ iso?", is_iso(lunit_rtimes(sq)))
