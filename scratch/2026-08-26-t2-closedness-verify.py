import itertools, random

random.seed(20260826)

def task1(trials=2000):
    passes = 0
    fails = []
    for _ in range(trials):
        q = random.choice([2, 3, 4])
        nS = random.randint(1, 3); nT = random.randint(1, 3); nR = random.randint(1, 3)
        p = [random.randint(1, 3) for _ in range(nS)]
        qd = [random.randint(1, 3) for _ in range(nT)]
        m = [random.randint(1, 3) for _ in range(nR)]

        # LHS: Fam( (S,P)⊗(T,Q) , (R,M) )
        # = ∏_{(s,t)} Σ_r q^{ m_r p_s q_t }
        lhs = 1
        for ps in p:
            for qt in qd:
                lhs *= sum(q ** (mr * ps * qt) for mr in m)

        # RHS: Fam( (S,P) , [(T,Q)⇒(R,M)] )
        # U = R^T (all ρ:T→R); dim N_ρ = Σ_t m_{ρ(t)} q_t
        # = ∏_s Σ_{ρ} q^{ (Σ_t m_{ρ(t)} q_t) * p_s }
        rho_dims = []
        for rho in itertools.product(range(nR), repeat=nT):
            d = sum(m[rho[t]] * qd[t] for t in range(nT))
            rho_dims.append(d)
        rhs = 1
        for ps in p:
            rhs *= sum(q ** (d * ps) for d in rho_dims)

        if lhs == rhs:
            passes += 1
        else:
            fails.append((q, p, qd, m, lhs, rhs))
    return passes, trials, fails


def task2(trials=2000):
    passes = 0
    fails = []
    for _ in range(trials):
        nS = random.randint(1, 3); nT = random.randint(1, 3); nR = random.randint(1, 3)
        p = [random.randint(1, 3) for _ in range(nS)]      # |P_s|
        qd = [random.randint(1, 3) for _ in range(nT)]     # |Q_t|
        m = [random.randint(1, 3) for _ in range(nR)]      # |M_r|

        # LHS: Fam( (S,P)⊗(T,Q) , (R,M) ) over Set
        # |Fam((A,X),(B,Y))| = ∏_a Σ_b |X_a|^{|Y_b|}
        # here A = S×T, X_(s,t)=P_s×Q_t (size p_s*q_t); B=R, Y_r=M_r (size m_r)
        lhs = 1
        for ps in p:
            for qt in qd:
                base = ps * qt
                lhs *= sum(base ** mr for mr in m)

        # RHS: Fam( (S,P) , [(T,Q)⇒(R,M)] )
        # U' = ⊔_{ρ:T→R} ∏_t (Q_t)^{M_{ρ(t)}}  -> component (ρ,choice), |N'| = Σ_t |M_{ρ(t)}|
        # For each a=s: Σ_{component b} |P_s|^{|N'_b|}
        # group by ρ: number of choices for ρ = ∏_t q_t^{m_{ρ(t)}}, each with |N'|=Σ_t m_{ρ(t)}
        # so Σ_b |P_s|^{|N'_b|} = Σ_ρ ( ∏_t q_t^{m_{ρ(t)}} ) * p_s^{ Σ_t m_{ρ(t)} }
        comp = []  # list of (multiplicity, Nprime_size)
        for rho in itertools.product(range(nR), repeat=nT):
            mult = 1
            Nsize = 0
            for t in range(nT):
                mult *= qd[t] ** m[rho[t]]
                Nsize += m[rho[t]]
            comp.append((mult, Nsize))
        rhs = 1
        for ps in p:
            rhs *= sum(mult * (ps ** Nsize) for (mult, Nsize) in comp)

        if lhs == rhs:
            passes += 1
        else:
            fails.append((p, qd, m, lhs, rhs))
    return passes, trials, fails


def task3():
    print("=== TASK 3 ===")
    print("Internal-hom position dimension for T={1..n}, q_t=1, R={*}, m_*=1: dim N = n")
    for n in [1, 2, 5, 20]:
        print(f"  n={n}: dim N = {n}")
    print("  -> as n->infinity dim N -> infinity; for T infinite the representing object leaves Vec_fd.")
    print("Corepresentability check: |F_q^d|^n == q^{n*d} ?")
    ok = True
    for q in [2, 3, 4]:
        for d in range(1, 4):
            for n in range(1, 5):
                lhs = (q ** d) ** n
                rhs = q ** (n * d)
                if lhs != rhs:
                    ok = False
                    print(f"  FAIL q={q} d={d} n={n}: {lhs} != {rhs}")
    print(f"  all |F_q^d|^n == q^(n*d) checks pass: {ok}")


if __name__ == "__main__":
    p1, n1, f1 = task1()
    print("=== TASK 1 (Vec_fd) ===")
    print(f"  passed {p1}/{n1}")
    for fc in f1[:5]:
        print("  FAIL:", fc)

    p2, n2, f2 = task2()
    print("=== TASK 2 (Set) ===")
    print(f"  passed {p2}/{n2}")
    for fc in f2[:5]:
        print("  FAIL:", fc)

    task3()
