#!/usr/bin/env python3
"""
WRITE-session self-verification of Rick's uid233 MUST M1.

Claim to re-derive MYSELF (not trust from the Lean leaf / Rick):
  * r_{s0}(s,g) = (s, const_{g(s0)}) IS a bicomodule morphism B -> B'
    (passes BOTH the lambda- and rho-equivariance squares) at shapes
    (2,2),(2,3),(3,2),(1,2),(2,1).
  * e(s,g) = (s, const_{g(s)}) is NOT: it passes rho everywhere but FAILS
    lambda exactly when a non-constant branch map exists (n,m >= 2).
  * Reproduce Rick's explicit (2,2) counterexample at position (0, g=(0,1)).

Model (Mathlib-free, mirrors lean/2026-10-18-retract-bicomodule-map.lean):
  Tree = ('leaf', v) | ('node', s, [children])
  delta(s, ch)      = (s, [ (i, ch) for i in range(len(ch)) ])   # store comult
  fmap u (s, ch)    = (s, [ u(c) for c in ch ])                   # DeltaS(u)
  lam = delta ; rho = fmap delta
  B-element: node s [ (t_0, psi_0), ..., (t_{n-1}, psi_{n-1}) ], branch map
             g = (t_0,...,t_{n-1}) read off the child heads.
  setHead h (s, ch) = (h, ch)       # rewrite head only; r# = id on directions
  e : broadcast head at CURRENT position s ; r_{s0}: at FIXED base s0.
  lamSquare f e = teq( delta(f e), fmap f (delta e) )
  rhoSquare f e = teq( rho(f e),  f (rho e) )
"""

from itertools import product

# ---- Tree engine ---------------------------------------------------------
def leaf(v): return ('leaf', v)
def node(s, ch): return ('node', s, list(ch))

def teq(a, b):
    if a[0] == 'leaf' and b[0] == 'leaf':
        return a[1] == b[1]
    if a[0] == 'node' and b[0] == 'node':
        return a[1] == b[1] and len(a[2]) == len(b[2]) and all(teq(x, y) for x, y in zip(a[2], b[2]))
    return False

def delta(e):
    if e[0] == 'leaf': return e
    s, ch = e[1], e[2]
    return node(s, [node(i, ch) for i in range(len(ch))])

def fmap(u, e):
    if e[0] == 'leaf': return e
    s, ch = e[1], e[2]
    return node(s, [u(c) for c in ch])

def lam(e): return delta(e)
def rho(e): return fmap(delta, e)

def headOf(e): return 0 if e[0] == 'leaf' else e[1]

def setHead(h):
    def f(e):
        if e[0] == 'leaf': return e
        return node(h, e[2])
    return f

def eMap(e):
    if e[0] == 'leaf': return e
    s, ch = e[1], e[2]
    h = headOf(ch[s])                       # head at CURRENT position s
    return node(s, [setHead(h)(c) for c in ch])

def rMap(s0):
    def f(e):
        if e[0] == 'leaf': return e
        s, ch = e[1], e[2]
        h = headOf(ch[s0])                  # head at FIXED base s0
        return node(s, [setHead(h)(c) for c in ch])
    return f

def lamSquare(f, e): return teq(lam(f(e)), fmap(f, lam(e)))
def rhoSquare(f, e): return teq(rho(f(e)), f(rho(e)))

# ---- carrier B(Fin k) = DeltaS(DeltaT(Fin k)) ----------------------------
def ground(k): return [leaf(v) for v in range(k)]

def dtElems(m, k):
    out = []
    for t in range(m):
        for psi in product(ground(k), repeat=m):
            out.append(node(t, list(psi)))
    return out

def bElems(n, m, k):
    out = []
    dt = dtElems(m, k)
    for s in range(n):
        for phi in product(dt, repeat=n):
            out.append(node(s, list(phi)))
    return out

def heads(e): return [] if e[0] == 'leaf' else [headOf(c) for c in e[2]]
def gConst(e):
    h = heads(e)
    return all(x == h[0] for x in h) if h else True
def bpElems(n, m, k): return [e for e in bElems(n, m, k) if gConst(e)]

# ---- checks --------------------------------------------------------------
SHAPES = [(2,2),(2,3),(3,2),(1,2),(2,1)]
K = 2
ok = True

print("== r_{s0=0}: both squares on ALL of B ==")
for (n, m) in SHAPES:
    B = bElems(n, m, K)
    r = rMap(0)
    rlam = all(lamSquare(r, e) for e in B)
    rrho = all(rhoSquare(r, e) for e in B)
    ridem = all(teq(r(r(e)), r(e)) for e in B)
    rimg = all(gConst(r(e)) for e in B)
    rret = all(teq(r(e), e) for e in bpElems(n, m, K))
    good = rlam and rrho and ridem and rimg and rret
    ok &= good
    print(f"  (n,m)=({n},{m}) |B|={len(B):4d}  lam={rlam} rho={rrho} idem={ridem} imgB'={rimg} retract={rret}  {'OK' if good else 'FAIL'}")

print("== e: rho everywhere, lambda fails iff non-constant g exists ==")
for (n, m) in SHAPES:
    B = bElems(n, m, K)
    erho = all(rhoSquare(eMap, e) for e in B)
    elam = all(lamSquare(eMap, e) for e in B)
    elam_bp = all(lamSquare(eMap, e) for e in bpElems(n, m, K))  # control: on B' e passes
    expect_lam = (n == 1 or m == 1)                              # passes iff all g constant
    good = erho and (elam == expect_lam) and elam_bp
    ok &= good
    print(f"  (n,m)=({n},{m})  rho={erho} lam(all B)={elam} (expect {expect_lam}) lam(B')={elam_bp}  {'OK' if good else 'FAIL'}")

print("== Rick's explicit (2,2) witness: pos (0, g=(0,1)), psi=(0,0) ==")
witE = node(0, [node(0, [leaf(0), leaf(0)]), node(1, [leaf(0), leaf(0)])])
B22 = bElems(2, 2, 2)
w_mem = any(teq(witE, e) for e in B22)
w_nonconst = not gConst(witE)
w_e_lam = lamSquare(eMap, witE)          # expect False
w_r0_lam = lamSquare(rMap(0), witE)      # expect True
w_r1_lam = lamSquare(rMap(1), witE)      # expect True
w_e_rho = rhoSquare(eMap, witE)          # expect True
good = w_mem and w_nonconst and (w_e_lam is False) and w_r0_lam and w_r1_lam and w_e_rho
ok &= good
print(f"  in B={w_mem} nonconst={w_nonconst} | e-lam={w_e_lam} (want False) "
      f"r0-lam={w_r0_lam} r1-lam={w_r1_lam} e-rho={w_e_rho}  {'OK' if good else 'FAIL'}")

# Show WHAT breaks e's lambda-square on the witness (for the write-up prose).
print("  -- diagnosis of the lambda-square on the witness --")
print("     delta(e(wit))   =", eMap(witE), "-> delta ->", delta(eMap(witE)))
print("     fmap e (delta wit) =", fmap(eMap, delta(witE)))

print("\nALL CHECKS PASS" if ok else "\n*** SOME CHECK FAILED ***")
