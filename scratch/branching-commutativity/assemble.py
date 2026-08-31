"""
Assemble the witness cube and verify: (i) each 2x2 face of (P1,P2,P3) is fully
populated  => pairwise independence; (ii) the only unrealised cell is (T,F,T).
Properties per witness are taken from the machine checks (commutativity.py /
magma_search.py) plus the two structural facts (branching, M1) recorded here.
PROVE 2026-07-31.
"""
from commutativity import (identity_monad, exc_writer_monad, writer_monad,
                           powerset_monad, distribution_monad, noncomm3_monoid,
                           Zn_monoid, is_commutative, affine_size)

X = ['x0', 'x1']; Y = ['y0', 'y1']

def const1_monad():
    """M X = 1.  eta: X->1 unique; mu: M(MX)=1 -> 1."""
    obj = lambda Xs: ['*']
    fmap = lambda f: (lambda m: '*')
    eta = lambda x: '*'
    mu = lambda mm: '*'
    return obj, fmap, eta, mu

# witness registry: name -> (monad-or-None, P1_nonbranch, P2_comm, P3_affine, note)
# For finite monads we RECHECK comm and affine live; branching is a structural fact.
def live(monad):
    obj, fmap, eta, mu = monad
    comm, _ = is_commutative(obj, fmap, eta, mu, X, Y)
    M1 = affine_size(obj)
    return comm, (M1 == 1)

def main():
    rows = []
    # (T,T,T)
    c, a = live(identity_monad());              rows.append(("Id", True, c, a))
    # (T,T,F)  Maybe = 1+(-)
    c, a = live(exc_writer_monad(['e0'], ['*'], lambda x,y:'*', '*', lambda a,e:e))
    rows.append(("Maybe 1+(-)", True, c, a))
    # (T,F,F)  Writer over noncomm N3
    e,m,u = noncomm3_monoid(); c, a = live(writer_monad(e,m,u))
    rows.append(("Writer N3 (noncomm)", True, c, a))
    # (T,F,F alt) exception 2+(-)
    c, a = live(exc_writer_monad(['e0','e1'], ['*'], lambda x,y:'*', '*', lambda a,e:e))
    rows.append(("Exception 2+(-)", True, c, a))
    # constant-1 monad: non-branching (nullary), affine, commutative
    c, a = live(const1_monad());                rows.append(("const-1  M X=1", True, c, a))
    # (F,T,T) P+ non-empty powerset  (and D)
    c, a = live(powerset_monad(nonempty=True)); rows.append(("P+ (nonempty powerset)", False, c, a))
    c, a = live(distribution_monad(2));         rows.append(("D (distribution)", False, c, a))
    # (F,T,F) Pf powerset with empty
    c, a = live(powerset_monad(nonempty=False));rows.append(("Pf (powerset w/ 0)", False, c, a))
    # (F,F,T) idempotent magma: non-branching=False, comm=False (medial fails), affine=True
    rows.append(("idempotent magma", False, False, True))   # from magma_search + M1=1 argument
    # (F,F,F) free magma
    rows.append(("free magma", False, False, False))        # medial fails; M1 infinite

    print("=" * 74)
    print(f"{'witness':26s} {'P1 nonbr':8s} {'P2 comm':7s} {'P3 aff':6s}  cell")
    print("=" * 74)
    realised = set()
    for name, p1, p2, p3 in rows:
        cell = (p1, p2, p3)
        realised.add(cell)
        t = lambda b: 'T' if b else 'F'
        print(f"{name:26s} {t(p1):^8s} {t(p2):^7s} {t(p3):^6s}  ({t(p1)},{t(p2)},{t(p3)})")

    print("\nRealised cells:", sorted(realised))
    allcells = set((a,b,c) for a in (True,False) for b in (True,False) for c in (True,False))
    print("Missing cells :", sorted(allcells - realised))

    # check each 2x2 face fully populated
    def face(idx1, idx2, label):
        proj = set((cell[idx1], cell[idx2]) for cell in realised)
        full = proj == {(True,True),(True,False),(False,True),(False,False)}
        print(f"  face {label}: {sorted(proj)}  {'FULL (independent)' if full else 'NOT full'}")
        return full
    print("\nPairwise-independence faces:")
    f12 = face(0,1,"P1×P2")
    f13 = face(0,2,"P1×P3")
    f23 = face(1,2,"P2×P3")
    hole_ok = (allcells - realised) == {(True, False, True)}
    print(f"\nAll three faces full: {f12 and f13 and f23}")
    print(f"Unique hole = (T,F,T) [non-branch ∧ ¬comm ∧ affine]: {hole_ok}")
    print("PAIRWISE INDEPENDENT + single structural hole:",
          f12 and f13 and f23 and hole_ok)

if __name__ == "__main__":
    main()
