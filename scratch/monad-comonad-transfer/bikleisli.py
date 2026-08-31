"""
BIKLEISLI CATEGORY of effect-coeffect arrows on Cont  (PROVE 2026-07-29).

An effect-coeffect ARROW  p ~> q  is a Cont-morphism   f : G_M p -> T_M q
  ( coeffect comonad G_M on the source, effect monad T_M on the target ).

Composition of  f : G p -> T q  and  g : G q -> T r  is the standard biKleisli
composite (coKleisli-of-Kleisli):

    G p --delta_p--> G G p --G f--> G T q --kappa_q--> T G q --T g--> T T r --mu_r--> T r

where  kappa : G T => T G   is the *reverse* mixed distributive law (GT=>TG),
NOT the entwining lambda : T G => G T proved on 2026-07-27.  kappa is the LAX
product-comparison on positions; it exists (coherently) iff M is NON-branching.

Identity  p ~> p  is   G p --eps_p--> p --eta^T_p--> T p .

THIS SCRIPT verifies:
  (1) biKleisli composition is well-typed;
  (2) for M = Maybe (non-branching): identity + associativity hold on ALL sampled
      arrows  ->  a genuine category;
  (3) for M = Pf (branching): a CONCRETE triple (f,g,h) with
      (h.g).f  !=  h.(g.f)  ->  NO category; the compositor fails.

Reuses the verified machinery in entwine.py.
"""
from entwine import (Cont, Mor, ident, compose, eq,
                     Maybe, Pf, Writer,
                     G_obj, T_obj, G_mor, T_mor,
                     eps_G, delta_G, eta_T, mu_T,
                     lambda_rev, lax_Maybe)
from itertools import product as iproduct

# ---------- the reverse law kappa : G T => T G via the LAX map -------------
def lax_Pf(M, P, labs, t):
    # t = (w_b)_b with w_b a frozenset in Pf(P(lab_b)); return cartesian product
    # as a subset of prod_b P(lab_b), i.e. an element of Pf(prod_b P(lab_b)).
    if len(labs) == 0:
        return frozenset([()])
    return frozenset(tuple(c) for c in iproduct(*[list(t[b]) for b in range(len(labs))]))

LAX = {'Maybe': lax_Maybe, 'Pf': lax_Pf}

def kappa(M, lax, A):
    return lambda_rev(M, lax, A)        # G T A -> T G A

# ---------- biKleisli identity and composition ----------------------------
def bik_id(M, p):
    # G p -> p -> T p
    return compose(eta_T(M, p), eps_G(M, p))

def bik_comp(M, lax, f, g, p, q, r):
    """f : G p -> T q,  g : G q -> T r   ==>   G p -> T r."""
    step1 = delta_G(M, p)               # G p -> G G p
    step2 = G_mor(M, f)                 # G G p -> G T q
    step3 = kappa(M, lax, q)            # G T q -> T G q
    step4 = T_mor(M, g)                 # T G q -> T T r
    step5 = mu_T(M, r)                  # T T r -> T r
    return compose(step5, compose(step4, compose(step3, compose(step2, step1))))

def welltyped(mor):
    """check every backward entry lands in the source position set."""
    for s in mor.src.S:                 # fwd/bwd are keyed by SOURCE shapes
        us = mor.fwd[s]
        srcset = set(map(str, mor.src.P[s]))
        for c in mor.tgt.P[us]:
            if str(mor.bwd[s][c]) not in srcset:
                return False
    return True

# ---------- enumerate Cont morphisms  X -> Y  (X,Y small) ------------------
def enum_mors(X, Y):
    outs = []
    Slist = X.S
    for uvals in iproduct(Y.S, repeat=len(Slist)):
        u = {s: uvals[i] for i, s in enumerate(Slist)}
        # for each s, choose backward map Y.P[u s] -> X.P[s]
        choice_spaces = []
        for s in Slist:
            tgtpos = Y.P[u[s]]
            srcpos = X.P[s]
            # a function tgtpos -> srcpos
            fns = list(iproduct(srcpos, repeat=len(tgtpos)))
            choice_spaces.append([(s, tgtpos, fn) for fn in fns])
        for combo in iproduct(*choice_spaces):
            bwd = {}
            for (s, tgtpos, fn) in combo:
                bwd[s] = {tgtpos[i]: fn[i] for i in range(len(tgtpos))}
            outs.append(Mor(X, Y, dict(u), bwd))
    return outs

