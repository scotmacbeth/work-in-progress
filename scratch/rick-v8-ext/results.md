# V_8 Ext cross-check: Ext^n_{F2[(Z/2)^3]}(k[G/A], k[G/B])

**Group** G = (Z/2)^3 = <x,y,z>, k = F_2. Computed result (engine = minimal free
resolution over the group algebra + Hom into k[G/B] + cohomology of the cochain
complex), cross-checked against the Mackey/Shapiro collapse formula for abelian G:

> Ext^n_{kG}(k[G/A], k[G/B]) = h · dim H^n(A∩B; F_2),  h = |A\G/B| = |G|/|AB|.

## V8 MAIN TEST  A=<x,y>, B=<y,z>  (A cap B=<y>)

- A = [0, 1, 2, 3]  |  B = [0, 2, 4, 6]  |  A∩B = [0, 2] (order 2)
- |AB| = 8,  h = |G|/|AB| = **1**
- Betti numbers of k[G/A]: [1, 2, 3, 4, 5, 6, 7, 8]

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| predicted | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| engine    | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Agree degree-by-degree: True**

## V8 CONTROL diagonal  A=B=<x,y>  (A cap B=<x,y>)

- A = [0, 1, 2, 3]  |  B = [0, 1, 2, 3]  |  A∩B = [0, 1, 2, 3] (order 4)
- |AB| = 4,  h = |G|/|AB| = **2**
- Betti numbers of k[G/A]: [1, 2, 3, 4, 5, 6, 7, 8]

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| predicted | 2 | 4 | 6 | 8 | 10 | 12 | 14 |
| engine    | 2 | 4 | 6 | 8 | 10 | 12 | 14 |

**Agree degree-by-degree: True**

## V8 CONTROL transverse  A=<x>, B=<z>  (A cap B={e})

- A = [0, 1]  |  B = [0, 4]  |  A∩B = [0] (order 1)
- |AB| = 4,  h = |G|/|AB| = **2**
- Betti numbers of k[G/A]: [1, 1, 1, 1, 1, 1, 1, 1]

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| predicted | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| engine    | 2 | 0 | 0 | 0 | 0 | 0 | 0 |

**Agree degree-by-degree: True**

## V4 SELF-TEST  A=<x>,B=<y> (transverse)

- A = [0, 1]  |  B = [0, 2]  |  A∩B = [0] (order 1)
- |AB| = 4,  h = |G|/|AB| = **1**
- Betti numbers of k[G/A]: [1, 1, 1, 1, 1, 1, 1, 1]

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| predicted | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| engine    | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

**Agree degree-by-degree: True**

## V4 SELF-TEST  A=B=<x> (diagonal)

- A = [0, 1]  |  B = [0, 1]  |  A∩B = [0, 1] (order 2)
- |AB| = 2,  h = |G|/|AB| = **2**
- Betti numbers of k[G/A]: [1, 1, 1, 1, 1, 1, 1, 1]

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| predicted | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| engine    | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

**Agree degree-by-degree: True**

## Summary

For the main V_8 test A=<x,y>, B=<y,z> we have A∩B=<y> (rank 1, order 2), |AB|=8=|G| so h=1, and the engine-computed Ext tower [1, 1, 1, 1, 1, 1, 1] matches the predicted [1,1,1,1,1,1,1] in every degree n=0..6 (dim H^n(Z/2;F_2)=1 for all n). The diagonal control A=B=<x,y> gives h=2 and A∩B=(Z/2)^2 with dim H^n=n+1, engine [2, 4, 6, 8, 10, 12, 14] = 2·[1,2,3,4,5,6,7]; the rank-1 transverse control A=<x>,B=<z> gives A∩B={e}, h=2, engine [2, 0, 0, 0, 0, 0, 0]=[2,0,0,0,0,0,0]. The two V_4 self-tests reproduce the earlier V_4 engine. All cases agree with the abelian collapse formula (all_agree=True). This is a COMPUTED cross-check, not a new proof.
