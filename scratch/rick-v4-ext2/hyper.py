"""
Hyper-Ext / mapping-cone computations for bounded complexes of F2[V4]-modules.
Builds explicit minimal free resolutions with augmentation + full boundary matrices,
comparison chain maps lifting a module map, and total-complex cohomology.
"""
import numpy as np
from f2lib import mod2, rank, kernel, solve
from modules import (min_generators, phi_matrix, act_elt, act_elt_regular,
                     free_act_elt, submodule_as_module, unit_vec)

def full_map_from_gen_images(images, tgt_act_fn):
    """images: list of column vectors (in target ambient space) = images of source generators.
       tgt_act_fn(u): action matrix of basis elt u on target module.
    Returns matrix (tgt_dim x 4*len(images)) : full R-linear map from R^{len} to target.
    Source R^{len} basis ordering: block t (0..len-1), within block u=0..3."""
    cols = []
    for t in range(len(images)):
        for u in range(4):
            cols.append((tgt_act_fn(u) @ images[t]) & 1)
    if not cols:
        # target dim from tgt_act_fn(0)
        return np.zeros((tgt_act_fn(0).shape[0], 0), dtype=np.uint8)
    return np.array(cols, dtype=np.uint8).T

def resolve(mod, length):
    """Full minimal free resolution data.
    Returns dict with:
      betti[n],
      gens[n]      : generators of the n-th syzygy as vectors in ambient of that syzygy module,
      auxmod[n]    : module dict at level n (auxmod[0]=mod, auxmod[n]= n-th syzygy submodule as module),
      aug[n]       : matrix P_n -> auxmod[n] ambient  (dim auxmod[n]['d'] x 4*betti[n]),
      bnd_full[n]  : full R-map matrix d_n : P_n -> P_{n-1}  (dim 4*betti[n-1] x 4*betti[n]), for n>=1.
    P_n free of rank betti[n]. The composite P_n -> P_{n-1} -> ... -> P_0 -> mod is the resolution."""
    betti = []
    gens_list = []
    auxmod = []
    aug = []
    bnd_full = [None]  # index 0 unused (no d_0)

    cur = mod
    gens = min_generators(cur)
    betti.append(len(gens)); gens_list.append(gens); auxmod.append(cur)
    aug.append(phi_matrix(gens, cur))   # P_0 -> mod

    for n in range(1, length+1):
        phi = aug[n-1] if n == 1 else None
        # kernel of the map P_{n-1} -> auxmod[n-1] (the aug at level n-1 composed appropriately)
        # The map whose kernel is the (n)-th syzygy is: P_{n-1} -> auxmod[n-1], = phi_matrix(gens_{n-1}, auxmod[n-1])
        phi_prev = phi_matrix(gens_list[n-1], auxmod[n-1])
        K = kernel(phi_prev)                     # (4*betti[n-1]) x r
        if K.shape[1] == 0:
            betti.append(0); gens_list.append([]);
            auxmod.append({'d':0,'act':[np.zeros((0,0),dtype=np.uint8)]*4})
            aug.append(np.zeros((0,0),dtype=np.uint8))
            bnd_full.append(np.zeros((4*betti[n-1],0),dtype=np.uint8))
            for _ in range(n+1, length+1):
                betti.append(0); gens_list.append([])
                auxmod.append({'d':0,'act':[np.zeros((0,0),dtype=np.uint8)]*4})
                aug.append(np.zeros((0,0),dtype=np.uint8))
                bnd_full.append(np.zeros((0,0),dtype=np.uint8))
            break
        Kmod, Kincl = submodule_as_module(K)     # Kmod in own basis (dim r), Kincl: r-basis -> P_{n-1} ambient
        kgens = min_generators(Kmod)             # vectors in F2^r
        m_n = len(kgens)
        betti.append(m_n); gens_list.append(kgens); auxmod.append(Kmod)
        aug.append(phi_matrix(kgens, Kmod))      # P_n -> Kmod
        # boundary d_n : P_n -> P_{n-1}: generator t -> Kincl @ kgens[t]  (element of P_{n-1} ambient)
        images = [ (Kincl @ g) & 1 for g in kgens ]
        prev_rank = betti[n-1]
        tgt_act = lambda u, pr=prev_rank: free_act_elt(pr, unit_vec(u))
        bnd_full.append(full_map_from_gen_images(images, tgt_act))
    return {'betti':betti, 'gens':gens_list, 'auxmod':auxmod, 'aug':aug, 'bnd_full':bnd_full}

