import itertools, random

random.seed(12345)

# ---------- helpers ----------
def all_functions(dom, cod):
    """List all functions dom->cod as dicts. dom, cod are lists."""
    cod = list(cod)
    for values in itertools.product(cod, repeat=len(dom)):
        yield dict(zip(dom, values))

# ============================================================
# TASK 1 — External distributive law
#   [P, ∐_t Y_t]  ≅  ∐_{c:P->T} ∏_t [P^c_t, Y_t]
# ============================================================
# Representations:
#  P = list of ints 0..|P|-1
#  T = list 0..|T|-1
#  Y = dict t -> list of elements (we use ('y', t, i) tagged elements for the coproduct)
# Element of LHS: function g: P -> ∐_t Y_t, i.e. dict p -> ('y', t, i)
# Element of RHS: (c, {t: h_t}) where c: P->T (dict), h_t: c^{-1}(t) -> Y_t

def coproduct_Y(Y, T):
    """Elements of ∐_t Y_t as tagged tuples ('y', t, i)."""
    elts = []
    for t in T:
        for i in range(len(Y[t])):
            elts.append(('y', t, i))
    return elts

def LHS1_elements(P, Y, T):
    cop = coproduct_Y(Y, T)
    return list(all_functions(P, cop))

def RHS1_elements(P, Y, T):
    elts = []
    for c in all_functions(P, T):
        # fibres
        fibres = {t: [p for p in P if c[p] == t] for t in T}
        # for each t, all functions fibres[t] -> Y_t  (Y_t indices 0..|Y_t|-1)
        per_t_choices = []
        tags = []
        for t in T:
            dom = fibres[t]
            cod = list(range(len(Y[t])))
            per_t_choices.append(list(all_functions(dom, cod)))
            tags.append(t)
        for combo in itertools.product(*per_t_choices):
            h = {tags[k]: combo[k] for k in range(len(tags))}
            # store c as tuple for hashability, h as frozen structure
            elts.append((tuple(c[p] for p in P), h))
    return elts

def forward1(g, P, Y, T):
    """LHS element g -> RHS element (c,h)."""
    c = {p: g[p][1] for p in P}  # tag t
    fibres = {t: [p for p in P if c[p] == t] for t in T}
    h = {}
    for t in T:
        h[t] = {p: g[p][2] for p in fibres[t]}  # index within Y_t
    return (tuple(c[p] for p in P), h)

def backward1(rhs, P, Y, T):
    """RHS element (c_tuple,h) -> LHS element g."""
    c_tuple, h = rhs
    c = {P[k]: c_tuple[k] for k in range(len(P))}
    g = {}
    for p in P:
        t = c[p]
        i = h[t][p]
        g[p] = ('y', t, i)
    return g

def rhs_key(rhs):
    c_tuple, h = rhs
    # normalise h into a hashable form
    hk = tuple((t, tuple(sorted(h[t].items()))) for t in sorted(h.keys()))
    return (c_tuple, hk)

def task1():
    N = 200
    card_mismatch = 0
    bij_fail = 0
    for _ in range(N):
        nP = random.randint(0, 4)
        nT = random.randint(1, 4)
        P = list(range(nP))
        T = list(range(nT))
        Y = {t: list(range(random.randint(0, 4))) for t in T}

        # (a) cardinality
        lhs_card = sum(len(Y[t]) for t in T) ** nP
        rhs_card = 0
        for c in all_functions(P, T):
            prod = 1
            for t in T:
                fib = sum(1 for p in P if c[p] == t)
                prod *= len(Y[t]) ** fib
            rhs_card += prod
        if lhs_card != rhs_card:
            card_mismatch += 1

        # (b) bijection: enumerate LHS, map forward, check image = RHS set, round-trip
        lhs = LHS1_elements(P, Y, T)
        rhs = RHS1_elements(P, Y, T)
        rhs_keys = set(rhs_key(r) for r in rhs)

        if len(rhs_keys) != len(rhs):
            bij_fail += 1
            continue

        image_keys = set()
        ok = True
        for g in lhs:
            r = forward1(g, P, Y, T)
            k = rhs_key(r)
            image_keys.add(k)
            # round trip forward then backward
            g2 = backward1(r, P, Y, T)
            if g2 != g:
                ok = False
                break
        if not ok:
            bij_fail += 1
            continue
        # image must equal rhs set, and be injective (|image|==|lhs|)
        if image_keys != rhs_keys or len(image_keys) != len(lhs):
            bij_fail += 1
            continue
        # round-trip other way: RHS -> LHS -> RHS
        ok2 = True
        for r in rhs:
            g = backward1(r, P, Y, T)
            r2 = forward1(g, P, Y, T)
            if rhs_key(r2) != rhs_key(r):
                ok2 = False
                break
        if not ok2:
            bij_fail += 1

    print(f"TASK 1: {N} instances | cardinality mismatches = {card_mismatch} | bijection failures = {bij_fail}")

# ============================================================
# TASK 2 — Derived admissibility formula
#   [P, ⟦q⟧X]  ≅  ∐_{c:P->T} [ ∐_t (P^c_t × Q_t), X ]
#   ⟦q⟧X = ∐_t [Q_t, X]
# ============================================================
# LHS element: g: P -> ∐_t [Q_t,X]. An element of ⟦q⟧X is ('f', t, f) where f: Q_t -> X.
# RHS element: (c, k) where c:P->T, k: ∐_t (P^c_t × Q_t) -> X.
#   ∐_t(P^c_t × Q_t) elements: ('e', t, p, m) for p in c^{-1}(t), m in Q_t.

