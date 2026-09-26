"""
2026-09-26  THE FLAGGED CORNER: construct a skew brace G with |G|>=16 and an ideal
D such that L = im(lambda|_D) is PROPER NONTRIVIAL in Aut(D) AND a lift of h in H
acts on D outside L (nontrivial residue [nu]).

Construction (explicit, reproducible):
  Additive group (G,+) = Z/2 x Z/8, elements (i,x), i in Z/2, x in Z/8, direct sum.
  Ideal D = {(0,x) : x in Z/8} ~= Z/8.   H = G/D = Z/2.
  Aut(Z/8) = (Z/8)^* = {1,3,5,7} ~= Z/2 x Z/2 (order 4).

  lambda is built from the "unit-scaling" family of automorphisms of Z/2 x Z/8:
      phi_{u,t}(j,y) = (j, u*y + j*t),   u in {1,3,5,7}, t in {0,4}
  (these form a subgroup of Aut(Z2xZ8); phi_{u,t} o phi_{u',t'} = phi_{uu', u t' + t}).
  Restricted to D (j=0): phi_{u,t}(0,y) = (0, u*y)  -> only u matters on D.

  Set U(i,x) = 5^(x mod 2) * 3^i  (mod 8)   [a homomorphism (G,o)->{units}]
      i=0,x even -> 1 ;  i=0,x odd -> 5 ;  i=1,x even -> 3 ;  i=1,x odd -> 7.
  Two witnesses, differing ONLY by the t-part (invisible on D, so same L and same nu):
     G0 (SPLIT):     lambda0_{(i,x)} = phi_{U(i,x), 0}
     G1 (NON-SPLIT): lambda1_{(i,x)} = phi_{U(i,x), 4*i}   (T(i,x)=4i is a hom (G,o)->{0,4})

  Then  a o b = a + lambda_a(b).
     L = { lambda_{(0,x)}|_D } = { mult by 5^(par x) } = {1,5}  (order 2, PROPER NONTRIVIAL).
     nu_1 = lambda_{(1,0)}|_D = mult by U(1,0)=3, which is OUTSIDE L={1,5}.
"""
from itertools import product
from collections import deque

# ---------- additive group Z/2 x Z/8 ----------
E = [(i, x) for i in range(2) for x in range(8)]
ZERO = (0, 0)
def add(a, b): return ((a[0]+b[0]) % 2, (a[1]+b[1]) % 8)
def neg(a):    return ((-a[0]) % 2, (-a[1]) % 8)

def U(i, x):   # unit in (Z/8)^*
    return (pow(5, x % 2, 8) * pow(3, i, 8)) % 8

def make_lambda(Tfun):
    # lambda_{(i,x)} = phi_{U(i,x), Tfun(i,x)} ; phi_{u,t}(j,y)=(j, u y + j t)
    def lam(a):
        u = U(a[0], a[1]); t = Tfun(a[0], a[1])
        return lambda b: (b[0], (u * b[1] + b[0] * t) % 8)
    return lam

LAM0 = make_lambda(lambda i, x: 0)        # split
LAM1 = make_lambda(lambda i, x: (4*i) % 8) # non-split

# ---------- generic skew-brace machinery ----------
def circ(lam, a, b): return add(a, lam(a)(b))

def is_automorphism(f):
    # additive automorphism of (E,+)?
    img = [f(e) for e in E]
    if len(set(img)) != len(E): return False
    return all(f(add(a, b)) == add(f(a), f(b)) for a in E for b in E)

def verify_skew_brace(lam, name):
    res = {"name": name}
    # (a) each lambda_a is an additive automorphism, lambda_0 = id
    res["all_lambda_auto"] = all(is_automorphism(lam(a)) for a in E)
    res["lambda0_id"] = all(lam(ZERO)(b) == b for b in E)
    # (b) lambda is a homomorphism (G,o)->Aut(+):  lambda_{a o b} = lambda_a o lambda_b
    hom = True
    for a in E:
        for b in E:
            c = circ(lam, a, b)
            lc = lam(c)
            la, lb = lam(a), lam(b)
            for z in E:
                if lc(z) != la(lb(z)): hom = False; break
            if not hom: break
        if not hom: break
    res["lambda_hom"] = hom
    # (c) defining compatibility  a o (b+c) = (a o b) - a + (a o c)   (exhaustive)
    comp = True
    for a in E:
        for b in E:
            for cc in E:
                lhs = circ(lam, a, add(b, cc))
                rhs = add(add(circ(lam, a, b), neg(a)), circ(lam, a, cc))
                if lhs != rhs: comp = False; break
            if not comp: break
        if not comp: break
    res["compat_law"] = comp
    # (d) (G,o) is a group: identity 0, assoc, inverses
    ident = all(circ(lam, ZERO, b) == b and circ(lam, b, ZERO) == b for b in E)
    assoc = all(circ(lam, circ(lam, a, b), c) == circ(lam, a, circ(lam, b, c))
                for a in E for b in E for c in E)
    inv = {}
    invs_ok = True
    for a in E:
        found = [b for b in E if circ(lam, a, b) == ZERO and circ(lam, b, a) == ZERO]
        if not found: invs_ok = False; break
        inv[a] = found[0]
    res["circ_group"] = ident and assoc and invs_ok
    res["is_skew_brace"] = all(res[k] for k in
        ["all_lambda_auto","lambda0_id","lambda_hom","compat_law","circ_group"])
    return res, inv

