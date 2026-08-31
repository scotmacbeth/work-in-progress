"""
Secondary claim: x-monoids (categorical product tensor) in Cont.
Characterization to test:
  x-monoid on c = Sigma_s y^{P_s}  <=>
     ( monoid (S,.,e) with P_e = EMPTY )
   + ( oplax monoidal functor P:(S,.,e) -> (Set, sqcup, empty) on fibres )
oplax-into-(Set,sqcup) data: psi_{s,t}: P_{s.t} -> P_s (+) P_t   (backward routing)
  and counit P_e -> empty (forces P_e empty), subject to assoc + unit coherence.
Compare count with table.count_monoids(Prod, .).
"""
import itertools
from table import cont, count_monoids, Prod

# encode P_s (+) P_t as ('l',p) / ('r',q)

def count_via_char(P_cards):
    S = list(range(len(P_cards)))
    P = {i: list(range(P_cards[i])) for i in S}
    total = 0
    for flat in itertools.product(S, repeat=len(S)*len(S)):
        m = {(i, j): flat[i*len(S)+j] for i in S for j in S}
        if not all(m[(m[(i,j)],k)] == m[(i,m[(j,k)])] for i in S for j in S for k in S):
            continue
        units = [e for e in S if all(m[(e,x)]==x and m[(x,e)]==x for x in S)]
        if not units:
            continue
        e = units[0]
        # UNIT-FIBRE CONSTRAINT: P_e must be empty (eta:1->c backward P_e->empty)
        if len(P[e]) != 0:
            continue
        pairs = [(s, t) for s in S for t in S]
        opt_lists = []
        for (s, t) in pairs:
            dom = P[m[(s, t)]]
            cod = [('l', p) for p in P[s]] + [('r', q) for q in P[t]]
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
            psi = {pairs[i]: combo[i] for i in range(len(pairs))}
            ok = True
            # unit coherence: since P_e empty, psi_{e,s}:P_s->P_e(+)P_s must land in
            # right-summand identically; psi_{s,e}:P_s->P_s(+)P_e in left identically.
            for s in S:
                for x in P[s]:
                    if psi[(e, s)][x] != ('r', x):
                        ok = False; break
                    if psi[(s, e)][x] != ('l', x):
                        ok = False; break
                if not ok: break
            if not ok:
                continue
            # associativity coherence:
            # (id (+) psi_{t,u}) o psi_{s,t.u} == (psi_{s,t} (+) id) o psi_{s.t,u}
            # both : P_{s.t.u} -> P_s (+) P_t (+) P_u.  Encode result in {s,t,u}xpos.
            def left_map(s,t,u,x):
                r = psi[(s, m[(t,u)])][x]      # in P_s (+) P_{t.u}
                if r[0]=='l': return ('s', r[1])
                r2 = psi[(t,u)][r[1]]           # in P_t (+) P_u
                if r2[0]=='l': return ('t', r2[1])
                return ('u', r2[1])
            def right_map(s,t,u,x):
                r = psi[(m[(s,t)], u)][x]       # in P_{s.t} (+) P_u
                if r[0]=='r': return ('u', r[1])
                r2 = psi[(s,t)][r[1]]           # in P_s (+) P_t
                if r2[0]=='l': return ('s', r2[1])
                return ('t', r2[1])
            for s in S:
                for t in S:
                    for u in S:
                        for x in P[m[(s, m[(t,u)])]]:
                            if left_map(s,t,u,x) != right_map(s,t,u,x):
                                ok = False; break
                        if not ok: break
                    if not ok: break
                if not ok: break
            if ok:
                total += 1
    return total

if __name__ == '__main__':
    print("=== x-monoid characterization cross-check ===")
    for cards in ([0], [1], [2], [0,0], [1,1], [0,1], [1,0], [0,0,0]):
        via_char = count_via_char(cards)
        res, _, _ = count_monoids(Prod, cont(cards))
        via_dir = len(res)
        flag = "OK" if via_char == via_dir else "MISMATCH!!"
        print(f"P_cards={cards}: char-count={via_char}  Prod-monoid-count={via_dir}  {flag}")
