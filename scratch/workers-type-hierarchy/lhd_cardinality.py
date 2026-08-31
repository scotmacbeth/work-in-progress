"""
◁ non-closedness via the DECISIVE invariant: cardinality sequence of the
candidate internal-hom functor
   T_R(A) = ∏_{γ:A→S_p} ⟦R⟧( Σ_{i∈A} P_p(γ i) ).
If Workers were ◁-closed, T_R would be a polynomial functor (a container H).
A polynomial functor F has |F(1)| = #shapes and |F(n)| = Σ_shapes n^{|pos|}.
We show t_n := |T_R([n])| grows DOUBLE-exponentially (∝ c^{2^n}), impossible
for any container: t_1 finite forces finitely many (indeed 1) shape, but then
t_n = n^k, contradicted by t_3.
No enumeration needed — just the product formula for cardinalities.
"""
def ext_card(R_shapes_pos, m):
    # |⟦R⟧(m)| = Σ_shapes m^{|pos|}
    return sum(m**k for k in R_shapes_pos)

def T_card_seq(Sp_size, p_fibsizes, R_shapes_pos, nmax=4):
    # p: shapes with position-set sizes p_fibsizes (list). γ:A->S_p, |A|=n.
    # For a fixed γ, Σ_{i∈A}P_p(γi) has size = Σ_i |P_p(γ i)|.
    # Product over all γ in (S_p)^A of |⟦R⟧(that size)|.
    from itertools import product
    seq=[]
    for n in range(nmax+1):
        A=list(range(n))
        tot=1
        for g in product(range(Sp_size), repeat=n):
            size = sum(p_fibsizes[g[i]] for i in range(n))
            tot *= ext_card(R_shapes_pos, size)
        seq.append(tot)
    return seq

def is_container_sequence(seq):
    # necessary check: t_1 = #shapes N (finite). If N finite, t_n = Σ_{N terms} n^{k}.
    # We test the strongest simple contradiction: assume 1 shape (t_1=1) => t_n=n^k.
    t1=seq[1]
    msg=[]
    if t1==0:
        msg.append("t_1=0")
    elif t1==1:
        # single shape of arity k: t_2=2^k
        import math
        if seq[2]>0:
            k=math.log2(seq[2]) if seq[2]>0 else None
            pred3 = round(3**k) if k is not None and abs(k-round(k))<1e-9 else None
            msg.append(f"t_1=1 ⟹ 1 shape, arity k with 2^k={seq[2]} ⟹ k={k}; predict t_3=3^k={pred3}, actual={seq[3]}")
    else:
        msg.append(f"t_1={t1} ⟹ {t1} shapes; a finite Σ n^k is ≤ {t1}·n^kmax (poly growth)")
    return "; ".join(msg)

if __name__=='__main__':
    print("p = 2 shapes, 1 position each (S_p={0,1}, |P_p|=1,1)")
    print()
    # R = Id (y):  shapes with pos-sizes [1]
    seq_id = T_card_seq(2, [1,1], [1], nmax=4)
    print(f"R = Id:            t_n (n=0..4) = {seq_id}")
    print(f"   contradiction:  {is_container_sequence(seq_id)}")
    print(f"   note t_n should be n^(2^n): {[ (n**(2**n)) for n in range(5)]}")
    print()
    # R = [ΔS,q], |S|=2, q=Id => ⟦R⟧(m)=⟦q⟧(2m)^2=(2m)^2=4m^2 : as container = shapes pos-sizes?
    # 4m^2 = Σ 4 copies of m^2 => shapes pos-sizes [2,2,2,2]
    seq_R = T_card_seq(2, [1,1], [2,2,2,2], nmax=3)
    print(f"R = [ΔS,q], q=Id, |S|=2  (⟦R⟧(m)=4m^2):  t_n (n=0..3) = {seq_R}")
    print(f"   contradiction:  {is_container_sequence(seq_R)}")
    print()
    # sanity: p = 1 shape (◁ with single-shape p) should be POLYNOMIAL (T_R(A)=⟦R⟧(|P_p|·A))
    print("SANITY p = 1 shape, 2 positions (S_p={0}, |P_p|=2): T_R(A)=⟦R⟧(2A) should be polynomial")
    seq_1 = T_card_seq(1, [2], [1], nmax=4)   # R=Id => T(A)=⟦Id⟧(2A)=2A => container 2y, t_n=2n
    print(f"   R=Id: t_n = {seq_1}   (=2n, container 2·y — POLYNOMIAL ✓)")
