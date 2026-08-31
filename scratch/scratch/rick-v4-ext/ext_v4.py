"""
Ext^1_{kV4}(M,N) over k = F_2, V4 = Klein four in S4.

Group V4 = {e,a,b,c}, a=(12)(34), b=(13)(24), c=(14)(23)=ab.
Index elements 0=e,1=a,2=b,3=c ; multiplication = XOR of Z/2 x Z/2 codes:
   e=(0,0) a=(1,0) b=(0,1) c=(1,1).

Modules (2-dim over F2):
   M = k[V4/A], A=<a>.  Cosets {A, bA}.  a fixes, b swaps, c swaps.
       rho_M(a)=I, rho_M(b)=S, rho_M(c)=S     with S=[[0,1],[1,0]]
   N = k[V4/B], B=<b>.  Cosets {B, aB}.  b fixes, a swaps, c swaps.
       rho_N(a)=S, rho_N(b)=I, rho_N(c)=S

All linear algebra over GF(2), hand-rolled.
"""

import itertools

# ---------- GF(2) linear algebra ----------
def rref(rows, ncols):
    """rows: list of int bitmasks (bit j = column j). Return (rref rows, pivot cols)."""
    rows = [r for r in rows]
    pivots = []
    r = 0
    for c in range(ncols):
        bit = 1 << c
        piv = None
        for i in range(r, len(rows)):
            if rows[i] & bit:
                piv = i; break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and (rows[i] & bit):
                rows[i] ^= rows[r]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    rows = [x for x in rows if x != 0]
    return rows, pivots

def rank(rows, ncols):
    return len(rref(rows, ncols)[0])

def nullspace(rows, ncols):
    """Basis of {x : A x = 0} where each row of A is a bitmask over ncols vars.
       Returns list of bitmask solutions."""
    R, piv = rref(rows, ncols)
    pivset = set(piv)
    free = [c for c in range(ncols) if c not in pivset]
    # express pivot vars in terms of free vars
    basis = []
    for f in free:
        x = 1 << f
        for row in R:
            # leading col of row
            lead = (row & -row).bit_length() - 1
            # value at free col f in this row
            if row & (1 << f):
                x ^= (1 << lead)
        basis.append(x)
    return basis

def mat_to_rows(M):
    """M: list of rows, each row list of 0/1. Return list of bitmasks."""
    out = []
    for row in M:
        m = 0
        for j, v in enumerate(row):
            if v & 1:
                m |= (1 << j)
        out.append(m)
    return out

# ---------- group ----------
def mul(g, h):   # XOR on 2-bit codes 0..3
    return g ^ h
ELTS = [0,1,2,3]  # e,a,b,c
INV = {g: g for g in ELTS}  # every elt order<=2

I2 = [[1,0],[0,1]]
S  = [[0,1],[1,0]]

def matmul(A, B):
    n=len(A); m=len(B[0]); p=len(B)
    return [[ sum(A[i][k]*B[k][j] for k in range(p))%2 for j in range(m)] for i in range(n)]

rhoM = {0:I2, 1:I2, 2:S, 3:S}
rhoN = {0:I2, 1:S,  2:I2,3:S}

# sanity: representation homomorphism
for g in ELTS:
    for h in ELTS:
        assert matmul(rhoM[g],rhoM[h])==rhoM[mul(g,h)], (g,h)
        assert matmul(rhoN[g],rhoN[h])==rhoN[mul(g,h)]
print("rho_M, rho_N are valid representations.")