def qbrak_elements(Q, T, X):
    """Elements of ⟦q⟧X = ∐_t [Q_t,X]."""
    elts = []
    for t in T:
        for f in all_functions(list(range(len(Q[t]))), X):
            # represent f as tuple of images
            elts.append(('f', t, tuple(f[m] for m in range(len(Q[t])))))
    return elts

def LHS2_elements(P, Q, T, X):
    dom_elts = qbrak_elements(Q, T, X)
    return list(all_functions(P, dom_elts))

def dom_coproduct2(P, Q, T, c):
    """∐_t (P^c_t × Q_t) as list of ('e',t,p,m)."""
    fibres = {t: [p for p in P if c[p] == t] for t in T}
    elts = []
    for t in T:
        for p in fibres[t]:
            for m in range(len(Q[t])):
                elts.append(('e', t, p, m))
    return elts

def RHS2_elements(P, Q, T, X):
    elts = []
    for c in all_functions(P, T):
        dom = dom_coproduct2(P, Q, T, c)
        for k in all_functions(dom, X):
            elts.append((tuple(c[p] for p in P), tuple((e, k[e]) for e in dom)))
    return elts

def forward2(g, P, Q, T, X):
    """LHS g -> RHS (c,k)."""
    c = {p: g[p][1] for p in P}
    fibres = {t: [p for p in P if c[p] == t] for t in T}
    k = {}
    for t in T:
        for p in fibres[t]:
            # g[p] = ('f', t, images_tuple), f: Q_t -> X
            images = g[p][2]
            for m in range(len(Q[t])):
                k[('e', t, p, m)] = images[m]
    c_tuple = tuple(c[p] for p in P)
    dom = dom_coproduct2(P, Q, T, c)
    return (c_tuple, tuple((e, k[e]) for e in dom))

def backward2(rhs, P, Q, T, X):
    """RHS (c_tuple, k_pairs) -> LHS g."""
    c_tuple, k_pairs = rhs
    c = {P[i]: c_tuple[i] for i in range(len(P))}
    k = dict(k_pairs)
    g = {}
    for p in P:
        t = c[p]
        images = tuple(k[('e', t, p, m)] for m in range(len(Q[t])))
        g[p] = ('f', t, images)
    return g

def rhs2_key(rhs):
    c_tuple, k_pairs = rhs
    return (c_tuple, tuple(sorted(k_pairs)))

def task2a():
    N = 200
    card_mismatch = 0
    for _ in range(N):
        nP = random.randint(0, 3)
        nT = random.randint(1, 3)
        nX = random.randint(0, 3)
        P = list(range(nP))
        T = list(range(nT))
        X = list(range(nX))
        Q = {t: list(range(random.randint(0, 3))) for t in T}

        lhs_card = sum(nX ** len(Q[t]) for t in T) ** nP
        rhs_card = 0
        for c in all_functions(P, T):
            expo = 0
            for t in T:
                fib = sum(1 for p in P if c[p] == t)
                expo += fib * len(Q[t])
            rhs_card += nX ** expo
        if lhs_card != rhs_card:
            card_mismatch += 1
    print(f"TASK 2a: {N} instances | cardinality mismatches = {card_mismatch}")

def task2b():
    """Naturality in X. Build iso at X and X', random elt, check square."""
    N = 50
    nat_fail = 0
    iso_fail = 0
    for _ in range(N):
        nP = random.randint(0, 3)
        nT = random.randint(1, 3)
        nX = random.randint(1, 3)
        nX2 = random.randint(1, 3)
        P = list(range(nP))
        T = list(range(nT))
        X = list(range(nX))
        X2 = list(range(nX2))
        Q = {t: list(range(random.randint(0, 3))) for t in T}
        # random phi: X -> X2
        phi = {x: random.choice(X2) for x in X}

        # First: sanity that forward2/backward2 form a bijection at X (exhaustive small)
        lhs = LHS2_elements(P, Q, T, X)
        rhs = RHS2_elements(P, Q, T, X)
        rhs_keys = set(rhs2_key(r) for r in rhs)
        image = set()
        ok = True
        for g in lhs:
            r = forward2(g, P, Q, T, X)
            image.add(rhs2_key(r))
            if backward2(r, P, Q, T, X) != g:
                ok = False; break
        if not ok or image != rhs_keys or len(image) != len(lhs):
            iso_fail += 1
            continue

        # Functorial action on LHS: postcompose g's inner function with phi.
        # g: P -> ∐_t [Q_t,X]; LHS(phi)(g)[p] = ('f', t, tuple(phi[img] for img in images))
        def LHS_phi(g):
            gg = {}
            for p in P:
                _, t, images = g[p]
                gg[p] = ('f', t, tuple(phi[im] for im in images))
            return gg

        # Functorial action on RHS: postcompose k with phi.
        def RHS_phi(r):
            c_tuple, k_pairs = r
            new_pairs = tuple((e, phi[val]) for (e, val) in k_pairs)
            return (c_tuple, new_pairs)

        # iso at X: forward2(.,X); iso at X2: forward2(.,X2)
        # Check for every g in LHS(X): iso_{X2}(LHS_phi(g)) == RHS_phi(iso_X(g))
        for g in lhs:
            left = forward2(LHS_phi(g), P, Q, T, X2)
            right = RHS_phi(forward2(g, P, Q, T, X))
            if rhs2_key(left) != rhs2_key(right):
                nat_fail += 1
                break
    print(f"TASK 2b: {N} instances | iso failures = {iso_fail} | naturality failures = {nat_fail}")

if __name__ == "__main__":
    task1()
    task2a()
    task2b()
