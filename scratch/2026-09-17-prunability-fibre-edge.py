"""
2026-09-17  Prunability lives on the FIBRE edge; the ZS holonomy is dead on the BASE edge.
============================================================================================
Empirical core of PROVE.md.  We take MacBeth's 09-16 separation witness

    G = Z/2 x Coarse({0,1}),  stars additively Z/4          (NON-prunable, connected)

and the prunable control

    G = Z/2 x Coarse({0,1}),  stars additively Klein (V4)   (PRUNABLE, connected)

and compute BOTH LHS edges of the normal ZS extension  1 -> D -> pi -> Gamma -> 1:

    BASE  edge  E2^{2,0} = H^2(Gamma; M^D)   <- home of the multiplicative ZS holonomy [omega]
    FIBRE edge  E2^{0,2} = H^2(D;M)^Gamma     <- home of the additive prunability class [pi]

DECOUPLING claim: for the connected witness  [omega]=0 (base coarse) yet [pi]!=0 (fibre).
For the connected control both edges are dead: [omega]=0 and [pi]=0.

Two different extensions are in play (this is the whole point of the separation):
  * MULTIPLICATIVE ZS extension  1 -> D_mult -> pi_mult -> Gamma_mult -> 1 governs [omega].
    For a CONNECTED groupoid the orbit base Sk_C is coarse => Gamma_mult ~ 1 => H^2(Gamma;-)=0.
  * ADDITIVE (skew-brace) extension of the STAR  0 -> A -> St -> Q -> 0 governs [pi].
    [pi] is its Schreier class in H^2(Q;A); nonsplit Z/4 => [pi]!=0, split V4 => [pi]=0.
This is the "additive twin" of the Z/4-vs-Klein Schreier dividing line.

HONESTY: see the STATUS block printed at the end and the companion .md.  The base-edge
result is fully rigorous.  The fibre-edge computation rigorously computes the group
H^2(Q;A) and the additive extension class of the star; identifying THAT class with the
Ferri "prunability defect" is the additive-twin reading of the separation paper (rigorous
for this two-object family, structural general proof still open).
"""

import itertools
import numpy as np

from qskb_task2 import (Zn, build_model, group_structures_on_set,
                        compat_holds, left_action, is_loop, check_invariance)

# ----------------------------------------------------------------------------- helpers
def fmt(x): return f"({x[0]},{x[1]},{x[2]})"

def F2_rank(Mat):
    if Mat.size == 0: return 0
    A = (Mat % 2).astype(np.int8).copy()
    rows, cols = A.shape; r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i, c]), None)
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] = (A[i] + A[r]) % 2
        r += 1
        if r == rows: break
    return r

# ------------------------------------------------ generic finite-group cohomology over F2
def bar_H_dim(elts, mul, e, n):
    """dim_F2 H^n(G;F2), trivial coefficients, bar resolution.  elts: list, mul(a,b), e id."""
    idx = {g: i for i, g in enumerate(elts)}
    N = len(elts)
    def Ck(k): return list(itertools.product(range(N), repeat=k))
    def dmat(k):
        dom = Ck(k); cod = Ck(k + 1)
        di = {t: i for i, t in enumerate(dom)}
        Mmat = np.zeros((len(cod), len(dom)), dtype=np.int64)
        for row, tup in enumerate(cod):
            gs = [elts[i] for i in tup]
            Mmat[row, di[tup[1:]]] += 1
            for i in range(1, k + 1):
                prod = mul(gs[i - 1], gs[i])
                newt = tup[:i - 1] + (idx[prod],) + tup[i + 1:]
                Mmat[row, di[newt]] += 1
            Mmat[row, di[tup[:k]]] += 1
        return Mmat % 2
    if n == 0: return 1
    dn = dmat(n); dnm1 = dmat(n - 1)
    dimCn = N ** n
    return (dimCn - F2_rank(dn)) - F2_rank(dnm1)