# ===================================================================
# Hom_{kV4}(X,Y): matrices phi (dimY x dimX) with rhoY(g) phi = phi rhoX(g) all g
# ===================================================================
def hom_space(rhoX, dimX, rhoY, dimY):
    # unknown phi entries: dimY*dimX, var index = i*dimX + j (phi[i][j])
    nvar = dimX*dimY
    eqrows = []
    for g in ELTS:
        RX = rhoX[g]; RY = rhoY[g]
        # (RY phi)[i][j] - (phi RX)[i][j] = 0
        for i in range(dimY):
            for j in range(dimX):
                row = 0
                # (RY phi)[i][j] = sum_k RY[i][k] phi[k][j]
                for k in range(dimY):
                    if RY[i][k]:
                        row ^= (1 << (k*dimX + j))
                # (phi RX)[i][j] = sum_k phi[i][k] RX[k][j]
                for k in range(dimX):
                    if RX[k][j]:
                        row ^= (1 << (i*dimX + k))
                if row: eqrows.append(row)
    dim = nvar - rank(eqrows, nvar)
    return dim

dimHomMN = hom_space(rhoM,2,rhoN,2)
dimHomMM = hom_space(rhoM,2,rhoM,2)
print("dim Hom_kV4(M,N) =", dimHomMN)
print("dim Hom_kV4(M,M) =", dimHomMM)

# ===================================================================
# METHOD 2: Ext^1(M,N) = H^1(V4, Hom_k(M,N)) with conjugation action
#   (g.phi) = rhoY(g) phi rhoX(g)^{-1},  inverse = self
#   W = Hom_k(M,N), dim = dimX*dimY = 4.  Basis E_{ij} -> var index i*dimX+j
#   group action matrices on W (4-dim), then standard cochain H^1.
# ===================================================================
def hom_module(rhoX, dimX, rhoY, dimY):
    """Return action matrices (dim = dimX*dimY) of each g on Hom_k(X,Y),
       g.phi = rhoY(g) phi rhoX(g)^{-1}."""
    d = dimX*dimY
    act = {}
    for g in ELTS:
        RY = rhoY[g]; RXi = rhoX[INV[g]]
        M = [[0]*d for _ in range(d)]
        # image of basis matrix E_{ab} (a in dimY rows, b in dimX cols): phi=E_ab
        # result R = RY E_ab RXi ; R[i][j] = RY[i][a]*RXi[b][j]
        for a in range(dimY):
            for b in range(dimX):
                col = a*dimX + b
                for i in range(dimY):
                    for j in range(dimX):
                        val = (RY[i][a]*RXi[b][j])%2
                        if val:
                            M[i*dimX+j][col] ^= 1
        act[g] = M
    return act, d

def H1(act, d):
    """H^1(V4, W) via full (non-normalized) cochain complex.
       C0=W (dim d), C1=Fun(G,W) (dim 4d), C2=Fun(GxG,W) (dim 16d).
       d0(w)(g)=g.w - w
       d1(f)(g,h)= g.f(h) - f(gh) + f(g)   (mod 2: signs irrelevant)
    """
    G = ELTS
    def apply(g, vecmask):
        # act[g] as matrix times vector given as bitmask over d coords -> bitmask
        M = act[g]; out = 0
        for i in range(d):
            s = 0
            for j in range(d):
                if (vecmask >> j) & 1:
                    s ^= M[i][j]
            if s: out |= (1 << i)
        return out
    # --- im d0 : columns are d0(basis w) ---
    imd0 = []
    for wi in range(d):
        wmask = 1 << wi
        # vector in C1: for each g store g.w - w  (mod2 => g.w ^ w)
        col = 0
        for gi, g in enumerate(G):
            block = apply(g, wmask) ^ wmask
            col |= block << (gi*d)   # place block for group elt g
        imd0.append(col)
    # --- ker d1 in C1 ---
    # C1 coordinate: (g index gi, coord in W) -> bit gi*d + coord
    # build d1 as linear map C1 -> C2, then nullspace.
    # C2 coordinate: (g,h) pair index ph = gi*4+hi, coord -> bit ph*d+coord
    d1rows = []  # each row = equation? We need matrix; build columns image of each C1 basis then transpose via building rows of the map.
    # Build map matrix rows: for each output coordinate, express as XOR of input coords.
    ncol_in = 4*d
    ncol_out = 16*d
    # We'll construct output-as-function-of-input: for each input basis vector compute image, store as columns; nullspace wants rows = the linear map with inputs as variables.
    # Represent linear map by list of output bitmasks per input basis? Easier: assemble equations rows over input vars for each output coord.
    # out_coord(ph, coord) = sum over inputs contributing. We'll accumulate.
    eqs = [0]*ncol_out  # bitmask over input vars for each output coordinate
    for gi, g in enumerate(G):
        for hi, h in enumerate(G):
            ph = gi*4 + hi
            gh = mul(g,h);
            # term g.f(h): f(h) is input block hi. g. acts via act[g].
            # For each output coord i: (act[g] applied to input block h)[i] + f(gh)[i] + f(g)[i]
            Mg = act[g]
            for i in range(d):
                outbit = ph*d + i
                acc = 0
                # g.f(h): sum_j Mg[i][j] * inputvar(hi, j)
                for j in range(d):
                    if Mg[i][j]:
                        acc ^= (1 << (hi*d + j))
                # - f(gh): input var (index of gh, i)
                ghi = G.index(gh)
                acc ^= (1 << (ghi*d + i))
                # + f(g): input var (gi, i)
                acc ^= (1 << (gi*d + i))
                eqs[outbit] ^= acc
    # ker d1 = nullspace of eqs (rows = eqs over ncol_in vars)
    ker = nullspace([e for e in eqs if e], ncol_in)
    dim_ker = len(ker)
    # dim im d0
    dim_imd0 = rank(imd0, ncol_in)
    dimH1 = dim_ker - dim_imd0
    return dimH1, dim_ker, dim_imd0

