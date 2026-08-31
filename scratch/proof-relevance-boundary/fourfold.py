"""
Fourfold check: for Reader/State, verify by BRUTE FORCE over all predicates P that
  - box  (proof-irrelevant forall):  box-box P(mm) => box P(mu mm)  for all P  <=> reverse-total
  - diamond (proof-irrelevant exists): dia-dia P(mm) => dia P(mu mm) for all P  <=> forward-total
This validates BOTH totality directions independently of the Yoneda (proof-relevant) argument.
The proof-relevant Pi/Sigma cases are governed by Lemma 1 (Yoneda) = the same matching condition.
"""
from itertools import product

def reader_double(E, X):
    inner = list(product(range(X), repeat=E))
    return list(product(inner, repeat=E))

def reader_tokens(mm, E):
    return [((b, c), mm[b][c]) for b in range(E) for c in range(E)]

def reader_leaves(mm, E):
    return [(e, mm[e][e]) for e in range(E)]

def state_all_g(S, X):
    cells = list(product(range(S), range(X)))
    return list(product(cells, repeat=S))

def state_double(S, X):
    gs = state_all_g(S, X)
    outer = [(s1, g) for s1 in range(S) for g in gs]
    return list(product(outer, repeat=S))

def state_tokens(mm, S):
    out = []
    for s0 in range(S):
        s1, g = mm[s0]
        for sp in range(S):
            out.append(((s0, sp), g[sp][1]))
    return out

def state_leaves(mm, S):
    lv = []
    for s0 in range(S):
        s1, g = mm[s0]
        lv.append((s0, g[s1][1]))
    return lv

def all_predicates(X):
    for bits in product([False, True], repeat=X):
        yield frozenset(i for i in range(X) if bits[i])

def fwd_total(toks, leaves):
    ll = set(l for _, l in leaves)
    return all(lab in ll for _, lab in toks)

def rev_total(toks, leaves):
    tl = set(l for _, l in toks)
    return all(lab in tl for _, lab in leaves)

def box_lift(toks, leaves, X):
    # for all P: (all tokens in P) => (all leaves in P)
    for P in all_predicates(X):
        if all(l in P for _, l in toks) and not all(l in P for _, l in leaves):
            return False
    return True

def dia_lift(toks, leaves, X):
    # for all P: (exists token in P) => (exists leaf in P)
    for P in all_predicates(X):
        if any(l in P for _, l in toks) and not any(l in P for _, l in leaves):
            return False
    return True

def run(name, doubles, tok, lv, X):
    n = len(doubles); ok = True
    for mm in doubles:
        t = tok(mm); l = lv(mm)
        f = fwd_total(t, l); r = rev_total(t, l)
        b = box_lift(t, l, X); d = dia_lift(t, l, X)
        if not (b == r and d == f):
            ok = False
            print(f"   MISMATCH mm={mm} box={b} rev={r} dia={d} fwd={f}")
            break
    print(f" {name}: #mm={n}  box<=>reverse-total AND diamond<=>forward-total : {ok}")

if __name__ == "__main__":
    print("Fourfold boundary (brute force over all P):")
    for (E, X) in [(2, 2), (2, 3), (3, 2)]:
        run(f"Reader E={E},X={X}", reader_double(E, X),
            lambda mm, E=E: reader_tokens(mm, E),
            lambda mm, E=E: reader_leaves(mm, E), X)
    for (S, X) in [(2, 2)]:
        run(f"State S={S},X={X}", state_double(S, X),
            lambda mm, S=S: state_tokens(mm, S),
            lambda mm, S=S: state_leaves(mm, S), X)
