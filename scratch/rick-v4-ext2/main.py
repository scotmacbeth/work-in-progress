import numpy as np
from f2lib import mod2, rank, kernel
from modules import (module_from_ab, regular_module, ext_tower, act_elt)

def swap2():  return np.array([[0,1],[1,0]], dtype=np.uint8)
def id2():    return np.array([[1,0],[0,1]], dtype=np.uint8)

# ---- Build M = k[G/A], A=<a>: cosets {e,a},{b,ab}. a fixes, b swaps ----
M = module_from_ab(mat_a=id2(),   mat_b=swap2())   # a trivial, b swap
# ---- Build N = k[G/B], B=<b>: cosets {e,b},{a,ab}. b fixes, a swaps ----
N = module_from_ab(mat_a=swap2(), mat_b=id2())     # a swap, b trivial

print("=== Module identifications ===")
print("M act_a=\n", M['act'][1], "\nM act_b=\n", M['act'][2])
print("N act_a=\n", N['act'][1], "\nN act_b=\n", N['act'][2])

# ---- Res_A N : restrict N to A=<a>. Structure = action of a on N ----
resA_N_a = N['act'][1]
print("\n=== Res_A N : action of generator a ===\n", resA_N_a)
# Identify: free kA (regular) means a acts as a nontrivial swap (single 2-cycle),
# i.e. a is a free permutation. Check: is it the regular rep of Z/2?
# kA regular: a acts by swapping the two basis elts e<->a. That's exactly swap2.
is_free = np.array_equal(resA_N_a, swap2())
print("Res_A N == regular kA (free)?", is_free)

# ---------- Ext^n_{kG}(M, N) two ways ----------
LEN = 4
print("\n=== (1a) Direct: Ext^n_{kG}(M,N) via minimal free resolution ===")
ext_direct, betti = ext_tower(M, N, LEN)
print("Betti numbers of M (ranks of P_n):", betti)
print("dim Ext^n(M,N), n=0..%d:" % LEN, ext_direct)

# ---------- H^n(A; Res_A N) ----------
def group_cohomology_Z2(actgen, degree):
    """H^n(Z/2; W) in char 2. W given by action matrix of the generator.
    x = actgen + I (=g-1). Periodic complex W-x->W-x->...
    H^0 = ker x ; H^{n>=1} = ker x / im x. Returns list dims 0..degree."""
    W = actgen
    d = W.shape[0]
    I = np.eye(d, dtype=np.uint8)
    x = (W + I) & 1
    ker_dim = d - rank(x)
    im_dim = rank(x)
    dims = []
    for n in range(degree+1):
        if n == 0:
            dims.append(ker_dim)                 # invariants
        else:
            dims.append(ker_dim - im_dim)        # ker/im (periodic)
    return dims

print("\n=== (1b) Eckmann-Shapiro: Ext^n_{kG}(M,N) = H^n(A; Res_A N) ===")
es = group_cohomology_Z2(resA_N_a, LEN)
print("H^n(A; Res_A N), n=0..%d:" % LEN, es)
print("AGREE (1a vs 1b)?", ext_direct == es)

# ---------- Part 2: the twist L = det(M) (x) det(N)^{-1} ----------
def det_char(mod):
    """1-dim module = determinant of mod: character g -> det(act(g)) in F2."""
    chars = []
    for u in range(4):
        # det over F2
        from numpy.linalg import det as npdet
        # compute det over F2 via rank-based / explicit for small: use int det mod 2
        M_ = mod['act'][u].astype(np.int64)
        d = round(np.linalg.det(M_))
        chars.append(d & 1)
    return chars  # [det(e),det(a),det(b),det(ab)]

detM = det_char(M)
detN = det_char(N)
print("\n=== (2) Twist L = det(M) (x) det(N)^{-1} ===")
print("det(M) char [e,a,b,ab]:", detM)
print("det(N) char [e,a,b,ab]:", detN)
# L character = det(M)*det(N)^{-1}; over F2, inverse of 1 is 1, and units are all 1
Lchar = [(detM[i] * detN[i]) & 1 for i in range(4)]   # product (F2*, inverse trivial)
print("L character [e,a,b,ab]:", Lchar)
print("L trivial (all 1)?", all(c == 1 for c in Lchar))

# N (x) L : diagonal action g -> Lchar[g]*act_N(g)
def tensor_line(mod, char):
    act = [ (char[u] * mod['act'][u]) & 1 for u in range(4) ]
    return {'d': mod['d'], 'act': act}

NL = tensor_line(N, Lchar)
print("\n=== Ext^n_{kG}(M, N(x)L) ===")
ext_tw, betti_tw = ext_tower(M, NL, LEN)
print("dim Ext^n(M, N(x)L), n=0..%d:" % LEN, ext_tw)
resA_NL_a = NL['act'][1]
es_tw = group_cohomology_Z2(resA_NL_a, LEN)
print("H^n(A; Res_A(N(x)L)), n=0..%d:" % LEN, es_tw)
print("AGREE (twisted, direct vs ES)?", ext_tw == es_tw)
print("Res_A(N(x)L) still free (== swap)?", np.array_equal(resA_NL_a, swap2()))

# ---------- Sanity: also compute Ext^n(M, M) and Ext^n(N,N) etc. for context ----------
print("\n=== Context checks ===")
print("dim Ext^n(M,M):", ext_tower(M, M, LEN)[0])
print("dim Ext^n(N,N):", ext_tower(N, N, LEN)[0])
print("dim Ext^n(M, kG regular):", ext_tower(M, regular_module(), LEN)[0])
print("Betti(M):", betti, " Betti(twisted N same):", betti_tw)