actW, dW = hom_module(rhoM,2,rhoN,2)
print("\n[Method 2] W = Hom_k(M,N), dim =", dW)
# report action to show W is the regular rep (free rank 1)
h1, kd, imd = H1(actW, dW)
print("  dim Z^1 =", kd, " dim B^1 =", imd, " => dim H^1(V4,W) = dim Ext^1(M,N) =", h1)

actWmm, dWmm = hom_module(rhoM,2,rhoM,2)
h1mm, kdm, imdm = H1(actWmm, dWmm)
print("\n[Method 2] W' = Hom_k(M,M), dim =", dWmm)
print("  dim Z^1 =", kdm, " dim B^1 =", imdm, " => dim H^1(V4,W') = dim Ext^1(M,M) =", h1mm)

# ===================================================================
# METHOD 1: honest minimal projective resolution over kV4, apply Hom(-,N).
# Free module kV4^n : basis (group elt g, copy i). Left regular action.
# ===================================================================
def free_action(n):
    """action matrices on kV4^n, dim 4n, basis idx = gi*n + i, g acts (h,i)->(gh,i)."""
    d = 4*n
    act = {}
    for x in ELTS:
        M=[[0]*d for _ in range(d)]
        for gi,g in enumerate(ELTS):
            for i in range(n):
                src = gi*n+i
                tg = mul(x,g)
                dst = ELTS.index(tg)*n+i
                M[dst][src]=1
        act[x]=M
    return act,d

def apply_mat(M,vec_bits,d):
    out=0
    for i in range(d):
        s=0
        for j in range(d):
            if (vec_bits>>j)&1: s^=M[i][j]
        if s: out|=(1<<i)
    return out

def radX(act,d):
    """rad*X = span of columns of (rho(g)-I) over all g."""
    cols=[]
    for g in ELTS:
        M=act[g]
        for j in range(d):
            col=0
            for i in range(d):
                v=M[i][j]^(1 if i==j else 0)
                if v: col|=(1<<i)
            if col: cols.append(col)
    R,_=rref(cols,d)
    return R  # rows are basis of radX as subspace (bitmask over coords)

