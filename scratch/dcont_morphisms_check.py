"""
Verify the morphism-level dictionary DCont <-> Cat.

A small category is given concretely. We enumerate, between two categories C, C':
  (A) functors  C -> C'
  (B) cofunctors C => C'
  (C) directed-container morphisms (f, f#) with conditions (M0),(M1),(M2)

Claim: #(C) == #(B)   (container morphisms ARE cofunctors)
       #(C) != #(B)? no -- equal; and in general != #(A) (functors).

Category representation:
  objs : list of hashable objects
  homs : dict (a,b) -> list of morphism-ids (morphisms a->b)
  ident: dict a -> morphism-id  (the identity at a)
  comp : dict (g, f) -> g∘f  where f: a->b, g: b->c, result a->c
  dom, cod : dict morphism-id -> object
Morphism-ids are globally unique labels (strings).
"""
from itertools import product

# ---------- category builders ----------
def make_category(objs, arrows, comp_table):
    """arrows: list of (id, dom, cod). comp_table: dict (g,f)->h (g after f).
       Identities must be present in arrows and comp_table."""
    dom = {a:d for (a,d,c) in arrows}
    cod = {a:c for (a,d,c) in arrows}
    homs = {(x,y):[] for x in objs for y in objs}
    for (a,d,c) in arrows:
        homs[(d,c)].append(a)
    ident = {}
    for x in objs:
        # identity = the unique e in hom(x,x) with e∘f=f and g∘e=g
        cands = homs[(x,x)]
        for e in cands:
            ok=True
            for f in [a for (a,_,_) in arrows if cod[a]==x]:
                if comp_table[(e,f)]!=f: ok=False;break
            if ok:
                for g in [a for (a,_,_) in arrows if dom[a]==x]:
                    if comp_table[(g,e)]!=g: ok=False;break
            if ok: ident[x]=e;break
        assert x in ident, f"no identity at {x}"
    return dict(objs=objs, arrows=[a for (a,_,_) in arrows],
               dom=dom, cod=cod, homs=homs, ident=ident, comp=comp_table)

def out_arrows(C, x):
    return [a for a in C['arrows'] if C['dom'][a]==x]

# ---------- concrete categories ----------
def cat_terminal():
    return make_category(['*'], [('i*','*','*')], {('i*','i*'):'i*'})

def cat_2():   # 0 --u--> 1
    objs=[0,1]
    arrows=[('i0',0,0),('i1',1,1),('u',0,1)]
    comp={('i0','i0'):'i0',('i1','i1'):'i1',('i1','u'):'u',('u','i0'):'u'}
    return make_category(objs,arrows,comp)

def cat_3chain(): # 0->1->2 (poset), arrows i0,i1,i2,a:0->1,b:1->2,c:0->2
    objs=[0,1,2]
    arrows=[('i0',0,0),('i1',1,1),('i2',2,2),('a',0,1),('b',1,2),('c',0,2)]
    comp={}
    ids={0:'i0',1:'i1',2:'i2'}
    # build composition for a poset: g∘f determined by endpoints
    arr={('i0'):(0,0),'i1':(1,1),'i2':(2,2),'a':(0,1),'b':(1,2),'c':(0,2)}
    def arrow_between(x,y):
        for k,(d,c) in arr.items():
            if d==x and c==y: return k
        return None
    for g,(gd,gc) in arr.items():
        for f,(fd,fc) in arr.items():
            if fc==gd:
                comp[(g,f)]=arrow_between(fd,gc)
    return make_category(objs,arrows,comp)

def cat_Zmod(n): # one object monoid Z/n
    objs=['*']
    arrows=[(f'm{k}','*','*') for k in range(n)]
    comp={}
    for i in range(n):
        for j in range(n):
            comp[(f'm{i}',f'm{j}')]=f'm{(i+j)%n}'
    return make_category(objs,arrows,comp)

def cat_mon_idem(): # one object, 2 elements: e=id, t with t∘t=t  (idempotent monoid {1,t})
    objs=['*']
    arrows=[('e','*','*'),('t','*','*')]
    comp={('e','e'):'e',('e','t'):'t',('t','e'):'t',('t','t'):'t'}
    return make_category(objs,arrows,comp)

# ---------- (A) functors ----------
def functors(C, D):
    res=[]
    for fobj in product(D['objs'], repeat=len(C['objs'])):
        omap=dict(zip(C['objs'],fobj))
        # enumerate arrow maps respecting dom/cod, ident, comp
        # for each non-identity arrow choose image in hom(omap[dom],omap[cod])
        arrs=C['arrows']
        choices=[]
        slots=[]
        for a in arrs:
            tgt=D['homs'][(omap[C['dom'][a]],omap[C['cod'][a]])]
            slots.append(a); choices.append(tgt)
        for pick in product(*choices):
            fmap=dict(zip(slots,pick))
            # identities -> identities
            if any(fmap[C['ident'][x]]!=D['ident'][omap[x]] for x in C['objs']): continue
            # composition
            ok=True
            for g in arrs:
                for f in arrs:
                    if C['cod'][f]==C['dom'][g]:
                        if fmap[C['comp'][(g,f)]]!=D['comp'][(fmap[g],fmap[f])]:
                            ok=False;break
                if not ok:break
            if ok: res.append((omap,fmap))
    return res

