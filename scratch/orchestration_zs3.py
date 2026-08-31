"""
A GENUINELY NONTRIVIAL coherent orchestration composition:
two supervisors over a shared worker pool whose dispatches interleave nontrivially
but consistently -> the joint agent is the Zappa-Szep (here semidirect) product
S_3 = Z/3 |><| Z/2.

  C = Z/3 = {0,1,2}   supervisor-C's dispatch counter mod 3 (cyclic worker rotation)
  D = Z/2 = {0,1}     supervisor-D's toggle
  left action ^d c :  d=1 REVERSES C's rotation, c |-> -c mod 3  (Aut(Z/3)=Z/2)
  right action d^c = d  (trivial) -> this is the SEMIDIRECT case, a valid ZS product.

ZS1-ZS4 hold (dihedral relation) => the two orchestrations FUSE into one consistent
joint agent S_3. Nontrivial: the order of the two supervisors' moves matters, yet
composition is well-defined (no obstruction). Contrast with K_bug where it is NOT.
"""
from pairwise_zs_check import FinCat, check_zs_axioms, build_zs_product


def cyclic(n, name):
    """One object 'O', End = Z/n = {e0,...,e_{n-1}}, e_i o e_j = e_{i+j mod n}."""
    objs = ["O"]
    els = [f"{name}{i}" for i in range(n)]
    arrows = {e: ("O", "O") for e in els}
    comp = {}
    for i in range(n):
        for j in range(n):
            comp[(els[i], els[j])] = els[(i + j) % n]
    return FinCat(objs, arrows, comp, {"O": f"{name}0"}), els


print("=" * 72)
print("NONTRIVIAL COHERENT COMPOSITION:  S_3 = Z/3 |><| Z/2  (dihedral matched pair)")
C, cel = cyclic(3, "c")   # c0,c1,c2
D, del_ = cyclic(2, "d")  # d0,d1
# left action: ^{d1} c_i = c_{-i};  ^{d0} c_i = c_i.  right action trivial d^c=d.
def inv3(ci): return {"c0": "c0", "c1": "c2", "c2": "c1"}[ci]
lam = {}
for d in D.arrows:
    for c in C.arrows:
        lc = inv3(c) if d == "d1" else c
        lam[(d, c)] = (lc, d)   # (^d c, d^c=d)

ax = check_zs_axioms(C, D, lam, verbose=True)
print("  ZS1-ZS4 + units hold:", ax)
K = build_zs_product(C, D, lam)
print("  C |><| D is a category:", K.check_category(verbose=True))
print("  # morphisms:", len(K.arrows), "(expect 6 = |S_3|)")

# confirm it's genuinely nonabelian (the join is nontrivial): c1 . d1 != d1 . c1
# in K, morphisms are pairs (c,d). compose (c1,d0)(c0,d1) vs (c0,d1)(c1,d0):
m_c1 = ("c1", "d0")   # pure C-move
m_d1 = ("c0", "d1")   # pure D-move
cd = K.compose(m_c1, m_d1)   # c1 after d1
dc = K.compose(m_d1, m_c1)   # d1 after c1
print(f"  (c1)o(d1) = {cd} ;  (d1)o(c1) = {dc} ;  differ? {cd != dc}  (nonabelian join)")

print("\n" + "=" * 72)
print("FINAL TABLE  --  shared-worker orchestration topology  ->  composable?")
print("-" * 72)
rows = [
    ("independent supervisors (read-only workers)",
     "trivial law delta=swap", "COMPOSES", "K = C x D"),
    ("two supervisors, coherent nontrivial interleaving",
     "semidirect Z/3|><|Z/2", "COMPOSES", "K = S_3, H^1=torsor"),
    ("re-entry, state-protected (lock)",
     "K_ok: token decoupled", "COMPOSES", "#SFS=2, [omega]=0"),
    ("re-entry, UNPROTECTED (worker flips sup state)",
     "K_bug ~= rigid twist", "OBSTRUCTED", "#SFS=0, [omega]=gen Z/2"),
]
print(f"  {'topology':50s} {'verdict':11s} {'invariant'}")
for topo, mech, verdict, inv in rows:
    print(f"  {topo:50s} {verdict:11s} {inv}")
print("-" * 72)
print("  The single bit that flips verdict: does a worker's outcome MUTATE the")
print("  supervisor's shared state?  If yes -> [omega] != 0 -> no joint agent.")
