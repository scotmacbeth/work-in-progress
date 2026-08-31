import itertools
# ⋆ : A * B := A ⊔ B ⊔ {•}  with • present iff A≠∅ and B≠∅.  Unit = ∅.
# Elements encoded: ('l',a), ('r',b), ('m',). Sets are tuples of small ints.

def star(A,B):
    els=[('l',a) for a in A]+[('r',b) for b in B]
    if len(A)>0 and len(B)>0: els.append(('m',))
    return tuple(els)

def star_map(f,g,A,B):
    # f:A->A' dict, g:B->B' dict ; returns dict on star(A,B)->star(A',B')
    d={}
    for e in star(A,B):
        if e[0]=='l': d[e]=('l',f[e[1]])
        elif e[0]=='r': d[e]=('r',g[e[1]])
        else: d[e]=('m',)   # both nonempty in source => both nonempty in target
    return d

def idmap(A): return {a:a for a in A}

# ---- functoriality checks ----
def all_maps(A,B):
    A=list(A);B=list(B)
    if len(A)==0: yield {}; return
    for vals in itertools.product(B,repeat=len(A)):
        yield {A[i]:vals[i] for i in range(len(A))}

sets=[(),(0,),(0,1),(0,1,2)]
ok=True
for A in sets:
 for B in sets:
  # identity
  d=star_map(idmap(A),idmap(B),A,B)
  if any(d[e]!=e for e in d): ok=False;print("id fail",A,B)
# composition (single-variable, fix B=(0,1)); check f2∘f1 in first slot
B=(0,1)
for A in sets:
 for Ap in sets:
  for App in sets:
   for f1 in all_maps(A,Ap):
    for f2 in all_maps(Ap,App):
     comp={a:f2[f1[a]] for a in A}
     lhs=star_map(f2,idmap(B),Ap,B)   # star(f2,id): star(Ap,B)->star(App,B)
     rhs=star_map(f1,idmap(B),A,B)    # star(f1,id): star(A,B)->star(Ap,B)
     both={e:lhs[rhs[e]] for e in star(A,B)}
     direct=star_map(comp,idmap(B),A,B)
     if both!=direct: ok=False;print("comp fail",A,Ap,App)
print("functoriality (id + first-slot composition):", ok)

# ---- try to build an associator satisfying pentagon ----
# (A*B)*C  and  A*(B*C).  Non-extra elements have a forced identity matching.
# The two "extra-ish" points on each side must be matched; enumerate the matching
# and require: (i) natural in A,B,C, (ii) bijection, (iii) pentagon, (iv) triangle.
def elems_L(A,B,C):  # (A*B)*C
    return star(star(A,B),C)
def elems_R(A,B,C):  # A*(B*C)
    return star(A,star(B,C))

def forced_part(A,B,C):
    # returns dict for the non-ambiguous elements from L->R, and lists of ambiguous src/tgt
    L=elems_L(A,B,C); R=elems_R(A,B,C)
    d={}; amb_src=[]; 
    for e in L:
        # e in (A*B)*C : ('l',p) p in A*B, or ('r',c), or ('m',)
        if e[0]=='l':
            p=e[1]
            if p[0]=='l': d[e]=('l',p[1])            # a in A
            elif p[0]=='r': d[e]=('r',('l',p[1]))    # b in B
            else: amb_src.append(e)                  # •_{AB}
        elif e[0]=='r':
            d[e]=('r',('r',e[1]))                    # c in C
        else:
            amb_src.append(e)                        # •_{(AB)C}
    tgt_used=set(d.values())
    amb_tgt=[r for r in R if r not in tgt_used]
    return d,amb_src,amb_tgt,L,R

# choose a matching rule for ambiguous points. Represent an "extra point" canonically
# by the SET of leaf-indices (from {0,1,2} = A,B,C) that are 'active below it'.
# •_{AB}: active {A,B}; •_{(AB)C}: active {A,B,C} if AB nonempty else {?}. This is the
# heuristic the negative control warns about. We'll just brute-force: for each (A,B,C)
# with all nonempty (the only case with 2 ambiguous points), try both matchings, and
# require the GLOBAL choice to be natural + satisfy pentagon. To keep it finite, we
# derive the matching from a rule keyed by "how many of A,B,C are nonempty and a tag".
# Simpler: define associator by a fixed structural rule and TEST pentagon; try all rules.

