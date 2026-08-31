"""
Proof-relevance boundary: forward-total (Task A) vs reverse-total (Task B)
for Reader_E and State_S base monads, via kappa_mu directions.

Self-contained finite enumeration. See task spec.
"""
from itertools import product

# ---------------------------------------------------------------------------
# READER_E:  M X = X^E  (functions E -> X)
# ---------------------------------------------------------------------------
# An element m in M X is a tuple of length |E| over X-labels (m[e] = label of leaf e).
# A double element mm in M(M X) is a function E -> (E -> X), i.e. tuple of tuples.
#   mm[b][c] = X-label of inner token (b,c).
# mu mm : E -> X, (mu mm)[e] = mm[e][e]   (DIAGONAL).

def reader_all_double(E, X):
    """all mm : E -> (E -> X), each represented as tuple of tuples of X-labels."""
    inner = list(product(range(X), repeat=E))          # all E->X
    return list(product(inner, repeat=E))              # all E->(E->X)

def reader_inner_tokens(mm, E):
    """I(mm): list of (token_id, label). token = (b,c), label = mm[b][c]."""
    toks = []
    for b in range(E):
        for c in range(E):
            toks.append(((b, c), mm[b][c]))
    return toks

def reader_mu_leaves(mm, E):
    """lv(mu mm): list of (leaf_id, label). leaf e, label mm[e][e]."""
    return [(e, mm[e][e]) for e in range(E)]

# ---------------------------------------------------------------------------
# STATE_S:  M X = (S x X)^S  (functions S -> S x X)
# ---------------------------------------------------------------------------
# element m : S -> (S, X-label).  represent as tuple over s of (s', label).
# double mm : S -> (S, g) where g : S -> (S, X-label).
#   We must represent mm as: for each s0, an (s1, g) with g a full S->(S,label) map.
# mu mm : S -> (S, label):  (s1, g) = mm[s0]; then result = g[s1].

def state_all_g(S, X):
    """all g : S -> (S, label)."""
    cells = list(product(range(S), range(X)))          # (s', label)
    return list(product(cells, repeat=S))              # S -> cell

def state_all_double(S, X):
    """all mm : S -> (S, g)."""
    gs = state_all_g(S, X)
    outer_cells = [(s1, g) for s1 in range(S) for g in gs]
    return list(product(outer_cells, repeat=S))

def state_inner_tokens(mm, S):
    """I(mm): token (s0, s') with inner element g = mm[s0][1]; label = snd(g[s'])."""
    toks = []
    for s0 in range(S):
        s1, g = mm[s0]
        for sp in range(S):
            toks.append(((s0, sp), g[sp][1]))
    return toks

def state_mu(mm, S):
    """mu mm : S -> (S, label). (s1,g)=mm[s0]; result[s0] = g[s1]."""
    res = []
    for s0 in range(S):
        s1, g = mm[s0]
        res.append(g[s1])          # (s', label)
    return res

def state_mu_leaves(mm, S):
    mu = state_mu(mm, S)
    return [(s0, mu[s0][1]) for s0 in range(S)]

# ---------------------------------------------------------------------------
# Totality predicates
# ---------------------------------------------------------------------------
def is_total_forward(inner_toks, leaves):
    """every inner-token label appears among surviving-leaf labels."""
    leaf_labels = set(l for _, l in leaves)
    return all(lab in leaf_labels for _, lab in inner_toks)

def is_total_reverse(inner_toks, leaves):
    """every surviving-leaf label appears among inner-token labels."""
    tok_labels = set(l for _, l in inner_toks)
    return all(lab in tok_labels for _, lab in leaves)

# ---------------------------------------------------------------------------
# Task B: propositional box conditions
# ---------------------------------------------------------------------------
def all_predicates(X):
    """all P : X -> bool, as frozenset subset of range(X)."""
    subs = []
    for bits in product([False, True], repeat=X):
        subs.append(frozenset(i for i in range(X) if bits[i]))
    return subs

def box(P, leaves):
    return all((lab in P) for _, lab in leaves)

def boxbox(P, inner_toks):
    return all((lab in P) for _, lab in inner_toks)

