"""
Verification for 2026-08-08-sigma-monad-is-triangle-monoid.md.

Core claim of the refutation (Lemma 4.2 / Thm 4.3):
  Bag (finite multiset monad) is reverse-total but is NOT a container functor,
  because it fails to preserve the connected pullback  A -> 1 <- B  (= A x B).
  Container/polynomial functors preserve wide (connected) pullbacks; Bag does not.
Therefore T^Sigma_Bag = Bag <| (-) is not even a functor on Cont, though Bag is
reverse-total (its mu is a leaf-bijection).  So reverse-total =/=> Sigma-monad.
"""
from math import comb
from collections import Counter
from itertools import combinations_with_replacement as cwr


def bag_size(k, n):
    """|Bag(k)|_n = number of size-n multisets over a k-element set."""
    return comb(k + n - 1, n)


def check_pullback_preservation(A=2, B=2, sizes=(2, 3)):
    print(f"=== Bag connected-pullback (product) preservation, A={A} B={B} ===")
    ok = True
    for n in sizes:
        lhs = bag_size(A * B, n)          # |Bag(AxB)|_n
        rhs = bag_size(A, n) * bag_size(B, n)  # |BagA x_{Bag1} BagB|_n
        preserved = (lhs == rhs)
        ok &= preserved
        print(f"  n={n}:  |Bag(AxB)|_n = {lhs:3d}   |BagA x_Bag1 BagB|_n = {rhs:3d}"
              f"   preserved={preserved}")
    print(f"  => Bag preserves this pullback: {ok}  (False means Bag is NOT a container)\n")
    return ok


def collision_witness():
    """Two distinct size-2 multisets over 2x2 with identical (projA, projB) image."""
    print("=== explicit non-injectivity witness (n=2, A=B={0,1}) ===")
    def img(ms):
        return (tuple(sorted(x[0] for x in ms)), tuple(sorted(x[1] for x in ms)))
    w1 = ((0, 0), (1, 1))
    w2 = ((0, 1), (1, 0))
    print(f"  w1 = {{{w1[0]},{w1[1]}}}  -> (projA,projB) = {img(w1)}")
    print(f"  w2 = {{{w2[0]},{w2[1]}}}  -> (projA,projB) = {img(w2)}")
    distinct = Counter(w1) != Counter(w2)
    same = img(w1) == img(w2)
    print(f"  distinct multisets: {distinct}   same image: {same}")
    print(f"  => comparison map non-injective: {distinct and same}"
          f"   (Bag forgets the pairing)\n")
    return distinct and same


def brute_force_all_witnesses(A=2, B=2, n=2):
    """Confirm the count gap by enumerating multisets directly (no formula)."""
    universe = [(a, b) for a in range(A) for b in range(B)]
    lhs = list(cwr(universe, n))
    def img(ms):
        return (tuple(sorted(x[0] for x in ms)), tuple(sorted(x[1] for x in ms)))
    images = {}
    for ms in lhs:
        images.setdefault(img(ms), []).append(ms)
    collisions = {k: v for k, v in images.items() if len(v) > 1}
    print(f"=== brute force A={A} B={B} n={n}: "
          f"|Bag(AxB)|={len(lhs)}  |distinct images|={len(images)} ===")
    for k, v in collisions.items():
        print(f"  image {k} hit by {len(v)} multisets: {v}")
    print()
    return len(lhs), len(images)


if __name__ == "__main__":
    p = check_pullback_preservation()
    w = collision_witness()
    brute_force_all_witnesses()
    assert not p, "expected Bag to FAIL pullback preservation"
    assert w, "expected an explicit collision witness"
    print("ALL CHECKS CONSISTENT: Bag is reverse-total but not a container "
          "=> reverse-total does NOT imply Sigma-monad.")
