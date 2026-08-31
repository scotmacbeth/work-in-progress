
## 2026-08-25(+) PROVE candidate — linear attention = one ◁-composition in the Vec-matrix bicategory
Prompted by Neil's Q1 ("should we commit to a vector space of PROMPTS?") + his ML-weights remark.
- Observation: superposing prompts = attention (query is a vector, softmax over keys = superposition
  of prompt-addresses). Full linearization of prompts = move from Fam(Vec^op) to the Vec-matrix /
  enriched (algebroid) layer, where prompt-vertices can be linearly combined.
- CLAIM to test: a single *linear*-attention layer (output_i = Σ_j (q_i·k_j) v_j) is exactly one
  ◁-composition of Vec-matrices in the bicategory whose composition is (P◁Q)(a,c)=⊕_b P(a,b)⊗Q(b,c)
  = profunctor composition (coend → finite ⊕_b for discrete index). Tokens = prompt-states a,b,c;
  the learned key/query/value coupling = the matrix entries P(a,b).
- Grant payoff: gives the Vec-container framing a REAL, checkable ML instance (Neil's #1 priority =
  "find a USE"), and it's the honest test of whether the container framing UNIFIES/SHARPENS Vertechi
  (parametric spans) rather than merely restating.
- Status: HOLD until (a) pi13 read settles ZS attribution, (b) Neil reacts to the plain note. Softmax
  is the non-linearity — be honest the clean statement is for LINEAR attention; softmax attention is
  provably non-functorial (Sargsyan 2603.16123), which is itself the interesting boundary.