def proj_cover(act,d):
    """Return (n, phi_cols) : n = # generators; phi: kV4^n -> X given by
       columns (image of each free basis elt (g,i)) as length-d bitmask lists.
       Also returns generator lift vectors."""
    R=radX(act,d)                     # basis of radX
    dim_rad=len(R)
    # top dimension = d - dim_rad ; choose gens = std basis vectors completing R
    # find coords not spanned: extend R to full space
    Rrows=list(R); n=0; gens=[]
    piv=set()
    Rr,pcols=rref(R,d)
    pivset=set(pcols)
    for c in range(d):
        if c in pivset: continue
        # e_c is a new generator (independent mod radX)
        vec=1<<c
        gens.append(vec)
        # add to spanning set
        Rr,pcols=rref(Rr+[vec],d)
        pivset=set(pcols)
    n=len(gens)
    # phi: free^n -> X. generator i (elt e) -> gens[i]; (g,i)->rho_X(g) gens[i]
    cols=[]
    for gi,g in enumerate(ELTS):
        for i in range(n):
            cols.append(apply_mat(act[g],gens[i],d))
    return n,cols,gens

def kernel_submodule(cols, d_target, d_free):
    """cols: list of d_free bitmasks (over d_target coords) = matrix phi (d_target x d_free).
       Return basis (list of bitmasks over d_free) of ker phi."""
    # build rows over variables = free coords (d_free vars). Each target coord = equation.
    eqs=[0]*d_target
    for j,col in enumerate(cols):
        for i in range(d_target):
            if (col>>i)&1:
                eqs[i]^=(1<<j)
    ker=nullspace([e for e in eqs if e], d_free)
    return ker

def restrict_action(free_act, d_free, ker_basis):
    """Action of V4 on submodule spanned by ker_basis (K columns).
       Return action matrices in the ker basis (dim K)."""
    K=len(ker_basis)
    # matrix B whose columns are ker basis vectors (d_free x K)
    # to express rho(g)*v in terms of basis, solve B x = rho(g) v.
    # Precompute rref of [B | ...] style: build solver.
    # Represent B as rows? We'll solve via augmented approach per g.
    # Build B as list of column bitmasks:
    Bcols=ker_basis
    # For solving, need to write target vector as combo of Bcols. Set up matrix with columns Bcols; use gaussian elim on rows.
    # Represent as rows over d_free with K unknowns: for each coordinate r: sum_c Bcols[c][r] x_c = target[r]
    def solve(target):
        # augmented system: rows d_free eqs, K unknowns
        rows=[]
        for r in range(d_free):
            row=0
            for c in range(K):
                if (Bcols[c]>>r)&1:
                    row|=(1<<c)
            # augment with target bit at position K
            if (target>>r)&1:
                row|=(1<<K)
            rows.append(row)
        Rr,pcols=rref(rows,K+1)
        # extract solution: assume consistent, pivots in first K cols
        x=0
        for row in Rr:
            lead=(row & -row).bit_length()-1
            if lead==K:  # inconsistent
                return None
            if lead<K:
                # value = bit K present?
                if (row>>K)&1:
                    x|=(1<<lead)
        return x
    act={}
    for g in ELTS:
        M=[[0]*K for _ in range(K)]
        for c in range(K):
            v=ker_basis[c]
            gv=apply_mat(free_act[g],v,d_free)
            x=solve(gv)
            assert x is not None,"submodule not invariant?"
            for i in range(K):
                if (x>>i)&1: M[i][c]=1
        act[g]=M
    return act,K

def module_from_rho(rho,dim):
    return {g:rho[g] for g in ELTS}, dim

# Build M as a module (act, dim)
actM,dM = module_from_rho(rhoM,2)

# P0 = proj cover of M
n0,phi0_cols,gens0 = proj_cover(actM,dM)
print("\n[Method 1] projective resolution of M:")
print("  P0 = kV4^%d (rank %d)"%(n0,n0))
free0,df0 = free_action(n0)
ker0 = kernel_submodule(phi0_cols, dM, df0)   # Omega M inside P0
print("  Omega^1 M = ker(P0->M) dim =", len(ker0), "(expect", df0-dM,")")
actO1,dO1 = restrict_action(free0,df0,ker0)