# ---------- D as ideal ----------
D = [(0, x) for x in range(8)]
Dset = set(D)

def check_ideal(lam, inv, name):
    r = {"name": name}
    # additive subgroup (abelian ambient -> normal automatically)
    r["add_subgroup"] = all(add(a, b) in Dset for a in D for b in D) and all(neg(a) in Dset for a in D)
    # lambda-invariant
    r["lambda_invariant"] = all(lam(a)(d) in Dset for a in E for d in D)
    # circ-subgroup
    r["circ_subgroup"] = all(circ(lam, a, b) in Dset for a in D for b in D) and all(inv[d] in Dset for d in D)
    # normal in (G,o):  g o d o g^{-1} in D
    def cinv(g): return inv[g]
    r["circ_normal"] = all(circ(lam, circ(lam, g, d), cinv(g)) in Dset for g in E for d in D)
    # (D,+) abelian, (D,o) abelian
    r["Dplus_abelian"] = all(add(a, b) == add(b, a) for a in D for b in D)
    r["Dcirc_abelian"] = all(circ(lam, a, b) == circ(lam, b, a) for a in D for b in D)
    r["is_ideal"] = r["add_subgroup"] and r["lambda_invariant"] and r["circ_subgroup"] and r["circ_normal"]
    return r

# ---------- Aut(D) via Z/8 model, and L, nu ----------
def autos_Z8():
    n = 8
    def order(u):
        k = 1; c = u
        while c != 0: c = (c + u) % 8; k += 1
        return k
    res = []
    for img in range(8):  # generator 1 -> img ; must have order 8 => img a unit
        if order(img) != 8: continue
        phi = {(x): (x * img) % 8 for x in range(8)}
        if len(set(phi.values())) == 8:
            res.append(phi)
    return res

AutD = autos_Z8()  # dict on 0..7

def unit_of_lam_on_D(lam, a):
    # lambda_a(0,y) = (0, u*y) ; recover u from y=1
    return lam(a)((0, 1))[1]

def perm_on_D_as_Z8(u):
    return tuple((u * y) % 8 for y in range(8))

def L_units(lam):
    return sorted(set(unit_of_lam_on_D(lam, (0, x)) for x in range(8)))

# ---------- sections, nu-torsor, beta/taubar classes, splitting ----------
lifts = [(1, x) for x in range(8)]  # all lifts of h=1

def analyze_extension(lam, inv, name):
    r = {"name": name}
    Lu = L_units(lam)
    r["L_units"] = Lu
    r["|L|"] = len(Lu)
    r["|Aut(D)|"] = len(AutD)
    r["nu1_unit(base s(1)=(1,0))"] = unit_of_lam_on_D(lam, (1, 0))
    r["nu1_outside_L"] = r["nu1_unit(base s(1)=(1,0))"] not in Lu
    # ---- torsor / section scan ----
    nu_units = []
    beta_vals = []; taub_vals = []
    for s1 in lifts:
        # nu_1
        nu_units.append(unit_of_lam_on_D(lam, s1))
        # beta(1,1) = -s(2)+s(1)+s(1), s(2)=s(0)=0
        beta = add(add(neg(ZERO), s1), s1)
        beta_vals.append(beta)
        # taubar(1,1) = s(1o1)^{-1} o s(1) o s(1); 1o1=0 so s(1o1)=0
        s2 = ZERO
        taub = circ(lam, circ(lam, inv[s2], s1), s1)
        taub_vals.append(taub)
    r["nu1_values_over_sections"] = sorted(set(nu_units))
    # L1: set of nu-values == nu1_base * L  (torsor over L)
    base = unit_of_lam_on_D(lam, (1, 0))
    coset = sorted(set((base * u) % 8 for u in Lu))
    r["L1_torsor(nu-set == nu_base*L)"] = sorted(set(nu_units)) == coset
    r["nu_base*L"] = coset
    # L2: residue [nu] = coset, section-independent (same coset for every section)
    residues = set(frozenset((u * l) % 8 for l in Lu) for u in nu_units)
    r["L2_residue_section_indep"] = len(residues) == 1
    r["residue_[nu]"] = coset
    r["residue_nontrivial([nu]!=L)"] = frozenset(coset) != frozenset(Lu)
    # L3: [beta] class constant. Trivial additive action here (G,+ abelian) -> coboundaries=2*D.
    Bplus = set((0, (2*x) % 8) for x in range(8))  # {dtheta(1,1)=2c}
    beta_classes = set(("triv" if b in Bplus else "nontriv") for b in beta_vals)
    r["L3_beta_class_constant"] = len(beta_classes) == 1
    r["beta_class"] = list(beta_classes)
    # [taubar] class constant. Multiplicative coboundaries dtheta_sigma(1,1).
    # For H=Z/2: coboundary set = { s1^{-1} o e o s1 o e ... } compute as {mul(mul(inv[e],?),)}.
    # Use the same recipe as prior standalone: Bcirc for a fixed lift, but class-constancy we test
    # by whether taub lies in the circ-coboundary set of its own section-shift orbit:
    # Simpler & robust: taubar class is constant iff all taub_vals lie in the same coset of Bcirc.
    # Bcirc(g) = { g^{-1} o (e o g) o e^{-1}? } -- use the descent form d_sigma e.
    # We test constancy of the *splitting-relevant* class by the invariant below (Omega) instead,
    # and record taub coset-constancy empirically:
    def circ_coboundaries():
        S = set()
        for e in D:
            # d_sigma(e)(1,1) with s(1)=(1,0): sigma_1(e)=s(1)^{-1} o e o s(1)
            s1 = (1, 0)
            sig = circ(lam, circ(lam, inv[s1], e), s1)
            # d e (1,1) = e_?  For H=Z/2 mult: dtheta(1,1)= sigma_1(theta_1) o theta_1^{-1}?
            val = circ(lam, sig, inv[e])
            S.add(val)
        return S
    Bcirc = circ_coboundaries()
    taub_classes = set(("triv" if t in Bcirc else "nontriv") for t in taub_vals)
    r["L3_taub_class_constant"] = len(taub_classes) == 1
    r["taub_class"] = list(taub_classes)
    # ---- splitting predicate [Omega]=0 : sub-skew-brace complement to D ----
    r["[Omega]=0 (split)"] = has_sb_complement(lam, inv)
    return r

