#!/bin/bash

# podigni CUDU 11.2
module load cuda/11-2

# aktiviraj condu
source /apps/miniforge3/bin/activate

# stvori virtualno okruženje za rapids
conda create --prefix venv-nbody \
    -c nvidia -c conda-forge  \
    python=3.8 \
    matplotlib \
    numpy \
    numba
