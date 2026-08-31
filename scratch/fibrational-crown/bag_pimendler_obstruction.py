"""
WHY Bag is NOT Pi-Mendler:  P*(m) = prod_{b in lv(m)} P(x_b) must be a
WELL-DEFINED function of the Bag-element m.  A repeated element {a,a} has a
leaf-swap sigma that FIXES the labelling (both labels = a) but permutes the
two factors of P(a) x P(a).  If |P(a)|>=2 this swap is non-trivial, so P*
is NOT invariant under the symmetry that Bag quotients by  ->  P* is not a
function on Bag(X).  Pf has NO such label-fixing leaf automorphism (a set's
elements are distinct), so its Pi-lift IS well-defined.
"""
from itertools import permutations

def label_fixing_leaf_autos(leaves_labels):
    """leaves_labels: list of labels, one per leaf position.
       return non-identity permutations of positions that FIX the label map."""
    n=len(leaves_labels); idperm=tuple(range(n)); out=[]
    for p in permutations(range(n)):
        if p==idperm: continue
        if all(leaves_labels[p[i]]==leaves_labels[i] for i in range(n)):
            out.append(p)
    return out

# Bag element {a,a}: two leaves, both labelled 'a'
print("Bag {a,a} : label-fixing non-triv leaf autos =",
      label_fixing_leaf_autos(['a','a']),
      "  -> product P(a)xP(a) NOT swap-invariant when |P(a)|>=2  => P* ill-defined")

# Bag element {a,b}: distinct labels -> none (this case is fine, like Pf)
print("Bag {a,b} : label-fixing non-triv leaf autos =",
      label_fixing_leaf_autos(['a','b']))

# Pf element {a,b}: leaves are the distinct set-elements, labels distinct -> none
print("Pf  {a,b} : label-fixing non-triv leaf autos =",
      label_fixing_leaf_autos(['a','b']),
      "  -> Pf Pi-lift well-defined")

# List element [a,a]: FREE positions (ordered) -> the two 'a' leaves are
# distinguishable positions 0,1; Bag identifies them, List does NOT.
print("List [a,a]: positions are FREE/ordered (0,1 distinguishable) -> container, no quotient")

print()
print("CONCLUSION: Bag has a label-fixing leaf automorphism (multiplicity symmetry),")
print("so the Pi-cointerpretation product is ill-defined => Bag NOT in Pi-Mendler.")
print("Within Pi-Mendler (label-rigid leaves): cartFun => no such symmetry => polynomial.")
