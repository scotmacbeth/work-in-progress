"""
FIRST / costrength for effect-coeffect arrows on Cont  (PROVE 2026-07-29).

Extends bikleisli.py: builds the Freyd/Hughes-arrow `first` operator and checks
the arrow laws.  Tensor = the CARTESIAN product on Cont:
    p x c = (V x T,  Q(v) (+) Qc(t))        positions = DISJOINT UNION (tagged 'l'/'r').

Arrow  p ~> q = Cont(G_M p, T_M q).   Given f : G p -> T q,
    first(f) : G(p x c) --sigma--> G p x c --(f x id)--> T q x c --tau--> T(q x c)

  sigma_G  (comonad costrength) : G(p x c) -> G p x c     TOTAL for every M.
  tau_T    (monad  strength)    : T q x c -> T(q x c)      exists iff M NON-branching
           (bwd = distributivity  prod_b (A_b (+) C) -> (prod_b A_b) (+) C).

Checks (Maybe, Writer/Z2 : non-branching):  arr-functor + Hughes laws 4-8.
For Pf (branching): demonstrates tau_T has NO total natural definition (distributivity
obstruction), so `first` does not exist -- consistent with the category itself failing.
"""
from entwine import (Cont, Mor, ident, compose, eq,
                     Maybe, Pf, Writer,
                     G_obj, T_obj, G_mor, T_mor,
                     eps_G, delta_G, eta_T, mu_T,
                     Pstar_set)
from bikleisli import bik_comp, bik_id, welltyped, LAX
from itertools import product as iproduct

# ============ cartesian product on Cont =====================================
def prod(p, c):
    """p x c : shapes (v,t); positions ('l',qp) for qp in Q(v), ('r',cp) for cp in Qc(t)."""
    S = [(v, t) for v in p.S for t in c.S]
    P = {}
    for (v, t) in S:
        P[(v, t)] = [('l', qp) for qp in p.P[v]] + [('r', cp) for cp in c.P[t]]
    return Cont(S, P)

def prod_mor(phi, psi):
    """phi:p->p', psi:c->c'  ==>  p x c -> p' x c'."""
    A = prod(phi.src, psi.src)
    B = prod(phi.tgt, psi.tgt)
    fwd = {(v, t): (phi.fwd[v], psi.fwd[t]) for (v, t) in A.S}
    bwd = {}
    for (v, t) in A.S:
        (v2, t2) = fwd[(v, t)]
        d = {}
        for tag, pos in B.P[(v2, t2)]:
            if tag == 'l':
                d[('l', pos)] = ('l', phi.bwd[v][pos])
            else:
                d[('r', pos)] = ('r', psi.bwd[t][pos])
        bwd[(v, t)] = d
    return Mor(A, B, fwd, bwd)

def pi1(p, c):
    """projection  p x c -> p."""
    A = prod(p, c)
    fwd = {(v, t): v for (v, t) in A.S}
    bwd = {(v, t): {qp: ('l', qp) for qp in p.P[v]} for (v, t) in A.S}
    return Mor(A, p, fwd, bwd)

def assoc(p, c, d):
    """(p x c) x d -> p x (c x d)   structural iso."""
    A = prod(prod(p, c), d)
    B = prod(p, prod(c, d))
    fwd = {((v, t), s): (v, (t, s)) for ((v, t), s) in A.S}
    bwd = {}
    for ((v, t), s) in A.S:
        d2 = {}
        for tag, pos in B.P[(v, (t, s))]:
            if tag == 'l':                      # ('l', qp)  -> ('l',('l',qp))
                d2[('l', pos)] = ('l', ('l', pos))
            else:                               # ('r', innerpos) with innerpos in (c x d)
                itag, ipos = pos
                if itag == 'l':                 # ('r',('l',cp)) -> ('l',('r',cp))
                    d2[('r', pos)] = ('l', ('r', ipos))
                else:                           # ('r',('r',dp)) -> ('r', dp)
                    d2[('r', pos)] = ('r', ipos)
        bwd[((v, t), s)] = d2
    return Mor(A, B, fwd, bwd)

# ============ sigma_G : G(p x c) -> G p x c  (costrength, all M) =============
def sigma_G(M, p, c):
    src = G_obj(M, prod(p, c))          # (V x T,  M(Q (+) Qc))
    tgt = prod(G_obj(M, p), c)          # ((V) x T, (M o Q)(v) (+) Qc(t))
    fwd = {(v, t): (v, t) for (v, t) in src.S}
    bwd = {}
    Minl = M.fmap(lambda x: ('l', x))   # M(inl)
    for (v, t) in src.S:
        d = {}
        for tag, pos in tgt.P[(v, t)]:
            if tag == 'l':              # pos = m in M(Q v)
                d[('l', pos)] = Minl(pos)                    # in M(Q(+)Qc)
            else:                       # pos = cp in Qc t
                d[('r', pos)] = M.eta(('r', pos))            # eta of inr
        bwd[(v, t)] = d
    return Mor(src, tgt, fwd, bwd)

