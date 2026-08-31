"""
Orchestration = Zappa-Szep product: the worked instantiation.

Supervisor-worker orchestration modeled as a small category (= directed container,
Ahman-Uustalu T1). Two orchestrations compose into a joint agent K = C |><| D
(a distributive law / ZS product, T2). A RE-ENTRANCY pattern is a (G)-failure:
(L) holds but no C closes => no single-valued distributive law => nonzero
[omega] in H^2(Sk; Z/2) (T3, rigid twist = generator).

Reuses the machine-checked pairwise-ZS framework verbatim.
"""
from itertools import product as iproduct
from pairwise_zs_check import FinCat, extract_lambda, check_zs_axioms, build_zs_product
from pairwise_end_to_end import (wide_subcats, is_sfs, Dmodule_is_free,
                                 criterion, full_check)


# ===========================================================================
# MODEL 1  --  K_bug : re-entrant orchestration (worker mutates supervisor state)
#
# Objects (control locations / roles):
#   S = supervisor        End(S) = {1S, tau},  tau^2 = 1S   (tau = pass 1-bit turn token)
#   W = worker-running phase
#   R = result/return phase
# Handoffs:
#   p, ptau : S -> W    dispatch to worker in turn-state 0 / 1   (ptau = p o tau)
#   s, s2   : W -> R    worker outcomes: s = normal return, s2 = RE-ENTRANT return
#   q, qtau : S -> R    composite handoffs
# Physics (the bug):
#   s o p   = q      normal return keeps the token
#   s2 o p  = qtau   RE-ENTRANT return FLIPS the supervisor's token  <-- shared-state mutation
#   s o ptau = qtau,  s2 o ptau = q      (forced by tau-equivariance)
#
# This is exactly the rigid twist with orchestration semantics.
# D = supervisor-internal moves = End = {1S, tau, 1W, 1R}.
# ===========================================================================

def K_bug():
    objs = ["S", "W", "R"]
    arrows = {"1S": ("S", "S"), "tau": ("S", "S"), "1W": ("W", "W"), "1R": ("R", "R"),
              "p": ("S", "W"), "ptau": ("S", "W"),
              "s": ("W", "R"), "s2": ("W", "R"),
              "q": ("S", "R"), "qtau": ("S", "R")}
    comp = {}
    idof = {"S": "1S", "W": "1W", "R": "1R"}
    for f, (d, c) in arrows.items():
        comp[(f, idof[d])] = f
        comp[(idof[c], f)] = f
    # End(S) = Z/2
    comp[("1S", "1S")] = "1S"; comp[("1S", "tau")] = "tau"
    comp[("tau", "1S")] = "tau"; comp[("tau", "tau")] = "1S"
    comp[("1W", "1W")] = "1W"; comp[("1R", "1R")] = "1R"
    # right End(S) = <tau> action on dispatches/results
    comp[("p", "tau")] = "ptau"; comp[("ptau", "tau")] = "p"
    comp[("q", "tau")] = "qtau"; comp[("qtau", "tau")] = "q"
    # worker outcomes composed after dispatch  (THE TWIST = re-entrancy)
    comp[("s", "p")] = "q";    comp[("s2", "p")] = "qtau"
    comp[("s", "ptau")] = "qtau"; comp[("s2", "ptau")] = "q"
    return FinCat(objs, arrows, comp, idof)


D_bug = {"1S", "tau", "1W", "1R"}   # supervisor-internal / token moves


# ===========================================================================
# MODEL 2  --  K_ok : state-protected orchestration (a lock; re-entry cannot
#             mutate the supervisor's token).  Worker still has two outcomes
#             s, s2, but NEITHER flips the token:
#                 s o p = q,   s2 o p = q,   s o ptau = qtau,  s2 o ptau = qtau
#             i.e. the outcome is independent of the token; token only moved by tau.
# ===========================================================================

def K_ok():
    objs = ["S", "W", "R"]
    arrows = {"1S": ("S", "S"), "tau": ("S", "S"), "1W": ("W", "W"), "1R": ("R", "R"),
              "p": ("S", "W"), "ptau": ("S", "W"),
              "s": ("W", "R"), "s2": ("W", "R"),
              "q": ("S", "R"), "qtau": ("S", "R")}
    comp = {}
    idof = {"S": "1S", "W": "1W", "R": "1R"}
    for f, (d, c) in arrows.items():
        comp[(f, idof[d])] = f
        comp[(idof[c], f)] = f
    comp[("1S", "1S")] = "1S"; comp[("1S", "tau")] = "tau"
    comp[("tau", "1S")] = "tau"; comp[("tau", "tau")] = "1S"
    comp[("1W", "1W")] = "1W"; comp[("1R", "1R")] = "1R"
    comp[("p", "tau")] = "ptau"; comp[("ptau", "tau")] = "p"
    comp[("q", "tau")] = "qtau"; comp[("qtau", "tau")] = "q"
    # NO twist: both outcomes preserve token
    comp[("s", "p")] = "q";    comp[("s2", "p")] = "q"
    comp[("s", "ptau")] = "qtau"; comp[("s2", "ptau")] = "qtau"
    return FinCat(objs, arrows, comp, idof)