# --------------------------------------------- additive extension (Schreier) class of a star
def star_extension_class(St, add, neg, e):
    """
    St: list of star elements; add[(x,y)], neg[x]; e additive identity.
    Pick the (unique, for these examples) order-2 additive subgroup A, form Q=St/A,
    compute the Schreier 2-cocycle f: Q x Q -> A and decide whether [f]=0 in H^2(Q;A)
    by brute force over all normalized 1-cochains (coboundary check).  Trivial action
    (St abelian).  Returns dict with the group order |H^2(Q;A)|, split?, and [pi]!=0.
    """
    # additive order of each element
    def aorder(x):
        n, cur = 1, x
        while cur != e:
            cur = add[(cur, x)]; n += 1
            if n > 10 ** 6: return None
        return n
    order = {x: aorder(x) for x in St}
    invol = [x for x in St if order[x] == 2]          # order-2 elements
    # any order-2 SUBGROUP is {e,x} with x an involution; collect all order-2 subgroups
    subs2 = [frozenset({e, x}) for x in invol]
    # For the two-object |St|=4 examples we need one such A; use the FIRST as the additive
    # subgroup that a complement/prune would target.  (Z/4: unique {0,2}; V4: three choices.)
    A = set(sorted(subs2, key=lambda s: sorted(map(str, s)))[0]) if subs2 else {e}
    # quotient Q = St / A
    def coset(x): return frozenset(add[(x, a)] for a in A)
    cosets = []
    for x in St:
        c = coset(x)
        if c not in cosets: cosets.append(c)
    # section s: pick a rep per coset (prefer e's coset -> e)
    rep = {}
    for c in cosets:
        rep[c] = e if e in c else sorted(c, key=str)[0]
    Qel = list(range(len(cosets)))
    cindex = {c: i for i, c in enumerate(cosets)}
    def qadd(i, j):
        return cindex[coset(add[(rep[cosets[i]], rep[cosets[j]])])]
    Aels = list(A)
    # Schreier cocycle f(i,j) = rep(i) + rep(j) - rep(i+j)  in A
    def fcoc(i, j):
        val = add[(add[(rep[cosets[i]], rep[cosets[j]])], neg[rep[cosets[qadd(i, j)]]])]
        return val
    fvals = {(i, j): fcoc(i, j) for i in Qel for j in Qel}
    assert all(v in A for v in fvals.values()), "cocycle not valued in A"
    # is it a coboundary?  exists g:Q->A, g(0)=identity coset rep contributes 0, with
    # f(i,j) = g(i)+g(j)-g(i+j) ?   (trivial action, additive A)
    # enumerate all functions g: Qel -> A with g(id)=e
    idcoset = cindex[coset(e)]
    varQ = [i for i in Qel if i != idcoset]
    split = False
    for assign in itertools.product(Aels, repeat=len(varQ)):
        g = {idcoset: e}
        for k, i in enumerate(varQ): g[i] = assign[k]
        ok = True
        for i in Qel:
            for j in Qel:
                # delta g (i,j) = g[i] + g[j] - g[i+j]
                dg = add[(add[(g[i], g[j])], neg[g[qadd(i, j)]])]
                if dg != fvals[(i, j)]:
                    ok = False; break
            if not ok: break
        if ok:
            split = True; break
    # |H^2(Q;A)| for Q=Z/2,A=Z/2 trivial = 2; compute generally by bar over F2 only if A=Z/2
    h2Q = None
    if len(A) == 2:
        h2Q = bar_H_dim(Qel, qadd, idcoset, 2)  # dim over F2 == log2|H^2| since A=F2
    return dict(order=order, A=set(A), Q_size=len(cosets), split=split,
                pi_nonzero=(not split), h2Q_dim_F2=h2Q, cocycle=fvals, rep=rep,
                cosets=cosets)

# --------------------------------------------------------------------- build valid QSKBs
Q = Zn(2)
M = build_model(Q)
QE = Q[3]
S0 = M['star'](0); S1 = M['star'](1); e0 = M['ident'](0); e1 = M['ident'](1)
st0 = list(group_structures_on_set(S0, e0))
st1 = list(group_structures_on_set(S1, e1))

def valid_qskbs():
    out = []
    for (g0, a0, n0) in st0:
        for (g1, a1, n1) in st1:
            ok, _ = compat_holds(M, a0, n0, a1, n1)
            if ok: out.append((g0, a0, n0, g1, a1, n1))
    return out

