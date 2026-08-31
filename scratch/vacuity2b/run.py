from bifun import *

BIFS = [COPROD(), JOIN(), VEE(nset(1)), VEE(nset(2)), SUPPORT()]

def show(x):
    return str(x)

print("#"*74)
print("# TASK 1 -- Lemma D    eta_{1*B}(u) ?= (1*eta_B)(u) on BALANCED u")
print("#"*74)
t1summary = {}
for bif in BIFS:
    print(f"\n=== {bif.name}")
    allpass = True
    for Bn, balanced, results in task1(bif):
        nb = len(balanced)
        viol = [u for (u, ok) in results if not ok]
        allpass = allpass and (len(viol) == 0)
        print(f"  B={Bn}: {nb} balanced u; violate Lemma D: {len(viol)}")
        for u, ok in results:
            print(f"       u={show(u):30s}  Lemma-D holds={ok}")
    t1summary[bif.name] = "PASS" if allpass else "FAIL"

print("\n" + "#"*74)
print("# TASK 2 -- star'  (pullback preservation)  phi_C bijection?")
print("#"*74)
t2summary = {}
for bif in BIFS:
    print(f"\n=== {bif.name}")
    res = task2(bif)
    allpass = True
    for Cn, d in res.items():
        allpass = allpass and d['phi_bij']
        print(f"  C={Cn}: phi_bij={d['phi_bij']} (inj={d['phi_inj']},onto={d['phi_onto']}) "
              f"| equiv-form={d['equiv']} agree={d['agree']} "
              f"fiber={d['fiber_size']} imC={d['imC_size']}")
    t2summary[bif.name] = "PASS" if allpass else "FAIL"
print("\n  DIRICHLET: unit=1 not empty; EMPTY-formulas N/A (skipped, see Task 3).")

print("\n" + "#"*74)
print("# TASK 3 -- WIDE star'   canonical E*C -> WPB bijection?")
print("#"*74)
t3summary = {}
for bif in BIFS:
    print(f"\n=== {bif.name}")
    res = task3(bif)
    allpass = True
    for (jn, Cn), d in res.items():
        allpass = allpass and d['passes']
        print(f"  |J|={jn} C={Cn}: PASS={d['passes']}  wpb={d['wpb_size']} "
              f"img={d['img_size']} img<=wpb={d['img_subset']} onto={d['onto']}")
    t3summary[bif.name] = "PASS" if allpass else "FAIL"
# Dirichlet wide (general form): unit 1, E*C = empty
print("\n=== DIRICHLET (general/wide form, unit=1)")
d = DIRICHLET()
for jn in (2, 3):
    for Cn, C in [("1", ONE), ("2", TWO)]:
        pts = [point(j) for j in nset(jn)]
        starOC = d.star(ONE, C)
        acts = [d.smap(a, idmap(C), ONE, C) for a in pts]
        WPB = {u for u in starOC if all(acts[i][u] == acts[0][u] for i in range(len(acts)))}
        starEC = d.star(EMPTY, C)               # empty x C = empty
        canon = d.smap(EMPTYMAP, idmap(C), EMPTY, C)
        img = set(canon.values())
        passes = (img == WPB)
        print(f"  |J|={jn} C={Cn}: E*C size={len(starEC)} WPB size={len(WPB)} PASS={passes}")
t3summary["DIRICHLET"] = "PASS(vacuous)"

print("\n" + "#"*74)
print("# TASK 4 -- eta_C mono & split")
print("#"*74)
for bif in BIFS:
    print(f"\n=== {bif.name}")
    for Cn, d in task4(bif).items():
        print(f"  C={Cn}: eta injective={d['inj']}  retraction exists={d['has_retraction']}")

print("\n" + "#"*74)
print("# TASK 2 CRUX -- exhaustive VALID functors G=F(1,-) + natural eta")
print("#   Does star' EVER fail for a valid unital-row functor (assoc irrelevant)?")
print("#"*74)
tested, fails = search_star_prime(3)
print(f"\n  valid (G,eta) configs tested: {tested}")
print(f"  star'_2 FAILURES found: {len(fails)}")
if fails:
    # smallest witness = min |W|, then |V|
    fails.sort(key=lambda d: (len(d['W']), len(d['V']), d['fiber']))
    w = fails[0]
    print("\n  SMALLEST WITNESS (a valid functor G with G(EMPTY)={*}):")
    print(f"    V=G(1)={w['V']}   W=G(2)={w['W']}   functor basepoint v0={w['v0']}")
    print(f"    G(i0)=p : {w['p']}")
    print(f"    G(i1)=q : {w['q']}")
    print(f"    G(!_2)=r: {w['r']}")
    print(f"    G(swap)=sigma: {w['sigma']}")
    print(f"    eta basepoint p_L=eta_1(*)={w['pL']}")
    print(f"    eta_2 image = {w['im_eta2']}   fiber r^-1(p_L) = {w['fiber']}")
    print(f"    eta_2 injective = {w['eta_inj']}")
    print(f"    => extra element(s) in fiber not hit by eta: "
          f"{sorted(set(w['fiber'])-set(w['im_eta2']))}")

print("\n" + "#"*74)
print("# SUMMARY TABLE")
print("#"*74)
names = [b.name.split()[0] for b in BIFS] + ["DIRICHLET"]
print(f"{'bifunctor':12s} {'Task1':8s} {'Task2':8s} {'Task3':14s}")
for b in BIFS:
    k = b.name
    short = k.split()[0]
    print(f"{short:12s} {t1summary[k]:8s} {t2summary[k]:8s} {t3summary[k]:14s}")
print(f"{'DIRICHLET':12s} {'N/A':8s} {'N/A':8s} {t3summary['DIRICHLET']:14s}")
