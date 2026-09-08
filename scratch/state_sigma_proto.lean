universe u
variable {S : Type u} (P : S → Type u)

/-- State unit, polymorphic: `η x = fun s => (s, x)` (keep the state). -/
def sEta {A : Type u} (x : A) : Bool → Bool × A := fun s => (s, x)

/-- State multiplication (threading), polymorphic:
`μ mm s = (mm s).2 ((mm s).1)` — read the inner element at the threaded state. -/
def sMu {A : Type u} (mm : Bool → Bool × (Bool → Bool × A)) : Bool → Bool × A :=
  fun s => (mm s).2 ((mm s).1)

/-- Σ-position of `T C` at a State element `m`: a surviving input-state leaf `s`
plus a `P`-position at its value label `(m s).2`. -/
def StateSigma (m : Bool → Bool × S) : Type u := Σ s : Bool, P (m s).2

/-- Σ-position of `T T C` at `mm`: outer state `s₀`, inner state `s'`, position at value. -/
def StateSigma2 (mm : Bool → Bool × (Bool → Bool × S)) : Type u :=
  Σ s₀ : Bool, Σ s' : Bool, P ((mm s₀).2 s').2

/-- Σ-position of `T T T C` at `mmm`: triple state token, position at value. -/
def StateSigma3 (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) : Type u :=
  Σ a : Bool, Σ b : Bool, Σ c : Bool, P (((mmm a).2 b).2 c).2

/-- Unit backward: the codiagonal fold `⟨s, p⟩ ↦ p`. -/
def sEtaBwd (x : S) : StateSigma P (sEta x) → P x := fun z => z.2

/-- Multiplication backward: reindex along the threaded section
`σ(mm, s₀) = (s₀, (mm s₀).1)`: `⟨s₀, p⟩ ↦ ⟨s₀, (mm s₀).1, p⟩`. -/
def sMuBwd (mm : Bool → Bool × (Bool → Bool × S)) :
    StateSigma P (sMu mm) → StateSigma2 P mm :=
  fun z => ⟨z.1, (mm z.1).1, z.2⟩

/-- `η^Σ_{TC}.♯` — outer fold at container `T C`: forget the pure outer leaf of `η_{MS} m`. -/
def etaSigTCState (m : Bool → Bool × S) :
    (Σ _s₀ : Bool, StateSigma P m) → StateSigma P m := fun z => z.2

/-- `T(η^Σ_C).♯` — leafwise inner fold: forget the pure inner leaf of `M(η) m`. -/
def TetaSigState (m : Bool → Bool × S) :
    (Σ s₀ : Bool, Σ _s' : Bool, P (m s₀).2) → StateSigma P m := fun z => ⟨z.1, z.2.2⟩

/-- `μ_{MS} mmm` — collapse the **outer** two `M`-levels (State threading). -/
def sDd (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    Bool → Bool × (Bool → Bool × S) := sMu mmm

/-- `M(μ) mmm` — leafwise collapse of the **inner** two levels. -/
def sEe (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    Bool → Bool × (Bool → Bool × S) := fun s => ((mmm s).1, sMu (mmm s).2)

/-- `μμ mmm` — fully collapsed shared shape (threading is associative). -/
def sDdiag (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    Bool → Bool × S := sMu (sDd mmm)

/-- `μ^Σ_{TC}.♯` — threaded section on the outer leaf: `⟨s₀, s', p⟩ ↦ ⟨s₀, (mmm s₀).1, s', p⟩`. -/
def muSigTCState (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    StateSigma2 P (sDd mmm) → StateSigma3 P mmm :=
  fun z => ⟨z.1, (mmm z.1).1, z.2.1, z.2.2⟩

/-- `T(μ^Σ_C).♯` — leafwise threaded section on the inner two levels:
`⟨a, L, p⟩ ↦ ⟨a, L, ((mmm a).2 L).1, p⟩`. -/
def TmuSigState (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    StateSigma2 P (sEe mmm) → StateSigma3 P mmm :=
  fun z => ⟨z.1, z.2.1, ((mmm z.1).2 z.2.1).1, z.2.2⟩

/-- LEFT UNIT (U1). -/
theorem state_sigma_left_unit (m : Bool → Bool × S) (x : StateSigma P m) :
    etaSigTCState P m (sMuBwd P (sEta m) x) = x := rfl

/-- RIGHT UNIT (U2). -/
theorem state_sigma_right_unit (m : Bool → Bool × S) (x : StateSigma P m) :
    TetaSigState P m (sMuBwd P (fun s => ((m s).1, sEta (m s).2)) x) = x := rfl

/-- ASSOCIATIVITY (A). -/
theorem state_sigma_assoc
    (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) (x : StateSigma P (sDdiag mmm)) :
    muSigTCState P mmm (sMuBwd P (sDd mmm) x) = TmuSigState P mmm (sMuBwd P (sEe mmm) x) := rfl
