"""
Magma-monad non-commutativity via the MEDIAL law.   PROVE 2026-07-31.

For a theory with a single binary operation *, the monad is COMMUTATIVE (Kock)
iff * is a homomorphism for itself in every algebra, which for a binary op is
exactly the MEDIAL (entropic/interchange) law:
        (a*b)*(c*d) = (a*c)*(b*d).
Hence: if SOME model (magma) violates mediality, the monad is NON-commutative.

- Free magma monad (no equations): need any medial-failing magma.  M1 = infinite (non-affine).
- Free IDEMPOTENT magma monad (only x*x=x): need an idempotent medial-failing magma.
  M1 = 1 (affine): every one-variable term collapses to x via x*x=x.
"""
from itertools import product as iproduct

def is_medial(n, tab):
    # tab[(i,j)] in range(n)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if tab[(a, b), ] if False else None:  # noqa
                        pass
                    lhs = tab[(tab[(a, b)], tab[(c, d)])]
                    rhs = tab[(tab[(a, c)], tab[(b, d)])]
                    if lhs != rhs:
                        return False, (a, b, c, d, lhs, rhs)
    return True, None

def search(n, idempotent):
    cells = [(i, j) for i in range(n) for j in range(n)]
    if idempotent:
        free_cells = [(i, j) for (i, j) in cells if i != j]
    else:
        free_cells = cells
    for vals in iproduct(range(n), repeat=len(free_cells)):
        tab = {}
        if idempotent:
            for i in range(n):
                tab[(i, i)] = i
        for k, (i, j) in enumerate(free_cells):
            tab[(i, j)] = vals[k]
        med, wit = is_medial(n, tab)
        if not med:
            return tab, wit
    return None, None

def show(tab, n, wit, label):
    print(f"\n--- {label} ---")
    print("   * | " + " ".join(str(j) for j in range(n)))
    for i in range(n):
        print(f"   {i} | " + " ".join(str(tab[(i, j)]) for j in range(n)))
    a, b, c, d, lhs, rhs = wit
    print(f"  mediality FAILS: ({a}*{b})*({c}*{d}) = {lhs}  !=  ({a}*{c})*({b}*{d}) = {rhs}")
    print("  => single-binary-op monad is NON-COMMUTATIVE (Kock: comm monad => op medial in all algebras)")

if __name__ == "__main__":
    print("=" * 70)
    print("Non-commutativity witnesses for magma monads (medial-law failure)")
    print("=" * 70)
    # Free magma: smallest medial-failing magma
    for n in [2, 3]:
        tab, wit = search(n, idempotent=False)
        if tab:
            show(tab, n, wit, f"FREE MAGMA: medial-failing magma on {n} elements")
            break
    # Idempotent magma: smallest idempotent medial-failing magma
    for n in [2, 3, 4]:
        tab, wit = search(n, idempotent=True)
        if tab:
            show(tab, n, wit, f"IDEMPOTENT MAGMA: idempotent medial-failing magma on {n} elements")
            break

    # sanity: confirm left-zero band IS medial (so it does NOT witness non-comm)
    print("\n--- sanity: left-zero band a*b=a is medial (does NOT witness) ---")
    n = 3
    tab = {(i, j): i for i in range(n) for j in range(n)}
    med, wit = is_medial(n, tab)
    print(f"  left-zero band medial? {med}")
