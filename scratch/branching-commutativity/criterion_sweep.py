"""
Confirm the E+A×(-) commutativity CRITERION by exhaustive sweep, and print the
explicit load-bearing witness.   PROVE 2026-07-31.

Criterion (hand-derived): E+A×(-) commutative  <=>
   (A commutative) AND (|E| <= 1) AND (action ⊙ trivial: a⊙e = e).
Sweep over: all monoid structures on small A, all left A-actions on small E.
"""
from itertools import product as iproduct
from commutativity import exc_writer_monad, is_commutative

X = ['x0', 'x1']; Y = ['y0', 'y1']

def all_monoids(n):
    """yield (elems, mul, unit) for all monoid structures on {0..n-1} with unit 0."""
    els = list(range(n))
    unit = 0
    # multiplication tables: mul[i][j] for i,j; unit row/col forced
    free_pairs = [(i, j) for i in els for j in els if i != unit and j != unit]
    for vals in iproduct(els, repeat=len(free_pairs)):
        tab = {}
        for i in els:
            tab[(unit, i)] = i
            tab[(i, unit)] = i
        for k, (i, j) in enumerate(free_pairs):
            tab[(i, j)] = vals[k]
        mul = lambda a, b, tab=tab: tab[(a, b)]
        # check associativity
        assoc = all(mul(mul(a, b), c) == mul(a, mul(b, c)) for a in els for b in els for c in els)
        if assoc:
            yield els, mul, unit

def all_actions(A_els, mul, unit, E_els):
    """yield left A-actions ⊙: A×E->E that are unital (unit⊙e=e) and assoc ((a.b)⊙e = a⊙(b⊙e))."""
    nonunit = [a for a in A_els if a != unit]
    pairs = [(a, e) for a in nonunit for e in E_els]
    for vals in iproduct(E_els, repeat=len(pairs)):
        act_tab = {}
        for e in E_els:
            act_tab[(unit, e)] = e
        for k, (a, e) in enumerate(pairs):
            act_tab[(a, e)] = vals[k]
        act = lambda a, e, t=act_tab: t[(a, e)]
        ok = all(act(mul(a, b), e) == act(a, act(b, e)) for a in A_els for b in A_els for e in E_els)
        if ok:
            yield act

def criterion(A_els, mul, unit, E_els, act):
    A_comm = all(mul(a, b) == mul(b, a) for a in A_els for b in A_els)
    E_small = len(E_els) <= 1
    triv = all(act(a, e) == e for a in A_els for e in E_els)
    return A_comm and E_small and triv

if __name__ == "__main__":
    print("=" * 70)
    print("E+A×(-) commutativity criterion sweep:  monad-comm  vs  (Acomm ∧ |E|≤1 ∧ triv⊙)")
    print("=" * 70)
    total = 0; mismatch = 0
    for nA in [1, 2, 3]:
        for nE in [0, 1, 2]:
            E_els = [f'e{i}' for i in range(nE)]
            cnt = 0; cnt_comm = 0
            for A_els, mul, unit in all_monoids(nA):
                for act in all_actions(A_els, mul, unit, E_els):
                    monad = exc_writer_monad(E_els, A_els, mul, unit, act)
                    obj, fmap, eta, mu = monad
                    comm, _ = is_commutative(obj, fmap, eta, mu, X, Y)
                    pred = criterion(A_els, mul, unit, E_els, act)
                    total += 1; cnt += 1; cnt_comm += comm
                    if comm != pred:
                        mismatch += 1
                        print(f"  MISMATCH nA={nA} nE={nE}: comm={comm} pred={pred}")
            print(f"  |A|={nA} |E|={nE}:  structures={cnt:4d}  #commutative={cnt_comm:4d}")
    print(f"\nTOTAL structures={total}   mismatches={mismatch}   "
          f"{'CRITERION CONFIRMED' if mismatch==0 else 'CRITERION FAILS'}")

    # ---- explicit load-bearing witness: Writer over noncomm N3 ----
    print("\n" + "=" * 70)
    print("LOAD-BEARING witness:  Writer M X = N3 × X,  N3 = {1,a,b}, a·b=a, b·a=b")
    print("=" * 70)
    from commutativity import writer_monad, noncomm3_monoid
    e, m, u = noncomm3_monoid()
    obj, fmap, eta, mu = writer_monad(e, m, u)
    comm, wit = is_commutative(obj, fmap, eta, mu, X, Y, verbose=True)
    print(f"  commutative? {comm}")
    if wit:
        mm, nn, Psi, Phi = wit
        print(f"  Ψ(m,n) uses a·b, Φ uses b·a:  Ψ={Psi}  Φ={Phi}  (a·b≠b·a)")