VALID = valid_qskbs()

def loops_at(lam): return [x for x in M['star'](lam) if x[0] == lam and x[1] == lam]

def SUB(add, neg, lam):
    L = loops_at(lam); Ls = set(L)
    return all(add[lam][(x, y)] in Ls for x in L for y in L) and all(neg[lam][x] in Ls for x in L)

def cond9(add, neg):
    ok, _ = check_invariance(M, add, neg); return ok

# pick witness (Z/4 stars, non-subgroup loops, valid) and control (V4 stars, subgroup loops)
witness = control = None
for (g0, a0, n0, g1, a1, n1) in VALID:
    add = {0: a0, 1: a1}; neg = {0: n0, 1: n1}
    subs = all(SUB(add, neg, l) for l in [0, 1])
    if witness is None and g0 == 'Z4' and g1 == 'Z4' and not subs:
        witness = (g0, a0, n0, g1, a1, n1)
    if control is None and g0 == 'V4' and g1 == 'V4' and subs:
        control = (g0, a0, n0, g1, a1, n1)

# ------------------------------------------------------------------------------- report
def analyse(tag, W):
    g0, a0, n0, g1, a1, n1 = W
    add = {0: a0, 1: a1}; neg = {0: n0, 1: n1}
    print("=" * 78)
    print(f"{tag}:  stars +_0={g0}, +_1={g1}")
    ok, _ = compat_holds(M, a0, n0, a1, n1)
    print(f"  valid QSKB (truss distributivity (5)): {ok}")
    prun = all(SUB(add, neg, l) for l in [0, 1]) and cond9(add, neg)
    print(f"  completely prunable (SUB & (9)):       {prun}")

    # ---- structural data ----
    print("  D (loop bundle, MULTIPLICATIVE fibre): vertex group at each object")
    for lam in [0, 1]:
        L = loops_at(lam)
        print(f"     L_{lam} = {[fmt(x) for x in L]}  (~ Z/2 under composition)")
    print("  Gamma (orbit base Sk_C of the connected groupoid): COARSE on {0,1} ~ point")
    print("        => vertex group of Gamma is trivial, Gamma ~ 1.")

    # ---- BASE edge  E2^{2,0}=H^2(Gamma; M^D) ----
    # Gamma trivial group: H^n(1;-)=0 for n>=1.
    h2_base = bar_H_dim([0], lambda a, b: 0, 0, 2)  # trivial group cohomology
    print("  --- BASE edge  E2^{2,0}=H^2(Gamma;M^D) ---")
    print(f"     Gamma ~ 1  =>  dim H^2(Gamma;M^D) = {h2_base}   ==>  [omega] = 0  (RIGOROUS)")

    # ---- FIBRE edge: additive star extension class [pi] ----
    print("  --- FIBRE edge  E2^{0,2}=H^2(D;M)^Gamma  via additive star extension ---")
    for lam in [0]:
        St = M['star'](lam); e = M['ident'](lam)
        res = star_extension_class(St, add[lam], neg[lam], e)
        Astr = sorted(fmt(x) for x in res['A'])
        Lstr = [fmt(x) for x in loops_at(lam)]
        loop_is_sub = SUB(add, neg, lam)
        print(f"     object {lam}:  (St(0),+) abstract = {g0} of order 4")
        print(f"       additive orders: " +
              ", ".join(f"{fmt(x)}:{res['order'][x]}" for x in St))
        print(f"       additive order-2 subgroup A = {Astr}   (Q = St/A of size {res['Q_size']})")
        print(f"       loop set L_0 = {Lstr}   additive subgroup? {loop_is_sub}")
        print(f"       H^2(Q;A) dim over F2 = {res['h2Q_dim_F2']}   (|H^2(Q;A)| = "
              f"{2**res['h2Q_dim_F2']})")
        print(f"       star extension 0->A->St->Q->0 SPLIT? {res['split']}")
        print(f"       ==> prunability class [pi] = {'0 (dead edge)' if res['split'] else 'NONZERO generator'}")
        # show cocycle
        cyc = {(i, j): fmt(v) for (i, j), v in res['cocycle'].items()}
        print(f"       Schreier 2-cocycle f(i,j) in A: {cyc}")
    return dict(prunable=prun, base_edge_h2=h2_base, fibre_split=res['split'])