def make_assoc(rule):
    # rule: function(A,B,C, amb_src_tags)-> matching. We implement two candidate rules.
    def alpha(A,B,C):
        d,amb_src,amb_tgt,L,R=forced_part(A,B,C)
        # tag each ambiguous src/tgt
        # src: ('l',('m',)) = "AB-point"; ('m',) = "top point"
        # tgt: ('r',('m',)) = "BC-point"; ('m',) = "top point"
        d=dict(d)
        if len(amb_src)!=len(amb_tgt):
            raise Exception("count mismatch "+str((A,B,C,amb_src,amb_tgt)))
        if len(amb_src)==0: pass
        elif len(amb_src)==1:
            d[amb_src[0]]=amb_tgt[0]
        else:
            # two points each side. src tags:
            src_tag={e:('AB' if e==('l',('m',)) else 'TOP') for e in amb_src}
            tgt_tag={r:('BC' if r==('r',('m',)) else 'TOP') for r in amb_tgt}
            # rule maps src tag-> tgt tag
            for e in amb_src:
                want=rule[src_tag[e]]
                # find tgt with that tag
                cand=[r for r in amb_tgt if tgt_tag[r]==want]
                d[e]=cand[0]
        return d,L,R
    return alpha

def is_bijection(d,L,R):
    return set(d.keys())==set(L) and set(d.values())==set(R) and len(set(d.values()))==len(R)

# pentagon: for A,B,C,D, two paths ((AB)C)D -> A(B(CD)).
def star3(A,B,C): return star(star(A,B),C)
def check_all(rule,sets):
    alpha=make_assoc(rule)
    # bijection + naturality quick check
    for A in sets:
     for B in sets:
      for C in sets:
       d,L,R=alpha(A,B,C)
       if not is_bijection(d,L,R): return ("not bijection",A,B,C)
    # pentagon on all quadruples of nonempty small sets (extras only appear then)
    S=[s for s in sets]
    for A in S:
     for B in S:
      for C in S:
       for D in S:
        # objects
        AB=star(A,B); CD=star(C,D); BC=star(B,C)
        # path1: ((A*B)*C)*D --α_{AB,C,D}--> (A*B)*(C*D) --α_{A,B,C*D}--> A*(B*(C*D))
        aBCD1,_,_=alpha(AB,C,D)                 # ((AB)C)D -> (AB)(CD)
        aBCD2,_,_=alpha(A,B,CD)                 # (AB)(CD) -> A(B(CD))
        # path2: ((A*B)*C)*D --α_{A,B,C}*D--> (A*(B*C))*D --α_{A,BC,D}--> A*((B*C)*D) --α_{A,B*C? }
        # standard pentagon: ((AB)C)D
        #  path top: α_{A,B,C} ⋆ id_D : ((AB)C)D -> (A(BC))D ; then α_{A,BC,D}: -> A((BC)D); then id_A ⋆ α_{B,C,D}: -> A(B(CD))
        aABC,_,_=alpha(A,B,C)                   # (AB)C -> A(BC)
        f_star_D=star_map(aABC, idmap(D), star(AB,C), D)   # ((AB)C)D -> (A(BC))D
        aA_BC_D,_,_=alpha(A,BC,D)               # (A(BC))D -> A((BC)D)
        aBCD,_,_=alpha(B,C,D)                   # (BC)D -> B(CD)
        id_star_a=star_map(idmap(A), aBCD, A, star(BC,D)) # A((BC)D) -> A(B(CD))
        # compose path2
        # careful: domain is ((A*B)*C)*D = star( star(star(A,B),C), D )
        dom=star(star(star(A,B),C),D)
        p2={}
        for e in dom:
            x=f_star_D[e]; x=aA_BC_D[x]; x=id_star_a[x]; p2[e]=x
        # compose path1
        p1={}
        for e in dom:
            x=aBCD1[e]; x=aBCD2[x]; p1[e]=x
        if p1!=p2:
            return ("PENTAGON FAILS",A,B,C,D)
    return ("ALL OK",)

sets2=[(),(0,),(0,1)]
for rule in [{'AB':'BC','TOP':'TOP'},{'AB':'TOP','TOP':'BC'}]:
    print("rule",rule,"->",check_all(rule,sets2))
