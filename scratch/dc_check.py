#!/usr/bin/env python3
"""
Exhaustive verification of the directed-container laws D1-D5 for:

  Example A -- the monoid directed container (S = 1), tested on
               (Z/6, +) and the multiplicative monoid (Z/6, *).

  Example B -- the non-empty-list / "tails" directed container
               S = N, P(n) = {0,...,n}, o_n = 0, n |> k = n - k,
               k (+) k' = k + k'.   Tested for all n <= 12.

The directed-container data is (S, P, o, sub, tr) with laws:

  (D1) sub(s, o(s)) = s
  (D2) sub(s, tr(s,p,p')) = sub( sub(s,p), p' )
  (D3) tr(s, o(s), p)  = p                  for p in P(s)         (left unit)
  (D4) tr(s, p, o(sub(s,p))) = p            for p in P(s)         (right unit)
  (D5) tr(s, tr(s,p,p'), p'')               (associativity)
         = tr(s, p, tr(sub(s,p), p', p''))

Throughout we ALSO assert that every position produced by o(.) and tr(.)
actually lies in the position set it is supposed to -- i.e. the operations
are well-typed / in range.  A law check is meaningless if the terms leave
their domains.
"""

# ----------------------------------------------------------------------
# Generic law checker.
#
# A directed container is given as a dict of callables:
#   shapes()        -> iterable of shapes s
#   positions(s)    -> iterable of positions p in P(s)
#   o(s)            -> root position in P(s)
#   sub(s, p)       -> shape  s |> p
#   tr(s, p, pp)    -> position p (+) pp  in P(s)
# ----------------------------------------------------------------------

def in_positions(dc, s, p):
    return p in set(dc["positions"](s))

def check(dc, name):
    o, sub, tr = dc["o"], dc["sub"], dc["tr"]
    n_checked = {"D1": 0, "D2": 0, "D3": 0, "D4": 0, "D5": 0, "range": 0}

    for s in dc["shapes"]():
        Ps = list(dc["positions"](s))

        # --- root is in range, and (D1) ---
        os = o(s)
        assert in_positions(dc, s, os), f"[{name}] root o({s})={os} not in P({s})"
        n_checked["range"] += 1
        assert sub(s, os) == s, f"[{name}] D1 fails at s={s}: sub(s,o)={sub(s,os)} != {s}"
        n_checked["D1"] += 1

        for p in Ps:
            sp = sub(s, p)          # the subshape s |> p
            Psp = list(dc["positions"](sp))

            # (D3) left unit: tr(s, o(s), p) = p
            lhs = tr(s, os, p)
            assert in_positions(dc, s, lhs), \
                f"[{name}] D3 result tr({s},o,{p})={lhs} out of P({s})"
            assert lhs == p, f"[{name}] D3 fails s={s} p={p}: {lhs} != {p}"
            n_checked["D3"] += 1

            # (D4) right unit: tr(s, p, o(sub(s,p))) = p
            osp = o(sp)
            assert in_positions(dc, sp, osp), \
                f"[{name}] root o({sp})={osp} out of P({sp})"
            rhs = tr(s, p, osp)
            assert in_positions(dc, s, rhs), \
                f"[{name}] D4 result tr({s},{p},o)={rhs} out of P({s})"
            assert rhs == p, f"[{name}] D4 fails s={s} p={p}: {rhs} != {p}"
            n_checked["D4"] += 1

            for pp in Psp:
                # tr must land in P(s); record range check
                t = tr(s, p, pp)
                assert in_positions(dc, s, t), \
                    f"[{name}] tr({s},{p},{pp})={t} out of P({s}) -- OUT OF RANGE"
                n_checked["range"] += 1

                # (D2) sub(s, tr(s,p,pp)) = sub(sub(s,p), pp)
                left = sub(s, t)
                right = sub(sp, pp)
                assert left == right, \
                    f"[{name}] D2 fails s={s} p={p} pp={pp}: {left} != {right}"
                n_checked["D2"] += 1

                # (D5) associativity over the inner subshape
                spp = sub(sp, pp)              # (s|>p)|>pp
                for ppp in dc["positions"](spp):
                    # tr(s, tr(s,p,pp), ppp)
                    l = tr(s, t, ppp)
                    # tr(s, p, tr(sub(s,p), pp, ppp))
                    inner = tr(sp, pp, ppp)
                    assert in_positions(dc, sp, inner), \
                        f"[{name}] D5 inner tr out of range"
                    r = tr(s, p, inner)
                    assert in_positions(dc, s, l) and in_positions(dc, s, r), \
                        f"[{name}] D5 outer tr out of range"
                    assert l == r, \
                        f"[{name}] D5 fails s={s} p={p} pp={pp} ppp={ppp}: {l} != {r}"
                    n_checked["D5"] += 1
    return n_checked


# ----------------------------------------------------------------------
# Example A -- monoid directed container.
# S = {0} (single shape), P(0) = M, o = e, sub = const(0), tr = product.
# ----------------------------------------------------------------------

def monoid_dc(elements, e, op):
    return {
        "shapes":    lambda: [0],
        "positions": lambda s: list(elements),
        "o":         lambda s: e,
        "sub":       lambda s, p: 0,
        "tr":        lambda s, p, pp: op(p, pp),
    }

# Z/6 under addition: identity 0, op = (a+b) mod 6
Z6_add = monoid_dc(range(6), 0, lambda a, b: (a + b) % 6)

# Z/6 under multiplication: identity 1, op = (a*b) mod 6
Z6_mul = monoid_dc(range(6), 1, lambda a, b: (a * b) % 6)


# ----------------------------------------------------------------------
# Example B -- non-empty-list / tails directed container.
# S = N (truncated to n <= NMAX), P(n) = {0,...,n},
# o_n = 0, n |> k = n - k, k (+) k' = k + k'.
# ----------------------------------------------------------------------

NMAX = 12

ListsDC = {
    "shapes":    lambda: range(NMAX + 1),
    "positions": lambda n: range(n + 1),     # {0,...,n}
    "o":         lambda n: 0,
    "sub":       lambda n, k: n - k,         # suffix length n-k (as shape)
    "tr":        lambda n, k, kp: k + kp,
}


if __name__ == "__main__":
    print("=" * 64)
    print("Directed-container law checker (D1-D5), exhaustive")
    print("=" * 64)

    for name, dc in [
        ("Example A: (Z/6, +, 0)", Z6_add),
        ("Example A: (Z/6, *, 1)", Z6_mul),
        (f"Example B: tails DC, n <= {NMAX}", ListsDC),
    ]:
        counts = check(dc, name)
        total = sum(counts.values())
        print(f"\n[PASS] {name}")
        print(f"        checks: D1={counts['D1']}  D2={counts['D2']}  "
              f"D3={counts['D3']}  D4={counts['D4']}  D5={counts['D5']}  "
              f"range={counts['range']}")
        print(f"        total assertions passed: {total}")

    print("\n" + "=" * 64)
    print("ALL ASSERTIONS PASSED.")
    print("=" * 64)