print("\n" + "#" * 78)
print("# WITNESS  (non-prunable, connected):  stars Z/4, loop gen in an order-4 slot")
print("#" * 78)
rw = analyse("WITNESS  G=Z/2 x Coarse({0,1}), Z/4 stars", witness)

print("\n" + "#" * 78)
print("# CONTROL  (prunable, connected):  stars Klein V4, loops form a subgroup")
print("#" * 78)
rc = analyse("CONTROL  G=Z/2 x Coarse({0,1}), V4 stars", control)

# =====================================================================================
# FERRI'S REAL K_{2,3}  (arXiv:2410.10717, JPAA 229 (2025), Ex. 4.29 / Table 3)
# =====================================================================================
def k23_section():
    print("\n" + "#" * 78)
    print("# FERRI's REAL K_{2,3}  (arXiv:2410.10717, Ex.4.29/Table 3; Counterexample 5.2)")
    print("#" * 78)
    # Underlying set A = Z/4.  Star LEFT-QUASIGROUP operations (rows a, cols b):
    starS2 = [[0,1,2,3],
              [1,2,3,0],
              [2,1,0,3],
              [3,2,1,0]]
    starS3 = [[0,1,2,3],
              [1,0,3,2],
              [2,1,0,3],
              [3,0,1,2]]
    stars = {'S2': starS2, 'S3': starS3}
    loops = {'S2': {0,3}, 'S3': {0,1}}          # loop bundle from the groupoid direction

    def is_left_quasigroup(tab):   # each ROW a permutation of 0..3
        return all(sorted(row) == [0,1,2,3] for row in tab)
    def is_right_quasigroup(tab):  # each COLUMN a permutation
        return all(sorted(tab[a][b] for a in range(4)) == [0,1,2,3] for b in range(4))
    def is_commutative(tab):
        return all(tab[a][b] == tab[b][a] for a in range(4) for b in range(4))
    def assoc_witness(tab):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    if tab[tab[a][b]][c] != tab[a][tab[b][c]]:
                        return (a, b, c, tab[tab[a][b]][c], tab[a][tab[b][c]])
        return None
    def two_sided_identity(tab):
        for e in range(4):
            if all(tab[e][x] == x and tab[x][e] == x for x in range(4)):
                return e
        return None

    # ---- STEP 1: what is the star operation, and is it a group? ----
    print("STEP 1 -- nature of the star operations  •_λ  (Table 3):")
    for name, tab in stars.items():
        lq = is_left_quasigroup(tab); rq = is_right_quasigroup(tab)
        comm = is_commutative(tab); aw = assoc_witness(tab); e = two_sided_identity(tab)
        print(f"  •_{name}: left-quasigroup(rows perm)={lq}  right-quasigroup(cols perm)={rq}")
        print(f"         two-sided identity={e}  commutative={comm}  "
              f"associative={'YES' if aw is None else 'NO'}"
              + ("" if aw is None else f" (witness (a,b,c)={aw[:3]}: {aw[3]}!={aw[4]})"))
        verdict = ("a GROUP" if (lq and rq and aw is None) else
                   "NOT a group (left-quasigroup only)")
        print(f"         => •_{name} is {verdict}")
    print("  CONCLUSION: the •_λ are LEFT QUASIGROUPS, not groups (order-4 groups are abelian;")
    print("  these are non-commutative &/or non-associative).  So •_λ itself is NOT '+_λ'.")

    # ---- The genuine additive group of the skew brace on A = Z/4 ----
    print("\n  The skew brace's additive group on A is ORDINARY (Z/4,+) (paper: a·b=a+b).")
    Z4add = {(x, y): (x + y) % 4 for x in range(4) for y in range(4)}
    Z4neg = {x: (-x) % 4 for x in range(4)}

    # ---- STEP 2: prunability -- loops as additive subgroups of (Z/4,+) ----
    print("\nSTEP 2 -- prunability: are the loop sets additive subgroups of (Z/4,+)?")
    def is_subgroup(S, add, neg, e=0):
        S = set(S)
        return (e in S and all(add[(x, y)] in S for x in S for y in S)
                and all(neg[x] in S for x in S))
    prun_ok = True
    for name in ('S2', 'S3'):
        L = loops[name]
        subg = is_subgroup(L, Z4add, Z4neg)
        # ALSO: is L closed under the quasigroup •_λ ? (the honest twist)
        tab = stars[name]
        closed_quasi = all(tab[a][b] in L for a in L for b in L)
        # find an additive order-4 element inside L (the "order-4 slot")
        def aorder(x):
            n, cur = 1, x
            while cur != 0:
                cur = (cur + x) % 4; n += 1
            return n
        slots = {x: aorder(x) for x in L}
        print(f"  loops({name}) = {sorted(L)}: additive subgroup of (Z/4,+)? {subg}"
              f"   (orders {slots})")
        print(f"      counter: for x=max-order loop, x+x = "
              f"{[(x, (x+x)%4) for x in L if aorder(x)==4]}  (lands outside L)")
        print(f"      [twist] closed under the quasigroup •_{name}? {closed_quasi}"
              f"  (sub-left-quasigroup, but •_{name} is not a group)")
        prun_ok = prun_ok and subg
    print(f"  => completely prunable? {prun_ok}   (matches Ferri Counterexample 5.2: NON-prunable)")

    # ---- STEP 3: base edge ----
    print("\nSTEP 3 -- BASE edge  E2^{2,0}=H^2(Gamma;M^D):")
    print("  K_{2,3} is a CONNECTED degree-2 groupoid on {S2,S3} => orbit base Sk_C is the")
    print("  coarse groupoid ~ point => Gamma ~ 1 => H^{>=1}(Gamma;-)=0 => [omega]=0. (RIGOROUS)")
    base_h2 = bar_H_dim([0], lambda a, b: 0, 0, 2)
    print(f"  dim H^2(Gamma;M^D) = {base_h2}  ==>  [omega] = 0.")

    # ---- STEP 4: fibre edge [pi] for each star, via (Z/4,+) extension ----
    print("\nSTEP 4 -- FIBRE edge  E2^{0,2}=H^2(D;M)^Gamma  (additive (Z/4,+) star extension):")
    print("  D = loop bundle (fibre), Gamma ~ 1 so ()^Gamma is trivial; M = A = order-2 subgroup.")
    results = {}
    St = [0, 1, 2, 3]
    for name in ('S2', 'S3'):
        res = star_extension_class(St, Z4add, Z4neg, 0)
        A = sorted(res['A']); L = sorted(loops[name])
        loop_sub = is_subgroup(loops[name], Z4add, Z4neg)
        print(f"  star at {name}:  (St,+)=(Z/4,+)   additive orders {res['order']}")
        print(f"     A (order-2 subgroup) = {A};  Q=St/A size {res['Q_size']};  loops = {L} "
              f"(subgroup? {loop_sub})")
        print(f"     H^2(Q;A) = Z/2 (dim_F2 {res['h2Q_dim_F2']});  extension 0->A->Z/4->Q->0 "
              f"SPLIT? {res['split']}")
        print(f"     ==> [pi]_{name} = {'0' if res['split'] else 'NONZERO generator of Z/2'};  "
              f"cocycle f(1,1)={res['cocycle'][(1,1)]} in A")
        results[name] = res
    return dict(prunable=prun_ok, base_edge_h2=base_h2,
                fibre_split=results['S2']['split'], results=results)