def comparison_map(res_src, phi_mat, src_mod, tgt_mod, res_tgt, length):
    """Lift a module map phi: src_mod -> tgt_mod (matrix tgt_dim x src_dim) to a chain map
    f_n : P_n(src) -> Q_n(tgt).  Returns list f[0..length], each a matrix (4*b^Q_n x 4*b^P_n)."""
    f = []
    # f_0: for each generator t of P_0(src) with image gens_src[0][t] in src_mod,
    # need z in Q_0 ambient with aug_Q0 (z) = phi @ gens_src[t].
    augQ0 = res_tgt['aug'][0]     # tgt_mod['d'] x 4*bQ0
    gens_src0 = res_src['gens'][0]
    images0 = []
    for t in range(res_src['betti'][0]):
        target = (phi_mat @ gens_src0[t]) & 1
        z = solve(augQ0, target.reshape(-1,1))[:,0]   # in F2^{4 bQ0}
        images0.append(z)
    bQ0 = res_tgt['betti'][0]
    tgt_act0 = lambda u: free_act_elt(bQ0, unit_vec(u))
    f0 = full_map_from_gen_images(images0, tgt_act0)
    f.append(f0)

    for n in range(1, length+1):
        bPn = res_src['betti'][n]
        bQn = res_tgt['betti'][n]
        bQprev = res_tgt['betti'][n-1]
        if bPn == 0:
            f.append(np.zeros((4*bQn, 0), dtype=np.uint8))
            continue
        dQn = res_tgt['bnd_full'][n]     # 4*bQprev x 4*bQn
        fprev = f[n-1]                   # 4*bQprev x 4*bPn... actually 4*bQ_{n-1} x 4*bP_{n-1}
        dPn = res_src['bnd_full'][n]     # 4*bP_{n-1} x 4*bPn
        images = []
        gens_srcn = res_src['gens'][n]
        for t in range(bPn):
            # gen t of P_n -> d_Pn(gen t) is column of ... but bnd_full columns are per (u,t)?
            # bnd_full is full map; generator t corresponds to source basis index (t, u=0) => column t*4+0
            col = dPn[:, t*4 + 0]                 # d^P_n(gen_t) in P_{n-1} ambient
            y = (fprev @ col) & 1                 # in Q_{n-1} ambient
            # solve dQn w = y
            if dQn.shape[1] == 0:
                w = np.zeros(0, dtype=np.uint8)
            else:
                w = solve(dQn, y.reshape(-1,1))[:,0]
            images.append(w)
        tgt_actn = lambda u, r=bQn: free_act_elt(r, unit_vec(u))
        fn = full_map_from_gen_images(images, tgt_actn)
        f.append(fn)
    return f

def hom_diff_free(bnd_full, N):
    """Induced Hom(-,N) differential from a full R-map d: R^{m} -> R^{m'} (bnd_full: 4m' x 4m).
    Hom(R^{m},N)=N^{m}. Returns matrix (dN*m' x dN*m) mapping Hom(R^{m'},N)->Hom(R^{m},N)??
    Careful: precompose. d: P->P' means Hom(P',N)->Hom(P,N).
    Here bnd_full given as d_n: P_n -> P_{n-1} (4*b_{n-1} x 4*b_n). Induces Hom(P_{n-1},N)->Hom(P_n,N).
    A hom in Hom(P_{n-1},N) is data (g_0..g_{b_{n-1}-1}) in N. (g d)(gen_t of P_n) = g(d gen_t).
    d gen_t (in P_{n-1} ambient) = column t*4+0. = sum_i w^i (blocks). g(w)=sum act_N(w^i) g_i."""
    dN = N['d']
    rows_amb, cols_amb = bnd_full.shape
    m_prev = rows_amb // 4
    m_n = cols_amb // 4
    out = np.zeros((dN*m_n, dN*m_prev), dtype=np.uint8)
    for t in range(m_n):
        col = bnd_full[:, t*4+0]
        for i in range(m_prev):
            w = col[4*i:4*i+4]
            out[dN*t:dN*t+dN, dN*i:dN*i+dN] = act_elt(N, w)
    return out
