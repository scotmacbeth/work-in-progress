"""
NECESSARY condition for a fibred lifting L^A (aggregator A: Set^E -> Set) of Reader R_E
to be a MONAD lifting: the multiplication backward map
      m_h : A(h o delta)  ->  A(A o hat h)          (natural in h in Set^{ExE})
must EXIST as a natural transformation.  A necessary condition for a natural map F=>G
between polynomial functors is empty-preservation:  for every h,  |F(h)|>0 => |G(h)|>0
(a natural map cannot manufacture an element of an empty set).

We test this over h : ExE -> {empty, nonempty} for E=2, ranging A over polynomial
aggregators  A(Q0,Q1) = coprod_i  Q0^{a_i} Q1^{b_i}  (monomials).  We print which A
pass -- the claim is that ONLY the 'coproduct of single-variable evaluations'
(A = sum of Q0's and Q1's, i.e. every monomial has degree exactly 1) survive, i.e.
the weighted-Sigma family; every monomial of degree>=2 (a genuine product across
leaves, incl. Q0*Q1 and Q0^2) is killed.
"""
import itertools

E = [0,1]
# a monomial is (a,b): exponents of Q0,Q1.  A = list of monomials (a coproduct).
def A_nonempty(A, Qbool):
    # Qbool: tuple (q0,q1) booleans (nonempty?). monomial (a,b) nonempty iff (a==0 or q0) and (b==0 or q1)
    for (a,b) in A:
        if (a==0 or Qbool[0]) and (b==0 or Qbool[1]):
            return True
    return False

def mult_empty_preserving(A):
    # h: ExE -> bool (nonempty?). 4 entries h00,h01,h10,h11.
    for bits in itertools.product([False,True], repeat=4):
        h = {(0,0):bits[0],(0,1):bits[1],(1,0):bits[2],(1,1):bits[3]}
        # source A(h o delta): Q = (h00, h11)
        src = A_nonempty(A, (h[(0,0)], h[(1,1)]))
        # target A(A o hat h): outer Q' over E: Q'(0)=A(h(0,-))=A(h00,h01); Q'(1)=A(h10,h11)
        q0 = A_nonempty(A, (h[(0,0)], h[(0,1)]))
        q1 = A_nonempty(A, (h[(1,0)], h[(1,1)]))
        tgt = A_nonempty(A, (q0, q1))
        if src and not tgt:
            return False, h
    return True, None

def unit_ok(A):
    # unit u: A(Delta V) -> V natural; necessary: A(Delta V) nonempty when V nonempty is fine,
    # but also need a natural map A(V,V)=>V. Empty-preservation: |A(V,V)|>0 => |V|>0 for V empty:
    # V empty: A(empty,empty) must be empty (else map to empty V impossible). A(0,0) nonempty iff monomial (0,0) present.
    # so unit needs NO constant monomial (0,0).  (constant term would break unit.)
    return (0,0) not in A

# enumerate A: nonempty coproducts of monomials with exponents in {0,1,2}, up to 3 monomials, as SETS
monos = [(a,b) for a in range(3) for b in range(3)]
survivors = []
seen=set()
for r in range(1,4):
    for combo in itertools.combinations(monos, r):
        A = frozenset(combo)
        if A in seen: continue
        seen.add(A)
        m_ok,_ = mult_empty_preserving(list(A))
        u_ok = unit_ok(list(A))
        if m_ok and u_ok:
            survivors.append(A)

def classify(A):
    degs = sorted(a+b for (a,b) in A)
    return degs

print("Survivors of NECESSARY (mult empty-preserving + unit no-constant), monomials over {Q0,Q1}, exps<=2:")
for A in sorted(survivors, key=lambda s: (len(s), sorted(s))):
    mon = " + ".join(f"Q0^{a}Q1^{b}" for (a,b) in sorted(A))
    print(f"   {mon:30s}   degrees={classify(A)}")

# Direct spotlight on the canonical cases:
print("\nSpotlight:")
for name,A in [("Sigma  Q0+Q1",[(1,0),(0,1)]),
               ("Prod   Q0*Q1",[(1,1)]),
               ("Pi via Q0*Q1 (=All)",[(1,1)]),
               ("proj   Q0",[(1,0)]),
               ("weighted 2*Q0+Q1",[(1,0),(1,0),(0,1)]),   # note: as a SET this collapses; multiset handled separately
               ("Q0^2",[(2,0)]),
               ("Q0+Q0*Q1",[(1,0),(1,1)])]:
    m_ok,w = mult_empty_preserving(A)
    print(f"   {name:22s} mult-empty-preserving={m_ok}" + (f"  witness h={w}" if not m_ok else ""))
