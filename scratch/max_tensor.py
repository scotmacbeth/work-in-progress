"""
Search for a monoidal structure on FinSet_{<=2} (objects of size 0,1,2)
with object map |A * B| = max(|A|,|B|) and unit I = empty set (size 0).

Objects: 0,1,2 (sizes). Standard set of size s = range(s).
Morphisms: all functions between standard sets.  Represented as (dom, cod, tab),
tab a tuple of length dom with entries in range(cod).
"""
import itertools, sys
sys.setrecursionlimit(100000)

# ---------- category C = FinSet_{<=2} ----------
morphs = []
for dom in range(3):
    for cod in range(3):
        for tab in itertools.product(range(cod), repeat=dom):
            morphs.append((dom, cod, tab))

def ident(a):
    return (a, a, tuple(range(a)))

def comp(g, f):
    # g after f ; f: A->B, g: B->C ; result A->C
    assert f[1] == g[0], (f, g)
    return (f[0], g[1], tuple(g[2][f[2][x]] for x in range(f[0])))

# sanity: composition closed, identities
for m in morphs:
    assert comp(ident(m[1]), m) == m
    assert comp(m, ident(m[0])) == m

print("num morphisms in C:", len(morphs))
# list them
from collections import defaultdict
byhom = defaultdict(list)
for m in morphs:
    byhom[(m[0], m[1])].append(m)
for k in sorted(byhom):
    print("  hom", k, "size", len(byhom[k]))

def star_obj(a, b):
    return max(a, b)

# candidate F-value morphisms for a pair (m1,m2)
def fvar_domcod(m1, m2):
    d = star_obj(m1[0], m2[0])
    c = star_obj(m1[1], m2[1])
    return d, c

def candidates(m1, m2):
    d, c = fvar_domcod(m1, m2)
    return byhom[(d, c)]

# ---------- enumerate bifunctors F: C x C -> C with this object map ----------
# assignment: dict pair(m1,m2) -> morph
# constraints: F(id,id)=id ; F((m1',m1),(m2',m2)) composition preserved.

pairs = [(m1, m2) for m1 in morphs for m2 in morphs]

def compose_pair(q, p):
    # q after p in product category ; p=(a1,a2), q=(b1,b2)
    # defined iff a1[1]==b1[0] and a2[1]==b2[0]
    (a1, a2) = p
    (b1, b2) = q
    if a1[1] != b1[0] or a2[1] != b2[0]:
        return None
    return (comp(b1, a1), comp(b2, a2))

def propagate(assign, newly):
    """Given assign dict and list of newly-assigned pairs, derive forced values.
    Returns list of all newly assigned (including derived) or None on contradiction."""
    added = list(newly)
    queue = list(newly)
    assigned_keys = list(assign.keys())
    while queue:
        p = queue.pop()
        fp = assign[p]
        # combine p with every currently assigned q, both orders
        for q in list(assign.keys()):
            fq = assign[q]
            # q after p
            r = compose_pair(q, p)
            if r is not None:
                val = comp(fq, fp)
                if r in assign:
                    if assign[r] != val:
                        return None
                else:
                    assign[r] = val
                    added.append(r); queue.append(r)
            # p after q
            r2 = compose_pair(p, q)
            if r2 is not None:
                val2 = comp(fp, fq)
                if r2 in assign:
                    if assign[r2] != val2:
                        return None
                else:
                    assign[r2] = val2
                    added.append(r2); queue.append(r2)
    return added

def solve_bifunctors(limit=None):
    # start: all identity pairs forced
    assign = {}
    newly = []
    for a in range(3):
        for b in range(3):
            p = (ident(a), ident(b))
            assign[p] = ident(star_obj(a, b))
            newly.append(p)
    if propagate(assign, newly) is None:
        return []
    results = []
    order = None

    def pick_var(assign):
        best = None; bestn = 999
        for p in pairs:
            if p not in assign:
                n = len(candidates(*p))
                if n < bestn:
                    bestn = n; best = p
                    if n == 1:
                        break
        return best

    def bt(assign):
        if limit is not None and len(results) >= limit:
            return
        var = pick_var(assign)
        if var is None:
            results.append(dict(assign))
            return
        for val in candidates(*var):
            a2 = dict(assign)
            a2[var] = val
            res = propagate(a2, [var])
            if res is not None:
                bt(a2)
                if limit is not None and len(results) >= limit:
                    return
    bt(assign)
    return results

if __name__ == "__main__":
    print("\nsearching bifunctors...")
    bfs = solve_bifunctors(limit=100000)
    print("number of bifunctors (functors CxC->C with object map max):", len(bfs))