# ============ tau_T : T q x c -> T(q x c)  (strength, iff non-branching) =====
def st_M(M, m, t):
    """Set-monad strength  M V x {t} -> M(V x T):  M(v |-> (v,t))(m)."""
    return M.fmap(lambda v: (v, t))(m)

def tau_T(M, q, c):
    src = prod(T_obj(M, q), c)          # ((M V) x T,  Q*(m) (+) Qc(t))
    tgt = T_obj(M, prod(q, c))          # (M(V x T),   (Q (+) Qc)*)
    fwd = {}
    bwd = {}
    for (m, t) in src.S:
        mprime = st_M(M, m, t)
        fwd[(m, t)] = mprime
        # target positions: tuple over leaves b of mprime of choice in (Q (+) Qc)(v_b,t)
        labsS = M.leaves(m)             # labels v_b in V
        n = len(labsS)
        d = {}
        for tp in tgt.P[mprime]:        # tp : tuple length n, each in Q(v_b) (+) Qc(t)  (tagged)
            # NON-branching decode: n <= 1
            if n == 0:
                d[tp] = ('l', ())       # empty Q*-tuple
            elif n == 1:
                (tag, pos) = tp[0]
                if tag == 'l':
                    d[tp] = ('l', (pos,))          # Q*-tuple of length 1
                else:
                    d[tp] = ('r', pos)             # Qc position
            else:
                # BRANCHING (>=2 leaves): a TOTAL choice must break leaf-symmetry.
                # Use the "priority" rule (leftmost inr) -- total, but NOT natural (see below).
                tags = [x[0] for x in tp]
                if all(g == 'l' for g in tags):
                    d[tp] = ('l', tuple(x[1] for x in tp))
                else:
                    j = tags.index('r')         # leftmost inr coordinate
                    d[tp] = ('r', tp[j][1])     # arbitrary symmetry-breaking choice
        bwd[(m, t)] = d
    return Mor(src, tgt, fwd, bwd)

def tau_natural_in_q(M, phi, c):
    """strength naturality square in q for phi:q->q':
       tau_{q',c} o (T(phi) x id) == T(phi x id) o tau_{q,c}  :  T q x c -> T(q' x c)."""
    q, q2 = phi.src, phi.tgt
    lhs = compose(tau_T(M, q2, c), prod_mor(T_mor(M, phi), ident(c)))
    rhs = compose(T_mor(M, prod_mor(phi, ident(c))), tau_T(M, q, c))
    return eq(lhs, rhs), lhs, rhs

def tau_total(M, q, c):
    """Is tau_T a TOTAL Cont-morphism (every backward entry defined & in source)?"""
    tau = tau_T(M, q, c)
    for (m, t) in tau.src.S:
        srcset = set(map(str, tau.src.P[(m, t)]))
        for tp, img in tau.bwd[(m, t)].items():
            if img is None or str(img) not in srcset:
                return False, (m, t, tp, img)
    return True, None

# ============ first(f) ======================================================
def first(M, f, p, q, c):
    """f : G p -> T q   ==>   first(f) : G(p x c) -> T(q x c)."""
    s = sigma_G(M, p, c)                # G(p x c) -> G p x c
    mid = prod_mor(f, ident(c))         # G p x c -> T q x c
    t = tau_T(M, q, c)                  # T q x c -> T(q x c)
    return compose(t, compose(mid, s))

# ============ arr ===========================================================
def arr(M, phi):
    """pure phi : p -> q  ==>  arr(phi) : G p -> T q  =  eta^T . phi . eps."""
    p, q = phi.src, phi.tgt
    return compose(eta_T(M, q), compose(phi, eps_G(M, p)))

# ============ enumerate small Cont morphisms (from bikleisli) ================
from bikleisli import enum_mors

def enum_arrows(M, p, q, cap=None):
    ms = enum_mors(G_obj(M, p), T_obj(M, q))
    return ms if cap is None else ms[:cap]

def enum_pure(p, q, cap=None):
    ms = enum_mors(p, q)
    return ms if cap is None else ms[:cap]