def mult_condition_holds(inner_toks, leaves, X):
    """for ALL P: boxbox P (mm) => box P (mu mm)."""
    for P in all_predicates(X):
        if boxbox(P, inner_toks) and not box(P, leaves):
            return False
    return True

# ---------------------------------------------------------------------------
# Reader monad-law sanity (unit + assoc) -- quick check via functions
# ---------------------------------------------------------------------------

def reader_report(E, X):
    mms = reader_all_double(E, X)
    n = len(mms)
    fwd = 0; rev = 0
    fwd_fail_witness = None
    equiv_ok = True; equiv_fail = None
    rev_always = True
    for mm in mms:
        toks = reader_inner_tokens(mm, E)
        leaves = reader_mu_leaves(mm, E)
        f = is_total_forward(toks, leaves)
        r = is_total_reverse(toks, leaves)
        if f: fwd += 1
        else:
            if fwd_fail_witness is None:
                leaf_labels = set(l for _, l in leaves)
                dropped = [(t, lab) for t, lab in toks if lab not in leaf_labels][0]
                fwd_fail_witness = (mm, dropped, leaves)
        if r: rev += 1
        else: rev_always = False
        mc = mult_condition_holds(toks, leaves, X)
        if mc != r:
            equiv_ok = False
            if equiv_fail is None: equiv_fail = (mm, mc, r)
    return dict(n=n, fwd=fwd, rev=rev, fwd_frac=fwd/n, rev_frac=rev/n,
               fwd_fail=fwd_fail_witness, equiv_ok=equiv_ok, equiv_fail=equiv_fail,
               rev_always=rev_always)

def state_report(S, X):
    mms = state_all_double(S, X)
    n = len(mms)
    fwd = 0; rev = 0
    fwd_fail_witness = None
    equiv_ok = True; equiv_fail = None
    rev_always = True
    for mm in mms:
        toks = state_inner_tokens(mm, S)
        leaves = state_mu_leaves(mm, S)
        f = is_total_forward(toks, leaves)
        r = is_total_reverse(toks, leaves)
        if f: fwd += 1
        else:
            if fwd_fail_witness is None:
                leaf_labels = set(l for _, l in leaves)
                dropped = [(t, lab) for t, lab in toks if lab not in leaf_labels][0]
                fwd_fail_witness = (mm, dropped, leaves)
        if r: rev += 1
        else: rev_always = False
        mc = mult_condition_holds(toks, leaves, X)
        if mc != r:
            equiv_ok = False
            if equiv_fail is None: equiv_fail = (mm, mc, r)
    return dict(n=n, fwd=fwd, rev=rev, fwd_frac=fwd/n, rev_frac=rev/n,
               fwd_fail=fwd_fail_witness, equiv_ok=equiv_ok, equiv_fail=equiv_fail,
               rev_always=rev_always)

