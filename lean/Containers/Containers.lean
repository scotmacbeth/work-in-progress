-- This module serves as the root of the `Containers` library.
-- Import modules here that should be built as part of the library.
import Containers.Basic
import Containers.Cont
import Containers.Sequential
import Containers.Monoidal
import Containers.Dirichlet
import Containers.DirichletComonoid
import Containers.DirichletMonoid
import Containers.TimesMonoid
import Containers.TimesMonoidConverse
import Containers.DirichletMonoidConverse
import Containers.DirichletComonoidConverse
import Containers.DirichletClosed
import Containers.DirichletHomPi
import Containers.FourMonoidal
import Containers.Directed
import Containers.ZappaSzep
import Containers.ProofSearch
import Containers.ProofSearchN
import Containers.DContCat
import Containers.Trust
import Containers.TrustBoundary
import Containers.Comonoid
import Containers.ComonadConverse
import Containers.ComonoidConverse
import Containers.Free
import Containers.FreeUniversal
import Containers.SeqProdDistrib
import Containers.SeqCoprodDistrib
import Containers.TensorCoprodDistrib
import Containers.TimesCoprodDistrib
import Containers.Trajectory
import Containers.TrajectoryComposition
import Containers.Reentrancy
import Containers.MonadComonadTransfer
import Containers.FibredTransfer
import Containers.DualTransfer
import Containers.StateComonad
import Containers.BiKleisli
import Containers.BiKleisliMaybe
import Containers.BiKleisliWriter
import Containers.BranchingObstruction
import Containers.AffineClassification
import Containers.FibredTransfer
import Containers.TMCartesianBoundary
import Containers.ReaderStateOutsidePiMendler
import Containers.ActionLifting
import Containers.SigmaLift
import Containers.ReaderGroupoidLifting
import Containers.StateProductLifting
import Containers.StateComonadTensor
import Containers.EndpointLocality
import Containers.HolonomyWitness
import Containers.EmergentHolonomy
import Containers.Disjointness
-- NOTE: three loose modules remain deliberately orphaned. They are *not* mere
-- import gaps — each conflicts with, or is defective against, the imports above,
-- so pulling any into the root breaks `lake build`. They are alternative or
-- incompatible developments, to be reconciled in a follow-up:
--   * `Containers.Composition` — redefines `Container.I` (hard clash with
--     `Sequential`: "environment already contains 'Containers.Container.I'");
--   * `Containers.Cofunctor`   — redefines `DContMorphism` (hard clash with
--     `DContCat`: "environment already contains 'Containers.DContMorphism.ctorIdx'");
--   * `Containers.CoKleisli`   — genuine compile errors (unsolved strength/counit
--     goals + a syntax error near line 166), not an import gap.
-- (`Trajectory` and `TrajectoryComposition` were previously orphaned; both are now
-- wired in above. `TrajectoryComposition` needed a one-line fix: its `import Trajectory`
-- was corrected to the qualified `import Containers.Trajectory`.)
import Containers.WorkersRetract
import Containers.CompLeftAdjoint
