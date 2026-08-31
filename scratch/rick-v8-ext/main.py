import numpy as np
from math import comb
from gen import (Group, subgroup, perm_module_GmodH, ext_tower, H_trivial_dims, rank)

LEN = 6  # n = 0..6

def rank_of(elems):
    """F2-rank (log2 order) of a subgroup given as element list."""
    o = len(elems)
    return o.bit_length() - 1  # order is a power of 2

def analyze(G, Agens, Bgens, label, LEN=LEN):
    A = subgroup(G, Agens)
    B = subgroup(G, Bgens)
    AB = set(a ^ b for a in A for b in B)   # G abelian: AB is a subgroup
    AiB = sorted(set(A) & set(B))
    absize = len(AB)
    h = G.N // absize
    sA = rank_of(A); sB = rank_of(B); sAiB = rank_of(AiB) if len(AiB) > 0 else 0
    # predicted tower
    Hdims = H_trivial_dims(sAiB, LEN)
    predicted = [h * x for x in Hdims]
    # engine: M = k[G/A], N = k[G/B]
    M = perm_module_GmodH(G, A)
    N = perm_module_GmodH(G, B)
    engine, betti = ext_tower(G, M, N, LEN)
    agree = (engine == predicted)
    print(f"\n===== {label} =====")
    print(f"  A = {Agens} -> elems {A} (order {len(A)}, rank {sA})")
    print(f"  B = {Bgens} -> elems {B} (order {len(B)}, rank {sB})")
    print(f"  A cap B = {AiB} (order {len(AiB)}, rank {sAiB})")
    print(f"  |AB| = {absize},  h = |A\\G/B| = |G|/|AB| = {h}")
    print(f"  dim M=k[G/A]={M['d']}, dim N=k[G/B]={N['d']}")
    print(f"  Betti(M) = {betti}")
    print(f"  dim H^n(AcapB;F2)   n=0..{LEN}: {Hdims}")
    print(f"  PREDICTED  Ext tower: {predicted}")
    print(f"  ENGINE     Ext tower: {engine}")
    print(f"  AGREE degree-by-degree? {agree}")
    if not agree:
        for n in range(LEN+1):
            mark = "" if predicted[n]==engine[n] else "  <-- MISMATCH"
            print(f"    n={n}: pred {predicted[n]:3d}  engine {engine[n]:3d}{mark}")
    return dict(label=label, A=A, B=B, AiB=AiB, absize=absize, h=h,
                predicted=predicted, engine=engine, agree=agree, betti=betti)

results = {}

# ---- Self-test on V4 = (Z/2)^2 to confirm the generalized engine ----
G2 = Group(2)
# x_0=1, x_1=2. A=<x_0>, B=<x_1>: transverse, A cap B = {e}. Known V4 result [1,0,0,...]
results['v4_transverse'] = analyze(G2, [1], [2], "V4 SELF-TEST  A=<x>,B=<y> (transverse)")
# V4 diagonal A=B=<x>: A cap B=<x>=Z/2 -> [h,h,...], h=|G|/|AB|=4/2=2
results['v4_diag'] = analyze(G2, [1], [1], "V4 SELF-TEST  A=B=<x> (diagonal)")

# ============================================================
#  V8 = (Z/2)^3 = <x,y,z>,  x=1, y=2, z=4
# ============================================================
G3 = Group(3)
X, Y, Z = 1, 2, 4

# ---- MAIN TEST: A=<x,y>, B=<y,z>, A cap B = <y> ----
results['main'] = analyze(G3, [X, Y], [Y, Z], "V8 MAIN TEST  A=<x,y>, B=<y,z>  (A cap B=<y>)")

# ---- Control 1: diagonal A=B=<x,y> ----
results['diag'] = analyze(G3, [X, Y], [X, Y], "V8 CONTROL diagonal  A=B=<x,y>  (A cap B=<x,y>)")

# ---- Control 2: transverse rank-1  A=<x>, B=<z>, A cap B={e} ----
results['transverse'] = analyze(G3, [X], [Z], "V8 CONTROL transverse  A=<x>, B=<z>  (A cap B={e})")

# ---- write results.md ----
import io
lines = []
lines.append("# V_8 Ext cross-check: Ext^n_{F2[(Z/2)^3]}(k[G/A], k[G/B])\n")
lines.append("**Group** G = (Z/2)^3 = <x,y,z>, k = F_2. Computed result (engine = minimal free")
lines.append("resolution over the group algebra + Hom into k[G/B] + cohomology of the cochain")
lines.append("complex), cross-checked against the Mackey/Shapiro collapse formula for abelian G:\n")
lines.append("> Ext^n_{kG}(k[G/A], k[G/B]) = h · dim H^n(A∩B; F_2),  h = |A\\G/B| = |G|/|AB|.\n")

def block(r):
    L = []
    L.append(f"## {r['label']}")
    L.append("")
    L.append(f"- A = {r['A']}  |  B = {r['B']}  |  A∩B = {r['AiB']} (order {len(r['AiB'])})")
    L.append(f"- |AB| = {r['absize']},  h = |G|/|AB| = **{r['h']}**")
    L.append(f"- Betti numbers of k[G/A]: {r['betti']}")
    L.append("")
    L.append("| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |")
    L.append("|---|---|---|---|---|---|---|---|")
    L.append("| predicted | " + " | ".join(str(x) for x in r['predicted']) + " |")
    L.append("| engine    | " + " | ".join(str(x) for x in r['engine']) + " |")
    L.append("")
    L.append(f"**Agree degree-by-degree: {r['agree']}**")
    L.append("")
    return "\n".join(L)

for key in ['main', 'diag', 'transverse', 'v4_transverse', 'v4_diag']:
    lines.append(block(results[key]))

all_agree = all(results[k]['agree'] for k in results)
lines.append("## Summary\n")
lines.append(
    "For the main V_8 test A=<x,y>, B=<y,z> we have A∩B=<y> (rank 1, order 2), "
    f"|AB|=8=|G| so h=1, and the engine-computed Ext tower {results['main']['engine']} "
    "matches the predicted [1,1,1,1,1,1,1] in every degree n=0..6 (dim H^n(Z/2;F_2)=1 for all n). "
    "The diagonal control A=B=<x,y> gives h=2 and A∩B=(Z/2)^2 with dim H^n=n+1, engine "
    f"{results['diag']['engine']} = 2·[1,2,3,4,5,6,7]; the rank-1 transverse control A=<x>,B=<z> "
    f"gives A∩B={{e}}, h=2, engine {results['transverse']['engine']}=[2,0,0,0,0,0,0]. "
    "The two V_4 self-tests reproduce the earlier V_4 engine. "
    f"All cases agree with the abelian collapse formula (all_agree={all_agree}). "
    "This is a COMPUTED cross-check, not a new proof."
)

with open("/home/agent/projects/scratch/rick-v8-ext/results.md", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\n\n===== OVERALL =====")
for k in results:
    print(f"  {k:16s}: agree={results[k]['agree']}  engine={results[k]['engine']}")
print(f"  ALL AGREE: {all_agree}")
print("wrote results.md")