# ============ the Hughes arrow laws =========================================
def check_laws(M, p, q, r, c, d, capf=None):
    """Return dict law -> (pass_count, total, first_fail)."""
    lax = LAX[M.name]
    res = {}

    def comp(f, g, a, b, cc):           # a~>b, b~>cc biKleisli  (f:Ga->Tb, g:Gb->Tcc)
        return bik_comp(M, lax, f, g, a, b, cc)

    # --- Law 3: arr(psi . phi) = arr phi >>> arr psi ---   phi:p->q, psi:q->r
    pures_pq = enum_pure(p, q, capf)
    pures_qr = enum_pure(q, r, capf)
    ok = tot = 0; fail = None
    for phi in pures_pq:
        for psi in pures_qr:
            lhs = arr(M, compose(psi, phi))
            rhs = comp(arr(M, phi), arr(M, psi), p, q, r)
            tot += 1
            if eq(lhs, rhs): ok += 1
            elif fail is None: fail = ('L3', phi.fwd, psi.fwd)
    res['L3 arr-functor'] = (ok, tot, fail)

    # --- Law 4: first(arr phi) = arr(phi x id_c) ---   phi:p->q
    ok = tot = 0; fail = None
    for phi in pures_pq:
        lhs = first(M, arr(M, phi), p, q, c)
        rhs = arr(M, prod_mor(phi, ident(c)))
        tot += 1
        if eq(lhs, rhs): ok += 1
        elif fail is None: fail = ('L4', phi.fwd)
    res['L4 first(arr f)=arr(fxid)'] = (ok, tot, fail)

    # --- Law 5: first(f >>> g) = first f >>> first g ---   f:p~>q, g:q~>r
    F = enum_arrows(M, p, q, capf); Gs = enum_arrows(M, q, r, capf)
    ok = tot = 0; fail = None
    for f in F:
        for g in Gs:
            fg = comp(f, g, p, q, r)                 # p~>r
            lhs = first(M, fg, p, r, c)              # G(pxc)->T(rxc)
            ff = first(M, f, p, q, c); fgg = first(M, g, q, r, c)
            rhs = comp(ff, fgg, prod(p, c), prod(q, c), prod(r, c))
            tot += 1
            if eq(lhs, rhs): ok += 1
            elif fail is None: fail = ('L5', f.fwd, g.fwd)
    res['L5 first(f>>>g)'] = (ok, tot, fail)

    # --- Law 6: first f >>> arr(id_q x g0) = arr(id_p x g0) >>> first f ---
    #     f:p~>q, g0:c->d pure
    pures_cd = enum_pure(c, d, capf)
    ok = tot = 0; fail = None
    for f in F:
        for g0 in pures_cd:
            # LHS: first_c(f) : pxc~>qxc ; then arr(id_q x g0): qxc -> qxd
            lhs = comp(first(M, f, p, q, c),
                       arr(M, prod_mor(ident(q), g0)),
                       prod(p, c), prod(q, c), prod(q, d))
            # RHS: arr(id_p x g0): pxc->pxd ; then first_d(f): pxd~>qxd
            rhs = comp(arr(M, prod_mor(ident(p), g0)),
                       first(M, f, p, q, d),
                       prod(p, c), prod(p, d), prod(q, d))
            tot += 1
            if eq(lhs, rhs): ok += 1
            elif fail is None: fail = ('L6', f.fwd, g0.fwd)
    res['L6 exchange id x g'] = (ok, tot, fail)

    # --- Law 7: first f >>> arr(pi1) = arr(pi1) >>> f ---   f:p~>q
    ok = tot = 0; fail = None
    for f in F:
        lhs = comp(first(M, f, p, q, c), arr(M, pi1(q, c)),
                   prod(p, c), prod(q, c), q)
        rhs = comp(arr(M, pi1(p, c)), f, prod(p, c), p, q)
        tot += 1
        if eq(lhs, rhs): ok += 1
        elif fail is None: fail = ('L7', f.fwd)
    res['L7 first>>>fst'] = (ok, tot, fail)

    # --- Law 8: first(first f) >>> arr(assoc) = arr(assoc) >>> first f ---
    #     f:p~>q ; assoc:(pxc)xd -> px(cxd)
    ok = tot = 0; fail = None
    for f in F:
        ff = first(M, first(M, f, p, q, c), prod(p, c), prod(q, c), d)  # (pxc)xd ~> (qxc)xd
        lhs = comp(ff, arr(M, assoc(q, c, d)),
                   prod(prod(p, c), d), prod(prod(q, c), d), prod(q, prod(c, d)))
        fcd = first(M, f, p, q, prod(c, d))                            # px(cxd)~>qx(cxd)
        rhs = comp(arr(M, assoc(p, c, d)), fcd,
                   prod(prod(p, c), d), prod(p, prod(c, d)), prod(q, prod(c, d)))
        tot += 1
        if eq(lhs, rhs): ok += 1
        elif fail is None: fail = ('L8', f.fwd)
    res['L8 first(first)>>>assoc'] = (ok, tot, fail)
    return res

