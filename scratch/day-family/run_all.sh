#!/bin/bash
# Reproduce every check.  Any FAIL string in the output is a real failure.
cd /home/agent/projects/scratch/day-family
for f in task1_convolution.py task2_spivak_monoidal.py task2e_negative_control.py \
         task3_kappa.py task4_pointwise.py task5_dirtoseq.py; do
  echo "### $f"
  python3 "$f" || echo "### $f CRASHED"
done
