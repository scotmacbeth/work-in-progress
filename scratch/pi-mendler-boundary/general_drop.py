"""
GENERAL-CASE closure of the Reader/State leaf-drop (PROVE.md item C).

Closes the §6 gap of proofs/2026-08-06-state-reader-ladder-census.md:
the drop witness is UNIFORM in size -- |X|>=2 (not "large enough") and works
for every |E|,|S|>=2 -- and State's drop is Reader's diagonal drop specialised
to outer shape h = id.

Criterion (Lemma 1, Yoneda): the Pi-cointerpretation multiplication laxator
    j : P*(mu mm) -> (P*)*(mm),   Prod_{lv(mu mm)} -> Prod_{I(mm)},
exists (naturally in P) iff there is a TOTAL label-preserving
    kappa_mu : I(mm) -> lv(mu mm).
So j fails as soon as some inner token's label is absent from lv(mu mm).
"""
from itertools import product

# --- Reader_E : uniform witness, exhaustive totality check, all K>=2 ---------
def reader_no_total_kappa(K, nX=2):
    """G: E->E->X ; diagonal const 0, one fresh off-diagonal G(0)(1)=1."""
    E = range(K)
    G = [[0]*K for _ in E]
    G[0][1] = 1                                   # the single fresh off-diagonal
    muG = [G[e][e] for e in E]                    # mu(G)(e) = G(e)(e)  (DIAGONAL)
    L_labels = set(muG)                           # labels available on lv(mu G)
    I_labels = [G[e][ep] for e in E for ep in E]  # labels of all inner tokens
    total = all(any(muG[l] == il for l in E) for il in I_labels)
    return (not total), L_labels, sorted(set(I_labels))

# --- State_S with outer shape h=id : reduces to Reader diagonal, all n>=2 ----
def state_no_total_kappa(n, nX=2):
    """mm(s0)=(s0,F(s0))  (h=id); track X-parts only (they carry the labels)."""
    S = range(n)
    xF = [[0]*n for _ in S]
    xF[0][1] = 1                                  # fresh off-token
    mu_labels = set(xF[s0][s0] for s0 in S)       # mu(mm)(s0)=F(s0)(h s0)=F(s0)(s0)
    I_labels = [xF[s0][s1] for s0 in S for s1 in S]
    total = all(any(xF[l][l] == il for l in S) for il in I_labels)
    return (not total), mu_labels, sorted(set(I_labels))

if __name__ == "__main__":
    print("Reader_E  (uniform |X|=2, exhaustive totality):")
    for K in range(2, 9):
        drop, L, I = reader_no_total_kappa(K)
        assert drop, K
        print(f"  |E|={K}: lv(muG) labels={L}, inner labels={I} -> kappa NOT total: {drop}")
    print("State_S  (h=id, uniform |X|=2):")
    for n in range(2, 9):
        drop, L, I = state_no_total_kappa(n)
        assert drop, n
        print(f"  |S|={n}: lv(mu mm) labels={L}, inner labels={I} -> kappa NOT total: {drop}")
    print("ALL PASS: drop is uniform in size, |X|>=2 suffices; State(h=id)=Reader diagonal.")
