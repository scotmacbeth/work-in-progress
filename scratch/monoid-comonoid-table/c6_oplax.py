"""
Independent check of the C6 characterization:
  (x)-monoid on c = Sigma_s y^{P_s}  <=>
     ( monoid (S,.,e) )  +  ( oplax monoidal functor P:(S,.,e)->(Set,x) )
oplax data: phi_{s,t}: P_{s.t} -> P_s x P_t  and  eps: P_e -> 1 (forced),
  subject to associativity + unit coherence.
We enumerate this data-from-scratch and compare the count with table.count_monoids(Dir,.).
"""
import itertools
from table import cont, count_monoids, Dir

def count_via_oplax(P_cards):
    S = list(range(len(P_cards)))
    P = {i: list(range(P_cards[i])) for i in S}
    total = 0
    # enumerate monoid structures (m: SxS->S, e) on S
    for flat in itertools.product(S, repeat=len(S)*len(S)):
        m = {(i, j): flat[i*len(S)+j] for i in S for j in S}
        if not all(m[(m[(i,j)],k)] == m[(i,m[(j,k)])] for i in S for j in S for k in S):
            continue
        units = [e for e in S if all(m[(e,x)]==x and m[(x,e)]==x for x in S)]
        if not units:
            continue
        e = units[0]
        # enumerate phi_{s,t}: P_{m(s,t)} -> P_s x P_t
        pairs = [(s, t) for s in S for t in S]
        opt_lists = []
        for (s, t) in pairs:
            dom = P[m[(s, t)]]
            cod = [(p, q) for p in P[s] for q in P[t]]
            if len(dom) == 0:
                opt_lists.append([{}])
            elif len(cod) == 0:
                opt_lists.append([])
            else:
                fs = [dict(zip(dom, vals)) for vals in itertools.product(cod, repeat=len(dom))]
                opt_lists.append(fs)
        if any(len(o) == 0 for o in opt_lists):
            continue
        for combo in itertools.product(*opt_lists):
            phi = {pairs[i]: combo[i] for i in range(len(pairs))}
            # unit coherence: phi_{e,s}: P_s -> P_e x P_s, then drop P_e component = id
            ok = True
            for s in S:
                for x in P[s]:
                    a, b = phi[(e, s)][x]      # in P_e x P_s
                    if b != x:
                        ok = False; break
                    a2, b2 = phi[(s, e)][x]    # in P_s x P_e
                    if a2 != x:
                        ok = False; break
                if not ok:
                    break
            if not ok:
                continue
            # associativity coherence:
            # (id x phi_{t,u}) o phi_{s, t.u}  ==  (phi_{s,t} x id) o phi_{s.t, u}
            #  both : P_{s.t.u} -> P_s x P_t x P_u
            for s in S:
                for t in S:
                    for u in S:
                        dom = P[m[(s, m[(t,u)])]]  # = P_{s.t.u}
                        for x in dom:
                            p_s, p_tu = phi[(s, m[(t,u)])][x]     # P_s x P_{t.u}
                            p_t, p_u = phi[(t, u)][p_tu]          # P_t x P_u
                            left = (p_s, p_t, p_u)
                            p_st, p_u2 = phi[(m[(s,t)], u)][x]    # P_{s.t} x P_u
                            p_s2, p_t2 = phi[(s, t)][p_st]        # P_s x P_t
                            right = (p_s2, p_t2, p_u2)
                            if left != right:
                                ok = False; break
                        if not ok: break
                    if not ok: break
                if not ok: break
            if ok:
                total += 1
    return total

for cards in ([1], [2], [3], [1, 1], [2, 1], [1, 1, 1]):
    via_oplax = count_via_oplax(cards)
    res, _, _ = count_monoids(Dir, cont(cards))
    via_dir = len(res)
    flag = "OK" if via_oplax == via_dir else "MISMATCH!!"
    print(f"P_cards={cards}: oplax-count={via_oplax}  Dir-monoid-count={via_dir}  {flag}")
