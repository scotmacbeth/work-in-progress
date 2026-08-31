"""
Comp 1 (Part 1): reproduce the BW cochain complex of Sk_C with natural system D,
confirm H^2 = Z/2 with generator (0,1) supported on ([s2],[p]), and confirm the
ISOTROPY RESTRICTION i_x* : C^n_BW(Sk_C;D) -> C^n(Aut(x);D(x)) is identically 0
because every Aut_{Sk_C}(x) is trivial.

Sk_C: objects Sup(0), Wk(1), Rt(2).
 generators: [p]:Sup->Wk, [q]:Sup->Rt, [s]:Wk->Rt, [s2]:Wk->Rt.
 composites: [s][p]=[q], [s2][p]=[q].
 D(Sup)=Z/2, D(Wk)=D(Rt)=0. All restriction maps vanish (no generator targets Sup).

BW cochains (normalized, on chains of NON-identity composable morphisms), coefficient of an
n-chain (f_n,...,f_1) lives in D(dom f_1). Only chains with dom f_1 = Sup contribute.
"""

# morphisms of Sk_C as (name, dom, cod). Objects 0=Sup,1=Wk,2=Rt.
MORPH = {
    'p':  (0,1),
    'q':  (0,2),
    's':  (1,2),
    's2': (1,2),
}
# composition table on non-identity composable pairs (g,f) meaning g o f, keyed (g,f)->name
COMP = {
    ('s','p'):  'q',
    ('s2','p'): 'q',
}
DOM = {m: MORPH[m][0] for m in MORPH}
COD = {m: MORPH[m][1] for m in MORPH}
# D on objects: Z/2 at Sup, 0 elsewhere.  coefficient group order (1 = trivial group {0})
Dord = {0: 2, 1: 1, 2: 1}

def contributes_chain(chain):
    """chain = tuple of morphism names (f_n,...,f_1) read right-to-left composable;
       here store as list [f1,f2,...] with f_{k+1} o f_k defined. Return dom f_1 group order."""
    # composability: cod f_k == dom f_{k+1}
    for k in range(len(chain)-1):
        if COD[chain[k]] != DOM[chain[k+1]]:
            return None
    return Dord[DOM[chain[0]]]

# Enumerate chains of length 1 and 2 that carry a NONtrivial coefficient group (order 2 => Sup-sourced)
def chains_of_len(n):
    out = []
    def rec(prefix):
        if len(prefix) == n:
            if contributes_chain(prefix) == 2:
                out.append(tuple(prefix))
            return
        for m in MORPH:
            if not prefix or COD[prefix[-1]] == DOM[m]:
                rec(prefix + [m])
    rec([])
    return out

C1 = chains_of_len(1)
C2 = chains_of_len(2)
C3 = chains_of_len(3)
print("C^1 nontrivial-coeff chains (Sup-sourced):", C1)      # expect [('p',),('q',)]
print("C^2 nontrivial-coeff chains:", C2)                    # expect [('p','s'),('p','s2')]
print("C^3 nontrivial-coeff chains:", C3)                    # expect []
print("dim C^1 =", len(C1), " dim C^2 =", len(C2), " dim C^3 =", len(C3))

# delta^1 : C^1 -> C^2 (all restriction maps phi=0 since targets of generators are Wk/Rt with D=0)
# (delta^1 h)(g,f) = phi_g(h(g)) - h(gf) + h(f).  Here g:Wk->Rt so phi_g:D(Rt)=0->D(Wk)=0 => term 0
#   but h(g) also lives in D(dom g)=D(Wk)=0. The surviving terms: -h(gf)+h(f) with dom f = Sup.
# chain stored [f, g] meaning g o f. f is first.
import itertools
F2 = [0,1]
def apply_delta1(h):
    # h: dict over C1 chains -> Z/2 ; here C1 relevant = ('p',),('q',)
    out = {}
    for ch in C2:
        f, g = ch[0], ch[1]           # g o f
        gf = COMP[(g,f)]              # composite name
        # phi_g(h((g,))): dom of the length-1 chain (g,) is Wk => group 0 => contributes 0, skip
        val = (- (h.get((gf,),0)) + h.get((f,),0)) % 2
        out[ch] = val
    return out

# Build B^2 = image of delta^1
B2 = set()
for a in F2:
    for b in F2:
        h = {('p',): a, ('q',): b}
        d = apply_delta1(h)
        B2.add(tuple(d[ch] for ch in C2))
print("C^2 coordinates order:", C2)
print("B^2 (image delta^1):", sorted(B2))     # expect {(0,0),(1,1)}
# Z^2 = ker delta^2 = C^2 (since C^3=0)
Z2 = set(itertools.product(F2, repeat=len(C2)))
# H^2 = Z2/B2
# quotient size
cosets = set()
for z in Z2:
    rep = min(tuple((z[i]^b[i]) for i in range(len(z))) for b in B2)
    cosets.add(rep)
print("|H^2| =", len(cosets), " reps:", sorted(cosets))

# omega_T = (0, epsilon):  coordinate on ([s],[p]) is 0, on ([s2],[p]) is epsilon.
for eps in (0,1):
    omega = {('p','s'):0, ('p','s2'):eps}
    vec = tuple(omega[ch] for ch in C2)
    # class rep
    rep = min(tuple((vec[i]^b[i]) for i in range(len(vec))) for b in B2)
    print(f"eps={eps}: omega_T={vec}  ->  class rep {rep}  ({'ZERO' if rep==(0,0) else 'GENERATOR'})")

print("\n--- ISOTROPY RESTRICTION ---")
# Aut_{Sk_C}(x): endomorphisms of x that are invertible. Endos of each object:
endos = {x: [m for m in MORPH if DOM[m]==x and COD[m]==x] for x in (0,1,2)}
print("non-identity endomorphisms per object:", endos)  # expect all empty
for x in (0,1,2):
    autx = ['id'] + endos[x]      # only identity
    print(f"Aut(Sup/Wk/Rt = {x}) = {autx}  => trivial group; H^{{>=1}}(Aut(x);D(x)) = 0")
# The restriction of ANY BW n-cochain to loops at x uses only chains of ENDO-morphisms at x.
# For n=2 those are pairs of endos at x; none exist => restricted cochain identically 0.
loop_chains_2 = [ch for ch in C2 if DOM[ch[0]]==COD[ch[0]]==DOM[ch[1]]==COD[ch[1]]]
print("length-2 endo-loop chains (support of any isotropy-restricted 2-cochain):", loop_chains_2)
print("=> i_x* omega_T = 0 at COCHAIN level for every x, and for EVERY class in H^2. QED Part 1.")
