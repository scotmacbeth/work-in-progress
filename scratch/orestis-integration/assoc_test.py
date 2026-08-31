"""
Associativity test for Orestis's  _⨾⇕_  (BiLift composition), List monad.

We test   (f ⨾ g) ⨾ h   vs   f ⨾ (g ⨾ h)   on branching witnesses.

Two liftings:
  * Any (◇/∃)  -- Orestis's actual Nondet/BiLift.agda lifting.  VERDICT question.
  * All (□/∀)  -- CONTROL = MacBeth's ∏-Mendler; must reproduce a known failure
                  (sanity check that the harness can DETECT non-associativity).

Uniform test container:  U = {*} ◁ {0,1}   (single shape, 2 positions = "menu of 2"
                          on the position/answer side; view lists give menus on the
                          shape/query side).
"""

import random
from itertools import product as iproduct
from bilift import Cont, Arrow, compose, arrows_equal, AnyLifting, AllLifting

STAR = "*"
POS = (0, 1)                                   # 2 positions per shape
U = Cont([STAR], {STAR: list(POS)})


# ---- arrow builders on U ---------------------------------------------------
# An arrow U ⇕ U is:
#   view(*)      = list of STARs of some length  (menu size)  -> encode by length L
#   update(*, w) = list over POS                              -> a chosen output list
#
# For enumeration we encode an arrow by:
#   vlen : the view length
#   table: dict from witness -> output list (a small list over POS)

def make_arrow(vlen, table, L):
    view = lambda s: [STAR] * vlen
    def update(s, w):
        return list(table[canon(w)])
    return Arrow(U, U, view, update)

def canon(w):
    # witnesses are hashable already (Any: (i,r); All: tuple) -> use as key
    return w


def all_arrows(L, out_options, vlens):
    """Exhaustively enumerate arrows U⇕U for given output-list options and view lengths."""
    arrows = []
    Qfun = U.P
    for vlen in vlens:
        ys = [STAR] * vlen
        ws = L.enum(Qfun, ys)                  # witnesses over view(*)
        # choose an output list (from out_options) for each witness
        for combo in iproduct(out_options, repeat=len(ws)):
            table = {canon(w): combo[k] for k, w in enumerate(ws)}
            arrows.append(make_arrow(vlen, table, L))
    return arrows


def random_arrow(L, max_vlen, max_out):
    vlen = random.randint(0, max_vlen)
    ys = [STAR] * vlen
    ws = L.enum(U.P, ys)
    table = {}
    for w in ws:
        olen = random.randint(0, max_out)
        table[canon(w)] = [random.choice(POS) for _ in range(olen)]
    return make_arrow(vlen, table, L)


# ---- the associativity check ----------------------------------------------
def check_triple(f, g, h, L):
    left  = compose(compose(f, g, L), h, L)     # (f⨾g)⨾h
    right = compose(f, compose(g, h, L), L)     # f⨾(g⨾h)
    return arrows_equal(left, right, L)


def describe_arrow(a, L):
    s = STAR
    ys = a.view(s)
    d = {}
    for w in L.enum(U.P, ys):
        d[w] = a.update(s, w)
    return {"view(*)_len": len(ys), "update": d}


def run_exhaustive(L, out_options, vlens, label):
    print(f"\n=== EXHAUSTIVE  [{label}]  lifting={L.name} ===")
    print(f"    out_options={out_options}  vlens={vlens}")
    arrows = all_arrows(L, out_options, vlens)
    print(f"    #arrows = {len(arrows)}   -> triples = {len(arrows)**3}")
    checked = 0
    violation = None
    for f in arrows:
        for g in arrows:
            for h in arrows:
                checked += 1
                ok, info = check_triple(f, g, h, L)
                if not ok:
                    violation = (f, g, h, info)
                    break
            if violation: break
        if violation: break
    print(f"    checked {checked} triples")
    if violation:
        f, g, h, info = violation
        print("    *** NON-ASSOCIATIVE ***")
        print("      f =", describe_arrow(f, L))
        print("      g =", describe_arrow(g, L))
        print("      h =", describe_arrow(h, L))
        print("      mismatch:", info)
    else:
        print("    associative on ALL triples in this space (0 violations)")
    return violation


def run_random(L, max_vlen, max_out, n, label, seed=0):
    print(f"\n=== RANDOM  [{label}]  lifting={L.name} ===")
    print(f"    max_vlen={max_vlen} max_out={max_out}  samples={n}  seed={seed}")
    random.seed(seed)
    violation = None
    for t in range(n):
        f = random_arrow(L, max_vlen, max_out)
        g = random_arrow(L, max_vlen, max_out)
        h = random_arrow(L, max_vlen, max_out)
        ok, info = check_triple(f, g, h, L)
        if not ok:
            violation = (f, g, h, info)
            print(f"    *** NON-ASSOCIATIVE at sample {t} ***")
            print("      f =", describe_arrow(f, L))
            print("      g =", describe_arrow(g, L))
            print("      h =", describe_arrow(h, L))
            print("      mismatch:", info)
            break
    if violation is None:
        print(f"    associative on all {n} random triples (0 violations)")
    return violation


if __name__ == "__main__":
    # ---- CONTROL: □/All must FAIL (validates the harness) -------------------
    # small space with one branching output [0,1]
    out_ctrl = ([], [0], [1], [0, 1])
    run_exhaustive(AllLifting, out_ctrl, (0, 1, 2), "control □")
    run_random(AllLifting, 2, 2, 20000, "control □")

    # ---- VERDICT: ◇/Any ----------------------------------------------------
    out_any = ([], [0], [1], [0, 1])
    run_exhaustive(AnyLifting, out_any, (0, 1, 2), "verdict ◇")
    # larger random sweep for confidence
    run_random(AnyLifting, 3, 3, 300000, "verdict ◇ (wide)")
    run_random(AnyLifting, 2, 2, 200000, "verdict ◇ (narrow)", seed=1)
