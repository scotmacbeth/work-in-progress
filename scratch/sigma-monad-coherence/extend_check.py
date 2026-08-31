"""Extend the Sigma-monad check: larger params + EXHAUSTIVE assoc enumeration."""
from itertools import product
import sigma_monad as sm

def exhaustive_assoc(M, C, base_labels):
    """Enumerate ALL depth-3 M-nestings over base_labels; check mu.mu_T = mu.T(mu)."""
    TC  = sm.T_container(M, C)
    muC = sm.mu(M, C); muTC = sm.mu(M, TC); T_muC = sm.T_mor(M, muC)
    LHS = sm.compose(muC, muTC); RHS = sm.compose(muC, T_muC)
    # enumerate all depth-3 nestings: element of M(M(M(labels)))
    lvl1 = M.elements(base_labels)          # M(labels)
    lvl2 = M.elements(lvl1)                 # M(M(labels))
    lvl3 = M.elements(lvl2)                 # M(M(M(labels)))
    cex = sm.mor_eq_on(LHS, RHS, lvl3)
    return len(lvl3), cex

def exhaustive_units(M, C):
    TC=sm.T_container(M,C); etaC=sm.eta(M,C); etaTC=sm.eta(M,TC); muC=sm.mu(M,C)
    T_etaC=sm.T_mor(M,etaC); idTC=sm.identity(TC)
    L=sm.compose(muC,etaTC); R=sm.compose(muC,T_etaC)
    sh=M.elements(C.shapes)
    return sm.mor_eq_on(L,idTC,sh), sm.mor_eq_on(R,idTC,sh)

# small base container with 2 shapes to keep exhaustive tractable
smallC = sm.Container(lambda s: list(range({0:1,1:2}[s])), shapes=[0,1])
tinyC  = sm.Container(lambda s: list(range({0:2}[s])), shapes=[0])

print("=== EXHAUSTIVE associativity (all depth-3 nestings) ===")
for M, C, labels, tag in [
    (sm.ReaderM(2), tinyC,  [0],   "Reader E=2, base labels=1shape"),
    (sm.ReaderM(2), smallC, [0,1], "Reader E=2, base=2shape"),
    (sm.StateM(2),  tinyC,  [0],   "State St=2, base=1shape"),
]:
    n, cex = exhaustive_assoc(M, C, labels)
    print(f"  {tag}: #depth3={n}  {'PASS' if cex is None else 'FAIL '+str(cex)}")

print("\n=== Larger-parameter unit + random assoc ===")
import random
for M in [sm.ReaderM(4), sm.StateM(3)]:
    for cname, C in sm.base_containers():
        rL,rR = exhaustive_units(M,C)
        rng=random.Random(1)
        muC=sm.mu(M,C); muTC=sm.mu(M,sm.T_container(M,C)); T_muC=sm.T_mor(M,muC)
        LHS=sm.compose(muC,muTC); RHS=sm.compose(muC,T_muC)
        samp=[M.random_elt(3,C.shapes,rng) for _ in range(4000)]
        ca=sm.mor_eq_on(LHS,RHS,samp)
        print(f"  {M.name}(p={getattr(M,'E',getattr(M,'St',0))}) [{cname}]: "
              f"unitL={'ok' if rL is None else rL}, unitR={'ok' if rR is None else rR}, "
              f"assoc(4k)={'ok' if ca is None else ca[0]}")