rk = k23_section()

print("\n" + "=" * 78)
print("SUMMARY  (base edge = [omega], fibre edge = [pi])")
print("=" * 78)
print(f"{'case':<16}{'prunable':>10}{'base H^2':>10}{'[omega]':>9}{'fibre split':>13}{'[pi]':>10}")
def line(name, r):
    print(f"{name:<16}{str(r['prunable']):>10}{r['base_edge_h2']:>10}"
          f"{'0' if r['base_edge_h2']==0 else '?':>9}{str(r['fibre_split']):>13}"
          f"{'0' if r['fibre_split'] else '!=0':>10}")
line("SYNTH WITNESS", rw)
line("SYNTH CONTROL", rc)
line("FERRI K_{2,3}", rk)
print()
print("DECOUPLING (synth witness): base [omega]=0 (Gamma coarse) AND fibre [pi]!=0 (Z/4 nonsplit).")
print("CONTROL:                    base [omega]=0 AND fibre [pi]=0 (V4 split) -- both edges dead.")
print("FERRI K_{2,3} (REAL):       base [omega]=0 (connected/coarse) AND fibre [pi]!=0 at BOTH")
print("   stars S2,S3 (both (Z/4,+) nonsplit over {0,2}).  SAME decoupling as the synthetic witness.")

