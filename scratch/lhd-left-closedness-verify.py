"""
Verify T4-left: ◁-left-closedness on Fam(Vec_fd^op) via the collapse ◁=⊗.

(a) COLLAPSE. Over Vec_fd, the substitution endofunctor composition ⟦p⟧∘⟦q⟧ equals the
    Dirichlet ⟦p⊗q⟧.  We check this at the level of DIMENSIONS of the composite functor
    evaluated on test spaces, computed two ways:
      - "compose":  dim ∐_s [P_s, ∐_t [Q_t, X]]  with the LINEAR internal hom (no branching)
      - "tensor" :  dim ∐_{s,t}[P_s⊗Q_t, X]
    Over Set the analogue would branch (T^Z); we also print the Set shape-count to contrast.

(b) CLOSURE ADJUNCTION.  Cardinality identity over F_2:
      |Fam((A,X)◁q,(R,M))| =?= |Fam((A,X), [q◁−](R,M))|
    with (A,X)◁q = (A×T,(X_a⊗Q_t))   [the collapse]
    and  [q◁−](R,M) = (R^T,(N_ρ)),  N_ρ = ⊕_t M_{ρ(t)}⊗Q_{t}^*,  dim N_ρ = Σ_t m_{ρt} q_t.
    Uses |Vec_{F2}(V,W)| = 2^{dim V · dim W}.
"""
import itertools, random

# ---------- (a) collapse: dim of composite via linear hom vs tensor ----------
# Over Vec_fd, [V,W] has dim (dim V)*(dim W); ∐ = ⊕ adds dims; internal hom preserves ⊕.
def dim_compose(P, Q, xdim):
    # ∐_s [P_s, ∐_t [Q_t, X]] ; inner ∐_t[Q_t,X] has dim sum_t q_t*xdim (hom preserves ⊕)
    inner = sum(q * xdim for q in Q)
    return sum(p * inner for p in P)          # sum_s p_s * (sum_t q_t * x)

def dim_tensor(P, Q, xdim):
    # ∐_{s,t}[P_s⊗Q_t, X] : dim sum_{s,t} (p_s*q_t)*x
    return sum((p * q) * xdim for p in P for q in Q)

print("=== (a) collapse ◁=⊗ over Vec_fd: composite-functor dim, compose vs tensor ===")
ok = True
random.seed(0)
for _ in range(20000):
    P = [random.randint(1,4) for _ in range(random.randint(1,3))]
    Q = [random.randint(1,4) for _ in range(random.randint(1,3))]
    x = random.randint(1,4)
    if dim_compose(P,Q,x) != dim_tensor(P,Q,x):
        ok = False; print("MISMATCH", P, Q, x); break
print("compose==tensor on 20000 random cases:", ok)
# contrast: Set shape count of p◁q = sum_s |T|^{|P_s|}  vs Vec shape count |S|*|T|
P,Q = [2,1], [1,1,1]   # |S|=2,|T|=3
set_shapes = sum(len(Q)**p for p in P)      # T^{P_s}
vec_shapes = len(P)*len(Q)
print(f"contrast |S|=2,|T|=3: Set shapes(◁)={set_shapes}  Vec shapes(◁=⊗)={vec_shapes}")

# ---------- (b) closure adjunction cardinality identity over F_2 ----------
def card_fam(src, tgt):
    # src=(A, X list of dims), tgt=(B, Y list of dims); |∏_a ∐_b Vec(Y_b,X_a)|
    A, X = src; B, Y = tgt
    tot = 1
    for xa in X:
        tot *= sum(2**(yb*xa) for yb in Y)
    return tot

def lhs(Xdims, Qdims, Mdims):
    # |Fam((A,X)◁q,(R,M))| with (A,X)◁q=(A×T,(X_a⊗Q_t)); positions dims x_a*q_t
    A = [xa*qt for xa in Xdims for qt in Qdims]     # dim list of (X_a⊗Q_t)
    return card_fam((len(A), A), (len(Mdims), Mdims))

def rhs(Xdims, Qdims, Mdims):
    # [q◁−](R,M)=(R^T,(N_ρ)), N_ρ dim = sum_t m_{ρt} q_t ; R indexes Mdims
    T = len(Qdims); R = range(len(Mdims))
    Ndims = [sum(Mdims[rho[t]]*Qdims[t] for t in range(T)) for rho in itertools.product(R, repeat=T)]
    return card_fam((len(Xdims), Xdims), (len(Ndims), Ndims))

print("\n=== (b) ◁-closure adjunction cardinality identity over F_2 ===")
ok = True; n = 0
random.seed(1)
for _ in range(3000):
    Xdims = [random.randint(1,3) for _ in range(random.randint(1,3))]  # source positions (=A shapes' dims)
    Qdims = [random.randint(1,3) for _ in range(random.randint(1,3))]  # q positions
    Mdims = [random.randint(1,3) for _ in range(random.randint(1,3))]  # target M positions
    L, Rr = lhs(Xdims,Qdims,Mdims), rhs(Xdims,Qdims,Mdims)
    n += 1
    if L != Rr:
        ok = False; print("MISMATCH", Xdims, Qdims, Mdims, L, Rr); break
print(f"LHS==RHS on {n} random small families:", ok)

# boundary cases
print("\n=== boundary checks ===")
# q = monomial (single shape): closure should exist even shape-count-wise; check identity
print("q monomial (T=1):", lhs([2],[3],[1,2])==rhs([2],[3],[1,2]))
# unit q = I = ({*},k): p◁I = p ; hom [I◁−](R,M) should be (R,M) itself
print("q=I=(1,[1]):", lhs([1,2],[1],[2,1])==rhs([1,2],[1],[2,1]))