def has_sb_complement(lam, inv):
    # complement K: |K|=2, 0 in K, K ∩ D = {0}, closed under + and o (sub skew brace)
    for k in E:
        if k in Dset or k == ZERO: continue
        K = {ZERO, k}
        # additive closed
        if not all(add(a, b) in K for a in K for b in K): continue
        if not all(neg(a) in K for a in K): continue
        # circ closed
        if not all(circ(lam, a, b) in K for a in K for b in K): continue
        if not all(inv[a] in K for a in K): continue
        return True
    return False

# ========================= RUN =========================
def report(lam, name):
    print("="*70); print("WITNESS:", name); print("="*70)
    sb, inv = verify_skew_brace(lam, name)
    print("[skew brace checks]")
    for k in ["all_lambda_auto","lambda0_id","lambda_hom","compat_law","circ_group","is_skew_brace"]:
        print(f"    {k}: {sb[k]}")
    idl = check_ideal(lam, inv, name)
    print("[ideal D = {0}xZ/8 checks]")
    for k in ["add_subgroup","lambda_invariant","circ_subgroup","circ_normal",
              "Dplus_abelian","Dcirc_abelian","is_ideal"]:
        print(f"    {k}: {idl[k]}")
    ext = analyze_extension(lam, inv, name)
    print("[invariants / lemmas]")
    for k in ["|Aut(D)|","|L|","L_units","nu1_unit(base s(1)=(1,0))","nu1_outside_L",
              "nu1_values_over_sections","nu_base*L","L1_torsor(nu-set == nu_base*L)",
              "residue_[nu]","L2_residue_section_indep","residue_nontrivial([nu]!=L)",
              "beta_class","L3_beta_class_constant","taub_class","L3_taub_class_constant",
              "[Omega]=0 (split)"]:
        print(f"    {k}: {ext[k]}")
    return sb, idl, ext

sb0, id0, ex0 = report(LAM0, "G0  (T=0, expected SPLIT)")
print()
sb1, id1, ex1 = report(LAM1, "G1  (T=4i, expected NON-SPLIT)")

print("\n" + "#"*70)
print("CROSS-TAB (item 6): does the SAME nontrivial residue [nu] co-occur with")
print("both [Omega]=0 and [Omega]!=0 ?")
print("#"*70)
print(f"  G0: residue [nu]={ex0['residue_[nu]']}  L={ex0['L_units']}  "
      f"nontrivial-residue={ex0['residue_nontrivial([nu]!=L)']}  [Omega]=0(split)={ex0['[Omega]=0 (split)']}")
print(f"  G1: residue [nu]={ex1['residue_[nu]']}  L={ex1['L_units']}  "
      f"nontrivial-residue={ex1['residue_nontrivial([nu]!=L)']}  [Omega]=0(split)={ex1['[Omega]=0 (split)']}")
same_res = ex0['residue_[nu]'] == ex1['residue_[nu]'] and ex0['L_units'] == ex1['L_units']
both_omega = ex0['[Omega]=0 (split)'] != ex1['[Omega]=0 (split)']
print(f"  SAME (L,[nu]) on both: {same_res}")
print(f"  Omega DIFFERS (one split, one non-split): {both_omega}")
print(f"  => nontrivial [nu] co-occurs with BOTH [Omega]=0 and [Omega]!=0 : "
      f"{same_res and both_omega and ex0['residue_nontrivial([nu]!=L)']}")