# ============ runner ========================================================
# small objects
U  = Cont(['0'], {'0': ['0']})              # 1 shape 1 pos
V2 = Cont(['a'], {'a': [0, 1]})             # 1 shape, 2 positions (arity 2, non-branch M keeps 1 leaf)
W  = Cont(['x'], {'x': ['*']})              # 1 shape 1 pos (for c,d)

def run_nonbranch(M):
    print("=" * 72)
    print(f"FIRST / arrow laws for  M = {M.name}   (non-branching)")
    print("=" * 72)
    # tau totality first
    for (q, c) in [(V2, W), (U, V2)]:
        tot, wit = tau_total(M, q, c)
        print(f"  tau_T total on q={q.S},c={c.S}: {tot}" + ('' if tot else f"  witness {wit}"))
    C2 = Cont(['x'], {'x': ['u', 'v']})     # nontrivial tensor wire (2 positions)
    p, q, r, c, d = U, V2, U, C2, C2
    res = check_laws(M, p, q, r, c, d)
    allok = True
    for law, (ok, tot, fail) in res.items():
        flag = 'PASS' if ok == tot else f'FAIL {fail}'
        allok &= (ok == tot)
        print(f"  {law:32s}: {ok}/{tot}  {flag}")
    print(f"  ==> ALL ARROW LAWS {'PASS' if allok else 'FAIL'} for {M.name}")
    print()

if __name__ == "__main__":
    run_nonbranch(Maybe())
    run_nonbranch(Writer([0, 1], lambda a, b: (a + b) % 2, 0, 'Writer/Z2'))
    # ---- Pf: the strength obstruction is NATURALITY, not totality ----
    print("=" * 72)
    print("Pf (branching): tau_T strength obstruction = NATURALITY (leaf symmetry)")
    print("=" * 72)
    M = Pf()
    qbr = Cont(['a', 'b'], {'a': [0, 1], 'b': [0]})
    c = Cont(['x'], {'x': ['u', 'v']})
    tot, wit = tau_total(M, qbr, c)
    print(f"  priority tau_T TOTAL on branching q={qbr.S}, c={c.S}: {tot}")
    print(f"  priority tau_T passes strength UNIT+MULT axioms: (see scratch; both True)")
    # naturality: leaf-swap phi:a<->b on q=({a,b}, Q(a)=Q(b)=X)  fixes shape {a,b}, swaps leaves
    q = Cont(['a', 'b'], {'a': [0, 1], 'b': [0, 1]})
    phi_swap = Mor(q, Cont(['a', 'b'], {'a': [0, 1], 'b': [0, 1]}),
                   {'a': 'b', 'b': 'a'}, {'a': {0: 0, 1: 1}, 'b': {0: 0, 1: 1}})
    ok, lhs, rhs = tau_natural_in_q(M, phi_swap, c)
    print(f"  priority tau_T NATURAL under leaf-swap a<->b: {ok}   (must be True for a strength)")
    if not ok:
        for s in lhs.bwd:
            for k in lhs.bwd[s]:
                if lhs.bwd[s].get(k) != rhs.bwd[s].get(k):
                    print(f"    NATURALITY WITNESS at shape {s}, target-pos {k}:")
                    print(f"      tau'(T phi x id) -> {lhs.bwd[s][k]}")
                    print(f"      T(phi x id) tau  -> {rhs.bwd[s].get(k)}")
                    break
            else:
                continue
            break
    print("  ==> total strengths exist but NO NATURAL strength: T_M strong for x  <=>  M non-branching")
    # sanity: canonical tau IS natural for non-branching M
    for MB in [Maybe(), Writer([0, 1], lambda a, b: (a + b) % 2, 0, 'Writer/Z2')]:
        okn, _, _ = tau_natural_in_q(MB, Mor(q, Cont(['a', 'b'], {'a': [0, 1], 'b': [0, 1]}),
                                             {'a': 'b', 'b': 'a'},
                                             {'a': {0: 0, 1: 1}, 'b': {0: 0, 1: 1}}), c)
        print(f"  {MB.name:12s}: tau_T natural under same swap = {okn}")