def enum_arrows(M, p, q, cap=None):
    """arrows p ~> q  =  Cont(G p, T q)."""
    Gp, Tq = G_obj(M, p), T_obj(M, q)
    ms = enum_mors(Gp, Tq)
    return ms if cap is None else ms[:cap]

# ---------- test containers -----------------------------------------------
U  = Cont(['0'], {'0': ['0']})                      # trivial-ish: 1 shape, 1 pos
A1 = Cont(['a', 'b'], {'a': [0, 1], 'b': [0]})      # branching-capable

def report(M):
    lax = LAX[M.name]
    print("=" * 70)
    print(f"biKleisli category of effect-coeffect arrows for  M = {M.name}")
    print("=" * 70)

    # choose objects: p=r=U (small), q=z=A1 (fat) so mu_T can overlap for Pf
    p, q, r, z = U, A1, U, A1

    F = enum_arrows(M, p, q)     # G p -> T q
    Gs = enum_arrows(M, q, r)    # G q -> T r
    H = enum_arrows(M, r, z)     # G r -> T z
    print(f"  #arrows  p~>q={len(F)}  q~>r={len(Gs)}  r~>z={len(H)}")

    # (1) well-typedness of composites (sample)
    wt = True
    for f in F[:6]:
        for g in Gs[:6]:
            c = bik_comp(M, lax, f, g, p, q, r)
            if not welltyped(c):
                wt = False
    print(f"  (1) sampled composites well-typed: {wt}")

    # (2) identity laws:  id_q . f == f   and   f . id_p == f
    idp, idq = bik_id(M, p), bik_id(M, q)
    unit_ok = True
    bad_unit = None
    for f in F:
        left  = bik_comp(M, lax, f, idq, p, q, q)   # G p ->..-> T q  (id_q after f)
        right = bik_comp(M, lax, idp, f, p, p, q)   # (f after id_p)
        if not (eq(left, f) and eq(right, f)):
            unit_ok = False
            bad_unit = f
            break
    print(f"  (2) identity laws hold on all {len(F)} arrows p~>q: {unit_ok}")

    # (3) associativity: (h.g).f  ==  h.(g.f)   for f:p~>q, g:q~>r, h:r~>z
    viol = 0
    first = None
    for i, f in enumerate(F):
        for g in Gs:
            gf = bik_comp(M, lax, f, g, p, q, r)          # G p -> T r
            for h in H:
                hg = bik_comp(M, lax, g, h, q, r, z)      # G q -> T z
                left  = bik_comp(M, lax, gf, h, p, r, z)  # (h.g).f
                right = bik_comp(M, lax, f, hg, p, q, z)  # h.(g.f)
                if not eq(left, right):
                    viol += 1
                    if first is None:
                        first = (f, g, h, left, right)
    print(f"  (3) associativity: {viol} violating triples "
          f"out of {len(F)*len(Gs)*len(H)}")
    if first is not None:
        f, g, h, left, right = first
        print("      FIRST VIOLATION (h.g).f != h.(g.f):")
        print(f"        f fwd={f.fwd} bwd={f.bwd}")
        print(f"        g fwd={g.fwd} bwd={g.bwd}")
        print(f"        h fwd={h.fwd} bwd={h.bwd}")
        # show where they differ
        for s in left.fwd:
            if left.fwd[s] != right.fwd[s]:
                print(f"        fwd differ @ {s}: {left.fwd[s]} vs {right.fwd[s]}")
            else:
                for c in left.tgt.P[left.fwd[s]]:
                    if left.bwd[s].get(c) != right.bwd[s].get(c):
                        print(f"        bwd differ @ shape {s}, pos {c}: "
                              f"{left.bwd[s].get(c)} vs {right.bwd[s].get(c)}")
                        break
    print()

