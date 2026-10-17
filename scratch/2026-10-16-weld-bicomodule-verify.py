"""
Verify B = ΔS◁ΔT is the regular (ΔT,ΔS)-bicomodule (SGF Def 4.2 axioms 34/35/36),
using functor-composite (nat-transf) semantics on nested tuples.

Store comonad ΔS on ground W:  element (s, phi), phi:S->W (tuple len n).
  comult  δ_S : ΔS(W) -> ΔS(ΔS(W)) ,  (s,phi) |-> (s, (i |-> (i,phi)))
  counit  ε_S : ΔS(W) -> W ,          (s,phi) |-> phi[s]
  functor ΔS(u) : ΔS(W)->ΔS(W') ,     (s,phi) |-> (s, (u(phi[0]),...,u(phi[n-1])))
Comonad laws ε·δ=id, ΔS(ε)·δ=id, coassoc all hold (checked below en route).

Regular bicomodule on carrier B = ΔS◁ΔT (d=ΔS head, c=ΔT tail):
  λ = δ_{ΔS} ⋆ 1_{ΔT} : B ⇒ ΔS◁ΔS◁ΔT   (left d=ΔS coaction)   λ_X = (δ_S)_{ΔT(X)}
  ρ = 1_{ΔS} ⋆ δ_{ΔT} : B ⇒ ΔS◁ΔT◁ΔT   (right c=ΔT coaction)  ρ_X = ΔS((δ_T)_X)
"""
from itertools import product

def store_ops(n):
    def delta(elt):
        s, phi = elt
        return (s, tuple((i, phi) for i in range(n)))
    def eps(elt):
        s, phi = elt
        return phi[s]
    def fmap(u, elt):
        s, phi = elt
        return (s, tuple(u(x) for x in phi))
    return delta, eps, fmap

def DT_elems(m, X):
    return [(t, psi) for t in range(m) for psi in product(X, repeat=m)]

def run(n, m, ks=(2, 3)):
    print(f"\n==== |S|={n} |T|={m} : carrier B=ΔS◁ΔT, (ΔT,ΔS)-bicomodule ====")
    dS, eS, fS = store_ops(n)
    dT, eT, fT = store_ops(m)

    allok = True
    for k in ks:
        X = tuple(range(k))
        TX = DT_elems(m, X)
        B = [(s, phi) for s in range(n) for phi in product(TX, repeat=n)]
        exp = n * (m * k**m)**n
        assert len(B) == exp, (len(B), exp)

        lam = lambda e: dS(e)                      # (δ_S)_{ΔT(X)}
        rho = lambda e: fS(dT, e)                  # ΔS((δ_T)_X)

        def ident(e): return e
        def dict_of(fn): return {e: fn(e) for e in B}
        I = {e: e for e in B}

        # (34) left counit:  (ε_S ⋆ 1)∘λ = id      ε removes outer (head) ΔS
        c = dict_of(lambda e: eS(lam(e)))
        o1 = (c == I); allok &= o1

        # (35) right counit: (1 ⋆ ε_T)∘ρ = id      ε_T removes innermost ΔT
        c = dict_of(lambda e: fS(lambda u: fT(eT, u), rho(e)))
        o2 = (c == I); allok &= o2

        # (34) left coassoc: (δ_S⋆1)∘λ = (1⋆λ)∘λ
        L = dict_of(lambda e: dS(lam(e)))
        R = dict_of(lambda e: fS(lam, lam(e)))
        o3 = (L == R); allok &= o3

        # (35) right coassoc: (ρ⋆1)∘ρ = (1⋆δ_T)∘ρ  (both whisker ΔT-coassoc under ΔS)
        L = dict_of(lambda e: fS(lambda t: dT(dT(t)), e))
        R = dict_of(lambda e: fS(lambda t: fT(dT, dT(t)), e))
        o4 = (L == R); allok &= o4

        # (36) bicomodule compat: (λ⋆1)∘ρ = (1⋆ρ)∘λ
        L = dict_of(lambda e: dS(rho(e)))
        R = dict_of(lambda e: fS(rho, lam(e)))
        o5 = (L == R); allok &= o5

        print(f"  k={k}: (34)counit={o1} (35)counit={o2} (34)coassoc={o3} "
              f"(35)coassoc={o4} (36)compat={o5}")
    print(f"  ==> ALL BICOMODULE AXIOMS HOLD: {allok}")
    return allok

def represented(n, m, ks=(1, 2, 3)):
    print(f"\n-- represented prafunctor F̄_B(V)=(T×V)^S, |S|={n} |T|={m} --")
    for V in ks:
        Fbar = (m * V)**n
        A_u = (n*m) * V**(n*m)          # underlying poly of worker A=Δ(S×T)
        B_u = (n*m**n) * V**(n*m)       # underlying poly of weld B=ΔS◁ΔT
        print(f"  V={V}: F̄_B=(T·V)^S=({m}·{V})^{n}={Fbar} ;  A_under={A_u} ; B_under={B_u} ;"
              f"  F̄_B≠A_under:{Fbar!=A_u}  F̄_B≠B_under:{Fbar!=B_u}")
    print(f"  content=(-)^S (power, right adj) ; Σ-tail index T^S={m**n} (= branch maps S->T)")

if __name__ == "__main__":
    for n, m in [(2, 2), (2, 3), (3, 2), (1, 2), (2, 1)]:
        run(n, m)
    represented(2, 2); represented(2, 3); represented(3, 2)
