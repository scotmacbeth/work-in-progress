# Verify the structural facts used in the classification, on finite sets, for ∨_S and ×.
from itertools import product

def vee(s):  # A ∨_s B = A + B + A×S×B ; represent sets as ints (cardinalities) for card checks,
    return lambda a,b: a + b + a*s*b
def times(a,b): return a*b

def Rcompose_check(op, unit, N=5, S=None):
    # Check (X⋆C)⋆B  vs  X⋆(C⋆B)  cardinalities  [associativity => R_B∘R_C = R_{C⋆B}]
    ok=True
    for X,C,B in product(range(N),repeat=3):
        if op(op(X,C),B)!=op(X,op(C,B)): ok=False;print("assoc fail",X,C,B)
    return ok

def unit_check(op,unit,N=6):
    return all(op(X,unit)==X and op(unit,X)==X for X in range(N))

# ∨_s: unit 0
for s in range(4):
    op=vee(s)
    assert unit_check(op,0), f"vee_{s} unit"
    assert Rcompose_check(op,0), f"vee_{s} assoc"
    # affine / arity<=1 : X⋆B = B + (1+sB)*X  linear in X
    for B in range(5):
        DB=1+s*B; CB=B
        assert all(op(X,B)==CB+DB*X for X in range(6)), f"vee_{s} affine B={B}"
print("∨_s (s=0..3): unit, associativity, affine form  X⋆B=B+(1+sB)X  ALL PASS")

# ×: unit 1
assert unit_check(times,1) and Rcompose_check(times,1)
for B in range(5):
    assert all(times(X,B)==0+B*X for X in range(6)), "times affine"
print("× : unit, associativity, affine form X⋆B=B·X (C_B=0,D_B=B) PASS")

# symmetry identity B + D_B X = X + D_X B  for vee_s  (D_B=1+sB)
for s in range(4):
    for X,B in product(range(6),repeat=2):
        assert B+(1+s*B)*X == X+(1+s*X)*B
print("symmetry identity  B+D_B·X = X+D_X·B  (D_B=1+sB) PASS for s=0..3")

# D_{B⋆C} = D_B · D_C  (D monoidal hom), unit D_∅=1
for s in range(4):
    op=vee(s); D=lambda B:1+s*B
    for B,C in product(range(6),repeat=2):
        assert D(op(B,C))==D(B)*D(C), (s,B,C)
    assert D(0)==1
print("D_{B⋆C}=D_B·D_C and D_∅=1  PASS for s=0..3")
print("\nALL RECONSTRUCTION CHECKS PASS")
