"""
Semicartesian vs cartesian monoidal structures on FinSet.

Question: is there a monoidal structure on FinSet whose unit is the terminal
object 1 (a one-element set) OTHER than the cartesian product x?

We settle:
  (a) polynomial F with F(1)=empty  ==>  F = empty  (trivial)
  (b) ANY functor E:FinSet->FinSet with E(1)=empty  ==>  E = empty
      (terminal-object argument; brute-force confirmed on small FinSet)
  (main) semicartesian ==> cartesian on Set, via the retract A x B  <=  A@B
      and the size-monoid / e(2,2)=1 candidate obstruction.

Everything below is a *witness generator*, not the proof itself.
"""

from itertools import product, combinations

# ---------------------------------------------------------------------------
# helpers: functions between standard finite sets  n = {0,...,n-1}
# ---------------------------------------------------------------------------
def all_functions(dom, cod):
    """all functions [dom] -> [cod] as tuples f with f[i] in range(cod)."""
    if dom == 0:
        return [()]                      # unique empty function
    if cod == 0:
        return []                        # no function nonempty -> empty
    return [tuple(t) for t in product(range(cod), repeat=dom)]

def compose(g, f):
    """(g o f)(i) = g[f[i]]."""
    return tuple(g[x] for x in f)

def ident(n):
    return tuple(range(n))

# ===========================================================================
# PART (a)   polynomial functor with F(1)=empty is empty
# ===========================================================================
def part_a():
    print("="*70)
    print("(a) Polynomial functor F = Sum_i (-)^{A_i}.")
    print("    F(1) = Sum_i 1^{|A_i|} = Sum_i 1 = |index set I|.")
    print("    So |F(1)| = number of terms.")
    print("    F(1) = empty  <=>  I = empty  <=>  F is identically empty.")
    # numeric sanity: pick some polynomial shapes, evaluate at 1
    for shapes in [[], [0], [2], [0, 3, 1], [5]]:
        f1 = sum(1 for _ in shapes)   # |F(1)| = |I|
        print(f"    exponents {str(shapes):20}  -> |F(1)| = {f1}  "
              f"{'(empty)' if f1==0 else '(nonempty)'}")
    print("    CONFIRMED: only the empty index set gives F(1)=empty.\n")

# ===========================================================================
# PART (b)   ANY functor E with E(1)=empty is empty
# ===========================================================================
def part_b_argument():
    print("="*70)
    print("(b) Terminal-object argument (general, all functors incl. non-poly):")
    print("    1 = {*} is TERMINAL in FinSet: every object A has a unique")
    print("    map !_A : A -> 1.  Apply E:  E(!_A): E(A) -> E(1) = empty.")
    print("    A function whose codomain is empty exists only if its domain")
    print("    is empty.  Hence E(A) = empty for EVERY A.")
    print("    ==> no functor with E(1)=empty and E(2) nonempty exists.\n")

def part_b_bruteforce(maxobj=2, maxEsize=3):
    """
    Brute-force confirmation: search for a functor E on the full subcategory
    of FinSet on objects {0,1,...,maxobj} (ALL functions as morphisms), with
    E(1)=empty, trying to make E(2) nonempty.  Should find NONE.
    """
    print(f"    Brute force on FinSet objects {{0..{maxobj}}}, |E(k)|<= {maxEsize}:")
    objs = list(range(maxobj+1))
    # enumerate object assignments E: obj -> size, with E(1)=0
    from itertools import product as iproduct
    found_nonempty = False
    for esizes in iproduct(range(maxEsize+1), repeat=len(objs)):
        Esz = dict(zip(objs, esizes))
        if Esz[1] != 0:            # force E(1) = empty
            continue
        if all(v == 0 for v in Esz.values()):
            continue               # skip the trivial all-empty (we know it works)
        # try to find a functorial action on ALL morphisms
        if functor_exists(objs, Esz):
            found_nonempty = True
            print(f"      !! FOUND nonempty functor with E sizes {Esz}")
    if not found_nonempty:
        print("      No nonempty functor with E(1)=empty exists. CONFIRMED.\n")

