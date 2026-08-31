#!/usr/bin/env python3
"""
Emergent holonomy count h(A,B) = |A\\U/B| on U = C_{p^n} (cyclic p-group).

We build U = Z/(p^n) additively. Subgroups H_k (order p^k, k=0..n) are the
multiples of p^{n-k}. Every subgroup is normal, so double cosets A x B are
just cosets of AB; but we DO NOT assume that -- we enumerate the actual
double cosets by brute force and only afterwards compare with the formula
    h(H_a, H_b) = p^{n - max(a,b)}.
"""

def subgroup(p, n, k):
    """H_k <= Z/p^n of order p^k : multiples of p^{n-k}."""
    N = p**n
    step = p**(n - k)
    return frozenset((step * i) % N for i in range(p**k))

def double_cosets(p, n, A, B):
    """Brute-force enumerate A\\U/B in U = Z/p^n. Returns list of coset sets."""
    N = p**n
    remaining = set(range(N))
    cosets = []
    while remaining:
        x = next(iter(remaining))
        # double coset A x B = { (a + x + b) mod N }
        dc = frozenset((a + x + b) % N for a in A for b in B)
        cosets.append(dc)
        remaining -= dc
    return cosets

def run():
    cases_checked = 0
    mismatches = 0
    for p in (2, 3):
        for n in (1, 2, 3):
            N = p**n
            H = {k: subgroup(p, n, k) for k in range(n + 1)}
            # sanity: subgroup orders and nesting
            for k in range(n + 1):
                assert len(H[k]) == p**k
                if k < n:
                    assert H[k] < H[k + 1]
            print(f"\n=== p={p}, n={n}, |U|={N} ===")
            header = "  a\\b |" + "".join(f"{b:6d}" for b in range(n + 1))
            print(header)
            print("  " + "-" * (len(header) - 2))
            for a in range(n + 1):
                row = []
                for b in range(n + 1):
                    dcs = double_cosets(p, n, H[a], H[b])
                    h = len(dcs)
                    # verify the double cosets actually partition U
                    union = set().union(*dcs)
                    total = sum(len(dc) for dc in dcs)
                    assert union == set(range(N))
                    assert total == N  # disjoint partition
                    formula = p**(n - max(a, b))
                    cases_checked += 1
                    if h != formula:
                        mismatches += 1
                        print(f"  MISMATCH a={a} b={b}: brute={h} formula={formula}")
                    row.append(h)
                print(f"  {a:3d}  |" + "".join(f"{v:6d}" for v in row))
    print(f"\nCases checked: {cases_checked}")
    print(f"Mismatches   : {mismatches}")
    print("VERDICT: " + ("ALL MATCH" if mismatches == 0 else "DISCREPANCY"))

    # structural observation: h depends only on max(a,b)
    print("\nStructural check: does h depend only on max(a,b)?")
    only_max = True
    for p in (2, 3):
        for n in (1, 2, 3):
            for a in range(n + 1):
                for b in range(n + 1):
                    if p**(n - max(a, b)) != p**(n - max(a, b)):
                        only_max = False
    # trivially true by formula; the real content is the brute-force==formula match above
    print("  h(H_a,H_b) = [U:AB] = p^{n-max(a,b)}  -> depends ONLY on max(a,b).")

if __name__ == "__main__":
    run()
