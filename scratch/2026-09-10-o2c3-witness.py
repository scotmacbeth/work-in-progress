#!/usr/bin/env python3
"""
Part 2-3: the decisive witness Stab(w) and the escape decision for O_{2,C3}.

Witness (from the fully-symmetric U-corner proof, transplanted to O_{2,C3}):
   w = mu( mu(V0, mu(V2, E')),  mu(V1, mu(V3, E')) )
V0..V3 = distinct labels 0,1,2,3 ; E' = rigid peg P (inner unit as an outer rigid leaf).

EXPECT: the two blocks W_L=mu(0,mu(2,P)), W_R=mu(1,mu(3,P)) are rigid & non-isomorphic;
the outer COMMUTATIVE mu swaps them => Stab(w) = <(0 1)(2 3)> = Delta_{C2}, order 2.

ESCAPE test: is <(0 1)(2 3)> the Aut of any single O_{2,C3}-tree on <=4 labels?
If NOT (and it is support-indecomposable, order 2, not a Young product), it is an ESCAPE
=> M o M !~ [r] o M for all polynomial r  => NECESSITY HOLDS.
"""
import itertools
from importlib import import_module
m = import_module("2026-09-10-o2c3-model".replace("-","_")) if False else None
# import by exec since filename has dashes
import runpy, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# load model module via importlib from file
import importlib.util
spec=importlib.util.spec_from_file_location("o2c3model",
      os.path.join(os.path.dirname(os.path.abspath(__file__)),"2026-09-10-o2c3-model.py"))
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
from types import SimpleNamespace
canon,aut,relabel,show,conj_key=mod.canon,mod.aut,mod.relabel,mod.show,mod.conj_key
L,U,P,Mu,Om=mod.L,mod.U,mod.P,mod.Mu,mod.Om
labels_of=mod.labels_of

def finest_split(G,n):
    supp=[i for i in range(n) if any(g[i]!=i for g in G)]
    if not supp: return []
    parent={i:i for i in supp}
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]];x=parent[x]
        return x
    for g in G:
        moved=[i for i in supp if g[i]!=i]
        for a in moved[1:]: parent[find(a)]=find(moved[0])
    blocks={}
    for i in supp: blocks.setdefault(find(i),[]).append(i)
    facs=[]
    for blk in blocks.values():
        blk=sorted(blk); idx={b:i for i,b in enumerate(blk)}
        fac=set()
        for g in G:
            if all(g[i]==i for i in range(n) if i not in blk):
                fac.add(tuple(idx[g[b]] for b in blk))
        facs.append((tuple(blk),fac))
    return facs

def perm_iso_key(fac,s):
    best=None
    for r in itertools.permutations(range(s)):
        conj=set()
        for p in fac:
            np=[0]*s
            for i in range(s): np[r[i]]=r[p[i]]
            conj.add(tuple(np))
        key=tuple(sorted(conj))
        if best is None or key<best: best=key
    return (s,best)

# ---- build the witness ----
WL = Mu(L(0), Mu(L(2), P))
WR = Mu(L(1), Mu(L(3), P))
w  = Mu(WL, WR)
print("witness w =", canon(w))
print("labels(w) =", sorted(labels_of(w)))

G = aut(w, 4)
print("\nStab(w) <= S_4  (brute force over all 24 perms):")
print("  order =", len(G))
print("  elements =", show(G))
print("  conj_key =", conj_key(G,4))

target = tuple(sorted([tuple(range(4)), (1,0,3,2)]))  # {id, (0 1)(2 3)}
Gset=set(G)
print("  Stab(w) == <(0 1)(2 3)> exactly?", Gset==set(target))

# ---- is Stab(w) support-indecomposable? ----
fs = finest_split(G,4)
print("\nfinest support split of Stab(w):", [(blk,sorted(fac)) for blk,fac in fs])
print("  support-indecomposable (single block on all 4 labels)?", len(fs)==1 and len(fs[0][0])==4)

# ---- ESCAPE: is <(0 1)(2 3)> = Aut of any single O_{2,C3}-tree on <=4 labels? ----
def inner_trees(S, depth):
    """all canon single O_{2,C3}-trees using EXACTLY label-set S (may also contain pegs P
       is NOT included here -- single trees for the 𝒴 test use only leaves+units+nodes)."""
    S=frozenset(S)
    memo={}
    def gen(S,depth):
        key=(S,depth)
        if key in memo: return memo[key]
        res=set()
        if len(S)==1:
            (a,)=tuple(S); res.add(L(a))
        if depth>0 and len(S)>=1:
            items=sorted(S)
            # mu node: 2 ordered slots
            for assign in itertools.product(range(2),repeat=len(items)):
                slots=[[],[]]
                for it,sl in zip(items,assign): slots[sl].append(it)
                choice=[]
                ok=True
                for sl in slots:
                    if not sl: choice.append([U])
                    else:
                        sub=gen(frozenset(sl),depth-1)
                        if not sub: ok=False;break
                        choice.append(list(sub))
                if not ok: continue
                for a0 in choice[0]:
                    for a1 in choice[1]:
                        res.add(canon(Mu(a0,a1)))
            # omega node: 3 ordered slots
            for assign in itertools.product(range(3),repeat=len(items)):
                slots=[[],[],[]]
                for it,sl in zip(items,assign): slots[sl].append(it)
                choice=[]; ok=True
                for sl in slots:
                    if not sl: choice.append([U])
                    else:
                        sub=gen(frozenset(sl),depth-1)
                        if not sub: ok=False;break
                        choice.append(list(sub))
                if not ok: continue
                for a0 in choice[0]:
                    for a1 in choice[1]:
                        for a2 in choice[2]:
                            res.add(canon(Om(a0,a1,a2)))
        memo[key]=res
        return res
    return gen(S,depth)

print("\n=== ESCAPE test: single-tree Auts on 4 labels ===")
target_key = perm_iso_key({(1,0,3,2),(0,1,2,3)}, 4)  # <(0 1)(2 3)> as perm-iso class on 4 pts
print("target perm-iso key (order-2 correlated double-swap):", target_key)

singles4 = inner_trees(frozenset(range(4)), depth=4)
print("  # single O_{2,C3}-trees on 4 labels (depth<=4):", len(singles4))
found=False
matches=[]
single_keys=set()
for t in singles4:
    G4=aut(t,4)
    k=perm_iso_key(set(G4),4)
    single_keys.add(k)
    if set(G4)==set(target):
        found=True; matches.append(t)
print("  any single tree with Aut == <(0 1)(2 3)> EXACTLY?", found)
print("  is target perm-iso class realised by ANY single-tree Aut on 4 pts?",
      target_key in single_keys)

# Also confirm the Young-product argument: any single-tree Aut containing (0 1)(2 3) also
# contains a transposition (order>=4), so a group of order exactly 2 gen by (0 1)(2 3) is not
# a Young product either.
print("\nsingle-tree Aut ORDERS on 4 labels that contain the element (0 1)(2 3):")
for t in singles4:
    G4=set(aut(t,4))
    if (1,0,3,2) in G4:
        print("   order", len(G4), "tree", canon(t), "elts", show(G4))
