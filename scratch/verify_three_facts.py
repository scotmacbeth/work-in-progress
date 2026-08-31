import numpy as np
rng = np.random.default_rng(0)
p, w, N = 2, 3, 4
results = []

# FACT 1: currying Hom(P,Hom(P,W)) ~= Hom(P (x) P, W); dims p*(p*w)=p^2*w
d_nested = p*(p*w); d_tensor = (p*p)*w
dim_ok = (d_nested == d_tensor)
# explicit currying iso as a permutation/reshape linear map on coordinates
n = d_tensor
M = rng.standard_normal((n, n))  # random element viewed generically
# currying is identity-on-coords up to reshape (i,(j,k)) <-> ((i,j),k): a bijection
perm = np.reshape(np.arange(n), (p, p, w)).transpose(1, 0, 2).ravel()  # a bijection of coords
Curry = np.eye(n)[perm]
inv_ok = np.allclose(Curry @ Curry.T, np.eye(n)) and abs(np.linalg.det(Curry)) > 0.5
results.append(("FACT1", "dims p*(p*w)==p^2*w & currying bijective",
                f"{d_nested}=={d_tensor}, det={np.linalg.det(Curry):.1f}", dim_ok and inv_ok))

# FACT 2: DirectSum series vs single Power
print("N : DirectSum(sum p^n*w, n=0..N) | Power(p^N*w)")
directsums, powers = [], []
for M_ in range(6):
    ds = sum(p**n * w for n in range(M_+1))
    pw = p**M_ * w
    directsums.append(ds); powers.append(pw)
    print(f"{M_} : {ds:6d} | {pw:6d}")
differ = all(ds != pw for ds, pw in zip(directsums[1:], powers[1:]))  # differ for N>=1
results.append(("FACT2", "DirectSum series != single Power (N>=1)",
                f"DS={directsums} vs POW={powers}", differ))

# FACT 3: associativity of composition = matrix product, and concat-then-compose
A1, A2, A3 = (rng.standard_normal((w, w)) for _ in range(3))
left  = (A3 @ A2) @ A1
right = A3 @ (A2 @ A1)
diff_a = np.max(np.abs(left - right))
# depth lists: fold-by-compose of concatenated layer list [A1,A2]++[A3]
def fold(layers):
    out = np.eye(w)
    for L in layers:
        out = L @ out
    return out
concat = fold([A1, A2] + [A3])
triple = A3 @ A2 @ A1
diff_b = np.max(np.abs(concat - triple))
results.append(("FACT3a", "assoc (A3 A2)A1 vs A3(A2 A1) max|diff|", f"{diff_a:.2e}", diff_a < 1e-10))
results.append(("FACT3b", "concat-then-compose vs triple product max|diff|", f"{diff_b:.2e}", diff_b < 1e-10))

print("\nFree-monad tower: T(W)=(+)_n Hom(P^{(x)n},W), n-th summand dim = p^n * w")
print("\n| FACT   | quantity | value | PASS/FAIL |")
print("|--------|----------|-------|-----------|")
for tag, q, v, ok in results:
    print(f"| {tag} | {q} | {v} | {'PASS' if ok else 'FAIL'} |")
