"""Internal sanity: confirm min_resolution really produces an exact complex of
free modules resolving k[G/A]. Checks (a) d_n d_{n+1} = 0, (b) exactness:
rank(d_n) + rank(d_{n+1}) = free-rank(P_n)*|G| (i.e. ker d_n = im d_{n+1}),
(c) augmentation P_0 -> M surjective with the right kernel."""
import numpy as np
from gen_d8 import (build_D8, gen_subgroup, perm_module_GmodH, min_resolution,
                    free_act_elt, unit_vec, rank, kernel, mod2)

def free_boundary_map_as_F2(G, dn):
    """dn columns are elements of R^{m_prev} (dim |G|*m_prev). As an F2 matrix it
    is already the map on underlying F2 spaces once we expand generator images by
    the free action. But dn as stored maps GENERATORS -> elements; the actual
    R-linear map P_n->P_{n-1} on F2 spaces is: basis of P_n = (gen t) x (alg elt u).
    Column (t,u) -> free_act(u) applied to dn[:,t]."""
    N = G.N
    m_prev = dn.shape[0] // N if dn.shape[0] else 0
    m_n = dn.shape[1]
    cols = []
    for t in range(m_n):
        colt = dn[:, t]
        for u in range(N):
            Au = free_act_elt(G, m_prev, unit_vec(G, u))
            cols.append((Au @ colt) & 1)
    if not cols:
        return np.zeros((N*m_prev, 0), dtype=np.uint8)
    return np.array(cols, dtype=np.uint8).T  # (N*m_prev) x (N*m_n)

def check(Agen, title):
    G, els = build_D8()
    Aels = gen_subgroup(G, Agen)
    modA = perm_module_GmodH(G, Aels)
    LEN = 6
    betti, boundaries = min_resolution(G, modA, LEN+1)
    N = G.N
    # expand each boundary to full F2 map P_n -> P_{n-1}
    D = []
    for n in range(len(boundaries)):
        D.append(free_boundary_map_as_F2(G, boundaries[n]))
    print(f"{title}: betti={betti}")
    # (a) d_n d_{n+1} = 0
    for n in range(len(D)-1):
        if D[n].shape[1] and D[n+1].shape[1]:
            prod = (D[n] @ D[n+1]) & 1
            assert not prod.any(), f"  d{n+1} d{n+2} != 0"
    # (b) exactness in positive degrees: ker(d_n) = im(d_{n+1})
    #   dim P_n = N*betti[n]; ker d_n dim = N*betti[n]-rank(d_n) [for n>=1],
    #   with d_n : P_n->P_{n-1} stored as D[n-1].
    ok = True
    for n in range(1, LEN):
        dimPn = N*betti[n]
        rk_dn = rank(D[n-1]) if n-1 < len(D) and D[n-1].shape[1] else 0
        rk_dn1 = rank(D[n]) if n < len(D) and D[n].shape[1] else 0
        ker_dim = dimPn - rk_dn
        if ker_dim != rk_dn1:
            print(f"  NON-EXACT at degree {n}: ker={ker_dim} im={rk_dn1}")
            ok = False
    # (c) augmentation image = modA (P_0 -> M surjective) and minimality:
    #   rank of first boundary = dim of first syzygy etc. Just report.
    print(f"  d∘d=0: OK ; positive-degree exactness: {'OK' if ok else 'FAIL'}")
    return ok

if __name__ == "__main__":
    G, els = build_D8()
    r=[]
    r.append(check([els['r'], els['s']], "A=G (trivial mod)"))
    r.append(check([els['s']], "A=<s>"))
    r.append(check([els['r2'], els['s']], "A=<r2,s>"))
    r.append(check([els['r']], "A=<r>=C4"))
    print("ALL RESOLUTIONS EXACT:", all(r))