# P1 = proj cover of Omega^1 M
n1,phi1_cols,gens1 = proj_cover(actO1,dO1)
print("  P1 = kV4^%d (rank %d)"%(n1,n1))
free1,df1 = free_action(n1)
ker1 = kernel_submodule(phi1_cols, dO1, df1)
print("  Omega^2 M dim =", len(ker1))
actO2,dO2 = restrict_action(free1,df1,ker1)

# P2 = proj cover of Omega^2 M
n2,phi2_cols,gens2 = proj_cover(actO2,dO2)
print("  P2 = kV4^%d (rank %d)"%(n2,n2))

# Need actual maps d1: P1->P0 and d2: P2->P1 as kV4-module maps (matrices over coords).
# d1 = incl(Omega^1 -> P0) o phi1(P1 -> Omega^1).
#   phi1_cols give images of P1-generators in Omega^1 coords (basis ker0).
#   incl: Omega^1 coord vector (over ker0 basis) -> P0 vector = sum coord * ker0[j].
def incl_map(ker_basis, d_free):
    """returns function: bitmask over |ker| -> bitmask over d_free"""
    def f(x):
        out=0
        for j in range(len(ker_basis)):
            if (x>>j)&1:
                out^=ker_basis[j]
        return out
    return f
incl0 = incl_map(ker0, df0)   # Omega^1 -> P0
incl1 = incl_map(ker1, df1)   # Omega^2 -> P1

# d1: P1 -> P0 : generator column i of P1 -> phi1_cols[i] (in Omega^1 basis) -> incl0 -> P0
# But we want d1 on ALL of P1 as a module map; determined by generators (columns where g=e).
# The free basis of P1 is (g,i); a module map to P0 is determined by images of generators (e,i),
# and image of (g,i) = rho_P0(g)*image(e,i).
def dmap_on_generators(phi_cols, n_src, incl, target_free_act, d_target):
    """phi_cols: images of ALL free basis elts of source in submodule-coord (len 4*n_src).
       We only need generator images (g=e,i) => indices i in 0..n_src-1 (since basis idx=gi*n+i, e=gi0).
       Return list over source-generators of target vector (bitmask over d_target)."""
    gen_imgs=[]
    for i in range(n_src):
        sub_vec = phi_cols[i]      # (e,i) -> image in submodule coords
        gen_imgs.append(incl(sub_vec))
    return gen_imgs

d1_gen = dmap_on_generators(phi1_cols, n1, incl0, free0, df0)  # P1 gens -> P0
d2_gen = dmap_on_generators(phi2_cols, n2, incl1, free1, df1)  # P2 gens -> P1

# Now express d1(gen_i) in P0 = kV4^{n0}: it's a bitmask over df0 = 4*n0 coords.
# coord index = gi*n0 + copy. So d1(gen_i) = sum_{g,j} c[g,j] (g,j).
# Apply Hom(-,N): a hom P0->N <-> tuple (w_1..w_{n0}) in N^{n0} (images of gens).
#   value on (g,j) = rho_N(g) w_j.  So f(d1(gen_i)) = sum c[g,j] rho_N(g) w_j.
# Build d1* : N^{n0} -> N^{n1}  (variables: n0*dimN, outputs n1*dimN).
dN=2
def dstar(dgen, n_src, n_dst):
    """d*: Hom(P_dst,N)=N^{n_dst} -> Hom(P_src,N)=N^{n_src}?
       Careful: d: P_src->P_dst (source has generators, maps into P_dst=kV4^{n_dst}).
       Precompose: f in Hom(P_dst,N) -> f o d in Hom(P_src,N).
       Input vars: n_dst * dN (w for P_dst gens). Output coords: n_src * dN.
       For source generator i: d(gen_i) in P_dst coords = bitmask over 4*n_dst.
         f(d(gen_i)) = sum over (g,j) coeff * rho_N(g) w_j.
    """
    nin = n_dst*dN
    nout = n_src*dN
    eqs=[0]*nout   # each output coord = linear combo of input vars
    for i in range(n_src):
        col = dgen[i]   # bitmask over 4*n_dst coords
        for coord in range(4*n_dst):
            if (col>>coord)&1:
                g_idx = coord // n_dst
                j = coord % n_dst
                g = ELTS[g_idx]
                RN = rhoN[g]
                # rho_N(g) w_j contributes to output block i:
                # out[i*dN + r] += sum_s RN[r][s] * inputvar(j*dN + s)
                for r in range(dN):
                    for s in range(dN):
                        if RN[r][s]:
                            eqs[i*dN + r] ^= (1 << (j*dN + s))
    return eqs, nin, nout