def functor_exists(objs, Esz):
    """
    Does there exist an action on morphisms making E a functor with given
    object sizes?  We only need a quick refutation: if any object A!=... has a
    morphism to an object with E-size 0 that's forced... Actually we just check
    the decisive constraint: for every morphism f:A->B, we need a function
    E(A)->E(B); a function X->Y exists iff (|X|=0 or |Y|>0).  Functor also needs
    to respect id/composition, but existence of SOME action already fails if any
    hom E(A)->E(B) is empty while E(A) nonempty.  We test that necessary cond.
    """
    for A in objs:
        if Esz[A] == 0:
            continue
        for B in objs:
            if all_functions(A, B):           # there is a morphism A->B
                if Esz[B] == 0:               # need E(A)->empty, impossible
                    return False
    # necessary condition passes for these sizes; would need full action check,
    # but for E(1)=0 the map A->1 already kills every nonempty E(A) above.
    return True

# ===========================================================================
# MAIN:  in Set, A x B  is a natural RETRACT of  A@B  (points argument),
#        so A@B ~= (A x B)  DISJOINT-UNION  E(A,B) with E(1,B)=E(A,1)=empty.
#        Fixing B, A |-> E(A,B) is a functor with value empty at A=1,
#        hence empty by (b).  So A@B ~= A x B  ==> cartesian.
# ===========================================================================
def main_argument():
    print("="*70)
    print("MAIN: semicartesian ==> cartesian on Set.")
    print("  Unit I=1 is terminal, so Hom(1,X) ~= X (points).  Given a:1->A,")
    print("  b:1->B define  a@b : 1 ~= 1@1 -> A@B, an element of A@B.")
    print("  mu:(a,b) |-> a@b  is a section of  <pi_A,pi_B>: A@B -> AxB")
    print("  because pi_A(a@b)=a, pi_B(a@b)=b (functoriality + unit iso;")
    print("  NO symmetry needed).  So  AxB  <--(mono)--  A@B  and")
    print("     A@B ~= (AxB)  U  E(A,B),   E(A,B)=A@B minus image(mu).")
    print("  E(1,B): 1@B=B, mu=id, complement empty. So E(1,B)=E(A,1)=empty.")
    print("  The idempotent e=mu o <pi,pi'> is NATURAL & idempotent; Set is")
    print("  idempotent-complete, so A|->E(A,B) is a FUNCTOR with E(1,B)=empty.")
    print("  By (b) it is identically empty.  Hence A@B ~= AxB naturally and")
    print("  <pi_A,pi_B> is iso  ==>  @ is the categorical product  ==> cartesian.")
    print("  VERDICT: NO semicartesian non-cartesian monoidal structure on Set.\n")

# ===========================================================================
# SUPPORTING COMPUTATION 1:  the size-monoid (N, t, unit=1)
#   |A@B| depends only on sizes (functoriality under bijections); associator
#   iso ==> t associative; unit ==> t(m,1)=t(1,n)=n; the empty set forces t(0,0)
#   to be a genuine natural number.  Test candidate additive law m+n-1.
# ===========================================================================
def size_monoid_tests(N=6):
    print("="*70)
    print("Size-monoid necessary conditions on (N, t, unit=1):")
    # cartesian
    def t_mul(m,n): return m*n
    # 'wedge/additive' candidate suggested by unit law
    def t_add(m,n): return m+n-1
    for name,t in [("multiplication m*n", t_mul), ("additive m+n-1", t_add)]:
        unit_ok = all(t(m,1)==m and t(1,n)==n for m in range(N) for n in range(N))
        # associativity over 0..N (values may leave range; check as integers)
        assoc_ok = True; assoc_wit=None
        nonneg_ok = True; neg_wit=None
        for m,n,p in product(range(N),repeat=3):
            if t(t(m,n),p) != t(m,t(n,p)):
                assoc_ok=False; assoc_wit=(m,n,p); break
        for m,n in product(range(N),repeat=2):
            if t(m,n) < 0:
                nonneg_ok=False; neg_wit=(m,n,t(m,n)); break
        print(f"  {name:22}: unit={unit_ok}  assoc={assoc_ok}"
              f"{'' if assoc_ok else f'(fail {assoc_wit})'}  "
              f"valued-in-N={nonneg_ok}"
              f"{'' if nonneg_ok else f' (fail: t{neg_wit[:2]}={neg_wit[2]})'}")
    print("  => additive law m+n-1 is unital & associative on integers but")
    print("     t(0,0) = -1 is NOT a natural number: the EMPTY SET (0@0) kills")
    print("     it. Cartesian's t(0,0)=0 is fine. This shows the 'wedge'")
    print("     candidate is not even realizable at the level of sizes.\n")