D_ok = {"1S", "tau", "1W", "1R"}


# ===========================================================================
# MODEL 3  --  K_indep : two independent supervisors C, D over read-only workers.
#   Build directly as a ZS product with the TRIVIAL (swap) distributive law.
#   C = <c>  (supervisor-C dispatch cycle, Z/2 for finiteness),
#   D = <d>  (supervisor-D dispatch cycle, Z/2), one object O.
#   Trivial law: ^d c = c, d^c = d  (they don't interfere). Expect a valid category
#   = the direct product Z/2 x Z/2, ZS axioms hold, SFS exists.
# ===========================================================================

def two_Z2():
    """One object, End = Z/2 = {1,g}. Used as both C and D factors."""
    objs = ["O"]
    arrows = {"1O": ("O", "O"), "g": ("O", "O")}
    comp = {("1O", "1O"): "1O", ("1O", "g"): "g", ("g", "1O"): "g", ("g", "g"): "1O"}
    return FinCat(objs, arrows, comp, {"O": "1O"})


def trivial_law(C, D):
    """delta = swap: ^d c = c, d^c = d for all c in C, d in D over shared object."""
    lam = {}
    for d in D.arrows:
        for c in C.arrows:
            if D.dom(d) == C.cod(c):
                lam[(d, c)] = (c, d)
    return lam


# ===========================================================================
# ANALYSIS
# ===========================================================================

def analyze(K, Dset, label):
    print("=" * 72)
    print("MODEL:", label)
    print("  is a category:", K.check_category(verbose=True))
    # D wide + closed?
    ids = set(K.ident[o] for o in K.objects)
    dwide = ids <= Dset and all(
        (K.cod(f) != K.dom(g)) or (K.compose(g, f) in Dset)
        for g in Dset for f in Dset)
    print("  D wide & closed:", dwide, " D =", sorted(Dset))
    # (L): freeness per target
    Lfree = {}
    for b in K.objects:
        bs = Dmodule_is_free(K, Dset, b)
        Lfree[b] = bs
        print(f"    Hom(-,{b}) free? {'YES' if bs else 'NO'}  "
              f"# bases = {len(bs)}")
    L = all(Lfree[b] for b in K.objects)
    # (G) via criterion + brute-force ground truth
    crit, Lflag, C = criterion(K, Dset, verbose=False)
    truth = any(is_sfs(K, Cc, Dset) for Cc in wide_subcats(K))
    print(f"  (L) holds: {L}")
    print(f"  (G)/SFS  criterion says: {crit}   brute-force truth: {truth}   "
          f"{'OK' if crit == truth else '*** MISMATCH ***'}")
    if crit:
        print("  ==> COMPOSES.  C =", sorted(C))
        # extract lambda & verify ZS axioms
        lam, fact, err = extract_lambda(K, C, Dset)
        if lam is not None:
            ok = check_zs_axioms(FinCat(K.objects, {a: K.arrows[a] for a in C},
                                        {k: v for k, v in K.comp.items()
                                         if k[0] in C and k[1] in C}, K.ident),
                                 FinCat(K.objects, {a: K.arrows[a] for a in Dset},
                                        {k: v for k, v in K.comp.items()
                                         if k[0] in Dset and k[1] in Dset}, K.ident),
                                 lam, verbose=True)
            print("  extracted lambda satisfies ZS1-ZS4 + units:", ok)
    else:
        print("  ==> OBSTRUCTED.  (L) holds but (G) fails => no distributive law.")
        # count SFS (= size of the torsor of solutions; 0 here)
        n_sfs = sum(1 for Cc in wide_subcats(K) if is_sfs(K, Cc, Dset))
        print("     # strict factorization systems over D:", n_sfs)
    return crit, truth


if __name__ == "__main__":
    r1 = analyze(K_bug(), D_bug, "K_bug  (re-entrant: worker flips supervisor token)")
    r2 = analyze(K_ok(),  D_ok,  "K_ok   (state-protected / locked)")

    # Model 3: independent supervisors, trivial law
    print("=" * 72)
    print("MODEL: K_indep (two independent supervisors, trivial distributive law)")
    C = two_Z2(); D = two_Z2()
    lam = trivial_law(C, D)
    ax = check_zs_axioms(C, D, lam, verbose=True)
    print("  trivial law satisfies ZS1-ZS4 + units:", ax)
    K = build_zs_product(C, D, lam)
    print("  C |><| D is a category:", K.check_category(verbose=True))
    print("  # morphisms in K:", len(K.arrows), "(expect 4 = Z/2 x Z/2)")

    print("\n" + "=" * 72)
    print("SUMMARY TABLE  (shared-worker topology -> composable?)")
    print(f"  independent supervisors (read-only workers)   : COMPOSES (trivial law)")
    print(f"  state-protected re-entry (lock)               : {'COMPOSES' if r2[0] else 'OBSTRUCTED'}")
    print(f"  unprotected re-entry (worker mutates sup state): {'COMPOSES' if r1[0] else 'OBSTRUCTED'}")