# ---------- (B) cofunctors C => D ----------
def cofunctors(C, D):
    """phi0: ob C -> ob D ; lift: for c in C, for h out of phi0(c) in D,
       choose lift in arrows-out-of-c in C with phi0(cod lift)=cod(h).
       laws: lift(id)=id ; lift(h'∘h)=lift(h')∘lift(h)."""
    res=[]
    for fobj in product(D['objs'], repeat=len(C['objs'])):
        phi0=dict(zip(C['objs'],fobj))
        # for each object c, lift is a function from out_arrows(D,phi0(c)) to out_arrows(C,c)
        # with cod constraint. Enumerate per object then check global laws.
        objs=C['objs']
        per_obj_options=[]
        for c in objs:
            Hout=out_arrows(D, phi0[c])
            # for each h, candidate lifts l with phi0(cod_C l)=cod_D h
            cand_lists=[]
            feasible=True
            for h in Hout:
                cd=D['cod'][h]
                cands=[l for l in out_arrows(C,c) if phi0[C['cod'][l]]==cd]
                if not cands: feasible=False;break
                cand_lists.append((h,cands))
            if not feasible:
                per_obj_options.append(None);break
            # enumerate all lift-functions for this object
            opts=[]
            for pick in product(*[cl for (_,cl) in cand_lists]):
                liftmap=dict(zip([h for (h,_) in cand_lists],pick))
                # unit law local: lift(id_{phi0 c})=id_c
                if liftmap[D['ident'][phi0[c]]]!=C['ident'][c]: continue
                opts.append(liftmap)
            per_obj_options.append(opts)
        if any(o is None for o in per_obj_options): continue
        if any(len(o)==0 for o in per_obj_options): continue
        # global: combine and check comult law
        for combo in product(*per_obj_options):
            lift={c:combo[i] for i,c in enumerate(objs)}
            # comult: for c, h: phi0c->d, h':d->d'',  lift_c(h'∘h)=lift_{c'}(h')∘lift_c(h),
            # c' = cod_C(lift_c(h))
            ok=True
            for c in objs:
                for h in out_arrows(D,phi0[c]):
                    d=D['cod'][h]
                    lh=lift[c][h]; cprime=C['cod'][lh]
                    for hp in out_arrows(D,d):
                        comp_hp_h=D['comp'][(hp,h)]
                        lhs=lift[c][comp_hp_h]
                        rhs=C['comp'][(lift[cprime][hp], lh)]
                        if lhs!=rhs: ok=False;break
                    if not ok:break
                if not ok:break
            if ok: res.append((phi0,lift))
    return res

# ---------- (C) directed-container morphisms ----------
# directed container of a category: S=objs, P(s)=out_arrows(s), o(s)=ident,
# s↓p = cod(p), p⊕q = comp(q,p).  A DCont morphism (f,f#):
#   f: S->S', f#_s: P'(f s)->P(s) with (M0),(M1),(M2).
def dcont_morphisms(C, D):
    """Enumerate (f, fsharp) directly from container data; check M0,M1,M2."""
    def P(cat,s): return out_arrows(cat,s)
    def down(cat,s,p): return cat['cod'][p]      # s↓p
    def root(cat,s): return cat['ident'][s]
    def oplus(cat,p,q): return cat['comp'][(q,p)]  # p⊕q = q∘p
    res=[]
    Sobj=C['objs']
    for fobj in product(D['objs'],repeat=len(Sobj)):
        f=dict(zip(Sobj,fobj))
        # f#_s : P'(f s) -> P(s).  enumerate functions, prune by M0,M1 early
        per=[]
        ok_all=True
        for s in Sobj:
            srcs=P(D,f[s])           # P'(f s)
            tgt=P(C,s)               # P(s)
            cand_lists=[]
            feas=True
            for h in srcs:
                # M0: f(s ↓ f#(h)) = (f s) ↓' h
                cd = down(D,f[s],h)
                cands=[p for p in tgt if f[ down(C,s,p) ]==cd ]
                if not cands: feas=False;break
                cand_lists.append((h,cands))
            if not feas: ok_all=False;break
            opts=[]
            for pick in product(*[cl for (_,cl) in cand_lists]):
                fs=dict(zip([h for(h,_) in cand_lists],pick))
                # M1: f#_s(o'(f s)) = o(s)
                if fs[root(D,f[s])]!=root(C,s): continue
                opts.append(fs)
            per.append(opts)
        if not ok_all: continue
        if any(len(o)==0 for o in per): continue
        for combo in product(*per):
            fsharp={s:combo[i] for i,s in enumerate(Sobj)}
            # M2: f#_s(h ⊕' k) = f#_s(h) ⊕ f#_{s↓f#_s(h)}(k)
            good=True
            for s in Sobj:
                for h in P(D,f[s]):
                    p=fsharp[s][h]                 # ∈ P(s)
                    sdp=down(C,s,p)                # s↓p
                    for k in P(D, down(D,f[s],h)): # k ∈ P'(f s ↓' h)=P'(f(s↓p))
                        lhs=fsharp[s][ oplus(D,h,k) ]
                        rhs=oplus(C, p, fsharp[sdp][k])
                        if lhs!=rhs: good=False;break
                    if not good:break
                if not good:break
            if good: res.append((f,fsharp))
    return res