# ===========================================================================
# SUPPORTING COMPUTATION 2:  E(A) = 2-element subsets  (binom(A,2))
#   functorial on injections, NOT on all maps.  Explicit witness.
# ===========================================================================
def binom_functor_test():
    print("="*70)
    print("Candidate E(A) = { 2-element subsets of A }  (binom(|A|,2)):")
    print("  E(1)=binom(1,2)=0 (empty), E(2)=binom(2,2)=1 (nonempty) -- looks")
    print("  promising, BUT check functoriality on a NON-injection.")
    # A = {0,1} -> B = {0} constant map f
    A, B = 2, 1
    f = (0, 0)                      # both elements to 0
    subsetsA = list(combinations(range(A), 2))   # [(0,1)]
    print(f"  f: 2->1 constant, f={f}.  2-subsets of A: {subsetsA}")
    for S in subsetsA:
        image = set(f[x] for x in S)
        print(f"    subset {S} maps to image {sorted(image)} of size {len(image)}"
              f" -> {'a 2-subset' if len(image)==2 else 'NOT a 2-subset (collapses)'}")
    print("  => E(f) has no well-defined value: {0,1} collapses to {0}.")
    print("     'binom(-,2)' is a functor on (FinSet, injections) only, NOT on")
    print("     all of FinSet. Consistent with (b): E(1)=empty forces E=empty.")
    print("  (Same failure for: injections-into-A, Sym^2 minus diagonal, etc.)\n")

def e22_candidate():
    print("="*70)
    print("Main-search candidate  |A@B| = |A||B| + e(|A|,|B|),  smallest bump")
    print("  e(2,2)=1 else 0  (so |2@2|=5), with e(m,1)=e(1,n)=0.")
    N = 7
    def t(m,n):
        return m*n + (1 if (m==2 and n==2) else 0)
    unit_ok = all(t(m,1)==m and t(1,n)==n for m in range(N) for n in range(N))
    assoc_ok=True; wit=None
    for m,n,p in product(range(4),repeat=3):
        if t(t(m,n),p) != t(m,t(n,p)):
            assoc_ok=False; wit=(m,n,p,t(t(m,n),p),t(m,t(n,p))); break
    print(f"  unit law: {unit_ok};  size-associativity over 0..3: {assoc_ok}"
          f"{'' if assoc_ok else f'  (breaks at (m,n,p)={wit[:3]}: '+str(wit[3])+' vs '+str(wit[4])+')'}")
    print("  Regardless of the size-monoid: this needs |E(2,2)|=1, i.e. the")
    print("  functor A|->E(A,2) has E(1,2)=empty but E(2,2) nonempty. That")
    print("  functor is FORBIDDEN by (b) (map 2->1 gives E(2,2)->E(1,2)=empty).")
    print("  So NO functorial monoidal @ realizes this size map. Earliest")
    print("  obstruction: FUNCTORIALITY of the tensor, before pentagon.\n")

if __name__ == "__main__":
    part_a()
    part_b_argument()
    part_b_bruteforce(maxobj=3, maxEsize=3)
    main_argument()
    size_monoid_tests(N=6)
    e22_candidate()
    binom_functor_test()
    print("="*70)
    print("FINAL VERDICT: On Set/FinSet, every semicartesian monoidal structure")
    print("is cartesian (= x). No non-cartesian example exists. The linchpin is")
    print("(b): 1 is terminal, so any functor E with E(1)=empty is empty.")
