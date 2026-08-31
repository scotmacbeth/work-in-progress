"""
Faithful Python reimplementation of Orestis's Effects/BiLift.agda  _⨾⇕_  composition,
instantiated for the LIST (nondeterminism) monad, with BOTH his ◇/∃ (Any) lifting
(Effects/Examples/Nondet/BiLift.agda) and, as a CONTROL, the □/∀ (All) lifting that
corresponds to MacBeth's ∏-Mendler T_M.

CONTAINER CONVENTIONS (from the Agda)
-------------------------------------
A container  C = S ◁ P   :  shapes S, positions P : S → Type.
A morphism   C ⇒ D  (D = T ◁ Q)  is  fwd ◁ bwd  where
    fwd = view   : S → T
    bwd = update : {s : S} → Q (view s) → P s

BiLift arrow      C ⇕ D  :=  Lift F C ⇒ CoLift L D
    Lift F C   = S ◁ (F ∘ P)
    CoLift L D = F T ◁ Λ Q
  so an arrow  f = view ◁ update  is
    view   : S → F T
    update : {s} → Λ Q (view s) → F (P s)

COMPOSITION  (verbatim from BiLift.agda, module BI):
    (f ◁ f†) ⨾⇕ (g ◁ g†)
      = join ∘ map g ∘ f
      ◁ join ∘ map f† ∘ Λ-dist ∘ Λ-map g† ∘ Λ-map⁻ ∘ Λ-join

We implement `compose` generically over an F-monad and a Lifting L, exactly threading
those six primitives, then instantiate L = Any (◇) and L = All (□).
"""

from itertools import product as iproduct


# ============================================================================
#  Containers and arrows
# ============================================================================

class Cont:
    """C = S ◁ P.  shapes : list;  pos : dict shape -> list of position-values."""
    def __init__(self, shapes, pos):
        self.shapes = list(shapes)
        self.pos = pos          # dict: shape -> list

    def P(self, s):
        return self.pos[s]


class Arrow:
    """A BiLift arrow C ⇕ D.
       view(s)      -> a list (F T) of D-shapes.
       update(s, w) -> a list (F (P s)) of C-positions at s, given witness w over view(s).
    """
    def __init__(self, C, D, view, update):
        self.C = C
        self.D = D
        self.view = view        # s -> list of D.shapes
        self.update = update    # (s, witness) -> list of C.pos[s]


# ============================================================================
#  F = List monad on Set   (Orestis: Monad₀ List ; return x = [x] ; join = concat)
# ============================================================================

def F_map(fn, xs):
    return [fn(x) for x in xs]

def F_join(xss):
    out = []
    for sub in xss:
        out.extend(sub)
    return out

def F_return(x):
    return [x]


# ============================================================================
#  Lifting interface.  A Lifting supplies, over the List monad:
#     enum(Q, ys)          : enumerate all witnesses of  Λ Q ys   (ys : list of D-shapes)
#     Lam_join(w, xss)     : Λ R (concat xss)          -> Λ (Λ R) xss
#     Lam_map_inv(w,fn,xs) : Λ Q (map fn xs)           -> Λ (Q∘fn) xs
#     Lam_map(w, h, xs)    : Λ P xs -> Λ P' xs   (h : elem, proof -> proof')
#     Lam_dist(w, xs)      : Λ (List∘Q) xs             -> List (Λ Q xs)
#  Witness reps differ per lifting but are threaded opaquely by `compose`.
# ============================================================================

# ---------------------------------------------------------------------------
#  ◇ / ∃  lifting  =  List.Any        (Orestis's  Λⁿ  in Nondet/BiLift.agda)
#      Any P xs  witness  ==  (i, p)   with  0<=i<len(xs),  p a P(xs[i])-value.
#      Λ-map     = LAny.map      : (i,p) -> (i, h xs[i] p)
#      Λ-map⁻    = LAnyₚ.map⁻     : index-preserving, identity on (i,p)
#      Λ-join    = LAnyₚ.concat⁻  : flat index j -> nested (i,(k,r))
#      Λ-dist    : dist (here qs)=map here qs ; dist (there p)=map there (dist p)
#                  i.e. (i, listp) -> [ (i,p) for p in listp ]
# ---------------------------------------------------------------------------
class AnyLifting:
    name = "Any (◇/∃)"

    @staticmethod
    def enum(Qfun, ys):
        # all (j, r), j index into ys, r in Q(ys[j])
        ws = []
        for j, y in enumerate(ys):
            for r in Qfun(y):
                ws.append((j, r))
        return ws

    @staticmethod
    def Lam_join(w, xss):
        # Any R (concat xss) -> Any (Any R) xss     (concat⁻)
        j, r = w
        for i, sub in enumerate(xss):
            if j < len(sub):
                return (i, (j, r))
            j -= len(sub)
        raise IndexError("Lam_join: flat index out of range")

    @staticmethod
    def Lam_map_inv(w, fn, xs):
        # Any Q (map fn xs) -> Any (Q∘fn) xs :  index-preserving identity
        return w

    @staticmethod
    def Lam_map(w, h, xs):
        # Any P xs -> Any P' xs :  apply h at the witnessed element
        i, p = w
        return (i, h(xs[i], p))

    @staticmethod
    def Lam_dist(w, xs):
        # Any (List∘Q) xs -> List (Any Q xs)
        i, listp = w
        return [(i, p) for p in listp]


