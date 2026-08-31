"""
Brute-force check of the Ahman-Uustalu dictionary, with the two sides coded INDEPENDENTLY.

LEFT  (container side): directed containers (S, P, o, down, oplus) with laws D1-D5,
                        diagrammatic order.
RIGHT (category side):  internal categories in Set: arrows A, dom, cod, id, comp,
                        classical order (g after f), classical axioms.

The point of coding them separately (different order convention, different axiom shape)
is that a convention error shows up as a COUNT MISMATCH rather than being hidden by a
shared implementation.

We fix objects S = {0,...,n-1} and an out-degree profile m = (m_0,...,m_{n-1}),
so P s = {0,...,m_s - 1}.  On the category side that is exactly:
|{a in A : dom a = s}| = m_s.  Enumerate all structures on each side; compare counts.
"""
from itertools import product


def directed_containers(m):
    """Enumerate directed containers with S={0..n-1}, |P s| = m[s]. Yield (o, down, oplus)."""
    n = len(m)
    A = [(s, p) for s in range(n) for p in range(m[s])]   # Sigma_s P s
    out = []
    # o : Pi_s P s
    for o in product(*[range(m[s]) for s in range(n)]):
        # down : A -> S
        for downvals in product(range(n), repeat=len(A)):
            down = dict(zip(A, downvals))
            # D1: s down o_s = s
            if any(down[(s, o[s])] != s for s in range(n)):
                continue
            # oplus : for each (s,p) in A, for each p' in P(s down p), gives element of P s
            slots = [((s, p), pp) for (s, p) in A for pp in range(m[down[(s, p)]])]
            for vals in product(*[range(m[s]) for ((s, p), pp) in slots]):
                oplus = dict(zip(slots, vals))

                def op(s, p, pp):
                    return oplus[((s, p), pp)]

                # D2: s down (p + p') = (s down p) down p'
                ok = True
                for (s, p) in A:
                    for pp in range(m[down[(s, p)]]):
                        if down[(s, op(s, p, pp))] != down[(down[(s, p)], pp)]:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                # D3: p + o_{s down p} = p
                if any(op(s, p, o[down[(s, p)]]) != p for (s, p) in A):
                    continue
                # D4: o_s + p = p    (p : P(s down o_s) = P s by D1)
                if any(op(s, o[s], p) != p for (s, p) in A):
                    continue
                # D5: (p + p') + p'' = p + (p' + p'')
                ok = True
                for (s, p) in A:
                    for pp in range(m[down[(s, p)]]):
                        s2 = down[(s, p)]                       # s down p
                        for ppp in range(m[down[(s2, pp)]]):    # p'' : P((s down p) down p')
                            lhs = op(s, op(s, p, pp), ppp)
                            rhs = op(s, p, op(s2, pp, ppp))
                            if lhs != rhs:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break
                if ok:
                    out.append((o, tuple(sorted(down.items())), tuple(sorted(oplus.items()))))
    return out


def categories(m):
    """Enumerate internal categories in Set on objects {0..n-1} with |out(s)| = m[s].

    Independent coding: arrows are labelled (s,k) with dom(s,k)=s.  A category is
    (cod, ident, comp) with comp CLASSICAL: comp[g][f] = g after f, defined when
    dom g = cod f.  Axioms: dom/cod of composite, identity laws, associativity.
    """
    n = len(m)
    A = [(s, k) for s in range(n) for k in range(m[s])]
    out = []
    for codvals in product(range(n), repeat=len(A)):
        cod = dict(zip(A, codvals))
        # identities: ident[s] must be an arrow with dom = s and cod = s
        cand = [[a for a in A if a[0] == s and cod[a] == s] for s in range(n)]
        if any(not c for c in cand):
            continue
        for ident in product(*cand):
            # composition: for each composable pair (f, g) with dom g = cod f,
            # choose g o f, an arrow with dom = dom f (and we then CHECK cod)
            pairs = [(f, g) for f in A for g in A if g[0] == cod[f]]
            choices = [[a for a in A if a[0] == f[0]] for (f, g) in pairs]
            for vals in product(*choices):
                comp = dict(zip(pairs, vals))
                # cod law: cod(g o f) = cod g
                if any(cod[comp[(f, g)]] != cod[g] for (f, g) in pairs):
                    continue
                # left unit: id_{cod f} o f = f
                if any(comp[(f, ident[cod[f]])] != f for f in A):
                    continue
                # right unit: f o id_{dom f} = f
                if any(comp[(ident[f[0]], f)] != f for f in A):
                    continue
                # associativity: h o (g o f) = (h o g) o f
                ok = True
                for f in A:
                    for g in [g for g in A if g[0] == cod[f]]:
                        gf = comp[(f, g)]
                        for h in [h for h in A if h[0] == cod[g]]:
                            hg = comp[(g, h)]
                            if comp[(gf, h)] != comp[(f, hg)]:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break
                if ok:
                    out.append((ident, tuple(sorted(cod.items())), tuple(sorted(comp.items()))))
    return out


if __name__ == "__main__":
    print(f"{'profile m':>12} | {'#DirCont':>9} | {'#Cat':>6} | match")
    print("-" * 44)
    profiles = [(1,), (2,), (3,), (1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (1, 3), (3, 2)]
    for m in profiles:
        dc = directed_containers(list(m))
        ct = categories(list(m))
        print(f"{str(m):>12} | {len(dc):>9} | {len(ct):>6} | {'OK' if len(dc) == len(ct) else 'MISMATCH'}")