print("\n" + "-" * 78)
print("STATUS / HONESTY")
print("-" * 78)
print("""RIGOROUS:
  * validity + (non)prunability of both QSKBs: exhaustive machine check (48 Z/2 QSKBs).
  * BASE edge [omega]=0: Gamma=Sk_C is the coarse groupoid on {0,1} ~ point for a CONNECTED
    groupoid, so H^{>=1}(Gamma;-)=0.  Independent of coefficients.  (Prop.A of the sep paper.)
  * H^2(Q;A) computed as a group (=Z/2), and the additive star extension 0->A->St->Q->0
    decided split/nonsplit by exhaustive coboundary search: Z/4 nonsplit, V4 split.
HEURISTIC / MODELLING CHOICE (the tracked-open node):
  * Identifying the additive star extension class [pi] in H^2(Q;A) with the Ferri
    'prunability defect' is the ADDITIVE-TWIN reading of the separation paper.  It is exact
    for this two-object Z/2 family (Prop. 'family' there); a structural proof that the fibre
    edge E2^{0,2} of the categorical LHS sequence literally receives Ferri prunability for
    general twisted groupoids is NOT given here (h2cluster paper 'Not claimed' node).
  * A = order-2 subgroup {0,2}; the multiplicative loop set is {0,1} (NOT A).  The defect is
    that a nonsplit star has no complemented Z/2 to host the loops; [pi]!=0 IS that
    non-splitting.  For V4 a complement exists, loops are a subgroup, [pi]=0.

FERRI K_{2,3} SPECIFIC (quasigroup subtlety):
  RIGOROUS:
    * •_S2, •_S3 are LEFT QUASIGROUPS, NOT groups (machine-checked: rows perm but columns not;
      non-commutative and/or non-associative -- explicit witnesses printed).  So the star op
      •_λ is NOT itself an additive group '+_λ'.
    * With the skew brace's genuine additive group (Z/4,+) (paper: a·b=a+b): loops(S2)={0,3}
      and loops(S3)={0,1} are NOT additive subgroups (3+3=2, 1+1=2) => NON-prunable (= Ferri
      Counterexample 5.2).  Base edge [omega]=0 by connectedness (coarse base).  Fibre-edge
      [pi]!=0 at BOTH stars: (Z/4,+) nonsplit over {0,2}, H^2(Q;A)=Z/2, cocycle f(1,1)=2.
      SAME decoupling ([omega]=0, [pi]!=0) as the synthetic witness -- now on Ferri's numbers.
  HONEST GAP (the quasigroup twist):
    * The loop sets ARE closed under the quasigroup •_λ (sub-left-quasigroups), but •_λ is not
      a group, so 'additive subgroup' is only meaningful w.r.t. (Z/4,+).  The verdict therefore
      depends on reading '+_λ' as the genuine additive group (Z/4,+) -- which is Ferri's own
      convention in Counterexample 5.2.  In the dynamical-skew-brace framework (2410.10717) the
      star can be quasigroup-only; whether the fibre edge E2^{0,2} of the categorical LHS
      sequence literally hosts THIS class for a genuinely dynamical (non-group) star is the same
      open node as before, and here additionally rests on the (Z/4,+) additive-group reading.""")
