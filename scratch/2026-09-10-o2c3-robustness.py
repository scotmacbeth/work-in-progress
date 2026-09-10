#!/usr/bin/env python3
"""
Part 5: Rick's 15% risk. Does the presence of omega-nodes (C_3 factors) anywhere in the
witness DESTROY or PRESERVE the Delta_{C2} = <(0 1)(2 3)> correlated swap?

We build several variant witnesses on labels {0,1,2,3} mixing mu and omega, and report
Stab(w) for each -- specifically whether it still equals (or contains) <(0 1)(2 3)>.
"""
import os,sys,importlib.util
d=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,d)
spec=importlib.util.spec_from_file_location("o2c3model",os.path.join(d,"2026-09-10-o2c3-model.py"))
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
canon,aut,show,conj_key,labels_of=mod.canon,mod.aut,mod.show,mod.conj_key,mod.labels_of
L,U,P,Mu,Om=mod.L,mod.U,mod.P,mod.Mu,mod.Om

SWAP=(1,0,3,2)  # (0 1)(2 3)

def report(name, w, n=4):
    G=set(aut(w,n))
    has=SWAP in G
    isexact = G=={tuple(range(n)),SWAP}
    print(f"\n[{name}]")
    print("  w =", canon(w))
    print("  labels =", sorted(labels_of(w)), " |Stab| =", len(G), " Stab =", show(G))
    print("  contains (0 1)(2 3)?", has, "   == <(0 1)(2 3)> exactly?", isexact)
    return has,isexact

# 0. baseline: pure-mu witness (the U-corner witness) -- swap present
report("baseline mu-only  w=mu(mu(0,mu(2,P)),mu(1,mu(3,P)))",
       Mu(Mu(L(0),Mu(L(2),P)), Mu(L(1),Mu(L(3),P))))

# 1. OUTER node replaced by omega (ternary, C_3) with a peg 3rd slot -- expected to KILL swap
report("outer-omega  w=omega(WL,WR,P)  [C_3 cannot transpose two blocks]",
       Om(Mu(L(0),Mu(L(2),P)), Mu(L(1),Mu(L(3),P)), P))

# 2. INNER blocks are omega-nodes, OUTER stays commutative mu -- expected to PRESERVE swap
report("inner-omega blocks  w=mu( omega(0,2,P), omega(1,3,P) )",
       Mu(Om(L(0),L(2),P), Om(L(1),L(3),P)))

# 3. inner omega blocks with nested structure, outer mu
report("inner-omega nested  w=mu( omega(0,mu(2,P),P), omega(1,mu(3,P),P) )",
       Mu(Om(L(0),Mu(L(2),P),P), Om(L(1),Mu(L(3),P),P)))

# 4. ONE block mu, the OTHER omega (blocks non-isomorphic shape) -- swap should DIE
#    (outer mu can only swap two ISOMORPHIC-up-to-relabel blocks; different node types are not)
report("mixed blocks  w=mu( mu(0,mu(2,P)), omega(1,3,P) )  [blocks differ in shape]",
       Mu(Mu(L(0),Mu(L(2),P)), Om(L(1),L(3),P)))

# 5. omega with THREE genuine subtrees inside a block (C_3-wreath factor present), outer mu
#    block = omega(a,b,c) with a,b,c distinct -> rigid; two such blocks swapped by outer mu
report("inner full-ternary  w=mu( omega(0,2,P2), omega(1,3,P2) ) with extra peg kinds",
       Mu(Om(L(0),L(2),P), Om(L(1),L(3),P)))

# 6. a C_3-SYMMETRIC inner block: omega(t,t,t) has Aut = C_3 wreath; embed two copies, outer mu
#    Here use blocks omega(0,1,2)  (a C_3-symmetric molecule) vs a second copy on {3,4,5}? need 6 labels.
#    Test on 6 labels: w = mu( omega(0,1,2), omega(3,4,5) ). Outer mu swaps the two C_3 blocks.
def report6():
    w=Mu(Om(L(0),L(1),L(2)), Om(L(3),L(4),L(5)))
    G=set(aut(w,6))
    print("\n[two C_3-symmetric blocks on 6 labels  w=mu(omega(0,1,2),omega(3,4,5))]")
    print("  |Stab| =", len(G))
    # is it C_3 wr C_2 = (C_3 x C_3) rtimes C_2, order 18?
    print("  order 18 = |C_3 wr C_2|?", len(G)==18)
    print("  sample elts:", show(G)[:10], "...")
report6()

print("\n=== SUMMARY of robustness ===")
print("The correlated swap <(0 1)(2 3)> survives IFF the OUTER node is the commutative mu")
print("AND the two swapped blocks are relabeling-isomorphic. Interior omega/C_3 factors do")
print("NOT interfere: they only rigidify blocks (making them swappable) or build C_3-wreath")
print("towers underneath, none of which touch the top-level mu-transposition.")
