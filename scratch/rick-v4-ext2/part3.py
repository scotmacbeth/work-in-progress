import numpy as np
from f2lib import mod2, rank
from modules import module_from_ab, regular_module, ext_tower, act_elt
from hyper import resolve, comparison_map, hom_diff_free

def swap2():  return np.array([[0,1],[1,0]], dtype=np.uint8)
def id2():    return np.array([[1,0],[0,1]], dtype=np.uint8)

M  = module_from_ab(id2(),   swap2())      # k[G/A]
N  = module_from_ab(swap2(), id2())        # k[G/B]
kG = regular_module()

# ---- kG-linearity checker ----
def is_kG_linear(phi, src, tgt):
    for u in range(4):
        lhs = (tgt['act'][u] @ phi) & 1
        rhs = (phi @ src['act'][u]) & 1
        if not np.array_equal(lhs, rhs):
            return False
    return True

# ---- natural maps ----
# transfer f: M=k[G/A] -> kG,   coset {e,a}->e+a, {b,ab}->b+ab
f = np.array([[1,0],
              [1,0],
              [0,1],
              [0,1]], dtype=np.uint8)      # 4x2  (kG-dim x M-dim)
# projection g: kG -> N=k[G/B],  e,b->coset0={e,b}; a,ab->coset1={a,ab}
g = np.array([[1,0,1,0],
              [0,1,0,1]], dtype=np.uint8)  # 2x4  (N-dim x kG-dim)

print("f: M->kG kG-linear?", is_kG_linear(f, M, kG))
print("g: kG->N kG-linear?", is_kG_linear(g, kG, N))
comp = (g @ f) & 1
print("composite g o f (M->N):\n", comp, " rank=", rank(comp))
print("=> 3-term sequence k[G/A]->kG->k[G/B] is a chain complex?", not comp.any())

# ---------------- mapping-cone hyper-Ext ----------------
def cone_hyperext(phi, C0, C1, N, L):
    """Hyper-Ext^k RHom(Cone(phi), N), phi:C0->C1.
    Cone(phi)_n = P_{n-1}(C0) (+) Q_n(C1); represents complex [C0(hdeg1) -> C1(hdeg0)]."""
    P = resolve(C0, L+1)
    Q = resolve(C1, L+1)
    fcomp = comparison_map(P, phi, C0, C1, Q, L+1)
    bP = P['betti']; bQ = Q['betti']
    def rankF(n):   # ambient dim of cone free module F_n
        pr = bP[n-1] if n-1 >= 0 else 0
        qr = bQ[n]   if n   < len(bQ) else 0
        return 4*pr, 4*qr   # (P-part dim, Q-part dim)
    # boundary of cone: d_n : F_n -> F_{n-1}
    def cone_bnd(n):
        # rows: P_{n-2} (+) Q_{n-1};  cols: P_{n-1} (+) Q_n
        pPrev = bP[n-2] if n-2 >= 0 else 0
        qPrev = bQ[n-1] if n-1 >= 0 else 0
        pCur  = bP[n-1] if n-1 >= 0 else 0
        qCur  = bQ[n]   if n   < len(bQ) else 0
        R = 4*pPrev + 4*qPrev
        Cc = 4*pCur + 4*qCur
        Mtx = np.zeros((R, Cc), dtype=np.uint8)
        # top-left  d^P_{n-1}: P_{n-1}->P_{n-2}
        if pPrev>0 and pCur>0 and n-1 >= 1 and P['bnd_full'][n-1] is not None:
            dP = P['bnd_full'][n-1]
            Mtx[0:4*pPrev, 0:4*pCur] = dP
        # bottom-left f_{n-1}: P_{n-1}->Q_{n-1}
        if qPrev>0 and pCur>0:
            fnm1 = fcomp[n-1]
            Mtx[4*pPrev:4*pPrev+4*qPrev, 0:4*pCur] = fnm1
        # bottom-right d^Q_n: Q_n->Q_{n-1}
        if qPrev>0 and qCur>0 and n >= 1 and Q['bnd_full'][n] is not None:
            dQ = Q['bnd_full'][n]
            Mtx[4*pPrev:4*pPrev+4*qPrev, 4*pCur:4*pCur+4*qCur] = dQ
        return Mtx
    dN = N['d']
    ranks = [ (bP[n-1] if n-1>=0 else 0) + (bQ[n] if n<len(bQ) else 0) for n in range(L+2) ]
    dims = [dN*r for r in ranks]
    # cochain differentials delta^k: C^k->C^{k+1} induced by cone_bnd(k+1)
    diffs=[]
    for k in range(L+1):
        B = cone_bnd(k+1)
        if B.size==0:
            diffs.append(np.zeros((dims[k+1], dims[k]), dtype=np.uint8))
        else:
            diffs.append(hom_diff_free(B, N))
    hext=[]
    for k in range(L+1):
        Ck=dims[k]
        dk=diffs[k]
        if dk.shape[1]!=Ck:
            dk=np.zeros((dk.shape[0],Ck),dtype=np.uint8)
        ker=Ck-rank(dk)
        im=0 if k==0 else rank(diffs[k-1])
        hext.append(ker-im)
    return hext

L=4
# sanity: Cone(id_M) must be acyclic -> all zero
print("\n[sanity] HExt(Cone(id_M), N):", cone_hyperext(np.eye(2,dtype=np.uint8), M, M, N, L))
# sanity: Cone(0: 0->N) -> just Ext(N,N) in degree 0
zero0 = np.zeros((N['d'],0),dtype=np.uint8)  # skip; use zero map M->N instead
print("[sanity] HExt(Cone(zeromap M->N), N):", cone_hyperext(np.zeros((N['d'],M['d']),dtype=np.uint8), M, N, N, L))
print("         (compare Ext(N,N)=",ext_tower(N,N,L)[0]," and Ext(M,N)=",ext_tower(M,N,L)[0],")")

print("\n=== Mapping cones for the natural maps ===")
hf = cone_hyperext(f, M, kG, N, L)
print("HExt^k(Cone(f: k[G/A]->kG), N), k=0..%d:"%L, hf)
hg = cone_hyperext(g, kG, N, N, L)
print("HExt^k(Cone(g: kG->k[G/B]), N), k=0..%d:"%L, hg)

# For reference, the constituent Ext towers
print("\nExt(M=k[G/A], N):", ext_tower(M,N,L)[0])
print("Ext(kG, N):       ", ext_tower(kG,N,L)[0])
print("Ext(N=k[G/B], N): ", ext_tower(N,N,L)[0])
