"""
Polynomial functors in several variables, natural transformations (via container
morphisms), and the Reader-lifting monad-law checker.

An aggregator L : Set^E -> Set is a polynomial functor in |E| variables:
    L(B) = sum_{s in shapes} prod_{v in E} (B_v)^{arity_s(v)}
represented by `shapes` = list of arity-tuples (one nat per variable).

A Reader-lifting of Reader = y^E is determined by such an L together with:
    eps_A : L(<A>) -> A                        (unit; <A> = constant family)
    del_D : L(b|->D(b,b)) -> L(b|->L(c|->D(b,c)))   (mult; D : E^2 -> Set)
both natural, satisfying the monad laws.  We enumerate natural eps, del as
container morphisms and check the monad laws on small test containers.
"""
from itertools import product

# ---------- generic polynomial functor over an ordered variable list ----------
class Poly:
    def __init__(self, nvars, shapes):
        # shapes: list of tuples of length nvars (arities, nonneg ints)
        self.n = nvars
        self.shapes = [tuple(s) for s in shapes]

    def eval(self, sizes):
        # sizes: tuple length n of finite-set sizes. Returns list of elements.
        # element = (shape_idx, tuple over vars of tuple(length arity) of ints in range(size_v))
        elts = []
        for si, ar in enumerate(self.shapes):
            # per var, all functions [arity]->range(size)
            per_var_choices = []
            for v in range(self.n):
                per_var_choices.append(list(product(range(sizes[v]), repeat=ar[v])))
            for combo in product(*per_var_choices):
                elts.append((si, tuple(combo)))
        return elts

    def act(self, elt, backmaps):
        # backmaps: tuple over vars of a function (list) mapping old range->new range
        si, combo = elt
        newcombo = tuple(tuple(backmaps[v][x] for x in combo[v]) for v in range(self.n))
        return (si, newcombo)

# ---------- substitution: L over vars Vin, theta[v] a Poly over Vout ----------
def subst(L, thetas, nvars_out):
    # thetas: list length L.n of Poly (each over nvars_out variables)
    new_shapes = []
    for ar in L.shapes:
        # for each variable v of L and each of ar[v] copies, choose a shape of thetas[v]
        copy_choice_lists = []
        copy_which_var = []
        for v in range(L.n):
            for _ in range(ar[v]):
                copy_choice_lists.append(range(len(thetas[v].shapes)))
                copy_which_var.append(v)
        for choices in product(*copy_choice_lists):
            out_ar = [0]*nvars_out
            for ci, sh_idx in enumerate(choices):
                v = copy_which_var[ci]
                sub_ar = thetas[v].shapes[sh_idx]
                for w in range(nvars_out):
                    out_ar[w] += sub_ar[w]
            new_shapes.append(tuple(out_ar))
    return Poly(nvars_out, new_shapes)

# monomial y_j over nvars variables: arity 1 in variable j, 0 else
def mono(nvars, j):
    ar = [0]*nvars; ar[j] = 1
    return Poly(nvars, [tuple(ar)])

# ---------- natural transformations between two polys over same vars ----------
# A nat transf P => Q : for each P-shape s (arity a), choose Q-shape t (arity b),
#   and per var v a backward map [b(v)] -> [a(v)].  Represented as list over
#   P-shapes of (t_index, tuple over vars of tuple(length b(v)) entries in range(a(v))).
def enum_nats(P, Q):
    per_shape_options = []
    for a in P.shapes:
        opts = []
        for ti, b in enumerate(Q.shapes):
            # per var v: all functions [b(v)]->range(a(v))
            pv = []
            ok = True
            for v in range(P.n):
                fns = list(product(range(a[v]), repeat=b[v]))
                if not fns:   # a[v]=0 but b[v]>0 : no map
                    ok = False; break
                pv.append(fns)
            if not ok:
                continue
            for combo in product(*pv):
                opts.append((ti, combo))
        per_shape_options.append(opts)
    # a nat transf = a choice per P-shape
    for choice in product(*per_shape_options):
        yield list(choice)

def nat_act(P, Q, nat, elt):
    # apply nat transf (P=>Q) to an element of P(fam) -> element of Q(fam)
    si, combo = elt
    ti, backs = nat[si]
    newcombo = tuple(tuple(combo[v][backs[v][k]] for k in range(len(backs[v])))
                     for v in range(P.n))
    return (ti, newcombo)

# ---------- the aggregator L, and derived polys ----------
def make_A2_B2(L, e):
    # variables of E^2 ordered as b*e+c  (b outer, c inner)
    n2 = e*e
    # A2 = subst(L, b |-> y_{(b,b)})     [over E^2]
    thetasA = [mono(n2, b*e+b) for b in range(e)]
    A2 = subst(L, thetasA, n2)
    # B2 = subst(L, b |-> subst(L, c|-> y_{(b,c)}))
    thetasB = []
    for b in range(e):
        inner = subst(L, [mono(n2, b*e+c) for c in range(e)], n2)
        thetasB.append(inner)
    B2 = subst(L, thetasB, n2)
    return A2, B2

def make_C1(L, e):
    # C1 = subst(L, e|-> y_*) over 1 var ; eps: C1 => y_*
    return subst(L, [mono(1,0) for _ in range(e)], 1)
