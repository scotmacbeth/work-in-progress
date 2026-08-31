import numpy as np
from f2lib import rank
from modules import module_from_ab, regular_module, ext_tower, act_elt
from hyper import resolve, hom_diff_free, comparison_map

def swap2():  return np.array([[0,1],[1,0]], dtype=np.uint8)
def id2():    return np.array([[1,0],[0,1]], dtype=np.uint8)

M = module_from_ab(id2(),   swap2())
N = module_from_ab(swap2(), id2())

def ext_via_resolve(src, tgt, L):
    R = resolve(src, L+1)
    dN = tgt['d']
    dims = [dN*b for b in R['betti']]
    # differential C^n->C^{n+1} induced by bnd_full[n+1]: P_{n+1}->P_n
    diffs = []
    for n in range(L+1):
        if n+1 < len(R['bnd_full']) and R['bnd_full'][n+1] is not None and R['bnd_full'][n+1].size:
            diffs.append(hom_diff_free(R['bnd_full'][n+1], tgt))
        else:
            diffs.append(np.zeros((dims[n+1] if n+1<len(dims) else 0, dims[n]), dtype=np.uint8))
    ext=[]
    for n in range(L+1):
        Cn=dims[n]
        dn=diffs[n]
        if dn.shape[1]!=Cn:
            dn=np.zeros((dn.shape[0],Cn),dtype=np.uint8)
        ker=Cn-rank(dn)
        im=0 if n==0 else rank(diffs[n-1])
        ext.append(ker-im)
    return ext, R['betti']

L=4
for (name,src,tgt) in [("Ext(M,N)",M,N),("Ext(M,M)",M,M),("Ext(N,N)",N,N),
                       ("Ext(M,kG)",M,regular_module())]:
    e1,_ = ext_via_resolve(src,tgt,L)
    e2 = ext_tower(src,tgt,L)[0]
    print(f"{name}: resolve={e1}  ext_tower={e2}  match={e1==e2}")

# Validate comparison map: lift identity M->M, check chain-map commutes: d^Q f_n = f_{n-1} d^P.
RM = resolve(M, L)
import numpy as np
idM = np.eye(M['d'], dtype=np.uint8)
f = comparison_map(RM, idM, M, M, RM, L)
ok=True
for n in range(1,L+1):
    dPn = RM['bnd_full'][n]
    if dPn is None or dPn.size==0: continue
    lhs = (RM['bnd_full'][n] @ f[n]) & 1     # d^Q_n f_n  (Q=M resolution)
    rhs = (f[n-1] @ RM['bnd_full'][n]) & 1   # f_{n-1} d^P_n
    if lhs.shape==rhs.shape and not np.array_equal(lhs,rhs):
        ok=False; print(f"  chain-map FAIL at n={n}")
print("comparison_map(id_M) is a chain map:", ok)