# complex: Hom(P0,N) --d1*--> Hom(P1,N) --d2*--> Hom(P2,N)
d1s_eqs, in1, out1 = dstar(d1_gen, n1, n0)   # maps N^{n0} -> N^{n1}
d2s_eqs, in2, out2 = dstar(d2_gen, n2, n1)   # maps N^{n1} -> N^{n2}

# im(d1*) subspace of N^{n1}: columns = images of basis of N^{n0}
# build image vectors:
def map_matrix_apply_all(eqs, nin, nout):
    """eqs[outcoord] = bitmask over nin vars. Return list of image bitmasks for each input basis e_k."""
    imgs=[]
    for k in range(nin):
        v=0
        for oc in range(nout):
            if (eqs[oc]>>k)&1:
                v|=(1<<oc)
        imgs.append(v)
    return imgs

im_d1s = map_matrix_apply_all(d1s_eqs, in1, out1)   # in N^{n1} (dim out1)
dim_im_d1s = rank(im_d1s, out1)
# ker(d2*) : nullspace of d2s_eqs over in2 vars (in2 == out1 == n1*dN)
ker_d2s = nullspace([e for e in d2s_eqs if e], in2)
dim_ker_d2s = len(ker_d2s)
dim_ext1 = dim_ker_d2s - dim_im_d1s
print("  Hom(P0,N)=N^%d dim %d ; Hom(P1,N)=N^%d dim %d ; Hom(P2,N)=N^%d dim %d"
      %(n0,n0*dN,n1,n1*dN,n2,n2*dN))
print("  dim ker(d2*) =", dim_ker_d2s, " dim im(d1*) =", dim_im_d1s)
print("  => dim Ext^1_kV4(M,N) [projective resolution] =", dim_ext1)

# --- also Ext^1(M,M) by same resolution, Hom(-,M) ---
def dstar_target(dgen, n_src, n_dst, rhoT, dT):
    nin=n_dst*dT; nout=n_src*dT
    eqs=[0]*nout
    for i in range(n_src):
        col=dgen[i]
        for coord in range(4*n_dst):
            if (col>>coord)&1:
                g=ELTS[coord//n_dst]; j=coord%n_dst
                RT=rhoT[g]
                for r in range(dT):
                    for s in range(dT):
                        if RT[r][s]:
                            eqs[i*dT+r]^=(1<<(j*dT+s))
    return eqs,nin,nout
e1,_,o1=dstar_target(d1_gen,n1,n0,rhoM,2)
e2,i2,o2=dstar_target(d2_gen,n2,n1,rhoM,2)
im1=map_matrix_apply_all(e1,n0*2,o1); dim_im1=rank(im1,o1)
ker2=nullspace([e for e in e2 if e],i2); dim_ker2=len(ker2)
print("  => dim Ext^1_kV4(M,M) [projective resolution] =", dim_ker2-dim_im1)

print("\n===== FINAL =====")
print("dim Hom_kV4(M,N)   =", dimHomMN)
print("dim Ext^1_kV4(M,N) =", h1, "(cochain)  /", dim_ext1, "(proj res)")
print("dim Ext^1_kV4(M,M) =", h1mm, "(cochain)  /", dim_ker2-dim_im1, "(proj res)")