# ---------------------------------------------------------------------------
# State monad-law sanity check (unit + assoc) on concrete small S,X
# ---------------------------------------------------------------------------
def state_monad_laws(S, Xset):
    """
    Check unit + assoc of state monad on Set with state S, value set Xset (as ints).
    Represent M X = functions S -> (S, x).  Use full function enumeration for a
    fixed small element to verify laws structurally.
    We check the three monad laws using eta and mu directly:
      left unit:  mu . eta_{MX} = id
      right unit: mu . M(eta) = id
      assoc:      mu . mu = mu . M(mu)
    We test on random-ish concrete triple-nested elements exhaustively for |S|=2,|X|=2.
    """
    S_ = S
    def eta(x):
        # X-> (S->(S,x))
        return tuple((s, x) for s in range(S_))
    def mu_gen(mm):
        # mm : S -> (S, g), g: S->(S,y).  returns S->(S,y)
        res = []
        for s0 in range(S_):
            s1, g = mm[s0]
            res.append(g[s1])
        return tuple(res)
    # left unit: eta at (MX) then mu = id.  eta_{MX}(m) = (s |-> (s, m)).
    # Build all m : S -> (S, x)
    Xs = list(Xset)
    all_m = list(product([(s, x) for s in range(S_) for x in Xs], repeat=S_))
    ok_left = True; ok_right = True
    for m in all_m:
        # left unit
        mm_left = tuple((s, m) for s in range(S_))    # eta_{MX}(m)
        if mu_gen(mm_left) != m:
            ok_left = False
        # right unit: M(eta)(m) = s |-> (s', eta(x)) where m[s]=(s',x)
        mm_right = tuple((m[s][0], eta(m[s][1])) for s in range(S_))
        if mu_gen(mm_right) != m:
            ok_right = False
    # assoc: on triple mmm : S -> (S, (S -> (S, g)))  -- exhaustive is large;
    # sample exhaustively for |S|=2,|X|=2 using representable structure.
    # mmm[s0] = (s1, mm) with mm : S -> (S, g), g : S->(S,x).
    gs = list(product([(s, x) for s in range(S_) for x in Xs], repeat=S_))
    mms_ = list(product([(s1, g) for s1 in range(S_) for g in gs], repeat=S_))
    # mmm : S -> (S, mm)
    outer = [(s2, mm) for s2 in range(S_) for mm in mms_]
    ok_assoc = True
    count = 0
    for mmm in product(outer, repeat=S_):
        count += 1
        # path1: mu . mu :  first mu on OUTER layer collapsing (S,(S,mm)) -> (S,mm')?
        # mu . M(mu): apply mu inside each, then mu.
        # Define lifted M(mu): mmm[s]=(s', mm) -> (s', mu(mm))
        Mmu = tuple((mmm[s][0], mu_gen(mmm[s][1])) for s in range(S_))
        left_path = mu_gen(Mmu)                 # mu . M(mu)
        # mu . mu : treat mmm as element of M(M(MX)); outer mu gives element of M(MX):
        #   mu(mmm) : S->(S, g?) ... need mu on the top two layers.
        #   top-level mm has type S->(S, mm_inner). mu_gen collapses one layer:
        outer_mu = mu_gen(mmm)                  # : S -> (S, g)  (element of M(MX))
        right_path = mu_gen(outer_mu)           # mu again
        if left_path != right_path:
            ok_assoc = False
            break
    return dict(left_unit=ok_left, right_unit=ok_right, assoc=ok_assoc, assoc_cases=count)


if __name__ == "__main__":
    print("="*70)
    print("READER  M X = X^E")
    print("="*70)
    for (E, X) in [(2,2),(2,3),(3,2)]:
        r = reader_report(E, X)
        print(f"\n Reader |E|={E}, |X|={X}:  #mm = {r['n']}")
        print(f"   forward-total fraction = {r['fwd']}/{r['n']} = {r['fwd_frac']:.4f}")
        print(f"   reverse-total fraction = {r['rev']}/{r['n']} = {r['rev_frac']:.4f}"
              f"   (always true? {r['rev_always']})")
        print(f"   equivalence (mult-cond <=> reverse-total) exact? {r['equiv_ok']}")
        if r['fwd_fail']:
            mm, dropped, leaves = r['fwd_fail']
            print(f"   forward-FAIL witness mm = {mm}")
            print(f"       dropped inner token {dropped[0]} label={dropped[1]}")
            print(f"       surviving leaves(id,label) = {leaves}")

    print("\n" + "="*70)
    print("STATE  M X = (S x X)^S")
    print("="*70)
    for (S, X) in [(2,2)]:
        r = state_report(S, X)
        print(f"\n State |S|={S}, |X|={X}:  #mm = {r['n']}")
        print(f"   forward-total fraction = {r['fwd']}/{r['n']} = {r['fwd_frac']:.4f}")
        print(f"   reverse-total fraction = {r['rev']}/{r['n']} = {r['rev_frac']:.4f}"
              f"   (always true? {r['rev_always']})")
        print(f"   equivalence (mult-cond <=> reverse-total) exact? {r['equiv_ok']}")
        if r['fwd_fail']:
            mm, dropped, leaves = r['fwd_fail']
            print(f"   forward-FAIL witness mm = {mm}")
            print(f"       dropped inner token {dropped[0]} label={dropped[1]}")
            print(f"       surviving leaves(id,label) = {leaves}")

    print("\n State monad-law sanity (|S|=2,|X|=2):")
    laws = state_monad_laws(2, [0,1])
    print(f"   left_unit={laws['left_unit']}  right_unit={laws['right_unit']}"
          f"  assoc={laws['assoc']}  (assoc cases checked={laws['assoc_cases']})")