def enum_mors_diverse(X, Y):
    """like enum_mors but yields forward-surjective (non-degenerate) arrows first."""
    ms = enum_mors(X, Y)
    def rank(m):
        return -len(set(m.fwd.values()))     # more distinct target shapes first
    return sorted(ms, key=rank)

def branch_rich(mor, need):
    """keep arrows whose forward image contains all Pf-shapes in `need`."""
    img = set(map(frozenset, mor.fwd.values()))
    return all(frozenset(x) in img for x in need)

def hunt_pf_nonassoc(objs, capF, capG, capH):
    """Search for a non-associative triple for M=Pf over the given objects.
    Filter each pool to branch-rich arrows (forward hits the overlapping shapes
    {a,b} and {a}) so the union-of-products vs product-of-unions gap can appear."""
    M = Pf(); lax = lax_Pf
    p, q, r, z = objs
    need = [{'a', 'b'}, {'a'}]
    F  = [m for m in enum_mors(G_obj(M, p), T_obj(M, q)) if branch_rich(m, need)][:capF]
    Gs = [m for m in enum_mors(G_obj(M, q), T_obj(M, r)) if branch_rich(m, need)][:capG]
    H  = [m for m in enum_mors(G_obj(M, r), T_obj(M, z)) if branch_rich(m, need)][:capH]
    print(f"  branch-rich pools: F={len(F)} G={len(Gs)} H={len(H)}")
    tested = 0
    for f in F:
        for g in Gs:
            gf = bik_comp(M, lax, f, g, p, q, r)
            for h in H:
                hg = bik_comp(M, lax, g, h, q, r, z)
                left  = bik_comp(M, lax, gf, h, p, r, z)   # (h.g).f
                right = bik_comp(M, lax, f, hg, p, q, z)    # h.(g.f)
                tested += 1
                if not eq(left, right):
                    return (f, g, h, left, right, tested)
    return (None, None, None, None, None, tested)

def lax_writer(M, P, labs, t):
    # Writer has arity 1 (exactly one leaf), so t = (w,) with w = ('w', z, n).
    # lax : prod_b M Z_b -> M(prod_b Z_b) rewraps into a single-entry product tuple.
    (w,) = t
    return ('w', (w[1],), w[2])
LAX['Writer/Z2'] = lax_writer

if __name__ == "__main__":
    report(Maybe())
    report(Writer([0, 1], lambda a, b: (a + b) % 2, 0, 'Writer/Z2'))
    report(Pf())
    print("=" * 70)
    print("TARGETED Pf non-associativity hunt (objects all = A1)")
    print("=" * 70)
    f, g, h, left, right, tested = hunt_pf_nonassoc((A1, A1, A1, A1), 40, 40, 40)
    if f is None:
        print(f"  no violation found in {tested} triples (widen caps)")
    else:
        print(f"  VIOLATION found after {tested} triples:")
        print(f"    f fwd={f.fwd} bwd={f.bwd}")
        print(f"    g fwd={g.fwd} bwd={g.bwd}")
        print(f"    h fwd={h.fwd} bwd={h.bwd}")
        for s in left.fwd:
            if left.fwd[s] != right.fwd[s]:
                print(f"    fwd differ @ {s}: {left.fwd[s]} vs {right.fwd[s]}")
            else:
                for c in left.tgt.P[left.fwd[s]]:
                    if left.bwd[s].get(c) != right.bwd[s].get(c):
                        print(f"    bwd differ @ shape {s}, pos {c}:")
                        print(f"        (h.g).f -> {left.bwd[s].get(c)}")
                        print(f"        h.(g.f) -> {right.bwd[s].get(c)}")
                        break