# ---------------------------------------------------------------------------
#  □ / ∀  lifting  =  List.All        (CONTROL = MacBeth's ∏-Mendler T_M)
#      All P xs  witness  ==  tuple (p_0,...,p_{n-1}),  p_i a P(xs[i])-value.
#      Λ-map     : elementwise
#      Λ-map⁻    : index-preserving identity
#      Λ-join    : regroup flat tuple into nested per xss[i] lengths
#      Λ-dist    : All (List∘Q) xs -> List (All Q xs)  =  CARTESIAN PRODUCT
#                  (this is the ∏ / "product-of-unions" that MacBeth flags as E2′)
# ---------------------------------------------------------------------------
class AllLifting:
    name = "All (□/∀)  [control = ∏-Mendler]"

    @staticmethod
    def enum(Qfun, ys):
        # all tuples with one Q-value per element of ys
        return [tuple(t) for t in iproduct(*[Qfun(y) for y in ys])]

    @staticmethod
    def Lam_join(w, xss):
        # All R (concat xss) -> All (All R) xss : regroup
        out = []
        idx = 0
        for sub in xss:
            out.append(tuple(w[idx:idx + len(sub)]))
            idx += len(sub)
        return tuple(out)

    @staticmethod
    def Lam_map_inv(w, fn, xs):
        return w

    @staticmethod
    def Lam_map(w, h, xs):
        return tuple(h(xs[i], w[i]) for i in range(len(xs)))

    @staticmethod
    def Lam_dist(w, xs):
        # All (List∘Q) xs -> List (All Q xs) : cartesian product of the per-position lists
        return [tuple(t) for t in iproduct(*w)]


# ============================================================================
#  The composition  _⨾⇕_   (generic; six primitives threaded verbatim)
# ============================================================================

def compose(f, g, L):
    """f : C ⇕ D,  g : D ⇕ E,  L a Lifting.  Returns  f ⨾⇕ g : C ⇕ E."""
    C, D, E = f.C, f.D, g.D

    def view_h(s):
        # join ∘ map g.view ∘ f.view
        return F_join(F_map(g.view, f.view(s)))

    def update_h(s, w):
        # w : Λ R (view_h s)
        fs = f.view(s)                          # : F T   (list of D-shapes)
        xss = F_map(g.view, fs)                 # : F (F U)  (list of lists of E-shapes)
        w1 = L.Lam_join(w, xss)                 # Λ (Λ R) xss
        w2 = L.Lam_map_inv(w1, g.view, fs)      # Λ (Λ R ∘ g.view) fs
        # Λ-map g† :  apply g.update at the witnessed D-shape t = fs[i]
        w3 = L.Lam_map(w2, lambda t, inner: g.update(t, inner), fs)   # Λ (F∘Q) fs
        w4 = L.Lam_dist(w3, fs)                 # F (Λ Q fs)  = list of Q-witnesses over fs
        w5 = F_map(lambda wit: f.update(s, wit), w4)                  # F (F (P s))
        return F_join(w5)                       # F (P s)

    return Arrow(C, E, view_h, update_h)


# ============================================================================
#  Arrow equality (extensional; ORDER of the output lists matters, as in Agda refl)
# ============================================================================

def arrows_equal(h1, h2, L):
    C, E = h1.C, h1.D
    Rfun = E.P
    for s in C.shapes:
        v1, v2 = h1.view(s), h2.view(s)
        if v1 != v2:
            return False, ("view", s, v1, v2)
        for w in L.enum(Rfun, v1):
            o1 = h1.update(s, w)
            o2 = h2.update(s, w)
            if o1 != o2:
                return False, ("update", s, w, o1, o2)
    return True, None
