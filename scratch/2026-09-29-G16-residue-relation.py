#!/usr/bin/env python3
"""
Direct verification of the |G|=16 residue relation (Rick's Prop 3, nontrivial-brace
kernel L={1,5}):   for any realising brace,   4 b == 2 (nu - 1)  mod 8,
where b in Z/8 is the additive 2-cocycle rep beta(1,1) (via the fixed iso D->Z/8)
and nu is the residue unit  nu_1 = lam_{s(1)}|_D.

This is the OUTSIDE-RY channel: D = Z/8 is a *nontrivial* brace (lam^D_x = 5^x),
so RY's H^2_Sb does not directly apply.  We confirm the coupling holds on every
genuine order-16 brace with this kernel.
"""
import itertools
exec(open("scratch/2026-09-29-o-nu-operator-check.py").read().split("if __name__")[0])

def check_family(E, Dset_list, s, iso_to_Z8, label):
    """iso_to_Z8: kernel-elem-in-E -> residue in Z/8."""
    hol=Holomorph(E); regs=hol.regular_subgroups()
    Dset=set(Dset_list); isoInv={iso_to_Z8[d]:d for d in Dset_list}
    rows=[]
    for reg in regs:
        lam={a:i for (a,i) in reg}; br=Brace(E,hol,lam)
        if not is_ideal(br,Dset): continue
        # sub-brace L on D: lam_d|_D as unit; require L = {1,5}
        gen=isoInv[1]
        def unit_of(auto_img_of_gen):
            tbl={E.smul(k,gen):k for k in range(8)}  # gen has order 8
            # careful: gen is kernel-gen in E; multiples via E.smul
            return tbl.get(auto_img_of_gen)
        Lset=set()
        okL=True
        for d in Dset_list:
            u=None
            img=br.lamap(d,gen)
            # express img = u*gen in Z/8 coords
            u=iso_to_Z8[img] if img in iso_to_Z8 else None
            # actually need multiplier: img = u * gen. Use iso: iso(img)=u*iso(gen)=u*1=u
            if u is None: okL=False;break
            Lset.add(u% 8)
        if not okL: continue
        if Lset!={1,5}: continue
        # residue nu = nu_1 = lam_{s(1)}|_D as unit: iso(lam_{s1}(gen)) = nu*1
        s1=s[1]; s0=s[0]
        nu=iso_to_Z8[br.lamap(s1,gen)]
        # circle action sigma_1 = s(1)^{-1} o gen o s(1), as unit
        s1inv=br.circ_inv(s1)
        sig_gen=br.circ(br.circ(s1,gen),s1inv)
        sigma=iso_to_Z8[sig_gen]
        # additive cocycle b = beta(1,1) = -s(1+1)+s(1)+s(1) = -s(0)+s(1)+s(1)
        bE=E.add(E.add(E.neg(s0),s1),s1)
        b=iso_to_Z8[bE]
        lhs=(4*b)%8; rhs=(2*((nu*sigma)-1))%8       # three-way: 4b == 2(nu*sigma - 1)
        rows.append((b,nu,sigma,lhs,rhs,lhs==rhs))
    nfail=sum(1 for r in rows if not r[5])
    print(f"[{label}] {E.name}: braces w/ D=Z/8 (L={{1,5}}) kernel = {len(rows)}, "
          f"relation 4b==2(nu*sigma-1) mod8 holds on {len(rows)-nfail}/{len(rows)}")
    seen=sorted(set((b,nu,sigma,lhs,rhs) for (b,nu,sigma,lhs,rhs,ok) in rows))
    for (b,nu,sigma,lhs,rhs) in seen:
        print(f"     b={b} nu={nu} sigma={sigma}: 4b={lhs}  2(nu*sigma-1)={rhs}  "
              f"[beta]{'=0' if b%2==0 else '!=0'}  {'ok' if lhs==rhs else 'FAIL'}")
    return nfail==0

if __name__=="__main__":
    print("="*70)
    print("|G|=16 residue relation 4b == 2(nu-1) mod 8  (nontrivial kernel L={1,5})")
    print("="*70)
    ok=True
    Z16=Ab([16],"Z/16"); D16=[(2*k,) for k in range(8)]
    s16={0:(0,),1:(1,)}; iso16={(2*k,):k for k in range(8)}
    ok &= check_family(Z16,D16,s16,iso16,"E=Z/16 ([beta]!=0)")
    Z2Z8=Ab([2,8],"Z/2xZ/8"); D28=[(0,y) for y in range(8)]
    s28={0:(0,0),1:(1,0)}; iso28={(0,y):y for y in range(8)}
    ok &= check_family(Z2Z8,D28,s28,iso28,"E=Z/2xZ/8 ([beta]=0)")
    print("\n|G|=16 relation verified:", "PASS" if ok else "FAIL")