# ---------- run ----------
cats={'1':cat_terminal(),'2':cat_2(),'3':cat_3chain(),
      'Z2':cat_Zmod(2),'Z3':cat_Zmod(3),'Mt':cat_mon_idem()}
names=list(cats)
print(f"{'C->D':8} {'#Fun':>5} {'#Cofun':>7} {'#DCont':>7}  cofun==dcont  cofun!=fun?")
allpass=True
for a in names:
    for b in names:
        C,D=cats[a],cats[b]
        nf=len(functors(C,D)); nc=len(cofunctors(C,D)); nd=len(dcont_morphisms(C,D))
        match = (nc==nd)
        allpass = allpass and match
        flag = '' if match else '   <<< MISMATCH'
        diff = '' if nc==nf else '  (differs)'
        print(f"{a+'->'+b:8} {nf:5d} {nc:7d} {nd:7d}      {str(match):5}      {nc!=nf}{diff}{flag}")
print()
print("ALL cofunctor==dcont :", allpass)

# ---------- (D) covariant-position (op-variance) morphisms = should equal FUNCTORS ----------
# f: S->S' on objects, phi_s: P(s)->P'(f s) COVARIANT, with:
#   (N0) f(s↓p) = (f s) ↓' phi_s(p)
#   (N1) phi_s(o(s)) = o'(f s)
#   (N2) phi_s(p⊕q) = phi_s(p) ⊕' phi_{s↓p}(q)
def covariant_pos_morphisms(C, D):
    def P(cat,s): return out_arrows(cat,s)
    def down(cat,s,p): return cat['cod'][p]
    def root(cat,s): return cat['ident'][s]
    def oplus(cat,p,q): return cat['comp'][(q,p)]
    res=[]; Sobj=C['objs']
    for fobj in product(D['objs'],repeat=len(Sobj)):
        f=dict(zip(Sobj,fobj)); per=[]; ok_all=True
        for s in Sobj:
            cand_lists=[]; feas=True
            for p in P(C,s):
                cd=f[down(C,s,p)]
                cands=[h for h in P(D,f[s]) if down(D,f[s],h)==cd]
                if not cands: feas=False;break
                cand_lists.append((p,cands))
            if not feas: ok_all=False;break
            opts=[]
            for pick in product(*[cl for(_,cl) in cand_lists]):
                ph=dict(zip([p for(p,_) in cand_lists],pick))
                if ph[root(C,s)]!=root(D,f[s]): continue
                opts.append(ph)
            per.append(opts)
        if not ok_all or any(len(o)==0 for o in per): continue
        for combo in product(*per):
            phi={s:combo[i] for i,s in enumerate(Sobj)}; good=True
            for s in Sobj:
                for p in P(C,s):
                    sdp=down(C,s,p)
                    for q in P(C,sdp):
                        lhs=phi[s][oplus(C,p,q)]
                        rhs=oplus(D, phi[s][p], phi[sdp][q])
                        if lhs!=rhs: good=False;break
                    if not good:break
                if not good:break
            if good: res.append((f,phi))
    return res

print("\n--- checking: covariant-position morphisms == functors ? ---")
allf=True
for a in names:
    for b in names:
        nf=len(functors(cats[a],cats[b])); ncov=len(covariant_pos_morphisms(cats[a],cats[b]))
        if nf!=ncov:
            allf=False; print(f"  {a}->{b}: FUN {nf} != COV {ncov}  <<<")
print("ALL covariant-position == functors :", allf)

# ---------- (E) TALLY: number of pairs with #functors != #cofunctors ----------
total_pairs=0; neq=0
for a in names:
    for b in names:
        total_pairs+=1
        nf=len(functors(cats[a],cats[b])); nc=len(cofunctors(cats[a],cats[b]))
        if nf!=nc: neq+=1
print(f"\nTotal ordered pairs tested: {total_pairs}")
print(f"Pairs with (#functors != #cofunctors): {neq}")
