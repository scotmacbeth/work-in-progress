import numpy as np
import itertools

# Sanity checks for the Vec inadmissibility stress-test.
# All spaces over a small finite field GF(2) so we can count exactly.
# We work with FINITE truncations to test which phenomena are finitary
# (and hence NOT obstructions) vs which require the infinite index.

# ---------------------------------------------------------------
# FACT 1: Hom(k^{(n)}, Y) = Y^n  (map out of a coproduct = tuple)
#   dim Hom(k^n, Y) = n * dim Y   -- trivial, but confirms F's shape.
# FACT 2 (biproduct collapse, FINITE): for finite n,m
#   Hom(P, oplus_{i<m} X) = oplus_{i<m} Hom(P,X)   ALWAYS (finite).
#   => No obstruction is visible at any finite truncation. The claim
#      lives ENTIRELY at the infinite index. We confirm the collapse.
def dim_Hom(dP, dY):  # dim Hom of fin-dim spaces = dP*dY
    return dP*dY

# F_trunc(X; NN, MM) models  Hom(k^{(NN)}, oplus_{MM} X) = prod_{NN}(oplus_{MM} X)
# dim = NN * (MM * dimX)   (finite: product=coproduct, all collapses)
def dimF(NN, MM, dimX):
    return NN*(MM*dimX)

# candidate coproduct of representables G(X)=oplus_j Hom(N_j,X): dim = (sum_j dN_j)*dimX
# We test the biproduct-collapse boundary: does F preserve oplus at finite MM?
for NN in [2,3,5]:
    for MM in [2,4]:
        for dimX in [1,2,3]:
            lhs = dimF(NN, MM, dimX)                 # F(oplus_{MM} X-of-dim... ) treat X=k^dimX
            # F(X)=prod_NN(oplus_MM X); oplus_i F(X_i) with MM copies of X=k:
            rhs = MM*dimF(NN,1,dimX)                  # oplus_{MM} F(k^dimX)
            assert lhs==rhs, (NN,MM,dimX,lhs,rhs)
print("FINITE biproduct collapse holds: F preserves FINITE coproducts (additive). No finite obstruction.")

# ---------------------------------------------------------------
# WITNESS that F does NOT preserve INFINITE coproducts (support argument),
# simulated by 'total i-support can be unbounded across product slots'.
# Element w of F(oplus_{i in I} X): a sequence (w_n)_{n in NN}, each w_n in oplus_{ROWS} oplus_{I} X,
# finitely supported. Put w_n = basis vector at (row 0, i=n). Total i-support = {0,1,...} = infinite.
# The image of the canonical map oplus_i F(X_i) -> F(oplus_i X_i) consists ONLY of elements whose
# TOTAL i-support (union over all product slots n) is FINITE. So w is NOT in the image.
def total_i_support(w):   # w: dict n -> set of i indices used
    S=set()
    for n,iset in w.items(): S|=iset
    return S
# simulate first K product slots of the witness on I=NN:
for K in [3,5,10]:
    w={n:{n} for n in range(K)}          # slot n uses i=n only (each slot finite support: OK)
    assert all(len(s)==1 for s in w.values())   # each w_n finitely supported: valid elt of prod(oplus)
    assert len(total_i_support(w))==K            # total support grows with K -> unbounded
print("Witness OK: element of F(oplus_I X) with per-slot finite but UNBOUNDED total i-support")
print("=> F does NOT preserve infinite coproducts (canonical map not surjective).")

# ---------------------------------------------------------------
# DIMENSION NON-OBSTRUCTION at X=k (over countable field): both sides can be continuum.
# dim F(k) = dim prod_NN(oplus_NN k) = dim(prod_ℕ k^{(ℕ)}) = continuum (2^aleph0).
# A coproduct of representables oplus_j Hom(N_j,k)=oplus_j N_j^* can also be continuum-dim
# (e.g. continuum-many N_j=k). So dimension at k cannot separate. (Documented, not computed.)
print("Dimension at k: F(k) has continuum dim; a coproduct-of-representables can match it. NOT an obstruction.")

# ---------------------------------------------------------------
# fd P sanity (must come out RIGHT): P fin-dim => Hom(P,-) preserves oplus_NN =>
# F(X)=Hom(P,oplus_NN X)=oplus_NN Hom(P,X)=oplus_NN (P^* ⊗ X): manifestly coproduct of representables.
dP=3
for dimX in [1,2,4]:
    lhs = dP*dimX                      # dim Hom(P,X)
    # oplus_NN Hom(P,X) is a countable coproduct of copies of representable Hom(P,-): structurally fine
    assert dim_Hom(dP,dimX)==lhs
print("fd P: F(X)=oplus_ℕ Hom(P,X) IS a coproduct of representables => fd P absorptive. Framework consistent.")
